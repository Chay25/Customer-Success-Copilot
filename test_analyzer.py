from app.services.analyzer import analyze_customer_message


def test_churn_risk_high_for_cancellation():
    result = analyze_customer_message(
        "TEST-1",
        "I am frustrated and I may cancel because this is still not fixed."
    )
    assert result["churn_risk_score"] >= 75
    assert result["intent"] == "Cancellation Risk"


def test_upsell_detection():
    result = analyze_customer_message(
        "TEST-2",
        "I want to upgrade to premium automation features."
    )
    assert result["upsell_opportunity"] is True
