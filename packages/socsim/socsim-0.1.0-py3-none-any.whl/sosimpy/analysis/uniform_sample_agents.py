import json
import os
import datetime
from typing import List, Tuple, Union

import time
import uuid

import pandas as pd
import torch
import random
import argparse

from SocSim.log_schemas import SimulationParameters, AgentLog, ConversationLog, MetricLog
from SocSim.assign_pairs import assign_pairs1

from SocSim.conversation import generate_conversation, _third_person_msgs_to_first_person_msgs
from SocSim.conversation_memory import ConversationMemory
from SocSim.generate_questionnaire_answer import generate_questionnaire_answer, \
    questionnaire_answering_prompt_constructor, parse_binary_strings

from SocSim.property_updates import update_properties
from SocSim.starter_prompts import starter_prompts
from SocSim.analysis.generate_vizualizaiton import generate_visualization_for_subdir

from dotenv import load_dotenv
import numpy as np

from vllm import SamplingParams
from SocSim.vllm_wrapper import BatchedLLM

from SocSim.log_schemas import CasualAndPoliticalStanceAP
from SocSim.questionnaire_questions import questionnaire_questions, OPENNESS_INCIDIES

from SocSim.database_manager import SimLogger

QUESTIONNAIRE_QUESTIONs = questionnaire_questions
QUESTIONNAIRE_MASK = OPENNESS_INCIDIES

ice_cream_questions = "What is your favorite ice cream flavor? "
political_question = "Do you believe the federal government should play an active role in reducing economic inequality, even if it requires raising taxes on higher earners and expanding social welfare programs? "
topics = [ice_cream_questions, political_question]

def main():
    MODEL = "meta-llama/Llama-3.1-8B-Instruct"
    # MODEL = "Qwen/Qwen2.5-7B-Instruct"
    SENARIO = "different demographics political debate"
    # llm = BatchedLLM(model=MODEL, max_model_len=8000, enable_prefix_caching=True, tensor_parallel_size=2)
    llm = BatchedLLM(model=MODEL, max_model_len=8000, enable_prefix_caching=True)
    sampling_params = SamplingParams(temperature=0, max_tokens=256, )

    # Get all combinations
    all_sys_prompts = CasualAndPoliticalStanceAP.generate_prompts_from_all_combinations()  #
    all_comb = CasualAndPoliticalStanceAP.all_combinations()
    AP_lst = CasualAndPoliticalStanceAP.generate_all_agents()
    assert len(all_comb)==len(AP_lst)
    all_prompts = []
    empty_memory = ConversationMemory()

    # Set up questionnaire prompts.
    for topic in topics:
        for AP in AP_lst:
            all_prompts.append(questionnaire_answering_prompt_constructor(AP, {"conversation_topic": topic}, QUESTIONNAIRE_QUESTIONs, 0, empty_memory))

    all_data = []
    # Get the response
    responses: List[str] = [r.outputs[0].text for r in llm.generate(all_prompts, sampling_params)]
    parsed_responses: List[List[int]] = parse_binary_strings(responses, len(QUESTIONNAIRE_QUESTIONs))
    i = 0
    for topic in topics:
        for combo in all_comb:
            age, gender, location, urbanicity, ethnicity, education, ice_cream, stance = combo
            # Store all relevant info
            row_dict = {
                'age': age,
                'gender': gender,
                'location': location,
                'urbanicity': urbanicity,
                'ethnicity': ethnicity,
                'education': education,
                'favorite_ice_cream_flavor': ice_cream,
                'political_stance': stance,
                "topic": topic,
                'prompt': json.dumps(all_prompts[i]),
                'response': json.dumps(parsed_responses[i]),
                'openness_score': sum(parsed_responses[i]),
            }
            all_data.append(row_dict)
            i+=1


    # log the opennes score
    df = pd.DataFrame(all_data)
    import sqlite3

    conn = sqlite3.connect('analysis/agent_responses.db')
    df.to_sql('responses', conn, if_exists='replace', index=False)
    conn.close()

    # record that in a file
    #
