# encoding: utf-8
# module System.Runtime.Serialization.Configuration calls itself Configuration
# from System.Runtime.Serialization, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Configuration import (Configuration, ConfigurationElement, 
    ConfigurationElementCollection, ConfigurationSection, 
    ConfigurationSectionGroup)

from typing import Self


# no functions
# classes

class DataContractSerializerSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ DataContractSerializerSection() """
    @property
    def DeclaredTypes(self) -> DeclaredTypeElementCollection:
        """ Get: DeclaredTypes(self: DataContractSerializerSection) -> DeclaredTypeElementCollection """
        ...



class DeclaredTypeElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    DeclaredTypeElement()
    DeclaredTypeElement(typeName: str)
    """
    @property
    def KnownTypes(self) -> TypeElementCollection:
        """ Get: KnownTypes(self: DeclaredTypeElement) -> TypeElementCollection """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: DeclaredTypeElement) -> str
        Set: Type(self: DeclaredTypeElement) = value
        """
        ...


    def __new__(cls, typeName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, typeName: str)
        """
        ...


class DeclaredTypeElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ DeclaredTypeElementCollection() """
    def Add(self, element:DeclaredTypeElement): # -> 
        """ Add(self: DeclaredTypeElementCollection, element: DeclaredTypeElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: DeclaredTypeElementCollection) """
        ...

    def Contains(self, typeName:str) -> bool:
        """ Contains(self: DeclaredTypeElementCollection, typeName: str) -> bool """
        ...

    def IndexOf(self, element:DeclaredTypeElement) -> int:
        """ IndexOf(self: DeclaredTypeElementCollection, element: DeclaredTypeElement) -> int """
        ...

    def Remove(self, *__args:DeclaredTypeElement): # -> 
        """ Remove(self: DeclaredTypeElementCollection, element: DeclaredTypeElement)Remove(self: DeclaredTypeElementCollection, typeName: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: DeclaredTypeElementCollection, index: int) """
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


class NetDataContractSerializerSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ NetDataContractSerializerSection() """
    @property
    def EnableUnsafeTypeForwarding(self) -> bool:
        """ Get: EnableUnsafeTypeForwarding(self: NetDataContractSerializerSection) -> bool """
        ...



class ParameterElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    ParameterElement()
    ParameterElement(typeName: str)
    ParameterElement(index: int)
    """
    @property
    def Index(self) -> int:
        """
        Get: Index(self: ParameterElement) -> int
        Set: Index(self: ParameterElement) = value
        """
        ...

    @property
    def Parameters(self) -> ParameterElementCollection:
        """ Get: Parameters(self: ParameterElement) -> ParameterElementCollection """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: ParameterElement) -> str
        Set: Type(self: ParameterElement) = value
        """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, typeName: str)
        __new__(cls: type, index: int)
        """
        ...


class ParameterElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ParameterElementCollection() """
    def Add(self, element:ParameterElement): # -> 
        """ Add(self: ParameterElementCollection, element: ParameterElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ParameterElementCollection) """
        ...

    def Contains(self, typeName:str) -> bool:
        """ Contains(self: ParameterElementCollection, typeName: str) -> bool """
        ...

    def IndexOf(self, element:ParameterElement) -> int:
        """ IndexOf(self: ParameterElementCollection, element: ParameterElement) -> int """
        ...

    def Remove(self, element:ParameterElement): # -> 
        """ Remove(self: ParameterElementCollection, element: ParameterElement) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ParameterElementCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class SerializationSectionGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ SerializationSectionGroup() """
    @property
    def DataContractSerializer(self) -> DataContractSerializerSection:
        """ Get: DataContractSerializer(self: SerializationSectionGroup) -> DataContractSerializerSection """
        ...

    @property
    def NetDataContractSerializer(self) -> NetDataContractSerializerSection:
        """ Get: NetDataContractSerializer(self: SerializationSectionGroup) -> NetDataContractSerializerSection """
        ...


    @staticmethod
    def GetSectionGroup(config:Configuration) -> SerializationSectionGroup:
        """ GetSectionGroup(config: Configuration) -> SerializationSectionGroup """
        ...


class TypeElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    TypeElement()
    TypeElement(typeName: str)
    """
    @property
    def Index(self) -> int:
        """
        Get: Index(self: TypeElement) -> int
        Set: Index(self: TypeElement) = value
        """
        ...

    @property
    def Parameters(self) -> ParameterElementCollection:
        """ Get: Parameters(self: TypeElement) -> ParameterElementCollection """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: TypeElement) -> str
        Set: Type(self: TypeElement) = value
        """
        ...


    def __new__(cls, typeName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, typeName: str)
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

    def IndexOf(self, element:TypeElement) -> int:
        """ IndexOf(self: TypeElementCollection, element: TypeElement) -> int """
        ...

    def Remove(self, element:TypeElement): # -> 
        """ Remove(self: TypeElementCollection, element: TypeElement) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: TypeElementCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


