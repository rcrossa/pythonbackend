import os
from dotenv import load_dotenv
from models.films import Films  # Importa el modelo desde la nueva ruta
from models.user import User

load_dotenv()  # Carga las variables de entorno desde un archivo .env

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
