from pathlib import Path
from flask import Flask, jsonify, request
import joblib
from simple_linear_regr import SimpleLinearRegression
import numpy as np

app = Flask(__name__)

model = None
version = None

def load_model():
    global model
    filename = "model.sav"
    model = joblib.load(open(filename, "rb"))

def read_version():
    global version
    version = Path("VERSION").read_text()

@app.route("/", methods=["GET"])
def info():
    result = model.predict(100)[0]
    r = {"status": "OK", "message": f"linear regression v{version}. Model ready, x=100, y={result}"}
    return jsonify(r)

@app.route("/stream", methods=["POST"])
def stream():
    input_dict = request.get_json()
    data = input_dict["input"]
    result = model.predict(data)
    r = {"status": "OK", "message": "response for /stream", "result": str(result)}
    return jsonify(r)

@app.route("/batch", methods=["POST"])
def batch():
    input_dict = request.get_json()
    data = input_dict["input"]
    data = np.array(data).reshape((len(data), 1))
    result = model.predict(data)
    r = {"status": "OK", "message": "response for /batch", "result": str(result)}
    return jsonify(r)


if __name__=="__main__":
    read_version()
    load_model()
    port = 80 # 5000
    print(F"======== Starting linear regression API on port {port} =========")
    app.run(host="0.0.0.0", port=port, debug=True)