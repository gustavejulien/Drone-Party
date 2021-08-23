import json
import os
import requests
import random
import sys
from pygame import mixer
import pyttsx3

from flask import Flask, request, jsonify, Response, Blueprint
from flask_cors import CORS, cross_origin

from config import TTS_VOLUME, TTS_RATE

app = Blueprint('speak', __name__)


# --------------------------------------------------------------------------------------- speak
# -------------------------------------------------------------- Json to send
"""
{
    "Sentence": "blablabla",
    "Voice": 0              #0 for male, 1 for female
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


# -------------------------------------------------------------- speak
@app.route('/speak', methods = ['GET'])
@cross_origin()
def speak():
    get = request.get_json()
    sentence = get['Sentence']
    voice = get['Voice']

    engine = pyttsx3.init()
    engine.setProperty('rate', TTS_RATE)
    engine.setProperty('volume', TTS_VOLUME)
    voices = engine.getProperty('voices')

    if type(sentence) == str and (voice == 0 or voice == 1):
        engine.setProperty('voice', voices[voice].id)
        engine.say(sentence)
        engine.runAndWait()
        engine.stop()
        return ({"ReqStatus" : "ok"})
    return ({"ReqStatus" : "error"})
# -------------------------------------------------------------- speak
# -------------------------------------------------------------------------------------- speak
