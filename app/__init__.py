from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    from app.models.compromisso_model import Compromisso

    from app.controllers.compromisso_controller import compromisso_bp
    app.register_blueprint(compromisso_bp)

    return app