#!/usr bin/env python

from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object('config')
client = MongoClient()
db = client['qr_quest']
objects = db['objects']

from app import views
