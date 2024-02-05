from pydantic import BaseModel

# Input schema
class PredictIn(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Output schema
class PredictOut(BaseModel):
    iris_class: int