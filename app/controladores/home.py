from app import app
import os
import urllib.request
#from chatbot_trainer import chatbot
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, url_for, render_template

@app.route("/")
def home():
    return render_template("index.html")

