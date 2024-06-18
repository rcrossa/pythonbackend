from utils.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    birthdate = db.Column(db.Date, nullable=False)

    def __init__(self, nombre, apellido, password, email, country, birthdate):
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.email = email
        self.country = country
        self.birthdate = birthdate
    
    def serialize(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'password': self.password,
            'email': self.email,
            'country': self.country,
            'birthdate': self.birthdate.isoformat()
            # Agrega más campos si es necesario
        }