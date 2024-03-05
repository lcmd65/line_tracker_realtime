from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class HomePage(QMainWindow):
    def __init__(self, parent = None):
        super().__init__()
        self.setWindowTitle("Home")
        self.resize(990, 540)
        self._createAction()
        self.set_external_variable()
        self.init_ui()
        self.set_object_style()

    def set_external_variable(self):
        pass
    
    def init_ui(self):
        self.main_layout = QFormLayout()
        self.main_layout.addItem()
        
        self.tool_bar = QBoxLayout()
        
    def set_object_style(self):
        pass
    
        