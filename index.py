from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from app.routes.routes import route
from static import swagger

app = Flask(__name__)


app.register_blueprint(swagger.swagger_ui_blueprint, url_prefix=swagger.SWAGGER_URL)
app.register_blueprint(route)

CORS(app)
if __name__ == '__main__':
    app.run(debug=True)