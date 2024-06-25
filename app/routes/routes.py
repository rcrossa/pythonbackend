
from flask import Blueprint

from app.views.views import index, getInformation, get_all_movies, get_movie, create_movie, update_movie, delete_movie

rout = Blueprint('rout', __name__)

rout.route('/', methods=['GET'])(index)
rout.route('/data', methods=['GET'])(getInformation)

rout.route('/', methods=['GET'])(index)
rout.route('/api/movies/', methods=['GET'])(get_all_movies)
rout.route('/api/movies/<int:movie_id>', methods=['GET'])(get_movie)
rout.route('/api/movies/', methods=['POST'])(create_movie)
rout.route('/api/movies/<int:movie_id>', methods=['PUT'])(update_movie)
rout.route('/api/movies/<int:movie_id>', methods=['DELETE'])(delete_movie)