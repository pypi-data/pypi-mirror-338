from sys import _getframe
import logstash
import os
from threading import Lock
from enum import Enum
import logging
from pythonjsonlogger import jsonlogger
from elasticsearch import Elasticsearch
import datetime
import psutil
import socket
from logging.handlers import RotatingFileHandler

from ..Infrastructure.Logging.ElasticSearch.elastic_search_handler import ElasticsearchHandler
from ..Domain.Configure.global_setting_service import GlobalSettingService

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

"""
handler = RotatingFileHandler(f"{LOG_DIR}/__system__.log", maxBytes=size_main_log_file, backupCount=DEFAULT_BACKUP_COUNT_LOG)
logging.basicConfig(encoding='utf-8', 
                    level=logging.DEBUG, 
                    format='%(asctime)s | %(name)s | %(levelname)s | %(thread)d | %(message)s', 
                    handlers=[handler])
"""

class SysLogging():
    def __init__(self, 
                 filename:str, 
                 logging_level=TypeLogging.INFO, 
                 size_log:int=10, 
                 backupCount:int=DEFAULT_BACKUP_COUNT_LOG,
                 ):
        self.__lock = Lock()  
        self.__name:str = filename
        self.__filename:str = f'{LOG_DIR}/{filename}.log'
        
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
        
        
        if not GlobalSettingService.log_to_file:
            self.__logger = logging.getLogger(self.__name)
        else:
            self.__logger = logging.getLogger(self.__filename)
        self.__logger.setLevel(level_log)
        
        formatter = jsonlogger.JsonFormatter(
                   '%(asctime)s| %(name)s | %(levelname)s | %(thread)d | %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S'
                )

        if GlobalSettingService.log_to_elastic:
            
            es_host:str = GlobalSettingService.elastic_conf.get('host', 'localhost')
            es_port:int = GlobalSettingService.elastic_conf.get('port', 5959)
            es_user:str = GlobalSettingService.elastic_conf.get('username', 'elastic')
            es_pass:str = GlobalSettingService.elastic_conf.get('password', '')
            es_search_index:str = GlobalSettingService.elastic_conf.get('elastic_search_index', 'microservice_system_log')

            if self.__check_avaibale_es(es_host, es_port, es_user, es_pass):
                es_handler = ElasticsearchHandler(
                                                host=es_host, 
                                                port=es_port, 
                                                username=es_user, 
                                                password=es_pass, 
                                                elastic_index=es_search_index
                                                )
                es_handler.setFormatter(formatter)
                self.__logger.addHandler(es_handler)
            else:
                print(f'Error Elastic not available.')

            """
            handler = logstash.LogstashHandler(elastic_host, elastic_port, version=1)
            self.__logger.addHandler(handler)
            handler.setFormatter(formatter)
            self.__logger.addHandler(logstash.TCPLogstashHandler(elastic_host, elastic_port , version=1))
            """
        
        if GlobalSettingService.log_to_console:
            # Add console output
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.__logger.addHandler(console_handler)

        if GlobalSettingService.log_to_file:
            handler = RotatingFileHandler(self.__filename, maxBytes=size_log*MEGA_BYTE, backupCount=backupCount)
            self.__logger.addHandler(handler)

            file_handler = logging.FileHandler(self.__filename)
            file_handler.setLevel(level_log)
            file_handler.setFormatter(formatter)
            self.__logger.addHandler(file_handler)

    def __check_avaibale_es(self, host:str, port:int, username:str, password:str)->bool:

        conn_str:str = f'http://{host}:{port}'
        es = Elasticsearch(conn_str, basic_auth=(username, password))
        return False if not es.ping() else True

    def __call__(self, message:str, type_log:str='INFO'):
        self.__lock.acquire()
        es_avaible:bool = False
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