from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

#DADOS
posts = [
    {
        "title": "Primeiro post 1",
        "body": "Texto post 1",
        "author": "Luana",
        "created": datetime(2022,7,25, 16, 23, 11)
    },
    {
        "title": "Segundo post 2",
        "body": "Texto post 2",
        "author": "Mayara",
        "created": datetime(2022,7,26, 8, 35, 7)
    },
    {
        "title": "Terceiro post 3",
        "body": "Texto post 3",
        "author": "Karen",
        "created": datetime(2022,7,18, 8, 37, 7)
    },
    {
        "title": "Quarto post 4",
        "body": "Texto post 4",
        "author": "Beth",
        "created": datetime(2022,7,2, 10, 22, 7)
    },
    {
        "title": "Quinto post 5",
        "body": "Texto post 5",
        "author": "Paty",
        "created": datetime(2022,7,3, 15, 43, 7)
    },
    {
        "title": "Sexto post 6",
        "body": "Texto post 6",
        "author": "Jack",
        "created": datetime(2022,7,21, 9, 21, 7)
    }
]

@app.route("/")
def hello():
    return render_template("index.html", posts=posts)

@app.route("/contato")
def meuContato():
    return "<h2>CFSJ, cfsj@gamil.com<h2>"

@app.route("/about")
def pagAbout():
    return render_template("index.html", email="d.cj@gmail.com", apelido = "minduba")

@app.route("/login")
def login():
    return render_template("login.html")