import time


class bd:
    def __init__(self):
        self.users = ["mark", "admin"]
        self.passwords = ["1", "123ghkijf"]

    def check_user(self, user, password):
        for i, el in enumerate(self.users):
            if el == user and self.passwords[i] == password:
                return [True, i]
        return [False, -1]


bd1 = bd()
from flask import Flask, request

app = Flask(__name__)


@app.route('/members')
def hello_world():
    rstequest
    return {'mark': "topssss"}


@app.route('/get_settings', methods=["POST", "GET"])
def hello_world1():
    time.sleep(1)
    user = str(request.json['user'])
    password = str(request.json['password'])
    print(request.json, request.method, [user, password])
    print(bd1.check_user(user, password))
    buf = bd1.check_user(user, password)
    if buf[0] == True:
        return {"status": "ok", "id": buf[1]}
    else:
        return {"status": "bad"}


app.run(debug=True)
