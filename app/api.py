from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from model import xgb_iris_model

modelo: xgb_iris_model = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global modelo

    modelo = xgb_iris_model()

    yield

    del modelo

app = FastAPI(lifespan=lifespan)

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


class PredictOutput(BaseModel):
    prediccion: list[str]

@app.post("/predict")
def predict(input_data: list[PredictInput]) -> PredictOutput:

    processed_data = list(map(lambda x: x.model_dump(mode="json"), input_data))
    processed_data = modelo.transformar_caracteristicas(processed_data)
    
    return JSONResponse({"prediccion": modelo.predecir(processed_data)}, status_code=200)
