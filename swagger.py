from swagger_ui import api_doc

from swagger_ui import flask_api_doc
from flask import Flask

app = Flask(__name__)
flask_api_doc(app, config_path='./conf/test.yaml', url_prefix='/api/doc', title='API doc')

if __name__ == '__main__':
    app.run(debug=True)