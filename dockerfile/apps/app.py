from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!"

@app.route('/predict')
def predict():
	 #use entries from the query string here but could also use json
     studytime = request.args.get('studytime')
     absences = request.args.get('absences')
     goout = request.args.get('goout')
     dalc = request.args.get('Dalc')
     G1 = request.args.get('G1')
     G2 = request.args.get('G2')


     data = [[studytime],[absences],[dalc],[goout],[G1],[G2]]
     query_df = pd.DataFrame({ 'studytime' : pd.Series(studytime) ,'goout' : pd.Series(goout),'Dalc' : pd.Series(dalc), 
     'absences' : pd.Series(absences) ,'G1' : pd.Series(G1), 'G2' : pd.Series(G2)
    })
     prediction = clf.predict(query_df)
     return jsonify(np.asscalar(prediction))     

if __name__ == '__main__':
    clf = joblib.load('/apps/model1.pkl')
    app.run(host="0.0.0.0", debug=True)