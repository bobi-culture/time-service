from flask import Flask
from time import ctime


app = Flask(__name__)


@app.route("/", methods = ['GET', 'POST'])
def get_time():    
    return str(ctime())


app.run(host='0.0.0.0', threaded = True, debug = True)