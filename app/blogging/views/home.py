from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtWebEngineWidgets
from pathlib import Path


class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Feelings App Prototype")

        view = QtWebEngineWidgets.QWebEngineView()
        html = Path('app/templates/home.html').read_text(encoding="utf8")
        view.setHtml(html)
        self.setCentralWidget(view)

