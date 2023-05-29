import pytest
import sys

#insert the path of modules folder
sys.path.append("C:\\Users\\Kris\\Documents\\Studia\\Semestr_IV\\Jezyki_skryptowe_L\\Laboratoria\\Lab_9")
from Journal import SSHLogJournal
from LogEntries import SSHLogEntryAcceptedPass, SSHLogEntryError, SSHLogEntryFailedPass, SSHLogOther 

@pytest.fixture(scope='module')
def journal():
    return SSHLogJournal()

@pytest.mark.parametrize(
    "raw_log, expected_type",
    [
        ('Dec 10 09:32:20 LabSZ sshd[24680]: Accepted password for fztu from 119.137.62.142 port 49116 ssh2', SSHLogEntryAcceptedPass),
        ('Dec 10 11:03:40 LabSZ sshd[25448]: error: Received disconnect from 103.99.0.122: 14: No more user authentication methods available. [preauth]', SSHLogEntryError),
        ('Dec 10 07:51:15 LabSZ sshd[24324]: error: Received disconnect from 195.154.37.122: 3: com.jcraft.jsch.JSchException: Auth fail [preauth]', SSHLogEntryError),
        ('Dec 10 07:07:45 LabSZ sshd[24206]: Failed password for invalid user test9 from 52.80.34.196 port 36060 ssh2', SSHLogEntryFailedPass),
        ('Dec 10 07:53:26 LabSZ sshd[24329]: Connection closed by 194.190.163.22 [preauth]', SSHLogOther),
        ('Dec 10 07:55:55 LabSZ sshd[24331]: Invalid user test from 52.80.34.196', SSHLogOther),
        ('Dec 10 09:07:56 LabSZ sshd[24417]: pam_unix(sshd:auth): check pass; user unknown', SSHLogOther)
    ] 
)
def test_append(raw_log, expected_type, journal):
    #journal: SSHLogJournal = SSHLogJournal()
    assert journal.append(raw_log) and type(journal.logList[-1]) == expected_type