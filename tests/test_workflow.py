from workflows.analysis_workflow import run_analysis_workflow


def test_analysis_workflow_success():
    result, logs = run_analysis_workflow("data/sample_sales.csv")

    assert result.status == "success"
    assert result.dataset_summary.rows == 10
    assert "sales" in result.statistics
    assert "sales" in result.trends
    assert len(result.charts) > 0
    assert "Validation passed" in logs