import json
import os
import requests
import random
import sys
from pygame import mixer

from flask import Flask, request, jsonify, Response, Blueprint
from flask_cors import CORS, cross_origin

from config import UPLOAD_FOLDER

app = Blueprint('song', __name__)


# --------------------------------------------------------------------------------------- play_song
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


# -------------------------------------------------------------- song
@app.route('/song/<string:song_name>', methods = ['GET'])
@cross_origin()
def song(song_name):
    get = request.get_json()
    song_path = os.path.join(UPLOAD_FOLDER, song_name)

    print(song_path)
    if os.path.isfile(song_path):
        play_song(song_path)
        return ({"ReqStatus" : "ok"})
    return ({"ReqStatus" : "error"})
# -------------------------------------------------------------- song


def play_song(song_path):
    mixer.init()
    mixer.music.set_volume(0.7)
    mixer.music.load(song_path)
    mixer.music.play()

# -------------------------------------------------------------------------------------- play_song
