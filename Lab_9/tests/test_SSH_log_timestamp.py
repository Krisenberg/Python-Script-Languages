import pytest
import sys
from datetime import datetime

sys.path.append("C:\\Users\\Kris\\Documents\\Studia\\Semestr_IV\\Jezyki_skryptowe_L\\Laboratoria\\Lab_9")

from src.Factory import Factory_Manager
from src.LogEntries import SSHLogEntry

def test_timestamp_extraction():
    raw_log = 'Dec 10 07:07:38 LabSZ sshd[24206]: pam_unix(sshd:auth): check pass; user unknown'
    entry: SSHLogEntry = Factory_Manager.create_log(raw_log)
    expected_timestamp = datetime(1900,12,10,7,7,38)
    assert entry.timestamp == expected_timestamp
