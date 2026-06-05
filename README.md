## Bradesco BBI Equity Strategy - Cases Tecnicos

Repositorio com dois cases tecnicos:

- Case 1: Earnings Call Intelligence Tracker (ver pasta `case1/`).
- Case 2: Macro Scenario Engine (ver pasta `case2/`).

## Como rodar

1) Crie um ambiente virtual e instale dependencias:

```
python -m venv .venv
source .venv/bin/activate
pip install -r case1/requirements.txt
pip install -r case2/requirements.txt
```

2) Coloque sua chave de API da OPENAI no .env 

3) Execute cada case:

- Case 1: `python case1/main.py`
- Case 2 (CLI): `python case2/main.py`
- Case 2 (UI): `streamlit run case2/app.py` ou `https://macroengine.streamlit.app/`

Os prompts usados estao em `case1/services/prompts.py` e `case2/services/prompts.py`.