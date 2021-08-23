import jwt
import requests
import datetime
from flask import request

from config import HOST_API_USER, PORT_API_USER, BASE_URL_API_USER

def confirm_JWT_token(token, refreshtoken):
    try:
        jwt.decode(token, "secret", leeway=10, algorithms=["HS256"])
        return ("ok")
    except:
        data = requests.post("http://" + HOST_API_USER + ":" + PORT_API_USER + BASE_URL_API_USER + "refresh/", json={"refreshtoken" : refreshtoken}).json()
        if "token" in data:
            return "ok"
        return ("ok")