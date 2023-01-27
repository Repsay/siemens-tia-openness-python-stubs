# encoding: utf-8
# module System.Activities.Debugger.Symbol calls itself Symbol
# from System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array

from System.Collections import ICollection

from System.Xaml import AttachableMemberIdentifier


# no functions
# classes

class ActivitySymbol: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def EndColumn(self) -> int:
        """ Get: EndColumn(self: ActivitySymbol) -> int """
        ...

    @property
    def EndLine(self) -> int:
        """ Get: EndLine(self: ActivitySymbol) -> int """
        ...

    @property
    def Id(self) -> str:
        """ Get: Id(self: ActivitySymbol) -> str """
        ...

    @property
    def StartColumn(self) -> int:
        """ Get: StartColumn(self: ActivitySymbol) -> int """
        ...

    @property
    def StartLine(self) -> int:
        """ Get: StartLine(self: ActivitySymbol) -> int """
        ...


    def ToString(self) -> str:
        """ ToString(self: ActivitySymbol) -> str """
        ...


class DebugSymbol: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetSymbol(instance:object) -> object:
        """ GetSymbol(instance: object) -> object """
        ...

    @staticmethod
    def SetSymbol(instance:object, value:object): # -> 
        """ SetSymbol(instance: object, value: object) """
        ...

    SymbolName: AttachableMemberIdentifier = ...
    __all__: list = ...


class WorkflowSymbol: # skipped bases: <type 'object'>, <type 'object'>
    """ WorkflowSymbol() """
    @property
    def FileName(self) -> str:
        """
        Get: FileName(self: WorkflowSymbol) -> str
        Set: FileName(self: WorkflowSymbol) = value
        """
        ...

    @property
    def Symbols(self) -> ICollection:
        """
        Get: Symbols(self: WorkflowSymbol) -> ICollection[ActivitySymbol]
        Set: Symbols(self: WorkflowSymbol) = value
        """
        ...


    def CalculateChecksum(self) -> bool:
        """ CalculateChecksum(self: WorkflowSymbol) -> bool """
        ...

    @staticmethod
    def Decode(symbolString:str) -> WorkflowSymbol:
        """ Decode(symbolString: str) -> WorkflowSymbol """
        ...

    def Encode(self) -> str:
        """ Encode(self: WorkflowSymbol) -> str """
        ...

    def GetChecksum(self) -> Array:
        """ GetChecksum(self: WorkflowSymbol) -> Array[Byte] """
        ...

    def ToString(self) -> str:
        """ ToString(self: WorkflowSymbol) -> str """
        ...


