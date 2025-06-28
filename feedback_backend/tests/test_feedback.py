import pytest
from app import app as flask_app


@pytest.fixture
def client():
    with flask_app.test_client() as client:
        yield client


def test_analyze_feedback_success_positive(client):
    payload = {"feedback_text": "The dashboard is GREAT and the AI WORKS."}
    response = client.post("/analyze-feedback", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert "sentiment" in data
    assert data["sentiment"] == "positive"
    assert "tags" in data and isinstance(data["tags"], list)
    assert "dashboard" in (t.lower() for t in data["tags"])


def test_analyze_feedback_success_negative(client):
    payload = {"feedback_text": "A major problem with this project."}
    response = client.post("/analyze-feedback", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["sentiment"] == "negative"


def test_analyze_feedback_success_neutral(client):
    payload = {"feedback_text": "No strong opinion."}
    response = client.post("/analyze-feedback", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["sentiment"] == "neutral"


def test_analyze_feedback_missing_feedback_text(client):
    response = client.post("/analyze-feedback", json={})
    assert response.status_code == 400


def test_analyze_feedback_empty_feedback_text(client):
    payload = {"feedback_text": ""}
    response = client.post("/analyze-feedback", json=payload)
    assert response.status_code == 400
