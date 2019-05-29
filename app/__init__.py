from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('app.conf')
    db.init_app(app)
    from .api.wxlogin import wx_login_api as wx_login_api_blueprint
    app.register_blueprint(wx_login_api_blueprint)
    from .api.classes import classes_api as classes_api_blueprint
    app.register_blueprint(classes_api_blueprint)
    from .api.chapters import chapters_api as chapters_api_blueprint
    app.register_blueprint(chapters_api_blueprint)
    from .api.musics import muiscs_api as muiscs_api_blueprint
    app.register_blueprint(muiscs_api_blueprint)
    from .api.vedios import vedios_api as vedios_api_blueprint
    app.register_blueprint(vedios_api_blueprint)
    return app
