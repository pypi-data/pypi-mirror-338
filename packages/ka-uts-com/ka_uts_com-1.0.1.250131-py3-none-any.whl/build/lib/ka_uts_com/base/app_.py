# coding=utf-8
from typing import Any

from logging import Logger

from ka_uts_com.utils.pacmod import PacMod
from ka_uts_com.ioc.yaml_ import Yaml_

TyAny = Any
TyArr = list[Any]
TyBool = bool
TyDic = dict[Any, Any]
TyLogger = Logger

TnAny = None | Any
TnArr = None | TyArr
TnBool = None | bool
TnDic = None | TyDic


class App_:
    """Aplication Class
    """
    sw_init: TyBool = False
    httpmod: TyAny = None
    sw_replace_keys: TnBool = None
    keys: TnArr = None
    reqs: TyDic = {}
    app: TyDic = {}

    @classmethod
    def init(cls, log: TyLogger, **kwargs) -> None:
        if cls.sw_init:
            return
        cls.sw_init = True
        cls.httpmod = kwargs.get('httpmod')
        cls.sw_replace_keys = kwargs.get('sw_replace_keys', False)
        try:
            if cls.sw_replace_keys:
                d_pacmod: TyDic = kwargs.get('d_pacmod', {})
                cls.keys = Yaml_.read(PacMod.sh_path_keys_yaml(d_pacmod), log)
        except Exception as exc:
            log.error(exc, exc_info=True)
            raise

    @classmethod
    def sh(cls, log: TyLogger, **kwargs) -> Any:
        if cls.sw_init:
            return cls
        cls.init(log, **kwargs)
        return cls
