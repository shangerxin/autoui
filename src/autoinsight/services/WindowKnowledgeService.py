import os
from typing import Union, NewType, Optional, Dict
from multiprocessing import Process
from functools import partial

from pywinauto import Desktop, WindowSpecification, Application
from pywinauto.win32_element_info import HwndElementInfo
from pywinauto.uia_element_info import UIAElementInfo

from autoinsight.common.models.Knowledge import Knowledge
from .KnowledgeServiceBase import KnowledgeServiceBase

WindowAutomationInstance = NewType("WindowAutomationInstance", Optional[Union[UIAElementInfo, HwndElementInfo]])


class WindowKnowledgeService(KnowledgeServiceBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.knowledge.append(Knowledge(alias=["windowscamera",
                                               "windowscamera.exe",
                                               "camera",
                                               "camera.exe",
                                               "microsoft.windows.camera"],
                                        launch=_launchCamera))

        self.knowledge.append(Knowledge(alias=["control panel"],
                                        launch=_launchControlPanel))

        self.knowledge.append(Knowledge(alias=["settings"],
                                        launch=_launchSettings))

        self.knowledge.append(Knowledge(alias=["calc", "calc.exe", "calculator"],
                                        launch=_launchCalc))

        self.knowledge.append(Knowledge(alias=["media player", "wmplayer.exe", "mediaplayer"],
                                        launch=_launchMediaPlayer))

    def recognize(self, name: str) -> WindowAutomationInstance:
        knowledge = None
        if name:
            name = name.lower()
            for k in self.knowledge:
                if name in k.alias:
                    knowledge = k
                    break

        if knowledge:
            return knowledge.launch(knowledge)

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def wait(self, timeoutSeconds: int = 0):
        pass


def _task(commandline: str):
    os.system(commandline)


def _worker(commandline: str, k: Knowledge):
    p = Process(target=partial(_task, commandline), args=k.arguments)
    p.start()


def _waitWindow(criteria: Dict[str, str]) -> WindowAutomationInstance:
    window = WindowSpecification(criteria)
    # TODO add magic numbers into global configuration
    window.wait("exists visible ready", timeout=30, retry_interval=3)
    return window


def _launchCamera(k: Knowledge) -> WindowAutomationInstance:
    _worker('cmd /C "start microsoft.windows.camera: "', k)
    return _waitWindow({"backend": "uia", "best_match": "Camera"})


def _launchControlPanel(k: Knowledge) -> WindowAutomationInstance:
    _worker('control.exe', k)
    return _waitWindow({"backend": "uia", "best_match": r"Control Panel\All Control Panel Items"})


def _launchSettings(k: Knowledge) -> WindowAutomationInstance:
    pass


def _launchCalc(k: Knowledge) -> WindowAutomationInstance:
    Application(backend="uia").start('calc.exe')

    return Desktop(backend="uia").Calculator


def _launchMediaPlayer(k: Knowledge) -> WindowAutomationInstance:
    _worker(r'"C:\Program Files\Windows Media Player\wmplayer.exe"', k)
    return _waitWindow({"backend": "uia", "best_match": "Windows Media Player"})