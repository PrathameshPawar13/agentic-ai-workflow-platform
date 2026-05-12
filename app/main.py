from workflows.analysis_workflow import run_analysis_workflow
from agents.insight_agent import generate_insight_report


if __name__ == "__main__":
    result, logs = run_analysis_workflow("data/sample_sales.csv")

    print("LOGS")
    for log in logs:
        print(f"- {log}")

    print("\nANALYSIS RESULT")
    print(result.model_dump_json(indent=2))

    try:
        insight_report = generate_insight_report(result)
        print("\nINSIGHT REPORT")
        print(insight_report.model_dump_json(indent=2))
    except Exception as e:
        print("\nINSIGHT REPORT FAILED")
        print(str(e))