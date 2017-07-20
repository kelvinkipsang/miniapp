from flask import Flask
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
