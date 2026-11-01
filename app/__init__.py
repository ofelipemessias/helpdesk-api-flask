import os

from flask import Flask

from .models import db
from .routes import tickets_bp


def create_app(config=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
        "DATABASE_URL", "sqlite:///helpdesk.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    if config:
        app.config.update(config)

    db.init_app(app)
    app.register_blueprint(tickets_bp)

    with app.app_context():
        db.create_all()

    return app
