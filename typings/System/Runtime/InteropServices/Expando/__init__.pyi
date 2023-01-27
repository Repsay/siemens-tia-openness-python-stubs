# encoding: utf-8
# module System.Runtime.InteropServices.Expando calls itself Expando
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Delegate

from System.Reflection import (FieldInfo, IReflect, MemberInfo, MethodInfo, 
    PropertyInfo)


# no functions
# classes

class IExpando(IReflect): # skipped bases: <type 'object'>
    """ no doc """
    def AddField(self, name:str) -> FieldInfo:
        """ AddField(self: IExpando, name: str) -> FieldInfo """
        ...

    def AddMethod(self, name:str, method:Delegate) -> MethodInfo:
        """ AddMethod(self: IExpando, name: str, method: Delegate) -> MethodInfo """
        ...

    def AddProperty(self, name:str) -> PropertyInfo:
        """ AddProperty(self: IExpando, name: str) -> PropertyInfo """
        ...

    def RemoveMember(self, m:MemberInfo): # -> 
        """ RemoveMember(self: IExpando, m: MemberInfo) """
        ...


