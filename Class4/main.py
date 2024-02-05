from fastapi import FastAPI

# FastAPI 인스턴스 생성
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}