import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from pathlib import Path


class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Home")
        view = QWebEngineView()

        html_content = Path(
            'app/templates/home.html').read_text(encoding="utf8")

        html_content = html_content.format(
            css_path = QUrl.fromLocalFile("app/static/css/home.css").toString())

        view.setHtml(html_content)
        self.setCentralWidget(view)
