from services.pipeline import Pipeline

if __name__ == "__main__":
    pipeline = Pipeline(transcript_period="q1_2026", previous_transcript="q4_2025")
    pipeline.run()

    # Fluxo: 

    # Ingere os dados

    # Faz 1 call de LLM com dados atuais e dados anteriores

    # Cria json com informações necessárias

    # Gera relatório