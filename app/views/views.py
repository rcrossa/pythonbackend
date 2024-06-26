from flask import jsonify, request
from app.models.movie import Movie
def index():
    return 'Hello World!'

def getInformation():
    prueba = [{"id": 1, "name": "Juan"}, {"id": 2, "name": "Pedro"}]
    return jsonify(prueba)



def index():
    return '<h1>Hola mundo con flask 🐍</h1>'

def get_all_movies():
    movies = Movie.get_all()
    list_movies = [movie.serialize() for movie in movies]
    return jsonify(list_movies)

def create_movie():
    #recepcionando los datos enviados en la peticion en formato JSON
    data = request.json
    print(data)
    new_movie = Movie(
        title=data['title'],
        director=data['director'],
        rating=data['rating'],
        release_date=data['release_date'],
        banner=data['banner']
    )
    new_movie.save()
    return jsonify({'message':'Pelicula creada con exito'}), 201
    
def update_movie(movie_id):
    movie = Movie.get_by_id(movie_id)
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404
    data = request.json
    movie.title = data['title']
    movie.director = data['director']
    movie.rating = data['rating']
    movie.release_date = data['release_date']
    movie.banner = data['banner']
    movie.save()
    return jsonify({'message': 'Movie updated successfully'})

def get_movie(movie_id):
    movie = Movie.get_by_id(movie_id)
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404
    return jsonify(movie.serialize())

def delete_movie(movie_id):
    movie = Movie.get_by_id(movie_id)
    if not movie:
        return jsonify({'message': 'Movie not found'}), 404
    movie.delete()
    return jsonify({'message': 'Movie deleted successfully'})