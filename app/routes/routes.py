
from flask import Blueprint

from app.views.views import index, getInformation

route = Blueprint('rout', __name__)

route.route('/', methods=['GET'])(index)
route.route('/data', methods=['GET'])(getInformation)