import yfinance
import requests
from datetime import datetime

TODAY = datetime.today()

class StockWrapper:
    def __init__(self) -> None:
        self.b3_stocks = [] #completar
        
        self.end = TODAY.strftime("%d/%m/%Y")
        self.start = TODAY.replace(year=TODAY.year - 10).strftime("%d/%m/%Y")

        self.base_url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{{CODE}}/dados?formato=json&dataInicial={self.start}&dataFinal={self.end}"

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
            dfs[key] = requests.get(adj_url).json()
        
    def process_similar_macro_stock_scenario(self, stocks_data: list, macro_data: list, affected_metrics: dict) -> list:
        pass

    def process_best_worst_tickers(self, periods: list) -> tuple:
        pass

    def process_best_worst_sectors(self, best_stocks: list, worst_stocks: list) -> tuple:
        pass


