from log_schemas import BaseAgentProperty


def get_sys_prompt(agent_property: BaseAgentProperty, additional_sys_inst=""):
    return agent_property.get_sys_prompt() + additional_sys_inst

