#!/usr/bin/python
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


@app.route('/', methods=['post', 'get'])
def usage():
    abort(Response('https://github.com/RyoLee/tinyapis'))


@app.route('/ping', methods=['post', 'get'])
def ping():
    return 'pong'


@app.route('/str2md5', methods=['post', 'get'])
def getMD5():
    s0 = request.form.to_dict()["str"]
    m = hashlib.md5()
    m.update(bytes(s0, encoding='utf-8'))
    return m.hexdigest()


@app.route('/2lowercase', methods=['post', 'get'])
def getLowerCase():
    s0 = request.form.to_dict()["str"]
    return s0.lower()


@app.route('/2uppercase', methods=['post', 'get'])
def getUpperCase():
    s0 = request.form.to_dict()["str"]
    return s0.upper()


@app.route('/gettoken', methods=['post', 'get'])
def getTokens():
    p = request.form.to_dict()["key"]
    ts = str(int(time.time())//30)
    m = hashlib.md5()
    m.update(bytes(ts+p, encoding='utf-8'))
    return m.hexdigest()


@app.route('/timestamp', methods=['post', 'get'])
def getTimestamp():
    return str(int(time.time()))


if __name__ == '__main__':
    app.run(host=host, port=port, debug=debug)
