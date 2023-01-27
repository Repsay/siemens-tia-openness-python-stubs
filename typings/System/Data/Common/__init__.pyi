# encoding: utf-8
# module System.Data.Common calls itself Common
# from System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Data.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Attribute, Byte, Char, DateTime, Decimal, Enum, 
    EventArgs, Guid, ICloneable, Int16, Int64, MarshalByRefObject, Nullable, 
    Single, Type)

from System.Collections import IDictionary, IEnumerable, IEnumerator

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel import Component, ICustomTypeDescriptor

from System.Configuration import IConfigurationSectionHandler

from System.Data import (ConflictOption, DataColumn, DataRow, DataRowVersion, 
    DataSet, DataTable, DbType, EntityKey, IColumnMapping, 
    IColumnMappingCollection, IDataAdapter, IDataParameterCollection, 
    IDataReader, IDataRecord, IDbCommand, IDbConnection, IDbDataAdapter, 
    IDbDataParameter, IDbTransaction, ITableMapping, ITableMappingCollection, 
    KeyRestrictionBehavior, LoadOption, MissingMappingAction, 
    MissingSchemaAction, ParameterDirection, StatementType, UpdateStatus)

from System.Data.Metadata.Edm import (EdmMember, EdmType, StoreItemCollection, 
    TypeUsage)

from System.Data.Spatial import DbSpatialDataReader, DbSpatialServices

from System.IO import Stream, TextReader

from System.Runtime.InteropServices import ExternalException

from System.Security import CodeAccessPermission

from System.Security.Permissions import (CodeAccessSecurityAttribute, 
    IUnrestrictedPermission, PermissionState)

from System.Text import StringBuilder

from System.Threading import CancellationToken

from System.Threading.Tasks import Task

from System.Transactions import Transaction

from System.Xml import XmlReader

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: BoundEvent, T, field#
"""

# no functions
# classes

class CatalogLocation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CatalogLocation, values: End (2), Start (1) """
    End: CatalogLocation = ...
    Start: CatalogLocation = ...
    value__ = ...


class DataAdapter(IDataAdapter, Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def AcceptChangesDuringFill(self) -> bool:
        """
        Get: AcceptChangesDuringFill(self: DataAdapter) -> bool
        Set: AcceptChangesDuringFill(self: DataAdapter) = value
        """
        ...

    @property
    def AcceptChangesDuringUpdate(self) -> bool:
        """
        Get: AcceptChangesDuringUpdate(self: DataAdapter) -> bool
        Set: AcceptChangesDuringUpdate(self: DataAdapter) = value
        """
        ...

    @property
    def ContinueUpdateOnError(self) -> bool:
        """
        Get: ContinueUpdateOnError(self: DataAdapter) -> bool
        Set: ContinueUpdateOnError(self: DataAdapter) = value
        """
        ...

    @property
    def FillLoadOption(self) -> LoadOption:
        """
        Get: FillLoadOption(self: DataAdapter) -> LoadOption
        Set: FillLoadOption(self: DataAdapter) = value
        """
        ...

    @property
    def ReturnProviderSpecificTypes(self) -> bool:
        """
        Get: ReturnProviderSpecificTypes(self: DataAdapter) -> bool
        Set: ReturnProviderSpecificTypes(self: DataAdapter) = value
        """
        ...


    def CloneInternals(self, *args): #cannot find CLR method
        """ CloneInternals(self: DataAdapter) -> DataAdapter """
        ...

    def CreateTableMappings(self, *args): #cannot find CLR method
        """ CreateTableMappings(self: DataAdapter) -> DataTableMappingCollection """
        ...

    def HasTableMappings(self, *args): #cannot find CLR method
        """ HasTableMappings(self: DataAdapter) -> bool """
        ...

    def OnFillError(self, *args): #cannot find CLR method
        """ OnFillError(self: DataAdapter, value: FillErrorEventArgs) """
        ...

    def ResetFillLoadOption(self): # -> 
        """ ResetFillLoadOption(self: DataAdapter) """
        ...

    def ShouldSerializeAcceptChangesDuringFill(self) -> bool:
        """ ShouldSerializeAcceptChangesDuringFill(self: DataAdapter) -> bool """
        ...

    def ShouldSerializeFillLoadOption(self) -> bool:
        """ ShouldSerializeFillLoadOption(self: DataAdapter) -> bool """
        ...

    def ShouldSerializeTableMappings(self, *args): #cannot find CLR method
        """ ShouldSerializeTableMappings(self: DataAdapter) -> bool """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, from: DataAdapter)
        """
        ...

    FillError = ...


class DataColumnMapping(ICloneable, MarshalByRefObject, IColumnMapping): # skipped bases: <type 'object'>
    """
    DataColumnMapping()
    DataColumnMapping(sourceColumn: str, dataSetColumn: str)
    """
    def GetDataColumnBySchemaAction(self, *__args) -> DataColumn:
        """
        GetDataColumnBySchemaAction(self: DataColumnMapping, dataTable: DataTable, dataType: Type, schemaAction: MissingSchemaAction) -> DataColumn
        GetDataColumnBySchemaAction(sourceColumn: str, dataSetColumn: str, dataTable: DataTable, dataType: Type, schemaAction: MissingSchemaAction) -> DataColumn
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: DataColumnMapping) -> str """
        ...

    def __new__(cls, sourceColumn:str = ..., dataSetColumn:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, sourceColumn: str, dataSetColumn: str)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class DataColumnMappingCollection(MarshalByRefObject, IColumnMappingCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DataColumnMappingCollection() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: DataColumnMappingCollection) -> int """
        ...


    def AddRange(self, values:Array): # -> 
        """ AddRange(self: DataColumnMappingCollection, values: Array[DataColumnMapping])AddRange(self: DataColumnMappingCollection, values: Array) """
        ...

    def Clear(self): # -> 
        """ Clear(self: DataColumnMappingCollection) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DataColumnMappingCollection, array: Array, index: int)CopyTo(self: DataColumnMappingCollection, array: Array[DataColumnMapping], index: int) """
        ...

    @staticmethod
    def GetColumnMappingBySchemaAction(columnMappings:DataColumnMappingCollection, sourceColumn:str, mappingAction:MissingMappingAction) -> DataColumnMapping:
        """ GetColumnMappingBySchemaAction(columnMappings: DataColumnMappingCollection, sourceColumn: str, mappingAction: MissingMappingAction) -> DataColumnMapping """
        ...

    @staticmethod
    def GetDataColumn(columnMappings:DataColumnMappingCollection, sourceColumn:str, dataType:Type, dataTable:DataTable, mappingAction:MissingMappingAction, schemaAction:MissingSchemaAction) -> DataColumn:
        """ GetDataColumn(columnMappings: DataColumnMappingCollection, sourceColumn: str, dataType: Type, dataTable: DataTable, mappingAction: MissingMappingAction, schemaAction: MissingSchemaAction) -> DataColumn """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DataColumnMappingCollection) -> IEnumerator """
        ...

    def IndexOfDataSetColumn(self, dataSetColumn:str) -> int:
        """ IndexOfDataSetColumn(self: DataColumnMappingCollection, dataSetColumn: str) -> int """
        ...

    def Insert(self, index:int, value:object): # -> 
        """ Insert(self: DataColumnMappingCollection, index: int, value: object)Insert(self: DataColumnMappingCollection, index: int, value: DataColumnMapping) """
        ...

    def Remove(self, value:object): # -> 
        """ Remove(self: DataColumnMappingCollection, value: object)Remove(self: DataColumnMappingCollection, value: DataColumnMapping) """
        ...


class DataRecordInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ DataRecordInfo(metadata: TypeUsage, memberInfo: IEnumerable[EdmMember]) """
    @property
    def FieldMetadata(self) -> ReadOnlyCollection:
        """ Get: FieldMetadata(self: DataRecordInfo) -> ReadOnlyCollection[FieldMetadata] """
        ...

    @property
    def RecordType(self) -> TypeUsage:
        """ Get: RecordType(self: DataRecordInfo) -> TypeUsage """
        ...



class DataTableMapping(ICloneable, MarshalByRefObject, ITableMapping): # skipped bases: <type 'object'>
    """
    DataTableMapping()
    DataTableMapping(sourceTable: str, dataSetTable: str)
    DataTableMapping(sourceTable: str, dataSetTable: str, columnMappings: Array[DataColumnMapping])
    """
    def GetColumnMappingBySchemaAction(self, sourceColumn:str, mappingAction:MissingMappingAction) -> DataColumnMapping:
        """ GetColumnMappingBySchemaAction(self: DataTableMapping, sourceColumn: str, mappingAction: MissingMappingAction) -> DataColumnMapping """
        ...

    def GetDataColumn(self, sourceColumn:str, dataType:Type, dataTable:DataTable, mappingAction:MissingMappingAction, schemaAction:MissingSchemaAction) -> DataColumn:
        """ GetDataColumn(self: DataTableMapping, sourceColumn: str, dataType: Type, dataTable: DataTable, mappingAction: MissingMappingAction, schemaAction: MissingSchemaAction) -> DataColumn """
        ...

    def GetDataTableBySchemaAction(self, dataSet:DataSet, schemaAction:MissingSchemaAction) -> DataTable:
        """ GetDataTableBySchemaAction(self: DataTableMapping, dataSet: DataSet, schemaAction: MissingSchemaAction) -> DataTable """
        ...

    def ToString(self) -> str:
        """ ToString(self: DataTableMapping) -> str """
        ...

    def __new__(cls, sourceTable:str = ..., dataSetTable:str = ..., columnMappings:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, sourceTable: str, dataSetTable: str)
        __new__(cls: type, sourceTable: str, dataSetTable: str, columnMappings: Array[DataColumnMapping])
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class DataTableMappingCollection(MarshalByRefObject, ITableMappingCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DataTableMappingCollection() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: DataTableMappingCollection) -> int """
        ...


    def AddRange(self, values:Array): # -> 
        """ AddRange(self: DataTableMappingCollection, values: Array[DataTableMapping])AddRange(self: DataTableMappingCollection, values: Array) """
        ...

    def Clear(self): # -> 
        """ Clear(self: DataTableMappingCollection) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DataTableMappingCollection, array: Array, index: int)CopyTo(self: DataTableMappingCollection, array: Array[DataTableMapping], index: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DataTableMappingCollection) -> IEnumerator """
        ...

    @staticmethod
    def GetTableMappingBySchemaAction(tableMappings:DataTableMappingCollection, sourceTable:str, dataSetTable:str, mappingAction:MissingMappingAction) -> DataTableMapping:
        """ GetTableMappingBySchemaAction(tableMappings: DataTableMappingCollection, sourceTable: str, dataSetTable: str, mappingAction: MissingMappingAction) -> DataTableMapping """
        ...

    def IndexOfDataSetTable(self, dataSetTable:str) -> int:
        """ IndexOfDataSetTable(self: DataTableMappingCollection, dataSetTable: str) -> int """
        ...

    def Insert(self, index:int, value:object): # -> 
        """ Insert(self: DataTableMappingCollection, index: int, value: object)Insert(self: DataTableMappingCollection, index: int, value: DataTableMapping) """
        ...

    def Remove(self, value:object): # -> 
        """ Remove(self: DataTableMappingCollection, value: object)Remove(self: DataTableMappingCollection, value: DataTableMapping) """
        ...


class DbColumn: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AllowDBNull(self) -> Nullable:
        """ Get: AllowDBNull(self: DbColumn) -> Nullable[bool] """
        ...

    @property
    def BaseCatalogName(self) -> str:
        """ Get: BaseCatalogName(self: DbColumn) -> str """
        ...

    @property
    def BaseColumnName(self) -> str:
        """ Get: BaseColumnName(self: DbColumn) -> str """
        ...

    @property
    def BaseSchemaName(self) -> str:
        """ Get: BaseSchemaName(self: DbColumn) -> str """
        ...

    @property
    def BaseServerName(self) -> str:
        """ Get: BaseServerName(self: DbColumn) -> str """
        ...

    @property
    def BaseTableName(self) -> str:
        """ Get: BaseTableName(self: DbColumn) -> str """
        ...

    @property
    def ColumnName(self) -> str:
        """ Get: ColumnName(self: DbColumn) -> str """
        ...

    @property
    def ColumnOrdinal(self) -> Nullable:
        """ Get: ColumnOrdinal(self: DbColumn) -> Nullable[int] """
        ...

    @property
    def ColumnSize(self) -> Nullable:
        """ Get: ColumnSize(self: DbColumn) -> Nullable[int] """
        ...

    @property
    def DataType(self) -> Type:
        """ Get: DataType(self: DbColumn) -> Type """
        ...

    @property
    def DataTypeName(self) -> str:
        """ Get: DataTypeName(self: DbColumn) -> str """
        ...

    @property
    def IsAliased(self) -> Nullable:
        """ Get: IsAliased(self: DbColumn) -> Nullable[bool] """
        ...

    @property
    def IsAutoIncrement(self) -> Nullable:
        """ Get: IsAutoIncrement(self: DbColumn) -> Nullable[bool] """
        ...

    @property
    def IsExpression(self) -> Nullable:
        """ Get: IsExpression(self: DbColumn) -> Nullable[bool] """
        ...

    @property
    def IsHidden(self) -> Nullable:
        """ Get: IsHidden(self: DbColumn) -> Nullable[bool] """
        ...

    @property
    def IsIdentity(self) -> Nullable:
        """ Get: IsIdentity(self: DbColumn) -> Nullable[bool] """
        ...

    @property
    def IsKey(self) -> Nullable:
        """ Get: IsKey(self: DbColumn) -> Nullable[bool] """
        ...

    @property
    def IsLong(self) -> Nullable:
        """ Get: IsLong(self: DbColumn) -> Nullable[bool] """
        ...

    @property
    def IsReadOnly(self) -> Nullable:
        """ Get: IsReadOnly(self: DbColumn) -> Nullable[bool] """
        ...

    @property
    def IsUnique(self) -> Nullable:
        """ Get: IsUnique(self: DbColumn) -> Nullable[bool] """
        ...

    @property
    def NumericPrecision(self) -> Nullable:
        """ Get: NumericPrecision(self: DbColumn) -> Nullable[int] """
        ...

    @property
    def NumericScale(self) -> Nullable:
        """ Get: NumericScale(self: DbColumn) -> Nullable[int] """
        ...

    @property
    def UdtAssemblyQualifiedName(self) -> str:
        """ Get: UdtAssemblyQualifiedName(self: DbColumn) -> str """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DbCommand(IDbCommand, Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def DbConnection(self):
        ...

    @property
    def DbParameterCollection(self):
        ...

    @property
    def DbTransaction(self):
        ...

    @property
    def DesignTimeVisible(self) -> bool:
        """
        Get: DesignTimeVisible(self: DbCommand) -> bool
        Set: DesignTimeVisible(self: DbCommand) = value
        """
        ...


    def CreateDbParameter(self, *args): #cannot find CLR method
        """ CreateDbParameter(self: DbCommand) -> DbParameter """
        ...

    def ExecuteDbDataReader(self, *args): #cannot find CLR method
        """ ExecuteDbDataReader(self: DbCommand, behavior: CommandBehavior) -> DbDataReader """
        ...

    def ExecuteDbDataReaderAsync(self, *args): #cannot find CLR method
        """ ExecuteDbDataReaderAsync(self: DbCommand, behavior: CommandBehavior, cancellationToken: CancellationToken) -> Task[DbDataReader] """
        ...

    def ExecuteNonQueryAsync(self, cancellationToken:CancellationToken = ...) -> Task:
        """
        ExecuteNonQueryAsync(self: DbCommand) -> Task[int]
        ExecuteNonQueryAsync(self: DbCommand, cancellationToken: CancellationToken) -> Task[int]
        """
        ...

    def ExecuteReaderAsync(self, *__args:CancellationToken) -> Task:
        """
        ExecuteReaderAsync(self: DbCommand) -> Task[DbDataReader]
        ExecuteReaderAsync(self: DbCommand, cancellationToken: CancellationToken) -> Task[DbDataReader]
        ExecuteReaderAsync(self: DbCommand, behavior: CommandBehavior) -> Task[DbDataReader]
        ExecuteReaderAsync(self: DbCommand, behavior: CommandBehavior, cancellationToken: CancellationToken) -> Task[DbDataReader]
        """
        ...

    def ExecuteScalarAsync(self, cancellationToken:CancellationToken = ...) -> Task:
        """
        ExecuteScalarAsync(self: DbCommand) -> Task[object]
        ExecuteScalarAsync(self: DbCommand, cancellationToken: CancellationToken) -> Task[object]
        """
        ...


class DbCommandBuilder(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def CatalogLocation(self) -> CatalogLocation:
        """
        Get: CatalogLocation(self: DbCommandBuilder) -> CatalogLocation
        Set: CatalogLocation(self: DbCommandBuilder) = value
        """
        ...

    @property
    def CatalogSeparator(self) -> str:
        """
        Get: CatalogSeparator(self: DbCommandBuilder) -> str
        Set: CatalogSeparator(self: DbCommandBuilder) = value
        """
        ...

    @property
    def ConflictOption(self) -> ConflictOption:
        """
        Get: ConflictOption(self: DbCommandBuilder) -> ConflictOption
        Set: ConflictOption(self: DbCommandBuilder) = value
        """
        ...

    @property
    def DataAdapter(self) -> DbDataAdapter:
        """
        Get: DataAdapter(self: DbCommandBuilder) -> DbDataAdapter
        Set: DataAdapter(self: DbCommandBuilder) = value
        """
        ...

    @property
    def QuotePrefix(self) -> str:
        """
        Get: QuotePrefix(self: DbCommandBuilder) -> str
        Set: QuotePrefix(self: DbCommandBuilder) = value
        """
        ...

    @property
    def QuoteSuffix(self) -> str:
        """
        Get: QuoteSuffix(self: DbCommandBuilder) -> str
        Set: QuoteSuffix(self: DbCommandBuilder) = value
        """
        ...

    @property
    def SchemaSeparator(self) -> str:
        """
        Get: SchemaSeparator(self: DbCommandBuilder) -> str
        Set: SchemaSeparator(self: DbCommandBuilder) = value
        """
        ...

    @property
    def SetAllValues(self) -> bool:
        """
        Get: SetAllValues(self: DbCommandBuilder) -> bool
        Set: SetAllValues(self: DbCommandBuilder) = value
        """
        ...


    def ApplyParameterInfo(self, *args): #cannot find CLR method
        """ ApplyParameterInfo(self: DbCommandBuilder, parameter: DbParameter, row: DataRow, statementType: StatementType, whereClause: bool) """
        ...

    def GetDeleteCommand(self, useColumnsForParameterNames:bool = ...) -> DbCommand:
        """
        GetDeleteCommand(self: DbCommandBuilder) -> DbCommand
        GetDeleteCommand(self: DbCommandBuilder, useColumnsForParameterNames: bool) -> DbCommand
        """
        ...

    def GetInsertCommand(self, useColumnsForParameterNames:bool = ...) -> DbCommand:
        """
        GetInsertCommand(self: DbCommandBuilder) -> DbCommand
        GetInsertCommand(self: DbCommandBuilder, useColumnsForParameterNames: bool) -> DbCommand
        """
        ...

    def GetParameterName(self, *args): #cannot find CLR method
        """
        GetParameterName(self: DbCommandBuilder, parameterOrdinal: int) -> str
        GetParameterName(self: DbCommandBuilder, parameterName: str) -> str
        """
        ...

    def GetParameterPlaceholder(self, *args): #cannot find CLR method
        """ GetParameterPlaceholder(self: DbCommandBuilder, parameterOrdinal: int) -> str """
        ...

    def GetSchemaTable(self, *args): #cannot find CLR method
        """ GetSchemaTable(self: DbCommandBuilder, sourceCommand: DbCommand) -> DataTable """
        ...

    def GetUpdateCommand(self, useColumnsForParameterNames:bool = ...) -> DbCommand:
        """
        GetUpdateCommand(self: DbCommandBuilder) -> DbCommand
        GetUpdateCommand(self: DbCommandBuilder, useColumnsForParameterNames: bool) -> DbCommand
        """
        ...

    def InitializeCommand(self, *args): #cannot find CLR method
        """ InitializeCommand(self: DbCommandBuilder, command: DbCommand) -> DbCommand """
        ...

    def QuoteIdentifier(self, unquotedIdentifier:str) -> str:
        """ QuoteIdentifier(self: DbCommandBuilder, unquotedIdentifier: str) -> str """
        ...

    def RefreshSchema(self): # -> 
        """ RefreshSchema(self: DbCommandBuilder) """
        ...

    def RowUpdatingHandler(self, *args): #cannot find CLR method
        """ RowUpdatingHandler(self: DbCommandBuilder, rowUpdatingEvent: RowUpdatingEventArgs) """
        ...

    def SetRowUpdatingHandler(self, *args): #cannot find CLR method
        """ SetRowUpdatingHandler(self: DbCommandBuilder, adapter: DbDataAdapter) """
        ...

    def UnquoteIdentifier(self, quotedIdentifier:str) -> str:
        """ UnquoteIdentifier(self: DbCommandBuilder, quotedIdentifier: str) -> str """
        ...


class DbCommandDefinition: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateCommand(self) -> DbCommand:
        """ CreateCommand(self: DbCommandDefinition) -> DbCommand """
        ...


class DbConnection(IDbConnection, Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def DataSource(self) -> str:
        """ Get: DataSource(self: DbConnection) -> str """
        ...

    @property
    def DbProviderFactory(self):
        ...

    @property
    def ServerVersion(self) -> str:
        """ Get: ServerVersion(self: DbConnection) -> str """
        ...


    def BeginDbTransaction(self, *args): #cannot find CLR method
        """ BeginDbTransaction(self: DbConnection, isolationLevel: IsolationLevel) -> DbTransaction """
        ...

    def CreateDbCommand(self, *args): #cannot find CLR method
        """ CreateDbCommand(self: DbConnection) -> DbCommand """
        ...

    def EnlistTransaction(self, transaction:Transaction): # -> 
        """ EnlistTransaction(self: DbConnection, transaction: Transaction) """
        ...

    def GetSchema(self, collectionName:str = ..., restrictionValues:Array = ...) -> DataTable:
        """
        GetSchema(self: DbConnection) -> DataTable
        GetSchema(self: DbConnection, collectionName: str) -> DataTable
        GetSchema(self: DbConnection, collectionName: str, restrictionValues: Array[str]) -> DataTable
        """
        ...

    def OnStateChange(self, *args): #cannot find CLR method
        """ OnStateChange(self: DbConnection, stateChange: StateChangeEventArgs) """
        ...

    def OpenAsync(self, cancellationToken:CancellationToken = ...) -> Task:
        """
        OpenAsync(self: DbConnection) -> Task
        OpenAsync(self: DbConnection, cancellationToken: CancellationToken) -> Task
        """
        ...

    StateChange = ...


class DbConnectionStringBuilder(IDictionary, ICustomTypeDescriptor): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    DbConnectionStringBuilder()
    DbConnectionStringBuilder(useOdbcRules: bool)
    """
    @property
    def BrowsableConnectionString(self) -> bool:
        """
        Get: BrowsableConnectionString(self: DbConnectionStringBuilder) -> bool
        Set: BrowsableConnectionString(self: DbConnectionStringBuilder) = value
        """
        ...

    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: DbConnectionStringBuilder) -> str
        Set: ConnectionString(self: DbConnectionStringBuilder) = value
        """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: DbConnectionStringBuilder) -> int """
        ...


    @staticmethod
    def AppendKeyValuePair(builder:StringBuilder, keyword:str, value:str, useOdbcRules:bool = ...): # -> 
        """ AppendKeyValuePair(builder: StringBuilder, keyword: str, value: str)AppendKeyValuePair(builder: StringBuilder, keyword: str, value: str, useOdbcRules: bool) """
        ...

    def ClearPropertyDescriptors(self, *args): #cannot find CLR method
        """ ClearPropertyDescriptors(self: DbConnectionStringBuilder) """
        ...

    def ContainsKey(self, keyword:str) -> bool:
        """ ContainsKey(self: DbConnectionStringBuilder, keyword: str) -> bool """
        ...

    def EquivalentTo(self, connectionStringBuilder:DbConnectionStringBuilder) -> bool:
        """ EquivalentTo(self: DbConnectionStringBuilder, connectionStringBuilder: DbConnectionStringBuilder) -> bool """
        ...

    def ShouldSerialize(self, keyword:str) -> bool:
        """ ShouldSerialize(self: DbConnectionStringBuilder, keyword: str) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: DbConnectionStringBuilder) -> str """
        ...

    def TryGetValue(self, keyword, value) -> Tuple_[bool, object]:
        """ TryGetValue(self: DbConnectionStringBuilder, keyword: str) -> (bool, object) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary, key: object) -> bool """
        ...


class DbDataAdapter(IDbDataAdapter, ICloneable, DataAdapter): # skipped bases: <type 'IDataAdapter'>, <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def FillCommandBehavior(self):
        ...

    @property
    def UpdateBatchSize(self) -> int:
        """
        Get: UpdateBatchSize(self: DbDataAdapter) -> int
        Set: UpdateBatchSize(self: DbDataAdapter) = value
        """
        ...


    def AddToBatch(self, *args): #cannot find CLR method
        """ AddToBatch(self: DbDataAdapter, command: IDbCommand) -> int """
        ...

    def ClearBatch(self, *args): #cannot find CLR method
        """ ClearBatch(self: DbDataAdapter) """
        ...

    def CreateRowUpdatedEvent(self, *args): #cannot find CLR method
        """ CreateRowUpdatedEvent(self: DbDataAdapter, dataRow: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping) -> RowUpdatedEventArgs """
        ...

    def CreateRowUpdatingEvent(self, *args): #cannot find CLR method
        """ CreateRowUpdatingEvent(self: DbDataAdapter, dataRow: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping) -> RowUpdatingEventArgs """
        ...

    def ExecuteBatch(self, *args): #cannot find CLR method
        """ ExecuteBatch(self: DbDataAdapter) -> int """
        ...

    def GetBatchedParameter(self, *args): #cannot find CLR method
        """ GetBatchedParameter(self: DbDataAdapter, commandIdentifier: int, parameterIndex: int) -> IDataParameter """
        ...

    def GetBatchedRecordsAffected(self, *args): #cannot find CLR method
        """ GetBatchedRecordsAffected(self: DbDataAdapter, commandIdentifier: int) -> (bool, int, Exception) """
        ...

    def InitializeBatching(self, *args): #cannot find CLR method
        """ InitializeBatching(self: DbDataAdapter) """
        ...

    def OnRowUpdated(self, *args): #cannot find CLR method
        """ OnRowUpdated(self: DbDataAdapter, value: RowUpdatedEventArgs) """
        ...

    def OnRowUpdating(self, *args): #cannot find CLR method
        """ OnRowUpdating(self: DbDataAdapter, value: RowUpdatingEventArgs) """
        ...

    def TerminateBatching(self, *args): #cannot find CLR method
        """ TerminateBatching(self: DbDataAdapter) """
        ...

    DefaultSourceTableName: str = ...


class DBDataPermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """ no doc """
    @property
    def AllowBlankPassword(self) -> bool:
        """
        Get: AllowBlankPassword(self: DBDataPermission) -> bool
        Set: AllowBlankPassword(self: DBDataPermission) = value
        """
        ...


    def Add(self, connectionString:str, restrictions:str, behavior:KeyRestrictionBehavior): # -> 
        """ Add(self: DBDataPermission, connectionString: str, restrictions: str, behavior: KeyRestrictionBehavior) """
        ...

    def Clear(self, *args): #cannot find CLR method
        """ Clear(self: DBDataPermission) """
        ...

    def CreateInstance(self, *args): #cannot find CLR method
        """ CreateInstance(self: DBDataPermission) -> DBDataPermission """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, state: PermissionState, allowBlankPassword: bool)
        __new__(cls: type, permission: DBDataPermission)
        __new__(cls: type, permissionAttribute: DBDataPermissionAttribute)
        """
        ...


class DBDataPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    @property
    def AllowBlankPassword(self) -> bool:
        """
        Get: AllowBlankPassword(self: DBDataPermissionAttribute) -> bool
        Set: AllowBlankPassword(self: DBDataPermissionAttribute) = value
        """
        ...

    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: DBDataPermissionAttribute) -> str
        Set: ConnectionString(self: DBDataPermissionAttribute) = value
        """
        ...

    @property
    def KeyRestrictionBehavior(self) -> KeyRestrictionBehavior:
        """
        Get: KeyRestrictionBehavior(self: DBDataPermissionAttribute) -> KeyRestrictionBehavior
        Set: KeyRestrictionBehavior(self: DBDataPermissionAttribute) = value
        """
        ...

    @property
    def KeyRestrictions(self) -> str:
        """
        Get: KeyRestrictions(self: DBDataPermissionAttribute) -> str
        Set: KeyRestrictions(self: DBDataPermissionAttribute) = value
        """
        ...


    def ShouldSerializeConnectionString(self) -> bool:
        """ ShouldSerializeConnectionString(self: DBDataPermissionAttribute) -> bool """
        ...

    def ShouldSerializeKeyRestrictions(self) -> bool:
        """ ShouldSerializeKeyRestrictions(self: DBDataPermissionAttribute) -> bool """
        ...


class DbDataReader(MarshalByRefObject, IEnumerable, IDataReader): # skipped bases: <type 'IDisposable'>, <type 'IDataRecord'>, <type 'object'>
    """ no doc """
    @property
    def FieldCount(self) -> int:
        """ Get: FieldCount(self: DbDataReader) -> int """
        ...

    @property
    def HasRows(self) -> bool:
        """ Get: HasRows(self: DbDataReader) -> bool """
        ...

    @property
    def VisibleFieldCount(self) -> int:
        """ Get: VisibleFieldCount(self: DbDataReader) -> int """
        ...


    def Dispose(self): # -> 
        """ Dispose(self: DbDataReader) """
        ...

    def GetBoolean(self, ordinal:int) -> bool:
        """ GetBoolean(self: DbDataReader, ordinal: int) -> bool """
        ...

    def GetByte(self, ordinal:int) -> Byte:
        """ GetByte(self: DbDataReader, ordinal: int) -> Byte """
        ...

    def GetBytes(self, ordinal:int, dataOffset:Int64, buffer:Array, bufferOffset:int, length:int) -> Int64:
        """ GetBytes(self: DbDataReader, ordinal: int, dataOffset: Int64, buffer: Array[Byte], bufferOffset: int, length: int) -> Int64 """
        ...

    def GetChar(self, ordinal:int) -> Char:
        """ GetChar(self: DbDataReader, ordinal: int) -> Char """
        ...

    def GetChars(self, ordinal:int, dataOffset:Int64, buffer:Array, bufferOffset:int, length:int) -> Int64:
        """ GetChars(self: DbDataReader, ordinal: int, dataOffset: Int64, buffer: Array[Char], bufferOffset: int, length: int) -> Int64 """
        ...

    def GetData(self, ordinal:int) -> DbDataReader:
        """ GetData(self: DbDataReader, ordinal: int) -> DbDataReader """
        ...

    def GetDataTypeName(self, ordinal:int) -> str:
        """ GetDataTypeName(self: DbDataReader, ordinal: int) -> str """
        ...

    def GetDateTime(self, ordinal:int) -> DateTime:
        """ GetDateTime(self: DbDataReader, ordinal: int) -> DateTime """
        ...

    def GetDbDataReader(self, *args): #cannot find CLR method
        """ GetDbDataReader(self: DbDataReader, ordinal: int) -> DbDataReader """
        ...

    def GetDecimal(self, ordinal:int) -> Decimal:
        """ GetDecimal(self: DbDataReader, ordinal: int) -> Decimal """
        ...

    def GetDouble(self, ordinal:int) -> float:
        """ GetDouble(self: DbDataReader, ordinal: int) -> float """
        ...

    def GetFieldType(self, ordinal:int) -> Type:
        """ GetFieldType(self: DbDataReader, ordinal: int) -> Type """
        ...

    def GetFieldValue(self, ordinal:int): # -> T
        """ GetFieldValue[T](self: DbDataReader, ordinal: int) -> T """
        ...

    def GetFieldValueAsync(self, ordinal:int, cancellationToken:CancellationToken = ...) -> Task:
        """
        GetFieldValueAsync[T](self: DbDataReader, ordinal: int) -> Task[T]
        GetFieldValueAsync[T](self: DbDataReader, ordinal: int, cancellationToken: CancellationToken) -> Task[T]
        """
        ...

    def GetFloat(self, ordinal:int) -> Single:
        """ GetFloat(self: DbDataReader, ordinal: int) -> Single """
        ...

    def GetGuid(self, ordinal:int) -> Guid:
        """ GetGuid(self: DbDataReader, ordinal: int) -> Guid """
        ...

    def GetInt16(self, ordinal:int) -> Int16:
        """ GetInt16(self: DbDataReader, ordinal: int) -> Int16 """
        ...

    def GetInt32(self, ordinal:int) -> int:
        """ GetInt32(self: DbDataReader, ordinal: int) -> int """
        ...

    def GetInt64(self, ordinal:int) -> Int64:
        """ GetInt64(self: DbDataReader, ordinal: int) -> Int64 """
        ...

    def GetName(self, ordinal:int) -> str:
        """ GetName(self: DbDataReader, ordinal: int) -> str """
        ...

    def GetOrdinal(self, name:str) -> int:
        """ GetOrdinal(self: DbDataReader, name: str) -> int """
        ...

    def GetProviderSpecificFieldType(self, ordinal:int) -> Type:
        """ GetProviderSpecificFieldType(self: DbDataReader, ordinal: int) -> Type """
        ...

    def GetProviderSpecificValue(self, ordinal:int) -> object:
        """ GetProviderSpecificValue(self: DbDataReader, ordinal: int) -> object """
        ...

    def GetProviderSpecificValues(self, values:Array) -> int:
        """ GetProviderSpecificValues(self: DbDataReader, values: Array[object]) -> int """
        ...

    def GetStream(self, ordinal:int) -> Stream:
        """ GetStream(self: DbDataReader, ordinal: int) -> Stream """
        ...

    def GetString(self, ordinal:int) -> str:
        """ GetString(self: DbDataReader, ordinal: int) -> str """
        ...

    def GetTextReader(self, ordinal:int) -> TextReader:
        """ GetTextReader(self: DbDataReader, ordinal: int) -> TextReader """
        ...

    def GetValue(self, ordinal:int) -> object:
        """ GetValue(self: DbDataReader, ordinal: int) -> object """
        ...

    def GetValues(self, values:Array) -> int:
        """ GetValues(self: DbDataReader, values: Array[object]) -> int """
        ...

    def IsDBNull(self, ordinal:int) -> bool:
        """ IsDBNull(self: DbDataReader, ordinal: int) -> bool """
        ...

    def IsDBNullAsync(self, ordinal:int, cancellationToken:CancellationToken = ...) -> Task:
        """
        IsDBNullAsync(self: DbDataReader, ordinal: int, cancellationToken: CancellationToken) -> Task[bool]
        IsDBNullAsync(self: DbDataReader, ordinal: int) -> Task[bool]
        """
        ...

    def NextResultAsync(self, cancellationToken:CancellationToken = ...) -> Task:
        """
        NextResultAsync(self: DbDataReader, cancellationToken: CancellationToken) -> Task[bool]
        NextResultAsync(self: DbDataReader) -> Task[bool]
        """
        ...

    def ReadAsync(self, cancellationToken:CancellationToken = ...) -> Task:
        """
        ReadAsync(self: DbDataReader, cancellationToken: CancellationToken) -> Task[bool]
        ReadAsync(self: DbDataReader) -> Task[bool]
        """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class DbDataReaderExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CanGetColumnSchema(reader:DbDataReader) -> bool:
        """ CanGetColumnSchema(reader: DbDataReader) -> bool """
        ...

    @staticmethod
    def GetColumnSchema(reader:DbDataReader) -> ReadOnlyCollection:
        """ GetColumnSchema(reader: DbDataReader) -> ReadOnlyCollection[DbColumn] """
        ...

    __all__: list = ...


class DbDataRecord(IDataRecord, ICustomTypeDescriptor): # skipped bases: <type 'object'>
    """ no doc """
    def GetDbDataReader(self, *args): #cannot find CLR method
        """ GetDbDataReader(self: DbDataRecord, i: int) -> DbDataReader """
        ...


class DbDataSourceEnumerator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetDataSources(self) -> DataTable:
        """ GetDataSources(self: DbDataSourceEnumerator) -> DataTable """
        ...


class DbEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """
    DbEnumerator(reader: IDataReader)
    DbEnumerator(reader: IDataReader, closeReader: bool)
    DbEnumerator(reader: DbDataReader)
    DbEnumerator(reader: DbDataReader, closeReader: bool)
    """
    pass

class DbException(ExternalException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    SerializeObjectState = ...


class DbMetaDataCollectionNames: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    DataSourceInformation: str = ...
    DataTypes: str = ...
    MetaDataCollections: str = ...
    ReservedWords: str = ...
    Restrictions: str = ...
    __all__: list = ...


class DbMetaDataColumnNames: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    CollectionName: str = ...
    ColumnSize: str = ...
    CompositeIdentifierSeparatorPattern: str = ...
    CreateFormat: str = ...
    CreateParameters: str = ...
    DataSourceProductName: str = ...
    DataSourceProductVersion: str = ...
    DataSourceProductVersionNormalized: str = ...
    DataType: str = ...
    GroupByBehavior: str = ...
    IdentifierCase: str = ...
    IdentifierPattern: str = ...
    IsAutoIncrementable: str = ...
    IsBestMatch: str = ...
    IsCaseSensitive: str = ...
    IsConcurrencyType: str = ...
    IsFixedLength: str = ...
    IsFixedPrecisionScale: str = ...
    IsLiteralSupported: str = ...
    IsLong: str = ...
    IsNullable: str = ...
    IsSearchable: str = ...
    IsSearchableWithLike: str = ...
    IsUnsigned: str = ...
    LiteralPrefix: str = ...
    LiteralSuffix: str = ...
    MaximumScale: str = ...
    MinimumScale: str = ...
    NumberOfIdentifierParts: str = ...
    NumberOfRestrictions: str = ...
    OrderByColumnsInSelect: str = ...
    ParameterMarkerFormat: str = ...
    ParameterMarkerPattern: str = ...
    ParameterNameMaxLength: str = ...
    ParameterNamePattern: str = ...
    ProviderDbType: str = ...
    QuotedIdentifierCase: str = ...
    QuotedIdentifierPattern: str = ...
    ReservedWord: str = ...
    StatementSeparatorPattern: str = ...
    StringLiteralPattern: str = ...
    SupportedJoinOperators: str = ...
    TypeName: str = ...
    __all__: list = ...


class DbParameter(MarshalByRefObject, IDbDataParameter): # skipped bases: <type 'IDataParameter'>, <type 'object'>
    """ no doc """
    @property
    def DbType(self) -> DbType:
        """
        Get: DbType(self: DbParameter) -> DbType
        Set: DbType(self: DbParameter) = value
        """
        ...

    @property
    def Direction(self) -> ParameterDirection:
        """
        Get: Direction(self: DbParameter) -> ParameterDirection
        Set: Direction(self: DbParameter) = value
        """
        ...

    @property
    def IsNullable(self) -> bool:
        """
        Get: IsNullable(self: DbParameter) -> bool
        Set: IsNullable(self: DbParameter) = value
        """
        ...

    @property
    def ParameterName(self) -> str:
        """
        Get: ParameterName(self: DbParameter) -> str
        Set: ParameterName(self: DbParameter) = value
        """
        ...

    @property
    def SourceColumn(self) -> str:
        """
        Get: SourceColumn(self: DbParameter) -> str
        Set: SourceColumn(self: DbParameter) = value
        """
        ...

    @property
    def SourceColumnNullMapping(self) -> bool:
        """
        Get: SourceColumnNullMapping(self: DbParameter) -> bool
        Set: SourceColumnNullMapping(self: DbParameter) = value
        """
        ...

    @property
    def SourceVersion(self) -> DataRowVersion:
        """
        Get: SourceVersion(self: DbParameter) -> DataRowVersion
        Set: SourceVersion(self: DbParameter) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: DbParameter) -> object
        Set: Value(self: DbParameter) = value
        """
        ...


    def ResetDbType(self): # -> 
        """ ResetDbType(self: DbParameter) """
        ...


class DbParameterCollection(MarshalByRefObject, IDataParameterCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: DbParameterCollection) -> int """
        ...

    @property
    def IsFixedSize(self) -> bool:
        """ Get: IsFixedSize(self: DbParameterCollection) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: DbParameterCollection) -> bool """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: DbParameterCollection) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: DbParameterCollection) -> object """
        ...


    def Add(self, value:object) -> int:
        """ Add(self: DbParameterCollection, value: object) -> int """
        ...

    def AddRange(self, values:Array): # -> 
        """ AddRange(self: DbParameterCollection, values: Array) """
        ...

    def Clear(self): # -> 
        """ Clear(self: DbParameterCollection) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DbParameterCollection, array: Array, index: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DbParameterCollection) -> IEnumerator """
        ...

    def GetParameter(self, *args): #cannot find CLR method
        """
        GetParameter(self: DbParameterCollection, index: int) -> DbParameter
        GetParameter(self: DbParameterCollection, parameterName: str) -> DbParameter
        """
        ...

    def Insert(self, index:int, value:object): # -> 
        """ Insert(self: DbParameterCollection, index: int, value: object) """
        ...

    def Remove(self, value:object): # -> 
        """ Remove(self: DbParameterCollection, value: object) """
        ...

    def SetParameter(self, *args): #cannot find CLR method
        """ SetParameter(self: DbParameterCollection, index: int, value: DbParameter)SetParameter(self: DbParameterCollection, parameterName: str, value: DbParameter) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class DbProviderConfigurationHandler(IConfigurationSectionHandler): # skipped bases: <type 'object'>
    """ DbProviderConfigurationHandler() """
    pass

class DbProviderFactories: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetFactory(*__args:str) -> DbProviderFactory:
        """
        GetFactory(providerInvariantName: str) -> DbProviderFactory
        GetFactory(providerRow: DataRow) -> DbProviderFactory
        GetFactory(connection: DbConnection) -> DbProviderFactory
        """
        ...

    @staticmethod
    def GetFactoryClasses() -> DataTable:
        """ GetFactoryClasses() -> DataTable """
        ...

    __all__: list = ...


class DbProviderFactoriesConfigurationHandler(IConfigurationSectionHandler): # skipped bases: <type 'object'>
    """ DbProviderFactoriesConfigurationHandler() """
    pass

class DbProviderFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CanCreateDataSourceEnumerator(self) -> bool:
        """ Get: CanCreateDataSourceEnumerator(self: DbProviderFactory) -> bool """
        ...


    def CreateCommand(self) -> DbCommand:
        """ CreateCommand(self: DbProviderFactory) -> DbCommand """
        ...

    def CreateCommandBuilder(self) -> DbCommandBuilder:
        """ CreateCommandBuilder(self: DbProviderFactory) -> DbCommandBuilder """
        ...

    def CreateConnection(self) -> DbConnection:
        """ CreateConnection(self: DbProviderFactory) -> DbConnection """
        ...

    def CreateConnectionStringBuilder(self) -> DbConnectionStringBuilder:
        """ CreateConnectionStringBuilder(self: DbProviderFactory) -> DbConnectionStringBuilder """
        ...

    def CreateDataAdapter(self) -> DbDataAdapter:
        """ CreateDataAdapter(self: DbProviderFactory) -> DbDataAdapter """
        ...

    def CreateDataSourceEnumerator(self) -> DbDataSourceEnumerator:
        """ CreateDataSourceEnumerator(self: DbProviderFactory) -> DbDataSourceEnumerator """
        ...

    def CreateParameter(self) -> DbParameter:
        """ CreateParameter(self: DbProviderFactory) -> DbParameter """
        ...

    def CreatePermission(self, state:PermissionState) -> CodeAccessPermission:
        """ CreatePermission(self: DbProviderFactory, state: PermissionState) -> CodeAccessPermission """
        ...


class DbProviderManifest: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def NamespaceName(self) -> str:
        """ Get: NamespaceName(self: DbProviderManifest) -> str """
        ...


    def EscapeLikeArgument(self, argument:str) -> str:
        """ EscapeLikeArgument(self: DbProviderManifest, argument: str) -> str """
        ...

    def GetDbInformation(self, *args): #cannot find CLR method
        """ GetDbInformation(self: DbProviderManifest, informationType: str) -> XmlReader """
        ...

    def GetEdmType(self, storeType:TypeUsage) -> TypeUsage:
        """ GetEdmType(self: DbProviderManifest, storeType: TypeUsage) -> TypeUsage """
        ...

    def GetFacetDescriptions(self, edmType:EdmType) -> ReadOnlyCollection:
        """ GetFacetDescriptions(self: DbProviderManifest, edmType: EdmType) -> ReadOnlyCollection[FacetDescription] """
        ...

    def GetInformation(self, informationType:str) -> XmlReader:
        """ GetInformation(self: DbProviderManifest, informationType: str) -> XmlReader """
        ...

    def GetStoreFunctions(self) -> ReadOnlyCollection:
        """ GetStoreFunctions(self: DbProviderManifest) -> ReadOnlyCollection[EdmFunction] """
        ...

    def GetStoreType(self, edmType:TypeUsage) -> TypeUsage:
        """ GetStoreType(self: DbProviderManifest, edmType: TypeUsage) -> TypeUsage """
        ...

    def GetStoreTypes(self) -> ReadOnlyCollection:
        """ GetStoreTypes(self: DbProviderManifest) -> ReadOnlyCollection[PrimitiveType] """
        ...

    def SupportsEscapingLikeArgument(self, escapeCharacter) -> Tuple_[bool, Char]:
        """ SupportsEscapingLikeArgument(self: DbProviderManifest) -> (bool, Char) """
        ...

    ConceptualSchemaDefinition: str = ...
    ConceptualSchemaDefinitionVersion3: str = ...
    StoreSchemaDefinition: str = ...
    StoreSchemaDefinitionVersion3: str = ...
    StoreSchemaMapping: str = ...
    StoreSchemaMappingVersion3: str = ...


class DbProviderServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateCommandDefinition(self, *__args:DbCommand) -> DbCommandDefinition:
        """
        CreateCommandDefinition(self: DbProviderServices, providerManifest: DbProviderManifest, commandTree: DbCommandTree) -> DbCommandDefinition
        CreateCommandDefinition(self: DbProviderServices, prototype: DbCommand) -> DbCommandDefinition
        CreateCommandDefinition(self: DbProviderServices, commandTree: DbCommandTree) -> DbCommandDefinition
        """
        ...

    def CreateDatabase(self, connection:DbConnection, commandTimeout:Nullable, storeItemCollection:StoreItemCollection): # -> 
        """ CreateDatabase(self: DbProviderServices, connection: DbConnection, commandTimeout: Nullable[int], storeItemCollection: StoreItemCollection) """
        ...

    def CreateDatabaseScript(self, providerManifestToken:str, storeItemCollection:StoreItemCollection) -> str:
        """ CreateDatabaseScript(self: DbProviderServices, providerManifestToken: str, storeItemCollection: StoreItemCollection) -> str """
        ...

    def CreateDbCommandDefinition(self, *args): #cannot find CLR method
        """ CreateDbCommandDefinition(self: DbProviderServices, providerManifest: DbProviderManifest, commandTree: DbCommandTree) -> DbCommandDefinition """
        ...

    def DatabaseExists(self, connection:DbConnection, commandTimeout:Nullable, storeItemCollection:StoreItemCollection) -> bool:
        """ DatabaseExists(self: DbProviderServices, connection: DbConnection, commandTimeout: Nullable[int], storeItemCollection: StoreItemCollection) -> bool """
        ...

    def DbCreateDatabase(self, *args): #cannot find CLR method
        """ DbCreateDatabase(self: DbProviderServices, connection: DbConnection, commandTimeout: Nullable[int], storeItemCollection: StoreItemCollection) """
        ...

    def DbCreateDatabaseScript(self, *args): #cannot find CLR method
        """ DbCreateDatabaseScript(self: DbProviderServices, providerManifestToken: str, storeItemCollection: StoreItemCollection) -> str """
        ...

    def DbDatabaseExists(self, *args): #cannot find CLR method
        """ DbDatabaseExists(self: DbProviderServices, connection: DbConnection, commandTimeout: Nullable[int], storeItemCollection: StoreItemCollection) -> bool """
        ...

    def DbDeleteDatabase(self, *args): #cannot find CLR method
        """ DbDeleteDatabase(self: DbProviderServices, connection: DbConnection, commandTimeout: Nullable[int], storeItemCollection: StoreItemCollection) """
        ...

    def DbGetSpatialServices(self, *args): #cannot find CLR method
        """ DbGetSpatialServices(self: DbProviderServices, manifestToken: str) -> DbSpatialServices """
        ...

    def DeleteDatabase(self, connection:DbConnection, commandTimeout:Nullable, storeItemCollection:StoreItemCollection): # -> 
        """ DeleteDatabase(self: DbProviderServices, connection: DbConnection, commandTimeout: Nullable[int], storeItemCollection: StoreItemCollection) """
        ...

    def GetDbProviderManifest(self, *args): #cannot find CLR method
        """ GetDbProviderManifest(self: DbProviderServices, manifestToken: str) -> DbProviderManifest """
        ...

    def GetDbProviderManifestToken(self, *args): #cannot find CLR method
        """ GetDbProviderManifestToken(self: DbProviderServices, connection: DbConnection) -> str """
        ...

    def GetDbSpatialDataReader(self, *args): #cannot find CLR method
        """ GetDbSpatialDataReader(self: DbProviderServices, fromReader: DbDataReader, manifestToken: str) -> DbSpatialDataReader """
        ...

    @staticmethod
    def GetProviderFactory(connection:DbConnection) -> DbProviderFactory:
        """ GetProviderFactory(connection: DbConnection) -> DbProviderFactory """
        ...

    def GetProviderManifest(self, manifestToken:str) -> DbProviderManifest:
        """ GetProviderManifest(self: DbProviderServices, manifestToken: str) -> DbProviderManifest """
        ...

    def GetProviderManifestToken(self, connection:DbConnection) -> str:
        """ GetProviderManifestToken(self: DbProviderServices, connection: DbConnection) -> str """
        ...

    @staticmethod
    def GetProviderServices(connection:DbConnection) -> DbProviderServices:
        """ GetProviderServices(connection: DbConnection) -> DbProviderServices """
        ...

    def GetSpatialDataReader(self, fromReader:DbDataReader, manifestToken:str) -> DbSpatialDataReader:
        """ GetSpatialDataReader(self: DbProviderServices, fromReader: DbDataReader, manifestToken: str) -> DbSpatialDataReader """
        ...

    def GetSpatialServices(self, manifestToken:str) -> DbSpatialServices:
        """ GetSpatialServices(self: DbProviderServices, manifestToken: str) -> DbSpatialServices """
        ...

    def SetDbParameterValue(self, *args): #cannot find CLR method
        """ SetDbParameterValue(self: DbProviderServices, parameter: DbParameter, parameterType: TypeUsage, value: object) """
        ...


class DbProviderSpecificTypePropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DbProviderSpecificTypePropertyAttribute(isProviderSpecificTypeProperty: bool) """
    @property
    def IsProviderSpecificTypeProperty(self) -> bool:
        """ Get: IsProviderSpecificTypeProperty(self: DbProviderSpecificTypePropertyAttribute) -> bool """
        ...


    def __new__(cls, isProviderSpecificTypeProperty:bool) -> Self:
        """ __new__(cls: type, isProviderSpecificTypeProperty: bool) """
        ...


class DbTransaction(MarshalByRefObject, IDbTransaction): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def DbConnection(self):
        ...


    def Dispose(self): # -> 
        """ Dispose(self: DbTransaction) """
        ...


class DbXmlEnabledProviderManifest(DbProviderManifest): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def StoreTypeNameToEdmPrimitiveType(self):
        ...

    @property
    def StoreTypeNameToStorePrimitiveType(self):
        ...


    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, reader: XmlReader) """
        ...


class EntityRecordInfo(DataRecordInfo): # skipped bases: <type 'object'>
    """ EntityRecordInfo(metadata: EntityType, memberInfo: IEnumerable[EdmMember], entityKey: EntityKey, entitySet: EntitySet) """
    @property
    def EntityKey(self) -> EntityKey:
        """ Get: EntityKey(self: EntityRecordInfo) -> EntityKey """
        ...



class FieldMetadata: # skipped bases: <type 'object'>, <type 'object'>
    """ FieldMetadata(ordinal: int, fieldType: EdmMember) """
    @property
    def FieldType(self) -> EdmMember:
        """ Get: FieldType(self: FieldMetadata) -> EdmMember """
        ...

    @property
    def Ordinal(self) -> int:
        """ Get: Ordinal(self: FieldMetadata) -> int """
        ...



class GroupByBehavior(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GroupByBehavior, values: ExactMatch (4), MustContainAll (3), NotSupported (1), Unknown (0), Unrelated (2) """
    ExactMatch: GroupByBehavior = ...
    MustContainAll: GroupByBehavior = ...
    NotSupported: GroupByBehavior = ...
    Unknown: GroupByBehavior = ...
    Unrelated: GroupByBehavior = ...
    value__ = ...


class IDbColumnSchemaGenerator: # skipped bases: <type 'object'>
    """ no doc """
    def GetColumnSchema(self) -> ReadOnlyCollection:
        """ GetColumnSchema(self: IDbColumnSchemaGenerator) -> ReadOnlyCollection[DbColumn] """
        ...


class IdentifierCase(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum IdentifierCase, values: Insensitive (1), Sensitive (2), Unknown (0) """
    Insensitive: IdentifierCase = ...
    Sensitive: IdentifierCase = ...
    Unknown: IdentifierCase = ...
    value__ = ...


class RowUpdatedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ RowUpdatedEventArgs(dataRow: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping) """
    @property
    def Command(self) -> IDbCommand:
        """ Get: Command(self: RowUpdatedEventArgs) -> IDbCommand """
        ...

    @property
    def Errors(self) -> Exception:
        """
        Get: Errors(self: RowUpdatedEventArgs) -> Exception
        Set: Errors(self: RowUpdatedEventArgs) = value
        """
        ...

    @property
    def RecordsAffected(self) -> int:
        """ Get: RecordsAffected(self: RowUpdatedEventArgs) -> int """
        ...

    @property
    def Row(self) -> DataRow:
        """ Get: Row(self: RowUpdatedEventArgs) -> DataRow """
        ...

    @property
    def RowCount(self) -> int:
        """ Get: RowCount(self: RowUpdatedEventArgs) -> int """
        ...

    @property
    def StatementType(self) -> StatementType:
        """ Get: StatementType(self: RowUpdatedEventArgs) -> StatementType """
        ...

    @property
    def Status(self) -> UpdateStatus:
        """
        Get: Status(self: RowUpdatedEventArgs) -> UpdateStatus
        Set: Status(self: RowUpdatedEventArgs) = value
        """
        ...

    @property
    def TableMapping(self) -> DataTableMapping:
        """ Get: TableMapping(self: RowUpdatedEventArgs) -> DataTableMapping """
        ...


    def CopyToRows(self, array:Array, arrayIndex:int = ...): # -> 
        """ CopyToRows(self: RowUpdatedEventArgs, array: Array[DataRow])CopyToRows(self: RowUpdatedEventArgs, array: Array[DataRow], arrayIndex: int) """
        ...

    def __new__(cls, dataRow:DataRow, command:IDbCommand, statementType:StatementType, tableMapping:DataTableMapping) -> Self:
        """ __new__(cls: type, dataRow: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping) """
        ...


class RowUpdatingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ RowUpdatingEventArgs(dataRow: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping) """
    @property
    def BaseCommand(self):
        ...

    @property
    def Command(self) -> IDbCommand:
        """
        Get: Command(self: RowUpdatingEventArgs) -> IDbCommand
        Set: Command(self: RowUpdatingEventArgs) = value
        """
        ...

    @property
    def Errors(self) -> Exception:
        """
        Get: Errors(self: RowUpdatingEventArgs) -> Exception
        Set: Errors(self: RowUpdatingEventArgs) = value
        """
        ...

    @property
    def Row(self) -> DataRow:
        """ Get: Row(self: RowUpdatingEventArgs) -> DataRow """
        ...

    @property
    def StatementType(self) -> StatementType:
        """ Get: StatementType(self: RowUpdatingEventArgs) -> StatementType """
        ...

    @property
    def Status(self) -> UpdateStatus:
        """
        Get: Status(self: RowUpdatingEventArgs) -> UpdateStatus
        Set: Status(self: RowUpdatingEventArgs) = value
        """
        ...

    @property
    def TableMapping(self) -> DataTableMapping:
        """ Get: TableMapping(self: RowUpdatingEventArgs) -> DataTableMapping """
        ...


    def __new__(cls, dataRow:DataRow, command:IDbCommand, statementType:StatementType, tableMapping:DataTableMapping) -> Self:
        """ __new__(cls: type, dataRow: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping) """
        ...


class SchemaTableColumn: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    AllowDBNull: str = ...
    BaseColumnName: str = ...
    BaseSchemaName: str = ...
    BaseTableName: str = ...
    ColumnName: str = ...
    ColumnOrdinal: str = ...
    ColumnSize: str = ...
    DataType: str = ...
    IsAliased: str = ...
    IsExpression: str = ...
    IsKey: str = ...
    IsLong: str = ...
    IsUnique: str = ...
    NonVersionedProviderType: str = ...
    NumericPrecision: str = ...
    NumericScale: str = ...
    ProviderType: str = ...
    __all__: list = ...


class SchemaTableOptionalColumn: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    AutoIncrementSeed: str = ...
    AutoIncrementStep: str = ...
    BaseCatalogName: str = ...
    BaseColumnNamespace: str = ...
    BaseServerName: str = ...
    BaseTableNamespace: str = ...
    ColumnMapping: str = ...
    DefaultValue: str = ...
    Expression: str = ...
    IsAutoIncrement: str = ...
    IsHidden: str = ...
    IsReadOnly: str = ...
    IsRowVersion: str = ...
    ProviderSpecificDataType: str = ...
    __all__: list = ...


class SupportedJoinOperators(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SupportedJoinOperators, values: FullOuter (8), Inner (1), LeftOuter (2), None (0), RightOuter (4) """
    FullOuter: SupportedJoinOperators = ...
    Inner: SupportedJoinOperators = ...
    LeftOuter: SupportedJoinOperators = ...
    RightOuter: SupportedJoinOperators = ...
    value__ = ...


# variables with complex values

