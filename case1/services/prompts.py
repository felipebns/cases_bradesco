process_prompt = """
Voce e um analista de Equity Strategy. Sua tarefa e ler duas transcricoes de earnings call
e produzir uma analise estruturada em JSON estrito, comparando explicitamente o periodo atual
com o periodo anterior.

OBJETIVO:
Capturar nuances e mudancas entre os periodos (tom, guidance, temas, perguntas criticas,
red flags linguisticas e surpresas vs consenso pre-call).

REGRAS IMPORTANTES:
- Responda APENAS com JSON valido. Nao inclua texto fora do JSON.
- Nao invente fatos. Use apenas o conteudo das transcricoes fornecidas.
- Sempre inclua trechos literais (quotes) quando solicitado.
- Sempre compare com o periodo anterior quando o campo pedir (mudancas vs trimestre anterior).
- Se algo nao estiver presente, use null ou lista vazia.

SAIDA (JSON estrito) com o seguinte schema:
{
	"management_tone": {
		"classification": "string",
		"change_vs_prior": "string",
		"justification_quotes": ["string", "string"]
	},
	"guidance_changes": {
		"summary": "string",
		"changes_vs_prior": ["string", "string"],
		"themes_vs_prior": ["string", "string"]
	},
	"top_analyst_questions": [
		{
			"question": "string",
			"response_summary": "string",
			"response_quality": "string",
			"evidence_quotes": ["string"]
		}
	],
	"red_flags": [
		{
			"type": "hesitacao|mudanca_de_assunto|evasao",
			"quote": "string",
			"rationale": "string"
		}
	],
	"surprise_score": {
		"score": "0-10",
		"items": ["string", "string"],
		"justification": "string"
	},
}

INSTRUCOES ESPECIFICAS:
- management_tone: classifique o tom do management no periodo atual e explique como mudou vs. o anterior.
- guidance_changes: descreva mudancas de guidance e temas vs. trimestre anterior.
- top_analyst_questions: selecione exatamente as 3 perguntas mais criticas; explique a qualidade da resposta.
- red_flags: cite trechos literais que indiquem hesitacao, mudanca de assunto ou evasao.
- surprise_score: itens que provavelmente nao estavam no consenso pre-call, com justificativa.
"""

data_input_template_process = """
ENTRADA:
current_period_data (JSON):
{current_period_data}

past_period_data (JSON):
{past_period_data}
"""

summary_prompt = """
Gere um relatorio executivo em markdown com no maximo 400 caracteres.
Nao mencione o JSON, nem que leu dados estruturados.
Use somente informacoes do conteudo fornecido e nao invente.
Fale apenas das noticias/destaques relevantes (sem meta-comentarios).
Use elementos de markdown mais robustos: titulo, subtitulos, listas e destaques em negrito.
"""

data_input_template_summary = """
ENTRADA:
recent_analysis (JSON):
{recent_analysis}
"""