# coding=utf-8
from typing import Any

import os
import time
import calendar
import logging
import logging.config
from logging import Logger
from datetime import datetime

from ka_uts_com.utils.aoeqstmt import AoEqStmt
from ka_uts_com.base.app_ import App_
from ka_uts_com.base.cfg_ import Cfg_
from ka_uts_com.base.exit_ import Exit_
from ka_uts_com.base.log_ import Log_

TyAny = Any
TyDateTime = datetime
TyTimeStamp = int
TyArr = list[Any]
TyBool = bool
TyDic = dict[Any, Any]
TyLogger = Logger

TnAny = None | Any
TnArr = None | TyArr
TnDic = None | TyDic
TnTimeStamp = None | TyTimeStamp
TnDateTime = None | TyDateTime


class Com:
    """Communication Class
    """
    sw_init: bool = False
    cfg: TnDic = None
    pid = None
    d_pacmod: TyDic = {}

    ts: TnTimeStamp
    ts_start: TnDateTime = None
    ts_end: TnDateTime = None
    ts_etime: TnDateTime = None
    d_timer: TyDic = {}

    Log: Logger = logging.getLogger('dummy_logger')
    App: Any = None
    Exit: Any = None

    @classmethod
    def init(cls, **kwargs):
        """ set log and application (module) configuration
        """
        if cls.sw_init:
            return
        cls.sw_init = True
        cls.d_pacmod = kwargs.get('d_pacmod', {})
        cls.ts = calendar.timegm(time.gmtime())
        cls.pid = os.getpid()

        cls.Log = Log_.sh(cls, **kwargs)
        cls.cfg = Cfg_.sh(cls.Log, cls.d_pacmod)
        cls.App = App_.sh(cls.Log, **kwargs)
        cls.Exit = Exit_.sh(**kwargs)

    @classmethod
    def sh_kwargs(cls, root_cls, d_parms, *args) -> TyDic:
        _kwargs: TyDic = AoEqStmt.sh_d_eq(
                *args, d_parms=d_parms, root_cls=root_cls)
        cls.init(**_kwargs)
        return _kwargs
