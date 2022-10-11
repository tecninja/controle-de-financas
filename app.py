from api_financas.api import *
from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "Index"

if __name__ == '__name__':
    app.run()