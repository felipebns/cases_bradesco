## Arquitetura

Fluxo simples e modular. O `main.py` instancia a `Pipeline`, que orquestra ingestão, chamada ao LLM e persistência de outputs. A `Pipeline` usa o `LLM_Wrapper` para chamar a LLM, enquanto os prompts ficam centralizados em `services/prompts.py`. O output e salvo em JSON (análise estruturada) e em Markdown (relatório executivo).

Resumo do fluxo:
1) Ingestão de transcrições (JSON já processado)
2) LLM 1: gera análise estruturada em JSON
3) LLM 2: gera relatório executivo em Markdown
4) Dump em `data/output/`

## Decisoes de prompt engineering

- Separação entre instruções e dados de entrada para reduzir ruido e manter o esquema estável.
- Saida JSON estrita com schema explícito para garantir parse e consistência.
- Ênfase em comparação com o trimestre anterior (campo de mudanças e temas vs. periodo anterior).
- Regras claras para incluir quotes literais quando necessário e evitar invenções.
- Segunda chamada focada apenas no relatório, com limite de caracteres e formato em Markdown.

## Limitacoes identificadas

- Ingestão de APENAS texto: não há detecção de voz/entonação, o que pode ocultar nuances.
- Ingestão ainda manual: copia/cola do Seeking Alpha e tratamento manual. É possivel automatizar, mas não foi prioridade dado o escopo simples.
- Duas calls de LLM: ajuda na separação de responsabilidades e pode melhorar precisão, mas aumenta custo e latência.
