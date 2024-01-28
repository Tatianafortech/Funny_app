# tests/test_funny_app.py

import pytest
from funny_app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the funny app!' in response.data
    print("Test index function executed successfully!")

def test_random_joke(client):
    response = client.get('/random_joke')
    assert response.status_code == 200
    assert any(joke.encode() in response.data for joke in app.jokes)
    print("Test random_joke function executed successfully!")
