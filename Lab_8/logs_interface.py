import sys
import re
from datetime import datetime
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QPlainTextEdit, QTextEdit, QMainWindow, QListWidget, QListWidgetItem, QMessageBox
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
        self.setGeometry(500, 500, 500, 500)
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
        self.logs_list.itemClicked.connect(self.showLogDetails)
        
        self.clear_button = QPushButton('Clear logs')
        self.clear_button.clicked.connect(self.clearLogs)

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
            
    def print_filtrated_logs(self):
        logs = self.storage.giveLogs()
        start_time_str = self.start_edit.text()
        end_time_str = self.end_edit.text()
        if start_time_str and end_time_str:
            start_time = datetime.strptime(start_time_str, '%m-%d %H:%M:%S')
            end_time = datetime.strptime(end_time_str, '%m-%d %H:%M:%S')
            logs = [log for log in logs if self.parse_ssh_log(log)['timestamp'] >= start_time and self.parse_ssh_log(log)['timestamp'] <= end_time]
        self.logs_list.clear()
        for log in logs:
            item = QListWidgetItem(log)
            self.logs_list.addItem(item)
        
    def clearLogs(self):
        self.logs_list.clear()
        
    def showLogDetails(self, item):
        log_details = self.parse_ssh_log(item.text())
        message_box = QMessageBox()
        message_box.setWindowTitle('Log Details')
        message_box.setText(f"Timestamp: {log_details['timestamp']}\nHost: {log_details['host']}\nComponent: {log_details['component']}\nPID: {log_details['pid']}\nMessage: {log_details['message']}")
        message_box.exec()

    def get_user_from_log(self, message):
        # If message is empty return None
        if message is None:
            return None
        # Define regex pattern for username
        username_pattern = r"user (\w+)"
        match = re.search(username_pattern, message)
        if match:
            return match.group(1)
        # If previous pattern didn't match try another one
        else:
            username_pattern = r"user=(\w+)"
            match = re.search(username_pattern, message)
            if match:
                return match.group(1)
            # If previous pattern didn't match try another one
            else:
                username_pattern = r"for (\w+)"
                match = re.search(username_pattern, message)
                if match:
                    return match.group(1)
        return None


    # Function that parses a log represented by a string to a dictionary
    def parse_ssh_log(self, log_string):
        # Define regex pattern
        pattern = r'^(.+)\s(\d+)\s(\d{2}:\d{2}:\d{2})\s(.+)\s(sshd)\[(\d+)\]:\s(.+)$'
        match = re.match(pattern, log_string)
        stringDate = match.group(1) + ' ' + match.group(2) + ' ' + match.group(3)
        # fullDate is a datetime object in format "1900 Jan 01 00:00:00" (year is not important)
        date = datetime.strptime(stringDate,"%b %d %H:%M:%S")
        component = match.group(5)
        pid = match.group(6)
        message = match.group(7)
        host = self.get_user_from_log(message)
        namesList = ['timestamp','host','component','pid','message']
        valuesList = [date, host, component, int(pid), message]
        return dict(zip(namesList, valuesList))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = LogViewer()
    viewer.show()
    sys.exit(app.exec())