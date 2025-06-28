import pytest
from app import app as flask_app


@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client


def test_match_resume_success(client):
    payload = {
        "resume_text": "Senior Python developer with experience in Flask, SQL",
        "job_description": "Seeking backend developer skilled in Python, Flask, SQL"
    }
    response = client.post("/match-resume", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert "matched" in data
    assert "score" in data
    assert data["matched"] is True
    assert data["score"] == 72
    assert isinstance(data.get("highlights"), list)


def test_match_resume_missing_resume_text(client):
    payload = {
        "job_description": "Backend dev job"
    }
    response = client.post("/match-resume", json=payload)
    assert response.status_code == 400


def test_match_resume_missing_job_description(client):
    payload = {
        "resume_text": "Python developer profile"
    }
    response = client.post("/match-resume", json=payload)
    assert response.status_code == 400


def test_match_resume_empty_input(client):
    payload = {}
    response = client.post("/match-resume", json=payload)
    assert response.status_code == 400
