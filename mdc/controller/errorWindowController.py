from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject,Signal,Slot,Property

app = QGuiApplication()
engine = QQmlApplicationEngine()

class ErrorController(QObject):
    errorTextChanged = Signal()
    titleTextChanged = Signal()

    def __init__(self):
        self._errorText = None
        self._titleText = None
        super().__init__()

    @Slot()
    def init_screen(self):
        pass

    @Property(str, notify=titleTextChanged)
    def titleText(self):
        return self._titleText

    @titleText.setter
    def titleText(self, value):
        self._titleText = value
        self.titleTextChanged.emit()

    @Property(str, notify=errorTextChanged)
    def errorText(self):
        return self._errorText

    @errorText.setter
    def errorText(self, value):
        self._errorText = value
        self.errorTextChanged.emit()

eCtrl = ErrorController()
