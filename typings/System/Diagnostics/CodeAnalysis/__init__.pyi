# encoding: utf-8
# module System.Diagnostics.CodeAnalysis calls itself CodeAnalysis
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute

from typing import Self


# no functions
# classes

class ExcludeFromCodeCoverageAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ExcludeFromCodeCoverageAttribute() """
    pass

class SuppressMessageAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SuppressMessageAttribute(category: str, checkId: str) """
    @property
    def Category(self) -> str:
        """ Get: Category(self: SuppressMessageAttribute) -> str """
        ...

    @property
    def CheckId(self) -> str:
        """ Get: CheckId(self: SuppressMessageAttribute) -> str """
        ...

    @property
    def Justification(self) -> str:
        """
        Get: Justification(self: SuppressMessageAttribute) -> str
        Set: Justification(self: SuppressMessageAttribute) = value
        """
        ...

    @property
    def MessageId(self) -> str:
        """
        Get: MessageId(self: SuppressMessageAttribute) -> str
        Set: MessageId(self: SuppressMessageAttribute) = value
        """
        ...

    @property
    def Scope(self) -> str:
        """
        Get: Scope(self: SuppressMessageAttribute) -> str
        Set: Scope(self: SuppressMessageAttribute) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: SuppressMessageAttribute) -> str
        Set: Target(self: SuppressMessageAttribute) = value
        """
        ...


    def __new__(cls, category:str, checkId:str) -> Self:
        """ __new__(cls: type, category: str, checkId: str) """
        ...


