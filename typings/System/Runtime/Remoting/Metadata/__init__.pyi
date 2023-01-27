# encoding: utf-8
# module System.Runtime.Remoting.Metadata calls itself Metadata
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Enum

"""The following names are not found in the module: field#
"""

# no functions
# classes

class SoapAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SoapAttribute() """
    @property
    def Embedded(self) -> bool:
        """
        Get: Embedded(self: SoapAttribute) -> bool
        Set: Embedded(self: SoapAttribute) = value
        """
        ...

    @property
    def UseAttribute(self) -> bool:
        """
        Get: UseAttribute(self: SoapAttribute) -> bool
        Set: UseAttribute(self: SoapAttribute) = value
        """
        ...

    @property
    def XmlNamespace(self) -> str:
        """
        Get: XmlNamespace(self: SoapAttribute) -> str
        Set: XmlNamespace(self: SoapAttribute) = value
        """
        ...


    ProtXmlNamespace = ...
    ReflectInfo = ...


class SoapFieldAttribute(SoapAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SoapFieldAttribute() """
    @property
    def Order(self) -> int:
        """
        Get: Order(self: SoapFieldAttribute) -> int
        Set: Order(self: SoapFieldAttribute) = value
        """
        ...

    @property
    def XmlElementName(self) -> str:
        """
        Get: XmlElementName(self: SoapFieldAttribute) -> str
        Set: XmlElementName(self: SoapFieldAttribute) = value
        """
        ...


    def IsInteropXmlElement(self) -> bool:
        """ IsInteropXmlElement(self: SoapFieldAttribute) -> bool """
        ...

    ProtXmlNamespace = ...
    ReflectInfo = ...


class SoapMethodAttribute(SoapAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SoapMethodAttribute() """
    @property
    def ResponseXmlElementName(self) -> str:
        """
        Get: ResponseXmlElementName(self: SoapMethodAttribute) -> str
        Set: ResponseXmlElementName(self: SoapMethodAttribute) = value
        """
        ...

    @property
    def ResponseXmlNamespace(self) -> str:
        """
        Get: ResponseXmlNamespace(self: SoapMethodAttribute) -> str
        Set: ResponseXmlNamespace(self: SoapMethodAttribute) = value
        """
        ...

    @property
    def ReturnXmlElementName(self) -> str:
        """
        Get: ReturnXmlElementName(self: SoapMethodAttribute) -> str
        Set: ReturnXmlElementName(self: SoapMethodAttribute) = value
        """
        ...

    @property
    def SoapAction(self) -> str:
        """
        Get: SoapAction(self: SoapMethodAttribute) -> str
        Set: SoapAction(self: SoapMethodAttribute) = value
        """
        ...


    ProtXmlNamespace = ...
    ReflectInfo = ...


class SoapOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SoapOption, values: AlwaysIncludeTypes (1), EmbedAll (4), None (0), Option1 (8), Option2 (16), XsdString (2) """
    AlwaysIncludeTypes: SoapOption = ...
    EmbedAll: SoapOption = ...
    Option1: SoapOption = ...
    Option2: SoapOption = ...
    value__ = ...
    XsdString: SoapOption = ...


class SoapParameterAttribute(SoapAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SoapParameterAttribute() """
    ProtXmlNamespace = ...
    ReflectInfo = ...


class SoapTypeAttribute(SoapAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SoapTypeAttribute() """
    @property
    def SoapOptions(self) -> SoapOption:
        """
        Get: SoapOptions(self: SoapTypeAttribute) -> SoapOption
        Set: SoapOptions(self: SoapTypeAttribute) = value
        """
        ...

    @property
    def XmlElementName(self) -> str:
        """
        Get: XmlElementName(self: SoapTypeAttribute) -> str
        Set: XmlElementName(self: SoapTypeAttribute) = value
        """
        ...

    @property
    def XmlFieldOrder(self) -> XmlFieldOrderOption:
        """
        Get: XmlFieldOrder(self: SoapTypeAttribute) -> XmlFieldOrderOption
        Set: XmlFieldOrder(self: SoapTypeAttribute) = value
        """
        ...

    @property
    def XmlTypeName(self) -> str:
        """
        Get: XmlTypeName(self: SoapTypeAttribute) -> str
        Set: XmlTypeName(self: SoapTypeAttribute) = value
        """
        ...

    @property
    def XmlTypeNamespace(self) -> str:
        """
        Get: XmlTypeNamespace(self: SoapTypeAttribute) -> str
        Set: XmlTypeNamespace(self: SoapTypeAttribute) = value
        """
        ...


    ProtXmlNamespace = ...
    ReflectInfo = ...


class XmlFieldOrderOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlFieldOrderOption, values: All (0), Choice (2), Sequence (1) """
    All: XmlFieldOrderOption = ...
    Choice: XmlFieldOrderOption = ...
    Sequence: XmlFieldOrderOption = ...
    value__ = ...


# variables with complex values

