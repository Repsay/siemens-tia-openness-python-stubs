# encoding: utf-8
# module Microsoft.SqlServer.Management.Diagnostics calls itself Diagnostics
# from Microsoft.SqlServer.SqlTDiagM, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, UInt32


# no functions
# classes

class SQLToolsCommonTraceLvl: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Always: UInt32 = ...
    Error: UInt32 = ...
    L1: UInt32 = ...
    L2: UInt32 = ...
    L3: UInt32 = ...
    L4: UInt32 = ...
    Warning: UInt32 = ...


class STrace: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AutoFlush(self) -> bool:
        """
        Get: AutoFlush() -> bool
        Set: AutoFlush() = value
        """
        ...


    @staticmethod
    def Assert(condition:bool, message:str = ...): # -> 
        """ Assert(condition: bool, message: str)Assert(condition: bool) """
        ...

    @staticmethod
    def Enter(): # -> 
        """ Enter() """
        ...

    @staticmethod
    def Implies(premise:bool, conclusion:bool, message:str = ...): # -> 
        """ Implies(premise: bool, conclusion: bool, message: str)Implies(premise: bool, conclusion: bool) """
        ...

    @staticmethod
    def Leave(): # -> 
        """ Leave() """
        ...

    @staticmethod
    def LogExCatch(ex:Exception): # -> 
        """ LogExCatch(ex: Exception) """
        ...

    @staticmethod
    def LogExThrow(): # -> 
        """ LogExThrow() """
        ...

    @staticmethod
    def Params(strComponentName:str, strFunctionName:str, strFormat:str, arg:Array): # -> 
        """ Params(strComponentName: str, strFunctionName: str, strFormat: str, *arg: Array[object]) """
        ...

    @staticmethod
    def SetDefaultLevel(strComponentName:str, nDefaultLevel:UInt32): # -> 
        """ SetDefaultLevel(strComponentName: str, nDefaultLevel: UInt32) """
        ...

    @staticmethod
    def Trace(strComponentName:str, *__args:str): # -> 
        """ Trace(strComponentName: str, strFormat: str, *arg: Array[object])Trace(strComponentName: str, nLevel: UInt32, strFormat: str, *arg: Array[object])Trace(strComponentName: str, strLine: str)Trace(strComponentName: str, nLevel: UInt32, strLine: str) """
        ...



