from flask import Flask
import time


app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def get_time():
    
    return str(time.time())


app.run(host='0.0.0.0', threaded = True, debug = True)