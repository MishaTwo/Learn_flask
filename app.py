from flask import Flask, render_template, redirect
from dotenv import load_dotenv
from models.base import create_database
import os

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

with app.app_context():
    create_database()

import routes