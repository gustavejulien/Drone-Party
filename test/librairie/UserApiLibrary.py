import requests

class UserApiLibrary:
    def __init__(self):
        pass

    def init_tests(self):
        self.urls = {
            "connect": "http://localhost:8001/user/connect/",
            "user": "http://localhost:8001/user/"
        }

    def kill_test(self):
        pass

    def connect(self):
        res = requests.post(self.urls["connect"], json={"password" : "test2", "username" : "test2"})
        if res.code != 200:
            raise Exception("Error on connect")

    def postuser(self):
        res = requests.post(self.urls["user"], json={"password" : "test2", "username" : "test2", "email":"pingouin2"})
        if res.code != 200:
            raise Exception("Error on post user")
    
    def putuser(self):
        res = requests.post(self.urls["user"], json={"password" : "test2", "username" : "test2"})
        if res.code != 200:
            raise Exception("Error on put user")

    def getuser(self):
        res = requests.post(self.urls["user"], json={"password" : "test2", "username" : "test2"})
        if res.code != 200:
            raise Exception("Error on get user")

    def deleteuser(self):
        res = requests.post(self.urls["user"], json={"password" : "test2", "username" : "test2"})
        if res.code != 200:
            raise Exception("Error on delete user")