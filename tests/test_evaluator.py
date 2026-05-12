from evaluation.evaluator import (
    calculate_report_completeness_score,
    calculate_trend_coverage,
)
from app.schemas import InsightReport
from workflows.analysis_workflow import run_analysis_workflow


def test_report_completeness_score_full_report():
    report = InsightReport(
        executive_summary="Summary",
        key_trends=["Trend"],
        anomalies_detected=["Anomaly"],
        recommendations=["Recommendation"],
        limitations=["Limitation"],
    )

    score = calculate_report_completeness_score(report)

    assert score == 1.0


def test_report_completeness_score_missing_report():
    score = calculate_report_completeness_score(None)

    assert score == 0.0


def test_trend_coverage():
    result, _ = run_analysis_workflow("data/sample_sales.csv")

    coverage = calculate_trend_coverage(result)

    assert coverage == 1.0