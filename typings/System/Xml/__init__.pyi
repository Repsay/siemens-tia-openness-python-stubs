# encoding: utf-8
# module System.Xml calls itself Xml
# from System.Xml.Linq, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Runtime.Serialization, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Xml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Data.SqlXml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Byte, Char, DateTime, 
    DateTimeOffset, Decimal, Enum, EventArgs, Guid, IAsyncResult, ICloneable, 
    IDisposable, Int16, Int64, MulticastDelegate, SByte, Single, 
    SystemException, TimeSpan, Type, UInt16, UInt32, UInt64, Uri)

from System.Collections import ICollection, IDictionary, IEnumerable

from System.IO import Stream, TextReader, TextWriter

from System.Security.Policy import Evidence

from System.Text import Encoding

from System.Threading.Tasks import Task

from System.Xml.Schema import (IXmlSchemaInfo, ValidationEventHandler, 
    XmlSchemaCollection, XmlSchemaSet, XmlSchemaValidationFlags)

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, DataRow, 
    DataSet, IXPathNavigable, IXmlDictionary, OnXmlDictionaryReaderClose, 
    XPathNavigator, XmlAttributeCollection, XmlBinaryReaderSession, 
    XmlBinaryWriterSession, XmlDeclaration, XmlDictionaryReader, 
    XmlDictionaryReaderQuotaTypes, XmlDictionaryReaderQuotas, 
    XmlDictionaryString, XmlDocument, XmlDocumentFragment, XmlDocumentType, 
    XmlElement, XmlEntityReference, XmlImplementation, XmlNamespaceManager, 
    XmlNamespaceScope, XmlNode, XmlNodeList, XmlNodeType, 
    XmlProcessingInstruction, XmlReader, XmlReaderSettings, 
    XmlSignificantWhitespace, XmlSpace, XmlText, XmlWhitespace, XmlWriter, 
    XmlWriterSettings, field#)
"""

# no functions
# classes

class ConformanceLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConformanceLevel, values: Auto (0), Document (2), Fragment (1) """
    Auto: ConformanceLevel = ...
    Document: ConformanceLevel = ...
    Fragment: ConformanceLevel = ...
    value__ = ...


class DtdProcessing(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DtdProcessing, values: Ignore (1), Parse (2), Prohibit (0) """
    Ignore: DtdProcessing = ...
    Parse: DtdProcessing = ...
    Prohibit: DtdProcessing = ...
    value__ = ...


class EntityHandling(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EntityHandling, values: ExpandCharEntities (2), ExpandEntities (1) """
    ExpandCharEntities: EntityHandling = ...
    ExpandEntities: EntityHandling = ...
    value__ = ...


class Formatting(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Formatting, values: Indented (1), None (0) """
    Indented: Formatting = ...
    value__ = ...


class IApplicationResourceStreamResolver: # skipped bases: <type 'object'>
    """ no doc """
    def GetApplicationResourceStream(self, relativeUri:Uri) -> Stream:
        """ GetApplicationResourceStream(self: IApplicationResourceStreamResolver, relativeUri: Uri) -> Stream """
        ...


class IFragmentCapableXmlDictionaryWriter: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CanFragment(self) -> bool:
        """ Get: CanFragment(self: IFragmentCapableXmlDictionaryWriter) -> bool """
        ...


    def EndFragment(self): # -> 
        """ EndFragment(self: IFragmentCapableXmlDictionaryWriter) """
        ...

    def StartFragment(self, stream:Stream, generateSelfContainedTextFragment:bool): # -> 
        """ StartFragment(self: IFragmentCapableXmlDictionaryWriter, stream: Stream, generateSelfContainedTextFragment: bool) """
        ...

    def WriteFragment(self, buffer:Array, offset:int, count:int): # -> 
        """ WriteFragment(self: IFragmentCapableXmlDictionaryWriter, buffer: Array[Byte], offset: int, count: int) """
        ...


class IHasXmlNode: # skipped bases: <type 'object'>
    """ no doc """
    def GetNode(self): # -> XmlNode
        """ GetNode(self: IHasXmlNode) -> XmlNode """
        ...


class IStreamProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetStream(self) -> Stream:
        """ GetStream(self: IStreamProvider) -> Stream """
        ...

    def ReleaseStream(self, stream:Stream): # -> 
        """ ReleaseStream(self: IStreamProvider, stream: Stream) """
        ...


class IXmlBinaryReaderInitializer: # skipped bases: <type 'object'>
    """ no doc """
    def SetInput(self, *__args): # -> 
        """ SetInput(self: IXmlBinaryReaderInitializer, buffer: Array[Byte], offset: int, count: int, dictionary: IXmlDictionary, quotas: XmlDictionaryReaderQuotas, session: XmlBinaryReaderSession, onClose: OnXmlDictionaryReaderClose)SetInput(self: IXmlBinaryReaderInitializer, stream: Stream, dictionary: IXmlDictionary, quotas: XmlDictionaryReaderQuotas, session: XmlBinaryReaderSession, onClose: OnXmlDictionaryReaderClose) """
        ...


class IXmlBinaryWriterInitializer: # skipped bases: <type 'object'>
    """ no doc """
    def SetOutput(self, stream:Stream, dictionary, session, ownsStream:bool): # ->  # Not found arg types: {'dictionary': 'IXmlDictionary', 'session': 'XmlBinaryWriterSession'}
        """ SetOutput(self: IXmlBinaryWriterInitializer, stream: Stream, dictionary: IXmlDictionary, session: XmlBinaryWriterSession, ownsStream: bool) """
        ...


class IXmlDictionary: # skipped bases: <type 'object'>
    """ no doc """
    def TryLookup(self, *__args:str): # -> Tuple_[bool, XmlDictionaryString]
        """
        TryLookup(self: IXmlDictionary, value: str) -> (bool, XmlDictionaryString)
        TryLookup(self: IXmlDictionary, key: int) -> (bool, XmlDictionaryString)
        TryLookup(self: IXmlDictionary, value: XmlDictionaryString) -> (bool, XmlDictionaryString)
        """
        ...


class IXmlLineInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: IXmlLineInfo) -> int """
        ...

    @property
    def LinePosition(self) -> int:
        """ Get: LinePosition(self: IXmlLineInfo) -> int """
        ...


    def HasLineInfo(self) -> bool:
        """ HasLineInfo(self: IXmlLineInfo) -> bool """
        ...


class IXmlMtomReaderInitializer: # skipped bases: <type 'object'>
    """ no doc """
    def SetInput(self, *__args): # -> 
        """ SetInput(self: IXmlMtomReaderInitializer, buffer: Array[Byte], offset: int, count: int, encodings: Array[Encoding], contentType: str, quotas: XmlDictionaryReaderQuotas, maxBufferSize: int, onClose: OnXmlDictionaryReaderClose)SetInput(self: IXmlMtomReaderInitializer, stream: Stream, encodings: Array[Encoding], contentType: str, quotas: XmlDictionaryReaderQuotas, maxBufferSize: int, onClose: OnXmlDictionaryReaderClose) """
        ...


class IXmlMtomWriterInitializer: # skipped bases: <type 'object'>
    """ no doc """
    def SetOutput(self, stream:Stream, encoding:Encoding, maxSizeInBytes:int, startInfo:str, boundary:str, startUri:str, writeMessageHeaders:bool, ownsStream:bool): # -> 
        """ SetOutput(self: IXmlMtomWriterInitializer, stream: Stream, encoding: Encoding, maxSizeInBytes: int, startInfo: str, boundary: str, startUri: str, writeMessageHeaders: bool, ownsStream: bool) """
        ...


class IXmlNamespaceResolver: # skipped bases: <type 'object'>
    """ no doc """
    def GetNamespacesInScope(self, scope) -> IDictionary: # Not found arg types: {'scope': 'XmlNamespaceScope'}
        """ GetNamespacesInScope(self: IXmlNamespaceResolver, scope: XmlNamespaceScope) -> IDictionary[str, str] """
        ...

    def LookupNamespace(self, prefix:str) -> str:
        """ LookupNamespace(self: IXmlNamespaceResolver, prefix: str) -> str """
        ...

    def LookupPrefix(self, namespaceName:str) -> str:
        """ LookupPrefix(self: IXmlNamespaceResolver, namespaceName: str) -> str """
        ...


class IXmlTextReaderInitializer: # skipped bases: <type 'object'>
    """ no doc """
    def SetInput(self, *__args): # -> 
        """ SetInput(self: IXmlTextReaderInitializer, buffer: Array[Byte], offset: int, count: int, encoding: Encoding, quotas: XmlDictionaryReaderQuotas, onClose: OnXmlDictionaryReaderClose)SetInput(self: IXmlTextReaderInitializer, stream: Stream, encoding: Encoding, quotas: XmlDictionaryReaderQuotas, onClose: OnXmlDictionaryReaderClose) """
        ...


class IXmlTextWriterInitializer: # skipped bases: <type 'object'>
    """ no doc """
    def SetOutput(self, stream:Stream, encoding:Encoding, ownsStream:bool): # -> 
        """ SetOutput(self: IXmlTextWriterInitializer, stream: Stream, encoding: Encoding, ownsStream: bool) """
        ...


class NamespaceHandling(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) NamespaceHandling, values: Default (0), OmitDuplicates (1) """
    Default: NamespaceHandling = ...
    OmitDuplicates: NamespaceHandling = ...
    value__ = ...


class XmlNameTable: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Add(self, array:Array, offset:int = ..., length:int = ...) -> str:
        """
        Add(self: XmlNameTable, array: Array[Char], offset: int, length: int) -> str
        Add(self: XmlNameTable, array: str) -> str
        """
        ...

    def Get(self, array:Array, offset:int = ..., length:int = ...) -> str:
        """
        Get(self: XmlNameTable, array: Array[Char], offset: int, length: int) -> str
        Get(self: XmlNameTable, array: str) -> str
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...


class NameTable(XmlNameTable): # skipped bases: <type 'object'>
    """ NameTable() """
    pass

class NewLineHandling(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NewLineHandling, values: Entitize (1), None (2), Replace (0) """
    Entitize: NewLineHandling = ...
    Replace: NewLineHandling = ...
    value__ = ...


class OnXmlDictionaryReaderClose(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OnXmlDictionaryReaderClose(object: object, method: IntPtr) """
    def BeginInvoke(self, reader, callback:AsyncCallback, object:object) -> IAsyncResult: # Not found arg types: {'reader': 'XmlDictionaryReader'}
        """ BeginInvoke(self: OnXmlDictionaryReaderClose, reader: XmlDictionaryReader, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: OnXmlDictionaryReaderClose, result: IAsyncResult) """
        ...

    def Invoke(self, reader): # ->  # Not found arg types: {'reader': 'XmlDictionaryReader'}
        """ Invoke(self: OnXmlDictionaryReaderClose, reader: XmlDictionaryReader) """
        ...


class ReadState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ReadState, values: Closed (4), EndOfFile (3), Error (2), Initial (0), Interactive (1) """
    Closed: ReadState = ...
    EndOfFile: ReadState = ...
    Error: ReadState = ...
    Initial: ReadState = ...
    Interactive: ReadState = ...
    value__ = ...


class UniqueId: # skipped bases: <type 'object'>, <type 'object'>
    """
    UniqueId()
    UniqueId(guid: Guid)
    UniqueId(guid: Array[Byte])
    UniqueId(guid: Array[Byte], offset: int)
    UniqueId(value: str)
    UniqueId(chars: Array[Char], offset: int, count: int)
    """
    @property
    def CharArrayLength(self) -> int:
        """ Get: CharArrayLength(self: UniqueId) -> int """
        ...

    @property
    def IsGuid(self) -> bool:
        """ Get: IsGuid(self: UniqueId) -> bool """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: UniqueId, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: UniqueId) -> int """
        ...

    def ToCharArray(self, chars:Array, offset:int) -> int:
        """ ToCharArray(self: UniqueId, chars: Array[Char], offset: int) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: UniqueId) -> str """
        ...

    def TryGetGuid(self, *__args) -> bool:
        """
        TryGetGuid(self: UniqueId, buffer: Array[Byte], offset: int) -> bool
        TryGetGuid(self: UniqueId) -> (bool, Guid)
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ValidationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ValidationType, values: Auto (1), DTD (2), None (0), Schema (4), XDR (3) """
    Auto: ValidationType = ...
    DTD: ValidationType = ...
    Schema: ValidationType = ...
    value__ = ...
    XDR: ValidationType = ...


class WhitespaceHandling(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WhitespaceHandling, values: All (0), None (2), Significant (1) """
    All: WhitespaceHandling = ...
    Significant: WhitespaceHandling = ...
    value__ = ...


class WriteState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WriteState, values: Attribute (3), Closed (5), Content (4), Element (2), Error (6), Prolog (1), Start (0) """
    Attribute: WriteState = ...
    Closed: WriteState = ...
    Content: WriteState = ...
    Element: WriteState = ...
    Error: WriteState = ...
    Prolog: WriteState = ...
    Start: WriteState = ...
    value__ = ...


class XmlNode(ICloneable, IEnumerable, IXPathNavigable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attributes(self): # -> XmlAttributeCollection
        """ Get: Attributes(self: XmlNode) -> XmlAttributeCollection """
        ...

    @property
    def BaseURI(self) -> str:
        """ Get: BaseURI(self: XmlNode) -> str """
        ...

    @property
    def ChildNodes(self): # -> XmlNodeList
        """ Get: ChildNodes(self: XmlNode) -> XmlNodeList """
        ...

    @property
    def FirstChild(self) -> XmlNode:
        """ Get: FirstChild(self: XmlNode) -> XmlNode """
        ...

    @property
    def HasChildNodes(self) -> bool:
        """ Get: HasChildNodes(self: XmlNode) -> bool """
        ...

    @property
    def InnerText(self) -> str:
        """
        Get: InnerText(self: XmlNode) -> str
        Set: InnerText(self: XmlNode) = value
        """
        ...

    @property
    def InnerXml(self) -> str:
        """
        Get: InnerXml(self: XmlNode) -> str
        Set: InnerXml(self: XmlNode) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: XmlNode) -> bool """
        ...

    @property
    def LastChild(self) -> XmlNode:
        """ Get: LastChild(self: XmlNode) -> XmlNode """
        ...

    @property
    def LocalName(self) -> str:
        """ Get: LocalName(self: XmlNode) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlNode) -> str """
        ...

    @property
    def NamespaceURI(self) -> str:
        """ Get: NamespaceURI(self: XmlNode) -> str """
        ...

    @property
    def NextSibling(self) -> XmlNode:
        """ Get: NextSibling(self: XmlNode) -> XmlNode """
        ...

    @property
    def NodeType(self): # -> XmlNodeType
        """ Get: NodeType(self: XmlNode) -> XmlNodeType """
        ...

    @property
    def OuterXml(self) -> str:
        """ Get: OuterXml(self: XmlNode) -> str """
        ...

    @property
    def OwnerDocument(self): # -> XmlDocument
        """ Get: OwnerDocument(self: XmlNode) -> XmlDocument """
        ...

    @property
    def ParentNode(self) -> XmlNode:
        """ Get: ParentNode(self: XmlNode) -> XmlNode """
        ...

    @property
    def Prefix(self) -> str:
        """
        Get: Prefix(self: XmlNode) -> str
        Set: Prefix(self: XmlNode) = value
        """
        ...

    @property
    def PreviousSibling(self) -> XmlNode:
        """ Get: PreviousSibling(self: XmlNode) -> XmlNode """
        ...

    @property
    def PreviousText(self) -> XmlNode:
        """ Get: PreviousText(self: XmlNode) -> XmlNode """
        ...

    @property
    def SchemaInfo(self) -> IXmlSchemaInfo:
        """ Get: SchemaInfo(self: XmlNode) -> IXmlSchemaInfo """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: XmlNode) -> str
        Set: Value(self: XmlNode) = value
        """
        ...


    def AppendChild(self, newChild:XmlNode) -> XmlNode:
        """ AppendChild(self: XmlNode, newChild: XmlNode) -> XmlNode """
        ...

    def CloneNode(self, deep:bool) -> XmlNode:
        """ CloneNode(self: XmlNode, deep: bool) -> XmlNode """
        ...

    def GetNamespaceOfPrefix(self, prefix:str) -> str:
        """ GetNamespaceOfPrefix(self: XmlNode, prefix: str) -> str """
        ...

    def GetPrefixOfNamespace(self, namespaceURI:str) -> str:
        """ GetPrefixOfNamespace(self: XmlNode, namespaceURI: str) -> str """
        ...

    def InsertAfter(self, newChild:XmlNode, refChild:XmlNode) -> XmlNode:
        """ InsertAfter(self: XmlNode, newChild: XmlNode, refChild: XmlNode) -> XmlNode """
        ...

    def InsertBefore(self, newChild:XmlNode, refChild:XmlNode) -> XmlNode:
        """ InsertBefore(self: XmlNode, newChild: XmlNode, refChild: XmlNode) -> XmlNode """
        ...

    def Normalize(self): # -> 
        """ Normalize(self: XmlNode) """
        ...

    def PrependChild(self, newChild:XmlNode) -> XmlNode:
        """ PrependChild(self: XmlNode, newChild: XmlNode) -> XmlNode """
        ...

    def RemoveAll(self): # -> 
        """ RemoveAll(self: XmlNode) """
        ...

    def RemoveChild(self, oldChild:XmlNode) -> XmlNode:
        """ RemoveChild(self: XmlNode, oldChild: XmlNode) -> XmlNode """
        ...

    def ReplaceChild(self, newChild:XmlNode, oldChild:XmlNode) -> XmlNode:
        """ ReplaceChild(self: XmlNode, newChild: XmlNode, oldChild: XmlNode) -> XmlNode """
        ...

    def SelectNodes(self, xpath:str, nsmgr = ...): # -> XmlNodeList # Not found arg types: {'nsmgr': 'XmlNamespaceManager'}
        """
        SelectNodes(self: XmlNode, xpath: str) -> XmlNodeList
        SelectNodes(self: XmlNode, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNodeList
        """
        ...

    def SelectSingleNode(self, xpath:str, nsmgr = ...) -> XmlNode: # Not found arg types: {'nsmgr': 'XmlNamespaceManager'}
        """
        SelectSingleNode(self: XmlNode, xpath: str) -> XmlNode
        SelectSingleNode(self: XmlNode, xpath: str, nsmgr: XmlNamespaceManager) -> XmlNode
        """
        ...

    def Supports(self, feature:str, version:str) -> bool:
        """ Supports(self: XmlNode, feature: str, version: str) -> bool """
        ...

    def WriteContentTo(self, w): # ->  # Not found arg types: {'w': 'XmlWriter'}
        """ WriteContentTo(self: XmlNode, w: XmlWriter) """
        ...

    def WriteTo(self, w): # ->  # Not found arg types: {'w': 'XmlWriter'}
        """ WriteTo(self: XmlNode, w: XmlWriter) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class XmlAttribute(XmlNode): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    @property
    def OwnerElement(self): # -> XmlElement
        """ Get: OwnerElement(self: XmlAttribute) -> XmlElement """
        ...

    @property
    def Specified(self) -> bool:
        """ Get: Specified(self: XmlAttribute) -> bool """
        ...


    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, prefix: str, localName: str, namespaceURI: str, doc: XmlDocument) """
        ...


class XmlNamedNodeMap(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: XmlNamedNodeMap) -> int """
        ...


    def GetNamedItem(self, *__args:str) -> XmlNode:
        """
        GetNamedItem(self: XmlNamedNodeMap, name: str) -> XmlNode
        GetNamedItem(self: XmlNamedNodeMap, localName: str, namespaceURI: str) -> XmlNode
        """
        ...

    def Item(self, index:int) -> XmlNode:
        """ Item(self: XmlNamedNodeMap, index: int) -> XmlNode """
        ...

    def RemoveNamedItem(self, *__args:str) -> XmlNode:
        """
        RemoveNamedItem(self: XmlNamedNodeMap, name: str) -> XmlNode
        RemoveNamedItem(self: XmlNamedNodeMap, localName: str, namespaceURI: str) -> XmlNode
        """
        ...

    def SetNamedItem(self, node:XmlNode) -> XmlNode:
        """ SetNamedItem(self: XmlNamedNodeMap, node: XmlNode) -> XmlNode """
        ...


class XmlAttributeCollection(XmlNamedNodeMap, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Append(self, node:XmlAttribute) -> XmlAttribute:
        """ Append(self: XmlAttributeCollection, node: XmlAttribute) -> XmlAttribute """
        ...

    def InsertAfter(self, newNode:XmlAttribute, refNode:XmlAttribute) -> XmlAttribute:
        """ InsertAfter(self: XmlAttributeCollection, newNode: XmlAttribute, refNode: XmlAttribute) -> XmlAttribute """
        ...

    def InsertBefore(self, newNode:XmlAttribute, refNode:XmlAttribute) -> XmlAttribute:
        """ InsertBefore(self: XmlAttributeCollection, newNode: XmlAttribute, refNode: XmlAttribute) -> XmlAttribute """
        ...

    def Prepend(self, node:XmlAttribute) -> XmlAttribute:
        """ Prepend(self: XmlAttributeCollection, node: XmlAttribute) -> XmlAttribute """
        ...

    def Remove(self, node:XmlAttribute) -> XmlAttribute:
        """ Remove(self: XmlAttributeCollection, node: XmlAttribute) -> XmlAttribute """
        ...

    def RemoveAll(self): # -> 
        """ RemoveAll(self: XmlAttributeCollection) """
        ...

    def RemoveAt(self, i:int) -> XmlAttribute:
        """ RemoveAt(self: XmlAttributeCollection, i: int) -> XmlAttribute """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class XmlBinaryReaderSession(IXmlDictionary): # skipped bases: <type 'object'>
    """ XmlBinaryReaderSession() """
    def Add(self, id:int, value:str): # -> XmlDictionaryString
        """ Add(self: XmlBinaryReaderSession, id: int, value: str) -> XmlDictionaryString """
        ...

    def Clear(self): # -> 
        """ Clear(self: XmlBinaryReaderSession) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class XmlBinaryWriterSession: # skipped bases: <type 'object'>, <type 'object'>
    """ XmlBinaryWriterSession() """
    def Reset(self): # -> 
        """ Reset(self: XmlBinaryWriterSession) """
        ...

    def TryAdd(self, value, key) -> Tuple_[bool, int]:
        """ TryAdd(self: XmlBinaryWriterSession, value: XmlDictionaryString) -> (bool, int) """
        ...


class XmlLinkedNode(XmlNode): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    pass

class XmlCharacterData(XmlLinkedNode): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    @property
    def Data(self) -> str:
        """
        Get: Data(self: XmlCharacterData) -> str
        Set: Data(self: XmlCharacterData) = value
        """
        ...

    @property
    def InnerText(self) -> str:
        """
        Get: InnerText(self: XmlCharacterData) -> str
        Set: InnerText(self: XmlCharacterData) = value
        """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: XmlCharacterData) -> int """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: XmlCharacterData) -> str
        Set: Value(self: XmlCharacterData) = value
        """
        ...


    def AppendData(self, strData:str): # -> 
        """ AppendData(self: XmlCharacterData, strData: str) """
        ...

    def DeleteData(self, offset:int, count:int): # -> 
        """ DeleteData(self: XmlCharacterData, offset: int, count: int) """
        ...

    def InsertData(self, offset:int, strData:str): # -> 
        """ InsertData(self: XmlCharacterData, offset: int, strData: str) """
        ...

    def ReplaceData(self, offset:int, count:int, strData:str): # -> 
        """ ReplaceData(self: XmlCharacterData, offset: int, count: int, strData: str) """
        ...

    def Substring(self, offset:int, count:int) -> str:
        """ Substring(self: XmlCharacterData, offset: int, count: int) -> str """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, data: str, doc: XmlDocument) """
        ...


class XmlCDataSection(XmlCharacterData): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    @property
    def LocalName(self) -> str:
        """ Get: LocalName(self: XmlCDataSection) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlCDataSection) -> str """
        ...

    @property
    def NodeType(self): # -> XmlNodeType
        """ Get: NodeType(self: XmlCDataSection) -> XmlNodeType """
        ...

    @property
    def ParentNode(self) -> XmlNode:
        """ Get: ParentNode(self: XmlCDataSection) -> XmlNode """
        ...

    @property
    def PreviousText(self) -> XmlNode:
        """ Get: PreviousText(self: XmlCDataSection) -> XmlNode """
        ...


    def CloneNode(self, deep:bool) -> XmlNode:
        """ CloneNode(self: XmlCDataSection, deep: bool) -> XmlNode """
        ...

    def WriteContentTo(self, w): # ->  # Not found arg types: {'w': 'XmlWriter'}
        """ WriteContentTo(self: XmlCDataSection, w: XmlWriter) """
        ...

    def WriteTo(self, w): # ->  # Not found arg types: {'w': 'XmlWriter'}
        """ WriteTo(self: XmlCDataSection, w: XmlWriter) """
        ...


class XmlComment(XmlCharacterData): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    @property
    def LocalName(self) -> str:
        """ Get: LocalName(self: XmlComment) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlComment) -> str """
        ...

    @property
    def NodeType(self): # -> XmlNodeType
        """ Get: NodeType(self: XmlComment) -> XmlNodeType """
        ...


    def CloneNode(self, deep:bool) -> XmlNode:
        """ CloneNode(self: XmlComment, deep: bool) -> XmlNode """
        ...

    def WriteContentTo(self, w): # ->  # Not found arg types: {'w': 'XmlWriter'}
        """ WriteContentTo(self: XmlComment, w: XmlWriter) """
        ...

    def WriteTo(self, w): # ->  # Not found arg types: {'w': 'XmlWriter'}
        """ WriteTo(self: XmlComment, w: XmlWriter) """
        ...


class XmlConvert: # skipped bases: <type 'object'>, <type 'object'>
    """ XmlConvert() """
    @staticmethod
    def DecodeName(name:str) -> str:
        """ DecodeName(name: str) -> str """
        ...

    @staticmethod
    def EncodeLocalName(name:str) -> str:
        """ EncodeLocalName(name: str) -> str """
        ...

    @staticmethod
    def EncodeName(name:str) -> str:
        """ EncodeName(name: str) -> str """
        ...

    @staticmethod
    def EncodeNmToken(name:str) -> str:
        """ EncodeNmToken(name: str) -> str """
        ...

    @staticmethod
    def IsNCNameChar(ch:Char) -> bool:
        """ IsNCNameChar(ch: Char) -> bool """
        ...

    @staticmethod
    def IsPublicIdChar(ch:Char) -> bool:
        """ IsPublicIdChar(ch: Char) -> bool """
        ...

    @staticmethod
    def IsStartNCNameChar(ch:Char) -> bool:
        """ IsStartNCNameChar(ch: Char) -> bool """
        ...

    @staticmethod
    def IsWhitespaceChar(ch:Char) -> bool:
        """ IsWhitespaceChar(ch: Char) -> bool """
        ...

    @staticmethod
    def IsXmlChar(ch:Char) -> bool:
        """ IsXmlChar(ch: Char) -> bool """
        ...

    @staticmethod
    def IsXmlSurrogatePair(lowChar:Char, highChar:Char) -> bool:
        """ IsXmlSurrogatePair(lowChar: Char, highChar: Char) -> bool """
        ...

    @staticmethod
    def ToBoolean(s:str) -> bool:
        """ ToBoolean(s: str) -> bool """
        ...

    @staticmethod
    def ToByte(s:str) -> Byte:
        """ ToByte(s: str) -> Byte """
        ...

    @staticmethod
    def ToChar(s:str) -> Char:
        """ ToChar(s: str) -> Char """
        ...

    @staticmethod
    def ToDateTime(s:str, *__args:str) -> DateTime:
        """
        ToDateTime(s: str) -> DateTime
        ToDateTime(s: str, format: str) -> DateTime
        ToDateTime(s: str, formats: Array[str]) -> DateTime
        ToDateTime(s: str, dateTimeOption: XmlDateTimeSerializationMode) -> DateTime
        """
        ...

    @staticmethod
    def ToDateTimeOffset(s:str, *__args:str) -> DateTimeOffset:
        """
        ToDateTimeOffset(s: str) -> DateTimeOffset
        ToDateTimeOffset(s: str, format: str) -> DateTimeOffset
        ToDateTimeOffset(s: str, formats: Array[str]) -> DateTimeOffset
        """
        ...

    @staticmethod
    def ToDecimal(s:str) -> Decimal:
        """ ToDecimal(s: str) -> Decimal """
        ...

    @staticmethod
    def ToDouble(s:str) -> float:
        """ ToDouble(s: str) -> float """
        ...

    @staticmethod
    def ToGuid(s:str) -> Guid:
        """ ToGuid(s: str) -> Guid """
        ...

    @staticmethod
    def ToInt16(s:str) -> Int16:
        """ ToInt16(s: str) -> Int16 """
        ...

    @staticmethod
    def ToInt32(s:str) -> int:
        """ ToInt32(s: str) -> int """
        ...

    @staticmethod
    def ToInt64(s:str) -> Int64:
        """ ToInt64(s: str) -> Int64 """
        ...

    @staticmethod
    def ToSByte(s:str) -> SByte:
        """ ToSByte(s: str) -> SByte """
        ...

    @staticmethod
    def ToSingle(s:str) -> Single:
        """ ToSingle(s: str) -> Single """
        ...

    @staticmethod
    def ToString(value:DateTimeOffset = ..., *__args:str) -> str:
        """
        ToString(value: Char) -> str
        ToString(value: DateTime) -> str
        ToString(value: float) -> str
        ToString(value: Single) -> str
        ToString(value: Guid) -> str
        ToString(value: DateTimeOffset, format: str) -> str
        ToString(value: DateTimeOffset) -> str
        ToString(value: DateTime, format: str) -> str
        ToString(value: TimeSpan) -> str
        ToString(value: UInt64) -> str
        ToString(value: UInt32) -> str
        ToString(value: UInt16) -> str
        ToString(value: Byte) -> str
        ToString(value: Int64) -> str
        ToString(value: int) -> str
        ToString(value: Int16) -> str
        ToString(value: SByte) -> str
        ToString(value: Decimal) -> str
        ToString(value: bool) -> str
        ToString(value: DateTime, dateTimeOption: XmlDateTimeSerializationMode) -> str
        """
        ...

    @staticmethod
    def ToTimeSpan(s:str) -> TimeSpan:
        """ ToTimeSpan(s: str) -> TimeSpan """
        ...

    @staticmethod
    def ToUInt16(s:str) -> UInt16:
        """ ToUInt16(s: str) -> UInt16 """
        ...

    @staticmethod
    def ToUInt32(s:str) -> UInt32:
        """ ToUInt32(s: str) -> UInt32 """
        ...

    @staticmethod
    def ToUInt64(s:str) -> UInt64:
        """ ToUInt64(s: str) -> UInt64 """
        ...

    @staticmethod
    def VerifyName(name:str) -> str:
        """ VerifyName(name: str) -> str """
        ...

    @staticmethod
    def VerifyNCName(name:str) -> str:
        """ VerifyNCName(name: str) -> str """
        ...

    @staticmethod
    def VerifyNMTOKEN(name:str) -> str:
        """ VerifyNMTOKEN(name: str) -> str """
        ...

    @staticmethod
    def VerifyPublicId(publicId:str) -> str:
        """ VerifyPublicId(publicId: str) -> str """
        ...

    @staticmethod
    def VerifyTOKEN(token:str) -> str:
        """ VerifyTOKEN(token: str) -> str """
        ...

    @staticmethod
    def VerifyWhitespace(content:str) -> str:
        """ VerifyWhitespace(content: str) -> str """
        ...

    @staticmethod
    def VerifyXmlChars(content:str) -> str:
        """ VerifyXmlChars(content: str) -> str """
        ...


class XmlDocument(XmlNode): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """
    XmlDocument()
    XmlDocument(nt: XmlNameTable)
    """
    @property
    def DocumentElement(self): # -> XmlElement
        """ Get: DocumentElement(self: XmlDocument) -> XmlElement """
        ...

    @property
    def DocumentType(self): # -> XmlDocumentType
        """ Get: DocumentType(self: XmlDocument) -> XmlDocumentType """
        ...

    @property
    def Implementation(self): # -> XmlImplementation
        """ Get: Implementation(self: XmlDocument) -> XmlImplementation """
        ...

    @property
    def NameTable(self) -> XmlNameTable:
        """ Get: NameTable(self: XmlDocument) -> XmlNameTable """
        ...

    @property
    def PreserveWhitespace(self) -> bool:
        """
        Get: PreserveWhitespace(self: XmlDocument) -> bool
        Set: PreserveWhitespace(self: XmlDocument) = value
        """
        ...

    @property
    def Schemas(self) -> XmlSchemaSet:
        """
        Get: Schemas(self: XmlDocument) -> XmlSchemaSet
        Set: Schemas(self: XmlDocument) = value
        """
        ...

    @property
    def XmlResolver(self): # -> 
        """ Set: XmlResolver(self: XmlDocument) = value """
        ...


    def CreateAttribute(self, *__args:str) -> XmlAttribute:
        """
        CreateAttribute(self: XmlDocument, name: str) -> XmlAttribute
        CreateAttribute(self: XmlDocument, qualifiedName: str, namespaceURI: str) -> XmlAttribute
        CreateAttribute(self: XmlDocument, prefix: str, localName: str, namespaceURI: str) -> XmlAttribute
        """
        ...

    def CreateCDataSection(self, data:str) -> XmlCDataSection:
        """ CreateCDataSection(self: XmlDocument, data: str) -> XmlCDataSection """
        ...

    def CreateComment(self, data:str) -> XmlComment:
        """ CreateComment(self: XmlDocument, data: str) -> XmlComment """
        ...

    def CreateDefaultAttribute(self, *args): #cannot find CLR method
        """ CreateDefaultAttribute(self: XmlDocument, prefix: str, localName: str, namespaceURI: str) -> XmlAttribute """
        ...

    def CreateDocumentFragment(self): # -> XmlDocumentFragment
        """ CreateDocumentFragment(self: XmlDocument) -> XmlDocumentFragment """
        ...

    def CreateDocumentType(self, name:str, publicId:str, systemId:str, internalSubset:str): # -> XmlDocumentType
        """ CreateDocumentType(self: XmlDocument, name: str, publicId: str, systemId: str, internalSubset: str) -> XmlDocumentType """
        ...

    def CreateElement(self, *__args:str): # -> XmlElement
        """
        CreateElement(self: XmlDocument, name: str) -> XmlElement
        CreateElement(self: XmlDocument, qualifiedName: str, namespaceURI: str) -> XmlElement
        CreateElement(self: XmlDocument, prefix: str, localName: str, namespaceURI: str) -> XmlElement
        """
        ...

    def CreateEntityReference(self, name:str): # -> XmlEntityReference
        """ CreateEntityReference(self: XmlDocument, name: str) -> XmlEntityReference """
        ...

    def CreateNode(self, *__args) -> XmlNode:
        """
        CreateNode(self: XmlDocument, nodeTypeString: str, name: str, namespaceURI: str) -> XmlNode
        CreateNode(self: XmlDocument, type: XmlNodeType, name: str, namespaceURI: str) -> XmlNode
        CreateNode(self: XmlDocument, type: XmlNodeType, prefix: str, name: str, namespaceURI: str) -> XmlNode
        """
        ...

    def CreateProcessingInstruction(self, target:str, data:str): # -> XmlProcessingInstruction
        """ CreateProcessingInstruction(self: XmlDocument, target: str, data: str) -> XmlProcessingInstruction """
        ...

    def CreateSignificantWhitespace(self, text:str): # -> XmlSignificantWhitespace
        """ CreateSignificantWhitespace(self: XmlDocument, text: str) -> XmlSignificantWhitespace """
        ...

    def CreateTextNode(self, text:str): # -> XmlText
        """ CreateTextNode(self: XmlDocument, text: str) -> XmlText """
        ...

    def CreateWhitespace(self, text:str): # -> XmlWhitespace
        """ CreateWhitespace(self: XmlDocument, text: str) -> XmlWhitespace """
        ...

    def CreateXmlDeclaration(self, version:str, encoding:str, standalone:str): # -> XmlDeclaration
        """ CreateXmlDeclaration(self: XmlDocument, version: str, encoding: str, standalone: str) -> XmlDeclaration """
        ...

    def GetElementById(self, elementId:str): # -> XmlElement
        """ GetElementById(self: XmlDocument, elementId: str) -> XmlElement """
        ...

    def GetElementsByTagName(self, *__args:str): # -> XmlNodeList
        """
        GetElementsByTagName(self: XmlDocument, name: str) -> XmlNodeList
        GetElementsByTagName(self: XmlDocument, localName: str, namespaceURI: str) -> XmlNodeList
        """
        ...

    def ImportNode(self, node:XmlNode, deep:bool) -> XmlNode:
        """ ImportNode(self: XmlDocument, node: XmlNode, deep: bool) -> XmlNode """
        ...

    def Load(self, *__args:str): # -> 
        """ Load(self: XmlDocument, filename: str)Load(self: XmlDocument, inStream: Stream)Load(self: XmlDocument, txtReader: TextReader)Load(self: XmlDocument, reader: XmlReader) """
        ...

    def LoadXml(self, xml:str): # -> 
        """ LoadXml(self: XmlDocument, xml: str) """
        ...

    def ReadNode(self, reader) -> XmlNode: # Not found arg types: {'reader': 'XmlReader'}
        """ ReadNode(self: XmlDocument, reader: XmlReader) -> XmlNode """
        ...

    def Save(self, *__args:str): # -> 
        """ Save(self: XmlDocument, filename: str)Save(self: XmlDocument, outStream: Stream)Save(self: XmlDocument, writer: TextWriter)Save(self: XmlDocument, w: XmlWriter) """
        ...

    def Validate(self, validationEventHandler:ValidationEventHandler, nodeToValidate:XmlNode = ...): # -> 
        """ Validate(self: XmlDocument, validationEventHandler: ValidationEventHandler)Validate(self: XmlDocument, validationEventHandler: ValidationEventHandler, nodeToValidate: XmlNode) """
        ...

    def __new__(cls, nt:XmlNameTable = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, nt: XmlNameTable)
        __new__(cls: type, imp: XmlImplementation)
        """
        ...

    NodeChanged = ...
    NodeChanging = ...
    NodeInserted = ...
    NodeInserting = ...
    NodeRemoved = ...
    NodeRemoving = ...


class XmlDataDocument(XmlDocument): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """
    XmlDataDocument()
    XmlDataDocument(dataset: DataSet)
    """
    @property
    def DataSet(self): # -> DataSet
        """ Get: DataSet(self: XmlDataDocument) -> DataSet """
        ...


    def GetElementFromRow(self, r): # -> XmlElement # Not found arg types: {'r': 'DataRow'}
        """ GetElementFromRow(self: XmlDataDocument, r: DataRow) -> XmlElement """
        ...

    def GetRowFromElement(self, e): # -> DataRow # Not found arg types: {'e': 'XmlElement'}
        """ GetRowFromElement(self: XmlDataDocument, e: XmlElement) -> DataRow """
        ...


class XmlDateTimeSerializationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlDateTimeSerializationMode, values: Local (0), RoundtripKind (3), Unspecified (2), Utc (1) """
    Local: XmlDateTimeSerializationMode = ...
    RoundtripKind: XmlDateTimeSerializationMode = ...
    Unspecified: XmlDateTimeSerializationMode = ...
    Utc: XmlDateTimeSerializationMode = ...
    value__ = ...


class XmlDeclaration(XmlLinkedNode): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: XmlDeclaration) -> str
        Set: Encoding(self: XmlDeclaration) = value
        """
        ...

    @property
    def InnerText(self) -> str:
        """
        Get: InnerText(self: XmlDeclaration) -> str
        Set: InnerText(self: XmlDeclaration) = value
        """
        ...

    @property
    def LocalName(self) -> str:
        """ Get: LocalName(self: XmlDeclaration) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlDeclaration) -> str """
        ...

    @property
    def NodeType(self): # -> XmlNodeType
        """ Get: NodeType(self: XmlDeclaration) -> XmlNodeType """
        ...

    @property
    def Standalone(self) -> str:
        """
        Get: Standalone(self: XmlDeclaration) -> str
        Set: Standalone(self: XmlDeclaration) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: XmlDeclaration) -> str
        Set: Value(self: XmlDeclaration) = value
        """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: XmlDeclaration) -> str """
        ...


    def CloneNode(self, deep:bool) -> XmlNode:
        """ CloneNode(self: XmlDeclaration, deep: bool) -> XmlNode """
        ...

    def WriteContentTo(self, w): # ->  # Not found arg types: {'w': 'XmlWriter'}
        """ WriteContentTo(self: XmlDeclaration, w: XmlWriter) """
        ...

    def WriteTo(self, w): # ->  # Not found arg types: {'w': 'XmlWriter'}
        """ WriteTo(self: XmlDeclaration, w: XmlWriter) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, version: str, encoding: str, standalone: str, doc: XmlDocument) """
        ...


class XmlDictionary(IXmlDictionary): # skipped bases: <type 'object'>
    """
    XmlDictionary()
    XmlDictionary(capacity: int)
    """
    @property
    def Empty(self) -> IXmlDictionary:
        """ Get: Empty() -> IXmlDictionary """
        ...


    def Add(self, value:str): # -> XmlDictionaryString
        """ Add(self: XmlDictionary, value: str) -> XmlDictionaryString """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...



class XmlReader(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AttributeCount(self) -> int:
        """ Get: AttributeCount(self: XmlReader) -> int """
        ...

    @property
    def BaseURI(self) -> str:
        """ Get: BaseURI(self: XmlReader) -> str """
        ...

    @property
    def CanReadBinaryContent(self) -> bool:
        """ Get: CanReadBinaryContent(self: XmlReader) -> bool """
        ...

    @property
    def CanReadValueChunk(self) -> bool:
        """ Get: CanReadValueChunk(self: XmlReader) -> bool """
        ...

    @property
    def CanResolveEntity(self) -> bool:
        """ Get: CanResolveEntity(self: XmlReader) -> bool """
        ...

    @property
    def Depth(self) -> int:
        """ Get: Depth(self: XmlReader) -> int """
        ...

    @property
    def EOF(self) -> bool:
        """ Get: EOF(self: XmlReader) -> bool """
        ...

    @property
    def HasAttributes(self) -> bool:
        """ Get: HasAttributes(self: XmlReader) -> bool """
        ...

    @property
    def HasValue(self) -> bool:
        """ Get: HasValue(self: XmlReader) -> bool """
        ...

    @property
    def IsDefault(self) -> bool:
        """ Get: IsDefault(self: XmlReader) -> bool """
        ...

    @property
    def IsEmptyElement(self) -> bool:
        """ Get: IsEmptyElement(self: XmlReader) -> bool """
        ...

    @property
    def LocalName(self) -> str:
        """ Get: LocalName(self: XmlReader) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlReader) -> str """
        ...

    @property
    def NamespaceURI(self) -> str:
        """ Get: NamespaceURI(self: XmlReader) -> str """
        ...

    @property
    def NameTable(self) -> XmlNameTable:
        """ Get: NameTable(self: XmlReader) -> XmlNameTable """
        ...

    @property
    def NodeType(self): # -> XmlNodeType
        """ Get: NodeType(self: XmlReader) -> XmlNodeType """
        ...

    @property
    def Prefix(self) -> str:
        """ Get: Prefix(self: XmlReader) -> str """
        ...

    @property
    def QuoteChar(self) -> Char:
        """ Get: QuoteChar(self: XmlReader) -> Char """
        ...

    @property
    def ReadState(self) -> ReadState:
        """ Get: ReadState(self: XmlReader) -> ReadState """
        ...

    @property
    def SchemaInfo(self) -> IXmlSchemaInfo:
        """ Get: SchemaInfo(self: XmlReader) -> IXmlSchemaInfo """
        ...

    @property
    def Settings(self): # -> XmlReaderSettings
        """ Get: Settings(self: XmlReader) -> XmlReaderSettings """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: XmlReader) -> str """
        ...

    @property
    def ValueType(self) -> Type:
        """ Get: ValueType(self: XmlReader) -> Type """
        ...

    @property
    def XmlLang(self) -> str:
        """ Get: XmlLang(self: XmlReader) -> str """
        ...

    @property
    def XmlSpace(self): # -> XmlSpace
        """ Get: XmlSpace(self: XmlReader) -> XmlSpace """
        ...


    def Close(self): # -> 
        """ Close(self: XmlReader) """
        ...

    @staticmethod
    def Create(*__args:str) -> XmlReader:
        """
        Create(inputUri: str) -> XmlReader
        Create(inputUri: str, settings: XmlReaderSettings) -> XmlReader
        Create(inputUri: str, settings: XmlReaderSettings, inputContext: XmlParserContext) -> XmlReader
        Create(input: Stream) -> XmlReader
        Create(input: Stream, settings: XmlReaderSettings) -> XmlReader
        Create(input: Stream, settings: XmlReaderSettings, baseUri: str) -> XmlReader
        Create(input: Stream, settings: XmlReaderSettings, inputContext: XmlParserContext) -> XmlReader
        Create(input: TextReader) -> XmlReader
        Create(input: TextReader, settings: XmlReaderSettings) -> XmlReader
        Create(input: TextReader, settings: XmlReaderSettings, baseUri: str) -> XmlReader
        Create(input: TextReader, settings: XmlReaderSettings, inputContext: XmlParserContext) -> XmlReader
        Create(reader: XmlReader, settings: XmlReaderSettings) -> XmlReader
        """
        ...

    def GetAttribute(self, *__args:str) -> str:
        """
        GetAttribute(self: XmlReader, name: str) -> str
        GetAttribute(self: XmlReader, name: str, namespaceURI: str) -> str
        GetAttribute(self: XmlReader, i: int) -> str
        """
        ...

    def GetValueAsync(self) -> Task:
        """ GetValueAsync(self: XmlReader) -> Task[str] """
        ...

    @staticmethod
    def IsName(str:str) -> bool:
        """ IsName(str: str) -> bool """
        ...

    @staticmethod
    def IsNameToken(str:str) -> bool:
        """ IsNameToken(str: str) -> bool """
        ...

    def IsStartElement(self, *__args:str) -> bool:
        """
        IsStartElement(self: XmlReader) -> bool
        IsStartElement(self: XmlReader, name: str) -> bool
        IsStartElement(self: XmlReader, localname: str, ns: str) -> bool
        """
        ...

    def LookupNamespace(self, prefix:str) -> str:
        """ LookupNamespace(self: XmlReader, prefix: str) -> str """
        ...

    def MoveToAttribute(self, *__args:int): # -> 
        """
        MoveToAttribute(self: XmlReader, i: int)MoveToAttribute(self: XmlReader, name: str) -> bool
        MoveToAttribute(self: XmlReader, name: str, ns: str) -> bool
        """
        ...

    def MoveToContent(self): # -> XmlNodeType
        """ MoveToContent(self: XmlReader) -> XmlNodeType """
        ...

    def MoveToContentAsync(self) -> Task:
        """ MoveToContentAsync(self: XmlReader) -> Task[XmlNodeType] """
        ...

    def MoveToElement(self) -> bool:
        """ MoveToElement(self: XmlReader) -> bool """
        ...

    def MoveToFirstAttribute(self) -> bool:
        """ MoveToFirstAttribute(self: XmlReader) -> bool """
        ...

    def MoveToNextAttribute(self) -> bool:
        """ MoveToNextAttribute(self: XmlReader) -> bool """
        ...

    def Read(self) -> bool:
        """ Read(self: XmlReader) -> bool """
        ...

    def ReadAsync(self) -> Task:
        """ ReadAsync(self: XmlReader) -> Task[bool] """
        ...

    def ReadAttributeValue(self) -> bool:
        """ ReadAttributeValue(self: XmlReader) -> bool """
        ...

    def ReadContentAs(self, returnType:Type, namespaceResolver:IXmlNamespaceResolver) -> object:
        """ ReadContentAs(self: XmlReader, returnType: Type, namespaceResolver: IXmlNamespaceResolver) -> object """
        ...

    def ReadContentAsAsync(self, returnType:Type, namespaceResolver:IXmlNamespaceResolver) -> Task:
        """ ReadContentAsAsync(self: XmlReader, returnType: Type, namespaceResolver: IXmlNamespaceResolver) -> Task[object] """
        ...

    def ReadContentAsBase64(self, buffer:Array, index:int, count:int) -> int:
        """ ReadContentAsBase64(self: XmlReader, buffer: Array[Byte], index: int, count: int) -> int """
        ...

    def ReadContentAsBase64Async(self, buffer:Array, index:int, count:int) -> Task:
        """ ReadContentAsBase64Async(self: XmlReader, buffer: Array[Byte], index: int, count: int) -> Task[int] """
        ...

    def ReadContentAsBinHex(self, buffer:Array, index:int, count:int) -> int:
        """ ReadContentAsBinHex(self: XmlReader, buffer: Array[Byte], index: int, count: int) -> int """
        ...

    def ReadContentAsBinHexAsync(self, buffer:Array, index:int, count:int) -> Task:
        """ ReadContentAsBinHexAsync(self: XmlReader, buffer: Array[Byte], index: int, count: int) -> Task[int] """
        ...

    def ReadContentAsBoolean(self) -> bool:
        """ ReadContentAsBoolean(self: XmlReader) -> bool """
        ...

    def ReadContentAsDateTime(self) -> DateTime:
        """ ReadContentAsDateTime(self: XmlReader) -> DateTime """
        ...

    def ReadContentAsDateTimeOffset(self) -> DateTimeOffset:
        """ ReadContentAsDateTimeOffset(self: XmlReader) -> DateTimeOffset """
        ...

    def ReadContentAsDecimal(self) -> Decimal:
        """ ReadContentAsDecimal(self: XmlReader) -> Decimal """
        ...

    def ReadContentAsDouble(self) -> float:
        """ ReadContentAsDouble(self: XmlReader) -> float """
        ...

    def ReadContentAsFloat(self) -> Single:
        """ ReadContentAsFloat(self: XmlReader) -> Single """
        ...

    def ReadContentAsInt(self) -> int:
        """ ReadContentAsInt(self: XmlReader) -> int """
        ...

    def ReadContentAsLong(self) -> Int64:
        """ ReadContentAsLong(self: XmlReader) -> Int64 """
        ...

    def ReadContentAsObject(self) -> object:
        """ ReadContentAsObject(self: XmlReader) -> object """
        ...

    def ReadContentAsObjectAsync(self) -> Task:
        """ ReadContentAsObjectAsync(self: XmlReader) -> Task[object] """
        ...

    def ReadContentAsString(self) -> str:
        """ ReadContentAsString(self: XmlReader) -> str """
        ...

    def ReadContentAsStringAsync(self) -> Task:
        """ ReadContentAsStringAsync(self: XmlReader) -> Task[str] """
        ...

    def ReadElementContentAs(self, returnType:Type, namespaceResolver:IXmlNamespaceResolver, localName:str = ..., namespaceURI:str = ...) -> object:
        """
        ReadElementContentAs(self: XmlReader, returnType: Type, namespaceResolver: IXmlNamespaceResolver, localName: str, namespaceURI: str) -> object
        ReadElementContentAs(self: XmlReader, returnType: Type, namespaceResolver: IXmlNamespaceResolver) -> object
        """
        ...

    def ReadElementContentAsAsync(self, returnType:Type, namespaceResolver:IXmlNamespaceResolver) -> Task:
        """ ReadElementContentAsAsync(self: XmlReader, returnType: Type, namespaceResolver: IXmlNamespaceResolver) -> Task[object] """
        ...

    def ReadElementContentAsBase64(self, buffer:Array, index:int, count:int) -> int:
        """ ReadElementContentAsBase64(self: XmlReader, buffer: Array[Byte], index: int, count: int) -> int """
        ...

    def ReadElementContentAsBase64Async(self, buffer:Array, index:int, count:int) -> Task:
        """ ReadElementContentAsBase64Async(self: XmlReader, buffer: Array[Byte], index: int, count: int) -> Task[int] """
        ...

    def ReadElementContentAsBinHex(self, buffer:Array, index:int, count:int) -> int:
        """ ReadElementContentAsBinHex(self: XmlReader, buffer: Array[Byte], index: int, count: int) -> int """
        ...

    def ReadElementContentAsBinHexAsync(self, buffer:Array, index:int, count:int) -> Task:
        """ ReadElementContentAsBinHexAsync(self: XmlReader, buffer: Array[Byte], index: int, count: int) -> Task[int] """
        ...

    def ReadElementContentAsBoolean(self, localName:str = ..., namespaceURI:str = ...) -> bool:
        """
        ReadElementContentAsBoolean(self: XmlReader, localName: str, namespaceURI: str) -> bool
        ReadElementContentAsBoolean(self: XmlReader) -> bool
        """
        ...

    def ReadElementContentAsDateTime(self, localName:str = ..., namespaceURI:str = ...) -> DateTime:
        """
        ReadElementContentAsDateTime(self: XmlReader, localName: str, namespaceURI: str) -> DateTime
        ReadElementContentAsDateTime(self: XmlReader) -> DateTime
        """
        ...

    def ReadElementContentAsDecimal(self, localName:str = ..., namespaceURI:str = ...) -> Decimal:
        """
        ReadElementContentAsDecimal(self: XmlReader, localName: str, namespaceURI: str) -> Decimal
        ReadElementContentAsDecimal(self: XmlReader) -> Decimal
        """
        ...

    def ReadElementContentAsDouble(self, localName:str = ..., namespaceURI:str = ...) -> float:
        """
        ReadElementContentAsDouble(self: XmlReader, localName: str, namespaceURI: str) -> float
        ReadElementContentAsDouble(self: XmlReader) -> float
        """
        ...

    def ReadElementContentAsFloat(self, localName:str = ..., namespaceURI:str = ...) -> Single:
        """
        ReadElementContentAsFloat(self: XmlReader, localName: str, namespaceURI: str) -> Single
        ReadElementContentAsFloat(self: XmlReader) -> Single
        """
        ...

    def ReadElementContentAsInt(self, localName:str = ..., namespaceURI:str = ...) -> int:
        """
        ReadElementContentAsInt(self: XmlReader, localName: str, namespaceURI: str) -> int
        ReadElementContentAsInt(self: XmlReader) -> int
        """
        ...

    def ReadElementContentAsLong(self, localName:str = ..., namespaceURI:str = ...) -> Int64:
        """
        ReadElementContentAsLong(self: XmlReader, localName: str, namespaceURI: str) -> Int64
        ReadElementContentAsLong(self: XmlReader) -> Int64
        """
        ...

    def ReadElementContentAsObject(self, localName:str = ..., namespaceURI:str = ...) -> object:
        """
        ReadElementContentAsObject(self: XmlReader, localName: str, namespaceURI: str) -> object
        ReadElementContentAsObject(self: XmlReader) -> object
        """
        ...

    def ReadElementContentAsObjectAsync(self) -> Task:
        """ ReadElementContentAsObjectAsync(self: XmlReader) -> Task[object] """
        ...

    def ReadElementContentAsString(self, localName:str = ..., namespaceURI:str = ...) -> str:
        """
        ReadElementContentAsString(self: XmlReader, localName: str, namespaceURI: str) -> str
        ReadElementContentAsString(self: XmlReader) -> str
        """
        ...

    def ReadElementContentAsStringAsync(self) -> Task:
        """ ReadElementContentAsStringAsync(self: XmlReader) -> Task[str] """
        ...

    def ReadElementString(self, *__args:str) -> str:
        """
        ReadElementString(self: XmlReader, name: str) -> str
        ReadElementString(self: XmlReader) -> str
        ReadElementString(self: XmlReader, localname: str, ns: str) -> str
        """
        ...

    def ReadEndElement(self): # -> 
        """ ReadEndElement(self: XmlReader) """
        ...

    def ReadInnerXml(self) -> str:
        """ ReadInnerXml(self: XmlReader) -> str """
        ...

    def ReadInnerXmlAsync(self) -> Task:
        """ ReadInnerXmlAsync(self: XmlReader) -> Task[str] """
        ...

    def ReadOuterXml(self) -> str:
        """ ReadOuterXml(self: XmlReader) -> str """
        ...

    def ReadOuterXmlAsync(self) -> Task:
        """ ReadOuterXmlAsync(self: XmlReader) -> Task[str] """
        ...

    def ReadStartElement(self, *__args:str): # -> 
        """ ReadStartElement(self: XmlReader)ReadStartElement(self: XmlReader, name: str)ReadStartElement(self: XmlReader, localname: str, ns: str) """
        ...

    def ReadString(self) -> str:
        """ ReadString(self: XmlReader) -> str """
        ...

    def ReadSubtree(self) -> XmlReader:
        """ ReadSubtree(self: XmlReader) -> XmlReader """
        ...

    def ReadToDescendant(self, *__args:str) -> bool:
        """
        ReadToDescendant(self: XmlReader, name: str) -> bool
        ReadToDescendant(self: XmlReader, localName: str, namespaceURI: str) -> bool
        """
        ...

    def ReadToFollowing(self, *__args:str) -> bool:
        """
        ReadToFollowing(self: XmlReader, name: str) -> bool
        ReadToFollowing(self: XmlReader, localName: str, namespaceURI: str) -> bool
        """
        ...

    def ReadToNextSibling(self, *__args:str) -> bool:
        """
        ReadToNextSibling(self: XmlReader, name: str) -> bool
        ReadToNextSibling(self: XmlReader, localName: str, namespaceURI: str) -> bool
        """
        ...

    def ReadValueChunk(self, buffer:Array, index:int, count:int) -> int:
        """ ReadValueChunk(self: XmlReader, buffer: Array[Char], index: int, count: int) -> int """
        ...

    def ReadValueChunkAsync(self, buffer:Array, index:int, count:int) -> Task:
        """ ReadValueChunkAsync(self: XmlReader, buffer: Array[Char], index: int, count: int) -> Task[int] """
        ...

    def ResolveEntity(self): # -> 
        """ ResolveEntity(self: XmlReader) """
        ...

    def Skip(self): # -> 
        """ Skip(self: XmlReader) """
        ...

    def SkipAsync(self) -> Task:
        """ SkipAsync(self: XmlReader) -> Task """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class XmlDictionaryReader(XmlReader): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def CanCanonicalize(self) -> bool:
        """ Get: CanCanonicalize(self: XmlDictionaryReader) -> bool """
        ...

    @property
    def Quotas(self): # -> XmlDictionaryReaderQuotas
        """ Get: Quotas(self: XmlDictionaryReader) -> XmlDictionaryReaderQuotas """
        ...


    @staticmethod
    def CreateBinaryReader(*__args) -> XmlDictionaryReader:
        """
        CreateBinaryReader(buffer: Array[Byte], quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateBinaryReader(buffer: Array[Byte], offset: int, count: int, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateBinaryReader(buffer: Array[Byte], offset: int, count: int, dictionary: IXmlDictionary, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateBinaryReader(buffer: Array[Byte], offset: int, count: int, dictionary: IXmlDictionary, quotas: XmlDictionaryReaderQuotas, session: XmlBinaryReaderSession) -> XmlDictionaryReader
        CreateBinaryReader(buffer: Array[Byte], offset: int, count: int, dictionary: IXmlDictionary, quotas: XmlDictionaryReaderQuotas, session: XmlBinaryReaderSession, onClose: OnXmlDictionaryReaderClose) -> XmlDictionaryReader
        CreateBinaryReader(stream: Stream, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateBinaryReader(stream: Stream, dictionary: IXmlDictionary, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateBinaryReader(stream: Stream, dictionary: IXmlDictionary, quotas: XmlDictionaryReaderQuotas, session: XmlBinaryReaderSession) -> XmlDictionaryReader
        CreateBinaryReader(stream: Stream, dictionary: IXmlDictionary, quotas: XmlDictionaryReaderQuotas, session: XmlBinaryReaderSession, onClose: OnXmlDictionaryReaderClose) -> XmlDictionaryReader
        """
        ...

    @staticmethod
    def CreateDictionaryReader(reader:XmlReader) -> XmlDictionaryReader:
        """ CreateDictionaryReader(reader: XmlReader) -> XmlDictionaryReader """
        ...

    @staticmethod
    def CreateMtomReader(*__args) -> XmlDictionaryReader:
        """
        CreateMtomReader(stream: Stream, encoding: Encoding, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateMtomReader(stream: Stream, encodings: Array[Encoding], quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateMtomReader(stream: Stream, encodings: Array[Encoding], contentType: str, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateMtomReader(stream: Stream, encodings: Array[Encoding], contentType: str, quotas: XmlDictionaryReaderQuotas, maxBufferSize: int, onClose: OnXmlDictionaryReaderClose) -> XmlDictionaryReader
        CreateMtomReader(buffer: Array[Byte], offset: int, count: int, encoding: Encoding, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateMtomReader(buffer: Array[Byte], offset: int, count: int, encodings: Array[Encoding], quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateMtomReader(buffer: Array[Byte], offset: int, count: int, encodings: Array[Encoding], contentType: str, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateMtomReader(buffer: Array[Byte], offset: int, count: int, encodings: Array[Encoding], contentType: str, quotas: XmlDictionaryReaderQuotas, maxBufferSize: int, onClose: OnXmlDictionaryReaderClose) -> XmlDictionaryReader
        """
        ...

    @staticmethod
    def CreateTextReader(*__args) -> XmlDictionaryReader:
        """
        CreateTextReader(buffer: Array[Byte], quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateTextReader(buffer: Array[Byte], offset: int, count: int, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateTextReader(buffer: Array[Byte], offset: int, count: int, encoding: Encoding, quotas: XmlDictionaryReaderQuotas, onClose: OnXmlDictionaryReaderClose) -> XmlDictionaryReader
        CreateTextReader(stream: Stream, quotas: XmlDictionaryReaderQuotas) -> XmlDictionaryReader
        CreateTextReader(stream: Stream, encoding: Encoding, quotas: XmlDictionaryReaderQuotas, onClose: OnXmlDictionaryReaderClose) -> XmlDictionaryReader
        """
        ...

    def EndCanonicalization(self): # -> 
        """ EndCanonicalization(self: XmlDictionaryReader) """
        ...

    def GetNonAtomizedNames(self, localName, namespaceUri) -> Tuple_[str, str]:
        """ GetNonAtomizedNames(self: XmlDictionaryReader) -> (str, str) """
        ...

    def IndexOfLocalName(self, localNames:Array, namespaceUri:str) -> int:
        """
        IndexOfLocalName(self: XmlDictionaryReader, localNames: Array[str], namespaceUri: str) -> int
        IndexOfLocalName(self: XmlDictionaryReader, localNames: Array[XmlDictionaryString], namespaceUri: XmlDictionaryString) -> int
        """
        ...

    def IsLocalName(self, localName:str) -> bool:
        """
        IsLocalName(self: XmlDictionaryReader, localName: str) -> bool
        IsLocalName(self: XmlDictionaryReader, localName: XmlDictionaryString) -> bool
        """
        ...

    def IsNamespaceUri(self, namespaceUri:str) -> bool:
        """
        IsNamespaceUri(self: XmlDictionaryReader, namespaceUri: str) -> bool
        IsNamespaceUri(self: XmlDictionaryReader, namespaceUri: XmlDictionaryString) -> bool
        """
        ...

    def IsStartArray(self, type) -> Tuple_[bool, Type]:
        """ IsStartArray(self: XmlDictionaryReader) -> (bool, Type) """
        ...

    def IsTextNode(self, *args): #cannot find CLR method
        """ IsTextNode(self: XmlDictionaryReader, nodeType: XmlNodeType) -> bool """
        ...

    def MoveToStartElement(self, *__args:str): # -> 
        """ MoveToStartElement(self: XmlDictionaryReader)MoveToStartElement(self: XmlDictionaryReader, name: str)MoveToStartElement(self: XmlDictionaryReader, localName: str, namespaceUri: str)MoveToStartElement(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) """
        ...

    def ReadArray(self, localName:str, namespaceUri:str, array:Array, offset:int, count:int) -> int:
        """
        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[bool], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Guid], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[Guid], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[DateTime], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[DateTime], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Decimal], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[Decimal], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[float], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[float], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Single], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[Single], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Int64], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[Int64], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[int], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[int], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Int16], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[Int16], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[bool], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: str, namespaceUri: str, array: Array[TimeSpan], offset: int, count: int) -> int
        ReadArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[TimeSpan], offset: int, count: int) -> int
        """
        ...

    def ReadBooleanArray(self, localName:str, namespaceUri:str) -> Array:
        """
        ReadBooleanArray(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[bool]
        ReadBooleanArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[bool]
        """
        ...

    def ReadContentAsChars(self, chars:Array, offset:int, count:int) -> int:
        """ ReadContentAsChars(self: XmlDictionaryReader, chars: Array[Char], offset: int, count: int) -> int """
        ...

    def ReadContentAsGuid(self) -> Guid:
        """ ReadContentAsGuid(self: XmlDictionaryReader) -> Guid """
        ...

    def ReadContentAsQualifiedName(self, localName, namespaceUri) -> Tuple_[str, str]:
        """ ReadContentAsQualifiedName(self: XmlDictionaryReader) -> (str, str) """
        ...

    def ReadContentAsTimeSpan(self) -> TimeSpan:
        """ ReadContentAsTimeSpan(self: XmlDictionaryReader) -> TimeSpan """
        ...

    def ReadContentAsUniqueId(self) -> UniqueId:
        """ ReadContentAsUniqueId(self: XmlDictionaryReader) -> UniqueId """
        ...

    def ReadDateTimeArray(self, localName:str, namespaceUri:str) -> Array:
        """
        ReadDateTimeArray(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[DateTime]
        ReadDateTimeArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[DateTime]
        """
        ...

    def ReadDecimalArray(self, localName:str, namespaceUri:str) -> Array:
        """
        ReadDecimalArray(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[Decimal]
        ReadDecimalArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[Decimal]
        """
        ...

    def ReadDoubleArray(self, localName:str, namespaceUri:str) -> Array:
        """
        ReadDoubleArray(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[float]
        ReadDoubleArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[float]
        """
        ...

    def ReadElementContentAsGuid(self) -> Guid:
        """ ReadElementContentAsGuid(self: XmlDictionaryReader) -> Guid """
        ...

    def ReadElementContentAsTimeSpan(self) -> TimeSpan:
        """ ReadElementContentAsTimeSpan(self: XmlDictionaryReader) -> TimeSpan """
        ...

    def ReadElementContentAsUniqueId(self) -> UniqueId:
        """ ReadElementContentAsUniqueId(self: XmlDictionaryReader) -> UniqueId """
        ...

    def ReadFullStartElement(self, *__args:str): # -> 
        """ ReadFullStartElement(self: XmlDictionaryReader)ReadFullStartElement(self: XmlDictionaryReader, name: str)ReadFullStartElement(self: XmlDictionaryReader, localName: str, namespaceUri: str)ReadFullStartElement(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) """
        ...

    def ReadGuidArray(self, localName:str, namespaceUri:str) -> Array:
        """
        ReadGuidArray(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[Guid]
        ReadGuidArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[Guid]
        """
        ...

    def ReadInt16Array(self, localName:str, namespaceUri:str) -> Array:
        """
        ReadInt16Array(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[Int16]
        ReadInt16Array(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[Int16]
        """
        ...

    def ReadInt32Array(self, localName:str, namespaceUri:str) -> Array:
        """
        ReadInt32Array(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[int]
        ReadInt32Array(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[int]
        """
        ...

    def ReadInt64Array(self, localName:str, namespaceUri:str) -> Array:
        """
        ReadInt64Array(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[Int64]
        ReadInt64Array(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[Int64]
        """
        ...

    def ReadSingleArray(self, localName:str, namespaceUri:str) -> Array:
        """
        ReadSingleArray(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[Single]
        ReadSingleArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[Single]
        """
        ...

    def ReadTimeSpanArray(self, localName:str, namespaceUri:str) -> Array:
        """
        ReadTimeSpanArray(self: XmlDictionaryReader, localName: str, namespaceUri: str) -> Array[TimeSpan]
        ReadTimeSpanArray(self: XmlDictionaryReader, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString) -> Array[TimeSpan]
        """
        ...

    def ReadValueAsBase64(self, buffer:Array, offset:int, count:int) -> int:
        """ ReadValueAsBase64(self: XmlDictionaryReader, buffer: Array[Byte], offset: int, count: int) -> int """
        ...

    def StartCanonicalization(self, stream:Stream, includeComments:bool, inclusivePrefixes:Array): # -> 
        """ StartCanonicalization(self: XmlDictionaryReader, stream: Stream, includeComments: bool, inclusivePrefixes: Array[str]) """
        ...

    def TryGetArrayLength(self, count) -> Tuple_[bool, int]:
        """ TryGetArrayLength(self: XmlDictionaryReader) -> (bool, int) """
        ...

    def TryGetBase64ContentLength(self, length) -> Tuple_[bool, int]:
        """ TryGetBase64ContentLength(self: XmlDictionaryReader) -> (bool, int) """
        ...

    def TryGetLocalNameAsDictionaryString(self, localName): # -> Tuple_[bool, XmlDictionaryString]
        """ TryGetLocalNameAsDictionaryString(self: XmlDictionaryReader) -> (bool, XmlDictionaryString) """
        ...

    def TryGetNamespaceUriAsDictionaryString(self, namespaceUri): # -> Tuple_[bool, XmlDictionaryString]
        """ TryGetNamespaceUriAsDictionaryString(self: XmlDictionaryReader) -> (bool, XmlDictionaryString) """
        ...

    def TryGetValueAsDictionaryString(self, value): # -> Tuple_[bool, XmlDictionaryString]
        """ TryGetValueAsDictionaryString(self: XmlDictionaryReader) -> (bool, XmlDictionaryString) """
        ...


class XmlDictionaryReaderQuotas: # skipped bases: <type 'object'>, <type 'object'>
    """ XmlDictionaryReaderQuotas() """
    @property
    def Max(self) -> XmlDictionaryReaderQuotas:
        """ Get: Max() -> XmlDictionaryReaderQuotas """
        ...

    @property
    def MaxArrayLength(self) -> int:
        """
        Get: MaxArrayLength(self: XmlDictionaryReaderQuotas) -> int
        Set: MaxArrayLength(self: XmlDictionaryReaderQuotas) = value
        """
        ...

    @property
    def MaxBytesPerRead(self) -> int:
        """
        Get: MaxBytesPerRead(self: XmlDictionaryReaderQuotas) -> int
        Set: MaxBytesPerRead(self: XmlDictionaryReaderQuotas) = value
        """
        ...

    @property
    def MaxDepth(self) -> int:
        """
        Get: MaxDepth(self: XmlDictionaryReaderQuotas) -> int
        Set: MaxDepth(self: XmlDictionaryReaderQuotas) = value
        """
        ...

    @property
    def MaxNameTableCharCount(self) -> int:
        """
        Get: MaxNameTableCharCount(self: XmlDictionaryReaderQuotas) -> int
        Set: MaxNameTableCharCount(self: XmlDictionaryReaderQuotas) = value
        """
        ...

    @property
    def MaxStringContentLength(self) -> int:
        """
        Get: MaxStringContentLength(self: XmlDictionaryReaderQuotas) -> int
        Set: MaxStringContentLength(self: XmlDictionaryReaderQuotas) = value
        """
        ...

    @property
    def ModifiedQuotas(self): # -> XmlDictionaryReaderQuotaTypes
        """ Get: ModifiedQuotas(self: XmlDictionaryReaderQuotas) -> XmlDictionaryReaderQuotaTypes """
        ...


    def CopyTo(self, quotas:XmlDictionaryReaderQuotas): # -> 
        """ CopyTo(self: XmlDictionaryReaderQuotas, quotas: XmlDictionaryReaderQuotas) """
        ...



class XmlDictionaryReaderQuotaTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) XmlDictionaryReaderQuotaTypes, values: MaxArrayLength (4), MaxBytesPerRead (8), MaxDepth (1), MaxNameTableCharCount (16), MaxStringContentLength (2) """
    MaxArrayLength: XmlDictionaryReaderQuotaTypes = ...
    MaxBytesPerRead: XmlDictionaryReaderQuotaTypes = ...
    MaxDepth: XmlDictionaryReaderQuotaTypes = ...
    MaxNameTableCharCount: XmlDictionaryReaderQuotaTypes = ...
    MaxStringContentLength: XmlDictionaryReaderQuotaTypes = ...
    value__ = ...


class XmlDictionaryString: # skipped bases: <type 'object'>, <type 'object'>
    """ XmlDictionaryString(dictionary: IXmlDictionary, value: str, key: int) """
    @property
    def Dictionary(self) -> IXmlDictionary:
        """ Get: Dictionary(self: XmlDictionaryString) -> IXmlDictionary """
        ...

    @property
    def Empty(self) -> XmlDictionaryString:
        """ Get: Empty() -> XmlDictionaryString """
        ...

    @property
    def Key(self) -> int:
        """ Get: Key(self: XmlDictionaryString) -> int """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: XmlDictionaryString) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: XmlDictionaryString) -> str """
        ...



class XmlWriter(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Settings(self): # -> XmlWriterSettings
        """ Get: Settings(self: XmlWriter) -> XmlWriterSettings """
        ...

    @property
    def WriteState(self) -> WriteState:
        """ Get: WriteState(self: XmlWriter) -> WriteState """
        ...

    @property
    def XmlLang(self) -> str:
        """ Get: XmlLang(self: XmlWriter) -> str """
        ...

    @property
    def XmlSpace(self): # -> XmlSpace
        """ Get: XmlSpace(self: XmlWriter) -> XmlSpace """
        ...


    def Close(self): # -> 
        """ Close(self: XmlWriter) """
        ...

    @staticmethod
    def Create(*__args:str) -> XmlWriter:
        """
        Create(outputFileName: str) -> XmlWriter
        Create(outputFileName: str, settings: XmlWriterSettings) -> XmlWriter
        Create(output: Stream) -> XmlWriter
        Create(output: Stream, settings: XmlWriterSettings) -> XmlWriter
        Create(output: TextWriter) -> XmlWriter
        Create(output: TextWriter, settings: XmlWriterSettings) -> XmlWriter
        Create(output: StringBuilder) -> XmlWriter
        Create(output: StringBuilder, settings: XmlWriterSettings) -> XmlWriter
        Create(output: XmlWriter) -> XmlWriter
        Create(output: XmlWriter, settings: XmlWriterSettings) -> XmlWriter
        """
        ...

    def Flush(self): # -> 
        """ Flush(self: XmlWriter) """
        ...

    def FlushAsync(self) -> Task:
        """ FlushAsync(self: XmlWriter) -> Task """
        ...

    def LookupPrefix(self, ns:str) -> str:
        """ LookupPrefix(self: XmlWriter, ns: str) -> str """
        ...

    def WriteAttributes(self, reader:XmlReader, defattr:bool): # -> 
        """ WriteAttributes(self: XmlWriter, reader: XmlReader, defattr: bool) """
        ...

    def WriteAttributesAsync(self, reader:XmlReader, defattr:bool) -> Task:
        """ WriteAttributesAsync(self: XmlWriter, reader: XmlReader, defattr: bool) -> Task """
        ...

    def WriteAttributeString(self, *__args): # -> 
        """ WriteAttributeString(self: XmlWriter, localName: str, ns: str, value: str)WriteAttributeString(self: XmlWriter, localName: str, value: str)WriteAttributeString(self: XmlWriter, prefix: str, localName: str, ns: str, value: str) """
        ...

    def WriteAttributeStringAsync(self, prefix:str, localName:str, ns:str, value:str) -> Task:
        """ WriteAttributeStringAsync(self: XmlWriter, prefix: str, localName: str, ns: str, value: str) -> Task """
        ...

    def WriteBase64(self, buffer:Array, index:int, count:int): # -> 
        """ WriteBase64(self: XmlWriter, buffer: Array[Byte], index: int, count: int) """
        ...

    def WriteBase64Async(self, buffer:Array, index:int, count:int) -> Task:
        """ WriteBase64Async(self: XmlWriter, buffer: Array[Byte], index: int, count: int) -> Task """
        ...

    def WriteBinHex(self, buffer:Array, index:int, count:int): # -> 
        """ WriteBinHex(self: XmlWriter, buffer: Array[Byte], index: int, count: int) """
        ...

    def WriteBinHexAsync(self, buffer:Array, index:int, count:int) -> Task:
        """ WriteBinHexAsync(self: XmlWriter, buffer: Array[Byte], index: int, count: int) -> Task """
        ...

    def WriteCData(self, text:str): # -> 
        """ WriteCData(self: XmlWriter, text: str) """
        ...

    def WriteCDataAsync(self, text:str) -> Task:
        """ WriteCDataAsync(self: XmlWriter, text: str) -> Task """
        ...

    def WriteCharEntity(self, ch:Char): # -> 
        """ WriteCharEntity(self: XmlWriter, ch: Char) """
        ...

    def WriteCharEntityAsync(self, ch:Char) -> Task:
        """ WriteCharEntityAsync(self: XmlWriter, ch: Char) -> Task """
        ...

    def WriteChars(self, buffer:Array, index:int, count:int): # -> 
        """ WriteChars(self: XmlWriter, buffer: Array[Char], index: int, count: int) """
        ...

    def WriteCharsAsync(self, buffer:Array, index:int, count:int) -> Task:
        """ WriteCharsAsync(self: XmlWriter, buffer: Array[Char], index: int, count: int) -> Task """
        ...

    def WriteComment(self, text:str): # -> 
        """ WriteComment(self: XmlWriter, text: str) """
        ...

    def WriteCommentAsync(self, text:str) -> Task:
        """ WriteCommentAsync(self: XmlWriter, text: str) -> Task """
        ...

    def WriteDocType(self, name:str, pubid:str, sysid:str, subset:str): # -> 
        """ WriteDocType(self: XmlWriter, name: str, pubid: str, sysid: str, subset: str) """
        ...

    def WriteDocTypeAsync(self, name:str, pubid:str, sysid:str, subset:str) -> Task:
        """ WriteDocTypeAsync(self: XmlWriter, name: str, pubid: str, sysid: str, subset: str) -> Task """
        ...

    def WriteElementString(self, *__args): # -> 
        """ WriteElementString(self: XmlWriter, localName: str, value: str)WriteElementString(self: XmlWriter, localName: str, ns: str, value: str)WriteElementString(self: XmlWriter, prefix: str, localName: str, ns: str, value: str) """
        ...

    def WriteElementStringAsync(self, prefix:str, localName:str, ns:str, value:str) -> Task:
        """ WriteElementStringAsync(self: XmlWriter, prefix: str, localName: str, ns: str, value: str) -> Task """
        ...

    def WriteEndAttribute(self): # -> 
        """ WriteEndAttribute(self: XmlWriter) """
        ...

    def WriteEndAttributeAsync(self, *args): #cannot find CLR method
        """ WriteEndAttributeAsync(self: XmlWriter) -> Task """
        ...

    def WriteEndDocument(self): # -> 
        """ WriteEndDocument(self: XmlWriter) """
        ...

    def WriteEndDocumentAsync(self) -> Task:
        """ WriteEndDocumentAsync(self: XmlWriter) -> Task """
        ...

    def WriteEndElement(self): # -> 
        """ WriteEndElement(self: XmlWriter) """
        ...

    def WriteEndElementAsync(self) -> Task:
        """ WriteEndElementAsync(self: XmlWriter) -> Task """
        ...

    def WriteEntityRef(self, name:str): # -> 
        """ WriteEntityRef(self: XmlWriter, name: str) """
        ...

    def WriteEntityRefAsync(self, name:str) -> Task:
        """ WriteEntityRefAsync(self: XmlWriter, name: str) -> Task """
        ...

    def WriteFullEndElement(self): # -> 
        """ WriteFullEndElement(self: XmlWriter) """
        ...

    def WriteFullEndElementAsync(self) -> Task:
        """ WriteFullEndElementAsync(self: XmlWriter) -> Task """
        ...

    def WriteName(self, name:str): # -> 
        """ WriteName(self: XmlWriter, name: str) """
        ...

    def WriteNameAsync(self, name:str) -> Task:
        """ WriteNameAsync(self: XmlWriter, name: str) -> Task """
        ...

    def WriteNmToken(self, name:str): # -> 
        """ WriteNmToken(self: XmlWriter, name: str) """
        ...

    def WriteNmTokenAsync(self, name:str) -> Task:
        """ WriteNmTokenAsync(self: XmlWriter, name: str) -> Task """
        ...

    def WriteNode(self, *__args): # -> 
        """ WriteNode(self: XmlWriter, navigator: XPathNavigator, defattr: bool)WriteNode(self: XmlWriter, reader: XmlReader, defattr: bool) """
        ...

    def WriteNodeAsync(self, *__args) -> Task:
        """
        WriteNodeAsync(self: XmlWriter, reader: XmlReader, defattr: bool) -> Task
        WriteNodeAsync(self: XmlWriter, navigator: XPathNavigator, defattr: bool) -> Task
        """
        ...

    def WriteProcessingInstruction(self, name:str, text:str): # -> 
        """ WriteProcessingInstruction(self: XmlWriter, name: str, text: str) """
        ...

    def WriteProcessingInstructionAsync(self, name:str, text:str) -> Task:
        """ WriteProcessingInstructionAsync(self: XmlWriter, name: str, text: str) -> Task """
        ...

    def WriteQualifiedName(self, localName:str, ns:str): # -> 
        """ WriteQualifiedName(self: XmlWriter, localName: str, ns: str) """
        ...

    def WriteQualifiedNameAsync(self, localName:str, ns:str) -> Task:
        """ WriteQualifiedNameAsync(self: XmlWriter, localName: str, ns: str) -> Task """
        ...

    def WriteRaw(self, *__args:str): # -> 
        """ WriteRaw(self: XmlWriter, buffer: Array[Char], index: int, count: int)WriteRaw(self: XmlWriter, data: str) """
        ...

    def WriteRawAsync(self, *__args:str) -> Task:
        """
        WriteRawAsync(self: XmlWriter, buffer: Array[Char], index: int, count: int) -> Task
        WriteRawAsync(self: XmlWriter, data: str) -> Task
        """
        ...

    def WriteStartAttribute(self, *__args:str): # -> 
        """ WriteStartAttribute(self: XmlWriter, localName: str, ns: str)WriteStartAttribute(self: XmlWriter, localName: str)WriteStartAttribute(self: XmlWriter, prefix: str, localName: str, ns: str) """
        ...

    def WriteStartAttributeAsync(self, *args): #cannot find CLR method
        """ WriteStartAttributeAsync(self: XmlWriter, prefix: str, localName: str, ns: str) -> Task """
        ...

    def WriteStartDocument(self, standalone:bool = ...): # -> 
        """ WriteStartDocument(self: XmlWriter)WriteStartDocument(self: XmlWriter, standalone: bool) """
        ...

    def WriteStartDocumentAsync(self, standalone:bool = ...) -> Task:
        """
        WriteStartDocumentAsync(self: XmlWriter) -> Task
        WriteStartDocumentAsync(self: XmlWriter, standalone: bool) -> Task
        """
        ...

    def WriteStartElement(self, *__args:str): # -> 
        """ WriteStartElement(self: XmlWriter, localName: str, ns: str)WriteStartElement(self: XmlWriter, localName: str)WriteStartElement(self: XmlWriter, prefix: str, localName: str, ns: str) """
        ...

    def WriteStartElementAsync(self, prefix:str, localName:str, ns:str) -> Task:
        """ WriteStartElementAsync(self: XmlWriter, prefix: str, localName: str, ns: str) -> Task """
        ...

    def WriteString(self, text:str): # -> 
        """ WriteString(self: XmlWriter, text: str) """
        ...

    def WriteStringAsync(self, text:str) -> Task:
        """ WriteStringAsync(self: XmlWriter, text: str) -> Task """
        ...

    def WriteSurrogateCharEntity(self, lowChar:Char, highChar:Char): # -> 
        """ WriteSurrogateCharEntity(self: XmlWriter, lowChar: Char, highChar: Char) """
        ...

    def WriteSurrogateCharEntityAsync(self, lowChar:Char, highChar:Char) -> Task:
        """ WriteSurrogateCharEntityAsync(self: XmlWriter, lowChar: Char, highChar: Char) -> Task """
        ...

    def WriteValue(self, value:object): # -> 
        """ WriteValue(self: XmlWriter, value: object)WriteValue(self: XmlWriter, value: str)WriteValue(self: XmlWriter, value: DateTime)WriteValue(self: XmlWriter, value: DateTimeOffset)WriteValue(self: XmlWriter, value: float)WriteValue(self: XmlWriter, value: Single)WriteValue(self: XmlWriter, value: Decimal)WriteValue(self: XmlWriter, value: int)WriteValue(self: XmlWriter, value: Int64)WriteValue(self: XmlWriter, value: bool) """
        ...

    def WriteWhitespace(self, ws:str): # -> 
        """ WriteWhitespace(self: XmlWriter, ws: str) """
        ...

    def WriteWhitespaceAsync(self, ws:str) -> Task:
        """ WriteWhitespaceAsync(self: XmlWriter, ws: str) -> Task """
        ...


class XmlDictionaryWriter(XmlWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def CanCanonicalize(self) -> bool:
        """ Get: CanCanonicalize(self: XmlDictionaryWriter) -> bool """
        ...


    @staticmethod
    def CreateBinaryWriter(stream:Stream, dictionary:IXmlDictionary = ..., session:XmlBinaryWriterSession = ..., ownsStream:bool = ...) -> XmlDictionaryWriter:
        """
        CreateBinaryWriter(stream: Stream) -> XmlDictionaryWriter
        CreateBinaryWriter(stream: Stream, dictionary: IXmlDictionary) -> XmlDictionaryWriter
        CreateBinaryWriter(stream: Stream, dictionary: IXmlDictionary, session: XmlBinaryWriterSession) -> XmlDictionaryWriter
        CreateBinaryWriter(stream: Stream, dictionary: IXmlDictionary, session: XmlBinaryWriterSession, ownsStream: bool) -> XmlDictionaryWriter
        """
        ...

    @staticmethod
    def CreateDictionaryWriter(writer:XmlWriter) -> XmlDictionaryWriter:
        """ CreateDictionaryWriter(writer: XmlWriter) -> XmlDictionaryWriter """
        ...

    @staticmethod
    def CreateMtomWriter(stream:Stream, encoding:Encoding, maxSizeInBytes:int, startInfo:str, boundary:str = ..., startUri:str = ..., writeMessageHeaders:bool = ..., ownsStream:bool = ...) -> XmlDictionaryWriter:
        """
        CreateMtomWriter(stream: Stream, encoding: Encoding, maxSizeInBytes: int, startInfo: str) -> XmlDictionaryWriter
        CreateMtomWriter(stream: Stream, encoding: Encoding, maxSizeInBytes: int, startInfo: str, boundary: str, startUri: str, writeMessageHeaders: bool, ownsStream: bool) -> XmlDictionaryWriter
        """
        ...

    @staticmethod
    def CreateTextWriter(stream:Stream, encoding:Encoding = ..., ownsStream:bool = ...) -> XmlDictionaryWriter:
        """
        CreateTextWriter(stream: Stream) -> XmlDictionaryWriter
        CreateTextWriter(stream: Stream, encoding: Encoding) -> XmlDictionaryWriter
        CreateTextWriter(stream: Stream, encoding: Encoding, ownsStream: bool) -> XmlDictionaryWriter
        """
        ...

    def EndCanonicalization(self): # -> 
        """ EndCanonicalization(self: XmlDictionaryWriter) """
        ...

    def StartCanonicalization(self, stream:Stream, includeComments:bool, inclusivePrefixes:Array): # -> 
        """ StartCanonicalization(self: XmlDictionaryWriter, stream: Stream, includeComments: bool, inclusivePrefixes: Array[str]) """
        ...

    def WriteArray(self, prefix:str, localName:str, namespaceUri:str, array:Array, offset:int, count:int): # -> 
        """ WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[bool], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Guid], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[Guid], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[DateTime], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[DateTime], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Decimal], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[Decimal], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[float], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[float], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Single], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[Single], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Int64], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[Int64], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[int], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[int], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[Int16], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[Int16], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[bool], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: str, namespaceUri: str, array: Array[TimeSpan], offset: int, count: int)WriteArray(self: XmlDictionaryWriter, prefix: str, localName: XmlDictionaryString, namespaceUri: XmlDictionaryString, array: Array[TimeSpan], offset: int, count: int) """
        ...

    def WriteTextNode(self, *args): #cannot find CLR method
        """ WriteTextNode(self: XmlDictionaryWriter, reader: XmlDictionaryReader, isAttribute: bool) """
        ...

    def WriteValueAsync(self, value:IStreamProvider) -> Task:
        """ WriteValueAsync(self: XmlDictionaryWriter, value: IStreamProvider) -> Task """
        ...

    def WriteXmlAttribute(self, localName:str, value:str): # -> 
        """ WriteXmlAttribute(self: XmlDictionaryWriter, localName: str, value: str)WriteXmlAttribute(self: XmlDictionaryWriter, localName: XmlDictionaryString, value: XmlDictionaryString) """
        ...

    def WriteXmlnsAttribute(self, prefix:str, namespaceUri:str): # -> 
        """ WriteXmlnsAttribute(self: XmlDictionaryWriter, prefix: str, namespaceUri: str)WriteXmlnsAttribute(self: XmlDictionaryWriter, prefix: str, namespaceUri: XmlDictionaryString) """
        ...


class XmlDocumentFragment(XmlNode): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, ownerDocument: XmlDocument) """
        ...


class XmlDocumentType(XmlLinkedNode): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    @property
    def Entities(self) -> XmlNamedNodeMap:
        """ Get: Entities(self: XmlDocumentType) -> XmlNamedNodeMap """
        ...

    @property
    def InternalSubset(self) -> str:
        """ Get: InternalSubset(self: XmlDocumentType) -> str """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: XmlDocumentType) -> bool """
        ...

    @property
    def LocalName(self) -> str:
        """ Get: LocalName(self: XmlDocumentType) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlDocumentType) -> str """
        ...

    @property
    def NodeType(self): # -> XmlNodeType
        """ Get: NodeType(self: XmlDocumentType) -> XmlNodeType """
        ...

    @property
    def Notations(self) -> XmlNamedNodeMap:
        """ Get: Notations(self: XmlDocumentType) -> XmlNamedNodeMap """
        ...

    @property
    def PublicId(self) -> str:
        """ Get: PublicId(self: XmlDocumentType) -> str """
        ...

    @property
    def SystemId(self) -> str:
        """ Get: SystemId(self: XmlDocumentType) -> str """
        ...


    def CloneNode(self, deep:bool) -> XmlNode:
        """ CloneNode(self: XmlDocumentType, deep: bool) -> XmlNode """
        ...

    def WriteContentTo(self, w:XmlWriter): # -> 
        """ WriteContentTo(self: XmlDocumentType, w: XmlWriter) """
        ...

    def WriteTo(self, w:XmlWriter): # -> 
        """ WriteTo(self: XmlDocumentType, w: XmlWriter) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, name: str, publicId: str, systemId: str, internalSubset: str, doc: XmlDocument) """
        ...


class XmlElement(XmlLinkedNode): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> XmlAttributeCollection:
        """ Get: Attributes(self: XmlElement) -> XmlAttributeCollection """
        ...

    @property
    def HasAttributes(self) -> bool:
        """ Get: HasAttributes(self: XmlElement) -> bool """
        ...

    @property
    def InnerText(self) -> str:
        """
        Get: InnerText(self: XmlElement) -> str
        Set: InnerText(self: XmlElement) = value
        """
        ...

    @property
    def InnerXml(self) -> str:
        """
        Get: InnerXml(self: XmlElement) -> str
        Set: InnerXml(self: XmlElement) = value
        """
        ...

    @property
    def IsEmpty(self) -> bool:
        """
        Get: IsEmpty(self: XmlElement) -> bool
        Set: IsEmpty(self: XmlElement) = value
        """
        ...

    @property
    def LocalName(self) -> str:
        """ Get: LocalName(self: XmlElement) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlElement) -> str """
        ...

    @property
    def NamespaceURI(self) -> str:
        """ Get: NamespaceURI(self: XmlElement) -> str """
        ...

    @property
    def NodeType(self): # -> XmlNodeType
        """ Get: NodeType(self: XmlElement) -> XmlNodeType """
        ...

    @property
    def OwnerDocument(self) -> XmlDocument:
        """ Get: OwnerDocument(self: XmlElement) -> XmlDocument """
        ...

    @property
    def ParentNode(self) -> XmlNode:
        """ Get: ParentNode(self: XmlElement) -> XmlNode """
        ...

    @property
    def Prefix(self) -> str:
        """
        Get: Prefix(self: XmlElement) -> str
        Set: Prefix(self: XmlElement) = value
        """
        ...

    @property
    def SchemaInfo(self) -> IXmlSchemaInfo:
        """ Get: SchemaInfo(self: XmlElement) -> IXmlSchemaInfo """
        ...


    def CloneNode(self, deep:bool) -> XmlNode:
        """ CloneNode(self: XmlElement, deep: bool) -> XmlNode """
        ...

    def GetAttribute(self, *__args:str) -> str:
        """
        GetAttribute(self: XmlElement, name: str) -> str
        GetAttribute(self: XmlElement, localName: str, namespaceURI: str) -> str
        """
        ...

    def GetAttributeNode(self, *__args:str) -> XmlAttribute:
        """
        GetAttributeNode(self: XmlElement, name: str) -> XmlAttribute
        GetAttributeNode(self: XmlElement, localName: str, namespaceURI: str) -> XmlAttribute
        """
        ...

    def GetElementsByTagName(self, *__args:str): # -> XmlNodeList
        """
        GetElementsByTagName(self: XmlElement, name: str) -> XmlNodeList
        GetElementsByTagName(self: XmlElement, localName: str, namespaceURI: str) -> XmlNodeList
        """
        ...

    def HasAttribute(self, *__args:str) -> bool:
        """
        HasAttribute(self: XmlElement, name: str) -> bool
        HasAttribute(self: XmlElement, localName: str, namespaceURI: str) -> bool
        """
        ...

    def RemoveAll(self): # -> 
        """ RemoveAll(self: XmlElement) """
        ...

    def RemoveAllAttributes(self): # -> 
        """ RemoveAllAttributes(self: XmlElement) """
        ...

    def RemoveAttribute(self, *__args:str): # -> 
        """ RemoveAttribute(self: XmlElement, name: str)RemoveAttribute(self: XmlElement, localName: str, namespaceURI: str) """
        ...

    def RemoveAttributeAt(self, i:int) -> XmlNode:
        """ RemoveAttributeAt(self: XmlElement, i: int) -> XmlNode """
        ...

    def RemoveAttributeNode(self, *__args:XmlAttribute) -> XmlAttribute:
        """
        RemoveAttributeNode(self: XmlElement, oldAttr: XmlAttribute) -> XmlAttribute
        RemoveAttributeNode(self: XmlElement, localName: str, namespaceURI: str) -> XmlAttribute
        """
        ...

    def SetAttribute(self, *__args): # -> 
        """ SetAttribute(self: XmlElement, name: str, value: str)SetAttribute(self: XmlElement, localName: str, namespaceURI: str, value: str) -> str """
        ...

    def SetAttributeNode(self, *__args:XmlAttribute) -> XmlAttribute:
        """
        SetAttributeNode(self: XmlElement, newAttr: XmlAttribute) -> XmlAttribute
        SetAttributeNode(self: XmlElement, localName: str, namespaceURI: str) -> XmlAttribute
        """
        ...

    def WriteContentTo(self, w:XmlWriter): # -> 
        """ WriteContentTo(self: XmlElement, w: XmlWriter) """
        ...

    def WriteTo(self, w:XmlWriter): # -> 
        """ WriteTo(self: XmlElement, w: XmlWriter) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, prefix: str, localName: str, namespaceURI: str, doc: XmlDocument) """
        ...


class XmlEntity(XmlNode): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    @property
    def NotationName(self) -> str:
        """ Get: NotationName(self: XmlEntity) -> str """
        ...

    @property
    def PublicId(self) -> str:
        """ Get: PublicId(self: XmlEntity) -> str """
        ...

    @property
    def SystemId(self) -> str:
        """ Get: SystemId(self: XmlEntity) -> str """
        ...



class XmlEntityReference(XmlLinkedNode): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    @property
    def BaseURI(self) -> str:
        """ Get: BaseURI(self: XmlEntityReference) -> str """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: XmlEntityReference) -> bool """
        ...

    @property
    def LocalName(self) -> str:
        """ Get: LocalName(self: XmlEntityReference) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlEntityReference) -> str """
        ...

    @property
    def NodeType(self): # -> XmlNodeType
        """ Get: NodeType(self: XmlEntityReference) -> XmlNodeType """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: XmlEntityReference) -> str
        Set: Value(self: XmlEntityReference) = value
        """
        ...


    def CloneNode(self, deep:bool) -> XmlNode:
        """ CloneNode(self: XmlEntityReference, deep: bool) -> XmlNode """
        ...

    def WriteContentTo(self, w:XmlWriter): # -> 
        """ WriteContentTo(self: XmlEntityReference, w: XmlWriter) """
        ...

    def WriteTo(self, w:XmlWriter): # -> 
        """ WriteTo(self: XmlEntityReference, w: XmlWriter) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, name: str, doc: XmlDocument) """
        ...


class XmlException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XmlException()
    XmlException(message: str)
    XmlException(message: str, innerException: Exception)
    XmlException(message: str, innerException: Exception, lineNumber: int, linePosition: int)
    """
    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: XmlException) -> int """
        ...

    @property
    def LinePosition(self) -> int:
        """ Get: LinePosition(self: XmlException) -> int """
        ...

    @property
    def SourceUri(self) -> str:
        """ Get: SourceUri(self: XmlException) -> str """
        ...


    SerializeObjectState = ...


class XmlImplementation: # skipped bases: <type 'object'>, <type 'object'>
    """
    XmlImplementation()
    XmlImplementation(nt: XmlNameTable)
    """
    def CreateDocument(self) -> XmlDocument:
        """ CreateDocument(self: XmlImplementation) -> XmlDocument """
        ...

    def HasFeature(self, strFeature:str, strVersion:str) -> bool:
        """ HasFeature(self: XmlImplementation, strFeature: str, strVersion: str) -> bool """
        ...


class XmlNamespaceManager(IXmlNamespaceResolver, IEnumerable): # skipped bases: <type 'object'>
    """ XmlNamespaceManager(nameTable: XmlNameTable) """
    @property
    def DefaultNamespace(self) -> str:
        """ Get: DefaultNamespace(self: XmlNamespaceManager) -> str """
        ...

    @property
    def NameTable(self) -> XmlNameTable:
        """ Get: NameTable(self: XmlNamespaceManager) -> XmlNameTable """
        ...


    def AddNamespace(self, prefix:str, uri:str): # -> 
        """ AddNamespace(self: XmlNamespaceManager, prefix: str, uri: str) """
        ...

    def HasNamespace(self, prefix:str) -> bool:
        """ HasNamespace(self: XmlNamespaceManager, prefix: str) -> bool """
        ...

    def PopScope(self) -> bool:
        """ PopScope(self: XmlNamespaceManager) -> bool """
        ...

    def PushScope(self): # -> 
        """ PushScope(self: XmlNamespaceManager) """
        ...

    def RemoveNamespace(self, prefix:str, uri:str): # -> 
        """ RemoveNamespace(self: XmlNamespaceManager, prefix: str, uri: str) """
        ...


class XmlNamespaceScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlNamespaceScope, values: All (0), ExcludeXml (1), Local (2) """
    All: XmlNamespaceScope = ...
    ExcludeXml: XmlNamespaceScope = ...
    Local: XmlNamespaceScope = ...
    value__ = ...


class XmlNodeChangedAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlNodeChangedAction, values: Change (2), Insert (0), Remove (1) """
    Change: XmlNodeChangedAction = ...
    Insert: XmlNodeChangedAction = ...
    Remove: XmlNodeChangedAction = ...
    value__ = ...


class XmlNodeChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ XmlNodeChangedEventArgs(node: XmlNode, oldParent: XmlNode, newParent: XmlNode, oldValue: str, newValue: str, action: XmlNodeChangedAction) """
    @property
    def Action(self) -> XmlNodeChangedAction:
        """ Get: Action(self: XmlNodeChangedEventArgs) -> XmlNodeChangedAction """
        ...

    @property
    def NewParent(self) -> XmlNode:
        """ Get: NewParent(self: XmlNodeChangedEventArgs) -> XmlNode """
        ...

    @property
    def NewValue(self) -> str:
        """ Get: NewValue(self: XmlNodeChangedEventArgs) -> str """
        ...

    @property
    def Node(self) -> XmlNode:
        """ Get: Node(self: XmlNodeChangedEventArgs) -> XmlNode """
        ...

    @property
    def OldParent(self) -> XmlNode:
        """ Get: OldParent(self: XmlNodeChangedEventArgs) -> XmlNode """
        ...

    @property
    def OldValue(self) -> str:
        """ Get: OldValue(self: XmlNodeChangedEventArgs) -> str """
        ...


    def __new__(cls, node:XmlNode, oldParent:XmlNode, newParent:XmlNode, oldValue:str, newValue:str, action:XmlNodeChangedAction) -> Self:
        """ __new__(cls: type, node: XmlNode, oldParent: XmlNode, newParent: XmlNode, oldValue: str, newValue: str, action: XmlNodeChangedAction) """
        ...


class XmlNodeChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ XmlNodeChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:XmlNodeChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: XmlNodeChangedEventHandler, sender: object, e: XmlNodeChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: XmlNodeChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:XmlNodeChangedEventArgs): # -> 
        """ Invoke(self: XmlNodeChangedEventHandler, sender: object, e: XmlNodeChangedEventArgs) """
        ...


class XmlNodeList(IDisposable, IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: XmlNodeList) -> int """
        ...


    def Item(self, index:int) -> XmlNode:
        """ Item(self: XmlNodeList, index: int) -> XmlNode """
        ...

    def PrivateDisposeNodeList(self, *args): #cannot find CLR method
        """ PrivateDisposeNodeList(self: XmlNodeList) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class XmlNodeOrder(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlNodeOrder, values: After (1), Before (0), Same (2), Unknown (3) """
    After: XmlNodeOrder = ...
    Before: XmlNodeOrder = ...
    Same: XmlNodeOrder = ...
    Unknown: XmlNodeOrder = ...
    value__ = ...


class XmlNodeReader(XmlReader, IXmlNamespaceResolver): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ XmlNodeReader(node: XmlNode) """
    def __new__(cls, node:XmlNode) -> Self:
        """ __new__(cls: type, node: XmlNode) """
        ...


class XmlNodeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlNodeType, values: Attribute (2), CDATA (4), Comment (8), Document (9), DocumentFragment (11), DocumentType (10), Element (1), EndElement (15), EndEntity (16), Entity (6), EntityReference (5), None (0), Notation (12), ProcessingInstruction (7), SignificantWhitespace (14), Text (3), Whitespace (13), XmlDeclaration (17) """
    Attribute: XmlNodeType = ...
    CDATA: XmlNodeType = ...
    Comment: XmlNodeType = ...
    Document: XmlNodeType = ...
    DocumentFragment: XmlNodeType = ...
    DocumentType: XmlNodeType = ...
    Element: XmlNodeType = ...
    EndElement: XmlNodeType = ...
    EndEntity: XmlNodeType = ...
    Entity: XmlNodeType = ...
    EntityReference: XmlNodeType = ...
    Notation: XmlNodeType = ...
    ProcessingInstruction: XmlNodeType = ...
    SignificantWhitespace: XmlNodeType = ...
    Text: XmlNodeType = ...
    value__ = ...
    Whitespace: XmlNodeType = ...
    XmlDeclaration: XmlNodeType = ...


class XmlNotation(XmlNode): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    @property
    def PublicId(self) -> str:
        """ Get: PublicId(self: XmlNotation) -> str """
        ...

    @property
    def SystemId(self) -> str:
        """ Get: SystemId(self: XmlNotation) -> str """
        ...



class XmlOutputMethod(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlOutputMethod, values: AutoDetect (3), Html (1), Text (2), Xml (0) """
    AutoDetect: XmlOutputMethod = ...
    Html: XmlOutputMethod = ...
    Text: XmlOutputMethod = ...
    value__ = ...
    Xml: XmlOutputMethod = ...


class XmlParserContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    XmlParserContext(nt: XmlNameTable, nsMgr: XmlNamespaceManager, xmlLang: str, xmlSpace: XmlSpace)
    XmlParserContext(nt: XmlNameTable, nsMgr: XmlNamespaceManager, xmlLang: str, xmlSpace: XmlSpace, enc: Encoding)
    XmlParserContext(nt: XmlNameTable, nsMgr: XmlNamespaceManager, docTypeName: str, pubId: str, sysId: str, internalSubset: str, baseURI: str, xmlLang: str, xmlSpace: XmlSpace)
    XmlParserContext(nt: XmlNameTable, nsMgr: XmlNamespaceManager, docTypeName: str, pubId: str, sysId: str, internalSubset: str, baseURI: str, xmlLang: str, xmlSpace: XmlSpace, enc: Encoding)
    """
    @property
    def BaseURI(self) -> str:
        """
        Get: BaseURI(self: XmlParserContext) -> str
        Set: BaseURI(self: XmlParserContext) = value
        """
        ...

    @property
    def DocTypeName(self) -> str:
        """
        Get: DocTypeName(self: XmlParserContext) -> str
        Set: DocTypeName(self: XmlParserContext) = value
        """
        ...

    @property
    def Encoding(self) -> Encoding:
        """
        Get: Encoding(self: XmlParserContext) -> Encoding
        Set: Encoding(self: XmlParserContext) = value
        """
        ...

    @property
    def InternalSubset(self) -> str:
        """
        Get: InternalSubset(self: XmlParserContext) -> str
        Set: InternalSubset(self: XmlParserContext) = value
        """
        ...

    @property
    def NamespaceManager(self) -> XmlNamespaceManager:
        """
        Get: NamespaceManager(self: XmlParserContext) -> XmlNamespaceManager
        Set: NamespaceManager(self: XmlParserContext) = value
        """
        ...

    @property
    def NameTable(self) -> XmlNameTable:
        """
        Get: NameTable(self: XmlParserContext) -> XmlNameTable
        Set: NameTable(self: XmlParserContext) = value
        """
        ...

    @property
    def PublicId(self) -> str:
        """
        Get: PublicId(self: XmlParserContext) -> str
        Set: PublicId(self: XmlParserContext) = value
        """
        ...

    @property
    def SystemId(self) -> str:
        """
        Get: SystemId(self: XmlParserContext) -> str
        Set: SystemId(self: XmlParserContext) = value
        """
        ...

    @property
    def XmlLang(self) -> str:
        """
        Get: XmlLang(self: XmlParserContext) -> str
        Set: XmlLang(self: XmlParserContext) = value
        """
        ...

    @property
    def XmlSpace(self): # -> XmlSpace
        """
        Get: XmlSpace(self: XmlParserContext) -> XmlSpace
        Set: XmlSpace(self: XmlParserContext) = value
        """
        ...



class XmlProcessingInstruction(XmlLinkedNode): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    @property
    def Data(self) -> str:
        """
        Get: Data(self: XmlProcessingInstruction) -> str
        Set: Data(self: XmlProcessingInstruction) = value
        """
        ...

    @property
    def InnerText(self) -> str:
        """
        Get: InnerText(self: XmlProcessingInstruction) -> str
        Set: InnerText(self: XmlProcessingInstruction) = value
        """
        ...

    @property
    def LocalName(self) -> str:
        """ Get: LocalName(self: XmlProcessingInstruction) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlProcessingInstruction) -> str """
        ...

    @property
    def NodeType(self) -> XmlNodeType:
        """ Get: NodeType(self: XmlProcessingInstruction) -> XmlNodeType """
        ...

    @property
    def Target(self) -> str:
        """ Get: Target(self: XmlProcessingInstruction) -> str """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: XmlProcessingInstruction) -> str
        Set: Value(self: XmlProcessingInstruction) = value
        """
        ...


    def CloneNode(self, deep:bool) -> XmlNode:
        """ CloneNode(self: XmlProcessingInstruction, deep: bool) -> XmlNode """
        ...

    def WriteContentTo(self, w:XmlWriter): # -> 
        """ WriteContentTo(self: XmlProcessingInstruction, w: XmlWriter) """
        ...

    def WriteTo(self, w:XmlWriter): # -> 
        """ WriteTo(self: XmlProcessingInstruction, w: XmlWriter) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, target: str, data: str, doc: XmlDocument) """
        ...


class XmlQualifiedName: # skipped bases: <type 'object'>, <type 'object'>
    """
    XmlQualifiedName()
    XmlQualifiedName(name: str)
    XmlQualifiedName(name: str, ns: str)
    """
    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: XmlQualifiedName) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlQualifiedName) -> str """
        ...

    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: XmlQualifiedName) -> str """
        ...


    def Equals(self, other:object) -> bool:
        """ Equals(self: XmlQualifiedName, other: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: XmlQualifiedName) -> int """
        ...

    def ToString(self, name=None, ns=None) -> str:
        """
        ToString(self: XmlQualifiedName) -> str
        ToString(name: str, ns: str) -> str
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Empty: XmlQualifiedName = ...


class XmlReaderSettings: # skipped bases: <type 'object'>, <type 'object'>
    """
    XmlReaderSettings()
    XmlReaderSettings(resolver: XmlResolver)
    """
    @property
    def Async(self) -> bool:
        """
        Get: Async(self: XmlReaderSettings) -> bool
        Set: Async(self: XmlReaderSettings) = value
        """
        ...

    @property
    def CheckCharacters(self) -> bool:
        """
        Get: CheckCharacters(self: XmlReaderSettings) -> bool
        Set: CheckCharacters(self: XmlReaderSettings) = value
        """
        ...

    @property
    def CloseInput(self) -> bool:
        """
        Get: CloseInput(self: XmlReaderSettings) -> bool
        Set: CloseInput(self: XmlReaderSettings) = value
        """
        ...

    @property
    def ConformanceLevel(self) -> ConformanceLevel:
        """
        Get: ConformanceLevel(self: XmlReaderSettings) -> ConformanceLevel
        Set: ConformanceLevel(self: XmlReaderSettings) = value
        """
        ...

    @property
    def DtdProcessing(self) -> DtdProcessing:
        """
        Get: DtdProcessing(self: XmlReaderSettings) -> DtdProcessing
        Set: DtdProcessing(self: XmlReaderSettings) = value
        """
        ...

    @property
    def IgnoreComments(self) -> bool:
        """
        Get: IgnoreComments(self: XmlReaderSettings) -> bool
        Set: IgnoreComments(self: XmlReaderSettings) = value
        """
        ...

    @property
    def IgnoreProcessingInstructions(self) -> bool:
        """
        Get: IgnoreProcessingInstructions(self: XmlReaderSettings) -> bool
        Set: IgnoreProcessingInstructions(self: XmlReaderSettings) = value
        """
        ...

    @property
    def IgnoreWhitespace(self) -> bool:
        """
        Get: IgnoreWhitespace(self: XmlReaderSettings) -> bool
        Set: IgnoreWhitespace(self: XmlReaderSettings) = value
        """
        ...

    @property
    def LineNumberOffset(self) -> int:
        """
        Get: LineNumberOffset(self: XmlReaderSettings) -> int
        Set: LineNumberOffset(self: XmlReaderSettings) = value
        """
        ...

    @property
    def LinePositionOffset(self) -> int:
        """
        Get: LinePositionOffset(self: XmlReaderSettings) -> int
        Set: LinePositionOffset(self: XmlReaderSettings) = value
        """
        ...

    @property
    def MaxCharactersFromEntities(self) -> Int64:
        """
        Get: MaxCharactersFromEntities(self: XmlReaderSettings) -> Int64
        Set: MaxCharactersFromEntities(self: XmlReaderSettings) = value
        """
        ...

    @property
    def MaxCharactersInDocument(self) -> Int64:
        """
        Get: MaxCharactersInDocument(self: XmlReaderSettings) -> Int64
        Set: MaxCharactersInDocument(self: XmlReaderSettings) = value
        """
        ...

    @property
    def NameTable(self) -> XmlNameTable:
        """
        Get: NameTable(self: XmlReaderSettings) -> XmlNameTable
        Set: NameTable(self: XmlReaderSettings) = value
        """
        ...

    @property
    def ProhibitDtd(self) -> bool:
        """
        Get: ProhibitDtd(self: XmlReaderSettings) -> bool
        Set: ProhibitDtd(self: XmlReaderSettings) = value
        """
        ...

    @property
    def Schemas(self) -> XmlSchemaSet:
        """
        Get: Schemas(self: XmlReaderSettings) -> XmlSchemaSet
        Set: Schemas(self: XmlReaderSettings) = value
        """
        ...

    @property
    def ValidationFlags(self) -> XmlSchemaValidationFlags:
        """
        Get: ValidationFlags(self: XmlReaderSettings) -> XmlSchemaValidationFlags
        Set: ValidationFlags(self: XmlReaderSettings) = value
        """
        ...

    @property
    def ValidationType(self) -> ValidationType:
        """
        Get: ValidationType(self: XmlReaderSettings) -> ValidationType
        Set: ValidationType(self: XmlReaderSettings) = value
        """
        ...

    @property
    def XmlResolver(self): # -> 
        """ Set: XmlResolver(self: XmlReaderSettings) = value """
        ...


    def Clone(self) -> XmlReaderSettings:
        """ Clone(self: XmlReaderSettings) -> XmlReaderSettings """
        ...

    def Reset(self): # -> 
        """ Reset(self: XmlReaderSettings) """
        ...

    ValidationEventHandler = ...


class XmlResolver: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Credentials(self): # -> 
        """ Set: Credentials(self: XmlResolver) = value """
        ...


    def GetEntity(self, absoluteUri:Uri, role:str, ofObjectToReturn:Type) -> object:
        """ GetEntity(self: XmlResolver, absoluteUri: Uri, role: str, ofObjectToReturn: Type) -> object """
        ...

    def GetEntityAsync(self, absoluteUri:Uri, role:str, ofObjectToReturn:Type) -> Task:
        """ GetEntityAsync(self: XmlResolver, absoluteUri: Uri, role: str, ofObjectToReturn: Type) -> Task[object] """
        ...

    def ResolveUri(self, baseUri:Uri, relativeUri:str) -> Uri:
        """ ResolveUri(self: XmlResolver, baseUri: Uri, relativeUri: str) -> Uri """
        ...

    def SupportsType(self, absoluteUri:Uri, type:Type) -> bool:
        """ SupportsType(self: XmlResolver, absoluteUri: Uri, type: Type) -> bool """
        ...


class XmlSecureResolver(XmlResolver): # skipped bases: <type 'object'>
    """
    XmlSecureResolver(resolver: XmlResolver, securityUrl: str)
    XmlSecureResolver(resolver: XmlResolver, evidence: Evidence)
    XmlSecureResolver(resolver: XmlResolver, permissionSet: PermissionSet)
    """
    @staticmethod
    def CreateEvidenceForUrl(securityUrl:str) -> Evidence:
        """ CreateEvidenceForUrl(securityUrl: str) -> Evidence """
        ...

    def __new__(cls, resolver:XmlResolver, *__args:str) -> Self:
        """
        __new__(cls: type, resolver: XmlResolver, securityUrl: str)
        __new__(cls: type, resolver: XmlResolver, evidence: Evidence)
        __new__(cls: type, resolver: XmlResolver, permissionSet: PermissionSet)
        """
        ...


class XmlSignificantWhitespace(XmlCharacterData): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    @property
    def LocalName(self) -> str:
        """ Get: LocalName(self: XmlSignificantWhitespace) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlSignificantWhitespace) -> str """
        ...

    @property
    def NodeType(self) -> XmlNodeType:
        """ Get: NodeType(self: XmlSignificantWhitespace) -> XmlNodeType """
        ...

    @property
    def ParentNode(self) -> XmlNode:
        """ Get: ParentNode(self: XmlSignificantWhitespace) -> XmlNode """
        ...

    @property
    def PreviousText(self) -> XmlNode:
        """ Get: PreviousText(self: XmlSignificantWhitespace) -> XmlNode """
        ...


    def CloneNode(self, deep:bool) -> XmlNode:
        """ CloneNode(self: XmlSignificantWhitespace, deep: bool) -> XmlNode """
        ...

    def WriteContentTo(self, w:XmlWriter): # -> 
        """ WriteContentTo(self: XmlSignificantWhitespace, w: XmlWriter) """
        ...

    def WriteTo(self, w:XmlWriter): # -> 
        """ WriteTo(self: XmlSignificantWhitespace, w: XmlWriter) """
        ...


class XmlSpace(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlSpace, values: Default (1), None (0), Preserve (2) """
    Default: XmlSpace = ...
    Preserve: XmlSpace = ...
    value__ = ...


class XmlText(XmlCharacterData): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    @property
    def LocalName(self) -> str:
        """ Get: LocalName(self: XmlText) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlText) -> str """
        ...

    @property
    def NodeType(self) -> XmlNodeType:
        """ Get: NodeType(self: XmlText) -> XmlNodeType """
        ...

    @property
    def ParentNode(self) -> XmlNode:
        """ Get: ParentNode(self: XmlText) -> XmlNode """
        ...

    @property
    def PreviousText(self) -> XmlNode:
        """ Get: PreviousText(self: XmlText) -> XmlNode """
        ...


    def CloneNode(self, deep:bool) -> XmlNode:
        """ CloneNode(self: XmlText, deep: bool) -> XmlNode """
        ...

    def SplitText(self, offset:int) -> XmlText:
        """ SplitText(self: XmlText, offset: int) -> XmlText """
        ...

    def WriteContentTo(self, w:XmlWriter): # -> 
        """ WriteContentTo(self: XmlText, w: XmlWriter) """
        ...

    def WriteTo(self, w:XmlWriter): # -> 
        """ WriteTo(self: XmlText, w: XmlWriter) """
        ...


class XmlTextReader(XmlReader, IXmlLineInfo, IXmlNamespaceResolver): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    XmlTextReader(input: Stream)
    XmlTextReader(url: str, input: Stream)
    XmlTextReader(input: Stream, nt: XmlNameTable)
    XmlTextReader(url: str, input: Stream, nt: XmlNameTable)
    XmlTextReader(input: TextReader)
    XmlTextReader(url: str, input: TextReader)
    XmlTextReader(input: TextReader, nt: XmlNameTable)
    XmlTextReader(url: str, input: TextReader, nt: XmlNameTable)
    XmlTextReader(xmlFragment: Stream, fragType: XmlNodeType, context: XmlParserContext)
    XmlTextReader(xmlFragment: str, fragType: XmlNodeType, context: XmlParserContext)
    XmlTextReader(url: str)
    XmlTextReader(url: str, nt: XmlNameTable)
    """
    @property
    def DtdProcessing(self) -> DtdProcessing:
        """
        Get: DtdProcessing(self: XmlTextReader) -> DtdProcessing
        Set: DtdProcessing(self: XmlTextReader) = value
        """
        ...

    @property
    def Encoding(self) -> Encoding:
        """ Get: Encoding(self: XmlTextReader) -> Encoding """
        ...

    @property
    def EntityHandling(self) -> EntityHandling:
        """
        Get: EntityHandling(self: XmlTextReader) -> EntityHandling
        Set: EntityHandling(self: XmlTextReader) = value
        """
        ...

    @property
    def Namespaces(self) -> bool:
        """
        Get: Namespaces(self: XmlTextReader) -> bool
        Set: Namespaces(self: XmlTextReader) = value
        """
        ...

    @property
    def Normalization(self) -> bool:
        """
        Get: Normalization(self: XmlTextReader) -> bool
        Set: Normalization(self: XmlTextReader) = value
        """
        ...

    @property
    def ProhibitDtd(self) -> bool:
        """
        Get: ProhibitDtd(self: XmlTextReader) -> bool
        Set: ProhibitDtd(self: XmlTextReader) = value
        """
        ...

    @property
    def WhitespaceHandling(self) -> WhitespaceHandling:
        """
        Get: WhitespaceHandling(self: XmlTextReader) -> WhitespaceHandling
        Set: WhitespaceHandling(self: XmlTextReader) = value
        """
        ...

    @property
    def XmlResolver(self): # -> 
        """ Set: XmlResolver(self: XmlTextReader) = value """
        ...


    def GetRemainder(self) -> TextReader:
        """ GetRemainder(self: XmlTextReader) -> TextReader """
        ...

    def ReadBase64(self, array:Array, offset:int, len:int) -> int:
        """ ReadBase64(self: XmlTextReader, array: Array[Byte], offset: int, len: int) -> int """
        ...

    def ReadBinHex(self, array:Array, offset:int, len:int) -> int:
        """ ReadBinHex(self: XmlTextReader, array: Array[Byte], offset: int, len: int) -> int """
        ...

    def ReadChars(self, buffer:Array, index:int, count:int) -> int:
        """ ReadChars(self: XmlTextReader, buffer: Array[Char], index: int, count: int) -> int """
        ...

    def ResetState(self): # -> 
        """ ResetState(self: XmlTextReader) """
        ...

    def __new__(cls, *__args:XmlNameTable) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, nt: XmlNameTable)
        __new__(cls: type, input: Stream)
        __new__(cls: type, url: str, input: Stream)
        __new__(cls: type, input: Stream, nt: XmlNameTable)
        __new__(cls: type, url: str, input: Stream, nt: XmlNameTable)
        __new__(cls: type, input: TextReader)
        __new__(cls: type, url: str, input: TextReader)
        __new__(cls: type, input: TextReader, nt: XmlNameTable)
        __new__(cls: type, url: str, input: TextReader, nt: XmlNameTable)
        __new__(cls: type, xmlFragment: Stream, fragType: XmlNodeType, context: XmlParserContext)
        __new__(cls: type, xmlFragment: str, fragType: XmlNodeType, context: XmlParserContext)
        __new__(cls: type, url: str)
        __new__(cls: type, url: str, nt: XmlNameTable)
        """
        ...


class XmlTextWriter(XmlWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    XmlTextWriter(w: Stream, encoding: Encoding)
    XmlTextWriter(filename: str, encoding: Encoding)
    XmlTextWriter(w: TextWriter)
    """
    @property
    def BaseStream(self) -> Stream:
        """ Get: BaseStream(self: XmlTextWriter) -> Stream """
        ...

    @property
    def Formatting(self) -> Formatting:
        """
        Get: Formatting(self: XmlTextWriter) -> Formatting
        Set: Formatting(self: XmlTextWriter) = value
        """
        ...

    @property
    def Indentation(self) -> int:
        """
        Get: Indentation(self: XmlTextWriter) -> int
        Set: Indentation(self: XmlTextWriter) = value
        """
        ...

    @property
    def IndentChar(self) -> Char:
        """
        Get: IndentChar(self: XmlTextWriter) -> Char
        Set: IndentChar(self: XmlTextWriter) = value
        """
        ...

    @property
    def Namespaces(self) -> bool:
        """
        Get: Namespaces(self: XmlTextWriter) -> bool
        Set: Namespaces(self: XmlTextWriter) = value
        """
        ...

    @property
    def QuoteChar(self) -> Char:
        """
        Get: QuoteChar(self: XmlTextWriter) -> Char
        Set: QuoteChar(self: XmlTextWriter) = value
        """
        ...


    def __new__(cls, *__args:TextWriter) -> Self:
        """
        __new__(cls: type, w: Stream, encoding: Encoding)
        __new__(cls: type, filename: str, encoding: Encoding)
        __new__(cls: type, w: TextWriter)
        """
        ...


class XmlTokenizedType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlTokenizedType, values: CDATA (0), ENTITIES (5), ENTITY (4), ENUMERATION (9), ID (1), IDREF (2), IDREFS (3), NCName (11), NMTOKEN (6), NMTOKENS (7), None (12), NOTATION (8), QName (10) """
    CDATA: XmlTokenizedType = ...
    ENTITIES: XmlTokenizedType = ...
    ENTITY: XmlTokenizedType = ...
    ENUMERATION: XmlTokenizedType = ...
    ID: XmlTokenizedType = ...
    IDREF: XmlTokenizedType = ...
    IDREFS: XmlTokenizedType = ...
    NCName: XmlTokenizedType = ...
    NMTOKEN: XmlTokenizedType = ...
    NMTOKENS: XmlTokenizedType = ...
    NOTATION: XmlTokenizedType = ...
    QName: XmlTokenizedType = ...
    value__ = ...


class XmlUrlResolver(XmlResolver): # skipped bases: <type 'object'>
    """ XmlUrlResolver() """
    @property
    def CachePolicy(self): # -> 
        """ Set: CachePolicy(self: XmlUrlResolver) = value """
        ...

    @property
    def Proxy(self): # -> 
        """ Set: Proxy(self: XmlUrlResolver) = value """
        ...



class XmlValidatingReader(XmlReader, IXmlLineInfo, IXmlNamespaceResolver): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    XmlValidatingReader(reader: XmlReader)
    XmlValidatingReader(xmlFragment: str, fragType: XmlNodeType, context: XmlParserContext)
    XmlValidatingReader(xmlFragment: Stream, fragType: XmlNodeType, context: XmlParserContext)
    """
    @property
    def Encoding(self) -> Encoding:
        """ Get: Encoding(self: XmlValidatingReader) -> Encoding """
        ...

    @property
    def EntityHandling(self) -> EntityHandling:
        """
        Get: EntityHandling(self: XmlValidatingReader) -> EntityHandling
        Set: EntityHandling(self: XmlValidatingReader) = value
        """
        ...

    @property
    def Namespaces(self) -> bool:
        """
        Get: Namespaces(self: XmlValidatingReader) -> bool
        Set: Namespaces(self: XmlValidatingReader) = value
        """
        ...

    @property
    def Reader(self) -> XmlReader:
        """ Get: Reader(self: XmlValidatingReader) -> XmlReader """
        ...

    @property
    def Schemas(self) -> XmlSchemaCollection:
        """ Get: Schemas(self: XmlValidatingReader) -> XmlSchemaCollection """
        ...

    @property
    def SchemaType(self) -> object:
        """ Get: SchemaType(self: XmlValidatingReader) -> object """
        ...

    @property
    def ValidationType(self) -> ValidationType:
        """
        Get: ValidationType(self: XmlValidatingReader) -> ValidationType
        Set: ValidationType(self: XmlValidatingReader) = value
        """
        ...

    @property
    def XmlResolver(self): # -> 
        """ Set: XmlResolver(self: XmlValidatingReader) = value """
        ...


    def ReadTypedValue(self) -> object:
        """ ReadTypedValue(self: XmlValidatingReader) -> object """
        ...

    def __new__(cls, *__args:XmlReader) -> Self:
        """
        __new__(cls: type, reader: XmlReader)
        __new__(cls: type, xmlFragment: str, fragType: XmlNodeType, context: XmlParserContext)
        __new__(cls: type, xmlFragment: Stream, fragType: XmlNodeType, context: XmlParserContext)
        """
        ...

    ValidationEventHandler = ...


class XmlWhitespace(XmlCharacterData): # skipped bases: <type 'IXPathNavigable'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'object'>
    """ no doc """
    @property
    def LocalName(self) -> str:
        """ Get: LocalName(self: XmlWhitespace) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlWhitespace) -> str """
        ...

    @property
    def NodeType(self) -> XmlNodeType:
        """ Get: NodeType(self: XmlWhitespace) -> XmlNodeType """
        ...

    @property
    def ParentNode(self) -> XmlNode:
        """ Get: ParentNode(self: XmlWhitespace) -> XmlNode """
        ...

    @property
    def PreviousText(self) -> XmlNode:
        """ Get: PreviousText(self: XmlWhitespace) -> XmlNode """
        ...


    def CloneNode(self, deep:bool) -> XmlNode:
        """ CloneNode(self: XmlWhitespace, deep: bool) -> XmlNode """
        ...

    def WriteContentTo(self, w:XmlWriter): # -> 
        """ WriteContentTo(self: XmlWhitespace, w: XmlWriter) """
        ...

    def WriteTo(self, w:XmlWriter): # -> 
        """ WriteTo(self: XmlWhitespace, w: XmlWriter) """
        ...


class XmlWriterSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ XmlWriterSettings() """
    @property
    def Async(self) -> bool:
        """
        Get: Async(self: XmlWriterSettings) -> bool
        Set: Async(self: XmlWriterSettings) = value
        """
        ...

    @property
    def CheckCharacters(self) -> bool:
        """
        Get: CheckCharacters(self: XmlWriterSettings) -> bool
        Set: CheckCharacters(self: XmlWriterSettings) = value
        """
        ...

    @property
    def CloseOutput(self) -> bool:
        """
        Get: CloseOutput(self: XmlWriterSettings) -> bool
        Set: CloseOutput(self: XmlWriterSettings) = value
        """
        ...

    @property
    def ConformanceLevel(self) -> ConformanceLevel:
        """
        Get: ConformanceLevel(self: XmlWriterSettings) -> ConformanceLevel
        Set: ConformanceLevel(self: XmlWriterSettings) = value
        """
        ...

    @property
    def DoNotEscapeUriAttributes(self) -> bool:
        """
        Get: DoNotEscapeUriAttributes(self: XmlWriterSettings) -> bool
        Set: DoNotEscapeUriAttributes(self: XmlWriterSettings) = value
        """
        ...

    @property
    def Encoding(self) -> Encoding:
        """
        Get: Encoding(self: XmlWriterSettings) -> Encoding
        Set: Encoding(self: XmlWriterSettings) = value
        """
        ...

    @property
    def Indent(self) -> bool:
        """
        Get: Indent(self: XmlWriterSettings) -> bool
        Set: Indent(self: XmlWriterSettings) = value
        """
        ...

    @property
    def IndentChars(self) -> str:
        """
        Get: IndentChars(self: XmlWriterSettings) -> str
        Set: IndentChars(self: XmlWriterSettings) = value
        """
        ...

    @property
    def NamespaceHandling(self) -> NamespaceHandling:
        """
        Get: NamespaceHandling(self: XmlWriterSettings) -> NamespaceHandling
        Set: NamespaceHandling(self: XmlWriterSettings) = value
        """
        ...

    @property
    def NewLineChars(self) -> str:
        """
        Get: NewLineChars(self: XmlWriterSettings) -> str
        Set: NewLineChars(self: XmlWriterSettings) = value
        """
        ...

    @property
    def NewLineHandling(self) -> NewLineHandling:
        """
        Get: NewLineHandling(self: XmlWriterSettings) -> NewLineHandling
        Set: NewLineHandling(self: XmlWriterSettings) = value
        """
        ...

    @property
    def NewLineOnAttributes(self) -> bool:
        """
        Get: NewLineOnAttributes(self: XmlWriterSettings) -> bool
        Set: NewLineOnAttributes(self: XmlWriterSettings) = value
        """
        ...

    @property
    def OmitXmlDeclaration(self) -> bool:
        """
        Get: OmitXmlDeclaration(self: XmlWriterSettings) -> bool
        Set: OmitXmlDeclaration(self: XmlWriterSettings) = value
        """
        ...

    @property
    def OutputMethod(self) -> XmlOutputMethod:
        """ Get: OutputMethod(self: XmlWriterSettings) -> XmlOutputMethod """
        ...

    @property
    def WriteEndDocumentOnClose(self) -> bool:
        """
        Get: WriteEndDocumentOnClose(self: XmlWriterSettings) -> bool
        Set: WriteEndDocumentOnClose(self: XmlWriterSettings) = value
        """
        ...


    def Clone(self) -> XmlWriterSettings:
        """ Clone(self: XmlWriterSettings) -> XmlWriterSettings """
        ...

    def Reset(self): # -> 
        """ Reset(self: XmlWriterSettings) """
        ...


class XmlXapResolver(XmlResolver): # skipped bases: <type 'object'>
    """ XmlXapResolver() """
    @staticmethod
    def RegisterApplicationResourceStreamResolver(appStreamResolver:IApplicationResourceStreamResolver): # -> 
        """ RegisterApplicationResourceStreamResolver(appStreamResolver: IApplicationResourceStreamResolver) """
        ...


# variables with complex values

