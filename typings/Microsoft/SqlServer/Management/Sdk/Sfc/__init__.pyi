# encoding: utf-8
# module Microsoft.SqlServer.Management.Sdk.Sfc calls itself Sfc
# from Microsoft.SqlServer.Management.Sdk.Sfc, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Common import (DatabaseEngineEdition, 
    DatabaseEngineType, ExecutionTypes, IAlterable, ICreatable, IDroppable, 
    IMarkForDrop, ISfcConnection, ServerConnection, ServerType, ServerVersion, 
    SqlServerManagementException)

from Microsoft.SqlServer.Management.Sdk.Sfc.Metadata import (
    SfcMetadataDiscovery)

from Microsoft.VisualBasic.CompilerServices import ObjectType

from System import (Array, AsyncCallback, Attribute, Byte, Char, DateTime, 
    Decimal, Enum, EventArgs, Guid, IAsyncResult, IDisposable, IEquatable, 
    Int16, Int64, MarshalByRefObject, MulticastDelegate, Single, Type, UInt32)

from System.Collections import (ArrayList, ICollection, IComparer, 
    IEnumerable, IEnumerator, IList, SortedList)

from System.Collections.Generic import Dictionary, List

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Collections.Specialized import StringCollection

from System.ComponentModel import (AttributeCollection, EnumConverter, 
    IListSource, INotifyPropertyChanged, ITypeDescriptorContext, 
    MemberDescriptor, PropertyChangedEventArgs, PropertyDescriptor, 
    PropertyDescriptorCollection, StringConverter, TypeConverter)

from System.Data import DataSet, DataTable, IDataReader

from System.Data.SqlClient import SqlConnection, SqlDataReader

from System.Globalization import CompareOptions, CultureInfo

from System.Reflection import Assembly, PropertyInfo

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from System.Text import StringBuilder

from System.Xml import XmlDocument, XmlReader, XmlTextReader, XmlWriter

from System.Xml.Serialization import IXmlSerializable

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (AliasKind, BoundEvent, 
    DependencyListEnumerator, DependencyTreeEnumerator, Direction, 
    ExecutionMode, Flags, IDisplayKey, K, StandardValuesCollection, T, TRef, 
    field#)
"""

# no functions
# classes

class ConditionedSql: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AcceptsMultipleHits(self):
        ...

    @property
    def Fields(self):
        ...

    @property
    def IsUsed(self) -> bool:
        """ Get: IsUsed(self: ConditionedSql) -> bool """
        ...

    @property
    def LinkFields(self) -> ArrayList:
        """ Get: LinkFields(self: ConditionedSql) -> ArrayList """
        ...

    @property
    def LinkMultiple(self) -> LinkMultiple:
        """
        Get: LinkMultiple(self: ConditionedSql) -> LinkMultiple
        Set: LinkMultiple(self: ConditionedSql) = value
        """
        ...

    @property
    def Used(self) -> bool:
        """ Get: Used(self: ConditionedSql) -> bool """
        ...


    def AddHit(self, field:str, obj:SqlObjectBase, sb:StatementBuilder): # -> 
        """ AddHit(self: ConditionedSql, field: str, obj: SqlObjectBase, sb: StatementBuilder) """
        ...

    def AddLinkMultiple(self, xrmpl:XmlReadMultipleLink): # -> 
        """ AddLinkMultiple(self: ConditionedSql, xrmpl: XmlReadMultipleLink) """
        ...

    def ClearHit(self): # -> 
        """ ClearHit(self: ConditionedSql) """
        ...

    def IsDefault(self) -> bool:
        """ IsDefault(self: ConditionedSql) -> bool """
        ...

    def IsHit(self, field:str) -> bool:
        """ IsHit(self: ConditionedSql, field: str) -> bool """
        ...

    def MarkHit(self): # -> 
        """ MarkHit(self: ConditionedSql) """
        ...

    def SetFields(self, fields:StringCollection): # -> 
        """ SetFields(self: ConditionedSql, fields: StringCollection) """
        ...

    def TestHit(self, *args): #cannot find CLR method
        """ TestHit(self: ConditionedSql, field: str) -> bool """
        ...


class ConditionedSqlList: # skipped bases: <type 'object'>, <type 'object'>
    """ ConditionedSqlList() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ConditionedSqlList) -> int """
        ...


    def Add(self, obj:ConditionedSql): # -> 
        """ Add(self: ConditionedSqlList, obj: ConditionedSql) """
        ...

    def AddDefault(self, sb:StatementBuilder): # -> 
        """ AddDefault(self: ConditionedSqlList, sb: StatementBuilder) """
        ...

    def AddHits(self, obj:SqlObjectBase, field:str, sb:StatementBuilder) -> bool:
        """ AddHits(self: ConditionedSqlList, obj: SqlObjectBase, field: str, sb: StatementBuilder) -> bool """
        ...

    def ClearHits(self): # -> 
        """ ClearHits(self: ConditionedSqlList) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ConditionedSqlList) -> IEnumerator """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ConnectionHelpers: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ToScopedServerConnection(sqlConnection:SqlConnection, urn:Urn) -> ServerConnection:
        """ ToScopedServerConnection(sqlConnection: SqlConnection, urn: Urn) -> ServerConnection """
        ...

    __all__: list = ...


class DataProvider(IDataReader): # skipped bases: <type 'IDisposable'>, <type 'IDataRecord'>, <type 'object'>
    """
    DataProvider(sb: StatementBuilder)
    DataProvider(sb: StatementBuilder, rm: RetriveMode)
    """
    @property
    def FieldCount(self) -> int:
        """ Get: FieldCount(self: DataProvider) -> int """
        ...


    def Dispose(self): # -> 
        """ Dispose(self: DataProvider) """
        ...

    def GetBoolean(self, i:int) -> bool:
        """ GetBoolean(self: DataProvider, i: int) -> bool """
        ...

    def GetByte(self, i:int) -> Byte:
        """ GetByte(self: DataProvider, i: int) -> Byte """
        ...

    def GetBytes(self, i:int, fieldOffset:Int64, buffer:Array, bufferoffset:int, length:int) -> Int64:
        """ GetBytes(self: DataProvider, i: int, fieldOffset: Int64, buffer: Array[Byte], bufferoffset: int, length: int) -> Int64 """
        ...

    def GetChar(self, i:int) -> Char:
        """ GetChar(self: DataProvider, i: int) -> Char """
        ...

    def GetChars(self, i:int, fieldoffset:Int64, buffer:Array, bufferoffset:int, length:int) -> Int64:
        """ GetChars(self: DataProvider, i: int, fieldoffset: Int64, buffer: Array[Char], bufferoffset: int, length: int) -> Int64 """
        ...

    def GetData(self, i:int) -> IDataReader:
        """ GetData(self: DataProvider, i: int) -> IDataReader """
        ...

    def GetDataTypeName(self, i:int) -> str:
        """ GetDataTypeName(self: DataProvider, i: int) -> str """
        ...

    def GetDateTime(self, i:int) -> DateTime:
        """ GetDateTime(self: DataProvider, i: int) -> DateTime """
        ...

    def GetDecimal(self, i:int) -> Decimal:
        """ GetDecimal(self: DataProvider, i: int) -> Decimal """
        ...

    def GetDouble(self, i:int) -> float:
        """ GetDouble(self: DataProvider, i: int) -> float """
        ...

    def GetFieldType(self, i:int) -> Type:
        """ GetFieldType(self: DataProvider, i: int) -> Type """
        ...

    def GetFloat(self, i:int) -> Single:
        """ GetFloat(self: DataProvider, i: int) -> Single """
        ...

    def GetGuid(self, i:int) -> Guid:
        """ GetGuid(self: DataProvider, i: int) -> Guid """
        ...

    def GetInt16(self, i:int) -> Int16:
        """ GetInt16(self: DataProvider, i: int) -> Int16 """
        ...

    def GetInt32(self, i:int) -> int:
        """ GetInt32(self: DataProvider, i: int) -> int """
        ...

    def GetInt64(self, i:int) -> Int64:
        """ GetInt64(self: DataProvider, i: int) -> Int64 """
        ...

    def GetName(self, i:int) -> str:
        """ GetName(self: DataProvider, i: int) -> str """
        ...

    def GetOrdinal(self, name:str) -> int:
        """ GetOrdinal(self: DataProvider, name: str) -> int """
        ...

    def GetString(self, i:int) -> str:
        """ GetString(self: DataProvider, i: int) -> str """
        ...

    def GetValue(self, i:int) -> object:
        """ GetValue(self: DataProvider, i: int) -> object """
        ...

    def GetValues(self, values:Array) -> int:
        """ GetValues(self: DataProvider, values: Array[object]) -> int """
        ...

    def InitRowDataManipulation(self, parentProperties:ArrayList, postProcessList:SortedList): # -> 
        """ InitRowDataManipulation(self: DataProvider, parentProperties: ArrayList, postProcessList: SortedList) """
        ...

    def InitSchemaTable(self, parentProperties:ArrayList): # -> 
        """ InitSchemaTable(self: DataProvider, parentProperties: ArrayList) """
        ...

    def IsDBNull(self, i:int) -> bool:
        """ IsDBNull(self: DataProvider, i: int) -> bool """
        ...

    def RetriveMode(self, *args): #cannot find CLR method
        """ enum RetriveMode, values: RetriveDataReader (0), RetriveDataTable (1) """
        ...

    def SetConnectionAndQuery(self, execSql:ExecuteSql, query:str): # -> 
        """ SetConnectionAndQuery(self: DataProvider, execSql: ExecuteSql, query: str) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...



class Dependency: # skipped bases: <type 'object'>, <type 'object'>
    """
    Dependency()
    Dependency(dep: Dependency)
    """
    @property
    def IsSchemaBound(self) -> bool:
        """
        Get: IsSchemaBound(self: Dependency) -> bool
        Set: IsSchemaBound(self: Dependency) = value
        """
        ...

    @property
    def Links(self) -> DependencyChainCollection:
        """ Get: Links(self: Dependency) -> DependencyChainCollection """
        ...

    @property
    def Urn(self) -> Urn:
        """
        Get: Urn(self: Dependency) -> Urn
        Set: Urn(self: Dependency) = value
        """
        ...


    def Copy(self) -> Dependency:
        """ Copy(self: Dependency) -> Dependency """
        ...


class DependencyChainCollection(ArrayList): # skipped bases: <type 'ICloneable'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    DependencyChainCollection()
    DependencyChainCollection(deps: DependencyChainCollection)
    """
    pass

class DependencyRequest: # skipped bases: <type 'object'>, <type 'object'>
    """ DependencyRequest() """
    @property
    def ParentDependencies(self) -> bool:
        """
        Get: ParentDependencies(self: DependencyRequest) -> bool
        Set: ParentDependencies(self: DependencyRequest) = value
        """
        ...

    @property
    def Urns(self) -> Array:
        """
        Get: Urns(self: DependencyRequest) -> Array[Urn]
        Set: Urns(self: DependencyRequest) = value
        """
        ...



class DisplayCategoryKeyAttribute(IDisplayKey, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DisplayCategoryKeyAttribute(key: str) """
    @property
    def Key(self) -> str:
        """ Get: Key(self: DisplayCategoryKeyAttribute) -> str """
        ...


    def GetDefaultKey(self, *__args:PropertyInfo) -> str:
        """
        GetDefaultKey(self: DisplayCategoryKeyAttribute, property: PropertyInfo) -> str
        GetDefaultKey(self: DisplayCategoryKeyAttribute, type: Type) -> str
        GetDefaultKey(self: DisplayCategoryKeyAttribute, field: FieldInfo) -> str
        """
        ...

    def __new__(cls, key:str) -> Self:
        """ __new__(cls: type, key: str) """
        ...


class DisplayDescriptionKeyAttribute(IDisplayKey, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DisplayDescriptionKeyAttribute(key: str) """
    @property
    def Key(self) -> str:
        """ Get: Key(self: DisplayDescriptionKeyAttribute) -> str """
        ...


    def GetDefaultKey(self, *__args:PropertyInfo) -> str:
        """
        GetDefaultKey(self: DisplayDescriptionKeyAttribute, property: PropertyInfo) -> str
        GetDefaultKey(self: DisplayDescriptionKeyAttribute, type: Type) -> str
        GetDefaultKey(self: DisplayDescriptionKeyAttribute, field: FieldInfo) -> str
        """
        ...

    def __new__(cls, key:str) -> Self:
        """ __new__(cls: type, key: str) """
        ...


class DisplayNameKeyAttribute(IDisplayKey, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DisplayNameKeyAttribute(key: str) """
    @property
    def Key(self) -> str:
        """ Get: Key(self: DisplayNameKeyAttribute) -> str """
        ...


    def GetDefaultKey(self, *__args:PropertyInfo) -> str:
        """
        GetDefaultKey(self: DisplayNameKeyAttribute, property: PropertyInfo) -> str
        GetDefaultKey(self: DisplayNameKeyAttribute, type: Type) -> str
        GetDefaultKey(self: DisplayNameKeyAttribute, field: FieldInfo) -> str
        """
        ...

    def __new__(cls, key:str) -> Self:
        """ __new__(cls: type, key: str) """
        ...


class DmfIgnorePropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DmfIgnorePropertyAttribute() """
    pass

class SfcKey(IEquatable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InstanceType(self) -> Type:
        """ Get: InstanceType(self: SfcKey) -> Type """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: SfcKey) -> int """
        ...

    def GetUrnFragment(self) -> str:
        """ GetUrnFragment(self: SfcKey) -> str """
        ...

    def ToString(self) -> str:
        """ ToString(self: SfcKey) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DomainRootKey(SfcKey): # skipped bases: <type 'IEquatable[SfcKey]'>, <type 'object'>
    """ no doc """
    @property
    def Domain(self) -> ISfcDomain:
        """
        Get: Domain(self: DomainRootKey) -> ISfcDomain
        Set: Domain(self: DomainRootKey) = value
        """
        ...


    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, domain: ISfcDomain) """
        ...


class DynamicValuesAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DynamicValuesAttribute(enabled: bool) """
    @property
    def Enabled(self) -> bool:
        """ Get: Enabled(self: DynamicValuesAttribute) -> bool """
        ...


    def __new__(cls, enabled:bool) -> Self:
        """ __new__(cls: type, enabled: bool) """
        ...


class DynamicValueTypeConverter(StringConverter): # skipped bases: <type 'object'>
    """ DynamicValueTypeConverter() """
    def GetStandardValues(self, context:ITypeDescriptorContext = ...): # -> StandardValuesCollection
        """ GetStandardValues(self: DynamicValueTypeConverter, context: ITypeDescriptorContext) -> StandardValuesCollection """
        ...

    def GetStandardValuesExclusive(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesExclusive(self: DynamicValueTypeConverter, context: ITypeDescriptorContext) -> bool """
        ...

    def GetStandardValuesSupported(self, context:ITypeDescriptorContext = ...) -> bool:
        """ GetStandardValuesSupported(self: DynamicValueTypeConverter, context: ITypeDescriptorContext) -> bool """
        ...


class Enumerator(MarshalByRefObject): # skipped bases: <type 'object'>
    """ Enumerator() """
    def EnumDependencies(self, connectionInfo:object, dependencyRequest:DependencyRequest) -> DependencyChainCollection:
        """ EnumDependencies(self: Enumerator, connectionInfo: object, dependencyRequest: DependencyRequest) -> DependencyChainCollection """
        ...

    @staticmethod
    def GetData(connectionInfo:object, *__args:Urn) -> EnumResult:
        """
        GetData(connectionInfo: object, urn: Urn) -> EnumResult
        GetData(connectionInfo: object, urn: Urn, requestedFields: Array[str]) -> EnumResult
        GetData(connectionInfo: object, urn: Urn, requestedFields: Array[str], orderBy: Array[OrderBy]) -> EnumResult
        GetData(connectionInfo: object, request: Request) -> EnumResult
        GetData(connectionInfo: object, urn: Urn, requestedFields: Array[str], orderBy: OrderBy) -> EnumResult
        """
        ...

    def Process(self, *__args) -> EnumResult:
        """
        Process(self: Enumerator, connectionInfo: object, request: Request) -> EnumResult
        Process(self: Enumerator, connectionInfo: object, requestObjectInfo: RequestObjectInfo) -> ObjectInfo
        Process(self: Enumerator, version: ServerVersion, requestObjectInfo: RequestObjectInfo) -> ObjectInfo
        """
        ...

    @staticmethod
    def RegisterExtension(urn:Urn, name:str, assembly:Assembly, implementsType:str): # -> 
        """ RegisterExtension(urn: Urn, name: str, assembly: Assembly, implementsType: str) """
        ...

    @staticmethod
    def TraceInfo(*__args:str): # -> 
        """ TraceInfo(strFormat: str, *arg: Array[object])TraceInfo(trace: str) """
        ...


class EnumeratorException(SqlServerManagementException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EnumeratorException()
    EnumeratorException(message: str)
    EnumeratorException(message: str, innerException: Exception)
    """
    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    SerializeObjectState = ...


class EnumObject: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ConnectionInfo(self) -> object:
        """
        Get: ConnectionInfo(self: EnumObject) -> object
        Set: ConnectionInfo(self: EnumObject) = value
        """
        ...

    @property
    def Filter(self) -> FilterNode:
        """
        Get: Filter(self: EnumObject) -> FilterNode
        Set: Filter(self: EnumObject) = value
        """
        ...

    @property
    def FixedProperties(self):
        ...

    @property
    def Name(self):
        ...

    @property
    def Request(self) -> Request:
        """
        Get: Request(self: EnumObject) -> Request
        Set: Request(self: EnumObject) = value
        """
        ...

    @property
    def ResultTypes(self) -> Array:
        """ Get: ResultTypes(self: EnumObject) -> Array[ResultType] """
        ...

    @property
    def Urn(self):
        ...


    def AddProperty(self, *args): #cannot find CLR method
        """ AddProperty(self: EnumObject, op: ObjectProperty) """
        ...

    def ComputeFixedProperties(self) -> bool:
        """ ComputeFixedProperties(self: EnumObject) -> bool """
        ...

    def GetAliasPropertyName(self, *args): #cannot find CLR method
        """ GetAliasPropertyName(self: EnumObject, prop: str) -> str """
        ...

    def GetData(self, erParent:EnumResult) -> EnumResult:
        """ GetData(self: EnumObject, erParent: EnumResult) -> EnumResult """
        ...

    def GetFixedStringProperty(self, *args): #cannot find CLR method
        """ GetFixedStringProperty(self: EnumObject, propertyName: str, removeEscape: bool) -> str """
        ...

    def GetProperties(self, usage:ObjectPropertyUsages) -> Array:
        """ GetProperties(self: EnumObject, usage: ObjectPropertyUsages) -> Array[ObjectProperty] """
        ...

    def GetProperty(self, *args): #cannot find CLR method
        """ GetProperty(self: EnumObject, name: str, usage: ObjectPropertyUsages) -> ObjectProperty """
        ...

    def GetUrnProperties(self) -> Array:
        """ GetUrnProperties(self: EnumObject) -> Array[ObjectProperty] """
        ...

    def Initialize(self, ci:object, block:XPathExpressionBlock): # -> 
        """ Initialize(self: EnumObject, ci: object, block: XPathExpressionBlock) """
        ...

    def PostProcess(self, erChildren:EnumResult): # -> 
        """ PostProcess(self: EnumObject, erChildren: EnumResult) """
        ...

    def RetrieveParentRequest(self) -> Request:
        """ RetrieveParentRequest(self: EnumObject) -> Request """
        ...

    def TryGetProperty(self, *args): #cannot find CLR method
        """ TryGetProperty(self: EnumObject, name: str, usage: ObjectPropertyUsages) -> ObjectProperty """
        ...


class EnumResult: # skipped bases: <type 'object'>, <type 'object'>
    """
    EnumResult(ob: object, resultType: ResultType)
    EnumResult()
    """
    @property
    def Data(self) -> object:
        """
        Get: Data(self: EnumResult) -> object
        Set: Data(self: EnumResult) = value
        """
        ...

    @property
    def Type(self) -> ResultType:
        """ Get: Type(self: EnumResult) -> ResultType """
        ...


    @staticmethod
    def ConvertToDataReader(er:EnumResult) -> IDataReader:
        """ ConvertToDataReader(er: EnumResult) -> IDataReader """
        ...

    @staticmethod
    def ConvertToDataSet(er:EnumResult) -> DataSet:
        """ ConvertToDataSet(er: EnumResult) -> DataSet """
        ...

    @staticmethod
    def ConvertToDataTable(er:EnumResult) -> DataTable:
        """ ConvertToDataTable(er: EnumResult) -> DataTable """
        ...

    @staticmethod
    def ConvertToXmlDocument(er:EnumResult) -> XmlDocument:
        """ ConvertToXmlDocument(er: EnumResult) -> XmlDocument """
        ...

    def SetType(self, *args): #cannot find CLR method
        """ SetType(self: EnumResult, type: ResultType) """
        ...


class ExecuteSql: # skipped bases: <type 'object'>, <type 'object'>
    """ ExecuteSql(con: object) """
    @staticmethod
    def ExecuteImmediate(query:str, con:object = ...): # -> 
        """ ExecuteImmediate(query: str, con: object)ExecuteImmediate(self: ExecuteSql, query: str) """
        ...

    @staticmethod
    def ExecuteImmediateGetMessage(query:str, con:object) -> ArrayList:
        """ ExecuteImmediateGetMessage(query: str, con: object) -> ArrayList """
        ...

    @staticmethod
    def ExecuteWithResults(query:StringCollection, con:object = ..., sb:StatementBuilder = ...) -> DataTable:
        """
        ExecuteWithResults(query: str, con: object) -> DataTable
        ExecuteWithResults(query: StringCollection, con: object, sb: StatementBuilder) -> DataTable
        ExecuteWithResults(query: StringCollection, con: object) -> DataTable
        ExecuteWithResults(self: ExecuteSql, query: str) -> DataTable
        """
        ...

    def GetDatabaseEngineEdition(self, con=None) -> DatabaseEngineEdition:
        """
        GetDatabaseEngineEdition(self: ExecuteSql) -> DatabaseEngineEdition
        GetDatabaseEngineEdition(con: object) -> DatabaseEngineEdition
        """
        ...

    def GetDatabaseEngineType(self, con=None) -> DatabaseEngineType:
        """
        GetDatabaseEngineType(self: ExecuteSql) -> DatabaseEngineType
        GetDatabaseEngineType(con: object) -> DatabaseEngineType
        """
        ...

    def GetDataReader(self, query, command=None) -> SqlDataReader:
        """
        GetDataReader(self: ExecuteSql, query: str) -> SqlDataReader
        GetDataReader(self: ExecuteSql, query: str) -> (SqlDataReader, SqlCommand)
        """
        ...

    def GetServerVersion(self, con=None) -> ServerVersion:
        """
        GetServerVersion(self: ExecuteSql) -> ServerVersion
        GetServerVersion(con: object) -> ServerVersion
        """
        ...


class ExtendedPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ExtendedPropertyAttribute()
    ExtendedPropertyAttribute(parentPropertyName: str)
    """
    @property
    def HasParent(self) -> bool:
        """ Get: HasParent(self: ExtendedPropertyAttribute) -> bool """
        ...

    @property
    def ParentPropertyName(self) -> str:
        """ Get: ParentPropertyName(self: ExtendedPropertyAttribute) -> str """
        ...


    def __new__(cls, parentPropertyName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parentPropertyName: str)
        """
        ...


class FilterDecoder: # skipped bases: <type 'object'>, <type 'object'>
    """ FilterDecoder(isfdc: ISqlFilterDecoderCallback) """
    @property
    def StringPrefix(self) -> str:
        """
        Get: StringPrefix(self: FilterDecoder) -> str
        Set: StringPrefix(self: FilterDecoder) = value
        """
        ...


    def GetSql(self, node:FilterNode) -> str:
        """ GetSql(self: FilterDecoder, node: FilterNode) -> str """
        ...


class FilterNode: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def NodeType(self) -> Type:
        """ Get: NodeType(self: FilterNode) -> Type """
        ...


    @staticmethod
    def Compare(f1:FilterNode, f2:FilterNode, compInfo:CompareOptions, cultureInfo:CultureInfo) -> bool:
        """ Compare(f1: FilterNode, f2: FilterNode, compInfo: CompareOptions, cultureInfo: CultureInfo) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: FilterNode) -> str """
        ...

    def Type(self, *args): #cannot find CLR method
        """ enum Type, values: Attribute (0), Constant (1), Function (3), Group (4), Operator (2) """
        ...



class FilterNodeAttribute(FilterNode): # skipped bases: <type 'object'>
    """ FilterNodeAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: FilterNodeAttribute) -> str """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: FilterNodeAttribute) -> int """
        ...

    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class FilterNodeChildren(FilterNode): # skipped bases: <type 'object'>
    """ no doc """
    def GetHashCode(self) -> int:
        """ GetHashCode(self: FilterNodeChildren) -> int """
        ...


class FilterNodeConstant(FilterNode): # skipped bases: <type 'object'>
    """ FilterNodeConstant(value: object, type: ObjectType) """
    @property
    def ObjType(self) -> ObjectType:
        """ Get: ObjType(self: FilterNodeConstant) -> ObjectType """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: FilterNodeConstant) -> object """
        ...

    @property
    def ValueAsString(self) -> str:
        """ Get: ValueAsString(self: FilterNodeConstant) -> str """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: FilterNodeConstant) -> int """
        ...

    def ObjectType(self, *args): #cannot find CLR method
        """ enum ObjectType, values: Boolean (1), Number (0), String (2) """
        ...

    def __new__(cls, value:object, type:ObjectType) -> Self:
        """ __new__(cls: type, value: object, type: ObjectType) """
        ...



class FilterNodeFunction(FilterNodeChildren): # skipped bases: <type 'object'>
    """ FilterNodeFunction(funcType: Type, name: str, *args: Array[FilterNode]) """
    @property
    def FunctionType(self) -> Type:
        """ Get: FunctionType(self: FilterNodeFunction) -> Type """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: FilterNodeFunction) -> str """
        ...

    @property
    def NodeType(self) -> Type:
        """ Get: NodeType(self: FilterNodeFunction) -> Type """
        ...

    @property
    def ParameterCount(self) -> int:
        """ Get: ParameterCount(self: FilterNodeFunction) -> int """
        ...


    @staticmethod
    def FuncTypeToString(type:Type) -> str:
        """ FuncTypeToString(type: Type) -> str """
        ...

    def GetParameter(self, index:int) -> FilterNode:
        """ GetParameter(self: FilterNodeFunction, index: int) -> FilterNode """
        ...

    def ToString(self) -> str:
        """ ToString(self: FilterNodeFunction) -> str """
        ...

    def __new__(cls, funcType:Type, name:str, args:Array) -> Self:
        """ __new__(cls: type, funcType: Type, name: str, *args: Array[FilterNode]) """
        ...



class FilterNodeGroup(FilterNodeChildren): # skipped bases: <type 'object'>
    """ FilterNodeGroup(node: FilterNode) """
    @property
    def Node(self) -> FilterNode:
        """ Get: Node(self: FilterNodeGroup) -> FilterNode """
        ...

    @property
    def NodeType(self) -> Type:
        """ Get: NodeType(self: FilterNodeGroup) -> Type """
        ...


    def ToString(self) -> str:
        """ ToString(self: FilterNodeGroup) -> str """
        ...

    def __new__(cls, node:FilterNode) -> Self:
        """ __new__(cls: type, node: FilterNode) """
        ...


class FilterNodeOperator(FilterNodeChildren): # skipped bases: <type 'object'>
    """ FilterNodeOperator(opType: Type, left: FilterNode, right: FilterNode) """
    @property
    def Left(self) -> FilterNode:
        """ Get: Left(self: FilterNodeOperator) -> FilterNode """
        ...

    @property
    def NodeType(self) -> Type:
        """ Get: NodeType(self: FilterNodeOperator) -> Type """
        ...

    @property
    def OpType(self) -> Type:
        """ Get: OpType(self: FilterNodeOperator) -> Type """
        ...

    @property
    def Right(self) -> FilterNode:
        """ Get: Right(self: FilterNodeOperator) -> FilterNode """
        ...


    @staticmethod
    def OpTypeToString(type:Type) -> str:
        """ OpTypeToString(type: Type) -> str """
        ...

    def ToString(self) -> str:
        """ ToString(self: FilterNodeOperator) -> str """
        ...

    def __new__(cls, opType:Type, left:FilterNode, right:FilterNode) -> Self:
        """ __new__(cls: type, opType: Type, left: FilterNode, right: FilterNode) """
        ...



class FilterPropertyEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ FilterPropertyEventArgs(instance: SfcInstance, propertyName: str) """
    @property
    def Instance(self) -> SfcInstance:
        """ Get: Instance(self: FilterPropertyEventArgs) -> SfcInstance """
        ...

    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: FilterPropertyEventArgs) -> str """
        ...


    def __new__(cls, instance:SfcInstance, propertyName:str) -> Self:
        """ __new__(cls: type, instance: SfcInstance, propertyName: str) """
        ...


class FilterPropertyHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FilterPropertyHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, serializer:SfcSerializer, propertyArgs:FilterPropertyEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: FilterPropertyHandler, serializer: SfcSerializer, propertyArgs: FilterPropertyEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> object:
        """ EndInvoke(self: FilterPropertyHandler, result: IAsyncResult) -> object """
        ...

    def Invoke(self, serializer:SfcSerializer, propertyArgs:FilterPropertyEventArgs) -> object:
        """ Invoke(self: FilterPropertyHandler, serializer: SfcSerializer, propertyArgs: FilterPropertyEventArgs) -> object """
        ...


class IAlienObject: # skipped bases: <type 'object'>
    """ no doc """
    def Discover(self) -> List:
        """ Discover(self: IAlienObject) -> List[object] """
        ...

    def GetDomainRoot(self) -> ISfcDomainLite:
        """ GetDomainRoot(self: IAlienObject) -> ISfcDomainLite """
        ...

    def GetParent(self) -> object:
        """ GetParent(self: IAlienObject) -> object """
        ...

    def GetPropertyType(self, propertyName:str) -> Type:
        """ GetPropertyType(self: IAlienObject, propertyName: str) -> Type """
        ...

    def GetPropertyValue(self, propertyName:str, propertyType:Type) -> object:
        """ GetPropertyValue(self: IAlienObject, propertyName: str, propertyType: Type) -> object """
        ...

    def GetUrn(self) -> Urn:
        """ GetUrn(self: IAlienObject) -> Urn """
        ...

    def Resolve(self, urnString:str) -> object:
        """ Resolve(self: IAlienObject, urnString: str) -> object """
        ...

    def SetObjectState(self, state:SfcObjectState): # -> 
        """ SetObjectState(self: IAlienObject, state: SfcObjectState) """
        ...

    def SetPropertyValue(self, propertyName:str, propertyType:Type, value:object): # -> 
        """ SetPropertyValue(self: IAlienObject, propertyName: str, propertyType: Type, value: object) """
        ...


class IAlienRoot: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ConnectionContext(self) -> ServerConnection:
        """ Get: ConnectionContext(self: IAlienRoot) -> ServerConnection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IAlienRoot) -> str """
        ...


    def DesignModeInitialize(self): # -> 
        """ DesignModeInitialize(self: IAlienRoot) """
        ...

    def SfcHelper_GetDataTable(self, connection:object, urn:str, fields:Array, orderByFields:Array) -> DataTable:
        """ SfcHelper_GetDataTable(self: IAlienRoot, connection: object, urn: str, fields: Array[str], orderByFields: Array[OrderBy]) -> DataTable """
        ...

    def SfcHelper_GetSmoObject(self, urn:str) -> object:
        """ SfcHelper_GetSmoObject(self: IAlienRoot, urn: str) -> object """
        ...

    def SfcHelper_GetSmoObjectQuery(self, queryString:str, fields:Array, orderByFields:Array) -> List:
        """ SfcHelper_GetSmoObjectQuery(self: IAlienRoot, queryString: str, fields: Array[str], orderByFields: Array[OrderBy]) -> List[str] """
        ...


class IDmfFacet: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDynamicProperties: # skipped bases: <type 'object'>
    """ no doc """
    def AddProperties(self, properties:PropertyDescriptorCollection, context:ITypeDescriptorContext, value:object, attributes:Array): # -> 
        """ AddProperties(self: IDynamicProperties, properties: PropertyDescriptorCollection, context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) """
        ...


class IDynamicReadOnly: # skipped bases: <type 'object'>
    """ no doc """
    def OverrideReadOnly(self, properties:IList, context:ITypeDescriptorContext, value:object, attributes:Array): # -> 
        """ OverrideReadOnly(self: IDynamicReadOnly, properties: IList[LocalizablePropertyDescriptor], context: ITypeDescriptorContext, value: object, attributes: Array[Attribute]) """
        ...

    ReadOnlyPropertyChanged = ...


class IDynamicValues: # skipped bases: <type 'object'>
    """ no doc """
    def GetStandardValues(self, context:ITypeDescriptorContext): # -> StandardValuesCollection
        """ GetStandardValues(self: IDynamicValues, context: ITypeDescriptorContext) -> StandardValuesCollection """
        ...


class IDynamicVisible: # skipped bases: <type 'object'>
    """ no doc """
    def ConfigureVisibleEnumFields(self, context:ITypeDescriptorContext, values:ArrayList) -> ICollection:
        """ ConfigureVisibleEnumFields(self: IDynamicVisible, context: ITypeDescriptorContext, values: ArrayList) -> ICollection """
        ...


class IEnumDependencies: # skipped bases: <type 'object'>
    """ no doc """
    def EnumDependencies(self, ci:object, rd:DependencyRequest) -> DependencyChainCollection:
        """ EnumDependencies(self: IEnumDependencies, ci: object, rd: DependencyRequest) -> DependencyChainCollection """
        ...


class InternalEnumeratorException(EnumeratorException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InternalEnumeratorException()
    InternalEnumeratorException(message: str)
    InternalEnumeratorException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InvalidConfigurationFileEnumeratorException(EnumeratorException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidConfigurationFileEnumeratorException()
    InvalidConfigurationFileEnumeratorException(message: str)
    InvalidConfigurationFileEnumeratorException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InvalidPropertyUsageEnumeratorException(EnumeratorException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidPropertyUsageEnumeratorException()
    InvalidPropertyUsageEnumeratorException(message: str)
    InvalidPropertyUsageEnumeratorException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InvalidQueryExpressionEnumeratorException(EnumeratorException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidQueryExpressionEnumeratorException()
    InvalidQueryExpressionEnumeratorException(message: str)
    InvalidQueryExpressionEnumeratorException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InvalidVersionEnumeratorException(EnumeratorException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidVersionEnumeratorException()
    InvalidVersionEnumeratorException(message: str)
    InvalidVersionEnumeratorException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class IReadOnlyCollection: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: IReadOnlyCollection) -> int """
        ...


    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        ...


class IReadOnlyDictionary(IReadOnlyCollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IReadOnlyCollection'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Keys(self) -> IEnumerable:
        """ Get: Keys(self: IReadOnlyDictionary[K, T]) -> IEnumerable[K] """
        ...

    @property
    def Values(self) -> IEnumerable:
        """ Get: Values(self: IReadOnlyDictionary[K, T]) -> IEnumerable[T] """
        ...


    def ContainsKey(self, key) -> bool: # Not found arg types: {'key': 'K'}
        """ ContainsKey(self: IReadOnlyDictionary[K, T], key: K) -> bool """
        ...

    def TryGetValue(self, key, value): # -> Tuple_[bool, T]
        """ TryGetValue(self: IReadOnlyDictionary[K, T], key: K) -> (bool, T) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IReadOnlyList(IReadOnlyCollection): # skipped bases: <type 'IReadOnlyCollection'>, <type 'IEnumerable'>, <type 'IEnumerable[T]'>, <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IReadOnlySet: # skipped bases: <type 'object'>
    """ no doc """
    def IsProperSubsetOf(self, other:IEnumerable) -> bool:
        """ IsProperSubsetOf(self: IReadOnlySet, other: IEnumerable) -> bool """
        ...

    def IsProperSupersetOf(self, other:IEnumerable) -> bool:
        """ IsProperSupersetOf(self: IReadOnlySet, other: IEnumerable) -> bool """
        ...

    def IsSubsetOf(self, other:IEnumerable) -> bool:
        """ IsSubsetOf(self: IReadOnlySet, other: IEnumerable) -> bool """
        ...

    def IsSupersetOf(self, other:IEnumerable) -> bool:
        """ IsSupersetOf(self: IReadOnlySet, other: IEnumerable) -> bool """
        ...

    def Overlaps(self, other:IEnumerable) -> bool:
        """ Overlaps(self: IReadOnlySet, other: IEnumerable) -> bool """
        ...

    def SetEquals(self, other:IEnumerable) -> bool:
        """ SetEquals(self: IReadOnlySet, other: IEnumerable) -> bool """
        ...

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        ...


class IScriptedByParent: # skipped bases: <type 'object'>
    """ no doc """
    pass

class ISfcAlterable(IAlterable): # skipped bases: <type 'object'>
    """ no doc """
    def ScriptAlter(self) -> ISfcScript:
        """ ScriptAlter(self: ISfcAlterable) -> ISfcScript """
        ...


class ISfcCollection: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ISfcCollection) -> int """
        ...

    @property
    def Initialized(self) -> bool:
        """
        Get: Initialized(self: ISfcCollection) -> bool
        Set: Initialized(self: ISfcCollection) = value
        """
        ...

    @property
    def Parent(self) -> SfcInstance:
        """ Get: Parent(self: ISfcCollection) -> SfcInstance """
        ...


    def Add(self, sfcInstance:SfcInstance): # -> 
        """ Add(self: ISfcCollection, sfcInstance: SfcInstance) """
        ...

    def AddShadow(self, sfcInstance:SfcInstance) -> bool:
        """ AddShadow(self: ISfcCollection, sfcInstance: SfcInstance) -> bool """
        ...

    def EnsureInitialized(self): # -> 
        """ EnsureInitialized(self: ISfcCollection) """
        ...

    def FinishMerge(self): # -> 
        """ FinishMerge(self: ISfcCollection) """
        ...

    def GetCollectionElementNameImpl(self) -> str:
        """ GetCollectionElementNameImpl(self: ISfcCollection) -> str """
        ...

    def GetElementFactory(self) -> SfcObjectFactory:
        """ GetElementFactory(self: ISfcCollection) -> SfcObjectFactory """
        ...

    def GetExisting(self, key, sfcInstance) -> Tuple_[bool, SfcInstance]:
        """ GetExisting(self: ISfcCollection, key: SfcKey) -> (bool, SfcInstance) """
        ...

    def GetObjectByKey(self, key:SfcKey) -> SfcInstance:
        """ GetObjectByKey(self: ISfcCollection, key: SfcKey) -> SfcInstance """
        ...

    def PrepareMerge(self): # -> 
        """ PrepareMerge(self: ISfcCollection) """
        ...

    def Remove(self, sfcInstance:SfcInstance): # -> 
        """ Remove(self: ISfcCollection, sfcInstance: SfcInstance) """
        ...

    def RemoveElement(self, sfcInstance:SfcInstance): # -> 
        """ RemoveElement(self: ISfcCollection, sfcInstance: SfcInstance) """
        ...

    def Rename(self, sfcInstance:SfcInstance, newKey:SfcKey): # -> 
        """ Rename(self: ISfcCollection, sfcInstance: SfcInstance, newKey: SfcKey) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class ISfcCreatable(ICreatable): # skipped bases: <type 'object'>
    """ no doc """
    def ScriptCreate(self) -> ISfcScript:
        """ ScriptCreate(self: ISfcCreatable) -> ISfcScript """
        ...


class ISfcDependencyDiscoveryObjectSink: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Action(self) -> SfcDependencyAction:
        """ Get: Action(self: ISfcDependencyDiscoveryObjectSink) -> SfcDependencyAction """
        ...


    def Add(self, direction, *__args): # -> 
        """ Add(self: ISfcDependencyDiscoveryObjectSink, direction: SfcDependencyDirection, targetObject: SfcInstance, relation: SfcTypeRelation, discovered: bool)Add(self: ISfcDependencyDiscoveryObjectSink, direction: SfcDependencyDirection, targetObjects: IEnumerator, relation: SfcTypeRelation, discovered: bool)Add[T](self: ISfcDependencyDiscoveryObjectSink, direction: SfcDependencyDirection, targetObjects: IEnumerable[T], relation: SfcTypeRelation, discovered: bool) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...


class ISfcDiscoverObject: # skipped bases: <type 'object'>
    """ no doc """
    def Discover(self, sink:ISfcDependencyDiscoveryObjectSink): # -> 
        """ Discover(self: ISfcDiscoverObject, sink: ISfcDependencyDiscoveryObjectSink) """
        ...


class ISfcHasConnection: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ConnectionContext(self) -> SfcConnectionContext:
        """ Get: ConnectionContext(self: ISfcHasConnection) -> SfcConnectionContext """
        ...


    def GetConnection(self, activeQueriesMode:SfcObjectQueryMode = ...) -> ISfcConnection:
        """
        GetConnection(self: ISfcHasConnection) -> ISfcConnection
        GetConnection(self: ISfcHasConnection, activeQueriesMode: SfcObjectQueryMode) -> ISfcConnection
        """
        ...

    def SetConnection(self, connection:ISfcConnection): # -> 
        """ SetConnection(self: ISfcHasConnection, connection: ISfcConnection) """
        ...


class ISfcDomainLite(ISfcHasConnection): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DomainInstanceName(self) -> str:
        """ Get: DomainInstanceName(self: ISfcDomainLite) -> str """
        ...

    @property
    def DomainName(self) -> str:
        """ Get: DomainName(self: ISfcDomainLite) -> str """
        ...


    def GetLogicalVersion(self) -> int:
        """ GetLogicalVersion(self: ISfcDomainLite) -> int """
        ...


class ISfcDomain(ISfcDomainLite): # skipped bases: <type 'ISfcHasConnection'>, <type 'object'>
    """ no doc """
    def GetExecutionEngine(self) -> ISfcExecutionEngine:
        """ GetExecutionEngine(self: ISfcDomain) -> ISfcExecutionEngine """
        ...

    def GetKey(self, urnFragment:IUrnFragment) -> SfcKey:
        """ GetKey(self: ISfcDomain, urnFragment: IUrnFragment) -> SfcKey """
        ...

    def GetType(self, typeName:str) -> Type:
        """ GetType(self: ISfcDomain, typeName: str) -> Type """
        ...

    def GetTypeMetadata(self, typeName:str) -> SfcTypeMetadata:
        """ GetTypeMetadata(self: ISfcDomain, typeName: str) -> SfcTypeMetadata """
        ...

    def UseSfcStateManagement(self) -> bool:
        """ UseSfcStateManagement(self: ISfcDomain) -> bool """
        ...


class ISfcDomain2(ISfcDomain): # skipped bases: <type 'ISfcDomainLite'>, <type 'ISfcHasConnection'>, <type 'object'>
    """ no doc """
    def GetUrnSkeletonsFromType(self, inputType:Type) -> List:
        """ GetUrnSkeletonsFromType(self: ISfcDomain2, inputType: Type) -> List[str] """
        ...


class ISfcDroppable(IDroppable): # skipped bases: <type 'object'>
    """ no doc """
    def ScriptDrop(self) -> ISfcScript:
        """ ScriptDrop(self: ISfcDroppable) -> ISfcScript """
        ...


class ISfcExecutionEngine: # skipped bases: <type 'object'>
    """ no doc """
    def Execute(self, script:ISfcScript) -> object:
        """ Execute(self: ISfcExecutionEngine, script: ISfcScript) -> object """
        ...


class ISfcMarkForDrop(IMarkForDrop): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ISfcMovable: # skipped bases: <type 'object'>
    """ no doc """
    def Move(self, newParent:SfcInstance): # -> 
        """ Move(self: ISfcMovable, newParent: SfcInstance) """
        ...

    def ScriptMove(self, newParent:SfcInstance) -> ISfcScript:
        """ ScriptMove(self: ISfcMovable, newParent: SfcInstance) -> ISfcScript """
        ...


class ISfcNotifyPropertyMetadataChanged: # skipped bases: <type 'object'>
    """ no doc """
    PropertyMetadataChanged = ...


class ISfcProperty: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> AttributeCollection:
        """ Get: Attributes(self: ISfcProperty) -> AttributeCollection """
        ...

    @property
    def Dirty(self) -> bool:
        """ Get: Dirty(self: ISfcProperty) -> bool """
        ...

    @property
    def Enabled(self) -> bool:
        """ Get: Enabled(self: ISfcProperty) -> bool """
        ...

    @property
    def IsNull(self) -> bool:
        """ Get: IsNull(self: ISfcProperty) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ISfcProperty) -> str """
        ...

    @property
    def Required(self) -> bool:
        """ Get: Required(self: ISfcProperty) -> bool """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: ISfcProperty) -> Type """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: ISfcProperty) -> object
        Set: Value(self: ISfcProperty) = value
        """
        ...

    @property
    def Writable(self) -> bool:
        """ Get: Writable(self: ISfcProperty) -> bool """
        ...



class ISfcPropertyProvider(ISfcNotifyPropertyMetadataChanged, INotifyPropertyChanged): # skipped bases: <type 'object'>
    """ no doc """
    def GetPropertySet(self) -> ISfcPropertySet:
        """ GetPropertySet(self: ISfcPropertyProvider) -> ISfcPropertySet """
        ...


class ISfcPropertySet: # skipped bases: <type 'object'>
    """ no doc """
    def Contains(self, *__args:str) -> bool:
        """
        Contains(self: ISfcPropertySet, propertyName: str) -> bool
        Contains(self: ISfcPropertySet, property: ISfcProperty) -> bool
        Contains[T](self: ISfcPropertySet, name: str) -> bool
        """
        ...

    def EnumProperties(self) -> IEnumerable:
        """ EnumProperties(self: ISfcPropertySet) -> IEnumerable[ISfcProperty] """
        ...

    def TryGetProperty(self, name, property) -> Tuple_[bool, ISfcProperty]:
        """ TryGetProperty(self: ISfcPropertySet, name: str) -> (bool, ISfcProperty) """
        ...

    def TryGetPropertyValue(self, name, value): # -> Tuple_[bool, T]
        """
        TryGetPropertyValue[T](self: ISfcPropertySet, name: str) -> (bool, T)
        TryGetPropertyValue(self: ISfcPropertySet, name: str) -> (bool, object)
        """
        ...


class ISfcPropertyStorageProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetPropertyValueImpl(self, propertyName:str) -> object:
        """ GetPropertyValueImpl(self: ISfcPropertyStorageProvider, propertyName: str) -> object """
        ...

    def SetPropertyValueImpl(self, propertyName:str, value:object): # -> 
        """ SetPropertyValueImpl(self: ISfcPropertyStorageProvider, propertyName: str, value: object) """
        ...


class ISfcRenamable: # skipped bases: <type 'object'>
    """ no doc """
    def Rename(self, newKey:SfcKey): # -> 
        """ Rename(self: ISfcRenamable, newKey: SfcKey) """
        ...

    def ScriptRename(self, newKey:SfcKey) -> ISfcScript:
        """ ScriptRename(self: ISfcRenamable, newKey: SfcKey) -> ISfcScript """
        ...


class ISfcScript: # skipped bases: <type 'object'>
    """ no doc """
    def Add(self, script:ISfcScript): # -> 
        """ Add(self: ISfcScript, script: ISfcScript) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class ISfcScriptCollector: # skipped bases: <type 'object'>
    """ no doc """
    def OpenWriter(self, append:bool = ...): # -> T
        """
        OpenWriter[T](self: ISfcScriptCollector) -> T
        OpenWriter[T](self: ISfcScriptCollector, append: bool) -> T
        """
        ...


class ISfcSerializableUpgrade: # skipped bases: <type 'object'>
    """ no doc """
    def StartSerializationUpgrade(self) -> UpgradeSession:
        """ StartSerializationUpgrade(self: ISfcSerializableUpgrade) -> UpgradeSession """
        ...


class ISfcSimpleList(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def ListReference(self) -> IEnumerable:
        """ Get: ListReference(self: ISfcSimpleList) -> IEnumerable """
        ...


    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ISfcSimpleNode](enumerable: IEnumerable[ISfcSimpleNode], value: ISfcSimpleNode) -> bool """
        ...


class ISfcSimpleMap: # skipped bases: <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ISfcSimpleNode: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ObjectReference(self) -> object:
        """ Get: ObjectReference(self: ISfcSimpleNode) -> object """
        ...

    @property
    def Properties(self) -> ISfcSimpleMap:
        """ Get: Properties(self: ISfcSimpleNode) -> ISfcSimpleMap[str, object] """
        ...

    @property
    def RelatedContainers(self) -> ISfcSimpleMap:
        """ Get: RelatedContainers(self: ISfcSimpleNode) -> ISfcSimpleMap[str, ISfcSimpleList] """
        ...

    @property
    def RelatedObjects(self) -> ISfcSimpleMap:
        """ Get: RelatedObjects(self: ISfcSimpleNode) -> ISfcSimpleMap[str, ISfcSimpleNode] """
        ...

    @property
    def Urn(self) -> Urn:
        """ Get: Urn(self: ISfcSimpleNode) -> Urn """
        ...



class ISfcSupportsDesignMode: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsDesignMode(self) -> bool:
        """ Get: IsDesignMode(self: ISfcSupportsDesignMode) -> bool """
        ...



class ISfcValidate: # skipped bases: <type 'object'>
    """ no doc """
    def Validate(self, methodName:str, arguments:Array) -> ValidationState:
        """ Validate(self: ISfcValidate, methodName: str, *arguments: Array[object]) -> ValidationState """
        ...


class ISqlFilterDecoderCallback: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SupportsParameterization(self) -> bool:
        """ Get: SupportsParameterization(self: ISqlFilterDecoderCallback) -> bool """
        ...


    def AddConstantForFilter(self, constantValue:str) -> str:
        """ AddConstantForFilter(self: ISqlFilterDecoderCallback, constantValue: str) -> str """
        ...

    def AddPropertyForFilter(self, name:str) -> str:
        """ AddPropertyForFilter(self: ISqlFilterDecoderCallback, name: str) -> str """
        ...


class ISupportDatabaseEngineEditions: # skipped bases: <type 'object'>
    """ no doc """
    def GetDatabaseEngineEdition(self, conn:object) -> DatabaseEngineEdition:
        """ GetDatabaseEngineEdition(self: ISupportDatabaseEngineEditions, conn: object) -> DatabaseEngineEdition """
        ...


class ISupportDatabaseEngineTypes: # skipped bases: <type 'object'>
    """ no doc """
    def GetDatabaseEngineType(self, conn:object) -> DatabaseEngineType:
        """ GetDatabaseEngineType(self: ISupportDatabaseEngineTypes, conn: object) -> DatabaseEngineType """
        ...


class ISupportInitData: # skipped bases: <type 'object'>
    """ no doc """
    def LoadInitData(self, file:str, ver:ServerVersion): # -> 
        """ LoadInitData(self: ISupportInitData, file: str, ver: ServerVersion) """
        ...


class ISupportInitDatabaseEngineData: # skipped bases: <type 'object'>
    """ no doc """
    def LoadInitData(self, file:str, ver:ServerVersion, databaseEngineType:DatabaseEngineType, databaseEngineEdition:DatabaseEngineEdition): # -> 
        """ LoadInitData(self: ISupportInitDatabaseEngineData, file: str, ver: ServerVersion, databaseEngineType: DatabaseEngineType, databaseEngineEdition: DatabaseEngineEdition) """
        ...


class ISupportVersions: # skipped bases: <type 'object'>
    """ no doc """
    def GetServerVersion(self, conn:object) -> ServerVersion:
        """ GetServerVersion(self: ISupportVersions, conn: object) -> ServerVersion """
        ...


class IUrnFragment: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def FieldDictionary(self) -> Dictionary:
        """ Get: FieldDictionary(self: IUrnFragment) -> Dictionary[str, object] """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IUrnFragment) -> str """
        ...



class IXmlSerializationAdapter: # skipped bases: <type 'object'>
    """ no doc """
    def ReadXml(self, reader, deserializedObject) -> object:
        """ ReadXml(self: IXmlSerializationAdapter, reader: XmlReader) -> object """
        ...

    def WriteXml(self, writer:XmlWriter, objectToSerialize:object): # -> 
        """ WriteXml(self: IXmlSerializationAdapter, writer: XmlWriter, objectToSerialize: object) """
        ...


class LinkField: # skipped bases: <type 'object'>, <type 'object'>
    """ LinkField() """
    @property
    def Field(self) -> str:
        """
        Get: Field(self: LinkField) -> str
        Set: Field(self: LinkField) = value
        """
        ...

    @property
    def Type(self) -> LinkFieldType:
        """
        Get: Type(self: LinkField) -> LinkFieldType
        Set: Type(self: LinkField) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: LinkField) -> str
        Set: Value(self: LinkField) = value
        """
        ...



class LinkFieldType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LinkFieldType, values: Computed (2), Filter (3), Local (1), Parent (0) """
    Computed: LinkFieldType = ...
    Filter: LinkFieldType = ...
    Local: LinkFieldType = ...
    Parent: LinkFieldType = ...
    value__ = ...


class LinkMultiple: # skipped bases: <type 'object'>, <type 'object'>
    """ LinkMultiple() """
    @property
    def LinkFields(self) -> ArrayList:
        """ Get: LinkFields(self: LinkMultiple) -> ArrayList """
        ...

    @property
    def No(self) -> str:
        """
        Get: No(self: LinkMultiple) -> str
        Set: No(self: LinkMultiple) = value
        """
        ...


    def GetSqlExpression(self, obj:SqlObjectBase) -> str:
        """ GetSqlExpression(self: LinkMultiple, obj: SqlObjectBase) -> str """
        ...

    def SetLinkFields(self, list:ArrayList): # -> 
        """ SetLinkFields(self: LinkMultiple, list: ArrayList) """
        ...


class LocalizableEnumConverter(EnumConverter): # skipped bases: <type 'object'>
    """ LocalizableEnumConverter(type: Type) """
    pass

class LocalizableMemberDescriptor(MemberDescriptor): # skipped bases: <type 'object'>
    """ LocalizableMemberDescriptor(type: Type, resourceManager: ResourceManager, isDefaultResourceManager: bool) """
    pass

class LocalizablePropertyDescriptor(PropertyDescriptor): # skipped bases: <type 'object'>
    """ LocalizablePropertyDescriptor(property: PropertyInfo, resourceManager: ResourceManager, isDefaultResourceManager: bool) """
    @property
    def Category(self) -> str:
        """ Get: Category(self: LocalizablePropertyDescriptor) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: LocalizablePropertyDescriptor) -> str """
        ...

    @property
    def DesignTimeOnly(self) -> bool:
        """ Get: DesignTimeOnly(self: LocalizablePropertyDescriptor) -> bool """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: LocalizablePropertyDescriptor) -> str """
        ...

    @property
    def DisplayOrdinal(self) -> int:
        """ Get: DisplayOrdinal(self: LocalizablePropertyDescriptor) -> int """
        ...

    @property
    def IsBrowsable(self) -> bool:
        """ Get: IsBrowsable(self: LocalizablePropertyDescriptor) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: LocalizablePropertyDescriptor) -> str """
        ...


    def ForceReadOnly(self): # -> 
        """ ForceReadOnly(self: LocalizablePropertyDescriptor) """
        ...


class LocalizableTypeConverter(TypeConverter): # skipped bases: <type 'object'>
    """ LocalizableTypeConverter() """
    def GetTypeMemberDescriptor(self, type:Type) -> LocalizableMemberDescriptor:
        """ GetTypeMemberDescriptor(self: LocalizableTypeConverter, type: Type) -> LocalizableMemberDescriptor """
        ...


class LocalizedPropertyResourcesAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    LocalizedPropertyResourcesAttribute(resourcesName: str)
    LocalizedPropertyResourcesAttribute(resourcesName: str, useDefaultKeys: bool)
    LocalizedPropertyResourcesAttribute(resourceType: Type)
    """
    @property
    def ResourcesName(self) -> str:
        """ Get: ResourcesName(self: LocalizedPropertyResourcesAttribute) -> str """
        ...

    @property
    def UseDefaultKeys(self) -> bool:
        """ Get: UseDefaultKeys(self: LocalizedPropertyResourcesAttribute) -> bool """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, resourcesName: str)
        __new__(cls: type, resourcesName: str, useDefaultKeys: bool)
        __new__(cls: type, resourceType: Type)
        """
        ...


class NamedDomainKey(DomainRootKey, IEquatable): # skipped bases: <type 'IEquatable[SfcKey]'>, <type 'object'>
    """
    NamedDomainKey[T]()
    NamedDomainKey[T](domain: ISfcDomain)
    NamedDomainKey[T](domain: ISfcDomain, name: str)
    NamedDomainKey[T](domain: ISfcDomain, fields: IDictionary[str, object])
    """
    @property
    def InstanceType(self) -> Type:
        """ Get: InstanceType(self: NamedDomainKey[T]) -> Type """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: NamedDomainKey[T]) -> str """
        ...

    @property
    def UrnName(self):
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: NamedDomainKey[T]) -> int """
        ...

    def GetUrnFragment(self) -> str:
        """ GetUrnFragment(self: NamedDomainKey[T]) -> str """
        ...

    def ToString(self) -> str:
        """ ToString(self: NamedDomainKey[T]) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class NamedKey(SfcKey, IEquatable): # skipped bases: <type 'IEquatable[SfcKey]'>, <type 'object'>
    """
    NamedKey[T]()
    NamedKey[T](other: NamedKey[T])
    NamedKey[T](name: str)
    NamedKey[T](fields: IDictionary[str, object])
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: NamedKey[T]) -> str """
        ...

    @property
    def UrnName(self):
        ...


    def __new__(cls, *__args:NamedKey) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, other: NamedKey[T])
        __new__(cls: type, name: str)
        __new__(cls: type, fields: IDictionary[str, object])
        """
        ...


class ObjectInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ ObjectInfo() """
    @property
    def Children(self) -> Array:
        """
        Get: Children(self: ObjectInfo) -> Array[str]
        Set: Children(self: ObjectInfo) = value
        """
        ...

    @property
    def Properties(self) -> Array:
        """
        Get: Properties(self: ObjectInfo) -> Array[ObjectProperty]
        Set: Properties(self: ObjectInfo) = value
        """
        ...

    @property
    def ResultTypes(self) -> Array:
        """
        Get: ResultTypes(self: ObjectInfo) -> Array[ResultType]
        Set: ResultTypes(self: ObjectInfo) = value
        """
        ...

    @property
    def UrnProperties(self) -> Array:
        """
        Get: UrnProperties(self: ObjectInfo) -> Array[ObjectProperty]
        Set: UrnProperties(self: ObjectInfo) = value
        """
        ...



class ObjectProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ ObjectProperty() """
    @property
    def DefaultValue(self) -> str:
        """
        Get: DefaultValue(self: ObjectProperty) -> str
        Set: DefaultValue(self: ObjectProperty) = value
        """
        ...

    @property
    def Expensive(self) -> bool:
        """
        Get: Expensive(self: ObjectProperty) -> bool
        Set: Expensive(self: ObjectProperty) = value
        """
        ...

    @property
    def ExtendedType(self) -> bool:
        """
        Get: ExtendedType(self: ObjectProperty) -> bool
        Set: ExtendedType(self: ObjectProperty) = value
        """
        ...

    @property
    def KeyIndex(self) -> Int16:
        """
        Get: KeyIndex(self: ObjectProperty) -> Int16
        Set: KeyIndex(self: ObjectProperty) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ObjectProperty) -> str
        Set: Name(self: ObjectProperty) = value
        """
        ...

    @property
    def PropertyMode(self) -> PropertyMode:
        """
        Get: PropertyMode(self: ObjectProperty) -> PropertyMode
        Set: PropertyMode(self: ObjectProperty) = value
        """
        ...

    @property
    def ReadOnly(self) -> bool:
        """
        Get: ReadOnly(self: ObjectProperty) -> bool
        Set: ReadOnly(self: ObjectProperty) = value
        """
        ...

    @property
    def ReadOnlyAfterCreation(self) -> bool:
        """
        Get: ReadOnlyAfterCreation(self: ObjectProperty) -> bool
        Set: ReadOnlyAfterCreation(self: ObjectProperty) = value
        """
        ...

    @property
    def ReferenceKeys(self) -> str:
        """
        Get: ReferenceKeys(self: ObjectProperty) -> str
        Set: ReferenceKeys(self: ObjectProperty) = value
        """
        ...

    @property
    def ReferenceTemplate(self) -> str:
        """
        Get: ReferenceTemplate(self: ObjectProperty) -> str
        Set: ReferenceTemplate(self: ObjectProperty) = value
        """
        ...

    @property
    def ReferenceTemplateParameters(self) -> str:
        """
        Get: ReferenceTemplateParameters(self: ObjectProperty) -> str
        Set: ReferenceTemplateParameters(self: ObjectProperty) = value
        """
        ...

    @property
    def ReferenceType(self) -> str:
        """
        Get: ReferenceType(self: ObjectProperty) -> str
        Set: ReferenceType(self: ObjectProperty) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: ObjectProperty) -> str
        Set: Type(self: ObjectProperty) = value
        """
        ...

    @property
    def Usage(self) -> ObjectPropertyUsages:
        """
        Get: Usage(self: ObjectProperty) -> ObjectPropertyUsages
        Set: Usage(self: ObjectProperty) = value
        """
        ...



class ObjectPropertyUsages(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ObjectPropertyUsages, values: All (7), Filter (1), None (0), OrderBy (4), Request (2), Reserved1 (8) """
    All: ObjectPropertyUsages = ...
    Filter: ObjectPropertyUsages = ...
    OrderBy: ObjectPropertyUsages = ...
    Request: ObjectPropertyUsages = ...
    Reserved1: ObjectPropertyUsages = ...
    value__ = ...


class OrderBy: # skipped bases: <type 'object'>, <type 'object'>
    """
    OrderBy()
    OrderBy(field: str, dir: Direction)
    """
    @property
    def Dir(self): # -> Direction
        """
        Get: Dir(self: OrderBy) -> Direction
        Set: Dir(self: OrderBy) = value
        """
        ...

    @property
    def Field(self) -> str:
        """
        Get: Field(self: OrderBy) -> str
        Set: Field(self: OrderBy) = value
        """
        ...


    def Direction(self, *args): #cannot find CLR method
        """ enum Direction, values: Asc (0), Desc (1) """
        ...



class PhysicalFacetAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    PhysicalFacetAttribute()
    PhysicalFacetAttribute(options: PhysicalFacetOptions)
    """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: PhysicalFacetAttribute) -> bool """
        ...


    def __new__(cls, options:PhysicalFacetOptions = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, options: PhysicalFacetOptions)
        """
        ...


class PhysicalFacetOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PhysicalFacetOptions, values: None (0), ReadOnly (1) """
    ReadOnly: PhysicalFacetOptions = ...
    value__ = ...


class PropertiesRequest: # skipped bases: <type 'object'>, <type 'object'>
    """
    PropertiesRequest()
    PropertiesRequest(fields: Array[str])
    PropertiesRequest(fields: Array[str], orderBy: Array[OrderBy])
    """
    @property
    def Fields(self) -> Array:
        """
        Get: Fields(self: PropertiesRequest) -> Array[str]
        Set: Fields(self: PropertiesRequest) = value
        """
        ...

    @property
    def OrderByList(self) -> Array:
        """
        Get: OrderByList(self: PropertiesRequest) -> Array[OrderBy]
        Set: OrderByList(self: PropertiesRequest) = value
        """
        ...

    @property
    def PropertyAlias(self) -> PropertyAlias:
        """
        Get: PropertyAlias(self: PropertiesRequest) -> PropertyAlias
        Set: PropertyAlias(self: PropertiesRequest) = value
        """
        ...

    @property
    def RequestFieldsTypes(self) -> RequestFieldsTypes:
        """
        Get: RequestFieldsTypes(self: PropertiesRequest) -> RequestFieldsTypes
        Set: RequestFieldsTypes(self: PropertiesRequest) = value
        """
        ...



class PropertyAlias: # skipped bases: <type 'object'>, <type 'object'>
    """
    PropertyAlias()
    PropertyAlias(prefix: str)
    PropertyAlias(aliases: Array[str])
    """
    @property
    def Aliases(self) -> Array:
        """
        Get: Aliases(self: PropertyAlias) -> Array[str]
        Set: Aliases(self: PropertyAlias) = value
        """
        ...

    @property
    def Kind(self): # -> AliasKind
        """
        Get: Kind(self: PropertyAlias) -> AliasKind
        Set: Kind(self: PropertyAlias) = value
        """
        ...

    @property
    def Prefix(self) -> str:
        """
        Get: Prefix(self: PropertyAlias) -> str
        Set: Prefix(self: PropertyAlias) = value
        """
        ...


    def AliasKind(self, *args): #cannot find CLR method
        """ enum AliasKind, values: Each (0), NodeName (2), Prefix (1) """
        ...



class PropertyMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PropertyMode, values: All (3), Deploy (2), Design (1), None (0) """
    All: PropertyMode = ...
    Deploy: PropertyMode = ...
    Design: PropertyMode = ...
    value__ = ...


class PropertyOrderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PropertyOrderAttribute(iOrder: int) """
    @property
    def Order(self) -> int:
        """ Get: Order(self: PropertyOrderAttribute) -> int """
        ...


    def __new__(cls, iOrder:int) -> Self:
        """ __new__(cls: type, iOrder: int) """
        ...


class QueryNotSupportedEnumeratorException(EnumeratorException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    QueryNotSupportedEnumeratorException()
    QueryNotSupportedEnumeratorException(message: str)
    QueryNotSupportedEnumeratorException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ReadOnlyList(IReadOnlyList): # skipped bases: <type 'IReadOnlyCollection'>, <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'IReadOnlyCollection[T]'>, <type 'object'>
    """ ReadOnlyList[T](list: IList[T]) """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ReadOnlyList[T]) -> int """
        ...


    def Contains(self, item) -> bool: # Not found arg types: {'item': 'T'}
        """ Contains(self: ReadOnlyList[T], item: T) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: ReadOnlyList[T], array: Array[T], arrayIndex: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ReadOnlyList[T]) -> IEnumerator[T] """
        ...

    def IndexOf(self, item) -> int: # Not found arg types: {'item': 'T'}
        """ IndexOf(self: ReadOnlyList[T], item: T) -> int """
        ...


class ReadOnlyPropertyChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ReadOnlyPropertyChangedEventArgs(propertyName: str) """
    @property
    def PropertyName(self) -> str:
        """
        Get: PropertyName(self: ReadOnlyPropertyChangedEventArgs) -> str
        Set: PropertyName(self: ReadOnlyPropertyChangedEventArgs) = value
        """
        ...


    def __new__(cls, propertyName:str) -> Self:
        """ __new__(cls: type, propertyName: str) """
        ...


class Request(PropertiesRequest): # skipped bases: <type 'object'>
    """
    Request()
    Request(urn: Urn)
    Request(urn: Urn, fields: Array[str])
    Request(urn: Urn, fields: Array[str], orderBy: Array[OrderBy])
    """
    @property
    def ParentPropertiesRequests(self) -> Array:
        """
        Get: ParentPropertiesRequests(self: Request) -> Array[PropertiesRequest]
        Set: ParentPropertiesRequests(self: Request) = value
        """
        ...

    @property
    def ResultType(self) -> ResultType:
        """
        Get: ResultType(self: Request) -> ResultType
        Set: ResultType(self: Request) = value
        """
        ...

    @property
    def Urn(self) -> Urn:
        """
        Get: Urn(self: Request) -> Urn
        Set: Urn(self: Request) = value
        """
        ...



class RequestFieldsTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) RequestFieldsTypes, values: IncludeExpensiveInResult (2), Reject (0), Request (1) """
    IncludeExpensiveInResult: RequestFieldsTypes = ...
    Reject: RequestFieldsTypes = ...
    Request: RequestFieldsTypes = ...
    value__ = ...


class RequestObjectInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    RequestObjectInfo()
    RequestObjectInfo(urn: Urn, infoType: Flags)
    """
    @property
    def InfoType(self): # -> Flags
        """
        Get: InfoType(self: RequestObjectInfo) -> Flags
        Set: InfoType(self: RequestObjectInfo) = value
        """
        ...

    @property
    def Urn(self) -> Urn:
        """
        Get: Urn(self: RequestObjectInfo) -> Urn
        Set: Urn(self: RequestObjectInfo) = value
        """
        ...


    def Flags(self, *args): #cannot find CLR method
        """ enum (flags) Flags, values: All (15), Children (2), None (0), Parents (4), Properties (1), ResultTypes (8), UrnProperties (16) """
        ...



class RequestParentSelect: # skipped bases: <type 'object'>, <type 'object'>
    """ RequestParentSelect(xrrps: XmlRequestParentSelect) """
    @property
    def Fields(self) -> StringCollection:
        """ Get: Fields(self: RequestParentSelect) -> StringCollection """
        ...



class ResultType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ResultType, values: DataSet (1), DataTable (2), Default (0), IDataReader (3), Reserved1 (5), Reserved2 (6), XmlDocument (4) """
    DataSet: ResultType = ...
    DataTable: ResultType = ...
    Default: ResultType = ...
    IDataReader: ResultType = ...
    Reserved1: ResultType = ...
    Reserved2: ResultType = ...
    value__ = ...
    XmlDocument: ResultType = ...


class ResultTypeNotSupportedEnumeratorException(EnumeratorException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ResultTypeNotSupportedEnumeratorException()
    ResultTypeNotSupportedEnumeratorException(msg: str)
    ResultTypeNotSupportedEnumeratorException(msg: str, e: Exception)
    ResultTypeNotSupportedEnumeratorException(type: ResultType)
    ResultTypeNotSupportedEnumeratorException(type: ResultType, innerException: Exception)
    """
    @property
    def ResultType(self) -> str:
        """ Get: ResultType(self: ResultTypeNotSupportedEnumeratorException) -> str """
        ...


    SerializeObjectState = ...


class RootFacetAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ RootFacetAttribute(rootType: Type) """
    @property
    def RootType(self) -> Type:
        """ Get: RootType(self: RootFacetAttribute) -> Type """
        ...


    def __new__(cls, rootType:Type) -> Self:
        """ __new__(cls: type, rootType: Type) """
        ...


class SchemaNamedKey(SfcKey, IEquatable): # skipped bases: <type 'IEquatable[SfcKey]'>, <type 'object'>
    """
    SchemaNamedKey[T]()
    SchemaNamedKey[T](name: str)
    SchemaNamedKey[T](schema: str, name: str)
    SchemaNamedKey[T](other: SchemaNamedKey[T])
    SchemaNamedKey[T](fields: IDictionary[str, object])
    """
    @property
    def Name(self) -> str:
        """ Get: Name(self: SchemaNamedKey[T]) -> str """
        ...

    @property
    def Schema(self) -> str:
        """ Get: Schema(self: SchemaNamedKey[T]) -> str """
        ...

    @property
    def UrnName(self):
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        __new__(cls: type, schema: str, name: str)
        __new__(cls: type, other: SchemaNamedKey[T])
        __new__(cls: type, fields: IDictionary[str, object])
        """
        ...


class SfcEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SfcEventArgs(urn: Urn, instance: SfcInstance) """
    @property
    def Instance(self) -> SfcInstance:
        """ Get: Instance(self: SfcEventArgs) -> SfcInstance """
        ...

    @property
    def Urn(self) -> Urn:
        """ Get: Urn(self: SfcEventArgs) -> Urn """
        ...


    def __new__(cls, urn:Urn, instance:SfcInstance) -> Self:
        """ __new__(cls: type, urn: Urn, instance: SfcInstance) """
        ...


class SfcAfterObjectMovedEventArgs(SfcEventArgs): # skipped bases: <type 'object'>
    """ SfcAfterObjectMovedEventArgs(urn: Urn, instance: SfcInstance, oldUrn: Urn, oldParent: SfcInstance) """
    @property
    def OldParent(self) -> SfcInstance:
        """ Get: OldParent(self: SfcAfterObjectMovedEventArgs) -> SfcInstance """
        ...

    @property
    def OldUrn(self) -> Urn:
        """ Get: OldUrn(self: SfcAfterObjectMovedEventArgs) -> Urn """
        ...



class SfcAfterObjectRenamedEventArgs(SfcEventArgs): # skipped bases: <type 'object'>
    """ SfcAfterObjectRenamedEventArgs(urn: Urn, instance: SfcInstance, oldUrn: Urn, oldKey: SfcKey) """
    @property
    def OldKey(self) -> SfcKey:
        """ Get: OldKey(self: SfcAfterObjectRenamedEventArgs) -> SfcKey """
        ...

    @property
    def OldUrn(self) -> Urn:
        """ Get: OldUrn(self: SfcAfterObjectRenamedEventArgs) -> Urn """
        ...



class SfcApplication: # skipped bases: <type 'object'>, <type 'object'>
    """ SfcApplication() """
    def SfcAfterObjectMovedEventHandler(self, *args): #cannot find CLR method
        """ SfcAfterObjectMovedEventHandler(object: object, method: IntPtr) """
        ...

    def SfcAfterObjectRenamedEventHandler(self, *args): #cannot find CLR method
        """ SfcAfterObjectRenamedEventHandler(object: object, method: IntPtr) """
        ...

    def SfcBeforeObjectMovedEventHandler(self, *args): #cannot find CLR method
        """ SfcBeforeObjectMovedEventHandler(object: object, method: IntPtr) """
        ...

    def SfcBeforeObjectRenamedEventHandler(self, *args): #cannot find CLR method
        """ SfcBeforeObjectRenamedEventHandler(object: object, method: IntPtr) """
        ...

    def SfcObjectAlteredEventHandler(self, *args): #cannot find CLR method
        """ SfcObjectAlteredEventHandler(object: object, method: IntPtr) """
        ...

    def SfcObjectCreatedEventHandler(self, *args): #cannot find CLR method
        """ SfcObjectCreatedEventHandler(object: object, method: IntPtr) """
        ...

    def SfcObjectDroppedEventHandler(self, *args): #cannot find CLR method
        """ SfcObjectDroppedEventHandler(object: object, method: IntPtr) """
        ...

    Events: SfcApplicationEvents = ...


class SfcApplicationEvents: # skipped bases: <type 'object'>, <type 'object'>
    """ SfcApplicationEvents() """
    def OnAfterObjectMoved(self, obj:SfcInstance, e:SfcAfterObjectMovedEventArgs): # -> 
        """ OnAfterObjectMoved(self: SfcApplicationEvents, obj: SfcInstance, e: SfcAfterObjectMovedEventArgs) """
        ...

    def OnAfterObjectRenamed(self, obj:SfcInstance, e:SfcAfterObjectRenamedEventArgs): # -> 
        """ OnAfterObjectRenamed(self: SfcApplicationEvents, obj: SfcInstance, e: SfcAfterObjectRenamedEventArgs) """
        ...

    def OnBeforeObjectMoved(self, obj:SfcInstance, e:SfcBeforeObjectMovedEventArgs): # -> 
        """ OnBeforeObjectMoved(self: SfcApplicationEvents, obj: SfcInstance, e: SfcBeforeObjectMovedEventArgs) """
        ...

    def OnBeforeObjectRenamed(self, obj:SfcInstance, e:SfcBeforeObjectRenamedEventArgs): # -> 
        """ OnBeforeObjectRenamed(self: SfcApplicationEvents, obj: SfcInstance, e: SfcBeforeObjectRenamedEventArgs) """
        ...

    def OnObjectAltered(self, obj:SfcInstance, e:SfcObjectAlteredEventArgs): # -> 
        """ OnObjectAltered(self: SfcApplicationEvents, obj: SfcInstance, e: SfcObjectAlteredEventArgs) """
        ...

    def OnObjectCreated(self, obj:SfcInstance, e:SfcObjectCreatedEventArgs): # -> 
        """ OnObjectCreated(self: SfcApplicationEvents, obj: SfcInstance, e: SfcObjectCreatedEventArgs) """
        ...

    def OnObjectDropped(self, obj:SfcInstance, e:SfcObjectDroppedEventArgs): # -> 
        """ OnObjectDropped(self: SfcApplicationEvents, obj: SfcInstance, e: SfcObjectDroppedEventArgs) """
        ...

    AfterObjectMoved = ...
    AfterObjectRenamed = ...
    BeforeObjectMoved = ...
    BeforeObjectRenamed = ...
    ObjectAltered = ...
    ObjectCreated = ...
    ObjectDropped = ...


class SfcBeforeObjectMovedEventArgs(SfcEventArgs): # skipped bases: <type 'object'>
    """ SfcBeforeObjectMovedEventArgs(urn: Urn, instance: SfcInstance, newUrn: Urn, newParent: SfcInstance) """
    @property
    def NewParent(self) -> SfcInstance:
        """ Get: NewParent(self: SfcBeforeObjectMovedEventArgs) -> SfcInstance """
        ...

    @property
    def NewUrn(self) -> Urn:
        """ Get: NewUrn(self: SfcBeforeObjectMovedEventArgs) -> Urn """
        ...



class SfcBeforeObjectRenamedEventArgs(SfcEventArgs): # skipped bases: <type 'object'>
    """ SfcBeforeObjectRenamedEventArgs(urn: Urn, instance: SfcInstance, newUrn: Urn, newKey: SfcKey) """
    @property
    def NewKey(self) -> SfcKey:
        """ Get: NewKey(self: SfcBeforeObjectRenamedEventArgs) -> SfcKey """
        ...

    @property
    def NewUrn(self) -> Urn:
        """ Get: NewUrn(self: SfcBeforeObjectRenamedEventArgs) -> Urn """
        ...



class SfcCollatedDictionaryCollection(SfcCollection, IComparer): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[T]'>, <type 'ICollection[T]'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Ascending(self) -> bool:
        """
        Get: Ascending(self: SfcCollatedDictionaryCollection[T, K, ParentT]) -> bool
        Set: Ascending(self: SfcCollatedDictionaryCollection[T, K, ParentT]) = value
        """
        ...

    @property
    def CultureInfo(self):
        ...

    @property
    def IgnoreCase(self):
        ...


    def ResetInnerCollection(self, *args): #cannot find CLR method
        """ ResetInnerCollection(self: SfcCollatedDictionaryCollection[T, K, ParentT]) """
        ...

    def TryGetValue(self, key, obj):
        """ no doc """
        ...


class SfcCollection(IListSource, ISfcCollection, ICollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def AddImpl(self, *args): #cannot find CLR method
        """ AddImpl(self: SfcCollection[T, K, ParentT], obj: T) """
        ...

    def CreateAndInitializeChildObject(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def EnsureCollectionInitialized(self, *args): #cannot find CLR method
        """ EnsureCollectionInitialized(self: SfcCollection[T, K, ParentT]) """
        ...

    def GetElementFactoryImpl(self, *args): #cannot find CLR method
        """ GetElementFactoryImpl(self: SfcCollection[T, K, ParentT]) -> SfcObjectFactory """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SfcCollection[T, K, ParentT]) -> IEnumerator[T] """
        ...

    def GetExistingObjectByKey(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def InitInnerCollection(self, *args): #cannot find CLR method
        """ InitInnerCollection(self: SfcCollection[T, K, ParentT]) """
        ...

    def Refresh(self, refreshChildObjects:bool = ...): # -> 
        """ Refresh(self: SfcCollection[T, K, ParentT])Refresh(self: SfcCollection[T, K, ParentT], refreshChildObjects: bool) """
        ...

    def RemoveImpl(self, *args): #cannot find CLR method
        """ RemoveImpl(self: SfcCollection[T, K, ParentT], obj: T) -> bool """
        ...

    def RemoveInternal(self, *args): #cannot find CLR method
        """ RemoveInternal(self: SfcCollection[T, K, ParentT], obj: T) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class SfcCollectionInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ SfcCollectionInfo(displayName: str, collection: object) """
    @property
    def Collection(self) -> object:
        """ Get: Collection(self: SfcCollectionInfo) -> object """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: SfcCollectionInfo) -> str """
        ...



class SfcConnection(ISfcConnection): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ConnectionType(self) -> ServerType:
        """ Get: ConnectionType(self: SfcConnection) -> ServerType """
        ...

    @property
    def ConnectTimeout(self) -> int:
        """
        Get: ConnectTimeout(self: SfcConnection) -> int
        Set: ConnectTimeout(self: SfcConnection) = value
        """
        ...

    @property
    def StatementTimeout(self) -> int:
        """
        Get: StatementTimeout(self: SfcConnection) -> int
        Set: StatementTimeout(self: SfcConnection) = value
        """
        ...


    def Equals(self, *__args:SfcConnection) -> bool:
        """ Equals(self: SfcConnection, connection: SfcConnection) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SfcConnection) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...


class SfcConnectionContext: # skipped bases: <type 'object'>, <type 'object'>
    """ SfcConnectionContext(domain: ISfcHasConnection) """
    @property
    def Mode(self) -> SfcConnectionContextMode:
        """
        Get: Mode(self: SfcConnectionContext) -> SfcConnectionContextMode
        Set: Mode(self: SfcConnectionContext) = value
        """
        ...


    def FlushActionLog(self): # -> 
        """ FlushActionLog(self: SfcConnectionContext) """
        ...


class SfcConnectionContextMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SfcConnectionContextMode, values: NonTransactedBatch (3), Offline (0), Online (1), TransactedBatch (2) """
    NonTransactedBatch: SfcConnectionContextMode = ...
    Offline: SfcConnectionContextMode = ...
    Online: SfcConnectionContextMode = ...
    TransactedBatch: SfcConnectionContextMode = ...
    value__ = ...


class SfcException(SqlServerManagementException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def ProdVer(self):
        ...


    def SetHelpContext(self, *args): #cannot find CLR method
        """ SetHelpContext(self: SfcException, resource: str) -> SfcException """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    SerializeObjectState = ...


class SfcCRUDOperationFailedException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcCRUDOperationFailedException()
    SfcCRUDOperationFailedException(message: str)
    SfcCRUDOperationFailedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcDependencyAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SfcDependencyAction, values: Alter (4), Copy (9), Create (2), Diff (8), Drop (3), Merge (7), Move (6), Rename (5), Serialize (1), Unknown (0) """
    Alter: SfcDependencyAction = ...
    Copy: SfcDependencyAction = ...
    Create: SfcDependencyAction = ...
    Diff: SfcDependencyAction = ...
    Drop: SfcDependencyAction = ...
    Merge: SfcDependencyAction = ...
    Move: SfcDependencyAction = ...
    Rename: SfcDependencyAction = ...
    Serialize: SfcDependencyAction = ...
    Unknown: SfcDependencyAction = ...
    value__ = ...


class SfcDependencyDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SfcDependencyDirection, values: Inbound (1), None (0), Outbound (2) """
    Inbound: SfcDependencyDirection = ...
    Outbound: SfcDependencyDirection = ...
    value__ = ...


class SfcDependencyDiscoveryMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SfcDependencyDiscoveryMode, values: Children (0), Full (1), Propagate (2), UsedBy (3), Uses (4) """
    Children: SfcDependencyDiscoveryMode = ...
    Full: SfcDependencyDiscoveryMode = ...
    Propagate: SfcDependencyDiscoveryMode = ...
    UsedBy: SfcDependencyDiscoveryMode = ...
    Uses: SfcDependencyDiscoveryMode = ...
    value__ = ...


class SfcDependencyEngine(IDisposable, ISfcDependencyDiscoveryObjectSink): # skipped bases: <type 'object'>
    """ SfcDependencyEngine(mode: SfcDependencyDiscoveryMode, action: SfcDependencyAction) """
    def DependencyListEnumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def DependencyNodeEnumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def DependencyTreeEnumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Discover(self): # -> 
        """ Discover(self: SfcDependencyEngine) """
        ...

    def GetListEnumerator(self): # -> DependencyListEnumerator
        """ GetListEnumerator(self: SfcDependencyEngine) -> DependencyListEnumerator """
        ...

    def GetTreeEnumerator(self): # -> DependencyTreeEnumerator
        """ GetTreeEnumerator(self: SfcDependencyEngine) -> DependencyTreeEnumerator """
        ...



class SfcDependencyNode: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AncestorCount(self) -> int:
        """ Get: AncestorCount(self: SfcDependencyNode) -> int """
        ...

    @property
    def Ancestors(self) -> IEnumerable:
        """ Get: Ancestors(self: SfcDependencyNode) -> IEnumerable[SfcDependencyNode] """
        ...

    @property
    def ChildCount(self) -> int:
        """ Get: ChildCount(self: SfcDependencyNode) -> int """
        ...

    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: SfcDependencyNode) -> IEnumerable[SfcDependencyNode] """
        ...

    @property
    def Discovered(self) -> bool:
        """
        Get: Discovered(self: SfcDependencyNode) -> bool
        Set: Discovered(self: SfcDependencyNode) = value
        """
        ...

    @property
    def Instance(self) -> SfcInstance:
        """ Get: Instance(self: SfcDependencyNode) -> SfcInstance """
        ...


    def IsPhysicalAncestor(self, index:int) -> bool:
        """ IsPhysicalAncestor(self: SfcDependencyNode, index: int) -> bool """
        ...

    def IsPhysicalChild(self, index:int) -> bool:
        """ IsPhysicalChild(self: SfcDependencyNode, index: int) -> bool """
        ...


class SfcDesignModeException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcDesignModeException()
    SfcDesignModeException(message: str, innerException: Exception)
    SfcDesignModeException(message: str)
    """
    SerializeObjectState = ...


class SfcDictionaryCollection(SfcCollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'IEnumerable'>, <type 'ICollection[T]'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def TryGetValue(self, key, obj):
        """ no doc """
        ...


class SfcDomainInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AssemblyStrongName(self) -> str:
        """ Get: AssemblyStrongName(self: SfcDomainInfo) -> str """
        ...

    @property
    def DomainNamespace(self) -> str:
        """ Get: DomainNamespace(self: SfcDomainInfo) -> str """
        ...

    @property
    def IsAssemblyInGAC(self) -> bool:
        """ Get: IsAssemblyInGAC(self: SfcDomainInfo) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: SfcDomainInfo) -> str """
        ...

    @property
    def NamespaceQualifier(self) -> str:
        """ Get: NamespaceQualifier(self: SfcDomainInfo) -> str """
        ...

    @property
    def PSDriveName(self) -> str:
        """ Get: PSDriveName(self: SfcDomainInfo) -> str """
        ...

    @property
    def RootType(self) -> Type:
        """ Get: RootType(self: SfcDomainInfo) -> Type """
        ...

    @property
    def RootTypeFullName(self) -> str:
        """ Get: RootTypeFullName(self: SfcDomainInfo) -> str """
        ...


    def GetLogicalVersion(self, instance:object) -> int:
        """ GetLogicalVersion(self: SfcDomainInfo, instance: object) -> int """
        ...


class SfcDomainInfoCollection(ReadOnlyCollection): # skipped bases: <type 'IReadOnlyList[SfcDomainInfo]'>, <type 'IList[SfcDomainInfo]'>, <type 'ICollection[SfcDomainInfo]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyCollection[SfcDomainInfo]'>, <type 'IEnumerable[SfcDomainInfo]'>, <type 'ICollection'>, <type 'object'>
    """ SfcDomainInfoCollection(list: IList[SfcDomainInfo]) """
    def GetDomainForNamespaceQualifier(self, namespaceQualifier:str) -> SfcDomainInfo:
        """ GetDomainForNamespaceQualifier(self: SfcDomainInfoCollection, namespaceQualifier: str) -> SfcDomainInfo """
        ...


class SfcEmptyXmlException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcEmptyXmlException()
    SfcEmptyXmlException(message: str)
    SfcEmptyXmlException(message: str, innerException: Exception)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: SfcEmptyXmlException) -> str """
        ...


    SerializeObjectState = ...


class SfcInstance: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AbstractIdentityKey(self):
        ...

    @property
    def Metadata(self) -> SfcMetadataDiscovery:
        """ Get: Metadata(self: SfcInstance) -> SfcMetadataDiscovery """
        ...

    @property
    def Parent(self) -> SfcInstance:
        """ Get: Parent(self: SfcInstance) -> SfcInstance """
        ...

    @property
    def Properties(self) -> SfcPropertyCollection:
        """ Get: Properties(self: SfcInstance) -> SfcPropertyCollection """
        ...

    @property
    def PropertyStorageProvider(self):
        ...

    @property
    def State(self):
        ...

    @property
    def Urn(self) -> Urn:
        """ Get: Urn(self: SfcInstance) -> Urn """
        ...


    def AlterImpl(self, *args): #cannot find CLR method
        """ AlterImpl(self: SfcInstance) """
        ...

    def CheckObjectCreated(self, *args): #cannot find CLR method
        """ CheckObjectCreated(self: SfcInstance) """
        ...

    def CheckObjectState(self, *args): #cannot find CLR method
        """ CheckObjectState(self: SfcInstance) """
        ...

    def CreateIdentityKey(self, *args): #cannot find CLR method
        """ CreateIdentityKey(self: SfcInstance) -> SfcKey """
        ...

    def CreateImpl(self, *args): #cannot find CLR method
        """ CreateImpl(self: SfcInstance) """
        ...

    def Discover(self, sink:ISfcDependencyDiscoveryObjectSink): # -> 
        """ Discover(self: SfcInstance, sink: ISfcDependencyDiscoveryObjectSink) """
        ...

    def DropImpl(self, *args): #cannot find CLR method
        """ DropImpl(self: SfcInstance) """
        ...

    def GetChildCollection(self, *args): #cannot find CLR method
        """ GetChildCollection(self: SfcInstance, elementType: str) -> ISfcCollection """
        ...

    def GetDomain(self) -> ISfcDomain:
        """ GetDomain(self: SfcInstance) -> ISfcDomain """
        ...

    def GetPropertySet(self) -> ISfcPropertySet:
        """ GetPropertySet(self: SfcInstance) -> ISfcPropertySet """
        ...

    def GetTypeMetadataImpl(self, *args): #cannot find CLR method
        """ GetTypeMetadataImpl(self: SfcInstance) -> SfcTypeMetadata """
        ...

    def InitializeUIPropertyState(self, *args): #cannot find CLR method
        """ InitializeUIPropertyState(self: SfcInstance) """
        ...

    def MarkForDropImpl(self, *args): #cannot find CLR method
        """ MarkForDropImpl(self: SfcInstance, dropOnAlter: bool) """
        ...

    def MarkRootAsConnected(self, *args): #cannot find CLR method
        """ MarkRootAsConnected(self: SfcInstance) """
        ...

    def MoveImpl(self, *args): #cannot find CLR method
        """ MoveImpl(self: SfcInstance, newParent: SfcInstance) """
        ...

    def OnPropertyMetadataChanges(self, *args): #cannot find CLR method
        """ OnPropertyMetadataChanges(self: SfcInstance, args: SfcPropertyMetadataChangedEventArgs) """
        ...

    def OnPropertyValueChanges(self, *args): #cannot find CLR method
        """ OnPropertyValueChanges(self: SfcInstance, args: PropertyChangedEventArgs) """
        ...

    def PostAlter(self, *args): #cannot find CLR method
        """ PostAlter(self: SfcInstance, executionResult: object) """
        ...

    def PostCreate(self, *args): #cannot find CLR method
        """ PostCreate(self: SfcInstance, executionResult: object) """
        ...

    def PostDrop(self, *args): #cannot find CLR method
        """ PostDrop(self: SfcInstance, executionResult: object) """
        ...

    def PostMove(self, *args): #cannot find CLR method
        """ PostMove(self: SfcInstance, executionResult: object) """
        ...

    def PostRename(self, *args): #cannot find CLR method
        """ PostRename(self: SfcInstance, executionResult: object) """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: SfcInstance) """
        ...

    def RenameImpl(self, *args): #cannot find CLR method
        """ RenameImpl(self: SfcInstance, newKey: SfcKey) """
        ...

    def ResetKey(self, *args): #cannot find CLR method
        """ ResetKey(self: SfcInstance) """
        ...

    def Serialize(self, writer:XmlWriter): # -> 
        """ Serialize(self: SfcInstance, writer: XmlWriter) """
        ...

    def ToString(self) -> str:
        """ ToString(self: SfcInstance) -> str """
        ...

    def UpdateUIPropertyState(self, *args): #cannot find CLR method
        """ UpdateUIPropertyState(self: SfcInstance) """
        ...

    def Validate(self, *args): #cannot find CLR method
        """ Validate(self: SfcInstance) -> ValidationState """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    propertyChanged = ...
    PropertyChanged = ...
    PropertyMetadataChanged = ...
    propertyMetadataChanged = ...


class SfcInstanceSerializedData: # skipped bases: <type 'object'>, <type 'object'>
    """ SfcInstanceSerializedData(serializedType: SfcSerializedTypes, name: str, type: str, value: object) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: SfcInstanceSerializedData) -> str """
        ...

    @property
    def SerializedType(self) -> SfcSerializedTypes:
        """ Get: SerializedType(self: SfcInstanceSerializedData) -> SfcSerializedTypes """
        ...

    @property
    def Type(self) -> str:
        """ Get: Type(self: SfcInstanceSerializedData) -> str """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: SfcInstanceSerializedData) -> object """
        ...



class SfcInvalidArgumentException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcInvalidArgumentException()
    SfcInvalidArgumentException(message: str)
    SfcInvalidArgumentException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcInvalidConnectionContextModeChangeException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcInvalidConnectionContextModeChangeException()
    SfcInvalidConnectionContextModeChangeException(fromMode: str, toMode: str)
    SfcInvalidConnectionContextModeChangeException(fromMode: str, toMode: str, innerException: Exception)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: SfcInvalidConnectionContextModeChangeException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: SfcInvalidConnectionContextModeChangeException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class SfcInvalidKeyChainException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcInvalidKeyChainException()
    SfcInvalidKeyChainException(message: str)
    SfcInvalidKeyChainException(message: str, innerException: Exception)
    SfcInvalidKeyChainException(innerException: Exception)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: SfcInvalidKeyChainException) -> str """
        ...


    SerializeObjectState = ...


class SfcInvalidKeyException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcInvalidKeyException()
    SfcInvalidKeyException(keyName: str)
    SfcInvalidKeyException(keyName: str, innerException: Exception)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: SfcInvalidKeyException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: SfcInvalidKeyException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class SfcInvalidMoveException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcInvalidMoveException()
    SfcInvalidMoveException(message: str)
    SfcInvalidMoveException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcInvalidQueryExpressionException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcInvalidQueryExpressionException()
    SfcInvalidQueryExpressionException(message: str)
    SfcInvalidQueryExpressionException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcInvalidRenameException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcInvalidRenameException()
    SfcInvalidRenameException(message: str)
    SfcInvalidRenameException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcInvalidStateException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcInvalidStateException()
    SfcInvalidStateException(message: str)
    SfcInvalidStateException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcInvalidStreamException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcInvalidStreamException()
    SfcInvalidStreamException(message: str)
    SfcInvalidStreamException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcInvalidXmlParentTypeException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcInvalidXmlParentTypeException()
    SfcInvalidXmlParentTypeException(message: str)
    SfcInvalidXmlParentTypeException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcListCollection(SfcCollection): # skipped bases: <type 'IEnumerable[T]'>, <type 'ICollection[T]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def GetInternalCollectionImpl(self, *args): #cannot find CLR method
        """ GetInternalCollectionImpl(self: SfcListCollection[T, K, ParentT]) -> ICollection[T] """
        ...


class SfcMetadataException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcMetadataException()
    SfcMetadataException(message: str)
    SfcMetadataException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcMissingParentException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcMissingParentException()
    SfcMissingParentException(message: str)
    SfcMissingParentException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcNonSerializablePropertyException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcNonSerializablePropertyException()
    SfcNonSerializablePropertyException(message: str)
    SfcNonSerializablePropertyException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcNonSerializableTypeException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcNonSerializableTypeException()
    SfcNonSerializableTypeException(message: str)
    SfcNonSerializableTypeException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcObjectAlteredEventArgs(SfcEventArgs): # skipped bases: <type 'object'>
    """ SfcObjectAlteredEventArgs(urn: Urn, instance: SfcInstance) """
    pass

class SfcObjectCreatedEventArgs(SfcEventArgs): # skipped bases: <type 'object'>
    """ SfcObjectCreatedEventArgs(urn: Urn, instance: SfcInstance) """
    pass

class SfcObjectDroppedEventArgs(SfcEventArgs): # skipped bases: <type 'object'>
    """ SfcObjectDroppedEventArgs(urn: Urn, instance: SfcInstance) """
    pass

class SfcObjectExtender(ISfcPropertyProvider): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'object'>
    """
    SfcObjectExtender[TSfcInstance]()
    SfcObjectExtender[TSfcInstance](parent: TSfcInstance)
    """
    @property
    def Parent(self):
        ...


    def GetParentSfcPropertySet(self, *args): #cannot find CLR method
        """ GetParentSfcPropertySet(self: SfcObjectExtender[TSfcInstance]) -> ISfcPropertySet """
        ...

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """ OnPropertyChanged(self: SfcObjectExtender[TSfcInstance], propertyName: str) """
        ...

    def OnPropertyMetadataChanged(self, *args): #cannot find CLR method
        """ OnPropertyMetadataChanged(self: SfcObjectExtender[TSfcInstance], propertyName: str) """
        ...

    def parent_PropertyChanged(self, *args): #cannot find CLR method
        """ parent_PropertyChanged(self: SfcObjectExtender[TSfcInstance], sender: object, e: PropertyChangedEventArgs) """
        ...

    def parent_PropertyMetadataChanged(self, *args): #cannot find CLR method
        """ parent_PropertyMetadataChanged(self: SfcObjectExtender[TSfcInstance], sender: object, e: SfcPropertyMetadataChangedEventArgs) """
        ...

    def RegisterParentProperty(self, *args): #cannot find CLR method
        """ RegisterParentProperty(self: SfcObjectExtender[TSfcInstance], propertyInfo: PropertyInfo) """
        ...

    def RegisterProperty(self, *args): #cannot find CLR method
        """ RegisterProperty(self: SfcObjectExtender[TSfcInstance], propertyInfo: PropertyInfo)RegisterProperty(self: SfcObjectExtender[TSfcInstance], propertyInfo: PropertyInfo, parentPropertyName: str) """
        ...

    PropertyChanged = ...
    PropertyMetadataChanged = ...


class SfcObjectFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateImpl(self, *args): #cannot find CLR method
        """ CreateImpl(self: SfcObjectFactory) -> SfcInstance """
        ...


class SfcObjectInitializationException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcObjectInitializationException()
    SfcObjectInitializationException(keyName: str)
    SfcObjectInitializationException(keyName: str, innerException: Exception)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: SfcObjectInitializationException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: SfcObjectInitializationException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class SfcObjectNotScriptableException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcObjectNotScriptableException()
    SfcObjectNotScriptableException(message: str)
    SfcObjectNotScriptableException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcObjectQuery: # skipped bases: <type 'object'>, <type 'object'>
    """
    SfcObjectQuery(domain: ISfcDomain, activeQueriesMode: SfcObjectQueryMode)
    SfcObjectQuery(domain: ISfcDomain)
    SfcObjectQuery(root: IAlienRoot)
    """
    @property
    def ActiveQueriesMode(self) -> SfcObjectQueryMode:
        """
        Get: ActiveQueriesMode(self: SfcObjectQuery) -> SfcObjectQueryMode
        Set: ActiveQueriesMode(self: SfcObjectQuery) = value
        """
        ...

    @property
    def SfcQueryExpression(self) -> SfcQueryExpression:
        """ Get: SfcQueryExpression(self: SfcObjectQuery) -> SfcQueryExpression """
        ...


    def ExecuteDataTable(self, query:SfcQueryExpression, fields:Array, orderByFields:Array) -> DataTable:
        """ ExecuteDataTable(self: SfcObjectQuery, query: SfcQueryExpression, fields: Array[str], orderByFields: Array[OrderBy]) -> DataTable """
        ...

    def ExecuteIterator(self, query:SfcQueryExpression, fields:Array, orderByFields:Array) -> IEnumerable:
        """ ExecuteIterator(self: SfcObjectQuery, query: SfcQueryExpression, fields: Array[str], orderByFields: Array[OrderBy]) -> IEnumerable """
        ...


class SfcObjectQueryMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SfcObjectQueryMode, values: CachedQuery (0), MultipleActiveQueries (2), SingleActiveQuery (1) """
    CachedQuery: SfcObjectQueryMode = ...
    MultipleActiveQueries: SfcObjectQueryMode = ...
    SingleActiveQuery: SfcObjectQueryMode = ...
    value__ = ...


class SfcObjectState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SfcObjectState, values: Dropped (3), Existing (2), None (0), Pending (1), Recreate (5), ToBeDropped (4) """
    Dropped: SfcObjectState = ...
    Existing: SfcObjectState = ...
    Pending: SfcObjectState = ...
    Recreate: SfcObjectState = ...
    ToBeDropped: SfcObjectState = ...
    value__ = ...


class SfcPathConversionException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcPathConversionException()
    SfcPathConversionException(message: str, innerException: Exception)
    SfcPathConversionException(message: str)
    """
    SerializeObjectState = ...


class SfcProperty(ISfcProperty): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Computed(self) -> bool:
        """ Get: Computed(self: SfcProperty) -> bool """
        ...

    @property
    def Encrypted(self) -> bool:
        """ Get: Encrypted(self: SfcProperty) -> bool """
        ...

    @property
    def Expensive(self) -> bool:
        """ Get: Expensive(self: SfcProperty) -> bool """
        ...

    @property
    def IdentityKey(self) -> bool:
        """ Get: IdentityKey(self: SfcProperty) -> bool """
        ...

    @property
    def IsAvailable(self) -> bool:
        """ Get: IsAvailable(self: SfcProperty) -> bool """
        ...

    @property
    def Readable(self) -> bool:
        """ Get: Readable(self: SfcProperty) -> bool """
        ...

    @property
    def Retrieved(self) -> bool:
        """ Get: Retrieved(self: SfcProperty) -> bool """
        ...

    @property
    def SqlAzureDatabase(self) -> bool:
        """ Get: SqlAzureDatabase(self: SfcProperty) -> bool """
        ...

    @property
    def Standalone(self) -> bool:
        """ Get: Standalone(self: SfcProperty) -> bool """
        ...


    def CompareTo(self, obj:object) -> int:
        """ CompareTo(self: SfcProperty, obj: object) -> int """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: SfcProperty, o: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SfcProperty) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: SfcProperty) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __gt__(self, *args): #cannot find CLR method
        ...

    def __lt__(self, *args): #cannot find CLR method
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SfcPropertyCollection(ISfcPropertySet, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SfcPropertyCollection) -> IEnumerator """
        ...

    def IsAvailable(self, propertyName:str) -> bool:
        """ IsAvailable(self: SfcPropertyCollection, propertyName: str) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class SfcPropertyMetadataChangedEventArgs(PropertyChangedEventArgs): # skipped bases: <type 'object'>
    """ SfcPropertyMetadataChangedEventArgs(propertyName: str) """
    pass

class SfcPropertyNotSetException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcPropertyNotSetException()
    SfcPropertyNotSetException(propertyName: str)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: SfcPropertyNotSetException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: SfcPropertyNotSetException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class SfcPropertyReadOnlyException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcPropertyReadOnlyException()
    SfcPropertyReadOnlyException(propertyName: str)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: SfcPropertyReadOnlyException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: SfcPropertyReadOnlyException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class SfcProxyInstance(SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    SfcProxyInstance[K, T, TRef]()
    SfcProxyInstance[K, T, TRef](reference: TRef)
    """
    @property
    def Reference(self):
        ...


    def GetReferenceImpl(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def __new__(cls, reference = ...) -> Self: # Not found arg types: {'reference': 'TRef'}
        """
        __new__(cls: type)
        __new__(cls: type, reference: TRef)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class SfcQueryConnectionUnavailableException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcQueryConnectionUnavailableException()
    SfcQueryConnectionUnavailableException(message: str)
    SfcQueryConnectionUnavailableException(message: str, innerException: Exception)
    """
    @property
    def Message(self) -> str:
        """ Get: Message(self: SfcQueryConnectionUnavailableException) -> str """
        ...


    SerializeObjectState = ...


class SfcQueryExpression(IXmlSerializable): # skipped bases: <type 'object'>
    """
    SfcQueryExpression()
    SfcQueryExpression(path: str)
    """
    @property
    def Expression(self) -> XPathExpression:
        """ Get: Expression(self: SfcQueryExpression) -> XPathExpression """
        ...

    @property
    def ExpressionSkeleton(self) -> str:
        """ Get: ExpressionSkeleton(self: SfcQueryExpression) -> str """
        ...


    def GetLeafTypeName(self) -> str:
        """ GetLeafTypeName(self: SfcQueryExpression) -> str """
        ...

    def SetExpression(self, expression:XPathExpression): # -> 
        """ SetExpression(self: SfcQueryExpression, expression: XPathExpression) """
        ...

    def ToString(self) -> str:
        """ ToString(self: SfcQueryExpression) -> str """
        ...


class SfcReferenceCollection(IReadOnlyDictionary, IListSource): # skipped bases: <type 'IReadOnlyCollection[T]'>, <type 'IReadOnlyCollection'>, <type 'IEnumerable'>, <type 'IEnumerable[T]'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: SfcReferenceCollection[K, T, S]) -> int """
        ...


    def Contains(self, item) -> bool: # Not found arg types: {'item': 'T'}
        """ Contains(self: SfcReferenceCollection[K, T, S], item: T) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: SfcReferenceCollection[K, T, S], array: Array[T], arrayIndex: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SfcReferenceCollection[K, T, S]) -> IEnumerator """
        ...

    def GetKeyFromValue(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: SfcReferenceCollection[K, T, S]) """
        ...


class SfcRegistration: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Domains(self) -> SfcDomainInfoCollection:
        """ Get: Domains() -> SfcDomainInfoCollection """
        ...


    @staticmethod
    def CreateObject(fullTypeName:str) -> object:
        """ CreateObject(fullTypeName: str) -> object """
        ...

    @staticmethod
    def GetObjectTypeFromFullName(fullTypeName:str, ignoreCase:bool = ...) -> Type:
        """
        GetObjectTypeFromFullName(fullTypeName: str) -> Type
        GetObjectTypeFromFullName(fullTypeName: str, ignoreCase: bool) -> Type
        """
        ...

    @staticmethod
    def GetRegisteredDomainForType(*__args:str) -> str:
        """
        GetRegisteredDomainForType(fullTypeName: str) -> str
        GetRegisteredDomainForType(type: Type) -> SfcDomainInfo
        GetRegisteredDomainForType(fullTypeName: str, throwOnUnregisteredDomain: bool) -> str
        """
        ...

    @staticmethod
    def TryGetObjectTypeFromFullName(fullTypeName:str) -> Type:
        """ TryGetObjectTypeFromFullName(fullTypeName: str) -> Type """
        ...



class SfcSecureString: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def EscapeBracket(value:str) -> str:
        """ EscapeBracket(value: str) -> str """
        ...

    @staticmethod
    def EscapeSquote(value:str) -> str:
        """ EscapeSquote(value: str) -> str """
        ...

    @staticmethod
    def SmlEscape(originalString:str) -> str:
        """ SmlEscape(originalString: str) -> str """
        ...

    @staticmethod
    def SmlUnEscape(escapedString:str) -> str:
        """ SmlUnEscape(escapedString: str) -> str """
        ...

    @staticmethod
    def XmlEscape(originalString:str) -> str:
        """ XmlEscape(originalString: str) -> str """
        ...

    @staticmethod
    def XmlUnEscape(escapedString:str) -> str:
        """ XmlUnEscape(escapedString: str) -> str """
        ...

    __all__: list = ...


class SfcSecurityException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcSecurityException()
    SfcSecurityException(message: str, innerException: Exception)
    SfcSecurityException(message: str)
    """
    SerializeObjectState = ...


class SfcSerializationException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcSerializationException()
    SfcSerializationException(message: str)
    SfcSerializationException(message: str, innerException: Exception)
    SfcSerializationException(innerException: Exception)
    """
    SerializeObjectState = ...


class SfcSerializedTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SfcSerializedTypes, values: Collection (3), None (0), Parent (2), Property (1), Reference (4) """
    Collection: SfcSerializedTypes = ...
    Parent: SfcSerializedTypes = ...
    Property: SfcSerializedTypes = ...
    Reference: SfcSerializedTypes = ...
    value__ = ...


class SfcSerializer: # skipped bases: <type 'object'>, <type 'object'>
    """ SfcSerializer() """
    @property
    def UnParentedReferences(self) -> List:
        """ Get: UnParentedReferences(self: SfcSerializer) -> List[object] """
        ...


    def Deserialize(self, xmlReader:XmlReader, state:SfcObjectState = ...) -> object:
        """
        Deserialize(self: SfcSerializer, xmlReader: XmlReader) -> object
        Deserialize(self: SfcSerializer, xmlReader: XmlReader, state: SfcObjectState) -> object
        """
        ...

    def Serialize(self, instance:object): # -> 
        """ Serialize(self: SfcSerializer, instance: object) """
        ...

    def Write(self, xmlWriter:XmlWriter): # -> 
        """ Write(self: SfcSerializer, xmlWriter: XmlWriter) """
        ...

    FilterPropertyHandler = ...


class SfcSimpleNodeFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ SfcSimpleNodeFactory() """
    @property
    def Factory(self) -> SfcSimpleNodeFactory:
        """ Get: Factory() -> SfcSimpleNodeFactory """
        ...


    def GetSimpleNode(self, node:object, adapter:SimpleNodeAdapter = ...) -> ISfcSimpleNode:
        """
        GetSimpleNode(self: SfcSimpleNodeFactory, node: object) -> ISfcSimpleNode
        GetSimpleNode(self: SfcSimpleNodeFactory, node: object, adapter: SimpleNodeAdapter) -> ISfcSimpleNode
        """
        ...

    def IsSupported(self, node:object) -> bool:
        """ IsSupported(self: SfcSimpleNodeFactory, node: object) -> bool """
        ...



class SfcSqlCeNotInstalledException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcSqlCeNotInstalledException()
    SfcSqlCeNotInstalledException(message: str)
    SfcSqlCeNotInstalledException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcSqlPathUtilities: # skipped bases: <type 'object'>, <type 'object'>
    """ SfcSqlPathUtilities() """
    @staticmethod
    def ConvertUrnToPath(urn:Urn) -> str:
        """ ConvertUrnToPath(urn: Urn) -> str """
        ...

    @staticmethod
    def DecodeSqlName(*__args:str) -> str:
        """
        DecodeSqlName(name: str) -> str
        DecodeSqlName(names: Array[str]) -> Array[str]
        """
        ...

    @staticmethod
    def EncodeSqlName(name:str) -> str:
        """ EncodeSqlName(name: str) -> str """
        ...


class SfcTSqlExecutionEngine(ISfcExecutionEngine): # skipped bases: <type 'object'>
    """ SfcTSqlExecutionEngine(connection: ServerConnection) """
    pass

class SfcTSqlExecutor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ExecuteNonQuery(connection:ServerConnection, script:str): # -> 
        """ ExecuteNonQuery(connection: ServerConnection, script: str) """
        ...

    @staticmethod
    def ExecuteScalar(connection:ServerConnection, script:str) -> object:
        """ ExecuteScalar(connection: ServerConnection, script: str) -> object """
        ...

    def ExecutionMode(self, *args): #cannot find CLR method
        """ enum ExecutionMode, values: NonQuery (1), Scalar (0), WithResults (2) """
        ...



class SfcTsqlProcFormatter: # skipped bases: <type 'object'>, <type 'object'>
    """ SfcTsqlProcFormatter() """
    @property
    def Arguments(self) -> List:
        """ Get: Arguments(self: SfcTsqlProcFormatter) -> List[SprocArg] """
        ...

    @property
    def Procedure(self) -> str:
        """
        Get: Procedure(self: SfcTsqlProcFormatter) -> str
        Set: Procedure(self: SfcTsqlProcFormatter) = value
        """
        ...


    @staticmethod
    def EscapeString(value:str, charToEscape:Char) -> str:
        """ EscapeString(value: str, charToEscape: Char) -> str """
        ...

    def GenerateScript(self, sfcObject:SfcInstance, runtimeArgs:IEnumerable = ..., declareArguments:bool = ...) -> str:
        """
        GenerateScript(self: SfcTsqlProcFormatter, sfcObject: SfcInstance) -> str
        GenerateScript(self: SfcTsqlProcFormatter, sfcObject: SfcInstance, runtimeArgs: IEnumerable[RuntimeArg]) -> str
        GenerateScript(self: SfcTsqlProcFormatter, sfcObject: SfcInstance, runtimeArgs: IEnumerable[RuntimeArg], declareArguments: bool) -> str
        """
        ...

    @staticmethod
    def MakeSqlBracket(value:str) -> str:
        """ MakeSqlBracket(value: str) -> str """
        ...

    @staticmethod
    def MakeSqlString(value:str) -> str:
        """ MakeSqlString(value: str) -> str """
        ...

    def RuntimeArg(self, *args): #cannot find CLR method
        """ RuntimeArg(type: Type, value: object) """
        ...

    def SprocArg(self, *args): #cannot find CLR method
        """
        SprocArg(name: str, property: str, required: bool, output: bool)
        SprocArg(name: str, required: bool)
        SprocArg(name: str, required: bool, output: bool)
        """
        ...

    @staticmethod
    def SqlBracket(value:str) -> str:
        """ SqlBracket(value: str) -> str """
        ...

    @staticmethod
    def SqlString(value:str) -> str:
        """ SqlString(value: str) -> str """
        ...

    @staticmethod
    def SqlStringBracket(value:str) -> str:
        """ SqlStringBracket(value: str) -> str """
        ...



class SfcTSqlScript(ISfcScript): # skipped bases: <type 'object'>
    """
    SfcTSqlScript()
    SfcTSqlScript(batch: str)
    """
    @property
    def ExecutionMode(self): # -> ExecutionMode
        """
        Get: ExecutionMode(self: SfcTSqlScript) -> ExecutionMode
        Set: ExecutionMode(self: SfcTSqlScript) = value
        """
        ...

    @property
    def ExecutionType(self) -> ExecutionTypes:
        """
        Get: ExecutionType(self: SfcTSqlScript) -> ExecutionTypes
        Set: ExecutionType(self: SfcTSqlScript) = value
        """
        ...


    def AddBatch(self, batch:str): # -> 
        """ AddBatch(self: SfcTSqlScript, batch: str) """
        ...

    def GetScript(self) -> StringCollection:
        """ GetScript(self: SfcTSqlScript) -> StringCollection """
        ...

    def ToString(self) -> str:
        """ ToString(self: SfcTSqlScript) -> str """
        ...


class SfcTypeMetadata: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def IsCrudActionHandledByParent(self, dependencyAction:SfcDependencyAction) -> bool:
        """ IsCrudActionHandledByParent(self: SfcTypeMetadata, dependencyAction: SfcDependencyAction) -> bool """
        ...


class SfcTypeRelation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SfcTypeRelation, values: ContainedChild (0), RequiredChild (1), StrongReference (2), WeakReference (3) """
    ContainedChild: SfcTypeRelation = ...
    RequiredChild: SfcTypeRelation = ...
    StrongReference: SfcTypeRelation = ...
    value__ = ...
    WeakReference: SfcTypeRelation = ...


class SfcUnregisteredXmlDomainException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcUnregisteredXmlDomainException()
    SfcUnregisteredXmlDomainException(message: str)
    SfcUnregisteredXmlDomainException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcUnregisteredXmlTypeException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcUnregisteredXmlTypeException()
    SfcUnregisteredXmlTypeException(message: str)
    SfcUnregisteredXmlTypeException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcUnsupportedVersionException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcUnsupportedVersionException()
    SfcUnsupportedVersionException(message: str)
    SfcUnsupportedVersionException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcUnsupportedVersionSerializationException(SfcException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SfcUnsupportedVersionSerializationException()
    SfcUnsupportedVersionSerializationException(message: str)
    SfcUnsupportedVersionSerializationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SfcUtility: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetSmlUri(urn:Urn, instanceType:Type) -> str:
        """ GetSmlUri(urn: Urn, instanceType: Type) -> str """
        ...

    @staticmethod
    def GetSqlCeToolsPath() -> str:
        """ GetSqlCeToolsPath() -> str """
        ...

    @staticmethod
    def GetUrn(obj:object) -> str:
        """ GetUrn(obj: object) -> str """
        ...

    @staticmethod
    def LoadSqlCeAssembly(assemblyName:str) -> Assembly:
        """ LoadSqlCeAssembly(assemblyName: str) -> Assembly """
        ...

    @staticmethod
    def TryGetSqlCeToolsPath() -> str:
        """ TryGetSqlCeToolsPath() -> str """
        ...

    __all__: list = ...


class SimpleNodeAdapter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetEnumerable(self, reference:object, enumName:str) -> IEnumerable:
        """ GetEnumerable(self: SimpleNodeAdapter, reference: object, enumName: str) -> IEnumerable """
        ...

    def GetObject(self, reference:object, childName:str) -> object:
        """ GetObject(self: SimpleNodeAdapter, reference: object, childName: str) -> object """
        ...

    def GetProperty(self, reference:object, propertyName:str) -> object:
        """ GetProperty(self: SimpleNodeAdapter, reference: object, propertyName: str) -> object """
        ...

    def GetUrn(self, reference:object) -> Urn:
        """ GetUrn(self: SimpleNodeAdapter, reference: object) -> Urn """
        ...

    def IsCriteriaMatched(self, reference:object) -> bool:
        """ IsCriteriaMatched(self: SimpleNodeAdapter, reference: object) -> bool """
        ...

    def IsSupported(self, reference:object) -> bool:
        """ IsSupported(self: SimpleNodeAdapter, reference: object) -> bool """
        ...


class SqlEnumResult(EnumResult): # skipped bases: <type 'object'>
    """ SqlEnumResult(ob: object, resultType: ResultType, databaseEngineType: DatabaseEngineType) """
    @property
    def Databases(self) -> DataTable:
        """
        Get: Databases(self: SqlEnumResult) -> DataTable
        Set: Databases(self: SqlEnumResult) = value
        """
        ...

    @property
    def LastDbLevelSet(self) -> bool:
        """
        Get: LastDbLevelSet(self: SqlEnumResult) -> bool
        Set: LastDbLevelSet(self: SqlEnumResult) = value
        """
        ...

    @property
    def Level(self) -> int:
        """ Get: Level(self: SqlEnumResult) -> int """
        ...

    @property
    def NameProperties(self) -> StringCollection:
        """
        Get: NameProperties(self: SqlEnumResult) -> StringCollection
        Set: NameProperties(self: SqlEnumResult) = value
        """
        ...

    @property
    def PostProcessFields(self) -> StringCollection:
        """ Get: PostProcessFields(self: SqlEnumResult) -> StringCollection """
        ...

    @property
    def SchemaPrefixes(self) -> DataTable:
        """
        Get: SchemaPrefixes(self: SqlEnumResult) -> DataTable
        Set: SchemaPrefixes(self: SqlEnumResult) = value
        """
        ...

    @property
    def SchemaPrefixProperties(self) -> StringCollection:
        """
        Get: SchemaPrefixProperties(self: SqlEnumResult) -> StringCollection
        Set: SchemaPrefixProperties(self: SqlEnumResult) = value
        """
        ...

    @property
    def StatementBuilder(self) -> StatementBuilder:
        """
        Get: StatementBuilder(self: SqlEnumResult) -> StatementBuilder
        Set: StatementBuilder(self: SqlEnumResult) = value
        """
        ...


    def BuildSql(self) -> StringCollection:
        """ BuildSql(self: SqlEnumResult) -> StringCollection """
        ...


class SqlObjectBase(ISqlFilterDecoderCallback, EnumObject): # skipped bases: <type 'object'>
    """ SqlObjectBase() """
    @property
    def ConditionedSqlList(self):
        ...

    @property
    def Distinct(self):
        ...

    @property
    def OrderByRedirect(self):
        ...

    @property
    def PostProcessList(self):
        ...

    @property
    def PropertyLinkList(self):
        ...

    @property
    def RequestParentSelect(self):
        ...

    @property
    def SpecialQuery(self):
        ...

    @property
    def SqlRequest(self):
        ...

    @property
    def StatementBuilder(self) -> StatementBuilder:
        """
        Get: StatementBuilder(self: SqlObjectBase) -> StatementBuilder
        Set: StatementBuilder(self: SqlObjectBase) = value
        """
        ...


    def AddConditionals(self, *args): #cannot find CLR method
        """ AddConditionals(self: SqlObjectBase, field: str) """
        ...

    def AddConditionalsJustPropDependencies(self, *args): #cannot find CLR method
        """ AddConditionalsJustPropDependencies(self: SqlObjectBase, name: str) """
        ...

    def AddFilterProperty(self, name:str) -> str:
        """ AddFilterProperty(self: SqlObjectBase, name: str) -> str """
        ...

    def AddLinkProperty(self, *args): #cannot find CLR method
        """ AddLinkProperty(self: SqlObjectBase, name: str) -> str """
        ...

    def AddOrderByAcrossDatabases(self, *args): #cannot find CLR method
        """ AddOrderByAcrossDatabases(self: SqlObjectBase) """
        ...

    def AddOrderByInDatabase(self, *args): #cannot find CLR method
        """ AddOrderByInDatabase(self: SqlObjectBase) """
        ...

    def AddOrderByProperty(self, name:str, overrideFlags:bool = ...) -> str:
        """
        AddOrderByProperty(self: SqlObjectBase, name: str) -> str
        AddOrderByProperty(self: SqlObjectBase, name: str, overrideFlags: bool) -> str
        """
        ...

    def BeforeStatementExecuted(self, *args): #cannot find CLR method
        """ BeforeStatementExecuted(self: SqlObjectBase, levelName: str) """
        ...

    def BuildStatement(self, *args): #cannot find CLR method
        """ BuildStatement(self: SqlObjectBase, erParent: EnumResult) """
        ...

    def ClearHits(self, *args): #cannot find CLR method
        """ ClearHits(self: SqlObjectBase) """
        ...

    def FillData(self, *args): #cannot find CLR method
        """ FillData(self: SqlObjectBase, resultType: ResultType, sql: StringCollection, connectionInfo: object, sb: StatementBuilder) -> object """
        ...

    def FillDataWithUseFailure(self, *args): #cannot find CLR method
        """ FillDataWithUseFailure(self: SqlObjectBase, sqlresult: SqlEnumResult, resultType: ResultType) -> object """
        ...

    def GetSqlProperty(self, field:str, usage:ObjectPropertyUsages) -> SqlObjectProperty:
        """ GetSqlProperty(self: SqlObjectBase, field: str, usage: ObjectPropertyUsages) -> SqlObjectProperty """
        ...

    def IntegrateParentResult(self, *args): #cannot find CLR method
        """ IntegrateParentResult(self: SqlObjectBase, erParent: EnumResult) """
        ...

    def ResolveComputedField(self, *args): #cannot find CLR method
        """ ResolveComputedField(self: SqlObjectBase, fieldName: str) -> str """
        ...

    def ResolveLocalLinkLinks(self, *args): #cannot find CLR method
        """ ResolveLocalLinkLinks(self: SqlObjectBase) """
        ...

    def RestoreInitialState(self, *args): #cannot find CLR method
        """ RestoreInitialState(self: SqlObjectBase) """
        ...

    def StoreInitialState(self, *args): #cannot find CLR method
        """ StoreInitialState(self: SqlObjectBase) """
        ...


class SqlObject(ISupportInitDatabaseEngineData, SqlObjectBase): # skipped bases: <type 'ISqlFilterDecoderCallback'>, <type 'object'>
    """ no doc """
    @property
    def ResourceAssembly(self) -> Assembly:
        """ Get: ResourceAssembly(self: SqlObject) -> Assembly """
        ...


    def Initialize(self, ci:object, block:XPathExpressionBlock): # -> 
        """ Initialize(self: SqlObject, ci: object, block: XPathExpressionBlock) """
        ...

    def LoadAndStore(self, *args): #cannot find CLR method
        """ LoadAndStore(self: SqlObject, xrd: XmlReadDoc, assemblyObject: Assembly, requestedFields: StringCollection) """
        ...

    def LoadInitDataFromAssembly(self, assemblyObject:Assembly, file:str, ver:ServerVersion, databaseEngineType:DatabaseEngineType, databaseEngineEdition:DatabaseEngineEdition): # -> 
        """ LoadInitDataFromAssembly(self: SqlObject, assemblyObject: Assembly, file: str, ver: ServerVersion, databaseEngineType: DatabaseEngineType, databaseEngineEdition: DatabaseEngineEdition) """
        ...


class SqlObjectProperty(ObjectProperty): # skipped bases: <type 'object'>
    """ SqlObjectProperty(xrp: XmlReadProperty) """
    @property
    def Alias(self) -> str:
        """
        Get: Alias(self: SqlObjectProperty) -> str
        Set: Alias(self: SqlObjectProperty) = value
        """
        ...

    @property
    def DBType(self) -> str:
        """ Get: DBType(self: SqlObjectProperty) -> str """
        ...

    @property
    def LinkFields(self) -> ArrayList:
        """ Get: LinkFields(self: SqlObjectProperty) -> ArrayList """
        ...

    @property
    def SessionValue(self) -> str:
        """
        Get: SessionValue(self: SqlObjectProperty) -> str
        Set: SessionValue(self: SqlObjectProperty) = value
        """
        ...

    @property
    def Size(self) -> str:
        """ Get: Size(self: SqlObjectProperty) -> str """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: SqlObjectProperty) -> str
        Set: Value(self: SqlObjectProperty) = value
        """
        ...


    def Add(self, o:SqlObjectBase, isTriggered:bool): # -> 
        """ Add(self: SqlObjectProperty, o: SqlObjectBase, isTriggered: bool) """
        ...

    def GetValue(self, o:SqlObjectBase) -> str:
        """ GetValue(self: SqlObjectProperty, o: SqlObjectBase) -> str """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __new__(cls, xrp:XmlReadProperty) -> Self:
        """ __new__(cls: type, xrp: XmlReadProperty) """
        ...


class SqlPropertyLink(ConditionedSql): # skipped bases: <type 'object'>
    """
    SqlPropertyLink(xrpl: XmlReadPropertyLink)
    SqlPropertyLink(xrp: XmlReadProperty)
    SqlPropertyLink(xrs: XmlReadSettings)
    """
    @property
    def Table(self) -> str:
        """
        Get: Table(self: SqlPropertyLink) -> str
        Set: Table(self: SqlPropertyLink) = value
        """
        ...


    @staticmethod
    def Add(list:ConditionedSqlList, *__args:XmlReadProperty): # -> 
        """ Add(list: ConditionedSqlList, xrp: XmlReadProperty)Add(list: ConditionedSqlList, xrs: XmlReadSettings) """
        ...

    @staticmethod
    def AddAll(list:ConditionedSqlList, xrpl:XmlReadPropertyLink): # -> 
        """ AddAll(list: ConditionedSqlList, xrpl: XmlReadPropertyLink) """
        ...

    def GetFilter(self, obj:SqlObjectBase) -> str:
        """ GetFilter(self: SqlPropertyLink, obj: SqlObjectBase) -> str """
        ...

    def GetTableNameWithAlias(self, obj:SqlObjectBase) -> str:
        """ GetTableNameWithAlias(self: SqlPropertyLink, obj: SqlObjectBase) -> str """
        ...

    def __new__(cls, *__args:XmlReadPropertyLink) -> Self:
        """
        __new__(cls: type, xrpl: XmlReadPropertyLink)
        __new__(cls: type, xrp: XmlReadProperty)
        __new__(cls: type, xrs: XmlReadSettings)
        """
        ...


class SqlRequest(Request): # skipped bases: <type 'object'>
    """
    SqlRequest()
    SqlRequest(reqUser: Request)
    """
    @property
    def LinkFields(self) -> ArrayList:
        """ Get: LinkFields(self: SqlRequest) -> ArrayList """
        ...

    @property
    def ResolveDatabases(self) -> bool:
        """
        Get: ResolveDatabases(self: SqlRequest) -> bool
        Set: ResolveDatabases(self: SqlRequest) = value
        """
        ...


    def SetLinkFields(self, list:ArrayList): # -> 
        """ SetLinkFields(self: SqlRequest, list: ArrayList) """
        ...


class SqlStoreConnection(SfcConnection): # skipped bases: <type 'ISfcConnection'>, <type 'object'>
    """ SqlStoreConnection(sqlConnection: SqlConnection) """
    @property
    def ServerConnection(self) -> ServerConnection:
        """ Get: ServerConnection(self: SqlStoreConnection) -> ServerConnection """
        ...


    def __new__(cls, sqlConnection:SqlConnection) -> Self:
        """ __new__(cls: type, sqlConnection: SqlConnection) """
        ...


class SQLToolsCommonTraceLvl: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Always: UInt32 = ...
    Error: UInt32 = ...
    L1: UInt32 = ...
    L2: UInt32 = ...
    L3: UInt32 = ...
    L4: UInt32 = ...
    Warning: UInt32 = ...


class StatementBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ StatementBuilder() """
    @property
    def Distinct(self) -> bool:
        """
        Get: Distinct(self: StatementBuilder) -> bool
        Set: Distinct(self: StatementBuilder) = value
        """
        ...

    @property
    def From(self) -> StringBuilder:
        """
        Get: From(self: StatementBuilder) -> StringBuilder
        Set: From(self: StatementBuilder) = value
        """
        ...

    @property
    def IsFirstJoin(self) -> bool:
        """ Get: IsFirstJoin(self: StatementBuilder) -> bool """
        ...

    @property
    def SqlPostfix(self) -> str:
        """ Get: SqlPostfix(self: StatementBuilder) -> str """
        ...

    @property
    def SqlStatement(self) -> str:
        """ Get: SqlStatement(self: StatementBuilder) -> str """
        ...


    def AddCondition(self, value:str): # -> 
        """ AddCondition(self: StatementBuilder, value: str) """
        ...

    def AddElement(self, *args): #cannot find CLR method
        """ AddElement(str: StringBuilder, value: str, delimStart: str, delimEnd: str, delimElems: str) """
        ...

    def AddFields(self, value:str): # -> 
        """ AddFields(self: StatementBuilder, value: str) """
        ...

    def AddFrom(self, value:str): # -> 
        """ AddFrom(self: StatementBuilder, value: str) """
        ...

    def AddJoin(self, value:str): # -> 
        """ AddJoin(self: StatementBuilder, value: str) """
        ...

    def AddOrderBy(self, *__args:str): # -> 
        """ AddOrderBy(self: StatementBuilder, str: str)AddOrderBy(self: StatementBuilder, prop: str, orderByValue: str, dir: Direction) """
        ...

    def AddPostfix(self, value:str): # -> 
        """ AddPostfix(self: StatementBuilder, value: str) """
        ...

    def AddPrefix(self, value:str): # -> 
        """ AddPrefix(self: StatementBuilder, value: str) """
        ...

    def AddProperty(self, name:str, value:str): # -> 
        """ AddProperty(self: StatementBuilder, name: str, value: str) """
        ...

    def AddUrn(self, value:str): # -> 
        """ AddUrn(self: StatementBuilder, value: str) """
        ...

    def AddWhere(self, value:str): # -> 
        """ AddWhere(self: StatementBuilder, value: str) """
        ...

    def ClearFailCondition(self): # -> 
        """ ClearFailCondition(self: StatementBuilder) """
        ...

    def GetSqlNoPrefixPostfix(self) -> str:
        """ GetSqlNoPrefixPostfix(self: StatementBuilder) -> str """
        ...

    def IsEmpty(self, s:StringBuilder) -> bool:
        """ IsEmpty(self: StatementBuilder, s: StringBuilder) -> bool """
        ...

    def MakeCopy(self) -> StatementBuilder:
        """ MakeCopy(self: StatementBuilder) -> StatementBuilder """
        ...

    def Merge(self, sb:StatementBuilder): # -> 
        """ Merge(self: StatementBuilder, sb: StatementBuilder) """
        ...


class TraceHelper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Assert(condition:bool, strFormat:str = ...): # -> 
        """ Assert(condition: bool)Assert(condition: bool, strFormat: str) """
        ...

    @staticmethod
    def LogExCatch(ex:Exception): # -> 
        """ LogExCatch(ex: Exception) """
        ...

    @staticmethod
    def Trace(strComponentName, *__args): # -> 
        """ Trace(strComponentName: str, strFormat: str, *args: Array[object])Trace(strComponentName: str, traceLevel: UInt32, strFormat: str, *args: Array[object]) """
        ...

    __all__: list = ...


class UnknownPropertyEnumeratorException(EnumeratorException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    UnknownPropertyEnumeratorException()
    UnknownPropertyEnumeratorException(propertyName: str)
    UnknownPropertyEnumeratorException(propertyName: str, innerException: Exception)
    """
    SerializeObjectState = ...


class UnknownTypeEnumeratorException(EnumeratorException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    UnknownTypeEnumeratorException()
    UnknownTypeEnumeratorException(typeName: str)
    UnknownTypeEnumeratorException(typeName: str, innerException: Exception)
    """
    SerializeObjectState = ...


class UpgradeSession: # skipped bases: <type 'object'>, <type 'object'>
    """ UpgradeSession() """
    def IsUpgradeRequiredOnType(self, instanceType:str, fileVersion:int) -> bool:
        """ IsUpgradeRequiredOnType(self: UpgradeSession, instanceType: str, fileVersion: int) -> bool """
        ...

    def PostProcessUpgrade(self, sfcCache:Dictionary, fileVersion:int): # -> 
        """ PostProcessUpgrade(self: UpgradeSession, sfcCache: Dictionary[str, object], fileVersion: int) """
        ...

    def UpgradeInstance(self, *__args) -> List:
        """
        UpgradeInstance(self: UpgradeSession, sfcInstanceData: List[SfcInstanceSerializedData], fileVersion: int, smlUri: str, sfcCache: Dictionary[str, object]) -> List[KeyValuePair[str, object]]
        UpgradeInstance(self: UpgradeSession, newInstanceType: Type, sfcInstanceData: List[SfcInstanceSerializedData]) -> object
        """
        ...


class Urn: # skipped bases: <type 'object'>, <type 'object'>
    """
    Urn()
    Urn(value: str)
    """
    @property
    def DomainInstanceName(self) -> str:
        """ Get: DomainInstanceName(self: Urn) -> str """
        ...

    @property
    def Parent(self) -> Urn:
        """ Get: Parent(self: Urn) -> Urn """
        ...

    @property
    def Type(self) -> str:
        """ Get: Type(self: Urn) -> str """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: Urn) -> str
        Set: Value(self: Urn) = value
        """
        ...

    @property
    def XPathExpression(self) -> XPathExpression:
        """ Get: XPathExpression(self: Urn) -> XPathExpression """
        ...


    @staticmethod
    def Compare(u1:Urn, u2:Urn, compInfoList:Array, cultureInfo:CultureInfo) -> bool:
        """ Compare(u1: Urn, u2: Urn, compInfoList: Array[CompareOptions], cultureInfo: CultureInfo) -> bool """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: Urn, o: object) -> bool """
        ...

    @staticmethod
    def EscapeString(value:str) -> str:
        """ EscapeString(value: str) -> str """
        ...

    def Fixed(self, ci:object) -> bool:
        """ Fixed(self: Urn, ci: object) -> bool """
        ...

    def GetAttribute(self, attributeName:str, type:str = ...) -> str:
        """
        GetAttribute(self: Urn, attributeName: str, type: str) -> str
        GetAttribute(self: Urn, attributeName: str) -> str
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Urn) -> int """
        ...

    def GetNameForType(self, type:str) -> str:
        """ GetNameForType(self: Urn, type: str) -> str """
        ...

    def IsValidUrn(self) -> bool:
        """ IsValidUrn(self: Urn) -> bool """
        ...

    def IsValidUrnSkeleton(self) -> bool:
        """ IsValidUrnSkeleton(self: Urn) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: Urn) -> str """
        ...

    @staticmethod
    def UnEscapeString(escapedValue:str) -> str:
        """ UnEscapeString(escapedValue: str) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Util: # skipped bases: <type 'object'>, <type 'object'>
    """ Util() """
    @staticmethod
    def DbTypeToClrType(strDBType:str) -> str:
        """ DbTypeToClrType(strDBType: str) -> str """
        ...

    @staticmethod
    def EscapeString(value:str, escapeCharacter:Char) -> str:
        """ EscapeString(value: str, escapeCharacter: Char) -> str """
        ...

    @staticmethod
    def LoadAssembly(assemblyName:str) -> Assembly:
        """ LoadAssembly(assemblyName: str) -> Assembly """
        ...

    def TransformToRequest(self, *args): #cannot find CLR method
        """ TransformToRequest(self: Util, ds: DataSet, res: ResultType) -> EnumResult """
        ...


class ValidationMethod: # skipped bases: <type 'object'>, <type 'object'>
    """ ValidationMethod() """
    Alter: str = ...
    Create: str = ...
    Rename: str = ...


class ValidationResult: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BindingKey(self) -> str:
        """ Get: BindingKey(self: ValidationResult) -> str """
        ...

    @property
    def ErrorDetails(self) -> Exception:
        """ Get: ErrorDetails(self: ValidationResult) -> Exception """
        ...

    @property
    def IsWarning(self) -> bool:
        """ Get: IsWarning(self: ValidationResult) -> bool """
        ...

    @property
    def Text(self) -> str:
        """ Get: Text(self: ValidationResult) -> str """
        ...



class ValidationState: # skipped bases: <type 'object'>, <type 'object'>
    """
    ValidationState()
    ValidationState(message: str, bindingKey: str, isWarning: bool)
    ValidationState(error: Exception, bindingKey: str, isWarning: bool)
    ValidationState(message: str, error: Exception, bindingKey: str, isWarning: bool)
    ValidationState(message: str, bindingKey: str)
    ValidationState(error: Exception, bindingKey: str)
    ValidationState(message: str, error: Exception, bindingKey: str)
    """
    @property
    def HasErrors(self) -> bool:
        """ Get: HasErrors(self: ValidationState) -> bool """
        ...

    @property
    def HasWarnings(self) -> bool:
        """ Get: HasWarnings(self: ValidationState) -> bool """
        ...

    @property
    def Results(self) -> IList:
        """ Get: Results(self: ValidationState) -> IList[ValidationResult] """
        ...


    def AddError(self, *__args): # -> 
        """ AddError(self: ValidationState, message: str, bindingKey: str)AddError(self: ValidationState, error: Exception, bindingKey: str)AddError(self: ValidationState, message: str, error: Exception, bindingKey: str) """
        ...

    def AddWarning(self, *__args): # -> 
        """ AddWarning(self: ValidationState, message: str, bindingKey: str)AddWarning(self: ValidationState, error: Exception, bindingKey: str)AddWarning(self: ValidationState, message: str, error: Exception, bindingKey: str) """
        ...


class XmlRead: # skipped bases: <type 'object'>, <type 'object'>
    """
    XmlRead(xmlReader: XmlRead)
    XmlRead(version: ServerVersion, serverAlias: str, databaseEngineType: DatabaseEngineType, databaseEngineEdition: DatabaseEngineEdition)
    XmlRead()
    """
    @property
    def Alias(self) -> str:
        """
        Get: Alias(self: XmlRead) -> str
        Set: Alias(self: XmlRead) = value
        """
        ...

    @property
    def Closed(self):
        ...

    @property
    def DatabaseEngineEdition(self) -> DatabaseEngineEdition:
        """
        Get: DatabaseEngineEdition(self: XmlRead) -> DatabaseEngineEdition
        Set: DatabaseEngineEdition(self: XmlRead) = value
        """
        ...

    @property
    def DatabaseEngineType(self) -> DatabaseEngineType:
        """
        Get: DatabaseEngineType(self: XmlRead) -> DatabaseEngineType
        Set: DatabaseEngineType(self: XmlRead) = value
        """
        ...

    @property
    def Reader(self):
        ...

    @property
    def Version(self) -> ServerVersion:
        """
        Get: Version(self: XmlRead) -> ServerVersion
        Set: Version(self: XmlRead) = value
        """
        ...


    def Close(self): # -> 
        """ Close(self: XmlRead) """
        ...

    def GetAliasString(self, *args): #cannot find CLR method
        """ GetAliasString(self: XmlRead, str: str) -> str """
        ...

    def GetFields(self, *args): #cannot find CLR method
        """ GetFields(fields: str) -> StringCollection """
        ...

    def GetTextOfElement(self, *args): #cannot find CLR method
        """ GetTextOfElement(self: XmlRead) -> str """
        ...

    def IsElementWithCheckVersion(self, *args): #cannot find CLR method
        """ IsElementWithCheckVersion(self: XmlRead, elemName: str) -> bool """
        ...

    def Skip(self): # -> 
        """ Skip(self: XmlRead) """
        ...

    ATTR_CLOUD_MAX_BUILD: str = ...
    ATTR_CLOUD_MAX_MAJOR: str = ...
    ATTR_CLOUD_MAX_MINOR: str = ...
    ATTR_CLOUD_MIN_BUILD: str = ...
    ATTR_CLOUD_MIN_MAJOR: str = ...
    ATTR_CLOUD_MIN_MINOR: str = ...
    ATTR_DATAWAREHOUSE_ENABLED: str = ...
    ATTR_MAX_BUILD: str = ...
    ATTR_MAX_MAJOR: str = ...
    ATTR_MAX_MINOR: str = ...
    ATTR_MIN_BUILD: str = ...
    ATTR_MIN_MAJOR: str = ...
    ATTR_MIN_MINOR: str = ...


class XmlReadRepeated(XmlRead): # skipped bases: <type 'object'>
    """
    XmlReadRepeated(xmlReader: XmlRead)
    XmlReadRepeated()
    """
    def Next(self, elemName:str = ...) -> bool:
        """
        Next(self: XmlReadRepeated) -> bool
        Next(self: XmlReadRepeated, elemName: str) -> bool
        """
        ...


class XmlReadConditionedStatement(XmlReadRepeated): # skipped bases: <type 'object'>
    """ XmlReadConditionedStatement(xmlReader: XmlRead) """
    @property
    def Fields(self) -> StringCollection:
        """ Get: Fields(self: XmlReadConditionedStatement) -> StringCollection """
        ...

    @property
    def MultipleLink(self) -> XmlReadMultipleLink:
        """ Get: MultipleLink(self: XmlReadConditionedStatement) -> XmlReadMultipleLink """
        ...

    @property
    def Sql(self) -> str:
        """ Get: Sql(self: XmlReadConditionedStatement) -> str """
        ...



class XmlReadConditionedStatementFailCondition(XmlReadConditionedStatement): # skipped bases: <type 'object'>
    """ XmlReadConditionedStatementFailCondition(xmlReader: XmlRead) """
    def Next(self, elemName=None) -> bool:
        """ Next(self: XmlReadConditionedStatementFailCondition) -> bool """
        ...


class XmlReadConditionedStatementPostfix(XmlReadConditionedStatement): # skipped bases: <type 'object'>
    """ XmlReadConditionedStatementPostfix(xmlReader: XmlRead) """
    def Next(self, elemName=None) -> bool:
        """ Next(self: XmlReadConditionedStatementPostfix) -> bool """
        ...


class XmlReadConditionedStatementPostProcess(XmlReadRepeated): # skipped bases: <type 'object'>
    """ XmlReadConditionedStatementPostProcess(xmlReader: XmlRead) """
    @property
    def ClassName(self) -> str:
        """ Get: ClassName(self: XmlReadConditionedStatementPostProcess) -> str """
        ...

    @property
    def Fields(self) -> StringCollection:
        """ Get: Fields(self: XmlReadConditionedStatementPostProcess) -> StringCollection """
        ...

    @property
    def TriggeredFields(self) -> StringCollection:
        """ Get: TriggeredFields(self: XmlReadConditionedStatementPostProcess) -> StringCollection """
        ...



class XmlReadConditionedStatementPrefix(XmlReadConditionedStatement): # skipped bases: <type 'object'>
    """ XmlReadConditionedStatementPrefix(xmlReader: XmlRead) """
    def Next(self, elemName=None) -> bool:
        """ Next(self: XmlReadConditionedStatementPrefix) -> bool """
        ...


class XmlReadDoc(XmlRead): # skipped bases: <type 'object'>
    """ XmlReadDoc(version: ServerVersion, serverAlias: str, databaseEngineType: DatabaseEngineType, databaseEngineEdition: DatabaseEngineEdition) """
    @property
    def Properties(self) -> XmlReadProperties:
        """ Get: Properties(self: XmlReadDoc) -> XmlReadProperties """
        ...

    @property
    def Settings(self) -> XmlReadSettings:
        """ Get: Settings(self: XmlReadDoc) -> XmlReadSettings """
        ...


    def LoadFile(self, a:Assembly, strFile:str): # -> 
        """ LoadFile(self: XmlReadDoc, a: Assembly, strFile: str) """
        ...

    def ReadUnion(self) -> bool:
        """ ReadUnion(self: XmlReadDoc) -> bool """
        ...


class XmlReadInclude(XmlRead): # skipped bases: <type 'object'>
    """ XmlReadInclude(xmlReader: XmlRead) """
    @property
    def File(self) -> str:
        """ Get: File(self: XmlReadInclude) -> str """
        ...

    @property
    def RequestedFields(self) -> StringCollection:
        """ Get: RequestedFields(self: XmlReadInclude) -> StringCollection """
        ...

    @property
    def TableAlias(self) -> str:
        """ Get: TableAlias(self: XmlReadInclude) -> str """
        ...



class XmlReadLinkFields(XmlReadRepeated): # skipped bases: <type 'object'>
    """ XmlReadLinkFields(xmlReader: XmlRead) """
    @property
    def DefaultValue(self) -> str:
        """ Get: DefaultValue(self: XmlReadLinkFields) -> str """
        ...

    @property
    def Field(self) -> str:
        """ Get: Field(self: XmlReadLinkFields) -> str """
        ...

    @property
    def Type(self) -> LinkFieldType:
        """ Get: Type(self: XmlReadLinkFields) -> LinkFieldType """
        ...



class XmlReadMultipleLink(XmlRead): # skipped bases: <type 'object'>
    """ XmlReadMultipleLink(xmlReader: XmlRead) """
    @property
    def Expression(self) -> str:
        """ Get: Expression(self: XmlReadMultipleLink) -> str """
        ...

    @property
    def LinkFields(self) -> XmlReadLinkFields:
        """ Get: LinkFields(self: XmlReadMultipleLink) -> XmlReadLinkFields """
        ...

    @property
    def No(self) -> str:
        """ Get: No(self: XmlReadMultipleLink) -> str """
        ...



class XmlReadOrderByRedirect(XmlReadRepeated): # skipped bases: <type 'object'>
    """ XmlReadOrderByRedirect(xmlReader: XmlRead) """
    @property
    def Field(self) -> str:
        """ Get: Field(self: XmlReadOrderByRedirect) -> str """
        ...

    @property
    def RedirectFields(self) -> StringCollection:
        """ Get: RedirectFields(self: XmlReadOrderByRedirect) -> StringCollection """
        ...



class XmlReadParentLink(XmlRead): # skipped bases: <type 'object'>
    """ XmlReadParentLink(xmlReader: XmlRead) """
    @property
    def MultipleLink(self) -> XmlReadMultipleLink:
        """ Get: MultipleLink(self: XmlReadParentLink) -> XmlReadMultipleLink """
        ...

    @property
    def SimpleParentLink(self) -> XmlReadSimpleParentLink:
        """ Get: SimpleParentLink(self: XmlReadParentLink) -> XmlReadSimpleParentLink """
        ...



class XmlReadProperties(XmlRead): # skipped bases: <type 'object'>
    """ XmlReadProperties(xmlReader: XmlRead) """
    @property
    def Include(self) -> XmlReadInclude:
        """ Get: Include(self: XmlReadProperties) -> XmlReadInclude """
        ...

    @property
    def Property(self) -> XmlReadProperty:
        """ Get: Property(self: XmlReadProperties) -> XmlReadProperty """
        ...



class XmlReadProperty(XmlRead): # skipped bases: <type 'object'>
    """ XmlReadProperty(xmlReader: XmlRead) """
    @property
    def Cast(self) -> bool:
        """ Get: Cast(self: XmlReadProperty) -> bool """
        ...

    @property
    def ClrType(self) -> str:
        """ Get: ClrType(self: XmlReadProperty) -> str """
        ...

    @property
    def DbType(self) -> str:
        """ Get: DbType(self: XmlReadProperty) -> str """
        ...

    @property
    def Expensive(self) -> bool:
        """ Get: Expensive(self: XmlReadProperty) -> bool """
        ...

    @property
    def ExtendedType(self) -> bool:
        """ Get: ExtendedType(self: XmlReadProperty) -> bool """
        ...

    @property
    def HasPropertyLink(self) -> bool:
        """ Get: HasPropertyLink(self: XmlReadProperty) -> bool """
        ...

    @property
    def Hidden(self) -> bool:
        """ Get: Hidden(self: XmlReadProperty) -> bool """
        ...

    @property
    def Link(self) -> str:
        """ Get: Link(self: XmlReadProperty) -> str """
        ...

    @property
    def MultipleLink(self) -> XmlReadMultipleLink:
        """ Get: MultipleLink(self: XmlReadProperty) -> XmlReadMultipleLink """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlReadProperty) -> str """
        ...

    @property
    def ReadOnly(self) -> bool:
        """ Get: ReadOnly(self: XmlReadProperty) -> bool """
        ...

    @property
    def Size(self) -> str:
        """ Get: Size(self: XmlReadProperty) -> str """
        ...

    @property
    def Table(self) -> str:
        """ Get: Table(self: XmlReadProperty) -> str """
        ...

    @property
    def Usage(self) -> ObjectPropertyUsages:
        """ Get: Usage(self: XmlReadProperty) -> ObjectPropertyUsages """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: XmlReadProperty) -> str """
        ...



class XmlReadPropertyLink(XmlReadRepeated): # skipped bases: <type 'object'>
    """ XmlReadPropertyLink(xmlReader: XmlRead) """
    @property
    def ExpressionIsForTableName(self) -> bool:
        """ Get: ExpressionIsForTableName(self: XmlReadPropertyLink) -> bool """
        ...

    @property
    def Fields(self) -> StringCollection:
        """ Get: Fields(self: XmlReadPropertyLink) -> StringCollection """
        ...

    @property
    def Filter(self) -> str:
        """ Get: Filter(self: XmlReadPropertyLink) -> str """
        ...

    @property
    def InnerJoin(self) -> str:
        """ Get: InnerJoin(self: XmlReadPropertyLink) -> str """
        ...

    @property
    def LeftJoin(self) -> str:
        """ Get: LeftJoin(self: XmlReadPropertyLink) -> str """
        ...

    @property
    def MultipleLink(self) -> XmlReadMultipleLink:
        """ Get: MultipleLink(self: XmlReadPropertyLink) -> XmlReadMultipleLink """
        ...

    @property
    def Table(self) -> str:
        """ Get: Table(self: XmlReadPropertyLink) -> str """
        ...

    @property
    def TableAlias(self) -> str:
        """ Get: TableAlias(self: XmlReadPropertyLink) -> str """
        ...



class XmlReadSettings(XmlRead): # skipped bases: <type 'object'>
    """ XmlReadSettings(xmlReader: XmlRead) """
    @property
    def AdditionalFilter(self) -> str:
        """ Get: AdditionalFilter(self: XmlReadSettings) -> str """
        ...

    @property
    def Distinct(self) -> bool:
        """ Get: Distinct(self: XmlReadSettings) -> bool """
        ...

    @property
    def FailCondition(self) -> XmlReadConditionedStatementFailCondition:
        """ Get: FailCondition(self: XmlReadSettings) -> XmlReadConditionedStatementFailCondition """
        ...

    @property
    def HasPropertyLink(self) -> bool:
        """ Get: HasPropertyLink(self: XmlReadSettings) -> bool """
        ...

    @property
    def Include(self) -> XmlReadInclude:
        """ Get: Include(self: XmlReadSettings) -> XmlReadInclude """
        ...

    @property
    def MainTable(self) -> str:
        """ Get: MainTable(self: XmlReadSettings) -> str """
        ...

    @property
    def OrderByRedirect(self) -> XmlReadOrderByRedirect:
        """ Get: OrderByRedirect(self: XmlReadSettings) -> XmlReadOrderByRedirect """
        ...

    @property
    def ParentLink(self) -> XmlReadParentLink:
        """ Get: ParentLink(self: XmlReadSettings) -> XmlReadParentLink """
        ...

    @property
    def Postfix(self) -> XmlReadConditionedStatementPostfix:
        """ Get: Postfix(self: XmlReadSettings) -> XmlReadConditionedStatementPostfix """
        ...

    @property
    def PostProcess(self) -> XmlReadConditionedStatementPostProcess:
        """ Get: PostProcess(self: XmlReadSettings) -> XmlReadConditionedStatementPostProcess """
        ...

    @property
    def Prefix(self) -> XmlReadConditionedStatementPrefix:
        """ Get: Prefix(self: XmlReadSettings) -> XmlReadConditionedStatementPrefix """
        ...

    @property
    def PropertyLink(self) -> XmlReadPropertyLink:
        """ Get: PropertyLink(self: XmlReadSettings) -> XmlReadPropertyLink """
        ...

    @property
    def RequestParentSelect(self) -> XmlRequestParentSelect:
        """ Get: RequestParentSelect(self: XmlReadSettings) -> XmlRequestParentSelect """
        ...

    @property
    def SpecialQuery(self) -> XmlReadSpecialQuery:
        """ Get: SpecialQuery(self: XmlReadSettings) -> XmlReadSpecialQuery """
        ...



class XmlReadSimpleParentLink(XmlReadRepeated): # skipped bases: <type 'object'>
    """ XmlReadSimpleParentLink(xmlReader: XmlRead) """
    @property
    def Local(self) -> str:
        """ Get: Local(self: XmlReadSimpleParentLink) -> str """
        ...

    @property
    def Parent(self) -> str:
        """ Get: Parent(self: XmlReadSimpleParentLink) -> str """
        ...



class XmlReadSpecialQuery(XmlRead): # skipped bases: <type 'object'>
    """ XmlReadSpecialQuery(xmlReader: XmlRead) """
    @property
    def Database(self) -> str:
        """ Get: Database(self: XmlReadSpecialQuery) -> str """
        ...

    @property
    def Query(self) -> str:
        """ Get: Query(self: XmlReadSpecialQuery) -> str """
        ...



class XmlRequestParentSelect(XmlRead): # skipped bases: <type 'object'>
    """ XmlRequestParentSelect(xmlReader: XmlRead) """
    @property
    def Field(self) -> XmlRequestParentSelectField:
        """ Get: Field(self: XmlRequestParentSelect) -> XmlRequestParentSelectField """
        ...



class XmlRequestParentSelectField(XmlReadRepeated): # skipped bases: <type 'object'>
    """ XmlRequestParentSelectField(xmlReader: XmlRead) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: XmlRequestParentSelectField) -> str """
        ...



class XmlUtility: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetFirstElementOnLevel(reader:XmlTextReader) -> bool:
        """ GetFirstElementOnLevel(reader: XmlTextReader) -> bool """
        ...

    @staticmethod
    def GoDownOneLevel(reader:XmlTextReader) -> bool:
        """ GoDownOneLevel(reader: XmlTextReader) -> bool """
        ...

    @staticmethod
    def GoUpOneLevel(reader:XmlTextReader) -> bool:
        """ GoUpOneLevel(reader: XmlTextReader) -> bool """
        ...

    @staticmethod
    def IsElement(reader:XmlTextReader, strName:str) -> bool:
        """ IsElement(reader: XmlTextReader, strName: str) -> bool """
        ...

    @staticmethod
    def SelectChildrenByAttribute(reader:XmlTextReader, strAttribute:str, strValue:str) -> bool:
        """ SelectChildrenByAttribute(reader: XmlTextReader, strAttribute: str, strValue: str) -> bool """
        ...

    @staticmethod
    def SelectChildrenByName(reader:XmlTextReader, strName:str) -> bool:
        """ SelectChildrenByName(reader: XmlTextReader, strName: str) -> bool """
        ...

    @staticmethod
    def SelectElementByName(reader:XmlTextReader, strName:str) -> bool:
        """ SelectElementByName(reader: XmlTextReader, strName: str) -> bool """
        ...

    @staticmethod
    def SelectNextElement(reader:XmlTextReader, strName:str = ...) -> bool:
        """
        SelectNextElement(reader: XmlTextReader, strName: str) -> bool
        SelectNextElement(reader: XmlTextReader) -> bool
        """
        ...

    @staticmethod
    def SelectNextElementOnLevel(reader:XmlTextReader) -> bool:
        """ SelectNextElementOnLevel(reader: XmlTextReader) -> bool """
        ...

    @staticmethod
    def SelectNextSibling(reader:XmlTextReader) -> bool:
        """ SelectNextSibling(reader: XmlTextReader) -> bool """
        ...


class XPathException(EnumeratorException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XPathException()
    XPathException(msg: str)
    XPathException(msg: str, e: Exception)
    """
    @property
    def ErrorCode(self) -> XPathExceptionCode:
        """ Get: ErrorCode(self: XPathException) -> XPathExceptionCode """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: XPathException) -> str """
        ...


    SerializeObjectState = ...


class XPathExceptionCode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XPathExceptionCode, values: BadContext (28), BadQueryObject (20), BooleanExpected (6), ConstantExpected (25), ExpressionExpected (4), FunctionExpected (15), InvalidArgument (10), InvalidDataRecordFilter (21), InvalidName (12), InvalidNodeType (13), InvalidNumArgs (11), InvalidPattern (19), InvalidPrefix (22), InvalidToken (14), InvalidVariable (26), Last (29), MovedFromSelection (24), NodeSetExpected (16), NodeTestExpected (3), NoSelectedSet (23), NotSupported (18), NoXPathActive (17), NumberExpected (5), QueryExpected (7), Success (0), TestExpected (9), TokenExpected (2), UnclosedString (1), UndefinedXsltContext (27), UnknownMethod (8) """
    BadContext: XPathExceptionCode = ...
    BadQueryObject: XPathExceptionCode = ...
    BooleanExpected: XPathExceptionCode = ...
    ConstantExpected: XPathExceptionCode = ...
    ExpressionExpected: XPathExceptionCode = ...
    FunctionExpected: XPathExceptionCode = ...
    InvalidArgument: XPathExceptionCode = ...
    InvalidDataRecordFilter: XPathExceptionCode = ...
    InvalidName: XPathExceptionCode = ...
    InvalidNodeType: XPathExceptionCode = ...
    InvalidNumArgs: XPathExceptionCode = ...
    InvalidPattern: XPathExceptionCode = ...
    InvalidPrefix: XPathExceptionCode = ...
    InvalidToken: XPathExceptionCode = ...
    InvalidVariable: XPathExceptionCode = ...
    Last: XPathExceptionCode = ...
    MovedFromSelection: XPathExceptionCode = ...
    NodeSetExpected: XPathExceptionCode = ...
    NodeTestExpected: XPathExceptionCode = ...
    NoSelectedSet: XPathExceptionCode = ...
    NotSupported: XPathExceptionCode = ...
    NoXPathActive: XPathExceptionCode = ...
    NumberExpected: XPathExceptionCode = ...
    QueryExpected: XPathExceptionCode = ...
    Success: XPathExceptionCode = ...
    TestExpected: XPathExceptionCode = ...
    TokenExpected: XPathExceptionCode = ...
    UnclosedString: XPathExceptionCode = ...
    UndefinedXsltContext: XPathExceptionCode = ...
    UnknownMethod: XPathExceptionCode = ...
    value__ = ...


class XPathExpression: # skipped bases: <type 'object'>, <type 'object'>
    """
    XPathExpression(strXPathExpression: str)
    XPathExpression(blocks: IList[XPathExpressionBlock])
    """
    @property
    def ExpressionSkeleton(self) -> str:
        """ Get: ExpressionSkeleton(self: XPathExpression) -> str """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: XPathExpression) -> int """
        ...


    def BlockExpressionSkeleton(self, blockIndex:int) -> str:
        """ BlockExpressionSkeleton(self: XPathExpression, blockIndex: int) -> str """
        ...

    def GetAttribute(self, attributeName:str, type:str) -> str:
        """ GetAttribute(self: XPathExpression, attributeName: str, type: str) -> str """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: XPathExpression) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: XPathExpression) -> str """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class XPathExpressionBlock: # skipped bases: <type 'object'>, <type 'object'>
    """
    XPathExpressionBlock()
    XPathExpressionBlock(name: str, filter: FilterNode)
    """
    @property
    def Filter(self) -> FilterNode:
        """
        Get: Filter(self: XPathExpressionBlock) -> FilterNode
        Set: Filter(self: XPathExpressionBlock) = value
        """
        ...

    @property
    def FixedProperties(self) -> SortedList:
        """ Get: FixedProperties(self: XPathExpressionBlock) -> SortedList """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: XPathExpressionBlock) -> str
        Set: Name(self: XPathExpressionBlock) = value
        """
        ...


    def Copy(self) -> XPathExpressionBlock:
        """ Copy(self: XPathExpressionBlock) -> XPathExpressionBlock """
        ...

    def GetAttributeFromFilter(self, attributeName:str) -> str:
        """ GetAttributeFromFilter(self: XPathExpressionBlock, attributeName: str) -> str """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: XPathExpressionBlock) -> int """
        ...

    @staticmethod
    def GetUniqueAttribute(filter:FilterNode) -> str:
        """ GetUniqueAttribute(filter: FilterNode) -> str """
        ...

    def ToString(self) -> str:
        """ ToString(self: XPathExpressionBlock) -> str """
        ...


# variables with complex values

