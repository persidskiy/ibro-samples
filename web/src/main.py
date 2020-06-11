import os
import time
from flask import Flask, redirect, render_template, request, abort

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "local-dev")


def redirect_final(text):
    return render_template("final.html", page_title="Redirect", text=text)


@app.route('/')
def home():
    return render_template("index.html",
                           page_title="IBRO samples",
                           menu="home",
                           app_version=APP_VERSION)


@app.route('/urls')
def custom_urls():
    return render_template("custom_urls.html",
                           page_title="Custom URLs",
                           menu="urls",
                           app_version=APP_VERSION)


# Simple HTTP
@app.route('/simple')
def simple():
    return redirect("/simple-1", code=302)


@app.route('/simple-1')
def simple_1():
    return redirect_final("Simple 1")


# Two HTTP
@app.route('/two-http')
def two_http():
    return redirect("/two-http-1", code=302)


@app.route('/two-http-1')
def two_http_1():
    return redirect("two-http-2")


@app.route('/two-http-2')
def two_http_2():
    return redirect_final("Two HTTP")


# Complex
@app.route('/complex')
def complex_redirect():
    return redirect("/complex-1", code=302)


@app.route('/complex-1')
def complex_redirect_1():
    return render_template("client_js_complex.html")


@app.route('/complex-2')
def complex_redirect_2():
    return redirect("/complex-3", code=302)


@app.route('/complex-3')
def complex_redirect_3():
    return redirect_final("Complex 3")


# Client JS
@app.route("/client-js")
def client_js():
    return render_template("client_js.html")


@app.route("/client-js-1")
def client_1():
    return redirect_final("Client JS 1")


# Client meta
@app.route("/client-meta")
def client_meta():
    return render_template("client_meta.html")


@app.route("/client-meta-1")
def client_meta_1():
    return redirect_final("Client Meta 1")


@app.route("/generic-redirect")
def generic_redirect():
    url = request.args.get("url")
    if not url:
        return abort(400)
    return redirect(url)


# Slow pages
@app.route("/slow-provision")
def slow_provision():
    time.sleep(20)
    return "Loaded"


@app.route("/slow-client-loading")
def slow_client():
    return render_template("slowpage.html")


# Forms
@app.route("/post-form", methods=["POST"])
def post_form():
    return redirect_final("Ok")
