#        _       __        __    __________    _____     __   __     __
#   	/ \	    |  |	  |__|  |__________|  |  _  \   |__|  \ \   / /
#      / _ \	|  |	   __       |  |      | |_)  |   __    \ \_/ /   Alitrix - Modern NLP
#     / /_\ \	|  |	  |  |      |  |      |  _  /   |  |    } _ {    Languages: Python, C#
#    / _____ \	|  |____  |  |      |  |      | | \ \   |  |   / / \ \   http://github.com/Alitrix
#   /_/     \_\	|_______| |__|	    |__|      |_|  \_\  |__|  /_/   \_\

# Licensed under the MIT License <http://opensource.org/licenses/MIT>
# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2021 The Alitrix Authors <http://github.com/Alitrix>

import time
from functools import wraps
import inspect
import itertools
from types import FunctionType
from typing import Any, TypeVar, Callable

from ..Domain.Configure.global_setting_service import GlobalSettingService, TypeLoggingLevel

from ..Application.DependencyInjection.resolve_provider import *
from ..Domain.Enums.type_methods import TypeMethod
from ..Utilites.system_logging import SysLogging

T = TypeVar('T')
_C = TypeVar("_C", bound=Callable[..., Any])

class ExtReflection():
    count_inject:int = 0
    
    @staticmethod
    def get_methods_class(cls):
        return set((x, y) for x, y in cls.__dict__.items()
                    if isinstance(y, (FunctionType, classmethod, staticmethod))
                    and not(x.startswith("__") and x.endswith("__")))

    @staticmethod
    def get_type_method(fn:_C, signature_has_self:bool)->TypeMethod:
        if not signature_has_self:
            return TypeMethod.Static
        else:
            if hasattr(fn, '__self__'):
                if inspect.isclass(fn.__self__):
                    return TypeMethod.Classmethod

        return TypeMethod.Instance
    
    @staticmethod
    def get_list_parent_methods(cls):
        return set(itertools.chain.from_iterable(
            ExtReflection.get_methods_class(c).union(ExtReflection.get_list_parent_methods(c)) for c in cls.__bases__))

    @staticmethod
    def list_class_methods(cls, is_narrow:bool):
        methods = ExtReflection.get_methods_class(cls)
        if  is_narrow:
            parentMethods = ExtReflection.get_list_parent_methods(cls)
            return set(cls for cls in methods if not (cls in parentMethods))
        else:
            return methods
    
    @staticmethod
    def get_handler_method(object:object, name_method:str, *args)->Callable:
        call_method = getattr(object, name_method)
        return call_method
    
    @staticmethod
    def get_init_info_v1(fn:Callable[..., Any], *args, **kwargs)->dict:
            fn_datas:dict = {}
            fn_args:list[dict] = []

            fn_datas['args'] = args
            fn_datas['kwargs'] = kwargs
            fn_datas['class'] = inspect._findclass(fn)
            fn_datas['name'] = fn.__name__
            fn_datas['type'] = type(fn_datas['class'].__dict__[fn.__name__])
            fn_datas['type_method'] = ExtReflection.get_type_method(fn)
            fn_datas['return_type'] = fn.__annotations__['return'] if 'return' in fn.__annotations__ else None

            fn_params = inspect.signature(fn)
            for index, param_name in enumerate(fn_params.parameters):
                param_d = fn_params.parameters[param_name]
                type_param = param_d.annotation if not param_d.annotation is inspect._empty else inspect._empty
                fn_args.append({'arg_pos': index, 'name': param_name, 'type': type_param})

                if param_d.default != inspect.Parameter.empty:
                    fn_args[index]['default'] = param_d.default

            fn_datas['params'] = fn_args

            return fn_datas

    @staticmethod
    def init_inject(func: _C)-> _C:

        @wraps(func)
        def wrapper(*args, **kwargs)->Any:
            if 'is_inject' not in kwargs:
                fn_datas = ExtReflection.get_init_info_v1(func)
                new_args = list(args)

                for item in fn_datas['params']:
                    if item['name'] != 'self':
                        check_type = item['type']
                        if ResolveProviderFWDI.contains(check_type):    #issubclass(check_type, BaseServiceFWDI):
                            search_service = ResolveProviderFWDI.get_service(item['type'])
                            if search_service != None:
                                new_args.append(search_service)

                result = func(*new_args, **kwargs)
                return result
            else:
                new_args = {}
                for item in [item for item in kwargs if item != 'is_inject']:
                    element = {item:kwargs[item]}
                    new_args.update(element)

                result = func(*args, **new_args)
                return result

        return wrapper

    @staticmethod
    def __get_default(lst_sign:list[inspect.Parameter], name_key:str) -> Any:
        search = [item for item in lst_sign if item.name == name_key and not item.default is inspect._empty]
        
        return search[0].default if len(search) > 0 else None

    def get_signature_args(fn:Callable[..., Any],fn_datas:dict = {})->dict:
        fn_datas['method_signature'] = list(inspect.signature(fn.__wrapped__ if hasattr(fn, '__wrapped__') else fn).parameters.values())
        
        return fn_datas
    
    def get_signature_has_self(fn_datas:dict)->dict:
        fn_datas['signature_has_self'] = True if len([item for item in fn_datas['method_signature'] if item.name == 'self']) > 0 else False

        return fn_datas
    
    def fn_have_self(args:tuple, type_fn:type)->bool:
        return False if len(args) == 0 else True if type(args[0]) == type_fn else False

    """
            test_arg:dict = {}
            ttt = [test_arg.update({i: item}) for i, item in enumerate(args)]
            test_arg.update(kwargs)
    """
    
    @staticmethod
    def get_inst_method_info_v2(fn:Callable[..., Any], args:tuple, kwargs:dict)->dict:
            fn_datas:dict = {}
            fn_args:list[dict] = []

            fn_datas['type'] = type(fn)
            fn_datas['origin_args'] = args
            fn_datas['origin_kwargs'] = kwargs
            fn_datas = ExtReflection.get_signature_args(fn, fn_datas)
            fn_datas = ExtReflection.get_signature_has_self(fn_datas)
            fn_datas['_arg_has_self_'] = ExtReflection.fn_have_self(args, inspect._findclass(fn))
            
            if not fn_datas['_arg_has_self_']:
                raise Exception(f"Error function:{fn} dont have self arument !")

            fn_datas['full_args'] = True if len(args) == len(fn_datas['method_signature']) else False

            fn_datas['method_signature'] = fn_datas['method_signature'][1:]
            #fn_datas['origin_args'] = args[1:]
                
            for param_name in fn_datas['method_signature']:
                type_param = param_name._annotation
                default_param = ExtReflection.__get_default(fn_datas['method_signature'], param_name.name)
                if not default_param is None:
                    fn_args.append({'name': param_name.name, 'type': type_param, 'default': default_param})
                else:
                    fn_args.append({'name': param_name.name, 'type': type_param})


            fn_datas['method_params'] = fn_args

            return fn_datas

    @staticmethod
    def get_static_method_info_v2(fn:Callable[..., Any], args:tuple, kwargs:dict)->dict:
            fn_datas:dict = {}
            fn_args:list[dict] = []

            fn_datas['type'] = type(fn)
            fn_datas['origin_args'] = args
            fn_datas['origin_kwargs'] = kwargs
            fn_datas = ExtReflection.get_signature_args(fn, fn_datas)
            fn_datas = ExtReflection.get_signature_has_self(fn_datas)

            if fn_datas['signature_has_self']:
                raise Exception("Error in Static method has Self argument")

            if ExtReflection.fn_have_self(args, inspect._findclass(fn)):
                fn_datas['origin_args'] = args[1:]
                
            for param_name in fn_datas['method_signature']:
                type_param = param_name._annotation
                default_param = ExtReflection.__get_default(fn_datas['method_signature'], param_name.name)
                if not default_param is None:
                    fn_args.append({'name': param_name.name, 'type': type_param, 'default': default_param})
                else:
                    fn_args.append({'name': param_name.name, 'type': type_param})


            fn_datas['method_params'] = fn_args

            return fn_datas    

    @staticmethod
    def __static_gen_new_args(info:dict)->dict:
        kwargs:dict = info['origin_kwargs']
        method_args:list[dict] = info['method_params']
        len_args = len(info['origin_args'])
        
        new_kwargs_params:dict[str, any] = {}

        if len_args > 0:
            method_args = method_args[len_args:]

        for item in method_args:
            arg_name, arg_type = item['name'], item['type']
            if arg_name in kwargs:
                try_get_value = kwargs.get(arg_name)
                new_kwargs_params[arg_name] = try_get_value
            else:
                if 'default' in item:
                    new_kwargs_params[arg_name] = item['default']
                elif ResolveProviderFWDI.contains(arg_type):
                    new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)
                else:
                    raise Exception(f"Code::1000:Error type:{arg_type} not found in Dependency Collection and not in kwargs or default value.")

        return new_kwargs_params

    @staticmethod
    def __instance_gen_new_args(info:dict)->dict:
        args:tuple = info['origin_args']
        kwargs:dict = info['origin_kwargs']
        method_args:list[dict] = info['method_params']

        new_kwargs_params:dict[str, any] = {}
        len_args:int = len(args)

        if len_args > 1:
            shift_args = len_args - 1
            method_args = method_args[shift_args:]

        for item in method_args:
            arg_name, arg_type = item['name'], item['type']
            if arg_name in kwargs:
                try_get_value = kwargs.get(arg_name)
                new_kwargs_params[arg_name] = try_get_value
            else:
                if 'default' in item:
                    new_kwargs_params[arg_name] = item['default']
                elif ResolveProviderFWDI.contains(arg_type):
                    new_kwargs_params[arg_name] = ResolveProviderFWDI.get_service(arg_type)
                else:
                    raise Exception(f"Code::1000:Error type:{arg_type} not found in Dependency Collection and not in kwargs or default value.")

        return new_kwargs_params

    @staticmethod
    def _log_inject(func: _C) -> _C:
        
        @wraps(func)
        def __sync(*args, **kwargs)->_C:
            __log__ = SysLogging(filename="__inject__")
            match GlobalSettingService.log_lvl:
                case TypeLoggingLevel.DEBUG:
                    __log__(f"sync exec :{func.__module__}::{func.__name__}", 'debug')
                case TypeLoggingLevel.ALL:
                    __log__(f"sync exec :{func.__module__}::{func.__name__}, args={args}, kwargs:{kwargs}", 'debug')

            try:
                t_start = time.perf_counter_ns()

                result_call = func(*args, **kwargs)

                if GlobalSettingService.log_lvl == TypeLoggingLevel.DEBUG or GlobalSettingService.log_lvl == TypeLoggingLevel.ALL:
                    time_call = time.perf_counter_ns() - t_start
                    __log__(f"run: {args} = duration time :{func.__name__}={time_call}")

                return result_call
            except Exception as ex:
                match GlobalSettingService.log_lvl:
                    case TypeLoggingLevel.INFO:
                        __log__(f"{ex}", 'error')
                    case TypeLoggingLevel.DEBUG:
                        __log__(f"error exec :{func.__name__} Error:{ex}", 'error')
                    case TypeLoggingLevel.ALL:
                        __log__(f"sync exec :{func.__module__}::{func.__name__}, args={args}, kwargs:{kwargs}", 'debug')
                
                return None
    
        @wraps(func)
        async def __async(*args, **kwargs)->_C:
            __log__ = SysLogging(filename="__inject__")
            if GlobalSettingService.log_lvl == TypeLoggingLevel.DEBUG or GlobalSettingService.log_lvl == TypeLoggingLevel.ALL:
                __log__(f"sync exec :{func.__module__}::{func.__name__}")
            try:
                t_start = time.perf_counter_ns()
                
                result_call = await func(*args, **kwargs)
                
                if GlobalSettingService.log_lvl == TypeLoggingLevel.DEBUG or GlobalSettingService.log_lvl == TypeLoggingLevel.ALL:
                    time_call = time.perf_counter_ns() - t_start
                    __log__(f"    duration time :{func.__name__}={time_call}")

                return result_call
            except Exception as ex:
                __log__(f"error exec :{func.__name__}\n Error:{ex}\n{args}, {kwargs}", 'error')
                return None

        
        return __async if inspect.iscoroutinefunction(func) else __sync

    #-----------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------
    @_log_inject
    def _inject_(func: _C)->_C:
        ExtReflection.count_inject += 1
        
        #-----------------------------------------------------------------------------
        #------------------------------INSTANCE SYNC METHOD INJECT
        #-----------------------------------------------------------------------------
        @wraps(func, updated=())
        def __inst_sync(*args, **kwargs)->_C:
            if not ResolveProviderFWDI.is_init():
                return func(*args, **kwargs)
            
            if 'is_inject' not in kwargs:
                method_info = ExtReflection.get_inst_method_info_v2(func, args, kwargs)
                length_param = len(method_info['method_params'])
                args = method_info['origin_args']
                kwargs = method_info['origin_kwargs']
                len_args = len(args)

                if method_info['_arg_has_self_'] and length_param == 0 or method_info['full_args']:
                    result = func(*args)
                    return result

                if len(kwargs) > 0 and len(kwargs) == len(method_info['method_signature']):
                    result = func(*args, **kwargs)
                    return result


                if not method_info['signature_has_self'] and len_args == length_param:
                    result = func(*args, **kwargs)
                    return result
                elif method_info['signature_has_self'] and (len_args - 1) == length_param:
                    result = func(*args, **kwargs)
                    return result
                elif method_info['signature_has_self'] and len_args == 1 and length_param == 0:
                    result = func(*args, **kwargs)
                    return result

                new_args:dict = ExtReflection.__instance_gen_new_args(method_info)
                result = func(*args, **new_args)
                return result
            else:
                new_args = [item for item in kwargs if item != 'is_inject']
                result = func(*args, **new_args)

            return result
        
        #-----------------------------------------------------------------------------
        #------------------------------INSTANCE ASYNC METHOD INJECT
        #-----------------------------------------------------------------------------

        @wraps(func)
        async def __inst_async(*args, **kwargs)->_C:
            if not ResolveProviderFWDI.is_init():
                return func(*args, **kwargs)
            
            if 'is_inject' not in kwargs:
                method_info = ExtReflection.get_inst_method_info_v2(func, args, kwargs)
                length_param = len(method_info['method_params'])
                args = method_info['origin_args']
                kwargs = method_info['origin_kwargs']
                len_args = len(args)
        
                if method_info['_arg_has_self_'] and length_param == 0:
                    result = func(*args)
                    return result

                if len(kwargs) > 0 and len(kwargs) == len(method_info['method_signature']):
                    result = func(*args, **kwargs)
                    return result


                if not method_info['signature_has_self'] and len_args == length_param:
                    result = func(*args, **kwargs)
                    return result
                elif method_info['signature_has_self'] and (len_args - 1) == length_param:
                    result = func(*args, **kwargs)
                    return result
                elif method_info['signature_has_self'] and len_args == 1 and length_param == 0:
                    result = func(*args, **kwargs)
                    return result

                new_args = ExtReflection.__instance_gen_new_args(method_info)
                result = await func(*args, **new_args)

                return result
            else:
                new_args = [item for item in kwargs if item != 'is_inject']
                result = await func(*args, **new_args)

            return result
    
        #-----------------------------------------------------------------------------
        #------------------------------STATIC SYNC METHOD INJECT
        #-----------------------------------------------------------------------------   
        @wraps(func, updated=())
        def __static_sync(*args, **kwargs)->_C:
            if not ResolveProviderFWDI.is_init():
                return func(*args, **kwargs)
            
            if 'is_inject' not in kwargs:
                fn_signature = list(inspect.signature(func.__wrapped__ if hasattr(func, '__wrapped__') else func).parameters.values())

                if len(kwargs) > 0 and len(kwargs) == len(fn_signature):
                    result = func(**kwargs)
                    return result

                method_info = ExtReflection.get_static_method_info_v2(func, args, kwargs)
                args = method_info['origin_args']
                kwargs = method_info['origin_kwargs']
                length_param = len(method_info['method_params'])
                len_args = len(args)

                if len_args == length_param:
                    result = func(*args, **kwargs)
                    return result

                new_args:dict = ExtReflection.__static_gen_new_args(method_info)
                result = func(*args, **new_args)
                return result
            else:
                new_args = [item for item in kwargs if item != 'is_inject']
                result = func(*args, **new_args)

            return result

        #-----------------------------------------------------------------------------
        #------------------------------STATIC ASYNC METHOD INJECT
        #-----------------------------------------------------------------------------   
        @wraps(func)
        async def __static_async(*args, **kwargs)->_C:
            if not ResolveProviderFWDI.is_init():
                return func(*args, **kwargs)
            
            if 'is_inject' not in kwargs:
                fn_signature = list(inspect.signature(func.__wrapped__ if hasattr(func, '__wrapped__') else func).parameters.values())

                if len(kwargs) > 0 and len(kwargs) == len(fn_signature):
                    result = func(**kwargs)
                    return result

                method_info = ExtReflection.get_static_method_info_v2(func, args, kwargs)
                args = method_info['origin_args']
                kwargs = method_info['origin_kwargs']
                length_param = len(method_info['method_params'])
                len_args = len(args)

                if len_args == length_param:
                    result = func(*args, **kwargs)
                    return result

                new_args = ExtReflection.__static_gen_new_args(method_info)
                result = await func(*args, **new_args)

                return result
            else:
                new_args = [item for item in kwargs if item != 'is_inject']
                result = await func(*args, **new_args)

            return result
        
        method_signature = list(inspect.signature(func.__wrapped__ if hasattr(func, '__wrapped__') else func).parameters.values())
        signature_has_self = True if len([item for item in method_signature if item.name == 'self']) > 0 else False
        type_call = ExtReflection.get_type_method(func, signature_has_self)

        match type_call:
            case TypeMethod.Instance:
                return __inst_async if inspect.iscoroutinefunction(func) else __inst_sync
            case TypeMethod.Static:
                return __static_async if inspect.iscoroutinefunction(func) else __static_sync
            case _:
                raise Exception("Error not found function type inject !")

    #-----------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------
    #     
    @staticmethod
    def is_class(obj)->bool:
        return True if isinstance(obj, type) else False
    
    @staticmethod
    def is_injectable_init(obj)->bool:
        return True if '__init__' in obj.__dict__ else False