from services.llm_wrapper import LLM_Wrapper
import json

class Pipeline:
    def __init__(self, user_scenery: str) -> None:
        self.user_scenery = user_scenery
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

    def run(self) -> None:
        best_sectors, worst_sectors = self.llm_wrapper.process_best_worst_sectors(self.user_scenery)
        best_tickers, worst_tickers = self.llm_wrapper.process_best_worst_tickers(best_sectors, worst_sectors)
        risks = self.llm_wrapper.process_risks(best_sectors, worst_sectors, best_tickers, worst_tickers)
        json, markdown = self.llm_wrapper.create_summaries(risks, best_sectors, worst_sectors, best_tickers, worst_tickers, self.user_scenery)
