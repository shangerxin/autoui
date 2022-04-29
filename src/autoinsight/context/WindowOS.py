import os
import subprocess

import pyautogui

from .OSBase import OSBase


class WindowOS(OSBase):
    @abstractmethod
    def launchApp(self, path) -> GUIApplicationBase:
        subprocess.Popen(path, shell=True)

    @abstractmethod
    def launchShell(self, path) -> ShellBase:
        pass

    @abstractmethod
    def kill(self, processId: int, processName: str):
        pass

    @abstractmethod
    def terminate(self, processId: int, processName: str):
        pass

    @abstractproperty
    def userHome(self):
        pass

    @property
    def environ(self) -> Dict:
        return self._environ

    @abstractproperty
    def displays(self):
        pass

    @abstractproperty
    def systeminfo(self) -> str:
        pass

    @abstractproperty
    def version(self) -> str:
        pass

    @abstractproperty
    def drivers(self) -> Iterable[str]:
        pass

    @abstractproperty
    def SBIOS(self) -> str:
        pass

    @abstractproperty
    def VBIOS(self) -> str:
        pass

    @abstractmethod
    def updateDriver(self):
        pass

    @abstractmethod
    def type(self, visibleKeys: Iterable[str], intervalSec: int = 0.25):
        """
        Simulate typing the visible characters
        """
        pass

    @abstractmethod
    def combineKeys(self, firstKey, secondKey, ThirdKey=None):
        pass

    @abstractmethod
    def snapshot(self):
        pass
