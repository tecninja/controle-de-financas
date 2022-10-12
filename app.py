from api_financas.api import *
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def index():
    page = "aut-page.html"
    return render_template(page)

@app.route("/teste")
def teste():
    return "pagina de teste"

app.run()