# encoding: utf-8
# module System.Data.Services.Common calls itself Common
# from System.Data.Services.Client, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Enum

from System.Collections.ObjectModel import ReadOnlyCollection

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class DataServiceEntityAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DataServiceEntityAttribute() """
    pass

class DataServiceKeyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DataServiceKeyAttribute(keyName: str)
    DataServiceKeyAttribute(*keyNames: Array[str])
    """
    @property
    def KeyNames(self) -> ReadOnlyCollection:
        """ Get: KeyNames(self: DataServiceKeyAttribute) -> ReadOnlyCollection[str] """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, keyName: str)
        __new__(cls: type, *keyNames: Array[str])
        """
        ...


class DataServiceProtocolVersion(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataServiceProtocolVersion, values: V1 (0), V2 (1) """
    V1: DataServiceProtocolVersion = ...
    V2: DataServiceProtocolVersion = ...
    value__ = ...


class EntityPropertyMappingAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    EntityPropertyMappingAttribute(sourcePath: str, targetSyndicationItem: SyndicationItemProperty, targetTextContentKind: SyndicationTextContentKind, keepInContent: bool)
    EntityPropertyMappingAttribute(sourcePath: str, targetPath: str, targetNamespacePrefix: str, targetNamespaceUri: str, keepInContent: bool)
    """
    @property
    def KeepInContent(self) -> bool:
        """ Get: KeepInContent(self: EntityPropertyMappingAttribute) -> bool """
        ...

    @property
    def SourcePath(self) -> str:
        """ Get: SourcePath(self: EntityPropertyMappingAttribute) -> str """
        ...

    @property
    def TargetNamespacePrefix(self) -> str:
        """ Get: TargetNamespacePrefix(self: EntityPropertyMappingAttribute) -> str """
        ...

    @property
    def TargetNamespaceUri(self) -> str:
        """ Get: TargetNamespaceUri(self: EntityPropertyMappingAttribute) -> str """
        ...

    @property
    def TargetPath(self) -> str:
        """ Get: TargetPath(self: EntityPropertyMappingAttribute) -> str """
        ...

    @property
    def TargetSyndicationItem(self) -> SyndicationItemProperty:
        """ Get: TargetSyndicationItem(self: EntityPropertyMappingAttribute) -> SyndicationItemProperty """
        ...

    @property
    def TargetTextContentKind(self) -> SyndicationTextContentKind:
        """ Get: TargetTextContentKind(self: EntityPropertyMappingAttribute) -> SyndicationTextContentKind """
        ...


    def __new__(cls, sourcePath, *__args) -> Self:
        """
        __new__(cls: type, sourcePath: str, targetSyndicationItem: SyndicationItemProperty, targetTextContentKind: SyndicationTextContentKind, keepInContent: bool)
        __new__(cls: type, sourcePath: str, targetPath: str, targetNamespacePrefix: str, targetNamespaceUri: str, keepInContent: bool)
        """
        ...


class EntitySetAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EntitySetAttribute(entitySet: str) """
    @property
    def EntitySet(self) -> str:
        """ Get: EntitySet(self: EntitySetAttribute) -> str """
        ...


    def __new__(cls, entitySet:str) -> Self:
        """ __new__(cls: type, entitySet: str) """
        ...


class HasStreamAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ HasStreamAttribute() """
    pass

class SyndicationItemProperty(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SyndicationItemProperty, values: AuthorEmail (1), AuthorName (2), AuthorUri (3), ContributorEmail (4), ContributorName (5), ContributorUri (6), CustomProperty (0), Published (8), Rights (9), Summary (10), Title (11), Updated (7) """
    AuthorEmail: SyndicationItemProperty = ...
    AuthorName: SyndicationItemProperty = ...
    AuthorUri: SyndicationItemProperty = ...
    ContributorEmail: SyndicationItemProperty = ...
    ContributorName: SyndicationItemProperty = ...
    ContributorUri: SyndicationItemProperty = ...
    CustomProperty: SyndicationItemProperty = ...
    Published: SyndicationItemProperty = ...
    Rights: SyndicationItemProperty = ...
    Summary: SyndicationItemProperty = ...
    Title: SyndicationItemProperty = ...
    Updated: SyndicationItemProperty = ...
    value__ = ...


class SyndicationTextContentKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SyndicationTextContentKind, values: Html (1), Plaintext (0), Xhtml (2) """
    Html: SyndicationTextContentKind = ...
    Plaintext: SyndicationTextContentKind = ...
    value__ = ...
    Xhtml: SyndicationTextContentKind = ...


