# Agentic AI Workflow Automation Platform

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![LLM](https://img.shields.io/badge/LLM-Groq%20%2B%20Llama-purple)
![Tests](https://img.shields.io/badge/Tests-Pytest-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

An AI-powered workflow platform that analyzes CSV datasets using deterministic data-processing tools and generates grounded business insights with an LLM.

The project demonstrates a practical pattern for building reliable AI applications: statistical computations are performed by deterministic tools, while the LLM is used only to summarize validated outputs into a structured insight report.

---

## Overview

Modern AI applications often fail when language models are asked to perform calculations, infer trends, or detect anomalies directly from raw data. This project addresses that problem by separating computation from explanation.

The platform first runs a deterministic analysis pipeline over an uploaded CSV file. It then passes the validated analysis result to an LLM, which generates a concise insight report based only on the computed outputs.

This makes the system more reliable, explainable, and suitable for real-world analytical workflows.

---

## Key Capabilities

- Upload and analyze CSV files
- Inspect dataset schema and column types
- Summarize missing values
- Apply basic data cleaning
- Generate descriptive statistics
- Detect anomalies using the IQR method
- Analyze numeric trends using linear regression slope
- Generate charts for numeric columns
- Produce structured LLM-generated insight reports
- Serve the workflow through a FastAPI backend
- Provide an interactive Streamlit UI
- Validate outputs with Pydantic schemas
- Test core workflow components with Pytest
- Evaluate workflow reliability using custom metrics

---

## System Architecture

```text
CSV File
   |
   v
Data Loading
   |
   v
Schema Inspection
   |
   v
Missing Value Analysis
   |
   v
Data Cleaning
   |
   v
Statistics + Trend Analysis + Anomaly Detection
   |
   v
Chart Generation
   |
   v
Validation Layer
   |
   v
LLM Insight Generation
   |
   v
FastAPI / Streamlit Output