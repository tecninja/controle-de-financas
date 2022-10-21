from app import Aplicacao
from flask import render_template

app = Aplicacao().app

@app.route("/")
def index():
    return render_template("login_page.html")

