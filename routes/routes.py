from flask import Blueprint, render_template, request, jsonify
from views.views import index, getInformation
from utils.db import db
from models.user import User
from models.films import Films
from datetime import datetime

home_blueprint = Blueprint('home', __name__)
register_user = Blueprint('register', __name__)
example1_blueprint = Blueprint('example_1', __name__)
example2_blueprint = Blueprint('example_2', __name__)
films_blueprint = Blueprint('films', __name__)
films_blueprint_all = Blueprint('films_all', __name__)
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

@register_user.route('/registro')
def register():
        return render_template('register.html')
    
@films_blueprint.route('/newmovie', methods=['POST'])
def new():
        try:
            # Imprime el contenido recibido para depuración
            print("Request received:", request.data)
            data = request.get_json(force=True)  # Usa get_json para asegurar que se procesa el JSON

            # Imprime los datos convertidos
            print("Parsed JSON:", data)

            # Verifica que data es un diccionario
            if not isinstance(data, dict):
                raise ValueError("Invalid JSON data")

            title = data['title']
            director = data['director']
            rating = data['rating']
            release_date_str = data['release_date']
            release_date = datetime.strptime(release_date_str, '%Y-%m-%d').date()
            print(f"releaseDate_str: {release_date_str} (type: {type(release_date_str)})")


            # Crear un nueva pelicula
            new_film = Films(title, director, rating, release_date=release_date)
            
            # Añadir y guardar el nuevo usuario en la base de datos
            db.session.add(new_film)
            db.session.commit()

            # Devolver la respuesta serializada
            return jsonify(new_film.serialize()), 201
        except Exception as e:
            print(f'Error: {e}')
            return jsonify({"error": str(e)}), 400


@films_blueprint_all.route('/all', methods=['GET'])
def films_all():
    try:
        # Obtiene todas las películas
        films = Films.query.all()
        
        # Comprobación de depuración
        if not films:
            return jsonify({'error': 'No films found'}), 404
        
        # Inicializa un diccionario para almacenar las películas serializadas
        films_dict = {}
        
        # Serializa las películas y las agrega al diccionario
        for index, film in enumerate(films):
            films_dict[index] = film.serialize()
        
        # Retorna el diccionario de películas en formato JSON
        return jsonify(films_dict), 200
    except Exception as e:
        # Manejo de errores
        return jsonify({'error': str(e)}), 500


@films_blueprint.route('/crud-movies')
def crud_movies():
    return render_template('crud-movies.html')

@films_blueprint.route('/deletemovie/<int:id>', methods=['DELETE'])
def delete_movie(id):
    try:
        print(f"Request to delete movie with id: {id}")
        
        film = Films.query.get(id)
        if not film:
            abort(404, description="Resource not found")

        db.session.delete(film)
        db.session.commit()

        return jsonify({"message": "Movie deleted successfully"}), 200
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({"error": str(e)}), 400

@films_blueprint.route('/update')
def update():
    return "update films"   

@films_blueprint.route('/movie/<int:id>')
def get_movie(id):
    try:
        film = Films.query.get(id)
        if not film:
            return jsonify({"error": "Movie not found"}), 404

        movie_data = {
            'id': film.id,
            'title': film.title,
            'director': film.director,
            'rating': film.rating,
            'release_date': film.release_date,
        }
        return jsonify(movie_data), 200
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({"error": "Internal Server Error"}), 500

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