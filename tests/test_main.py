from fastapi.testclient import TestClient
from app.main import app   # Import the app from the app package

client = TestClient(app)

def test_read_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, CI/CD!"}
