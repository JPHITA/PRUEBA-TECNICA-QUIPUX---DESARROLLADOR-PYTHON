import os
from typing import Dict
import pandas as pd

from xgboost import XGBClassifier

class xgb_iris_model:
    def __init__(self):
        self.modelo: XGBClassifier = None
        self.clases: pd.Series = pd.Series(["setosa", "versicolor", "virginica"])

        self.cargar_modelo()

    def cargar_modelo(self, model_name = "xgboost_model.json"):
        self.modelo = XGBClassifier()

        self.modelo.load_model(os.path.join(os.getcwd(), "models", model_name))

        print("Modelo cargado")

    def transformar_caracteristicas(self, X: list[Dict[str, float]]):
        FEATURE_MAPPING = {
            "sepal_length": "sepal length (cm)",
            "sepal_width": "sepal width (cm)",
            "petal_length": "petal length (cm)",
            "petal_width": "petal width (cm)",
        }

        data = pd.DataFrame(X)
        data = data.rename(columns=FEATURE_MAPPING)

        return data

    def predecir(self, X):
        predicted = self.modelo.predict(X)

        return self.clases[predicted].to_list()
    