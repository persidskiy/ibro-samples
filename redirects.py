import os
from flask import Flask,redirect, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

# Simple HTTP
@app.route('/simple')
def simple():
    return redirect("/simple-1", code=302)

@app.route('/simple-1')
def simple_1():
    return "Simple 1"

# Two HTTP
@app.route('/two-http')
def two_http():
    return redirect("/two-http-1", code=302)

@app.route('/two-http-1')
def two_http_1():
    return redirect("two-http-2")

@app.route('/two-http-2')
def two_http_2():
    return "Two HTTP"


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
    return "Complex 3"

# Client JS
@app.route("/client-js")
def client_js():
    return render_template("client_js.html")

@app.route("/client-js-1")
def client_1():
    return "Client JS 1"

# Client meta
@app.route("/client-meta")
def client_meta():
    return render_template("client_meta.html")

@app.route("/client-meta-1")
def client_meta_1():
    return "Client Meta 1"

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
