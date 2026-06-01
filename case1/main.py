from services.pipeline import Pipeline

if __name__ == "__main__":
    pipeline = Pipeline(transcript_period="q1_2026", previous_transcript="q4_2025")
    pipeline.run()