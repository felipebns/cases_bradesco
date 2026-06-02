import yfinance
import requests
import pandas as pd
from datetime import datetime

TODAY = datetime.today()

class StockWrapper:
    def __init__(self) -> None:
        self.b3_stocks = [] #completar
        
        self.end = TODAY.strftime("%d/%m/%Y")
        self.start = TODAY.replace(year=TODAY.year - 10).strftime("%d/%m/%Y")

        self.base_url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{{CODE}}/dados?formato=json&dataInicial={self.start}&dataFinal={self.end}"

    @staticmethod
    def _normalize_in_semesters(values: list, key: str) -> dict:

        df = pd.DataFrame(values)

        df["data"] = pd.to_datetime(df["data"], format="%d/%m/%Y", errors="coerce")
        df["valor"] = pd.to_numeric(df["valor"], errors="coerce")

        df["year"] = df["data"].dt.year
        df["semester"] = df["data"].dt.month.apply(lambda m: 1 if m <= 6 else 2)
        semester_avg = df.groupby(["year", "semester"])["valor"].mean().sort_index()

        diff = semester_avg.diff()
        diff = diff.dropna()
        diff_std = diff.std() #dividi por 2 arbitrariamente para gerar maior diversidade de dados
        # print(diff)
        direction = diff.apply(
            lambda v: "estavel" if -(diff_std/2) <= v <= (diff_std/2) else ("subiu" if v > 0 else "desceu")
        )
        # print(direction)

        return {
            f"{year}.{sem}": value
            for (year, sem), value in direction.items()
        }

    def get_stocks(self) -> list:
        pass

    def get_macro_metrics(self) -> list:
        print("Downloading macroeconomic data...")

        codes = {
            "selic": 11, #Selic efetiva / diario
            "inflacao": 433, #IPCA / mensal
            "dolar": 1, # PTAX venda / diario
            "pib": 24364 #IBC - Br / mensal
        }
        dfs = {}

        for key, value in codes.items():
            adj_url = self.base_url.format(CODE=value)
            values = requests.get(adj_url).json()
            values = self._normalize_in_semesters(values, key)
            dfs[key] = values

        df = pd.DataFrame(dfs)
        df.index.name = "periodo"
        return df
        
    def process_similar_macro_stock_scenario(self, stocks_data: list, macro_data: list, affected_metrics: dict) -> list:
        pass

    def process_best_worst_tickers(self, periods: list) -> tuple:
        pass

    def process_best_worst_sectors(self, best_stocks: list, worst_stocks: list) -> tuple:
        pass


