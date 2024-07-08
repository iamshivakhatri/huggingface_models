from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel

class ScoringItem(BaseModel):
    YearsAtCompany: float
    EmployeeSatisfaction: float
    Position: str
    Salary: int

# Load the model
with open("rfmodel.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

@app.post("/")
async def root(item: ScoringItem):
    # Convert ScoringItem to DataFrame
    df = pd.DataFrame([item.model_dump().values()], columns=item.model_dump().keys())

    # Make prediction
    yhat = model.predict(df)

    return {"Prediction": int(yhat)}
