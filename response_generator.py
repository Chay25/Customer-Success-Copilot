def generate_reply(sentiment: str, intent: str, urgency: str, churn_score: int) -> str:
    """Generate a professional customer success response template."""

    if churn_score >= 75:
        return (
            "Thank you for bringing this to our attention. I understand how frustrating this experience has been, "
            "and I want to make sure this is handled with priority. I am escalating this issue to our senior support team "
            "and we will follow up with a clear resolution plan as soon as possible."
        )

    if intent == "Upgrade Interest":
        return (
            "Thank you for your interest. Based on what you shared, an upgraded plan or add-on feature may be a good fit. "
            "I would be happy to walk you through the best option based on your current needs."
        )

    if sentiment == "Negative":
        return (
            "Thank you for sharing this feedback. I understand your concern, and our team will review the issue carefully. "
            "We appreciate your patience while we work toward a solution."
        )

    return (
        "Thank you for reaching out. We reviewed your message and will be happy to help. "
        "Our team will guide you with the next best step."
    )
