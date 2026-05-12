import json
from app.schemas import AnalysisResult, InsightReport
from llm.factory import get_llm_client


def build_insight_prompt(analysis_result: AnalysisResult) -> str:
    """
    Build a prompt for generating structured business insights.
    """
    analysis_json = analysis_result.model_dump_json(indent=2)

    return f"""
You are given the following deterministic data analysis result.

Generate a valid JSON object with exactly these fields:

{{
  "executive_summary": "string",
  "key_trends": ["string"],
  "anomalies_detected": ["string"],
  "recommendations": ["string"],
  "limitations": ["string"]
}}

Rules:
- Return only valid JSON.
- Do not include markdown.
- Do not include explanations outside JSON.
- Do not invent values.
- Use only the statistics, anomalies, and schema provided below.
- Keep the output concise and professional.

Analysis result:
{analysis_json}
"""


def extract_json(raw_response: str) -> dict:
    """
    Extract JSON from an LLM response.
    Handles cases where the model wraps JSON in extra text.
    """
    raw_response = raw_response.strip()

    if raw_response.startswith("```"):
        raw_response = raw_response.replace("```json", "").replace("```", "").strip()

    start = raw_response.find("{")
    end = raw_response.rfind("}")

    if start == -1 or end == -1:
        raise ValueError(f"No JSON object found in response: {raw_response}")

    json_text = raw_response[start:end + 1]
    return json.loads(json_text)


def generate_insight_report(analysis_result: AnalysisResult) -> InsightReport:
    """
    Generate structured insight report using the configured LLM provider.
    """
    llm_client = get_llm_client()
    prompt = build_insight_prompt(analysis_result)

    raw_response = llm_client.generate(prompt)
    parsed = extract_json(raw_response)

    return InsightReport(**parsed)