from agents.insight_agent import extract_json


def test_extract_json_from_clean_json():
    raw_response = """
    {
      "executive_summary": "Summary",
      "key_trends": ["Trend"],
      "anomalies_detected": ["Anomaly"],
      "recommendations": ["Recommendation"],
      "limitations": ["Limitation"]
    }
    """

    parsed = extract_json(raw_response)

    assert parsed["executive_summary"] == "Summary"
    assert parsed["key_trends"] == ["Trend"]


def test_extract_json_from_markdown_block():
    raw_response = '''
    ```json
    {
      "executive_summary": "Summary",
      "key_trends": ["Trend"],
      "anomalies_detected": ["Anomaly"],
      "recommendations": ["Recommendation"],
      "limitations": ["Limitation"]
    }
    ```
    '''

    parsed = extract_json(raw_response)

    assert parsed["executive_summary"] == "Summary"
    assert parsed["limitations"] == ["Limitation"]