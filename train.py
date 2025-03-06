import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Load the trained model at startup


@app.get("/")
async def root():
    return {"message": "🎓 Welcome to the Student Grade Prediction API"}

@app.post("/predict/")
async def predict(x: int = Query(..., description="input x)"),
    y: int = Query(..., description="input y"),):
    z = x+y 
    print(f"z (x+y) =  {z}")
    return z