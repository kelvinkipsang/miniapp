from flask import render_template,flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


from app import app
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])




@app.route('/',methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def index():
    form = ReusableForm(request.form)
    print (form.errors)
    if request.method == 'POST':
        name=request.form['name']
        print (name)


        if form.validate():
            # Save the comment here.
            flash(name)
        else:
            flash('please add an item to the bucketlist. ')
    return render_template("index.html",form=form)

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

@app.route('/viewblist.html')
def viewblist():
    return render_template("viewblist.html")
