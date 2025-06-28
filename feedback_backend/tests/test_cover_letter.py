import pytest
from app import app as flask_app


@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client


def test_cover_letter_success(client):
    payload = {
        "resume_text": "Experienced developer.",
        "job_description": "Software engineer opening"
    }
    response = client.post("/cover-letter", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert "cover_letter" in data
    assert "message" in data
    assert isinstance(data["cover_letter"], str)
    assert data["cover_letter"].startswith("Dear")


def test_cover_letter_missing_resume_text(client):
    payload = {"job_description": "Job"}
    response = client.post("/cover-letter", json=payload)
    assert response.status_code == 400


def test_cover_letter_missing_job_description(client):
    payload = {"resume_text": "Some resume"}
    response = client.post("/cover-letter", json=payload)
    assert response.status_code == 400


def test_cover_letter_empty_input(client):
    response = client.post("/cover-letter", json={})
    assert response.status_code == 400
