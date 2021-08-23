import requests

class MasterApiPatrouille:
    def __init__(self):
        pass

    def init_tests(self):
        self.urls = {
            "start": "http://localhost:8001/patrouille/start/",
            "active": "http://localhost:8001/patrouille/active/",
            "desactive": "http://localhost:8001/patrouille/desactive/",
            "destroy": "http://localhost:8001/patrouille/destroy/",
            "land": "http://localhost:8001/manual/land/",
            "takeoff": "http://localhost:8001/manual/takeoff/"
        }
        self.takeoff()

    def kill_test(self):
        self.land()

    def land(self):
        res = requests.post(self.urls["land"], json={"value": 1})
        if (res.code != 200):
            raise Exception("Error on land")

    def takeoff(self):
        res = requests.post(self.urls["takeoff"], json={"value": 1})
        if (res.code != 200):
            raise Exception("Error on takeoff")

    def start(self):
        res = requests.post(self.urls["start"])
        if (res.code != 200):
            raise Exception("Error on start")
    
    def active(self):
        res = requests.post(self.urls["active"])
        if (res.code != 200):
            raise Exception("Error on active")

    def desactive(self):
        res = requests.post(self.urls["desactive"])
        if (res.code != 200):
            raise Exception("Error on desactive")

    def destroy(self):
        res = requests.post(self.urls["destroy"])
        if (res.code != 200):
            raise Exception("Error on destroy")