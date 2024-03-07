import sys
from PyQt6.QtWidgets import (
    QApplication
)
from PyQt6.QtGui import (
    QIcon
)
import app.blogging.views.home
import flask
from flask import Flask, session
from api.api import api_blueprint

def main():
    app = Flask(__name__)
    app.config(
        {
            "PORT": "8080",
            "user": "dat",
            "password": "123456",
        }
    )
    app.blueprints()
    
    application = QApplication(sys.argv)
    app_icon = QIcon("app/static/images/app-icon.png")
    application.setWindowIcon(app_icon)
    screen = app.blogging.views.home.HomePage()
    screen.show()
    application.exec()
    