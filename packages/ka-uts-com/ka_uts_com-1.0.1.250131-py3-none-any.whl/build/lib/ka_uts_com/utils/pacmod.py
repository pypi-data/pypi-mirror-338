# coding=utf-8
from typing import Any

from os import path as os_path
import pkg_resources

TyArr = list[Any]
TyDic = dict[Any, Any]
TnDic = None | TyDic


class PacMod:
    """ Package Module Management
    """
    @staticmethod
    def sh_d_pacmod(root_cls, tenant: Any) -> TyDic:
        """ Show Pacmod Dictionary
        """
        a_pacmod: TyArr = root_cls.__module__.split(".")
        package = a_pacmod[0]
        module = a_pacmod[1]
        d_pacmod: TyDic = {}
        d_pacmod['tenant'] = tenant
        d_pacmod['package'] = package
        d_pacmod['module'] = module
        return d_pacmod

    # class Cfg:
    #    """ Configuration Sub Class of Package Module Class
    #    """
    @staticmethod
    def sh_path_cfg_yaml(d_pacmod: TyDic) -> str:
        """ show directory
        """
        package = d_pacmod['package']
        module = d_pacmod['module']

        directory: str = f"{package}.data"

        # print(f"dir = {dir}")
        # print(f"package = {package}")
        # print(f"module = {module}")

        path: str = pkg_resources.resource_filename(directory, f"{module}.yml")
        return path

    @staticmethod
    def sh_path_keys_yaml(
            d_pacmod: TyDic, filename: str = 'keys.yml') -> str:
        """ show directory
        """
        package = d_pacmod['package']
        directory = f"{package}.data"
        path: str = pkg_resources.resource_filename(directory, filename)
        return path

    @staticmethod
    def sh_pacmod_type(d_pacmod: TyDic, type_: str) -> str:
        """ show Data File Path
        """
        package = d_pacmod['package']
        module = d_pacmod['module']
        return f"/data/{package}/{module}/{type_}"

    @classmethod
    def sh_file_path(
            cls, d_pacmod: TyDic, type_: str, suffix: str,
            pid: Any, ts: Any, **kwargs) -> str:
        """ show type specific path
        """
        filename = kwargs.get('filename')
        if filename is not None:
            filename_ = filename
        else:
            filename_ = type_

        sw_run_pid_ts = kwargs.get('sw_run_pid_ts', True)
        if sw_run_pid_ts is None:
            sw_run_pid_ts = True

        _dir: str = cls.sh_pacmod_type(d_pacmod, type_)
        if sw_run_pid_ts:
            file_path = os_path.join(
                _dir, f"{filename_}_{pid}_{ts}.{suffix}")
        else:
            file_path = os_path.join(_dir, f"{filename_}.{suffix}")
        return file_path

    @classmethod
    def sh_pattern(
            cls, d_pacmod: TyDic, type_: str, suffix: str, **kwargs) -> str:
        """ show type specific path
        """
        filename = kwargs.get('filename')
        _directory: str = cls.sh_pacmod_type(d_pacmod, type_)
        path = os_path.join(_directory, f"{filename}*.{suffix}")
        return path

    @staticmethod
    def sh_path_cfg_log(d_pacmod: TnDic = None, filename: str = 'log.yml'):
        """ show directory
        """
        if d_pacmod is None:
            d_pacmod = {'package': 'ka_uts_com', 'module': 'com'}
        return pkg_resources.resource_filename(
            f"{d_pacmod['package']}.data", filename
        )
