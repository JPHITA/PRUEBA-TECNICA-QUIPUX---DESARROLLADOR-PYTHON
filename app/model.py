import os

from xgboost import XGBClassifier

class xgb_model:
    def __init__(self):
        self.model: XGBClassifier = None

        self.cargar_modelo()

    def cargar_modelo(self, model_name = "xgboost_model.json"):
        self.model = XGBClassifier()

        self.model.load_model(os.path.join(os.getcwd(), "models", model_name))

        print("Modelo cargado")

    def predecir(self, X):
        return self.model.predict(X)