from enum import Enum

class TypeLoggingLevel(Enum):
    INFO = 0,
    DEBUG=1,
    ALL=2,

class GlobalSettingService():
    log_lvl:TypeLoggingLevel = TypeLoggingLevel.INFO
    to_elastic:bool = False
    elastic_conf:dict = {'host': 'localhost', 'port': 5959 }