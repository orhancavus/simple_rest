from flask import Flask, jsonify
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello from Python Flask"


@app.route("/api/data")
def get_data():
    data = {"name": "John", "age": 30, "city": "New York"}
    return jsonify(data)


# Wrap Flask with WsgiToAsgi
asgi_app = WsgiToAsgi(app)
