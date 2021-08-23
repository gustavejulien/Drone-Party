import json
import os
import requests
import random
import sys
from pygame import mixer

from flask import Flask, request, jsonify, Response, Blueprint
from flask_cors import CORS, cross_origin

app = Blueprint('stop', __name__)


# --------------------------------------------------------------------------------------- stop
# -------------------------------------------------------------- Json to send
"""
{
}
"""
# -------------------------------------------------------------- Json to send

# -------------------------------------------------------------- Json answer
"""
{
    "ReqStatus" : "ok"
}
"""
# -------------------------------------------------------------- Json answer


# -------------------------------------------------------------- stop
@app.route('/stop', methods = ['GET'])
@cross_origin()
def stop():
    if mixer.get_init() is not None:
        stop_song()
        return ({"ReqStatus" : "ok"})
    print("No mixer up")
    return ({"ReqStatus" : "error"})
# -------------------------------------------------------------- stop


def stop_song():
    mixer.music.stop()
# -------------------------------------------------------------------------------------- stop