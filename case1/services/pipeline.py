from services.llm_wrapper import LLM_Wrapper
import json

class Pipeline:
    def __init__(self, transcript_period: str, previous_transcript: str) -> None:
        self.transcript_period = transcript_period
        self.previous_transcript = previous_transcript
        self.llm_wrapper = LLM_Wrapper()

    @staticmethod
    def _dump_json(response: str) -> None:

        try:
            parsed_response = json.loads(response)
        except json.JSONDecodeError as exc:
            raise ValueError("LLM response is not valid JSON.") from exc
        
        path = "data/output/results.json"

        with open(path, "w", encoding="utf-8") as f:
            json.dump(parsed_response, f, ensure_ascii=False, indent=4)

    @staticmethod
    def _dump_markdown(response: str) -> None:
        path = "data/output/report.md"

        with open(path, "w", encoding="utf-8") as f:
            f.write(response)

    def _ingest(self) -> tuple:
        try:
            current_period_path = f"data/{self.transcript_period}/processed/{self.transcript_period}.json"
            with open(current_period_path, '+r', encoding='utf-8') as f:
                current_period_data = json.load(f)
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"Current period data file not found at {current_period_path}.") from exc

        try:
            past_period_path = f"data/{self.previous_transcript}/processed/{self.previous_transcript}.json"
            with open(past_period_path, '+r', encoding='utf-8') as f:
                past_period_data = json.load(f)
        except FileNotFoundError as exc:
            raise FileNotFoundError(f"Past period data file not found at {past_period_path}.") from exc

        return current_period_data, past_period_data

    def run(self) -> None:
        current_period_data, past_period_data = self._ingest()
        analysis = self.llm_wrapper.process(current_period_data, past_period_data)
        self._dump_json(analysis)
        markdown = self.llm_wrapper.create_summary()
        self._dump_markdown(markdown)
        print("Pipeline execution completed successfully.")
