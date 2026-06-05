## Arquitetura

Fluxo simples e modular. O `main.py` instancia a `Pipeline`, que orquestra ingestao, chamada ao LLM e persistencia de outputs. A `Pipeline` usa o `LLM_Wrapper` para chamar a LLM, enquanto os prompts ficam centralizados em `services/prompts.py`. O output e salvo em JSON (analise estruturada) e em Markdown (relatorio executivo).

Resumo do fluxo:
1) Ingestao da transcricao.
2) LLM 1: gera analise estruturada em JSON.
3) LLM 2: gera relatorio executivo em Markdown.
4) Dump em `data/output/`.

## Decisoes de prompt engineering

Os prompts usados estao dentro do codigo (em `services/prompts.py`), com separacao por etapa:

- Analise estruturada: JSON estrito com schema explicito para garantir parse e consistencia.
- Guidance/temas: enfase em mudancas vs. trimestre anterior.
- Citacoes literais: regras claras para trechos de transcricao e red flags.
- Relatorio: segunda chamada focada apenas no resumo em Markdown.

## Extensoes escolhidas

Nenhuma extensao no Case 1. Priorizei o investimento de extensoes no Case 2.

## Tempo gasto

Aproximadamente 6-7 horas, gastei bastante tempo formulando a arquitetura do código, que foi reaproveitada em partes no case 2 e bastante tempo fazendo os prompts das LLMs

## Limitacoes identificadas

- Ingestao apenas de texto: nao ha deteccao de voz/entonacao, o que pode ocultar nuances.
- Ingestao manual: copia/cola do Seeking Alpha e tratamento manual.
- Duas chamadas de LLM aumentam custo e latencia.

## Com mais 2 semanas eu faria

- Incluir analise do preco da acao durante a call para medir surpresa em tempo real.
- Automatizar a coleta e limpeza das transcricoes.

## Exemplo de execucao

Input: 