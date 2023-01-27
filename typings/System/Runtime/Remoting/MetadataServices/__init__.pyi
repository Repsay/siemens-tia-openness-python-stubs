# encoding: utf-8
# module System.Runtime.Remoting.MetadataServices calls itself MetadataServices
# from System.Runtime.Remoting, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, Type

from System.Collections import ArrayList, IDictionary

from System.IO import Stream

from System.Runtime.Remoting.Channels import (IServerChannelSink, 
    IServerChannelSinkProvider)

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class MetaData: # skipped bases: <type 'object'>, <type 'object'>
    """ MetaData() """
    @staticmethod
    def ConvertCodeSourceFileToAssemblyFile(codePath:str, assemblyPath:str, strongNameFilename:str): # -> 
        """ ConvertCodeSourceFileToAssemblyFile(codePath: str, assemblyPath: str, strongNameFilename: str) """
        ...

    @staticmethod
    def ConvertCodeSourceStreamToAssemblyFile(outCodeStreamList:ArrayList, assemblyPath:str, strongNameFilename:str): # -> 
        """ ConvertCodeSourceStreamToAssemblyFile(outCodeStreamList: ArrayList, assemblyPath: str, strongNameFilename: str) """
        ...

    @staticmethod
    def ConvertSchemaStreamToCodeSourceStream(clientProxy:bool, outputDirectory:str, inputStream:Stream, outCodeStreamList:ArrayList, proxyUrl:str = ..., proxyNamespace:str = ...): # -> 
        """ ConvertSchemaStreamToCodeSourceStream(clientProxy: bool, outputDirectory: str, inputStream: Stream, outCodeStreamList: ArrayList, proxyUrl: str, proxyNamespace: str)ConvertSchemaStreamToCodeSourceStream(clientProxy: bool, outputDirectory: str, inputStream: Stream, outCodeStreamList: ArrayList, proxyUrl: str)ConvertSchemaStreamToCodeSourceStream(clientProxy: bool, outputDirectory: str, inputStream: Stream, outCodeStreamList: ArrayList) """
        ...

    @staticmethod
    def ConvertTypesToSchemaToFile(types:Array, sdlType:SdlType, path:str): # -> 
        """ ConvertTypesToSchemaToFile(types: Array[Type], sdlType: SdlType, path: str)ConvertTypesToSchemaToFile(types: Array[ServiceType], sdlType: SdlType, path: str) """
        ...

    @staticmethod
    def ConvertTypesToSchemaToStream(*__args): # -> 
        """ ConvertTypesToSchemaToStream(types: Array[Type], sdlType: SdlType, outputStream: Stream)ConvertTypesToSchemaToStream(serviceTypes: Array[ServiceType], sdlType: SdlType, outputStream: Stream) """
        ...

    @staticmethod
    def RetrieveSchemaFromUrlToFile(url:str, path:str): # -> 
        """ RetrieveSchemaFromUrlToFile(url: str, path: str) """
        ...

    @staticmethod
    def RetrieveSchemaFromUrlToStream(url:str, outputStream:Stream): # -> 
        """ RetrieveSchemaFromUrlToStream(url: str, outputStream: Stream) """
        ...

    @staticmethod
    def SaveStreamToFile(inputStream:Stream, path:str): # -> 
        """ SaveStreamToFile(inputStream: Stream, path: str) """
        ...


class SdlChannelSink(IServerChannelSink): # skipped bases: <type 'IChannelSinkBase'>, <type 'object'>
    """ SdlChannelSink(receiver: IChannelReceiver, nextSink: IServerChannelSink) """
    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: SdlChannelSink) -> IDictionary """
        ...



class SdlChannelSinkProvider(IServerChannelSinkProvider): # skipped bases: <type 'object'>
    """
    SdlChannelSinkProvider()
    SdlChannelSinkProvider(properties: IDictionary, providerData: ICollection)
    """
    pass

class SdlType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SdlType, values: Sdl (0), Wsdl (1) """
    Sdl: SdlType = ...
    value__ = ...
    Wsdl: SdlType = ...


class ServiceType: # skipped bases: <type 'object'>, <type 'object'>
    """
    ServiceType(type: Type)
    ServiceType(type: Type, url: str)
    """
    @property
    def ObjectType(self) -> Type:
        """ Get: ObjectType(self: ServiceType) -> Type """
        ...

    @property
    def Url(self) -> str:
        """ Get: Url(self: ServiceType) -> str """
        ...



class SUDSGeneratorException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    SerializeObjectState = ...


class SUDSParserException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    SerializeObjectState = ...


