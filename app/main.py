from workflows.analysis_workflow import run_analysis_workflow


if __name__ == "__main__":
    result, logs = run_analysis_workflow("data/sample_sales.csv")

    print("LOGS")
    for log in logs:
        print(f"- {log}")

    print("\nRESULT")
    print(result.model_dump_json(indent=2))