from flask import Blueprint, redirect, render_template, url_for, request
import urllib.parse


bp = Blueprint("redir", __name__, url_prefix="/redir")


@bp.route("/simple")
def simple():
    return redirect(url_for("redir.final", text="Simple redirect final"), code=302)


@bp.route("/two-http/1")
def two_http():
    return redirect(url_for("redir.two_http_2"), code=302)


@bp.route("/two-http/2")
def two_http_2():
    return redirect(url_for("redir.final", text="Two redirects final"), code=302)


# Complex
@bp.route("/complex/1")
def complex_1():
    return redirect(url_for("redir.complex_2"), code=302)


@bp.route("/complex/2")
def complex_2():
    return render_template(
        "client_redir.html",
        type="js",
        url=url_for("redir.final", text="Final complex redirect"),
    )


@bp.route("/client/js")
def client_js():
    return render_template(
        "client_redir.html",
        type="js",
        url=url_for("redir.final", text="Final js cliet redirect"),
    )


@bp.route("/client/meta")
def client_meta():
    return render_template(
        "client_redir.html",
        type="meta",
        url=url_for("redir.final", text="Final meta client redirect"),
    )


@bp.route("/final")
def final():
    text = request.args.get("text", "Redirected")
    return render_template("final.html", page_title=text, text=text)


@bp.route("/generic")
def generic():
    url = request.args.get('url', None)
    if url is None:
        return 404
    url = urllib.parse.unquote(url)
    return redirect(url, code=302)


@bp.route("/generic-js")
def generic_js():
    url = request.args.get('url', None)
    if url is None:
        return 404
    url = urllib.parse.unquote(url)
    return render_template("client_redir.html", type="js", url=url)
