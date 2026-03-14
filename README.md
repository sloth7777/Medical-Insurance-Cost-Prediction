# 🩺Medical Insurance Cost Prediction

## 📊Overview

This project predicts medical insurance charges based on personal and health-related attributes such as age, BMI, smoking status, and region.
The model is trained using machine learning techniques and deployed through a simple web interface.

The goal is to estimate insurance costs and analyze which factors significantly influence medical expenses.

### Dataset

The dataset contains the following features:

- Age – Age of the individual
- Sex – Gender of the individual
- BMI – Body Mass Index
- Children – Number of dependents covered by insurance
- Smoker – Smoking status (Yes/No)
- Region – Residential region in the US
- Charges – Individual medical insurance cost (Target Variable)

### 📈Exploratory Data Analysis (EDA)

Key insights from the dataset:

- Smoking status is the most influential factor affecting insurance charges.
- Smokers incur significantly higher medical costs compared to non-smokers.
- Individuals with high BMI and smoking habits tend to have the highest insurance expenses.
- Age shows a positive relationship with insurance charges.
- Region has minimal impact on insurance costs.


### 📉Visualization techniques used:

- Box plots
- Violin plots
- Scatter plots
- Regression plots

### Machine Learning Model

Algorithms evaluated:

- Linear Regression

- Random Forest Regressor

Random Forest performed better due to its ability to capture non-linear relationships between variables.

### Evaluation metrics used:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

### 💻Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Flask
- Render
- Spline

### 🚀Model Deployment

The trained model is deployed using Flask, allowing users to input parameters through a web interface and receive predicted insurance costs. 

https://medical-insurance-cost-prediction-b6d0.onrender.com

## Author

Shristi Singh
