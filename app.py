from api_financas.api import *
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Index"

@app.route("/teste")
def teste():
    return "pagina de teste"

app.run()