# encoding: utf-8
# module System.Xml.Linq calls itself Linq
# from System.Xml.Linq, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, EventArgs, IEquatable, Type

from System.Collections import IComparer, IEnumerable, IEqualityComparer

from System.Runtime.Serialization import ISerializable

from System.Xml import IXmlLineInfo, XmlNodeType, XmlReader, XmlWriter

from System.Xml.Serialization import IXmlSerializable

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class Extensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Ancestors(source:IEnumerable, name:XName = ...) -> IEnumerable:
        """
        Ancestors[T](source: IEnumerable[T]) -> IEnumerable[XElement]
        Ancestors[T](source: IEnumerable[T], name: XName) -> IEnumerable[XElement]
        """
        ...

    @staticmethod
    def AncestorsAndSelf(source:IEnumerable, name:XName = ...) -> IEnumerable:
        """
        AncestorsAndSelf(source: IEnumerable[XElement]) -> IEnumerable[XElement]
        AncestorsAndSelf(source: IEnumerable[XElement], name: XName) -> IEnumerable[XElement]
        """
        ...

    @staticmethod
    def Attributes(source:IEnumerable, name:XName = ...) -> IEnumerable:
        """
        Attributes(source: IEnumerable[XElement]) -> IEnumerable[XAttribute]
        Attributes(source: IEnumerable[XElement], name: XName) -> IEnumerable[XAttribute]
        """
        ...

    @staticmethod
    def DescendantNodes(source:IEnumerable) -> IEnumerable:
        """ DescendantNodes[T](source: IEnumerable[T]) -> IEnumerable[XNode] """
        ...

    @staticmethod
    def DescendantNodesAndSelf(source:IEnumerable) -> IEnumerable:
        """ DescendantNodesAndSelf(source: IEnumerable[XElement]) -> IEnumerable[XNode] """
        ...

    @staticmethod
    def Descendants(source:IEnumerable, name:XName = ...) -> IEnumerable:
        """
        Descendants[T](source: IEnumerable[T]) -> IEnumerable[XElement]
        Descendants[T](source: IEnumerable[T], name: XName) -> IEnumerable[XElement]
        """
        ...

    @staticmethod
    def DescendantsAndSelf(source:IEnumerable, name:XName = ...) -> IEnumerable:
        """
        DescendantsAndSelf(source: IEnumerable[XElement]) -> IEnumerable[XElement]
        DescendantsAndSelf(source: IEnumerable[XElement], name: XName) -> IEnumerable[XElement]
        """
        ...

    @staticmethod
    def Elements(source:IEnumerable, name:XName = ...) -> IEnumerable:
        """
        Elements[T](source: IEnumerable[T]) -> IEnumerable[XElement]
        Elements[T](source: IEnumerable[T], name: XName) -> IEnumerable[XElement]
        """
        ...

    @staticmethod
    def InDocumentOrder(source:IEnumerable) -> IEnumerable:
        """ InDocumentOrder[T](source: IEnumerable[T]) -> IEnumerable[T] """
        ...

    @staticmethod
    def Nodes(source:IEnumerable) -> IEnumerable:
        """ Nodes[T](source: IEnumerable[T]) -> IEnumerable[XNode] """
        ...

    @staticmethod
    def Remove(source:IEnumerable): # -> 
        """ Remove(source: IEnumerable[XAttribute])Remove[T](source: IEnumerable[T]) """
        ...

    __all__: list = ...


class LoadOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) LoadOptions, values: None (0), PreserveWhitespace (1), SetBaseUri (2), SetLineInfo (4) """
    PreserveWhitespace: LoadOptions = ...
    SetBaseUri: LoadOptions = ...
    SetLineInfo: LoadOptions = ...
    value__ = ...


class ReaderOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ReaderOptions, values: None (0), OmitDuplicateNamespaces (1) """
    OmitDuplicateNamespaces: ReaderOptions = ...
    value__ = ...


class SaveOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SaveOptions, values: DisableFormatting (1), None (0), OmitDuplicateNamespaces (2) """
    DisableFormatting: SaveOptions = ...
    OmitDuplicateNamespaces: SaveOptions = ...
    value__ = ...


class XObject(IXmlLineInfo): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BaseUri(self) -> str:
        """ Get: BaseUri(self: XObject) -> str """
        ...

    @property
    def Document(self) -> XDocument:
        """ Get: Document(self: XObject) -> XDocument """
        ...

    @property
    def NodeType(self) -> XmlNodeType:
        """ Get: NodeType(self: XObject) -> XmlNodeType """
        ...

    @property
    def Parent(self) -> XElement:
        """ Get: Parent(self: XObject) -> XElement """
        ...


    def AddAnnotation(self, annotation:object): # -> 
        """ AddAnnotation(self: XObject, annotation: object) """
        ...

    def Annotation(self, type:Type = ...) -> object:
        """
        Annotation(self: XObject, type: Type) -> object
        Annotation[T](self: XObject) -> T
        """
        ...

    def Annotations(self, type:Type = ...) -> IEnumerable:
        """
        Annotations(self: XObject, type: Type) -> IEnumerable[object]
        Annotations[T](self: XObject) -> IEnumerable[T]
        """
        ...

    def RemoveAnnotations(self, type:Type = ...): # -> 
        """ RemoveAnnotations(self: XObject, type: Type)RemoveAnnotations[T](self: XObject) """
        ...

    Changed = ...
    Changing = ...


class XAttribute(XObject): # skipped bases: <type 'IXmlLineInfo'>, <type 'object'>
    """
    XAttribute(name: XName, value: object)
    XAttribute(other: XAttribute)
    """
    @property
    def EmptySequence(self) -> IEnumerable:
        """ Get: EmptySequence() -> IEnumerable[XAttribute] """
        ...

    @property
    def IsNamespaceDeclaration(self) -> bool:
        """ Get: IsNamespaceDeclaration(self: XAttribute) -> bool """
        ...

    @property
    def Name(self) -> XName:
        """ Get: Name(self: XAttribute) -> XName """
        ...

    @property
    def NextAttribute(self) -> XAttribute:
        """ Get: NextAttribute(self: XAttribute) -> XAttribute """
        ...

    @property
    def PreviousAttribute(self) -> XAttribute:
        """ Get: PreviousAttribute(self: XAttribute) -> XAttribute """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: XAttribute) -> str
        Set: Value(self: XAttribute) = value
        """
        ...


    def Remove(self): # -> 
        """ Remove(self: XAttribute) """
        ...

    def SetValue(self, value:object): # -> 
        """ SetValue(self: XAttribute, value: object) """
        ...

    def ToString(self) -> str:
        """ ToString(self: XAttribute) -> str """
        ...

    def __complex__(self, *args): #cannot find CLR method
        """ __complex__(attribute: XAttribute) -> float """
        ...

    def __float__(self, *args): #cannot find CLR method
        """ __complex__(attribute: XAttribute) -> float """
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(attribute: XAttribute) -> int """
        ...

    def __long__(self, *args): #cannot find CLR method
        """ __int__(attribute: XAttribute) -> int """
        ...

    def __new__(cls, *__args:XAttribute) -> Self:
        """
        __new__(cls: type, name: XName, value: object)
        __new__(cls: type, other: XAttribute)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...



class XNode(XObject): # skipped bases: <type 'IXmlLineInfo'>, <type 'object'>
    """ no doc """
    @property
    def DocumentOrderComparer(self) -> XNodeDocumentOrderComparer:
        """ Get: DocumentOrderComparer() -> XNodeDocumentOrderComparer """
        ...

    @property
    def EqualityComparer(self) -> XNodeEqualityComparer:
        """ Get: EqualityComparer() -> XNodeEqualityComparer """
        ...

    @property
    def NextNode(self) -> XNode:
        """ Get: NextNode(self: XNode) -> XNode """
        ...

    @property
    def PreviousNode(self) -> XNode:
        """ Get: PreviousNode(self: XNode) -> XNode """
        ...


    def AddAfterSelf(self, content:object): # -> 
        """ AddAfterSelf(self: XNode, content: object)AddAfterSelf(self: XNode, *content: Array[object]) """
        ...

    def AddBeforeSelf(self, content:object): # -> 
        """ AddBeforeSelf(self: XNode, content: object)AddBeforeSelf(self: XNode, *content: Array[object]) """
        ...

    def Ancestors(self, name:XName = ...) -> IEnumerable:
        """
        Ancestors(self: XNode) -> IEnumerable[XElement]
        Ancestors(self: XNode, name: XName) -> IEnumerable[XElement]
        """
        ...

    @staticmethod
    def CompareDocumentOrder(n1:XNode, n2:XNode) -> int:
        """ CompareDocumentOrder(n1: XNode, n2: XNode) -> int """
        ...

    def CreateReader(self, readerOptions:ReaderOptions = ...) -> XmlReader:
        """
        CreateReader(self: XNode) -> XmlReader
        CreateReader(self: XNode, readerOptions: ReaderOptions) -> XmlReader
        """
        ...

    @staticmethod
    def DeepEquals(n1:XNode, n2:XNode) -> bool:
        """ DeepEquals(n1: XNode, n2: XNode) -> bool """
        ...

    def ElementsAfterSelf(self, name:XName = ...) -> IEnumerable:
        """
        ElementsAfterSelf(self: XNode) -> IEnumerable[XElement]
        ElementsAfterSelf(self: XNode, name: XName) -> IEnumerable[XElement]
        """
        ...

    def ElementsBeforeSelf(self, name:XName = ...) -> IEnumerable:
        """
        ElementsBeforeSelf(self: XNode) -> IEnumerable[XElement]
        ElementsBeforeSelf(self: XNode, name: XName) -> IEnumerable[XElement]
        """
        ...

    def IsAfter(self, node:XNode) -> bool:
        """ IsAfter(self: XNode, node: XNode) -> bool """
        ...

    def IsBefore(self, node:XNode) -> bool:
        """ IsBefore(self: XNode, node: XNode) -> bool """
        ...

    def NodesAfterSelf(self) -> IEnumerable:
        """ NodesAfterSelf(self: XNode) -> IEnumerable[XNode] """
        ...

    def NodesBeforeSelf(self) -> IEnumerable:
        """ NodesBeforeSelf(self: XNode) -> IEnumerable[XNode] """
        ...

    @staticmethod
    def ReadFrom(reader:XmlReader) -> XNode:
        """ ReadFrom(reader: XmlReader) -> XNode """
        ...

    def Remove(self): # -> 
        """ Remove(self: XNode) """
        ...

    def ReplaceWith(self, content:object): # -> 
        """ ReplaceWith(self: XNode, content: object)ReplaceWith(self: XNode, *content: Array[object]) """
        ...

    def ToString(self, options:SaveOptions = ...) -> str:
        """
        ToString(self: XNode) -> str
        ToString(self: XNode, options: SaveOptions) -> str
        """
        ...

    def WriteTo(self, writer:XmlWriter): # -> 
        """ WriteTo(self: XNode, writer: XmlWriter) """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...



class XText(XNode): # skipped bases: <type 'IXmlLineInfo'>, <type 'object'>
    """
    XText(value: str)
    XText(other: XText)
    """
    @property
    def NodeType(self) -> XmlNodeType:
        """ Get: NodeType(self: XText) -> XmlNodeType """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: XText) -> str
        Set: Value(self: XText) = value
        """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, value: str)
        __new__(cls: type, other: XText)
        """
        ...


class XCData(XText): # skipped bases: <type 'IXmlLineInfo'>, <type 'object'>
    """
    XCData(value: str)
    XCData(other: XCData)
    """
    pass

class XComment(XNode): # skipped bases: <type 'IXmlLineInfo'>, <type 'object'>
    """
    XComment(value: str)
    XComment(other: XComment)
    """
    @property
    def NodeType(self) -> XmlNodeType:
        """ Get: NodeType(self: XComment) -> XmlNodeType """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: XComment) -> str
        Set: Value(self: XComment) = value
        """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, value: str)
        __new__(cls: type, other: XComment)
        """
        ...


class XContainer(XNode): # skipped bases: <type 'IXmlLineInfo'>, <type 'object'>
    """ no doc """
    @property
    def FirstNode(self) -> XNode:
        """ Get: FirstNode(self: XContainer) -> XNode """
        ...

    @property
    def LastNode(self) -> XNode:
        """ Get: LastNode(self: XContainer) -> XNode """
        ...


    def Add(self, content:object): # -> 
        """ Add(self: XContainer, content: object)Add(self: XContainer, *content: Array[object]) """
        ...

    def AddFirst(self, content:object): # -> 
        """ AddFirst(self: XContainer, content: object)AddFirst(self: XContainer, *content: Array[object]) """
        ...

    def CreateWriter(self) -> XmlWriter:
        """ CreateWriter(self: XContainer) -> XmlWriter """
        ...

    def DescendantNodes(self) -> IEnumerable:
        """ DescendantNodes(self: XContainer) -> IEnumerable[XNode] """
        ...

    def Descendants(self, name:XName = ...) -> IEnumerable:
        """
        Descendants(self: XContainer) -> IEnumerable[XElement]
        Descendants(self: XContainer, name: XName) -> IEnumerable[XElement]
        """
        ...

    def Element(self, name:XName) -> XElement:
        """ Element(self: XContainer, name: XName) -> XElement """
        ...

    def Elements(self, name:XName = ...) -> IEnumerable:
        """
        Elements(self: XContainer) -> IEnumerable[XElement]
        Elements(self: XContainer, name: XName) -> IEnumerable[XElement]
        """
        ...

    def Nodes(self) -> IEnumerable:
        """ Nodes(self: XContainer) -> IEnumerable[XNode] """
        ...

    def RemoveNodes(self): # -> 
        """ RemoveNodes(self: XContainer) """
        ...

    def ReplaceNodes(self, content:object): # -> 
        """ ReplaceNodes(self: XContainer, content: object)ReplaceNodes(self: XContainer, *content: Array[object]) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...


class XDeclaration: # skipped bases: <type 'object'>, <type 'object'>
    """
    XDeclaration(version: str, encoding: str, standalone: str)
    XDeclaration(other: XDeclaration)
    """
    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: XDeclaration) -> str
        Set: Encoding(self: XDeclaration) = value
        """
        ...

    @property
    def Standalone(self) -> str:
        """
        Get: Standalone(self: XDeclaration) -> str
        Set: Standalone(self: XDeclaration) = value
        """
        ...

    @property
    def Version(self) -> str:
        """
        Get: Version(self: XDeclaration) -> str
        Set: Version(self: XDeclaration) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: XDeclaration) -> str """
        ...


class XDocument(XContainer): # skipped bases: <type 'IXmlLineInfo'>, <type 'object'>
    """
    XDocument()
    XDocument(*content: Array[object])
    XDocument(declaration: XDeclaration, *content: Array[object])
    XDocument(other: XDocument)
    """
    @property
    def Declaration(self) -> XDeclaration:
        """
        Get: Declaration(self: XDocument) -> XDeclaration
        Set: Declaration(self: XDocument) = value
        """
        ...

    @property
    def DocumentType(self) -> XDocumentType:
        """ Get: DocumentType(self: XDocument) -> XDocumentType """
        ...

    @property
    def NodeType(self) -> XmlNodeType:
        """ Get: NodeType(self: XDocument) -> XmlNodeType """
        ...

    @property
    def Root(self) -> XElement:
        """ Get: Root(self: XDocument) -> XElement """
        ...


    @staticmethod
    def Load(*__args:str) -> XDocument:
        """
        Load(uri: str) -> XDocument
        Load(uri: str, options: LoadOptions) -> XDocument
        Load(stream: Stream) -> XDocument
        Load(stream: Stream, options: LoadOptions) -> XDocument
        Load(textReader: TextReader) -> XDocument
        Load(textReader: TextReader, options: LoadOptions) -> XDocument
        Load(reader: XmlReader) -> XDocument
        Load(reader: XmlReader, options: LoadOptions) -> XDocument
        """
        ...

    @staticmethod
    def Parse(text:str, options:LoadOptions = ...) -> XDocument:
        """
        Parse(text: str) -> XDocument
        Parse(text: str, options: LoadOptions) -> XDocument
        """
        ...

    def Save(self, *__args:str): # -> 
        """ Save(self: XDocument, fileName: str)Save(self: XDocument, fileName: str, options: SaveOptions)Save(self: XDocument, stream: Stream)Save(self: XDocument, stream: Stream, options: SaveOptions)Save(self: XDocument, textWriter: TextWriter)Save(self: XDocument, textWriter: TextWriter, options: SaveOptions)Save(self: XDocument, writer: XmlWriter) """
        ...

    def WriteTo(self, writer:XmlWriter): # -> 
        """ WriteTo(self: XDocument, writer: XmlWriter) """
        ...

    def __new__(cls, *__args:Array) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, *content: Array[object])
        __new__(cls: type, declaration: XDeclaration, *content: Array[object])
        __new__(cls: type, other: XDocument)
        """
        ...


class XDocumentType(XNode): # skipped bases: <type 'IXmlLineInfo'>, <type 'object'>
    """
    XDocumentType(name: str, publicId: str, systemId: str, internalSubset: str)
    XDocumentType(other: XDocumentType)
    """
    @property
    def InternalSubset(self) -> str:
        """
        Get: InternalSubset(self: XDocumentType) -> str
        Set: InternalSubset(self: XDocumentType) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: XDocumentType) -> str
        Set: Name(self: XDocumentType) = value
        """
        ...

    @property
    def NodeType(self) -> XmlNodeType:
        """ Get: NodeType(self: XDocumentType) -> XmlNodeType """
        ...

    @property
    def PublicId(self) -> str:
        """
        Get: PublicId(self: XDocumentType) -> str
        Set: PublicId(self: XDocumentType) = value
        """
        ...

    @property
    def SystemId(self) -> str:
        """
        Get: SystemId(self: XDocumentType) -> str
        Set: SystemId(self: XDocumentType) = value
        """
        ...


    def __new__(cls, *__args:XDocumentType) -> Self:
        """
        __new__(cls: type, name: str, publicId: str, systemId: str, internalSubset: str)
        __new__(cls: type, other: XDocumentType)
        """
        ...


class XElement(IXmlSerializable, XContainer): # skipped bases: <type 'IXmlLineInfo'>, <type 'object'>
    """
    XElement(name: XName)
    XElement(name: XName, content: object)
    XElement(name: XName, *content: Array[object])
    XElement(other: XElement)
    XElement(other: XStreamingElement)
    """
    @property
    def EmptySequence(self) -> IEnumerable:
        """ Get: EmptySequence() -> IEnumerable[XElement] """
        ...

    @property
    def FirstAttribute(self) -> XAttribute:
        """ Get: FirstAttribute(self: XElement) -> XAttribute """
        ...

    @property
    def HasAttributes(self) -> bool:
        """ Get: HasAttributes(self: XElement) -> bool """
        ...

    @property
    def HasElements(self) -> bool:
        """ Get: HasElements(self: XElement) -> bool """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: XElement) -> bool """
        ...

    @property
    def LastAttribute(self) -> XAttribute:
        """ Get: LastAttribute(self: XElement) -> XAttribute """
        ...

    @property
    def Name(self) -> XName:
        """
        Get: Name(self: XElement) -> XName
        Set: Name(self: XElement) = value
        """
        ...

    @property
    def NodeType(self) -> XmlNodeType:
        """ Get: NodeType(self: XElement) -> XmlNodeType """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: XElement) -> str
        Set: Value(self: XElement) = value
        """
        ...


    def AncestorsAndSelf(self, name:XName = ...) -> IEnumerable:
        """
        AncestorsAndSelf(self: XElement) -> IEnumerable[XElement]
        AncestorsAndSelf(self: XElement, name: XName) -> IEnumerable[XElement]
        """
        ...

    def Attribute(self, name:XName) -> XAttribute:
        """ Attribute(self: XElement, name: XName) -> XAttribute """
        ...

    def Attributes(self, name:XName = ...) -> IEnumerable:
        """
        Attributes(self: XElement) -> IEnumerable[XAttribute]
        Attributes(self: XElement, name: XName) -> IEnumerable[XAttribute]
        """
        ...

    def DescendantNodesAndSelf(self) -> IEnumerable:
        """ DescendantNodesAndSelf(self: XElement) -> IEnumerable[XNode] """
        ...

    def DescendantsAndSelf(self, name:XName = ...) -> IEnumerable:
        """
        DescendantsAndSelf(self: XElement) -> IEnumerable[XElement]
        DescendantsAndSelf(self: XElement, name: XName) -> IEnumerable[XElement]
        """
        ...

    def GetDefaultNamespace(self) -> XNamespace:
        """ GetDefaultNamespace(self: XElement) -> XNamespace """
        ...

    def GetNamespaceOfPrefix(self, prefix:str) -> XNamespace:
        """ GetNamespaceOfPrefix(self: XElement, prefix: str) -> XNamespace """
        ...

    def GetPrefixOfNamespace(self, ns:XNamespace) -> str:
        """ GetPrefixOfNamespace(self: XElement, ns: XNamespace) -> str """
        ...

    @staticmethod
    def Load(*__args:str) -> XElement:
        """
        Load(uri: str) -> XElement
        Load(uri: str, options: LoadOptions) -> XElement
        Load(stream: Stream) -> XElement
        Load(stream: Stream, options: LoadOptions) -> XElement
        Load(textReader: TextReader) -> XElement
        Load(textReader: TextReader, options: LoadOptions) -> XElement
        Load(reader: XmlReader) -> XElement
        Load(reader: XmlReader, options: LoadOptions) -> XElement
        """
        ...

    @staticmethod
    def Parse(text:str, options:LoadOptions = ...) -> XElement:
        """
        Parse(text: str) -> XElement
        Parse(text: str, options: LoadOptions) -> XElement
        """
        ...

    def RemoveAll(self): # -> 
        """ RemoveAll(self: XElement) """
        ...

    def RemoveAttributes(self): # -> 
        """ RemoveAttributes(self: XElement) """
        ...

    def ReplaceAll(self, content:object): # -> 
        """ ReplaceAll(self: XElement, content: object)ReplaceAll(self: XElement, *content: Array[object]) """
        ...

    def ReplaceAttributes(self, content:object): # -> 
        """ ReplaceAttributes(self: XElement, content: object)ReplaceAttributes(self: XElement, *content: Array[object]) """
        ...

    def Save(self, *__args:str): # -> 
        """ Save(self: XElement, fileName: str)Save(self: XElement, fileName: str, options: SaveOptions)Save(self: XElement, stream: Stream)Save(self: XElement, stream: Stream, options: SaveOptions)Save(self: XElement, textWriter: TextWriter)Save(self: XElement, textWriter: TextWriter, options: SaveOptions)Save(self: XElement, writer: XmlWriter) """
        ...

    def SetAttributeValue(self, name:XName, value:object): # -> 
        """ SetAttributeValue(self: XElement, name: XName, value: object) """
        ...

    def SetElementValue(self, name:XName, value:object): # -> 
        """ SetElementValue(self: XElement, name: XName, value: object) """
        ...

    def SetValue(self, value:object): # -> 
        """ SetValue(self: XElement, value: object) """
        ...

    def WriteTo(self, writer:XmlWriter): # -> 
        """ WriteTo(self: XElement, writer: XmlWriter) """
        ...

    def __complex__(self, *args): #cannot find CLR method
        """ __complex__(element: XElement) -> float """
        ...

    def __float__(self, *args): #cannot find CLR method
        """ __complex__(element: XElement) -> float """
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(element: XElement) -> int """
        ...

    def __long__(self, *args): #cannot find CLR method
        """ __int__(element: XElement) -> int """
        ...

    def __new__(cls, *__args:XName) -> Self:
        """
        __new__(cls: type, name: XName)
        __new__(cls: type, name: XName, content: object)
        __new__(cls: type, name: XName, *content: Array[object])
        __new__(cls: type, other: XElement)
        __new__(cls: type, other: XStreamingElement)
        """
        ...



class XName(ISerializable, IEquatable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LocalName(self) -> str:
        """ Get: LocalName(self: XName) -> str """
        ...

    @property
    def Namespace(self) -> XNamespace:
        """ Get: Namespace(self: XName) -> XNamespace """
        ...

    @property
    def NamespaceName(self) -> str:
        """ Get: NamespaceName(self: XName) -> str """
        ...


    @staticmethod
    def Get(*__args:str) -> XName:
        """
        Get(localName: str, namespaceName: str) -> XName
        Get(expandedName: str) -> XName
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: XName) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: XName) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class XNamespace: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def NamespaceName(self) -> str:
        """ Get: NamespaceName(self: XNamespace) -> str """
        ...

    @property
    def Xml(self) -> XNamespace:
        """ Get: Xml() -> XNamespace """
        ...

    @property
    def Xmlns(self) -> XNamespace:
        """ Get: Xmlns() -> XNamespace """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: XNamespace, obj: object) -> bool """
        ...

    @staticmethod
    def Get(namespaceName:str) -> XNamespace:
        """ Get(namespaceName: str) -> XNamespace """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: XNamespace) -> int """
        ...

    def GetName(self, localName:str) -> XName:
        """ GetName(self: XNamespace, localName: str) -> XName """
        ...

    def ToString(self) -> str:
        """ ToString(self: XNamespace) -> str """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class XNodeDocumentOrderComparer(IComparer): # skipped bases: <type 'object'>
    """ XNodeDocumentOrderComparer() """
    pass

class XNodeEqualityComparer(IEqualityComparer): # skipped bases: <type 'object'>
    """ XNodeEqualityComparer() """
    pass

class XObjectChange(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XObjectChange, values: Add (0), Name (2), Remove (1), Value (3) """
    Add: XObjectChange = ...
    Name: XObjectChange = ...
    Remove: XObjectChange = ...
    Value: XObjectChange = ...
    value__ = ...


class XObjectChangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ XObjectChangeEventArgs(objectChange: XObjectChange) """
    @property
    def ObjectChange(self) -> XObjectChange:
        """ Get: ObjectChange(self: XObjectChangeEventArgs) -> XObjectChange """
        ...


    def __new__(cls, objectChange:XObjectChange) -> Self:
        """ __new__(cls: type, objectChange: XObjectChange) """
        ...

    Add: XObjectChangeEventArgs = ...
    Name: XObjectChangeEventArgs = ...
    Remove: XObjectChangeEventArgs = ...
    Value: XObjectChangeEventArgs = ...


class XProcessingInstruction(XNode): # skipped bases: <type 'IXmlLineInfo'>, <type 'object'>
    """
    XProcessingInstruction(target: str, data: str)
    XProcessingInstruction(other: XProcessingInstruction)
    """
    @property
    def Data(self) -> str:
        """
        Get: Data(self: XProcessingInstruction) -> str
        Set: Data(self: XProcessingInstruction) = value
        """
        ...

    @property
    def NodeType(self) -> XmlNodeType:
        """ Get: NodeType(self: XProcessingInstruction) -> XmlNodeType """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: XProcessingInstruction) -> str
        Set: Target(self: XProcessingInstruction) = value
        """
        ...


    def __new__(cls, *__args:XProcessingInstruction) -> Self:
        """
        __new__(cls: type, target: str, data: str)
        __new__(cls: type, other: XProcessingInstruction)
        """
        ...


class XStreamingElement: # skipped bases: <type 'object'>, <type 'object'>
    """
    XStreamingElement(name: XName)
    XStreamingElement(name: XName, content: object)
    XStreamingElement(name: XName, *content: Array[object])
    """
    @property
    def Name(self) -> XName:
        """
        Get: Name(self: XStreamingElement) -> XName
        Set: Name(self: XStreamingElement) = value
        """
        ...


    def Add(self, content:Array): # -> 
        """ Add(self: XStreamingElement, *content: Array[object])Add(self: XStreamingElement, content: object) """
        ...

    def Save(self, *__args:str): # -> 
        """ Save(self: XStreamingElement, fileName: str)Save(self: XStreamingElement, stream: Stream)Save(self: XStreamingElement, textWriter: TextWriter)Save(self: XStreamingElement, fileName: str, options: SaveOptions)Save(self: XStreamingElement, stream: Stream, options: SaveOptions)Save(self: XStreamingElement, textWriter: TextWriter, options: SaveOptions)Save(self: XStreamingElement, writer: XmlWriter) """
        ...

    def ToString(self, options:SaveOptions = ...) -> str:
        """
        ToString(self: XStreamingElement) -> str
        ToString(self: XStreamingElement, options: SaveOptions) -> str
        """
        ...

    def WriteTo(self, writer:XmlWriter): # -> 
        """ WriteTo(self: XStreamingElement, writer: XmlWriter) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...


