# class to be able to generate data using openai
from openai import OpenAI
from openai.types.chat import ChatCompletion

class Gpt:
    """Gpt class to allow access to gpt endpoints"""
    def __init__(self, api_key: str, temperature: float = 0.7, model: str = "gpt-4o-mini", system_prompt: str = ""):
        self.client = self._create_client(api_key)
        self.model = model
        self.system_prompt = system_prompt
        self.temperature = temperature


    def _create_client(self, api_key: str) -> OpenAI:
        """Create gpt client from api key"""
        return OpenAI(api_key=api_key)

    @property
    def model(self) -> str:
        return self._model
    
    @property
    def temperature(self) -> int:
        return self._temperature
    
    @property
    def system_prompt(self) -> str:
        return self._system_prompt
    

    @model.setter
    def model(self, value: str):
        if not isinstance(value, str):
            raise ValueError(f"Gpt model must be a string, got: {type(value)}")
        if value not in [model.id for model in self.client.models.list()]:
            raise ValueError(f"model variable: {value} not an available model.")
        self._model = value
    
    @temperature.setter
    def temperature(self, value: float):
        if not isinstance(value, float):
            raise ValueError(f"Gpt temperature must be of type float, not of type: {type(value)}")
        if value < 0:
            raise ValueError(f"Gpt temperature must be greater than 0, not: {value}")
        self._temperature = value
    
    @system_prompt.setter
    def system_prompt(self, value: str):
        if not isinstance(value, str):
            raise ValueError(f"The system prompt must be of type str, not of type: {type(value)}")
        self._system_prompt = value

    # main class function
    def run(self, prompt: str) -> ChatCompletion:
        """A function to return a open ai response object via a given prompt"""
        return self.client.chat.completions.create(
            model = self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature
            )