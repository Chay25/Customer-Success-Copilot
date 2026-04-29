"""Optional response generation layer.

The project can run without a paid API key. When OpenAI settings are not provided,
it returns a local template-based reply.
"""
from app.core.config import settings


def generate_llm_reply(customer_message: str, intent: str, sentiment: str, urgency: str) -> str:
    if settings.llm_provider.lower() != "openai" or not settings.openai_api_key:
        return _fallback_reply(intent, sentiment, urgency)

    try:
        from openai import OpenAI

        client = OpenAI(api_key=settings.openai_api_key)
        prompt = f"""
Write a short, professional customer-support reply.

Customer message: {customer_message}
Intent: {intent}
Sentiment: {sentiment}
Urgency: {urgency}

Keep the tone calm, helpful, and direct.
"""
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return _fallback_reply(intent, sentiment, urgency)


def _fallback_reply(intent: str, sentiment: str, urgency: str) -> str:
    if urgency == "High":
        return (
            "I’m sorry for the trouble. I understand this needs attention, "
            "and I’m escalating it so we can provide a clear update and next steps."
        )

    if intent == "Billing Concern":
        return (
            "Thanks for reaching out. I’ll review the billing details and help clarify "
            "the charge, adjustment, or next action needed."
        )

    if intent == "Upgrade Interest":
        return (
            "Thanks for your interest. I can share the best upgrade options based on "
            "your current needs and help you choose the right plan."
        )

    if sentiment == "Negative":
        return (
            "Thank you for sharing this. I understand your concern, and I’ll help move "
            "this toward the right next step."
        )

    return "Thanks for reaching out. I’ll review this and help you with the right next step."
