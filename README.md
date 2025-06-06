# 🔥 Forest Fire Prediction System

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-2.0%2B-green" alt="Flask Version">
  <img src="https://img.shields.io/badge/scikit--learn-1.0%2B-orange" alt="scikit-learn Version">
</div>

## 🌟 Overview
This project is an intelligent web application that predicts forest fire intensity using advanced machine learning techniques. It provides a user-friendly interface for environmental scientists, forest rangers, and researchers to make accurate predictions based on weather parameters.

## 🎯 Key Objectives
- 🔍 Predict forest fire intensity using machine learning
- 📊 Provide real-time predictions through a web interface
- 📈 Help in early warning and prevention of forest fires
- 🎯 Assist in resource allocation for fire management

## 🚀 Features
- 🌡️ Real-time fire intensity prediction
- 📱 User-friendly web interface
- 📊 Input validation and error handling
- 🔄 Instant prediction results
- 📈 Multiple ML models for accurate predictions

## 🛠️ Technology Stack
- **Backend**: Flask
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Frontend**: HTML, CSS

## 📋 Prerequisites
Before you begin, ensure you have:
- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone <repository_url>
cd forest-fire-prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
python application.py
```

### 4. Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

## 📊 Input Parameters
The model uses the following parameters for prediction:
- 🌡️ Temperature
- 💧 Relative Humidity (RH)
- 💨 Wind Speed (Ws)
- 🌧️ Rainfall
- 🔥 FFMC (Fine Fuel Moisture Code)
- 🌿 DMC (Duff Moisture Code)
- 📏 ISI (Initial Spread Index)
- 🔥 Classes (Fire/No Fire)
- 🌍 Region

## 📁 Project Structure
```
forest-fire-prediction/
├── application.py          # Main Flask application
├── models/                 # Trained models
│   ├── linear_regression_model.pkl  # Linear Regression model
│   └── scaler.pkl         # StandardScaler
├── templates/             # HTML templates
│   ├── home.html         # Prediction interface
│   └── index.html        # Landing page
├── data/                  # Dataset files
│   ├── Algerian_forest_fires_cleaned_dataset.csv
│   └── Algerian_forest_fires_dataset_UPDATE.csv
├── notebook/             # Jupyter notebooks
│   ├── EDA_FE_Algerian_Forest_Fire_Dataset.ipynb
│   └── Enhanced_Forest_Fire_Model_Training.ipynb
└── requirements.txt      # Project dependencies
```

## 📚 Dataset
The model is trained on the Algerian Forest Fires Dataset, which includes:
- Historical fire data
- Weather parameters
- Environmental conditions
- Fire intensity measurements

## 🤖 Machine Learning Models
The project implements and evaluates multiple machine learning models:
- Linear Regression
- Lasso Regression
- Ridge Regression
- ElasticNet
- Decision Tree
- Random Forest
- Gradient Boosting

Each model is evaluated using multiple metrics:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score
- Explained Variance

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors
- John Tojo - Initial work

## 🙏 Acknowledgments
- Algerian Forest Fires Dataset
- scikit-learn community
- Flask framework

---
<div align="center">
  <sub>Built with ❤️ for forest conservation</sub>
</div>
