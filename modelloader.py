import joblib

from simple_linear_regr import SimpleLinearRegression

filename = "model.sav"
try:
    with open(filename, "rb") as f:
        m = joblib.load(f)
        result = m.predict(4)
        print(result)
        result = m.predict(([4],[5],[6],[10]))
        print(result)
except Exception as ex:
        print("exception:", ex)
