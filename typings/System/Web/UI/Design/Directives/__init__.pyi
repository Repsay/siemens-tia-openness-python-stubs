# encoding: utf-8
# module System.Web.UI.Design.Directives calls itself Directives
# from System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Version

from System.Collections.ObjectModel import ReadOnlyCollection

from typing import Self


# no functions
# classes

class DirectiveAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DirectiveAttribute() """
    @property
    def AllowedOnMobilePages(self) -> bool:
        """
        Get: AllowedOnMobilePages(self: DirectiveAttribute) -> bool
        Set: AllowedOnMobilePages(self: DirectiveAttribute) = value
        """
        ...

    @property
    def BuilderType(self) -> str:
        """
        Get: BuilderType(self: DirectiveAttribute) -> str
        Set: BuilderType(self: DirectiveAttribute) = value
        """
        ...

    @property
    def Culture(self) -> bool:
        """
        Get: Culture(self: DirectiveAttribute) -> bool
        Set: Culture(self: DirectiveAttribute) = value
        """
        ...

    @property
    def RenameType(self) -> str:
        """
        Get: RenameType(self: DirectiveAttribute) -> str
        Set: RenameType(self: DirectiveAttribute) = value
        """
        ...

    @property
    def ServerLanguageExtensions(self) -> bool:
        """
        Get: ServerLanguageExtensions(self: DirectiveAttribute) -> bool
        Set: ServerLanguageExtensions(self: DirectiveAttribute) = value
        """
        ...

    @property
    def ServerLanguageNames(self) -> bool:
        """
        Get: ServerLanguageNames(self: DirectiveAttribute) -> bool
        Set: ServerLanguageNames(self: DirectiveAttribute) = value
        """
        ...



class DirectiveRegistry: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetDirectives(frameworkVersion:Version, extension:str) -> ReadOnlyCollection:
        """ GetDirectives(frameworkVersion: Version, extension: str) -> ReadOnlyCollection[Type] """
        ...

    __all__: list = ...


class SchemaElementNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SchemaElementNameAttribute(value: str) """
    @property
    def Value(self) -> str:
        """ Get: Value(self: SchemaElementNameAttribute) -> str """
        ...


    def __new__(cls, value:str) -> Self:
        """ __new__(cls: type, value: str) """
        ...


