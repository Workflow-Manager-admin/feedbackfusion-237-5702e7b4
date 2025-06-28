"""
feedback_analysis.py

Provides dummy AI-like feedback sentiment and topics analysis.
"""

from typing import Dict, Any


# PUBLIC_INTERFACE
def analyze_feedback(feedback_text: str) -> Dict[str, Any]:
    """
    Returns dummy sentiment/tags for the submitted feedback.
    Args:
        feedback_text (str): Text to analyze.
    Returns:
        Dict: Analysis with sentiment and topic tags.
    """
    # Simple stub sentiment
    if "great" in feedback_text or "good" in feedback_text:
        sentiment = "positive"
    elif "bad" in feedback_text or "problem" in feedback_text:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    tags = []
    if "dashboard" in feedback_text.lower():
        tags.append("dashboard")
    if "AI" in feedback_text.upper():
        tags.append("AI")
    if not tags:
        tags = ["general"]

    return {
        "sentiment": sentiment,
        "tags": tags,
        "message": "Stubbed feedback analysis"
    }
