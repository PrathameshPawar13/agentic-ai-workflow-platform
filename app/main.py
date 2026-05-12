import os
import shutil
import tempfile
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from workflows.analysis_workflow import run_analysis_workflow
from agents.insight_agent import generate_insight_report
from app.schemas import WorkflowResponse


app = FastAPI(
    title="Agentic AI Workflow Automation Platform",
    description="API for CSV analysis, deterministic analytics, anomaly detection, trend analysis, and LLM-generated insights.",
    version="0.1.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    """
    Health check endpoint.
    """
    return {
        "message": "Agentic AI Workflow Automation Platform API is running",
        "docs": "/docs",
    }


@app.post("/analyze", response_model=WorkflowResponse)
async def analyze_csv(file: UploadFile = File(...)):
    """
    Analyze an uploaded CSV file and return deterministic analysis,
    LLM-generated insight report, and workflow logs.
    """
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported.")

    temp_file_path = None

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
            temp_file_path = temp_file.name
            shutil.copyfileobj(file.file, temp_file)

        analysis_result, logs = run_analysis_workflow(temp_file_path)

        try:
            insight_report = generate_insight_report(analysis_result)
            logs.append("Generated LLM insight report")
        except Exception as insight_error:
            insight_report = None
            logs.append(f"Insight generation failed: {str(insight_error)}")

        return WorkflowResponse(
            analysis_result=analysis_result,
            insight_report=insight_report,
            logs=logs,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            os.remove(temp_file_path)