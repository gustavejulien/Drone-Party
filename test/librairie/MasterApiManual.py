import requests


class MasterApiManual:
    def __init__(self):
        pass

    def init_test(self):
        self.urls = {
            "secforward": "http://localhost:8001/manual/sec/forward/",
            "cmforward": "http://localhost:8001/manual/cm/forward/",
            "secbackward": "http://localhost:8001/manual/sec/backward/",
            "cmbackward": "http://localhost:8001/manual/cm/backward/",
            "cmleft": "http://localhost:8001/manual/cm/left/",
            "secleft": "http://localhost:8001/manual/sec/left/",
            "cmright": "http://localhost:8001/manual/cm/right/",
            "secright": "http://localhost:8001/manual/sec/right/",
            "secup":  "http://localhost:8001/manual/sec/up/",
            "cmup": "http://localhost:8001/manual/cm/up/",
            "cmdown": "http://localhost:8001/manual/cm/down/",
            "secdown": "http://localhost:8001/manual/sec/down/",
            "playsong": "http://localhost:8001/manual/playsong/",
            "takepicture": "http://localhost:8001/manual/takepicture/",
            "setspeed": "http://localhost:8001/manual/setspeed/",
            "turnleft": "http://localhost:8001/manual/turnleft/",
            "turnright": "http://localhost:8001/manual/turnright/",
            "land": "http://localhost:8001/manual/land/",
            "takeoff": "http://localhost:8001/manual/takeoff/"
        }
        self.takeoff()

    def kill_test(self):
        self.land()

    def secforward(self):
        res = requests.post(self.urls["secforward"], json={"value": 3})
        if (res.code != 200):
            raise Exception("Error on secforward")

    def cmforward(self):
        res = requests.post(self.urls["cmforward"], json={"value": 25})
        if (res.code != 200):
            raise Exception("Error on cmforward")

    def secbackward(self):
        res = requests.post(self.urls["secbackward"], json={"value": 3})
        if (res.code != 200):
            raise Exception("Error on secbackward")

    def cmbackward(self):
        res = requests.post(self.urls["cmbackward"], json={"value": 25})
        if (res.code != 200):
            raise Exception("Error on cmbackward")

    def cmleft(self):
        res = requests.post(self.urls["cmleft"], json={"value": 25})
        if (res.code != 200):
            raise Exception("Error on cmleft")

    def secleft(self):
        res = requests.post(self.urls["secleft"], json={"value": 3})
        if (res.code != 200):
            raise Exception("Error on secleft")

    def cmright(self):
        res = requests.post(self.urls["cmright"], json={"value": 25})
        if (res.code != 200):
            raise Exception("Error on cmright")

    def secright(self):
        res = requests.post(self.urls["secright"], json={"value": 3})
        if (res.code != 200):
            raise Exception("Error on secright")

    def secup(self):
        res = requests.post(self.urls["secup"], json={"value": 3})
        if (res.code != 200):
            raise Exception("Error on secup")

    def cmup(self):
        res = requests.post(self.urls["cmup"], json={"value": 25})
        if (res.code != 200):
            raise Exception("Error on cmup")

    def cmdown(self):
        res = requests.post(self.urls["cmdown"], json={"value": 25})
        if (res.code != 200):
            raise Exception("Error on cmup")

    def secdown(self):
        res = requests.post(self.urls["secdown"], json={"value": 3})
        if (res.code != 200):
            raise Exception("Error on secdown")

    def playsong(self):
        res = requests.post(self.urls["playsong"], json={"value": "song1"})
        if (res.code != 200):
            raise Exception("Error on playsong")

    def takepicture(self):
        res = requests.post(self.urls["takepicture"], json={
                            "value": "picture"})
        if (res.code != 200):
            raise Exception("Error on takepicture")

    def setspeed(self):
        res = requests.post(self.urls["setspeed"], json={"value": 50})
        if (res.code != 200):
            raise Exception("Error on setspeed")

    def turnleft(self):
        res = requests.post(self.urls["turnleft"], json={"value": 90})
        if (res.code != 200):
            raise Exception("Error on turnleft")

    def turnright(self):
        res = requests.post(self.urls["turnright"], json={"value": 90})
        if (res.code != 200):
            raise Exception("Error on turnright")

    def land(self):
        res = requests.post(self.urls["land"], json={"value": 1})
        if (res.code != 200):
            raise Exception("Error on land")

    def takeoff(self):
        res = requests.post(self.urls["takeoff"], json={"value": 1})
        if (res.code != 200):
            raise Exception("Error on takeoff")

# if __name__ == "__main__":
#     cl = MasterApiManual()
#     cl.init_test()
#     cl.secforward()
#     cl.cmforward()
