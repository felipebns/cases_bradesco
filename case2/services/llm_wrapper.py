from services.config import OPENAI_KEY
from services.prompts import parse_input_prompt
from openai import OpenAI

class LLM_Wrapper:
    def __init__(self, model: str = "gpt-5-mini") -> None:
        self.url = OPENAI_KEY
        self.client = OpenAI(api_key=OPENAI_KEY)
        self.model = model

    def parse_input(self, user_scenery: str) -> dict:
        print("Starting to parse user input and fetch macro metrics...")
        try:
            response = self.client.responses.create(
                model=self.model,
                input=[
                    {"role": "system", "content": parse_input_prompt},
                    {"role": "user", "content": user_scenery},
                ],
            )
        except Exception as exc:
            raise RuntimeError("Error during LLM processing.") from exc
        
        return response.output_text

    def analyse_risk(self, context: dict) -> str:
        pass


