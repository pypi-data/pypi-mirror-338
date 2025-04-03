
def log_simulation_setup(num_agents, step_sz, num_iterations, topk, model, sampling_params, scenario, starter_prompts,
                         output_dir):
    from property_updates import construct_judge_prompt
    judge_prompt = construct_judge_prompt("{question}", "{reply}", "{final_reply}")
    system_instruction = BaseAgentProperty.get_sys_prompt_template()
    s = SimulationParameters(num_agents, step_sz, num_iterations, topk, model, sampling_params, scenario,
                             starter_prompts,
                             judge_prompt, system_instruction)
    # Log to json file
    sim_params_dict = s.__dict__
    setup_log_path = os.path.join(output_dir, "simulation_setup.json")
    save_json(sim_params_dict, setup_log_path)


def log_simulation_init_conditions(questionnaire_questions, static_agent_properties_lst: List[BaseAgentProperty],
                                   output_dir):
    # TODO: Log static agent properties and other questionnaire questions. Worry about this later.
    # Log questionnaire questions
    setup_log_path = os.path.join(output_dir, "questionnaire_questions.txt")
    with open(setup_log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(questionnaire_questions))

    # Log static agent properties
    for agent_id, static_agent_property in enumerate(static_agent_properties_lst):
        logger.insert_agent_properties(agent_id=agent_id, age=static_agent_property.age,
                                       gender=static_agent_property.gender,
                                       location=static_agent_property.location,
                                       urbanicity=static_agent_property.urbanicity,
                                       ethnicity=static_agent_property.ethnicity,
                                       education=static_agent_property.education)
    return


def log_agents(iter_idx, agent_locs: List[Tuple[int, int]], questionnaire_r_lst: List[str], log_dir,
               latent_attributes: List[List[Union[int, float]]], memory: ConversationMemory = None):
    # Receives a list of agents, their properties (locations, boolean values)

    for agent_id, (location, questionnaire_r, latent_attribute) in enumerate(
            zip(agent_locs, questionnaire_r_lst, latent_attributes)):

        if memory is None:
            agent_history = ""
        else:
            # TODO json dumping is not at the correct place
            agent_history = json.dumps(
                _third_person_msgs_to_first_person_msgs(memory.fetch_conversation(agent_id), agent_id))

        AL = AgentLog(agent_id, iter_idx, location,
                      questionnaire_r, latent_attribute, json.dumps(agent_history))
        # database log
        logger.insert_agent_log(agent_id, iter_idx, location,
                                questionnaire_r, latent_attribute, agent_history)


def log_conversations(iter_idx, curr_pairs, curr_questions, curr_replies, final_responses: List[str], curr_agreements,
                      log_dir):
    # Log the list of pairs and questions
    # Log the replies and final responses
    for conv_pair, question, reply, final_response, agreement_score in zip(curr_pairs,
                                                                           curr_questions,
                                                                           curr_replies,
                                                                           final_responses,
                                                                           curr_agreements):
        conv_id = uuid.uuid4()
        CL = ConversationLog(id=str(conv_id), conv_pair=conv_pair, iteration_idx=iter_idx, question=question,
                             reply=reply, final_response=final_response, agreement_score=agreement_score)

        # database log
        logger.insert_conversation_log(CL.id, CL.conv_pair, CL.iteration_idx, CL.question, CL.reply,
                                       CL.final_response,
                                       CL.agreement_score,
                                       )


def log_metrics(iter_idx, metric_names, metrics, log_dir):
    # Log the metrics
    for metric_name, metric in zip(metric_names, metrics):
        ML = MetricLog(iter_idx, metric_name, metric)
        # print(f"At iteration {ML.iteration_idx}, the metric {ML.metric_name} was {ML.metric_scores}")
        logger.insert_metric_log(ML.iteration_idx, ML.metric_name, ML.metric_scores)


def log_final_round(all_pairs, all_questions, all_replies, final_responses, cur_agreements, log_dir,
                    agent_properties_lst):
    with open(os.path.join(log_dir, "sample_conversation.txt"), "w") as f:
        sample_conversation_s = ""
        for i in range(min(len(all_pairs), 5)):
            sample_conversation_s += f"""
The question given was:
{all_questions[i]}

the response was: 
{all_replies[i]}

the reply was: 
{final_responses[i]}
their agreement score is {cur_agreements[i]}


the agent properties if you are interested is: 
{agent_properties_lst[all_pairs[i][0]]}
{agent_properties_lst[all_pairs[i][1]]}
"""
        f.write(sample_conversation_s)
