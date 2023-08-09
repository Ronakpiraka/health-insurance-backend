# app/__init__.py
from flask import Flask
from flask_pymongo import PyMongo
from app.config import MONGO_URI  # Update import path

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)

from app import routes
