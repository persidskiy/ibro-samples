import os
import time

from flask import Flask, redirect, render_template, request, abort
from template_helpers import setup_context_processors
from redirs import bp as redirs_bp


app = Flask(__name__)
setup_context_processors(app)
app.register_blueprint(redirs_bp)


def redirect_final(text):
    return render_template("final.html", page_title="Redirect", text=text)


@app.route("/")
def home():
    return render_template("index.html",
                           page_title="IBRO samples",
                           menu="home")


@app.route("/urls")
def custom_urls():
    return render_template("custom_urls.html",
                           page_title="Custom URLs",
                           menu="urls")
                           
@app.route("/readability")
def readability():
    return render_template("readability_markup.html",
                           page_title="Readability Markup testing",
                           menu="readability")
                           
@app.route("/other")
def other():
    return render_template("other.html",
                           page_title="Other known tesing pages",
                           menu="other")


@app.route("/slow-provision")
def slow_provision():
    time.sleep(20)
    return "Loaded"


@app.route("/slow-client-loading")
def slow_client():
    return render_template("slowpage.html")


@app.route("/post-form", methods=["POST"])
def post_form():
    return redirect_final("Ok")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")
