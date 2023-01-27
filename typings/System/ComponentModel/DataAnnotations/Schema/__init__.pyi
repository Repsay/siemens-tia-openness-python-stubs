# encoding: utf-8
# module System.ComponentModel.DataAnnotations.Schema calls itself Schema
# from System.ComponentModel.DataAnnotations, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Enum

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ColumnAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ColumnAttribute()
    ColumnAttribute(name: str)
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ColumnAttribute) -> str """
        ...

    @property
    def Order(self) -> int:
        """
        Get: Order(self: ColumnAttribute) -> int
        Set: Order(self: ColumnAttribute) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: ColumnAttribute) -> str
        Set: TypeName(self: ColumnAttribute) = value
        """
        ...


    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...


class ComplexTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ComplexTypeAttribute() """
    pass

class DatabaseGeneratedAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DatabaseGeneratedAttribute(databaseGeneratedOption: DatabaseGeneratedOption) """
    @property
    def DatabaseGeneratedOption(self) -> DatabaseGeneratedOption:
        """ Get: DatabaseGeneratedOption(self: DatabaseGeneratedAttribute) -> DatabaseGeneratedOption """
        ...


    def __new__(cls, databaseGeneratedOption:DatabaseGeneratedOption) -> Self:
        """ __new__(cls: type, databaseGeneratedOption: DatabaseGeneratedOption) """
        ...


class DatabaseGeneratedOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DatabaseGeneratedOption, values: Computed (2), Identity (1), None (0) """
    Computed: DatabaseGeneratedOption = ...
    Identity: DatabaseGeneratedOption = ...
    value__ = ...


class ForeignKeyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ForeignKeyAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ForeignKeyAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class InversePropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ InversePropertyAttribute(property: str) """
    @property
    def Property(self) -> str:
        """ Get: Property(self: InversePropertyAttribute) -> str """
        ...


    def __new__(cls, property:str) -> Self:
        """ __new__(cls: type, property: str) """
        ...


class NotMappedAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ NotMappedAttribute() """
    pass

class TableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TableAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: TableAttribute) -> str """
        ...

    @property
    def Schema(self) -> str:
        """
        Get: Schema(self: TableAttribute) -> str
        Set: Schema(self: TableAttribute) = value
        """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


