from sys import _getframe
import logging.handlers
import os
from threading import Lock
from enum import Enum
import logging
from logging.handlers import RotatingFileHandler

DEFAULT_BACKUP_COUNT_LOG:int = 20
MEGA_BYTE:int = 1 * 1024 * 1024
LOG_DIR:str = 'logs'

class TypeLogging(Enum):
    DEBUG = 0
    INFO = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4
    NOTSET = 5

if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

currentFuncName = lambda n=0: _getframe(n + 1).f_code.co_name

size_main_log_file = 10 * 1024 * 1024
handler = RotatingFileHandler(f"{LOG_DIR}/__system__.log", maxBytes=size_main_log_file, backupCount=DEFAULT_BACKUP_COUNT_LOG)
logging.basicConfig(encoding='utf-8', 
                    level=logging.DEBUG, 
                    format='%(asctime)s | %(name)s | %(levelname)s | %(thread)d | %(message)s', 
                    handlers=[handler])

class SysLogging():
    def __init__(self, filename:str, logging_level=TypeLogging.INFO, size_log:int=10, backupCount:int=DEFAULT_BACKUP_COUNT_LOG):
        self.__lock = Lock()  
        self.__filename = f'{LOG_DIR}/{filename}.log'
        
        match(logging_level):
            case TypeLogging.INFO:
                level_log = logging.INFO
            case TypeLogging.DEBUG:
                level_log = logging.DEBUG
            case TypeLogging.WARNING:
                level_log = logging.WARNING
            case TypeLogging.ERROR:
                level_log = logging.ERROR
            case TypeLogging.CRITICAL:
                level_log = logging.CRITICAL
            case TypeLogging.NOTSET:
                level_log = logging.NOTSET
        
        self.__logger = logging.getLogger(self.__filename)
        self.__logger.setLevel(level_log)
        
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(thread)d | %(message)s')
        handler = RotatingFileHandler(self.__filename, maxBytes=size_log*MEGA_BYTE, backupCount=backupCount)
        self.__logger.addHandler(handler)

        file_handler = logging.FileHandler(self.__filename)
        file_handler.setLevel(level_log)
        file_handler.setFormatter(formatter)
        self.__logger.addHandler(file_handler)

    def __call__(self, message:str, type_log:str='INFO'):
        self.__lock.acquire()
        try:
            match(type_log.upper()):
                case 'INFO':
                    self.__logger.info(message)
                case 'DEBUG':
                    self.__logger.debug(message)
                case 'WARNING':
                    self.__logger.warning(message)
                case 'ERROR':
                    self.__logger.error(message)
                case _:
                    self.__logger.info(message)
        
        except Exception as ex:
            print(ex)
        finally:
            self.__lock.release()