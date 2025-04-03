from pydantic import BaseModel
from abc import ABC, abstractmethod
# from .. import Agent
from typing import List, Tuple, Any, Dict

from vllm_wrapper import BatchedLLM, SamplingParams

from sosimpy.config import get_sys_prompt
from sosimpy.simulation.conversation.conversation_memory import ConversationMemory

# class Conversation(BaseModel, ABC):
#     conversation_agent_lst: List[Agent]
#     conversation_history: str
#
#     @abstractmethod
#     def talk(self):
#         raise NotImplementedError("You need to implement talk method for your custom conversation")


def generate_conversation(llm: BatchedLLM, sampling_params: SamplingParams, all_pairs, all_questions, agent_properties_lst,
                          memory: ConversationMemory) -> Tuple[List[str], List[str]]:
    """
    Generate conversation responses by fetching and updating conversation memory.
    For each conversation pair, we record the conversation topic and question, then
    build a prompt as a list of dicts by:
      1. Fetching the conversation history,
      2. Transforming messages to a first-person perspective (using _third_person_msgs_to_first_person_msgs),
      3. Prepending a system message (using get_sys_prompt according to the agent property).
    Finally, responses from the llm are recorded back in memory.
    """
    initial_prompts = []
    # Build initial prompts for the first agent's response
    for idx, pair in enumerate(all_pairs):
        question = all_questions[idx]
        # Record the conversation topic and the question from agent pair[0]
        memory.record_conversation(pair, [{"conversation_topic": question}])

        # Fetch the conversation history and transform it for agent pair[0]
        conv_history = memory.fetch_conversation(pair[0]) # all the conversation history for the first agent
        transformed_history = _third_person_msgs_to_first_person_msgs(conv_history, pair[0])
        # Prepend system message
        sys_msg = {"role": "system",
                   "content": get_sys_prompt(agent_properties_lst[pair[0]])}
        prompt_messages = [sys_msg] + transformed_history

        initial_prompts.append(prompt_messages)

    # Generate responses for the first agent
    responses: List[str] = [r.outputs[0].text for r in llm.generate(initial_prompts, sampling_params)]

    # Record first agent responses in memory
    for idx, pair in enumerate(all_pairs):
        memory.record_conversation(pair, [{str(pair[0]): responses[idx]}])

    # Build prompts for the second agent's replies
    reply_prompts = []
    for idx, pair in enumerate(all_pairs):
        conv_history = memory.fetch_conversation(pair[1]) # All the conversation history from the second agent
        transformed_history = _third_person_msgs_to_first_person_msgs(conv_history, pair[1])
        sys_msg = {"role": "system",
                   "content": get_sys_prompt(agent_properties_lst[pair[1]])}
        prompt_messages = [sys_msg] + transformed_history
        reply_prompts.append(prompt_messages)

    # Generate responses for the second agent
    final_responses: List[str] = [r.outputs[0].text for r in llm.generate(reply_prompts, sampling_params)]

    # Record second agent responses in memory
    for idx, pair in enumerate(all_pairs):
        memory.record_conversation(pair, [{str(pair[1]): final_responses[idx]}])
    # conversation_histories = []
    # for idx, pair in enumerate(all_pairs):
    #     conversation_histories.append(memory.fetch_conversation(pair))
    return responses, final_responses



def _third_person_msgs_to_first_person_msgs(messages: List[Dict], self_agent_id: int) -> List[Dict]:
    """
    Given a list of messages (each having a key "agent_id"),
    replace the agent_id value with "usr" if it matches the provided agent_id,
    or with "ai" otherwise.

    Args:
        messages (List[Dict]): A list of messages, where each message looks like:
                               {"agent_id"<some int>: content, ...}
        self_agent_id (int): The ID of the "user" (or main speaker) to be labeled as "usr".

    Returns:
        List[Dict]: A new list of messages with "agent_id" replaced by "usr" or "ai".
    """
    transformed = []
    for msg in messages:
        # Make a shallow copy so we don't modify the original message in-place
        for agent_id, content in msg.items():
            if str(agent_id) == "system": # Don't think this would ever be possible
                raise f"Something is wrong over here"
            if str(agent_id) == str(self_agent_id):
                transformed.append({"role": "assistant", "content": content})
            else:
                transformed.append({"role": "user", "content": content})

    return transformed



if __name__ == '__main__':
    # Create LLM backbone
    MODEL = "meta-llama/Llama-3.1-8B-Instruct"
    SENARIO = "different demographics political debate"
    llm = BatchedLLM(model=MODEL, max_model_len=8000, enable_prefix_caching=True)
    sampling_params = SamplingParams(temperature=0, top_p=0.9, max_tokens=256)

    # Create conversation memory
    memory = ConversationMemory()

    from log_schemas import BaseAgentProperty
    import torch
    comb_generator = BaseAgentProperty.random_agent_generator()
    agents_loc = torch.rand(4, 2)
    agent_properties_lst = [next(comb_generator) for _ in range(4)]

    # Define two example conversation pairs and their topics
    all_pairs = [(0, 1), (2, 3)]
    all_questions = [
        "What are your thoughts on increasing taxes for the wealthy?",
        "Should the government provide free college education?"
    ]

    # Call generate_conversation function
    generate_conversation(llm, sampling_params, all_pairs, all_questions, agent_properties_lst, memory)
    # Have a second round of conversation
    responses, final_responses = generate_conversation(llm, sampling_params, all_pairs, all_questions, agent_properties_lst, memory)

    # Print out the prompts used and responses generated
    print("\n=== Example Conversations ===")

    for idx, (pair, question, response, final_response) in enumerate(zip(all_pairs, all_questions, responses, final_responses)):
        print(f"\n--- Conversation {idx + 1} ---")
        print(f"Agent {pair[0]} (User): {question}")
        print(f"Agent {pair[0]} (Response): {response}")
        print(f"Agent {pair[1]} (Reply): {final_response}")

    print("\n=== Conversation Memory ===")
    for pair in all_pairs:
        print(f"\nConversation between Agent {pair[0]} and Agent {pair[1]}:")
        print(memory.fetch_conversation(pair))
