from flask import Flask
from flask_cors import CORS
from app.routes.routes import rout
from static import swagger
from utils.db import init_app

app = Flask(__name__)


app.register_blueprint(swagger.swagger_ui_blueprint, url_prefix=swagger.SWAGGER_URL)
app.register_blueprint(rout)

CORS(
    app,
    resources={
        r"/*": {
            "origins": [
                "http://localhost",
                "http://codoacodo.duckdns.org:5000",
                "http://127.0.0.1:5500/",
                "https://starlit-mochi-82dea3.netlify.app/"
            ]
        }
    },
)
if __name__ == '__main__':
    app.run(debug=True)