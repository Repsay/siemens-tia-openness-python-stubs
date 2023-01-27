# encoding: utf-8
# module System.ServiceModel.Syndication calls itself Syndication
# from System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import DateTimeOffset, Enum, Int64, Type, Uri

from System.Collections import IEnumerable

from System.Collections.Generic import Dictionary

from System.Xml import XmlDictionaryReader, XmlReader, XmlWriter

from System.Xml.Serialization import IXmlSerializable

from typing import Self

"""The following names are not found in the module: (
    IExtensibleSyndicationObject, TContent, TExtension, XmlObjectSerializer, 
    field#)
"""

# no functions
# classes

class Atom10FeedFormatter: # skipped bases: <type 'object'>
    """
    Atom10FeedFormatter()
    Atom10FeedFormatter(feedTypeToCreate: Type)
    Atom10FeedFormatter(feedToWrite: SyndicationFeed)
    """
    @property
    def FeedType(self):
        ...

    @property
    def PreserveAttributeExtensions(self) -> bool:
        """
        Get: PreserveAttributeExtensions(self: Atom10FeedFormatter) -> bool
        Set: PreserveAttributeExtensions(self: Atom10FeedFormatter) = value
        """
        ...

    @property
    def PreserveElementExtensions(self) -> bool:
        """
        Get: PreserveElementExtensions(self: Atom10FeedFormatter) -> bool
        Set: PreserveElementExtensions(self: Atom10FeedFormatter) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: Atom10FeedFormatter) -> str """
        ...


    def CanRead(self, reader:XmlReader) -> bool:
        """ CanRead(self: Atom10FeedFormatter, reader: XmlReader) -> bool """
        ...

    def CreateFeedInstance(self, *args): #cannot find CLR method
        """ CreateFeedInstance(self: Atom10FeedFormatter) -> SyndicationFeed """
        ...

    def ReadFrom(self, reader:XmlReader): # -> 
        """ ReadFrom(self: Atom10FeedFormatter, reader: XmlReader) """
        ...

    def ReadItem(self, *args): #cannot find CLR method
        """ ReadItem(self: Atom10FeedFormatter, reader: XmlReader, feed: SyndicationFeed) -> SyndicationItem """
        ...

    def ReadItems(self, *args): #cannot find CLR method
        """ ReadItems(self: Atom10FeedFormatter, reader: XmlReader, feed: SyndicationFeed) -> (IEnumerable[SyndicationItem], bool) """
        ...

    def SetFeed(self, *args): #cannot find CLR method
        """ SetFeed(self: SyndicationFeedFormatter, feed: SyndicationFeed) """
        ...

    def WriteItem(self, *args): #cannot find CLR method
        """ WriteItem(self: Atom10FeedFormatter, writer: XmlWriter, item: SyndicationItem, feedBaseUri: Uri) """
        ...

    def WriteItems(self, *args): #cannot find CLR method
        """ WriteItems(self: Atom10FeedFormatter, writer: XmlWriter, items: IEnumerable[SyndicationItem], feedBaseUri: Uri) """
        ...

    def WriteTo(self, writer:XmlWriter): # -> 
        """ WriteTo(self: Atom10FeedFormatter, writer: XmlWriter) """
        ...

    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, feedTypeToCreate: Type)
        __new__(cls: type, feedToWrite: SyndicationFeed)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class Atom10ItemFormatter: # skipped bases: <type 'object'>
    """
    Atom10ItemFormatter()
    Atom10ItemFormatter(itemTypeToCreate: Type)
    Atom10ItemFormatter(itemToWrite: SyndicationItem)
    """
    @property
    def ItemType(self):
        ...

    @property
    def PreserveAttributeExtensions(self) -> bool:
        """
        Get: PreserveAttributeExtensions(self: Atom10ItemFormatter) -> bool
        Set: PreserveAttributeExtensions(self: Atom10ItemFormatter) = value
        """
        ...

    @property
    def PreserveElementExtensions(self) -> bool:
        """
        Get: PreserveElementExtensions(self: Atom10ItemFormatter) -> bool
        Set: PreserveElementExtensions(self: Atom10ItemFormatter) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: Atom10ItemFormatter) -> str """
        ...


    def CanRead(self, reader:XmlReader) -> bool:
        """ CanRead(self: Atom10ItemFormatter, reader: XmlReader) -> bool """
        ...

    def CreateItemInstance(self, *args): #cannot find CLR method
        """ CreateItemInstance(self: Atom10ItemFormatter) -> SyndicationItem """
        ...

    def ReadFrom(self, reader:XmlReader): # -> 
        """ ReadFrom(self: Atom10ItemFormatter, reader: XmlReader) """
        ...

    def SetItem(self, *args): #cannot find CLR method
        """ SetItem(self: SyndicationItemFormatter, item: SyndicationItem) """
        ...

    def WriteElementExtensions(self, *args): #cannot find CLR method
        """ WriteElementExtensions(writer: XmlWriter, item: SyndicationItem, version: str)WriteElementExtensions(self: SyndicationItemFormatter, writer: XmlWriter, category: SyndicationCategory, version: str)WriteElementExtensions(self: SyndicationItemFormatter, writer: XmlWriter, link: SyndicationLink, version: str)WriteElementExtensions(self: SyndicationItemFormatter, writer: XmlWriter, person: SyndicationPerson, version: str) """
        ...

    def WriteTo(self, writer:XmlWriter): # -> 
        """ WriteTo(self: Atom10ItemFormatter, writer: XmlWriter) """
        ...

    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, itemTypeToCreate: Type)
        __new__(cls: type, itemToWrite: SyndicationItem)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class CategoriesDocumentFormatter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Document(self) -> CategoriesDocument:
        """ Get: Document(self: CategoriesDocumentFormatter) -> CategoriesDocument """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: CategoriesDocumentFormatter) -> str """
        ...


    def CanRead(self, reader:XmlReader) -> bool:
        """ CanRead(self: CategoriesDocumentFormatter, reader: XmlReader) -> bool """
        ...

    def CreateInlineCategoriesDocument(self, *args): #cannot find CLR method
        """ CreateInlineCategoriesDocument(self: CategoriesDocumentFormatter) -> InlineCategoriesDocument """
        ...

    def CreateReferencedCategoriesDocument(self, *args): #cannot find CLR method
        """ CreateReferencedCategoriesDocument(self: CategoriesDocumentFormatter) -> ReferencedCategoriesDocument """
        ...

    def ReadFrom(self, reader:XmlReader): # -> 
        """ ReadFrom(self: CategoriesDocumentFormatter, reader: XmlReader) """
        ...

    def SetDocument(self, *args): #cannot find CLR method
        """ SetDocument(self: CategoriesDocumentFormatter, document: CategoriesDocument) """
        ...

    def WriteTo(self, writer:XmlWriter): # -> 
        """ WriteTo(self: CategoriesDocumentFormatter, writer: XmlWriter) """
        ...


class AtomPub10CategoriesDocumentFormatter(CategoriesDocumentFormatter, IXmlSerializable): # skipped bases: <type 'object'>
    """
    AtomPub10CategoriesDocumentFormatter()
    AtomPub10CategoriesDocumentFormatter(inlineDocumentType: Type, referencedDocumentType: Type)
    AtomPub10CategoriesDocumentFormatter(documentToWrite: CategoriesDocument)
    """
    pass

class AtomPub10ServiceDocumentFormatter: # skipped bases: <type 'object'>
    """
    AtomPub10ServiceDocumentFormatter()
    AtomPub10ServiceDocumentFormatter(documentTypeToCreate: Type)
    AtomPub10ServiceDocumentFormatter(documentToWrite: ServiceDocument)
    """
    @property
    def Version(self) -> str:
        """ Get: Version(self: AtomPub10ServiceDocumentFormatter) -> str """
        ...


    def CanRead(self, reader:XmlReader) -> bool:
        """ CanRead(self: AtomPub10ServiceDocumentFormatter, reader: XmlReader) -> bool """
        ...

    def CreateDocumentInstance(self, *args): #cannot find CLR method
        """ CreateDocumentInstance(self: AtomPub10ServiceDocumentFormatter) -> ServiceDocument """
        ...

    def ReadFrom(self, reader:XmlReader): # -> 
        """ ReadFrom(self: AtomPub10ServiceDocumentFormatter, reader: XmlReader) """
        ...

    def SetDocument(self, *args): #cannot find CLR method
        """ SetDocument(self: ServiceDocumentFormatter, document: ServiceDocument) """
        ...

    def WriteTo(self, writer:XmlWriter): # -> 
        """ WriteTo(self: AtomPub10ServiceDocumentFormatter, writer: XmlWriter) """
        ...

    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, documentTypeToCreate: Type)
        __new__(cls: type, documentToWrite: ServiceDocument)
        """
        ...


class CategoriesDocument(IExtensibleSyndicationObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AttributeExtensions(self) -> Dictionary:
        """ Get: AttributeExtensions(self: CategoriesDocument) -> Dictionary[XmlQualifiedName, str] """
        ...

    @property
    def BaseUri(self) -> Uri:
        """
        Get: BaseUri(self: CategoriesDocument) -> Uri
        Set: BaseUri(self: CategoriesDocument) = value
        """
        ...

    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection:
        """ Get: ElementExtensions(self: CategoriesDocument) -> SyndicationElementExtensionCollection """
        ...

    @property
    def Language(self) -> str:
        """
        Get: Language(self: CategoriesDocument) -> str
        Set: Language(self: CategoriesDocument) = value
        """
        ...


    @staticmethod
    def Create(*__args:Collection) -> InlineCategoriesDocument:
        """
        Create(categories: Collection[SyndicationCategory]) -> InlineCategoriesDocument
        Create(categories: Collection[SyndicationCategory], isFixed: bool, scheme: str) -> InlineCategoriesDocument
        Create(linkToCategoriesDocument: Uri) -> ReferencedCategoriesDocument
        """
        ...

    def GetFormatter(self) -> CategoriesDocumentFormatter:
        """ GetFormatter(self: CategoriesDocument) -> CategoriesDocumentFormatter """
        ...

    @staticmethod
    def Load(reader:XmlReader) -> CategoriesDocument:
        """ Load(reader: XmlReader) -> CategoriesDocument """
        ...

    def Save(self, writer:XmlWriter): # -> 
        """ Save(self: CategoriesDocument, writer: XmlWriter) """
        ...

    def TryParseAttribute(self, *args): #cannot find CLR method
        """ TryParseAttribute(self: CategoriesDocument, name: str, ns: str, value: str, version: str) -> bool """
        ...

    def TryParseElement(self, *args): #cannot find CLR method
        """ TryParseElement(self: CategoriesDocument, reader: XmlReader, version: str) -> bool """
        ...

    def WriteAttributeExtensions(self, *args): #cannot find CLR method
        """ WriteAttributeExtensions(self: CategoriesDocument, writer: XmlWriter, version: str) """
        ...

    def WriteElementExtensions(self, *args): #cannot find CLR method
        """ WriteElementExtensions(self: CategoriesDocument, writer: XmlWriter, version: str) """
        ...


class InlineCategoriesDocument(CategoriesDocument): # skipped bases: <type 'IExtensibleSyndicationObject'>, <type 'object'>
    """
    InlineCategoriesDocument()
    InlineCategoriesDocument(categories: IEnumerable[SyndicationCategory])
    InlineCategoriesDocument(categories: IEnumerable[SyndicationCategory], isFixed: bool, scheme: str)
    """
    @property
    def Categories(self) -> Collection:
        """ Get: Categories(self: InlineCategoriesDocument) -> Collection[SyndicationCategory] """
        ...

    @property
    def IsFixed(self) -> bool:
        """
        Get: IsFixed(self: InlineCategoriesDocument) -> bool
        Set: IsFixed(self: InlineCategoriesDocument) = value
        """
        ...

    @property
    def Scheme(self) -> str:
        """
        Get: Scheme(self: InlineCategoriesDocument) -> str
        Set: Scheme(self: InlineCategoriesDocument) = value
        """
        ...


    def CreateCategory(self, *args): #cannot find CLR method
        """ CreateCategory(self: InlineCategoriesDocument) -> SyndicationCategory """
        ...

    def __new__(cls, categories:IEnumerable = ..., isFixed:bool = ..., scheme:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, categories: IEnumerable[SyndicationCategory])
        __new__(cls: type, categories: IEnumerable[SyndicationCategory], isFixed: bool, scheme: str)
        """
        ...


class ReferencedCategoriesDocument(CategoriesDocument): # skipped bases: <type 'IExtensibleSyndicationObject'>, <type 'object'>
    """
    ReferencedCategoriesDocument()
    ReferencedCategoriesDocument(link: Uri)
    """
    @property
    def Link(self) -> Uri:
        """
        Get: Link(self: ReferencedCategoriesDocument) -> Uri
        Set: Link(self: ReferencedCategoriesDocument) = value
        """
        ...


    def __new__(cls, link:Uri = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, link: Uri)
        """
        ...


class ResourceCollectionInfo(IExtensibleSyndicationObject): # skipped bases: <type 'object'>
    """
    ResourceCollectionInfo()
    ResourceCollectionInfo(title: str, link: Uri)
    ResourceCollectionInfo(title: TextSyndicationContent, link: Uri)
    ResourceCollectionInfo(title: TextSyndicationContent, link: Uri, categories: IEnumerable[CategoriesDocument], allowsNewEntries: bool)
    ResourceCollectionInfo(title: TextSyndicationContent, link: Uri, categories: IEnumerable[CategoriesDocument], accepts: IEnumerable[str])
    """
    @property
    def Accepts(self) -> Collection:
        """ Get: Accepts(self: ResourceCollectionInfo) -> Collection[str] """
        ...

    @property
    def AttributeExtensions(self) -> Dictionary:
        """ Get: AttributeExtensions(self: ResourceCollectionInfo) -> Dictionary[XmlQualifiedName, str] """
        ...

    @property
    def BaseUri(self) -> Uri:
        """
        Get: BaseUri(self: ResourceCollectionInfo) -> Uri
        Set: BaseUri(self: ResourceCollectionInfo) = value
        """
        ...

    @property
    def Categories(self) -> Collection:
        """ Get: Categories(self: ResourceCollectionInfo) -> Collection[CategoriesDocument] """
        ...

    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection:
        """ Get: ElementExtensions(self: ResourceCollectionInfo) -> SyndicationElementExtensionCollection """
        ...

    @property
    def Link(self) -> Uri:
        """
        Get: Link(self: ResourceCollectionInfo) -> Uri
        Set: Link(self: ResourceCollectionInfo) = value
        """
        ...

    @property
    def Title(self) -> TextSyndicationContent:
        """
        Get: Title(self: ResourceCollectionInfo) -> TextSyndicationContent
        Set: Title(self: ResourceCollectionInfo) = value
        """
        ...


    def CreateInlineCategoriesDocument(self, *args): #cannot find CLR method
        """ CreateInlineCategoriesDocument(self: ResourceCollectionInfo) -> InlineCategoriesDocument """
        ...

    def CreateReferencedCategoriesDocument(self, *args): #cannot find CLR method
        """ CreateReferencedCategoriesDocument(self: ResourceCollectionInfo) -> ReferencedCategoriesDocument """
        ...

    def TryParseAttribute(self, *args): #cannot find CLR method
        """ TryParseAttribute(self: ResourceCollectionInfo, name: str, ns: str, value: str, version: str) -> bool """
        ...

    def TryParseElement(self, *args): #cannot find CLR method
        """ TryParseElement(self: ResourceCollectionInfo, reader: XmlReader, version: str) -> bool """
        ...

    def WriteAttributeExtensions(self, *args): #cannot find CLR method
        """ WriteAttributeExtensions(self: ResourceCollectionInfo, writer: XmlWriter, version: str) """
        ...

    def WriteElementExtensions(self, *args): #cannot find CLR method
        """ WriteElementExtensions(self: ResourceCollectionInfo, writer: XmlWriter, version: str) """
        ...


class Rss20FeedFormatter: # skipped bases: <type 'object'>
    """
    Rss20FeedFormatter()
    Rss20FeedFormatter(feedTypeToCreate: Type)
    Rss20FeedFormatter(feedToWrite: SyndicationFeed)
    Rss20FeedFormatter(feedToWrite: SyndicationFeed, serializeExtensionsAsAtom: bool)
    """
    @property
    def FeedType(self):
        ...

    @property
    def PreserveAttributeExtensions(self) -> bool:
        """
        Get: PreserveAttributeExtensions(self: Rss20FeedFormatter) -> bool
        Set: PreserveAttributeExtensions(self: Rss20FeedFormatter) = value
        """
        ...

    @property
    def PreserveElementExtensions(self) -> bool:
        """
        Get: PreserveElementExtensions(self: Rss20FeedFormatter) -> bool
        Set: PreserveElementExtensions(self: Rss20FeedFormatter) = value
        """
        ...

    @property
    def SerializeExtensionsAsAtom(self) -> bool:
        """
        Get: SerializeExtensionsAsAtom(self: Rss20FeedFormatter) -> bool
        Set: SerializeExtensionsAsAtom(self: Rss20FeedFormatter) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: Rss20FeedFormatter) -> str """
        ...


    def CanRead(self, reader:XmlReader) -> bool:
        """ CanRead(self: Rss20FeedFormatter, reader: XmlReader) -> bool """
        ...

    def CreateFeedInstance(self, *args): #cannot find CLR method
        """ CreateFeedInstance(self: Rss20FeedFormatter) -> SyndicationFeed """
        ...

    def ReadFrom(self, reader:XmlReader): # -> 
        """ ReadFrom(self: Rss20FeedFormatter, reader: XmlReader) """
        ...

    def ReadItem(self, *args): #cannot find CLR method
        """ ReadItem(self: Rss20FeedFormatter, reader: XmlReader, feed: SyndicationFeed) -> SyndicationItem """
        ...

    def ReadItems(self, *args): #cannot find CLR method
        """ ReadItems(self: Rss20FeedFormatter, reader: XmlReader, feed: SyndicationFeed) -> (IEnumerable[SyndicationItem], bool) """
        ...

    def SetFeed(self, *args): #cannot find CLR method
        """ SetFeed(self: Rss20FeedFormatter, feed: SyndicationFeed) """
        ...

    def WriteItem(self, *args): #cannot find CLR method
        """ WriteItem(self: Rss20FeedFormatter, writer: XmlWriter, item: SyndicationItem, feedBaseUri: Uri) """
        ...

    def WriteItems(self, *args): #cannot find CLR method
        """ WriteItems(self: Rss20FeedFormatter, writer: XmlWriter, items: IEnumerable[SyndicationItem], feedBaseUri: Uri) """
        ...

    def WriteTo(self, writer:XmlWriter): # -> 
        """ WriteTo(self: Rss20FeedFormatter, writer: XmlWriter) """
        ...

    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, feedTypeToCreate: Type)
        __new__(cls: type, feedToWrite: SyndicationFeed)
        __new__(cls: type, feedToWrite: SyndicationFeed, serializeExtensionsAsAtom: bool)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class Rss20ItemFormatter: # skipped bases: <type 'object'>
    """
    Rss20ItemFormatter()
    Rss20ItemFormatter(itemTypeToCreate: Type)
    Rss20ItemFormatter(itemToWrite: SyndicationItem)
    Rss20ItemFormatter(itemToWrite: SyndicationItem, serializeExtensionsAsAtom: bool)
    """
    @property
    def ItemType(self):
        ...

    @property
    def PreserveAttributeExtensions(self) -> bool:
        """
        Get: PreserveAttributeExtensions(self: Rss20ItemFormatter) -> bool
        Set: PreserveAttributeExtensions(self: Rss20ItemFormatter) = value
        """
        ...

    @property
    def PreserveElementExtensions(self) -> bool:
        """
        Get: PreserveElementExtensions(self: Rss20ItemFormatter) -> bool
        Set: PreserveElementExtensions(self: Rss20ItemFormatter) = value
        """
        ...

    @property
    def SerializeExtensionsAsAtom(self) -> bool:
        """
        Get: SerializeExtensionsAsAtom(self: Rss20ItemFormatter) -> bool
        Set: SerializeExtensionsAsAtom(self: Rss20ItemFormatter) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: Rss20ItemFormatter) -> str """
        ...


    def CanRead(self, reader:XmlReader) -> bool:
        """ CanRead(self: Rss20ItemFormatter, reader: XmlReader) -> bool """
        ...

    def CreateItemInstance(self, *args): #cannot find CLR method
        """ CreateItemInstance(self: Rss20ItemFormatter) -> SyndicationItem """
        ...

    def ReadFrom(self, reader:XmlReader): # -> 
        """ ReadFrom(self: Rss20ItemFormatter, reader: XmlReader) """
        ...

    def SetItem(self, *args): #cannot find CLR method
        """ SetItem(self: SyndicationItemFormatter, item: SyndicationItem) """
        ...

    def WriteElementExtensions(self, *args): #cannot find CLR method
        """ WriteElementExtensions(writer: XmlWriter, item: SyndicationItem, version: str)WriteElementExtensions(self: SyndicationItemFormatter, writer: XmlWriter, category: SyndicationCategory, version: str)WriteElementExtensions(self: SyndicationItemFormatter, writer: XmlWriter, link: SyndicationLink, version: str)WriteElementExtensions(self: SyndicationItemFormatter, writer: XmlWriter, person: SyndicationPerson, version: str) """
        ...

    def WriteTo(self, writer:XmlWriter): # -> 
        """ WriteTo(self: Rss20ItemFormatter, writer: XmlWriter) """
        ...

    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, itemTypeToCreate: Type)
        __new__(cls: type, itemToWrite: SyndicationItem)
        __new__(cls: type, itemToWrite: SyndicationItem, serializeExtensionsAsAtom: bool)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class ServiceDocument(IExtensibleSyndicationObject): # skipped bases: <type 'object'>
    """
    ServiceDocument()
    ServiceDocument(workspaces: IEnumerable[Workspace])
    """
    @property
    def AttributeExtensions(self) -> Dictionary:
        """ Get: AttributeExtensions(self: ServiceDocument) -> Dictionary[XmlQualifiedName, str] """
        ...

    @property
    def BaseUri(self) -> Uri:
        """
        Get: BaseUri(self: ServiceDocument) -> Uri
        Set: BaseUri(self: ServiceDocument) = value
        """
        ...

    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection:
        """ Get: ElementExtensions(self: ServiceDocument) -> SyndicationElementExtensionCollection """
        ...

    @property
    def Language(self) -> str:
        """
        Get: Language(self: ServiceDocument) -> str
        Set: Language(self: ServiceDocument) = value
        """
        ...

    @property
    def Workspaces(self) -> Collection:
        """ Get: Workspaces(self: ServiceDocument) -> Collection[Workspace] """
        ...


    def CreateWorkspace(self, *args): #cannot find CLR method
        """ CreateWorkspace(self: ServiceDocument) -> Workspace """
        ...

    def GetFormatter(self) -> ServiceDocumentFormatter:
        """ GetFormatter(self: ServiceDocument) -> ServiceDocumentFormatter """
        ...

    @staticmethod
    def Load(reader):
        """ no doc """
        ...

    def Save(self, writer:XmlWriter): # -> 
        """ Save(self: ServiceDocument, writer: XmlWriter) """
        ...

    def TryParseAttribute(self, *args): #cannot find CLR method
        """ TryParseAttribute(self: ServiceDocument, name: str, ns: str, value: str, version: str) -> bool """
        ...

    def TryParseElement(self, *args): #cannot find CLR method
        """ TryParseElement(self: ServiceDocument, reader: XmlReader, version: str) -> bool """
        ...

    def WriteAttributeExtensions(self, *args): #cannot find CLR method
        """ WriteAttributeExtensions(self: ServiceDocument, writer: XmlWriter, version: str) """
        ...

    def WriteElementExtensions(self, *args): #cannot find CLR method
        """ WriteElementExtensions(self: ServiceDocument, writer: XmlWriter, version: str) """
        ...


class ServiceDocumentFormatter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Document(self) -> ServiceDocument:
        """ Get: Document(self: ServiceDocumentFormatter) -> ServiceDocument """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: ServiceDocumentFormatter) -> str """
        ...


    def CanRead(self, reader:XmlReader) -> bool:
        """ CanRead(self: ServiceDocumentFormatter, reader: XmlReader) -> bool """
        ...

    def CreateCategory(self, *args): #cannot find CLR method
        """ CreateCategory(inlineCategories: InlineCategoriesDocument) -> SyndicationCategory """
        ...

    def CreateCollection(self, *args): #cannot find CLR method
        """ CreateCollection(workspace: Workspace) -> ResourceCollectionInfo """
        ...

    def CreateDocumentInstance(self, *args): #cannot find CLR method
        """ CreateDocumentInstance(self: ServiceDocumentFormatter) -> ServiceDocument """
        ...

    def CreateInlineCategories(self, *args): #cannot find CLR method
        """ CreateInlineCategories(collection: ResourceCollectionInfo) -> InlineCategoriesDocument """
        ...

    def CreateReferencedCategories(self, *args): #cannot find CLR method
        """ CreateReferencedCategories(collection: ResourceCollectionInfo) -> ReferencedCategoriesDocument """
        ...

    def CreateWorkspace(self, *args): #cannot find CLR method
        """ CreateWorkspace(document: ServiceDocument) -> Workspace """
        ...

    def LoadElementExtensions(self, *args): #cannot find CLR method
        """ LoadElementExtensions(reader: XmlReader, categories: CategoriesDocument, maxExtensionSize: int)LoadElementExtensions(reader: XmlReader, collection: ResourceCollectionInfo, maxExtensionSize: int)LoadElementExtensions(reader: XmlReader, workspace: Workspace, maxExtensionSize: int)LoadElementExtensions(reader: XmlReader, document: ServiceDocument, maxExtensionSize: int) """
        ...

    def ReadFrom(self, reader:XmlReader): # -> 
        """ ReadFrom(self: ServiceDocumentFormatter, reader: XmlReader) """
        ...

    def SetDocument(self, *args): #cannot find CLR method
        """ SetDocument(self: ServiceDocumentFormatter, document: ServiceDocument) """
        ...

    def TryParseAttribute(self, *args): #cannot find CLR method
        """
        TryParseAttribute(name: str, ns: str, value: str, document: ServiceDocument, version: str) -> bool
        TryParseAttribute(name: str, ns: str, value: str, collection: ResourceCollectionInfo, version: str) -> bool
        TryParseAttribute(name: str, ns: str, value: str, categories: CategoriesDocument, version: str) -> bool
        TryParseAttribute(name: str, ns: str, value: str, workspace: Workspace, version: str) -> bool
        """
        ...

    def TryParseElement(self, *args): #cannot find CLR method
        """
        TryParseElement(reader: XmlReader, collection: ResourceCollectionInfo, version: str) -> bool
        TryParseElement(reader: XmlReader, document: ServiceDocument, version: str) -> bool
        TryParseElement(reader: XmlReader, workspace: Workspace, version: str) -> bool
        TryParseElement(reader: XmlReader, categories: CategoriesDocument, version: str) -> bool
        """
        ...

    def WriteAttributeExtensions(self, *args): #cannot find CLR method
        """ WriteAttributeExtensions(writer: XmlWriter, document: ServiceDocument, version: str)WriteAttributeExtensions(writer: XmlWriter, workspace: Workspace, version: str)WriteAttributeExtensions(writer: XmlWriter, collection: ResourceCollectionInfo, version: str)WriteAttributeExtensions(writer: XmlWriter, categories: CategoriesDocument, version: str) """
        ...

    def WriteElementExtensions(self, *args): #cannot find CLR method
        """ WriteElementExtensions(writer: XmlWriter, document: ServiceDocument, version: str)WriteElementExtensions(writer: XmlWriter, workspace: Workspace, version: str)WriteElementExtensions(writer: XmlWriter, collection: ResourceCollectionInfo, version: str)WriteElementExtensions(writer: XmlWriter, categories: CategoriesDocument, version: str) """
        ...

    def WriteTo(self, writer:XmlWriter): # -> 
        """ WriteTo(self: ServiceDocumentFormatter, writer: XmlWriter) """
        ...


class SyndicationCategory(IExtensibleSyndicationObject): # skipped bases: <type 'object'>
    """
    SyndicationCategory()
    SyndicationCategory(name: str)
    SyndicationCategory(name: str, scheme: str, label: str)
    """
    @property
    def AttributeExtensions(self) -> Dictionary:
        """ Get: AttributeExtensions(self: SyndicationCategory) -> Dictionary[XmlQualifiedName, str] """
        ...

    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection:
        """ Get: ElementExtensions(self: SyndicationCategory) -> SyndicationElementExtensionCollection """
        ...

    @property
    def Label(self) -> str:
        """
        Get: Label(self: SyndicationCategory) -> str
        Set: Label(self: SyndicationCategory) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SyndicationCategory) -> str
        Set: Name(self: SyndicationCategory) = value
        """
        ...

    @property
    def Scheme(self) -> str:
        """
        Get: Scheme(self: SyndicationCategory) -> str
        Set: Scheme(self: SyndicationCategory) = value
        """
        ...


    def Clone(self) -> SyndicationCategory:
        """ Clone(self: SyndicationCategory) -> SyndicationCategory """
        ...

    def TryParseAttribute(self, *args): #cannot find CLR method
        """ TryParseAttribute(self: SyndicationCategory, name: str, ns: str, value: str, version: str) -> bool """
        ...

    def TryParseElement(self, *args): #cannot find CLR method
        """ TryParseElement(self: SyndicationCategory, reader: XmlReader, version: str) -> bool """
        ...

    def WriteAttributeExtensions(self, *args): #cannot find CLR method
        """ WriteAttributeExtensions(self: SyndicationCategory, writer: XmlWriter, version: str) """
        ...

    def WriteElementExtensions(self, *args): #cannot find CLR method
        """ WriteElementExtensions(self: SyndicationCategory, writer: XmlWriter, version: str) """
        ...


class SyndicationContent: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AttributeExtensions(self) -> Dictionary:
        """ Get: AttributeExtensions(self: SyndicationContent) -> Dictionary[XmlQualifiedName, str] """
        ...

    @property
    def Type(self) -> str:
        """ Get: Type(self: SyndicationContent) -> str """
        ...


    def Clone(self) -> SyndicationContent:
        """ Clone(self: SyndicationContent) -> SyndicationContent """
        ...

    @staticmethod
    def CreateHtmlContent(content:str) -> TextSyndicationContent:
        """ CreateHtmlContent(content: str) -> TextSyndicationContent """
        ...

    @staticmethod
    def CreatePlaintextContent(content:str) -> TextSyndicationContent:
        """ CreatePlaintextContent(content: str) -> TextSyndicationContent """
        ...

    @staticmethod
    def CreateUrlContent(url:Uri, mediaType:str) -> UrlSyndicationContent:
        """ CreateUrlContent(url: Uri, mediaType: str) -> UrlSyndicationContent """
        ...

    @staticmethod
    def CreateXhtmlContent(content:str) -> TextSyndicationContent:
        """ CreateXhtmlContent(content: str) -> TextSyndicationContent """
        ...

    @staticmethod
    def CreateXmlContent(*__args:XmlReader) -> XmlSyndicationContent:
        """
        CreateXmlContent(xmlReader: XmlReader) -> XmlSyndicationContent
        CreateXmlContent(dataContractObject: object) -> XmlSyndicationContent
        CreateXmlContent(dataContractObject: object, dataContractSerializer: XmlObjectSerializer) -> XmlSyndicationContent
        CreateXmlContent(xmlSerializerObject: object, serializer: XmlSerializer) -> XmlSyndicationContent
        """
        ...

    def WriteContentsTo(self, *args): #cannot find CLR method
        """ WriteContentsTo(self: SyndicationContent, writer: XmlWriter) """
        ...

    def WriteTo(self, writer:XmlWriter, outerElementName:str, outerElementNamespace:str): # -> 
        """ WriteTo(self: SyndicationContent, writer: XmlWriter, outerElementName: str, outerElementNamespace: str) """
        ...


class SyndicationElementExtension: # skipped bases: <type 'object'>, <type 'object'>
    """
    SyndicationElementExtension(xmlReader: XmlReader)
    SyndicationElementExtension(dataContractExtension: object)
    SyndicationElementExtension(dataContractExtension: object, dataContractSerializer: XmlObjectSerializer)
    SyndicationElementExtension(outerName: str, outerNamespace: str, dataContractExtension: object)
    SyndicationElementExtension(outerName: str, outerNamespace: str, dataContractExtension: object, dataContractSerializer: XmlObjectSerializer)
    SyndicationElementExtension(xmlSerializerExtension: object, serializer: XmlSerializer)
    """
    @property
    def OuterName(self) -> str:
        """ Get: OuterName(self: SyndicationElementExtension) -> str """
        ...

    @property
    def OuterNamespace(self) -> str:
        """ Get: OuterNamespace(self: SyndicationElementExtension) -> str """
        ...


    def GetObject(self, serializer = ...): # -> TExtension # Not found arg types: {'serializer': 'XmlObjectSerializer'}
        """
        GetObject[TExtension](self: SyndicationElementExtension) -> TExtension
        GetObject[TExtension](self: SyndicationElementExtension, serializer: XmlObjectSerializer) -> TExtension
        GetObject[TExtension](self: SyndicationElementExtension, serializer: XmlSerializer) -> TExtension
        """
        ...

    def GetReader(self) -> XmlReader:
        """ GetReader(self: SyndicationElementExtension) -> XmlReader """
        ...

    def WriteTo(self, writer:XmlWriter): # -> 
        """ WriteTo(self: SyndicationElementExtension, writer: XmlWriter) """
        ...


class SyndicationElementExtensionCollection(Collection): # skipped bases: <type 'IReadOnlyList[SyndicationElementExtension]'>, <type 'IEnumerable'>, <type 'IList[SyndicationElementExtension]'>, <type 'IList'>, <type 'IReadOnlyCollection[SyndicationElementExtension]'>, <type 'ICollection[SyndicationElementExtension]'>, <type 'ICollection'>, <type 'IEnumerable[SyndicationElementExtension]'>, <type 'object'>
    """ no doc """
    def GetReaderAtElementExtensions(self) -> XmlReader:
        """ GetReaderAtElementExtensions(self: SyndicationElementExtensionCollection) -> XmlReader """
        ...

    def ReadElementExtensions(self, extensionName:str, extensionNamespace:str, serializer = ...) -> Collection: # Not found arg types: {'serializer': 'XmlObjectSerializer'}
        """
        ReadElementExtensions[TExtension](self: SyndicationElementExtensionCollection, extensionName: str, extensionNamespace: str) -> Collection[TExtension]
        ReadElementExtensions[TExtension](self: SyndicationElementExtensionCollection, extensionName: str, extensionNamespace: str, serializer: XmlObjectSerializer) -> Collection[TExtension]
        ReadElementExtensions[TExtension](self: SyndicationElementExtensionCollection, extensionName: str, extensionNamespace: str, serializer: XmlSerializer) -> Collection[TExtension]
        """
        ...


class SyndicationFeed(IExtensibleSyndicationObject): # skipped bases: <type 'object'>
    """
    SyndicationFeed()
    SyndicationFeed(items: IEnumerable[SyndicationItem])
    SyndicationFeed(title: str, description: str, feedAlternateLink: Uri)
    SyndicationFeed(title: str, description: str, feedAlternateLink: Uri, items: IEnumerable[SyndicationItem])
    SyndicationFeed(title: str, description: str, feedAlternateLink: Uri, id: str, lastUpdatedTime: DateTimeOffset)
    SyndicationFeed(title: str, description: str, feedAlternateLink: Uri, id: str, lastUpdatedTime: DateTimeOffset, items: IEnumerable[SyndicationItem])
    """
    @property
    def AttributeExtensions(self) -> Dictionary:
        """ Get: AttributeExtensions(self: SyndicationFeed) -> Dictionary[XmlQualifiedName, str] """
        ...

    @property
    def Authors(self) -> Collection:
        """ Get: Authors(self: SyndicationFeed) -> Collection[SyndicationPerson] """
        ...

    @property
    def BaseUri(self) -> Uri:
        """
        Get: BaseUri(self: SyndicationFeed) -> Uri
        Set: BaseUri(self: SyndicationFeed) = value
        """
        ...

    @property
    def Categories(self) -> Collection:
        """ Get: Categories(self: SyndicationFeed) -> Collection[SyndicationCategory] """
        ...

    @property
    def Contributors(self) -> Collection:
        """ Get: Contributors(self: SyndicationFeed) -> Collection[SyndicationPerson] """
        ...

    @property
    def Copyright(self) -> TextSyndicationContent:
        """
        Get: Copyright(self: SyndicationFeed) -> TextSyndicationContent
        Set: Copyright(self: SyndicationFeed) = value
        """
        ...

    @property
    def Description(self) -> TextSyndicationContent:
        """
        Get: Description(self: SyndicationFeed) -> TextSyndicationContent
        Set: Description(self: SyndicationFeed) = value
        """
        ...

    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection:
        """ Get: ElementExtensions(self: SyndicationFeed) -> SyndicationElementExtensionCollection """
        ...

    @property
    def Generator(self) -> str:
        """
        Get: Generator(self: SyndicationFeed) -> str
        Set: Generator(self: SyndicationFeed) = value
        """
        ...

    @property
    def Id(self) -> str:
        """
        Get: Id(self: SyndicationFeed) -> str
        Set: Id(self: SyndicationFeed) = value
        """
        ...

    @property
    def ImageUrl(self) -> Uri:
        """
        Get: ImageUrl(self: SyndicationFeed) -> Uri
        Set: ImageUrl(self: SyndicationFeed) = value
        """
        ...

    @property
    def Items(self) -> IEnumerable:
        """
        Get: Items(self: SyndicationFeed) -> IEnumerable[SyndicationItem]
        Set: Items(self: SyndicationFeed) = value
        """
        ...

    @property
    def Language(self) -> str:
        """
        Get: Language(self: SyndicationFeed) -> str
        Set: Language(self: SyndicationFeed) = value
        """
        ...

    @property
    def LastUpdatedTime(self) -> DateTimeOffset:
        """
        Get: LastUpdatedTime(self: SyndicationFeed) -> DateTimeOffset
        Set: LastUpdatedTime(self: SyndicationFeed) = value
        """
        ...

    @property
    def Links(self) -> Collection:
        """ Get: Links(self: SyndicationFeed) -> Collection[SyndicationLink] """
        ...

    @property
    def Title(self) -> TextSyndicationContent:
        """
        Get: Title(self: SyndicationFeed) -> TextSyndicationContent
        Set: Title(self: SyndicationFeed) = value
        """
        ...


    def Clone(self, cloneItems:bool) -> SyndicationFeed:
        """ Clone(self: SyndicationFeed, cloneItems: bool) -> SyndicationFeed """
        ...

    def CreateCategory(self, *args): #cannot find CLR method
        """ CreateCategory(self: SyndicationFeed) -> SyndicationCategory """
        ...

    def CreateItem(self, *args): #cannot find CLR method
        """ CreateItem(self: SyndicationFeed) -> SyndicationItem """
        ...

    def CreateLink(self, *args): #cannot find CLR method
        """ CreateLink(self: SyndicationFeed) -> SyndicationLink """
        ...

    def CreatePerson(self, *args): #cannot find CLR method
        """ CreatePerson(self: SyndicationFeed) -> SyndicationPerson """
        ...

    def GetAtom10Formatter(self) -> Atom10FeedFormatter:
        """ GetAtom10Formatter(self: SyndicationFeed) -> Atom10FeedFormatter """
        ...

    def GetRss20Formatter(self, serializeExtensionsAsAtom:bool = ...) -> Rss20FeedFormatter:
        """
        GetRss20Formatter(self: SyndicationFeed) -> Rss20FeedFormatter
        GetRss20Formatter(self: SyndicationFeed, serializeExtensionsAsAtom: bool) -> Rss20FeedFormatter
        """
        ...

    @staticmethod
    def Load(reader):
        """ no doc """
        ...

    def SaveAsAtom10(self, writer:XmlWriter): # -> 
        """ SaveAsAtom10(self: SyndicationFeed, writer: XmlWriter) """
        ...

    def SaveAsRss20(self, writer:XmlWriter): # -> 
        """ SaveAsRss20(self: SyndicationFeed, writer: XmlWriter) """
        ...

    def TryParseAttribute(self, *args): #cannot find CLR method
        """ TryParseAttribute(self: SyndicationFeed, name: str, ns: str, value: str, version: str) -> bool """
        ...

    def TryParseElement(self, *args): #cannot find CLR method
        """ TryParseElement(self: SyndicationFeed, reader: XmlReader, version: str) -> bool """
        ...

    def WriteAttributeExtensions(self, *args): #cannot find CLR method
        """ WriteAttributeExtensions(self: SyndicationFeed, writer: XmlWriter, version: str) """
        ...

    def WriteElementExtensions(self, *args): #cannot find CLR method
        """ WriteElementExtensions(self: SyndicationFeed, writer: XmlWriter, version: str) """
        ...


class SyndicationFeedFormatter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Feed(self) -> SyndicationFeed:
        """ Get: Feed(self: SyndicationFeedFormatter) -> SyndicationFeed """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: SyndicationFeedFormatter) -> str """
        ...


    def CanRead(self, reader:XmlReader) -> bool:
        """ CanRead(self: SyndicationFeedFormatter, reader: XmlReader) -> bool """
        ...

    def CreateCategory(self, *args): #cannot find CLR method
        """
        CreateCategory(feed: SyndicationFeed) -> SyndicationCategory
        CreateCategory(item: SyndicationItem) -> SyndicationCategory
        """
        ...

    def CreateFeedInstance(self, *args): #cannot find CLR method
        """ CreateFeedInstance(self: SyndicationFeedFormatter) -> SyndicationFeed """
        ...

    def CreateItem(self, *args): #cannot find CLR method
        """ CreateItem(feed: SyndicationFeed) -> SyndicationItem """
        ...

    def CreateLink(self, *args): #cannot find CLR method
        """
        CreateLink(feed: SyndicationFeed) -> SyndicationLink
        CreateLink(item: SyndicationItem) -> SyndicationLink
        """
        ...

    def CreatePerson(self, *args): #cannot find CLR method
        """
        CreatePerson(feed: SyndicationFeed) -> SyndicationPerson
        CreatePerson(item: SyndicationItem) -> SyndicationPerson
        """
        ...

    def LoadElementExtensions(self, *args): #cannot find CLR method
        """ LoadElementExtensions(reader: XmlReader, feed: SyndicationFeed, maxExtensionSize: int)LoadElementExtensions(reader: XmlReader, item: SyndicationItem, maxExtensionSize: int)LoadElementExtensions(reader: XmlReader, category: SyndicationCategory, maxExtensionSize: int)LoadElementExtensions(reader: XmlReader, link: SyndicationLink, maxExtensionSize: int)LoadElementExtensions(reader: XmlReader, person: SyndicationPerson, maxExtensionSize: int) """
        ...

    def ReadFrom(self, reader:XmlReader): # -> 
        """ ReadFrom(self: SyndicationFeedFormatter, reader: XmlReader) """
        ...

    def SetFeed(self, *args): #cannot find CLR method
        """ SetFeed(self: SyndicationFeedFormatter, feed: SyndicationFeed) """
        ...

    def ToString(self) -> str:
        """ ToString(self: SyndicationFeedFormatter) -> str """
        ...

    def TryParseAttribute(self, *args): #cannot find CLR method
        """
        TryParseAttribute(name: str, ns: str, value: str, feed: SyndicationFeed, version: str) -> bool
        TryParseAttribute(name: str, ns: str, value: str, item: SyndicationItem, version: str) -> bool
        TryParseAttribute(name: str, ns: str, value: str, category: SyndicationCategory, version: str) -> bool
        TryParseAttribute(name: str, ns: str, value: str, link: SyndicationLink, version: str) -> bool
        TryParseAttribute(name: str, ns: str, value: str, person: SyndicationPerson, version: str) -> bool
        """
        ...

    def TryParseContent(self, *args): #cannot find CLR method
        """ TryParseContent(reader: XmlReader, item: SyndicationItem, contentType: str, version: str) -> (bool, SyndicationContent) """
        ...

    def TryParseElement(self, *args): #cannot find CLR method
        """
        TryParseElement(reader: XmlReader, feed: SyndicationFeed, version: str) -> bool
        TryParseElement(reader: XmlReader, item: SyndicationItem, version: str) -> bool
        TryParseElement(reader: XmlReader, category: SyndicationCategory, version: str) -> bool
        TryParseElement(reader: XmlReader, link: SyndicationLink, version: str) -> bool
        TryParseElement(reader: XmlReader, person: SyndicationPerson, version: str) -> bool
        """
        ...

    def WriteAttributeExtensions(self, *args): #cannot find CLR method
        """ WriteAttributeExtensions(writer: XmlWriter, feed: SyndicationFeed, version: str)WriteAttributeExtensions(writer: XmlWriter, item: SyndicationItem, version: str)WriteAttributeExtensions(writer: XmlWriter, category: SyndicationCategory, version: str)WriteAttributeExtensions(writer: XmlWriter, link: SyndicationLink, version: str)WriteAttributeExtensions(writer: XmlWriter, person: SyndicationPerson, version: str) """
        ...

    def WriteElementExtensions(self, *args): #cannot find CLR method
        """ WriteElementExtensions(writer: XmlWriter, feed: SyndicationFeed, version: str)WriteElementExtensions(writer: XmlWriter, item: SyndicationItem, version: str)WriteElementExtensions(writer: XmlWriter, category: SyndicationCategory, version: str)WriteElementExtensions(writer: XmlWriter, link: SyndicationLink, version: str)WriteElementExtensions(writer: XmlWriter, person: SyndicationPerson, version: str) """
        ...

    def WriteTo(self, writer:XmlWriter): # -> 
        """ WriteTo(self: SyndicationFeedFormatter, writer: XmlWriter) """
        ...


class SyndicationItem(IExtensibleSyndicationObject): # skipped bases: <type 'object'>
    """
    SyndicationItem()
    SyndicationItem(title: str, content: str, itemAlternateLink: Uri)
    SyndicationItem(title: str, content: str, itemAlternateLink: Uri, id: str, lastUpdatedTime: DateTimeOffset)
    SyndicationItem(title: str, content: SyndicationContent, itemAlternateLink: Uri, id: str, lastUpdatedTime: DateTimeOffset)
    """
    @property
    def AttributeExtensions(self) -> Dictionary:
        """ Get: AttributeExtensions(self: SyndicationItem) -> Dictionary[XmlQualifiedName, str] """
        ...

    @property
    def Authors(self) -> Collection:
        """ Get: Authors(self: SyndicationItem) -> Collection[SyndicationPerson] """
        ...

    @property
    def BaseUri(self) -> Uri:
        """
        Get: BaseUri(self: SyndicationItem) -> Uri
        Set: BaseUri(self: SyndicationItem) = value
        """
        ...

    @property
    def Categories(self) -> Collection:
        """ Get: Categories(self: SyndicationItem) -> Collection[SyndicationCategory] """
        ...

    @property
    def Content(self) -> SyndicationContent:
        """
        Get: Content(self: SyndicationItem) -> SyndicationContent
        Set: Content(self: SyndicationItem) = value
        """
        ...

    @property
    def Contributors(self) -> Collection:
        """ Get: Contributors(self: SyndicationItem) -> Collection[SyndicationPerson] """
        ...

    @property
    def Copyright(self) -> TextSyndicationContent:
        """
        Get: Copyright(self: SyndicationItem) -> TextSyndicationContent
        Set: Copyright(self: SyndicationItem) = value
        """
        ...

    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection:
        """ Get: ElementExtensions(self: SyndicationItem) -> SyndicationElementExtensionCollection """
        ...

    @property
    def Id(self) -> str:
        """
        Get: Id(self: SyndicationItem) -> str
        Set: Id(self: SyndicationItem) = value
        """
        ...

    @property
    def LastUpdatedTime(self) -> DateTimeOffset:
        """
        Get: LastUpdatedTime(self: SyndicationItem) -> DateTimeOffset
        Set: LastUpdatedTime(self: SyndicationItem) = value
        """
        ...

    @property
    def Links(self) -> Collection:
        """ Get: Links(self: SyndicationItem) -> Collection[SyndicationLink] """
        ...

    @property
    def PublishDate(self) -> DateTimeOffset:
        """
        Get: PublishDate(self: SyndicationItem) -> DateTimeOffset
        Set: PublishDate(self: SyndicationItem) = value
        """
        ...

    @property
    def SourceFeed(self) -> SyndicationFeed:
        """
        Get: SourceFeed(self: SyndicationItem) -> SyndicationFeed
        Set: SourceFeed(self: SyndicationItem) = value
        """
        ...

    @property
    def Summary(self) -> TextSyndicationContent:
        """
        Get: Summary(self: SyndicationItem) -> TextSyndicationContent
        Set: Summary(self: SyndicationItem) = value
        """
        ...

    @property
    def Title(self) -> TextSyndicationContent:
        """
        Get: Title(self: SyndicationItem) -> TextSyndicationContent
        Set: Title(self: SyndicationItem) = value
        """
        ...


    def AddPermalink(self, permalink:Uri): # -> 
        """ AddPermalink(self: SyndicationItem, permalink: Uri) """
        ...

    def Clone(self) -> SyndicationItem:
        """ Clone(self: SyndicationItem) -> SyndicationItem """
        ...

    def CreateCategory(self, *args): #cannot find CLR method
        """ CreateCategory(self: SyndicationItem) -> SyndicationCategory """
        ...

    def CreateLink(self, *args): #cannot find CLR method
        """ CreateLink(self: SyndicationItem) -> SyndicationLink """
        ...

    def CreatePerson(self, *args): #cannot find CLR method
        """ CreatePerson(self: SyndicationItem) -> SyndicationPerson """
        ...

    def GetAtom10Formatter(self) -> Atom10ItemFormatter:
        """ GetAtom10Formatter(self: SyndicationItem) -> Atom10ItemFormatter """
        ...

    def GetRss20Formatter(self, serializeExtensionsAsAtom:bool = ...) -> Rss20ItemFormatter:
        """
        GetRss20Formatter(self: SyndicationItem) -> Rss20ItemFormatter
        GetRss20Formatter(self: SyndicationItem, serializeExtensionsAsAtom: bool) -> Rss20ItemFormatter
        """
        ...

    @staticmethod
    def Load(reader):
        """ no doc """
        ...

    def SaveAsAtom10(self, writer:XmlWriter): # -> 
        """ SaveAsAtom10(self: SyndicationItem, writer: XmlWriter) """
        ...

    def SaveAsRss20(self, writer:XmlWriter): # -> 
        """ SaveAsRss20(self: SyndicationItem, writer: XmlWriter) """
        ...

    def TryParseAttribute(self, *args): #cannot find CLR method
        """ TryParseAttribute(self: SyndicationItem, name: str, ns: str, value: str, version: str) -> bool """
        ...

    def TryParseContent(self, *args): #cannot find CLR method
        """ TryParseContent(self: SyndicationItem, reader: XmlReader, contentType: str, version: str) -> (bool, SyndicationContent) """
        ...

    def TryParseElement(self, *args): #cannot find CLR method
        """ TryParseElement(self: SyndicationItem, reader: XmlReader, version: str) -> bool """
        ...

    def WriteAttributeExtensions(self, *args): #cannot find CLR method
        """ WriteAttributeExtensions(self: SyndicationItem, writer: XmlWriter, version: str) """
        ...

    def WriteElementExtensions(self, *args): #cannot find CLR method
        """ WriteElementExtensions(self: SyndicationItem, writer: XmlWriter, version: str) """
        ...


class SyndicationItemFormatter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Item(self) -> SyndicationItem:
        """ Get: Item(self: SyndicationItemFormatter) -> SyndicationItem """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: SyndicationItemFormatter) -> str """
        ...


    def CanRead(self, reader:XmlReader) -> bool:
        """ CanRead(self: SyndicationItemFormatter, reader: XmlReader) -> bool """
        ...

    def CreateCategory(self, *args): #cannot find CLR method
        """ CreateCategory(item: SyndicationItem) -> SyndicationCategory """
        ...

    def CreateItemInstance(self, *args): #cannot find CLR method
        """ CreateItemInstance(self: SyndicationItemFormatter) -> SyndicationItem """
        ...

    def CreateLink(self, *args): #cannot find CLR method
        """ CreateLink(item: SyndicationItem) -> SyndicationLink """
        ...

    def CreatePerson(self, *args): #cannot find CLR method
        """ CreatePerson(item: SyndicationItem) -> SyndicationPerson """
        ...

    def LoadElementExtensions(self, *args): #cannot find CLR method
        """ LoadElementExtensions(reader: XmlReader, item: SyndicationItem, maxExtensionSize: int)LoadElementExtensions(reader: XmlReader, category: SyndicationCategory, maxExtensionSize: int)LoadElementExtensions(reader: XmlReader, link: SyndicationLink, maxExtensionSize: int)LoadElementExtensions(reader: XmlReader, person: SyndicationPerson, maxExtensionSize: int) """
        ...

    def ReadFrom(self, reader:XmlReader): # -> 
        """ ReadFrom(self: SyndicationItemFormatter, reader: XmlReader) """
        ...

    def SetItem(self, *args): #cannot find CLR method
        """ SetItem(self: SyndicationItemFormatter, item: SyndicationItem) """
        ...

    def ToString(self) -> str:
        """ ToString(self: SyndicationItemFormatter) -> str """
        ...

    def TryParseAttribute(self, *args): #cannot find CLR method
        """
        TryParseAttribute(name: str, ns: str, value: str, item: SyndicationItem, version: str) -> bool
        TryParseAttribute(name: str, ns: str, value: str, category: SyndicationCategory, version: str) -> bool
        TryParseAttribute(name: str, ns: str, value: str, link: SyndicationLink, version: str) -> bool
        TryParseAttribute(name: str, ns: str, value: str, person: SyndicationPerson, version: str) -> bool
        """
        ...

    def TryParseContent(self, *args): #cannot find CLR method
        """ TryParseContent(reader: XmlReader, item: SyndicationItem, contentType: str, version: str) -> (bool, SyndicationContent) """
        ...

    def TryParseElement(self, *args): #cannot find CLR method
        """
        TryParseElement(reader: XmlReader, item: SyndicationItem, version: str) -> bool
        TryParseElement(reader: XmlReader, category: SyndicationCategory, version: str) -> bool
        TryParseElement(reader: XmlReader, link: SyndicationLink, version: str) -> bool
        TryParseElement(reader: XmlReader, person: SyndicationPerson, version: str) -> bool
        """
        ...

    def WriteAttributeExtensions(self, *args): #cannot find CLR method
        """ WriteAttributeExtensions(writer: XmlWriter, item: SyndicationItem, version: str)WriteAttributeExtensions(writer: XmlWriter, category: SyndicationCategory, version: str)WriteAttributeExtensions(writer: XmlWriter, link: SyndicationLink, version: str)WriteAttributeExtensions(writer: XmlWriter, person: SyndicationPerson, version: str) """
        ...

    def WriteElementExtensions(self, *args): #cannot find CLR method
        """ WriteElementExtensions(writer: XmlWriter, item: SyndicationItem, version: str)WriteElementExtensions(self: SyndicationItemFormatter, writer: XmlWriter, category: SyndicationCategory, version: str)WriteElementExtensions(self: SyndicationItemFormatter, writer: XmlWriter, link: SyndicationLink, version: str)WriteElementExtensions(self: SyndicationItemFormatter, writer: XmlWriter, person: SyndicationPerson, version: str) """
        ...

    def WriteTo(self, writer:XmlWriter): # -> 
        """ WriteTo(self: SyndicationItemFormatter, writer: XmlWriter) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class SyndicationLink(IExtensibleSyndicationObject): # skipped bases: <type 'object'>
    """
    SyndicationLink(uri: Uri)
    SyndicationLink(uri: Uri, relationshipType: str, title: str, mediaType: str, length: Int64)
    SyndicationLink()
    """
    @property
    def AttributeExtensions(self) -> Dictionary:
        """ Get: AttributeExtensions(self: SyndicationLink) -> Dictionary[XmlQualifiedName, str] """
        ...

    @property
    def BaseUri(self) -> Uri:
        """
        Get: BaseUri(self: SyndicationLink) -> Uri
        Set: BaseUri(self: SyndicationLink) = value
        """
        ...

    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection:
        """ Get: ElementExtensions(self: SyndicationLink) -> SyndicationElementExtensionCollection """
        ...

    @property
    def Length(self) -> Int64:
        """
        Get: Length(self: SyndicationLink) -> Int64
        Set: Length(self: SyndicationLink) = value
        """
        ...

    @property
    def MediaType(self) -> str:
        """
        Get: MediaType(self: SyndicationLink) -> str
        Set: MediaType(self: SyndicationLink) = value
        """
        ...

    @property
    def RelationshipType(self) -> str:
        """
        Get: RelationshipType(self: SyndicationLink) -> str
        Set: RelationshipType(self: SyndicationLink) = value
        """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: SyndicationLink) -> str
        Set: Title(self: SyndicationLink) = value
        """
        ...

    @property
    def Uri(self) -> Uri:
        """
        Get: Uri(self: SyndicationLink) -> Uri
        Set: Uri(self: SyndicationLink) = value
        """
        ...


    def Clone(self) -> SyndicationLink:
        """ Clone(self: SyndicationLink) -> SyndicationLink """
        ...

    @staticmethod
    def CreateAlternateLink(uri:Uri, mediaType:str = ...) -> SyndicationLink:
        """
        CreateAlternateLink(uri: Uri) -> SyndicationLink
        CreateAlternateLink(uri: Uri, mediaType: str) -> SyndicationLink
        """
        ...

    @staticmethod
    def CreateMediaEnclosureLink(uri:Uri, mediaType:str, length:Int64) -> SyndicationLink:
        """ CreateMediaEnclosureLink(uri: Uri, mediaType: str, length: Int64) -> SyndicationLink """
        ...

    @staticmethod
    def CreateSelfLink(uri:Uri, mediaType:str = ...) -> SyndicationLink:
        """
        CreateSelfLink(uri: Uri) -> SyndicationLink
        CreateSelfLink(uri: Uri, mediaType: str) -> SyndicationLink
        """
        ...

    def GetAbsoluteUri(self) -> Uri:
        """ GetAbsoluteUri(self: SyndicationLink) -> Uri """
        ...

    def TryParseAttribute(self, *args): #cannot find CLR method
        """ TryParseAttribute(self: SyndicationLink, name: str, ns: str, value: str, version: str) -> bool """
        ...

    def TryParseElement(self, *args): #cannot find CLR method
        """ TryParseElement(self: SyndicationLink, reader: XmlReader, version: str) -> bool """
        ...

    def WriteAttributeExtensions(self, *args): #cannot find CLR method
        """ WriteAttributeExtensions(self: SyndicationLink, writer: XmlWriter, version: str) """
        ...

    def WriteElementExtensions(self, *args): #cannot find CLR method
        """ WriteElementExtensions(self: SyndicationLink, writer: XmlWriter, version: str) """
        ...


class SyndicationPerson(IExtensibleSyndicationObject): # skipped bases: <type 'object'>
    """
    SyndicationPerson()
    SyndicationPerson(email: str)
    SyndicationPerson(email: str, name: str, uri: str)
    """
    @property
    def AttributeExtensions(self) -> Dictionary:
        """ Get: AttributeExtensions(self: SyndicationPerson) -> Dictionary[XmlQualifiedName, str] """
        ...

    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection:
        """ Get: ElementExtensions(self: SyndicationPerson) -> SyndicationElementExtensionCollection """
        ...

    @property
    def Email(self) -> str:
        """
        Get: Email(self: SyndicationPerson) -> str
        Set: Email(self: SyndicationPerson) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SyndicationPerson) -> str
        Set: Name(self: SyndicationPerson) = value
        """
        ...

    @property
    def Uri(self) -> str:
        """
        Get: Uri(self: SyndicationPerson) -> str
        Set: Uri(self: SyndicationPerson) = value
        """
        ...


    def Clone(self) -> SyndicationPerson:
        """ Clone(self: SyndicationPerson) -> SyndicationPerson """
        ...

    def TryParseAttribute(self, *args): #cannot find CLR method
        """ TryParseAttribute(self: SyndicationPerson, name: str, ns: str, value: str, version: str) -> bool """
        ...

    def TryParseElement(self, *args): #cannot find CLR method
        """ TryParseElement(self: SyndicationPerson, reader: XmlReader, version: str) -> bool """
        ...

    def WriteAttributeExtensions(self, *args): #cannot find CLR method
        """ WriteAttributeExtensions(self: SyndicationPerson, writer: XmlWriter, version: str) """
        ...

    def WriteElementExtensions(self, *args): #cannot find CLR method
        """ WriteElementExtensions(self: SyndicationPerson, writer: XmlWriter, version: str) """
        ...


class SyndicationVersions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Atom10: str = ...
    Rss20: str = ...
    __all__: list = ...


class TextSyndicationContent(SyndicationContent): # skipped bases: <type 'object'>
    """
    TextSyndicationContent(text: str)
    TextSyndicationContent(text: str, textKind: TextSyndicationContentKind)
    """
    @property
    def Text(self) -> str:
        """ Get: Text(self: TextSyndicationContent) -> str """
        ...



class TextSyndicationContentKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TextSyndicationContentKind, values: Html (1), Plaintext (0), XHtml (2) """
    Html: TextSyndicationContentKind = ...
    Plaintext: TextSyndicationContentKind = ...
    value__ = ...
    XHtml: TextSyndicationContentKind = ...


class UrlSyndicationContent(SyndicationContent): # skipped bases: <type 'object'>
    """ UrlSyndicationContent(url: Uri, mediaType: str) """
    @property
    def Url(self) -> Uri:
        """ Get: Url(self: UrlSyndicationContent) -> Uri """
        ...



class Workspace(IExtensibleSyndicationObject): # skipped bases: <type 'object'>
    """
    Workspace()
    Workspace(title: str, collections: IEnumerable[ResourceCollectionInfo])
    Workspace(title: TextSyndicationContent, collections: IEnumerable[ResourceCollectionInfo])
    """
    @property
    def AttributeExtensions(self) -> Dictionary:
        """ Get: AttributeExtensions(self: Workspace) -> Dictionary[XmlQualifiedName, str] """
        ...

    @property
    def BaseUri(self) -> Uri:
        """
        Get: BaseUri(self: Workspace) -> Uri
        Set: BaseUri(self: Workspace) = value
        """
        ...

    @property
    def Collections(self) -> Collection:
        """ Get: Collections(self: Workspace) -> Collection[ResourceCollectionInfo] """
        ...

    @property
    def ElementExtensions(self) -> SyndicationElementExtensionCollection:
        """ Get: ElementExtensions(self: Workspace) -> SyndicationElementExtensionCollection """
        ...

    @property
    def Title(self) -> TextSyndicationContent:
        """
        Get: Title(self: Workspace) -> TextSyndicationContent
        Set: Title(self: Workspace) = value
        """
        ...


    def CreateResourceCollection(self, *args): #cannot find CLR method
        """ CreateResourceCollection(self: Workspace) -> ResourceCollectionInfo """
        ...

    def TryParseAttribute(self, *args): #cannot find CLR method
        """ TryParseAttribute(self: Workspace, name: str, ns: str, value: str, version: str) -> bool """
        ...

    def TryParseElement(self, *args): #cannot find CLR method
        """ TryParseElement(self: Workspace, reader: XmlReader, version: str) -> bool """
        ...

    def WriteAttributeExtensions(self, *args): #cannot find CLR method
        """ WriteAttributeExtensions(self: Workspace, writer: XmlWriter, version: str) """
        ...

    def WriteElementExtensions(self, *args): #cannot find CLR method
        """ WriteElementExtensions(self: Workspace, writer: XmlWriter, version: str) """
        ...


class XmlSyndicationContent(SyndicationContent): # skipped bases: <type 'object'>
    """
    XmlSyndicationContent(reader: XmlReader)
    XmlSyndicationContent(type: str, dataContractExtension: object, dataContractSerializer: XmlObjectSerializer)
    XmlSyndicationContent(type: str, xmlSerializerExtension: object, serializer: XmlSerializer)
    XmlSyndicationContent(type: str, extension: SyndicationElementExtension)
    """
    @property
    def Extension(self) -> SyndicationElementExtension:
        """ Get: Extension(self: XmlSyndicationContent) -> SyndicationElementExtension """
        ...


    def GetReaderAtContent(self) -> XmlDictionaryReader:
        """ GetReaderAtContent(self: XmlSyndicationContent) -> XmlDictionaryReader """
        ...

    def ReadContent(self, *__args): # -> TContent # Not found arg types: {'*__args': 'XmlObjectSerializer'}
        """
        ReadContent[TContent](self: XmlSyndicationContent) -> TContent
        ReadContent[TContent](self: XmlSyndicationContent, dataContractSerializer: XmlObjectSerializer) -> TContent
        ReadContent[TContent](self: XmlSyndicationContent, serializer: XmlSerializer) -> TContent
        """
        ...


