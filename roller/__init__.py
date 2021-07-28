from flask import *
from flask_sqlalchemy import *
from roller.config import Config


db = SQLAlchemy()


def activate(config_class = Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from roller.main.routes import main
    from roller.profiles.routes import profiles
    from roller.options.routes import options
    from roller.errors.handlers import errors
    app.register_blueprint(main)
    app.register_blueprint(profiles)
    app.register_blueprint(options)
    app.register_blueprint(errors)

    return app
