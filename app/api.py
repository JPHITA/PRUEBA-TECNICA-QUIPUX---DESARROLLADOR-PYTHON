from fastapi import FastAPI
from fastapi.responses import JSONResponse

from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],  # solo se permiten peticiones desde localhost ya que no se especifica en el prueba desde donde se va a probar la API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





class PredictInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(input_data: list[PredictInput]):
    
    return JSONResponse({"message": "prediccion"})
