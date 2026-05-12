import os
import pandas as pd

from tools.schema_inspector import inspect_schema
from tools.data_cleaner import summarize_missing_values, clean_data
from tools.statistics_tool import generate_statistics
from tools.anomaly_detector import detect_anomalies_iqr
from tools.trend_analyzer import analyze_trends
from tools.chart_generator import generate_charts


def sample_dataframe():
    return pd.DataFrame({
        "date": ["2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04"],
        "region": ["North", "South", "East", "West"],
        "sales": [100.0, 120.0, 130.0, 1000.0],
        "units_sold": [10.0, 12.0, 13.0, 100.0],
        "rating": [4.0, 4.1, 4.2, 4.3],
    })


def test_schema_inspection():
    df = sample_dataframe()
    summary = inspect_schema(df)

    assert summary.rows == 4
    assert summary.columns == 5
    assert "sales" in summary.numeric_columns
    assert "region" in summary.categorical_columns


def test_missing_value_summary():
    df = sample_dataframe()
    df.loc[0, "region"] = None

    missing = summarize_missing_values(df)

    assert missing["region"] == 1


def test_clean_data_fills_missing_values():
    df = sample_dataframe()
    df.loc[0, "sales"] = None
    df.loc[1, "region"] = None

    cleaned = clean_data(df)

    assert cleaned["sales"].isnull().sum() == 0
    assert cleaned["region"].isnull().sum() == 0


def test_statistics_generation():
    df = sample_dataframe()
    stats = generate_statistics(df)

    assert "sales" in stats
    assert stats["sales"]["count"] == 4.0


def test_anomaly_detection():
    df = sample_dataframe()
    anomalies = detect_anomalies_iqr(df)

    assert isinstance(anomalies, list)
    assert any(item["column"] == "sales" for item in anomalies)


def test_trend_analysis():
    df = sample_dataframe()
    trends = analyze_trends(df)

    assert "sales" in trends
    assert "slope" in trends["sales"]
    assert "direction" in trends["sales"]


def test_chart_generation(tmp_path):
    df = sample_dataframe()
    chart_paths = generate_charts(df, output_dir=str(tmp_path))

    assert len(chart_paths) > 0

    for path in chart_paths:
        assert os.path.exists(path)