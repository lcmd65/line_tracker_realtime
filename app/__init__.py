
import sys
import os
from flask import (Flask,
                   Blueprint,
                   render_template,
                   redirect, request,
                   url_for)
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from openai import OpenAI
import warnings
warnings.filterwarnings("ignore")
import app.blogging.views.home
from PyQt6.QtWidgets import QApplication, QIcon

def main():
    app = Flask(__name__, instance_relative_config= True)
    app.config.from_mapping(
        SECRET_KEY='unilever',
        DATABASE= os.path.join(app.instance_path, 'flaskr.sqlite'),
        CACHE_TYPE='FileSystemCache',
        CACHE_DIR='cache',
        CACHE_THRESHOLD=100000,
    )
    from app.blogging.views.home import home
    from app.authentication.views.authen import authen
    app.register_blueprint(home)
    app.register_blueprint(authen)
    application = QApplication(sys.argv)
    app_icon = QIcon("app/static/images/app-icon.png")
    application.setWindowIcon(app_icon)
    screen = app.blogging.views.home.HomePage()
    screen.show()
    application.exec()
    