# encoding: utf-8
# module System.Management.Automation.Remoting.Internal calls itself Internal
# from System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum

from System.Management.Automation import Cmdlet

"""The following names are not found in the module: field#
"""

# no functions
# classes

class PSStreamObject: # skipped bases: <type 'object'>, <type 'object'>
    """ PSStreamObject(objectType: PSStreamObjectType, value: object) """
    @property
    def ObjectType(self) -> PSStreamObjectType:
        """
        Get: ObjectType(self: PSStreamObject) -> PSStreamObjectType
        Set: ObjectType(self: PSStreamObject) = value
        """
        ...


    def WriteStreamObject(self, cmdlet:Cmdlet, overrideInquire:bool): # -> 
        """ WriteStreamObject(self: PSStreamObject, cmdlet: Cmdlet, overrideInquire: bool) """
        ...


class PSStreamObjectType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PSStreamObjectType, values: BlockingError (5), Debug (8), Error (2), Exception (12), Information (11), MethodExecutor (3), Output (1), Progress (9), ShouldMethod (6), Verbose (10), Warning (4), WarningRecord (7) """
    BlockingError: PSStreamObjectType = ...
    Debug: PSStreamObjectType = ...
    Error: PSStreamObjectType = ...
    Exception: PSStreamObjectType = ...
    Information: PSStreamObjectType = ...
    MethodExecutor: PSStreamObjectType = ...
    Output: PSStreamObjectType = ...
    Progress: PSStreamObjectType = ...
    ShouldMethod: PSStreamObjectType = ...
    value__ = ...
    Verbose: PSStreamObjectType = ...
    Warning: PSStreamObjectType = ...
    WarningRecord: PSStreamObjectType = ...


