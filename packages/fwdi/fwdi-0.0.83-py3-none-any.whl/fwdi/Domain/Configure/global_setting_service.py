from enum import Enum

class TypeLoggingLevel(Enum):
    INFO = 0,
    DEBUG=1,
    ALL=2,

class GlobalSettingService():
    log_lvl:TypeLoggingLevel = TypeLoggingLevel.INFO
    log_to_elastic:bool = False
    log_to_console:bool = False
    log_to_file:bool = False
    elastic_conf:dict = {'host': 'localhost', 'port': 9200, 'elastic_search_index': 'system_log', 'username': 'elastic', 'password': ''}