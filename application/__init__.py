from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
# from flask_login import LoginManager
# from flask_assets import Environment
# from .assets import compile_assets



# Globally accessible libraries
db = SQLAlchemy()
r = FlaskRedis()
# login_manager = LoginManager()
# assets = Environment()

def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    r.init_app(app)
    # login_manager.init_app(app)
    # assets.init_app(app)
    

    with app.app_context():
        # Include Routes
        from .home import routes
        from .projects import routes
        from .faq import routes
        from .about import routes
        from .contact import routes
        from . import auth

        # db.create_all()

        # Register Blueprints
        app.register_blueprint(home.routes.home_bp)
        app.register_blueprint(projects.routes.projects_bp)
        app.register_blueprint(faq.routes.faq_bp)
        app.register_blueprint(about.routes.about_bp)
        app.register_blueprint(contact.routes.contact_bp)
        app.register_blueprint(auth.auth_bp)

        # compile_assets(assets)

        return app