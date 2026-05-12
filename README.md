# Agentic AI Workflow Automation Platform

![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red)
![LLM](https://img.shields.io/badge/LLM-Groq%20%2B%20Llama-purple)
![Tests](https://img.shields.io/badge/Tests-Pytest-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

A portfolio-grade AI engineering project for automated CSV analysis using deterministic data tools and LLM-generated insights.

The system combines traditional data analysis with an LLM insight layer. Deterministic tools compute schema summaries, missing values, descriptive statistics, trend analysis, anomaly detection, and charts. A Groq-hosted open model then generates a structured business insight report grounded in those computed outputs.

## Why this project matters

This project demonstrates how to build reliable AI workflows where LLMs do not directly invent analysis. Instead, deterministic tools compute facts, and the LLM explains the validated outputs.

This design is relevant for:

- AI Engineer roles
- AI Agent Engineer roles
- Data Scientist roles
- AI Architect roles
- Quant/Data Analytics platform roles

## Features

- CSV upload and analysis
- Dataset schema inspection
- Missing-value summary
- Basic data cleaning
- Descriptive statistics
- IQR-based anomaly detection
- Deterministic trend analysis using linear regression slope
- Chart generation with Matplotlib
- Groq-based LLM insight generation
- FastAPI backend
- Streamlit frontend
- Pydantic response schemas
- Pytest test suite

## Evaluation Harness

The project includes an evaluation module for measuring workflow reliability.   

## Architecture

```text
CSV Upload
   |
   v
Data Loader
   |
   v
Schema Inspector -> Missing Value Analyzer -> Data Cleaner
   |
   v
Statistics Tool -> Trend Analyzer -> Anomaly Detector -> Chart Generator
   |
   v
Validation Layer
   |
   v
LLM Insight Agent
   |
   v
FastAPI / Streamlit Output
```

## Screenshots

Screenshots will be added for:

- Streamlit workflow UI
- FastAPI Swagger documentation
- Evaluation harness output

```text
screenshots/
├── streamlit-ui.png
├── fastapi-docs.png
└── evaluation-output.png
