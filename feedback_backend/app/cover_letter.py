"""
cover_letter.py

Implements dummy logic for cover letter generation.
"""

from typing import Dict, Any


# PUBLIC_INTERFACE
def generate_cover_letter(resume_text: str, job_description: str) -> Dict[str, Any]:
    """
    Returns a dummy/generated cover letter (stub logic).
    Args:
        resume_text (str): The user's resume text.
        job_description (str): The target job description.
    Returns:
        Dict: Cover letter content.
    """
    # Dummy output
    content = (
        "Dear Hiring Manager,\n\n"
        "I am excited to apply for this opportunity. My experience in Python and Flask "
        "aligns well with your requirements. I am confident that my background would make me a "
        "valuable contribution to your team.\n\nSincerely,\nYour Name"
    )
    return {
        "cover_letter": content,
        "message": "Stubbed cover letter generated."
    }
