
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
import os
import json


class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home")
        self.view = QWebEngineView()

        with open("app/schema.json", "r") as file:
            data = json.load(file)

        self._path = data["path"]
        self.html_path = os.path.join(self._path, "app/templates/home.html")
        self.css_path = os.path.join(self._path, "app/static/css/home.css")

        self.view = QWebEngineView()
        self.view.setHtml(open(self.html_path).read())

            
        self.view.loadFinished.connect(self.on_load_finished)
        self.setCentralWidget(self.view)
        
    def on_load_finished(self):
        self.view.setStyleSheet(open(self.css_path).read())
        
