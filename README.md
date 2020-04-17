# kiwoom

== Error msg below ==
Traceback (most recent call last):
  File "C:/Users/jackp/PycharmProjects/kiwoom/__init__.py", line 10, in <module>
    Main()
  File "C:/Users/jackp/PycharmProjects/kiwoom/__init__.py", line 7, in __init__
    UI_class()
  File "C:\Users\jackp\PycharmProjects\kiwoom\ui\ui.py", line 11, in __init__
    Kiwoom()
  File "C:\Users\jackp\PycharmProjects\kiwoom\kiwoom\kiwoom.py", line 10, in __init__
    self.kiwoom.OnEventConnect.connect(self.login_event)
AttributeError: 'QAxWidget' object has no attribute 'OnEventConnect'
