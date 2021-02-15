
import glob
import json
import pickle

import time

import pandas as pd

from flask import Flask, jsonify

from functions import clusterN, clusterUnknown, getChips

app = Flask(__name__)

# @app.route('/PersonList')
# def f0():
#     with open('../data/persons.json') as f:
#         data = json.load(f)
#     return jsonify(data)

@app.route('/clusterN', defaults = { 'n' : 4 })
@app.route('/clusterN/<int:n>')
def f1(n):
    info = clusterN(n)
    return jsonify(info)

@app.route('/clusterU')
def f2():
    info = clusterUnknown()
    return jsonify(info)

@app.route('/getChipsN')
def f3():
    chips = getChips(known=True)
    return jsonify(chips)

@app.route('/getChipsU')
def f4():
    chips = getChips(known=False)
    return jsonify(chips)
