import requests
import sys

from flask import Flask, request, jsonify, Response, Blueprint
from flask_cors import CORS, cross_origin
from flask import abort

from src.jwtManager import confirm_JWT_token
from interface_low.template import template_interface_low as template_interface
from interface_low.DroneController import DroneController
from config import HOST_API_SONG, PORT_API_SONG, BASE_URL_API_SONG

app = Blueprint('manual', __name__, url_prefix="/manual/")

template_interface = template_interface()

controller = DroneController()

# --------------------------------------------------------------------------------------- move
# -------------------------------------------------------------- Json to send
"""
header : 
{
    "token" : xxxx
    "refreshtoken" : xxxx
}

body : 
{
    "value" : value (int)
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
# -------------------------------------------------------------- forward
@app.route('/cm/forward/', methods=['POST'])
@cross_origin()
def forwardcm():
    try:
        value = request.get_json()["value"]
        controller.forwardCm(value)
        return Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})

@app.route('/sec/forward/', methods=['POST'])
@cross_origin()
def forwardSec():
    try:
        value = request.get_json()["value"]
        controller.forwardSec(value)
        return Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})
# -------------------------------------------------------------- forward
# -------------------------------------------------------------- backward
@app.route('/cm/backward/', methods=['POST'])
@cross_origin()
def backwardcm():
    try:
        value = request.get_json()["value"]
        controller.backwardCm(value)
        return Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})

@app.route('/sec/backward/', methods=['POST'])
@cross_origin()
def backwardSec():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)
        value = request.get_json()["value"]
        controller.backwardSec(value)
        return Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})
# -------------------------------------------------------------- backward
# -------------------------------------------------------------- left
@app.route('/cm/left/', methods=['POST'])
@cross_origin()
def leftcm():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)
        value = request.get_json()["value"]
        controller.leftCm(value)
        return Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})

@app.route('/sec/left/', methods=['POST'])
@cross_origin()
def leftSec():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)
        value = request.get_json()["value"]
        controller.leftSec(value)
        return Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})
# -------------------------------------------------------------- left
# -------------------------------------------------------------- right
@app.route('/cm/right/', methods=['POST'])
@cross_origin()
def rightcm():
    try:
        value = request.get_json()["value"]
        controller.rightCm(value)
        return Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})

@app.route('/sec/right/', methods=['POST'])
@cross_origin()
def rightSec():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)
        value = request.get_json()["value"]
        controller.rightSec(value)
        return Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})
# -------------------------------------------------------------- right
# --------------------------------------------------------------------------------------- move

# --------------------------------------------------------------------------------------- takepicture
# -------------------------------------------------------------- Json to send
"""
header : 
{
    "token" : xxxx
    "refreshtoken" : xxxx
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
# -------------------------------------------------------------- takepicture
@app.route('/takepicture/', methods=['POST'])
@cross_origin()
def takepicture():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)
        controller.takepicture()
        return Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})
# -------------------------------------------------------------- takepicture
# --------------------------------------------------------------------------------------- takepicture

# --------------------------------------------------------------------------------------- move up / down
# -------------------------------------------------------------- Json to send
"""
header : 
{
    "token" : xxxx
    "refreshtoken" : xxxx
}
body : 
{
    "value" : value (int)
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
# -------------------------------------------------------------- move up
@app.route('/cm/up/', methods=['POST'])
@cross_origin()
def upcm():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)
        value = request.get_json()["value"]
        controller.upCm(value)
        return Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})

@app.route('/sec/up/', methods=['POST'])
@cross_origin()
def upSec():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)
        value = request.get_json()["value"]
        controller.upSec(value)
        return Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})

# -------------------------------------------------------------- move up
# -------------------------------------------------------------- move down
@app.route('/cm/down/', methods=['POST'])
@cross_origin()
def downcm():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)
        value = request.get_json()["value"]
        controller.downCm(value)
        return Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})

@app.route('/sec/down/', methods=['POST'])
@cross_origin()
def downSec():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)
        value = request.get_json()["value"]
        controller.downSec(value)
        return Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})

# -------------------------------------------------------------- move down
# --------------------------------------------------------------------------------------- move up / down

# --------------------------------------------------------------------------------------- playsong
# -------------------------------------------------------------- Json to send
"""
header : 
{
    "token" : xxxx
    "refreshtoken" : xxxx
}
body : 
{
    "value" : value
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
# -------------------------------------------------------------- playsong
@app.route('/playsong/', methods=['POST'])
@cross_origin()
def playsong():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)
        value = request.get_json()["value"]
        data = requests.post("http://" + HOST_API_SONG + ":" + PORT_API_SONG + BASE_URL_API_SONG + str(value)).json()
        return Response({"status" : data["status"]})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})

# -------------------------------------------------------------- playsong
# --------------------------------------------------------------------------------------- playsong

# --------------------------------------------------------------------------------------- set speed
# -------------------------------------------------------------- Json to send
"""
header : 
{
    "token" : xxxx
    "refreshtoken" : xxxx
}
body : 
{
    "value" : value (int)
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
# -------------------------------------------------------------- set speed
@app.route('/setspeed/', methods=['POST'])
@cross_origin()
def setSpeed():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)
        value = request.get_json()["value"]
        controller.setSpeed(value)
        return Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})

# -------------------------------------------------------------- set speed
# --------------------------------------------------------------------------------------- set speed


# --------------------------------------------------------------------------------------- turn
# -------------------------------------------------------------- Json to send
"""
header : 
{
    "token" : xxxx
    "refreshtoken" : xxxx
}
body : 
{
    "value" : value (int)
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
# -------------------------------------------------------------- turn
@app.route('/turnleft/', methods=['POST'])
@cross_origin()
def turnleft():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)
        value = request.get_json()["value"]
        controller.turnLeft(value)
        return Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})

@app.route('/turnright/', methods=['POST'])
@cross_origin()
def turnRight():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)
        value = request.get_json()["value"]
        controller.turnRight(value)
        return Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})

# -------------------------------------------------------------- turn
# --------------------------------------------------------------------------------------- turn

@app.route('/takeoff/', methods=['POST'])
@cross_origin()
def takeoff():
    try:
        controller.takeOff()
        return Response({"status" : "ok"})
    except Exception as e:
        print(e,file=sys.stderr)
        return Response({"status" : "ko", "error" : str(e)})

@app.route('/land/', methods=['POST'])
@cross_origin()
def land():
    try:
        controller.land()
        return Response({"status" : "ok"})
    except Exception as e:
        print(e,file=sys.stderr)
        return Response({"status" : "ko", "error" : str(e)})