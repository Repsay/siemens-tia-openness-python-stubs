# encoding: utf-8
# module Microsoft.Scripting.Hosting.Configuration calls itself Configuration
# from Microsoft.Scripting, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Nullable

from System.Collections import IEnumerable

from System.Configuration import (ConfigurationElement, 
    ConfigurationElementCollection, ConfigurationSection)


# no functions
# classes

class LanguageElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ LanguageElement() """
    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: LanguageElement) -> str
        Set: DisplayName(self: LanguageElement) = value
        """
        ...

    @property
    def Extensions(self) -> str:
        """
        Get: Extensions(self: LanguageElement) -> str
        Set: Extensions(self: LanguageElement) = value
        """
        ...

    @property
    def Names(self) -> str:
        """
        Get: Names(self: LanguageElement) -> str
        Set: Names(self: LanguageElement) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: LanguageElement) -> str
        Set: Type(self: LanguageElement) = value
        """
        ...


    def GetExtensionsArray(self) -> Array:
        """ GetExtensionsArray(self: LanguageElement) -> Array[str] """
        ...

    def GetNamesArray(self) -> Array:
        """ GetNamesArray(self: LanguageElement) -> Array[str] """
        ...


class LanguageElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ LanguageElementCollection() """
    pass

class OptionElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ OptionElement() """
    @property
    def Language(self) -> str:
        """
        Get: Language(self: OptionElement) -> str
        Set: Language(self: OptionElement) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: OptionElement) -> str
        Set: Name(self: OptionElement) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: OptionElement) -> str
        Set: Value(self: OptionElement) = value
        """
        ...



class OptionElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ OptionElementCollection() """
    pass

class Section(ConfigurationSection): # skipped bases: <type 'object'>
    """ Section() """
    @property
    def DebugMode(self) -> Nullable:
        """
        Get: DebugMode(self: Section) -> Nullable[bool]
        Set: DebugMode(self: Section) = value
        """
        ...

    @property
    def PrivateBinding(self) -> Nullable:
        """
        Get: PrivateBinding(self: Section) -> Nullable[bool]
        Set: PrivateBinding(self: Section) = value
        """
        ...


    def GetLanguages(self) -> IEnumerable:
        """ GetLanguages(self: Section) -> IEnumerable[LanguageElement] """
        ...

    def GetOptions(self) -> IEnumerable:
        """ GetOptions(self: Section) -> IEnumerable[OptionElement] """
        ...

    SectionName: str = ...


