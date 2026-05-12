import os
import tempfile

import pandas as pd
import streamlit as st

from workflows.analysis_workflow import run_analysis_workflow
from agents.insight_agent import generate_insight_report


st.set_page_config(
    page_title="Agentic AI Workflow Platform",
    page_icon="🤖",
    layout="wide",
)


st.title("Agentic AI Workflow Automation Platform")
st.write(
    "Upload a CSV file to run deterministic data analysis, anomaly detection, "
    "trend analysis, chart generation, and LLM-generated insights."
)


uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])


def display_dataset_summary(result):
    st.subheader("Dataset Summary")

    summary = result.dataset_summary

    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", summary.rows)
    col2.metric("Columns", summary.columns)
    col3.metric("Numeric Columns", len(summary.numeric_columns))

    st.write("Column names:")
    st.write(summary.column_names)

    st.write("Numeric columns:")
    st.write(summary.numeric_columns)

    st.write("Categorical columns:")
    st.write(summary.categorical_columns)


def display_missing_values(result):
    st.subheader("Missing Values")
    missing_df = pd.DataFrame(
        list(result.missing_values.items()),
        columns=["Column", "Missing Values"],
    )
    st.dataframe(missing_df, use_container_width=True)


def display_statistics(result):
    st.subheader("Descriptive Statistics")
    stats_df = pd.DataFrame(result.statistics).T
    st.dataframe(stats_df, use_container_width=True)


def display_trends(result):
    st.subheader("Trend Analysis")
    trends_data = []

    for column, trend in result.trends.items():
        trends_data.append({
            "Column": column,
            "Slope": trend.slope,
            "Direction": trend.direction,
        })

    trends_df = pd.DataFrame(trends_data)
    st.dataframe(trends_df, use_container_width=True)


def display_anomalies(result):
    st.subheader("Anomalies")

    if not result.anomalies:
        st.success("No anomalies detected.")
        return

    anomalies_df = pd.DataFrame(result.anomalies)
    st.dataframe(anomalies_df, use_container_width=True)


def display_charts(result):
    st.subheader("Generated Charts")

    if not result.charts:
        st.info("No charts generated.")
        return

    chart_columns = st.columns(2)

    for index, chart_path in enumerate(result.charts):
        if os.path.exists(chart_path):
            with chart_columns[index % 2]:
                st.image(chart_path, caption=os.path.basename(chart_path), use_container_width=True)


def display_insight_report(insight_report):
    st.subheader("LLM Insight Report")

    if insight_report is None:
        st.warning("Insight report could not be generated.")
        return

    st.markdown("### Executive Summary")
    st.write(insight_report.executive_summary)

    st.markdown("### Key Trends")
    for item in insight_report.key_trends:
        st.write(f"- {item}")

    st.markdown("### Anomalies Detected")
    for item in insight_report.anomalies_detected:
        st.write(f"- {item}")

    st.markdown("### Recommendations")
    for item in insight_report.recommendations:
        st.write(f"- {item}")

    st.markdown("### Limitations")
    for item in insight_report.limitations:
        st.write(f"- {item}")


def display_logs(logs):
    st.subheader("Workflow Logs")
    for log in logs:
        st.write(f"- {log}")


if uploaded_file is not None:
    st.success(f"Uploaded file: {uploaded_file.name}")

    preview_df = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(preview_df.head(), use_container_width=True)

    uploaded_file.seek(0)

    if st.button("Run Analysis", type="primary"):
        with st.spinner("Running analysis workflow..."):
            temp_file_path = None

            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
                    temp_file.write(uploaded_file.getvalue())
                    temp_file_path = temp_file.name

                result, logs = run_analysis_workflow(temp_file_path)

                try:
                    insight_report = generate_insight_report(result)
                    logs.append("Generated LLM insight report")
                except Exception as insight_error:
                    insight_report = None
                    logs.append(f"Insight generation failed: {str(insight_error)}")

                st.success("Analysis completed successfully.")

                display_dataset_summary(result)
                display_missing_values(result)
                display_statistics(result)
                display_trends(result)
                display_anomalies(result)
                display_charts(result)
                display_insight_report(insight_report)
                display_logs(logs)

            except Exception as e:
                st.error(f"Analysis failed: {str(e)}")

            finally:
                if temp_file_path and os.path.exists(temp_file_path):
                    os.remove(temp_file_path)