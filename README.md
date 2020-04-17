# kiwoom

**Error msg below**   
Traceback (most recent call last):
  File "C:/Users/jackp/PycharmProjects/kiwoom/__init__.py", line 10, in <module>
    Main()
  File "C:/Users/jackp/PycharmProjects/kiwoom/__init__.py", line 7, in __init__
    UI_class()
  File "C:\Users\jackp\PycharmProjects\kiwoom\ui\ui.py", line 11, in __init__
    Kiwoom()
  File "C:\Users\jackp\PycharmProjects\kiwoom\kiwoom\kiwoom.py", line 8, in __init__
    self.event_slot()
  File "C:\Users\jackp\PycharmProjects\kiwoom\kiwoom\kiwoom.py", line 16, in event_slot
    self.OnEventConnect.connect(self.login_slot)
AttributeError: 'Kiwoom' object has no attribute 'OnEventConnect'
