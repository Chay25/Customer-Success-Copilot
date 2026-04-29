from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="AI Customer Success Copilot",
    description="AI/ML system for customer sentiment, intent, churn risk, and automated response recommendations.",
    version="1.0.0"
)

app.include_router(router, prefix="/api", tags=["Customer Success AI"])


@app.get("/")
def health_check():
    return {
        "status": "running",
        "project": "AI Customer Success Copilot",
        "message": "Visit /docs to test the API."
    }
