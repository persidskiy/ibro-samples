from flask import Blueprint, redirect, render_template, url_for, request

bp = Blueprint("pages", __name__, url_prefix="/pages")


@bp.route("/")
def pages():
    return render_template("pages/index.html", page_title="Testing Pages", menu="pages")


@bp.route("/readability")
def readability():
    return render_template(
        "pages/readability.html", page_title="Readability Markup testing", menu="pages",
    )


@bp.route("/youtube")
def youtube():
    return render_template(
        "pages/youtube.html", page_title="YouTube embeds", menu="pages",
    )

@bp.route("/videos")
def videos():
    return render_template(
        "pages/videos.html", page_title="Videos", menu="pages",
    )

@bp.route("/dark-mode")
def dark_mode():
    return render_template(
        "pages/dark_mode.html", page_title="Dark Mode", menu="pages",
    )

