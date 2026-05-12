from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional


class DatasetSummary(BaseModel):
    rows: int
    columns: int
    column_names: List[str]
    numeric_columns: List[str]
    categorical_columns: List[str]


class TrendResult(BaseModel):
    slope: float
    direction: str


class AnalysisResult(BaseModel):
    dataset_summary: DatasetSummary
    missing_values: Dict[str, int]
    statistics: Dict[str, Dict[str, float]]
    trends: Dict[str, TrendResult]
    anomalies: List[Dict[str, Any]]
    charts: List[str]
    status: str = "success"


class InsightReport(BaseModel):
    executive_summary: str = Field(..., description="Short business-level summary")
    key_trends: List[str]
    anomalies_detected: List[str]
    recommendations: List[str]
    limitations: List[str]


class WorkflowResponse(BaseModel):
    analysis_result: AnalysisResult
    insight_report: Optional[InsightReport] = None
    logs: List[str]