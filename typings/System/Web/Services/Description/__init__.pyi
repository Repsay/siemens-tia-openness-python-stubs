# encoding: utf-8
# module System.Web.Services.Description calls itself Description
# from System.Web.Services, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, Type

from System.CodeDom import (CodeAttributeDeclarationCollection, 
    CodeCommentStatementCollection, CodeCompileUnit, CodeNamespace, 
    CodeTypeDeclaration)

from System.CodeDom.Compiler import CodeDomProvider

from System.Collections import CollectionBase, IEnumerable, IEnumerator

from System.Collections.Specialized import StringCollection

from System.IO import TextReader

from System.Web.Services import WebMethodAttribute, WsiProfiles

from System.Web.Services.Discovery import DiscoveryClientDocumentCollection

from System.Web.Services.Protocols import LogicalMethodInfo

from System.Xml import XmlElement, XmlQualifiedName, XmlReader

from System.Xml.Schema import ValidationEventHandler, XmlSchema

from System.Xml.Serialization import (CodeGenerationOptions, CodeIdentifiers, 
    SoapCodeExporter, SoapSchemaImporter, XmlCodeExporter, 
    XmlReflectionImporter, XmlSchemaExporter, XmlSchemaImporter, XmlSchemas, 
    XmlSerializer, XmlSerializerNamespaces)

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class BasicProfileViolation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Claims(self) -> WsiProfiles:
        """ Get: Claims(self: BasicProfileViolation) -> WsiProfiles """
        ...

    @property
    def Details(self) -> str:
        """ Get: Details(self: BasicProfileViolation) -> str """
        ...

    @property
    def Elements(self) -> StringCollection:
        """ Get: Elements(self: BasicProfileViolation) -> StringCollection """
        ...

    @property
    def NormativeStatement(self) -> str:
        """ Get: NormativeStatement(self: BasicProfileViolation) -> str """
        ...

    @property
    def Recommendation(self) -> str:
        """ Get: Recommendation(self: BasicProfileViolation) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: BasicProfileViolation) -> str """
        ...


class BasicProfileViolationCollection(CollectionBase, IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ BasicProfileViolationCollection() """
    def Contains(self, violation:BasicProfileViolation) -> bool:
        """ Contains(self: BasicProfileViolationCollection, violation: BasicProfileViolation) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: BasicProfileViolationCollection, array: Array[BasicProfileViolation], index: int) """
        ...

    def IndexOf(self, violation:BasicProfileViolation) -> int:
        """ IndexOf(self: BasicProfileViolationCollection, violation: BasicProfileViolation) -> int """
        ...

    def Insert(self, index:int, violation:BasicProfileViolation): # -> 
        """ Insert(self: BasicProfileViolationCollection, index: int, violation: BasicProfileViolation) """
        ...

    def Remove(self, violation:BasicProfileViolation): # -> 
        """ Remove(self: BasicProfileViolationCollection, violation: BasicProfileViolation) """
        ...

    def ToString(self) -> str:
        """ ToString(self: BasicProfileViolationCollection) -> str """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class BasicProfileViolationEnumerator(IEnumerator): # skipped bases: <type 'IDisposable'>, <type 'IEnumerator'>, <type 'object'>
    """ BasicProfileViolationEnumerator(list: BasicProfileViolationCollection) """
    def Dispose(self): # -> 
        """ Dispose(self: BasicProfileViolationEnumerator) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: BasicProfileViolationEnumerator) -> bool """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BasicProfileViolation](enumerator: IEnumerator[BasicProfileViolation], value: BasicProfileViolation) -> bool """
        ...


class DocumentableItem: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Documentation(self) -> str:
        """
        Get: Documentation(self: DocumentableItem) -> str
        Set: Documentation(self: DocumentableItem) = value
        """
        ...

    @property
    def DocumentationElement(self) -> XmlElement:
        """
        Get: DocumentationElement(self: DocumentableItem) -> XmlElement
        Set: DocumentationElement(self: DocumentableItem) = value
        """
        ...

    @property
    def ExtensibleAttributes(self) -> Array:
        """
        Get: ExtensibleAttributes(self: DocumentableItem) -> Array[XmlAttribute]
        Set: ExtensibleAttributes(self: DocumentableItem) = value
        """
        ...

    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: DocumentableItem) -> ServiceDescriptionFormatExtensionCollection """
        ...

    @property
    def Namespaces(self) -> XmlSerializerNamespaces:
        """
        Get: Namespaces(self: DocumentableItem) -> XmlSerializerNamespaces
        Set: Namespaces(self: DocumentableItem) = value
        """
        ...



class NamedItem(DocumentableItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: NamedItem) -> str
        Set: Name(self: NamedItem) = value
        """
        ...



class Binding(NamedItem): # skipped bases: <type 'object'>
    """ Binding() """
    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: Binding) -> ServiceDescriptionFormatExtensionCollection """
        ...

    @property
    def Operations(self) -> OperationBindingCollection:
        """ Get: Operations(self: Binding) -> OperationBindingCollection """
        ...

    @property
    def ServiceDescription(self) -> ServiceDescription:
        """ Get: ServiceDescription(self: Binding) -> ServiceDescription """
        ...

    @property
    def Type(self) -> XmlQualifiedName:
        """
        Get: Type(self: Binding) -> XmlQualifiedName
        Set: Type(self: Binding) = value
        """
        ...



class ServiceDescriptionBaseCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    @property
    def Table(self):
        ...


    def GetKey(self, *args): #cannot find CLR method
        """ GetKey(self: ServiceDescriptionBaseCollection, value: object) -> str """
        ...

    def SetParent(self, *args): #cannot find CLR method
        """ SetParent(self: ServiceDescriptionBaseCollection, value: object, parent: object) """
        ...


class BindingCollection(ServiceDescriptionBaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: BindingCollection, array: Array[Binding], index: int) """
        ...


class MessageBinding(NamedItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def OperationBinding(self) -> OperationBinding:
        """ Get: OperationBinding(self: MessageBinding) -> OperationBinding """
        ...



class FaultBinding(MessageBinding): # skipped bases: <type 'object'>
    """ FaultBinding() """
    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: FaultBinding) -> ServiceDescriptionFormatExtensionCollection """
        ...



class FaultBindingCollection(ServiceDescriptionBaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: FaultBindingCollection, array: Array[FaultBinding], index: int) """
        ...


class ServiceDescriptionFormatExtension: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Handled(self) -> bool:
        """
        Get: Handled(self: ServiceDescriptionFormatExtension) -> bool
        Set: Handled(self: ServiceDescriptionFormatExtension) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: ServiceDescriptionFormatExtension) -> object """
        ...

    @property
    def Required(self) -> bool:
        """
        Get: Required(self: ServiceDescriptionFormatExtension) -> bool
        Set: Required(self: ServiceDescriptionFormatExtension) = value
        """
        ...



class HttpAddressBinding(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ HttpAddressBinding() """
    @property
    def Location(self) -> str:
        """
        Get: Location(self: HttpAddressBinding) -> str
        Set: Location(self: HttpAddressBinding) = value
        """
        ...



class HttpBinding(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ HttpBinding() """
    @property
    def Verb(self) -> str:
        """
        Get: Verb(self: HttpBinding) -> str
        Set: Verb(self: HttpBinding) = value
        """
        ...


    Namespace: str = ...


class HttpOperationBinding(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ HttpOperationBinding() """
    @property
    def Location(self) -> str:
        """
        Get: Location(self: HttpOperationBinding) -> str
        Set: Location(self: HttpOperationBinding) = value
        """
        ...



class HttpUrlEncodedBinding(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ HttpUrlEncodedBinding() """
    pass

class HttpUrlReplacementBinding(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ HttpUrlReplacementBinding() """
    pass

class Import(DocumentableItem): # skipped bases: <type 'object'>
    """ Import() """
    @property
    def Location(self) -> str:
        """
        Get: Location(self: Import) -> str
        Set: Location(self: Import) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: Import) -> str
        Set: Namespace(self: Import) = value
        """
        ...

    @property
    def ServiceDescription(self) -> ServiceDescription:
        """ Get: ServiceDescription(self: Import) -> ServiceDescription """
        ...



class ImportCollection(ServiceDescriptionBaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ImportCollection, array: Array[Import], index: int) """
        ...


class InputBinding(MessageBinding): # skipped bases: <type 'object'>
    """ InputBinding() """
    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: InputBinding) -> ServiceDescriptionFormatExtensionCollection """
        ...



class Message(NamedItem): # skipped bases: <type 'object'>
    """ Message() """
    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: Message) -> ServiceDescriptionFormatExtensionCollection """
        ...

    @property
    def Parts(self) -> MessagePartCollection:
        """ Get: Parts(self: Message) -> MessagePartCollection """
        ...

    @property
    def ServiceDescription(self) -> ServiceDescription:
        """ Get: ServiceDescription(self: Message) -> ServiceDescription """
        ...


    def FindPartByName(self, partName:str) -> MessagePart:
        """ FindPartByName(self: Message, partName: str) -> MessagePart """
        ...

    def FindPartsByName(self, partNames:Array) -> Array:
        """ FindPartsByName(self: Message, partNames: Array[str]) -> Array[MessagePart] """
        ...


class MessageCollection(ServiceDescriptionBaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: MessageCollection, array: Array[Message], index: int) """
        ...


class MessagePart(NamedItem): # skipped bases: <type 'object'>
    """ MessagePart() """
    @property
    def Element(self) -> XmlQualifiedName:
        """
        Get: Element(self: MessagePart) -> XmlQualifiedName
        Set: Element(self: MessagePart) = value
        """
        ...

    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: MessagePart) -> ServiceDescriptionFormatExtensionCollection """
        ...

    @property
    def Message(self) -> Message:
        """ Get: Message(self: MessagePart) -> Message """
        ...

    @property
    def Type(self) -> XmlQualifiedName:
        """
        Get: Type(self: MessagePart) -> XmlQualifiedName
        Set: Type(self: MessagePart) = value
        """
        ...



class MessagePartCollection(ServiceDescriptionBaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: MessagePartCollection, array: Array[MessagePart], index: int) """
        ...


class MimeContentBinding(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ MimeContentBinding() """
    @property
    def Part(self) -> str:
        """
        Get: Part(self: MimeContentBinding) -> str
        Set: Part(self: MimeContentBinding) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: MimeContentBinding) -> str
        Set: Type(self: MimeContentBinding) = value
        """
        ...


    Namespace: str = ...


class MimeMultipartRelatedBinding(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ MimeMultipartRelatedBinding() """
    @property
    def Parts(self) -> MimePartCollection:
        """ Get: Parts(self: MimeMultipartRelatedBinding) -> MimePartCollection """
        ...



class MimePart(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ MimePart() """
    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: MimePart) -> ServiceDescriptionFormatExtensionCollection """
        ...



class MimePartCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ MimePartCollection() """
    def Add(self, mimePart:MimePart) -> int:
        """ Add(self: MimePartCollection, mimePart: MimePart) -> int """
        ...

    def Contains(self, mimePart:MimePart) -> bool:
        """ Contains(self: MimePartCollection, mimePart: MimePart) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: MimePartCollection, array: Array[MimePart], index: int) """
        ...

    def IndexOf(self, mimePart:MimePart) -> int:
        """ IndexOf(self: MimePartCollection, mimePart: MimePart) -> int """
        ...

    def Insert(self, index:int, mimePart:MimePart): # -> 
        """ Insert(self: MimePartCollection, index: int, mimePart: MimePart) """
        ...

    def Remove(self, mimePart:MimePart): # -> 
        """ Remove(self: MimePartCollection, mimePart: MimePart) """
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


class MimeTextBinding(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ MimeTextBinding() """
    @property
    def Matches(self) -> MimeTextMatchCollection:
        """ Get: Matches(self: MimeTextBinding) -> MimeTextMatchCollection """
        ...


    Namespace: str = ...


class MimeTextMatch: # skipped bases: <type 'object'>, <type 'object'>
    """ MimeTextMatch() """
    @property
    def Capture(self) -> int:
        """
        Get: Capture(self: MimeTextMatch) -> int
        Set: Capture(self: MimeTextMatch) = value
        """
        ...

    @property
    def Group(self) -> int:
        """
        Get: Group(self: MimeTextMatch) -> int
        Set: Group(self: MimeTextMatch) = value
        """
        ...

    @property
    def IgnoreCase(self) -> bool:
        """
        Get: IgnoreCase(self: MimeTextMatch) -> bool
        Set: IgnoreCase(self: MimeTextMatch) = value
        """
        ...

    @property
    def Matches(self) -> MimeTextMatchCollection:
        """ Get: Matches(self: MimeTextMatch) -> MimeTextMatchCollection """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: MimeTextMatch) -> str
        Set: Name(self: MimeTextMatch) = value
        """
        ...

    @property
    def Pattern(self) -> str:
        """
        Get: Pattern(self: MimeTextMatch) -> str
        Set: Pattern(self: MimeTextMatch) = value
        """
        ...

    @property
    def Repeats(self) -> int:
        """
        Get: Repeats(self: MimeTextMatch) -> int
        Set: Repeats(self: MimeTextMatch) = value
        """
        ...

    @property
    def RepeatsString(self) -> str:
        """
        Get: RepeatsString(self: MimeTextMatch) -> str
        Set: RepeatsString(self: MimeTextMatch) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: MimeTextMatch) -> str
        Set: Type(self: MimeTextMatch) = value
        """
        ...



class MimeTextMatchCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ MimeTextMatchCollection() """
    def Add(self, match:MimeTextMatch) -> int:
        """ Add(self: MimeTextMatchCollection, match: MimeTextMatch) -> int """
        ...

    def Contains(self, match:MimeTextMatch) -> bool:
        """ Contains(self: MimeTextMatchCollection, match: MimeTextMatch) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: MimeTextMatchCollection, array: Array[MimeTextMatch], index: int) """
        ...

    def IndexOf(self, match:MimeTextMatch) -> int:
        """ IndexOf(self: MimeTextMatchCollection, match: MimeTextMatch) -> int """
        ...

    def Insert(self, index:int, match:MimeTextMatch): # -> 
        """ Insert(self: MimeTextMatchCollection, index: int, match: MimeTextMatch) """
        ...

    def Remove(self, match:MimeTextMatch): # -> 
        """ Remove(self: MimeTextMatchCollection, match: MimeTextMatch) """
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


class MimeXmlBinding(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ MimeXmlBinding() """
    @property
    def Part(self) -> str:
        """
        Get: Part(self: MimeXmlBinding) -> str
        Set: Part(self: MimeXmlBinding) = value
        """
        ...



class Operation(NamedItem): # skipped bases: <type 'object'>
    """ Operation() """
    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: Operation) -> ServiceDescriptionFormatExtensionCollection """
        ...

    @property
    def Faults(self) -> OperationFaultCollection:
        """ Get: Faults(self: Operation) -> OperationFaultCollection """
        ...

    @property
    def Messages(self) -> OperationMessageCollection:
        """ Get: Messages(self: Operation) -> OperationMessageCollection """
        ...

    @property
    def ParameterOrder(self) -> Array:
        """
        Get: ParameterOrder(self: Operation) -> Array[str]
        Set: ParameterOrder(self: Operation) = value
        """
        ...

    @property
    def ParameterOrderString(self) -> str:
        """
        Get: ParameterOrderString(self: Operation) -> str
        Set: ParameterOrderString(self: Operation) = value
        """
        ...

    @property
    def PortType(self) -> PortType:
        """ Get: PortType(self: Operation) -> PortType """
        ...


    def IsBoundBy(self, operationBinding:OperationBinding) -> bool:
        """ IsBoundBy(self: Operation, operationBinding: OperationBinding) -> bool """
        ...


class OperationBinding(NamedItem): # skipped bases: <type 'object'>
    """ OperationBinding() """
    @property
    def Binding(self) -> Binding:
        """ Get: Binding(self: OperationBinding) -> Binding """
        ...

    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: OperationBinding) -> ServiceDescriptionFormatExtensionCollection """
        ...

    @property
    def Faults(self) -> FaultBindingCollection:
        """ Get: Faults(self: OperationBinding) -> FaultBindingCollection """
        ...

    @property
    def Input(self) -> InputBinding:
        """
        Get: Input(self: OperationBinding) -> InputBinding
        Set: Input(self: OperationBinding) = value
        """
        ...

    @property
    def Output(self) -> OutputBinding:
        """
        Get: Output(self: OperationBinding) -> OutputBinding
        Set: Output(self: OperationBinding) = value
        """
        ...



class OperationBindingCollection(ServiceDescriptionBaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: OperationBindingCollection, array: Array[OperationBinding], index: int) """
        ...


class OperationCollection(ServiceDescriptionBaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: OperationCollection, array: Array[Operation], index: int) """
        ...


class OperationMessage(NamedItem): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Message(self) -> XmlQualifiedName:
        """
        Get: Message(self: OperationMessage) -> XmlQualifiedName
        Set: Message(self: OperationMessage) = value
        """
        ...

    @property
    def Operation(self) -> Operation:
        """ Get: Operation(self: OperationMessage) -> Operation """
        ...



class OperationFault(OperationMessage): # skipped bases: <type 'object'>
    """ OperationFault() """
    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: OperationFault) -> ServiceDescriptionFormatExtensionCollection """
        ...



class OperationFaultCollection(ServiceDescriptionBaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: OperationFaultCollection, array: Array[OperationFault], index: int) """
        ...


class OperationFlow(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OperationFlow, values: None (0), Notification (2), OneWay (1), RequestResponse (3), SolicitResponse (4) """
    Notification: OperationFlow = ...
    OneWay: OperationFlow = ...
    RequestResponse: OperationFlow = ...
    SolicitResponse: OperationFlow = ...
    value__ = ...


class OperationInput(OperationMessage): # skipped bases: <type 'object'>
    """ OperationInput() """
    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: OperationInput) -> ServiceDescriptionFormatExtensionCollection """
        ...



class OperationMessageCollection(ServiceDescriptionBaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    @property
    def Flow(self) -> OperationFlow:
        """ Get: Flow(self: OperationMessageCollection) -> OperationFlow """
        ...

    @property
    def Input(self) -> OperationInput:
        """ Get: Input(self: OperationMessageCollection) -> OperationInput """
        ...

    @property
    def Output(self) -> OperationOutput:
        """ Get: Output(self: OperationMessageCollection) -> OperationOutput """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: OperationMessageCollection, array: Array[OperationMessage], index: int) """
        ...


class OperationOutput(OperationMessage): # skipped bases: <type 'object'>
    """ OperationOutput() """
    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: OperationOutput) -> ServiceDescriptionFormatExtensionCollection """
        ...



class OutputBinding(MessageBinding): # skipped bases: <type 'object'>
    """ OutputBinding() """
    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: OutputBinding) -> ServiceDescriptionFormatExtensionCollection """
        ...



class Port(NamedItem): # skipped bases: <type 'object'>
    """ Port() """
    @property
    def Binding(self) -> XmlQualifiedName:
        """
        Get: Binding(self: Port) -> XmlQualifiedName
        Set: Binding(self: Port) = value
        """
        ...

    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: Port) -> ServiceDescriptionFormatExtensionCollection """
        ...

    @property
    def Service(self) -> Service:
        """ Get: Service(self: Port) -> Service """
        ...



class PortCollection(ServiceDescriptionBaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: PortCollection, array: Array[Port], index: int) """
        ...


class PortType(NamedItem): # skipped bases: <type 'object'>
    """ PortType() """
    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: PortType) -> ServiceDescriptionFormatExtensionCollection """
        ...

    @property
    def Operations(self) -> OperationCollection:
        """ Get: Operations(self: PortType) -> OperationCollection """
        ...

    @property
    def ServiceDescription(self) -> ServiceDescription:
        """ Get: ServiceDescription(self: PortType) -> ServiceDescription """
        ...



class PortTypeCollection(ServiceDescriptionBaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: PortTypeCollection, array: Array[PortType], index: int) """
        ...


class ProtocolImporter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AbstractSchemas(self) -> XmlSchemas:
        """ Get: AbstractSchemas(self: ProtocolImporter) -> XmlSchemas """
        ...

    @property
    def Binding(self) -> Binding:
        """ Get: Binding(self: ProtocolImporter) -> Binding """
        ...

    @property
    def ClassName(self) -> str:
        """ Get: ClassName(self: ProtocolImporter) -> str """
        ...

    @property
    def ClassNames(self) -> CodeIdentifiers:
        """ Get: ClassNames(self: ProtocolImporter) -> CodeIdentifiers """
        ...

    @property
    def CodeNamespace(self) -> CodeNamespace:
        """ Get: CodeNamespace(self: ProtocolImporter) -> CodeNamespace """
        ...

    @property
    def CodeTypeDeclaration(self) -> CodeTypeDeclaration:
        """ Get: CodeTypeDeclaration(self: ProtocolImporter) -> CodeTypeDeclaration """
        ...

    @property
    def ConcreteSchemas(self) -> XmlSchemas:
        """ Get: ConcreteSchemas(self: ProtocolImporter) -> XmlSchemas """
        ...

    @property
    def InputMessage(self) -> Message:
        """ Get: InputMessage(self: ProtocolImporter) -> Message """
        ...

    @property
    def MethodName(self) -> str:
        """ Get: MethodName(self: ProtocolImporter) -> str """
        ...

    @property
    def Operation(self) -> Operation:
        """ Get: Operation(self: ProtocolImporter) -> Operation """
        ...

    @property
    def OperationBinding(self) -> OperationBinding:
        """ Get: OperationBinding(self: ProtocolImporter) -> OperationBinding """
        ...

    @property
    def OutputMessage(self) -> Message:
        """ Get: OutputMessage(self: ProtocolImporter) -> Message """
        ...

    @property
    def Port(self) -> Port:
        """ Get: Port(self: ProtocolImporter) -> Port """
        ...

    @property
    def PortType(self) -> PortType:
        """ Get: PortType(self: ProtocolImporter) -> PortType """
        ...

    @property
    def ProtocolName(self) -> str:
        """ Get: ProtocolName(self: ProtocolImporter) -> str """
        ...

    @property
    def Schemas(self) -> XmlSchemas:
        """ Get: Schemas(self: ProtocolImporter) -> XmlSchemas """
        ...

    @property
    def Service(self) -> Service:
        """ Get: Service(self: ProtocolImporter) -> Service """
        ...

    @property
    def ServiceDescriptions(self) -> ServiceDescriptionCollection:
        """ Get: ServiceDescriptions(self: ProtocolImporter) -> ServiceDescriptionCollection """
        ...

    @property
    def Style(self) -> ServiceDescriptionImportStyle:
        """ Get: Style(self: ProtocolImporter) -> ServiceDescriptionImportStyle """
        ...

    @property
    def Warnings(self) -> ServiceDescriptionImportWarnings:
        """
        Get: Warnings(self: ProtocolImporter) -> ServiceDescriptionImportWarnings
        Set: Warnings(self: ProtocolImporter) = value
        """
        ...


    def AddExtensionWarningComments(self, comments:CodeCommentStatementCollection, extensions:ServiceDescriptionFormatExtensionCollection): # -> 
        """ AddExtensionWarningComments(self: ProtocolImporter, comments: CodeCommentStatementCollection, extensions: ServiceDescriptionFormatExtensionCollection) """
        ...

    def BeginClass(self, *args): #cannot find CLR method
        """ BeginClass(self: ProtocolImporter) -> CodeTypeDeclaration """
        ...

    def BeginNamespace(self, *args): #cannot find CLR method
        """ BeginNamespace(self: ProtocolImporter) """
        ...

    def EndClass(self, *args): #cannot find CLR method
        """ EndClass(self: ProtocolImporter) """
        ...

    def EndNamespace(self, *args): #cannot find CLR method
        """ EndNamespace(self: ProtocolImporter) """
        ...

    def GenerateMethod(self, *args): #cannot find CLR method
        """ GenerateMethod(self: ProtocolImporter) -> CodeMemberMethod """
        ...

    def IsBindingSupported(self, *args): #cannot find CLR method
        """ IsBindingSupported(self: ProtocolImporter) -> bool """
        ...

    def IsOperationFlowSupported(self, *args): #cannot find CLR method
        """ IsOperationFlowSupported(self: ProtocolImporter, flow: OperationFlow) -> bool """
        ...

    def OperationBindingSyntaxException(self, text:str) -> Exception:
        """ OperationBindingSyntaxException(self: ProtocolImporter, text: str) -> Exception """
        ...

    def OperationSyntaxException(self, text:str) -> Exception:
        """ OperationSyntaxException(self: ProtocolImporter, text: str) -> Exception """
        ...

    def UnsupportedBindingWarning(self, text:str): # -> 
        """ UnsupportedBindingWarning(self: ProtocolImporter, text: str) """
        ...

    def UnsupportedOperationBindingWarning(self, text:str): # -> 
        """ UnsupportedOperationBindingWarning(self: ProtocolImporter, text: str) """
        ...

    def UnsupportedOperationWarning(self, text:str): # -> 
        """ UnsupportedOperationWarning(self: ProtocolImporter, text: str) """
        ...


class ProtocolReflector: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Binding(self) -> Binding:
        """ Get: Binding(self: ProtocolReflector) -> Binding """
        ...

    @property
    def DefaultNamespace(self) -> str:
        """ Get: DefaultNamespace(self: ProtocolReflector) -> str """
        ...

    @property
    def HeaderMessages(self) -> MessageCollection:
        """ Get: HeaderMessages(self: ProtocolReflector) -> MessageCollection """
        ...

    @property
    def InputMessage(self) -> Message:
        """ Get: InputMessage(self: ProtocolReflector) -> Message """
        ...

    @property
    def Method(self) -> LogicalMethodInfo:
        """ Get: Method(self: ProtocolReflector) -> LogicalMethodInfo """
        ...

    @property
    def MethodAttribute(self) -> WebMethodAttribute:
        """ Get: MethodAttribute(self: ProtocolReflector) -> WebMethodAttribute """
        ...

    @property
    def Methods(self) -> Array:
        """ Get: Methods(self: ProtocolReflector) -> Array[LogicalMethodInfo] """
        ...

    @property
    def Operation(self) -> Operation:
        """ Get: Operation(self: ProtocolReflector) -> Operation """
        ...

    @property
    def OperationBinding(self) -> OperationBinding:
        """ Get: OperationBinding(self: ProtocolReflector) -> OperationBinding """
        ...

    @property
    def OutputMessage(self) -> Message:
        """ Get: OutputMessage(self: ProtocolReflector) -> Message """
        ...

    @property
    def Port(self) -> Port:
        """ Get: Port(self: ProtocolReflector) -> Port """
        ...

    @property
    def PortType(self) -> PortType:
        """ Get: PortType(self: ProtocolReflector) -> PortType """
        ...

    @property
    def ProtocolName(self) -> str:
        """ Get: ProtocolName(self: ProtocolReflector) -> str """
        ...

    @property
    def ReflectionImporter(self) -> XmlReflectionImporter:
        """ Get: ReflectionImporter(self: ProtocolReflector) -> XmlReflectionImporter """
        ...

    @property
    def SchemaExporter(self) -> XmlSchemaExporter:
        """ Get: SchemaExporter(self: ProtocolReflector) -> XmlSchemaExporter """
        ...

    @property
    def Schemas(self) -> XmlSchemas:
        """ Get: Schemas(self: ProtocolReflector) -> XmlSchemas """
        ...

    @property
    def Service(self) -> Service:
        """ Get: Service(self: ProtocolReflector) -> Service """
        ...

    @property
    def ServiceDescription(self) -> ServiceDescription:
        """ Get: ServiceDescription(self: ProtocolReflector) -> ServiceDescription """
        ...

    @property
    def ServiceDescriptions(self) -> ServiceDescriptionCollection:
        """ Get: ServiceDescriptions(self: ProtocolReflector) -> ServiceDescriptionCollection """
        ...

    @property
    def ServiceType(self) -> Type:
        """ Get: ServiceType(self: ProtocolReflector) -> Type """
        ...

    @property
    def ServiceUrl(self) -> str:
        """ Get: ServiceUrl(self: ProtocolReflector) -> str """
        ...


    def BeginClass(self, *args): #cannot find CLR method
        """ BeginClass(self: ProtocolReflector) """
        ...

    def EndClass(self, *args): #cannot find CLR method
        """ EndClass(self: ProtocolReflector) """
        ...

    def GetServiceDescription(self, ns:str) -> ServiceDescription:
        """ GetServiceDescription(self: ProtocolReflector, ns: str) -> ServiceDescription """
        ...

    def ReflectDescription(self, *args): #cannot find CLR method
        """ ReflectDescription(self: ProtocolReflector) """
        ...

    def ReflectMethod(self, *args): #cannot find CLR method
        """ ReflectMethod(self: ProtocolReflector) -> bool """
        ...

    def ReflectMethodBinding(self, *args): #cannot find CLR method
        """ ReflectMethodBinding(self: ProtocolReflector) -> str """
        ...


class Service(NamedItem): # skipped bases: <type 'object'>
    """ Service() """
    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: Service) -> ServiceDescriptionFormatExtensionCollection """
        ...

    @property
    def Ports(self) -> PortCollection:
        """ Get: Ports(self: Service) -> PortCollection """
        ...

    @property
    def ServiceDescription(self) -> ServiceDescription:
        """ Get: ServiceDescription(self: Service) -> ServiceDescription """
        ...



class ServiceCollection(ServiceDescriptionBaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ServiceCollection, array: Array[Service], index: int) """
        ...


class ServiceDescription(NamedItem): # skipped bases: <type 'object'>
    """ ServiceDescription() """
    @property
    def Bindings(self) -> BindingCollection:
        """ Get: Bindings(self: ServiceDescription) -> BindingCollection """
        ...

    @property
    def Extensions(self) -> ServiceDescriptionFormatExtensionCollection:
        """ Get: Extensions(self: ServiceDescription) -> ServiceDescriptionFormatExtensionCollection """
        ...

    @property
    def Imports(self) -> ImportCollection:
        """ Get: Imports(self: ServiceDescription) -> ImportCollection """
        ...

    @property
    def Messages(self) -> MessageCollection:
        """ Get: Messages(self: ServiceDescription) -> MessageCollection """
        ...

    @property
    def PortTypes(self) -> PortTypeCollection:
        """ Get: PortTypes(self: ServiceDescription) -> PortTypeCollection """
        ...

    @property
    def RetrievalUrl(self) -> str:
        """
        Get: RetrievalUrl(self: ServiceDescription) -> str
        Set: RetrievalUrl(self: ServiceDescription) = value
        """
        ...

    @property
    def Schema(self) -> XmlSchema:
        """ Get: Schema() -> XmlSchema """
        ...

    @property
    def Serializer(self) -> XmlSerializer:
        """ Get: Serializer() -> XmlSerializer """
        ...

    @property
    def ServiceDescriptions(self) -> ServiceDescriptionCollection:
        """ Get: ServiceDescriptions(self: ServiceDescription) -> ServiceDescriptionCollection """
        ...

    @property
    def Services(self) -> ServiceCollection:
        """ Get: Services(self: ServiceDescription) -> ServiceCollection """
        ...

    @property
    def TargetNamespace(self) -> str:
        """
        Get: TargetNamespace(self: ServiceDescription) -> str
        Set: TargetNamespace(self: ServiceDescription) = value
        """
        ...

    @property
    def Types(self) -> Types:
        """
        Get: Types(self: ServiceDescription) -> Types
        Set: Types(self: ServiceDescription) = value
        """
        ...

    @property
    def ValidationWarnings(self) -> StringCollection:
        """ Get: ValidationWarnings(self: ServiceDescription) -> StringCollection """
        ...


    @staticmethod
    def CanRead(reader:XmlReader) -> bool:
        """ CanRead(reader: XmlReader) -> bool """
        ...

    @staticmethod
    def Read(*__args:TextReader) -> ServiceDescription:
        """
        Read(textReader: TextReader) -> ServiceDescription
        Read(stream: Stream) -> ServiceDescription
        Read(reader: XmlReader) -> ServiceDescription
        Read(fileName: str) -> ServiceDescription
        Read(fileName: str, validate: bool) -> ServiceDescription
        Read(textReader: TextReader, validate: bool) -> ServiceDescription
        Read(stream: Stream, validate: bool) -> ServiceDescription
        Read(reader: XmlReader, validate: bool) -> ServiceDescription
        """
        ...

    def Write(self, *__args:str): # -> 
        """ Write(self: ServiceDescription, fileName: str)Write(self: ServiceDescription, stream: Stream)Write(self: ServiceDescription, writer: TextWriter)Write(self: ServiceDescription, writer: XmlWriter) """
        ...

    Namespace: str = ...


class ServiceDescriptionCollection(ServiceDescriptionBaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ ServiceDescriptionCollection() """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ServiceDescriptionCollection, array: Array[ServiceDescription], index: int) """
        ...

    def GetBinding(self, name:XmlQualifiedName) -> Binding:
        """ GetBinding(self: ServiceDescriptionCollection, name: XmlQualifiedName) -> Binding """
        ...

    def GetMessage(self, name:XmlQualifiedName) -> Message:
        """ GetMessage(self: ServiceDescriptionCollection, name: XmlQualifiedName) -> Message """
        ...

    def GetPortType(self, name:XmlQualifiedName) -> PortType:
        """ GetPortType(self: ServiceDescriptionCollection, name: XmlQualifiedName) -> PortType """
        ...

    def GetService(self, name:XmlQualifiedName) -> Service:
        """ GetService(self: ServiceDescriptionCollection, name: XmlQualifiedName) -> Service """
        ...


class ServiceDescriptionFormatExtensionCollection(ServiceDescriptionBaseCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ ServiceDescriptionFormatExtensionCollection(parent: object) """
    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ServiceDescriptionFormatExtensionCollection, array: Array[object], index: int) """
        ...

    def Find(self, *__args:Type) -> object:
        """
        Find(self: ServiceDescriptionFormatExtensionCollection, type: Type) -> object
        Find(self: ServiceDescriptionFormatExtensionCollection, name: str, ns: str) -> XmlElement
        """
        ...

    def FindAll(self, *__args:Type) -> Array:
        """
        FindAll(self: ServiceDescriptionFormatExtensionCollection, type: Type) -> Array[object]
        FindAll(self: ServiceDescriptionFormatExtensionCollection, name: str, ns: str) -> Array[XmlElement]
        """
        ...

    def IsHandled(self, item:object) -> bool:
        """ IsHandled(self: ServiceDescriptionFormatExtensionCollection, item: object) -> bool """
        ...

    def IsRequired(self, item:object) -> bool:
        """ IsRequired(self: ServiceDescriptionFormatExtensionCollection, item: object) -> bool """
        ...

    def __new__(cls, parent:object) -> Self:
        """ __new__(cls: type, parent: object) """
        ...


class ServiceDescriptionImporter: # skipped bases: <type 'object'>, <type 'object'>
    """ ServiceDescriptionImporter() """
    @property
    def CodeGenerationOptions(self) -> CodeGenerationOptions:
        """
        Get: CodeGenerationOptions(self: ServiceDescriptionImporter) -> CodeGenerationOptions
        Set: CodeGenerationOptions(self: ServiceDescriptionImporter) = value
        """
        ...

    @property
    def CodeGenerator(self) -> CodeDomProvider:
        """
        Get: CodeGenerator(self: ServiceDescriptionImporter) -> CodeDomProvider
        Set: CodeGenerator(self: ServiceDescriptionImporter) = value
        """
        ...

    @property
    def ProtocolName(self) -> str:
        """
        Get: ProtocolName(self: ServiceDescriptionImporter) -> str
        Set: ProtocolName(self: ServiceDescriptionImporter) = value
        """
        ...

    @property
    def Schemas(self) -> XmlSchemas:
        """ Get: Schemas(self: ServiceDescriptionImporter) -> XmlSchemas """
        ...

    @property
    def ServiceDescriptions(self) -> ServiceDescriptionCollection:
        """ Get: ServiceDescriptions(self: ServiceDescriptionImporter) -> ServiceDescriptionCollection """
        ...

    @property
    def Style(self) -> ServiceDescriptionImportStyle:
        """
        Get: Style(self: ServiceDescriptionImporter) -> ServiceDescriptionImportStyle
        Set: Style(self: ServiceDescriptionImporter) = value
        """
        ...


    def AddServiceDescription(self, serviceDescription:ServiceDescription, appSettingUrlKey:str, appSettingBaseUrl:str): # -> 
        """ AddServiceDescription(self: ServiceDescriptionImporter, serviceDescription: ServiceDescription, appSettingUrlKey: str, appSettingBaseUrl: str) """
        ...

    @staticmethod
    def GenerateWebReferences(webReferences:WebReferenceCollection, codeProvider:CodeDomProvider, codeCompileUnit:CodeCompileUnit, options:WebReferenceOptions) -> StringCollection:
        """ GenerateWebReferences(webReferences: WebReferenceCollection, codeProvider: CodeDomProvider, codeCompileUnit: CodeCompileUnit, options: WebReferenceOptions) -> StringCollection """
        ...

    def Import(self, codeNamespace:CodeNamespace, codeCompileUnit:CodeCompileUnit) -> ServiceDescriptionImportWarnings:
        """ Import(self: ServiceDescriptionImporter, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit) -> ServiceDescriptionImportWarnings """
        ...


class ServiceDescriptionImportStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ServiceDescriptionImportStyle, values: Client (0), Server (1), ServerInterface (2) """
    Client: ServiceDescriptionImportStyle = ...
    Server: ServiceDescriptionImportStyle = ...
    ServerInterface: ServiceDescriptionImportStyle = ...
    value__ = ...


class ServiceDescriptionImportWarnings(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ServiceDescriptionImportWarnings, values: NoCodeGenerated (1), NoMethodsGenerated (32), OptionalExtensionsIgnored (2), RequiredExtensionsIgnored (4), SchemaValidation (64), UnsupportedBindingsIgnored (16), UnsupportedOperationsIgnored (8), WsiConformance (128) """
    NoCodeGenerated: ServiceDescriptionImportWarnings = ...
    NoMethodsGenerated: ServiceDescriptionImportWarnings = ...
    OptionalExtensionsIgnored: ServiceDescriptionImportWarnings = ...
    RequiredExtensionsIgnored: ServiceDescriptionImportWarnings = ...
    SchemaValidation: ServiceDescriptionImportWarnings = ...
    UnsupportedBindingsIgnored: ServiceDescriptionImportWarnings = ...
    UnsupportedOperationsIgnored: ServiceDescriptionImportWarnings = ...
    value__ = ...
    WsiConformance: ServiceDescriptionImportWarnings = ...


class ServiceDescriptionReflector: # skipped bases: <type 'object'>, <type 'object'>
    """ ServiceDescriptionReflector() """
    @property
    def Schemas(self) -> XmlSchemas:
        """ Get: Schemas(self: ServiceDescriptionReflector) -> XmlSchemas """
        ...

    @property
    def ServiceDescriptions(self) -> ServiceDescriptionCollection:
        """ Get: ServiceDescriptions(self: ServiceDescriptionReflector) -> ServiceDescriptionCollection """
        ...


    def Reflect(self, type:Type, url:str): # -> 
        """ Reflect(self: ServiceDescriptionReflector, type: Type, url: str) """
        ...


class SoapAddressBinding(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ SoapAddressBinding() """
    @property
    def Location(self) -> str:
        """
        Get: Location(self: SoapAddressBinding) -> str
        Set: Location(self: SoapAddressBinding) = value
        """
        ...



class Soap12AddressBinding(SoapAddressBinding): # skipped bases: <type 'object'>
    """ Soap12AddressBinding() """
    pass

class SoapBinding(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ SoapBinding() """
    @property
    def Schema(self) -> XmlSchema:
        """ Get: Schema() -> XmlSchema """
        ...

    @property
    def Style(self) -> SoapBindingStyle:
        """
        Get: Style(self: SoapBinding) -> SoapBindingStyle
        Set: Style(self: SoapBinding) = value
        """
        ...

    @property
    def Transport(self) -> str:
        """
        Get: Transport(self: SoapBinding) -> str
        Set: Transport(self: SoapBinding) = value
        """
        ...


    HttpTransport: str = ...
    Namespace: str = ...


class Soap12Binding(SoapBinding): # skipped bases: <type 'object'>
    """ Soap12Binding() """
    HttpTransport: str = ...
    Namespace: str = ...


class SoapBodyBinding(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ SoapBodyBinding() """
    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: SoapBodyBinding) -> str
        Set: Encoding(self: SoapBodyBinding) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: SoapBodyBinding) -> str
        Set: Namespace(self: SoapBodyBinding) = value
        """
        ...

    @property
    def Parts(self) -> Array:
        """
        Get: Parts(self: SoapBodyBinding) -> Array[str]
        Set: Parts(self: SoapBodyBinding) = value
        """
        ...

    @property
    def PartsString(self) -> str:
        """
        Get: PartsString(self: SoapBodyBinding) -> str
        Set: PartsString(self: SoapBodyBinding) = value
        """
        ...

    @property
    def Use(self) -> SoapBindingUse:
        """
        Get: Use(self: SoapBodyBinding) -> SoapBindingUse
        Set: Use(self: SoapBodyBinding) = value
        """
        ...



class Soap12BodyBinding(SoapBodyBinding): # skipped bases: <type 'object'>
    """ Soap12BodyBinding() """
    pass

class SoapFaultBinding(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ SoapFaultBinding() """
    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: SoapFaultBinding) -> str
        Set: Encoding(self: SoapFaultBinding) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SoapFaultBinding) -> str
        Set: Name(self: SoapFaultBinding) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: SoapFaultBinding) -> str
        Set: Namespace(self: SoapFaultBinding) = value
        """
        ...

    @property
    def Use(self) -> SoapBindingUse:
        """
        Get: Use(self: SoapFaultBinding) -> SoapBindingUse
        Set: Use(self: SoapFaultBinding) = value
        """
        ...



class Soap12FaultBinding(SoapFaultBinding): # skipped bases: <type 'object'>
    """ Soap12FaultBinding() """
    pass

class SoapHeaderBinding(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ SoapHeaderBinding() """
    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: SoapHeaderBinding) -> str
        Set: Encoding(self: SoapHeaderBinding) = value
        """
        ...

    @property
    def Fault(self) -> SoapHeaderFaultBinding:
        """
        Get: Fault(self: SoapHeaderBinding) -> SoapHeaderFaultBinding
        Set: Fault(self: SoapHeaderBinding) = value
        """
        ...

    @property
    def MapToProperty(self) -> bool:
        """
        Get: MapToProperty(self: SoapHeaderBinding) -> bool
        Set: MapToProperty(self: SoapHeaderBinding) = value
        """
        ...

    @property
    def Message(self) -> XmlQualifiedName:
        """
        Get: Message(self: SoapHeaderBinding) -> XmlQualifiedName
        Set: Message(self: SoapHeaderBinding) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: SoapHeaderBinding) -> str
        Set: Namespace(self: SoapHeaderBinding) = value
        """
        ...

    @property
    def Part(self) -> str:
        """
        Get: Part(self: SoapHeaderBinding) -> str
        Set: Part(self: SoapHeaderBinding) = value
        """
        ...

    @property
    def Use(self) -> SoapBindingUse:
        """
        Get: Use(self: SoapHeaderBinding) -> SoapBindingUse
        Set: Use(self: SoapHeaderBinding) = value
        """
        ...



class Soap12HeaderBinding(SoapHeaderBinding): # skipped bases: <type 'object'>
    """ Soap12HeaderBinding() """
    pass

class SoapOperationBinding(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ SoapOperationBinding() """
    @property
    def SoapAction(self) -> str:
        """
        Get: SoapAction(self: SoapOperationBinding) -> str
        Set: SoapAction(self: SoapOperationBinding) = value
        """
        ...

    @property
    def Style(self) -> SoapBindingStyle:
        """
        Get: Style(self: SoapOperationBinding) -> SoapBindingStyle
        Set: Style(self: SoapOperationBinding) = value
        """
        ...



class Soap12OperationBinding(SoapOperationBinding): # skipped bases: <type 'object'>
    """ Soap12OperationBinding() """
    @property
    def SoapActionRequired(self) -> bool:
        """
        Get: SoapActionRequired(self: Soap12OperationBinding) -> bool
        Set: SoapActionRequired(self: Soap12OperationBinding) = value
        """
        ...



class SoapBindingStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SoapBindingStyle, values: Default (0), Document (1), Rpc (2) """
    Default: SoapBindingStyle = ...
    Document: SoapBindingStyle = ...
    Rpc: SoapBindingStyle = ...
    value__ = ...


class SoapBindingUse(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SoapBindingUse, values: Default (0), Encoded (1), Literal (2) """
    Default: SoapBindingUse = ...
    Encoded: SoapBindingUse = ...
    Literal: SoapBindingUse = ...
    value__ = ...


class SoapExtensionImporter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ImportContext(self) -> SoapProtocolImporter:
        """
        Get: ImportContext(self: SoapExtensionImporter) -> SoapProtocolImporter
        Set: ImportContext(self: SoapExtensionImporter) = value
        """
        ...


    def ImportMethod(self, metadata:CodeAttributeDeclarationCollection): # -> 
        """ ImportMethod(self: SoapExtensionImporter, metadata: CodeAttributeDeclarationCollection) """
        ...


class SoapExtensionReflector: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ReflectionContext(self) -> ProtocolReflector:
        """
        Get: ReflectionContext(self: SoapExtensionReflector) -> ProtocolReflector
        Set: ReflectionContext(self: SoapExtensionReflector) = value
        """
        ...


    def ReflectDescription(self): # -> 
        """ ReflectDescription(self: SoapExtensionReflector) """
        ...

    def ReflectMethod(self): # -> 
        """ ReflectMethod(self: SoapExtensionReflector) """
        ...


class SoapHeaderFaultBinding(ServiceDescriptionFormatExtension): # skipped bases: <type 'object'>
    """ SoapHeaderFaultBinding() """
    @property
    def Encoding(self) -> str:
        """
        Get: Encoding(self: SoapHeaderFaultBinding) -> str
        Set: Encoding(self: SoapHeaderFaultBinding) = value
        """
        ...

    @property
    def Message(self) -> XmlQualifiedName:
        """
        Get: Message(self: SoapHeaderFaultBinding) -> XmlQualifiedName
        Set: Message(self: SoapHeaderFaultBinding) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: SoapHeaderFaultBinding) -> str
        Set: Namespace(self: SoapHeaderFaultBinding) = value
        """
        ...

    @property
    def Part(self) -> str:
        """
        Get: Part(self: SoapHeaderFaultBinding) -> str
        Set: Part(self: SoapHeaderFaultBinding) = value
        """
        ...

    @property
    def Use(self) -> SoapBindingUse:
        """
        Get: Use(self: SoapHeaderFaultBinding) -> SoapBindingUse
        Set: Use(self: SoapHeaderFaultBinding) = value
        """
        ...



class SoapProtocolImporter(ProtocolImporter): # skipped bases: <type 'object'>
    """ SoapProtocolImporter() """
    @property
    def SoapBinding(self) -> SoapBinding:
        """ Get: SoapBinding(self: SoapProtocolImporter) -> SoapBinding """
        ...

    @property
    def SoapExporter(self) -> SoapCodeExporter:
        """ Get: SoapExporter(self: SoapProtocolImporter) -> SoapCodeExporter """
        ...

    @property
    def SoapImporter(self) -> SoapSchemaImporter:
        """ Get: SoapImporter(self: SoapProtocolImporter) -> SoapSchemaImporter """
        ...

    @property
    def XmlExporter(self) -> XmlCodeExporter:
        """ Get: XmlExporter(self: SoapProtocolImporter) -> XmlCodeExporter """
        ...

    @property
    def XmlImporter(self) -> XmlSchemaImporter:
        """ Get: XmlImporter(self: SoapProtocolImporter) -> XmlSchemaImporter """
        ...


    def IsSoapEncodingPresent(self, *args): #cannot find CLR method
        """ IsSoapEncodingPresent(self: SoapProtocolImporter, uriList: str) -> bool """
        ...


class SoapTransportImporter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ImportContext(self) -> SoapProtocolImporter:
        """
        Get: ImportContext(self: SoapTransportImporter) -> SoapProtocolImporter
        Set: ImportContext(self: SoapTransportImporter) = value
        """
        ...


    def ImportClass(self): # -> 
        """ ImportClass(self: SoapTransportImporter) """
        ...

    def IsSupportedTransport(self, transport:str) -> bool:
        """ IsSupportedTransport(self: SoapTransportImporter, transport: str) -> bool """
        ...


class Types(DocumentableItem): # skipped bases: <type 'object'>
    """ Types() """
    @property
    def Schemas(self) -> XmlSchemas:
        """ Get: Schemas(self: Types) -> XmlSchemas """
        ...



class WebReference: # skipped bases: <type 'object'>, <type 'object'>
    """
    WebReference(documents: DiscoveryClientDocumentCollection, proxyCode: CodeNamespace, protocolName: str, appSettingUrlKey: str, appSettingBaseUrl: str)
    WebReference(documents: DiscoveryClientDocumentCollection, proxyCode: CodeNamespace)
    WebReference(documents: DiscoveryClientDocumentCollection, proxyCode: CodeNamespace, appSettingUrlKey: str, appSettingBaseUrl: str)
    """
    @property
    def AppSettingBaseUrl(self) -> str:
        """ Get: AppSettingBaseUrl(self: WebReference) -> str """
        ...

    @property
    def AppSettingUrlKey(self) -> str:
        """ Get: AppSettingUrlKey(self: WebReference) -> str """
        ...

    @property
    def Documents(self) -> DiscoveryClientDocumentCollection:
        """ Get: Documents(self: WebReference) -> DiscoveryClientDocumentCollection """
        ...

    @property
    def ProtocolName(self) -> str:
        """
        Get: ProtocolName(self: WebReference) -> str
        Set: ProtocolName(self: WebReference) = value
        """
        ...

    @property
    def ProxyCode(self) -> CodeNamespace:
        """ Get: ProxyCode(self: WebReference) -> CodeNamespace """
        ...

    @property
    def ValidationWarnings(self) -> StringCollection:
        """ Get: ValidationWarnings(self: WebReference) -> StringCollection """
        ...

    @property
    def Warnings(self) -> ServiceDescriptionImportWarnings:
        """
        Get: Warnings(self: WebReference) -> ServiceDescriptionImportWarnings
        Set: Warnings(self: WebReference) = value
        """
        ...



class WebReferenceCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ WebReferenceCollection() """
    def Add(self, webReference:WebReference) -> int:
        """ Add(self: WebReferenceCollection, webReference: WebReference) -> int """
        ...

    def Contains(self, webReference:WebReference) -> bool:
        """ Contains(self: WebReferenceCollection, webReference: WebReference) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: WebReferenceCollection, array: Array[WebReference], index: int) """
        ...

    def IndexOf(self, webReference:WebReference) -> int:
        """ IndexOf(self: WebReferenceCollection, webReference: WebReference) -> int """
        ...

    def Insert(self, index:int, webReference:WebReference): # -> 
        """ Insert(self: WebReferenceCollection, index: int, webReference: WebReference) """
        ...

    def Remove(self, webReference:WebReference): # -> 
        """ Remove(self: WebReferenceCollection, webReference: WebReference) """
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


class WebReferenceOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ WebReferenceOptions() """
    @property
    def CodeGenerationOptions(self) -> CodeGenerationOptions:
        """
        Get: CodeGenerationOptions(self: WebReferenceOptions) -> CodeGenerationOptions
        Set: CodeGenerationOptions(self: WebReferenceOptions) = value
        """
        ...

    @property
    def Schema(self) -> XmlSchema:
        """ Get: Schema() -> XmlSchema """
        ...

    @property
    def SchemaImporterExtensions(self) -> StringCollection:
        """ Get: SchemaImporterExtensions(self: WebReferenceOptions) -> StringCollection """
        ...

    @property
    def Style(self) -> ServiceDescriptionImportStyle:
        """
        Get: Style(self: WebReferenceOptions) -> ServiceDescriptionImportStyle
        Set: Style(self: WebReferenceOptions) = value
        """
        ...

    @property
    def Verbose(self) -> bool:
        """
        Get: Verbose(self: WebReferenceOptions) -> bool
        Set: Verbose(self: WebReferenceOptions) = value
        """
        ...


    @staticmethod
    def Read(*__args) -> WebReferenceOptions:
        """
        Read(reader: TextReader, validationEventHandler: ValidationEventHandler) -> WebReferenceOptions
        Read(stream: Stream, validationEventHandler: ValidationEventHandler) -> WebReferenceOptions
        Read(xmlReader: XmlReader, validationEventHandler: ValidationEventHandler) -> WebReferenceOptions
        """
        ...

    TargetNamespace: str = ...


class WebServicesInteroperability: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CheckConformance(claims, *__args) -> bool:
        """
        CheckConformance(claims: WsiProfiles, description: ServiceDescription, violations: BasicProfileViolationCollection) -> bool
        CheckConformance(claims: WsiProfiles, descriptions: ServiceDescriptionCollection, violations: BasicProfileViolationCollection) -> bool
        CheckConformance(claims: WsiProfiles, webReference: WebReference, violations: BasicProfileViolationCollection) -> bool
        """
        ...


