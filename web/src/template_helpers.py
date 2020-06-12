import os
import urllib.parse
from flask import url_for


APP_VERSION = os.getenv("APP_VERSION", "local-dev")


def setup_context_processors(app):
    @app.context_processor
    def app_version_processor():
        return dict(app_version=APP_VERSION)

    @app.context_processor
    def utilitity_processor():
        def url_for_redirect(url):
            return url_for('redir.generic', url=urllib.parse.quote(url, safe=''))

        def url_for_redirect_js(url):
            return url_for('redir.generic_js', url=urllib.parse.quote(url, safe=''))

        return dict(url_for_redirect=url_for_redirect,
                    url_for_redirect_js=url_for_redirect_js)
