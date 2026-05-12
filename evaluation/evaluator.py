import json
import time
from typing import Optional

from pydantic import BaseModel

from workflows.analysis_workflow import run_analysis_workflow
from agents.insight_agent import generate_insight_report
from app.schemas import InsightReport


class EvaluationResult(BaseModel):
    """
    Evaluation metrics for the analysis and insight workflow.
    """

    workflow_success: bool
    validation_passed: bool
    runtime_seconds: float
    num_anomalies: int
    num_charts: int
    trend_coverage: float
    insight_generated: bool
    report_completeness_score: float
    error: Optional[str] = None


def calculate_report_completeness_score(insight_report: Optional[InsightReport]) -> float:
    """
    Calculate completeness score for the LLM insight report.
    """
    if insight_report is None:
        return 0.0

    required_fields = [
        insight_report.executive_summary,
        insight_report.key_trends,
        insight_report.anomalies_detected,
        insight_report.recommendations,
        insight_report.limitations,
    ]

    completed_fields = 0

    for field in required_fields:
        if isinstance(field, str) and field.strip():
            completed_fields += 1
        elif isinstance(field, list) and len(field) > 0:
            completed_fields += 1

    return completed_fields / len(required_fields)


def calculate_trend_coverage(result) -> float:
    """
    Calculate the share of numeric columns that received trend analysis.
    """
    numeric_columns = result.dataset_summary.numeric_columns

    if not numeric_columns:
        return 1.0

    analyzed_columns = set(result.trends.keys())
    expected_columns = set(numeric_columns)

    return len(analyzed_columns.intersection(expected_columns)) / len(expected_columns)


def evaluate_workflow(file_path: str) -> EvaluationResult:
    """
    Run the full workflow and calculate evaluation metrics.
    """
    start_time = time.time()

    try:
        analysis_result, logs = run_analysis_workflow(file_path)

        try:
            insight_report = generate_insight_report(analysis_result)
            insight_generated = True
        except Exception:
            insight_report = None
            insight_generated = False

        runtime_seconds = round(time.time() - start_time, 4)

        return EvaluationResult(
            workflow_success=analysis_result.status == "success",
            validation_passed="Validation passed" in logs,
            runtime_seconds=runtime_seconds,
            num_anomalies=len(analysis_result.anomalies),
            num_charts=len(analysis_result.charts),
            trend_coverage=calculate_trend_coverage(analysis_result),
            insight_generated=insight_generated,
            report_completeness_score=calculate_report_completeness_score(insight_report),
            error=None,
        )

    except Exception as e:
        runtime_seconds = round(time.time() - start_time, 4)

        return EvaluationResult(
            workflow_success=False,
            validation_passed=False,
            runtime_seconds=runtime_seconds,
            num_anomalies=0,
            num_charts=0,
            trend_coverage=0.0,
            insight_generated=False,
            report_completeness_score=0.0,
            error=str(e),
        )


if __name__ == "__main__":
    result = evaluate_workflow("data/sample_sales.csv")
    print(result.model_dump_json(indent=2))