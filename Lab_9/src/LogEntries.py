# First task
import sys
sys.path.append("C:\\Users\\Kris\\Documents\\Studia\\Semestr_IV\\Jezyki_skryptowe_L\\Laboratoria\\Lab_9")

import re, sys
import ipaddress
from ipaddress import AddressValueError
from src.parse_log import parse_ssh_log
from src.Utils import *
import abc
from datetime import datetime
from typing import Optional, Dict, Any, List, Tuple

# Class that represents a single log
class SSHLogEntry(metaclass=abc.ABCMeta):
    # Constructor for a log represented by a raw log
    @abc.abstractmethod
    def __init__(self, log: str) -> None:
        log_dict: Dict[str, Any] = parse_ssh_log(log)
        self.timestamp: datetime = log_dict['timestamp']
        self.host: Optional[str] = get_user_from_log(log_dict['message'])
        self.process_name: str = log_dict['process_name']
        self.pid: int = log_dict['pid']
        self.message: str = log_dict['message']
        self._raw_log: str = log
    
    # To string method
    def __str__(self) -> str:
        user: Optional[str] = self.host
        if self.host is None or self.host=='unknown':
            user = "Uknown user"
        return f"{user} - {self.timestamp} {self.process_name}[{self.pid}]: {self.message}"

    def get_ipv4(self) -> Optional[ipaddress.IPv4Address]:
        ipv4_list: List[str] = get_ipv4s_from_log(self.message)
        if not ipv4_list:
            return None
        else:
            try:
                return ipaddress.IPv4Address(ipv4_list[0])
            except AddressValueError:
                return None
    
    @abc.abstractmethod
    def validate(self) -> bool:
        # print("Validating log: ", self.message)
        pass

    @property
    def has_ip(self) -> bool:
        return self.get_ipv4() is not None
    
    # __str__ goal is to be readable while __repr__ goal is to be unambigous
    def __repr__(self) -> str:
        reprString: str = f'SSHLogEntry({self.timestamp},{self.process_name},[{self.pid}],{self.message})'
        return reprString

    def __eq__(self, other: 'object') -> bool:
        if not isinstance(other, SSHLogEntry):
            return NotImplemented
        return self.timestamp == other.timestamp and self.message == other.message

    def __lt__(self, other: 'SSHLogEntry') -> bool:
        return (self.timestamp, self.message) < (other.timestamp, other.message)

    def __gt__(self, other: 'SSHLogEntry') -> bool:
        return (self.timestamp, self.message) > (other.timestamp, other.message)
        
class SSHLogEntryFailedPass(SSHLogEntry):

    def __init__(self, log: str) -> None:
        super().__init__(log)
        attributes: Optional[Tuple[str, str]] = failedPasswordArgs(self.message)
        if attributes is not None:
            self.address: str = attributes[0]
            self.port: str = attributes[1]
        # if not(attributes==None):
        #     self.address = attributes[0]
        #     self.port = attributes[1]

    def validate(self) -> bool:
        log_dict: Dict[str, Any] = parse_ssh_log(self._raw_log)
        attributes: Optional[Tuple[str,str]] = failedPasswordArgs(log_dict['message'])

        if attributes is not None: 
            return (self.timestamp == log_dict['timestamp']
                    and self.host == get_user_from_log(log_dict['message'])
                    and self.process_name == log_dict['process_name']
                    and self.pid == log_dict['pid']
                    and self.message == log_dict['message']
                    and self.address == attributes[0]
                    and self.port == attributes[1])
        return False

class SSHLogEntryAcceptedPass(SSHLogEntry):

    def __init__(self, log: str) -> None:
        super().__init__(log)
        attributes: Optional[Tuple[str,str]] = acceptedPasswordArgs(self.message)
        if attributes is not None:
            self.address: str = attributes[0]
            self.port: str = attributes[1]
        # if not(attributes==None):
        #     self.address = attributes[0]
        #     self.port = attributes[1]

    def validate(self) -> bool:
        log_dict: Dict[str, Any] = parse_ssh_log(self._raw_log)
        attributes: Optional[Tuple[str,str]] = acceptedPasswordArgs(log_dict['message'])
        if attributes is not None: 
            return (self.timestamp == log_dict['timestamp']
                    and self.host == get_user_from_log(log_dict['message'])
                    and self.process_name == log_dict['process_name']
                    and self.pid == log_dict['pid']
                    and self.message == log_dict['message']
                    and self.address == attributes[0]
                    and self.port == attributes[1])
        return False

class SSHLogEntryError(SSHLogEntry):

    def __init__(self, log: str) -> None:
        super().__init__(log)
        attributes: Optional[Tuple[str,str,str]] = errorArgs(self.message)
        if attributes is not None:
            self.address: str = attributes[0]
            self.errNumber: str = attributes[1]
            self.errMessage: str = attributes[2]

    def validate(self) -> bool:
        log_dict: Dict[str, Any] = parse_ssh_log(self._raw_log)
        attributes: Optional[Tuple[str,str,str]] = errorArgs(log_dict['message'])
        if attributes is not None: 
            return (self.timestamp == log_dict['timestamp']
                    and self.host == get_user_from_log(log_dict['message'])
                    and self.process_name == log_dict['process_name']
                    and self.pid == log_dict['pid']
                    and self.message == log_dict['message']
                    and self.address == attributes[0]
                    and self.errNumber == attributes[1]
                    and self.errMessage == attributes[2])
        return False
    
class SSHLogOther(SSHLogEntry):

    def __init__(self, log: str) -> None:
        super().__init__(log)

    def validate(self) -> bool:
        return True