from PyQt5.QAxContainer import *


class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()

        self.get_instance()
        self.event_slot()

        self.signal_login()

    def get_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")

    def event_slot(self):
        self.OnEventConnect.connect(self.login_slot)

    def login_slot(self, errCode):
        print(errCode)

    def signal_login(self):
        self.dynamicCall("CommConnect()")
