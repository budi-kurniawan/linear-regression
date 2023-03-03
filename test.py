import unittest
import json
import main
from simple_linear_regr import SimpleLinearRegression

class Test(unittest.TestCase):
    def setUp(self):
        main.app.testing = True
        self.client = main.app.test_client()
    
    def test_batch(self):
        data = [10, 15, 20]
        response = self.client.post('/batch', data=json.dumps(data), content_type="application/json")
        content = response.data
        print(content)

        #self.assertEqual(content, 'Say something')
    
    def test_stream(self):
        data = 10
        response = self.client.post('/stream', data=json.dumps(data), content_type="application/json")
        content = response.data
        print(content)
