from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_get_home():
    response = client.get("/home/test1")
    assert response.status_code == 200
