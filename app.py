from flask import Flask, render_template

app = Flask("hello")

@app.route("/")

def hello():
    return "<h1>quero funcionando assim</h1><p>nao me lembro do que fazer</p>"

@app.route("/contato")
def meuContato():
    return "<h2>CFSJ, cfsj@gamil.com<h2>"

@app.route("/about")
def pagAbout():
    return render_template("index.html")