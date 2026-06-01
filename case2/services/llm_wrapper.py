from services.config import OPENAI_KEY
from openai import OpenAI
import json

class LLM_Wrapper:
    def __init__(self, model: str = "gpt-5-mini") -> None:
        self.url = OPENAI_KEY
        self.client = OpenAI(api_key=OPENAI_KEY)
        self.model = model

    def process_best_worst_sectors(self, user_scenery: str) -> tuple:
        pass

    def process_best_worst_tickers(self, best_sectors: dict, worst_sectors: dict) -> tuple:
        pass

    def process_risks(self, best_sectors: dict, worst_sectors: dict, best_tickers: dict, worst_tickers: dict) -> dict:
        pass

    def create_summary(self, risks: dict, best_sectors: dict, worst_sectors: dict, best_tickers: dict, worst_tickers: dict, user_scenery: str) -> tuple:
        pass


