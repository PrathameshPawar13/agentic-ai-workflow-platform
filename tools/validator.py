from app.schemas import AnalysisResult


def validate_analysis_result(result: AnalysisResult) -> bool:
    """
    Validate that the analysis result contains minimum required information.
    """
    if result.dataset_summary.rows <= 0:
        return False

    if result.dataset_summary.columns <= 0:
        return False

    if result.status != "success":
        return False

    return True