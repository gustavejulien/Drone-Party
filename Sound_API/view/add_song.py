import json
import os
import requests
import random
import sys

from flask import Flask, request, jsonify, Response, Blueprint, send_file
from flask_cors import CORS, cross_origin

from werkzeug.utils import secure_filename

from config import UPLOAD_FOLDER

app = Blueprint('add_song', __name__)

ALLOWED_EXTENSIONS = {'mp3'}  # add extensions later maybe

# --------------------------------------------------------------------------------------- add_song
# -------------------------------------------------------------- Json to send
"""
{
    "path" : "blabla",
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


# -------------------------------------------------------------- add_song
@app.route('/add_song', methods = ['POST'])
@cross_origin()
def add_song():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return ({"ReqStatus" : "error"})
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print('No selected file')
            return ({"ReqStatus" : "error"})
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            return ({"ReqStatus" : "ok"})

# -------------------------------------------------------------- add_song


def allowed_file(filename):
    print(filename)
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# --------------------------------------------------------------------------------------- add_song
