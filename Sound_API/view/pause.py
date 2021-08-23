import json
import os
import requests
import random
import sys
from pygame import mixer

from flask import Flask, request, jsonify, Response, Blueprint
from flask_cors import CORS, cross_origin

app = Blueprint('pause', __name__)


# --------------------------------------------------------------------------------------- pause
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


# -------------------------------------------------------------- pause
@app.route('/pause', methods = ['GET'])
@cross_origin()
def pause():
    if mixer.get_init() is not None:
        print(mixer)
        pause_song()
        return ({"ReqStatus" : "ok"})
    print("No mixer up")
    return ({"ReqStatus" : "error"})
# -------------------------------------------------------------- pause


def pause_song():
    print(mixer.music.get_busy())
    if mixer.music. get_busy() == 1:
        mixer.music.pause()
    else:
        mixer.music.unpause()
# -------------------------------------------------------------------------------------- pause
