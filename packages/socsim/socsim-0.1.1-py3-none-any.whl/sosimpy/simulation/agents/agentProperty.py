from pydantic import BaseModel
from abc import ABC, abstractmethod
from dataclasses import dataclass
import random
from typing import List, Literal, Generator, Tuple, Union
from itertools import product


@dataclass
class BaseAgentProperty:
    age: int
    gender: str
    location: str
    urbanicity: str
    ethnicity: str
    education: str

    # --------------------------------------------------------------------
    # State population data:
    # --------------------------------------------------------------------
    _STATES_DATA = [
        ("California", 39431263),
        ("Texas", 31290831),
        ("Florida", 23372215),
        ("New York", 19867248),
        ("Pennsylvania", 13078751),
        ("Illinois", 12710158),
        ("Ohio", 11883304),
        ("Georgia", 11180878),
        ("North Carolina", 11046024),
        ("Michigan", 10140459),
        ("New Jersey", 9500851),
        ("Virginia", 8811195),
        ("Washington", 7958180),
        ("Arizona", 7582384),
        ("Tennessee", 7227750),
        ("Massachusetts", 7136171),
        ("Indiana", 6924275),
        ("Missouri", 6263220),
        ("Maryland", 6245466),
        ("Wisconsin", 5960975),
        ("Colorado", 5957493),
        ("Minnesota", 5793151),
        ("South Carolina", 5478831),
        ("Alabama", 5157699),
        ("Louisiana", 4597740),
        ("Kentucky", 4588372),
        ("Oregon", 4272371),
        ("Oklahoma", 4095393),
        ("Connecticut", 3675069),
        ("Utah", 3503613),
        ("Iowa", 3267467),
        ("Nevada", 3241488),
        ("Arkansas", 3203295),
        ("Mississippi", 2970606),
        ("Kansas", 2943045),
        ("New Mexico", 2130256),
        ("Nebraska", 2005465),
        ("Idaho", 2001619),
        ("West Virginia", 1769979),
        ("Hawaii", 1446146),
        ("Maine", 1409032),
        ("New Hampshire", 1405012),
        ("Montana", 1137233),
        ("Rhode Island", 1112308),
        ("Delaware", 1051917),
        ("South Dakota", 924669),
        ("North Dakota", 796568),
        ("Alaska", 740133),
        ("Vermont", 702250),
        ("Wyoming", 648493),
    ]
    _TOTAL_POP = sum(pop for _, pop in _STATES_DATA)
    _LOCATION_VALUES = [state for (state, _) in _STATES_DATA]
    _LOCATION_WEIGHTS = []
    for _, pop in _STATES_DATA:
        _LOCATION_WEIGHTS.append(pop / _TOTAL_POP)

    # --------------------------------------------------------------------
    # The rest of the distribution data follows from the real-world info:
    # (approximate, bucketed for simplicity)
    # --------------------------------------------------------------------
    ATTRIBUTES = {
        "age": {
            "values": [16, 28, 40, 50, 65, 80],
            "weights": [0.16, 0.17, 0.16, 0.15, 0.16, 0.20]
        },
        "gender": {
            "values": ["male", "female"],
            "weights": [0.495, 0.505]
        },
        "ethnicity": {
            "values": ["White", "Hispanic", "Black", "Native American", "Asian"],
            "weights": [0.616, 0.187, 0.121, 0.010, 0.059]
            # adjusted from your notes: White (61.6%), Hispanic (18.7%), Black (12.1%),
            # Asian (5.9%), Native American (1.0%) => normalized to sum ~ 1.0
        },
        "urbanicity": {
            # Pew data: Urban (31%), Suburban (55%), Rural (14%)
            # We’ve carved out “Exurban” from Suburban for demonstration
            "values": ["Urban", "Suburban", "Exurban", "Rural"],
            "weights": [0.31, 0.50, 0.05, 0.14]
        },
        "education": {
            # Breaking out “Bachelor’s or higher” (33%) into College vs. Postgrad
            "values": [
                "Not High School",
                "High School",
                "Associate’s",
                "Some College",
                "College",
                "Postgraduate"
            ],
            "weights": [0.10, 0.29, 0.10, 0.18, 0.20, 0.13]
        },
        # Use the computed values/weights for states
        "location": {
            "values": _LOCATION_VALUES,
            "weights": _LOCATION_WEIGHTS
        },
    }

    SYSTEM_PROMPT_TEMPLATE = (
        "You are now adopting the persona of a {age}-year-old {gender} from {location}, "
        "a {urbanicity} area. You identify as {ethnicity}, and your highest level of formal "
        "education is {education}. "

    )
    SIMULATION_SENARIO_PROMPT = ("Whenever you respond to prompts or questions, you should "
                                 "maintain consistency with these background details and viewpoints, grounding your "
                                 "answers in the lived experience and perspective of this hypothetical individual."
                                 "You are going to engage in conversation with other politically minded individuals "
                                 "from the United States. Give your opinion on culture, economy, foreign affairs, "
                                 "and other political topics. Limit your response to 1-2 sentences.")
    USER_PROMPT = "Tell me about yourself."

    @classmethod
    def _random_choice(cls, attr_name: str):
        """
        Helper method that picks a random value from the named attribute spec.
        """
        spec = cls.ATTRIBUTES[attr_name]
        return random.choices(spec["values"], weights=spec["weights"], k=1)[0]

    @classmethod
    def random_combination_gen(cls) -> Generator[Tuple[int, str, str, str, str, str], None, None]:
        """
        Infinite generator that yields a random combination of
        (age, gender, location, urbanicity, ethnicity, education),
        approximating the real-world U.S. distributions (2020–2021).
        """
        while True:
            combo = (
                cls._random_choice("age"),
                cls._random_choice("gender"),
                cls._random_choice("location"),
                cls._random_choice("urbanicity"),
                cls._random_choice("ethnicity"),
                cls._random_choice("education")
            )
            yield combo

    @classmethod
    def get_sys_prompt_template(cls):
        return cls.SYSTEM_PROMPT_TEMPLATE + cls.SIMULATION_SENARIO_PROMPT

    @classmethod
    def random_agent_generator(cls) -> Generator["AgentProperty2", None, None]:
        """
        Infinite generator that yields a new AgentProperty2 object
        with randomly selected attributes each time it is called.
        """
        position_counter = 0  # To keep track of generated agents (optional)
        gen = cls.random_combination_gen()

        while True:
            # Get a new random combination
            age, gender, location, urbanicity, ethnicity, education = next(gen)

            # Create a new AgentProperty2 instance
            agent = cls(
                age=age,
                gender=gender,
                location=location,
                urbanicity=urbanicity,
                ethnicity=ethnicity,
                education=education,
            )

            position_counter += 1  # Increment position for uniqueness
            yield agent  # Yield the AgentProperty2 instance

    @classmethod
    def generate_all_agents(cls) -> list["BaseAgentProperty"]:
        """
        Generate and return a list of BaseAgentProperty objects,
        one for each possible attribute combination.
        """
        agents = []
        for combo in cls.all_combinations():
            age, gender, location, urbanicity, ethnicity, education = combo
            agent = cls(
                age=age,
                gender=gender,
                location=location,
                urbanicity=urbanicity,
                ethnicity=ethnicity,
                education=education
            )
            agents.append(agent)
        return agents

    def get_sys_prompt(self):
        return self.get_sys_prompt_template().format(
            age=self.age,
            gender=self.gender,
            location=self.location,
            urbanicity=self.urbanicity,
            ethnicity=self.ethnicity,
            education=self.education
        )

    @classmethod
    def all_combinations(cls) -> list[tuple[int, str, str, str, str, str]]:
        """
        Generate all possible combinations of the six attributes.
        Returns a list of tuples: (age, gender, location, urbanicity, ethnicity, education)
        """
        return list(product(
            cls.ATTRIBUTES["age"]["values"],
            cls.ATTRIBUTES["gender"]["values"],
            cls.ATTRIBUTES["location"]["values"],
            cls.ATTRIBUTES["urbanicity"]["values"],
            cls.ATTRIBUTES["ethnicity"]["values"],
            cls.ATTRIBUTES["education"]["values"],
        ))

    @classmethod
    def generate_prompts_from_all_combinations(cls) -> list[str]:
        """
        Applies the system prompt to all combinations of attributes.
        Returns a list of formatted system prompts.
        """
        prompts = []
        for combo in cls.all_combinations():
            age, gender, location, urbanicity, ethnicity, education = combo
            prompt = cls.get_sys_prompt_template().format(
                age=age,
                gender=gender,
                location=location,
                urbanicity=urbanicity,
                ethnicity=ethnicity,
                education=education
            )
            prompts.append(prompt)
        return prompts



@dataclass
class CasualAndPoliticalStanceAP(BaseAgentProperty):
    favorite_ice_cream_flavor: str
    political_stance: str

    # Extended attributes
    EXTRA_ATTRIBUTES = {
        "favorite_ice_cream_flavor": {
            "values": ["vanilla", "chocolate"],
            "weights": [0.5, 0.5]
        },
        "political_stance": {
            "values": ["Democrat", "Republican"],
            "weights": [0.5, 0.5]
        }
    }

    # Overriding the system prompt template
    SYSTEM_PROMPT_TEMPLATE = (
            BaseAgentProperty.SYSTEM_PROMPT_TEMPLATE +
            " You enjoy {favorite_ice_cream_flavor} ice cream and lean politically as a {political_stance}. "
    )

    @classmethod
    def _random_choice(cls, attr_name: str):
        if attr_name in cls.ATTRIBUTES:
            return super()._random_choice(attr_name)
        elif attr_name in cls.EXTRA_ATTRIBUTES:
            spec = cls.EXTRA_ATTRIBUTES[attr_name]
            return random.choices(spec["values"], weights=spec["weights"], k=1)[0]
        else:
            raise ValueError(f"Unknown attribute: {attr_name}")

    @classmethod
    def random_combination_gen(cls) -> Generator[Tuple[int, str, str, str, str, str, str, str], None, None]:
        while True:
            base_combo = tuple(super()._random_choice(attr) for attr in [
                "age", "gender", "location", "urbanicity", "ethnicity", "education"
            ])
            extra_combo = (
                cls._random_choice("favorite_ice_cream_flavor"),
                cls._random_choice("political_stance")
            )
            yield base_combo + extra_combo

    @classmethod
    def random_agent_generator(cls) -> Generator["CasualAndPoliticalStanceAP", None, None]:
        gen = cls.random_combination_gen()
        while True:
            age, gender, location, urbanicity, ethnicity, education, ice_cream, stance = next(gen)
            yield cls(
                age=age,
                gender=gender,
                location=location,
                urbanicity=urbanicity,
                ethnicity=ethnicity,
                education=education,
                favorite_ice_cream_flavor=ice_cream,
                political_stance=stance
            )

    @classmethod
    def generate_all_agents(cls) -> list["CasualAndPoliticalStanceAP"]:
        """
        Generate and return a list of CasualAndPoliticalStanceAP objects,
        one for each possible attribute combination (base + extra).
        """
        agents = []
        for combo in cls.all_combinations():
            (age, gender, location, urbanicity,
             ethnicity, education, ice_cream, stance) = combo

            agent = cls(
                age=age,
                gender=gender,
                location=location,
                urbanicity=urbanicity,
                ethnicity=ethnicity,
                education=education,
                favorite_ice_cream_flavor=ice_cream,
                political_stance=stance,
            )
            agents.append(agent)
        return agents

    def get_sys_prompt(self):
        return self.get_sys_prompt_template().format(
            age=self.age,
            gender=self.gender,
            location=self.location,
            urbanicity=self.urbanicity,
            ethnicity=self.ethnicity,
            education=self.education,
            favorite_ice_cream_flavor=self.favorite_ice_cream_flavor,
            political_stance=self.political_stance
        )

    from itertools import product

    @classmethod
    def all_combinations(cls) -> list[tuple[int, str, str, str, str, str, str, str]]:
        """
        Generate all possible combinations of base and extra attributes
        using itertools.product for efficiency.
        Returns a list of tuples:
        (age, gender, location, urbanicity, ethnicity, education,
         favorite_ice_cream_flavor, political_stance)
        """
        base_attrs = (
            cls.ATTRIBUTES["age"]["values"],
            cls.ATTRIBUTES["gender"]["values"],
            cls.ATTRIBUTES["location"]["values"],
            cls.ATTRIBUTES["urbanicity"]["values"],
            cls.ATTRIBUTES["ethnicity"]["values"],
            cls.ATTRIBUTES["education"]["values"],
        )
        extra_attrs = (
            cls.EXTRA_ATTRIBUTES["favorite_ice_cream_flavor"]["values"],
            cls.EXTRA_ATTRIBUTES["political_stance"]["values"],
        )

        return list(product(*base_attrs, *extra_attrs))

    @classmethod
    def generate_prompts_from_all_combinations(cls) -> list[str]:
        prompts = []
        base_combos = cls.all_combinations()
        for combo in base_combos:
            age, gender, location, urbanicity, ethnicity, education, ice_cream, stance = combo
            prompt = cls.get_sys_prompt_template().format(
                age=age,
                gender=gender,
                location=location,
                urbanicity=urbanicity,
                ethnicity=ethnicity,
                education=education,
                favorite_ice_cream_flavor=ice_cream,
                political_stance=stance
            )
            prompts.append(prompt)
        return prompts

