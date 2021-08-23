import json
import os
import requests
import random
import sys

from flask import Flask, request, jsonify, Response, Blueprint
from flask_cors import CORS, cross_origin

from view.add_song import app as add_song
from view.play_song import app as play_song
from view.pause import app as pause
from view.stop import app as stop

APP = Flask(__name__)
UPLOAD_FOLDER = './song'
APP.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(APP)

APP.register_blueprint(add_song)
APP.register_blueprint(play_song)
APP.register_blueprint(pause)
APP.register_blueprint(stop)

@APP.route('/ping', methods=['GET'])
@cross_origin()
def ping():
    return Response("pong", mimetype='text/html')


if __name__ == "__main__":
    print("API start")
    try:
        APP.run(host="0.0.0.0", port=80, debug=True)
    except Exception as e:
        print(str(e))
        pass
