# coding=utf-8
from datetime import datetime

from ka_uts_com.com import Com
from ka_uts_com.log import Log

from typing import Any
TyAny = Any
TyArr = list[Any]
TyDic = dict[Any, Any]
TyStr = str
TnAny = None | TyAny
TnStr = None | TyStr


class Timestamp:

    @staticmethod
    def sh_elapse_time_sec(end: Any, start: TnAny) -> TnAny:
        if start is None:
            return None
        return end.timestamp()-start.timestamp()


class Timer:
    """ Timer Management
    """
    @staticmethod
    def sh_task_id(d_pacmod: TyDic, class_id: Any, parms: TnAny, sep: TyStr) -> TyStr:
        """ start Timer
        """
        package = d_pacmod.get('package')
        module = d_pacmod.get('module')
        if isinstance(class_id, str):
            class_name = class_id
        else:
            class_name = class_id.__qualname__
        if not parms:
            parms = ""
        else:
            parms = f" {parms}"
        arr: TyArr = []
        for item in [package, module, class_name, parms]:
            if not item:
                continue
            arr.append(item)
        return sep.join(arr)

    @classmethod
    def start(cls, class_id: TyAny, parms: TnAny = None, sep: TyStr = ".") -> None:
        """ start Timer
        """
        task_id = cls.sh_task_id(Com.d_pacmod, class_id, parms, sep)
        Com.d_timer[task_id] = datetime.now()

    @classmethod
    def end(cls, class_id: TyAny, parms: TnAny = None, sep: TyStr = ".") -> None:
        """ end Timer
        """
        task_id = cls.sh_task_id(Com.d_pacmod, class_id, parms, sep)
        start = Com.d_timer.get(task_id)
        end = datetime.now()
        elapse_time_sec = Timestamp.sh_elapse_time_sec(end, start)
        msg = f"{task_id} elapse time [sec] = {elapse_time_sec}"
        Log.info(msg, stacklevel=2)
