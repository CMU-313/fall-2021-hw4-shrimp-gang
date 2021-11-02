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
    required_params = ['studytime', 'absences', 'goout', 'Dalc', 'G1', 'G2']
    for param in required_params:
        #checks for missing parameter
        if not param in request.args:
            return "Missing parameter: " + param, 400

        #checks for wrong parameter type
        if request.args.get(param, type=float) is None:
            return f"Invalid type for {param}. Expected int/float.", 400

    studytime = request.args.get('studytime', type = int)
    absences = request.args.get('absences', type = int)
    goout = request.args.get('goout', type = int)
    dalc = request.args.get('Dalc', type = int)
    G1 = request.args.get('G1', type = float)
    G2 = request.args.get('G2', type = float)


    data = [[studytime],[absences],[dalc],[goout],[G1],[G2]]
    query_df = pd.DataFrame({ 'studytime' : pd.Series(studytime) ,'goout' : pd.Series(goout),'Dalc' : pd.Series(dalc), 
     'absences' : pd.Series(absences) ,'G1' : pd.Series(G1), 'G2' : pd.Series(G2)
    })
    prediction = clf.predict(query_df)
    return jsonify(np.asscalar(prediction))  

if __name__ == '__main__':
    clf = joblib.load('/apps/model1.pkl')
    app.run(host="0.0.0.0", debug=True)