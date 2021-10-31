from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)
KEY = "e6c5b746bd836be89003f2e23842f473196eddf1"

@app.route("/")
def title_screen():
    return render_template("title.html")

