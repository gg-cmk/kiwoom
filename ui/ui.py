import sys
from PyQt5.QtWidgets import *
from kiwoom.kiwoom import *

class UI_class():
    def __init__(self):
        print("ui class입니다")

        self.app = QApplication(sys.argv)

        Kiwoom()

        self.app.exec_()