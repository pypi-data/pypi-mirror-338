"""
This module provides task scheduling classes for the management of OmniTracker
SRR (NHRR) processing for Department UMH.
    SRR: Sustainability Risk Rating
    NHRR: Nachhaltigkeits Risiko Rating
"""
import os
import time

from ka_uts_com.log import Log
from ka_uts_dic.dic import Dic
from ka_uts_obj.path import Path

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from typing import Any
TyArr = list[Any]
TyDic = dict[Any, Any]
TyStr = str


class PmeHandler(PatternMatchingEventHandler):
    """
    WatchDog Event Handler for pattern matching of files paths
    """
    msg_evt: TyStr = "Watchdog received {E} - {P}"
    msg_exe: TyStr = "Watchdog executes script: {S}"

    def __init__(self, patterns, scripts):
        # Set the patterns for PatternMatchingEventHandler
        # self.kwargs = kwargs
        super().__init__(
                patterns=patterns,
                ignore_patterns=None,
                ignore_directories=True,
                case_sensitive=False)
        self.scripts = scripts

    def on_created(self, event):
        """
        process 'files paths are created' event
        """
        _path = event.src_path
        Log.debug(f"Watchdog received created event - {_path}")
        # result = subprocess.run(scripts, capture_output=True, text=True)
        for _script in self.scripts:
            Log.debug(f"Watchdog executes script: {_script}")
            os.system(_script)

    def on_modified(self, event):
        _path = event.src_path
        Log.debug(f"Watchdog received mdified event - {_path}")
        # result = subprocess.run(scripts, capture_output=True, text=True)
        for _script in self.scripts:
            Log.debug(f"Watchdog executes script: {_script}")
            Log.debug(f"Watchdog executes script: {_script}")
            os.system(_script)


class WdP:
    """
    General Task class
    """
    @staticmethod
    def pmeh(kwargs: TyDic) -> None:
        """
        WatchDog Task for pattern matching of files paths
        """
        _path = Path.sh_path_using_pathnm('in_dir_wdp', **kwargs)
        # _patterns = kwargs.get('in_patterns_wdp', [])
        # _scripts = kwargs.get('scripts_wdp', [])
        # if isinstance(_patterns, str):
        #     _patterns = [_patterns]
        # if isinstance(_scripts, str):
        #     _scripts = [_scripts]
        _patterns: TyArr = Dic.get_as_array(kwargs, 'in_patterns_wdp')
        _scripts: TyArr = Dic.get_as_array(kwargs, 'scripts_wdp')

        Log.debug(f"_path = {_path}")
        Log.debug(f"_patterns = {_patterns}")
        Log.debug(f"_scripts = {_scripts}")

        _pmehandler = PmeHandler(_patterns, _scripts)
        _observer = Observer()
        _observer.schedule(_pmehandler, path=_path, recursive=False)
        _observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            _observer.stop()
        _observer.join()
