# encoding: utf-8
# module System.Xml.XPath calls itself XPath
# from System.Xml.Linq, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Xml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Sdk.Sfc import XPathExpression

from System import DateTime, Enum, ICloneable, Int64, SystemException, Type

from System.Collections import IComparer, IEnumerable, IEqualityComparer

from System.Xml import (IXmlNamespaceResolver, XmlNameTable, 
    XmlNamespaceManager, XmlNodeOrder, XmlReader, XmlWriter)

from System.Xml.Linq import XElement, XNode

from System.Xml.Schema import (IXmlSchemaInfo, ValidationEventHandler, 
    XmlSchemaSet, XmlSchemaType)

"""The following names are not found in the module: (BoundEvent, 
    XPathNavigator, XPathNodeIterator, XPathNodeType, XPathResultType, field#)
"""

# no functions
# classes

class Extensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateNavigator(node:XNode, nameTable:XmlNameTable = ...): # -> XPathNavigator
        """
        CreateNavigator(node: XNode) -> XPathNavigator
        CreateNavigator(node: XNode, nameTable: XmlNameTable) -> XPathNavigator
        """
        ...

    @staticmethod
    def XPathEvaluate(node:XNode, expression:str, resolver:IXmlNamespaceResolver = ...) -> object:
        """
        XPathEvaluate(node: XNode, expression: str) -> object
        XPathEvaluate(node: XNode, expression: str, resolver: IXmlNamespaceResolver) -> object
        """
        ...

    @staticmethod
    def XPathSelectElement(node:XNode, expression:str, resolver:IXmlNamespaceResolver = ...) -> XElement:
        """
        XPathSelectElement(node: XNode, expression: str) -> XElement
        XPathSelectElement(node: XNode, expression: str, resolver: IXmlNamespaceResolver) -> XElement
        """
        ...

    @staticmethod
    def XPathSelectElements(node:XNode, expression:str, resolver:IXmlNamespaceResolver = ...) -> IEnumerable:
        """
        XPathSelectElements(node: XNode, expression: str) -> IEnumerable[XElement]
        XPathSelectElements(node: XNode, expression: str, resolver: IXmlNamespaceResolver) -> IEnumerable[XElement]
        """
        ...

    __all__: list = ...


class IXPathNavigable: # skipped bases: <type 'object'>
    """ no doc """
    def CreateNavigator(self): # -> XPathNavigator
        """ CreateNavigator(self: IXPathNavigable) -> XPathNavigator """
        ...


class XDocumentExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ToXPathNavigable(node:XNode) -> IXPathNavigable:
        """ ToXPathNavigable(node: XNode) -> IXPathNavigable """
        ...

    __all__: list = ...


class XmlCaseOrder(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlCaseOrder, values: LowerFirst (2), None (0), UpperFirst (1) """
    LowerFirst: XmlCaseOrder = ...
    UpperFirst: XmlCaseOrder = ...
    value__ = ...


class XmlDataType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlDataType, values: Number (2), Text (1) """
    Number: XmlDataType = ...
    Text: XmlDataType = ...
    value__ = ...


class XmlSortOrder(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlSortOrder, values: Ascending (1), Descending (2) """
    Ascending: XmlSortOrder = ...
    Descending: XmlSortOrder = ...
    value__ = ...


class XPathDocument(IXPathNavigable): # skipped bases: <type 'object'>
    """
    XPathDocument(reader: XmlReader)
    XPathDocument(reader: XmlReader, space: XmlSpace)
    XPathDocument(textReader: TextReader)
    XPathDocument(stream: Stream)
    XPathDocument(uri: str)
    XPathDocument(uri: str, space: XmlSpace)
    """
    pass

class XPathException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XPathException()
    XPathException(message: str)
    XPathException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class XPathExpression: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Expression(self) -> str:
        """ Get: Expression(self: XPathExpression) -> str """
        ...

    @property
    def ReturnType(self): # -> XPathResultType
        """ Get: ReturnType(self: XPathExpression) -> XPathResultType """
        ...


    def AddSort(self, expr:object, *__args:IComparer): # -> 
        """ AddSort(self: XPathExpression, expr: object, comparer: IComparer)AddSort(self: XPathExpression, expr: object, order: XmlSortOrder, caseOrder: XmlCaseOrder, lang: str, dataType: XmlDataType) """
        ...

    def Clone(self) -> XPathExpression:
        """ Clone(self: XPathExpression) -> XPathExpression """
        ...

    @staticmethod
    def Compile(xpath:str, nsResolver:IXmlNamespaceResolver = ...) -> XPathExpression:
        """
        Compile(xpath: str) -> XPathExpression
        Compile(xpath: str, nsResolver: IXmlNamespaceResolver) -> XPathExpression
        """
        ...

    def SetContext(self, *__args:XmlNamespaceManager): # -> 
        """ SetContext(self: XPathExpression, nsManager: XmlNamespaceManager)SetContext(self: XPathExpression, nsResolver: IXmlNamespaceResolver) """
        ...


class XPathItem: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsNode(self) -> bool:
        """ Get: IsNode(self: XPathItem) -> bool """
        ...

    @property
    def TypedValue(self) -> object:
        """ Get: TypedValue(self: XPathItem) -> object """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: XPathItem) -> str """
        ...

    @property
    def ValueAsBoolean(self) -> bool:
        """ Get: ValueAsBoolean(self: XPathItem) -> bool """
        ...

    @property
    def ValueAsDateTime(self) -> DateTime:
        """ Get: ValueAsDateTime(self: XPathItem) -> DateTime """
        ...

    @property
    def ValueAsDouble(self) -> float:
        """ Get: ValueAsDouble(self: XPathItem) -> float """
        ...

    @property
    def ValueAsInt(self) -> int:
        """ Get: ValueAsInt(self: XPathItem) -> int """
        ...

    @property
    def ValueAsLong(self) -> Int64:
        """ Get: ValueAsLong(self: XPathItem) -> Int64 """
        ...

    @property
    def ValueType(self) -> Type:
        """ Get: ValueType(self: XPathItem) -> Type """
        ...

    @property
    def XmlType(self) -> XmlSchemaType:
        """ Get: XmlType(self: XPathItem) -> XmlSchemaType """
        ...


    def ValueAs(self, returnType:Type, nsResolver:IXmlNamespaceResolver = ...) -> object:
        """
        ValueAs(self: XPathItem, returnType: Type) -> object
        ValueAs(self: XPathItem, returnType: Type, nsResolver: IXmlNamespaceResolver) -> object
        """
        ...


class XPathNamespaceScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XPathNamespaceScope, values: All (0), ExcludeXml (1), Local (2) """
    All: XPathNamespaceScope = ...
    ExcludeXml: XPathNamespaceScope = ...
    Local: XPathNamespaceScope = ...
    value__ = ...


class XPathNavigator(IXmlNamespaceResolver, ICloneable, IXPathNavigable, XPathItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BaseURI(self) -> str:
        """ Get: BaseURI(self: XPathNavigator) -> str """
        ...

    @property
    def CanEdit(self) -> bool:
        """ Get: CanEdit(self: XPathNavigator) -> bool """
        ...

    @property
    def HasAttributes(self) -> bool:
        """ Get: HasAttributes(self: XPathNavigator) -> bool """
        ...

    @property
    def HasChildren(self) -> bool:
        """ Get: HasChildren(self: XPathNavigator) -> bool """
        ...

    @property
    def InnerXml(self) -> str:
        """
        Get: InnerXml(self: XPathNavigator) -> str
        Set: InnerXml(self: XPathNavigator) = value
        """
        ...

    @property
    def IsEmptyElement(self) -> bool:
        """ Get: IsEmptyElement(self: XPathNavigator) -> bool """
        ...

    @property
    def LocalName(self) -> str:
        """ Get: LocalName(self: XPathNavigator) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XPathNavigator) -> str """
        ...

    @property
    def NamespaceURI(self) -> str:
        """ Get: NamespaceURI(self: XPathNavigator) -> str """
        ...

    @property
    def NameTable(self) -> XmlNameTable:
        """ Get: NameTable(self: XPathNavigator) -> XmlNameTable """
        ...

    @property
    def NavigatorComparer(self) -> IEqualityComparer:
        """ Get: NavigatorComparer() -> IEqualityComparer """
        ...

    @property
    def NodeType(self): # -> XPathNodeType
        """ Get: NodeType(self: XPathNavigator) -> XPathNodeType """
        ...

    @property
    def OuterXml(self) -> str:
        """
        Get: OuterXml(self: XPathNavigator) -> str
        Set: OuterXml(self: XPathNavigator) = value
        """
        ...

    @property
    def Prefix(self) -> str:
        """ Get: Prefix(self: XPathNavigator) -> str """
        ...

    @property
    def SchemaInfo(self) -> IXmlSchemaInfo:
        """ Get: SchemaInfo(self: XPathNavigator) -> IXmlSchemaInfo """
        ...

    @property
    def UnderlyingObject(self) -> object:
        """ Get: UnderlyingObject(self: XPathNavigator) -> object """
        ...

    @property
    def XmlLang(self) -> str:
        """ Get: XmlLang(self: XPathNavigator) -> str """
        ...


    def AppendChild(self, newChild:str = ...): # -> 
        """
        AppendChild(self: XPathNavigator) -> XmlWriter
        AppendChild(self: XPathNavigator, newChild: str)AppendChild(self: XPathNavigator, newChild: XmlReader)AppendChild(self: XPathNavigator, newChild: XPathNavigator)
        """
        ...

    def AppendChildElement(self, prefix:str, localName:str, namespaceURI:str, value:str): # -> 
        """ AppendChildElement(self: XPathNavigator, prefix: str, localName: str, namespaceURI: str, value: str) """
        ...

    def CheckValidity(self, schemas:XmlSchemaSet, validationEventHandler:ValidationEventHandler) -> bool:
        """ CheckValidity(self: XPathNavigator, schemas: XmlSchemaSet, validationEventHandler: ValidationEventHandler) -> bool """
        ...

    def ComparePosition(self, nav:XPathNavigator) -> XmlNodeOrder:
        """ ComparePosition(self: XPathNavigator, nav: XPathNavigator) -> XmlNodeOrder """
        ...

    def Compile(self, xpath:str) -> XPathExpression:
        """ Compile(self: XPathNavigator, xpath: str) -> XPathExpression """
        ...

    def CreateAttribute(self, prefix:str, localName:str, namespaceURI:str, value:str): # -> 
        """ CreateAttribute(self: XPathNavigator, prefix: str, localName: str, namespaceURI: str, value: str) """
        ...

    def CreateAttributes(self) -> XmlWriter:
        """ CreateAttributes(self: XPathNavigator) -> XmlWriter """
        ...

    def DeleteRange(self, lastSiblingToDelete:XPathNavigator): # -> 
        """ DeleteRange(self: XPathNavigator, lastSiblingToDelete: XPathNavigator) """
        ...

    def DeleteSelf(self): # -> 
        """ DeleteSelf(self: XPathNavigator) """
        ...

    def Evaluate(self, *__args:str) -> object:
        """
        Evaluate(self: XPathNavigator, xpath: str) -> object
        Evaluate(self: XPathNavigator, xpath: str, resolver: IXmlNamespaceResolver) -> object
        Evaluate(self: XPathNavigator, expr: XPathExpression) -> object
        Evaluate(self: XPathNavigator, expr: XPathExpression, context: XPathNodeIterator) -> object
        """
        ...

    def GetAttribute(self, localName:str, namespaceURI:str) -> str:
        """ GetAttribute(self: XPathNavigator, localName: str, namespaceURI: str) -> str """
        ...

    def GetNamespace(self, name:str) -> str:
        """ GetNamespace(self: XPathNavigator, name: str) -> str """
        ...

    def InsertAfter(self, newSibling:str = ...): # -> 
        """
        InsertAfter(self: XPathNavigator) -> XmlWriter
        InsertAfter(self: XPathNavigator, newSibling: str)InsertAfter(self: XPathNavigator, newSibling: XmlReader)InsertAfter(self: XPathNavigator, newSibling: XPathNavigator)
        """
        ...

    def InsertBefore(self, newSibling:str = ...): # -> 
        """
        InsertBefore(self: XPathNavigator) -> XmlWriter
        InsertBefore(self: XPathNavigator, newSibling: str)InsertBefore(self: XPathNavigator, newSibling: XmlReader)InsertBefore(self: XPathNavigator, newSibling: XPathNavigator)
        """
        ...

    def InsertElementAfter(self, prefix:str, localName:str, namespaceURI:str, value:str): # -> 
        """ InsertElementAfter(self: XPathNavigator, prefix: str, localName: str, namespaceURI: str, value: str) """
        ...

    def InsertElementBefore(self, prefix:str, localName:str, namespaceURI:str, value:str): # -> 
        """ InsertElementBefore(self: XPathNavigator, prefix: str, localName: str, namespaceURI: str, value: str) """
        ...

    def IsDescendant(self, nav:XPathNavigator) -> bool:
        """ IsDescendant(self: XPathNavigator, nav: XPathNavigator) -> bool """
        ...

    def IsSamePosition(self, other:XPathNavigator) -> bool:
        """ IsSamePosition(self: XPathNavigator, other: XPathNavigator) -> bool """
        ...

    def Matches(self, *__args:XPathExpression) -> bool:
        """
        Matches(self: XPathNavigator, expr: XPathExpression) -> bool
        Matches(self: XPathNavigator, xpath: str) -> bool
        """
        ...

    def MoveTo(self, other:XPathNavigator) -> bool:
        """ MoveTo(self: XPathNavigator, other: XPathNavigator) -> bool """
        ...

    def MoveToAttribute(self, localName:str, namespaceURI:str) -> bool:
        """ MoveToAttribute(self: XPathNavigator, localName: str, namespaceURI: str) -> bool """
        ...

    def MoveToChild(self, *__args) -> bool: # Not found arg types: {'*__args': 'XPathNodeType'}
        """
        MoveToChild(self: XPathNavigator, localName: str, namespaceURI: str) -> bool
        MoveToChild(self: XPathNavigator, type: XPathNodeType) -> bool
        """
        ...

    def MoveToFirst(self) -> bool:
        """ MoveToFirst(self: XPathNavigator) -> bool """
        ...

    def MoveToFirstAttribute(self) -> bool:
        """ MoveToFirstAttribute(self: XPathNavigator) -> bool """
        ...

    def MoveToFirstChild(self) -> bool:
        """ MoveToFirstChild(self: XPathNavigator) -> bool """
        ...

    def MoveToFirstNamespace(self, namespaceScope:XPathNamespaceScope = ...) -> bool:
        """
        MoveToFirstNamespace(self: XPathNavigator) -> bool
        MoveToFirstNamespace(self: XPathNavigator, namespaceScope: XPathNamespaceScope) -> bool
        """
        ...

    def MoveToFollowing(self, *__args) -> bool: # Not found arg types: {'*__args': 'XPathNodeType'}
        """
        MoveToFollowing(self: XPathNavigator, localName: str, namespaceURI: str) -> bool
        MoveToFollowing(self: XPathNavigator, localName: str, namespaceURI: str, end: XPathNavigator) -> bool
        MoveToFollowing(self: XPathNavigator, type: XPathNodeType) -> bool
        MoveToFollowing(self: XPathNavigator, type: XPathNodeType, end: XPathNavigator) -> bool
        """
        ...

    def MoveToId(self, id:str) -> bool:
        """ MoveToId(self: XPathNavigator, id: str) -> bool """
        ...

    def MoveToNamespace(self, name:str) -> bool:
        """ MoveToNamespace(self: XPathNavigator, name: str) -> bool """
        ...

    def MoveToNext(self, *__args) -> bool: # Not found arg types: {'*__args': 'XPathNodeType'}
        """
        MoveToNext(self: XPathNavigator, localName: str, namespaceURI: str) -> bool
        MoveToNext(self: XPathNavigator, type: XPathNodeType) -> bool
        MoveToNext(self: XPathNavigator) -> bool
        """
        ...

    def MoveToNextAttribute(self) -> bool:
        """ MoveToNextAttribute(self: XPathNavigator) -> bool """
        ...

    def MoveToNextNamespace(self, namespaceScope:XPathNamespaceScope = ...) -> bool:
        """
        MoveToNextNamespace(self: XPathNavigator) -> bool
        MoveToNextNamespace(self: XPathNavigator, namespaceScope: XPathNamespaceScope) -> bool
        """
        ...

    def MoveToParent(self) -> bool:
        """ MoveToParent(self: XPathNavigator) -> bool """
        ...

    def MoveToPrevious(self) -> bool:
        """ MoveToPrevious(self: XPathNavigator) -> bool """
        ...

    def MoveToRoot(self): # -> 
        """ MoveToRoot(self: XPathNavigator) """
        ...

    def PrependChild(self, newChild:str = ...): # -> 
        """
        PrependChild(self: XPathNavigator) -> XmlWriter
        PrependChild(self: XPathNavigator, newChild: str)PrependChild(self: XPathNavigator, newChild: XmlReader)PrependChild(self: XPathNavigator, newChild: XPathNavigator)
        """
        ...

    def PrependChildElement(self, prefix:str, localName:str, namespaceURI:str, value:str): # -> 
        """ PrependChildElement(self: XPathNavigator, prefix: str, localName: str, namespaceURI: str, value: str) """
        ...

    def ReadSubtree(self) -> XmlReader:
        """ ReadSubtree(self: XPathNavigator) -> XmlReader """
        ...

    def ReplaceRange(self, lastSiblingToReplace:XPathNavigator) -> XmlWriter:
        """ ReplaceRange(self: XPathNavigator, lastSiblingToReplace: XPathNavigator) -> XmlWriter """
        ...

    def ReplaceSelf(self, newNode:str): # -> 
        """ ReplaceSelf(self: XPathNavigator, newNode: str)ReplaceSelf(self: XPathNavigator, newNode: XmlReader)ReplaceSelf(self: XPathNavigator, newNode: XPathNavigator) """
        ...

    def Select(self, *__args:str): # -> XPathNodeIterator
        """
        Select(self: XPathNavigator, xpath: str) -> XPathNodeIterator
        Select(self: XPathNavigator, xpath: str, resolver: IXmlNamespaceResolver) -> XPathNodeIterator
        Select(self: XPathNavigator, expr: XPathExpression) -> XPathNodeIterator
        """
        ...

    def SelectAncestors(self, *__args): # -> XPathNodeIterator
        """
        SelectAncestors(self: XPathNavigator, type: XPathNodeType, matchSelf: bool) -> XPathNodeIterator
        SelectAncestors(self: XPathNavigator, name: str, namespaceURI: str, matchSelf: bool) -> XPathNodeIterator
        """
        ...

    def SelectChildren(self, *__args): # -> XPathNodeIterator # Not found arg types: {'*__args': 'XPathNodeType'}
        """
        SelectChildren(self: XPathNavigator, type: XPathNodeType) -> XPathNodeIterator
        SelectChildren(self: XPathNavigator, name: str, namespaceURI: str) -> XPathNodeIterator
        """
        ...

    def SelectDescendants(self, *__args): # -> XPathNodeIterator
        """
        SelectDescendants(self: XPathNavigator, type: XPathNodeType, matchSelf: bool) -> XPathNodeIterator
        SelectDescendants(self: XPathNavigator, name: str, namespaceURI: str, matchSelf: bool) -> XPathNodeIterator
        """
        ...

    def SelectSingleNode(self, *__args:str) -> XPathNavigator:
        """
        SelectSingleNode(self: XPathNavigator, xpath: str) -> XPathNavigator
        SelectSingleNode(self: XPathNavigator, xpath: str, resolver: IXmlNamespaceResolver) -> XPathNavigator
        SelectSingleNode(self: XPathNavigator, expression: XPathExpression) -> XPathNavigator
        """
        ...

    def SetTypedValue(self, typedValue:object): # -> 
        """ SetTypedValue(self: XPathNavigator, typedValue: object) """
        ...

    def SetValue(self, value:str): # -> 
        """ SetValue(self: XPathNavigator, value: str) """
        ...

    def ToString(self) -> str:
        """ ToString(self: XPathNavigator) -> str """
        ...

    def WriteSubtree(self, writer:XmlWriter): # -> 
        """ WriteSubtree(self: XPathNavigator, writer: XmlWriter) """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...



class XPathNodeIterator(ICloneable, IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: XPathNodeIterator) -> int """
        ...

    @property
    def Current(self) -> XPathNavigator:
        """ Get: Current(self: XPathNodeIterator) -> XPathNavigator """
        ...

    @property
    def CurrentPosition(self) -> int:
        """ Get: CurrentPosition(self: XPathNodeIterator) -> int """
        ...


    def MoveNext(self) -> bool:
        """ MoveNext(self: XPathNodeIterator) -> bool """
        ...


class XPathNodeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XPathNodeType, values: All (9), Attribute (2), Comment (8), Element (1), Namespace (3), ProcessingInstruction (7), Root (0), SignificantWhitespace (5), Text (4), Whitespace (6) """
    All: XPathNodeType = ...
    Attribute: XPathNodeType = ...
    Comment: XPathNodeType = ...
    Element: XPathNodeType = ...
    Namespace: XPathNodeType = ...
    ProcessingInstruction: XPathNodeType = ...
    Root: XPathNodeType = ...
    SignificantWhitespace: XPathNodeType = ...
    Text: XPathNodeType = ...
    value__ = ...
    Whitespace: XPathNodeType = ...


class XPathResultType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XPathResultType, values: Any (5), Boolean (2), Error (6), Navigator (1), NodeSet (3), Number (0), String (1) """
    Any: XPathResultType = ...
    Boolean: XPathResultType = ...
    Error: XPathResultType = ...
    Navigator: XPathResultType = ...
    NodeSet: XPathResultType = ...
    Number: XPathResultType = ...
    String: XPathResultType = ...
    value__ = ...


