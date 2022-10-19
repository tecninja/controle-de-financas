from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
import json

class Aplicacao:
    
    app = Flask(__name__)
    
    def __init__(self) -> None:
        pass
    
    @app.route('/')
    @app.route("/autenticacao")
    def index():
        page = "\\view\\template\\login_page.html"
        return render_template(page)

    @app.route("/index")
    def teste():
        return "pagina de teste"

    @app.route("/done", methods=["POST","GET"])    
    def done():
        return json.dumps(request.form)
    
if __name__ == '__main__':
    Aplicacao.app.run(debug=True, port="3000")