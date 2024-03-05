import sys
from PyQt6.QtWidgets import (
    QApplication
)
import app

if __name__ == "__main__":
    screen = app.templates.home.HomePage()
    application = QApplication(sys.argv)
    screen.show()
    application.exec()
    