from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

# Create FastAPI app
app = FastAPI(
    title="Student Performance Prediction API"
)

# Input schema
class StudentInput(BaseModel):
    weekly_self_study_hours: float
    attendance_percentage: float
    class_participation: float

# Home route
@app.get("/")
def home():
    return {
        "message": "API is running"
    }

# Prediction route
@app.post("/predict")
def predict(data: StudentInput):

    input_df = pd.DataFrame([{
        "weekly_self_study_hours":
            data.weekly_self_study_hours,

        "attendance_percentage":
            data.attendance_percentage,

        "class_participation":
            data.class_participation
    }])

    prediction = model.predict(input_df)[0]

    return {
        "predicted_score": round(float(prediction), 2)
    }