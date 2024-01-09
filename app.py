from flask import flask, render_template, request
import pickle
import numpy as np

app = flask(__name__)

model = pickle.load(open("()"))

@app route('/predict'. methods = ['POST'])
def home():
    tenure = request.form['a']
    PS = request.form['a']
    C = request.form['a']
    PB = request.form['a']
    PM = request.form['a']
    MC = request.form['a']
    array = np.array([(tenure, PS, C,PB, PM, MC)])
    pred = model.predict(array)
    return render_template("hasil.html", data = pred)

if__name__ == "__main__";
app.run(debug = True)