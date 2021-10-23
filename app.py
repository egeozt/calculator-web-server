from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sum/<int:value_1>/<int:value_2>")
def sum(value_1, value_2):
    return str(value_1 + value_2)

@app.route("/sub/<int:value_1>/<int:value_2>")
def sub(value_1, value_2):
    return str(value_1 - value_2)

@app.route("/multi/<int:value_1>/<int:value_2>")
def multi(value_1, value_2):
    return str(value_1 * value_2)

@app.route("/div/<int:value_1>/<int:value_2>")
def div(value_1, value_2):
    return str(value_1 / value_2)