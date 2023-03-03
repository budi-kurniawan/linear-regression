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

    print("load_model. abs path:", os.path.abspath(filename))

    model = joblib.load(open(filename, "rb"))
    print("load_model. ")
    print(type(model))

def load_model_from_file():
    print("loading from file")
    filename = "model.sav"
    print("load_model_from_file. abs path:", os.path.abspath(filename))
    m = None
    try:
        with open(filename, "rb") as f:
            m = joblib.load(f)
    except Exception as ex:
            print("exception:", ex)
    return m

@app.route("/", methods=["GET"])
def info():
    model2 = load_model_from_file()
    print('info(). type of model:' ,type(model2))
    if model2 is None:
        print("model2 is None")
    else:
        data = 5
        result = model2.predict(data)
        print("result: ", result)
    return Response("This is a linear regression microservice." + str(result))

@app.route("/stream", methods=["POST"])
def stream():
    data = request.get_json()
    print("stream called data is ", data)
    model2 = load_model_from_file()
    print('type of model:' ,type(model2))
    if model2 is None:
        print("model2 is None")
    else:
        result = model2.predict(data)
        print("result: ", result)
    return Response("This is /stream.")

@app.route("/batch", methods=["POST"])
def batch():
    data = request.get_json()
    print("batch called, data is ", data)
    return Response("This is /batch.")

if __name__=="__main__":
    load_model()
    app.run(host="127.0.0.1", port=5000, debug=True)