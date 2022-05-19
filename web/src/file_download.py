from flask import Blueprint, request, redirect, abort, send_file, url_for, send_from_directory

bp = Blueprint("file_download", __name__, url_prefix="/file-download")

COOKIE_NAME = "file-download-enabled"

def is_cookie_set():
    return request.cookies.get(COOKIE_NAME, default="false") == "true"


def do_set_cookie(resp, val):
   resp.set_cookie(COOKIE_NAME, "true" if val else "false")


@bp.route("/set-cookie", methods=["POST"])
def set_cookie():
    if is_cookie_set():
        abort(400)

    resp = redirect(url_for('home'))
    do_set_cookie(resp, True)
    return resp


@bp.route("/unset-cookie", methods=["POST"])
def unset_cookie():
    if not is_cookie_set():
        abort(400)

    resp = redirect(url_for('home'))
    do_set_cookie(resp, False)
    return resp

@bp.route("/")
def download():
    filename = request.args.get('filename', None)
    as_attachment = request.args.get('as_attachment', None) is not None
    check_cookie = request.args.get('check_cookie', None) is not None
    if not filename:
        abort(400)

    if check_cookie and not is_cookie_set():
        abort(401)
    
    return send_from_directory('static/files', filename, as_attachment=as_attachment)