# encoding: utf-8
# module System.Management.Automation.Security calls itself Security
# from System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum

from System.Runtime.InteropServices import SafeHandle

"""The following names are not found in the module: field#
"""

# no functions
# classes

class SystemEnforcementMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SystemEnforcementMode, values: Audit (1), Enforce (2), None (0) """
    Audit: SystemEnforcementMode = ...
    Enforce: SystemEnforcementMode = ...
    value__ = ...


class SystemPolicy: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetLockdownPolicy(path:str, handle:SafeHandle) -> SystemEnforcementMode:
        """ GetLockdownPolicy(path: str, handle: SafeHandle) -> SystemEnforcementMode """
        ...

    @staticmethod
    def GetSystemLockdownPolicy() -> SystemEnforcementMode:
        """ GetSystemLockdownPolicy() -> SystemEnforcementMode """
        ...


