"""
Tests for the Rick and Morty Characters Service
"""
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_healthcheck(client):
    """Test the healthcheck endpoint"""
    response = client.get('/healthcheck')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['status'] == 'healthy'
    assert json_data['message'] == 'The service is running!'