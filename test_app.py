import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_okresponse(client):
    response = client.get('/')
    assert response.status_code == 200

def test_hello_route(client):
    response = client.get('/')
    assert response.data.decode('utf-8') == "Hello, Dockerized Python App!"

def test_badresponse(client):
    response = client.get('/badresponse')
    assert response.status_code == 404