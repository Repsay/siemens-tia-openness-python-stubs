# encoding: utf-8
# module System.Runtime.Serialization.Json calls itself Json
# from System.Runtime.Serialization, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Type

from System.Collections import IEnumerable

from System.Collections.ObjectModel import ReadOnlyCollection

from System.IO import Stream

from System.Runtime.Serialization import (DateTimeFormat, EmitTypeInformation, 
    IDataContractSurrogate, XmlObjectSerializer)

from System.Text import Encoding

from System.Xml import (OnXmlDictionaryReaderClose, XmlDictionaryReader, 
    XmlDictionaryReaderQuotas, XmlDictionaryWriter)

from typing import Self


# no functions
# classes

class DataContractJsonSerializer(XmlObjectSerializer): # skipped bases: <type 'object'>
    """
    DataContractJsonSerializer(type: Type)
    DataContractJsonSerializer(type: Type, rootName: str)
    DataContractJsonSerializer(type: Type, rootName: XmlDictionaryString)
    DataContractJsonSerializer(type: Type, knownTypes: IEnumerable[Type])
    DataContractJsonSerializer(type: Type, rootName: str, knownTypes: IEnumerable[Type])
    DataContractJsonSerializer(type: Type, rootName: XmlDictionaryString, knownTypes: IEnumerable[Type])
    DataContractJsonSerializer(type: Type, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, dataContractSurrogate: IDataContractSurrogate, alwaysEmitTypeInformation: bool)
    DataContractJsonSerializer(type: Type, rootName: str, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, dataContractSurrogate: IDataContractSurrogate, alwaysEmitTypeInformation: bool)
    DataContractJsonSerializer(type: Type, rootName: XmlDictionaryString, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, dataContractSurrogate: IDataContractSurrogate, alwaysEmitTypeInformation: bool)
    DataContractJsonSerializer(type: Type, settings: DataContractJsonSerializerSettings)
    """
    @property
    def DataContractSurrogate(self) -> IDataContractSurrogate:
        """ Get: DataContractSurrogate(self: DataContractJsonSerializer) -> IDataContractSurrogate """
        ...

    @property
    def DateTimeFormat(self) -> DateTimeFormat:
        """ Get: DateTimeFormat(self: DataContractJsonSerializer) -> DateTimeFormat """
        ...

    @property
    def EmitTypeInformation(self) -> EmitTypeInformation:
        """ Get: EmitTypeInformation(self: DataContractJsonSerializer) -> EmitTypeInformation """
        ...

    @property
    def IgnoreExtensionDataObject(self) -> bool:
        """ Get: IgnoreExtensionDataObject(self: DataContractJsonSerializer) -> bool """
        ...

    @property
    def KnownTypes(self) -> ReadOnlyCollection:
        """ Get: KnownTypes(self: DataContractJsonSerializer) -> ReadOnlyCollection[Type] """
        ...

    @property
    def MaxItemsInObjectGraph(self) -> int:
        """ Get: MaxItemsInObjectGraph(self: DataContractJsonSerializer) -> int """
        ...

    @property
    def SerializeReadOnlyTypes(self) -> bool:
        """ Get: SerializeReadOnlyTypes(self: DataContractJsonSerializer) -> bool """
        ...

    @property
    def UseSimpleDictionaryFormat(self) -> bool:
        """ Get: UseSimpleDictionaryFormat(self: DataContractJsonSerializer) -> bool """
        ...


    def __new__(cls, type:Type, *__args:str) -> Self:
        """
        __new__(cls: type, type: Type)
        __new__(cls: type, type: Type, rootName: str)
        __new__(cls: type, type: Type, rootName: XmlDictionaryString)
        __new__(cls: type, type: Type, knownTypes: IEnumerable[Type])
        __new__(cls: type, type: Type, rootName: str, knownTypes: IEnumerable[Type])
        __new__(cls: type, type: Type, rootName: XmlDictionaryString, knownTypes: IEnumerable[Type])
        __new__(cls: type, type: Type, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, dataContractSurrogate: IDataContractSurrogate, alwaysEmitTypeInformation: bool)
        __new__(cls: type, type: Type, rootName: str, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, dataContractSurrogate: IDataContractSurrogate, alwaysEmitTypeInformation: bool)
        __new__(cls: type, type: Type, rootName: XmlDictionaryString, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, dataContractSurrogate: IDataContractSurrogate, alwaysEmitTypeInformation: bool)
        __new__(cls: type, type: Type, settings: DataContractJsonSerializerSettings)
        """
        ...


class DataContractJsonSerializerSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ DataContractJsonSerializerSettings() """
    @property
    def DataContractSurrogate(self) -> IDataContractSurrogate:
        """
        Get: DataContractSurrogate(self: DataContractJsonSerializerSettings) -> IDataContractSurrogate
        Set: DataContractSurrogate(self: DataContractJsonSerializerSettings) = value
        """
        ...

    @property
    def DateTimeFormat(self) -> DateTimeFormat:
        """
        Get: DateTimeFormat(self: DataContractJsonSerializerSettings) -> DateTimeFormat
        Set: DateTimeFormat(self: DataContractJsonSerializerSettings) = value
        """
        ...

    @property
    def EmitTypeInformation(self) -> EmitTypeInformation:
        """
        Get: EmitTypeInformation(self: DataContractJsonSerializerSettings) -> EmitTypeInformation
        Set: EmitTypeInformation(self: DataContractJsonSerializerSettings) = value
        """
        ...

    @property
    def IgnoreExtensionDataObject(self) -> bool:
        """
        Get: IgnoreExtensionDataObject(self: DataContractJsonSerializerSettings) -> bool
        Set: IgnoreExtensionDataObject(self: DataContractJsonSerializerSettings) = value
        """
        ...

    @property
    def KnownTypes(self) -> IEnumerable:
        """
        Get: KnownTypes(self: DataContractJsonSerializerSettings) -> IEnumerable[Type]
        Set: KnownTypes(self: DataContractJsonSerializerSettings) = value
        """
        ...

    @property
    def MaxItemsInObjectGraph(self) -> int:
        """
        Get: MaxItemsInObjectGraph(self: DataContractJsonSerializerSettings) -> int
        Set: MaxItemsInObjectGraph(self: DataContractJsonSerializerSettings) = value
        """
        ...

    @property
    def RootName(self) -> str:
        """
        Get: RootName(self: DataContractJsonSerializerSettings) -> str
        Set: RootName(self: DataContractJsonSerializerSettings) = value
        """
        ...

    @property
    def SerializeReadOnlyTypes(self) -> bool:
        """
        Get: SerializeReadOnlyTypes(self: DataContractJsonSerializerSettings) -> bool
        Set: SerializeReadOnlyTypes(self: DataContractJsonSerializerSettings) = value
        """
        ...

    @property
    def UseSimpleDictionaryFormat(self) -> bool:
        """
        Get: UseSimpleDictionaryFormat(self: DataContractJsonSerializerSettings) -> bool
        Set: UseSimpleDictionaryFormat(self: DataContractJsonSerializerSettings) = value
        """
        ...



class IXmlJsonReaderInitializer: # skipped bases: <type 'object'>
    """ no doc """
    def SetInput(self, *__args): # -> 
        """ SetInput(self: IXmlJsonReaderInitializer, buffer: Array[Byte], offset: int, count: int, encoding: Encoding, quotas: XmlDictionaryReaderQuotas, onClose: OnXmlDictionaryReaderClose)SetInput(self: IXmlJsonReaderInitializer, stream: Stream, encoding: Encoding, quotas: XmlDictionaryReaderQuotas, onClose: OnXmlDictionaryReaderClose) """
        ...


class IXmlJsonWriterInitializer: # skipped bases: <type 'object'>
    """ no doc """
    def SetOutput(self, stream:Stream, encoding:Encoding, ownsStream:bool): # -> 
        """ SetOutput(self: IXmlJsonWriterInitializer, stream: Stream, encoding: Encoding, ownsStream: bool) """
        ...


class JsonReaderWriterFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateJsonReader(*__args) -> XmlDictionaryReader:
        """
        CreateJsonReader(stream: Stream, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateJsonReader(buffer: Array[Byte], quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateJsonReader(stream: Stream, encoding: Encoding, quotas: XmlDictionaryReaderQuotas, onClose: OnXmlDictionaryReaderClose) -> XmlDictionaryReader
        CreateJsonReader(buffer: Array[Byte], offset: int, count: int, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateJsonReader(buffer: Array[Byte], offset: int, count: int, encoding: Encoding, quotas: XmlDictionaryReaderQuotas, onClose: OnXmlDictionaryReaderClose) -> XmlDictionaryReader
        """
        ...

    @staticmethod
    def CreateJsonWriter(stream:Stream, encoding:Encoding = ..., ownsStream:bool = ..., indent:bool = ..., indentChars:str = ...) -> XmlDictionaryWriter:
        """
        CreateJsonWriter(stream: Stream) -> XmlDictionaryWriter
        CreateJsonWriter(stream: Stream, encoding: Encoding) -> XmlDictionaryWriter
        CreateJsonWriter(stream: Stream, encoding: Encoding, ownsStream: bool) -> XmlDictionaryWriter
        CreateJsonWriter(stream: Stream, encoding: Encoding, ownsStream: bool, indent: bool) -> XmlDictionaryWriter
        CreateJsonWriter(stream: Stream, encoding: Encoding, ownsStream: bool, indent: bool, indentChars: str) -> XmlDictionaryWriter
        """
        ...

    __all__: list = ...


