import sys
from PyQt6.QtWidgets import (
    QApplication
)
from PyQt6.QtGui import (
    QIcon
)
import app.blogging.views.home

def main():
    application = QApplication(sys.argv)
    app_icon = QIcon("app/static/images/app-icon.png")
    application.setWindowIcon(app_icon)
    screen = app.blogging.views.home.HomePage()
    screen.show()
    application.exec()
    