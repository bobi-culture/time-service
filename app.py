from flask import Flask
from flask import jsonify
from time import ctime
import os, sys

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():    
    return f"<font face=tahoma size=3> Time service is up! </font>"

@app.route("/api/time", methods = ['GET'])
def time_me():
    data = {"time" : str(ctime())}    
    return jsonify(data)

@app.route("/api/hello", methods = ['GET', 'POST'])
def hello():
    return f"<font face=tahoma size=3> Hello there again!!!"

@app.route("/api/pingme", methods = ['GET', 'POST'])
def pingme():

    hosts = ["8.8.8.8", "216.239.38.120"] #, ,  ", , "192.168.0.100",  ];

    i = 0;

    for host in hosts:
        response = os.system("ping -c 1 " + hosts[i])
    
        if response == 0:
            return f"<center> <font face=tahoma size=5 color=green> \
                The Internet connection is stabilished and is Fine :) <br> </font>" \
            f"<font face=tahoma size=5 color=blue> \
                </br> Ping  could reach to Google.com <br> </font> </center>" \
    

        else:
            return f"<center> <font face=tahoma size=5 color=red> \
                The Internet connection is Failed !!! </font> </center>"


    # <!DOCTYPE html>
    # <html>
    # return f"<meta http-equiv='refresh' content='10'>"
#app.run(debug=True)
#"<html><meta http-equiv='refresh' content='5' ></html>"
#app.run(host='172.18.0.22', threaded = True, debug = True)