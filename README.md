# Forest Fire Prediction

## Description
This project is a Flask web application that predicts forest fire intensity using a machine learning model. It provides a simple interface to input weather parameters and get a prediction.

## Features
- Predicts forest fire intensity based on input weather parameters.
- Provides a simple web interface for predictions.

## How to Use
1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application:**
   ```bash
   python application.py
   ```
4. **Access the application:**
   Open your web browser and go to `http://localhost:5000` (or the address shown in the terminal).
5. **Make Predictions:**
   - Navigate to the `/predictdata` endpoint (or follow links in the UI).
   - Input the required weather parameters into the form.
   - Submit the form to get the forest fire prediction.

## Data
The model was trained on the Algerian Forest Fires Dataset. The dataset files are:
- `data/Algerian_forest_fires_cleaned_dataset.csv`
- `data/Algerian_forest_fires_dataset_UPDATE.csv`

The features used for prediction include: Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, and Region.

## Model
The prediction model is a Ridge Regression model.
- The trained model is saved in `models/ridge.pkl`.
- A StandardScaler, saved in `models/scaler.pkl`, is used for preprocessing the input data.

## Dependencies
This project uses the following libraries, as listed in `requirements.txt`:
- Flask
- numpy
- pandas
- scikit-learn

## Project Structure
- `application.py`: Main Flask application file.
- `templates/`: Contains HTML templates for the web interface.
  - `home.html`: The main page for making predictions.
  - `index.html`: Landing page (if any, or could be the same as `home.html`).
- `models/`: Stores the trained machine learning model and scaler.
  - `ridge.pkl`: The trained Ridge Regression model.
  - `scaler.pkl`: The StandardScaler object for data preprocessing.
- `data/`: Contains the dataset files used for training and reference.
  - `Algerian_forest_fires_cleaned_dataset.csv`: Cleaned dataset.
  - `Algerian_forest_fires_dataset_UPDATE.csv`: Original/updated dataset.
- `notebook/`: Jupyter notebooks for model training, exploration, and analysis.
  - `EDA_FE_Algerian_Forest_Fire_Dataset.ipynb`: Notebook for Exploratory Data Analysis and Feature Engineering.
  - `Model_Training_Algerian_Forest_Fire_Dataset.ipynb`: Notebook for training the prediction model.
- `requirements.txt`: Lists all Python dependencies for the project.
- `README.md`: This file, providing an overview and instructions for the project.
