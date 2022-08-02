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
    return "Hello there !!!"

@app.route("/api/pingme", methods = ['GET', 'POST'])
def pingme():

    # host = "8.8.8.8";
    # response = os.system("ping -c 1 " + host)
    # if response == 0:
    #     return f"<font face=tahoma size=10 color=green> Fine :) </font>"
    # else:
    #     return f"<font face=tahoma size=20 color=red> Failed </font>"

    hosts = ["8.8.8.8", "4.4.4.4"];

    i = 0;

    for host in hosts:
        response = os.system("ping -c 1 " + hosts[i])
    
        if response == 0:
            return f"<font face=tahoma size=10 color=green> \
                The Internet connection is stabilished and is Fine :) </font>"
        else:
            return f"<font face=tahoma size=20 color=red> \
                The Internet connection is Failed !!! </font>"

#app.run(debug=True)
#"<html><meta http-equiv='refresh' content='5' ></html>"
#app.run(host='172.18.0.22', threaded = True, debug = True)