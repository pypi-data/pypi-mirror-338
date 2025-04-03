from typing import Union, List, Dict

from transformers import AutoTokenizer
from vllm import LLM, SamplingParams
from functools import partial
from dotenv import load_dotenv

load_dotenv()

class BatchedLLM(LLM):
    """
    A subclass of vllm.LLM that overwrites the `generate` method
    to process multiple prompts in smaller batches.

    New Features:
      - Keeps track of the model type from the `model` keyword argument.
      - Can accept a list of prompts. Each prompt can be:
          (a) A string,
          (b) A list of message dictionaries representing conversation history.
             Each dict should have keys "role" and "content". For backward compatibility,
             dicts with keys "system", "usr", or "ai" are also supported.
        In either case, an empty assistant message is appended (with `eot=False`)
        to prompt the assistant's response.
    """

    def __init__(self, *args, batch_size=8, **kwargs):
        """
        Args:
            batch_size (int): Maximum number of prompts to process at once.
            *args: Passed through to the base LLM class.
            **kwargs: Passed through to the base LLM class (including model=...).
        """

        self.testing = kwargs.get("testing", False)
        # Keep track of the model type
        assert "model" in kwargs, "You have to provide a model, and the args name must be `model`"
        self.model_type = kwargs.get("model", "") or ""

        self.batch_size = batch_size

        if not self.testing:
            super().__init__(*args, **kwargs)


    def generate(
        self,
        prompts: Union[str, List[Union[str, List[Dict]]]],
        sampling_params: SamplingParams,
        testing: bool = False
    ):
        """
        Overwrites the default `generate` method to handle lists of prompts in batches.

        Args:
            prompts (str or List[str] or List[List[Dict]]):
                - If a string, it is treated as a single prompt.
                - If a list of strings, each element is a separate prompt.
                - If a list of lists of dicts, each sub-list is conversation history.
                  Each dict should have **ONLY** keys "role" and "content" (or the legacy keys).
                  Example (new format):
                  ```
                  [
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": "Who won the world cup in 2018?"},
                    {"role": "assistant", "content": "France won the 2018 FIFA World Cup."},
                    {"role": "user", "content": "Who was the top scorer?"}
                  ]
                  ```
            sampling_params (SamplingParams): Sampling parameters.
            testing (bool): If True, will return a mock response without calling the model.

        Returns:
            str or List[str]: A single generated response (if `prompts` was a single string)
                              or a list of generated responses.
        """
        # 1) If it's a single string, just call the parent directly or return mock if testing
        if isinstance(prompts, str):
            if testing:
                return "[TEST_RESPONSE]"
            return super().generate(prompts, sampling_params, use_tqdm=False)

        # 2) Otherwise, handle a list of prompts (strings or conversation lists).
        # Convert each prompt to a single string if needed.
        transformed_prompts = []
        if isinstance(prompts, list):
            if all(isinstance(prompt, list) and all(isinstance(m, dict) for m in prompt) for prompt in prompts):
                transformed_prompts = self.get_tokenizer().apply_chat_template(
                    prompts, tokenize=False, add_generation_prompt=True
                )
            else:
                for prompt in prompts:
                    assert isinstance(prompt, str), "Each prompt must be a raw string or a dict"
                    transformed_prompts.append(prompt)
        else:
            raise ValueError("Each prompt must be either a string or a list of dicts or list of str.")

        # If testing mode is on, skip real generation
        if testing:
            print(f"messages to prompts:\n{transformed_prompts}\n\n")
            return ["[TEST_RESPONSE]" for _ in transformed_prompts]

        # 3) Process in batches using the parent class's generate method
        all_responses = []
        total_prompts = len(transformed_prompts)
        for i in range(0, total_prompts, self.batch_size):
            batch_prompts = transformed_prompts[i : i + self.batch_size]
            batch_responses = super().generate(batch_prompts, sampling_params, use_tqdm=False)
            all_responses.extend(batch_responses)

        return all_responses


if __name__ == '__main__':
    # Example model initialization
    model = "meta-llama/Llama-3.1-8B-Instruct"
    model = "Qwen/Qwen2.5-7B-Instruct"
    llm = BatchedLLM(model=model, batch_size=2)

    # Define sampling parameters (example)
    sampling_params = SamplingParams(
        temperature=0, top_p=0.9, max_tokens=200
    )

    # Example 1: Single string prompt
    single_prompt = "What is the capital of France?"

    # Example 2: List of string prompts
    multiple_prompts = [
        "Who discovered gravity?",
        "What is the speed of light?"
    ]

    # Example 3: Conversation history as List[List[Dict]]
    # Using the new format with "role" and "content"
    conversation_prompt = [
        [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": "Who won the world cup in 2018?"},
            {"role": "assistant", "content": "France won the 2018 FIFA World Cup."},
            {"role": "user", "content": "Who was the top scorer?"}
        ],
        [
            {"role": "system", "content": "You are an AI specialized in history."},
            {"role": "user", "content": "Tell me about the American Revolution."},
            {"role": "assistant", "content": "The American Revolution was fought between 1775 and 1783."},
            {"role": "user", "content": "Who was the first President of the United States?"}
        ]
    ]

    # Running the model in testing mode (to simulate without actual API calls)
    print("\n=== Single Prompt Test ===")
    print(llm.generate(single_prompt, sampling_params, testing=True))

    print("\n=== Multiple Prompts Test ===")
    print(llm.generate(multiple_prompts, sampling_params, testing=True))

    print("\n=== Conversation History Test ===")
    print(llm.generate(conversation_prompt, sampling_params, testing=True))

