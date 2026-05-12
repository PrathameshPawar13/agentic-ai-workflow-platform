from tools.data_loader import load_csv
from tools.schema_inspector import inspect_schema
from tools.data_cleaner import summarize_missing_values, clean_data
from tools.statistics_tool import generate_statistics
from tools.anomaly_detector import detect_anomalies_iqr
from tools.chart_generator import generate_charts
from tools.validator import validate_analysis_result
from app.schemas import AnalysisResult
from tools.trend_analyzer import analyze_trends

def run_analysis_workflow(file_path: str) -> tuple[AnalysisResult, list[str]]:
    """
    Run the deterministic analysis workflow on a CSV file.
    """
    logs = []

    logs.append("Loading dataset")
    df = load_csv(file_path)

    logs.append("Inspecting schema")
    dataset_summary = inspect_schema(df)

    logs.append("Summarizing missing values")
    missing_values = summarize_missing_values(df)

    logs.append("Cleaning dataset")
    cleaned_df = clean_data(df)

    logs.append("Generating descriptive statistics")
    statistics = generate_statistics(cleaned_df)

    logs.append("Analyzing trends")
    trends = analyze_trends(cleaned_df)

    logs.append("Detecting anomalies")
    anomalies = detect_anomalies_iqr(cleaned_df)

    logs.append("Generating charts")
    charts = generate_charts(cleaned_df)

    result = AnalysisResult(
    dataset_summary=dataset_summary,
    missing_values=missing_values,
    statistics=statistics,
    trends=trends,
    anomalies=anomalies,
    charts=charts,
    status="success"
    )

    logs.append("Validating analysis result")
    is_valid = validate_analysis_result(result)

    if not is_valid:
        logs.append("Validation failed")
        result.status = "failed"
    else:
        logs.append("Validation passed")

    return result, logs