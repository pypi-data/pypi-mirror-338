import os
import threading
import time
import logging
import click
import requests
import webbrowser
import keyring
import sys
from flask import Flask, request
from eocube.integrations.auth.client import ROCS_DISCOVERY_URL
from authlib.integrations.requests_client import OAuth2Session


EOCUBE_CLI_CLIENT_ID="eocube-cli"
EOCUBE_CLI_REDIRECT_URI="http://localhost:5123/callback"

login_done = threading.Event()

authorize_url = None
token_url = None
@click.group("auth")
def auth_cli():
    """Authentication related functionality"""


@auth_cli.command("login")
def login():
    """Login to EOCube.ro"""

    logging.getLogger('werkzeug').setLevel(logging.ERROR)

    app = Flask(__name__)
    server_thread = None


    def start_oauth_flow():
        global authorize_url
        global token_url
        oauth = OAuth2Session(EOCUBE_CLI_CLIENT_ID, redirect_uri=EOCUBE_CLI_REDIRECT_URI)
        metadata = requests.get(ROCS_DISCOVERY_URL).json()
        authorize_url = metadata["authorization_endpoint"]
        token_url = metadata["token_endpoint"]
        uri, state = oauth.create_authorization_url(
            authorize_url,
            scope='openid offline_access'
        )
        webbrowser.open(uri)
        return oauth

    def run_flask():
        app.run(port=5123, use_reloader=False)

    def shutdown_server():
        func = request.environ.get('werkzeug.server.shutdown')
        if func:
            func()

    @app.route("/callback")
    def callback():
        global oauth_token
        global token_url

        code = request.args.get("code")
        if not code:
            return "❌ No code received. Something went wrong."

        token = app.oauth_session.fetch_token(
            token_url,
            code=code
        )

        oauth_token = token  # salvează tokenul pt codul principal
        login_done.set()
        shutdown_server()  # oprește Flask


        return """
        ✅ Te-ai autentificat!<br><br>
        Poți închide fereastra.<br>
        Vezi terminalul pentru token-uri.
        """

    print("🚀 Începem loginul...")
    #global server_thread
    server_thread = threading.Thread(target=run_flask)
    server_thread.start()
    time.sleep(1)
    app.oauth_session = start_oauth_flow()
    login_done.wait()

    keyring.set_password("eocube-cli", "offline-refresh-token", oauth_token["refresh_token"])
    keyring.set_password("eocube-cli", "access-token",
                         oauth_token["access_token"])
    print("🔐 Saved tokens in keyring")
    os._exit(0)

