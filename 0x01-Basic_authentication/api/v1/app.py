#!/usr/bin/env python3
"""
Route module for the API
"""
from api.v1.auth.auth import Auth
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
authentication = getenv('AUTH_TYPE', 'auth')
if authentication == 'auth':
    auth = Auth()
if authentication == 'basic_auth':
    auth = BasicAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found (404) event handler"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Unauthorized error (401) event handler"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden error (403) event handler"""
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def authenticate():
    """func that authenticates a user"""
    if auth:
        excluded_paths = [
            'api/v1/status/',
            '/api/v1/unauthorized/',
            '/api/v1/forbidden/',
        ]

    if auth.require_auth(request.path, excluded_paths):
        header = auth.authorization_header(request)
        user = auth.current_user(request)

        if header is None:
            abort(401)
        if user is None:
            abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
