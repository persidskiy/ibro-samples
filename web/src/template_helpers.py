import os
import urllib.parse
from flask import url_for
from file_download import is_cookie_set


APP_VERSION = os.getenv("APP_VERSION")


def setup_context_processors(app):
    @app.context_processor
    def app_state_processor():
        return dict(app_version=APP_VERSION, download_cookie_is_set=is_cookie_set())

    @app.context_processor
    def utilitity_processor():
        def url_for_redirect(url):
            return url_for("redir.generic", url=urllib.parse.quote(url, safe=""))

        def url_for_redirect_js(url):
            return url_for("redir.generic_js", url=urllib.parse.quote(url, safe=""))

        def get_fragment(string):
            return string.lower().replace(" ", "-")

        return dict(
            url_for_redirect=url_for_redirect,
            url_for_redirect_js=url_for_redirect_js,
            get_fragment=get_fragment,
        )
