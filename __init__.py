from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__melissa__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('HelloWorld.html') 
  
if __name__ == "__main__":
  app.run(debug=True)
