from flask import Blueprint, redirect, render_template, url_for, request
import urllib.parse
import json


bp = Blueprint("forms", __name__, url_prefix="/forms")


@bp.route("/signin")
def signin_username():
    return render_template(
        'forms/signin_username.html',
        menu='forms',
        forms_menu="signin_username",
        page_title="SignIn via Username")

@bp.route("/signin-email")
def signin_email():
    return render_template(
        'forms/signin_email.html',
        menu='forms',
        forms_menu="signin_email",
        page_title="SignIn via Email")


@bp.route("/signup")
def signup_username():
    return render_template(
        'forms/signup_username.html',
        menu='forms',
        forms_menu="signup_username",
        page_title="SignUp via Username")


@bp.route("/change-password")
def change_password():
    return render_template(
        'forms/change_password.html',
        menu='forms',
        forms_menu="change_password",
        page_title="Change Password")

def respond_to_submit():
    form_json_str = json.dumps(request.form.to_dict(), indent=2)
    return render_template(
        'forms/login_resp.html',
        menu='forms',
        form_json_str=form_json_str,
        page_title=request.args.get('title', 'Ok'))

@bp.route("/other")
def other():
    return render_template(
        'forms/other_forms.html',
        menu='forms',
        forms_menu="other_forms",
        page_title="Ohter Forms")

@bp.route("/handle-login", methods=["POST"])
def handle_login():
    return respond_to_submit()


@bp.route("/handle-signup", methods=["POST"])
def handle_signup():
    return respond_to_submit()


@bp.route("/handle-change", methods=["POST"])
def handle_change():
    return respond_to_submit()
