from flask import Flask, render_template, redirect, url_for

from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import joblib
import tensorflow as tf


import pickle
with open("customer_pickle_model", 'rb') as f:
    pm = pickle.load(f)
#with open("model_pickle", 'rb') as f:
#    pm = pickle.load(f)
app = Flask(__name__)
#model = joblib.load(r"model (1).z")
@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/predict', methods = ["POST"])
def predict():
    # Get the values from the form
    input1 = int(request.form.get('input1'))
    print(input1)
    input2 = int(request.form.get('input2'))
    print(input2)
    input3 = int(request.form.get('input3'))
    print(input3)
    input4 = int(request.form.get('input4'))
    print(input4)
    pred = pm.predict([[input1, input2, input3, input4]])
    if pred>50:
        prediction = "WILL PURCHASE"
    else:
        prediction = "WILL NOT PURCHASE"
        
    return render_template('index.html', prediction_text=f"CUSTOMER {prediction} THE PRODUCT")

if __name__=="__main__":
    app.run(debug=True)