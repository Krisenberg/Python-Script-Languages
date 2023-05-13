import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QPlainTextEdit, QTextEdit, QMainWindow
from PySide6.QtGui import QColor, QPalette

class LogStorage:
    def __init__(self):
        self.logs = []

    def readLogs(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                self.logs.append(line)

    def giveLogs(self):
        return self.logs

class LogViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Log Viewer')
        self.setGeometry(300, 300, 500, 500)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
    
        self.main_widget = QWidget()
        self.main_widget.setAutoFillBackground(True)
        self.main_widget.setPalette(palette)
        self.setCentralWidget(self.main_widget)

        self.storage = LogStorage()

        self.path_label = QLabel('Path to log file:')
        self.path_edit = QLineEdit()
        self.load_button = QPushButton('Load logs')
        self.load_button.clicked.connect(self.loadLogs)

        self.logs_field = QTextEdit()
        self.print_button = QPushButton('Print logs')
        self.print_button.clicked.connect(self.printLogs)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.path_label)
        self.layout.addWidget(self.path_edit)
        self.layout.addWidget(self.load_button)
        self.layout.addWidget(self.print_button)
        self.layout.addWidget(self.logs_field)

        self.main_widget.setLayout(self.layout)

    def loadLogs(self):
        path = self.path_edit.text()
        self.storage.readLogs(path)

    def printLogs(self):
        logs = self.storage.giveLogs()
        self.logs_field.setText(''.join(logs))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = LogViewer()
    viewer.show()
    sys.exit(app.exec())