import os
import time

from flask import Flask, redirect, render_template, request, abort, Blueprint
from template_helpers import setup_context_processors
import file_download, redirs, forms, pages

app = Flask(__name__)
setup_context_processors(app)
app.register_blueprint(redirs.bp)
app.register_blueprint(forms.bp)
app.register_blueprint(file_download.bp)
app.register_blueprint(pages.bp)


def redirect_final(text):
    return render_template("final.html", page_title="Redirect", text=text)


@app.route("/")
def home():
    return render_template("index.html", page_title="IBRO samples", menu="home")


@app.route("/urls")
def custom_urls():
    return render_template("custom_urls.html", page_title="Custom URLs", menu="urls")


@app.route("/slow-provision")
def slow_provision():
    time.sleep(20)
    return "Loaded"


@app.route("/slow-client-loading")
def slow_client():
    return render_template("slowpage.html")

@app.route("/replace-state")
def replace_state():
    return render_template("replace_state.html")


@app.route("/post-form", methods=["POST"])
def post_form():
    return redirect_final("Ok")


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")
