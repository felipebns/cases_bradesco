from services.config import OPENAI_KEY
from openai import OpenAI
import json

class LLM_Wrapper:
    def __init__(self, model: str = "gpt-5-mini") -> None:
        self.url = OPENAI_KEY
        self.client = OpenAI(api_key=OPENAI_KEY)
        self.model = model

    def process(self, current_period_data: json, past_period_data: json):
        response = self.client.responses.create(
            model=self.model,
            input="bom dia",
        )
        print(response.output_text)

    def create_summary(self) -> None:
        pass