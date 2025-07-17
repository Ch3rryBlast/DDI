from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, send_file, url_for
from flask_session import Session
import io
from transformers import pipeline

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
    session.clear()
    if request.method == "GET":
        return render_template("index.html")
    else:

        d1 = request.form.get("D1")
        d2 = request.form.get("D2")

        qa_pipeline = pipeline('question-answering')
        context = "You are a medical doctor answering question about drug to drug interactions"
        question = f"What are the side effects when these two drugs are used at the same time, not side effects specific to each drug, side effects that happen when both are used together: {d1}, {d2}?"
        answer = qa_pipeline(question=question, context=context)

        if(not d1 or not d2 or d1.isdigit() or d2.isdigit()):
            return redirect("/")
        
    

        return render_template("index.html", test=answer)