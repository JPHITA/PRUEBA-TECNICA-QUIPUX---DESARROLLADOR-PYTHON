# Prueba tecnica - desarrollador python - Quipux

## Instalación

#### requisitos previos

Es necesario tener instalado docker para correr la aplicacion, o si se va a correr en local, tener instalado python 3.12

#### Instalación con docker

1. Clonar el repositorio

   ```bash
   git clone https://github.com/JPHITA/PRUEBA-TECNICA-QUIPUX---DESARROLLADOR-PYTHON.git
   cd PRUEBA-TECNICA-QUIPUX---DESARROLLADOR-PYTHON
    ```

2. Construir la imagen de docker
   
   ```bash
    docker build -t fastapi-iris-app .
   ```

3. Correr el contenedor

   ```bash
    docker run -p 8000:8000 fastapi-iris-app
    ```

Con esto, la API debería estar disponible en http://localhost:8000.


## Estructura del proyecto

```plaintext
.
├── README.md
├── Dockerfile
├── requirements.txt
├── app
│   ├── api.py
│   └── model.py
├── models
│   └── xgboost_model.json
└── scripts
    └── train_model.ipynb
```

- `Dockerfile`: Archivo de configuración de Docker para contenerizar la API.
- `requirements.txt`: Archivo con las dependencias de python del proyecto.
- `app/api.py`: Contiene la definición de la API usando fastapi.
- `app/model.py`: Archivo que contiene una clase para abstraer las siguientes funciones:
  -  cargar el modelo preentrenado
  -  transformar las características
  -  hacer predicciones sobre el conjunto de datos.
- `models/xgboost_model.json`: Modelo entrenado.
- `scripts/train_model.ipynb`: Jupyter notebook con el entrenamiento del modelo.


## Uso de la API

#### endpoint `/predict`

**Método**: POST

**Descripción**: Este endpoint recibe las características de la flor (longitud y ancho del sépalo y pétalo) y devuelve las clases predecida por el modelo (puede ser varias flores a la vez).

**Entrada** (JSON):

```json
[
  {
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  },
  ...
]
```
**Salida** (JSON):

```json
{
    "prediccion": ["setosa", ...]
}
```

#### Ejemplo de uso con `curl`

```bash
curl -X POST http://localhost:8000/predict \
    -H "Content-Type: application/json" \
    -d '[{"sepal_length":1, "sepal_width": 1, "petal_length": 1, "petal_width": 1}, {"sepal_length":1, "sepal_width": 5, "petal_length": 5, "petal_width": 5}]'
```


---

Realizado por: Juan Nicolas Piedrahita Salas

17 de enero de 2025

jphita18@gmail.com