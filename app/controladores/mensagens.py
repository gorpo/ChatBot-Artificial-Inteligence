
from app import app
import os
import urllib.request
#from chatbot_trainer import chatbot
from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, url_for, render_template



@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return 'oi'#str(chatbot.get_response(userText))