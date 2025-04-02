# coding=utf-8
from typing import Any

from logging import Logger

from ka_uts_com.utils.pacmod import PacMod
from ka_uts_com.ioc.yaml_ import Yaml_

TyAny = Any
TyTimeStamp = int
TyArr = list[Any]
TyBool = bool
TyDic = dict[Any, Any]
TyLogger = Logger


class Cfg_:
    """Configuration Class
    """
    cfg: Any = None

    @classmethod
    def sh(cls, log: TyLogger, d_pacmod: TyDic) -> Any:
        """ show configuration
        """
        cls.cfg = Yaml_.read(PacMod.sh_path_cfg_yaml(d_pacmod), log)
        return cls.cfg
