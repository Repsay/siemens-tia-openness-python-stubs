# encoding: utf-8
# module System.Runtime.Serialization calls itself Serialization
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Runtime.Serialization.Formatters.Soap, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Runtime.Serialization, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import (Array, Attribute, Byte, Char, DateTime, Decimal, Enum, 
    EventArgs, IFormatProvider, Int16, Int64, SByte, Single, SystemException, 
    Type, UInt16, UInt32, UInt64)

from System.CodeDom import (CodeCompileUnit, CodeTypeDeclaration, 
    CodeTypeReference)

from System.CodeDom.Compiler import CodeDomProvider

from System.Collections import (ICollection, IDictionary, IEnumerable, 
    IEnumerator)

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Globalization import DateTimeStyles

from System.IO import Stream

from System.Reflection import Assembly, MemberInfo

from System.Runtime.Serialization.Formatters import (FormatterAssemblyStyle, 
    TypeFilterLevel)

from System.Text import StringBuilder

from System.Xml import (XmlDictionaryReader, XmlDictionaryString, 
    XmlDictionaryWriter, XmlNamespaceManager, XmlQualifiedName, XmlReader, 
    XmlWriter)

from System.Xml.Schema import XmlSchemaElement, XmlSchemaSet, XmlSchemaType

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    IDataContractSurrogate, ISerializationSurrogateProvider, field#)
"""

# no functions
# classes

class CollectionDataContractAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CollectionDataContractAttribute() """
    @property
    def IsItemNameSetExplicitly(self) -> bool:
        """ Get: IsItemNameSetExplicitly(self: CollectionDataContractAttribute) -> bool """
        ...

    @property
    def IsKeyNameSetExplicitly(self) -> bool:
        """ Get: IsKeyNameSetExplicitly(self: CollectionDataContractAttribute) -> bool """
        ...

    @property
    def IsNameSetExplicitly(self) -> bool:
        """ Get: IsNameSetExplicitly(self: CollectionDataContractAttribute) -> bool """
        ...

    @property
    def IsNamespaceSetExplicitly(self) -> bool:
        """ Get: IsNamespaceSetExplicitly(self: CollectionDataContractAttribute) -> bool """
        ...

    @property
    def IsReference(self) -> bool:
        """
        Get: IsReference(self: CollectionDataContractAttribute) -> bool
        Set: IsReference(self: CollectionDataContractAttribute) = value
        """
        ...

    @property
    def IsReferenceSetExplicitly(self) -> bool:
        """ Get: IsReferenceSetExplicitly(self: CollectionDataContractAttribute) -> bool """
        ...

    @property
    def IsValueNameSetExplicitly(self) -> bool:
        """ Get: IsValueNameSetExplicitly(self: CollectionDataContractAttribute) -> bool """
        ...

    @property
    def ItemName(self) -> str:
        """
        Get: ItemName(self: CollectionDataContractAttribute) -> str
        Set: ItemName(self: CollectionDataContractAttribute) = value
        """
        ...

    @property
    def KeyName(self) -> str:
        """
        Get: KeyName(self: CollectionDataContractAttribute) -> str
        Set: KeyName(self: CollectionDataContractAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CollectionDataContractAttribute) -> str
        Set: Name(self: CollectionDataContractAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: CollectionDataContractAttribute) -> str
        Set: Namespace(self: CollectionDataContractAttribute) = value
        """
        ...

    @property
    def ValueName(self) -> str:
        """
        Get: ValueName(self: CollectionDataContractAttribute) -> str
        Set: ValueName(self: CollectionDataContractAttribute) = value
        """
        ...



class ContractNamespaceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ContractNamespaceAttribute(contractNamespace: str) """
    @property
    def ClrNamespace(self) -> str:
        """
        Get: ClrNamespace(self: ContractNamespaceAttribute) -> str
        Set: ClrNamespace(self: ContractNamespaceAttribute) = value
        """
        ...

    @property
    def ContractNamespace(self) -> str:
        """ Get: ContractNamespace(self: ContractNamespaceAttribute) -> str """
        ...


    def __new__(cls, contractNamespace:str) -> Self:
        """ __new__(cls: type, contractNamespace: str) """
        ...


class DataContractAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DataContractAttribute() """
    @property
    def IsNameSetExplicitly(self) -> bool:
        """ Get: IsNameSetExplicitly(self: DataContractAttribute) -> bool """
        ...

    @property
    def IsNamespaceSetExplicitly(self) -> bool:
        """ Get: IsNamespaceSetExplicitly(self: DataContractAttribute) -> bool """
        ...

    @property
    def IsReference(self) -> bool:
        """
        Get: IsReference(self: DataContractAttribute) -> bool
        Set: IsReference(self: DataContractAttribute) = value
        """
        ...

    @property
    def IsReferenceSetExplicitly(self) -> bool:
        """ Get: IsReferenceSetExplicitly(self: DataContractAttribute) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: DataContractAttribute) -> str
        Set: Name(self: DataContractAttribute) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: DataContractAttribute) -> str
        Set: Namespace(self: DataContractAttribute) = value
        """
        ...



class DataContractResolver: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def ResolveName(self, typeName:str, typeNamespace:str, declaredType:Type, knownTypeResolver:DataContractResolver) -> Type:
        """ ResolveName(self: DataContractResolver, typeName: str, typeNamespace: str, declaredType: Type, knownTypeResolver: DataContractResolver) -> Type """
        ...

    def TryResolveType(self, type, declaredType, knownTypeResolver, typeName, typeNamespace) -> Tuple_[bool, XmlDictionaryString, XmlDictionaryString]:
        """ TryResolveType(self: DataContractResolver, type: Type, declaredType: Type, knownTypeResolver: DataContractResolver) -> (bool, XmlDictionaryString, XmlDictionaryString) """
        ...


class XmlObjectSerializer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def IsStartObject(self, reader:XmlReader) -> bool:
        """
        IsStartObject(self: XmlObjectSerializer, reader: XmlReader) -> bool
        IsStartObject(self: XmlObjectSerializer, reader: XmlDictionaryReader) -> bool
        """
        ...

    def ReadObject(self, *__args:XmlDictionaryReader) -> object:
        """
        ReadObject(self: XmlObjectSerializer, reader: XmlDictionaryReader) -> object
        ReadObject(self: XmlObjectSerializer, stream: Stream) -> object
        ReadObject(self: XmlObjectSerializer, reader: XmlReader) -> object
        ReadObject(self: XmlObjectSerializer, reader: XmlReader, verifyObjectName: bool) -> object
        ReadObject(self: XmlObjectSerializer, reader: XmlDictionaryReader, verifyObjectName: bool) -> object
        """
        ...

    def WriteEndObject(self, writer:XmlDictionaryWriter): # -> 
        """ WriteEndObject(self: XmlObjectSerializer, writer: XmlDictionaryWriter)WriteEndObject(self: XmlObjectSerializer, writer: XmlWriter) """
        ...

    def WriteObject(self, *__args): # -> 
        """ WriteObject(self: XmlObjectSerializer, writer: XmlDictionaryWriter, graph: object)WriteObject(self: XmlObjectSerializer, stream: Stream, graph: object)WriteObject(self: XmlObjectSerializer, writer: XmlWriter, graph: object) """
        ...

    def WriteObjectContent(self, writer:XmlDictionaryWriter, graph:object): # -> 
        """ WriteObjectContent(self: XmlObjectSerializer, writer: XmlDictionaryWriter, graph: object)WriteObjectContent(self: XmlObjectSerializer, writer: XmlWriter, graph: object) """
        ...

    def WriteStartObject(self, writer:XmlDictionaryWriter, graph:object): # -> 
        """ WriteStartObject(self: XmlObjectSerializer, writer: XmlDictionaryWriter, graph: object)WriteStartObject(self: XmlObjectSerializer, writer: XmlWriter, graph: object) """
        ...


class DataContractSerializer(XmlObjectSerializer): # skipped bases: <type 'object'>
    """
    DataContractSerializer(type: Type)
    DataContractSerializer(type: Type, knownTypes: IEnumerable[Type])
    DataContractSerializer(type: Type, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate)
    DataContractSerializer(type: Type, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate, dataContractResolver: DataContractResolver)
    DataContractSerializer(type: Type, rootName: str, rootNamespace: str)
    DataContractSerializer(type: Type, rootName: str, rootNamespace: str, knownTypes: IEnumerable[Type])
    DataContractSerializer(type: Type, rootName: str, rootNamespace: str, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate)
    DataContractSerializer(type: Type, rootName: str, rootNamespace: str, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate, dataContractResolver: DataContractResolver)
    DataContractSerializer(type: Type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString)
    DataContractSerializer(type: Type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString, knownTypes: IEnumerable[Type])
    DataContractSerializer(type: Type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate)
    DataContractSerializer(type: Type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate, dataContractResolver: DataContractResolver)
    DataContractSerializer(type: Type, settings: DataContractSerializerSettings)
    """
    @property
    def DataContractResolver(self) -> DataContractResolver:
        """ Get: DataContractResolver(self: DataContractSerializer) -> DataContractResolver """
        ...

    @property
    def DataContractSurrogate(self): # -> IDataContractSurrogate
        """ Get: DataContractSurrogate(self: DataContractSerializer) -> IDataContractSurrogate """
        ...

    @property
    def IgnoreExtensionDataObject(self) -> bool:
        """ Get: IgnoreExtensionDataObject(self: DataContractSerializer) -> bool """
        ...

    @property
    def KnownTypes(self) -> ReadOnlyCollection:
        """ Get: KnownTypes(self: DataContractSerializer) -> ReadOnlyCollection[Type] """
        ...

    @property
    def MaxItemsInObjectGraph(self) -> int:
        """ Get: MaxItemsInObjectGraph(self: DataContractSerializer) -> int """
        ...

    @property
    def PreserveObjectReferences(self) -> bool:
        """ Get: PreserveObjectReferences(self: DataContractSerializer) -> bool """
        ...

    @property
    def SerializeReadOnlyTypes(self) -> bool:
        """ Get: SerializeReadOnlyTypes(self: DataContractSerializer) -> bool """
        ...


    def __new__(cls, type:Type, *__args:IEnumerable) -> Self:
        """
        __new__(cls: type, type: Type)
        __new__(cls: type, type: Type, knownTypes: IEnumerable[Type])
        __new__(cls: type, type: Type, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate)
        __new__(cls: type, type: Type, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate, dataContractResolver: DataContractResolver)
        __new__(cls: type, type: Type, rootName: str, rootNamespace: str)
        __new__(cls: type, type: Type, rootName: str, rootNamespace: str, knownTypes: IEnumerable[Type])
        __new__(cls: type, type: Type, rootName: str, rootNamespace: str, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate)
        __new__(cls: type, type: Type, rootName: str, rootNamespace: str, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate, dataContractResolver: DataContractResolver)
        __new__(cls: type, type: Type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString)
        __new__(cls: type, type: Type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString, knownTypes: IEnumerable[Type])
        __new__(cls: type, type: Type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate)
        __new__(cls: type, type: Type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString, knownTypes: IEnumerable[Type], maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, preserveObjectReferences: bool, dataContractSurrogate: IDataContractSurrogate, dataContractResolver: DataContractResolver)
        __new__(cls: type, type: Type, settings: DataContractSerializerSettings)
        """
        ...


class DataContractSerializerExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetSerializationSurrogateProvider(serializer:DataContractSerializer): # -> ISerializationSurrogateProvider
        """ GetSerializationSurrogateProvider(serializer: DataContractSerializer) -> ISerializationSurrogateProvider """
        ...

    @staticmethod
    def SetSerializationSurrogateProvider(serializer:DataContractSerializer, provider): # ->  # Not found arg types: {'provider': 'ISerializationSurrogateProvider'}
        """ SetSerializationSurrogateProvider(serializer: DataContractSerializer, provider: ISerializationSurrogateProvider) """
        ...

    __all__: list = ...


class DataContractSerializerSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ DataContractSerializerSettings() """
    @property
    def DataContractResolver(self) -> DataContractResolver:
        """
        Get: DataContractResolver(self: DataContractSerializerSettings) -> DataContractResolver
        Set: DataContractResolver(self: DataContractSerializerSettings) = value
        """
        ...

    @property
    def DataContractSurrogate(self): # -> IDataContractSurrogate
        """
        Get: DataContractSurrogate(self: DataContractSerializerSettings) -> IDataContractSurrogate
        Set: DataContractSurrogate(self: DataContractSerializerSettings) = value
        """
        ...

    @property
    def IgnoreExtensionDataObject(self) -> bool:
        """
        Get: IgnoreExtensionDataObject(self: DataContractSerializerSettings) -> bool
        Set: IgnoreExtensionDataObject(self: DataContractSerializerSettings) = value
        """
        ...

    @property
    def KnownTypes(self) -> IEnumerable:
        """
        Get: KnownTypes(self: DataContractSerializerSettings) -> IEnumerable[Type]
        Set: KnownTypes(self: DataContractSerializerSettings) = value
        """
        ...

    @property
    def MaxItemsInObjectGraph(self) -> int:
        """
        Get: MaxItemsInObjectGraph(self: DataContractSerializerSettings) -> int
        Set: MaxItemsInObjectGraph(self: DataContractSerializerSettings) = value
        """
        ...

    @property
    def PreserveObjectReferences(self) -> bool:
        """
        Get: PreserveObjectReferences(self: DataContractSerializerSettings) -> bool
        Set: PreserveObjectReferences(self: DataContractSerializerSettings) = value
        """
        ...

    @property
    def RootName(self) -> XmlDictionaryString:
        """
        Get: RootName(self: DataContractSerializerSettings) -> XmlDictionaryString
        Set: RootName(self: DataContractSerializerSettings) = value
        """
        ...

    @property
    def RootNamespace(self) -> XmlDictionaryString:
        """
        Get: RootNamespace(self: DataContractSerializerSettings) -> XmlDictionaryString
        Set: RootNamespace(self: DataContractSerializerSettings) = value
        """
        ...

    @property
    def SerializeReadOnlyTypes(self) -> bool:
        """
        Get: SerializeReadOnlyTypes(self: DataContractSerializerSettings) -> bool
        Set: SerializeReadOnlyTypes(self: DataContractSerializerSettings) = value
        """
        ...



class DataMemberAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DataMemberAttribute() """
    @property
    def EmitDefaultValue(self) -> bool:
        """
        Get: EmitDefaultValue(self: DataMemberAttribute) -> bool
        Set: EmitDefaultValue(self: DataMemberAttribute) = value
        """
        ...

    @property
    def IsNameSetExplicitly(self) -> bool:
        """ Get: IsNameSetExplicitly(self: DataMemberAttribute) -> bool """
        ...

    @property
    def IsRequired(self) -> bool:
        """
        Get: IsRequired(self: DataMemberAttribute) -> bool
        Set: IsRequired(self: DataMemberAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: DataMemberAttribute) -> str
        Set: Name(self: DataMemberAttribute) = value
        """
        ...

    @property
    def Order(self) -> int:
        """
        Get: Order(self: DataMemberAttribute) -> int
        Set: Order(self: DataMemberAttribute) = value
        """
        ...



class DateTimeFormat: # skipped bases: <type 'object'>, <type 'object'>
    """
    DateTimeFormat(formatString: str)
    DateTimeFormat(formatString: str, formatProvider: IFormatProvider)
    """
    @property
    def DateTimeStyles(self) -> DateTimeStyles:
        """
        Get: DateTimeStyles(self: DateTimeFormat) -> DateTimeStyles
        Set: DateTimeStyles(self: DateTimeFormat) = value
        """
        ...

    @property
    def FormatProvider(self) -> IFormatProvider:
        """ Get: FormatProvider(self: DateTimeFormat) -> IFormatProvider """
        ...

    @property
    def FormatString(self) -> str:
        """ Get: FormatString(self: DateTimeFormat) -> str """
        ...



class EmitTypeInformation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EmitTypeInformation, values: Always (1), AsNeeded (0), Never (2) """
    Always: EmitTypeInformation = ...
    AsNeeded: EmitTypeInformation = ...
    Never: EmitTypeInformation = ...
    value__ = ...


class EnumMemberAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EnumMemberAttribute() """
    @property
    def IsValueSetExplicitly(self) -> bool:
        """ Get: IsValueSetExplicitly(self: EnumMemberAttribute) -> bool """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: EnumMemberAttribute) -> str
        Set: Value(self: EnumMemberAttribute) = value
        """
        ...



class ExportOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ ExportOptions() """
    @property
    def DataContractSurrogate(self): # -> IDataContractSurrogate
        """
        Get: DataContractSurrogate(self: ExportOptions) -> IDataContractSurrogate
        Set: DataContractSurrogate(self: ExportOptions) = value
        """
        ...

    @property
    def KnownTypes(self) -> Collection:
        """ Get: KnownTypes(self: ExportOptions) -> Collection[Type] """
        ...



class ExtensionDataObject: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class Formatter(IFormatter): # skipped bases: <type 'object'>
    """ no doc """
    def GetNext(self, *args): #cannot find CLR method
        """ GetNext(self: Formatter) -> (object, Int64) """
        ...

    def Schedule(self, *args): #cannot find CLR method
        """ Schedule(self: Formatter, obj: object) -> Int64 """
        ...

    def WriteArray(self, *args): #cannot find CLR method
        """ WriteArray(self: Formatter, obj: object, name: str, memberType: Type) """
        ...

    def WriteBoolean(self, *args): #cannot find CLR method
        """ WriteBoolean(self: Formatter, val: bool, name: str) """
        ...

    def WriteByte(self, *args): #cannot find CLR method
        """ WriteByte(self: Formatter, val: Byte, name: str) """
        ...

    def WriteChar(self, *args): #cannot find CLR method
        """ WriteChar(self: Formatter, val: Char, name: str) """
        ...

    def WriteDateTime(self, *args): #cannot find CLR method
        """ WriteDateTime(self: Formatter, val: DateTime, name: str) """
        ...

    def WriteDecimal(self, *args): #cannot find CLR method
        """ WriteDecimal(self: Formatter, val: Decimal, name: str) """
        ...

    def WriteDouble(self, *args): #cannot find CLR method
        """ WriteDouble(self: Formatter, val: float, name: str) """
        ...

    def WriteInt16(self, *args): #cannot find CLR method
        """ WriteInt16(self: Formatter, val: Int16, name: str) """
        ...

    def WriteInt32(self, *args): #cannot find CLR method
        """ WriteInt32(self: Formatter, val: int, name: str) """
        ...

    def WriteInt64(self, *args): #cannot find CLR method
        """ WriteInt64(self: Formatter, val: Int64, name: str) """
        ...

    def WriteMember(self, *args): #cannot find CLR method
        """ WriteMember(self: Formatter, memberName: str, data: object) """
        ...

    def WriteObjectRef(self, *args): #cannot find CLR method
        """ WriteObjectRef(self: Formatter, obj: object, name: str, memberType: Type) """
        ...

    def WriteSByte(self, *args): #cannot find CLR method
        """ WriteSByte(self: Formatter, val: SByte, name: str) """
        ...

    def WriteSingle(self, *args): #cannot find CLR method
        """ WriteSingle(self: Formatter, val: Single, name: str) """
        ...

    def WriteTimeSpan(self, *args): #cannot find CLR method
        """ WriteTimeSpan(self: Formatter, val: TimeSpan, name: str) """
        ...

    def WriteUInt16(self, *args): #cannot find CLR method
        """ WriteUInt16(self: Formatter, val: UInt16, name: str) """
        ...

    def WriteUInt32(self, *args): #cannot find CLR method
        """ WriteUInt32(self: Formatter, val: UInt32, name: str) """
        ...

    def WriteUInt64(self, *args): #cannot find CLR method
        """ WriteUInt64(self: Formatter, val: UInt64, name: str) """
        ...

    def WriteValueType(self, *args): #cannot find CLR method
        """ WriteValueType(self: Formatter, obj: object, name: str, memberType: Type) """
        ...

    m_idGenerator = ...
    m_objectQueue = ...


class FormatterConverter(IFormatterConverter): # skipped bases: <type 'object'>
    """ FormatterConverter() """
    pass

class FormatterServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CheckTypeSecurity(t:Type, securityLevel:TypeFilterLevel): # -> 
        """ CheckTypeSecurity(t: Type, securityLevel: TypeFilterLevel) """
        ...

    @staticmethod
    def GetObjectData(obj:object, members:Array) -> Array:
        """ GetObjectData(obj: object, members: Array[MemberInfo]) -> Array[object] """
        ...

    @staticmethod
    def GetSafeUninitializedObject(type:Type) -> object:
        """ GetSafeUninitializedObject(type: Type) -> object """
        ...

    @staticmethod
    def GetSerializableMembers(type:Type, context:StreamingContext = ...) -> Array:
        """
        GetSerializableMembers(type: Type, context: StreamingContext) -> Array[MemberInfo]
        GetSerializableMembers(type: Type) -> Array[MemberInfo]
        """
        ...

    @staticmethod
    def GetSurrogateForCyclicalReference(innerSurrogate:ISerializationSurrogate) -> ISerializationSurrogate:
        """ GetSurrogateForCyclicalReference(innerSurrogate: ISerializationSurrogate) -> ISerializationSurrogate """
        ...

    @staticmethod
    def GetTypeFromAssembly(assem:Assembly, name:str) -> Type:
        """ GetTypeFromAssembly(assem: Assembly, name: str) -> Type """
        ...

    @staticmethod
    def GetUninitializedObject(type:Type) -> object:
        """ GetUninitializedObject(type: Type) -> object """
        ...

    @staticmethod
    def PopulateObjectMembers(obj:object, members:Array, data:Array) -> object:
        """ PopulateObjectMembers(obj: object, members: Array[MemberInfo], data: Array[object]) -> object """
        ...

    __all__: list = ...


class IDataContractSurrogate: # skipped bases: <type 'object'>
    """ no doc """
    def GetCustomDataToExport(self, *__args) -> object:
        """
        GetCustomDataToExport(self: IDataContractSurrogate, memberInfo: MemberInfo, dataContractType: Type) -> object
        GetCustomDataToExport(self: IDataContractSurrogate, clrType: Type, dataContractType: Type) -> object
        """
        ...

    def GetDataContractType(self, type:Type) -> Type:
        """ GetDataContractType(self: IDataContractSurrogate, type: Type) -> Type """
        ...

    def GetDeserializedObject(self, obj:object, targetType:Type) -> object:
        """ GetDeserializedObject(self: IDataContractSurrogate, obj: object, targetType: Type) -> object """
        ...

    def GetKnownCustomDataTypes(self, customDataTypes:Collection): # -> 
        """ GetKnownCustomDataTypes(self: IDataContractSurrogate, customDataTypes: Collection[Type]) """
        ...

    def GetObjectToSerialize(self, obj:object, targetType:Type) -> object:
        """ GetObjectToSerialize(self: IDataContractSurrogate, obj: object, targetType: Type) -> object """
        ...

    def GetReferencedTypeOnImport(self, typeName:str, typeNamespace:str, customData:object) -> Type:
        """ GetReferencedTypeOnImport(self: IDataContractSurrogate, typeName: str, typeNamespace: str, customData: object) -> Type """
        ...

    def ProcessImportedType(self, typeDeclaration:CodeTypeDeclaration, compileUnit:CodeCompileUnit) -> CodeTypeDeclaration:
        """ ProcessImportedType(self: IDataContractSurrogate, typeDeclaration: CodeTypeDeclaration, compileUnit: CodeCompileUnit) -> CodeTypeDeclaration """
        ...


class IDeserializationCallback: # skipped bases: <type 'object'>
    """ no doc """
    def OnDeserialization(self, sender:object): # -> 
        """ OnDeserialization(self: IDeserializationCallback, sender: object) """
        ...


class IExtensibleDataObject: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ExtensionData(self) -> ExtensionDataObject:
        """
        Get: ExtensionData(self: IExtensibleDataObject) -> ExtensionDataObject
        Set: ExtensionData(self: IExtensibleDataObject) = value
        """
        ...



class IFormatter: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Binder(self) -> SerializationBinder:
        """
        Get: Binder(self: IFormatter) -> SerializationBinder
        Set: Binder(self: IFormatter) = value
        """
        ...

    @property
    def Context(self) -> StreamingContext:
        """
        Get: Context(self: IFormatter) -> StreamingContext
        Set: Context(self: IFormatter) = value
        """
        ...

    @property
    def SurrogateSelector(self) -> ISurrogateSelector:
        """
        Get: SurrogateSelector(self: IFormatter) -> ISurrogateSelector
        Set: SurrogateSelector(self: IFormatter) = value
        """
        ...


    def Deserialize(self, serializationStream:Stream) -> object:
        """ Deserialize(self: IFormatter, serializationStream: Stream) -> object """
        ...

    def Serialize(self, serializationStream:Stream, graph:object): # -> 
        """ Serialize(self: IFormatter, serializationStream: Stream, graph: object) """
        ...


class IFormatterConverter: # skipped bases: <type 'object'>
    """ no doc """
    def Convert(self, value:object, *__args:Type) -> object:
        """
        Convert(self: IFormatterConverter, value: object, type: Type) -> object
        Convert(self: IFormatterConverter, value: object, typeCode: TypeCode) -> object
        """
        ...

    def ToBoolean(self, value:object) -> bool:
        """ ToBoolean(self: IFormatterConverter, value: object) -> bool """
        ...

    def ToByte(self, value:object) -> Byte:
        """ ToByte(self: IFormatterConverter, value: object) -> Byte """
        ...

    def ToChar(self, value:object) -> Char:
        """ ToChar(self: IFormatterConverter, value: object) -> Char """
        ...

    def ToDateTime(self, value:object) -> DateTime:
        """ ToDateTime(self: IFormatterConverter, value: object) -> DateTime """
        ...

    def ToDecimal(self, value:object) -> Decimal:
        """ ToDecimal(self: IFormatterConverter, value: object) -> Decimal """
        ...

    def ToDouble(self, value:object) -> float:
        """ ToDouble(self: IFormatterConverter, value: object) -> float """
        ...

    def ToInt16(self, value:object) -> Int16:
        """ ToInt16(self: IFormatterConverter, value: object) -> Int16 """
        ...

    def ToInt32(self, value:object) -> int:
        """ ToInt32(self: IFormatterConverter, value: object) -> int """
        ...

    def ToInt64(self, value:object) -> Int64:
        """ ToInt64(self: IFormatterConverter, value: object) -> Int64 """
        ...

    def ToSByte(self, value:object) -> SByte:
        """ ToSByte(self: IFormatterConverter, value: object) -> SByte """
        ...

    def ToSingle(self, value:object) -> Single:
        """ ToSingle(self: IFormatterConverter, value: object) -> Single """
        ...

    def ToString(self, value:object) -> str:
        """ ToString(self: IFormatterConverter, value: object) -> str """
        ...

    def ToUInt16(self, value:object) -> UInt16:
        """ ToUInt16(self: IFormatterConverter, value: object) -> UInt16 """
        ...

    def ToUInt32(self, value:object) -> UInt32:
        """ ToUInt32(self: IFormatterConverter, value: object) -> UInt32 """
        ...

    def ToUInt64(self, value:object) -> UInt64:
        """ ToUInt64(self: IFormatterConverter, value: object) -> UInt64 """
        ...


class IgnoreDataMemberAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ IgnoreDataMemberAttribute() """
    pass

class ImportOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ ImportOptions() """
    @property
    def CodeProvider(self) -> CodeDomProvider:
        """
        Get: CodeProvider(self: ImportOptions) -> CodeDomProvider
        Set: CodeProvider(self: ImportOptions) = value
        """
        ...

    @property
    def DataContractSurrogate(self) -> IDataContractSurrogate:
        """
        Get: DataContractSurrogate(self: ImportOptions) -> IDataContractSurrogate
        Set: DataContractSurrogate(self: ImportOptions) = value
        """
        ...

    @property
    def EnableDataBinding(self) -> bool:
        """
        Get: EnableDataBinding(self: ImportOptions) -> bool
        Set: EnableDataBinding(self: ImportOptions) = value
        """
        ...

    @property
    def GenerateInternal(self) -> bool:
        """
        Get: GenerateInternal(self: ImportOptions) -> bool
        Set: GenerateInternal(self: ImportOptions) = value
        """
        ...

    @property
    def GenerateSerializable(self) -> bool:
        """
        Get: GenerateSerializable(self: ImportOptions) -> bool
        Set: GenerateSerializable(self: ImportOptions) = value
        """
        ...

    @property
    def ImportXmlType(self) -> bool:
        """
        Get: ImportXmlType(self: ImportOptions) -> bool
        Set: ImportXmlType(self: ImportOptions) = value
        """
        ...

    @property
    def Namespaces(self) -> IDictionary:
        """ Get: Namespaces(self: ImportOptions) -> IDictionary[str, str] """
        ...

    @property
    def ReferencedCollectionTypes(self) -> ICollection:
        """ Get: ReferencedCollectionTypes(self: ImportOptions) -> ICollection[Type] """
        ...

    @property
    def ReferencedTypes(self) -> ICollection:
        """ Get: ReferencedTypes(self: ImportOptions) -> ICollection[Type] """
        ...



class InvalidDataContractException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidDataContractException()
    InvalidDataContractException(message: str)
    InvalidDataContractException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class IObjectReference: # skipped bases: <type 'object'>
    """ no doc """
    def GetRealObject(self, context:StreamingContext) -> object:
        """ GetRealObject(self: IObjectReference, context: StreamingContext) -> object """
        ...


class ISafeSerializationData: # skipped bases: <type 'object'>
    """ no doc """
    def CompleteDeserialization(self, deserialized:object): # -> 
        """ CompleteDeserialization(self: ISafeSerializationData, deserialized: object) """
        ...


class ISerializable: # skipped bases: <type 'object'>
    """ no doc """
    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: ISerializable, info: SerializationInfo, context: StreamingContext) """
        ...


class ISerializationSurrogate: # skipped bases: <type 'object'>
    """ no doc """
    def GetObjectData(self, obj:object, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: ISerializationSurrogate, obj: object, info: SerializationInfo, context: StreamingContext) """
        ...

    def SetObjectData(self, obj:object, info:SerializationInfo, context:StreamingContext, selector:ISurrogateSelector) -> object:
        """ SetObjectData(self: ISerializationSurrogate, obj: object, info: SerializationInfo, context: StreamingContext, selector: ISurrogateSelector) -> object """
        ...


class ISerializationSurrogateProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetDeserializedObject(self, obj:object, targetType:Type) -> object:
        """ GetDeserializedObject(self: ISerializationSurrogateProvider, obj: object, targetType: Type) -> object """
        ...

    def GetObjectToSerialize(self, obj:object, targetType:Type) -> object:
        """ GetObjectToSerialize(self: ISerializationSurrogateProvider, obj: object, targetType: Type) -> object """
        ...

    def GetSurrogateType(self, type:Type) -> Type:
        """ GetSurrogateType(self: ISerializationSurrogateProvider, type: Type) -> Type """
        ...


class ISurrogateSelector: # skipped bases: <type 'object'>
    """ no doc """
    def ChainSelector(self, selector:ISurrogateSelector): # -> 
        """ ChainSelector(self: ISurrogateSelector, selector: ISurrogateSelector) """
        ...

    def GetNextSelector(self) -> ISurrogateSelector:
        """ GetNextSelector(self: ISurrogateSelector) -> ISurrogateSelector """
        ...

    def GetSurrogate(self, type, context, selector) -> Tuple_[ISerializationSurrogate, ISurrogateSelector]:
        """ GetSurrogate(self: ISurrogateSelector, type: Type, context: StreamingContext) -> (ISerializationSurrogate, ISurrogateSelector) """
        ...


class KnownTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    KnownTypeAttribute(type: Type)
    KnownTypeAttribute(methodName: str)
    """
    @property
    def MethodName(self) -> str:
        """ Get: MethodName(self: KnownTypeAttribute) -> str """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: KnownTypeAttribute) -> Type """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type, type: Type)
        __new__(cls: type, methodName: str)
        """
        ...


class NetDataContractSerializer(XmlObjectSerializer, IFormatter): # skipped bases: <type 'object'>
    """
    NetDataContractSerializer()
    NetDataContractSerializer(context: StreamingContext)
    NetDataContractSerializer(context: StreamingContext, maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, assemblyFormat: FormatterAssemblyStyle, surrogateSelector: ISurrogateSelector)
    NetDataContractSerializer(rootName: str, rootNamespace: str)
    NetDataContractSerializer(rootName: str, rootNamespace: str, context: StreamingContext, maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, assemblyFormat: FormatterAssemblyStyle, surrogateSelector: ISurrogateSelector)
    NetDataContractSerializer(rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString)
    NetDataContractSerializer(rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString, context: StreamingContext, maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, assemblyFormat: FormatterAssemblyStyle, surrogateSelector: ISurrogateSelector)
    """
    @property
    def AssemblyFormat(self) -> FormatterAssemblyStyle:
        """
        Get: AssemblyFormat(self: NetDataContractSerializer) -> FormatterAssemblyStyle
        Set: AssemblyFormat(self: NetDataContractSerializer) = value
        """
        ...

    @property
    def IgnoreExtensionDataObject(self) -> bool:
        """ Get: IgnoreExtensionDataObject(self: NetDataContractSerializer) -> bool """
        ...

    @property
    def MaxItemsInObjectGraph(self) -> int:
        """ Get: MaxItemsInObjectGraph(self: NetDataContractSerializer) -> int """
        ...


    def __new__(cls, *__args:StreamingContext) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, context: StreamingContext)
        __new__(cls: type, context: StreamingContext, maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, assemblyFormat: FormatterAssemblyStyle, surrogateSelector: ISurrogateSelector)
        __new__(cls: type, rootName: str, rootNamespace: str)
        __new__(cls: type, rootName: str, rootNamespace: str, context: StreamingContext, maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, assemblyFormat: FormatterAssemblyStyle, surrogateSelector: ISurrogateSelector)
        __new__(cls: type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString)
        __new__(cls: type, rootName: XmlDictionaryString, rootNamespace: XmlDictionaryString, context: StreamingContext, maxItemsInObjectGraph: int, ignoreExtensionDataObject: bool, assemblyFormat: FormatterAssemblyStyle, surrogateSelector: ISurrogateSelector)
        """
        ...


class ObjectIDGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """ ObjectIDGenerator() """
    def GetId(self, obj, firstTime) -> Tuple_[Int64, bool]:
        """ GetId(self: ObjectIDGenerator, obj: object) -> (Int64, bool) """
        ...

    def HasId(self, obj, firstTime) -> Tuple_[Int64, bool]:
        """ HasId(self: ObjectIDGenerator, obj: object) -> (Int64, bool) """
        ...


class ObjectManager: # skipped bases: <type 'object'>, <type 'object'>
    """ ObjectManager(selector: ISurrogateSelector, context: StreamingContext) """
    def DoFixups(self): # -> 
        """ DoFixups(self: ObjectManager) """
        ...

    def GetObject(self, objectID:Int64) -> object:
        """ GetObject(self: ObjectManager, objectID: Int64) -> object """
        ...

    def RaiseDeserializationEvent(self): # -> 
        """ RaiseDeserializationEvent(self: ObjectManager) """
        ...

    def RaiseOnDeserializingEvent(self, obj:object): # -> 
        """ RaiseOnDeserializingEvent(self: ObjectManager, obj: object) """
        ...

    def RecordArrayElementFixup(self, arrayToBeFixed, *__args): # -> 
        """ RecordArrayElementFixup(self: ObjectManager, arrayToBeFixed: Int64, indices: Array[int], objectRequired: Int64)RecordArrayElementFixup(self: ObjectManager, arrayToBeFixed: Int64, index: int, objectRequired: Int64) """
        ...

    def RecordDelayedFixup(self, objectToBeFixed:Int64, memberName:str, objectRequired:Int64): # -> 
        """ RecordDelayedFixup(self: ObjectManager, objectToBeFixed: Int64, memberName: str, objectRequired: Int64) """
        ...

    def RecordFixup(self, objectToBeFixed:Int64, member:MemberInfo, objectRequired:Int64): # -> 
        """ RecordFixup(self: ObjectManager, objectToBeFixed: Int64, member: MemberInfo, objectRequired: Int64) """
        ...

    def RegisterObject(self, obj:object, objectID:Int64, info:SerializationInfo = ..., idOfContainingObj:Int64 = ..., member:MemberInfo = ..., arrayIndex:Array = ...): # -> 
        """ RegisterObject(self: ObjectManager, obj: object, objectID: Int64)RegisterObject(self: ObjectManager, obj: object, objectID: Int64, info: SerializationInfo)RegisterObject(self: ObjectManager, obj: object, objectID: Int64, info: SerializationInfo, idOfContainingObj: Int64, member: MemberInfo)RegisterObject(self: ObjectManager, obj: object, objectID: Int64, info: SerializationInfo, idOfContainingObj: Int64, member: MemberInfo, arrayIndex: Array[int]) """
        ...


class OnDeserializedAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ OnDeserializedAttribute() """
    pass

class OnDeserializingAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ OnDeserializingAttribute() """
    pass

class OnSerializedAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ OnSerializedAttribute() """
    pass

class OnSerializingAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ OnSerializingAttribute() """
    pass

class OptionalFieldAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ OptionalFieldAttribute() """
    @property
    def VersionAdded(self) -> int:
        """
        Get: VersionAdded(self: OptionalFieldAttribute) -> int
        Set: VersionAdded(self: OptionalFieldAttribute) = value
        """
        ...



class SafeSerializationEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def StreamingContext(self) -> StreamingContext:
        """ Get: StreamingContext(self: SafeSerializationEventArgs) -> StreamingContext """
        ...


    def AddSerializedState(self, serializedState:ISafeSerializationData): # -> 
        """ AddSerializedState(self: SafeSerializationEventArgs, serializedState: ISafeSerializationData) """
        ...


class SerializationBinder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def BindToName(self, serializedType, assemblyName, typeName) -> Tuple_[str, str]:
        """ BindToName(self: SerializationBinder, serializedType: Type) -> (str, str) """
        ...

    def BindToType(self, assemblyName:str, typeName:str) -> Type:
        """ BindToType(self: SerializationBinder, assemblyName: str, typeName: str) -> Type """
        ...


class SerializationEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: SerializationEntry) -> str """
        ...

    @property
    def ObjectType(self) -> Type:
        """ Get: ObjectType(self: SerializationEntry) -> Type """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: SerializationEntry) -> object """
        ...



class SerializationException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SerializationException()
    SerializationException(message: str)
    SerializationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SerializationInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    SerializationInfo(type: Type, converter: IFormatterConverter)
    SerializationInfo(type: Type, converter: IFormatterConverter, requireSameTokenInPartialTrust: bool)
    """
    @property
    def AssemblyName(self) -> str:
        """
        Get: AssemblyName(self: SerializationInfo) -> str
        Set: AssemblyName(self: SerializationInfo) = value
        """
        ...

    @property
    def FullTypeName(self) -> str:
        """
        Get: FullTypeName(self: SerializationInfo) -> str
        Set: FullTypeName(self: SerializationInfo) = value
        """
        ...

    @property
    def IsAssemblyNameSetExplicit(self) -> bool:
        """ Get: IsAssemblyNameSetExplicit(self: SerializationInfo) -> bool """
        ...

    @property
    def IsFullTypeNameSetExplicit(self) -> bool:
        """ Get: IsFullTypeNameSetExplicit(self: SerializationInfo) -> bool """
        ...

    @property
    def MemberCount(self) -> int:
        """ Get: MemberCount(self: SerializationInfo) -> int """
        ...

    @property
    def ObjectType(self) -> Type:
        """ Get: ObjectType(self: SerializationInfo) -> Type """
        ...


    def AddValue(self, name:str, value:object, type:Type = ...): # -> 
        """ AddValue(self: SerializationInfo, name: str, value: object, type: Type)AddValue(self: SerializationInfo, name: str, value: object)AddValue(self: SerializationInfo, name: str, value: bool)AddValue(self: SerializationInfo, name: str, value: Char)AddValue(self: SerializationInfo, name: str, value: SByte)AddValue(self: SerializationInfo, name: str, value: Byte)AddValue(self: SerializationInfo, name: str, value: Int16)AddValue(self: SerializationInfo, name: str, value: UInt16)AddValue(self: SerializationInfo, name: str, value: int)AddValue(self: SerializationInfo, name: str, value: UInt32)AddValue(self: SerializationInfo, name: str, value: Int64)AddValue(self: SerializationInfo, name: str, value: UInt64)AddValue(self: SerializationInfo, name: str, value: Single)AddValue(self: SerializationInfo, name: str, value: float)AddValue(self: SerializationInfo, name: str, value: Decimal)AddValue(self: SerializationInfo, name: str, value: DateTime) """
        ...

    def GetBoolean(self, name:str) -> bool:
        """ GetBoolean(self: SerializationInfo, name: str) -> bool """
        ...

    def GetByte(self, name:str) -> Byte:
        """ GetByte(self: SerializationInfo, name: str) -> Byte """
        ...

    def GetChar(self, name:str) -> Char:
        """ GetChar(self: SerializationInfo, name: str) -> Char """
        ...

    def GetDateTime(self, name:str) -> DateTime:
        """ GetDateTime(self: SerializationInfo, name: str) -> DateTime """
        ...

    def GetDecimal(self, name:str) -> Decimal:
        """ GetDecimal(self: SerializationInfo, name: str) -> Decimal """
        ...

    def GetDouble(self, name:str) -> float:
        """ GetDouble(self: SerializationInfo, name: str) -> float """
        ...

    def GetEnumerator(self) -> SerializationInfoEnumerator:
        """ GetEnumerator(self: SerializationInfo) -> SerializationInfoEnumerator """
        ...

    def GetInt16(self, name:str) -> Int16:
        """ GetInt16(self: SerializationInfo, name: str) -> Int16 """
        ...

    def GetInt32(self, name:str) -> int:
        """ GetInt32(self: SerializationInfo, name: str) -> int """
        ...

    def GetInt64(self, name:str) -> Int64:
        """ GetInt64(self: SerializationInfo, name: str) -> Int64 """
        ...

    def GetSByte(self, name:str) -> SByte:
        """ GetSByte(self: SerializationInfo, name: str) -> SByte """
        ...

    def GetSingle(self, name:str) -> Single:
        """ GetSingle(self: SerializationInfo, name: str) -> Single """
        ...

    def GetString(self, name:str) -> str:
        """ GetString(self: SerializationInfo, name: str) -> str """
        ...

    def GetUInt16(self, name:str) -> UInt16:
        """ GetUInt16(self: SerializationInfo, name: str) -> UInt16 """
        ...

    def GetUInt32(self, name:str) -> UInt32:
        """ GetUInt32(self: SerializationInfo, name: str) -> UInt32 """
        ...

    def GetUInt64(self, name:str) -> UInt64:
        """ GetUInt64(self: SerializationInfo, name: str) -> UInt64 """
        ...

    def GetValue(self, name:str, type:Type) -> object:
        """ GetValue(self: SerializationInfo, name: str, type: Type) -> object """
        ...

    def SetType(self, type:Type): # -> 
        """ SetType(self: SerializationInfo, type: Type) """
        ...


class SerializationInfoEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: SerializationInfoEnumerator) -> str """
        ...

    @property
    def ObjectType(self) -> Type:
        """ Get: ObjectType(self: SerializationInfoEnumerator) -> Type """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: SerializationInfoEnumerator) -> object """
        ...



class SerializationObjectManager: # skipped bases: <type 'object'>, <type 'object'>
    """ SerializationObjectManager(context: StreamingContext) """
    def RaiseOnSerializedEvent(self): # -> 
        """ RaiseOnSerializedEvent(self: SerializationObjectManager) """
        ...

    def RegisterObject(self, obj:object): # -> 
        """ RegisterObject(self: SerializationObjectManager, obj: object) """
        ...


class StreamingContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    StreamingContext(state: StreamingContextStates)
    StreamingContext(state: StreamingContextStates, additional: object)
    """
    @property
    def Context(self) -> object:
        """ Get: Context(self: StreamingContext) -> object """
        ...

    @property
    def State(self) -> StreamingContextStates:
        """ Get: State(self: StreamingContext) -> StreamingContextStates """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: StreamingContext, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: StreamingContext) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class StreamingContextStates(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) StreamingContextStates, values: All (255), Clone (64), CrossAppDomain (128), CrossMachine (2), CrossProcess (1), File (4), Other (32), Persistence (8), Remoting (16) """
    All: StreamingContextStates = ...
    Clone: StreamingContextStates = ...
    CrossAppDomain: StreamingContextStates = ...
    CrossMachine: StreamingContextStates = ...
    CrossProcess: StreamingContextStates = ...
    File: StreamingContextStates = ...
    Other: StreamingContextStates = ...
    Persistence: StreamingContextStates = ...
    Remoting: StreamingContextStates = ...
    value__ = ...


class SurrogateSelector(ISurrogateSelector): # skipped bases: <type 'object'>
    """ SurrogateSelector() """
    def AddSurrogate(self, type:Type, context:StreamingContext, surrogate:ISerializationSurrogate): # -> 
        """ AddSurrogate(self: SurrogateSelector, type: Type, context: StreamingContext, surrogate: ISerializationSurrogate) """
        ...

    def RemoveSurrogate(self, type:Type, context:StreamingContext): # -> 
        """ RemoveSurrogate(self: SurrogateSelector, type: Type, context: StreamingContext) """
        ...


class XmlSerializableServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AddDefaultSchema(schemas:XmlSchemaSet, typeQName:XmlQualifiedName): # -> 
        """ AddDefaultSchema(schemas: XmlSchemaSet, typeQName: XmlQualifiedName) """
        ...

    @staticmethod
    def ReadNodes(xmlReader:XmlReader) -> Array:
        """ ReadNodes(xmlReader: XmlReader) -> Array[XmlNode] """
        ...

    @staticmethod
    def WriteNodes(xmlWriter:XmlWriter, nodes:Array): # -> 
        """ WriteNodes(xmlWriter: XmlWriter, nodes: Array[XmlNode]) """
        ...

    __all__: list = ...


class XPathQueryGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateFromDataContractSerializer(type:Type, pathToMember:Array, *__args:StringBuilder) -> Tuple_[str, XmlNamespaceManager]:
        """
        CreateFromDataContractSerializer(type: Type, pathToMember: Array[MemberInfo]) -> (str, XmlNamespaceManager)
        CreateFromDataContractSerializer(type: Type, pathToMember: Array[MemberInfo], rootElementXpath: StringBuilder) -> (str, XmlNamespaceManager)
        """
        ...

    __all__: list = ...


class XsdDataContractExporter: # skipped bases: <type 'object'>, <type 'object'>
    """
    XsdDataContractExporter()
    XsdDataContractExporter(schemas: XmlSchemaSet)
    """
    @property
    def Options(self) -> ExportOptions:
        """
        Get: Options(self: XsdDataContractExporter) -> ExportOptions
        Set: Options(self: XsdDataContractExporter) = value
        """
        ...

    @property
    def Schemas(self) -> XmlSchemaSet:
        """ Get: Schemas(self: XsdDataContractExporter) -> XmlSchemaSet """
        ...


    def CanExport(self, *__args:ICollection) -> bool:
        """
        CanExport(self: XsdDataContractExporter, assemblies: ICollection[Assembly]) -> bool
        CanExport(self: XsdDataContractExporter, types: ICollection[Type]) -> bool
        CanExport(self: XsdDataContractExporter, type: Type) -> bool
        """
        ...

    def Export(self, *__args:ICollection): # -> 
        """ Export(self: XsdDataContractExporter, assemblies: ICollection[Assembly])Export(self: XsdDataContractExporter, types: ICollection[Type])Export(self: XsdDataContractExporter, type: Type) """
        ...

    def GetRootElementName(self, type:Type) -> XmlQualifiedName:
        """ GetRootElementName(self: XsdDataContractExporter, type: Type) -> XmlQualifiedName """
        ...

    def GetSchemaType(self, type:Type) -> XmlSchemaType:
        """ GetSchemaType(self: XsdDataContractExporter, type: Type) -> XmlSchemaType """
        ...

    def GetSchemaTypeName(self, type:Type) -> XmlQualifiedName:
        """ GetSchemaTypeName(self: XsdDataContractExporter, type: Type) -> XmlQualifiedName """
        ...


class XsdDataContractImporter: # skipped bases: <type 'object'>, <type 'object'>
    """
    XsdDataContractImporter()
    XsdDataContractImporter(codeCompileUnit: CodeCompileUnit)
    """
    @property
    def CodeCompileUnit(self) -> CodeCompileUnit:
        """ Get: CodeCompileUnit(self: XsdDataContractImporter) -> CodeCompileUnit """
        ...

    @property
    def Options(self) -> ImportOptions:
        """
        Get: Options(self: XsdDataContractImporter) -> ImportOptions
        Set: Options(self: XsdDataContractImporter) = value
        """
        ...


    def CanImport(self, schemas:XmlSchemaSet, *__args:ICollection) -> bool:
        """
        CanImport(self: XsdDataContractImporter, schemas: XmlSchemaSet) -> bool
        CanImport(self: XsdDataContractImporter, schemas: XmlSchemaSet, typeNames: ICollection[XmlQualifiedName]) -> bool
        CanImport(self: XsdDataContractImporter, schemas: XmlSchemaSet, typeName: XmlQualifiedName) -> bool
        CanImport(self: XsdDataContractImporter, schemas: XmlSchemaSet, element: XmlSchemaElement) -> bool
        """
        ...

    def GetCodeTypeReference(self, typeName:XmlQualifiedName, element:XmlSchemaElement = ...) -> CodeTypeReference:
        """
        GetCodeTypeReference(self: XsdDataContractImporter, typeName: XmlQualifiedName) -> CodeTypeReference
        GetCodeTypeReference(self: XsdDataContractImporter, typeName: XmlQualifiedName, element: XmlSchemaElement) -> CodeTypeReference
        """
        ...

    def GetKnownTypeReferences(self, typeName:XmlQualifiedName) -> ICollection:
        """ GetKnownTypeReferences(self: XsdDataContractImporter, typeName: XmlQualifiedName) -> ICollection[CodeTypeReference] """
        ...

    def Import(self, schemas:XmlSchemaSet, *__args:ICollection): # -> 
        """ Import(self: XsdDataContractImporter, schemas: XmlSchemaSet)Import(self: XsdDataContractImporter, schemas: XmlSchemaSet, typeNames: ICollection[XmlQualifiedName])Import(self: XsdDataContractImporter, schemas: XmlSchemaSet, typeName: XmlQualifiedName)Import(self: XsdDataContractImporter, schemas: XmlSchemaSet, element: XmlSchemaElement) -> XmlQualifiedName """
        ...


# variables with complex values

