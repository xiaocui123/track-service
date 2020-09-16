from flask import Flask

app = Flask(__name__)

from app.api import bp as api_bp
app.register_blueprint(api_bp)

from app import routes