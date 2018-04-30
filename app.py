from flask import Flask,jsonify
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/')
def homepage():
  return"<b>Rad! it works!<b>"

if __name__=="main":
    app.run(debug=True , use_reloader= True)

