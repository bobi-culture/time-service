#from crypt import methods
#from urllib import response
from flask import Flask
from flask import jsonify
from time import ctime
import os, sys

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():    
    return "Time service is up!"

@app.route("/api/time", methods = ['GET'])
def time_me():
    data = {"time" : str(ctime())}    
    return jsonify(data)

@app.route("/api/hello", methods = ['GET', 'POST'])
def hello():
    return "Hi !!!"

@app.route("/api/pingme", methods = ['GET', 'POST'])
def pingme():

    host = "8.8.8.8";
    response = os.system("ping -c 1 " + host)
    if response == 0:
        return "Fine"
    else:
        return "Failed !!!"

app.run(host='0.0.0.0', threaded = True, debug = True)