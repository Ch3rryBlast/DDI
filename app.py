from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, send_file, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import io

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    """The site's main route"""
    session.clear
    if request.method == "GET":
        return render_template("index.html")
    else:
        #TODO
        ...