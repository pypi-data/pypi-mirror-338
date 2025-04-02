# coding=utf-8
from collections.abc import Callable
from typing import Any

import os
import logging
import logging.config
from logging import Logger
from datetime import datetime
import psutil

from ka_uts_com.utils.pacmod import PacMod
from ka_uts_com.ioc.jinja2_ import Jinja2_

TyAny = Any
TyCallable = Callable[..., Any]
TyDateTime = datetime
TyTimeStamp = int
TyArr = list[Any]
TyBool = bool
TyDic = dict[Any, Any]
TyDir = str
TyLogger = Logger

TnAny = None | Any
TnArr = None | TyArr
TnBool = None | bool
TnDic = None | TyDic
TnTimeStamp = None | TyTimeStamp
TnDateTime = None | TyDateTime


class LogStandard:
    """Standard Logging
    """


class Log_:

    sw_init: bool = False
    log: TyLogger = logging.getLogger('dummy_logger')
    username: str = psutil.Process().username()

    @classmethod
    def sh_run_dir(cls, com, **kwargs) -> TyDir:
        """Show run_dir
        """
        tenant: str = com.d_pacmod['tenant']
        package: str = com.d_pacmod['package']
        module: str = com.d_pacmod['module']
        log_type: str = kwargs.get('log_type', 'std')
        if log_type == "std":
            return f"/data/{tenant}/RUN/{package}/{module}"
        return f"/data/{tenant}/RUN/{package}/{module}/{cls.username}"

    @classmethod
    def sh_cfg(cls, com, **kwargs) -> TyDic:
        """Read log file path with jinja2
        """
        run_dir = kwargs.get('run_dir', cls.sh_run_dir(com, **kwargs))
        run_dir_debug: str = kwargs.get('run_dir_debug', f"{run_dir}/debs")
        run_dir_info: str = kwargs.get('run_dir_info', f"{run_dir}/logs")
        run_dir_error: str = kwargs.get('run_dir_error', f"{run_dir}/errs")

        if kwargs.get('sw_mklogdirs', True):
            os.makedirs(run_dir_debug, exist_ok=True)
            os.makedirs(run_dir_info, exist_ok=True)
            os.makedirs(run_dir_error, exist_ok=True)

        log_type = kwargs.get('log_type', 'std')
        logcfg_file = f'log.{log_type}.yml'
        logcfg_path: str = PacMod.sh_path_cfg_log(filename=logcfg_file)
        cfg: TyDic = Jinja2_.read(
                logcfg_path,
                com.Log,
                debug_dir=run_dir_debug,
                info_dir=run_dir_info,
                error_dir=run_dir_error,
                module=com.d_pacmod['module'],
                pid=com.pid,
                ts=com.ts)
        # ts=com.ts_start)
        sw_debug: TyBool = kwargs.get('sw_debug', False)
        if sw_debug:
            level = logging.DEBUG
        else:
            level = logging.INFO
        if log_type == 'std':
            logger_name = 'main'
        else:
            logger_name = 'person'
        cfg['handlers'][f"{logger_name}_debug_console"]['level'] = level
        cfg['handlers'][f"{logger_name}_debug_file"]['level'] = level

        return cfg

    @classmethod
    def init(cls, com, **kwargs) -> None:
        """Set static variable log level in log configuration handlers
        """
        log_type = kwargs.get('log_type', 'std')
        cls.sw_init = True
        cfg = cls.sh_cfg(com, **kwargs)
        logging.config.dictConfig(cfg)
        if log_type == "std":
            cls.log = logging.getLogger('main')
        else:
            cls.log = logging.getLogger(log_type)

    @classmethod
    def sh(cls, com, **kwargs) -> TyLogger:
        if cls.sw_init:
            return cls.log
        cls.init(com, **kwargs)
        return cls.log
