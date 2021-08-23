import requests
import sys

from flask import Flask, request, jsonify, Response, Blueprint, jsonify
from flask_cors import CORS, cross_origin
from flask import abort

from src.jwtManager import confirm_JWT_token
from config import HOST_API_USER, PORT_API_USER, BASE_URL_API_USER

app = Blueprint('user', __name__)

# --------------------------------------------------------------------------------------- connect
# -------------------------------------------------------------- Json to send
"""
body :
{
    "password" : password,
    "username" : username,
}

"""
# -------------------------------------------------------------- Json to send
# -------------------------------------------------------------- Json answer
"""
{
    "status" : "ok"/"ko"
}
"""
# -------------------------------------------------------------- Json answer
# -------------------------------------------------------------- connect
@app.route('/user/connect/', methods=['POST'])
@cross_origin()
def connect():
    try:
        jsonObject = dict(request.get_json())
        print("entry ->", jsonObject, file=sys.stderr)
        data = requests.post("http://" + HOST_API_USER + ":" + PORT_API_USER + "/connect/", json=jsonObject).json()
        print("out ->", data, file=sys.stderr)
        if (data["status"] == "ok"):
            return jsonify({"status": "ok", "token" : data["token"],  "refreshtoken" : data["refreshtoken"]})
        return jsonify({"status": "ko"})
    except Exception as e:
        return jsonify({"status" : "ko", "error" : str(e)})


# -------------------------------------------------------------- connect
# --------------------------------------------------------------------------------------- connect


# --------------------------------------------------------------------------------------- user
# -------------------------------------------------------------- Json to send
"""
header : 
{
    "token" : xxxx
    "refreshtoken" : xxxx
}

body :
{
    "password" : password,
    "username" : username,
}
"""
# -------------------------------------------------------------- Json to send
# -------------------------------------------------------------- Json answer
"""
{
    "status" : "ok"/"ko"
}
"""

# -------------------------------------------------------------- Json answer
# -------------------------------------------------------------- user
@app.route('/user/', methods=['POST', 'GET', 'PUT', 'DELETE'])
@cross_origin()
def user_crud():
    try:
        # --------------------------------------------------- handle crud
        jsonObject = dict(request.get_json())
        headerObject = dict(request.headers)
        print("entry ->", jsonObject, file=sys.stderr)
        print("header ->", headerObject, file=sys.stderr)
        if (request.method == 'POST'):
            data = requests.post("http://" + HOST_API_USER + ":" + PORT_API_USER + BASE_URL_API_USER, json=jsonObject).json()
        if (request.method == 'DELETE'):
            data = requests.delete("http://" + HOST_API_USER + ":" + PORT_API_USER + BASE_URL_API_USER, json=jsonObject, headers=headerObject).json()
        if (request.method == 'GET'):
            data = requests.get("http://" + HOST_API_USER + ":" + PORT_API_USER + BASE_URL_API_USER, json=jsonObject, headers=headerObject).json()
        if (request.method == 'PUT'):
            data = requests.put("http://" + HOST_API_USER + ":" + PORT_API_USER + BASE_URL_API_USER, json=jsonObject, headers=headerObject).json()
        print("out ->", data, file=sys.stderr)
        # --------------------------------------------------- handle crud
        if (data["status"] == "ok"):
            return jsonify(data)
        return jsonify(data)
    except Exception as e:
        return jsonify({"status" : "ko", "error" : str(e)})
# -------------------------------------------------------------- user
# --------------------------------------------------------------------------------------- user


# Je viens de voir ton fichier, je suis à peine étonné. 

# Tu as juste repris le fichier de la vidéo avec des modifications mineures. Le fichier mapping.py pour être précis.

# Nous t'avions dit la semaine dernière que tu étais sur la sellette mais la c'est excessif. Tu nous prends vraiment pour imbéciles.

# Tu ne travailles pas, et j'espère que tu auras au moins l'honnetete de l'admettre. 

# Nous allons contacter lucas pour t'exclure du goupe. Notre décision est prise et l'ensemble du groupe est d'accord, tu aurais pu le comprendre si tu avais fournit l'effort de rejoindre les réunions. 