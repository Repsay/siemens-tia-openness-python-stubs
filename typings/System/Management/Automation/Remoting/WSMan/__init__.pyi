# encoding: utf-8
# module System.Management.Automation.Remoting.WSMan calls itself WSMan
# from System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import EventArgs

from typing import Self

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class ActiveSessionsChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ActiveSessionsChangedEventArgs(activeSessionsCount: int) """
    @property
    def ActiveSessionsCount(self) -> int:
        """ Get: ActiveSessionsCount(self: ActiveSessionsChangedEventArgs) -> int """
        ...


    def __new__(cls, activeSessionsCount:int) -> Self:
        """ __new__(cls: type, activeSessionsCount: int) """
        ...


class WSManServerChannelEvents: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    ActiveSessionsChanged = ...
    ShuttingDown = ...
    __all__: list = ...


