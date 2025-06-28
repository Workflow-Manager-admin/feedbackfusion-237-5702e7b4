"""
resume.py

Implements dummy/stub logic for resume matching.
"""

from typing import Dict, Any


# PUBLIC_INTERFACE
def match_resume(resume_text: str, job_description: str) -> Dict[str, Any]:
    """
    Returns a stubbed resume-job match score and highlights.
    Args:
        resume_text (str): The resume text to evaluate.
        job_description (str): The job description.
    Returns:
        Dict[str, Any]: Match score and highlights (stub).
    """
    # Dummy logic: always returns 72% match and static highlights
    score = 72
    highlights = [
        {"section": "Experience", "reason": "Relevant job titles"},
        {"section": "Skills", "reason": "Python, Flask, SQL match"},
    ]
    return {
        "matched": True,
        "score": score,
        "highlights": highlights,
        "message": "Stubbed match logic"
    }
