# encoding: utf-8
# module System.Xaml.Schema calls itself Schema
# from System.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, EventHandler, IEquatable, Type

from System.Collections import IEnumerator, IList

from System.ComponentModel import TypeConverter

from System.Reflection import MethodInfo

from System.Xaml import (INamespacePrefixLookup, IXamlNamespaceResolver, 
    XamlType)

from typing import Tuple as Tuple_

"""The following names are not found in the module: TConverterBase, field#
"""

# no functions
# classes

class AllowedMemberLocations(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) AllowedMemberLocations, values: Any (3), Attribute (1), MemberElement (2), None (0) """
    Any: AllowedMemberLocations = ...
    Attribute: AllowedMemberLocations = ...
    MemberElement: AllowedMemberLocations = ...
    value__ = ...


class ShouldSerializeResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ShouldSerializeResult, values: Default (0), False (2), True (1) """
    Default: ShouldSerializeResult = ...
    value__ = ...


class XamlCollectionKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XamlCollectionKind, values: Array (3), Collection (1), Dictionary (2), None (0) """
    Array: XamlCollectionKind = ...
    Collection: XamlCollectionKind = ...
    Dictionary: XamlCollectionKind = ...
    value__ = ...


class XamlMemberInvoker: # skipped bases: <type 'object'>, <type 'object'>
    """ XamlMemberInvoker(member: XamlMember) """
    @property
    def UnderlyingGetter(self) -> MethodInfo:
        """ Get: UnderlyingGetter(self: XamlMemberInvoker) -> MethodInfo """
        ...

    @property
    def UnderlyingSetter(self) -> MethodInfo:
        """ Get: UnderlyingSetter(self: XamlMemberInvoker) -> MethodInfo """
        ...

    @property
    def UnknownInvoker(self) -> XamlMemberInvoker:
        """ Get: UnknownInvoker() -> XamlMemberInvoker """
        ...


    def GetValue(self, instance:object) -> object:
        """ GetValue(self: XamlMemberInvoker, instance: object) -> object """
        ...

    def SetValue(self, instance:object, value:object): # -> 
        """ SetValue(self: XamlMemberInvoker, instance: object, value: object) """
        ...

    def ShouldSerializeValue(self, instance:object) -> ShouldSerializeResult:
        """ ShouldSerializeValue(self: XamlMemberInvoker, instance: object) -> ShouldSerializeResult """
        ...



class XamlTypeInvoker: # skipped bases: <type 'object'>, <type 'object'>
    """ XamlTypeInvoker(type: XamlType) """
    @property
    def SetMarkupExtensionHandler(self) -> EventHandler:
        """ Get: SetMarkupExtensionHandler(self: XamlTypeInvoker) -> EventHandler[XamlSetMarkupExtensionEventArgs] """
        ...

    @property
    def SetTypeConverterHandler(self) -> EventHandler:
        """ Get: SetTypeConverterHandler(self: XamlTypeInvoker) -> EventHandler[XamlSetTypeConverterEventArgs] """
        ...

    @property
    def UnknownInvoker(self) -> XamlTypeInvoker:
        """ Get: UnknownInvoker() -> XamlTypeInvoker """
        ...


    def AddToCollection(self, instance:object, item:object): # -> 
        """ AddToCollection(self: XamlTypeInvoker, instance: object, item: object) """
        ...

    def AddToDictionary(self, instance:object, key:object, item:object): # -> 
        """ AddToDictionary(self: XamlTypeInvoker, instance: object, key: object, item: object) """
        ...

    def CreateInstance(self, arguments:Array) -> object:
        """ CreateInstance(self: XamlTypeInvoker, arguments: Array[object]) -> object """
        ...

    def GetAddMethod(self, contentType:XamlType) -> MethodInfo:
        """ GetAddMethod(self: XamlTypeInvoker, contentType: XamlType) -> MethodInfo """
        ...

    def GetEnumeratorMethod(self) -> MethodInfo:
        """ GetEnumeratorMethod(self: XamlTypeInvoker) -> MethodInfo """
        ...

    def GetItems(self, instance:object) -> IEnumerator:
        """ GetItems(self: XamlTypeInvoker, instance: object) -> IEnumerator """
        ...



class XamlTypeName: # skipped bases: <type 'object'>, <type 'object'>
    """
    XamlTypeName()
    XamlTypeName(xamlNamespace: str, name: str)
    XamlTypeName(xamlNamespace: str, name: str, typeArguments: IEnumerable[XamlTypeName])
    XamlTypeName(xamlType: XamlType)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: XamlTypeName) -> str
        Set: Name(self: XamlTypeName) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: XamlTypeName) -> str
        Set: Namespace(self: XamlTypeName) = value
        """
        ...

    @property
    def TypeArguments(self) -> IList:
        """ Get: TypeArguments(self: XamlTypeName) -> IList[XamlTypeName] """
        ...


    @staticmethod
    def Parse(typeName:str, namespaceResolver:IXamlNamespaceResolver) -> XamlTypeName:
        """ Parse(typeName: str, namespaceResolver: IXamlNamespaceResolver) -> XamlTypeName """
        ...

    @staticmethod
    def ParseList(typeNameList:str, namespaceResolver:IXamlNamespaceResolver) -> IList:
        """ ParseList(typeNameList: str, namespaceResolver: IXamlNamespaceResolver) -> IList[XamlTypeName] """
        ...

    def ToString(self, *__args:INamespacePrefixLookup) -> str:
        """
        ToString(self: XamlTypeName) -> str
        ToString(self: XamlTypeName, prefixLookup: INamespacePrefixLookup) -> str
        ToString(typeNameList: IList[XamlTypeName], prefixLookup: INamespacePrefixLookup) -> str
        """
        ...

    @staticmethod
    def TryParse(typeName, namespaceResolver, result) -> Tuple_[bool, XamlTypeName]:
        """ TryParse(typeName: str, namespaceResolver: IXamlNamespaceResolver) -> (bool, XamlTypeName) """
        ...

    @staticmethod
    def TryParseList(typeNameList, namespaceResolver, result) -> Tuple_[bool, IList]:
        """ TryParseList(typeNameList: str, namespaceResolver: IXamlNamespaceResolver) -> (bool, IList[XamlTypeName]) """
        ...


class XamlTypeTypeConverter(TypeConverter): # skipped bases: <type 'object'>
    """ XamlTypeTypeConverter() """
    pass

class XamlValueConverter(IEquatable): # skipped bases: <type 'object'>
    """
    XamlValueConverter[TConverterBase](converterType: Type, targetType: XamlType)
    XamlValueConverter[TConverterBase](converterType: Type, targetType: XamlType, name: str)
    """
    @property
    def ConverterInstance(self): # -> TConverterBase
        """ Get: ConverterInstance(self: XamlValueConverter[TConverterBase]) -> TConverterBase """
        ...

    @property
    def ConverterType(self) -> Type:
        """ Get: ConverterType(self: XamlValueConverter[TConverterBase]) -> Type """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XamlValueConverter[TConverterBase]) -> str """
        ...

    @property
    def TargetType(self) -> XamlType:
        """ Get: TargetType(self: XamlValueConverter[TConverterBase]) -> XamlType """
        ...


    def CreateInstance(self, *args): #cannot find CLR method
        """ CreateInstance(self: XamlValueConverter[TConverterBase]) -> TConverterBase """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: XamlValueConverter[TConverterBase]) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: XamlValueConverter[TConverterBase]) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


