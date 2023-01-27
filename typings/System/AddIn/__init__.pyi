# encoding: utf-8
# module System.AddIn calls itself AddIn
# from System.Windows.Presentation, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.AddIn.Contract, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.AddIn, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute

from typing import Self


# no functions
# classes

class AddInAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AddInAttribute(name: str) """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: AddInAttribute) -> str
        Set: Description(self: AddInAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: AddInAttribute) -> str """
        ...

    @property
    def Publisher(self) -> str:
        """
        Get: Publisher(self: AddInAttribute) -> str
        Set: Publisher(self: AddInAttribute) = value
        """
        ...

    @property
    def Version(self) -> str:
        """
        Get: Version(self: AddInAttribute) -> str
        Set: Version(self: AddInAttribute) = value
        """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


# variables with complex values

