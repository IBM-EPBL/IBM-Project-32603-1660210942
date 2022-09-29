# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 14:47:23 2022

@author: M17
"""

from flask import Flask,render_template, request 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login', methods =["POST"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return render_template ("index.html", y = user)
    
    
if __name__==('__main__'):
    app.run(debug = True)