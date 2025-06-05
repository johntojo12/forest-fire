from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)

#import ridhe regressor and standard scaler pickle
ridge_model=pickle.load(open('models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

@application.route("/")
def hello_world():
    return render_template('index.html')

@application.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        try:
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Ws = float(request.form.get('Ws'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            Classes = float(request.form.get('Classes'))
            Region = float(request.form.get('Region'))
        except ValueError:
            error_message = "Invalid input. Please ensure all fields are numeric and provided."
            return render_template('home.html', error_message=error_message)
        except Exception as e: # Catch any other unexpected errors during form data retrieval
            print(f"Error retrieving form data: {e}") # Log for debugging
            error_message = "An unexpected error occurred while processing your request. Please try again."
            return render_template('home.html', error_message=error_message)

        try:
            new_data_scaled=standard_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
            result=ridge_model.predict(new_data_scaled)
            return render_template('home.html',results=result[0])
        except Exception as e:
            print(f"Prediction error: {e}") # Log for debugging
            error_message = "An error occurred during the prediction process."
            return render_template('home.html', error_message=error_message)

    else: # GET request
        return render_template('home.html')

if __name__=="__main__":
    application.run(host="0.0.0.0")