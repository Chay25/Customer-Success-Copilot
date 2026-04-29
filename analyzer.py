from textblob import TextBlob
from app.services.llm_service import generate_llm_reply

NEGATIVE_KEYWORDS = [
    "angry", "bad", "cancel", "cancellation", "frustrated", "issue", "problem",
    "not working", "terrible", "delay", "unhappy", "refund", "broken", "worst"
]

URGENT_KEYWORDS = [
    "urgent", "immediately", "asap", "today", "right now", "still not fixed",
    "multiple times", "three times", "again", "escalate"
]

BILLING_KEYWORDS = ["billing", "invoice", "charged", "payment", "refund", "price", "cost"]
TECH_KEYWORDS = ["error", "bug", "login", "not working", "device", "system", "app", "dashboard"]
UPSELL_KEYWORDS = ["upgrade", "premium", "more features", "advanced", "automation", "add-on", "additional"]
CANCEL_KEYWORDS = ["cancel", "switch", "leave", "terminate", "unsubscribe"]


def detect_sentiment(message: str) -> str:
    polarity = TextBlob(message).sentiment.polarity

    if polarity > 0.15:
        return "Positive"
    if polarity < -0.10:
        return "Negative"
    return "Neutral"


def detect_intent(message: str) -> str:
    text = message.lower()

    if any(keyword in text for keyword in CANCEL_KEYWORDS):
        return "Cancellation Risk"
    if any(keyword in text for keyword in BILLING_KEYWORDS):
        return "Billing Concern"
    if any(keyword in text for keyword in UPSELL_KEYWORDS):
        return "Upgrade Interest"
    if any(keyword in text for keyword in TECH_KEYWORDS):
        return "Technical Issue"
    if any(keyword in text for keyword in NEGATIVE_KEYWORDS):
        return "Complaint"

    return "General Support"


def detect_urgency(message: str) -> str:
    text = message.lower()

    if any(keyword in text for keyword in URGENT_KEYWORDS):
        return "High"
    if any(keyword in text for keyword in NEGATIVE_KEYWORDS):
        return "Medium"

    return "Low"


def calculate_churn_risk(message: str, sentiment: str, intent: str, urgency: str) -> int:
    text = message.lower()
    score = 20

    if sentiment == "Negative":
        score += 25
    if intent == "Cancellation Risk":
        score += 30
    if intent == "Billing Concern":
        score += 15
    if urgency == "High":
        score += 20
    if any(keyword in text for keyword in NEGATIVE_KEYWORDS):
        score += 10
    if "refund" in text or "not fixed" in text:
        score += 10

    return min(score, 100)


def detect_upsell(message: str, intent: str, sentiment: str) -> bool:
    text = message.lower()
    has_upgrade_language = any(keyword in text for keyword in UPSELL_KEYWORDS)

    return intent == "Upgrade Interest" or (sentiment == "Positive" and has_upgrade_language)


def recommend_action(intent: str, urgency: str, churn_score: int, upsell: bool) -> str:
    if churn_score >= 75:
        return "Escalate to senior support immediately and follow up within 24 hours."
    if upsell:
        return "Offer a short product demo or recommend the most relevant upgrade."
    if intent == "Billing Concern":
        return "Send the message to billing and confirm the customer account details."
    if intent == "Technical Issue":
        return "Create a support ticket and ask for logs or screenshots if needed."
    if urgency == "Medium":
        return "Reply with empathy and provide a clear next step."

    return "Handle through the standard customer-success workflow."


def analyze_customer_message(customer_id: str, message: str) -> dict:
    sentiment = detect_sentiment(message)
    intent = detect_intent(message)
    urgency = detect_urgency(message)
    churn_score = calculate_churn_risk(message, sentiment, intent, urgency)
    upsell = detect_upsell(message, intent, sentiment)
    action = recommend_action(intent, urgency, churn_score, upsell)
    reply = generate_llm_reply(message, intent, sentiment, urgency)

    return {
        "customer_id": customer_id,
        "sentiment": sentiment,
        "intent": intent,
        "urgency": urgency,
        "churn_risk_score": churn_score,
        "upsell_opportunity": upsell,
        "recommended_action": action,
        "suggested_reply": reply,
    }
