## Arquitetura

Fluxo modular com separacao clara entre orquestracao, dados, LLM e UI.

1) `app.py` (Streamlit) recebe o cenario, aciona a `Pipeline` e renderiza JSON, markdown e graficos.
2) `Pipeline` coordena as etapas e consolida o contexto final.
3) `StockWrapper` baixa dados macro e de acoes, calcula periodos similares, retornos medios e ranking de setores/tickers.
4) `LLM_Wrapper` executa as etapas de parsing, riscos, JSON final e relatorio (com self-critique).
5) `Plot` gera graficos salvos em `data/plots`.

## Decisoes de prompt engineering

Os prompts usados estao dentro do codigo (em `services/prompts.py`), com separacao por etapa:

- Parsing: transforma o cenario em variacoes percentuais padronizadas.
- Riscos: força grounding no contexto e no cenario macro (evita justificativas meta).
- JSON final: explicita canais de transmissao e justificativas por setor/ticker.
- Self-critique: revisa o JSON final e remove incoerencias, mantendo o mesmo schema.

## Extensoes escolhidas

- Self-critique loop: garante racional mais consistente e canais de transmissao mais claros.
- Interface Streamlit: entrega uma UI simples e funcional para analise interativa.
- Canais de transmissao explicitos: presentes no JSON final e no relatorio.

## Por que escolhi aprofundar o Case 2

O Case 2 pareceu mais desafiador e alinhado as minhas habilidades de Tech/AI. Ele permite demonstrar
engenharia de dados, prompts, orquestracao e UI em um fluxo unico, e as extensoes agregam valor direto
para a interpretacao macro-setorial.

## Tempo gasto

Aproximadamente 20 horas, gastei muito tempo para baixar os relatórios FOCUS, mas eles se mostraram excepcionalmente difíceis de extrair dados consistentemente. Como utilizo algumas chamadas de LLM aqui, gastei bastante tempo também configurando seus prompts e como eu estou pegando dados de múltiplas fontes também, o processamento deles para decidir um período ideal para análise demorou mais do que esperava

## Limitacoes identificadas

- A comparacao usa o cenario atual do usuario versus variacoes historicas observadas, sem incorporar
	projeoes de mercado oficiais como baseline.
- Varias chamadas de LLM aumentam custo e podem propagar subjetividades ao longo do fluxo.
- A integracao com o relatório Focus foi tentada, mas a extracao dos PDFs mostrou baixa confiabilidade.

## Com mais 2 semanas eu faria

- Integraria dados de projeoes do relatorio Focus como baseline do cenario, com parser mais robusto.
- Implementaria validacao de consistencia dos outputs e testes automatizados para LLM e dados.

## Exemplo de execucao

TODO: incluir um exemplo completo de input e output (JSON + markdown).
