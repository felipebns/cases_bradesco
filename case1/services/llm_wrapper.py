from services.config import OPENAI_KEY
from services.prompts import process_prompt, data_input_template_process, data_input_template_summary, summary_prompt
from openai import OpenAI
import json

class LLM_Wrapper:
    def __init__(self, model: str = "gpt-5-mini") -> None:
        self.url = OPENAI_KEY
        self.client = OpenAI(api_key=OPENAI_KEY)
        self.model = model

    def analyse_data(self, current_period_data: json, past_period_data: json) -> str:
        data_input = data_input_template_process.format(
            current_period_data=json.dumps(current_period_data),
            past_period_data=json.dumps(past_period_data),
        )
        print("Starting LLM processing...")
        try:
            response = self.client.responses.create(
                model=self.model,
                input=[
                    {"role": "system", "content": process_prompt},
                    {"role": "user", "content": data_input},
                ],
            )
        except Exception as exc:
            raise RuntimeError("Error during LLM processing.") from exc

        return response.output_text

    def create_summary(self) -> str:
        path = "data/output/results.json"

        try:
            with open(path, "r", encoding="utf-8") as f:
                recent_analysis = json.load(f)
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"Current period data file not found at {path}.") from exc
        
        data_input = data_input_template_summary.format(
            recent_analysis=json.dumps(recent_analysis),
        )
        print("Starting LLM summary...")
        try:
            response = self.client.responses.create(
                model=self.model,
                input=[
                    {"role": "system", "content": summary_prompt},
                    {"role": "user", "content": data_input},
                ],
            )
        except Exception as exc:
            raise RuntimeError("Error during LLM processing.") from exc
        
        return response.output_text


