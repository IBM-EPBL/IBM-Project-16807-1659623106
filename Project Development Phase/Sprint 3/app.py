import os
import requests
from flask import Flask, request, render_template, redirect, url_for
import pickle
# from cloudant.client import Cloudant

filename = 'Multiple_Linear_Regression.pkl'

regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()

    if request.method == 'POST':
        #gre_score = request.form[gre]
        #toefl_score = request.form[tofl]
        #university_rating = request.form[rating]
        #sop = request.form[sop]
        #lor = request.form[lor]
        #cgpa = request.form[cgpa]
        #research = request.form[research]

        gre_score = int(request.form['gre'])
        toefl_score = int(request.form['tofl'])
        university_rating= int(request.form['rating'])
        sop = float(request.form['sop'])
        lor = float(request.form['lor'])
        cgpa = float(request.form['cgpa'])
        research = int(request.form['research'])


        my_prediction = int(regressor.predict(data)[0])
	
    #return render_template('result.html') # the name of another html document


if __name__ == "__main__":
    app.run(debug=True)