from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/createbucketlist')
def create():
    return render_template("create.html")

@app.route('/addactivity')
def add():
    return render_template("addactivity.html")

@app.route('/myactivities')
def myactivities():
    return render_template("mybucket.html")