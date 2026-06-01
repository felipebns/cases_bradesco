from services.llm_wrapper import LLM_Wrapper
import json

class Pipeline:
    def __init__(self, transcript_period: str, previous_transcript: str) -> None:
        self.transcript_period = transcript_period
        self.previous_transcript = previous_transcript
        self.llm_wrapper = LLM_Wrapper()

    def _ingest(self) -> tuple:
        current_period_path = f"data/{self.transcript_period}/processed/{self.transcript_period}.json"
        with open(current_period_path, '+r', encoding='utf-8') as f:
            current_period_data = json.load(f)

        past_period_path = f"data/{self.previous_transcript}/processed/{self.previous_transcript}.json"
        with open(past_period_path, '+r', encoding='utf-8') as f:
            past_period_data = json.load(f)
        
        return current_period_data, past_period_data
    
    def _dump_json() -> None:
        pass

    def run(self) -> None:
        current_period_data, past_period_data = self._ingest()

        self.llm_wrapper.process(current_period_data, past_period_data)

