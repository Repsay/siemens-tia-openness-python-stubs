# encoding: utf-8
# module Microsoft.AnalysisServices.AdomdClient calls itself AdomdClient
# from Microsoft.AnalysisServices.AdomdClient, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Sdk.Sfc import Enumerator

from Microsoft.SqlServer.Management.SqlParser.Metadata import (
    IMetadataObject)

from System import (Array, Byte, Char, DateTime, Decimal, Enum, Guid, 
    ICloneable, Int16, Int64, MarshalByRefObject, Single, TimeSpan, Type)

from System.Collections import ICollection, IEnumerable, IList

from System.ComponentModel import Component

from System.Data import (DataRowVersion, DataSet, DbType, 
    IDataParameterCollection, IDataReader, IDbCommand, IDbConnection, 
    IDbDataParameter, IDbTransaction, ParameterDirection)

from System.Data.Common import DbDataAdapter

from System.IO import Stream

from System.Xml import XmlReader

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    IAdomdBaseObject, ICommandContentProvider, IDataReaderConsumer, 
    ISubordinateObject, IXmlaDataReaderOwner, IXmlaProperty, field#)
"""

# no functions
# classes

class AadAuthenticator(IAadAuthenticator): # skipped bases: <type 'object'>
    """ AadAuthenticator() """
    Instance: AadAuthenticator = ...


class AadTokenHolder(IAadTokenHolder): # skipped bases: <type 'object'>
    """ no doc """
    pass

class AdomdDataReader(MarshalByRefObject, IEnumerable, IXmlaDataReaderOwner, IDataReader): # skipped bases: <type 'IDisposable'>, <type 'IDataRecord'>, <type 'object'>
    """ no doc """
    @property
    def FieldCount(self) -> int:
        """ Get: FieldCount(self: AdomdDataReader) -> int """
        ...

    @property
    def RowsetName(self) -> str:
        """ Get: RowsetName(self: AdomdDataReader) -> str """
        ...


    def Dispose(self): # -> 
        """ Dispose(self: AdomdDataReader) """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def GetBoolean(self, ordinal:int) -> bool:
        """ GetBoolean(self: AdomdDataReader, ordinal: int) -> bool """
        ...

    def GetByte(self, ordinal:int) -> Byte:
        """ GetByte(self: AdomdDataReader, ordinal: int) -> Byte """
        ...

    def GetBytes(self, ordinal:int, dataIndex:Int64, buffer:Array, bufferIndex:int, length:int) -> Int64:
        """ GetBytes(self: AdomdDataReader, ordinal: int, dataIndex: Int64, buffer: Array[Byte], bufferIndex: int, length: int) -> Int64 """
        ...

    def GetChar(self, ordinal:int) -> Char:
        """ GetChar(self: AdomdDataReader, ordinal: int) -> Char """
        ...

    def GetChars(self, ordinal:int, dataIndex:Int64, buffer:Array, bufferIndex:int, length:int) -> Int64:
        """ GetChars(self: AdomdDataReader, ordinal: int, dataIndex: Int64, buffer: Array[Char], bufferIndex: int, length: int) -> Int64 """
        ...

    def GetData(self, ordinal:int) -> IDataReader:
        """ GetData(self: AdomdDataReader, ordinal: int) -> IDataReader """
        ...

    def GetDataReader(self, ordinal:int) -> AdomdDataReader:
        """ GetDataReader(self: AdomdDataReader, ordinal: int) -> AdomdDataReader """
        ...

    def GetDataTypeName(self, index:int) -> str:
        """ GetDataTypeName(self: AdomdDataReader, index: int) -> str """
        ...

    def GetDateTime(self, ordinal:int) -> DateTime:
        """ GetDateTime(self: AdomdDataReader, ordinal: int) -> DateTime """
        ...

    def GetDecimal(self, ordinal:int) -> Decimal:
        """ GetDecimal(self: AdomdDataReader, ordinal: int) -> Decimal """
        ...

    def GetDouble(self, ordinal:int) -> float:
        """ GetDouble(self: AdomdDataReader, ordinal: int) -> float """
        ...

    def GetFieldType(self, ordinal:int) -> Type:
        """ GetFieldType(self: AdomdDataReader, ordinal: int) -> Type """
        ...

    def GetFloat(self, ordinal:int) -> Single:
        """ GetFloat(self: AdomdDataReader, ordinal: int) -> Single """
        ...

    def GetGuid(self, ordinal:int) -> Guid:
        """ GetGuid(self: AdomdDataReader, ordinal: int) -> Guid """
        ...

    def GetInt16(self, ordinal:int) -> Int16:
        """ GetInt16(self: AdomdDataReader, ordinal: int) -> Int16 """
        ...

    def GetInt32(self, ordinal:int) -> int:
        """ GetInt32(self: AdomdDataReader, ordinal: int) -> int """
        ...

    def GetInt64(self, ordinal:int) -> Int64:
        """ GetInt64(self: AdomdDataReader, ordinal: int) -> Int64 """
        ...

    def GetName(self, ordinal:int) -> str:
        """ GetName(self: AdomdDataReader, ordinal: int) -> str """
        ...

    def GetOrdinal(self, name:str) -> int:
        """ GetOrdinal(self: AdomdDataReader, name: str) -> int """
        ...

    def GetString(self, ordinal:int) -> str:
        """ GetString(self: AdomdDataReader, ordinal: int) -> str """
        ...

    def GetTimeSpan(self, ordinal:int) -> TimeSpan:
        """ GetTimeSpan(self: AdomdDataReader, ordinal: int) -> TimeSpan """
        ...

    def GetValue(self, ordinal:int) -> object:
        """ GetValue(self: AdomdDataReader, ordinal: int) -> object """
        ...

    def GetValues(self, values:Array) -> int:
        """ GetValues(self: AdomdDataReader, values: Array[object]) -> int """
        ...

    def IsDBNull(self, ordinal:int) -> bool:
        """ IsDBNull(self: AdomdDataReader, ordinal: int) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, xmlReader: XmlReader, commandBehavior: CommandBehavior, connection: AdomdConnection, readerAtRoot: bool) """
        ...



class AdomdAffectedObjectsReader(AdomdDataReader): # skipped bases: <type 'IDisposable'>, <type 'IDataReader'>, <type 'IDataRecord'>, <type 'IEnumerable'>, <type 'IXmlaDataReaderOwner'>, <type 'object'>
    """ no doc """
    @property
    def BaseVersion(self) -> int:
        """ Get: BaseVersion(self: AdomdAffectedObjectsReader) -> int """
        ...

    @property
    def CurrentVersion(self) -> int:
        """ Get: CurrentVersion(self: AdomdAffectedObjectsReader) -> int """
        ...

    @property
    def Database(self) -> str:
        """ Get: Database(self: AdomdAffectedObjectsReader) -> str """
        ...



class AdomdException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    SerializeObjectState = ...


class AdomdCacheExpiredException(AdomdException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    SerializeObjectState = ...


class AdomdCommand(ICloneable, IDbCommand, ICommandContentProvider, Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    AdomdCommand()
    AdomdCommand(commandText: str)
    AdomdCommand(commandText: str, connection: AdomdConnection)
    """
    @property
    def ActivityID(self) -> Guid:
        """
        Get: ActivityID(self: AdomdCommand) -> Guid
        Set: ActivityID(self: AdomdCommand) = value
        """
        ...

    @property
    def CommandStream(self) -> Stream:
        """
        Get: CommandStream(self: AdomdCommand) -> Stream
        Set: CommandStream(self: AdomdCommand) = value
        """
        ...

    @property
    def Properties(self) -> AdomdPropertyCollection:
        """ Get: Properties(self: AdomdCommand) -> AdomdPropertyCollection """
        ...

    @property
    def RequestPriority(self) -> RequestPriorities:
        """
        Get: RequestPriority(self: AdomdCommand) -> RequestPriorities
        Set: RequestPriority(self: AdomdCommand) = value
        """
        ...


    def Execute(self) -> object:
        """ Execute(self: AdomdCommand) -> object """
        ...

    def ExecuteCellSet(self) -> CellSet:
        """ ExecuteCellSet(self: AdomdCommand) -> CellSet """
        ...

    def ExecuteXmlReader(self) -> XmlReader:
        """ ExecuteXmlReader(self: AdomdCommand) -> XmlReader """
        ...

    def __new__(cls, commandText:str = ..., connection:AdomdConnection = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, commandText: str)
        __new__(cls: type, commandText: str, connection: AdomdConnection)
        """
        ...


class AdomdConnection(ICloneable, IDbConnection, Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    AdomdConnection()
    AdomdConnection(connectionString: str)
    AdomdConnection(connection: AdomdConnection)
    """
    @property
    def ClientVersion(self) -> str:
        """ Get: ClientVersion(self: AdomdConnection) -> str """
        ...

    @property
    def Cubes(self) -> CubeCollection:
        """ Get: Cubes(self: AdomdConnection) -> CubeCollection """
        ...

    @property
    def MiningModels(self) -> MiningModelCollection:
        """ Get: MiningModels(self: AdomdConnection) -> MiningModelCollection """
        ...

    @property
    def MiningServices(self) -> MiningServiceCollection:
        """ Get: MiningServices(self: AdomdConnection) -> MiningServiceCollection """
        ...

    @property
    def MiningStructures(self) -> MiningStructureCollection:
        """ Get: MiningStructures(self: AdomdConnection) -> MiningStructureCollection """
        ...

    @property
    def Properties(self) -> AdomdPropertyCollection:
        """ Get: Properties(self: AdomdConnection) -> AdomdPropertyCollection """
        ...

    @property
    def ProviderVersion(self) -> str:
        """ Get: ProviderVersion(self: AdomdConnection) -> str """
        ...

    @property
    def ServerVersion(self) -> str:
        """ Get: ServerVersion(self: AdomdConnection) -> str """
        ...

    @property
    def SessionID(self) -> str:
        """
        Get: SessionID(self: AdomdConnection) -> str
        Set: SessionID(self: AdomdConnection) = value
        """
        ...

    @property
    def ShowHiddenObjects(self) -> bool:
        """
        Get: ShowHiddenObjects(self: AdomdConnection) -> bool
        Set: ShowHiddenObjects(self: AdomdConnection) = value
        """
        ...


    def ChangeEffectiveUser(self, effectiveUserName:str): # -> 
        """ ChangeEffectiveUser(self: AdomdConnection, effectiveUserName: str) """
        ...

    def GetSchemaDataSet(self, *__args) -> DataSet:
        """
        GetSchemaDataSet(self: AdomdConnection, schema: Guid, restrictions: Array[object], throwOnInlineErrors: bool) -> DataSet
        GetSchemaDataSet(self: AdomdConnection, schemaName: str, restrictions: AdomdRestrictionCollection, throwOnInlineErrors: bool) -> DataSet
        GetSchemaDataSet(self: AdomdConnection, schemaName: str, schemaNamespace: str, restrictions: AdomdRestrictionCollection, throwOnInlineErrors: bool) -> DataSet
        GetSchemaDataSet(self: AdomdConnection, schemaName: str, schemaNamespace: str, restrictions: AdomdRestrictionCollection, throwOnInlineErrors: bool, requestProperties: AdomdPropertyCollection) -> DataSet
        GetSchemaDataSet(self: AdomdConnection, schema: Guid, restrictions: Array[object]) -> DataSet
        GetSchemaDataSet(self: AdomdConnection, schemaName: str, restrictions: AdomdRestrictionCollection) -> DataSet
        GetSchemaDataSet(self: AdomdConnection, schemaName: str, schemaNamespace: str, restrictions: AdomdRestrictionCollection) -> DataSet
        """
        ...

    def RefreshMetadata(self): # -> 
        """ RefreshMetadata(self: AdomdConnection) """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, connectionString: str)
        __new__(cls: type, connection: AdomdConnection)
        """
        ...


class AdomdConnectionException(AdomdException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def ExceptionCause(self) -> ConnectionExceptionCause:
        """ Get: ExceptionCause(self: AdomdConnectionException) -> ConnectionExceptionCause """
        ...


    SerializeObjectState = ...


class AdomdDataAdapter(IDataReaderConsumer, DbDataAdapter): # skipped bases: <type 'IDataAdapter'>, <type 'IDisposable'>, <type 'IComponent'>, <type 'ICloneable'>, <type 'IDbDataAdapter'>, <type 'object'>
    """
    AdomdDataAdapter()
    AdomdDataAdapter(selectCommand: AdomdCommand)
    AdomdDataAdapter(selectCommandText: str, selectConnection: AdomdConnection)
    AdomdDataAdapter(selectCommandText: str, selectConnectionString: str)
    """
    pass

class AdomdError: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CallStack(self) -> str:
        """ Get: CallStack(self: AdomdError) -> str """
        ...

    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: AdomdError) -> int """
        ...

    @property
    def HelpLink(self) -> str:
        """ Get: HelpLink(self: AdomdError) -> str """
        ...

    @property
    def Location(self) -> AdomdErrorLocation:
        """ Get: Location(self: AdomdError) -> AdomdErrorLocation """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: AdomdError) -> str """
        ...

    @property
    def Source(self) -> str:
        """ Get: Source(self: AdomdError) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: AdomdError) -> str """
        ...


class AdomdErrorCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: AdomdErrorCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class AdomdErrorLocation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def EndColumn(self) -> int:
        """ Get: EndColumn(self: AdomdErrorLocation) -> int """
        ...

    @property
    def EndLine(self) -> int:
        """ Get: EndLine(self: AdomdErrorLocation) -> int """
        ...

    @property
    def LineOffset(self) -> int:
        """ Get: LineOffset(self: AdomdErrorLocation) -> int """
        ...

    @property
    def StartColumn(self) -> int:
        """ Get: StartColumn(self: AdomdErrorLocation) -> int """
        ...

    @property
    def StartLine(self) -> int:
        """ Get: StartLine(self: AdomdErrorLocation) -> int """
        ...

    @property
    def TextLength(self) -> int:
        """ Get: TextLength(self: AdomdErrorLocation) -> int """
        ...



class AdomdErrorResponseException(AdomdException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: AdomdErrorResponseException) -> int """
        ...

    @property
    def Errors(self) -> AdomdErrorCollection:
        """ Get: Errors(self: AdomdErrorResponseException) -> AdomdErrorCollection """
        ...


    SerializeObjectState = ...


class AdomdParameter(ICloneable, MarshalByRefObject, IDbDataParameter): # skipped bases: <type 'IDataParameter'>, <type 'object'>
    """
    AdomdParameter()
    AdomdParameter(parameterName: str, value: object)
    """
    @property
    def DbType(self) -> DbType:
        """
        Get: DbType(self: AdomdParameter) -> DbType
        Set: DbType(self: AdomdParameter) = value
        """
        ...

    @property
    def Direction(self) -> ParameterDirection:
        """
        Get: Direction(self: AdomdParameter) -> ParameterDirection
        Set: Direction(self: AdomdParameter) = value
        """
        ...

    @property
    def IsNullable(self) -> bool:
        """
        Get: IsNullable(self: AdomdParameter) -> bool
        Set: IsNullable(self: AdomdParameter) = value
        """
        ...

    @property
    def ParameterName(self) -> str:
        """
        Get: ParameterName(self: AdomdParameter) -> str
        Set: ParameterName(self: AdomdParameter) = value
        """
        ...

    @property
    def SourceColumn(self) -> str:
        """
        Get: SourceColumn(self: AdomdParameter) -> str
        Set: SourceColumn(self: AdomdParameter) = value
        """
        ...

    @property
    def SourceVersion(self) -> DataRowVersion:
        """
        Get: SourceVersion(self: AdomdParameter) -> DataRowVersion
        Set: SourceVersion(self: AdomdParameter) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: AdomdParameter) -> object
        Set: Value(self: AdomdParameter) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: AdomdParameter) -> str """
        ...

    def __new__(cls, parameterName:str = ..., value:object = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parameterName: str, value: object)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class AdomdParameterCollection(MarshalByRefObject, IDataParameterCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: AdomdParameterCollection) -> int """
        ...


    def Add(self, *__args:AdomdParameter) -> AdomdParameter:
        """
        Add(self: AdomdParameterCollection, value: AdomdParameter) -> AdomdParameter
        Add(self: AdomdParameterCollection, parameterName: str, value: object) -> AdomdParameter
        """
        ...

    def Clear(self): # -> 
        """ Clear(self: AdomdParameterCollection) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: AdomdParameterCollection, array: Array[AdomdParameter], index: int) """
        ...

    def Find(self, parameterName:str) -> AdomdParameter:
        """ Find(self: AdomdParameterCollection, parameterName: str) -> AdomdParameter """
        ...

    def Insert(self, index:int, value:AdomdParameter): # -> 
        """ Insert(self: AdomdParameterCollection, index: int, value: AdomdParameter) """
        ...

    def Remove(self, value:AdomdParameter): # -> 
        """ Remove(self: AdomdParameterCollection, value: AdomdParameter) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...


class AdomdProperty(IXmlaProperty): # skipped bases: <type 'IXmlaPropertyKey'>, <type 'object'>
    """
    AdomdProperty(name: str, propertyValue: object)
    AdomdProperty(name: str, propertyNamespace: str, propertyValue: object)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: AdomdProperty) -> str
        Set: Name(self: AdomdProperty) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: AdomdProperty) -> str
        Set: Namespace(self: AdomdProperty) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: AdomdProperty) -> object """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: AdomdProperty) -> object
        Set: Value(self: AdomdProperty) = value
        """
        ...



class AdomdPropertyCollection(MarshalByRefObject, IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ AdomdPropertyCollection() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: AdomdPropertyCollection) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: AdomdPropertyCollection) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: AdomdPropertyCollection) -> object """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: AdomdPropertyCollection, array: Array[AdomdProperty], index: int) """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, propertyName:str, propertyNamespace:str = ...) -> AdomdProperty:
        """
        Find(self: AdomdPropertyCollection, propertyName: str) -> AdomdProperty
        Find(self: AdomdPropertyCollection, propertyName: str, propertyNamespace: str) -> AdomdProperty
        """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: AdomdPropertyCollection) -> Enumerator """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...



class AdomdRestriction(IXmlaProperty): # skipped bases: <type 'IXmlaPropertyKey'>, <type 'object'>
    """
    AdomdRestriction(name: str, restrictionValue: object)
    AdomdRestriction(name: str, restrictionNamespace: str, restrictionValue: object)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: AdomdRestriction) -> str
        Set: Name(self: AdomdRestriction) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: AdomdRestriction) -> str
        Set: Namespace(self: AdomdRestriction) = value
        """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: AdomdRestriction) -> object """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: AdomdRestriction) -> object
        Set: Value(self: AdomdRestriction) = value
        """
        ...



class AdomdRestrictionCollection(MarshalByRefObject, IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ AdomdRestrictionCollection() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: AdomdRestrictionCollection) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: AdomdRestrictionCollection) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: AdomdRestrictionCollection) -> object """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: AdomdRestrictionCollection, array: Array[AdomdRestriction], index: int) """
        ...

    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, propertyName:str, propertyNamespace:str = ...) -> AdomdRestriction:
        """
        Find(self: AdomdRestrictionCollection, propertyName: str) -> AdomdRestriction
        Find(self: AdomdRestrictionCollection, propertyName: str, propertyNamespace: str) -> AdomdRestriction
        """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: AdomdRestrictionCollection) -> Enumerator """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...



class AdomdSchemaGuid: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Actions: Guid = ...
    Catalogs: Guid = ...
    Columns: Guid = ...
    CommandObjects: Guid = ...
    Commands: Guid = ...
    Connections: Guid = ...
    Csdl: Guid = ...
    Cubes: Guid = ...
    DataSources: Guid = ...
    DBConnections: Guid = ...
    DependecyGraph: Guid = ...
    Dimensions: Guid = ...
    DimensionStat: Guid = ...
    Enumerators: Guid = ...
    Functions: Guid = ...
    Hierarchies: Guid = ...
    InputDataSources: Guid = ...
    Instances: Guid = ...
    Jobs: Guid = ...
    Keywords: Guid = ...
    Kpis: Guid = ...
    Levels: Guid = ...
    Literals: Guid = ...
    Locations: Guid = ...
    Locks: Guid = ...
    MasterKey: Guid = ...
    MeasureGroupDimensions: Guid = ...
    MeasureGroups: Guid = ...
    Measures: Guid = ...
    MemberProperties: Guid = ...
    Members: Guid = ...
    MemoryGrant: Guid = ...
    MemoryUsage: Guid = ...
    MiningColumns: Guid = ...
    MiningFunctions: Guid = ...
    MiningModelContent: Guid = ...
    MiningModelContentPmml: Guid = ...
    MiningModels: Guid = ...
    MiningModelXml: Guid = ...
    MiningServiceParameters: Guid = ...
    MiningServices: Guid = ...
    MiningStructureColumns: Guid = ...
    MiningStructures: Guid = ...
    ObjectActivity: Guid = ...
    ObjectMemoryUsage: Guid = ...
    PartitionDimensionStat: Guid = ...
    PartitionStat: Guid = ...
    PerformanceCounters: Guid = ...
    ProviderTypes: Guid = ...
    ResourcePools: Guid = ...
    RingBuffers: Guid = ...
    SchemaRowsets: Guid = ...
    Sessions: Guid = ...
    Sets: Guid = ...
    StorageSegments: Guid = ...
    StorageTableColumns: Guid = ...
    StorageTables: Guid = ...
    Tables: Guid = ...
    TablesInfo: Guid = ...
    TabularAnnotations: Guid = ...
    TabularAttributeHierarchies: Guid = ...
    TabularAttributeHierarchyStorages: Guid = ...
    TabularColumnPartitionStorages: Guid = ...
    TabularColumnPermissions: Guid = ...
    TabularColumns: Guid = ...
    TabularColumnStorages: Guid = ...
    TabularCultures: Guid = ...
    TabularDataSources: Guid = ...
    TabularDetailRowsDefinitions: Guid = ...
    TabularDictionaryStorages: Guid = ...
    TabularExpressions: Guid = ...
    TabularExtendedProperties: Guid = ...
    TabularGroupByColumns: Guid = ...
    TabularHierarchies: Guid = ...
    TabularHierarchyStorages: Guid = ...
    TabularKpis: Guid = ...
    TabularLevels: Guid = ...
    TabularLinguisticMetadata: Guid = ...
    TabularMeasures: Guid = ...
    TabularModel: Guid = ...
    TabularObjectTranslations: Guid = ...
    TabularPartitions: Guid = ...
    TabularPartitionStorages: Guid = ...
    TabularPerspectiveColumns: Guid = ...
    TabularPerspectiveHierarchies: Guid = ...
    TabularPerspectiveMeasures: Guid = ...
    TabularPerspectives: Guid = ...
    TabularPerspectiveSets: Guid = ...
    TabularPerspectiveTables: Guid = ...
    TabularRelatedColumnDetails: Guid = ...
    TabularRelationshipIndexStorages: Guid = ...
    TabularRelationships: Guid = ...
    TabularRelationshipStorages: Guid = ...
    TabularRoleMemberships: Guid = ...
    TabularRoles: Guid = ...
    TabularSegmentMapStorages: Guid = ...
    TabularSegmentStorages: Guid = ...
    TabularSets: Guid = ...
    TabularStorageFiles: Guid = ...
    TabularStorageFolders: Guid = ...
    TabularTablePermissions: Guid = ...
    TabularTables: Guid = ...
    TabularTableStorages: Guid = ...
    TabularVariations: Guid = ...
    TraceColumns: Guid = ...
    TraceDefinitionProviderInfo: Guid = ...
    TraceEventCategories: Guid = ...
    Traces: Guid = ...
    Transactions: Guid = ...
    XEventObjectColumns: Guid = ...
    XEventObjects: Guid = ...
    XEventPackages: Guid = ...
    XEventSessions: Guid = ...
    XEventSessionTargets: Guid = ...
    XmlaProperties: Guid = ...
    XmlMetadata: Guid = ...


class AdomdTransaction(IDbTransaction): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    def Dispose(self): # -> 
        """ Dispose(self: AdomdTransaction) """
        ...


class AdomdUnknownResponseException(AdomdException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    SerializeObjectState = ...


class AxesInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Axes(self) -> OlapInfoAxisCollection:
        """ Get: Axes(self: AxesInfo) -> OlapInfoAxisCollection """
        ...

    @property
    def FilterAxis(self) -> OlapInfoAxis:
        """ Get: FilterAxis(self: AxesInfo) -> OlapInfoAxis """
        ...



class Axis(ISubordinateObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: Axis) -> str """
        ...

    @property
    def Positions(self) -> PositionCollection:
        """ Get: Positions(self: Axis) -> PositionCollection """
        ...

    @property
    def Set(self) -> Set:
        """ Get: Set(self: Axis) -> Set """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Axis, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Axis) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Axis) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AxisCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, name:str) -> Axis:
        """ Find(self: AxisCollection, name: str) -> Axis """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: AxisCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class CacheContent: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CacheDataAsString(self) -> str:
        """
        Get: CacheDataAsString(self: CacheContent) -> str
        Set: CacheDataAsString(self: CacheContent) = value
        """
        ...

    @property
    def DataSource(self) -> str:
        """
        Get: DataSource(self: CacheContent) -> str
        Set: DataSource(self: CacheContent) = value
        """
        ...



class Cell(ISubordinateObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CellProperties(self) -> CellPropertyCollection:
        """ Get: CellProperties(self: Cell) -> CellPropertyCollection """
        ...

    @property
    def FormattedValue(self) -> str:
        """ Get: FormattedValue(self: Cell) -> str """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: Cell) -> object """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Cell, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Cell) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CellCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: CellCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class CellInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CellProperties(self) -> OlapInfoPropertyCollection:
        """ Get: CellProperties(self: CellInfo) -> OlapInfoPropertyCollection """
        ...



class CellProperty(ISubordinateObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: CellProperty) -> str """
        ...

    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: CellProperty) -> str """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: CellProperty) -> object """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: CellProperty, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CellProperty) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: CellProperty) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CellPropertyCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, name:str) -> CellProperty:
        """ Find(self: CellPropertyCollection, name: str) -> CellProperty """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: CellPropertyCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class CellSet: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Axes(self) -> AxisCollection:
        """ Get: Axes(self: CellSet) -> AxisCollection """
        ...

    @property
    def Cells(self) -> CellCollection:
        """ Get: Cells(self: CellSet) -> CellCollection """
        ...

    @property
    def FilterAxis(self) -> Axis:
        """ Get: FilterAxis(self: CellSet) -> Axis """
        ...

    @property
    def OlapInfo(self) -> OlapInfo:
        """ Get: OlapInfo(self: CellSet) -> OlapInfo """
        ...


    @staticmethod
    def LoadXml(xmlTextReader:XmlReader) -> CellSet:
        """ LoadXml(xmlTextReader: XmlReader) -> CellSet """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class ConnectionExceptionCause(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConnectionExceptionCause, values: AuthenticationFailed (1), Unspecified (0) """
    AuthenticationFailed: ConnectionExceptionCause = ...
    Unspecified: ConnectionExceptionCause = ...
    value__ = ...


class CubeCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> CubeDef:
        """ Find(self: CubeCollection, index: str) -> CubeDef """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: CubeCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class CubeDef(IAdomdBaseObject, IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Caption(self) -> str:
        """ Get: Caption(self: CubeDef) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: CubeDef) -> str """
        ...

    @property
    def Dimensions(self) -> DimensionCollection:
        """ Get: Dimensions(self: CubeDef) -> DimensionCollection """
        ...

    @property
    def Kpis(self) -> KpiCollection:
        """ Get: Kpis(self: CubeDef) -> KpiCollection """
        ...

    @property
    def LastProcessed(self) -> DateTime:
        """ Get: LastProcessed(self: CubeDef) -> DateTime """
        ...

    @property
    def LastUpdated(self) -> DateTime:
        """ Get: LastUpdated(self: CubeDef) -> DateTime """
        ...

    @property
    def Measures(self) -> MeasureCollection:
        """ Get: Measures(self: CubeDef) -> MeasureCollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: CubeDef) -> str """
        ...

    @property
    def NamedSets(self) -> NamedSetCollection:
        """ Get: NamedSets(self: CubeDef) -> NamedSetCollection """
        ...

    @property
    def ParentConnection(self) -> AdomdConnection:
        """ Get: ParentConnection(self: CubeDef) -> AdomdConnection """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: CubeDef) -> PropertyCollection """
        ...

    @property
    def Type(self) -> CubeType:
        """ Get: Type(self: CubeDef) -> CubeType """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: CubeDef, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CubeDef) -> int """
        ...

    def GetSchemaObject(self, schemaObjectType:SchemaObjectType, uniqueName:str, retryUniqueNameOnServer:bool = ...) -> object:
        """
        GetSchemaObject(self: CubeDef, schemaObjectType: SchemaObjectType, uniqueName: str) -> object
        GetSchemaObject(self: CubeDef, schemaObjectType: SchemaObjectType, uniqueName: str, retryUniqueNameOnServer: bool) -> object
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: CubeDef) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CubeInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Cubes(self) -> OlapInfoCubeCollection:
        """ Get: Cubes(self: CubeInfo) -> OlapInfoCubeCollection """
        ...



class CubeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CubeType, values: Cube (1), Dimension (2), Unknown (0) """
    Cube: CubeType = ...
    Dimension: CubeType = ...
    Unknown: CubeType = ...
    value__ = ...


class Dimension(IAdomdBaseObject, IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AttributeHierarchies(self) -> HierarchyCollection:
        """ Get: AttributeHierarchies(self: Dimension) -> HierarchyCollection """
        ...

    @property
    def Caption(self) -> str:
        """ Get: Caption(self: Dimension) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: Dimension) -> str """
        ...

    @property
    def DimensionType(self) -> DimensionTypeEnum:
        """ Get: DimensionType(self: Dimension) -> DimensionTypeEnum """
        ...

    @property
    def Hierarchies(self) -> HierarchyCollection:
        """ Get: Hierarchies(self: Dimension) -> HierarchyCollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Dimension) -> str """
        ...

    @property
    def ParentCube(self) -> CubeDef:
        """ Get: ParentCube(self: Dimension) -> CubeDef """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: Dimension) -> PropertyCollection """
        ...

    @property
    def UniqueName(self) -> str:
        """ Get: UniqueName(self: Dimension) -> str """
        ...

    @property
    def WriteEnabled(self) -> bool:
        """ Get: WriteEnabled(self: Dimension) -> bool """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Dimension, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Dimension) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Dimension) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DimensionCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> Dimension:
        """ Find(self: DimensionCollection, index: str) -> Dimension """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: DimensionCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class DimensionTypeEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DimensionTypeEnum, values: Accounts (6), BillOfMaterials (16), Channel (13), Currency (11), Customers (7), Geography (17), Measure (2), Organization (15), Other (3), Products (8), Promotion (14), Quantitative (5), Rates (12), Scenario (9), Time (1), Unknown (0), Utility (10) """
    Accounts: DimensionTypeEnum = ...
    BillOfMaterials: DimensionTypeEnum = ...
    Channel: DimensionTypeEnum = ...
    Currency: DimensionTypeEnum = ...
    Customers: DimensionTypeEnum = ...
    Geography: DimensionTypeEnum = ...
    Measure: DimensionTypeEnum = ...
    Organization: DimensionTypeEnum = ...
    Other: DimensionTypeEnum = ...
    Products: DimensionTypeEnum = ...
    Promotion: DimensionTypeEnum = ...
    Quantitative: DimensionTypeEnum = ...
    Rates: DimensionTypeEnum = ...
    Scenario: DimensionTypeEnum = ...
    Time: DimensionTypeEnum = ...
    Unknown: DimensionTypeEnum = ...
    Utility: DimensionTypeEnum = ...
    value__ = ...


class Hierarchy(IAdomdBaseObject, IMetadataObject, ISubordinateObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Caption(self) -> str:
        """ Get: Caption(self: Hierarchy) -> str """
        ...

    @property
    def DefaultMember(self) -> str:
        """ Get: DefaultMember(self: Hierarchy) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: Hierarchy) -> str """
        ...

    @property
    def DisplayFolder(self) -> str:
        """ Get: DisplayFolder(self: Hierarchy) -> str """
        ...

    @property
    def HierarchyOrigin(self) -> HierarchyOrigin:
        """ Get: HierarchyOrigin(self: Hierarchy) -> HierarchyOrigin """
        ...

    @property
    def Levels(self) -> LevelCollection:
        """ Get: Levels(self: Hierarchy) -> LevelCollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Hierarchy) -> str """
        ...

    @property
    def ParentDimension(self) -> Dimension:
        """ Get: ParentDimension(self: Hierarchy) -> Dimension """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: Hierarchy) -> PropertyCollection """
        ...

    @property
    def UniqueName(self) -> str:
        """ Get: UniqueName(self: Hierarchy) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Hierarchy, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Hierarchy) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Hierarchy) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class HierarchyCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> Hierarchy:
        """ Find(self: HierarchyCollection, index: str) -> Hierarchy """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: HierarchyCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class HierarchyOrigin(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HierarchyOrigin, values: AttributeHierarchy (2), ParentChildHierarchy (3), UserHierarchy (1) """
    AttributeHierarchy: HierarchyOrigin = ...
    ParentChildHierarchy: HierarchyOrigin = ...
    UserHierarchy: HierarchyOrigin = ...
    value__ = ...


class IAadAuthenticator: # skipped bases: <type 'object'>
    """ no doc """
    def AcquireToken(self, resource:str, dataSource:str, identityProvider:str, tenantId:str, userId:str, password:str, useAdalCache:bool, useAdTranslation:bool) -> AadTokenHolder:
        """ AcquireToken(self: IAadAuthenticator, resource: str, dataSource: str, identityProvider: str, tenantId: str, userId: str, password: str, useAdalCache: bool, useAdTranslation: bool) -> AadTokenHolder """
        ...


class IAadTokenHolder: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DisplayableId(self) -> str:
        """ Get: DisplayableId(self: IAadTokenHolder) -> str """
        ...

    @property
    def FamilyName(self) -> str:
        """ Get: FamilyName(self: IAadTokenHolder) -> str """
        ...

    @property
    def GivenName(self) -> str:
        """ Get: GivenName(self: IAadTokenHolder) -> str """
        ...

    @property
    def IdentityProvider(self) -> str:
        """ Get: IdentityProvider(self: IAadTokenHolder) -> str """
        ...

    @property
    def TenantId(self) -> str:
        """ Get: TenantId(self: IAadTokenHolder) -> str """
        ...


    def GetValidAccessToken(self) -> str:
        """ GetValidAccessToken(self: IAadTokenHolder) -> str """
        ...


class Kpi(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Caption(self) -> str:
        """ Get: Caption(self: Kpi) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: Kpi) -> str """
        ...

    @property
    def DisplayFolder(self) -> str:
        """ Get: DisplayFolder(self: Kpi) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Kpi) -> str """
        ...

    @property
    def ParentCube(self) -> CubeDef:
        """ Get: ParentCube(self: Kpi) -> CubeDef """
        ...

    @property
    def ParentKpi(self) -> Kpi:
        """ Get: ParentKpi(self: Kpi) -> Kpi """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: Kpi) -> PropertyCollection """
        ...

    @property
    def StatusGraphic(self) -> str:
        """ Get: StatusGraphic(self: Kpi) -> str """
        ...

    @property
    def TrendGraphic(self) -> str:
        """ Get: TrendGraphic(self: Kpi) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Kpi, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Kpi) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Kpi) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class KpiCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> Kpi:
        """ Find(self: KpiCollection, index: str) -> Kpi """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: KpiCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class Level(IAdomdBaseObject, IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Caption(self) -> str:
        """ Get: Caption(self: Level) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: Level) -> str """
        ...

    @property
    def LevelNumber(self) -> int:
        """ Get: LevelNumber(self: Level) -> int """
        ...

    @property
    def LevelProperties(self) -> LevelPropertyCollection:
        """ Get: LevelProperties(self: Level) -> LevelPropertyCollection """
        ...

    @property
    def LevelType(self) -> LevelTypeEnum:
        """ Get: LevelType(self: Level) -> LevelTypeEnum """
        ...

    @property
    def MemberCount(self) -> Int64:
        """ Get: MemberCount(self: Level) -> Int64 """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Level) -> str """
        ...

    @property
    def ParentHierarchy(self) -> Hierarchy:
        """ Get: ParentHierarchy(self: Level) -> Hierarchy """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: Level) -> PropertyCollection """
        ...

    @property
    def UniqueName(self) -> str:
        """ Get: UniqueName(self: Level) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Level, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Level) -> int """
        ...

    def GetMembers(self, start:Int64 = ..., count:Int64 = ..., *__args:Array) -> MemberCollection:
        """
        GetMembers(self: Level) -> MemberCollection
        GetMembers(self: Level, start: Int64, count: Int64) -> MemberCollection
        GetMembers(self: Level, start: Int64, count: Int64, *filters: Array[MemberFilter]) -> MemberCollection
        GetMembers(self: Level, start: Int64, count: Int64, properties: Array[str], *filters: Array[MemberFilter]) -> MemberCollection
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: Level) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LevelCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> Level:
        """ Find(self: LevelCollection, index: str) -> Level """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: LevelCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class LevelProperty(ISubordinateObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Caption(self) -> str:
        """ Get: Caption(self: LevelProperty) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: LevelProperty) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: LevelProperty) -> str """
        ...

    @property
    def ParentLevel(self) -> Level:
        """ Get: ParentLevel(self: LevelProperty) -> Level """
        ...

    @property
    def UniqueName(self) -> str:
        """ Get: UniqueName(self: LevelProperty) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: LevelProperty, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: LevelProperty) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: LevelProperty) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LevelPropertyCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> LevelProperty:
        """ Find(self: LevelPropertyCollection, index: str) -> LevelProperty """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: LevelPropertyCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class LevelTypeEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LevelTypeEnum, values: Account (4116), All (1), BomResource (4114), Calculated (2), Channel (4193), Company (4162), CurrencyDestination (4178), CurrencySource (4177), Customer (4129), CustomerGroup (4130), CustomerHousehold (4131), GeoCity (8198), GeoContinent (8193), GeoCountry (8195), GeoCounty (8197), GeoPoint (8200), GeoPostalCode (8199), GeoRegion (8194), GeoStateOrProvince (8196), OrgUnit (4113), Person (4161), Product (4145), ProductGroup (4146), Promotion (4209), Quantitative (4115), Regular (0), Representative (4194), Reserved1 (8), Scenario (4117), Time (4), TimeDays (516), TimeHalfYears (36), TimeHours (772), TimeMinutes (1028), TimeMonths (132), TimeQuarters (68), TimeSeconds (2052), TimeUndefined (4100), TimeWeeks (260), TimeYears (20), Utility (4118) """
    Account: LevelTypeEnum = ...
    All: LevelTypeEnum = ...
    BomResource: LevelTypeEnum = ...
    Calculated: LevelTypeEnum = ...
    Channel: LevelTypeEnum = ...
    Company: LevelTypeEnum = ...
    CurrencyDestination: LevelTypeEnum = ...
    CurrencySource: LevelTypeEnum = ...
    Customer: LevelTypeEnum = ...
    CustomerGroup: LevelTypeEnum = ...
    CustomerHousehold: LevelTypeEnum = ...
    GeoCity: LevelTypeEnum = ...
    GeoContinent: LevelTypeEnum = ...
    GeoCountry: LevelTypeEnum = ...
    GeoCounty: LevelTypeEnum = ...
    GeoPoint: LevelTypeEnum = ...
    GeoPostalCode: LevelTypeEnum = ...
    GeoRegion: LevelTypeEnum = ...
    GeoStateOrProvince: LevelTypeEnum = ...
    OrgUnit: LevelTypeEnum = ...
    Person: LevelTypeEnum = ...
    Product: LevelTypeEnum = ...
    ProductGroup: LevelTypeEnum = ...
    Promotion: LevelTypeEnum = ...
    Quantitative: LevelTypeEnum = ...
    Regular: LevelTypeEnum = ...
    Representative: LevelTypeEnum = ...
    Reserved1: LevelTypeEnum = ...
    Scenario: LevelTypeEnum = ...
    Time: LevelTypeEnum = ...
    TimeDays: LevelTypeEnum = ...
    TimeHalfYears: LevelTypeEnum = ...
    TimeHours: LevelTypeEnum = ...
    TimeMinutes: LevelTypeEnum = ...
    TimeMonths: LevelTypeEnum = ...
    TimeQuarters: LevelTypeEnum = ...
    TimeSeconds: LevelTypeEnum = ...
    TimeUndefined: LevelTypeEnum = ...
    TimeWeeks: LevelTypeEnum = ...
    TimeYears: LevelTypeEnum = ...
    Utility: LevelTypeEnum = ...
    value__ = ...


class Measure(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Caption(self) -> str:
        """ Get: Caption(self: Measure) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: Measure) -> str """
        ...

    @property
    def DisplayFolder(self) -> str:
        """ Get: DisplayFolder(self: Measure) -> str """
        ...

    @property
    def Expression(self) -> str:
        """ Get: Expression(self: Measure) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Measure) -> str """
        ...

    @property
    def NumericPrecision(self) -> int:
        """ Get: NumericPrecision(self: Measure) -> int """
        ...

    @property
    def NumericScale(self) -> Int16:
        """ Get: NumericScale(self: Measure) -> Int16 """
        ...

    @property
    def ParentCube(self) -> CubeDef:
        """ Get: ParentCube(self: Measure) -> CubeDef """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: Measure) -> PropertyCollection """
        ...

    @property
    def UniqueName(self) -> str:
        """ Get: UniqueName(self: Measure) -> str """
        ...

    @property
    def Units(self) -> str:
        """ Get: Units(self: Measure) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Measure, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Measure) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Measure) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MeasureCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> Measure:
        """ Find(self: MeasureCollection, index: str) -> Measure """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: MeasureCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class Member(IAdomdBaseObject, IMetadataObject, ISubordinateObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Caption(self) -> str:
        """ Get: Caption(self: Member) -> str """
        ...

    @property
    def ChildCount(self) -> Int64:
        """ Get: ChildCount(self: Member) -> Int64 """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: Member) -> str """
        ...

    @property
    def DrilledDown(self) -> bool:
        """ Get: DrilledDown(self: Member) -> bool """
        ...

    @property
    def LevelDepth(self) -> int:
        """ Get: LevelDepth(self: Member) -> int """
        ...

    @property
    def LevelName(self) -> str:
        """ Get: LevelName(self: Member) -> str """
        ...

    @property
    def MemberProperties(self) -> MemberPropertyCollection:
        """ Get: MemberProperties(self: Member) -> MemberPropertyCollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Member) -> str """
        ...

    @property
    def Parent(self) -> Member:
        """ Get: Parent(self: Member) -> Member """
        ...

    @property
    def ParentLevel(self) -> Level:
        """ Get: ParentLevel(self: Member) -> Level """
        ...

    @property
    def ParentSameAsPrevious(self) -> bool:
        """ Get: ParentSameAsPrevious(self: Member) -> bool """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: Member) -> PropertyCollection """
        ...

    @property
    def Type(self) -> MemberTypeEnum:
        """ Get: Type(self: Member) -> MemberTypeEnum """
        ...

    @property
    def UniqueName(self) -> str:
        """ Get: UniqueName(self: Member) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Member, obj: object) -> bool """
        ...

    def FetchAllProperties(self): # -> 
        """ FetchAllProperties(self: Member) """
        ...

    def GetChildren(self, start:Int64 = ..., count:Int64 = ..., *__args:Array) -> MemberCollection:
        """
        GetChildren(self: Member) -> MemberCollection
        GetChildren(self: Member, start: Int64, count: Int64) -> MemberCollection
        GetChildren(self: Member, start: Int64, count: Int64, *filters: Array[MemberFilter]) -> MemberCollection
        GetChildren(self: Member, start: Int64, count: Int64, properties: Array[str], *filters: Array[MemberFilter]) -> MemberCollection
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Member) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Member) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MemberCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> Member:
        """ Find(self: MemberCollection, index: str) -> Member """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: MemberCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class MemberFilter: # skipped bases: <type 'object'>, <type 'object'>
    """
    MemberFilter(propertyName: str, propertyValue: str)
    MemberFilter(propertyName: str, filterType: MemberFilterType, propertyValue: str)
    """
    @property
    def FilterType(self) -> MemberFilterType:
        """
        Get: FilterType(self: MemberFilter) -> MemberFilterType
        Set: FilterType(self: MemberFilter) = value
        """
        ...

    @property
    def PropertyName(self) -> str:
        """
        Get: PropertyName(self: MemberFilter) -> str
        Set: PropertyName(self: MemberFilter) = value
        """
        ...

    @property
    def PropertyValue(self) -> str:
        """
        Get: PropertyValue(self: MemberFilter) -> str
        Set: PropertyValue(self: MemberFilter) = value
        """
        ...



class MemberFilterType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MemberFilterType, values: BeginsWith (2), Contains (4), EndsWith (3), Equals (1) """
    BeginsWith: MemberFilterType = ...
    Contains: MemberFilterType = ...
    EndsWith: MemberFilterType = ...
    Equals: MemberFilterType = ...
    value__ = ...


class MemberProperty(ISubordinateObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: MemberProperty) -> str """
        ...

    @property
    def UniqueName(self) -> str:
        """ Get: UniqueName(self: MemberProperty) -> str """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: MemberProperty) -> object """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: MemberProperty, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MemberProperty) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: MemberProperty) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MemberPropertyCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> MemberProperty:
        """ Find(self: MemberPropertyCollection, index: str) -> MemberProperty """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: MemberPropertyCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class MemberTypeEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MemberTypeEnum, values: All (2), Formula (4), Measure (3), Regular (1), Unknown (0) """
    All: MemberTypeEnum = ...
    Formula: MemberTypeEnum = ...
    Measure: MemberTypeEnum = ...
    Regular: MemberTypeEnum = ...
    Unknown: MemberTypeEnum = ...
    value__ = ...


class MiningAttribute: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AttributeID(self) -> int:
        """ Get: AttributeID(self: MiningAttribute) -> int """
        ...

    @property
    def FeatureSelection(self) -> MiningFeatureSelection:
        """ Get: FeatureSelection(self: MiningAttribute) -> MiningFeatureSelection """
        ...

    @property
    def IsInput(self) -> bool:
        """ Get: IsInput(self: MiningAttribute) -> bool """
        ...

    @property
    def IsPredictable(self) -> bool:
        """ Get: IsPredictable(self: MiningAttribute) -> bool """
        ...

    @property
    def KeyColumn(self) -> MiningModelColumn:
        """ Get: KeyColumn(self: MiningAttribute) -> MiningModelColumn """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MiningAttribute) -> str """
        ...

    @property
    def ShortName(self) -> str:
        """ Get: ShortName(self: MiningAttribute) -> str """
        ...

    @property
    def ValueColumn(self) -> MiningModelColumn:
        """ Get: ValueColumn(self: MiningAttribute) -> MiningModelColumn """
        ...



class MiningAttributeCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> MiningAttribute:
        """ Find(self: MiningAttributeCollection, index: str) -> MiningAttribute """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: MiningAttributeCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class MiningColumnDistribution(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MiningColumnDistribution, values: Custom (4), LogNormal (3), Missing (0), Normal (1), Uniform (2) """
    Custom: MiningColumnDistribution = ...
    LogNormal: MiningColumnDistribution = ...
    Missing: MiningColumnDistribution = ...
    Normal: MiningColumnDistribution = ...
    Uniform: MiningColumnDistribution = ...
    value__ = ...


class MiningColumnType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MiningColumnType, values: Boolean (3), Custom (1), Date (6), Double (5), Long (2), Missing (0), Table (7), Text (4) """
    Boolean: MiningColumnType = ...
    Custom: MiningColumnType = ...
    Date: MiningColumnType = ...
    Double: MiningColumnType = ...
    Long: MiningColumnType = ...
    Missing: MiningColumnType = ...
    Table: MiningColumnType = ...
    Text: MiningColumnType = ...
    value__ = ...


class MiningContentNode(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Ancestors(self) -> MiningContentNodeCollection:
        """ Get: Ancestors(self: MiningContentNode) -> MiningContentNodeCollection """
        ...

    @property
    def Attribute(self) -> MiningAttribute:
        """ Get: Attribute(self: MiningContentNode) -> MiningAttribute """
        ...

    @property
    def Caption(self) -> str:
        """ Get: Caption(self: MiningContentNode) -> str """
        ...

    @property
    def Children(self) -> MiningContentNodeCollection:
        """ Get: Children(self: MiningContentNode) -> MiningContentNodeCollection """
        ...

    @property
    def Descendants(self) -> MiningContentNodeCollection:
        """ Get: Descendants(self: MiningContentNode) -> MiningContentNodeCollection """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: MiningContentNode) -> str """
        ...

    @property
    def Distribution(self) -> MiningDistributionCollection:
        """ Get: Distribution(self: MiningContentNode) -> MiningDistributionCollection """
        ...

    @property
    def MarginalProbability(self) -> float:
        """ Get: MarginalProbability(self: MiningContentNode) -> float """
        ...

    @property
    def MarginalRule(self) -> str:
        """ Get: MarginalRule(self: MiningContentNode) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MiningContentNode) -> str """
        ...

    @property
    def NodeRule(self) -> str:
        """ Get: NodeRule(self: MiningContentNode) -> str """
        ...

    @property
    def ParentMiningModel(self) -> MiningModel:
        """ Get: ParentMiningModel(self: MiningContentNode) -> MiningModel """
        ...

    @property
    def ParentNode(self) -> MiningContentNode:
        """ Get: ParentNode(self: MiningContentNode) -> MiningContentNode """
        ...

    @property
    def ParentUniqueName(self) -> str:
        """ Get: ParentUniqueName(self: MiningContentNode) -> str """
        ...

    @property
    def Probability(self) -> float:
        """ Get: Probability(self: MiningContentNode) -> float """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: MiningContentNode) -> PropertyCollection """
        ...

    @property
    def Score(self) -> float:
        """ Get: Score(self: MiningContentNode) -> float """
        ...

    @property
    def ShortCaption(self) -> str:
        """ Get: ShortCaption(self: MiningContentNode) -> str """
        ...

    @property
    def Siblings(self) -> MiningContentNodeCollection:
        """ Get: Siblings(self: MiningContentNode) -> MiningContentNodeCollection """
        ...

    @property
    def Support(self) -> float:
        """ Get: Support(self: MiningContentNode) -> float """
        ...

    @property
    def Type(self) -> MiningNodeType:
        """ Get: Type(self: MiningContentNode) -> MiningNodeType """
        ...

    @property
    def UniqueName(self) -> str:
        """ Get: UniqueName(self: MiningContentNode) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: MiningContentNode, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MiningContentNode) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: MiningContentNode) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MiningContentNodeCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> MiningContentNode:
        """ Find(self: MiningContentNodeCollection, index: str) -> MiningContentNode """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: MiningContentNodeCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class MiningDistribution(ISubordinateObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attribute(self) -> MiningAttribute:
        """ Get: Attribute(self: MiningDistribution) -> MiningAttribute """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MiningDistribution) -> str """
        ...

    @property
    def ParentMiningModel(self) -> MiningModel:
        """ Get: ParentMiningModel(self: MiningDistribution) -> MiningModel """
        ...

    @property
    def ParentNode(self) -> MiningContentNode:
        """ Get: ParentNode(self: MiningDistribution) -> MiningContentNode """
        ...

    @property
    def Probability(self) -> float:
        """ Get: Probability(self: MiningDistribution) -> float """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: MiningDistribution) -> PropertyCollection """
        ...

    @property
    def Support(self) -> float:
        """ Get: Support(self: MiningDistribution) -> float """
        ...

    @property
    def Value(self) -> MiningValue:
        """ Get: Value(self: MiningDistribution) -> MiningValue """
        ...

    @property
    def ValueType(self) -> MiningValueType:
        """ Get: ValueType(self: MiningDistribution) -> MiningValueType """
        ...

    @property
    def Variance(self) -> float:
        """ Get: Variance(self: MiningDistribution) -> float """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: MiningDistribution, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MiningDistribution) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: MiningDistribution) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MiningDistributionCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: MiningDistributionCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class MiningFeatureSelection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MiningFeatureSelection, values: All (0), Input (4), InputAndOutput (12), NotSelected (1), Output (8), Selected (2) """
    All: MiningFeatureSelection = ...
    Input: MiningFeatureSelection = ...
    InputAndOutput: MiningFeatureSelection = ...
    NotSelected: MiningFeatureSelection = ...
    Output: MiningFeatureSelection = ...
    Selected: MiningFeatureSelection = ...
    value__ = ...


class MiningModel(IAdomdBaseObject, IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Algorithm(self) -> str:
        """ Get: Algorithm(self: MiningModel) -> str """
        ...

    @property
    def AllowDrillThrough(self) -> bool:
        """ Get: AllowDrillThrough(self: MiningModel) -> bool """
        ...

    @property
    def Attributes(self) -> MiningAttributeCollection:
        """ Get: Attributes(self: MiningModel) -> MiningAttributeCollection """
        ...

    @property
    def Columns(self) -> MiningModelColumnCollection:
        """ Get: Columns(self: MiningModel) -> MiningModelColumnCollection """
        ...

    @property
    def Content(self) -> MiningContentNodeCollection:
        """ Get: Content(self: MiningModel) -> MiningContentNodeCollection """
        ...

    @property
    def Created(self) -> DateTime:
        """ Get: Created(self: MiningModel) -> DateTime """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: MiningModel) -> str """
        ...

    @property
    def Filter(self) -> str:
        """ Get: Filter(self: MiningModel) -> str """
        ...

    @property
    def IsProcessed(self) -> bool:
        """ Get: IsProcessed(self: MiningModel) -> bool """
        ...

    @property
    def LastProcessed(self) -> DateTime:
        """ Get: LastProcessed(self: MiningModel) -> DateTime """
        ...

    @property
    def LastUpdated(self) -> DateTime:
        """ Get: LastUpdated(self: MiningModel) -> DateTime """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MiningModel) -> str """
        ...

    @property
    def Parameters(self) -> MiningParameterCollection:
        """ Get: Parameters(self: MiningModel) -> MiningParameterCollection """
        ...

    @property
    def Parent(self) -> MiningStructure:
        """ Get: Parent(self: MiningModel) -> MiningStructure """
        ...

    @property
    def ParentConnection(self) -> AdomdConnection:
        """ Get: ParentConnection(self: MiningModel) -> AdomdConnection """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: MiningModel) -> PropertyCollection """
        ...

    @property
    def TrainingSetSize(self) -> Int64:
        """ Get: TrainingSetSize(self: MiningModel) -> Int64 """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: MiningModel, obj: object) -> bool """
        ...

    def FindAttribute(self, attributeId:int) -> MiningAttribute:
        """ FindAttribute(self: MiningModel, attributeId: int) -> MiningAttribute """
        ...

    def GetAttributes(self, filter:MiningFeatureSelection) -> MiningAttributeCollection:
        """ GetAttributes(self: MiningModel, filter: MiningFeatureSelection) -> MiningAttributeCollection """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MiningModel) -> int """
        ...

    def GetNodeFromUniqueName(self, nodeUniqueName:str) -> MiningContentNode:
        """ GetNodeFromUniqueName(self: MiningModel, nodeUniqueName: str) -> MiningContentNode """
        ...

    def ToString(self) -> str:
        """ ToString(self: MiningModel) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MiningModelCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> MiningModel:
        """ Find(self: MiningModelCollection, index: str) -> MiningModel """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: MiningModelCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class MiningModelColumn(IAdomdBaseObject, IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Columns(self) -> MiningModelColumnCollection:
        """ Get: Columns(self: MiningModelColumn) -> MiningModelColumnCollection """
        ...

    @property
    def ContainingColumn(self) -> str:
        """ Get: ContainingColumn(self: MiningModelColumn) -> str """
        ...

    @property
    def Content(self) -> str:
        """ Get: Content(self: MiningModelColumn) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: MiningModelColumn) -> str """
        ...

    @property
    def Distribution(self) -> MiningColumnDistribution:
        """ Get: Distribution(self: MiningModelColumn) -> MiningColumnDistribution """
        ...

    @property
    def Filter(self) -> str:
        """ Get: Filter(self: MiningModelColumn) -> str """
        ...

    @property
    def Flags(self) -> str:
        """ Get: Flags(self: MiningModelColumn) -> str """
        ...

    @property
    def FullyQualifiedName(self) -> str:
        """ Get: FullyQualifiedName(self: MiningModelColumn) -> str """
        ...

    @property
    def IsInput(self) -> bool:
        """ Get: IsInput(self: MiningModelColumn) -> bool """
        ...

    @property
    def IsPredictable(self) -> bool:
        """ Get: IsPredictable(self: MiningModelColumn) -> bool """
        ...

    @property
    def IsProcessed(self) -> bool:
        """ Get: IsProcessed(self: MiningModelColumn) -> bool """
        ...

    @property
    def IsRelatedToKey(self) -> bool:
        """ Get: IsRelatedToKey(self: MiningModelColumn) -> bool """
        ...

    @property
    def IsTable(self) -> bool:
        """ Get: IsTable(self: MiningModelColumn) -> bool """
        ...

    @property
    def LastProcessed(self) -> DateTime:
        """ Get: LastProcessed(self: MiningModelColumn) -> DateTime """
        ...

    @property
    def LastUpdated(self) -> DateTime:
        """ Get: LastUpdated(self: MiningModelColumn) -> DateTime """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MiningModelColumn) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: MiningModelColumn) -> object """
        ...

    @property
    def ParentMiningModel(self) -> MiningModel:
        """ Get: ParentMiningModel(self: MiningModelColumn) -> MiningModel """
        ...

    @property
    def PredictionScore(self) -> float:
        """ Get: PredictionScore(self: MiningModelColumn) -> float """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: MiningModelColumn) -> PropertyCollection """
        ...

    @property
    def RelatedAttribute(self) -> str:
        """ Get: RelatedAttribute(self: MiningModelColumn) -> str """
        ...

    @property
    def StructureColumn(self) -> str:
        """ Get: StructureColumn(self: MiningModelColumn) -> str """
        ...

    @property
    def Type(self) -> MiningColumnType:
        """ Get: Type(self: MiningModelColumn) -> MiningColumnType """
        ...

    @property
    def UniqueName(self) -> str:
        """ Get: UniqueName(self: MiningModelColumn) -> str """
        ...

    @property
    def Values(self) -> MiningValueCollection:
        """ Get: Values(self: MiningModelColumn) -> MiningValueCollection """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: MiningModelColumn, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MiningModelColumn) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: MiningModelColumn) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MiningModelColumnCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> MiningModelColumn:
        """ Find(self: MiningModelColumnCollection, index: str) -> MiningModelColumn """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: MiningModelColumnCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class MiningNodeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MiningNodeType, values: ArimaAutoRegressive (29), ArimaMovingAverage (30), ArimaPeriodicStructure (28), ArimaRoot (27), AssociationRule (8), Cluster (5), CustomBase (1000), Distribution (4), InputAttribute (10), InputAttributeState (11), Interior (3), ItemSet (7), Model (1), NaiveBayesMarginalStatNode (26), NNetHiddenLayer (19), NNetHiddenNode (22), NNetInputLayer (18), NNetInputNode (21), NNetMarginalNode (24), NNetOutputLayer (20), NNetOutputNode (23), NNetSubnetwork (17), PredictableAttribute (9), RegressionTreeRoot (25), Sequence (13), TimeSeries (15), Transition (14), Tree (2), TsTree (16), Unknown (6) """
    ArimaAutoRegressive: MiningNodeType = ...
    ArimaMovingAverage: MiningNodeType = ...
    ArimaPeriodicStructure: MiningNodeType = ...
    ArimaRoot: MiningNodeType = ...
    AssociationRule: MiningNodeType = ...
    Cluster: MiningNodeType = ...
    CustomBase: MiningNodeType = ...
    Distribution: MiningNodeType = ...
    InputAttribute: MiningNodeType = ...
    InputAttributeState: MiningNodeType = ...
    Interior: MiningNodeType = ...
    ItemSet: MiningNodeType = ...
    Model: MiningNodeType = ...
    NaiveBayesMarginalStatNode: MiningNodeType = ...
    NNetHiddenLayer: MiningNodeType = ...
    NNetHiddenNode: MiningNodeType = ...
    NNetInputLayer: MiningNodeType = ...
    NNetInputNode: MiningNodeType = ...
    NNetMarginalNode: MiningNodeType = ...
    NNetOutputLayer: MiningNodeType = ...
    NNetOutputNode: MiningNodeType = ...
    NNetSubnetwork: MiningNodeType = ...
    PredictableAttribute: MiningNodeType = ...
    RegressionTreeRoot: MiningNodeType = ...
    Sequence: MiningNodeType = ...
    TimeSeries: MiningNodeType = ...
    Transition: MiningNodeType = ...
    Tree: MiningNodeType = ...
    TsTree: MiningNodeType = ...
    Unknown: MiningNodeType = ...
    value__ = ...


class MiningParameter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: MiningParameter) -> str """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: MiningParameter) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: MiningParameter) -> str """
        ...


class MiningParameterCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, name:str) -> MiningParameter:
        """ Find(self: MiningParameterCollection, name: str) -> MiningParameter """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: MiningParameterCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class MiningService(IAdomdBaseObject, IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AllowsDuplicateKey(self) -> bool:
        """ Get: AllowsDuplicateKey(self: MiningService) -> bool """
        ...

    @property
    def AllowsIncrementalInsert(self) -> bool:
        """ Get: AllowsIncrementalInsert(self: MiningService) -> bool """
        ...

    @property
    def AllowsPMMLInitialization(self) -> bool:
        """ Get: AllowsPMMLInitialization(self: MiningService) -> bool """
        ...

    @property
    def AvailableParameters(self) -> MiningServiceParameterCollection:
        """ Get: AvailableParameters(self: MiningService) -> MiningServiceParameterCollection """
        ...

    @property
    def Control(self) -> MiningServiceControl:
        """ Get: Control(self: MiningService) -> MiningServiceControl """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: MiningService) -> str """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: MiningService) -> str """
        ...

    @property
    def ExpectedQuality(self) -> MiningServiceExpectedQuality:
        """ Get: ExpectedQuality(self: MiningService) -> MiningServiceExpectedQuality """
        ...

    @property
    def Guid(self) -> str:
        """ Get: Guid(self: MiningService) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MiningService) -> str """
        ...

    @property
    def ParentConnection(self) -> AdomdConnection:
        """ Get: ParentConnection(self: MiningService) -> AdomdConnection """
        ...

    @property
    def PredictionComplexity(self) -> MiningServicePredictionComplexity:
        """ Get: PredictionComplexity(self: MiningService) -> MiningServicePredictionComplexity """
        ...

    @property
    def PredictionLimit(self) -> int:
        """ Get: PredictionLimit(self: MiningService) -> int """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: MiningService) -> PropertyCollection """
        ...

    @property
    def Scaling(self) -> MiningServiceScaling:
        """ Get: Scaling(self: MiningService) -> MiningServiceScaling """
        ...

    @property
    def SupportedDistributionFlags(self) -> Array:
        """ Get: SupportedDistributionFlags(self: MiningService) -> Array[MiningColumnDistribution] """
        ...

    @property
    def SupportedInputContentTypes(self) -> Array:
        """ Get: SupportedInputContentTypes(self: MiningService) -> Array[str] """
        ...

    @property
    def SupportedModelingFlags(self) -> Array:
        """ Get: SupportedModelingFlags(self: MiningService) -> Array[str] """
        ...

    @property
    def SupportedPredictionContentTypes(self) -> Array:
        """ Get: SupportedPredictionContentTypes(self: MiningService) -> Array[str] """
        ...

    @property
    def SupportsDMDimensions(self) -> bool:
        """ Get: SupportsDMDimensions(self: MiningService) -> bool """
        ...

    @property
    def SupportsDrillthrough(self) -> bool:
        """ Get: SupportsDrillthrough(self: MiningService) -> bool """
        ...

    @property
    def TrainingComplexity(self) -> MiningServiceTrainingComplexity:
        """ Get: TrainingComplexity(self: MiningService) -> MiningServiceTrainingComplexity """
        ...

    @property
    def ViewerType(self) -> str:
        """ Get: ViewerType(self: MiningService) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: MiningService, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MiningService) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: MiningService) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MiningServiceCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> MiningService:
        """ Find(self: MiningServiceCollection, index: str) -> MiningService """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: MiningServiceCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class MiningServiceControl(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MiningServiceControl, values: Cancel (1), None (0), SuspendResume (2), SuspendWithResult (2) """
    Cancel: MiningServiceControl = ...
    SuspendResume: MiningServiceControl = ...
    SuspendWithResult: MiningServiceControl = ...
    value__ = ...


class MiningServiceExpectedQuality(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MiningServiceExpectedQuality, values: High (2), Low (0), Medium (1) """
    High: MiningServiceExpectedQuality = ...
    Low: MiningServiceExpectedQuality = ...
    Medium: MiningServiceExpectedQuality = ...
    value__ = ...


class MiningServiceParameter(IAdomdBaseObject, IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DefaultValue(self) -> str:
        """ Get: DefaultValue(self: MiningServiceParameter) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: MiningServiceParameter) -> str """
        ...

    @property
    def IsRequired(self) -> bool:
        """ Get: IsRequired(self: MiningServiceParameter) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MiningServiceParameter) -> str """
        ...

    @property
    def ParameterType(self) -> str:
        """ Get: ParameterType(self: MiningServiceParameter) -> str """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: MiningServiceParameter) -> PropertyCollection """
        ...

    @property
    def ServiceName(self) -> str:
        """ Get: ServiceName(self: MiningServiceParameter) -> str """
        ...

    @property
    def ValueEnumeration(self) -> str:
        """ Get: ValueEnumeration(self: MiningServiceParameter) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: MiningServiceParameter, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MiningServiceParameter) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: MiningServiceParameter) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MiningServiceParameterCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> MiningServiceParameter:
        """ Find(self: MiningServiceParameterCollection, index: str) -> MiningServiceParameter """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: MiningServiceParameterCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class MiningServicePredictionComplexity(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MiningServicePredictionComplexity, values: High (2), Low (0), Medium (1) """
    High: MiningServicePredictionComplexity = ...
    Low: MiningServicePredictionComplexity = ...
    Medium: MiningServicePredictionComplexity = ...
    value__ = ...


class MiningServiceScaling(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MiningServiceScaling, values: High (2), Low (0), Medium (1) """
    High: MiningServiceScaling = ...
    Low: MiningServiceScaling = ...
    Medium: MiningServiceScaling = ...
    value__ = ...


class MiningServiceTrainingComplexity(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MiningServiceTrainingComplexity, values: High (2), Low (0), Medium (1) """
    High: MiningServiceTrainingComplexity = ...
    Low: MiningServiceTrainingComplexity = ...
    Medium: MiningServiceTrainingComplexity = ...
    value__ = ...


class MiningStructure(IAdomdBaseObject, IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Caption(self) -> str:
        """ Get: Caption(self: MiningStructure) -> str """
        ...

    @property
    def Columns(self) -> MiningStructureColumnCollection:
        """ Get: Columns(self: MiningStructure) -> MiningStructureColumnCollection """
        ...

    @property
    def Created(self) -> DateTime:
        """ Get: Created(self: MiningStructure) -> DateTime """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: MiningStructure) -> str """
        ...

    @property
    def HoldoutActualSize(self) -> Int64:
        """ Get: HoldoutActualSize(self: MiningStructure) -> Int64 """
        ...

    @property
    def HoldoutMaxCases(self) -> Int64:
        """ Get: HoldoutMaxCases(self: MiningStructure) -> Int64 """
        ...

    @property
    def HoldoutMaxPercent(self) -> int:
        """ Get: HoldoutMaxPercent(self: MiningStructure) -> int """
        ...

    @property
    def HoldoutSeed(self) -> Int64:
        """ Get: HoldoutSeed(self: MiningStructure) -> Int64 """
        ...

    @property
    def IsProcessed(self) -> bool:
        """ Get: IsProcessed(self: MiningStructure) -> bool """
        ...

    @property
    def LastProcessed(self) -> DateTime:
        """ Get: LastProcessed(self: MiningStructure) -> DateTime """
        ...

    @property
    def LastUpdated(self) -> DateTime:
        """ Get: LastUpdated(self: MiningStructure) -> DateTime """
        ...

    @property
    def MiningModels(self) -> MiningModelCollection:
        """ Get: MiningModels(self: MiningStructure) -> MiningModelCollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MiningStructure) -> str """
        ...

    @property
    def ParentConnection(self) -> AdomdConnection:
        """ Get: ParentConnection(self: MiningStructure) -> AdomdConnection """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: MiningStructure) -> PropertyCollection """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: MiningStructure, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MiningStructure) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: MiningStructure) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MiningStructureCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> MiningStructure:
        """ Find(self: MiningStructureCollection, index: str) -> MiningStructure """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: MiningStructureCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class MiningStructureColumn(IAdomdBaseObject, IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Columns(self) -> MiningStructureColumnCollection:
        """ Get: Columns(self: MiningStructureColumn) -> MiningStructureColumnCollection """
        ...

    @property
    def ContainingColumn(self) -> str:
        """ Get: ContainingColumn(self: MiningStructureColumn) -> str """
        ...

    @property
    def Content(self) -> str:
        """ Get: Content(self: MiningStructureColumn) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: MiningStructureColumn) -> str """
        ...

    @property
    def Distribution(self) -> MiningColumnDistribution:
        """ Get: Distribution(self: MiningStructureColumn) -> MiningColumnDistribution """
        ...

    @property
    def Flags(self) -> str:
        """ Get: Flags(self: MiningStructureColumn) -> str """
        ...

    @property
    def FullyQualifiedName(self) -> str:
        """ Get: FullyQualifiedName(self: MiningStructureColumn) -> str """
        ...

    @property
    def IsProcessed(self) -> bool:
        """ Get: IsProcessed(self: MiningStructureColumn) -> bool """
        ...

    @property
    def IsRelatedToKey(self) -> bool:
        """ Get: IsRelatedToKey(self: MiningStructureColumn) -> bool """
        ...

    @property
    def LastProcessed(self) -> DateTime:
        """ Get: LastProcessed(self: MiningStructureColumn) -> DateTime """
        ...

    @property
    def LastUpdated(self) -> DateTime:
        """ Get: LastUpdated(self: MiningStructureColumn) -> DateTime """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MiningStructureColumn) -> str """
        ...

    @property
    def Parent(self) -> object:
        """ Get: Parent(self: MiningStructureColumn) -> object """
        ...

    @property
    def ParentMiningStructure(self) -> MiningStructure:
        """ Get: ParentMiningStructure(self: MiningStructureColumn) -> MiningStructure """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: MiningStructureColumn) -> PropertyCollection """
        ...

    @property
    def RelatedAttribute(self) -> str:
        """ Get: RelatedAttribute(self: MiningStructureColumn) -> str """
        ...

    @property
    def Type(self) -> MiningColumnType:
        """ Get: Type(self: MiningStructureColumn) -> MiningColumnType """
        ...

    @property
    def UniqueName(self) -> str:
        """ Get: UniqueName(self: MiningStructureColumn) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: MiningStructureColumn, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MiningStructureColumn) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: MiningStructureColumn) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MiningStructureColumnCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> MiningStructureColumn:
        """ Find(self: MiningStructureColumnCollection, index: str) -> MiningStructureColumn """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: MiningStructureColumnCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class MiningValue: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Index(self) -> int:
        """ Get: Index(self: MiningValue) -> int """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: MiningValue) -> object """
        ...

    @property
    def ValueType(self) -> MiningValueType:
        """ Get: ValueType(self: MiningValue) -> MiningValueType """
        ...


    def ToString(self) -> str:
        """ ToString(self: MiningValue) -> str """
        ...


class MiningValueCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: MiningValueCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class MiningValueType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MiningValueType, values: AutoRegressiveOrder (13), Boolean (6), Coefficient (7), Continuous (3), DifferenceOrder (15), Discrete (4), Discretized (5), Existing (2), Intercept (11), Missing (1), MovingAverageOrder (14), NodeUniqueName (10), Other (16), Periodicity (12), PreRenderedString (-1), RegressorStatistics (9), ScoreGain (8) """
    AutoRegressiveOrder: MiningValueType = ...
    Boolean: MiningValueType = ...
    Coefficient: MiningValueType = ...
    Continuous: MiningValueType = ...
    DifferenceOrder: MiningValueType = ...
    Discrete: MiningValueType = ...
    Discretized: MiningValueType = ...
    Existing: MiningValueType = ...
    Intercept: MiningValueType = ...
    Missing: MiningValueType = ...
    MovingAverageOrder: MiningValueType = ...
    NodeUniqueName: MiningValueType = ...
    Other: MiningValueType = ...
    Periodicity: MiningValueType = ...
    PreRenderedString: MiningValueType = ...
    RegressorStatistics: MiningValueType = ...
    ScoreGain: MiningValueType = ...
    value__ = ...


class NamedSet(IMetadataObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Caption(self) -> str:
        """ Get: Caption(self: NamedSet) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: NamedSet) -> str """
        ...

    @property
    def DisplayFolder(self) -> str:
        """ Get: DisplayFolder(self: NamedSet) -> str """
        ...

    @property
    def Expression(self) -> str:
        """ Get: Expression(self: NamedSet) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: NamedSet) -> str """
        ...

    @property
    def ParentCube(self) -> CubeDef:
        """ Get: ParentCube(self: NamedSet) -> CubeDef """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: NamedSet) -> PropertyCollection """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: NamedSet, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: NamedSet) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: NamedSet) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class NamedSetCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, index:str) -> NamedSet:
        """ Find(self: NamedSetCollection, index: str) -> NamedSet """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: NamedSetCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class OlapInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AxesInfo(self) -> AxesInfo:
        """ Get: AxesInfo(self: OlapInfo) -> AxesInfo """
        ...

    @property
    def CellInfo(self) -> CellInfo:
        """ Get: CellInfo(self: OlapInfo) -> CellInfo """
        ...

    @property
    def CubeInfo(self) -> CubeInfo:
        """ Get: CubeInfo(self: OlapInfo) -> CubeInfo """
        ...



class OlapInfoAxis: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Hierarchies(self) -> OlapInfoHierarchyCollection:
        """ Get: Hierarchies(self: OlapInfoAxis) -> OlapInfoHierarchyCollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: OlapInfoAxis) -> str """
        ...



class OlapInfoAxisCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, name:str) -> OlapInfoAxis:
        """ Find(self: OlapInfoAxisCollection, name: str) -> OlapInfoAxis """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: OlapInfoAxisCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class OlapInfoCube: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CubeName(self) -> str:
        """ Get: CubeName(self: OlapInfoCube) -> str """
        ...

    @property
    def LastDataUpdate(self) -> DateTime:
        """ Get: LastDataUpdate(self: OlapInfoCube) -> DateTime """
        ...

    @property
    def LastSchemaUpdate(self) -> DateTime:
        """ Get: LastSchemaUpdate(self: OlapInfoCube) -> DateTime """
        ...



class OlapInfoCubeCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, name:str) -> OlapInfoCube:
        """ Find(self: OlapInfoCubeCollection, name: str) -> OlapInfoCube """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: OlapInfoCubeCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class OlapInfoHierarchy: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def HierarchyProperties(self) -> OlapInfoPropertyCollection:
        """ Get: HierarchyProperties(self: OlapInfoHierarchy) -> OlapInfoPropertyCollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: OlapInfoHierarchy) -> str """
        ...



class OlapInfoHierarchyCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, name:str) -> OlapInfoHierarchy:
        """ Find(self: OlapInfoHierarchyCollection, name: str) -> OlapInfoHierarchy """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: OlapInfoHierarchyCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class OlapInfoProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: OlapInfoProperty) -> str """
        ...

    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: OlapInfoProperty) -> str """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: OlapInfoProperty) -> Type """
        ...



class OlapInfoPropertyCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, name:str) -> OlapInfoProperty:
        """ Find(self: OlapInfoPropertyCollection, name: str) -> OlapInfoProperty """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: OlapInfoPropertyCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class Position(ISubordinateObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Members(self) -> MemberCollection:
        """ Get: Members(self: Position) -> MemberCollection """
        ...

    @property
    def Ordinal(self) -> int:
        """ Get: Ordinal(self: Position) -> int """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Position, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Position) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PositionCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: PositionCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class Property(ISubordinateObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: Property) -> str """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: Property) -> Type """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: Property) -> object """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Property, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Property) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Property) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PropertyCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Find(self, name:str) -> Property:
        """ Find(self: PropertyCollection, name: str) -> Property """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: PropertyCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class RequestPriorities(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RequestPriorities, values: Low (1), Normal (0) """
    Low: RequestPriorities = ...
    Normal: RequestPriorities = ...
    value__ = ...


class SchemaObjectType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SchemaObjectType, values: ObjectTypeDimension (1), ObjectTypeHierarchy (2), ObjectTypeKpi (7), ObjectTypeLevel (3), ObjectTypeMeasure (6), ObjectTypeMember (4), ObjectTypeMiningContentNode (12), ObjectTypeMiningDistribution (13), ObjectTypeMiningModel (9), ObjectTypeMiningModelColumn (10), ObjectTypeMiningService (14), ObjectTypeMiningServiceParameter (15), ObjectTypeMiningStructure (8), ObjectTypeMiningStructureColumn (11), ObjectTypeNamedSet (20) """
    ObjectTypeDimension: SchemaObjectType = ...
    ObjectTypeHierarchy: SchemaObjectType = ...
    ObjectTypeKpi: SchemaObjectType = ...
    ObjectTypeLevel: SchemaObjectType = ...
    ObjectTypeMeasure: SchemaObjectType = ...
    ObjectTypeMember: SchemaObjectType = ...
    ObjectTypeMiningContentNode: SchemaObjectType = ...
    ObjectTypeMiningDistribution: SchemaObjectType = ...
    ObjectTypeMiningModel: SchemaObjectType = ...
    ObjectTypeMiningModelColumn: SchemaObjectType = ...
    ObjectTypeMiningService: SchemaObjectType = ...
    ObjectTypeMiningServiceParameter: SchemaObjectType = ...
    ObjectTypeMiningStructure: SchemaObjectType = ...
    ObjectTypeMiningStructureColumn: SchemaObjectType = ...
    ObjectTypeNamedSet: SchemaObjectType = ...
    value__ = ...


class Set(ISubordinateObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Hierarchies(self) -> HierarchyCollection:
        """ Get: Hierarchies(self: Set) -> HierarchyCollection """
        ...

    @property
    def Tuples(self) -> TupleCollection:
        """ Get: Tuples(self: Set) -> TupleCollection """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Set, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Set) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Tuple(ISubordinateObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Members(self) -> MemberCollection:
        """ Get: Members(self: Tuple) -> MemberCollection """
        ...

    @property
    def TupleOrdinal(self) -> int:
        """ Get: TupleOrdinal(self: Tuple) -> int """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Tuple, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Tuple) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TupleCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Enumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: TupleCollection) -> Enumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



