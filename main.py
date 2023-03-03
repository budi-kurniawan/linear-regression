from flask import Flask, Response, jsonify, request
import os
import joblib
from simple_linear_regr import SimpleLinearRegression

app = Flask(__name__)

# assign model to a global variable so subsequent inferences won't require reload
model = None
def load_model():
    global model
    filename = "model.sav"
    model = joblib.load(open(filename, "rb"))
    print("load_model. ")
    print(type(model))

@app.route("/", methods=["GET"])
def info():
    data = 5
    result = model.predict(data)
    print("result for data: ", result)
    return Response("This is a linear regression microservice." + str(result))

@app.route("/stream", methods=["POST"])
def stream():
    #data = request.get_json()
    data = 50
    print("stream called data is ", data)
    result = model.predict(data)
    print("result: ", result)
    return Response("This is /stream. Result:" + str(result))

@app.route("/batch", methods=["POST"])
def batch():
    data = ([1], [20]) #request.get_json()
    print("batch called, data is ", data)
    result = model.predict(data)
    print("result: ", result)
    return Response("This is /batch. Result:" + str(result))

if __name__=="__main__":
    load_model()
    app.run(host="127.0.0.1", port=5000, debug=True)