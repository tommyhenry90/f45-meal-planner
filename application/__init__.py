from flask import Flask, render_template
from flask_cors import CORS
import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '.env')
load_dotenv(filename)

app = Flask(__name__)
app.static_folder = os.path.abspath('frontend/dist/static')
app.template_folder = os.path.abspath('frontend/dist')
CORS(app)

from application import server
from application.models import recipes, shopping_list
