# encoding: utf-8
# module System.Xml.Serialization calls itself Serialization
# from System.Xml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Attribute, Enum, EventArgs, 
    IAsyncResult, MulticastDelegate, Type)

from System.CodeDom import (CodeAttributeDeclarationCollection, 
    CodeCompileUnit, CodeNamespace)

from System.CodeDom.Compiler import CodeDomProvider, CompilerParameters

from System.Collections import (CollectionBase, Hashtable, IEnumerable, 
    IEnumerator, IList)

from System.Collections.Specialized import StringCollection

from System.IO import Stream, TextWriter

from System.Reflection import Assembly, ICustomAttributeProvider

from System.Xml import (WhitespaceHandling, XmlAttribute, XmlElement, 
    XmlNodeType, XmlQualifiedName, XmlReader, XmlWriter)

from System.Xml.Schema import (ValidationEventHandler, XmlSchema, 
    XmlSchemaForm)

from System.Xml.Serialization.Advanced import (
    SchemaImporterExtensionCollection)

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class CodeExporter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IncludeMetadata(self) -> CodeAttributeDeclarationCollection:
        """ Get: IncludeMetadata(self: CodeExporter) -> CodeAttributeDeclarationCollection """
        ...



class CodeGenerationOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CodeGenerationOptions, values: EnableDataBinding (16), GenerateNewAsync (2), GenerateOldAsync (4), GenerateOrder (8), GenerateProperties (1), None (0) """
    EnableDataBinding: CodeGenerationOptions = ...
    GenerateNewAsync: CodeGenerationOptions = ...
    GenerateOldAsync: CodeGenerationOptions = ...
    GenerateOrder: CodeGenerationOptions = ...
    GenerateProperties: CodeGenerationOptions = ...
    value__ = ...


class CodeIdentifier: # skipped bases: <type 'object'>, <type 'object'>
    """ CodeIdentifier() """
    @staticmethod
    def MakeCamel(identifier:str) -> str:
        """ MakeCamel(identifier: str) -> str """
        ...

    @staticmethod
    def MakePascal(identifier:str) -> str:
        """ MakePascal(identifier: str) -> str """
        ...

    @staticmethod
    def MakeValid(identifier:str) -> str:
        """ MakeValid(identifier: str) -> str """
        ...


class CodeIdentifiers: # skipped bases: <type 'object'>, <type 'object'>
    """
    CodeIdentifiers()
    CodeIdentifiers(caseSensitive: bool)
    """
    @property
    def UseCamelCasing(self) -> bool:
        """
        Get: UseCamelCasing(self: CodeIdentifiers) -> bool
        Set: UseCamelCasing(self: CodeIdentifiers) = value
        """
        ...


    def Add(self, identifier:str, value:object): # -> 
        """ Add(self: CodeIdentifiers, identifier: str, value: object) """
        ...

    def AddReserved(self, identifier:str): # -> 
        """ AddReserved(self: CodeIdentifiers, identifier: str) """
        ...

    def AddUnique(self, identifier:str, value:object) -> str:
        """ AddUnique(self: CodeIdentifiers, identifier: str, value: object) -> str """
        ...

    def Clear(self): # -> 
        """ Clear(self: CodeIdentifiers) """
        ...

    def IsInUse(self, identifier:str) -> bool:
        """ IsInUse(self: CodeIdentifiers, identifier: str) -> bool """
        ...

    def MakeRightCase(self, identifier:str) -> str:
        """ MakeRightCase(self: CodeIdentifiers, identifier: str) -> str """
        ...

    def MakeUnique(self, identifier:str) -> str:
        """ MakeUnique(self: CodeIdentifiers, identifier: str) -> str """
        ...

    def Remove(self, identifier:str): # -> 
        """ Remove(self: CodeIdentifiers, identifier: str) """
        ...

    def RemoveReserved(self, identifier:str): # -> 
        """ RemoveReserved(self: CodeIdentifiers, identifier: str) """
        ...

    def ToArray(self, type:Type) -> object:
        """ ToArray(self: CodeIdentifiers, type: Type) -> object """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class ImportContext: # skipped bases: <type 'object'>, <type 'object'>
    """ ImportContext(identifiers: CodeIdentifiers, shareTypes: bool) """
    @property
    def ShareTypes(self) -> bool:
        """ Get: ShareTypes(self: ImportContext) -> bool """
        ...

    @property
    def TypeIdentifiers(self) -> CodeIdentifiers:
        """ Get: TypeIdentifiers(self: ImportContext) -> CodeIdentifiers """
        ...

    @property
    def Warnings(self) -> StringCollection:
        """ Get: Warnings(self: ImportContext) -> StringCollection """
        ...



class IXmlSerializable: # skipped bases: <type 'object'>
    """ no doc """
    def GetSchema(self) -> XmlSchema:
        """ GetSchema(self: IXmlSerializable) -> XmlSchema """
        ...

    def ReadXml(self, reader:XmlReader): # -> 
        """ ReadXml(self: IXmlSerializable, reader: XmlReader) """
        ...

    def WriteXml(self, writer:XmlWriter): # -> 
        """ WriteXml(self: IXmlSerializable, writer: XmlWriter) """
        ...


class IXmlTextParser: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Normalized(self) -> bool:
        """
        Get: Normalized(self: IXmlTextParser) -> bool
        Set: Normalized(self: IXmlTextParser) = value
        """
        ...

    @property
    def WhitespaceHandling(self) -> WhitespaceHandling:
        """
        Get: WhitespaceHandling(self: IXmlTextParser) -> WhitespaceHandling
        Set: WhitespaceHandling(self: IXmlTextParser) = value
        """
        ...



class SchemaImporter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Extensions(self) -> SchemaImporterExtensionCollection:
        """ Get: Extensions(self: SchemaImporter) -> SchemaImporterExtensionCollection """
        ...



class SoapAttributeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SoapAttributeAttribute()
    SoapAttributeAttribute(attributeName: str)
    """
    @property
    def AttributeName(self) -> str:
        """
        Get: AttributeName(self: SoapAttributeAttribute) -> str
        Set: AttributeName(self: SoapAttributeAttribute) = value
        """
        ...

    @property
    def DataType(self) -> str:
        """
        Get: DataType(self: SoapAttributeAttribute) -> str
        Set: DataType(self: SoapAttributeAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: SoapAttributeAttribute) -> str
        Set: Namespace(self: SoapAttributeAttribute) = value
        """
        ...


    def __new__(cls, attributeName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, attributeName: str)
        """
        ...


class SoapAttributeOverrides: # skipped bases: <type 'object'>, <type 'object'>
    """ SoapAttributeOverrides() """
    def Add(self, type:Type, *__args:SoapAttributes): # -> 
        """ Add(self: SoapAttributeOverrides, type: Type, attributes: SoapAttributes)Add(self: SoapAttributeOverrides, type: Type, member: str, attributes: SoapAttributes) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class SoapAttributes: # skipped bases: <type 'object'>, <type 'object'>
    """
    SoapAttributes()
    SoapAttributes(provider: ICustomAttributeProvider)
    """
    @property
    def SoapAttribute(self) -> SoapAttributeAttribute:
        """
        Get: SoapAttribute(self: SoapAttributes) -> SoapAttributeAttribute
        Set: SoapAttribute(self: SoapAttributes) = value
        """
        ...

    @property
    def SoapDefaultValue(self) -> object:
        """
        Get: SoapDefaultValue(self: SoapAttributes) -> object
        Set: SoapDefaultValue(self: SoapAttributes) = value
        """
        ...

    @property
    def SoapElement(self) -> SoapElementAttribute:
        """
        Get: SoapElement(self: SoapAttributes) -> SoapElementAttribute
        Set: SoapElement(self: SoapAttributes) = value
        """
        ...

    @property
    def SoapEnum(self) -> SoapEnumAttribute:
        """
        Get: SoapEnum(self: SoapAttributes) -> SoapEnumAttribute
        Set: SoapEnum(self: SoapAttributes) = value
        """
        ...

    @property
    def SoapIgnore(self) -> bool:
        """
        Get: SoapIgnore(self: SoapAttributes) -> bool
        Set: SoapIgnore(self: SoapAttributes) = value
        """
        ...

    @property
    def SoapType(self) -> SoapTypeAttribute:
        """
        Get: SoapType(self: SoapAttributes) -> SoapTypeAttribute
        Set: SoapType(self: SoapAttributes) = value
        """
        ...



class SoapCodeExporter(CodeExporter): # skipped bases: <type 'object'>
    """
    SoapCodeExporter(codeNamespace: CodeNamespace)
    SoapCodeExporter(codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit)
    SoapCodeExporter(codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, options: CodeGenerationOptions)
    SoapCodeExporter(codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, options: CodeGenerationOptions, mappings: Hashtable)
    SoapCodeExporter(codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, codeProvider: CodeDomProvider, options: CodeGenerationOptions, mappings: Hashtable)
    """
    def AddMappingMetadata(self, metadata:CodeAttributeDeclarationCollection, member:XmlMemberMapping, forceUseMemberName:bool = ...): # -> 
        """ AddMappingMetadata(self: SoapCodeExporter, metadata: CodeAttributeDeclarationCollection, member: XmlMemberMapping, forceUseMemberName: bool)AddMappingMetadata(self: SoapCodeExporter, metadata: CodeAttributeDeclarationCollection, member: XmlMemberMapping) """
        ...

    def ExportMembersMapping(self, xmlMembersMapping:XmlMembersMapping): # -> 
        """ ExportMembersMapping(self: SoapCodeExporter, xmlMembersMapping: XmlMembersMapping) """
        ...

    def ExportTypeMapping(self, xmlTypeMapping:XmlTypeMapping): # -> 
        """ ExportTypeMapping(self: SoapCodeExporter, xmlTypeMapping: XmlTypeMapping) """
        ...

    def __new__(cls, codeNamespace:CodeNamespace, codeCompileUnit:CodeCompileUnit = ..., *__args:CodeGenerationOptions) -> Self:
        """
        __new__(cls: type, codeNamespace: CodeNamespace)
        __new__(cls: type, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit)
        __new__(cls: type, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, options: CodeGenerationOptions)
        __new__(cls: type, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, options: CodeGenerationOptions, mappings: Hashtable)
        __new__(cls: type, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, codeProvider: CodeDomProvider, options: CodeGenerationOptions, mappings: Hashtable)
        """
        ...


class SoapElementAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SoapElementAttribute()
    SoapElementAttribute(elementName: str)
    """
    @property
    def DataType(self) -> str:
        """
        Get: DataType(self: SoapElementAttribute) -> str
        Set: DataType(self: SoapElementAttribute) = value
        """
        ...

    @property
    def ElementName(self) -> str:
        """
        Get: ElementName(self: SoapElementAttribute) -> str
        Set: ElementName(self: SoapElementAttribute) = value
        """
        ...

    @property
    def IsNullable(self) -> bool:
        """
        Get: IsNullable(self: SoapElementAttribute) -> bool
        Set: IsNullable(self: SoapElementAttribute) = value
        """
        ...


    def __new__(cls, elementName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, elementName: str)
        """
        ...


class SoapEnumAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SoapEnumAttribute()
    SoapEnumAttribute(name: str)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: SoapEnumAttribute) -> str
        Set: Name(self: SoapEnumAttribute) = value
        """
        ...


    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...


class SoapIgnoreAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SoapIgnoreAttribute() """
    pass

class SoapIncludeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SoapIncludeAttribute(type: Type) """
    @property
    def Type(self) -> Type:
        """
        Get: Type(self: SoapIncludeAttribute) -> Type
        Set: Type(self: SoapIncludeAttribute) = value
        """
        ...


    def __new__(cls, type:Type) -> Self:
        """ __new__(cls: type, type: Type) """
        ...


class SoapReflectionImporter: # skipped bases: <type 'object'>, <type 'object'>
    """
    SoapReflectionImporter()
    SoapReflectionImporter(defaultNamespace: str)
    SoapReflectionImporter(attributeOverrides: SoapAttributeOverrides)
    SoapReflectionImporter(attributeOverrides: SoapAttributeOverrides, defaultNamespace: str)
    """
    def ImportMembersMapping(self, elementName:str, ns:str, members:Array, hasWrapperElement:bool = ..., writeAccessors:bool = ..., validate:bool = ..., access:XmlMappingAccess = ...) -> XmlMembersMapping:
        """
        ImportMembersMapping(self: SoapReflectionImporter, elementName: str, ns: str, members: Array[XmlReflectionMember]) -> XmlMembersMapping
        ImportMembersMapping(self: SoapReflectionImporter, elementName: str, ns: str, members: Array[XmlReflectionMember], hasWrapperElement: bool, writeAccessors: bool) -> XmlMembersMapping
        ImportMembersMapping(self: SoapReflectionImporter, elementName: str, ns: str, members: Array[XmlReflectionMember], hasWrapperElement: bool, writeAccessors: bool, validate: bool) -> XmlMembersMapping
        ImportMembersMapping(self: SoapReflectionImporter, elementName: str, ns: str, members: Array[XmlReflectionMember], hasWrapperElement: bool, writeAccessors: bool, validate: bool, access: XmlMappingAccess) -> XmlMembersMapping
        """
        ...

    def ImportTypeMapping(self, type:Type, defaultNamespace:str = ...) -> XmlTypeMapping:
        """
        ImportTypeMapping(self: SoapReflectionImporter, type: Type) -> XmlTypeMapping
        ImportTypeMapping(self: SoapReflectionImporter, type: Type, defaultNamespace: str) -> XmlTypeMapping
        """
        ...

    def IncludeType(self, type:Type): # -> 
        """ IncludeType(self: SoapReflectionImporter, type: Type) """
        ...

    def IncludeTypes(self, provider:ICustomAttributeProvider): # -> 
        """ IncludeTypes(self: SoapReflectionImporter, provider: ICustomAttributeProvider) """
        ...


class SoapSchemaExporter: # skipped bases: <type 'object'>, <type 'object'>
    """ SoapSchemaExporter(schemas: XmlSchemas) """
    def ExportMembersMapping(self, xmlMembersMapping:XmlMembersMapping, exportEnclosingType:bool = ...): # -> 
        """ ExportMembersMapping(self: SoapSchemaExporter, xmlMembersMapping: XmlMembersMapping)ExportMembersMapping(self: SoapSchemaExporter, xmlMembersMapping: XmlMembersMapping, exportEnclosingType: bool) """
        ...

    def ExportTypeMapping(self, xmlTypeMapping:XmlTypeMapping): # -> 
        """ ExportTypeMapping(self: SoapSchemaExporter, xmlTypeMapping: XmlTypeMapping) """
        ...


class SoapSchemaImporter(SchemaImporter): # skipped bases: <type 'object'>
    """
    SoapSchemaImporter(schemas: XmlSchemas)
    SoapSchemaImporter(schemas: XmlSchemas, typeIdentifiers: CodeIdentifiers)
    SoapSchemaImporter(schemas: XmlSchemas, typeIdentifiers: CodeIdentifiers, options: CodeGenerationOptions)
    SoapSchemaImporter(schemas: XmlSchemas, options: CodeGenerationOptions, context: ImportContext)
    SoapSchemaImporter(schemas: XmlSchemas, options: CodeGenerationOptions, codeProvider: CodeDomProvider, context: ImportContext)
    """
    def ImportDerivedTypeMapping(self, name:XmlQualifiedName, baseType:Type, baseTypeCanBeIndirect:bool) -> XmlTypeMapping:
        """ ImportDerivedTypeMapping(self: SoapSchemaImporter, name: XmlQualifiedName, baseType: Type, baseTypeCanBeIndirect: bool) -> XmlTypeMapping """
        ...

    def ImportMembersMapping(self, name:str, ns:str, *__args:Array) -> XmlMembersMapping:
        """
        ImportMembersMapping(self: SoapSchemaImporter, name: str, ns: str, members: Array[SoapSchemaMember]) -> XmlMembersMapping
        ImportMembersMapping(self: SoapSchemaImporter, name: str, ns: str, members: Array[SoapSchemaMember], hasWrapperElement: bool) -> XmlMembersMapping
        ImportMembersMapping(self: SoapSchemaImporter, name: str, ns: str, member: SoapSchemaMember) -> XmlMembersMapping
        ImportMembersMapping(self: SoapSchemaImporter, name: str, ns: str, members: Array[SoapSchemaMember], hasWrapperElement: bool, baseType: Type, baseTypeCanBeIndirect: bool) -> XmlMembersMapping
        """
        ...

    def __new__(cls, schemas:XmlSchemas, *__args:CodeIdentifiers) -> Self:
        """
        __new__(cls: type, schemas: XmlSchemas)
        __new__(cls: type, schemas: XmlSchemas, typeIdentifiers: CodeIdentifiers)
        __new__(cls: type, schemas: XmlSchemas, typeIdentifiers: CodeIdentifiers, options: CodeGenerationOptions)
        __new__(cls: type, schemas: XmlSchemas, options: CodeGenerationOptions, context: ImportContext)
        __new__(cls: type, schemas: XmlSchemas, options: CodeGenerationOptions, codeProvider: CodeDomProvider, context: ImportContext)
        """
        ...


class SoapSchemaMember: # skipped bases: <type 'object'>, <type 'object'>
    """ SoapSchemaMember() """
    @property
    def MemberName(self) -> str:
        """
        Get: MemberName(self: SoapSchemaMember) -> str
        Set: MemberName(self: SoapSchemaMember) = value
        """
        ...

    @property
    def MemberType(self) -> XmlQualifiedName:
        """
        Get: MemberType(self: SoapSchemaMember) -> XmlQualifiedName
        Set: MemberType(self: SoapSchemaMember) = value
        """
        ...



class SoapTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SoapTypeAttribute()
    SoapTypeAttribute(typeName: str)
    SoapTypeAttribute(typeName: str, ns: str)
    """
    @property
    def IncludeInSchema(self) -> bool:
        """
        Get: IncludeInSchema(self: SoapTypeAttribute) -> bool
        Set: IncludeInSchema(self: SoapTypeAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: SoapTypeAttribute) -> str
        Set: Namespace(self: SoapTypeAttribute) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: SoapTypeAttribute) -> str
        Set: TypeName(self: SoapTypeAttribute) = value
        """
        ...


    def __new__(cls, typeName:str = ..., ns:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, typeName: str)
        __new__(cls: type, typeName: str, ns: str)
        """
        ...


class UnreferencedObjectEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ UnreferencedObjectEventArgs(o: object, id: str) """
    @property
    def UnreferencedId(self) -> str:
        """ Get: UnreferencedId(self: UnreferencedObjectEventArgs) -> str """
        ...

    @property
    def UnreferencedObject(self) -> object:
        """ Get: UnreferencedObject(self: UnreferencedObjectEventArgs) -> object """
        ...


    def __new__(cls, o:object, id:str) -> Self:
        """ __new__(cls: type, o: object, id: str) """
        ...


class UnreferencedObjectEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ UnreferencedObjectEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:UnreferencedObjectEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: UnreferencedObjectEventHandler, sender: object, e: UnreferencedObjectEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: UnreferencedObjectEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:UnreferencedObjectEventArgs): # -> 
        """ Invoke(self: UnreferencedObjectEventHandler, sender: object, e: UnreferencedObjectEventArgs) """
        ...


class XmlAnyAttributeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ XmlAnyAttributeAttribute() """
    pass

class XmlAnyElementAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    XmlAnyElementAttribute()
    XmlAnyElementAttribute(name: str)
    XmlAnyElementAttribute(name: str, ns: str)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: XmlAnyElementAttribute) -> str
        Set: Name(self: XmlAnyElementAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: XmlAnyElementAttribute) -> str
        Set: Namespace(self: XmlAnyElementAttribute) = value
        """
        ...

    @property
    def Order(self) -> int:
        """
        Get: Order(self: XmlAnyElementAttribute) -> int
        Set: Order(self: XmlAnyElementAttribute) = value
        """
        ...


    def __new__(cls, name:str = ..., ns:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, ns: str)
        """
        ...


class XmlAnyElementAttributes(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ XmlAnyElementAttributes() """
    def Add(self, attribute:XmlAnyElementAttribute) -> int:
        """ Add(self: XmlAnyElementAttributes, attribute: XmlAnyElementAttribute) -> int """
        ...

    def Contains(self, attribute:XmlAnyElementAttribute) -> bool:
        """ Contains(self: XmlAnyElementAttributes, attribute: XmlAnyElementAttribute) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: XmlAnyElementAttributes, array: Array[XmlAnyElementAttribute], index: int) """
        ...

    def IndexOf(self, attribute:XmlAnyElementAttribute) -> int:
        """ IndexOf(self: XmlAnyElementAttributes, attribute: XmlAnyElementAttribute) -> int """
        ...

    def Insert(self, index:int, attribute:XmlAnyElementAttribute): # -> 
        """ Insert(self: XmlAnyElementAttributes, index: int, attribute: XmlAnyElementAttribute) """
        ...

    def Remove(self, attribute:XmlAnyElementAttribute): # -> 
        """ Remove(self: XmlAnyElementAttributes, attribute: XmlAnyElementAttribute) """
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


class XmlArrayAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    XmlArrayAttribute()
    XmlArrayAttribute(elementName: str)
    """
    @property
    def ElementName(self) -> str:
        """
        Get: ElementName(self: XmlArrayAttribute) -> str
        Set: ElementName(self: XmlArrayAttribute) = value
        """
        ...

    @property
    def Form(self) -> XmlSchemaForm:
        """
        Get: Form(self: XmlArrayAttribute) -> XmlSchemaForm
        Set: Form(self: XmlArrayAttribute) = value
        """
        ...

    @property
    def IsNullable(self) -> bool:
        """
        Get: IsNullable(self: XmlArrayAttribute) -> bool
        Set: IsNullable(self: XmlArrayAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: XmlArrayAttribute) -> str
        Set: Namespace(self: XmlArrayAttribute) = value
        """
        ...

    @property
    def Order(self) -> int:
        """
        Get: Order(self: XmlArrayAttribute) -> int
        Set: Order(self: XmlArrayAttribute) = value
        """
        ...


    def __new__(cls, elementName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, elementName: str)
        """
        ...


class XmlArrayItemAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    XmlArrayItemAttribute()
    XmlArrayItemAttribute(elementName: str)
    XmlArrayItemAttribute(type: Type)
    XmlArrayItemAttribute(elementName: str, type: Type)
    """
    @property
    def DataType(self) -> str:
        """
        Get: DataType(self: XmlArrayItemAttribute) -> str
        Set: DataType(self: XmlArrayItemAttribute) = value
        """
        ...

    @property
    def ElementName(self) -> str:
        """
        Get: ElementName(self: XmlArrayItemAttribute) -> str
        Set: ElementName(self: XmlArrayItemAttribute) = value
        """
        ...

    @property
    def Form(self) -> XmlSchemaForm:
        """
        Get: Form(self: XmlArrayItemAttribute) -> XmlSchemaForm
        Set: Form(self: XmlArrayItemAttribute) = value
        """
        ...

    @property
    def IsNullable(self) -> bool:
        """
        Get: IsNullable(self: XmlArrayItemAttribute) -> bool
        Set: IsNullable(self: XmlArrayItemAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: XmlArrayItemAttribute) -> str
        Set: Namespace(self: XmlArrayItemAttribute) = value
        """
        ...

    @property
    def NestingLevel(self) -> int:
        """
        Get: NestingLevel(self: XmlArrayItemAttribute) -> int
        Set: NestingLevel(self: XmlArrayItemAttribute) = value
        """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: XmlArrayItemAttribute) -> Type
        Set: Type(self: XmlArrayItemAttribute) = value
        """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, elementName: str)
        __new__(cls: type, type: Type)
        __new__(cls: type, elementName: str, type: Type)
        """
        ...


class XmlArrayItemAttributes(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ XmlArrayItemAttributes() """
    def Add(self, attribute:XmlArrayItemAttribute) -> int:
        """ Add(self: XmlArrayItemAttributes, attribute: XmlArrayItemAttribute) -> int """
        ...

    def Contains(self, attribute:XmlArrayItemAttribute) -> bool:
        """ Contains(self: XmlArrayItemAttributes, attribute: XmlArrayItemAttribute) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: XmlArrayItemAttributes, array: Array[XmlArrayItemAttribute], index: int) """
        ...

    def IndexOf(self, attribute:XmlArrayItemAttribute) -> int:
        """ IndexOf(self: XmlArrayItemAttributes, attribute: XmlArrayItemAttribute) -> int """
        ...

    def Insert(self, index:int, attribute:XmlArrayItemAttribute): # -> 
        """ Insert(self: XmlArrayItemAttributes, index: int, attribute: XmlArrayItemAttribute) """
        ...

    def Remove(self, attribute:XmlArrayItemAttribute): # -> 
        """ Remove(self: XmlArrayItemAttributes, attribute: XmlArrayItemAttribute) """
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


class XmlAttributeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    XmlAttributeAttribute()
    XmlAttributeAttribute(attributeName: str)
    XmlAttributeAttribute(type: Type)
    XmlAttributeAttribute(attributeName: str, type: Type)
    """
    @property
    def AttributeName(self) -> str:
        """
        Get: AttributeName(self: XmlAttributeAttribute) -> str
        Set: AttributeName(self: XmlAttributeAttribute) = value
        """
        ...

    @property
    def DataType(self) -> str:
        """
        Get: DataType(self: XmlAttributeAttribute) -> str
        Set: DataType(self: XmlAttributeAttribute) = value
        """
        ...

    @property
    def Form(self) -> XmlSchemaForm:
        """
        Get: Form(self: XmlAttributeAttribute) -> XmlSchemaForm
        Set: Form(self: XmlAttributeAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: XmlAttributeAttribute) -> str
        Set: Namespace(self: XmlAttributeAttribute) = value
        """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: XmlAttributeAttribute) -> Type
        Set: Type(self: XmlAttributeAttribute) = value
        """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, attributeName: str)
        __new__(cls: type, type: Type)
        __new__(cls: type, attributeName: str, type: Type)
        """
        ...


class XmlAttributeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attr(self) -> XmlAttribute:
        """ Get: Attr(self: XmlAttributeEventArgs) -> XmlAttribute """
        ...

    @property
    def ExpectedAttributes(self) -> str:
        """ Get: ExpectedAttributes(self: XmlAttributeEventArgs) -> str """
        ...

    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: XmlAttributeEventArgs) -> int """
        ...

    @property
    def LinePosition(self) -> int:
        """ Get: LinePosition(self: XmlAttributeEventArgs) -> int """
        ...

    @property
    def ObjectBeingDeserialized(self) -> object:
        """ Get: ObjectBeingDeserialized(self: XmlAttributeEventArgs) -> object """
        ...



class XmlAttributeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ XmlAttributeEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:XmlAttributeEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: XmlAttributeEventHandler, sender: object, e: XmlAttributeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: XmlAttributeEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:XmlAttributeEventArgs): # -> 
        """ Invoke(self: XmlAttributeEventHandler, sender: object, e: XmlAttributeEventArgs) """
        ...


class XmlAttributeOverrides: # skipped bases: <type 'object'>, <type 'object'>
    """ XmlAttributeOverrides() """
    def Add(self, type:Type, *__args:XmlAttributes): # -> 
        """ Add(self: XmlAttributeOverrides, type: Type, attributes: XmlAttributes)Add(self: XmlAttributeOverrides, type: Type, member: str, attributes: XmlAttributes) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class XmlAttributes: # skipped bases: <type 'object'>, <type 'object'>
    """
    XmlAttributes()
    XmlAttributes(provider: ICustomAttributeProvider)
    """
    @property
    def XmlAnyAttribute(self) -> XmlAnyAttributeAttribute:
        """
        Get: XmlAnyAttribute(self: XmlAttributes) -> XmlAnyAttributeAttribute
        Set: XmlAnyAttribute(self: XmlAttributes) = value
        """
        ...

    @property
    def XmlAnyElements(self) -> XmlAnyElementAttributes:
        """ Get: XmlAnyElements(self: XmlAttributes) -> XmlAnyElementAttributes """
        ...

    @property
    def XmlArray(self) -> XmlArrayAttribute:
        """
        Get: XmlArray(self: XmlAttributes) -> XmlArrayAttribute
        Set: XmlArray(self: XmlAttributes) = value
        """
        ...

    @property
    def XmlArrayItems(self) -> XmlArrayItemAttributes:
        """ Get: XmlArrayItems(self: XmlAttributes) -> XmlArrayItemAttributes """
        ...

    @property
    def XmlAttribute(self) -> XmlAttributeAttribute:
        """
        Get: XmlAttribute(self: XmlAttributes) -> XmlAttributeAttribute
        Set: XmlAttribute(self: XmlAttributes) = value
        """
        ...

    @property
    def XmlChoiceIdentifier(self) -> XmlChoiceIdentifierAttribute:
        """ Get: XmlChoiceIdentifier(self: XmlAttributes) -> XmlChoiceIdentifierAttribute """
        ...

    @property
    def XmlDefaultValue(self) -> object:
        """
        Get: XmlDefaultValue(self: XmlAttributes) -> object
        Set: XmlDefaultValue(self: XmlAttributes) = value
        """
        ...

    @property
    def XmlElements(self) -> XmlElementAttributes:
        """ Get: XmlElements(self: XmlAttributes) -> XmlElementAttributes """
        ...

    @property
    def XmlEnum(self) -> XmlEnumAttribute:
        """
        Get: XmlEnum(self: XmlAttributes) -> XmlEnumAttribute
        Set: XmlEnum(self: XmlAttributes) = value
        """
        ...

    @property
    def XmlIgnore(self) -> bool:
        """
        Get: XmlIgnore(self: XmlAttributes) -> bool
        Set: XmlIgnore(self: XmlAttributes) = value
        """
        ...

    @property
    def Xmlns(self) -> bool:
        """
        Get: Xmlns(self: XmlAttributes) -> bool
        Set: Xmlns(self: XmlAttributes) = value
        """
        ...

    @property
    def XmlRoot(self) -> XmlRootAttribute:
        """
        Get: XmlRoot(self: XmlAttributes) -> XmlRootAttribute
        Set: XmlRoot(self: XmlAttributes) = value
        """
        ...

    @property
    def XmlText(self) -> XmlTextAttribute:
        """
        Get: XmlText(self: XmlAttributes) -> XmlTextAttribute
        Set: XmlText(self: XmlAttributes) = value
        """
        ...

    @property
    def XmlType(self) -> XmlTypeAttribute:
        """
        Get: XmlType(self: XmlAttributes) -> XmlTypeAttribute
        Set: XmlType(self: XmlAttributes) = value
        """
        ...



class XmlChoiceIdentifierAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    XmlChoiceIdentifierAttribute()
    XmlChoiceIdentifierAttribute(name: str)
    """
    @property
    def MemberName(self) -> str:
        """
        Get: MemberName(self: XmlChoiceIdentifierAttribute) -> str
        Set: MemberName(self: XmlChoiceIdentifierAttribute) = value
        """
        ...


    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...


class XmlCodeExporter(CodeExporter): # skipped bases: <type 'object'>
    """
    XmlCodeExporter(codeNamespace: CodeNamespace)
    XmlCodeExporter(codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit)
    XmlCodeExporter(codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, options: CodeGenerationOptions)
    XmlCodeExporter(codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, options: CodeGenerationOptions, mappings: Hashtable)
    XmlCodeExporter(codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, codeProvider: CodeDomProvider, options: CodeGenerationOptions, mappings: Hashtable)
    """
    def AddMappingMetadata(self, metadata, *__args): # -> 
        """ AddMappingMetadata(self: XmlCodeExporter, metadata: CodeAttributeDeclarationCollection, mapping: XmlTypeMapping, ns: str)AddMappingMetadata(self: XmlCodeExporter, metadata: CodeAttributeDeclarationCollection, member: XmlMemberMapping, ns: str, forceUseMemberName: bool)AddMappingMetadata(self: XmlCodeExporter, metadata: CodeAttributeDeclarationCollection, member: XmlMemberMapping, ns: str) """
        ...

    def ExportMembersMapping(self, xmlMembersMapping:XmlMembersMapping): # -> 
        """ ExportMembersMapping(self: XmlCodeExporter, xmlMembersMapping: XmlMembersMapping) """
        ...

    def ExportTypeMapping(self, xmlTypeMapping:XmlTypeMapping): # -> 
        """ ExportTypeMapping(self: XmlCodeExporter, xmlTypeMapping: XmlTypeMapping) """
        ...

    def __new__(cls, codeNamespace:CodeNamespace, codeCompileUnit:CodeCompileUnit = ..., *__args:CodeGenerationOptions) -> Self:
        """
        __new__(cls: type, codeNamespace: CodeNamespace)
        __new__(cls: type, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit)
        __new__(cls: type, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, options: CodeGenerationOptions)
        __new__(cls: type, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, options: CodeGenerationOptions, mappings: Hashtable)
        __new__(cls: type, codeNamespace: CodeNamespace, codeCompileUnit: CodeCompileUnit, codeProvider: CodeDomProvider, options: CodeGenerationOptions, mappings: Hashtable)
        """
        ...


class XmlDeserializationEvents: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def OnUnknownAttribute(self) -> XmlAttributeEventHandler:
        """
        Get: OnUnknownAttribute(self: XmlDeserializationEvents) -> XmlAttributeEventHandler
        Set: OnUnknownAttribute(self: XmlDeserializationEvents) = value
        """
        ...

    @property
    def OnUnknownElement(self) -> XmlElementEventHandler:
        """
        Get: OnUnknownElement(self: XmlDeserializationEvents) -> XmlElementEventHandler
        Set: OnUnknownElement(self: XmlDeserializationEvents) = value
        """
        ...

    @property
    def OnUnknownNode(self) -> XmlNodeEventHandler:
        """
        Get: OnUnknownNode(self: XmlDeserializationEvents) -> XmlNodeEventHandler
        Set: OnUnknownNode(self: XmlDeserializationEvents) = value
        """
        ...

    @property
    def OnUnreferencedObject(self) -> UnreferencedObjectEventHandler:
        """
        Get: OnUnreferencedObject(self: XmlDeserializationEvents) -> UnreferencedObjectEventHandler
        Set: OnUnreferencedObject(self: XmlDeserializationEvents) = value
        """
        ...



class XmlElementAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    XmlElementAttribute()
    XmlElementAttribute(elementName: str)
    XmlElementAttribute(type: Type)
    XmlElementAttribute(elementName: str, type: Type)
    """
    @property
    def DataType(self) -> str:
        """
        Get: DataType(self: XmlElementAttribute) -> str
        Set: DataType(self: XmlElementAttribute) = value
        """
        ...

    @property
    def ElementName(self) -> str:
        """
        Get: ElementName(self: XmlElementAttribute) -> str
        Set: ElementName(self: XmlElementAttribute) = value
        """
        ...

    @property
    def Form(self) -> XmlSchemaForm:
        """
        Get: Form(self: XmlElementAttribute) -> XmlSchemaForm
        Set: Form(self: XmlElementAttribute) = value
        """
        ...

    @property
    def IsNullable(self) -> bool:
        """
        Get: IsNullable(self: XmlElementAttribute) -> bool
        Set: IsNullable(self: XmlElementAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: XmlElementAttribute) -> str
        Set: Namespace(self: XmlElementAttribute) = value
        """
        ...

    @property
    def Order(self) -> int:
        """
        Get: Order(self: XmlElementAttribute) -> int
        Set: Order(self: XmlElementAttribute) = value
        """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: XmlElementAttribute) -> Type
        Set: Type(self: XmlElementAttribute) = value
        """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, elementName: str)
        __new__(cls: type, type: Type)
        __new__(cls: type, elementName: str, type: Type)
        """
        ...


class XmlElementAttributes(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ XmlElementAttributes() """
    def Add(self, attribute:XmlElementAttribute) -> int:
        """ Add(self: XmlElementAttributes, attribute: XmlElementAttribute) -> int """
        ...

    def Contains(self, attribute:XmlElementAttribute) -> bool:
        """ Contains(self: XmlElementAttributes, attribute: XmlElementAttribute) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: XmlElementAttributes, array: Array[XmlElementAttribute], index: int) """
        ...

    def IndexOf(self, attribute:XmlElementAttribute) -> int:
        """ IndexOf(self: XmlElementAttributes, attribute: XmlElementAttribute) -> int """
        ...

    def Insert(self, index:int, attribute:XmlElementAttribute): # -> 
        """ Insert(self: XmlElementAttributes, index: int, attribute: XmlElementAttribute) """
        ...

    def Remove(self, attribute:XmlElementAttribute): # -> 
        """ Remove(self: XmlElementAttributes, attribute: XmlElementAttribute) """
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


class XmlElementEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Element(self) -> XmlElement:
        """ Get: Element(self: XmlElementEventArgs) -> XmlElement """
        ...

    @property
    def ExpectedElements(self) -> str:
        """ Get: ExpectedElements(self: XmlElementEventArgs) -> str """
        ...

    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: XmlElementEventArgs) -> int """
        ...

    @property
    def LinePosition(self) -> int:
        """ Get: LinePosition(self: XmlElementEventArgs) -> int """
        ...

    @property
    def ObjectBeingDeserialized(self) -> object:
        """ Get: ObjectBeingDeserialized(self: XmlElementEventArgs) -> object """
        ...



class XmlElementEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ XmlElementEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:XmlElementEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: XmlElementEventHandler, sender: object, e: XmlElementEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: XmlElementEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:XmlElementEventArgs): # -> 
        """ Invoke(self: XmlElementEventHandler, sender: object, e: XmlElementEventArgs) """
        ...


class XmlEnumAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    XmlEnumAttribute()
    XmlEnumAttribute(name: str)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: XmlEnumAttribute) -> str
        Set: Name(self: XmlEnumAttribute) = value
        """
        ...


    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...


class XmlIgnoreAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ XmlIgnoreAttribute() """
    pass

class XmlIncludeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ XmlIncludeAttribute(type: Type) """
    @property
    def Type(self) -> Type:
        """
        Get: Type(self: XmlIncludeAttribute) -> Type
        Set: Type(self: XmlIncludeAttribute) = value
        """
        ...


    def __new__(cls, type:Type) -> Self:
        """ __new__(cls: type, type: Type) """
        ...


class XmlMapping: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ElementName(self) -> str:
        """ Get: ElementName(self: XmlMapping) -> str """
        ...

    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: XmlMapping) -> str """
        ...

    @property
    def XsdElementName(self) -> str:
        """ Get: XsdElementName(self: XmlMapping) -> str """
        ...


    def SetKey(self, key:str): # -> 
        """ SetKey(self: XmlMapping, key: str) """
        ...


class XmlMappingAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) XmlMappingAccess, values: None (0), Read (1), Write (2) """
    Read: XmlMappingAccess = ...
    value__ = ...
    Write: XmlMappingAccess = ...


class XmlMemberMapping: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Any(self) -> bool:
        """ Get: Any(self: XmlMemberMapping) -> bool """
        ...

    @property
    def CheckSpecified(self) -> bool:
        """ Get: CheckSpecified(self: XmlMemberMapping) -> bool """
        ...

    @property
    def ElementName(self) -> str:
        """ Get: ElementName(self: XmlMemberMapping) -> str """
        ...

    @property
    def MemberName(self) -> str:
        """ Get: MemberName(self: XmlMemberMapping) -> str """
        ...

    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: XmlMemberMapping) -> str """
        ...

    @property
    def TypeFullName(self) -> str:
        """ Get: TypeFullName(self: XmlMemberMapping) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: XmlMemberMapping) -> str """
        ...

    @property
    def TypeNamespace(self) -> str:
        """ Get: TypeNamespace(self: XmlMemberMapping) -> str """
        ...

    @property
    def XsdElementName(self) -> str:
        """ Get: XsdElementName(self: XmlMemberMapping) -> str """
        ...


    def GenerateTypeName(self, codeProvider:CodeDomProvider) -> str:
        """ GenerateTypeName(self: XmlMemberMapping, codeProvider: CodeDomProvider) -> str """
        ...


class XmlMembersMapping(XmlMapping): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: XmlMembersMapping) -> int """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: XmlMembersMapping) -> str """
        ...

    @property
    def TypeNamespace(self) -> str:
        """ Get: TypeNamespace(self: XmlMembersMapping) -> str """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class XmlNamespaceDeclarationsAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ XmlNamespaceDeclarationsAttribute() """
    pass

class XmlNodeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: XmlNodeEventArgs) -> int """
        ...

    @property
    def LinePosition(self) -> int:
        """ Get: LinePosition(self: XmlNodeEventArgs) -> int """
        ...

    @property
    def LocalName(self) -> str:
        """ Get: LocalName(self: XmlNodeEventArgs) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlNodeEventArgs) -> str """
        ...

    @property
    def NamespaceURI(self) -> str:
        """ Get: NamespaceURI(self: XmlNodeEventArgs) -> str """
        ...

    @property
    def NodeType(self) -> XmlNodeType:
        """ Get: NodeType(self: XmlNodeEventArgs) -> XmlNodeType """
        ...

    @property
    def ObjectBeingDeserialized(self) -> object:
        """ Get: ObjectBeingDeserialized(self: XmlNodeEventArgs) -> object """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: XmlNodeEventArgs) -> str """
        ...



class XmlNodeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ XmlNodeEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:XmlNodeEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: XmlNodeEventHandler, sender: object, e: XmlNodeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: XmlNodeEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:XmlNodeEventArgs): # -> 
        """ Invoke(self: XmlNodeEventHandler, sender: object, e: XmlNodeEventArgs) """
        ...


class XmlReflectionImporter: # skipped bases: <type 'object'>, <type 'object'>
    """
    XmlReflectionImporter()
    XmlReflectionImporter(defaultNamespace: str)
    XmlReflectionImporter(attributeOverrides: XmlAttributeOverrides)
    XmlReflectionImporter(attributeOverrides: XmlAttributeOverrides, defaultNamespace: str)
    """
    def ImportMembersMapping(self, elementName:str, ns:str, members:Array, hasWrapperElement:bool, rpc:bool = ..., openModel:bool = ..., access:XmlMappingAccess = ...) -> XmlMembersMapping:
        """
        ImportMembersMapping(self: XmlReflectionImporter, elementName: str, ns: str, members: Array[XmlReflectionMember], hasWrapperElement: bool) -> XmlMembersMapping
        ImportMembersMapping(self: XmlReflectionImporter, elementName: str, ns: str, members: Array[XmlReflectionMember], hasWrapperElement: bool, rpc: bool) -> XmlMembersMapping
        ImportMembersMapping(self: XmlReflectionImporter, elementName: str, ns: str, members: Array[XmlReflectionMember], hasWrapperElement: bool, rpc: bool, openModel: bool) -> XmlMembersMapping
        ImportMembersMapping(self: XmlReflectionImporter, elementName: str, ns: str, members: Array[XmlReflectionMember], hasWrapperElement: bool, rpc: bool, openModel: bool, access: XmlMappingAccess) -> XmlMembersMapping
        """
        ...

    def ImportTypeMapping(self, type:Type, *__args:str) -> XmlTypeMapping:
        """
        ImportTypeMapping(self: XmlReflectionImporter, type: Type) -> XmlTypeMapping
        ImportTypeMapping(self: XmlReflectionImporter, type: Type, defaultNamespace: str) -> XmlTypeMapping
        ImportTypeMapping(self: XmlReflectionImporter, type: Type, root: XmlRootAttribute) -> XmlTypeMapping
        ImportTypeMapping(self: XmlReflectionImporter, type: Type, root: XmlRootAttribute, defaultNamespace: str) -> XmlTypeMapping
        """
        ...

    def IncludeType(self, type:Type): # -> 
        """ IncludeType(self: XmlReflectionImporter, type: Type) """
        ...

    def IncludeTypes(self, provider:ICustomAttributeProvider): # -> 
        """ IncludeTypes(self: XmlReflectionImporter, provider: ICustomAttributeProvider) """
        ...


class XmlReflectionMember: # skipped bases: <type 'object'>, <type 'object'>
    """ XmlReflectionMember() """
    @property
    def IsReturnValue(self) -> bool:
        """
        Get: IsReturnValue(self: XmlReflectionMember) -> bool
        Set: IsReturnValue(self: XmlReflectionMember) = value
        """
        ...

    @property
    def MemberName(self) -> str:
        """
        Get: MemberName(self: XmlReflectionMember) -> str
        Set: MemberName(self: XmlReflectionMember) = value
        """
        ...

    @property
    def MemberType(self) -> Type:
        """
        Get: MemberType(self: XmlReflectionMember) -> Type
        Set: MemberType(self: XmlReflectionMember) = value
        """
        ...

    @property
    def OverrideIsNullable(self) -> bool:
        """
        Get: OverrideIsNullable(self: XmlReflectionMember) -> bool
        Set: OverrideIsNullable(self: XmlReflectionMember) = value
        """
        ...

    @property
    def SoapAttributes(self) -> SoapAttributes:
        """
        Get: SoapAttributes(self: XmlReflectionMember) -> SoapAttributes
        Set: SoapAttributes(self: XmlReflectionMember) = value
        """
        ...

    @property
    def XmlAttributes(self) -> XmlAttributes:
        """
        Get: XmlAttributes(self: XmlReflectionMember) -> XmlAttributes
        Set: XmlAttributes(self: XmlReflectionMember) = value
        """
        ...



class XmlRootAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    XmlRootAttribute()
    XmlRootAttribute(elementName: str)
    """
    @property
    def DataType(self) -> str:
        """
        Get: DataType(self: XmlRootAttribute) -> str
        Set: DataType(self: XmlRootAttribute) = value
        """
        ...

    @property
    def ElementName(self) -> str:
        """
        Get: ElementName(self: XmlRootAttribute) -> str
        Set: ElementName(self: XmlRootAttribute) = value
        """
        ...

    @property
    def IsNullable(self) -> bool:
        """
        Get: IsNullable(self: XmlRootAttribute) -> bool
        Set: IsNullable(self: XmlRootAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: XmlRootAttribute) -> str
        Set: Namespace(self: XmlRootAttribute) = value
        """
        ...


    def __new__(cls, elementName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, elementName: str)
        """
        ...


class XmlSchemaEnumerator(IEnumerator): # skipped bases: <type 'IDisposable'>, <type 'IEnumerator'>, <type 'object'>
    """ XmlSchemaEnumerator(list: XmlSchemas) """
    def Dispose(self): # -> 
        """ Dispose(self: XmlSchemaEnumerator) """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: XmlSchemaEnumerator) -> bool """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[XmlSchema](enumerator: IEnumerator[XmlSchema], value: XmlSchema) -> bool """
        ...


class XmlSchemaExporter: # skipped bases: <type 'object'>, <type 'object'>
    """ XmlSchemaExporter(schemas: XmlSchemas) """
    def ExportAnyType(self, *__args:str) -> str:
        """
        ExportAnyType(self: XmlSchemaExporter, ns: str) -> str
        ExportAnyType(self: XmlSchemaExporter, members: XmlMembersMapping) -> str
        """
        ...

    def ExportMembersMapping(self, xmlMembersMapping:XmlMembersMapping, exportEnclosingType:bool = ...): # -> 
        """ ExportMembersMapping(self: XmlSchemaExporter, xmlMembersMapping: XmlMembersMapping)ExportMembersMapping(self: XmlSchemaExporter, xmlMembersMapping: XmlMembersMapping, exportEnclosingType: bool) """
        ...

    def ExportTypeMapping(self, *__args:XmlTypeMapping): # -> 
        """ ExportTypeMapping(self: XmlSchemaExporter, xmlTypeMapping: XmlTypeMapping)ExportTypeMapping(self: XmlSchemaExporter, xmlMembersMapping: XmlMembersMapping) -> XmlQualifiedName """
        ...


class XmlSchemaImporter(SchemaImporter): # skipped bases: <type 'object'>
    """
    XmlSchemaImporter(schemas: XmlSchemas)
    XmlSchemaImporter(schemas: XmlSchemas, typeIdentifiers: CodeIdentifiers)
    XmlSchemaImporter(schemas: XmlSchemas, typeIdentifiers: CodeIdentifiers, options: CodeGenerationOptions)
    XmlSchemaImporter(schemas: XmlSchemas, options: CodeGenerationOptions, context: ImportContext)
    XmlSchemaImporter(schemas: XmlSchemas, options: CodeGenerationOptions, codeProvider: CodeDomProvider, context: ImportContext)
    """
    def ImportAnyType(self, typeName:XmlQualifiedName, elementName:str) -> XmlMembersMapping:
        """ ImportAnyType(self: XmlSchemaImporter, typeName: XmlQualifiedName, elementName: str) -> XmlMembersMapping """
        ...

    def ImportDerivedTypeMapping(self, name:XmlQualifiedName, baseType:Type, baseTypeCanBeIndirect:bool = ...) -> XmlTypeMapping:
        """
        ImportDerivedTypeMapping(self: XmlSchemaImporter, name: XmlQualifiedName, baseType: Type) -> XmlTypeMapping
        ImportDerivedTypeMapping(self: XmlSchemaImporter, name: XmlQualifiedName, baseType: Type, baseTypeCanBeIndirect: bool) -> XmlTypeMapping
        """
        ...

    def ImportMembersMapping(self, *__args:XmlQualifiedName) -> XmlMembersMapping:
        """
        ImportMembersMapping(self: XmlSchemaImporter, name: XmlQualifiedName) -> XmlMembersMapping
        ImportMembersMapping(self: XmlSchemaImporter, names: Array[XmlQualifiedName]) -> XmlMembersMapping
        ImportMembersMapping(self: XmlSchemaImporter, name: str, ns: str, members: Array[SoapSchemaMember]) -> XmlMembersMapping
        ImportMembersMapping(self: XmlSchemaImporter, names: Array[XmlQualifiedName], baseType: Type, baseTypeCanBeIndirect: bool) -> XmlMembersMapping
        """
        ...

    def ImportSchemaType(self, typeName:XmlQualifiedName, baseType:Type = ..., baseTypeCanBeIndirect:bool = ...) -> XmlTypeMapping:
        """
        ImportSchemaType(self: XmlSchemaImporter, typeName: XmlQualifiedName) -> XmlTypeMapping
        ImportSchemaType(self: XmlSchemaImporter, typeName: XmlQualifiedName, baseType: Type) -> XmlTypeMapping
        ImportSchemaType(self: XmlSchemaImporter, typeName: XmlQualifiedName, baseType: Type, baseTypeCanBeIndirect: bool) -> XmlTypeMapping
        """
        ...

    def ImportTypeMapping(self, name:XmlQualifiedName) -> XmlTypeMapping:
        """ ImportTypeMapping(self: XmlSchemaImporter, name: XmlQualifiedName) -> XmlTypeMapping """
        ...

    def __new__(cls, schemas:XmlSchemas, *__args:CodeIdentifiers) -> Self:
        """
        __new__(cls: type, schemas: XmlSchemas)
        __new__(cls: type, schemas: XmlSchemas, typeIdentifiers: CodeIdentifiers)
        __new__(cls: type, schemas: XmlSchemas, typeIdentifiers: CodeIdentifiers, options: CodeGenerationOptions)
        __new__(cls: type, schemas: XmlSchemas, options: CodeGenerationOptions, context: ImportContext)
        __new__(cls: type, schemas: XmlSchemas, options: CodeGenerationOptions, codeProvider: CodeDomProvider, context: ImportContext)
        """
        ...


class XmlSchemaProviderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ XmlSchemaProviderAttribute(methodName: str) """
    @property
    def IsAny(self) -> bool:
        """
        Get: IsAny(self: XmlSchemaProviderAttribute) -> bool
        Set: IsAny(self: XmlSchemaProviderAttribute) = value
        """
        ...

    @property
    def MethodName(self) -> str:
        """ Get: MethodName(self: XmlSchemaProviderAttribute) -> str """
        ...


    def __new__(cls, methodName:str) -> Self:
        """ __new__(cls: type, methodName: str) """
        ...


class XmlSchemas(CollectionBase, IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ XmlSchemas() """
    @property
    def IsCompiled(self) -> bool:
        """ Get: IsCompiled(self: XmlSchemas) -> bool """
        ...


    def Add(self, *__args:XmlSchema) -> int:
        """
        Add(self: XmlSchemas, schema: XmlSchema) -> int
        Add(self: XmlSchemas, schema: XmlSchema, baseUri: Uri) -> int
        Add(self: XmlSchemas, schemas: XmlSchemas)
        """
        ...

    def AddReference(self, schema:XmlSchema): # -> 
        """ AddReference(self: XmlSchemas, schema: XmlSchema) """
        ...

    def Compile(self, handler:ValidationEventHandler, fullCompile:bool): # -> 
        """ Compile(self: XmlSchemas, handler: ValidationEventHandler, fullCompile: bool) """
        ...

    def Contains(self, *__args:XmlSchema) -> bool:
        """
        Contains(self: XmlSchemas, schema: XmlSchema) -> bool
        Contains(self: XmlSchemas, targetNamespace: str) -> bool
        """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: XmlSchemas, array: Array[XmlSchema], index: int) """
        ...

    def Find(self, name:XmlQualifiedName, type:Type) -> object:
        """ Find(self: XmlSchemas, name: XmlQualifiedName, type: Type) -> object """
        ...

    def GetSchemas(self, ns:str) -> IList:
        """ GetSchemas(self: XmlSchemas, ns: str) -> IList """
        ...

    def IndexOf(self, schema:XmlSchema) -> int:
        """ IndexOf(self: XmlSchemas, schema: XmlSchema) -> int """
        ...

    def Insert(self, index:int, schema:XmlSchema): # -> 
        """ Insert(self: XmlSchemas, index: int, schema: XmlSchema) """
        ...

    @staticmethod
    def IsDataSet(schema:XmlSchema) -> bool:
        """ IsDataSet(schema: XmlSchema) -> bool """
        ...

    def Remove(self, schema:XmlSchema): # -> 
        """ Remove(self: XmlSchemas, schema: XmlSchema) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class XmlSerializationCollectionFixupCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ XmlSerializationCollectionFixupCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, collection:object, collectionItems:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: XmlSerializationCollectionFixupCallback, collection: object, collectionItems: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: XmlSerializationCollectionFixupCallback, result: IAsyncResult) """
        ...

    def Invoke(self, collection:object, collectionItems:object): # -> 
        """ Invoke(self: XmlSerializationCollectionFixupCallback, collection: object, collectionItems: object) """
        ...


class XmlSerializationFixupCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ XmlSerializationFixupCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, fixup:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: XmlSerializationFixupCallback, fixup: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: XmlSerializationFixupCallback, result: IAsyncResult) """
        ...

    def Invoke(self, fixup:object): # -> 
        """ Invoke(self: XmlSerializationFixupCallback, fixup: object) """
        ...


class XmlSerializationGeneratedCode: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class XmlSerializationReadCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ XmlSerializationReadCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: XmlSerializationReadCallback, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> object:
        """ EndInvoke(self: XmlSerializationReadCallback, result: IAsyncResult) -> object """
        ...

    def Invoke(self) -> object:
        """ Invoke(self: XmlSerializationReadCallback) -> object """
        ...


class XmlSerializationReader(XmlSerializationGeneratedCode): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DecodeName(self):
        ...

    @property
    def Document(self):
        ...

    @property
    def IsReturnValue(self):
        ...

    @property
    def Reader(self):
        ...

    @property
    def ReaderCount(self):
        ...


    def AddFixup(self, *args): #cannot find CLR method
        """ AddFixup(self: XmlSerializationReader, fixup: Fixup)AddFixup(self: XmlSerializationReader, fixup: CollectionFixup) """
        ...

    def AddReadCallback(self, *args): #cannot find CLR method
        """ AddReadCallback(self: XmlSerializationReader, name: str, ns: str, type: Type, read: XmlSerializationReadCallback) """
        ...

    def AddTarget(self, *args): #cannot find CLR method
        """ AddTarget(self: XmlSerializationReader, id: str, o: object) """
        ...

    def CheckReaderCount(self, *args): #cannot find CLR method
        """ CheckReaderCount(self: XmlSerializationReader, whileIterations: int, readerCount: int) -> (int, int) """
        ...

    def CollapseWhitespace(self, *args): #cannot find CLR method
        """ CollapseWhitespace(self: XmlSerializationReader, value: str) -> str """
        ...

    def CollectionFixup(self, *args): #cannot find CLR method
        """ CollectionFixup(collection: object, callback: XmlSerializationCollectionFixupCallback, collectionItems: object) """
        ...

    def CreateAbstractTypeException(self, *args): #cannot find CLR method
        """ CreateAbstractTypeException(self: XmlSerializationReader, name: str, ns: str) -> Exception """
        ...

    def CreateBadDerivationException(self, *args): #cannot find CLR method
        """ CreateBadDerivationException(self: XmlSerializationReader, xsdDerived: str, nsDerived: str, xsdBase: str, nsBase: str, clrDerived: str, clrBase: str) -> Exception """
        ...

    def CreateCtorHasSecurityException(self, *args): #cannot find CLR method
        """ CreateCtorHasSecurityException(self: XmlSerializationReader, typeName: str) -> Exception """
        ...

    def CreateInaccessibleConstructorException(self, *args): #cannot find CLR method
        """ CreateInaccessibleConstructorException(self: XmlSerializationReader, typeName: str) -> Exception """
        ...

    def CreateInvalidCastException(self, *args): #cannot find CLR method
        """
        CreateInvalidCastException(self: XmlSerializationReader, type: Type, value: object) -> Exception
        CreateInvalidCastException(self: XmlSerializationReader, type: Type, value: object, id: str) -> Exception
        """
        ...

    def CreateMissingIXmlSerializableType(self, *args): #cannot find CLR method
        """ CreateMissingIXmlSerializableType(self: XmlSerializationReader, name: str, ns: str, clrType: str) -> Exception """
        ...

    def CreateReadOnlyCollectionException(self, *args): #cannot find CLR method
        """ CreateReadOnlyCollectionException(self: XmlSerializationReader, name: str) -> Exception """
        ...

    def CreateUnknownConstantException(self, *args): #cannot find CLR method
        """ CreateUnknownConstantException(self: XmlSerializationReader, value: str, enumType: Type) -> Exception """
        ...

    def CreateUnknownNodeException(self, *args): #cannot find CLR method
        """ CreateUnknownNodeException(self: XmlSerializationReader) -> Exception """
        ...

    def CreateUnknownTypeException(self, *args): #cannot find CLR method
        """ CreateUnknownTypeException(self: XmlSerializationReader, type: XmlQualifiedName) -> Exception """
        ...

    def EnsureArrayIndex(self, *args): #cannot find CLR method
        """ EnsureArrayIndex(self: XmlSerializationReader, a: Array, index: int, elementType: Type) -> Array """
        ...

    def Fixup(self, *args): #cannot find CLR method
        """
        Fixup(o: object, callback: XmlSerializationFixupCallback, count: int)
        Fixup(o: object, callback: XmlSerializationFixupCallback, ids: Array[str])
        """
        ...

    def FixupArrayRefs(self, *args): #cannot find CLR method
        """ FixupArrayRefs(self: XmlSerializationReader, fixup: object) """
        ...

    def GetArrayLength(self, *args): #cannot find CLR method
        """ GetArrayLength(self: XmlSerializationReader, name: str, ns: str) -> int """
        ...

    def GetNullAttr(self, *args): #cannot find CLR method
        """ GetNullAttr(self: XmlSerializationReader) -> bool """
        ...

    def GetTarget(self, *args): #cannot find CLR method
        """ GetTarget(self: XmlSerializationReader, id: str) -> object """
        ...

    def GetXsiType(self, *args): #cannot find CLR method
        """ GetXsiType(self: XmlSerializationReader) -> XmlQualifiedName """
        ...

    def InitCallbacks(self, *args): #cannot find CLR method
        """ InitCallbacks(self: XmlSerializationReader) """
        ...

    def InitIDs(self, *args): #cannot find CLR method
        """ InitIDs(self: XmlSerializationReader) """
        ...

    def IsXmlnsAttribute(self, *args): #cannot find CLR method
        """ IsXmlnsAttribute(self: XmlSerializationReader, name: str) -> bool """
        ...

    def ParseWsdlArrayType(self, *args): #cannot find CLR method
        """ ParseWsdlArrayType(self: XmlSerializationReader, attr: XmlAttribute) """
        ...

    def ReadElementQualifiedName(self, *args): #cannot find CLR method
        """ ReadElementQualifiedName(self: XmlSerializationReader) -> XmlQualifiedName """
        ...

    def ReadEndElement(self, *args): #cannot find CLR method
        """ ReadEndElement(self: XmlSerializationReader) """
        ...

    def ReadNull(self, *args): #cannot find CLR method
        """ ReadNull(self: XmlSerializationReader) -> bool """
        ...

    def ReadNullableQualifiedName(self, *args): #cannot find CLR method
        """ ReadNullableQualifiedName(self: XmlSerializationReader) -> XmlQualifiedName """
        ...

    def ReadNullableString(self, *args): #cannot find CLR method
        """ ReadNullableString(self: XmlSerializationReader) -> str """
        ...

    def ReadReference(self, *args): #cannot find CLR method
        """ ReadReference(self: XmlSerializationReader) -> (bool, str) """
        ...

    def ReadReferencedElement(self, *args): #cannot find CLR method
        """
        ReadReferencedElement(self: XmlSerializationReader) -> object
        ReadReferencedElement(self: XmlSerializationReader, name: str, ns: str) -> object
        """
        ...

    def ReadReferencedElements(self, *args): #cannot find CLR method
        """ ReadReferencedElements(self: XmlSerializationReader) """
        ...

    def ReadReferencingElement(self, *args): #cannot find CLR method
        """
        ReadReferencingElement(self: XmlSerializationReader) -> (object, str)
        ReadReferencingElement(self: XmlSerializationReader, name: str, ns: str) -> (object, str)
        ReadReferencingElement(self: XmlSerializationReader, name: str, ns: str, elementCanBeType: bool) -> (object, str)
        """
        ...

    def ReadSerializable(self, *args): #cannot find CLR method
        """
        ReadSerializable(self: XmlSerializationReader, serializable: IXmlSerializable) -> IXmlSerializable
        ReadSerializable(self: XmlSerializationReader, serializable: IXmlSerializable, wrappedAny: bool) -> IXmlSerializable
        """
        ...

    def ReadString(self, *args): #cannot find CLR method
        """
        ReadString(self: XmlSerializationReader, value: str) -> str
        ReadString(self: XmlSerializationReader, value: str, trim: bool) -> str
        """
        ...

    def ReadTypedNull(self, *args): #cannot find CLR method
        """ ReadTypedNull(self: XmlSerializationReader, type: XmlQualifiedName) -> object """
        ...

    def ReadTypedPrimitive(self, *args): #cannot find CLR method
        """ ReadTypedPrimitive(self: XmlSerializationReader, type: XmlQualifiedName) -> object """
        ...

    def ReadXmlDocument(self, *args): #cannot find CLR method
        """ ReadXmlDocument(self: XmlSerializationReader, wrapped: bool) -> XmlDocument """
        ...

    def ReadXmlNode(self, *args): #cannot find CLR method
        """ ReadXmlNode(self: XmlSerializationReader, wrapped: bool) -> XmlNode """
        ...

    def Referenced(self, *args): #cannot find CLR method
        """ Referenced(self: XmlSerializationReader, o: object) """
        ...

    def ResolveDynamicAssembly(self, *args): #cannot find CLR method
        """ ResolveDynamicAssembly(assemblyFullName: str) -> Assembly """
        ...

    def ShrinkArray(self, *args): #cannot find CLR method
        """ ShrinkArray(self: XmlSerializationReader, a: Array, length: int, elementType: Type, isNullable: bool) -> Array """
        ...

    def ToByteArrayBase64(self, *args): #cannot find CLR method
        """
        ToByteArrayBase64(value: str) -> Array[Byte]
        ToByteArrayBase64(self: XmlSerializationReader, isNull: bool) -> Array[Byte]
        """
        ...

    def ToByteArrayHex(self, *args): #cannot find CLR method
        """
        ToByteArrayHex(value: str) -> Array[Byte]
        ToByteArrayHex(self: XmlSerializationReader, isNull: bool) -> Array[Byte]
        """
        ...

    def ToChar(self, *args): #cannot find CLR method
        """ ToChar(value: str) -> Char """
        ...

    def ToDate(self, *args): #cannot find CLR method
        """ ToDate(value: str) -> DateTime """
        ...

    def ToDateTime(self, *args): #cannot find CLR method
        """ ToDateTime(value: str) -> DateTime """
        ...

    def ToEnum(self, *args): #cannot find CLR method
        """ ToEnum(value: str, h: Hashtable, typeName: str) -> Int64 """
        ...

    def ToTime(self, *args): #cannot find CLR method
        """ ToTime(value: str) -> DateTime """
        ...

    def ToXmlName(self, *args): #cannot find CLR method
        """ ToXmlName(value: str) -> str """
        ...

    def ToXmlNCName(self, *args): #cannot find CLR method
        """ ToXmlNCName(value: str) -> str """
        ...

    def ToXmlNmToken(self, *args): #cannot find CLR method
        """ ToXmlNmToken(value: str) -> str """
        ...

    def ToXmlNmTokens(self, *args): #cannot find CLR method
        """ ToXmlNmTokens(value: str) -> str """
        ...

    def ToXmlQualifiedName(self, *args): #cannot find CLR method
        """ ToXmlQualifiedName(self: XmlSerializationReader, value: str) -> XmlQualifiedName """
        ...

    def UnknownAttribute(self, *args): #cannot find CLR method
        """ UnknownAttribute(self: XmlSerializationReader, o: object, attr: XmlAttribute)UnknownAttribute(self: XmlSerializationReader, o: object, attr: XmlAttribute, qnames: str) """
        ...

    def UnknownElement(self, *args): #cannot find CLR method
        """ UnknownElement(self: XmlSerializationReader, o: object, elem: XmlElement)UnknownElement(self: XmlSerializationReader, o: object, elem: XmlElement, qnames: str) """
        ...

    def UnknownNode(self, *args): #cannot find CLR method
        """ UnknownNode(self: XmlSerializationReader, o: object)UnknownNode(self: XmlSerializationReader, o: object, qnames: str) """
        ...

    def UnreferencedObject(self, *args): #cannot find CLR method
        """ UnreferencedObject(self: XmlSerializationReader, id: str, o: object) """
        ...



class XmlSerializationWriteCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ XmlSerializationWriteCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, o:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: XmlSerializationWriteCallback, o: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: XmlSerializationWriteCallback, result: IAsyncResult) """
        ...

    def Invoke(self, o:object): # -> 
        """ Invoke(self: XmlSerializationWriteCallback, o: object) """
        ...


class XmlSerializationWriter(XmlSerializationGeneratedCode): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EscapeName(self):
        ...

    @property
    def Namespaces(self):
        ...

    @property
    def Writer(self):
        ...


    def AddWriteCallback(self, *args): #cannot find CLR method
        """ AddWriteCallback(self: XmlSerializationWriter, type: Type, typeName: str, typeNs: str, callback: XmlSerializationWriteCallback) """
        ...

    def CreateChoiceIdentifierValueException(self, *args): #cannot find CLR method
        """ CreateChoiceIdentifierValueException(self: XmlSerializationWriter, value: str, identifier: str, name: str, ns: str) -> Exception """
        ...

    def CreateInvalidAnyTypeException(self, *args): #cannot find CLR method
        """
        CreateInvalidAnyTypeException(self: XmlSerializationWriter, o: object) -> Exception
        CreateInvalidAnyTypeException(self: XmlSerializationWriter, type: Type) -> Exception
        """
        ...

    def CreateInvalidChoiceIdentifierValueException(self, *args): #cannot find CLR method
        """ CreateInvalidChoiceIdentifierValueException(self: XmlSerializationWriter, type: str, identifier: str) -> Exception """
        ...

    def CreateInvalidEnumValueException(self, *args): #cannot find CLR method
        """ CreateInvalidEnumValueException(self: XmlSerializationWriter, value: object, typeName: str) -> Exception """
        ...

    def CreateMismatchChoiceException(self, *args): #cannot find CLR method
        """ CreateMismatchChoiceException(self: XmlSerializationWriter, value: str, elementName: str, enumValue: str) -> Exception """
        ...

    def CreateUnknownAnyElementException(self, *args): #cannot find CLR method
        """ CreateUnknownAnyElementException(self: XmlSerializationWriter, name: str, ns: str) -> Exception """
        ...

    def CreateUnknownTypeException(self, *args): #cannot find CLR method
        """
        CreateUnknownTypeException(self: XmlSerializationWriter, o: object) -> Exception
        CreateUnknownTypeException(self: XmlSerializationWriter, type: Type) -> Exception
        """
        ...

    def FromByteArrayBase64(self, *args): #cannot find CLR method
        """ FromByteArrayBase64(value: Array[Byte]) -> Array[Byte] """
        ...

    def FromByteArrayHex(self, *args): #cannot find CLR method
        """ FromByteArrayHex(value: Array[Byte]) -> str """
        ...

    def FromChar(self, *args): #cannot find CLR method
        """ FromChar(value: Char) -> str """
        ...

    def FromDate(self, *args): #cannot find CLR method
        """ FromDate(value: DateTime) -> str """
        ...

    def FromDateTime(self, *args): #cannot find CLR method
        """ FromDateTime(value: DateTime) -> str """
        ...

    def FromEnum(self, *args): #cannot find CLR method
        """
        FromEnum(value: Int64, values: Array[str], ids: Array[Int64]) -> str
        FromEnum(value: Int64, values: Array[str], ids: Array[Int64], typeName: str) -> str
        """
        ...

    def FromTime(self, *args): #cannot find CLR method
        """ FromTime(value: DateTime) -> str """
        ...

    def FromXmlName(self, *args): #cannot find CLR method
        """ FromXmlName(name: str) -> str """
        ...

    def FromXmlNCName(self, *args): #cannot find CLR method
        """ FromXmlNCName(ncName: str) -> str """
        ...

    def FromXmlNmToken(self, *args): #cannot find CLR method
        """ FromXmlNmToken(nmToken: str) -> str """
        ...

    def FromXmlNmTokens(self, *args): #cannot find CLR method
        """ FromXmlNmTokens(nmTokens: str) -> str """
        ...

    def FromXmlQualifiedName(self, *args): #cannot find CLR method
        """
        FromXmlQualifiedName(self: XmlSerializationWriter, xmlQualifiedName: XmlQualifiedName) -> str
        FromXmlQualifiedName(self: XmlSerializationWriter, xmlQualifiedName: XmlQualifiedName, ignoreEmpty: bool) -> str
        """
        ...

    def InitCallbacks(self, *args): #cannot find CLR method
        """ InitCallbacks(self: XmlSerializationWriter) """
        ...

    def ResolveDynamicAssembly(self, *args): #cannot find CLR method
        """ ResolveDynamicAssembly(assemblyFullName: str) -> Assembly """
        ...

    def TopLevelElement(self, *args): #cannot find CLR method
        """ TopLevelElement(self: XmlSerializationWriter) """
        ...

    def WriteAttribute(self, *args): #cannot find CLR method
        """ WriteAttribute(self: XmlSerializationWriter, localName: str, value: str)WriteAttribute(self: XmlSerializationWriter, localName: str, value: Array[Byte])WriteAttribute(self: XmlSerializationWriter, prefix: str, localName: str, ns: str, value: str)WriteAttribute(self: XmlSerializationWriter, localName: str, ns: str, value: str)WriteAttribute(self: XmlSerializationWriter, localName: str, ns: str, value: Array[Byte]) """
        ...

    def WriteElementEncoded(self, *args): #cannot find CLR method
        """ WriteElementEncoded(self: XmlSerializationWriter, node: XmlNode, name: str, ns: str, isNullable: bool, any: bool) """
        ...

    def WriteElementLiteral(self, *args): #cannot find CLR method
        """ WriteElementLiteral(self: XmlSerializationWriter, node: XmlNode, name: str, ns: str, isNullable: bool, any: bool) """
        ...

    def WriteElementQualifiedName(self, *args): #cannot find CLR method
        """ WriteElementQualifiedName(self: XmlSerializationWriter, localName: str, value: XmlQualifiedName)WriteElementQualifiedName(self: XmlSerializationWriter, localName: str, value: XmlQualifiedName, xsiType: XmlQualifiedName)WriteElementQualifiedName(self: XmlSerializationWriter, localName: str, ns: str, value: XmlQualifiedName)WriteElementQualifiedName(self: XmlSerializationWriter, localName: str, ns: str, value: XmlQualifiedName, xsiType: XmlQualifiedName) """
        ...

    def WriteElementString(self, *args): #cannot find CLR method
        """ WriteElementString(self: XmlSerializationWriter, localName: str, value: str)WriteElementString(self: XmlSerializationWriter, localName: str, ns: str, value: str)WriteElementString(self: XmlSerializationWriter, localName: str, value: str, xsiType: XmlQualifiedName)WriteElementString(self: XmlSerializationWriter, localName: str, ns: str, value: str, xsiType: XmlQualifiedName) """
        ...

    def WriteElementStringRaw(self, *args): #cannot find CLR method
        """ WriteElementStringRaw(self: XmlSerializationWriter, localName: str, value: str)WriteElementStringRaw(self: XmlSerializationWriter, localName: str, value: Array[Byte])WriteElementStringRaw(self: XmlSerializationWriter, localName: str, ns: str, value: str)WriteElementStringRaw(self: XmlSerializationWriter, localName: str, ns: str, value: Array[Byte])WriteElementStringRaw(self: XmlSerializationWriter, localName: str, value: str, xsiType: XmlQualifiedName)WriteElementStringRaw(self: XmlSerializationWriter, localName: str, value: Array[Byte], xsiType: XmlQualifiedName)WriteElementStringRaw(self: XmlSerializationWriter, localName: str, ns: str, value: str, xsiType: XmlQualifiedName)WriteElementStringRaw(self: XmlSerializationWriter, localName: str, ns: str, value: Array[Byte], xsiType: XmlQualifiedName) """
        ...

    def WriteEmptyTag(self, *args): #cannot find CLR method
        """ WriteEmptyTag(self: XmlSerializationWriter, name: str)WriteEmptyTag(self: XmlSerializationWriter, name: str, ns: str) """
        ...

    def WriteEndElement(self, *args): #cannot find CLR method
        """ WriteEndElement(self: XmlSerializationWriter)WriteEndElement(self: XmlSerializationWriter, o: object) """
        ...

    def WriteId(self, *args): #cannot find CLR method
        """ WriteId(self: XmlSerializationWriter, o: object) """
        ...

    def WriteNamespaceDeclarations(self, *args): #cannot find CLR method
        """ WriteNamespaceDeclarations(self: XmlSerializationWriter, xmlns: XmlSerializerNamespaces) """
        ...

    def WriteNullableQualifiedNameEncoded(self, *args): #cannot find CLR method
        """ WriteNullableQualifiedNameEncoded(self: XmlSerializationWriter, name: str, ns: str, value: XmlQualifiedName, xsiType: XmlQualifiedName) """
        ...

    def WriteNullableQualifiedNameLiteral(self, *args): #cannot find CLR method
        """ WriteNullableQualifiedNameLiteral(self: XmlSerializationWriter, name: str, ns: str, value: XmlQualifiedName) """
        ...

    def WriteNullableStringEncoded(self, *args): #cannot find CLR method
        """ WriteNullableStringEncoded(self: XmlSerializationWriter, name: str, ns: str, value: str, xsiType: XmlQualifiedName) """
        ...

    def WriteNullableStringEncodedRaw(self, *args): #cannot find CLR method
        """ WriteNullableStringEncodedRaw(self: XmlSerializationWriter, name: str, ns: str, value: str, xsiType: XmlQualifiedName)WriteNullableStringEncodedRaw(self: XmlSerializationWriter, name: str, ns: str, value: Array[Byte], xsiType: XmlQualifiedName) """
        ...

    def WriteNullableStringLiteral(self, *args): #cannot find CLR method
        """ WriteNullableStringLiteral(self: XmlSerializationWriter, name: str, ns: str, value: str) """
        ...

    def WriteNullableStringLiteralRaw(self, *args): #cannot find CLR method
        """ WriteNullableStringLiteralRaw(self: XmlSerializationWriter, name: str, ns: str, value: str)WriteNullableStringLiteralRaw(self: XmlSerializationWriter, name: str, ns: str, value: Array[Byte]) """
        ...

    def WriteNullTagEncoded(self, *args): #cannot find CLR method
        """ WriteNullTagEncoded(self: XmlSerializationWriter, name: str)WriteNullTagEncoded(self: XmlSerializationWriter, name: str, ns: str) """
        ...

    def WriteNullTagLiteral(self, *args): #cannot find CLR method
        """ WriteNullTagLiteral(self: XmlSerializationWriter, name: str)WriteNullTagLiteral(self: XmlSerializationWriter, name: str, ns: str) """
        ...

    def WritePotentiallyReferencingElement(self, *args): #cannot find CLR method
        """ WritePotentiallyReferencingElement(self: XmlSerializationWriter, n: str, ns: str, o: object)WritePotentiallyReferencingElement(self: XmlSerializationWriter, n: str, ns: str, o: object, ambientType: Type)WritePotentiallyReferencingElement(self: XmlSerializationWriter, n: str, ns: str, o: object, ambientType: Type, suppressReference: bool)WritePotentiallyReferencingElement(self: XmlSerializationWriter, n: str, ns: str, o: object, ambientType: Type, suppressReference: bool, isNullable: bool) """
        ...

    def WriteReferencedElements(self, *args): #cannot find CLR method
        """ WriteReferencedElements(self: XmlSerializationWriter) """
        ...

    def WriteReferencingElement(self, *args): #cannot find CLR method
        """ WriteReferencingElement(self: XmlSerializationWriter, n: str, ns: str, o: object)WriteReferencingElement(self: XmlSerializationWriter, n: str, ns: str, o: object, isNullable: bool) """
        ...

    def WriteRpcResult(self, *args): #cannot find CLR method
        """ WriteRpcResult(self: XmlSerializationWriter, name: str, ns: str) """
        ...

    def WriteSerializable(self, *args): #cannot find CLR method
        """ WriteSerializable(self: XmlSerializationWriter, serializable: IXmlSerializable, name: str, ns: str, isNullable: bool)WriteSerializable(self: XmlSerializationWriter, serializable: IXmlSerializable, name: str, ns: str, isNullable: bool, wrapped: bool) """
        ...

    def WriteStartDocument(self, *args): #cannot find CLR method
        """ WriteStartDocument(self: XmlSerializationWriter) """
        ...

    def WriteStartElement(self, *args): #cannot find CLR method
        """ WriteStartElement(self: XmlSerializationWriter, name: str)WriteStartElement(self: XmlSerializationWriter, name: str, ns: str)WriteStartElement(self: XmlSerializationWriter, name: str, ns: str, writePrefixed: bool)WriteStartElement(self: XmlSerializationWriter, name: str, ns: str, o: object)WriteStartElement(self: XmlSerializationWriter, name: str, ns: str, o: object, writePrefixed: bool)WriteStartElement(self: XmlSerializationWriter, name: str, ns: str, o: object, writePrefixed: bool, xmlns: XmlSerializerNamespaces) """
        ...

    def WriteTypedPrimitive(self, *args): #cannot find CLR method
        """ WriteTypedPrimitive(self: XmlSerializationWriter, name: str, ns: str, o: object, xsiType: bool) """
        ...

    def WriteValue(self, *args): #cannot find CLR method
        """ WriteValue(self: XmlSerializationWriter, value: str)WriteValue(self: XmlSerializationWriter, value: Array[Byte]) """
        ...

    def WriteXmlAttribute(self, *args): #cannot find CLR method
        """ WriteXmlAttribute(self: XmlSerializationWriter, node: XmlNode)WriteXmlAttribute(self: XmlSerializationWriter, node: XmlNode, container: object) """
        ...

    def WriteXsiType(self, *args): #cannot find CLR method
        """ WriteXsiType(self: XmlSerializationWriter, name: str, ns: str) """
        ...


class XmlSerializer: # skipped bases: <type 'object'>, <type 'object'>
    """
    XmlSerializer(type: Type, overrides: XmlAttributeOverrides, extraTypes: Array[Type], root: XmlRootAttribute, defaultNamespace: str)
    XmlSerializer(type: Type, root: XmlRootAttribute)
    XmlSerializer(type: Type, extraTypes: Array[Type])
    XmlSerializer(type: Type, overrides: XmlAttributeOverrides)
    XmlSerializer(xmlTypeMapping: XmlTypeMapping)
    XmlSerializer(type: Type)
    XmlSerializer(type: Type, defaultNamespace: str)
    XmlSerializer(type: Type, overrides: XmlAttributeOverrides, extraTypes: Array[Type], root: XmlRootAttribute, defaultNamespace: str, location: str)
    XmlSerializer(type: Type, overrides: XmlAttributeOverrides, extraTypes: Array[Type], root: XmlRootAttribute, defaultNamespace: str, location: str, evidence: Evidence)
    """
    def CanDeserialize(self, xmlReader:XmlReader) -> bool:
        """ CanDeserialize(self: XmlSerializer, xmlReader: XmlReader) -> bool """
        ...

    def CreateReader(self, *args): #cannot find CLR method
        """ CreateReader(self: XmlSerializer) -> XmlSerializationReader """
        ...

    def CreateWriter(self, *args): #cannot find CLR method
        """ CreateWriter(self: XmlSerializer) -> XmlSerializationWriter """
        ...

    def Deserialize(self, *__args:Stream) -> object:
        """
        Deserialize(self: XmlSerializer, stream: Stream) -> object
        Deserialize(self: XmlSerializer, textReader: TextReader) -> object
        Deserialize(self: XmlSerializer, xmlReader: XmlReader) -> object
        Deserialize(self: XmlSerializer, xmlReader: XmlReader, events: XmlDeserializationEvents) -> object
        Deserialize(self: XmlSerializer, xmlReader: XmlReader, encodingStyle: str) -> object
        Deserialize(self: XmlSerializer, xmlReader: XmlReader, encodingStyle: str, events: XmlDeserializationEvents) -> object
        """
        ...

    @staticmethod
    def FromMappings(mappings:Array, *__args:Type) -> Array:
        """
        FromMappings(mappings: Array[XmlMapping]) -> Array[XmlSerializer]
        FromMappings(mappings: Array[XmlMapping], type: Type) -> Array[XmlSerializer]
        FromMappings(mappings: Array[XmlMapping], evidence: Evidence) -> Array[XmlSerializer]
        """
        ...

    @staticmethod
    def FromTypes(types:Array) -> Array:
        """ FromTypes(types: Array[Type]) -> Array[XmlSerializer] """
        ...

    @staticmethod
    def GenerateSerializer(types:Array, mappings:Array, parameters:CompilerParameters = ...) -> Assembly:
        """
        GenerateSerializer(types: Array[Type], mappings: Array[XmlMapping]) -> Assembly
        GenerateSerializer(types: Array[Type], mappings: Array[XmlMapping], parameters: CompilerParameters) -> Assembly
        """
        ...

    @staticmethod
    def GetXmlSerializerAssemblyName(type:Type, defaultNamespace:str = ...) -> str:
        """
        GetXmlSerializerAssemblyName(type: Type) -> str
        GetXmlSerializerAssemblyName(type: Type, defaultNamespace: str) -> str
        """
        ...

    def Serialize(self, *__args): # -> 
        """ Serialize(self: XmlSerializer, textWriter: TextWriter, o: object)Serialize(self: XmlSerializer, textWriter: TextWriter, o: object, namespaces: XmlSerializerNamespaces)Serialize(self: XmlSerializer, stream: Stream, o: object)Serialize(self: XmlSerializer, stream: Stream, o: object, namespaces: XmlSerializerNamespaces)Serialize(self: XmlSerializer, xmlWriter: XmlWriter, o: object)Serialize(self: XmlSerializer, xmlWriter: XmlWriter, o: object, namespaces: XmlSerializerNamespaces)Serialize(self: XmlSerializer, xmlWriter: XmlWriter, o: object, namespaces: XmlSerializerNamespaces, encodingStyle: str)Serialize(self: XmlSerializer, xmlWriter: XmlWriter, o: object, namespaces: XmlSerializerNamespaces, encodingStyle: str, id: str) """
        ...

    UnknownAttribute = ...
    UnknownElement = ...
    UnknownNode = ...
    UnreferencedObject = ...


class XmlSerializerAssemblyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    XmlSerializerAssemblyAttribute()
    XmlSerializerAssemblyAttribute(assemblyName: str)
    XmlSerializerAssemblyAttribute(assemblyName: str, codeBase: str)
    """
    @property
    def AssemblyName(self) -> str:
        """
        Get: AssemblyName(self: XmlSerializerAssemblyAttribute) -> str
        Set: AssemblyName(self: XmlSerializerAssemblyAttribute) = value
        """
        ...

    @property
    def CodeBase(self) -> str:
        """
        Get: CodeBase(self: XmlSerializerAssemblyAttribute) -> str
        Set: CodeBase(self: XmlSerializerAssemblyAttribute) = value
        """
        ...


    def __new__(cls, assemblyName:str = ..., codeBase:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, assemblyName: str)
        __new__(cls: type, assemblyName: str, codeBase: str)
        """
        ...


class XmlSerializerFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ XmlSerializerFactory() """
    def CreateSerializer(self, *__args:XmlTypeMapping) -> XmlSerializer:
        """
        CreateSerializer(self: XmlSerializerFactory, type: Type, overrides: XmlAttributeOverrides, extraTypes: Array[Type], root: XmlRootAttribute, defaultNamespace: str) -> XmlSerializer
        CreateSerializer(self: XmlSerializerFactory, type: Type, extraTypes: Array[Type]) -> XmlSerializer
        CreateSerializer(self: XmlSerializerFactory, xmlTypeMapping: XmlTypeMapping) -> XmlSerializer
        CreateSerializer(self: XmlSerializerFactory, type: Type) -> XmlSerializer
        CreateSerializer(self: XmlSerializerFactory, type: Type, defaultNamespace: str) -> XmlSerializer
        CreateSerializer(self: XmlSerializerFactory, type: Type, overrides: XmlAttributeOverrides, extraTypes: Array[Type], root: XmlRootAttribute, defaultNamespace: str, location: str) -> XmlSerializer
        CreateSerializer(self: XmlSerializerFactory, type: Type, overrides: XmlAttributeOverrides, extraTypes: Array[Type], root: XmlRootAttribute, defaultNamespace: str, location: str, evidence: Evidence) -> XmlSerializer
        CreateSerializer(self: XmlSerializerFactory, type: Type, root: XmlRootAttribute) -> XmlSerializer
        CreateSerializer(self: XmlSerializerFactory, type: Type, overrides: XmlAttributeOverrides) -> XmlSerializer
        """
        ...


class XmlSerializerImplementation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Reader(self) -> XmlSerializationReader:
        """ Get: Reader(self: XmlSerializerImplementation) -> XmlSerializationReader """
        ...

    @property
    def ReadMethods(self) -> Hashtable:
        """ Get: ReadMethods(self: XmlSerializerImplementation) -> Hashtable """
        ...

    @property
    def TypedSerializers(self) -> Hashtable:
        """ Get: TypedSerializers(self: XmlSerializerImplementation) -> Hashtable """
        ...

    @property
    def WriteMethods(self) -> Hashtable:
        """ Get: WriteMethods(self: XmlSerializerImplementation) -> Hashtable """
        ...

    @property
    def Writer(self) -> XmlSerializationWriter:
        """ Get: Writer(self: XmlSerializerImplementation) -> XmlSerializationWriter """
        ...


    def CanSerialize(self, type:Type) -> bool:
        """ CanSerialize(self: XmlSerializerImplementation, type: Type) -> bool """
        ...

    def GetSerializer(self, type:Type) -> XmlSerializer:
        """ GetSerializer(self: XmlSerializerImplementation, type: Type) -> XmlSerializer """
        ...


class XmlSerializerNamespaces: # skipped bases: <type 'object'>, <type 'object'>
    """
    XmlSerializerNamespaces()
    XmlSerializerNamespaces(namespaces: XmlSerializerNamespaces)
    XmlSerializerNamespaces(namespaces: Array[XmlQualifiedName])
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: XmlSerializerNamespaces) -> int """
        ...


    def Add(self, prefix:str, ns:str): # -> 
        """ Add(self: XmlSerializerNamespaces, prefix: str, ns: str) """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: XmlSerializerNamespaces) -> Array[XmlQualifiedName] """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class XmlSerializerVersionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    XmlSerializerVersionAttribute()
    XmlSerializerVersionAttribute(type: Type)
    """
    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: XmlSerializerVersionAttribute) -> str
        Set: Namespace(self: XmlSerializerVersionAttribute) = value
        """
        ...

    @property
    def ParentAssemblyId(self) -> str:
        """
        Get: ParentAssemblyId(self: XmlSerializerVersionAttribute) -> str
        Set: ParentAssemblyId(self: XmlSerializerVersionAttribute) = value
        """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: XmlSerializerVersionAttribute) -> Type
        Set: Type(self: XmlSerializerVersionAttribute) = value
        """
        ...

    @property
    def Version(self) -> str:
        """
        Get: Version(self: XmlSerializerVersionAttribute) -> str
        Set: Version(self: XmlSerializerVersionAttribute) = value
        """
        ...


    def __new__(cls, type:Type = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: Type)
        """
        ...


class XmlTextAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    XmlTextAttribute()
    XmlTextAttribute(type: Type)
    """
    @property
    def DataType(self) -> str:
        """
        Get: DataType(self: XmlTextAttribute) -> str
        Set: DataType(self: XmlTextAttribute) = value
        """
        ...

    @property
    def Type(self) -> Type:
        """
        Get: Type(self: XmlTextAttribute) -> Type
        Set: Type(self: XmlTextAttribute) = value
        """
        ...


    def __new__(cls, type:Type = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: Type)
        """
        ...


class XmlTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    XmlTypeAttribute()
    XmlTypeAttribute(typeName: str)
    """
    @property
    def AnonymousType(self) -> bool:
        """
        Get: AnonymousType(self: XmlTypeAttribute) -> bool
        Set: AnonymousType(self: XmlTypeAttribute) = value
        """
        ...

    @property
    def IncludeInSchema(self) -> bool:
        """
        Get: IncludeInSchema(self: XmlTypeAttribute) -> bool
        Set: IncludeInSchema(self: XmlTypeAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: XmlTypeAttribute) -> str
        Set: Namespace(self: XmlTypeAttribute) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: XmlTypeAttribute) -> str
        Set: TypeName(self: XmlTypeAttribute) = value
        """
        ...


    def __new__(cls, typeName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, typeName: str)
        """
        ...


class XmlTypeMapping(XmlMapping): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def TypeFullName(self) -> str:
        """ Get: TypeFullName(self: XmlTypeMapping) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: XmlTypeMapping) -> str """
        ...

    @property
    def XsdTypeName(self) -> str:
        """ Get: XsdTypeName(self: XmlTypeMapping) -> str """
        ...

    @property
    def XsdTypeNamespace(self) -> str:
        """ Get: XsdTypeNamespace(self: XmlTypeMapping) -> str """
        ...



# variables with complex values

