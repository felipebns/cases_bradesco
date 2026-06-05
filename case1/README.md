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

Input: python main.py

Dados: Earning calls q1_2026 e q4_2025 da AMBEV 

Output json: 

```json
{
    "management_tone": {
        "classification": "cautiously confident / execution-focused",
        "change_vs_prior": "Shifted from a year-end tone of resilience and reflection to a more forward-facing, execution and growth tone that emphasizes momentum, commercial wins and confidence in cyclical recovery (World Cup/calendar tailwinds). Prior period emphasized having been 'stress tested' and preparing for 2026; current period emphasizes having already started 2026 with tangible momentum and operational execution.",
        "justification_quotes": [
            "\"Last year was the many and that made the third objective, the hardest to deliver. As a team, we embrace the challenge elevated our market intelligence capabilities and focus on what we could control, guided by our growth strategy.\"",
            "\"Ambev delivered a solid start to the year. Total volumes were broadly flat against the toughest comparison base of the year while beer returned to growth, up low single digit.\"",
            "\"We made meaningful progress on the mission we set from day 1, even in a dynamic context that stress tested our strategy.\"",
            "\"We entered the year maintaining the same financial discipline that has guided us over the past quarters to drive long-term value creation through our capital allocation framework.\""
        ]
    },
    "guidance_changes": {
        "summary": "Management maintained existing cost guidance (Brazil Beer cash COGS per hectoliter, excl. marketplace) for 2026 at 4.5%–7.5% and reiterated confidence in margin expansion ambition while flagging Q1 as peak cost intensity with easing expected from Q2. No upward or downward revision to the stated 2026 COGS guidance was announced.",
        "changes_vs_prior": [
            "Guidance unchanged: Brazil Beer cash COGS per hectoliter excl. marketplace maintained at 4.5%–7.5% for 2026 (same range referenced in prior period).",
            "No new formal guidance ranges were introduced; management reiterated the same cost guidance and emphasized cadence (Q1 higher; easing from Q2) rather than changing ranges."
        ],
        "themes_vs_prior": [
            "Prior period theme: reflection on 2025 as a stress test, emphasizing resilience, margin expansion delivered in 2025 and the strategy validated.",
            "Current period theme: execution and momentum — translating 2025 strengthening into Q1 results, commercial wins (mix/premium growth), strong Q1 cash generation, and preparing to leverage event-driven demand (World Cup) while keeping prior guidance."
        ],
        "objective_metrics": [
            {
                "metric": "Net revenue per hectoliter (Brazil / consolidated)",
                "prior_period_value": "7.5% (full year 2025 net revenue per hectoliter growth)",
                "current_period_value": "8.3% (net revenue per hectoliter growth in Q1)",
                "delta": "+0.8 percentage point (Q1 vs FY reference)",
                "evidence_quotes": [
                    "\"In essence, Zé gives us a direct window into the future... This portfolio supported a solid net revenue per hectoliter performance, up 8.3% in the quarter\"",
                    "\"We closed 2025 delivering consolidated normalized EBITDA margin expansion of 50 bps... First, net revenue per hectoliter growth of 7.5%\""
                ]
            },
            {
                "metric": "Brazil Beer cash COGS per hectoliter (excluding marketplace) — point change",
                "prior_period_value": "6.1% increase in 2025 (cash COGS per hectoliter, excluding non-Ambev marketplace, for full year 2025)",
                "current_period_value": "14.6% increase in the quarter (Brazil Beer cash COGS per hectoliter in Q1)",
                "delta": "+8.5 percentage points (Q1 YoY vs 2025 full-year increase)",
                "evidence_quotes": [
                    "\"Consolidated cash COGS per hectoliter excluding marketplace, increased 9% in the period, with Brazil Beer up 14.6%\"",
                    "\"Brazil Beer is a clear proof point... our cash COGS per hectoliter, excluding non-Ambev marketplace products increased by 6.1% in 2025\""
                ]
            },
            {
                "metric": "Guidance range — Brazil Beer cash COGS per hectoliter (2026)",
                "prior_period_value": "4.5% to 7.5% (stated for 2026 in prior call)",
                "current_period_value": "4.5% to 7.5% (reaffirmed unchanged)",
                "delta": "no change",
                "evidence_quotes": [
                    "\"we maintain our Brazil Beer cash COGS per hectoliter, excluding marketplace guidance unchanged from 4.5% to 7.5% increase in 2026\"",
                    "\"for 2026, we expect Brazil Beer cash COGS per hectoliter, excluding non-Ambev marketplace products to increase between 4.5% and 7.5%\""
                ]
            }
        ]
    },
    "top_analyst_questions": [
        {
            "question": "My question is about net revenue per hectoliter in Brazil Beer... If you could qualify the 8% year-on-year increase, what drove that in terms of the contribution from mix? Any contribution from price increases... and anything different in the ICMS dynamic this year?",
            "response_summary": "Management attributed the net revenue per hectoliter increase to three hierarchical components: carryover from 2025 RGM (easier comp vs prior years), revenue management initiatives carried into 2026, and positive mix driven by above-core and premium growth. They explicitly said tax (ICMS) dynamics were not material/changed year-over-year.",
            "response_quality": "high — provided a clear hierarchy of drivers (carryover, RGM, mix) and a direct denial of tax-effect contribution, extracting granular qualitative drivers behind the 8%.",
            "evidence_quotes": [
                "\"the first component is exactly the -- all the effort put behind our revenue management agenda in '25 and the carryover we brought into the first quarter of '26.\"",
                "\"the second component in the hierarchy comes from our revenue management agenda into '26... And the third component comes from the mix since our above core segment continued to grow in a very solid pace\"",
                "\"On the tax side, there was nothing that was important to highlight during the quarter. So same as last year.\""
            ]
        },
        {
            "question": "I just wanted to follow up a little bit on the COGS outlook... given the current environment with higher aluminum prices, etc. How should we think about the cost flow through for you guys based on the hedges for the rest of the year?",
            "response_summary": "CFO explained hedging/visibility processes, reiterated the 2026 Brazil Beer cash COGS per hectoliter guidance of 4.5%–7.5%, noted Q1 is probably the cost peak and expected easing from Q2 onward, and emphasized ongoing cost initiatives and efficiencies.",
            "response_quality": "high — provided explicit guidance maintenance, timing/cadence (Q1 peak, easing Q2+), and rationale (hedges, cost projects), giving useful inputs for modeling cadence of cost pressure.",
            "evidence_quotes": [
                "\"When we're starting '26, what we have said to the market is our range between 4.5% for Brazil Beer cash COGS per hectoliter, excluding marketplace from 4.5% to 7.5%.\"",
                "\"We know... that Q1 is probably the highest on cost, and that should start easing through the second quarter onwards.\"",
                "\"we have our hedges, which give us a very good visibility on the forecast going forward... we are maintaining our cash COGS from 4.5% to 7.5% for the year.\""
            ]
        },
        {
            "question": "How confident are you that volumes can grow in the balance of 2026... cycling through the comp, World Cup effects and confidence in category recovery?",
            "response_summary": "Management clarified the comp (Q1 '25 was a strong positive; current cycle is the toughest comp), emphasized that weakness was cyclical (weather / occasion frequency) rather than structural, pointed to calendar tailwinds (World Cup, long holidays) and portfolio momentum as drivers for recovery, and expressed confidence in gradual recovery while noting household income pressure as a watch item.",
            "response_quality": "high — drew out the comp math clarification, reiterated that drivers were cyclical (weather) and provided qualitative confidence drivers (calendar, portfolio momentum), helping assess probability of volume recovery.",
            "evidence_quotes": [
                "\"First, actually, the industry is cycling through the toughest comparison base, not the easiest comparison base...\"",
                "\"the issue was not whether consumers wanted beer, but how often the right occasions happen... the most relevant impact coming from the weather.\"",
                "\"we do expect that, first and foremost, the calendar will bring a pretty interesting right ground for the industry to continue recovering moving forward, right? A combination of long holidays, a combination of FIFA World Cup...\""
            ]
        }
    ],
    "red_flags": [
        {
            "type": "evasao",
            "quote": "\"I will keep the protocol in place. I'm going to answer 1 question to give you all the chance to interact with us, okay?\"",
            "rationale": "Management limited the number of questions answered (refused to address multiple parts of a multi-part question in that exchange), which can be interpreted as evasive when analysts asked multiple related items."
        },
        {
            "type": "evasao",
            "quote": "\"...without going to any -- a territory that we don't want.\"",
            "rationale": "When pressed on sensitive pricing specifics, management explicitly avoided providing detailed numeric guidance, indicating an unwillingness to give potentially market-moving detail."
        },
        {
            "type": "mudanca_de_assunto",
            "quote": "\"And just to add one thing here, Lisboa, I think it's important to remember that on this World Cup, different from the prior, our digital platforms are much more evolved. So we're going to see a lot of activations through something that we've been developing for a long period of time.\"",
            "rationale": "Rather than directly quantifying expected World Cup demand or pricing dynamics when asked, management pivoted to promoting digital activation capabilities — a shift from the analyst's requested topic to a strategic capability narrative."
        }
    ],
    "surprise_score": {
        "score": "4",
        "items": [
            "\"strongest first quarter performance in the past 10 years\" (operating cash flow: BRL 3.2 billion in Q1, +BRL 2 billion YoY)",
            "Brazil Beer volumes grew 1.2% in the quarter despite a tough year-on-year comparison base",
            "Guidance for Brazil Beer cash COGS per hectoliter (4.5%–7.5% for 2026) was reaffirmed unchanged"
        ],
        "justification": "The quarter delivered a few modestly surprising positive datapoints relative to a cautious backdrop — notably unusually strong Q1 cash generation and positive beer volumes in Brazil — but management did not change guidance materially and framed most results as execution of already-communicated initiatives. These outcomes are mildly surprising (tactical upside) but not transformative to the investment case."
    }
}
```

Output markdown: 

# Relatório Executivo — Earnings Call

## Resultado
- **Tom da gestão:** passou a ser mais focado em execução e crescimento, destacando momentum comercial e aproveitamento de efeitos de calendário (ex.: Copa do Mundo).
- **Receita / preço-mix:** **Net revenue por hectolitro subiu 8,3% no trimestre**, impulsionado por carryover da agenda de RGM, iniciativas de revenue management e mix favorável (crescimento acima-core/premium). Impacto fiscal (ICMS) não foi material.
- **Volume:** **Brazil Beer cresceu 1,2% no trimestre**, em contexto de comparação difícil.
- **Custos:** **Brazil Beer cash COGS por hl (excl. marketplace) subiu 14,6% em Q1**, versus aumento de 6,1% em 2025; consolidado excl. marketplace aumentou **9%** no período.
- **Fluxo de caixa operacional:** **R$ 3,2 bi em Q1 (+R$ 2,0 bi YoY)** — apontado como o melhor primeiro trimestre em 10 anos.

## Guidance
- **Guidance reafirmado:** Brazil Beer cash COGS por hl (excl. marketplace) mantido entre **4,5%–7,5% para 2026** (sem alteração).
- **Cadência:** Q1 apontado como **pico de intensidade de custos**, com expectativa de alívio a partir do Q2; gestão cita hedges e iniciativas de eficiência como mitigantes.
- **Prioridade:** continuidade da disciplina financeira e objetivo de **expansão de margem** preservado.

## Riscos
- **Transparência na divulgação:** gestão limitou interações em Q&A e evitou detalhar preços específicos — pode dificultar modelagem fina de preço e promoções.
- **Mudança de assunto em perguntas sensíveis:** preferiram destacar capacidades digitais (ativação na Copa) ao invés de quantificar demanda incremental, reduzindo sinalização quantitativa sobre efeito de eventos.
- **Ambiente macro:** recuperação de volumes considerada principalmente cíclica (clima/ocasiões); **pressão em renda das famílias** é fator de monitoramento relevante.

## Sinais de surpresa
- Itens surpreendentes, moderados em magnitude:
  - **Fluxo operacional forte:** R$ 3,2 bi em Q1 (+R$ 2 bi YoY).
  - **Crescimento de volumes no Brasil** apesar de comps difíceis (**+1,2%**).
  - **Reafirmação de guidance de custos** para 2026 (4,5%–7,5%) apesar de pressão de preços de insumos.
- Avaliação: resultados trazem **surpresas táticas positivas**, reforçando execução; não implicaram mudança de guidance nem alteraram materialmente a tese de investimento.

Principais implicações para decisões: monitorear evolução de custos a partir do Q2, acompanhamento dos impactos da Copa e da renda das famílias sobre volumes, e insistir em clareza adicional nas próximas interações sobre price cadence e hedge exposure.