# !/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import hashlib
from flask import Flask, request, abort, Response
from configparser import ConfigParser

app = Flask(__name__)
cp = ConfigParser()
cp.read('/config/TinyApis.cfg')
host = cp.get('main', 'host')
port = int(cp.get('main', 'port'))
debug = ("1" == cp.get('main', 'debug'))
mainpw = cp.get('main', 'password')


@app.route('/')
def usage():
    abort(Response('https://github.com/RyoLee/tinyapis'))


@app.route('/ping')
def ping():
    return 'pong'


@app.route('/str2md5')
def getMD5():
    s0 = request.form.to_dict()["str"]
    m = hashlib.md5()
    m.update(bytes(s0, encoding='utf-8'))
    return m.hexdigest()


@app.route('/2lowercase')
def getLowerCase():
    s0 = request.form.to_dict()["str"]
    return s0.lower()


@app.route('/2uppercase')
def getLowerCase():
    s0 = request.form.to_dict()["str"]
    return s0.upper()


@app.route('/gettoken')
def getTokens():
    p = request.form.to_dict()["key"]
    ts = str(int(time.time())//30)
    m = hashlib.md5()
    m.update(bytes(ts+p, encoding='utf-8'))
    return m.hexdigest()


@app.route('/timestamp')
def getTimestamp():
    return int(time.time())


if __name__ == '__main__':
    app.run(host=host, port=port, debug=debug)
