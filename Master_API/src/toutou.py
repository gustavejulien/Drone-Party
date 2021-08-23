import requests

from flask import Flask, request, jsonify, Response, Blueprint
from flask_cors import CORS, cross_origin
from flask import abort
from flaskthreads import AppContextThread

from src.jwtManager import confirm_JWT_token
from interface_high.template import template_interface

app = Blueprint('toutou', __name__, url_prefix="/toutou/")

template_interface = template_interface()

# --------------------------------------------------------------------------------------- active / desactive
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
# -------------------------------------------------------------- active
@app.route('/active/', methods=['POST'])
@cross_origin()
def active():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)        
        template_interface.activate()
        Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})
# -------------------------------------------------------------- active
# -------------------------------------------------------------- desactive
@app.route('/desactive/', methods=['POST'])
@cross_origin()
def desactive():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)        
        template_interface.desactivate()
        Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})
# -------------------------------------------------------------- desactive
# --------------------------------------------------------------------------------------- active / desactive


# --------------------------------------------------------------------------------------- start / destroy
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
# -------------------------------------------------------------- start
@app.route('/start/', methods=['POST'])
@cross_origin()
def start():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)        
        template_interface.start()
        Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})
# -------------------------------------------------------------- start
# -------------------------------------------------------------- destroy
@app.route('/destroy/', methods=['POST'])
@cross_origin()
def destroy():
    try:
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)        
        template_interface.destroy()
        Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})
# -------------------------------------------------------------- destroy
# --------------------------------------------------------------------------------------- active / desactive

# --------------------------------------------------------------------------------------- launch
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
# -------------------------------------------------------------- launch
@app.route('/launch/', methods=['POST'])
@cross_origin()
def launch():
    try:

        """
            thread ici pour éviter de rendre bloquant la boucle infinie.
        
        token = confirm_JWT_token(request.headers.get('token'), request.headers.get('refreshtoken'))
        if type(token) == str and token == "ko":
            abort(403)        """
        t = AppContextThread(target=launch_thread)
        t.start()
        t.join()
        template_interface.featuresloop()
        Response({"status" : "ok"})
    except Exception as e:
        return Response({"status" : "ko", "error" : str(e)})

def launch_thread():
    template_interface.featuresloop()
    Response({"status" : "ok"})
#https://github.com/sintezcs/flask-threads
# -------------------------------------------------------------- launch
# --------------------------------------------------------------------------------------- launch