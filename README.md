# PredictAI — Student Performance Prediction API

A machine learning-powered REST API that predicts student academic performance from educational and behavioral data using **Random Forest Regression** and **FastAPI**.

The project demonstrates a complete ML workflow — from model training and data processing to serving real-time predictions through a REST API.

---

## 🚀 Features

* 🤖 Machine learning model for student score prediction
* 🌲 Random Forest Regression for prediction
* ⚡ FastAPI-based REST API
* 📊 Structured educational data processing
* 🔄 Real-time prediction through API requests
* 📦 Serialized model using Joblib
* 🧪 Interactive API testing with Swagger UI
* 📄 JSON-based request and response format
* 📓 Jupyter Notebook for model development and experimentation

---

## 🧠 How It Works

The application follows a simple machine learning prediction pipeline:

```text
Student Data
     │
     ▼
Feature Input
     │
     ▼
Trained Random Forest Model
     │
     ▼
Prediction
     │
     ▼
FastAPI REST API
     │
     ▼
JSON Response
```

The API receives information about a student's study habits, attendance, and class participation, then uses the trained model to estimate the student's total academic score.

---

## 📌 Input Features

The model uses the following features:

| Feature                   | Description                      |
| ------------------------- | -------------------------------- |
| `weekly_self_study_hours` | Weekly hours spent on self-study |
| `attendance_percentage`   | Student attendance percentage    |
| `class_participation`     | Level of classroom participation |

### Target Variable

```text
total_score
```

The model predicts the student's expected total score based on the input features.

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Random Forest Regression
* Pandas
* Matplotlib

### API Development

* FastAPI
* Uvicorn

### Model Persistence

* Joblib

### Development

* Jupyter Notebook
* Swagger UI

---

## 🔄 Machine Learning Workflow

The model development process follows these steps:

```text
Dataset
   ↓
Data Exploration
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Random Forest Regression
   ↓
Model Evaluation
   ↓
Model Serialization
   ↓
FastAPI Integration
   ↓
Real-Time Prediction
```

The trained model is saved as `model.pkl` and loaded by the API during prediction requests.

---

## 🌐 API Documentation

FastAPI automatically provides interactive API documentation through Swagger UI.

### Swagger UI

![API Documentation](screenshots/api-docs.png)

Once the application is running, open:

```text
http://127.0.0.1:8000/docs
```

Swagger allows you to test the prediction endpoint directly from your browser.

---

## 🔮 Prediction API

### POST `/predict`

The `/predict` endpoint accepts student information and returns the predicted academic score.

### Request

```json
{
  "weekly_self_study_hours": 16,
  "attendance_percentage": 85,
  "class_participation": 7
}
```

### Response

```json
{
  "predicted_score": 89.17
}
```

### Prediction Response

![Prediction Response](screenshots/prediction-response.png)

---

## 📂 Project Structure

```text
student-performance-prediction-api/
│
├── notebook/
│   └── Student_Performance_Prediction_Project.ipynb
│
├── screenshots/
│   ├── api-docs.png
│   └── prediction-response.png
│
├── app.py
├── train_model.py
├── model.pkl
├── student_performance.csv
├── README.md
└── .gitignore
```

---

## ⚙️ Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/asthasinghcs/student-performance-prediction-api.git
```

```bash
cd student-performance-prediction-api
```

### 2. Install Dependencies

```bash
pip install fastapi uvicorn scikit-learn pandas matplotlib joblib
```

### 3. Run the API

```bash
uvicorn app:app --reload
```

### 4. Open Swagger Documentation

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

You can then use Swagger UI to send prediction requests to the API.

---

## 🧪 Example Prediction

### Input

```json
{
  "weekly_self_study_hours": 16,
  "attendance_percentage": 85,
  "class_participation": 7
}
```

### Output

```json
{
  "predicted_score": 89.17
}
```

This demonstrates how structured student information is converted into a real-time machine learning prediction.

---

## 🤖 Model Information

### Algorithm

**Random Forest Regressor**

Random Forest combines multiple decision trees and averages their predictions to produce the final regression output.

### Input Features

```text
weekly_self_study_hours
attendance_percentage
class_participation
```

### Prediction Target

```text
total_score
```

### Model File

```text
model.pkl
```

The trained model is serialized using **Joblib** so that it can be loaded directly by the FastAPI application without retraining every time the server starts.

---

## 🎯 Project Goals

This project demonstrates practical experience with:

* Machine learning model development
* Regression problems
* Feature selection
* Model serialization
* REST API development
* FastAPI
* Real-time ML inference
* JSON request/response handling
* API documentation with Swagger

---

## 🚀 Future Improvements

Potential improvements include:

* Add additional student behavioral and academic features
* Perform advanced feature engineering
* Tune Random Forest hyperparameters
* Compare multiple regression algorithms
* Add model performance metrics
* Add input validation and better error handling
* Add authentication and API security
* Build a frontend prediction interface
* Deploy the API to a cloud platform
* Add automated model retraining

---

## 💡 Key Learning Areas

This project provides hands-on experience with the complete path from an ML model to a usable API:

```text
Machine Learning
      +
Model Serialization
      +
FastAPI
      +
REST APIs
      =
ML Prediction Service
```

It is particularly useful for understanding how a trained machine learning model can be integrated into a backend application and exposed as a real-time prediction service.

---

## 📜 License

This project is intended for educational and portfolio purposes.

---

## 👨‍💻 Project Summary

**PredictAI** is a lightweight machine learning serving project that combines **Scikit-learn** and **FastAPI** to expose a trained Random Forest regression model through a REST API.

It demonstrates the practical transition from **ML experimentation → trained model → model serialization → API deployment → real-time inference**.
