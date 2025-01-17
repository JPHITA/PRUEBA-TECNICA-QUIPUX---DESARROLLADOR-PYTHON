import os
from typing import Dict
import pandas as pd

from xgboost import XGBClassifier

class xgb_iris_model:
    """
    Clase para representar el modelo clasificador XGBoost para el conjunto de datos de Iris.

    Atributos
    ---------
    modelo : XGBClassifier
        El modelo clasificador XGBoost.
    clases : pd.Series
        Una Serie de pandas que contiene las etiquetas de clase para el conjunto de datos de Iris.
    """

    def __init__(self):
        self.modelo: XGBClassifier = None
        self.clases: pd.Series = pd.Series(["setosa", "versicolor", "virginica"])

        self.cargar_modelo()


    def cargar_modelo(self, model_name: str = "xgboost_model.json") -> None:
        """
        Carga el modelo XGBoost preentrenado desde un archivo especificado.

        Args:
            model_name (str): El nombre del archivo del modelo a cargar. Por defecto es "xgboost_model.json".
        Returns:
            None
        """
        
        self.modelo = XGBClassifier()

        self.modelo.load_model(os.path.join(os.getcwd(), "models", model_name))

        print("Modelo cargado")



    def transformar_caracteristicas(self, X: list[Dict[str, float]]) -> pd.DataFrame:
        """
        Transforma las características para que coincidan con el formato esperado por el modelo.

        Args:
            X (list[Dict[str, float]]): Una lista de diccionarios donde cada diccionario representa una muestra con los nombres de las características como claves y sus valores correspondientes.

        Returns:
            pd.DataFrame: Un DataFrame de pandas con los nombres de las características transformados.
        """

        FEATURE_MAPPING = {
            "sepal_length": "sepal length (cm)",
            "sepal_width": "sepal width (cm)",
            "petal_length": "petal length (cm)",
            "petal_width": "petal width (cm)",
        }

        data = pd.DataFrame(X)
        data = data.rename(columns=FEATURE_MAPPING)

        return data
    


    def predecir(self, X: pd.DataFrame) -> list[str]:
        """
        Predice las etiquetas de clase para los datos de entrada proporcionados.

        Args:
            X (pd.DataFrame): Los datos de entrada para los cuales predecir las etiquetas de clase.

        Returns:
            list[str]: Una lista de etiquetas de clases predichas.
        """

        predicted = self.modelo.predict(X)

        return self.clases[predicted].to_list()
    