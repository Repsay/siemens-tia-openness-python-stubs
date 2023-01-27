# encoding: utf-8
# module System.Runtime.ExceptionServices calls itself ExceptionServices
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, EventArgs

from typing import Self


# no functions
# classes

class ExceptionDispatchInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def SourceException(self) -> Exception:
        """ Get: SourceException(self: ExceptionDispatchInfo) -> Exception """
        ...


    @staticmethod
    def Capture(source:Exception) -> ExceptionDispatchInfo:
        """ Capture(source: Exception) -> ExceptionDispatchInfo """
        ...

    def Throw(self): # -> 
        """ Throw(self: ExceptionDispatchInfo) """
        ...


class FirstChanceExceptionEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ FirstChanceExceptionEventArgs(exception: Exception) """
    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: FirstChanceExceptionEventArgs) -> Exception """
        ...


    def __new__(cls, exception:Exception) -> Self:
        """ __new__(cls: type, exception: Exception) """
        ...


class HandleProcessCorruptedStateExceptionsAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ HandleProcessCorruptedStateExceptionsAttribute() """
    pass

