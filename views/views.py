from flask import jsonify

def index():
    return 'Hello World!'

def getInformation():
    prueba = [{"id": 1, "name": "Juan"}, {"id": 2, "name": "Pedro"}]
    return jsonify(prueba)
