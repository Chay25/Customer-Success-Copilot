import pandas as pd
from fastapi import APIRouter
from app.models.schemas import CustomerMessage, AnalysisResult
from app.services.analyzer import analyze_customer_message

router = APIRouter()


@router.post("/analyze", response_model=AnalysisResult)
def analyze_message(payload: CustomerMessage):
    return analyze_customer_message(payload.customer_id, payload.message)


@router.get("/analyze-sample-data")
def analyze_sample_data():
    df = pd.read_csv("data/sample_tickets.csv")
    results = []

    for _, row in df.iterrows():
        results.append(analyze_customer_message(row["customer_id"], row["message"]))

    return {"total_records": len(results), "results": results}
