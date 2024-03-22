from flask import Flask, request, make_response
from flask_talisman import Talisman


def setup_security(app: Flask):
    # Setup Flask-Talisman for most security headers
    Talisman(app, content_security_policy=None)  # Customize the CSP as needed

    @app.after_request
    def add_security_headers(response):
        # Example of manually adding headers if needed
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-XSS-Protection'] = '1; mode=block'

        # CORS headers setup, adjust according to your CORS policy
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'

        return response
