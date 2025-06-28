from flask import Flask
from flask_cors import CORS
from .routes.health import blp as health_blp
from .routes.feedback import blp as feedback_blp
from flask_smorest import Api
from .models import init_db

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config["API_TITLE"] = "My Flask API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config['OPENAPI_URL_PREFIX'] = '/docs'
app.config["OPENAPI_SWAGGER_UI_PATH"] = ""
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

init_db()  # ensure DB & table exists

api = Api(app)
api.register_blueprint(health_blp)
api.register_blueprint(feedback_blp)
