import random
import json
from typing import List, TypedDict, Dict, Union, Tuple
from agent_prompting import get_sys_prompt

from log_schemas import BaseAgentProperty
from conversation_memory import ConversationMemory


class ConversationSchema(TypedDict):
    conversation_topic: str
    primary_agent_response: str
    second_agent_response: str


def questionnaire_answering_prompt_constructor(agent_property: BaseAgentProperty,
                                               previous_conversations: ConversationSchema,
                                               questionnaire_question_lst: List[str],
                                               agent_id: int,
                                               memory: ConversationMemory):
    # sys_inst = get_sys_prompt(agent_property) # political debate case
    sys_inst = get_sys_prompt(agent_property, additional_sys_inst="Additionally, answer any questionnaires provided. ")  # political debate case
    conversation_topic = previous_conversations['conversation_topic']

    conversation_history = json.dumps(memory.fetch_conversation(agent_id))
    def format_questionnaire():
        formatted_questions = "\n".join(
            f"{idx + 1}. {question.strip()}" for idx, question in enumerate(questionnaire_question_lst))
        return formatted_questions

    example_response = [random.randint(0, 1) for _ in range(len(questionnaire_question_lst))]
    prompt = [{"role": "system",
              "content": (
                    f"{sys_inst}\n"
                    f"You are agent {agent_id}"
                    f"You are discussing the topic '{conversation_topic}'.\n"
                    "Below is the interaction between you and another agent.\n\n"
                    "Answer the questionnaire based on your political stance and the conversation.\n"
                    "Your response **must** follow these strict rules:\n"
                    "1. Output **only** a Python-style list of binary integers (`0` or `1`). No other text.\n"
                    "2. The list **must** have the same length and order as the questionnaire items.\n"
                    "3. Do **not** include explanations, disclaimers, formatting, or any additional characters.\n"
                    "4. The response should be **only** the list, with no quotation marks or additional syntax.\n"
                    f"5. The format **must** match this example exactly: {example_response}\n\n"
                    "=== Conversation History ===\n"
                    f"{conversation_history}"
                    "\n=== End of Conversation History ===\n\n"
                    "<|eot_id|><|start_header_id|>user<|end_header_id|>\n"
                    f"{format_questionnaire()}\n\n"
                    "Please respond with your answers as a single list of binary integers.\n"
                    f"Example response: {example_response}\n"
                        )
              }]

    return prompt


from typing import List, Tuple, Union


def chunk_list(lst, n):
    """
    Yields successive n-sized chunks from lst.
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def generate_questionnaire_answer(llm,
                                  sampling_params,
                                  all_pairs,
                                  agent_properties_lst,
                                  all_questions,
                                  all_replies,
                                  final_responses,
                                  questionnaire_question_lst: List[str],
                                  memory: ConversationMemory,
                                  mask: List[int]
                                  ) -> Tuple[List[List[int]], List[List[Union[int, float]]]]:
    # Prepare an answer container: one list of binary answers per agent
    agent_questionnaire_answers: List[Union[List[int], None]] = [None for _ in range(len(agent_properties_lst))]

    # We will also keep track of the complete answers for *all* prompts,
    # so we can feed them into `questionnaire_res_to_latent_score`.
    # This will have 2 entries per conversation: (primary answers, secondary answers).
    all_answer_rows: List[List[int]] = []

    for i, (pair, q, r, final_r) in enumerate(zip(all_pairs, all_questions, all_replies, final_responses)):
        primary_agent_id, second_agent_id = pair

        # Create the conversation schema
        previous_conversations: ConversationSchema = {
            'conversation_topic': q,
            'primary_agent_response': r,
            'second_agent_response': final_r
        }

        # We'll accumulate partial answers from each chunk to form full answers
        # covering all questions for this conversation.
        primary_full_answers = []
        secondary_full_answers = []

        # Split the questionnaire_question_lst into smaller sub-lists of size <= 10
        for question_chunk in chunk_list(questionnaire_question_lst, 10):
            # Build the primary prompt
            primary_prompt = questionnaire_answering_prompt_constructor(
                agent_property=agent_properties_lst[i],
                previous_conversations=previous_conversations,
                questionnaire_question_lst=question_chunk,  # pass the chunk instead of full list
                agent_id=pair[0],
                memory=memory
            )
            # Build the secondary prompt
            secondary_prompt = questionnaire_answering_prompt_constructor(
                agent_property=agent_properties_lst[i],
                previous_conversations=previous_conversations,
                questionnaire_question_lst=question_chunk,  # pass the chunk instead of full list
                agent_id=pair[1],
                memory=memory
            )

            # Call the LLM on both prompts at once
            partial_responses = llm.generate([primary_prompt, secondary_prompt], sampling_params)

            # partial_responses is a list of length 2. Each element has .outputs[0].text
            # Parse the text for each chunk.
            primary_text = partial_responses[0].outputs[0].text.strip()
            secondary_text = partial_responses[1].outputs[0].text.strip()

            # parse_binary_strings takes a list of strings and returns a list of lists of int
            # Each string corresponds to one response. We have only 1 response per agent here,
            # so we'll parse them separately.
            parsed_primary = parse_binary_strings([primary_text], len(question_chunk))[0]
            parsed_secondary = parse_binary_strings([secondary_text], len(question_chunk))[0]

            # Extend the agent's answers with the partial chunk
            primary_full_answers.extend(parsed_primary)
            secondary_full_answers.extend(parsed_secondary)

        # We now have the *complete* answer arrays for the entire questionnaire_question_lst
        agent_questionnaire_answers[primary_agent_id] = primary_full_answers
        agent_questionnaire_answers[second_agent_id] = secondary_full_answers

        # Also store them in all_answer_rows so we can compute the latent factor across all agents
        all_answer_rows.append(primary_full_answers)
        all_answer_rows.append(secondary_full_answers)

    # Now that we have the full set of answers for all agents,
    # compute the latent factor using the entire list of answers.
    latent_factor = questionnaire_res_to_latent_score(all_answer_rows, mask)

    return agent_questionnaire_answers, latent_factor


def parse_binary_strings(binary_strings: List[str], list_len: int) -> List[List[int]]:
    allowed_chars = {'0', '1', '\n', '\t', ' ', '[', ']', ','}
    parsed_lists = []

    for i, binary_string in enumerate(binary_strings):
        try:
            # Check for invalid characters
            if any(char not in allowed_chars for char in binary_string):
                raise ValueError("Invalid character detected")

            # Extract only 0s and 1s
            parsed_list = [int(char) for char in binary_string if char in {'0', '1'}]

            # Validate the extracted list length
            if len(parsed_list) != list_len:
                raise ValueError("Incorrect number of binary values")

            parsed_lists.append(parsed_list)
        except Exception as e:
            print(f"Parsing error for: {binary_string}\nError: {e}")
            with open("./temp.txt", "a") as f:
                f.write(f"{str(e)} for agent {i}: \n{binary_string}\n")
            # If an error occurs, replace with a list of -1s of the expected length
            parsed_lists.append([-1] * list_len)

    return parsed_lists


def questionnaire_res_to_latent_score(responses: List[List[int]], mask: List[bool]) -> List[
    List[int]]:
    # Apply mask to the responses
    results = []
    for agent_response in responses:
        masked_response = [agent_response[i] for i in mask]
        results.append(masked_response)
    return results

if __name__ == '__main__':
    responses = [
        [5, 3, 2],
        [1, 4, 6],
        [7, 0, 5]
    ]
    mask = [1]  # Only first and third responses should be counted

    expected_output = [[3], [4], [0]]
    output = questionnaire_res_to_latent_score(responses, mask)
    print(output)
    assert output == expected_output
    print("Test case 1 passed!")
