from pydantic import BaseModel, Field


class CustomerMessage(BaseModel):
    customer_id: str = Field(..., example="CUST-1042")
    message: str = Field(..., example="I am frustrated because my issue is still not fixed. I may cancel soon.")


class AnalysisResult(BaseModel):
    customer_id: str
    sentiment: str
    intent: str
    urgency: str
    churn_risk_score: int
    upsell_opportunity: bool
    recommended_action: str
    suggested_reply: str
