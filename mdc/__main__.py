from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

def main():
    import mdc.controller.sync_settings
    app = QGuiApplication()
    engine = QQmlApplicationEngine()
    engine.load("mdc/ui/App.qml")
    engine.quit.connect(app.quit)
    app.exec()

    print("Hello, MetaDataCollector!")

if __name__ == "__main__":
    main()