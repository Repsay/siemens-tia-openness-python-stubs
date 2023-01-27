# encoding: utf-8
# module System.Runtime.DesignerServices calls itself DesignerServices
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Type

from System.Collections import IEnumerable

from System.Reflection import Assembly


# no functions
# classes

class WindowsRuntimeDesignerContext: # skipped bases: <type 'object'>, <type 'object'>
    """ WindowsRuntimeDesignerContext(paths: IEnumerable[str], name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: WindowsRuntimeDesignerContext) -> str """
        ...


    def GetAssembly(self, assemblyName:str) -> Assembly:
        """ GetAssembly(self: WindowsRuntimeDesignerContext, assemblyName: str) -> Assembly """
        ...

    def GetType(self, typeName:str = ...) -> Type:
        """ GetType(self: WindowsRuntimeDesignerContext, typeName: str) -> Type """
        ...

    @staticmethod
    def InitializeSharedContext(paths:IEnumerable): # -> 
        """ InitializeSharedContext(paths: IEnumerable[str]) """
        ...

    @staticmethod
    def SetIterationContext(context:WindowsRuntimeDesignerContext): # -> 
        """ SetIterationContext(context: WindowsRuntimeDesignerContext) """
        ...


