# class to be able to generate data using openai
from gpt import Gpt
import pandas as pd


class DataGenerator:
    def __init__(self, gpt: Gpt):
        self.gpt = gpt
        self._generation_results = []

    @property
    def generation_results(self) -> list:
        return self._generation_results.copy()

    @property
    def df_generation_results(self) -> pd.DataFrame:
        return pd.DataFrame.from_records(self.generation_results)

    def single_generation(self, prompt: str, target: str = "", system_prompt: str = ""):
        if system_prompt:
            self.gpt.system_prompt = system_prompt

        response = self.gpt.run(prompt)

        self._generation_results.append({
            "GPT prompt": prompt,
            "Result": response.choices[0].message.content,
            "Target (optional)": target,
        })

    def bulk_generation(self, prompts: list[str], targets: list[str] = None, system_prompts: list[str] = None):
        if not isinstance(prompts, list) or not all(isinstance(p, str) for p in prompts):
            raise ValueError("prompts must be a list of strings.")
        if targets and len(targets) != len(prompts):
            raise ValueError("targets must match length of prompts.")
        if system_prompts and len(system_prompts) != len(prompts):
            raise ValueError("system_prompts must match length of prompts.")

        for i, prompt in enumerate(prompts):
            target = targets[i] if targets else ""
            sys_prompt = system_prompts[i] if system_prompts else self.gpt.system_prompt
            self.single_generation(prompt=prompt, target=target, system_prompt=sys_prompt)

        return self.df_generation_results

if '__main__' == __name__:
    api_key = "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"
    gpt = Gpt(api_key=api_key, temperature=0.7, model="gpt-4o-mini", system_prompt="You're a helpful assistant.")
    data_gen = DataGenerator(gpt=gpt)
    data_gen.single_generation(prompt="return me 10 random words")

    print(data_gen.df_generation_results)






    

