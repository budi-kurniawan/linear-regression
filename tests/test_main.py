import pytest
from main import app
import requests

def test_index_route():
    # response = app.test_client().get('/')
    response = requests.get('http://localhost:5000')
    print(response.text)
    # assert response.data.decode('utf-8') == 'Testing, Flask!'


def test_stream():
    response = requests.post('http://localhost:5000/stream')
    print(response.text)

def test_batch():
    # response = app.test_client().get('/')
    response = requests.post('http://localhost:5000/batch')
    print(response.text)
