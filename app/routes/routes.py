
from flask import Blueprint

from app.views.views import index, getInformation

rout = Blueprint('rout', __name__)

rout.route('/', methods=['GET'])(index)
rout.route('/data', methods=['GET'])(getInformation)