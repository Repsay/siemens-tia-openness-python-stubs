# encoding: utf-8
# module System.Web.Services.Discovery calls itself Discovery
# from System.Web.Services, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array

from System.Collections import (CollectionBase, DictionaryBase, ICollection, 
    IList)

from System.IO import Stream

from System.ServiceModel.Description import ServiceDescription

from System.Web import IHttpHandler

from System.Web.Services.Protocols import HttpWebClientProtocol

from System.Xml import XmlQualifiedName, XmlReader

from System.Xml.Schema import XmlSchema

from typing import Self, Tuple as Tuple_


# no functions
# classes

class DiscoveryReference: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ClientProtocol(self) -> DiscoveryClientProtocol:
        """
        Get: ClientProtocol(self: DiscoveryReference) -> DiscoveryClientProtocol
        Set: ClientProtocol(self: DiscoveryReference) = value
        """
        ...

    @property
    def DefaultFilename(self) -> str:
        """ Get: DefaultFilename(self: DiscoveryReference) -> str """
        ...

    @property
    def Url(self) -> str:
        """
        Get: Url(self: DiscoveryReference) -> str
        Set: Url(self: DiscoveryReference) = value
        """
        ...


    @staticmethod
    def FilenameFromUrl(url:str) -> str:
        """ FilenameFromUrl(url: str) -> str """
        ...

    def ReadDocument(self, stream:Stream) -> object:
        """ ReadDocument(self: DiscoveryReference, stream: Stream) -> object """
        ...

    def Resolve(self): # -> 
        """ Resolve(self: DiscoveryReference) """
        ...

    def WriteDocument(self, document:object, stream:Stream): # -> 
        """ WriteDocument(self: DiscoveryReference, document: object, stream: Stream) """
        ...


class ContractReference(DiscoveryReference): # skipped bases: <type 'object'>
    """
    ContractReference()
    ContractReference(href: str)
    ContractReference(href: str, docRef: str)
    """
    @property
    def Contract(self) -> ServiceDescription:
        """ Get: Contract(self: ContractReference) -> ServiceDescription """
        ...

    @property
    def DocRef(self) -> str:
        """
        Get: DocRef(self: ContractReference) -> str
        Set: DocRef(self: ContractReference) = value
        """
        ...

    @property
    def Ref(self) -> str:
        """
        Get: Ref(self: ContractReference) -> str
        Set: Ref(self: ContractReference) = value
        """
        ...


    def __new__(cls, href:str = ..., docRef:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, href: str)
        __new__(cls: type, href: str, docRef: str)
        """
        ...

    Namespace: str = ...


class DiscoverySearchPattern: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Pattern(self) -> str:
        """ Get: Pattern(self: DiscoverySearchPattern) -> str """
        ...


    def GetDiscoveryReference(self, filename:str) -> DiscoveryReference:
        """ GetDiscoveryReference(self: DiscoverySearchPattern, filename: str) -> DiscoveryReference """
        ...


class ContractSearchPattern(DiscoverySearchPattern): # skipped bases: <type 'object'>
    """ ContractSearchPattern() """
    pass

class DiscoveryClientDocumentCollection(DictionaryBase): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ DiscoveryClientDocumentCollection() """
    @property
    def Keys(self) -> ICollection:
        """ Get: Keys(self: DiscoveryClientDocumentCollection) -> ICollection """
        ...

    @property
    def Values(self) -> ICollection:
        """ Get: Values(self: DiscoveryClientDocumentCollection) -> ICollection """
        ...


    def Add(self, url:str, value:object): # -> 
        """ Add(self: DiscoveryClientDocumentCollection, url: str, value: object) """
        ...

    def Contains(self, url:str) -> bool:
        """ Contains(self: DiscoveryClientDocumentCollection, url: str) -> bool """
        ...

    def Remove(self, url:str): # -> 
        """ Remove(self: DiscoveryClientDocumentCollection, url: str) """
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


class DiscoveryClientProtocol(HttpWebClientProtocol): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ DiscoveryClientProtocol() """
    @property
    def AdditionalInformation(self) -> IList:
        """ Get: AdditionalInformation(self: DiscoveryClientProtocol) -> IList """
        ...

    @property
    def Documents(self) -> DiscoveryClientDocumentCollection:
        """ Get: Documents(self: DiscoveryClientProtocol) -> DiscoveryClientDocumentCollection """
        ...

    @property
    def Errors(self) -> DiscoveryExceptionDictionary:
        """ Get: Errors(self: DiscoveryClientProtocol) -> DiscoveryExceptionDictionary """
        ...

    @property
    def References(self) -> DiscoveryClientReferenceCollection:
        """ Get: References(self: DiscoveryClientProtocol) -> DiscoveryClientReferenceCollection """
        ...


    def Discover(self, url:str) -> DiscoveryDocument:
        """ Discover(self: DiscoveryClientProtocol, url: str) -> DiscoveryDocument """
        ...

    def DiscoverAny(self, url:str) -> DiscoveryDocument:
        """ DiscoverAny(self: DiscoveryClientProtocol, url: str) -> DiscoveryDocument """
        ...

    def DiscoveryClientResultsFile(self, *args): #cannot find CLR method
        """ DiscoveryClientResultsFile() """
        ...

    def Download(self, url:str, contentType:str = ...) -> Tuple_[Stream, str, str]:
        """
        Download(self: DiscoveryClientProtocol, url: str) -> (Stream, str)
        Download(self: DiscoveryClientProtocol, url: str, contentType: str) -> (Stream, str, str)
        """
        ...

    def LoadExternals(self): # -> 
        """ LoadExternals(self: DiscoveryClientProtocol) """
        ...

    def ReadAll(self, topLevelFilename:str) -> DiscoveryClientResultCollection:
        """ ReadAll(self: DiscoveryClientProtocol, topLevelFilename: str) -> DiscoveryClientResultCollection """
        ...

    def ResolveAll(self): # -> 
        """ ResolveAll(self: DiscoveryClientProtocol) """
        ...

    def ResolveOneLevel(self): # -> 
        """ ResolveOneLevel(self: DiscoveryClientProtocol) """
        ...

    def WriteAll(self, directory:str, topLevelFilename:str) -> DiscoveryClientResultCollection:
        """ WriteAll(self: DiscoveryClientProtocol, directory: str, topLevelFilename: str) -> DiscoveryClientResultCollection """
        ...



class DiscoveryClientReferenceCollection(DictionaryBase): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ DiscoveryClientReferenceCollection() """
    @property
    def Keys(self) -> ICollection:
        """ Get: Keys(self: DiscoveryClientReferenceCollection) -> ICollection """
        ...

    @property
    def Values(self) -> ICollection:
        """ Get: Values(self: DiscoveryClientReferenceCollection) -> ICollection """
        ...


    def Add(self, *__args:DiscoveryReference): # -> 
        """ Add(self: DiscoveryClientReferenceCollection, value: DiscoveryReference)Add(self: DiscoveryClientReferenceCollection, url: str, value: DiscoveryReference) """
        ...

    def Contains(self, url:str) -> bool:
        """ Contains(self: DiscoveryClientReferenceCollection, url: str) -> bool """
        ...

    def Remove(self, url:str): # -> 
        """ Remove(self: DiscoveryClientReferenceCollection, url: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class DiscoveryClientResult: # skipped bases: <type 'object'>, <type 'object'>
    """
    DiscoveryClientResult()
    DiscoveryClientResult(referenceType: Type, url: str, filename: str)
    """
    @property
    def Filename(self) -> str:
        """
        Get: Filename(self: DiscoveryClientResult) -> str
        Set: Filename(self: DiscoveryClientResult) = value
        """
        ...

    @property
    def ReferenceTypeName(self) -> str:
        """
        Get: ReferenceTypeName(self: DiscoveryClientResult) -> str
        Set: ReferenceTypeName(self: DiscoveryClientResult) = value
        """
        ...

    @property
    def Url(self) -> str:
        """
        Get: Url(self: DiscoveryClientResult) -> str
        Set: Url(self: DiscoveryClientResult) = value
        """
        ...



class DiscoveryClientResultCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DiscoveryClientResultCollection() """
    def Add(self, value:DiscoveryClientResult) -> int:
        """ Add(self: DiscoveryClientResultCollection, value: DiscoveryClientResult) -> int """
        ...

    def Contains(self, value:DiscoveryClientResult) -> bool:
        """ Contains(self: DiscoveryClientResultCollection, value: DiscoveryClientResult) -> bool """
        ...

    def Remove(self, value:DiscoveryClientResult): # -> 
        """ Remove(self: DiscoveryClientResultCollection, value: DiscoveryClientResult) """
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


class DiscoveryDocument: # skipped bases: <type 'object'>, <type 'object'>
    """ DiscoveryDocument() """
    @property
    def References(self) -> IList:
        """ Get: References(self: DiscoveryDocument) -> IList """
        ...


    @staticmethod
    def CanRead(xmlReader:XmlReader) -> bool:
        """ CanRead(xmlReader: XmlReader) -> bool """
        ...

    @staticmethod
    def Read(*__args:Stream) -> DiscoveryDocument:
        """
        Read(stream: Stream) -> DiscoveryDocument
        Read(reader: TextReader) -> DiscoveryDocument
        Read(xmlReader: XmlReader) -> DiscoveryDocument
        """
        ...

    def Write(self, *__args:Stream): # -> 
        """ Write(self: DiscoveryDocument, stream: Stream)Write(self: DiscoveryDocument, writer: TextWriter)Write(self: DiscoveryDocument, writer: XmlWriter) """
        ...

    Namespace: str = ...


class DiscoveryDocumentLinksPattern(DiscoverySearchPattern): # skipped bases: <type 'object'>
    """ DiscoveryDocumentLinksPattern() """
    pass

class DiscoveryDocumentReference(DiscoveryReference): # skipped bases: <type 'object'>
    """
    DiscoveryDocumentReference()
    DiscoveryDocumentReference(href: str)
    """
    @property
    def Document(self) -> DiscoveryDocument:
        """ Get: Document(self: DiscoveryDocumentReference) -> DiscoveryDocument """
        ...

    @property
    def Ref(self) -> str:
        """
        Get: Ref(self: DiscoveryDocumentReference) -> str
        Set: Ref(self: DiscoveryDocumentReference) = value
        """
        ...


    def ResolveAll(self): # -> 
        """ ResolveAll(self: DiscoveryDocumentReference) """
        ...

    def __new__(cls, href:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, href: str)
        """
        ...


class DiscoveryDocumentSearchPattern(DiscoverySearchPattern): # skipped bases: <type 'object'>
    """ DiscoveryDocumentSearchPattern() """
    pass

class DiscoveryExceptionDictionary(DictionaryBase): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ DiscoveryExceptionDictionary() """
    @property
    def Keys(self) -> ICollection:
        """ Get: Keys(self: DiscoveryExceptionDictionary) -> ICollection """
        ...

    @property
    def Values(self) -> ICollection:
        """ Get: Values(self: DiscoveryExceptionDictionary) -> ICollection """
        ...


    def Add(self, url:str, value:Exception): # -> 
        """ Add(self: DiscoveryExceptionDictionary, url: str, value: Exception) """
        ...

    def Contains(self, url:str) -> bool:
        """ Contains(self: DiscoveryExceptionDictionary, url: str) -> bool """
        ...

    def Remove(self, url:str): # -> 
        """ Remove(self: DiscoveryExceptionDictionary, url: str) """
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


class DiscoveryReferenceCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DiscoveryReferenceCollection() """
    def Add(self, value:DiscoveryReference) -> int:
        """ Add(self: DiscoveryReferenceCollection, value: DiscoveryReference) -> int """
        ...

    def Contains(self, value:DiscoveryReference) -> bool:
        """ Contains(self: DiscoveryReferenceCollection, value: DiscoveryReference) -> bool """
        ...

    def Remove(self, value:DiscoveryReference): # -> 
        """ Remove(self: DiscoveryReferenceCollection, value: DiscoveryReference) """
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


class DiscoveryRequestHandler(IHttpHandler): # skipped bases: <type 'object'>
    """ DiscoveryRequestHandler() """
    pass

class DynamicDiscoveryDocument: # skipped bases: <type 'object'>, <type 'object'>
    """ DynamicDiscoveryDocument() """
    @property
    def ExcludePaths(self) -> Array:
        """
        Get: ExcludePaths(self: DynamicDiscoveryDocument) -> Array[ExcludePathInfo]
        Set: ExcludePaths(self: DynamicDiscoveryDocument) = value
        """
        ...


    @staticmethod
    def Load(stream:Stream) -> DynamicDiscoveryDocument:
        """ Load(stream: Stream) -> DynamicDiscoveryDocument """
        ...

    def Write(self, stream:Stream): # -> 
        """ Write(self: DynamicDiscoveryDocument, stream: Stream) """
        ...

    Namespace: str = ...


class ExcludePathInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    ExcludePathInfo()
    ExcludePathInfo(path: str)
    """
    @property
    def Path(self) -> str:
        """
        Get: Path(self: ExcludePathInfo) -> str
        Set: Path(self: ExcludePathInfo) = value
        """
        ...



class SchemaReference(DiscoveryReference): # skipped bases: <type 'object'>
    """
    SchemaReference()
    SchemaReference(url: str)
    """
    @property
    def Ref(self) -> str:
        """
        Get: Ref(self: SchemaReference) -> str
        Set: Ref(self: SchemaReference) = value
        """
        ...

    @property
    def Schema(self) -> XmlSchema:
        """ Get: Schema(self: SchemaReference) -> XmlSchema """
        ...

    @property
    def TargetNamespace(self) -> str:
        """
        Get: TargetNamespace(self: SchemaReference) -> str
        Set: TargetNamespace(self: SchemaReference) = value
        """
        ...


    def __new__(cls, url:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, url: str)
        """
        ...

    Namespace: str = ...


class SoapBinding: # skipped bases: <type 'object'>, <type 'object'>
    """ SoapBinding() """
    @property
    def Address(self) -> str:
        """
        Get: Address(self: SoapBinding) -> str
        Set: Address(self: SoapBinding) = value
        """
        ...

    @property
    def Binding(self) -> XmlQualifiedName:
        """
        Get: Binding(self: SoapBinding) -> XmlQualifiedName
        Set: Binding(self: SoapBinding) = value
        """
        ...


    Namespace: str = ...


class XmlSchemaSearchPattern(DiscoverySearchPattern): # skipped bases: <type 'object'>
    """ XmlSchemaSearchPattern() """
    pass

