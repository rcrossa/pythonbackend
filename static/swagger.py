from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)
def swagger(swagger_ui_blueprint,SWAGGER_URL):
    url_prefix=SWAGGER_URL
    return swagger_ui_blueprint, url_prefix