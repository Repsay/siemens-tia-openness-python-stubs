# encoding: utf-8
# module Microsoft.SqlServer.Server calls itself Server
# from System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Attribute, Byte, Char, DateTime, DateTimeOffset, 
    Decimal, Enum, Guid, Int16, Int64, Single, SystemException, TimeSpan, 
    Type)

from System.Data import DbType, IDataRecord, SqlDbType

from System.Data.SqlClient import SortOrder, SqlCommand

from System.Data.SqlTypes import (SqlBinary, SqlBoolean, SqlByte, SqlBytes, 
    SqlChars, SqlCompareOptions, SqlDateTime, SqlDecimal, SqlDouble, SqlGuid, 
    SqlInt16, SqlInt32, SqlInt64, SqlMoney, SqlSingle, SqlString, SqlXml)

from System.IO import BinaryReader, BinaryWriter

from System.Security.Principal import WindowsIdentity

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class DataAccessKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataAccessKind, values: None (0), Read (1) """
    Read: DataAccessKind = ...
    value__ = ...


class Format(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Format, values: Native (1), Unknown (0), UserDefined (2) """
    Native: Format = ...
    Unknown: Format = ...
    UserDefined: Format = ...
    value__ = ...


class IBinarySerialize: # skipped bases: <type 'object'>
    """ no doc """
    def Read(self, r:BinaryReader): # -> 
        """ Read(self: IBinarySerialize, r: BinaryReader) """
        ...

    def Write(self, w:BinaryWriter): # -> 
        """ Write(self: IBinarySerialize, w: BinaryWriter) """
        ...


class InvalidUdtException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    SerializeObjectState = ...


class SqlContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsAvailable(self) -> bool:
        """ Get: IsAvailable() -> bool """
        ...

    @property
    def Pipe(self) -> SqlPipe:
        """ Get: Pipe() -> SqlPipe """
        ...

    @property
    def TriggerContext(self) -> SqlTriggerContext:
        """ Get: TriggerContext() -> SqlTriggerContext """
        ...

    @property
    def WindowsIdentity(self) -> WindowsIdentity:
        """ Get: WindowsIdentity() -> WindowsIdentity """
        ...




class SqlDataRecord(IDataRecord): # skipped bases: <type 'object'>
    """ SqlDataRecord(*metaData: Array[SqlMetaData]) """
    def GetDateTimeOffset(self, ordinal:int) -> DateTimeOffset:
        """ GetDateTimeOffset(self: SqlDataRecord, ordinal: int) -> DateTimeOffset """
        ...

    def GetSqlBinary(self, ordinal:int) -> SqlBinary:
        """ GetSqlBinary(self: SqlDataRecord, ordinal: int) -> SqlBinary """
        ...

    def GetSqlBoolean(self, ordinal:int) -> SqlBoolean:
        """ GetSqlBoolean(self: SqlDataRecord, ordinal: int) -> SqlBoolean """
        ...

    def GetSqlByte(self, ordinal:int) -> SqlByte:
        """ GetSqlByte(self: SqlDataRecord, ordinal: int) -> SqlByte """
        ...

    def GetSqlBytes(self, ordinal:int) -> SqlBytes:
        """ GetSqlBytes(self: SqlDataRecord, ordinal: int) -> SqlBytes """
        ...

    def GetSqlChars(self, ordinal:int) -> SqlChars:
        """ GetSqlChars(self: SqlDataRecord, ordinal: int) -> SqlChars """
        ...

    def GetSqlDateTime(self, ordinal:int) -> SqlDateTime:
        """ GetSqlDateTime(self: SqlDataRecord, ordinal: int) -> SqlDateTime """
        ...

    def GetSqlDecimal(self, ordinal:int) -> SqlDecimal:
        """ GetSqlDecimal(self: SqlDataRecord, ordinal: int) -> SqlDecimal """
        ...

    def GetSqlDouble(self, ordinal:int) -> SqlDouble:
        """ GetSqlDouble(self: SqlDataRecord, ordinal: int) -> SqlDouble """
        ...

    def GetSqlFieldType(self, ordinal:int) -> Type:
        """ GetSqlFieldType(self: SqlDataRecord, ordinal: int) -> Type """
        ...

    def GetSqlGuid(self, ordinal:int) -> SqlGuid:
        """ GetSqlGuid(self: SqlDataRecord, ordinal: int) -> SqlGuid """
        ...

    def GetSqlInt16(self, ordinal:int) -> SqlInt16:
        """ GetSqlInt16(self: SqlDataRecord, ordinal: int) -> SqlInt16 """
        ...

    def GetSqlInt32(self, ordinal:int) -> SqlInt32:
        """ GetSqlInt32(self: SqlDataRecord, ordinal: int) -> SqlInt32 """
        ...

    def GetSqlInt64(self, ordinal:int) -> SqlInt64:
        """ GetSqlInt64(self: SqlDataRecord, ordinal: int) -> SqlInt64 """
        ...

    def GetSqlMetaData(self, ordinal:int) -> SqlMetaData:
        """ GetSqlMetaData(self: SqlDataRecord, ordinal: int) -> SqlMetaData """
        ...

    def GetSqlMoney(self, ordinal:int) -> SqlMoney:
        """ GetSqlMoney(self: SqlDataRecord, ordinal: int) -> SqlMoney """
        ...

    def GetSqlSingle(self, ordinal:int) -> SqlSingle:
        """ GetSqlSingle(self: SqlDataRecord, ordinal: int) -> SqlSingle """
        ...

    def GetSqlString(self, ordinal:int) -> SqlString:
        """ GetSqlString(self: SqlDataRecord, ordinal: int) -> SqlString """
        ...

    def GetSqlValue(self, ordinal:int) -> object:
        """ GetSqlValue(self: SqlDataRecord, ordinal: int) -> object """
        ...

    def GetSqlValues(self, values:Array) -> int:
        """ GetSqlValues(self: SqlDataRecord, values: Array[object]) -> int """
        ...

    def GetSqlXml(self, ordinal:int) -> SqlXml:
        """ GetSqlXml(self: SqlDataRecord, ordinal: int) -> SqlXml """
        ...

    def GetTimeSpan(self, ordinal:int) -> TimeSpan:
        """ GetTimeSpan(self: SqlDataRecord, ordinal: int) -> TimeSpan """
        ...

    def SetBoolean(self, ordinal:int, value:bool): # -> 
        """ SetBoolean(self: SqlDataRecord, ordinal: int, value: bool) """
        ...

    def SetByte(self, ordinal:int, value:Byte): # -> 
        """ SetByte(self: SqlDataRecord, ordinal: int, value: Byte) """
        ...

    def SetBytes(self, ordinal:int, fieldOffset:Int64, buffer:Array, bufferOffset:int, length:int): # -> 
        """ SetBytes(self: SqlDataRecord, ordinal: int, fieldOffset: Int64, buffer: Array[Byte], bufferOffset: int, length: int) """
        ...

    def SetChar(self, ordinal:int, value:Char): # -> 
        """ SetChar(self: SqlDataRecord, ordinal: int, value: Char) """
        ...

    def SetChars(self, ordinal:int, fieldOffset:Int64, buffer:Array, bufferOffset:int, length:int): # -> 
        """ SetChars(self: SqlDataRecord, ordinal: int, fieldOffset: Int64, buffer: Array[Char], bufferOffset: int, length: int) """
        ...

    def SetDateTime(self, ordinal:int, value:DateTime): # -> 
        """ SetDateTime(self: SqlDataRecord, ordinal: int, value: DateTime) """
        ...

    def SetDateTimeOffset(self, ordinal:int, value:DateTimeOffset): # -> 
        """ SetDateTimeOffset(self: SqlDataRecord, ordinal: int, value: DateTimeOffset) """
        ...

    def SetDBNull(self, ordinal:int): # -> 
        """ SetDBNull(self: SqlDataRecord, ordinal: int) """
        ...

    def SetDecimal(self, ordinal:int, value:Decimal): # -> 
        """ SetDecimal(self: SqlDataRecord, ordinal: int, value: Decimal) """
        ...

    def SetDouble(self, ordinal:int, value:float): # -> 
        """ SetDouble(self: SqlDataRecord, ordinal: int, value: float) """
        ...

    def SetFloat(self, ordinal:int, value:Single): # -> 
        """ SetFloat(self: SqlDataRecord, ordinal: int, value: Single) """
        ...

    def SetGuid(self, ordinal:int, value:Guid): # -> 
        """ SetGuid(self: SqlDataRecord, ordinal: int, value: Guid) """
        ...

    def SetInt16(self, ordinal:int, value:Int16): # -> 
        """ SetInt16(self: SqlDataRecord, ordinal: int, value: Int16) """
        ...

    def SetInt32(self, ordinal:int, value:int): # -> 
        """ SetInt32(self: SqlDataRecord, ordinal: int, value: int) """
        ...

    def SetInt64(self, ordinal:int, value:Int64): # -> 
        """ SetInt64(self: SqlDataRecord, ordinal: int, value: Int64) """
        ...

    def SetSqlBinary(self, ordinal:int, value:SqlBinary): # -> 
        """ SetSqlBinary(self: SqlDataRecord, ordinal: int, value: SqlBinary) """
        ...

    def SetSqlBoolean(self, ordinal:int, value:SqlBoolean): # -> 
        """ SetSqlBoolean(self: SqlDataRecord, ordinal: int, value: SqlBoolean) """
        ...

    def SetSqlByte(self, ordinal:int, value:SqlByte): # -> 
        """ SetSqlByte(self: SqlDataRecord, ordinal: int, value: SqlByte) """
        ...

    def SetSqlBytes(self, ordinal:int, value:SqlBytes): # -> 
        """ SetSqlBytes(self: SqlDataRecord, ordinal: int, value: SqlBytes) """
        ...

    def SetSqlChars(self, ordinal:int, value:SqlChars): # -> 
        """ SetSqlChars(self: SqlDataRecord, ordinal: int, value: SqlChars) """
        ...

    def SetSqlDateTime(self, ordinal:int, value:SqlDateTime): # -> 
        """ SetSqlDateTime(self: SqlDataRecord, ordinal: int, value: SqlDateTime) """
        ...

    def SetSqlDecimal(self, ordinal:int, value:SqlDecimal): # -> 
        """ SetSqlDecimal(self: SqlDataRecord, ordinal: int, value: SqlDecimal) """
        ...

    def SetSqlDouble(self, ordinal:int, value:SqlDouble): # -> 
        """ SetSqlDouble(self: SqlDataRecord, ordinal: int, value: SqlDouble) """
        ...

    def SetSqlGuid(self, ordinal:int, value:SqlGuid): # -> 
        """ SetSqlGuid(self: SqlDataRecord, ordinal: int, value: SqlGuid) """
        ...

    def SetSqlInt16(self, ordinal:int, value:SqlInt16): # -> 
        """ SetSqlInt16(self: SqlDataRecord, ordinal: int, value: SqlInt16) """
        ...

    def SetSqlInt32(self, ordinal:int, value:SqlInt32): # -> 
        """ SetSqlInt32(self: SqlDataRecord, ordinal: int, value: SqlInt32) """
        ...

    def SetSqlInt64(self, ordinal:int, value:SqlInt64): # -> 
        """ SetSqlInt64(self: SqlDataRecord, ordinal: int, value: SqlInt64) """
        ...

    def SetSqlMoney(self, ordinal:int, value:SqlMoney): # -> 
        """ SetSqlMoney(self: SqlDataRecord, ordinal: int, value: SqlMoney) """
        ...

    def SetSqlSingle(self, ordinal:int, value:SqlSingle): # -> 
        """ SetSqlSingle(self: SqlDataRecord, ordinal: int, value: SqlSingle) """
        ...

    def SetSqlString(self, ordinal:int, value:SqlString): # -> 
        """ SetSqlString(self: SqlDataRecord, ordinal: int, value: SqlString) """
        ...

    def SetSqlXml(self, ordinal:int, value:SqlXml): # -> 
        """ SetSqlXml(self: SqlDataRecord, ordinal: int, value: SqlXml) """
        ...

    def SetString(self, ordinal:int, value:str): # -> 
        """ SetString(self: SqlDataRecord, ordinal: int, value: str) """
        ...

    def SetTimeSpan(self, ordinal:int, value:TimeSpan): # -> 
        """ SetTimeSpan(self: SqlDataRecord, ordinal: int, value: TimeSpan) """
        ...

    def SetValue(self, ordinal:int, value:object): # -> 
        """ SetValue(self: SqlDataRecord, ordinal: int, value: object) """
        ...

    def SetValues(self, values:Array) -> int:
        """ SetValues(self: SqlDataRecord, *values: Array[object]) -> int """
        ...


class SqlFacetAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SqlFacetAttribute() """
    @property
    def IsFixedLength(self) -> bool:
        """
        Get: IsFixedLength(self: SqlFacetAttribute) -> bool
        Set: IsFixedLength(self: SqlFacetAttribute) = value
        """
        ...

    @property
    def IsNullable(self) -> bool:
        """
        Get: IsNullable(self: SqlFacetAttribute) -> bool
        Set: IsNullable(self: SqlFacetAttribute) = value
        """
        ...

    @property
    def MaxSize(self) -> int:
        """
        Get: MaxSize(self: SqlFacetAttribute) -> int
        Set: MaxSize(self: SqlFacetAttribute) = value
        """
        ...

    @property
    def Precision(self) -> int:
        """
        Get: Precision(self: SqlFacetAttribute) -> int
        Set: Precision(self: SqlFacetAttribute) = value
        """
        ...

    @property
    def Scale(self) -> int:
        """
        Get: Scale(self: SqlFacetAttribute) -> int
        Set: Scale(self: SqlFacetAttribute) = value
        """
        ...



class SqlFunctionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SqlFunctionAttribute() """
    @property
    def DataAccess(self) -> DataAccessKind:
        """
        Get: DataAccess(self: SqlFunctionAttribute) -> DataAccessKind
        Set: DataAccess(self: SqlFunctionAttribute) = value
        """
        ...

    @property
    def FillRowMethodName(self) -> str:
        """
        Get: FillRowMethodName(self: SqlFunctionAttribute) -> str
        Set: FillRowMethodName(self: SqlFunctionAttribute) = value
        """
        ...

    @property
    def IsDeterministic(self) -> bool:
        """
        Get: IsDeterministic(self: SqlFunctionAttribute) -> bool
        Set: IsDeterministic(self: SqlFunctionAttribute) = value
        """
        ...

    @property
    def IsPrecise(self) -> bool:
        """
        Get: IsPrecise(self: SqlFunctionAttribute) -> bool
        Set: IsPrecise(self: SqlFunctionAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SqlFunctionAttribute) -> str
        Set: Name(self: SqlFunctionAttribute) = value
        """
        ...

    @property
    def SystemDataAccess(self) -> SystemDataAccessKind:
        """
        Get: SystemDataAccess(self: SqlFunctionAttribute) -> SystemDataAccessKind
        Set: SystemDataAccess(self: SqlFunctionAttribute) = value
        """
        ...

    @property
    def TableDefinition(self) -> str:
        """
        Get: TableDefinition(self: SqlFunctionAttribute) -> str
        Set: TableDefinition(self: SqlFunctionAttribute) = value
        """
        ...



class SqlMetaData: # skipped bases: <type 'object'>, <type 'object'>
    """
    SqlMetaData(name: str, dbType: SqlDbType)
    SqlMetaData(name: str, dbType: SqlDbType, useServerDefault: bool, isUniqueKey: bool, columnSortOrder: SortOrder, sortOrdinal: int)
    SqlMetaData(name: str, dbType: SqlDbType, maxLength: Int64)
    SqlMetaData(name: str, dbType: SqlDbType, maxLength: Int64, useServerDefault: bool, isUniqueKey: bool, columnSortOrder: SortOrder, sortOrdinal: int)
    SqlMetaData(name: str, dbType: SqlDbType, userDefinedType: Type)
    SqlMetaData(name: str, dbType: SqlDbType, userDefinedType: Type, serverTypeName: str)
    SqlMetaData(name: str, dbType: SqlDbType, userDefinedType: Type, serverTypeName: str, useServerDefault: bool, isUniqueKey: bool, columnSortOrder: SortOrder, sortOrdinal: int)
    SqlMetaData(name: str, dbType: SqlDbType, precision: Byte, scale: Byte)
    SqlMetaData(name: str, dbType: SqlDbType, precision: Byte, scale: Byte, useServerDefault: bool, isUniqueKey: bool, columnSortOrder: SortOrder, sortOrdinal: int)
    SqlMetaData(name: str, dbType: SqlDbType, maxLength: Int64, locale: Int64, compareOptions: SqlCompareOptions)
    SqlMetaData(name: str, dbType: SqlDbType, maxLength: Int64, locale: Int64, compareOptions: SqlCompareOptions, useServerDefault: bool, isUniqueKey: bool, columnSortOrder: SortOrder, sortOrdinal: int)
    SqlMetaData(name: str, dbType: SqlDbType, database: str, owningSchema: str, objectName: str, useServerDefault: bool, isUniqueKey: bool, columnSortOrder: SortOrder, sortOrdinal: int)
    SqlMetaData(name: str, dbType: SqlDbType, maxLength: Int64, precision: Byte, scale: Byte, locale: Int64, compareOptions: SqlCompareOptions, userDefinedType: Type)
    SqlMetaData(name: str, dbType: SqlDbType, maxLength: Int64, precision: Byte, scale: Byte, localeId: Int64, compareOptions: SqlCompareOptions, userDefinedType: Type, useServerDefault: bool, isUniqueKey: bool, columnSortOrder: SortOrder, sortOrdinal: int)
    SqlMetaData(name: str, dbType: SqlDbType, database: str, owningSchema: str, objectName: str)
    """
    @property
    def CompareOptions(self) -> SqlCompareOptions:
        """ Get: CompareOptions(self: SqlMetaData) -> SqlCompareOptions """
        ...

    @property
    def DbType(self) -> DbType:
        """ Get: DbType(self: SqlMetaData) -> DbType """
        ...

    @property
    def IsUniqueKey(self) -> bool:
        """ Get: IsUniqueKey(self: SqlMetaData) -> bool """
        ...

    @property
    def LocaleId(self) -> Int64:
        """ Get: LocaleId(self: SqlMetaData) -> Int64 """
        ...

    @property
    def Max(self) -> Int64:
        """ Get: Max() -> Int64 """
        ...

    @property
    def MaxLength(self) -> Int64:
        """ Get: MaxLength(self: SqlMetaData) -> Int64 """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: SqlMetaData) -> str """
        ...

    @property
    def Precision(self) -> Byte:
        """ Get: Precision(self: SqlMetaData) -> Byte """
        ...

    @property
    def Scale(self) -> Byte:
        """ Get: Scale(self: SqlMetaData) -> Byte """
        ...

    @property
    def SortOrder(self) -> SortOrder:
        """ Get: SortOrder(self: SqlMetaData) -> SortOrder """
        ...

    @property
    def SortOrdinal(self) -> int:
        """ Get: SortOrdinal(self: SqlMetaData) -> int """
        ...

    @property
    def SqlDbType(self) -> SqlDbType:
        """ Get: SqlDbType(self: SqlMetaData) -> SqlDbType """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: SqlMetaData) -> Type """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: SqlMetaData) -> str """
        ...

    @property
    def UseServerDefault(self) -> bool:
        """ Get: UseServerDefault(self: SqlMetaData) -> bool """
        ...

    @property
    def XmlSchemaCollectionDatabase(self) -> str:
        """ Get: XmlSchemaCollectionDatabase(self: SqlMetaData) -> str """
        ...

    @property
    def XmlSchemaCollectionName(self) -> str:
        """ Get: XmlSchemaCollectionName(self: SqlMetaData) -> str """
        ...

    @property
    def XmlSchemaCollectionOwningSchema(self) -> str:
        """ Get: XmlSchemaCollectionOwningSchema(self: SqlMetaData) -> str """
        ...


    def Adjust(self, value:Int16) -> Int16:
        """
        Adjust(self: SqlMetaData, value: Int16) -> Int16
        Adjust(self: SqlMetaData, value: object) -> object
        Adjust(self: SqlMetaData, value: SqlBytes) -> SqlBytes
        Adjust(self: SqlMetaData, value: SqlChars) -> SqlChars
        Adjust(self: SqlMetaData, value: SqlBinary) -> SqlBinary
        Adjust(self: SqlMetaData, value: SqlDecimal) -> SqlDecimal
        Adjust(self: SqlMetaData, value: SqlMoney) -> SqlMoney
        Adjust(self: SqlMetaData, value: Decimal) -> Decimal
        Adjust(self: SqlMetaData, value: Char) -> Char
        Adjust(self: SqlMetaData, value: Byte) -> Byte
        Adjust(self: SqlMetaData, value: bool) -> bool
        Adjust(self: SqlMetaData, value: DateTimeOffset) -> DateTimeOffset
        Adjust(self: SqlMetaData, value: TimeSpan) -> TimeSpan
        Adjust(self: SqlMetaData, value: SqlXml) -> SqlXml
        Adjust(self: SqlMetaData, value: SqlGuid) -> SqlGuid
        Adjust(self: SqlMetaData, value: Array[Byte]) -> Array[Byte]
        Adjust(self: SqlMetaData, value: SqlString) -> SqlString
        Adjust(self: SqlMetaData, value: SqlDouble) -> SqlDouble
        Adjust(self: SqlMetaData, value: SqlSingle) -> SqlSingle
        Adjust(self: SqlMetaData, value: SqlInt64) -> SqlInt64
        Adjust(self: SqlMetaData, value: SqlInt32) -> SqlInt32
        Adjust(self: SqlMetaData, value: SqlInt16) -> SqlInt16
        Adjust(self: SqlMetaData, value: SqlByte) -> SqlByte
        Adjust(self: SqlMetaData, value: SqlBoolean) -> SqlBoolean
        Adjust(self: SqlMetaData, value: Guid) -> Guid
        Adjust(self: SqlMetaData, value: DateTime) -> DateTime
        Adjust(self: SqlMetaData, value: str) -> str
        Adjust(self: SqlMetaData, value: float) -> float
        Adjust(self: SqlMetaData, value: Single) -> Single
        Adjust(self: SqlMetaData, value: Int64) -> Int64
        Adjust(self: SqlMetaData, value: int) -> int
        Adjust(self: SqlMetaData, value: SqlDateTime) -> SqlDateTime
        Adjust(self: SqlMetaData, value: Array[Char]) -> Array[Char]
        """
        ...

    @staticmethod
    def InferFromValue(value:object, name:str) -> SqlMetaData:
        """ InferFromValue(value: object, name: str) -> SqlMetaData """
        ...



class SqlMethodAttribute(SqlFunctionAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SqlMethodAttribute() """
    @property
    def InvokeIfReceiverIsNull(self) -> bool:
        """
        Get: InvokeIfReceiverIsNull(self: SqlMethodAttribute) -> bool
        Set: InvokeIfReceiverIsNull(self: SqlMethodAttribute) = value
        """
        ...

    @property
    def IsMutator(self) -> bool:
        """
        Get: IsMutator(self: SqlMethodAttribute) -> bool
        Set: IsMutator(self: SqlMethodAttribute) = value
        """
        ...

    @property
    def OnNullCall(self) -> bool:
        """
        Get: OnNullCall(self: SqlMethodAttribute) -> bool
        Set: OnNullCall(self: SqlMethodAttribute) = value
        """
        ...



class SqlPipe: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsSendingResults(self) -> bool:
        """ Get: IsSendingResults(self: SqlPipe) -> bool """
        ...


    def ExecuteAndSend(self, command:SqlCommand): # -> 
        """ ExecuteAndSend(self: SqlPipe, command: SqlCommand) """
        ...

    def Send(self, *__args:str): # -> 
        """ Send(self: SqlPipe, message: str)Send(self: SqlPipe, reader: SqlDataReader)Send(self: SqlPipe, record: SqlDataRecord) """
        ...

    def SendResultsEnd(self): # -> 
        """ SendResultsEnd(self: SqlPipe) """
        ...

    def SendResultsRow(self, record:SqlDataRecord): # -> 
        """ SendResultsRow(self: SqlPipe, record: SqlDataRecord) """
        ...

    def SendResultsStart(self, record:SqlDataRecord): # -> 
        """ SendResultsStart(self: SqlPipe, record: SqlDataRecord) """
        ...


class SqlProcedureAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SqlProcedureAttribute() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: SqlProcedureAttribute) -> str
        Set: Name(self: SqlProcedureAttribute) = value
        """
        ...



class SqlTriggerAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SqlTriggerAttribute() """
    @property
    def Event(self) -> str:
        """
        Get: Event(self: SqlTriggerAttribute) -> str
        Set: Event(self: SqlTriggerAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SqlTriggerAttribute) -> str
        Set: Name(self: SqlTriggerAttribute) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: SqlTriggerAttribute) -> str
        Set: Target(self: SqlTriggerAttribute) = value
        """
        ...



class SqlTriggerContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ColumnCount(self) -> int:
        """ Get: ColumnCount(self: SqlTriggerContext) -> int """
        ...

    @property
    def EventData(self) -> SqlXml:
        """ Get: EventData(self: SqlTriggerContext) -> SqlXml """
        ...

    @property
    def TriggerAction(self) -> TriggerAction:
        """ Get: TriggerAction(self: SqlTriggerContext) -> TriggerAction """
        ...


    def IsUpdatedColumn(self, columnOrdinal:int) -> bool:
        """ IsUpdatedColumn(self: SqlTriggerContext, columnOrdinal: int) -> bool """
        ...


class SqlUserDefinedAggregateAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SqlUserDefinedAggregateAttribute(format: Format) """
    @property
    def Format(self) -> Format:
        """ Get: Format(self: SqlUserDefinedAggregateAttribute) -> Format """
        ...

    @property
    def IsInvariantToDuplicates(self) -> bool:
        """
        Get: IsInvariantToDuplicates(self: SqlUserDefinedAggregateAttribute) -> bool
        Set: IsInvariantToDuplicates(self: SqlUserDefinedAggregateAttribute) = value
        """
        ...

    @property
    def IsInvariantToNulls(self) -> bool:
        """
        Get: IsInvariantToNulls(self: SqlUserDefinedAggregateAttribute) -> bool
        Set: IsInvariantToNulls(self: SqlUserDefinedAggregateAttribute) = value
        """
        ...

    @property
    def IsInvariantToOrder(self) -> bool:
        """
        Get: IsInvariantToOrder(self: SqlUserDefinedAggregateAttribute) -> bool
        Set: IsInvariantToOrder(self: SqlUserDefinedAggregateAttribute) = value
        """
        ...

    @property
    def IsNullIfEmpty(self) -> bool:
        """
        Get: IsNullIfEmpty(self: SqlUserDefinedAggregateAttribute) -> bool
        Set: IsNullIfEmpty(self: SqlUserDefinedAggregateAttribute) = value
        """
        ...

    @property
    def MaxByteSize(self) -> int:
        """
        Get: MaxByteSize(self: SqlUserDefinedAggregateAttribute) -> int
        Set: MaxByteSize(self: SqlUserDefinedAggregateAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SqlUserDefinedAggregateAttribute) -> str
        Set: Name(self: SqlUserDefinedAggregateAttribute) = value
        """
        ...


    def __new__(cls, format:Format) -> Self:
        """ __new__(cls: type, format: Format) """
        ...

    MaxByteSizeValue: int = ...


class SqlUserDefinedTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SqlUserDefinedTypeAttribute(format: Format) """
    @property
    def Format(self) -> Format:
        """ Get: Format(self: SqlUserDefinedTypeAttribute) -> Format """
        ...

    @property
    def IsByteOrdered(self) -> bool:
        """
        Get: IsByteOrdered(self: SqlUserDefinedTypeAttribute) -> bool
        Set: IsByteOrdered(self: SqlUserDefinedTypeAttribute) = value
        """
        ...

    @property
    def IsFixedLength(self) -> bool:
        """
        Get: IsFixedLength(self: SqlUserDefinedTypeAttribute) -> bool
        Set: IsFixedLength(self: SqlUserDefinedTypeAttribute) = value
        """
        ...

    @property
    def MaxByteSize(self) -> int:
        """
        Get: MaxByteSize(self: SqlUserDefinedTypeAttribute) -> int
        Set: MaxByteSize(self: SqlUserDefinedTypeAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: SqlUserDefinedTypeAttribute) -> str
        Set: Name(self: SqlUserDefinedTypeAttribute) = value
        """
        ...

    @property
    def ValidationMethodName(self) -> str:
        """
        Get: ValidationMethodName(self: SqlUserDefinedTypeAttribute) -> str
        Set: ValidationMethodName(self: SqlUserDefinedTypeAttribute) = value
        """
        ...


    def __new__(cls, format:Format) -> Self:
        """ __new__(cls: type, format: Format) """
        ...


class SystemDataAccessKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SystemDataAccessKind, values: None (0), Read (1) """
    Read: SystemDataAccessKind = ...
    value__ = ...


class TriggerAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TriggerAction, values: AlterAppRole (138), AlterAssembly (102), AlterBinding (175), AlterFunction (62), AlterIndex (25), AlterLogin (145), AlterPartitionFunction (192), AlterPartitionScheme (195), AlterProcedure (52), AlterQueue (158), AlterRole (135), AlterRoute (165), AlterSchema (142), AlterService (162), AlterTable (22), AlterTrigger (72), AlterUser (132), AlterView (42), CreateAppRole (137), CreateAssembly (101), CreateBinding (174), CreateContract (154), CreateEventNotification (74), CreateFunction (61), CreateIndex (24), CreateLogin (144), CreateMsgType (151), CreatePartitionFunction (191), CreatePartitionScheme (194), CreateProcedure (51), CreateQueue (157), CreateRole (134), CreateRoute (164), CreateSchema (141), CreateSecurityExpression (31), CreateService (161), CreateSynonym (34), CreateTable (21), CreateTrigger (71), CreateType (91), CreateUser (131), CreateView (41), Delete (3), DenyObject (171), DenyStatement (168), DropAppRole (139), DropAssembly (103), DropBinding (176), DropContract (156), DropEventNotification (76), DropFunction (63), DropIndex (26), DropLogin (146), DropMsgType (153), DropPartitionFunction (193), DropPartitionScheme (196), DropProcedure (53), DropQueue (159), DropRole (136), DropRoute (166), DropSchema (143), DropSecurityExpression (33), DropService (163), DropSynonym (36), DropTable (23), DropTrigger (73), DropType (93), DropUser (133), DropView (43), GrantObject (170), GrantStatement (167), Insert (1), Invalid (0), RevokeObject (172), RevokeStatement (169), Update (2) """
    AlterAppRole: TriggerAction = ...
    AlterAssembly: TriggerAction = ...
    AlterBinding: TriggerAction = ...
    AlterFunction: TriggerAction = ...
    AlterIndex: TriggerAction = ...
    AlterLogin: TriggerAction = ...
    AlterPartitionFunction: TriggerAction = ...
    AlterPartitionScheme: TriggerAction = ...
    AlterProcedure: TriggerAction = ...
    AlterQueue: TriggerAction = ...
    AlterRole: TriggerAction = ...
    AlterRoute: TriggerAction = ...
    AlterSchema: TriggerAction = ...
    AlterService: TriggerAction = ...
    AlterTable: TriggerAction = ...
    AlterTrigger: TriggerAction = ...
    AlterUser: TriggerAction = ...
    AlterView: TriggerAction = ...
    CreateAppRole: TriggerAction = ...
    CreateAssembly: TriggerAction = ...
    CreateBinding: TriggerAction = ...
    CreateContract: TriggerAction = ...
    CreateEventNotification: TriggerAction = ...
    CreateFunction: TriggerAction = ...
    CreateIndex: TriggerAction = ...
    CreateLogin: TriggerAction = ...
    CreateMsgType: TriggerAction = ...
    CreatePartitionFunction: TriggerAction = ...
    CreatePartitionScheme: TriggerAction = ...
    CreateProcedure: TriggerAction = ...
    CreateQueue: TriggerAction = ...
    CreateRole: TriggerAction = ...
    CreateRoute: TriggerAction = ...
    CreateSchema: TriggerAction = ...
    CreateSecurityExpression: TriggerAction = ...
    CreateService: TriggerAction = ...
    CreateSynonym: TriggerAction = ...
    CreateTable: TriggerAction = ...
    CreateTrigger: TriggerAction = ...
    CreateType: TriggerAction = ...
    CreateUser: TriggerAction = ...
    CreateView: TriggerAction = ...
    Delete: TriggerAction = ...
    DenyObject: TriggerAction = ...
    DenyStatement: TriggerAction = ...
    DropAppRole: TriggerAction = ...
    DropAssembly: TriggerAction = ...
    DropBinding: TriggerAction = ...
    DropContract: TriggerAction = ...
    DropEventNotification: TriggerAction = ...
    DropFunction: TriggerAction = ...
    DropIndex: TriggerAction = ...
    DropLogin: TriggerAction = ...
    DropMsgType: TriggerAction = ...
    DropPartitionFunction: TriggerAction = ...
    DropPartitionScheme: TriggerAction = ...
    DropProcedure: TriggerAction = ...
    DropQueue: TriggerAction = ...
    DropRole: TriggerAction = ...
    DropRoute: TriggerAction = ...
    DropSchema: TriggerAction = ...
    DropSecurityExpression: TriggerAction = ...
    DropService: TriggerAction = ...
    DropSynonym: TriggerAction = ...
    DropTable: TriggerAction = ...
    DropTrigger: TriggerAction = ...
    DropType: TriggerAction = ...
    DropUser: TriggerAction = ...
    DropView: TriggerAction = ...
    GrantObject: TriggerAction = ...
    GrantStatement: TriggerAction = ...
    Insert: TriggerAction = ...
    Invalid: TriggerAction = ...
    RevokeObject: TriggerAction = ...
    RevokeStatement: TriggerAction = ...
    Update: TriggerAction = ...
    value__ = ...


