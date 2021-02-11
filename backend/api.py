
import glob
import json
import pickle

import pandas as pd

from flask import Flask, jsonify

from functions import clusterN, clusterUnknown

app = Flask(__name__)

@app.route('/PersonList')
def f0():
    with open('../data/persons.json') as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/clusterN', defaults = { 'n' : 4 })
@app.route('/clusterN/<int:n>')
def f1(n):
    info = clusterN(n)
    return jsonify(info)

@app.route('/clusterUnknown')
def f2():
    info = clusterUnknown()
    return jsonify(info)