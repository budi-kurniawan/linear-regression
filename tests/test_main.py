import pytest
import requests
# from main import app
# from simple_linear_regr import SimpleLinearRegression

def test_index_route():
    # using app.test_client().get('/') won't work because it will create a new instance of the endpoint
    print("test index")
    # response = requests.get('http://localhost:5000')
    # assert response.status_code == 200
    

# def test_stream():
#     input = 100
#     headers = {"Content-type": "application/json"}
#     response = requests.post('http://localhost:5000/stream', json={"input": input},
#                              headers=headers)
#     assert response.status_code == 200
#     print(response.text)

# def test_batch():
#     input = (100, 120, 140)
#     headers = {"Content-type": "application/json"}
#     response = requests.post('http://localhost:5000/batch', json={"input": input},
#                              headers=headers)
#     assert response.status_code == 200
#     print(response.text)
