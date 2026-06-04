from services.llm_wrapper import LLM_Wrapper
from services.stock_wrapper import StockWrapper
import json

class Pipeline:
    def __init__(self, user_scenery: str) -> None:
        self.user_scenery = user_scenery
        self.llm_wrapper = LLM_Wrapper()
        self.stock_wrapper = StockWrapper()

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

    @staticmethod
    def _group_context(best_stocks: list, worst_stocks: list, best_sectors: list, worst_sectors: list) -> dict:
        return {
            "best_stocks": best_stocks,
            "worst_stocks": worst_stocks,
            "best_sectors": best_sectors,
            "worst_sectors": worst_sectors
        }

    def run(self) -> None:
        print("Starting pipeline execution...")
        # ===============================================================
        # input VAI ter que ter as 4 variáveis, depois buscar por rolling semestres mais semelhantes a esse cenário
        # pib, inflação, selic(juros) e dolar -> calcular variação, identificar periodos que a variavel mudou na mesma taxa ou apenas direção
        # baixa preço fechamento ações ibovespa, rotular qual setor ela pertence, peso cada papel diariamente
        # avaliar quais ações subiram mais nesse periodo, agrupar por setor com todas as ações para avaliar, junto com o peso de cada ação
        # ===============================================================

        affected_metrics = self.llm_wrapper.parse_input(self.user_scenery) #done
        macro_data = self.stock_wrapper.get_macro_metrics() #done 
        stocks_data = self.stock_wrapper.get_stocks() #done
        periods = self.stock_wrapper.process_similar_macro_scenario(macro_data, affected_metrics) #done
        best_stocks, worst_stocks, all_stocks_sorted = self.stock_wrapper.process_best_worst_tickers(periods, stocks_data) #done
        best_sectors, worst_sectors, sorted_sectors = self.stock_wrapper.process_best_worst_sectors(all_stocks_sorted) #done 
        # print(all_stocks_sorted)
        print(best_stocks)
        print(worst_stocks)
        print()
        print(best_sectors)
        print(worst_sectors)
        # print(sorted_sectors)

        # context = self._group_context(best_stocks, worst_stocks, best_sectors, worst_sectors)
        # risks = self.llm_wrapper.analyse_risk(context)
        # self.llm_wrapper.generate_json()
        # self.llm_wrapper.generate_report()

        # Visulização stocks na interface streamlit
        # No final usar uma ia parar justifcar a escolha dos stocks e os setores, juntando métricas quantitativas com lógica