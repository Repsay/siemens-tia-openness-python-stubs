# encoding: utf-8
# module System.Resources calls itself Resources
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Attribute, Enum, IDisposable, SystemException, 
    Type)

from System.Collections import IDictionaryEnumerator, IEnumerable

from System.ComponentModel.Design import ITypeResolutionService

from System.Globalization import CultureInfo

from System.IO import UnmanagedMemoryStream

from System.Reflection import AssemblyName

from System.Runtime.Serialization import ISerializable

from System.Text import Encoding

from typing import Self, Tuple as Tuple_

from Windows.Foundation import Point

"""The following names are not found in the module: (BoundEvent, Func, 
    ResXFileRef, field#)
"""

# no functions
# classes

class IResourceReader(IDisposable, IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    def Close(self): # -> 
        """ Close(self: IResourceReader) """
        ...


class IResourceWriter(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def AddResource(self, name:str, value:str): # -> 
        """ AddResource(self: IResourceWriter, name: str, value: str)AddResource(self: IResourceWriter, name: str, value: object)AddResource(self: IResourceWriter, name: str, value: Array[Byte]) """
        ...

    def Close(self): # -> 
        """ Close(self: IResourceWriter) """
        ...

    def Generate(self): # -> 
        """ Generate(self: IResourceWriter) """
        ...


class MissingManifestResourceException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MissingManifestResourceException()
    MissingManifestResourceException(message: str)
    MissingManifestResourceException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class MissingSatelliteAssemblyException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MissingSatelliteAssemblyException()
    MissingSatelliteAssemblyException(message: str)
    MissingSatelliteAssemblyException(message: str, cultureName: str)
    MissingSatelliteAssemblyException(message: str, inner: Exception)
    """
    @property
    def CultureName(self) -> str:
        """ Get: CultureName(self: MissingSatelliteAssemblyException) -> str """
        ...


    SerializeObjectState = ...


class NeutralResourcesLanguageAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    NeutralResourcesLanguageAttribute(cultureName: str)
    NeutralResourcesLanguageAttribute(cultureName: str, location: UltimateResourceFallbackLocation)
    """
    @property
    def CultureName(self) -> str:
        """ Get: CultureName(self: NeutralResourcesLanguageAttribute) -> str """
        ...

    @property
    def Location(self) -> UltimateResourceFallbackLocation:
        """ Get: Location(self: NeutralResourcesLanguageAttribute) -> UltimateResourceFallbackLocation """
        ...


    def __new__(cls, cultureName:str, location:UltimateResourceFallbackLocation = ...) -> Self:
        """
        __new__(cls: type, cultureName: str)
        __new__(cls: type, cultureName: str, location: UltimateResourceFallbackLocation)
        """
        ...


class ResourceManager: # skipped bases: <type 'object'>, <type 'object'>
    """
    ResourceManager(baseName: str, assembly: Assembly)
    ResourceManager(baseName: str, assembly: Assembly, usingResourceSet: Type)
    ResourceManager(resourceSource: Type)
    """
    @property
    def BaseName(self) -> str:
        """ Get: BaseName(self: ResourceManager) -> str """
        ...

    @property
    def FallbackLocation(self):
        ...

    @property
    def IgnoreCase(self) -> bool:
        """
        Get: IgnoreCase(self: ResourceManager) -> bool
        Set: IgnoreCase(self: ResourceManager) = value
        """
        ...

    @property
    def ResourceSetType(self) -> Type:
        """ Get: ResourceSetType(self: ResourceManager) -> Type """
        ...


    @staticmethod
    def CreateFileBasedResourceManager(baseName:str, resourceDir:str, usingResourceSet:Type) -> ResourceManager:
        """ CreateFileBasedResourceManager(baseName: str, resourceDir: str, usingResourceSet: Type) -> ResourceManager """
        ...

    def GetNeutralResourcesLanguage(self, *args): #cannot find CLR method
        """ GetNeutralResourcesLanguage(a: Assembly) -> CultureInfo """
        ...

    def GetObject(self, name:str, culture:CultureInfo = ...) -> object:
        """
        GetObject(self: ResourceManager, name: str) -> object
        GetObject(self: ResourceManager, name: str, culture: CultureInfo) -> object
        """
        ...

    def GetResourceFileName(self, *args): #cannot find CLR method
        """ GetResourceFileName(self: ResourceManager, culture: CultureInfo) -> str """
        ...

    def GetResourceSet(self, culture:CultureInfo, createIfNotExists:bool, tryParents:bool) -> ResourceSet:
        """ GetResourceSet(self: ResourceManager, culture: CultureInfo, createIfNotExists: bool, tryParents: bool) -> ResourceSet """
        ...

    def GetSatelliteContractVersion(self, *args): #cannot find CLR method
        """ GetSatelliteContractVersion(a: Assembly) -> Version """
        ...

    def GetStream(self, name:str, culture:CultureInfo = ...) -> UnmanagedMemoryStream:
        """
        GetStream(self: ResourceManager, name: str) -> UnmanagedMemoryStream
        GetStream(self: ResourceManager, name: str, culture: CultureInfo) -> UnmanagedMemoryStream
        """
        ...

    def GetString(self, name:str, culture:CultureInfo = ...) -> str:
        """
        GetString(self: ResourceManager, name: str) -> str
        GetString(self: ResourceManager, name: str, culture: CultureInfo) -> str
        """
        ...

    def InternalGetResourceSet(self, *args): #cannot find CLR method
        """ InternalGetResourceSet(self: ResourceManager, culture: CultureInfo, createIfNotExists: bool, tryParents: bool) -> ResourceSet """
        ...

    def ReleaseAllResources(self): # -> 
        """ ReleaseAllResources(self: ResourceManager) """
        ...

    BaseNameField = ...
    HeaderVersionNumber: int = ...
    MagicNumber: int = ...
    MainAssembly = ...
    ResourceSets = ...


class ResourceReader(IResourceReader): # skipped bases: <type 'IDisposable'>, <type 'IEnumerable'>, <type 'object'>
    """
    ResourceReader(fileName: str)
    ResourceReader(stream: Stream)
    """
    def Dispose(self): # -> 
        """ Dispose(self: ResourceReader) """
        ...

    def GetResourceData(self, resourceName, resourceType, resourceData) -> Tuple_[str, Array]:
        """ GetResourceData(self: ResourceReader, resourceName: str) -> (str, Array[Byte]) """
        ...


class ResourceSet(IDisposable, IEnumerable): # skipped bases: <type 'object'>
    """
    ResourceSet(fileName: str)
    ResourceSet(stream: Stream)
    ResourceSet(reader: IResourceReader)
    """
    def Close(self): # -> 
        """ Close(self: ResourceSet) """
        ...

    def GetDefaultReader(self) -> Type:
        """ GetDefaultReader(self: ResourceSet) -> Type """
        ...

    def GetDefaultWriter(self) -> Type:
        """ GetDefaultWriter(self: ResourceSet) -> Type """
        ...

    def GetObject(self, name:str, ignoreCase:bool = ...) -> object:
        """
        GetObject(self: ResourceSet, name: str) -> object
        GetObject(self: ResourceSet, name: str, ignoreCase: bool) -> object
        """
        ...

    def GetString(self, name:str, ignoreCase:bool = ...) -> str:
        """
        GetString(self: ResourceSet, name: str) -> str
        GetString(self: ResourceSet, name: str, ignoreCase: bool) -> str
        """
        ...

    def ReadResources(self, *args): #cannot find CLR method
        """ ReadResources(self: ResourceSet) """
        ...

    Reader = ...
    Table = ...


class ResourceWriter(IResourceWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    ResourceWriter(fileName: str)
    ResourceWriter(stream: Stream)
    """
    @property
    def TypeNameConverter(self): # -> Func
        """
        Get: TypeNameConverter(self: ResourceWriter) -> Func[Type, str]
        Set: TypeNameConverter(self: ResourceWriter) = value
        """
        ...


    def AddResourceData(self, name:str, typeName:str, serializedData:Array): # -> 
        """ AddResourceData(self: ResourceWriter, name: str, typeName: str, serializedData: Array[Byte]) """
        ...

    def Dispose(self): # -> 
        """ Dispose(self: ResourceWriter) """
        ...


class ResXDataNode(ISerializable): # skipped bases: <type 'object'>
    """
    ResXDataNode(name: str, value: object)
    ResXDataNode(name: str, value: object, typeNameConverter: Func[Type, str])
    ResXDataNode(name: str, fileRef: ResXFileRef)
    ResXDataNode(name: str, fileRef: ResXFileRef, typeNameConverter: Func[Type, str])
    """
    @property
    def Comment(self) -> str:
        """
        Get: Comment(self: ResXDataNode) -> str
        Set: Comment(self: ResXDataNode) = value
        """
        ...

    @property
    def FileRef(self): # -> ResXFileRef
        """ Get: FileRef(self: ResXDataNode) -> ResXFileRef """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ResXDataNode) -> str
        Set: Name(self: ResXDataNode) = value
        """
        ...


    def GetNodePosition(self) -> Point:
        """ GetNodePosition(self: ResXDataNode) -> Point """
        ...

    def GetValue(self, *__args:Array) -> object:
        """
        GetValue(self: ResXDataNode, names: Array[AssemblyName]) -> object
        GetValue(self: ResXDataNode, typeResolver: ITypeResolutionService) -> object
        """
        ...

    def GetValueTypeName(self, *__args:ITypeResolutionService) -> str:
        """
        GetValueTypeName(self: ResXDataNode, typeResolver: ITypeResolutionService) -> str
        GetValueTypeName(self: ResXDataNode, names: Array[AssemblyName]) -> str
        """
        ...


class ResXFileRef: # skipped bases: <type 'object'>, <type 'object'>
    """
    ResXFileRef(fileName: str, typeName: str)
    ResXFileRef(fileName: str, typeName: str, textFileEncoding: Encoding)
    """
    @property
    def FileName(self) -> str:
        """ Get: FileName(self: ResXFileRef) -> str """
        ...

    @property
    def TextFileEncoding(self) -> Encoding:
        """ Get: TextFileEncoding(self: ResXFileRef) -> Encoding """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: ResXFileRef) -> str """
        ...


    def Converter(self, *args): #cannot find CLR method
        """ Converter() """
        ...

    def ToString(self) -> str:
        """ ToString(self: ResXFileRef) -> str """
        ...



class ResXResourceReader(IResourceReader): # skipped bases: <type 'IDisposable'>, <type 'IEnumerable'>, <type 'object'>
    """
    ResXResourceReader(fileName: str)
    ResXResourceReader(fileName: str, typeResolver: ITypeResolutionService)
    ResXResourceReader(reader: TextReader)
    ResXResourceReader(reader: TextReader, typeResolver: ITypeResolutionService)
    ResXResourceReader(stream: Stream)
    ResXResourceReader(stream: Stream, typeResolver: ITypeResolutionService)
    ResXResourceReader(stream: Stream, assemblyNames: Array[AssemblyName])
    ResXResourceReader(reader: TextReader, assemblyNames: Array[AssemblyName])
    ResXResourceReader(fileName: str, assemblyNames: Array[AssemblyName])
    """
    @property
    def BasePath(self) -> str:
        """
        Get: BasePath(self: ResXResourceReader) -> str
        Set: BasePath(self: ResXResourceReader) = value
        """
        ...

    @property
    def UseResXDataNodes(self) -> bool:
        """
        Get: UseResXDataNodes(self: ResXResourceReader) -> bool
        Set: UseResXDataNodes(self: ResXResourceReader) = value
        """
        ...


    def Dispose(self, *args): #cannot find CLR method
        """ Dispose(self: ResXResourceReader, disposing: bool) """
        ...

    @staticmethod
    def FromFileContents(fileContents:str, *__args:ITypeResolutionService) -> ResXResourceReader:
        """
        FromFileContents(fileContents: str) -> ResXResourceReader
        FromFileContents(fileContents: str, typeResolver: ITypeResolutionService) -> ResXResourceReader
        FromFileContents(fileContents: str, assemblyNames: Array[AssemblyName]) -> ResXResourceReader
        """
        ...

    def GetMetadataEnumerator(self) -> IDictionaryEnumerator:
        """ GetMetadataEnumerator(self: ResXResourceReader) -> IDictionaryEnumerator """
        ...


class ResXResourceSet(ResourceSet): # skipped bases: <type 'IDisposable'>, <type 'IEnumerable'>, <type 'object'>
    """
    ResXResourceSet(fileName: str)
    ResXResourceSet(stream: Stream)
    """
    Reader = ...
    Table = ...


class ResXResourceWriter(IResourceWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    ResXResourceWriter(fileName: str)
    ResXResourceWriter(fileName: str, typeNameConverter: Func[Type, str])
    ResXResourceWriter(stream: Stream)
    ResXResourceWriter(stream: Stream, typeNameConverter: Func[Type, str])
    ResXResourceWriter(textWriter: TextWriter)
    ResXResourceWriter(textWriter: TextWriter, typeNameConverter: Func[Type, str])
    """
    @property
    def BasePath(self) -> str:
        """
        Get: BasePath(self: ResXResourceWriter) -> str
        Set: BasePath(self: ResXResourceWriter) = value
        """
        ...


    def AddAlias(self, aliasName:str, assemblyName:AssemblyName): # -> 
        """ AddAlias(self: ResXResourceWriter, aliasName: str, assemblyName: AssemblyName) """
        ...

    def AddMetadata(self, name:str, value:Array): # -> 
        """ AddMetadata(self: ResXResourceWriter, name: str, value: Array[Byte])AddMetadata(self: ResXResourceWriter, name: str, value: str)AddMetadata(self: ResXResourceWriter, name: str, value: object) """
        ...

    def Dispose(self): # -> 
        """ Dispose(self: ResXResourceWriter) """
        ...

    BinSerializedObjectMimeType: str = ...
    ByteArraySerializedObjectMimeType: str = ...
    DefaultSerializedObjectMimeType: str = ...
    ResMimeType: str = ...
    ResourceSchema: str = ...
    SoapSerializedObjectMimeType: str = ...
    Version: str = ...


class SatelliteContractVersionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SatelliteContractVersionAttribute(version: str) """
    @property
    def Version(self) -> str:
        """ Get: Version(self: SatelliteContractVersionAttribute) -> str """
        ...


    def __new__(cls, version:str) -> Self:
        """ __new__(cls: type, version: str) """
        ...


class UltimateResourceFallbackLocation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UltimateResourceFallbackLocation, values: MainAssembly (0), Satellite (1) """
    MainAssembly: UltimateResourceFallbackLocation = ...
    Satellite: UltimateResourceFallbackLocation = ...
    value__ = ...


# variables with complex values

