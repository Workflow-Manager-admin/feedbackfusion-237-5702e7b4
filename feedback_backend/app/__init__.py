from flask import Flask
from flask_cors import CORS
from .routes.health import blp as health_blp
from .routes.feedback import blp as feedback_blp
from .routes.resume import blp as resume_blp
from .routes.cover_letter import blp as cover_letter_blp
from .routes.feedback_analysis import blp as feedback_analysis_blp
from .routes.dashboard import blp as dashboard_blp

from flask_smorest import Api
from .models import init_db
from .config import Config

app = Flask(__name__)

# Load config from config.py (reads env vars)
app.config.from_object(Config)

# CORS configuration
cors_origins = Config.CORS_ORIGINS
if cors_origins == "*" or not cors_origins:
    CORS(app, resources={r"/*": {"origins": "*"}})
else:
    # Support comma-separated origins
    origins = [origin.strip() for origin in cors_origins.split(",")]
    CORS(app, resources={r"/*": {"origins": origins}})

init_db()  # ensure DB & table exists

api = Api(app)
api.register_blueprint(health_blp)
api.register_blueprint(feedback_blp)
api.register_blueprint(resume_blp)
api.register_blueprint(cover_letter_blp)
api.register_blueprint(feedback_analysis_blp)
api.register_blueprint(dashboard_blp)
