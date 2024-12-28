import os
from fastapi import FastAPI
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from src.pipeline.prediction import PredictionPipeline

text: str = "The quick brown fox jumps over the lazy dog."

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python app/main.py")
        return Response(content="Training completed successfully", status_code=200)
    except Exception as e:
        return Response(content=f"An error occurred: {str(e)}", status_code=500)

@app.post("/predict")
async def predict(text: str):
    try:
        pipeline = PredictionPipeline()
        summary = pipeline.predict(text)
        return Response(content=summary, status_code=200)
    except Exception as e:
        return Response(content=f"An error occurred: {str(e)}", status_code=500)
    

if __name__ == "__main__":
    uvicorn.run("app.app:app", host="127.0.0.1", port=8000, reload=True)