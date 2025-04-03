from dataclasses import dataclass
import random
from typing import List, Literal, Generator, Tuple, Union
from itertools import product

from vllm import SamplingParams

from sosimpy.simulation.agents.agentProperty import *

@dataclass
class SimulationParameters:
    num_agents: int
    step_sz: float
    num_iterations: int
    topk: int
    model: str
    sampling_params: SamplingParams
    scenario: str
    starter_questions: List[str]
    judge_prompt: str
    system_instructions: List[str]  # All the possible system prompts


@dataclass
class SimulationInitConditions:
    agent_static_properties_lst: List[BaseAgentProperty]
    questionnaire_questions: List[str]



@dataclass
class AgentLog:
    agent_id: int
    iter_idx: int
    location: (int, int)
    questionnaire_responses: List[Union[str,int]]
    latent_attributes: List[Union[float, int]]
    agent_history: str


@dataclass
class ConversationLog:
    id: str
    conv_pair: (int, int)
    iteration_idx: int
    question: str
    reply: str
    final_response: str
    agreement_score: Literal[-1, 0, 1]


@dataclass
class MetricLog:
    iteration_idx: int
    metric_name: List[str]
    metric_scores: List[float]


# 1,16,male,New York,Urban,White,Not High School,Llama3.2-2b
if __name__ == '__main__':
    # comb_generator = BaseAgentProperty.random_combination_gen()
    # all_combinations = [next(comb_generator) for i in range(2)]
    # print(all_combinations)
    # all_system_prompts = CasualAndPoliticalStanceAP.generate_prompts_from_all_combinations()
    # print(all_system_prompts[:2])
    AgentLog(agent_id=1,
             iter_idx=1,
             location=(0.1, 0.1),
             questionnaire_responses=['0', '1', '0'],
             latent_attributes=[1,2,3],
             agent_history="",
             unused_param=True)