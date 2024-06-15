from flask import Flask
from app.views import *
from flask_swagger_ui import get_swaggerui_blueprint
from app.routes.routes import rout

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"
app = Flask(__name__)

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)
app.register_blueprint(rout)



if __name__ == '__main__':
    app.run(debug=True)