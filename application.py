from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler


application = Flask(__name__)

# Import linear regression model and standard scaler 
try:
    ridge_model = joblib.load(open(r'models\linear_regression_model.pkl', 'rb'))
    standard_scaler = joblib.load(open(r'models\scaler.pkl', 'rb'))
except Exception as e:
    print(f"Error loading model files: {e}")
    raise

@application.route("/")
def hello_world():
    return render_template('index.html')

@application.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
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
            return render_template('home.html', error_message=error_message, results=None)
        except Exception as e:
            print(f"Error retrieving form data: {e}")
            error_message = "An unexpected error occurred while processing your request. Please try again."
            return render_template('home.html', error_message=error_message, results=None)

        try:
            new_data_scaled = standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
            result = ridge_model.predict(new_data_scaled)
            return render_template('home.html', results=result[0], error_message=None)
        except Exception as e:
            print(f"Prediction error: {e}")
            error_message = "An error occurred during the prediction process."
            return render_template('home.html', error_message=error_message, results=None)

    return render_template('home.html', results=None, error_message=None)

if __name__ == "__main__":
    application.run(host="0.0.0.0", debug=True)