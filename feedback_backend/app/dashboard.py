"""
dashboard.py

Dummy job dashboard data and stub for job addition.
"""

from typing import List, Dict, Any


# This would be replaced by DB or actual job API in production
MOCK_JOBS = [
    {
        "id": 1,
        "title": "Python Backend Developer",
        "company": "Acme Corp",
        "description": "Work on modern Flask APIs.",
        "location": "Remote"
    },
    {
        "id": 2,
        "title": "AI Solutions Engineer",
        "company": "Beta AI",
        "description": "Develop AI-driven applications.",
        "location": "Hybrid"
    }
]


# PUBLIC_INTERFACE
def list_jobs() -> List[Dict[str, Any]]:
    """Return a list of mock jobs."""
    return MOCK_JOBS


# PUBLIC_INTERFACE
def add_job(job: Dict[str, Any]) -> Dict[str, Any]:
    """
    Adds a job to the mock list (does not persist).
    Args:
        job (dict): The job dictionary with required fields.
    Returns:
        Dict: Confirmation and the created job data.
    """
    mock_id = max(j["id"] for j in MOCK_JOBS) + 1 if MOCK_JOBS else 1
    job_with_id = dict(job)
    job_with_id["id"] = mock_id
    MOCK_JOBS.append(job_with_id)
    return {"message": "Job added (mock, not persisted)", "job": job_with_id}
