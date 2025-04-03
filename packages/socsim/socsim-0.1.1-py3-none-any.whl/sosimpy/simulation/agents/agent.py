import random
from typing import List, Tuple, Union, Optional, ClassVar, Generator
from pydantic import BaseModel, Field
from .agentProperty import BaseAgentProperty
from ..logging.database_manager import SimLogger

from dataclasses import dataclass
from itertools import product


class Agent(BaseModel):
    """
    A Pydantic model representing a single simulation agent.
    """
    agent_id: int
    iter_idx: int = 0
    location: Tuple[float, float] = (0.0, 0.0)
    questionnaire_responses: List[Union[str, int]] = Field(default_factory=list)
    latent_attributes: List[Union[float, int]] = Field(default_factory=list)
    agent_property: Optional["BaseAgentProperty"] = None

    # CLASS-LEVEL references for:
    #   1. Shared logger
    #   2. Shared generator for random properties
    logger: ClassVar[Optional["SimLogger"]] = None
    property_generator: ClassVar[Optional[Generator["BaseAgentProperty", None, None]]] = None

    # ----------------------------
    # CLASS METHODS
    # ----------------------------
    @classmethod
    def set_logger(cls, logger_obj: SimLogger) -> None:
        """Attach a shared SimLogger instance at the class level."""
        cls.logger = logger_obj

    @classmethod
    def set_property_generator(cls, gen: Generator[BaseAgentProperty, None, None]) -> None:
        """
        Set a shared property generator for all Agents.
        If not set, we default to BaseAgentProperty.random_agent_generator().
        """
        cls.property_generator = gen

    @classmethod
    def generate_random_agents(cls, count: int) -> List["Agent"]:
        """
        Generates 'count' new Agent objects, each pulling from a shared property
        generator (to preserve the original logic of a single generator that
        yields unique random property draws in sequence).
        """
        if cls.property_generator is None:
            # Default to a fresh generator from BaseAgentProperty
            cls.property_generator = BaseAgentProperty.random_agent_generator()

        agents = []
        for i in range(count):
            # Pull the next property from the shared generator
            prop = next(cls.property_generator)
            # Assign a random 2D location in [0.0,1.0)
            loc = (random.random(), random.random())

            agent = cls(
                agent_id=i,
                location=loc,
                agent_property=prop
            )
            agents.append(agent)

        return agents

    @classmethod
    def generate_agents_for_all_property_combinations(cls) -> List["Agent"]:
        """
        Generates one Agent for each possible combination of
        BaseAgentProperty attributes (age, gender, location, urbanicity, ethnicity, education).
        """
        all_props = BaseAgentProperty.generate_all_agents()
        agents = []

        for i, prop in enumerate(all_props):
            # location is random in [0,1]
            loc = (random.random(), random.random())
            agents.append(cls(
                agent_id=i,
                location=loc,
                agent_property=prop
            ))
        return agents

    # ----------------------------
    # LOGGING UTILITIES
    # ----------------------------
    @classmethod
    def log_all_agents(cls,
                       iter_idx: int,
                       agents: List["Agent"],
                       memory: Optional["ConversationMemory"] = None) -> None:
        """
        Class method that logs the state of a list of agents via the shared logger.
        Essentially replaces the old free-standing log_agents function.
        """
        if cls.logger is None:
            raise RuntimeError("Agent.logger is not set. Please call Agent.set_logger(...) first.")

        for agent in agents:
            agent.log_agent(iter_idx, memory=memory)

    def log_agent(self,
                  iter_idx: int,
                  memory: Optional["ConversationMemory"] = None) -> None:
        """
        Instance method that logs this agent's state via the shared logger.
        Called by log_all_agents.
        """
        if self.logger is None:
            raise RuntimeError("Agent.logger is not set. Please call Agent.set_logger(...) first.")

        # If you store conversation logs in memory, you can fetch them here:
        if memory is not None:
            # Example: memory may have a method fetch_conversation(agent_id)
            conv = memory.fetch_conversation(self.agent_id)
            # Potentially convert 3rd-person to 1st-person, or do something else
            conv_json = str(conv)  # or e.g. json.dumps(...)
        else:
            conv_json = ""

        # Insert into the database
        self.logger.insert_agent_log(
            agent_id=self.agent_id,
            iter_idx=iter_idx,
            location=self.location,
            questionnaire_responses=self.questionnaire_responses,
            latent_attributes=self.latent_attributes,
            agent_history=conv_json
        )

    # ----------------------------
    # INSTANCE UTILITIES
    # ----------------------------
    def update_location(self, new_location: Tuple[float, float]) -> None:
        """Convenience method to update the agent's location if needed."""
        self.location = new_location

    def get_full_system_prompt(self) -> str:
        """Returns the system prompt for this agent based on its property object."""
        if self.agent_property:
            return self.agent_property.get_sys_prompt()
        return "No agent property set."