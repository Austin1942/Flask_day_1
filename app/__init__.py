from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config 
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# app instaniation

login = LoginManager()
login.login_view = 'auth.login'
datab = SQLAlchemy()

migrate = Migrate()
def create_app(config_class=Config):
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(config_class)
    login.init_app(app)
    datab.init_app(app)
    migrate.init_app(app, datab)
    from .blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)
    from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    return app