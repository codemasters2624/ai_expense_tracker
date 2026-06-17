from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "UP"

def test_ready_check():
    response = client.get("/ready")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "READY"

    assert data["database"] == "UP"