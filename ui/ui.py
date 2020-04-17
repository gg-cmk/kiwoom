import sys
from PyQt5.QtWidgets import *
from kiwoom.kiwoom import *


class UIclass():
    def __init__(self):
        print("ui class입니다")

        self.app = QApplication(sys.argv)

        Kiwoom()

        self.app.exec_()