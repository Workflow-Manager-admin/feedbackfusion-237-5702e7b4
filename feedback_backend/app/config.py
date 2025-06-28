"""
config.py

Loads all application configuration from environment variables. Used for global
app settings, Kavai API keys, Flask configuration, and CORS support.

Secrets and configuration can be set in a `.env` file in the backend root.
"""

import os
from dotenv import load_dotenv


# Load environment variables from .env if present
load_dotenv()


class Config:
    """Flask app configuration, loaded from environment variables."""

    # Core Flask settings
    SECRET_KEY = os.environ.get("SECRET_KEY", "not-so-secret-key")  # For session signing

    # API URLs and keys
    BASE_URL = os.environ.get("BASE_URL", "http://127.0.0.1:5000")
    KAVAI_API_KEY = os.environ.get("KAVAI_API_KEY", "")            # Your Kavai API key
    KAVAI_API_URL = os.environ.get("KAVAI_API_URL", "")            # Kavai endpoint

    # CORS support: comma-separated list of allowed origins, or '*' for all
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "*")

    # Flask-Smorest/OpenAPI
    API_TITLE = os.environ.get("API_TITLE", "My Flask API")
    API_VERSION = os.environ.get("API_VERSION", "v1")
    OPENAPI_VERSION = os.environ.get("OPENAPI_VERSION", "3.0.3")
    OPENAPI_URL_PREFIX = os.environ.get("OPENAPI_URL_PREFIX", "/docs")
    OPENAPI_SWAGGER_UI_PATH = os.environ.get("OPENAPI_SWAGGER_UI_PATH", "")
    OPENAPI_SWAGGER_UI_URL = os.environ.get(
        "OPENAPI_SWAGGER_UI_URL",
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )

    # Other settings...
    # Add more environment-driven configuration as needed
