import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget
from PySide6.QtGui import QColor, QPalette

palette = QPalette()

def greet():
    name = name_input.text()
    greeting = "Hello, " + name + "!"
    greeting_label.setText(greeting)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello App")
        
        # create a main widget and set its background color
        main_widget = QWidget(self)
        palette.setColor(QPalette.Window, QColor(255, 255, 255))
        main_widget.setAutoFillBackground(True)
        main_widget.setPalette(palette)
        
        self.setCentralWidget(main_widget)

app = QApplication(sys.argv)
window = QMainWindow()

name_label = QLabel("Enter your name:")
name_input = QLineEdit()
button = QPushButton("Say Hello")
button.setStyleSheet("border-radius: 1px;")
button.setGeometry(50, 50, 100, 50)
palette.setColor(QPalette.Window, QColor(255, 255, 255))
button.setAutoFillBackground(True)
button.setPalette(palette)
greeting_label = QLabel()

layout = QVBoxLayout()
layout.addWidget(name_label)
layout.addWidget(name_input)
layout.addWidget(button)
layout.addWidget(greeting_label)

widget = QWidget()
widget.setLayout(layout)
palette.setColor(QPalette.Window, QColor(255, 255, 255))
widget.setAutoFillBackground(True)
widget.setPalette(palette)
window.setCentralWidget(widget)

button.clicked.connect(greet)
window.show()
sys.exit(app.exec())
