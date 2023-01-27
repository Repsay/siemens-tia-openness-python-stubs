# encoding: utf-8
# module System.Xml.Schema calls itself Schema
# from System.Xml.Linq, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Xml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Office.Interop.Excel import XmlSchema

from System import (Array, AsyncCallback, Decimal, Enum, EventArgs, 
    IAsyncResult, ICloneable, MulticastDelegate, SystemException, Type, Uri)

from System.Collections import (ArrayList, CollectionBase, ICollection, 
    IDictionaryEnumerator, IEnumerator)

from System.IO import Stream, TextReader

from System.Xml.Linq import XDocument, XElement

from System.Xml.Serialization import XmlSerializerNamespaces

"""The following names are not found in the module: (BoundEvent, IXmlLineInfo, 
    IXmlNamespaceResolver, IXmlSchemaInfo, InferenceOption, 
    ValidationEventHandler, XPathItem, XmlNameTable, XmlQualifiedName, 
    XmlReader, XmlResolver, XmlSchemaAnnotation, XmlSchemaAttribute, 
    XmlSchemaCollectionEnumerator, XmlSchemaComplexType, XmlSchemaContent, 
    XmlSchemaContentProcessing, XmlSchemaContentType, XmlSchemaDatatype, 
    XmlSchemaDatatypeVariety, XmlSchemaDerivationMethod, XmlSchemaElement, 
    XmlSchemaException, XmlSchemaForm, XmlSchemaObjectCollection, 
    XmlSchemaObjectTable, XmlSchemaSet, XmlSchemaSimpleType, 
    XmlSchemaSimpleTypeContent, XmlSchemaType, XmlSchemaUse, 
    XmlSchemaValidity, XmlSchemaXPath, XmlSeverityType, XmlTokenizedType, 
    XmlTypeCode, field#)
"""

# no functions
# classes

class Extensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetSchemaInfo(source:XElement): # -> IXmlSchemaInfo
        """
        GetSchemaInfo(source: XElement) -> IXmlSchemaInfo
        GetSchemaInfo(source: XAttribute) -> IXmlSchemaInfo
        """
        ...

    @staticmethod
    def Validate(source, *__args): # -> 
        """ Validate(source: XDocument, schemas: XmlSchemaSet, validationEventHandler: ValidationEventHandler)Validate(source: XDocument, schemas: XmlSchemaSet, validationEventHandler: ValidationEventHandler, addSchemaInfo: bool)Validate(source: XElement, partialValidationType: XmlSchemaObject, schemas: XmlSchemaSet, validationEventHandler: ValidationEventHandler)Validate(source: XElement, partialValidationType: XmlSchemaObject, schemas: XmlSchemaSet, validationEventHandler: ValidationEventHandler, addSchemaInfo: bool)Validate(source: XAttribute, partialValidationType: XmlSchemaObject, schemas: XmlSchemaSet, validationEventHandler: ValidationEventHandler)Validate(source: XAttribute, partialValidationType: XmlSchemaObject, schemas: XmlSchemaSet, validationEventHandler: ValidationEventHandler, addSchemaInfo: bool) """
        ...

    __all__: list = ...


class IXmlSchemaInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsDefault(self) -> bool:
        """ Get: IsDefault(self: IXmlSchemaInfo) -> bool """
        ...

    @property
    def IsNil(self) -> bool:
        """ Get: IsNil(self: IXmlSchemaInfo) -> bool """
        ...

    @property
    def MemberType(self): # -> XmlSchemaSimpleType
        """ Get: MemberType(self: IXmlSchemaInfo) -> XmlSchemaSimpleType """
        ...

    @property
    def SchemaAttribute(self): # -> XmlSchemaAttribute
        """ Get: SchemaAttribute(self: IXmlSchemaInfo) -> XmlSchemaAttribute """
        ...

    @property
    def SchemaElement(self): # -> XmlSchemaElement
        """ Get: SchemaElement(self: IXmlSchemaInfo) -> XmlSchemaElement """
        ...

    @property
    def SchemaType(self): # -> XmlSchemaType
        """ Get: SchemaType(self: IXmlSchemaInfo) -> XmlSchemaType """
        ...

    @property
    def Validity(self): # -> XmlSchemaValidity
        """ Get: Validity(self: IXmlSchemaInfo) -> XmlSchemaValidity """
        ...



class ValidationEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Exception(self): # -> XmlSchemaException
        """ Get: Exception(self: ValidationEventArgs) -> XmlSchemaException """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: ValidationEventArgs) -> str """
        ...

    @property
    def Severity(self): # -> XmlSeverityType
        """ Get: Severity(self: ValidationEventArgs) -> XmlSeverityType """
        ...



class ValidationEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ValidationEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ValidationEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ValidationEventHandler, sender: object, e: ValidationEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ValidationEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ValidationEventArgs): # -> 
        """ Invoke(self: ValidationEventHandler, sender: object, e: ValidationEventArgs) """
        ...


class XmlAtomicValue(ICloneable, XPathItem): # skipped bases: <type 'object'>
    """ no doc """
    def ToString(self) -> str:
        """ ToString(self: XmlAtomicValue) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class XmlSchemaObject: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def LineNumber(self) -> int:
        """
        Get: LineNumber(self: XmlSchemaObject) -> int
        Set: LineNumber(self: XmlSchemaObject) = value
        """
        ...

    @property
    def LinePosition(self) -> int:
        """
        Get: LinePosition(self: XmlSchemaObject) -> int
        Set: LinePosition(self: XmlSchemaObject) = value
        """
        ...

    @property
    def Namespaces(self) -> XmlSerializerNamespaces:
        """
        Get: Namespaces(self: XmlSchemaObject) -> XmlSerializerNamespaces
        Set: Namespaces(self: XmlSchemaObject) = value
        """
        ...

    @property
    def Parent(self) -> XmlSchemaObject:
        """
        Get: Parent(self: XmlSchemaObject) -> XmlSchemaObject
        Set: Parent(self: XmlSchemaObject) = value
        """
        ...

    @property
    def SourceUri(self) -> str:
        """
        Get: SourceUri(self: XmlSchemaObject) -> str
        Set: SourceUri(self: XmlSchemaObject) = value
        """
        ...



class XmlSchema(XmlSchemaObject): # skipped bases: <type 'object'>
    """ XmlSchema() """
    @property
    def AttributeFormDefault(self): # -> XmlSchemaForm
        """
        Get: AttributeFormDefault(self: XmlSchema) -> XmlSchemaForm
        Set: AttributeFormDefault(self: XmlSchema) = value
        """
        ...

    @property
    def AttributeGroups(self): # -> XmlSchemaObjectTable
        """ Get: AttributeGroups(self: XmlSchema) -> XmlSchemaObjectTable """
        ...

    @property
    def Attributes(self): # -> XmlSchemaObjectTable
        """ Get: Attributes(self: XmlSchema) -> XmlSchemaObjectTable """
        ...

    @property
    def BlockDefault(self): # -> XmlSchemaDerivationMethod
        """
        Get: BlockDefault(self: XmlSchema) -> XmlSchemaDerivationMethod
        Set: BlockDefault(self: XmlSchema) = value
        """
        ...

    @property
    def ElementFormDefault(self): # -> XmlSchemaForm
        """
        Get: ElementFormDefault(self: XmlSchema) -> XmlSchemaForm
        Set: ElementFormDefault(self: XmlSchema) = value
        """
        ...

    @property
    def Elements(self): # -> XmlSchemaObjectTable
        """ Get: Elements(self: XmlSchema) -> XmlSchemaObjectTable """
        ...

    @property
    def FinalDefault(self): # -> XmlSchemaDerivationMethod
        """
        Get: FinalDefault(self: XmlSchema) -> XmlSchemaDerivationMethod
        Set: FinalDefault(self: XmlSchema) = value
        """
        ...

    @property
    def Groups(self): # -> XmlSchemaObjectTable
        """ Get: Groups(self: XmlSchema) -> XmlSchemaObjectTable """
        ...

    @property
    def Id(self) -> str:
        """
        Get: Id(self: XmlSchema) -> str
        Set: Id(self: XmlSchema) = value
        """
        ...

    @property
    def Includes(self): # -> XmlSchemaObjectCollection
        """ Get: Includes(self: XmlSchema) -> XmlSchemaObjectCollection """
        ...

    @property
    def IsCompiled(self) -> bool:
        """ Get: IsCompiled(self: XmlSchema) -> bool """
        ...

    @property
    def Items(self): # -> XmlSchemaObjectCollection
        """ Get: Items(self: XmlSchema) -> XmlSchemaObjectCollection """
        ...

    @property
    def Notations(self): # -> XmlSchemaObjectTable
        """ Get: Notations(self: XmlSchema) -> XmlSchemaObjectTable """
        ...

    @property
    def SchemaTypes(self): # -> XmlSchemaObjectTable
        """ Get: SchemaTypes(self: XmlSchema) -> XmlSchemaObjectTable """
        ...

    @property
    def TargetNamespace(self) -> str:
        """
        Get: TargetNamespace(self: XmlSchema) -> str
        Set: TargetNamespace(self: XmlSchema) = value
        """
        ...

    @property
    def UnhandledAttributes(self) -> Array:
        """
        Get: UnhandledAttributes(self: XmlSchema) -> Array[XmlAttribute]
        Set: UnhandledAttributes(self: XmlSchema) = value
        """
        ...

    @property
    def Version(self) -> str:
        """
        Get: Version(self: XmlSchema) -> str
        Set: Version(self: XmlSchema) = value
        """
        ...


    def Compile(self, validationEventHandler:ValidationEventHandler, resolver = ...): # ->  # Not found arg types: {'resolver': 'XmlResolver'}
        """ Compile(self: XmlSchema, validationEventHandler: ValidationEventHandler, resolver: XmlResolver)Compile(self: XmlSchema, validationEventHandler: ValidationEventHandler) """
        ...

    @staticmethod
    def Read(*__args) -> XmlSchema:
        """
        Read(reader: TextReader, validationEventHandler: ValidationEventHandler) -> XmlSchema
        Read(stream: Stream, validationEventHandler: ValidationEventHandler) -> XmlSchema
        Read(reader: XmlReader, validationEventHandler: ValidationEventHandler) -> XmlSchema
        """
        ...

    def Write(self, *__args:Stream): # -> 
        """ Write(self: XmlSchema, stream: Stream)Write(self: XmlSchema, stream: Stream, namespaceManager: XmlNamespaceManager)Write(self: XmlSchema, writer: TextWriter)Write(self: XmlSchema, writer: TextWriter, namespaceManager: XmlNamespaceManager)Write(self: XmlSchema, writer: XmlWriter)Write(self: XmlSchema, writer: XmlWriter, namespaceManager: XmlNamespaceManager) """
        ...

    InstanceNamespace: str = ...
    Namespace: str = ...


class XmlSchemaAnnotated(XmlSchemaObject): # skipped bases: <type 'object'>
    """ XmlSchemaAnnotated() """
    @property
    def Annotation(self): # -> XmlSchemaAnnotation
        """
        Get: Annotation(self: XmlSchemaAnnotated) -> XmlSchemaAnnotation
        Set: Annotation(self: XmlSchemaAnnotated) = value
        """
        ...

    @property
    def Id(self) -> str:
        """
        Get: Id(self: XmlSchemaAnnotated) -> str
        Set: Id(self: XmlSchemaAnnotated) = value
        """
        ...

    @property
    def UnhandledAttributes(self) -> Array:
        """
        Get: UnhandledAttributes(self: XmlSchemaAnnotated) -> Array[XmlAttribute]
        Set: UnhandledAttributes(self: XmlSchemaAnnotated) = value
        """
        ...



class XmlSchemaParticle(XmlSchemaAnnotated): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def MaxOccurs(self) -> Decimal:
        """
        Get: MaxOccurs(self: XmlSchemaParticle) -> Decimal
        Set: MaxOccurs(self: XmlSchemaParticle) = value
        """
        ...

    @property
    def MaxOccursString(self) -> str:
        """
        Get: MaxOccursString(self: XmlSchemaParticle) -> str
        Set: MaxOccursString(self: XmlSchemaParticle) = value
        """
        ...

    @property
    def MinOccurs(self) -> Decimal:
        """
        Get: MinOccurs(self: XmlSchemaParticle) -> Decimal
        Set: MinOccurs(self: XmlSchemaParticle) = value
        """
        ...

    @property
    def MinOccursString(self) -> str:
        """
        Get: MinOccursString(self: XmlSchemaParticle) -> str
        Set: MinOccursString(self: XmlSchemaParticle) = value
        """
        ...



class XmlSchemaGroupBase(XmlSchemaParticle): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Items(self): # -> XmlSchemaObjectCollection
        """ Get: Items(self: XmlSchemaGroupBase) -> XmlSchemaObjectCollection """
        ...



class XmlSchemaAll(XmlSchemaGroupBase): # skipped bases: <type 'object'>
    """ XmlSchemaAll() """
    pass

class XmlSchemaAnnotation(XmlSchemaObject): # skipped bases: <type 'object'>
    """ XmlSchemaAnnotation() """
    @property
    def Id(self) -> str:
        """
        Get: Id(self: XmlSchemaAnnotation) -> str
        Set: Id(self: XmlSchemaAnnotation) = value
        """
        ...

    @property
    def Items(self): # -> XmlSchemaObjectCollection
        """ Get: Items(self: XmlSchemaAnnotation) -> XmlSchemaObjectCollection """
        ...

    @property
    def UnhandledAttributes(self) -> Array:
        """
        Get: UnhandledAttributes(self: XmlSchemaAnnotation) -> Array[XmlAttribute]
        Set: UnhandledAttributes(self: XmlSchemaAnnotation) = value
        """
        ...



class XmlSchemaAny(XmlSchemaParticle): # skipped bases: <type 'object'>
    """ XmlSchemaAny() """
    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: XmlSchemaAny) -> str
        Set: Namespace(self: XmlSchemaAny) = value
        """
        ...

    @property
    def ProcessContents(self): # -> XmlSchemaContentProcessing
        """
        Get: ProcessContents(self: XmlSchemaAny) -> XmlSchemaContentProcessing
        Set: ProcessContents(self: XmlSchemaAny) = value
        """
        ...



class XmlSchemaAnyAttribute(XmlSchemaAnnotated): # skipped bases: <type 'object'>
    """ XmlSchemaAnyAttribute() """
    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: XmlSchemaAnyAttribute) -> str
        Set: Namespace(self: XmlSchemaAnyAttribute) = value
        """
        ...

    @property
    def ProcessContents(self): # -> XmlSchemaContentProcessing
        """
        Get: ProcessContents(self: XmlSchemaAnyAttribute) -> XmlSchemaContentProcessing
        Set: ProcessContents(self: XmlSchemaAnyAttribute) = value
        """
        ...



class XmlSchemaAppInfo(XmlSchemaObject): # skipped bases: <type 'object'>
    """ XmlSchemaAppInfo() """
    @property
    def Markup(self) -> Array:
        """
        Get: Markup(self: XmlSchemaAppInfo) -> Array[XmlNode]
        Set: Markup(self: XmlSchemaAppInfo) = value
        """
        ...

    @property
    def Source(self) -> str:
        """
        Get: Source(self: XmlSchemaAppInfo) -> str
        Set: Source(self: XmlSchemaAppInfo) = value
        """
        ...



class XmlSchemaAttribute(XmlSchemaAnnotated): # skipped bases: <type 'object'>
    """ XmlSchemaAttribute() """
    @property
    def AttributeSchemaType(self): # -> XmlSchemaSimpleType
        """ Get: AttributeSchemaType(self: XmlSchemaAttribute) -> XmlSchemaSimpleType """
        ...

    @property
    def AttributeType(self) -> object:
        """ Get: AttributeType(self: XmlSchemaAttribute) -> object """
        ...

    @property
    def DefaultValue(self) -> str:
        """
        Get: DefaultValue(self: XmlSchemaAttribute) -> str
        Set: DefaultValue(self: XmlSchemaAttribute) = value
        """
        ...

    @property
    def FixedValue(self) -> str:
        """
        Get: FixedValue(self: XmlSchemaAttribute) -> str
        Set: FixedValue(self: XmlSchemaAttribute) = value
        """
        ...

    @property
    def Form(self): # -> XmlSchemaForm
        """
        Get: Form(self: XmlSchemaAttribute) -> XmlSchemaForm
        Set: Form(self: XmlSchemaAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: XmlSchemaAttribute) -> str
        Set: Name(self: XmlSchemaAttribute) = value
        """
        ...

    @property
    def QualifiedName(self): # -> XmlQualifiedName
        """ Get: QualifiedName(self: XmlSchemaAttribute) -> XmlQualifiedName """
        ...

    @property
    def RefName(self): # -> XmlQualifiedName
        """
        Get: RefName(self: XmlSchemaAttribute) -> XmlQualifiedName
        Set: RefName(self: XmlSchemaAttribute) = value
        """
        ...

    @property
    def SchemaType(self): # -> XmlSchemaSimpleType
        """
        Get: SchemaType(self: XmlSchemaAttribute) -> XmlSchemaSimpleType
        Set: SchemaType(self: XmlSchemaAttribute) = value
        """
        ...

    @property
    def SchemaTypeName(self): # -> XmlQualifiedName
        """
        Get: SchemaTypeName(self: XmlSchemaAttribute) -> XmlQualifiedName
        Set: SchemaTypeName(self: XmlSchemaAttribute) = value
        """
        ...

    @property
    def Use(self): # -> XmlSchemaUse
        """
        Get: Use(self: XmlSchemaAttribute) -> XmlSchemaUse
        Set: Use(self: XmlSchemaAttribute) = value
        """
        ...



class XmlSchemaAttributeGroup(XmlSchemaAnnotated): # skipped bases: <type 'object'>
    """ XmlSchemaAttributeGroup() """
    @property
    def AnyAttribute(self) -> XmlSchemaAnyAttribute:
        """
        Get: AnyAttribute(self: XmlSchemaAttributeGroup) -> XmlSchemaAnyAttribute
        Set: AnyAttribute(self: XmlSchemaAttributeGroup) = value
        """
        ...

    @property
    def Attributes(self): # -> XmlSchemaObjectCollection
        """ Get: Attributes(self: XmlSchemaAttributeGroup) -> XmlSchemaObjectCollection """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: XmlSchemaAttributeGroup) -> str
        Set: Name(self: XmlSchemaAttributeGroup) = value
        """
        ...

    @property
    def QualifiedName(self): # -> XmlQualifiedName
        """ Get: QualifiedName(self: XmlSchemaAttributeGroup) -> XmlQualifiedName """
        ...

    @property
    def RedefinedAttributeGroup(self) -> XmlSchemaAttributeGroup:
        """ Get: RedefinedAttributeGroup(self: XmlSchemaAttributeGroup) -> XmlSchemaAttributeGroup """
        ...



class XmlSchemaAttributeGroupRef(XmlSchemaAnnotated): # skipped bases: <type 'object'>
    """ XmlSchemaAttributeGroupRef() """
    @property
    def RefName(self): # -> XmlQualifiedName
        """
        Get: RefName(self: XmlSchemaAttributeGroupRef) -> XmlQualifiedName
        Set: RefName(self: XmlSchemaAttributeGroupRef) = value
        """
        ...



class XmlSchemaChoice(XmlSchemaGroupBase): # skipped bases: <type 'object'>
    """ XmlSchemaChoice() """
    pass

class XmlSchemaCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    XmlSchemaCollection()
    XmlSchemaCollection(nametable: XmlNameTable)
    """
    @property
    def NameTable(self): # -> XmlNameTable
        """ Get: NameTable(self: XmlSchemaCollection) -> XmlNameTable """
        ...


    def Add(self, *__args:XmlSchema) -> XmlSchema:
        """
        Add(self: XmlSchemaCollection, ns: str, uri: str) -> XmlSchema
        Add(self: XmlSchemaCollection, ns: str, reader: XmlReader) -> XmlSchema
        Add(self: XmlSchemaCollection, ns: str, reader: XmlReader, resolver: XmlResolver) -> XmlSchema
        Add(self: XmlSchemaCollection, schema: XmlSchema) -> XmlSchema
        Add(self: XmlSchemaCollection, schema: XmlSchema, resolver: XmlResolver) -> XmlSchema
        Add(self: XmlSchemaCollection, schema: XmlSchemaCollection)
        """
        ...

    def Contains(self, *__args:XmlSchema) -> bool:
        """
        Contains(self: XmlSchemaCollection, schema: XmlSchema) -> bool
        Contains(self: XmlSchemaCollection, ns: str) -> bool
        """
        ...

    def GetEnumerator(self): # -> XmlSchemaCollectionEnumerator
        """ GetEnumerator(self: XmlSchemaCollection) -> XmlSchemaCollectionEnumerator """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    ValidationEventHandler = ...


class XmlSchemaCollectionEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class XmlSchemaCompilationSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ XmlSchemaCompilationSettings() """
    @property
    def EnableUpaCheck(self) -> bool:
        """
        Get: EnableUpaCheck(self: XmlSchemaCompilationSettings) -> bool
        Set: EnableUpaCheck(self: XmlSchemaCompilationSettings) = value
        """
        ...



class XmlSchemaContentModel(XmlSchemaAnnotated): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Content(self): # -> XmlSchemaContent
        """
        Get: Content(self: XmlSchemaContentModel) -> XmlSchemaContent
        Set: Content(self: XmlSchemaContentModel) = value
        """
        ...



class XmlSchemaComplexContent(XmlSchemaContentModel): # skipped bases: <type 'object'>
    """ XmlSchemaComplexContent() """
    @property
    def IsMixed(self) -> bool:
        """
        Get: IsMixed(self: XmlSchemaComplexContent) -> bool
        Set: IsMixed(self: XmlSchemaComplexContent) = value
        """
        ...



class XmlSchemaContent(XmlSchemaAnnotated): # skipped bases: <type 'object'>
    """ no doc """
    pass

class XmlSchemaComplexContentExtension(XmlSchemaContent): # skipped bases: <type 'object'>
    """ XmlSchemaComplexContentExtension() """
    @property
    def AnyAttribute(self) -> XmlSchemaAnyAttribute:
        """
        Get: AnyAttribute(self: XmlSchemaComplexContentExtension) -> XmlSchemaAnyAttribute
        Set: AnyAttribute(self: XmlSchemaComplexContentExtension) = value
        """
        ...

    @property
    def Attributes(self): # -> XmlSchemaObjectCollection
        """ Get: Attributes(self: XmlSchemaComplexContentExtension) -> XmlSchemaObjectCollection """
        ...

    @property
    def BaseTypeName(self): # -> XmlQualifiedName
        """
        Get: BaseTypeName(self: XmlSchemaComplexContentExtension) -> XmlQualifiedName
        Set: BaseTypeName(self: XmlSchemaComplexContentExtension) = value
        """
        ...

    @property
    def Particle(self) -> XmlSchemaParticle:
        """
        Get: Particle(self: XmlSchemaComplexContentExtension) -> XmlSchemaParticle
        Set: Particle(self: XmlSchemaComplexContentExtension) = value
        """
        ...



class XmlSchemaComplexContentRestriction(XmlSchemaContent): # skipped bases: <type 'object'>
    """ XmlSchemaComplexContentRestriction() """
    @property
    def AnyAttribute(self) -> XmlSchemaAnyAttribute:
        """
        Get: AnyAttribute(self: XmlSchemaComplexContentRestriction) -> XmlSchemaAnyAttribute
        Set: AnyAttribute(self: XmlSchemaComplexContentRestriction) = value
        """
        ...

    @property
    def Attributes(self): # -> XmlSchemaObjectCollection
        """ Get: Attributes(self: XmlSchemaComplexContentRestriction) -> XmlSchemaObjectCollection """
        ...

    @property
    def BaseTypeName(self): # -> XmlQualifiedName
        """
        Get: BaseTypeName(self: XmlSchemaComplexContentRestriction) -> XmlQualifiedName
        Set: BaseTypeName(self: XmlSchemaComplexContentRestriction) = value
        """
        ...

    @property
    def Particle(self) -> XmlSchemaParticle:
        """
        Get: Particle(self: XmlSchemaComplexContentRestriction) -> XmlSchemaParticle
        Set: Particle(self: XmlSchemaComplexContentRestriction) = value
        """
        ...



class XmlSchemaType(XmlSchemaAnnotated): # skipped bases: <type 'object'>
    """ XmlSchemaType() """
    @property
    def BaseSchemaType(self) -> object:
        """ Get: BaseSchemaType(self: XmlSchemaType) -> object """
        ...

    @property
    def BaseXmlSchemaType(self) -> XmlSchemaType:
        """ Get: BaseXmlSchemaType(self: XmlSchemaType) -> XmlSchemaType """
        ...

    @property
    def Datatype(self): # -> XmlSchemaDatatype
        """ Get: Datatype(self: XmlSchemaType) -> XmlSchemaDatatype """
        ...

    @property
    def DerivedBy(self): # -> XmlSchemaDerivationMethod
        """ Get: DerivedBy(self: XmlSchemaType) -> XmlSchemaDerivationMethod """
        ...

    @property
    def Final(self): # -> XmlSchemaDerivationMethod
        """
        Get: Final(self: XmlSchemaType) -> XmlSchemaDerivationMethod
        Set: Final(self: XmlSchemaType) = value
        """
        ...

    @property
    def FinalResolved(self): # -> XmlSchemaDerivationMethod
        """ Get: FinalResolved(self: XmlSchemaType) -> XmlSchemaDerivationMethod """
        ...

    @property
    def IsMixed(self) -> bool:
        """
        Get: IsMixed(self: XmlSchemaType) -> bool
        Set: IsMixed(self: XmlSchemaType) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: XmlSchemaType) -> str
        Set: Name(self: XmlSchemaType) = value
        """
        ...

    @property
    def QualifiedName(self): # -> XmlQualifiedName
        """ Get: QualifiedName(self: XmlSchemaType) -> XmlQualifiedName """
        ...

    @property
    def TypeCode(self): # -> XmlTypeCode
        """ Get: TypeCode(self: XmlSchemaType) -> XmlTypeCode """
        ...


    @staticmethod
    def GetBuiltInComplexType(*__args): # -> XmlSchemaComplexType # Not found arg types: {'*__args': 'XmlTypeCode'}
        """
        GetBuiltInComplexType(typeCode: XmlTypeCode) -> XmlSchemaComplexType
        GetBuiltInComplexType(qualifiedName: XmlQualifiedName) -> XmlSchemaComplexType
        """
        ...

    @staticmethod
    def GetBuiltInSimpleType(*__args): # -> XmlSchemaSimpleType # Not found arg types: {'*__args': 'XmlQualifiedName'}
        """
        GetBuiltInSimpleType(qualifiedName: XmlQualifiedName) -> XmlSchemaSimpleType
        GetBuiltInSimpleType(typeCode: XmlTypeCode) -> XmlSchemaSimpleType
        """
        ...

    @staticmethod
    def IsDerivedFrom(derivedType:XmlSchemaType, baseType:XmlSchemaType, except_) -> bool: # Not found arg types: {'except_': 'XmlSchemaDerivationMethod'}
        """ IsDerivedFrom(derivedType: XmlSchemaType, baseType: XmlSchemaType, except: XmlSchemaDerivationMethod) -> bool """
        ...


class XmlSchemaComplexType(XmlSchemaType): # skipped bases: <type 'object'>
    """ XmlSchemaComplexType() """
    @property
    def AnyAttribute(self) -> XmlSchemaAnyAttribute:
        """
        Get: AnyAttribute(self: XmlSchemaComplexType) -> XmlSchemaAnyAttribute
        Set: AnyAttribute(self: XmlSchemaComplexType) = value
        """
        ...

    @property
    def Attributes(self): # -> XmlSchemaObjectCollection
        """ Get: Attributes(self: XmlSchemaComplexType) -> XmlSchemaObjectCollection """
        ...

    @property
    def AttributeUses(self): # -> XmlSchemaObjectTable
        """ Get: AttributeUses(self: XmlSchemaComplexType) -> XmlSchemaObjectTable """
        ...

    @property
    def AttributeWildcard(self) -> XmlSchemaAnyAttribute:
        """ Get: AttributeWildcard(self: XmlSchemaComplexType) -> XmlSchemaAnyAttribute """
        ...

    @property
    def Block(self): # -> XmlSchemaDerivationMethod
        """
        Get: Block(self: XmlSchemaComplexType) -> XmlSchemaDerivationMethod
        Set: Block(self: XmlSchemaComplexType) = value
        """
        ...

    @property
    def BlockResolved(self): # -> XmlSchemaDerivationMethod
        """ Get: BlockResolved(self: XmlSchemaComplexType) -> XmlSchemaDerivationMethod """
        ...

    @property
    def ContentModel(self) -> XmlSchemaContentModel:
        """
        Get: ContentModel(self: XmlSchemaComplexType) -> XmlSchemaContentModel
        Set: ContentModel(self: XmlSchemaComplexType) = value
        """
        ...

    @property
    def ContentType(self): # -> XmlSchemaContentType
        """ Get: ContentType(self: XmlSchemaComplexType) -> XmlSchemaContentType """
        ...

    @property
    def ContentTypeParticle(self) -> XmlSchemaParticle:
        """ Get: ContentTypeParticle(self: XmlSchemaComplexType) -> XmlSchemaParticle """
        ...

    @property
    def IsAbstract(self) -> bool:
        """
        Get: IsAbstract(self: XmlSchemaComplexType) -> bool
        Set: IsAbstract(self: XmlSchemaComplexType) = value
        """
        ...

    @property
    def Particle(self) -> XmlSchemaParticle:
        """
        Get: Particle(self: XmlSchemaComplexType) -> XmlSchemaParticle
        Set: Particle(self: XmlSchemaComplexType) = value
        """
        ...



class XmlSchemaContentProcessing(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlSchemaContentProcessing, values: Lax (2), None (0), Skip (1), Strict (3) """
    Lax: XmlSchemaContentProcessing = ...
    Skip: XmlSchemaContentProcessing = ...
    Strict: XmlSchemaContentProcessing = ...
    value__ = ...


class XmlSchemaContentType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlSchemaContentType, values: ElementOnly (2), Empty (1), Mixed (3), TextOnly (0) """
    ElementOnly: XmlSchemaContentType = ...
    Empty: XmlSchemaContentType = ...
    Mixed: XmlSchemaContentType = ...
    TextOnly: XmlSchemaContentType = ...
    value__ = ...


class XmlSchemaDatatype: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def TokenizedType(self): # -> XmlTokenizedType
        """ Get: TokenizedType(self: XmlSchemaDatatype) -> XmlTokenizedType """
        ...

    @property
    def TypeCode(self): # -> XmlTypeCode
        """ Get: TypeCode(self: XmlSchemaDatatype) -> XmlTypeCode """
        ...

    @property
    def ValueType(self) -> Type:
        """ Get: ValueType(self: XmlSchemaDatatype) -> Type """
        ...

    @property
    def Variety(self): # -> XmlSchemaDatatypeVariety
        """ Get: Variety(self: XmlSchemaDatatype) -> XmlSchemaDatatypeVariety """
        ...


    def ChangeType(self, value:object, targetType:Type, namespaceResolver = ...) -> object: # Not found arg types: {'namespaceResolver': 'IXmlNamespaceResolver'}
        """
        ChangeType(self: XmlSchemaDatatype, value: object, targetType: Type) -> object
        ChangeType(self: XmlSchemaDatatype, value: object, targetType: Type, namespaceResolver: IXmlNamespaceResolver) -> object
        """
        ...

    def IsDerivedFrom(self, datatype:XmlSchemaDatatype) -> bool:
        """ IsDerivedFrom(self: XmlSchemaDatatype, datatype: XmlSchemaDatatype) -> bool """
        ...

    def ParseValue(self, s:str, nameTable, nsmgr) -> object: # Not found arg types: {'nsmgr': 'IXmlNamespaceResolver', 'nameTable': 'XmlNameTable'}
        """ ParseValue(self: XmlSchemaDatatype, s: str, nameTable: XmlNameTable, nsmgr: IXmlNamespaceResolver) -> object """
        ...


class XmlSchemaDatatypeVariety(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlSchemaDatatypeVariety, values: Atomic (0), List (1), Union (2) """
    Atomic: XmlSchemaDatatypeVariety = ...
    List: XmlSchemaDatatypeVariety = ...
    Union: XmlSchemaDatatypeVariety = ...
    value__ = ...


class XmlSchemaDerivationMethod(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) XmlSchemaDerivationMethod, values: All (255), Empty (0), Extension (2), List (8), None (256), Restriction (4), Substitution (1), Union (16) """
    All: XmlSchemaDerivationMethod = ...
    Empty: XmlSchemaDerivationMethod = ...
    Extension: XmlSchemaDerivationMethod = ...
    List: XmlSchemaDerivationMethod = ...
    Restriction: XmlSchemaDerivationMethod = ...
    Substitution: XmlSchemaDerivationMethod = ...
    Union: XmlSchemaDerivationMethod = ...
    value__ = ...


class XmlSchemaDocumentation(XmlSchemaObject): # skipped bases: <type 'object'>
    """ XmlSchemaDocumentation() """
    @property
    def Language(self) -> str:
        """
        Get: Language(self: XmlSchemaDocumentation) -> str
        Set: Language(self: XmlSchemaDocumentation) = value
        """
        ...

    @property
    def Markup(self) -> Array:
        """
        Get: Markup(self: XmlSchemaDocumentation) -> Array[XmlNode]
        Set: Markup(self: XmlSchemaDocumentation) = value
        """
        ...

    @property
    def Source(self) -> str:
        """
        Get: Source(self: XmlSchemaDocumentation) -> str
        Set: Source(self: XmlSchemaDocumentation) = value
        """
        ...



class XmlSchemaElement(XmlSchemaParticle): # skipped bases: <type 'object'>
    """ XmlSchemaElement() """
    @property
    def Block(self) -> XmlSchemaDerivationMethod:
        """
        Get: Block(self: XmlSchemaElement) -> XmlSchemaDerivationMethod
        Set: Block(self: XmlSchemaElement) = value
        """
        ...

    @property
    def BlockResolved(self) -> XmlSchemaDerivationMethod:
        """ Get: BlockResolved(self: XmlSchemaElement) -> XmlSchemaDerivationMethod """
        ...

    @property
    def Constraints(self): # -> XmlSchemaObjectCollection
        """ Get: Constraints(self: XmlSchemaElement) -> XmlSchemaObjectCollection """
        ...

    @property
    def DefaultValue(self) -> str:
        """
        Get: DefaultValue(self: XmlSchemaElement) -> str
        Set: DefaultValue(self: XmlSchemaElement) = value
        """
        ...

    @property
    def ElementSchemaType(self) -> XmlSchemaType:
        """ Get: ElementSchemaType(self: XmlSchemaElement) -> XmlSchemaType """
        ...

    @property
    def ElementType(self) -> object:
        """ Get: ElementType(self: XmlSchemaElement) -> object """
        ...

    @property
    def Final(self) -> XmlSchemaDerivationMethod:
        """
        Get: Final(self: XmlSchemaElement) -> XmlSchemaDerivationMethod
        Set: Final(self: XmlSchemaElement) = value
        """
        ...

    @property
    def FinalResolved(self) -> XmlSchemaDerivationMethod:
        """ Get: FinalResolved(self: XmlSchemaElement) -> XmlSchemaDerivationMethod """
        ...

    @property
    def FixedValue(self) -> str:
        """
        Get: FixedValue(self: XmlSchemaElement) -> str
        Set: FixedValue(self: XmlSchemaElement) = value
        """
        ...

    @property
    def Form(self): # -> XmlSchemaForm
        """
        Get: Form(self: XmlSchemaElement) -> XmlSchemaForm
        Set: Form(self: XmlSchemaElement) = value
        """
        ...

    @property
    def IsAbstract(self) -> bool:
        """
        Get: IsAbstract(self: XmlSchemaElement) -> bool
        Set: IsAbstract(self: XmlSchemaElement) = value
        """
        ...

    @property
    def IsNillable(self) -> bool:
        """
        Get: IsNillable(self: XmlSchemaElement) -> bool
        Set: IsNillable(self: XmlSchemaElement) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: XmlSchemaElement) -> str
        Set: Name(self: XmlSchemaElement) = value
        """
        ...

    @property
    def QualifiedName(self): # -> XmlQualifiedName
        """ Get: QualifiedName(self: XmlSchemaElement) -> XmlQualifiedName """
        ...

    @property
    def RefName(self): # -> XmlQualifiedName
        """
        Get: RefName(self: XmlSchemaElement) -> XmlQualifiedName
        Set: RefName(self: XmlSchemaElement) = value
        """
        ...

    @property
    def SchemaType(self) -> XmlSchemaType:
        """
        Get: SchemaType(self: XmlSchemaElement) -> XmlSchemaType
        Set: SchemaType(self: XmlSchemaElement) = value
        """
        ...

    @property
    def SchemaTypeName(self): # -> XmlQualifiedName
        """
        Get: SchemaTypeName(self: XmlSchemaElement) -> XmlQualifiedName
        Set: SchemaTypeName(self: XmlSchemaElement) = value
        """
        ...

    @property
    def SubstitutionGroup(self): # -> XmlQualifiedName
        """
        Get: SubstitutionGroup(self: XmlSchemaElement) -> XmlQualifiedName
        Set: SubstitutionGroup(self: XmlSchemaElement) = value
        """
        ...



class XmlSchemaFacet(XmlSchemaAnnotated): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsFixed(self) -> bool:
        """
        Get: IsFixed(self: XmlSchemaFacet) -> bool
        Set: IsFixed(self: XmlSchemaFacet) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: XmlSchemaFacet) -> str
        Set: Value(self: XmlSchemaFacet) = value
        """
        ...



class XmlSchemaEnumerationFacet(XmlSchemaFacet): # skipped bases: <type 'object'>
    """ XmlSchemaEnumerationFacet() """
    pass

class XmlSchemaException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XmlSchemaException()
    XmlSchemaException(message: str)
    XmlSchemaException(message: str, innerException: Exception)
    XmlSchemaException(message: str, innerException: Exception, lineNumber: int, linePosition: int)
    """
    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: XmlSchemaException) -> int """
        ...

    @property
    def LinePosition(self) -> int:
        """ Get: LinePosition(self: XmlSchemaException) -> int """
        ...

    @property
    def SourceSchemaObject(self) -> XmlSchemaObject:
        """ Get: SourceSchemaObject(self: XmlSchemaException) -> XmlSchemaObject """
        ...

    @property
    def SourceUri(self) -> str:
        """ Get: SourceUri(self: XmlSchemaException) -> str """
        ...


    SerializeObjectState = ...


class XmlSchemaExternal(XmlSchemaObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Id(self) -> str:
        """
        Get: Id(self: XmlSchemaExternal) -> str
        Set: Id(self: XmlSchemaExternal) = value
        """
        ...

    @property
    def Schema(self) -> XmlSchema:
        """
        Get: Schema(self: XmlSchemaExternal) -> XmlSchema
        Set: Schema(self: XmlSchemaExternal) = value
        """
        ...

    @property
    def SchemaLocation(self) -> str:
        """
        Get: SchemaLocation(self: XmlSchemaExternal) -> str
        Set: SchemaLocation(self: XmlSchemaExternal) = value
        """
        ...

    @property
    def UnhandledAttributes(self) -> Array:
        """
        Get: UnhandledAttributes(self: XmlSchemaExternal) -> Array[XmlAttribute]
        Set: UnhandledAttributes(self: XmlSchemaExternal) = value
        """
        ...



class XmlSchemaForm(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlSchemaForm, values: None (0), Qualified (1), Unqualified (2) """
    Qualified: XmlSchemaForm = ...
    Unqualified: XmlSchemaForm = ...
    value__ = ...


class XmlSchemaNumericFacet(XmlSchemaFacet): # skipped bases: <type 'object'>
    """ no doc """
    pass

class XmlSchemaFractionDigitsFacet(XmlSchemaNumericFacet): # skipped bases: <type 'object'>
    """ XmlSchemaFractionDigitsFacet() """
    pass

class XmlSchemaGroup(XmlSchemaAnnotated): # skipped bases: <type 'object'>
    """ XmlSchemaGroup() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: XmlSchemaGroup) -> str
        Set: Name(self: XmlSchemaGroup) = value
        """
        ...

    @property
    def Particle(self) -> XmlSchemaGroupBase:
        """
        Get: Particle(self: XmlSchemaGroup) -> XmlSchemaGroupBase
        Set: Particle(self: XmlSchemaGroup) = value
        """
        ...

    @property
    def QualifiedName(self): # -> XmlQualifiedName
        """ Get: QualifiedName(self: XmlSchemaGroup) -> XmlQualifiedName """
        ...



class XmlSchemaGroupRef(XmlSchemaParticle): # skipped bases: <type 'object'>
    """ XmlSchemaGroupRef() """
    @property
    def Particle(self) -> XmlSchemaGroupBase:
        """ Get: Particle(self: XmlSchemaGroupRef) -> XmlSchemaGroupBase """
        ...

    @property
    def RefName(self): # -> XmlQualifiedName
        """
        Get: RefName(self: XmlSchemaGroupRef) -> XmlQualifiedName
        Set: RefName(self: XmlSchemaGroupRef) = value
        """
        ...



class XmlSchemaIdentityConstraint(XmlSchemaAnnotated): # skipped bases: <type 'object'>
    """ XmlSchemaIdentityConstraint() """
    @property
    def Fields(self): # -> XmlSchemaObjectCollection
        """ Get: Fields(self: XmlSchemaIdentityConstraint) -> XmlSchemaObjectCollection """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: XmlSchemaIdentityConstraint) -> str
        Set: Name(self: XmlSchemaIdentityConstraint) = value
        """
        ...

    @property
    def QualifiedName(self): # -> XmlQualifiedName
        """ Get: QualifiedName(self: XmlSchemaIdentityConstraint) -> XmlQualifiedName """
        ...

    @property
    def Selector(self): # -> XmlSchemaXPath
        """
        Get: Selector(self: XmlSchemaIdentityConstraint) -> XmlSchemaXPath
        Set: Selector(self: XmlSchemaIdentityConstraint) = value
        """
        ...



class XmlSchemaImport(XmlSchemaExternal): # skipped bases: <type 'object'>
    """ XmlSchemaImport() """
    @property
    def Annotation(self) -> XmlSchemaAnnotation:
        """
        Get: Annotation(self: XmlSchemaImport) -> XmlSchemaAnnotation
        Set: Annotation(self: XmlSchemaImport) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: XmlSchemaImport) -> str
        Set: Namespace(self: XmlSchemaImport) = value
        """
        ...



class XmlSchemaInclude(XmlSchemaExternal): # skipped bases: <type 'object'>
    """ XmlSchemaInclude() """
    @property
    def Annotation(self) -> XmlSchemaAnnotation:
        """
        Get: Annotation(self: XmlSchemaInclude) -> XmlSchemaAnnotation
        Set: Annotation(self: XmlSchemaInclude) = value
        """
        ...



class XmlSchemaInference: # skipped bases: <type 'object'>, <type 'object'>
    """ XmlSchemaInference() """
    @property
    def Occurrence(self): # -> InferenceOption
        """
        Get: Occurrence(self: XmlSchemaInference) -> InferenceOption
        Set: Occurrence(self: XmlSchemaInference) = value
        """
        ...

    @property
    def TypeInference(self): # -> InferenceOption
        """
        Get: TypeInference(self: XmlSchemaInference) -> InferenceOption
        Set: TypeInference(self: XmlSchemaInference) = value
        """
        ...


    def InferenceOption(self, *args): #cannot find CLR method
        """ enum InferenceOption, values: Relaxed (1), Restricted (0) """
        ...

    def InferSchema(self, instanceDocument, schemas = ...): # -> XmlSchemaSet # Not found arg types: {'instanceDocument': 'XmlReader', 'schemas': 'XmlSchemaSet'}
        """
        InferSchema(self: XmlSchemaInference, instanceDocument: XmlReader) -> XmlSchemaSet
        InferSchema(self: XmlSchemaInference, instanceDocument: XmlReader, schemas: XmlSchemaSet) -> XmlSchemaSet
        """
        ...



class XmlSchemaInferenceException(XmlSchemaException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XmlSchemaInferenceException()
    XmlSchemaInferenceException(message: str)
    XmlSchemaInferenceException(message: str, innerException: Exception)
    XmlSchemaInferenceException(message: str, innerException: Exception, lineNumber: int, linePosition: int)
    """
    SerializeObjectState = ...


class XmlSchemaInfo(IXmlSchemaInfo): # skipped bases: <type 'object'>
    """ XmlSchemaInfo() """
    @property
    def ContentType(self) -> XmlSchemaContentType:
        """
        Get: ContentType(self: XmlSchemaInfo) -> XmlSchemaContentType
        Set: ContentType(self: XmlSchemaInfo) = value
        """
        ...



class XmlSchemaKey(XmlSchemaIdentityConstraint): # skipped bases: <type 'object'>
    """ XmlSchemaKey() """
    pass

class XmlSchemaKeyref(XmlSchemaIdentityConstraint): # skipped bases: <type 'object'>
    """ XmlSchemaKeyref() """
    @property
    def Refer(self): # -> XmlQualifiedName
        """
        Get: Refer(self: XmlSchemaKeyref) -> XmlQualifiedName
        Set: Refer(self: XmlSchemaKeyref) = value
        """
        ...



class XmlSchemaLengthFacet(XmlSchemaNumericFacet): # skipped bases: <type 'object'>
    """ XmlSchemaLengthFacet() """
    pass

class XmlSchemaMaxExclusiveFacet(XmlSchemaFacet): # skipped bases: <type 'object'>
    """ XmlSchemaMaxExclusiveFacet() """
    pass

class XmlSchemaMaxInclusiveFacet(XmlSchemaFacet): # skipped bases: <type 'object'>
    """ XmlSchemaMaxInclusiveFacet() """
    pass

class XmlSchemaMaxLengthFacet(XmlSchemaNumericFacet): # skipped bases: <type 'object'>
    """ XmlSchemaMaxLengthFacet() """
    pass

class XmlSchemaMinExclusiveFacet(XmlSchemaFacet): # skipped bases: <type 'object'>
    """ XmlSchemaMinExclusiveFacet() """
    pass

class XmlSchemaMinInclusiveFacet(XmlSchemaFacet): # skipped bases: <type 'object'>
    """ XmlSchemaMinInclusiveFacet() """
    pass

class XmlSchemaMinLengthFacet(XmlSchemaNumericFacet): # skipped bases: <type 'object'>
    """ XmlSchemaMinLengthFacet() """
    pass

class XmlSchemaNotation(XmlSchemaAnnotated): # skipped bases: <type 'object'>
    """ XmlSchemaNotation() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: XmlSchemaNotation) -> str
        Set: Name(self: XmlSchemaNotation) = value
        """
        ...

    @property
    def Public(self) -> str:
        """
        Get: Public(self: XmlSchemaNotation) -> str
        Set: Public(self: XmlSchemaNotation) = value
        """
        ...

    @property
    def System(self) -> str:
        """
        Get: System(self: XmlSchemaNotation) -> str
        Set: System(self: XmlSchemaNotation) = value
        """
        ...



class XmlSchemaObjectCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    XmlSchemaObjectCollection()
    XmlSchemaObjectCollection(parent: XmlSchemaObject)
    """
    def Add(self, item:XmlSchemaObject) -> int:
        """ Add(self: XmlSchemaObjectCollection, item: XmlSchemaObject) -> int """
        ...

    def Contains(self, item:XmlSchemaObject) -> bool:
        """ Contains(self: XmlSchemaObjectCollection, item: XmlSchemaObject) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: XmlSchemaObjectCollection, array: Array[XmlSchemaObject], index: int) """
        ...

    def IndexOf(self, item:XmlSchemaObject) -> int:
        """ IndexOf(self: XmlSchemaObjectCollection, item: XmlSchemaObject) -> int """
        ...

    def Insert(self, index:int, item:XmlSchemaObject): # -> 
        """ Insert(self: XmlSchemaObjectCollection, index: int, item: XmlSchemaObject) """
        ...

    def Remove(self, item:XmlSchemaObject): # -> 
        """ Remove(self: XmlSchemaObjectCollection, item: XmlSchemaObject) """
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


class XmlSchemaObjectEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class XmlSchemaObjectTable: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: XmlSchemaObjectTable) -> int """
        ...

    @property
    def Names(self) -> ICollection:
        """ Get: Names(self: XmlSchemaObjectTable) -> ICollection """
        ...

    @property
    def Values(self) -> ICollection:
        """ Get: Values(self: XmlSchemaObjectTable) -> ICollection """
        ...


    def Contains(self, name) -> bool: # Not found arg types: {'name': 'XmlQualifiedName'}
        """ Contains(self: XmlSchemaObjectTable, name: XmlQualifiedName) -> bool """
        ...

    def GetEnumerator(self) -> IDictionaryEnumerator:
        """ GetEnumerator(self: XmlSchemaObjectTable) -> IDictionaryEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class XmlSchemaPatternFacet(XmlSchemaFacet): # skipped bases: <type 'object'>
    """ XmlSchemaPatternFacet() """
    pass

class XmlSchemaRedefine(XmlSchemaExternal): # skipped bases: <type 'object'>
    """ XmlSchemaRedefine() """
    @property
    def AttributeGroups(self) -> XmlSchemaObjectTable:
        """ Get: AttributeGroups(self: XmlSchemaRedefine) -> XmlSchemaObjectTable """
        ...

    @property
    def Groups(self) -> XmlSchemaObjectTable:
        """ Get: Groups(self: XmlSchemaRedefine) -> XmlSchemaObjectTable """
        ...

    @property
    def Items(self) -> XmlSchemaObjectCollection:
        """ Get: Items(self: XmlSchemaRedefine) -> XmlSchemaObjectCollection """
        ...

    @property
    def SchemaTypes(self) -> XmlSchemaObjectTable:
        """ Get: SchemaTypes(self: XmlSchemaRedefine) -> XmlSchemaObjectTable """
        ...



class XmlSchemaSequence(XmlSchemaGroupBase): # skipped bases: <type 'object'>
    """ XmlSchemaSequence() """
    pass

class XmlSchemaSet: # skipped bases: <type 'object'>, <type 'object'>
    """
    XmlSchemaSet()
    XmlSchemaSet(nameTable: XmlNameTable)
    """
    @property
    def CompilationSettings(self) -> XmlSchemaCompilationSettings:
        """
        Get: CompilationSettings(self: XmlSchemaSet) -> XmlSchemaCompilationSettings
        Set: CompilationSettings(self: XmlSchemaSet) = value
        """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: XmlSchemaSet) -> int """
        ...

    @property
    def GlobalAttributes(self) -> XmlSchemaObjectTable:
        """ Get: GlobalAttributes(self: XmlSchemaSet) -> XmlSchemaObjectTable """
        ...

    @property
    def GlobalElements(self) -> XmlSchemaObjectTable:
        """ Get: GlobalElements(self: XmlSchemaSet) -> XmlSchemaObjectTable """
        ...

    @property
    def GlobalTypes(self) -> XmlSchemaObjectTable:
        """ Get: GlobalTypes(self: XmlSchemaSet) -> XmlSchemaObjectTable """
        ...

    @property
    def IsCompiled(self) -> bool:
        """ Get: IsCompiled(self: XmlSchemaSet) -> bool """
        ...

    @property
    def NameTable(self): # -> XmlNameTable
        """ Get: NameTable(self: XmlSchemaSet) -> XmlNameTable """
        ...

    @property
    def XmlResolver(self): # -> 
        """ Set: XmlResolver(self: XmlSchemaSet) = value """
        ...


    def Add(self, *__args:XmlSchemaSet): # -> 
        """
        Add(self: XmlSchemaSet, targetNamespace: str, schemaUri: str) -> XmlSchema
        Add(self: XmlSchemaSet, targetNamespace: str, schemaDocument: XmlReader) -> XmlSchema
        Add(self: XmlSchemaSet, schemas: XmlSchemaSet)Add(self: XmlSchemaSet, schema: XmlSchema) -> XmlSchema
        """
        ...

    def Compile(self): # -> 
        """ Compile(self: XmlSchemaSet) """
        ...

    def Contains(self, *__args:str) -> bool:
        """
        Contains(self: XmlSchemaSet, targetNamespace: str) -> bool
        Contains(self: XmlSchemaSet, schema: XmlSchema) -> bool
        """
        ...

    def CopyTo(self, schemas:Array, index:int): # -> 
        """ CopyTo(self: XmlSchemaSet, schemas: Array[XmlSchema], index: int) """
        ...

    def Remove(self, schema:XmlSchema) -> XmlSchema:
        """ Remove(self: XmlSchemaSet, schema: XmlSchema) -> XmlSchema """
        ...

    def RemoveRecursive(self, schemaToRemove:XmlSchema) -> bool:
        """ RemoveRecursive(self: XmlSchemaSet, schemaToRemove: XmlSchema) -> bool """
        ...

    def Reprocess(self, schema:XmlSchema) -> XmlSchema:
        """ Reprocess(self: XmlSchemaSet, schema: XmlSchema) -> XmlSchema """
        ...

    def Schemas(self, targetNamespace:str = ...) -> ICollection:
        """
        Schemas(self: XmlSchemaSet) -> ICollection
        Schemas(self: XmlSchemaSet, targetNamespace: str) -> ICollection
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    ValidationEventHandler = ...


class XmlSchemaSimpleContent(XmlSchemaContentModel): # skipped bases: <type 'object'>
    """ XmlSchemaSimpleContent() """
    pass

class XmlSchemaSimpleContentExtension(XmlSchemaContent): # skipped bases: <type 'object'>
    """ XmlSchemaSimpleContentExtension() """
    @property
    def AnyAttribute(self) -> XmlSchemaAnyAttribute:
        """
        Get: AnyAttribute(self: XmlSchemaSimpleContentExtension) -> XmlSchemaAnyAttribute
        Set: AnyAttribute(self: XmlSchemaSimpleContentExtension) = value
        """
        ...

    @property
    def Attributes(self) -> XmlSchemaObjectCollection:
        """ Get: Attributes(self: XmlSchemaSimpleContentExtension) -> XmlSchemaObjectCollection """
        ...

    @property
    def BaseTypeName(self): # -> XmlQualifiedName
        """
        Get: BaseTypeName(self: XmlSchemaSimpleContentExtension) -> XmlQualifiedName
        Set: BaseTypeName(self: XmlSchemaSimpleContentExtension) = value
        """
        ...



class XmlSchemaSimpleContentRestriction(XmlSchemaContent): # skipped bases: <type 'object'>
    """ XmlSchemaSimpleContentRestriction() """
    @property
    def AnyAttribute(self) -> XmlSchemaAnyAttribute:
        """
        Get: AnyAttribute(self: XmlSchemaSimpleContentRestriction) -> XmlSchemaAnyAttribute
        Set: AnyAttribute(self: XmlSchemaSimpleContentRestriction) = value
        """
        ...

    @property
    def Attributes(self) -> XmlSchemaObjectCollection:
        """ Get: Attributes(self: XmlSchemaSimpleContentRestriction) -> XmlSchemaObjectCollection """
        ...

    @property
    def BaseType(self): # -> XmlSchemaSimpleType
        """
        Get: BaseType(self: XmlSchemaSimpleContentRestriction) -> XmlSchemaSimpleType
        Set: BaseType(self: XmlSchemaSimpleContentRestriction) = value
        """
        ...

    @property
    def BaseTypeName(self): # -> XmlQualifiedName
        """
        Get: BaseTypeName(self: XmlSchemaSimpleContentRestriction) -> XmlQualifiedName
        Set: BaseTypeName(self: XmlSchemaSimpleContentRestriction) = value
        """
        ...

    @property
    def Facets(self) -> XmlSchemaObjectCollection:
        """ Get: Facets(self: XmlSchemaSimpleContentRestriction) -> XmlSchemaObjectCollection """
        ...



class XmlSchemaSimpleType(XmlSchemaType): # skipped bases: <type 'object'>
    """ XmlSchemaSimpleType() """
    @property
    def Content(self): # -> XmlSchemaSimpleTypeContent
        """
        Get: Content(self: XmlSchemaSimpleType) -> XmlSchemaSimpleTypeContent
        Set: Content(self: XmlSchemaSimpleType) = value
        """
        ...



class XmlSchemaSimpleTypeContent(XmlSchemaAnnotated): # skipped bases: <type 'object'>
    """ no doc """
    pass

class XmlSchemaSimpleTypeList(XmlSchemaSimpleTypeContent): # skipped bases: <type 'object'>
    """ XmlSchemaSimpleTypeList() """
    @property
    def BaseItemType(self) -> XmlSchemaSimpleType:
        """
        Get: BaseItemType(self: XmlSchemaSimpleTypeList) -> XmlSchemaSimpleType
        Set: BaseItemType(self: XmlSchemaSimpleTypeList) = value
        """
        ...

    @property
    def ItemType(self) -> XmlSchemaSimpleType:
        """
        Get: ItemType(self: XmlSchemaSimpleTypeList) -> XmlSchemaSimpleType
        Set: ItemType(self: XmlSchemaSimpleTypeList) = value
        """
        ...

    @property
    def ItemTypeName(self): # -> XmlQualifiedName
        """
        Get: ItemTypeName(self: XmlSchemaSimpleTypeList) -> XmlQualifiedName
        Set: ItemTypeName(self: XmlSchemaSimpleTypeList) = value
        """
        ...



class XmlSchemaSimpleTypeRestriction(XmlSchemaSimpleTypeContent): # skipped bases: <type 'object'>
    """ XmlSchemaSimpleTypeRestriction() """
    @property
    def BaseType(self) -> XmlSchemaSimpleType:
        """
        Get: BaseType(self: XmlSchemaSimpleTypeRestriction) -> XmlSchemaSimpleType
        Set: BaseType(self: XmlSchemaSimpleTypeRestriction) = value
        """
        ...

    @property
    def BaseTypeName(self): # -> XmlQualifiedName
        """
        Get: BaseTypeName(self: XmlSchemaSimpleTypeRestriction) -> XmlQualifiedName
        Set: BaseTypeName(self: XmlSchemaSimpleTypeRestriction) = value
        """
        ...

    @property
    def Facets(self) -> XmlSchemaObjectCollection:
        """ Get: Facets(self: XmlSchemaSimpleTypeRestriction) -> XmlSchemaObjectCollection """
        ...



class XmlSchemaSimpleTypeUnion(XmlSchemaSimpleTypeContent): # skipped bases: <type 'object'>
    """ XmlSchemaSimpleTypeUnion() """
    @property
    def BaseMemberTypes(self) -> Array:
        """ Get: BaseMemberTypes(self: XmlSchemaSimpleTypeUnion) -> Array[XmlSchemaSimpleType] """
        ...

    @property
    def BaseTypes(self) -> XmlSchemaObjectCollection:
        """ Get: BaseTypes(self: XmlSchemaSimpleTypeUnion) -> XmlSchemaObjectCollection """
        ...

    @property
    def MemberTypes(self) -> Array:
        """
        Get: MemberTypes(self: XmlSchemaSimpleTypeUnion) -> Array[XmlQualifiedName]
        Set: MemberTypes(self: XmlSchemaSimpleTypeUnion) = value
        """
        ...



class XmlSchemaTotalDigitsFacet(XmlSchemaNumericFacet): # skipped bases: <type 'object'>
    """ XmlSchemaTotalDigitsFacet() """
    pass

class XmlSchemaUnique(XmlSchemaIdentityConstraint): # skipped bases: <type 'object'>
    """ XmlSchemaUnique() """
    pass

class XmlSchemaUse(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlSchemaUse, values: None (0), Optional (1), Prohibited (2), Required (3) """
    Optional: XmlSchemaUse = ...
    Prohibited: XmlSchemaUse = ...
    Required: XmlSchemaUse = ...
    value__ = ...


class XmlSchemaValidationException(XmlSchemaException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XmlSchemaValidationException()
    XmlSchemaValidationException(message: str)
    XmlSchemaValidationException(message: str, innerException: Exception)
    XmlSchemaValidationException(message: str, innerException: Exception, lineNumber: int, linePosition: int)
    """
    @property
    def SourceObject(self) -> object:
        """ Get: SourceObject(self: XmlSchemaValidationException) -> object """
        ...


    def SetSourceObject(self, *args): #cannot find CLR method
        """ SetSourceObject(self: XmlSchemaValidationException, sourceObject: object) """
        ...

    SerializeObjectState = ...


class XmlSchemaValidationFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) XmlSchemaValidationFlags, values: AllowXmlAttributes (16), None (0), ProcessIdentityConstraints (8), ProcessInlineSchema (1), ProcessSchemaLocation (2), ReportValidationWarnings (4) """
    AllowXmlAttributes: XmlSchemaValidationFlags = ...
    ProcessIdentityConstraints: XmlSchemaValidationFlags = ...
    ProcessInlineSchema: XmlSchemaValidationFlags = ...
    ProcessSchemaLocation: XmlSchemaValidationFlags = ...
    ReportValidationWarnings: XmlSchemaValidationFlags = ...
    value__ = ...


class XmlSchemaValidator: # skipped bases: <type 'object'>, <type 'object'>
    """ XmlSchemaValidator(nameTable: XmlNameTable, schemas: XmlSchemaSet, namespaceResolver: IXmlNamespaceResolver, validationFlags: XmlSchemaValidationFlags) """
    @property
    def LineInfoProvider(self): # -> IXmlLineInfo
        """
        Get: LineInfoProvider(self: XmlSchemaValidator) -> IXmlLineInfo
        Set: LineInfoProvider(self: XmlSchemaValidator) = value
        """
        ...

    @property
    def SourceUri(self) -> Uri:
        """
        Get: SourceUri(self: XmlSchemaValidator) -> Uri
        Set: SourceUri(self: XmlSchemaValidator) = value
        """
        ...

    @property
    def ValidationEventSender(self) -> object:
        """
        Get: ValidationEventSender(self: XmlSchemaValidator) -> object
        Set: ValidationEventSender(self: XmlSchemaValidator) = value
        """
        ...

    @property
    def XmlResolver(self): # -> 
        """ Set: XmlResolver(self: XmlSchemaValidator) = value """
        ...


    def AddSchema(self, schema:XmlSchema): # -> 
        """ AddSchema(self: XmlSchemaValidator, schema: XmlSchema) """
        ...

    def EndValidation(self): # -> 
        """ EndValidation(self: XmlSchemaValidator) """
        ...

    def GetExpectedAttributes(self) -> Array:
        """ GetExpectedAttributes(self: XmlSchemaValidator) -> Array[XmlSchemaAttribute] """
        ...

    def GetExpectedParticles(self) -> Array:
        """ GetExpectedParticles(self: XmlSchemaValidator) -> Array[XmlSchemaParticle] """
        ...

    def GetUnspecifiedDefaultAttributes(self, defaultAttributes:ArrayList): # -> 
        """ GetUnspecifiedDefaultAttributes(self: XmlSchemaValidator, defaultAttributes: ArrayList) """
        ...

    def Initialize(self, partialValidationType:XmlSchemaObject = ...): # -> 
        """ Initialize(self: XmlSchemaValidator)Initialize(self: XmlSchemaValidator, partialValidationType: XmlSchemaObject) """
        ...

    def SkipToEndElement(self, schemaInfo:XmlSchemaInfo): # -> 
        """ SkipToEndElement(self: XmlSchemaValidator, schemaInfo: XmlSchemaInfo) """
        ...

    def ValidateAttribute(self, localName:str, namespaceUri:str, attributeValue:str, schemaInfo:XmlSchemaInfo) -> object:
        """
        ValidateAttribute(self: XmlSchemaValidator, localName: str, namespaceUri: str, attributeValue: str, schemaInfo: XmlSchemaInfo) -> object
        ValidateAttribute(self: XmlSchemaValidator, localName: str, namespaceUri: str, attributeValue: XmlValueGetter, schemaInfo: XmlSchemaInfo) -> object
        """
        ...

    def ValidateElement(self, localName:str, namespaceUri:str, schemaInfo:XmlSchemaInfo, xsiType:str = ..., xsiNil:str = ..., xsiSchemaLocation:str = ..., xsiNoNamespaceSchemaLocation:str = ...): # -> 
        """ ValidateElement(self: XmlSchemaValidator, localName: str, namespaceUri: str, schemaInfo: XmlSchemaInfo)ValidateElement(self: XmlSchemaValidator, localName: str, namespaceUri: str, schemaInfo: XmlSchemaInfo, xsiType: str, xsiNil: str, xsiSchemaLocation: str, xsiNoNamespaceSchemaLocation: str) """
        ...

    def ValidateEndElement(self, schemaInfo:XmlSchemaInfo, typedValue:object = ...) -> object:
        """
        ValidateEndElement(self: XmlSchemaValidator, schemaInfo: XmlSchemaInfo) -> object
        ValidateEndElement(self: XmlSchemaValidator, schemaInfo: XmlSchemaInfo, typedValue: object) -> object
        """
        ...

    def ValidateEndOfAttributes(self, schemaInfo:XmlSchemaInfo): # -> 
        """ ValidateEndOfAttributes(self: XmlSchemaValidator, schemaInfo: XmlSchemaInfo) """
        ...

    def ValidateText(self, elementValue:str): # -> 
        """ ValidateText(self: XmlSchemaValidator, elementValue: str)ValidateText(self: XmlSchemaValidator, elementValue: XmlValueGetter) """
        ...

    def ValidateWhitespace(self, elementValue:str): # -> 
        """ ValidateWhitespace(self: XmlSchemaValidator, elementValue: str)ValidateWhitespace(self: XmlSchemaValidator, elementValue: XmlValueGetter) """
        ...

    ValidationEventHandler = ...


class XmlSchemaValidity(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlSchemaValidity, values: Invalid (2), NotKnown (0), Valid (1) """
    Invalid: XmlSchemaValidity = ...
    NotKnown: XmlSchemaValidity = ...
    Valid: XmlSchemaValidity = ...
    value__ = ...


class XmlSchemaWhiteSpaceFacet(XmlSchemaFacet): # skipped bases: <type 'object'>
    """ XmlSchemaWhiteSpaceFacet() """
    pass

class XmlSchemaXPath(XmlSchemaAnnotated): # skipped bases: <type 'object'>
    """ XmlSchemaXPath() """
    @property
    def XPath(self) -> str:
        """
        Get: XPath(self: XmlSchemaXPath) -> str
        Set: XPath(self: XmlSchemaXPath) = value
        """
        ...



class XmlSeverityType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlSeverityType, values: Error (0), Warning (1) """
    Error: XmlSeverityType = ...
    value__ = ...
    Warning: XmlSeverityType = ...


class XmlTypeCode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlTypeCode, values: AnyAtomicType (10), AnyUri (28), Attribute (5), Base64Binary (27), Boolean (13), Byte (46), Comment (8), Date (20), DateTime (18), DayTimeDuration (54), Decimal (14), Document (3), Double (16), Duration (17), Element (4), Entity (39), Float (15), GDay (24), GMonth (25), GMonthDay (23), GYear (22), GYearMonth (21), HexBinary (26), Id (37), Idref (38), Int (44), Integer (40), Item (1), Language (33), Long (43), Name (35), Namespace (6), NCName (36), NegativeInteger (42), NmToken (34), Node (2), None (0), NonNegativeInteger (47), NonPositiveInteger (41), NormalizedString (31), Notation (30), PositiveInteger (52), ProcessingInstruction (7), QName (29), Short (45), String (12), Text (9), Time (19), Token (32), UnsignedByte (51), UnsignedInt (49), UnsignedLong (48), UnsignedShort (50), UntypedAtomic (11), YearMonthDuration (53) """
    AnyAtomicType: XmlTypeCode = ...
    AnyUri: XmlTypeCode = ...
    Attribute: XmlTypeCode = ...
    Base64Binary: XmlTypeCode = ...
    Boolean: XmlTypeCode = ...
    Byte: XmlTypeCode = ...
    Comment: XmlTypeCode = ...
    Date: XmlTypeCode = ...
    DateTime: XmlTypeCode = ...
    DayTimeDuration: XmlTypeCode = ...
    Decimal: XmlTypeCode = ...
    Document: XmlTypeCode = ...
    Double: XmlTypeCode = ...
    Duration: XmlTypeCode = ...
    Element: XmlTypeCode = ...
    Entity: XmlTypeCode = ...
    Float: XmlTypeCode = ...
    GDay: XmlTypeCode = ...
    GMonth: XmlTypeCode = ...
    GMonthDay: XmlTypeCode = ...
    GYear: XmlTypeCode = ...
    GYearMonth: XmlTypeCode = ...
    HexBinary: XmlTypeCode = ...
    Id: XmlTypeCode = ...
    Idref: XmlTypeCode = ...
    Int: XmlTypeCode = ...
    Integer: XmlTypeCode = ...
    Item: XmlTypeCode = ...
    Language: XmlTypeCode = ...
    Long: XmlTypeCode = ...
    Name: XmlTypeCode = ...
    Namespace: XmlTypeCode = ...
    NCName: XmlTypeCode = ...
    NegativeInteger: XmlTypeCode = ...
    NmToken: XmlTypeCode = ...
    Node: XmlTypeCode = ...
    NonNegativeInteger: XmlTypeCode = ...
    NonPositiveInteger: XmlTypeCode = ...
    NormalizedString: XmlTypeCode = ...
    Notation: XmlTypeCode = ...
    PositiveInteger: XmlTypeCode = ...
    ProcessingInstruction: XmlTypeCode = ...
    QName: XmlTypeCode = ...
    Short: XmlTypeCode = ...
    String: XmlTypeCode = ...
    Text: XmlTypeCode = ...
    Time: XmlTypeCode = ...
    Token: XmlTypeCode = ...
    UnsignedByte: XmlTypeCode = ...
    UnsignedInt: XmlTypeCode = ...
    UnsignedLong: XmlTypeCode = ...
    UnsignedShort: XmlTypeCode = ...
    UntypedAtomic: XmlTypeCode = ...
    value__ = ...
    YearMonthDuration: XmlTypeCode = ...


class XmlValueGetter(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ XmlValueGetter(object: object, method: IntPtr) """
    def BeginInvoke(self, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: XmlValueGetter, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> object:
        """ EndInvoke(self: XmlValueGetter, result: IAsyncResult) -> object """
        ...

    def Invoke(self) -> object:
        """ Invoke(self: XmlValueGetter) -> object """
        ...


