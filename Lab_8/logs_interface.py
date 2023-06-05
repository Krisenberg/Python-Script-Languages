import sys
import re
from datetime import datetime
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QPlainTextEdit, QTextEdit, QMainWindow, QListWidget, QListWidgetItem, QMessageBox
from PySide6.QtGui import QColor, QPalette
from utils import parse_ssh_log, get_user_from_log

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
        self.setGeometry(200, 30, 800, 800)
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
        self.load_button.clicked.connect(self.printLogs)

        self.start_label = QLabel('Start time (MM-DD HH:MM:SS):')
        self.start_edit = QLineEdit()
        self.end_label = QLabel('End time (MM-DD HH:MM:SS):')
        self.end_edit = QLineEdit()
        self.filter_button = QPushButton('Filter logs')
        self.filter_button.clicked.connect(self.print_filtrated_logs)

        self.logs_list = QListWidget()
        self.timestamp_label = QLabel('Timestamp:')
        self.timestamp_edit = QLineEdit()
        self.timestamp_edit.setReadOnly(True)
        self.host_label = QLabel('Host:')
        self.host_edit = QLineEdit()
        self.host_edit.setReadOnly(True)
        self.component_label = QLabel('Component:')
        self.component_edit = QLineEdit()
        self.component_edit.setReadOnly(True)
        self.pid_label = QLabel('PID:')
        self.pid_edit = QLineEdit()
        self.pid_edit.setReadOnly(True)
        self.message_label = QLabel('Message:')
        self.message_edit = QTextEdit()
        self.message_edit.setReadOnly(True)
        self.logs_list.itemClicked.connect(self.showLogDetails)
        
        self.clear_button = QPushButton('Clear logs')
        self.clear_button.clicked.connect(self.clearLogs)

        self.next_button = QPushButton('Next')
        self.next_button.setEnabled(False)
        self.next_button.clicked.connect(self.showNextLog)
        self.previous_button = QPushButton('Previous')
        self.previous_button.setEnabled(False)
        self.previous_button.clicked.connect(self.showPreviousLog)
        self.current_log_index = -1

        self.layout = QVBoxLayout()
        path_layout = QHBoxLayout()
        path_layout.addWidget(self.path_label)
        path_layout.addWidget(self.path_edit)
        path_layout.addWidget(self.load_button)
        self.layout.addLayout(path_layout)
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(self.start_label)
        filter_layout.addWidget(self.start_edit)
        filter_layout.addWidget(self.end_label)
        filter_layout.addWidget(self.end_edit)
        filter_layout.addWidget(self.filter_button)
        self.layout.addLayout(filter_layout)
        self.layout.addWidget(self.logs_list)
        self.layout.addWidget(self.clear_button)
        details_layout = QVBoxLayout()
        details_layout.addWidget(self.timestamp_label)
        details_layout.addWidget(self.timestamp_edit)
        details_layout.addWidget(self.host_label)
        details_layout.addWidget(self.host_edit)
        details_layout.addWidget(self.component_label)
        details_layout.addWidget(self.component_edit)
        details_layout.addWidget(self.pid_label)
        details_layout.addWidget(self.pid_edit)
        details_layout.addWidget(self.message_label)
        details_layout.addWidget(self.message_edit)
        self.layout.addLayout(details_layout)
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.previous_button)
        button_layout.addWidget(self.next_button)
        self.layout.addLayout(button_layout)
        
        self.main_widget.setLayout(self.layout)

    def loadLogs(self):
        path = self.path_edit.text()
        self.storage.readLogs(path)

    def printLogs(self):
        logs = self.storage.giveLogs()
        self.logs_list.clear()
        for log in logs:
            item = QListWidgetItem(log)
            self.logs_list.addItem(item)
        self.next_button.setEnabled(len(logs) > 0)
        self.previous_button.setEnabled(len(logs) > 0)
            
    def print_filtrated_logs(self):
        logs = self.storage.giveLogs()
        start_time_str = self.start_edit.text()
        end_time_str = self.end_edit.text()
        if start_time_str and end_time_str:
            start_time = datetime.strptime(start_time_str, '%m-%d %H:%M:%S')
            end_time = datetime.strptime(end_time_str, '%m-%d %H:%M:%S')
            logs = [log for log in logs if parse_ssh_log(log)['timestamp'] >= start_time and parse_ssh_log(log)['timestamp'] <= end_time]
        self.logs_list.clear()
        for log in logs:
            item = QListWidgetItem(log) 
            self.logs_list.addItem(item)
        self.next_button.setEnabled(len(logs) > 0)
        self.previous_button.setEnabled(len(logs) > 0)
        
    def clearLogs(self):
        self.logs_list.clear()    
    
    def showNextLog(self):
        if self.current_log_index + 1 < self.logs_list.count():
            self.current_log_index += 1
            log_item = self.logs_list.item(self.current_log_index)
            self.logs_list.setCurrentItem(log_item)
            self.showLogDetails(log_item)
            self.previous_button.setEnabled(True)

        self.next_button.setEnabled(self.current_log_index + 1 < self.logs_list.count())

    def showPreviousLog(self):
        if self.current_log_index - 1 >= 0:
            self.current_log_index -= 1
            log_item = self.logs_list.item(self.current_log_index)
            self.logs_list.setCurrentItem(log_item)
            self.showLogDetails(log_item)
            self.next_button.setEnabled(True)

        self.previous_button.setEnabled(self.current_log_index - 1> 0)
        
    def showLogDetails(self, item):
        log_details = parse_ssh_log(item.text())
        self.current_log_index = self.logs_list.currentRow()
        self.next_button.setEnabled(self.current_log_index + 1 < self.logs_list.count())
        self.previous_button.setEnabled(self.current_log_index > 0)
        self.timestamp_edit.setText(log_details['timestamp'].strftime('%m-%d %H:%M:%S'))
        self.host_edit.setText(log_details['host'])
        self.component_edit.setText(log_details['component'])
        self.pid_edit.setText(str(log_details['pid']))
        self.message_edit.setText(log_details['message'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = LogViewer()
    viewer.show()
    sys.exit(app.exec())