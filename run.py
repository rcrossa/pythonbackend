from flask import Flask
from app.views import *

app = Flask(__name__)

app.route('/', methods=['GET'])(index)
app.route('/data', methods=['GET'])(getInformation)

if __name__ == '__main__':
    app.run(debug=True)