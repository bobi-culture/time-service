from flask import Flask
from flask import jsonify
from time import ctime


app = Flask(__name__)


@app.route("/api/time", methods = ['GET'])
def ping():
    data = {"time" : str(ctime())}    
    return jsonify(data)


@app.route("/", methods = ['GET', 'POST'])
def home():    
    return "Time service is up!"


app.run(host='0.0.0.0', threaded = True, debug = True)