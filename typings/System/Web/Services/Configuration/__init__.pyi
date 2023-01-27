# encoding: utf-8
# module System.Web.Services.Configuration calls itself Configuration
# from System.Web.Services, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Attribute, Enum, Type

from System.Configuration import (Configuration, ConfigurationElement, 
    ConfigurationElementCollection, ConfigurationSection)

from System.Web.Services import WsiProfiles

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class DiagnosticsElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ DiagnosticsElement() """
    @property
    def SuppressReturningExceptions(self) -> bool:
        """
        Get: SuppressReturningExceptions(self: DiagnosticsElement) -> bool
        Set: SuppressReturningExceptions(self: DiagnosticsElement) = value
        """
        ...



class PriorityGroup(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PriorityGroup, values: High (0), Low (1) """
    High: PriorityGroup = ...
    Low: PriorityGroup = ...
    value__ = ...


class ProtocolElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    ProtocolElement()
    ProtocolElement(protocol: WebServiceProtocols)
    """
    @property
    def Name(self) -> WebServiceProtocols:
        """
        Get: Name(self: ProtocolElement) -> WebServiceProtocols
        Set: Name(self: ProtocolElement) = value
        """
        ...


    def __new__(cls, protocol:WebServiceProtocols = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, protocol: WebServiceProtocols)
        """
        ...


class ProtocolElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ProtocolElementCollection() """
    def Add(self, element:ProtocolElement): # -> 
        """ Add(self: ProtocolElementCollection, element: ProtocolElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ProtocolElementCollection) """
        ...

    def ContainsKey(self, key:object) -> bool:
        """ ContainsKey(self: ProtocolElementCollection, key: object) -> bool """
        ...

    def IndexOf(self, element:ProtocolElement) -> int:
        """ IndexOf(self: ProtocolElementCollection, element: ProtocolElement) -> int """
        ...

    def Remove(self, element:ProtocolElement): # -> 
        """ Remove(self: ProtocolElementCollection, element: ProtocolElement) """
        ...

    def RemoveAt(self, *__args:object): # -> 
        """ RemoveAt(self: ProtocolElementCollection, key: object)RemoveAt(self: ProtocolElementCollection, index: int) """
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


class SoapEnvelopeProcessingElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    SoapEnvelopeProcessingElement()
    SoapEnvelopeProcessingElement(readTimeout: int)
    SoapEnvelopeProcessingElement(readTimeout: int, strict: bool)
    """
    @property
    def IsStrict(self) -> bool:
        """
        Get: IsStrict(self: SoapEnvelopeProcessingElement) -> bool
        Set: IsStrict(self: SoapEnvelopeProcessingElement) = value
        """
        ...

    @property
    def ReadTimeout(self) -> int:
        """
        Get: ReadTimeout(self: SoapEnvelopeProcessingElement) -> int
        Set: ReadTimeout(self: SoapEnvelopeProcessingElement) = value
        """
        ...


    def __new__(cls, readTimeout:int = ..., strict:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, readTimeout: int)
        __new__(cls: type, readTimeout: int, strict: bool)
        """
        ...


class SoapExtensionTypeElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    SoapExtensionTypeElement()
    SoapExtensionTypeElement(type: str, priority: int, group: PriorityGroup)
    SoapExtensionTypeElement(type: Type, priority: int, group: PriorityGroup)
    """
    @property
    def Group(self) -> PriorityGroup:
        """
        Get: Group(self: SoapExtensionTypeElement) -> PriorityGroup
        Set: Group(self: SoapExtensionTypeElement) = value
        """
        ...

    @property
    def Priority(self) -> int:
        """
        Get: Priority(self: SoapExtensionTypeElement) -> int
        Set: Priority(self: SoapExtensionTypeElement) = value
        """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: SoapExtensionTypeElement) -> Type
        Set: Type(self: SoapExtensionTypeElement) = value
        """
        ...


    def __new__(cls, type:str = ..., priority:int = ..., group:PriorityGroup = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: str, priority: int, group: PriorityGroup)
        __new__(cls: type, type: Type, priority: int, group: PriorityGroup)
        """
        ...


class SoapExtensionTypeElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ SoapExtensionTypeElementCollection() """
    def Add(self, element:SoapExtensionTypeElement): # -> 
        """ Add(self: SoapExtensionTypeElementCollection, element: SoapExtensionTypeElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: SoapExtensionTypeElementCollection) """
        ...

    def ContainsKey(self, key:object) -> bool:
        """ ContainsKey(self: SoapExtensionTypeElementCollection, key: object) -> bool """
        ...

    def IndexOf(self, element:SoapExtensionTypeElement) -> int:
        """ IndexOf(self: SoapExtensionTypeElementCollection, element: SoapExtensionTypeElement) -> int """
        ...

    def Remove(self, element:SoapExtensionTypeElement): # -> 
        """ Remove(self: SoapExtensionTypeElementCollection, element: SoapExtensionTypeElement) """
        ...

    def RemoveAt(self, *__args:object): # -> 
        """ RemoveAt(self: SoapExtensionTypeElementCollection, key: object)RemoveAt(self: SoapExtensionTypeElementCollection, index: int) """
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


class TypeElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    TypeElement()
    TypeElement(type: str)
    TypeElement(type: Type)
    """
    @property
    def Type(self) -> Type:
        """
        Get: Type(self: TypeElement) -> Type
        Set: Type(self: TypeElement) = value
        """
        ...


    def __new__(cls, type:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: str)
        __new__(cls: type, type: Type)
        """
        ...


class TypeElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ TypeElementCollection() """
    def Add(self, element:TypeElement): # -> 
        """ Add(self: TypeElementCollection, element: TypeElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: TypeElementCollection) """
        ...

    def ContainsKey(self, key:object) -> bool:
        """ ContainsKey(self: TypeElementCollection, key: object) -> bool """
        ...

    def IndexOf(self, element:TypeElement) -> int:
        """ IndexOf(self: TypeElementCollection, element: TypeElement) -> int """
        ...

    def Remove(self, element:TypeElement): # -> 
        """ Remove(self: TypeElementCollection, element: TypeElement) """
        ...

    def RemoveAt(self, *__args:object): # -> 
        """ RemoveAt(self: TypeElementCollection, key: object)RemoveAt(self: TypeElementCollection, index: int) """
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


class WebServiceProtocols(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) WebServiceProtocols, values: AnyHttpSoap (33), Documentation (8), HttpGet (2), HttpPost (4), HttpPostLocalhost (16), HttpSoap (1), HttpSoap12 (32), Unknown (0) """
    AnyHttpSoap: WebServiceProtocols = ...
    Documentation: WebServiceProtocols = ...
    HttpGet: WebServiceProtocols = ...
    HttpPost: WebServiceProtocols = ...
    HttpPostLocalhost: WebServiceProtocols = ...
    HttpSoap: WebServiceProtocols = ...
    HttpSoap12: WebServiceProtocols = ...
    Unknown: WebServiceProtocols = ...
    value__ = ...


class WebServicesSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ WebServicesSection() """
    @property
    def ConformanceWarnings(self) -> WsiProfilesElementCollection:
        """ Get: ConformanceWarnings(self: WebServicesSection) -> WsiProfilesElementCollection """
        ...

    @property
    def Current(self) -> WebServicesSection:
        """ Get: Current() -> WebServicesSection """
        ...

    @property
    def Diagnostics(self) -> DiagnosticsElement:
        """
        Get: Diagnostics(self: WebServicesSection) -> DiagnosticsElement
        Set: Diagnostics(self: WebServicesSection) = value
        """
        ...

    @property
    def EnabledProtocols(self) -> WebServiceProtocols:
        """ Get: EnabledProtocols(self: WebServicesSection) -> WebServiceProtocols """
        ...

    @property
    def Protocols(self) -> ProtocolElementCollection:
        """ Get: Protocols(self: WebServicesSection) -> ProtocolElementCollection """
        ...

    @property
    def ServiceDescriptionFormatExtensionTypes(self) -> TypeElementCollection:
        """ Get: ServiceDescriptionFormatExtensionTypes(self: WebServicesSection) -> TypeElementCollection """
        ...

    @property
    def SoapEnvelopeProcessing(self) -> SoapEnvelopeProcessingElement:
        """
        Get: SoapEnvelopeProcessing(self: WebServicesSection) -> SoapEnvelopeProcessingElement
        Set: SoapEnvelopeProcessing(self: WebServicesSection) = value
        """
        ...

    @property
    def SoapExtensionImporterTypes(self) -> TypeElementCollection:
        """ Get: SoapExtensionImporterTypes(self: WebServicesSection) -> TypeElementCollection """
        ...

    @property
    def SoapExtensionReflectorTypes(self) -> TypeElementCollection:
        """ Get: SoapExtensionReflectorTypes(self: WebServicesSection) -> TypeElementCollection """
        ...

    @property
    def SoapExtensionTypes(self) -> SoapExtensionTypeElementCollection:
        """ Get: SoapExtensionTypes(self: WebServicesSection) -> SoapExtensionTypeElementCollection """
        ...

    @property
    def SoapServerProtocolFactoryType(self) -> TypeElement:
        """ Get: SoapServerProtocolFactoryType(self: WebServicesSection) -> TypeElement """
        ...

    @property
    def SoapTransportImporterTypes(self) -> TypeElementCollection:
        """ Get: SoapTransportImporterTypes(self: WebServicesSection) -> TypeElementCollection """
        ...

    @property
    def WsdlHelpGenerator(self) -> WsdlHelpGeneratorElement:
        """ Get: WsdlHelpGenerator(self: WebServicesSection) -> WsdlHelpGeneratorElement """
        ...


    @staticmethod
    def GetSection(config:Configuration) -> WebServicesSection:
        """ GetSection(config: Configuration) -> WebServicesSection """
        ...



class WsdlHelpGeneratorElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ WsdlHelpGeneratorElement() """
    @property
    def Href(self) -> str:
        """
        Get: Href(self: WsdlHelpGeneratorElement) -> str
        Set: Href(self: WsdlHelpGeneratorElement) = value
        """
        ...



class WsiProfilesElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    WsiProfilesElement()
    WsiProfilesElement(name: WsiProfiles)
    """
    @property
    def Name(self) -> WsiProfiles:
        """
        Get: Name(self: WsiProfilesElement) -> WsiProfiles
        Set: Name(self: WsiProfilesElement) = value
        """
        ...


    def __new__(cls, name:WsiProfiles = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: WsiProfiles)
        """
        ...


class WsiProfilesElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ WsiProfilesElementCollection() """
    def Add(self, element:WsiProfilesElement): # -> 
        """ Add(self: WsiProfilesElementCollection, element: WsiProfilesElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: WsiProfilesElementCollection) """
        ...

    def ContainsKey(self, key:object) -> bool:
        """ ContainsKey(self: WsiProfilesElementCollection, key: object) -> bool """
        ...

    def IndexOf(self, element:WsiProfilesElement) -> int:
        """ IndexOf(self: WsiProfilesElementCollection, element: WsiProfilesElement) -> int """
        ...

    def Remove(self, element:WsiProfilesElement): # -> 
        """ Remove(self: WsiProfilesElementCollection, element: WsiProfilesElement) """
        ...

    def RemoveAt(self, *__args:object): # -> 
        """ RemoveAt(self: WsiProfilesElementCollection, key: object)RemoveAt(self: WsiProfilesElementCollection, index: int) """
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


class XmlFormatExtensionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    XmlFormatExtensionAttribute()
    XmlFormatExtensionAttribute(elementName: str, ns: str, extensionPoint1: Type)
    XmlFormatExtensionAttribute(elementName: str, ns: str, extensionPoint1: Type, extensionPoint2: Type)
    XmlFormatExtensionAttribute(elementName: str, ns: str, extensionPoint1: Type, extensionPoint2: Type, extensionPoint3: Type)
    XmlFormatExtensionAttribute(elementName: str, ns: str, extensionPoint1: Type, extensionPoint2: Type, extensionPoint3: Type, extensionPoint4: Type)
    XmlFormatExtensionAttribute(elementName: str, ns: str, extensionPoints: Array[Type])
    """
    @property
    def ElementName(self) -> str:
        """
        Get: ElementName(self: XmlFormatExtensionAttribute) -> str
        Set: ElementName(self: XmlFormatExtensionAttribute) = value
        """
        ...

    @property
    def ExtensionPoints(self) -> Array:
        """
        Get: ExtensionPoints(self: XmlFormatExtensionAttribute) -> Array[Type]
        Set: ExtensionPoints(self: XmlFormatExtensionAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: XmlFormatExtensionAttribute) -> str
        Set: Namespace(self: XmlFormatExtensionAttribute) = value
        """
        ...


    def __new__(cls, elementName:str = ..., ns:str = ..., *__args:Type) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, elementName: str, ns: str, extensionPoint1: Type)
        __new__(cls: type, elementName: str, ns: str, extensionPoint1: Type, extensionPoint2: Type)
        __new__(cls: type, elementName: str, ns: str, extensionPoint1: Type, extensionPoint2: Type, extensionPoint3: Type)
        __new__(cls: type, elementName: str, ns: str, extensionPoint1: Type, extensionPoint2: Type, extensionPoint3: Type, extensionPoint4: Type)
        __new__(cls: type, elementName: str, ns: str, extensionPoints: Array[Type])
        """
        ...


class XmlFormatExtensionPointAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ XmlFormatExtensionPointAttribute(memberName: str) """
    @property
    def AllowElements(self) -> bool:
        """
        Get: AllowElements(self: XmlFormatExtensionPointAttribute) -> bool
        Set: AllowElements(self: XmlFormatExtensionPointAttribute) = value
        """
        ...

    @property
    def MemberName(self) -> str:
        """
        Get: MemberName(self: XmlFormatExtensionPointAttribute) -> str
        Set: MemberName(self: XmlFormatExtensionPointAttribute) = value
        """
        ...


    def __new__(cls, memberName:str) -> Self:
        """ __new__(cls: type, memberName: str) """
        ...


class XmlFormatExtensionPrefixAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    XmlFormatExtensionPrefixAttribute()
    XmlFormatExtensionPrefixAttribute(prefix: str, ns: str)
    """
    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: XmlFormatExtensionPrefixAttribute) -> str
        Set: Namespace(self: XmlFormatExtensionPrefixAttribute) = value
        """
        ...

    @property
    def Prefix(self) -> str:
        """
        Get: Prefix(self: XmlFormatExtensionPrefixAttribute) -> str
        Set: Prefix(self: XmlFormatExtensionPrefixAttribute) = value
        """
        ...


    def __new__(cls, prefix:str = ..., ns:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, prefix: str, ns: str)
        """
        ...


