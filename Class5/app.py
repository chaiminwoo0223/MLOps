from fastapi import FastAPI
from schemas import PredictIn, PredictOut
import mlflow
import pandas as pd

# 모델 불러오기
def get_model():
    model = mlflow.sklearn.load_model(model_uri="./sk_model")
    return model
MODEL = get_model()

# FastAPI 인스턴스 생성
app = FastAPI()

# Predict(Create)
@app.post("/predict", response_model=PredictOut)
def predict(data: PredictIn) -> PredictOut:
    df = pd.DataFrame([data.dict()])
    pred = MODEL.predict(df).item()
    return PredictOut(iris_class=pred)