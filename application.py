from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/t")
def t():
    return render_template("training.html")

@app.route("/comunidade")
def comunidade():
    return render_template("comunity.html")

@app.route("/inscrição")
def inscrição():
    return render_template("pages/inscrição.html")

@app.route("/entrar")
def entrar():
    return render_template("pages/login.html")

@app.route("/contato")
def contato():
    return render_template("pages/contato.html")

@app.route("/alfabeto")
def alfabeto():
    return render_template("grama/alfabeto.html")

@app.route("/simplep")
def simplep():
    return render_template("grama/simplep.html")

@app.route("/tra")
def tra():
    return render_template("training1.html")

@app.route("/mc")
def mc():
    return render_template("mc.html")
