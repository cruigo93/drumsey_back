import os
import requests
from loguru import logger
from flask import Flask, Response, Request, request
from werkzeug.utils import secure_filename
from flask_cors import CORS

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/index", methods=["GET"])
@app.route("/", methods=["GET"])
def index():
    return Response(status=202)

@app.route("/course", methods=["POST", "GET"])
def course():
    if request.method == "GET":
        return {
            "list": [
                {
                    "name": "Accients: Practice with Benny Greb",
                    "price": 200,
                    "rating": 4.8,
                    "desc": "Legendary Benny Greb brings some great tutorials about accients"
                },
                {
                    "name": "Accients: Practice with Benny Greb",
                    "price": 200,
                    "rating": 4.8,
                    "desc": "Legendary Benny Greb brings some great tutorials about accients"
                }
            ]
        }

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files['file']

    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return Response(status=202)


def main():
    app.run(host="localhost", port=8800)


if __name__ == '__main__':
    main()