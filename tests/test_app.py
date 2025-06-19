import json
from src.app import app

def test_index():
    client = app.test_client()
    resp = client.get('/')
    data = json.loads(resp.data)
    assert data['status'] == 'ok'


def test_diagnostic_default():
    client = app.test_client()
    resp = client.get('/diagnostic')
    data = json.loads(resp.data)
    assert 'online' in data


def test_http_check_route():
    client = app.test_client()
    resp = client.get('/http_check?url=https://example.com')
    data = json.loads(resp.data)
    assert 'reachable' in data
