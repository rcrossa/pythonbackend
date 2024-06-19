from flask import Blueprint, render_template, request
from flask import jsonify
from views.views import index, getInformation
from utils.db import db
from models.user import User
from datetime import datetime

home_blueprint = Blueprint('home', __name__)
register_user = Blueprint('register', __name__)
example1_blueprint = Blueprint('example_1', __name__)
example2_blueprint = Blueprint('example_2', __name__)
films_blueprint = Blueprint('films', __name__)
register_new_user = Blueprint('register_new_user', __name__)

@example1_blueprint.route("/data1", methods=["GET"])
def example_1():
    return index()

@example2_blueprint.route('/data2', methods=['GET'])
def example_2():
    return getInformation()



@home_blueprint.route('/')
def home():
    return render_template('index.html')

@register_user.route('/registro', methods=['GET'])
def register():
        return render_template('register.html')
    
@films_blueprint.route('/new')
def new():
    return "save"

@films_blueprint.route('/all')
def all():
    return render_template('crud-movies.html')

@films_blueprint.route('/delete')
def delete():
    return "delete films"

@films_blueprint.route('/update')
def update():
    return "update films"   

@register_new_user.route('/newuser', methods=['POST'])
def new_user():
    try:
        # Imprime el contenido recibido para depuración
        print("Request received:", request.data)
        data = request.get_json(force=True)  # Usa get_json para asegurar que se procesa el JSON

        # Imprime los datos convertidos
        print("Parsed JSON:", data)

        # Verifica que data es un diccionario
        if not isinstance(data, dict):
            raise ValueError("Invalid JSON data")

        nombre = data['firstname']
        apellido = data['lastname']
        email = data['email']
        password = data['password']
        country = data['country']
        birthdate_str = data['birthdate']
        birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d').date()

        # Crear un nuevo usuario
        new_user = User(nombre=nombre, apellido=apellido, password=password, email=email, country=country,birthdate=birthdate)
        
        # Añadir y guardar el nuevo usuario en la base de datos
        db.session.add(new_user)
        db.session.commit()

        # Devolver la respuesta serializada
        return jsonify(new_user.serialize()), 201
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({"error": str(e)}), 400