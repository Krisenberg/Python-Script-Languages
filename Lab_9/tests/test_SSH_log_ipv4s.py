import pytest
import sys
from ipaddress import IPv4Address

sys.path.append("C:\\Users\\Kris\\Documents\\Studia\\Semestr_IV\\Jezyki_skryptowe_L\\Laboratoria\\Lab_9")
# from src import decorator_logging

from Factory import Factory_Manager
from LogEntries import SSHLogEntry


class TestIPv4Addresses:

    def testCorrectIPv4(self):
        raw_log = 'Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186 port 38926 ssh2'
        entry: SSHLogEntry = Factory_Manager.create_log(raw_log)
        expected_IPv4 = IPv4Address('173.234.31.186')
        assert entry.get_ipv4() == expected_IPv4

    def testIncorrectIPv4(self):
        raw_log = 'Dec 10 06:55:48 LabSZ sshd[24200]: Failed password for invalid user webmaster from 666.777.88.213 port 38926 ssh2'
        entry: SSHLogEntry = Factory_Manager.create_log(raw_log)
        # expected_IPv4 = IPv4Address('666.777.88.213')
        assert entry.get_ipv4() == None

    def testNoIPv4(self):
        raw_log = 'Dec 10 07:08:28 LabSZ sshd[24208]: input_userauth_request: invalid user webmaster [preauth]'
        entry: SSHLogEntry = Factory_Manager.create_log(raw_log)
        assert entry.get_ipv4() == None

    def testAllCases(self):
        self.testCorrectIPv4()
        self.testIncorrectIPv4()
        self.testNoIPv4()