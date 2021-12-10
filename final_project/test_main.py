from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_get_home():
    response = client.get("/home/test1")
    assert response.status_code == 200
    assert response.template.name == 'index.html'
    assert "classes" in response.context

def test_get_courses():
    response = client.get("/course-list/test1")
    assert response.status_code == 200
    assert response.template.name == 'course-list.html'
    assert "courses" in response.context