from flask import Flask
from routes.routes import example1_blueprint, example2_blueprint, home_blueprint, register_user,register_new_user, films_blueprint,films_blueprint_all
from swagger_config import swagger
from utils.db import db # 

from config.config import Config  # Importa la configuración

app = Flask(__name__)
app.config.from_object(Config)  # Carga la configuración desde el objeto Config

app.register_blueprint(swagger.swagger_ui_blueprint, url_prefix=swagger.SWAGGER_URL)
app.register_blueprint(example1_blueprint)
app.register_blueprint(example2_blueprint)
app.register_blueprint(home_blueprint)
app.register_blueprint(register_user)
app.register_blueprint(register_new_user)
app.register_blueprint(films_blueprint)
app.register_blueprint(films_blueprint_all)

db.init_app(app)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
