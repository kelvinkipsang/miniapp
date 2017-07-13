from flask import render_template

from app import app

@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html")

@app.route('/login.html')
def login():
    return render_template("login.html")

@app.route('/register.html')
def register():
    return render_template("register.html")

@app.route('/create.html')
def create():
    return render_template("create.html")

@app.route('/Add.html')
def add():
    return render_template("Add.html")

@app.route('/myactivities.html')
def myactivities():
    return render_template("mybucket.html")