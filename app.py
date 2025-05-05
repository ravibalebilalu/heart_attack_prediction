from flask import Flask
import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("./pickle_models/model.pkl","rb"))
scaler =  pickle.load(open("./pickle_models/scaler.pkl","rb"))

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict",methods=['POST'])
def predict():
    data =  [float(x) for x in request.form.values()]
    new_data = scaler.transform(np.array(data).reshape(1,-1))
    pred = model.predict(new_data)
    return render_template("home.html",result = pred[0])


if __name__ == "__main__":
    app.run(debug=True)