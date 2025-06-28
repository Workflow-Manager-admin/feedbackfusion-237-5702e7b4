"""
Module for feedback-related services, including optional AI-based sentiment analysis
and summarization.
"""

from .models import add_feedback, get_all_feedback
from typing import Optional, List, Dict


def analyze_sentiment(message: str) -> Optional[str]:
    """
    Optionally analyze and return sentiment label of the message.
    Here, returns None or 'positive'/'negative'/'neutral' (dummy).
    """
    # Dummy logic for now
    if "good" in message.lower():
        return "positive"
    elif "bad" in message.lower():
        return "negative"
    else:
        return "neutral"


def summarize_message(message: str) -> Optional[str]:
    """
    Optionally provide a (dummy) summary for the message.
    """
    if len(message) <= 50:
        return None
    # Just a simple example; use real summarization API here as needed
    return message[:47] + "..."


# PUBLIC_INTERFACE
def submit_feedback(user: Optional[str], message: str, perform_ai: bool = True) -> int:
    """Save feedback, optionally process AI tasks."""
    sentiment, summary = None, None
    if perform_ai:
        sentiment = analyze_sentiment(message)
        summary = summarize_message(message)
    new_id = add_feedback(user, message, sentiment, summary)
    return new_id


# PUBLIC_INTERFACE
def list_feedback() -> List[Dict]:
    """Retrieve all feedback records."""
    return get_all_feedback()
