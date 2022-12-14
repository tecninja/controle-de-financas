from flask import Flask
from flask_login import LoginManager

app = Flask(__name__, template_folder='template')

lm = LoginManager(app)

from .controller import default  