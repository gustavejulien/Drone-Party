#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import requests
import random
import sys

from flask import Flask, request, jsonify, Response, Blueprint
from flask_cors import CORS, cross_origin

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

APP = Flask(__name__)
CORS(APP)


from src.user import app as user
from src.patrouille import app as patrouille
from src.manuel import app as manuel
from src.toutou import app as toutou

APP.register_blueprint(user)
APP.register_blueprint(patrouille)
APP.register_blueprint(manuel)
APP.register_blueprint(toutou)

limiter = Limiter(
    APP,
    key_func=get_remote_address,
    default_limits=["1000 per day", "500 per hour"]
)

@APP.route('/ping', methods=['GET'])
@cross_origin()
def ping():
    return Response("pong",mimetype='text/html')

if __name__ == "__main__":
    try :
        APP.run(host="0.0.0.0", port=8001, debug=True)
    except Exception as e:
        print(str(e))