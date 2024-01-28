# tests/test_main.py

import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to the funny app!' in response.data

def test_random_joke(client):
    response = client.get('/random_joke')
    assert response.status_code == 200
    assert any(joke.encode() in response.data for joke in app.jokes)
