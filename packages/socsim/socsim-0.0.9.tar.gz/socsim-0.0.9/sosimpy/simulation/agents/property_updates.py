import os.path
from typing import List




def update_properties(llm, sampling_params, final_response, all_questions, all_replies, all_pairs, agent_properties_lst,
                      agents_loc, step_sz, cur_agreements):
    grade = llm_judge(llm, sampling_params, final_response, all_questions, all_replies)

    # Update the current positions of the agents
    for idx, g in enumerate(grade):
        idx_0 = all_pairs[idx][0]
        idx_1 = all_pairs[idx][1]

        try:
            g_val = int(g)
            cur_agreements.append(g_val)
        except:
            print("non-integer judge output")
            # Very rarely happens, but assume average agreement if reward not shown
            cur_agreements.append(0)
            continue

        loc_1 = agents_loc[idx_0]
        loc_2 = agents_loc[idx_1]
        diff_vec = loc_1 - loc_2

        # Don't move if g_val == 0
        if g_val == -1:
            # Move Apart by step_sz
            agents_loc[idx_1] -= diff_vec * step_sz
            agents_loc[idx_0] += diff_vec * step_sz
        elif g_val == 1:
            # Move Closer by step_sz
            agents_loc[idx_1] += diff_vec * step_sz
            agents_loc[idx_0] -= diff_vec * step_sz

    # Adjust for agents that have went off the grid [0, 1] x [0, 1]
    agents_loc[agents_loc > 1] = 1
    agents_loc[agents_loc < 0] = 0

    return agents_loc


import os.path
from typing import List

def llm_judge(llm, sampling_params, final_response: List[str], all_questions, all_replies) -> List[str]:
    # Judge the agreement between the two agents
    all_judge_prompts = []
    all_final_replies = []
    for idx, f_response in enumerate(final_response):
        question = all_questions[idx]
        reply_text = all_replies[idx]
        final_reply = f_response
        all_final_replies.append(final_reply)
        all_judge_prompts.append(construct_judge_prompt(question, reply_text, final_reply))

    grade = [r.outputs[0].text for r in llm.generate(all_judge_prompts, sampling_params)]

    with open("./grade_log.txt", "w") as f:
        # just log a few judge prompts
        if os.path.getsize("./grade_log.txt") < 4096:
            f.write(f"grade is {grade} for the conversation: \n"
                    f"{all_judge_prompts}\n\n\n")
    return grade


def construct_judge_prompt(question, reply, final_reply):
    # System message with judging criteria
    llm_judge_sys = "Given an initial question and response from two political agents, score how much the agents agree with one another with values of -1, 0, or 1, where 1 means they agree and -1 means they disagree. Respond with an integer number only. Your response should contain no words, only a number, please."

    # Example interactions for context
    user_example = "Question: Are taxes too high?\n"
    user_example += "Agent 1: I believe that the wealthy should pay a fair share of taxes to support essential public services like universal healthcare, education, and infrastructure, which benefit everyone, not just the top 1%. The current tax code is often more beneficial to corporations and the ultra-wealthy than to the middle and lower classes, and it's time for a more progressive tax system.\n"
    user_example += "Agent 2: I think the tax burden is too high for individuals and businesses, and we need to simplify the tax code and reduce the number of tax brackets, so people can keep more of their hard-earned money and invest in their communities."

    user_example2 = "Question: What is your solution to the deficit?\n"
    user_example2 += "Agent 1: Cutting the welfare state.\n"
    user_example2 += "Agent 2: I agree, cutting the welfare state will decrease the deficit."

    # Construct the actual user input
    user_prompt = f"Question: {question}\nAgent 1: {reply}\nAgent 2: {final_reply}"

    # Returning the prompt as a structured list of dictionaries
    return [
        {"role": "system", "content": llm_judge_sys},
        {"role": "user", "content": user_example},
        {"role": "assistant", "content": "-1"}, # disagree example
        {"role": "user", "content": user_example2},
        {"role": "assistant", "content": "1"}, # agree example
        {"role": "user", "content": user_prompt}
    ]

"""
The question given was:
Are taxes too high?

the response was: 


the reply was: 
Absolutely, taxes can feel pretty high, especially when you're trying to make ends meet. I think we need to make sure the money is being spent wisely on things that really matter, like education and infrastructure, but we shouldn't overburden people who are already working hard to get by.
their agreement score is 1
"""

if __name__ == '__main__':
    from vllm import SamplingParams
    from vllm_wrapper import BatchedLLM
    MODEL = "meta-llama/Llama-3.1-8B-Instruct"

    llm = BatchedLLM(model=MODEL, max_model_len=8000, enable_prefix_caching=True)
    sampling_params = SamplingParams(temperature=0.7, top_p=0.9, max_tokens=256, )
    final_response = ["Absolutely, taxes can feel pretty high, especially when you're trying to make ends meet. I think we need to make sure the money is being spent wisely on things that really matter, like education and infrastructure, but we shouldn't overburden people who are already working hard to get by."]
    all_questions = ["Are taxes too high? "]
    all_replies = ["Taxes can definitely feel high, especially when you're trying to support a family and make ends meet. I think it's important to find a balance that funds essential services without placing an undue burden on taxpayers."]

    print(llm_judge(llm, sampling_params, final_response, all_questions, all_replies))