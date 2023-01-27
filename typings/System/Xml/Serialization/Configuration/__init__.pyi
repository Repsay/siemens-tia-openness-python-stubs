# encoding: utf-8
# module System.Xml.Serialization.Configuration calls itself Configuration
# from System.Xml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Type

from System.Configuration import (ConfigurationElement, 
    ConfigurationElementCollection, ConfigurationSection, 
    ConfigurationSectionGroup, ConfigurationValidatorBase)

from typing import Self

"""The following names are not found in the module: (
    DateTimeSerializationMode)
"""

# no functions
# classes

class DateTimeSerializationSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ DateTimeSerializationSection() """
    @property
    def Mode(self): # -> DateTimeSerializationMode
        """
        Get: Mode(self: DateTimeSerializationSection) -> DateTimeSerializationMode
        Set: Mode(self: DateTimeSerializationSection) = value
        """
        ...


    def DateTimeSerializationMode(self, *args): #cannot find CLR method
        """ enum DateTimeSerializationMode, values: Default (0), Local (2), Roundtrip (1) """
        ...



class RootedPathValidator(ConfigurationValidatorBase): # skipped bases: <type 'object'>
    """ RootedPathValidator() """
    pass

class SchemaImporterExtensionElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    SchemaImporterExtensionElement()
    SchemaImporterExtensionElement(name: str, type: str)
    SchemaImporterExtensionElement(name: str, type: Type)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: SchemaImporterExtensionElement) -> str
        Set: Name(self: SchemaImporterExtensionElement) = value
        """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: SchemaImporterExtensionElement) -> Type
        Set: Type(self: SchemaImporterExtensionElement) = value
        """
        ...


    def __new__(cls, name:str = ..., type:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str, type: str)
        __new__(cls: type, name: str, type: Type)
        """
        ...


class SchemaImporterExtensionElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ SchemaImporterExtensionElementCollection() """
    def Add(self, element:SchemaImporterExtensionElement): # -> 
        """ Add(self: SchemaImporterExtensionElementCollection, element: SchemaImporterExtensionElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: SchemaImporterExtensionElementCollection) """
        ...

    def IndexOf(self, element:SchemaImporterExtensionElement) -> int:
        """ IndexOf(self: SchemaImporterExtensionElementCollection, element: SchemaImporterExtensionElement) -> int """
        ...

    def Remove(self, *__args:SchemaImporterExtensionElement): # -> 
        """ Remove(self: SchemaImporterExtensionElementCollection, element: SchemaImporterExtensionElement)Remove(self: SchemaImporterExtensionElementCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: SchemaImporterExtensionElementCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...


class SchemaImporterExtensionsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ SchemaImporterExtensionsSection() """
    @property
    def SchemaImporterExtensions(self) -> SchemaImporterExtensionElementCollection:
        """ Get: SchemaImporterExtensions(self: SchemaImporterExtensionsSection) -> SchemaImporterExtensionElementCollection """
        ...



class SerializationSectionGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ SerializationSectionGroup() """
    @property
    def DateTimeSerialization(self) -> DateTimeSerializationSection:
        """ Get: DateTimeSerialization(self: SerializationSectionGroup) -> DateTimeSerializationSection """
        ...

    @property
    def SchemaImporterExtensions(self) -> SchemaImporterExtensionsSection:
        """ Get: SchemaImporterExtensions(self: SerializationSectionGroup) -> SchemaImporterExtensionsSection """
        ...

    @property
    def XmlSerializer(self) -> XmlSerializerSection:
        """ Get: XmlSerializer(self: SerializationSectionGroup) -> XmlSerializerSection """
        ...



class XmlSerializerSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ XmlSerializerSection() """
    @property
    def CheckDeserializeAdvances(self) -> bool:
        """
        Get: CheckDeserializeAdvances(self: XmlSerializerSection) -> bool
        Set: CheckDeserializeAdvances(self: XmlSerializerSection) = value
        """
        ...

    @property
    def TempFilesLocation(self) -> str:
        """
        Get: TempFilesLocation(self: XmlSerializerSection) -> str
        Set: TempFilesLocation(self: XmlSerializerSection) = value
        """
        ...

    @property
    def UseLegacySerializerGeneration(self) -> bool:
        """
        Get: UseLegacySerializerGeneration(self: XmlSerializerSection) -> bool
        Set: UseLegacySerializerGeneration(self: XmlSerializerSection) = value
        """
        ...



