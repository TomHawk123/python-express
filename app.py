from flask import Flask
import os
from app import create_app  # Assuming you have a function to create your Flask app

app = create_app()  # Create your Flask app instance

if __name__ == "__main__":
    # Note: Gunicorn will not use this way to run the application.
    # This is only for running a development server locally.
    PORT = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=PORT)
