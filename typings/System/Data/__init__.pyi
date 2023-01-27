# encoding: utf-8
# module System.Data calls itself Data
# from System.Data.Linq, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Data.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Data.Services.Client, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Data.Entity.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Data.OracleClient, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Data.Services, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Data.Services.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Data.DataSetExtensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Build.Framework.XamlTypes import Rule

from Microsoft.Office.Interop.Graph import DataTable

from Microsoft.SqlServer.Management.SqlParser.MetadataProvider import (
    ConstraintCollection)

from System import (Array, AsyncCallback, Byte, Char, DateTime, Decimal, Enum, 
    EventArgs, Guid, IAsyncResult, IDisposable, IEquatable, Int16, Int64, 
    MulticastDelegate, Single, SystemException, Type)

from System.Activities.Validation import Constraint

from System.CodeDom import CodeNamespace

from System.CodeDom.Compiler import ICodeGenerator

from System.Collections import (ArrayList, Hashtable, ICollection, IComparer, 
    IEnumerable, IEnumerator, IList)

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel import (IBindingList, IBindingListView, 
    ICustomTypeDescriptor, IDataErrorInfo, IEditableObject, IListSource, 
    INotifyPropertyChanged, ISupportInitializeNotification, ITypedList, 
    MarshalByValueComponent)

from System.Data.Common import DbDataReader, DbDataRecord

from System.Data.Linq import EntitySet

from System.Data.Metadata.Edm import MetadataWorkspace

from System.DirectoryServices import PropertyCollection

from System.EnterpriseServices import DescriptionAttribute

from System.Globalization import CultureInfo

from System.IO import Stream

from System.Reflection import PropertyAttributes

from System.Runtime.Serialization import (ISerializable, SerializationInfo, 
    StreamingContext)

from System.Transactions import IsolationLevel

from System.Xml import XmlReader

from System.Xml.Schema import XmlSchemaComplexType, XmlSchemaSet

from System.Xml.Serialization import IXmlSerializable

from System.Xml.Serialization.Advanced import SchemaImporterExtension

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    DataRecordInfo, DataRow, DataRowState, DataRowVersion, DataSet, 
    DataSetDateTime, DataTableCollection, DataTableReader, DataView, 
    DataViewManager, DataViewRowState, DataViewSettingCollection, 
    EnumerableRowCollection, FillErrorEventHandler, ForeignKeyConstraint, 
    Func, IDataReader, IDbConnection, IDbDataParameter, IDbTransaction, 
    ITableMappingCollection, LoadOption, MappingType, MissingMappingAction, 
    MissingSchemaAction, OrderedEnumerableRowCollection, ParameterDirection, 
    SchemaSerializationMode, SchemaType, SerializationFormat, T, TRow, 
    UniqueConstraint, UpdateRowSource, field#)
"""

# no functions
# classes

class AcceptRejectRule(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AcceptRejectRule, values: Cascade (1), None (0) """
    Cascade: AcceptRejectRule = ...
    value__ = ...


class CommandBehavior(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CommandBehavior, values: CloseConnection (32), Default (0), KeyInfo (4), SchemaOnly (2), SequentialAccess (16), SingleResult (1), SingleRow (8) """
    CloseConnection: CommandBehavior = ...
    Default: CommandBehavior = ...
    KeyInfo: CommandBehavior = ...
    SchemaOnly: CommandBehavior = ...
    SequentialAccess: CommandBehavior = ...
    SingleResult: CommandBehavior = ...
    SingleRow: CommandBehavior = ...
    value__ = ...


class CommandType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CommandType, values: StoredProcedure (4), TableDirect (512), Text (1) """
    StoredProcedure: CommandType = ...
    TableDirect: CommandType = ...
    Text: CommandType = ...
    value__ = ...


class ConflictOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConflictOption, values: CompareAllSearchableValues (1), CompareRowVersion (2), OverwriteChanges (3) """
    CompareAllSearchableValues: ConflictOption = ...
    CompareRowVersion: ConflictOption = ...
    OverwriteChanges: ConflictOption = ...
    value__ = ...


class ConnectionState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ConnectionState, values: Broken (16), Closed (0), Connecting (2), Executing (4), Fetching (8), Open (1) """
    Broken: ConnectionState = ...
    Closed: ConnectionState = ...
    Connecting: ConnectionState = ...
    Executing: ConnectionState = ...
    Fetching: ConnectionState = ...
    Open: ConnectionState = ...
    value__ = ...


class Constraint: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ConstraintName(self) -> str:
        """
        Get: ConstraintName(self: Constraint) -> str
        Set: ConstraintName(self: Constraint) = value
        """
        ...

    @property
    def ExtendedProperties(self) -> PropertyCollection:
        """ Get: ExtendedProperties(self: Constraint) -> PropertyCollection """
        ...

    @property
    def Table(self) -> DataTable:
        """ Get: Table(self: Constraint) -> DataTable """
        ...

    @property
    def _DataSet(self):
        ...


    def CheckStateForProperty(self, *args): #cannot find CLR method
        """ CheckStateForProperty(self: Constraint) """
        ...

    def SetDataSet(self, *args): #cannot find CLR method
        """ SetDataSet(self: Constraint, dataSet: DataSet) """
        ...

    def ToString(self) -> str:
        """ ToString(self: Constraint) -> str """
        ...


class InternalDataCollectionBase(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ InternalDataCollectionBase() """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: InternalDataCollectionBase) -> bool """
        ...

    @property
    def List(self):
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: InternalDataCollectionBase) -> IEnumerator """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class ConstraintCollection(InternalDataCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Add(self, *__args:Constraint): # -> 
        """
        Add(self: ConstraintCollection, constraint: Constraint)Add(self: ConstraintCollection, name: str, columns: Array[DataColumn], primaryKey: bool) -> Constraint
        Add(self: ConstraintCollection, name: str, column: DataColumn, primaryKey: bool) -> Constraint
        Add(self: ConstraintCollection, name: str, primaryKeyColumn: DataColumn, foreignKeyColumn: DataColumn) -> Constraint
        Add(self: ConstraintCollection, name: str, primaryKeyColumns: Array[DataColumn], foreignKeyColumns: Array[DataColumn]) -> Constraint
        """
        ...

    def AddRange(self, constraints:Array): # -> 
        """ AddRange(self: ConstraintCollection, constraints: Array[Constraint]) """
        ...

    def CanRemove(self, constraint:Constraint) -> bool:
        """ CanRemove(self: ConstraintCollection, constraint: Constraint) -> bool """
        ...

    def Clear(self): # -> 
        """ Clear(self: ConstraintCollection) """
        ...

    def Contains(self, name:str) -> bool:
        """ Contains(self: ConstraintCollection, name: str) -> bool """
        ...

    def IndexOf(self, *__args:Constraint) -> int:
        """
        IndexOf(self: ConstraintCollection, constraint: Constraint) -> int
        IndexOf(self: ConstraintCollection, constraintName: str) -> int
        """
        ...

    def Remove(self, *__args:Constraint): # -> 
        """ Remove(self: ConstraintCollection, constraint: Constraint)Remove(self: ConstraintCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: ConstraintCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    CollectionChanged = ...


class DataException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DataException()
    DataException(s: str)
    DataException(s: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ConstraintException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ConstraintException()
    ConstraintException(s: str)
    ConstraintException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class DataColumn(MarshalByValueComponent): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IServiceProvider'>, <type 'object'>
    """
    DataColumn()
    DataColumn(columnName: str)
    DataColumn(columnName: str, dataType: Type)
    DataColumn(columnName: str, dataType: Type, expr: str)
    DataColumn(columnName: str, dataType: Type, expr: str, type: MappingType)
    """
    @property
    def AllowDBNull(self) -> bool:
        """
        Get: AllowDBNull(self: DataColumn) -> bool
        Set: AllowDBNull(self: DataColumn) = value
        """
        ...

    @property
    def AutoIncrement(self) -> bool:
        """
        Get: AutoIncrement(self: DataColumn) -> bool
        Set: AutoIncrement(self: DataColumn) = value
        """
        ...

    @property
    def AutoIncrementSeed(self) -> Int64:
        """
        Get: AutoIncrementSeed(self: DataColumn) -> Int64
        Set: AutoIncrementSeed(self: DataColumn) = value
        """
        ...

    @property
    def AutoIncrementStep(self) -> Int64:
        """
        Get: AutoIncrementStep(self: DataColumn) -> Int64
        Set: AutoIncrementStep(self: DataColumn) = value
        """
        ...

    @property
    def Caption(self) -> str:
        """
        Get: Caption(self: DataColumn) -> str
        Set: Caption(self: DataColumn) = value
        """
        ...

    @property
    def ColumnMapping(self): # -> MappingType
        """
        Get: ColumnMapping(self: DataColumn) -> MappingType
        Set: ColumnMapping(self: DataColumn) = value
        """
        ...

    @property
    def ColumnName(self) -> str:
        """
        Get: ColumnName(self: DataColumn) -> str
        Set: ColumnName(self: DataColumn) = value
        """
        ...

    @property
    def DataType(self) -> Type:
        """
        Get: DataType(self: DataColumn) -> Type
        Set: DataType(self: DataColumn) = value
        """
        ...

    @property
    def DateTimeMode(self): # -> DataSetDateTime
        """
        Get: DateTimeMode(self: DataColumn) -> DataSetDateTime
        Set: DateTimeMode(self: DataColumn) = value
        """
        ...

    @property
    def DefaultValue(self) -> object:
        """
        Get: DefaultValue(self: DataColumn) -> object
        Set: DefaultValue(self: DataColumn) = value
        """
        ...

    @property
    def Expression(self) -> str:
        """
        Get: Expression(self: DataColumn) -> str
        Set: Expression(self: DataColumn) = value
        """
        ...

    @property
    def ExtendedProperties(self) -> PropertyCollection:
        """ Get: ExtendedProperties(self: DataColumn) -> PropertyCollection """
        ...

    @property
    def MaxLength(self) -> int:
        """
        Get: MaxLength(self: DataColumn) -> int
        Set: MaxLength(self: DataColumn) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: DataColumn) -> str
        Set: Namespace(self: DataColumn) = value
        """
        ...

    @property
    def Ordinal(self) -> int:
        """ Get: Ordinal(self: DataColumn) -> int """
        ...

    @property
    def Prefix(self) -> str:
        """
        Get: Prefix(self: DataColumn) -> str
        Set: Prefix(self: DataColumn) = value
        """
        ...

    @property
    def ReadOnly(self) -> bool:
        """
        Get: ReadOnly(self: DataColumn) -> bool
        Set: ReadOnly(self: DataColumn) = value
        """
        ...

    @property
    def Table(self) -> DataTable:
        """ Get: Table(self: DataColumn) -> DataTable """
        ...

    @property
    def Unique(self) -> bool:
        """
        Get: Unique(self: DataColumn) -> bool
        Set: Unique(self: DataColumn) = value
        """
        ...


    def CheckNotAllowNull(self, *args): #cannot find CLR method
        """ CheckNotAllowNull(self: DataColumn) """
        ...

    def CheckUnique(self, *args): #cannot find CLR method
        """ CheckUnique(self: DataColumn) """
        ...

    def OnPropertyChanging(self, *args): #cannot find CLR method
        """ OnPropertyChanging(self: DataColumn, pcevent: PropertyChangedEventArgs) """
        ...

    def RaisePropertyChanging(self, *args): #cannot find CLR method
        """ RaisePropertyChanging(self: DataColumn, name: str) """
        ...

    def SetOrdinal(self, ordinal:int): # -> 
        """ SetOrdinal(self: DataColumn, ordinal: int) """
        ...

    def __new__(cls, columnName:str = ..., dataType:Type = ..., expr:str = ..., type = ...) -> Self: # Not found arg types: {'type': 'MappingType'}
        """
        __new__(cls: type)
        __new__(cls: type, columnName: str)
        __new__(cls: type, columnName: str, dataType: Type)
        __new__(cls: type, columnName: str, dataType: Type, expr: str)
        __new__(cls: type, columnName: str, dataType: Type, expr: str, type: MappingType)
        """
        ...


class DataColumnChangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DataColumnChangeEventArgs(row: DataRow, column: DataColumn, value: object) """
    @property
    def Column(self) -> DataColumn:
        """ Get: Column(self: DataColumnChangeEventArgs) -> DataColumn """
        ...

    @property
    def ProposedValue(self) -> object:
        """
        Get: ProposedValue(self: DataColumnChangeEventArgs) -> object
        Set: ProposedValue(self: DataColumnChangeEventArgs) = value
        """
        ...

    @property
    def Row(self): # -> DataRow
        """ Get: Row(self: DataColumnChangeEventArgs) -> DataRow """
        ...


    def __new__(cls, row, column:DataColumn, value:object) -> Self: # Not found arg types: {'row': 'DataRow'}
        """ __new__(cls: type, row: DataRow, column: DataColumn, value: object) """
        ...


class DataColumnChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataColumnChangeEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DataColumnChangeEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataColumnChangeEventHandler, sender: object, e: DataColumnChangeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DataColumnChangeEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DataColumnChangeEventArgs): # -> 
        """ Invoke(self: DataColumnChangeEventHandler, sender: object, e: DataColumnChangeEventArgs) """
        ...


class DataColumnCollection(InternalDataCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Add(self, *__args:DataColumn): # -> 
        """
        Add(self: DataColumnCollection, column: DataColumn)Add(self: DataColumnCollection, columnName: str, type: Type, expression: str) -> DataColumn
        Add(self: DataColumnCollection, columnName: str, type: Type) -> DataColumn
        Add(self: DataColumnCollection, columnName: str) -> DataColumn
        Add(self: DataColumnCollection) -> DataColumn
        """
        ...

    def AddRange(self, columns:Array): # -> 
        """ AddRange(self: DataColumnCollection, columns: Array[DataColumn]) """
        ...

    def CanRemove(self, column:DataColumn) -> bool:
        """ CanRemove(self: DataColumnCollection, column: DataColumn) -> bool """
        ...

    def Clear(self): # -> 
        """ Clear(self: DataColumnCollection) """
        ...

    def Contains(self, name:str) -> bool:
        """ Contains(self: DataColumnCollection, name: str) -> bool """
        ...

    def IndexOf(self, *__args:DataColumn) -> int:
        """
        IndexOf(self: DataColumnCollection, column: DataColumn) -> int
        IndexOf(self: DataColumnCollection, columnName: str) -> int
        """
        ...

    def Remove(self, *__args:DataColumn): # -> 
        """ Remove(self: DataColumnCollection, column: DataColumn)Remove(self: DataColumnCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: DataColumnCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    CollectionChanged = ...


class DataRelation: # skipped bases: <type 'object'>, <type 'object'>
    """
    DataRelation(relationName: str, parentColumn: DataColumn, childColumn: DataColumn)
    DataRelation(relationName: str, parentColumn: DataColumn, childColumn: DataColumn, createConstraints: bool)
    DataRelation(relationName: str, parentColumns: Array[DataColumn], childColumns: Array[DataColumn])
    DataRelation(relationName: str, parentColumns: Array[DataColumn], childColumns: Array[DataColumn], createConstraints: bool)
    DataRelation(relationName: str, parentTableName: str, childTableName: str, parentColumnNames: Array[str], childColumnNames: Array[str], nested: bool)
    DataRelation(relationName: str, parentTableName: str, parentTableNamespace: str, childTableName: str, childTableNamespace: str, parentColumnNames: Array[str], childColumnNames: Array[str], nested: bool)
    """
    @property
    def ChildColumns(self) -> Array:
        """ Get: ChildColumns(self: DataRelation) -> Array[DataColumn] """
        ...

    @property
    def ChildKeyConstraint(self): # -> ForeignKeyConstraint
        """ Get: ChildKeyConstraint(self: DataRelation) -> ForeignKeyConstraint """
        ...

    @property
    def ChildTable(self) -> DataTable:
        """ Get: ChildTable(self: DataRelation) -> DataTable """
        ...

    @property
    def DataSet(self): # -> DataSet
        """ Get: DataSet(self: DataRelation) -> DataSet """
        ...

    @property
    def ExtendedProperties(self) -> PropertyCollection:
        """ Get: ExtendedProperties(self: DataRelation) -> PropertyCollection """
        ...

    @property
    def Nested(self) -> bool:
        """
        Get: Nested(self: DataRelation) -> bool
        Set: Nested(self: DataRelation) = value
        """
        ...

    @property
    def ParentColumns(self) -> Array:
        """ Get: ParentColumns(self: DataRelation) -> Array[DataColumn] """
        ...

    @property
    def ParentKeyConstraint(self): # -> UniqueConstraint
        """ Get: ParentKeyConstraint(self: DataRelation) -> UniqueConstraint """
        ...

    @property
    def ParentTable(self) -> DataTable:
        """ Get: ParentTable(self: DataRelation) -> DataTable """
        ...

    @property
    def RelationName(self) -> str:
        """
        Get: RelationName(self: DataRelation) -> str
        Set: RelationName(self: DataRelation) = value
        """
        ...


    def CheckStateForProperty(self, *args): #cannot find CLR method
        """ CheckStateForProperty(self: DataRelation) """
        ...

    def OnPropertyChanging(self, *args): #cannot find CLR method
        """ OnPropertyChanging(self: DataRelation, pcevent: PropertyChangedEventArgs) """
        ...

    def RaisePropertyChanging(self, *args): #cannot find CLR method
        """ RaisePropertyChanging(self: DataRelation, name: str) """
        ...

    def ToString(self) -> str:
        """ ToString(self: DataRelation) -> str """
        ...


class DataRelationCollection(InternalDataCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Add(self, *__args:DataRelation): # -> 
        """
        Add(self: DataRelationCollection, name: str, parentColumns: Array[DataColumn], childColumns: Array[DataColumn]) -> DataRelation
        Add(self: DataRelationCollection, name: str, parentColumns: Array[DataColumn], childColumns: Array[DataColumn], createConstraints: bool) -> DataRelation
        Add(self: DataRelationCollection, parentColumns: Array[DataColumn], childColumns: Array[DataColumn]) -> DataRelation
        Add(self: DataRelationCollection, name: str, parentColumn: DataColumn, childColumn: DataColumn) -> DataRelation
        Add(self: DataRelationCollection, name: str, parentColumn: DataColumn, childColumn: DataColumn, createConstraints: bool) -> DataRelation
        Add(self: DataRelationCollection, parentColumn: DataColumn, childColumn: DataColumn) -> DataRelation
        Add(self: DataRelationCollection, relation: DataRelation)
        """
        ...

    def AddCore(self, *args): #cannot find CLR method
        """ AddCore(self: DataRelationCollection, relation: DataRelation) """
        ...

    def AddRange(self, relations:Array): # -> 
        """ AddRange(self: DataRelationCollection, relations: Array[DataRelation]) """
        ...

    def CanRemove(self, relation:DataRelation) -> bool:
        """ CanRemove(self: DataRelationCollection, relation: DataRelation) -> bool """
        ...

    def Clear(self): # -> 
        """ Clear(self: DataRelationCollection) """
        ...

    def Contains(self, name:str) -> bool:
        """ Contains(self: DataRelationCollection, name: str) -> bool """
        ...

    def GetDataSet(self, *args): #cannot find CLR method
        """ GetDataSet(self: DataRelationCollection) -> DataSet """
        ...

    def IndexOf(self, *__args:DataRelation) -> int:
        """
        IndexOf(self: DataRelationCollection, relation: DataRelation) -> int
        IndexOf(self: DataRelationCollection, relationName: str) -> int
        """
        ...

    def OnCollectionChanged(self, *args): #cannot find CLR method
        """ OnCollectionChanged(self: DataRelationCollection, ccevent: CollectionChangeEventArgs) """
        ...

    def OnCollectionChanging(self, *args): #cannot find CLR method
        """ OnCollectionChanging(self: DataRelationCollection, ccevent: CollectionChangeEventArgs) """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: DataRelationCollection, name: str)Remove(self: DataRelationCollection, relation: DataRelation) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: DataRelationCollection, index: int) """
        ...

    def RemoveCore(self, *args): #cannot find CLR method
        """ RemoveCore(self: DataRelationCollection, relation: DataRelation) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    CollectionChanged = ...


class DataRow: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def HasErrors(self) -> bool:
        """ Get: HasErrors(self: DataRow) -> bool """
        ...

    @property
    def ItemArray(self) -> Array:
        """
        Get: ItemArray(self: DataRow) -> Array[object]
        Set: ItemArray(self: DataRow) = value
        """
        ...

    @property
    def RowError(self) -> str:
        """
        Get: RowError(self: DataRow) -> str
        Set: RowError(self: DataRow) = value
        """
        ...

    @property
    def RowState(self): # -> DataRowState
        """ Get: RowState(self: DataRow) -> DataRowState """
        ...

    @property
    def Table(self) -> DataTable:
        """ Get: Table(self: DataRow) -> DataTable """
        ...


    def AcceptChanges(self): # -> 
        """ AcceptChanges(self: DataRow) """
        ...

    def BeginEdit(self): # -> 
        """ BeginEdit(self: DataRow) """
        ...

    def CancelEdit(self): # -> 
        """ CancelEdit(self: DataRow) """
        ...

    def ClearErrors(self): # -> 
        """ ClearErrors(self: DataRow) """
        ...

    def Delete(self): # -> 
        """ Delete(self: DataRow) """
        ...

    def EndEdit(self): # -> 
        """ EndEdit(self: DataRow) """
        ...

    def GetChildRows(self, *__args:str) -> Array:
        """
        GetChildRows(self: DataRow, relationName: str) -> Array[DataRow]
        GetChildRows(self: DataRow, relationName: str, version: DataRowVersion) -> Array[DataRow]
        GetChildRows(self: DataRow, relation: DataRelation) -> Array[DataRow]
        GetChildRows(self: DataRow, relation: DataRelation, version: DataRowVersion) -> Array[DataRow]
        """
        ...

    def GetColumnError(self, *__args:int) -> str:
        """
        GetColumnError(self: DataRow, columnIndex: int) -> str
        GetColumnError(self: DataRow, columnName: str) -> str
        GetColumnError(self: DataRow, column: DataColumn) -> str
        """
        ...

    def GetColumnsInError(self) -> Array:
        """ GetColumnsInError(self: DataRow) -> Array[DataColumn] """
        ...

    def GetParentRow(self, *__args:str) -> DataRow:
        """
        GetParentRow(self: DataRow, relationName: str) -> DataRow
        GetParentRow(self: DataRow, relationName: str, version: DataRowVersion) -> DataRow
        GetParentRow(self: DataRow, relation: DataRelation) -> DataRow
        GetParentRow(self: DataRow, relation: DataRelation, version: DataRowVersion) -> DataRow
        """
        ...

    def GetParentRows(self, *__args:str) -> Array:
        """
        GetParentRows(self: DataRow, relationName: str) -> Array[DataRow]
        GetParentRows(self: DataRow, relationName: str, version: DataRowVersion) -> Array[DataRow]
        GetParentRows(self: DataRow, relation: DataRelation) -> Array[DataRow]
        GetParentRows(self: DataRow, relation: DataRelation, version: DataRowVersion) -> Array[DataRow]
        """
        ...

    def HasVersion(self, version) -> bool: # Not found arg types: {'version': 'DataRowVersion'}
        """ HasVersion(self: DataRow, version: DataRowVersion) -> bool """
        ...

    def IsNull(self, *__args:int) -> bool:
        """
        IsNull(self: DataRow, columnIndex: int) -> bool
        IsNull(self: DataRow, columnName: str) -> bool
        IsNull(self: DataRow, column: DataColumn) -> bool
        IsNull(self: DataRow, column: DataColumn, version: DataRowVersion) -> bool
        """
        ...

    def RejectChanges(self): # -> 
        """ RejectChanges(self: DataRow) """
        ...

    def SetAdded(self): # -> 
        """ SetAdded(self: DataRow) """
        ...

    def SetColumnError(self, *__args): # -> 
        """ SetColumnError(self: DataRow, columnIndex: int, error: str)SetColumnError(self: DataRow, columnName: str, error: str)SetColumnError(self: DataRow, column: DataColumn, error: str) """
        ...

    def SetModified(self): # -> 
        """ SetModified(self: DataRow) """
        ...

    def SetNull(self, *args): #cannot find CLR method
        """ SetNull(self: DataRow, column: DataColumn) """
        ...

    def SetParentRow(self, parentRow:DataRow, relation:DataRelation = ...): # -> 
        """ SetParentRow(self: DataRow, parentRow: DataRow)SetParentRow(self: DataRow, parentRow: DataRow, relation: DataRelation) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...


class DataRowAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DataRowAction, values: Add (16), Change (2), ChangeCurrentAndOriginal (64), ChangeOriginal (32), Commit (8), Delete (1), Nothing (0), Rollback (4) """
    Add: DataRowAction = ...
    Change: DataRowAction = ...
    ChangeCurrentAndOriginal: DataRowAction = ...
    ChangeOriginal: DataRowAction = ...
    Commit: DataRowAction = ...
    Delete: DataRowAction = ...
    Nothing: DataRowAction = ...
    Rollback: DataRowAction = ...
    value__ = ...


class DataRowBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class DataRowChangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DataRowChangeEventArgs(row: DataRow, action: DataRowAction) """
    @property
    def Action(self) -> DataRowAction:
        """ Get: Action(self: DataRowChangeEventArgs) -> DataRowAction """
        ...

    @property
    def Row(self) -> DataRow:
        """ Get: Row(self: DataRowChangeEventArgs) -> DataRow """
        ...


    def __new__(cls, row:DataRow, action:DataRowAction) -> Self:
        """ __new__(cls: type, row: DataRow, action: DataRowAction) """
        ...


class DataRowChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataRowChangeEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DataRowChangeEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataRowChangeEventHandler, sender: object, e: DataRowChangeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DataRowChangeEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DataRowChangeEventArgs): # -> 
        """ Invoke(self: DataRowChangeEventHandler, sender: object, e: DataRowChangeEventArgs) """
        ...


class DataRowCollection(InternalDataCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Add(self, *__args:DataRow): # -> 
        """ Add(self: DataRowCollection, row: DataRow)Add(self: DataRowCollection, *values: Array[object]) -> DataRow """
        ...

    def Clear(self): # -> 
        """ Clear(self: DataRowCollection) """
        ...

    def Contains(self, *__args:object) -> bool:
        """
        Contains(self: DataRowCollection, key: object) -> bool
        Contains(self: DataRowCollection, keys: Array[object]) -> bool
        """
        ...

    def Find(self, *__args:object) -> DataRow:
        """
        Find(self: DataRowCollection, key: object) -> DataRow
        Find(self: DataRowCollection, keys: Array[object]) -> DataRow
        """
        ...

    def IndexOf(self, row:DataRow) -> int:
        """ IndexOf(self: DataRowCollection, row: DataRow) -> int """
        ...

    def InsertAt(self, row:DataRow, pos:int): # -> 
        """ InsertAt(self: DataRowCollection, row: DataRow, pos: int) """
        ...

    def Remove(self, row:DataRow): # -> 
        """ Remove(self: DataRowCollection, row: DataRow) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: DataRowCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class DataRowComparer: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Default(self) -> DataRowComparer:
        """ Get: Default() -> DataRowComparer[DataRow] """
        ...


    __all__: list = ...


class DataRowExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Field(row:DataRow, *__args:str): # -> T
        """
        Field[T](row: DataRow, columnName: str) -> T
        Field[T](row: DataRow, column: DataColumn) -> T
        Field[T](row: DataRow, columnIndex: int) -> T
        Field[T](row: DataRow, columnIndex: int, version: DataRowVersion) -> T
        Field[T](row: DataRow, columnName: str, version: DataRowVersion) -> T
        Field[T](row: DataRow, column: DataColumn, version: DataRowVersion) -> T
        """
        ...

    @staticmethod
    def SetField(row, *__args): # -> 
        """ SetField[T](row: DataRow, columnIndex: int, value: T)SetField[T](row: DataRow, columnName: str, value: T)SetField[T](row: DataRow, column: DataColumn, value: T) """
        ...

    __all__: list = ...


class DataRowState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DataRowState, values: Added (4), Deleted (8), Detached (1), Modified (16), Unchanged (2) """
    Added: DataRowState = ...
    Deleted: DataRowState = ...
    Detached: DataRowState = ...
    Modified: DataRowState = ...
    Unchanged: DataRowState = ...
    value__ = ...


class DataRowVersion(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataRowVersion, values: Current (512), Default (1536), Original (256), Proposed (1024) """
    Current: DataRowVersion = ...
    Default: DataRowVersion = ...
    Original: DataRowVersion = ...
    Proposed: DataRowVersion = ...
    value__ = ...


class DataRowView(ICustomTypeDescriptor, IEditableObject, IDataErrorInfo, INotifyPropertyChanged): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataView(self): # -> DataView
        """ Get: DataView(self: DataRowView) -> DataView """
        ...

    @property
    def IsEdit(self) -> bool:
        """ Get: IsEdit(self: DataRowView) -> bool """
        ...

    @property
    def IsNew(self) -> bool:
        """ Get: IsNew(self: DataRowView) -> bool """
        ...

    @property
    def Row(self) -> DataRow:
        """ Get: Row(self: DataRowView) -> DataRow """
        ...

    @property
    def RowVersion(self) -> DataRowVersion:
        """ Get: RowVersion(self: DataRowView) -> DataRowVersion """
        ...


    def CreateChildView(self, *__args:DataRelation): # -> DataView
        """
        CreateChildView(self: DataRowView, relation: DataRelation, followParent: bool) -> DataView
        CreateChildView(self: DataRowView, relation: DataRelation) -> DataView
        CreateChildView(self: DataRowView, relationName: str, followParent: bool) -> DataView
        CreateChildView(self: DataRowView, relationName: str) -> DataView
        """
        ...

    def Delete(self): # -> 
        """ Delete(self: DataRowView) """
        ...

    def Equals(self, other:object) -> bool:
        """ Equals(self: DataRowView, other: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: DataRowView) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...

    PropertyChanged = ...


class DataSet(ISupportInitializeNotification, IXmlSerializable, IListSource, ISerializable, MarshalByValueComponent): # skipped bases: <type 'IDisposable'>, <type 'ISupportInitialize'>, <type 'IComponent'>, <type 'IServiceProvider'>, <type 'object'>
    """
    DataSet()
    DataSet(dataSetName: str)
    """
    @property
    def CaseSensitive(self) -> bool:
        """
        Get: CaseSensitive(self: DataSet) -> bool
        Set: CaseSensitive(self: DataSet) = value
        """
        ...

    @property
    def DataSetName(self) -> str:
        """
        Get: DataSetName(self: DataSet) -> str
        Set: DataSetName(self: DataSet) = value
        """
        ...

    @property
    def DefaultViewManager(self): # -> DataViewManager
        """ Get: DefaultViewManager(self: DataSet) -> DataViewManager """
        ...

    @property
    def EnforceConstraints(self) -> bool:
        """
        Get: EnforceConstraints(self: DataSet) -> bool
        Set: EnforceConstraints(self: DataSet) = value
        """
        ...

    @property
    def ExtendedProperties(self) -> PropertyCollection:
        """ Get: ExtendedProperties(self: DataSet) -> PropertyCollection """
        ...

    @property
    def HasErrors(self) -> bool:
        """ Get: HasErrors(self: DataSet) -> bool """
        ...

    @property
    def Locale(self) -> CultureInfo:
        """
        Get: Locale(self: DataSet) -> CultureInfo
        Set: Locale(self: DataSet) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: DataSet) -> str
        Set: Namespace(self: DataSet) = value
        """
        ...

    @property
    def Prefix(self) -> str:
        """
        Get: Prefix(self: DataSet) -> str
        Set: Prefix(self: DataSet) = value
        """
        ...

    @property
    def Relations(self) -> DataRelationCollection:
        """ Get: Relations(self: DataSet) -> DataRelationCollection """
        ...

    @property
    def RemotingFormat(self): # -> SerializationFormat
        """
        Get: RemotingFormat(self: DataSet) -> SerializationFormat
        Set: RemotingFormat(self: DataSet) = value
        """
        ...

    @property
    def SchemaSerializationMode(self): # -> SchemaSerializationMode
        """
        Get: SchemaSerializationMode(self: DataSet) -> SchemaSerializationMode
        Set: SchemaSerializationMode(self: DataSet) = value
        """
        ...

    @property
    def Tables(self): # -> DataTableCollection
        """ Get: Tables(self: DataSet) -> DataTableCollection """
        ...


    def AcceptChanges(self): # -> 
        """ AcceptChanges(self: DataSet) """
        ...

    def BeginInit(self): # -> 
        """ BeginInit(self: DataSet) """
        ...

    def Clear(self): # -> 
        """ Clear(self: DataSet) """
        ...

    def Clone(self) -> DataSet:
        """ Clone(self: DataSet) -> DataSet """
        ...

    def Copy(self) -> DataSet:
        """ Copy(self: DataSet) -> DataSet """
        ...

    def CreateDataReader(self, dataTables:Array = ...): # -> DataTableReader
        """
        CreateDataReader(self: DataSet) -> DataTableReader
        CreateDataReader(self: DataSet, *dataTables: Array[DataTable]) -> DataTableReader
        """
        ...

    def DetermineSchemaSerializationMode(self, *args): #cannot find CLR method
        """
        DetermineSchemaSerializationMode(self: DataSet, info: SerializationInfo, context: StreamingContext) -> SchemaSerializationMode
        DetermineSchemaSerializationMode(self: DataSet, reader: XmlReader) -> SchemaSerializationMode
        """
        ...

    def EndInit(self): # -> 
        """ EndInit(self: DataSet) """
        ...

    def GetChanges(self, rowStates:DataRowState = ...) -> DataSet:
        """
        GetChanges(self: DataSet) -> DataSet
        GetChanges(self: DataSet, rowStates: DataRowState) -> DataSet
        """
        ...

    @staticmethod
    def GetDataSetSchema(schemaSet:XmlSchemaSet) -> XmlSchemaComplexType:
        """ GetDataSetSchema(schemaSet: XmlSchemaSet) -> XmlSchemaComplexType """
        ...

    def GetSchemaSerializable(self, *args): #cannot find CLR method
        """ GetSchemaSerializable(self: DataSet) -> XmlSchema """
        ...

    def GetSerializationData(self, *args): #cannot find CLR method
        """ GetSerializationData(self: DataSet, info: SerializationInfo, context: StreamingContext) """
        ...

    def GetXml(self) -> str:
        """ GetXml(self: DataSet) -> str """
        ...

    def GetXmlSchema(self) -> str:
        """ GetXmlSchema(self: DataSet) -> str """
        ...

    def HasChanges(self, rowStates:DataRowState = ...) -> bool:
        """
        HasChanges(self: DataSet) -> bool
        HasChanges(self: DataSet, rowStates: DataRowState) -> bool
        """
        ...

    def InferXmlSchema(self, *__args): # -> 
        """ InferXmlSchema(self: DataSet, reader: XmlReader, nsArray: Array[str])InferXmlSchema(self: DataSet, stream: Stream, nsArray: Array[str])InferXmlSchema(self: DataSet, reader: TextReader, nsArray: Array[str])InferXmlSchema(self: DataSet, fileName: str, nsArray: Array[str]) """
        ...

    def InitializeDerivedDataSet(self, *args): #cannot find CLR method
        """ InitializeDerivedDataSet(self: DataSet) """
        ...

    def IsBinarySerialized(self, *args): #cannot find CLR method
        """ IsBinarySerialized(self: DataSet, info: SerializationInfo, context: StreamingContext) -> bool """
        ...

    def Load(self, reader, loadOption, *__args:Array): # ->  # Not found arg types: {'loadOption': 'LoadOption', 'reader': 'IDataReader'}
        """ Load(self: DataSet, reader: IDataReader, loadOption: LoadOption, errorHandler: FillErrorEventHandler, *tables: Array[DataTable])Load(self: DataSet, reader: IDataReader, loadOption: LoadOption, *tables: Array[DataTable])Load(self: DataSet, reader: IDataReader, loadOption: LoadOption, *tables: Array[str]) """
        ...

    def Merge(self, *__args:DataSet): # -> 
        """ Merge(self: DataSet, dataSet: DataSet)Merge(self: DataSet, dataSet: DataSet, preserveChanges: bool)Merge(self: DataSet, dataSet: DataSet, preserveChanges: bool, missingSchemaAction: MissingSchemaAction)Merge(self: DataSet, table: DataTable)Merge(self: DataSet, table: DataTable, preserveChanges: bool, missingSchemaAction: MissingSchemaAction)Merge(self: DataSet, rows: Array[DataRow])Merge(self: DataSet, rows: Array[DataRow], preserveChanges: bool, missingSchemaAction: MissingSchemaAction) """
        ...

    def OnPropertyChanging(self, *args): #cannot find CLR method
        """ OnPropertyChanging(self: DataSet, pcevent: PropertyChangedEventArgs) """
        ...

    def OnRemoveRelation(self, *args): #cannot find CLR method
        """ OnRemoveRelation(self: DataSet, relation: DataRelation) """
        ...

    def OnRemoveTable(self, *args): #cannot find CLR method
        """ OnRemoveTable(self: DataSet, table: DataTable) """
        ...

    def RaisePropertyChanging(self, *args): #cannot find CLR method
        """ RaisePropertyChanging(self: DataSet, name: str) """
        ...

    def ReadXmlSchema(self, *__args:XmlReader): # -> 
        """ ReadXmlSchema(self: DataSet, reader: XmlReader)ReadXmlSchema(self: DataSet, stream: Stream)ReadXmlSchema(self: DataSet, reader: TextReader)ReadXmlSchema(self: DataSet, fileName: str) """
        ...

    def ReadXmlSerializable(self, *args): #cannot find CLR method
        """ ReadXmlSerializable(self: DataSet, reader: XmlReader) """
        ...

    def RejectChanges(self): # -> 
        """ RejectChanges(self: DataSet) """
        ...

    def Reset(self): # -> 
        """ Reset(self: DataSet) """
        ...

    def ShouldSerializeRelations(self, *args): #cannot find CLR method
        """ ShouldSerializeRelations(self: DataSet) -> bool """
        ...

    def ShouldSerializeTables(self, *args): #cannot find CLR method
        """ ShouldSerializeTables(self: DataSet) -> bool """
        ...

    def WriteXmlSchema(self, *__args:Stream): # -> 
        """ WriteXmlSchema(self: DataSet, stream: Stream)WriteXmlSchema(self: DataSet, stream: Stream, multipleTargetConverter: Converter[Type, str])WriteXmlSchema(self: DataSet, fileName: str)WriteXmlSchema(self: DataSet, fileName: str, multipleTargetConverter: Converter[Type, str])WriteXmlSchema(self: DataSet, writer: TextWriter)WriteXmlSchema(self: DataSet, writer: TextWriter, multipleTargetConverter: Converter[Type, str])WriteXmlSchema(self: DataSet, writer: XmlWriter)WriteXmlSchema(self: DataSet, writer: XmlWriter, multipleTargetConverter: Converter[Type, str]) """
        ...

    def __new__(cls, dataSetName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, dataSetName: str)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext, ConstructSchema: bool)
        """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    Initialized = ...
    MergeFailed = ...


class DataSetDateTime(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataSetDateTime, values: Local (1), Unspecified (2), UnspecifiedLocal (3), Utc (4) """
    Local: DataSetDateTime = ...
    Unspecified: DataSetDateTime = ...
    UnspecifiedLocal: DataSetDateTime = ...
    Utc: DataSetDateTime = ...
    value__ = ...


class DataSetSchemaImporterExtension(SchemaImporterExtension): # skipped bases: <type 'object'>
    """ DataSetSchemaImporterExtension() """
    pass

class DataSysDescriptionAttribute(DescriptionAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DataSysDescriptionAttribute(description: str) """
    pass

class DataTable(ISupportInitializeNotification, IXmlSerializable, IListSource, ISerializable, MarshalByValueComponent): # skipped bases: <type 'IDisposable'>, <type 'ISupportInitialize'>, <type 'IComponent'>, <type 'IServiceProvider'>, <type 'object'>
    """
    DataTable()
    DataTable(tableName: str)
    DataTable(tableName: str, tableNamespace: str)
    """
    @property
    def CaseSensitive(self) -> bool:
        """
        Get: CaseSensitive(self: DataTable) -> bool
        Set: CaseSensitive(self: DataTable) = value
        """
        ...

    @property
    def ChildRelations(self) -> DataRelationCollection:
        """ Get: ChildRelations(self: DataTable) -> DataRelationCollection """
        ...

    @property
    def Columns(self) -> DataColumnCollection:
        """ Get: Columns(self: DataTable) -> DataColumnCollection """
        ...

    @property
    def Constraints(self) -> ConstraintCollection:
        """ Get: Constraints(self: DataTable) -> ConstraintCollection """
        ...

    @property
    def DataSet(self) -> DataSet:
        """ Get: DataSet(self: DataTable) -> DataSet """
        ...

    @property
    def DefaultView(self): # -> DataView
        """ Get: DefaultView(self: DataTable) -> DataView """
        ...

    @property
    def DisplayExpression(self) -> str:
        """
        Get: DisplayExpression(self: DataTable) -> str
        Set: DisplayExpression(self: DataTable) = value
        """
        ...

    @property
    def ExtendedProperties(self) -> PropertyCollection:
        """ Get: ExtendedProperties(self: DataTable) -> PropertyCollection """
        ...

    @property
    def HasErrors(self) -> bool:
        """ Get: HasErrors(self: DataTable) -> bool """
        ...

    @property
    def Locale(self) -> CultureInfo:
        """
        Get: Locale(self: DataTable) -> CultureInfo
        Set: Locale(self: DataTable) = value
        """
        ...

    @property
    def MinimumCapacity(self) -> int:
        """
        Get: MinimumCapacity(self: DataTable) -> int
        Set: MinimumCapacity(self: DataTable) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: DataTable) -> str
        Set: Namespace(self: DataTable) = value
        """
        ...

    @property
    def ParentRelations(self) -> DataRelationCollection:
        """ Get: ParentRelations(self: DataTable) -> DataRelationCollection """
        ...

    @property
    def Prefix(self) -> str:
        """
        Get: Prefix(self: DataTable) -> str
        Set: Prefix(self: DataTable) = value
        """
        ...

    @property
    def PrimaryKey(self) -> Array:
        """
        Get: PrimaryKey(self: DataTable) -> Array[DataColumn]
        Set: PrimaryKey(self: DataTable) = value
        """
        ...

    @property
    def RemotingFormat(self): # -> SerializationFormat
        """
        Get: RemotingFormat(self: DataTable) -> SerializationFormat
        Set: RemotingFormat(self: DataTable) = value
        """
        ...

    @property
    def Rows(self) -> DataRowCollection:
        """ Get: Rows(self: DataTable) -> DataRowCollection """
        ...

    @property
    def TableName(self) -> str:
        """
        Get: TableName(self: DataTable) -> str
        Set: TableName(self: DataTable) = value
        """
        ...


    def AcceptChanges(self): # -> 
        """ AcceptChanges(self: DataTable) """
        ...

    def BeginInit(self): # -> 
        """ BeginInit(self: DataTable) """
        ...

    def BeginLoadData(self): # -> 
        """ BeginLoadData(self: DataTable) """
        ...

    def Clear(self): # -> 
        """ Clear(self: DataTable) """
        ...

    def Clone(self) -> DataTable:
        """ Clone(self: DataTable) -> DataTable """
        ...

    def Compute(self, expression:str, filter:str) -> object:
        """ Compute(self: DataTable, expression: str, filter: str) -> object """
        ...

    def Copy(self) -> DataTable:
        """ Copy(self: DataTable) -> DataTable """
        ...

    def CreateDataReader(self): # -> DataTableReader
        """ CreateDataReader(self: DataTable) -> DataTableReader """
        ...

    def CreateInstance(self, *args): #cannot find CLR method
        """ CreateInstance(self: DataTable) -> DataTable """
        ...

    def EndInit(self): # -> 
        """ EndInit(self: DataTable) """
        ...

    def EndLoadData(self): # -> 
        """ EndLoadData(self: DataTable) """
        ...

    def GetChanges(self, rowStates:DataRowState = ...) -> DataTable:
        """
        GetChanges(self: DataTable) -> DataTable
        GetChanges(self: DataTable, rowStates: DataRowState) -> DataTable
        """
        ...

    @staticmethod
    def GetDataTableSchema(schemaSet:XmlSchemaSet) -> XmlSchemaComplexType:
        """ GetDataTableSchema(schemaSet: XmlSchemaSet) -> XmlSchemaComplexType """
        ...

    def GetErrors(self) -> Array:
        """ GetErrors(self: DataTable) -> Array[DataRow] """
        ...

    def GetRowType(self, *args): #cannot find CLR method
        """ GetRowType(self: DataTable) -> Type """
        ...

    def ImportRow(self, row:DataRow): # -> 
        """ ImportRow(self: DataTable, row: DataRow) """
        ...

    def Load(self, reader, loadOption = ..., errorHandler = ...): # ->  # Not found arg types: {'errorHandler': 'FillErrorEventHandler', 'loadOption': 'LoadOption', 'reader': 'IDataReader'}
        """ Load(self: DataTable, reader: IDataReader)Load(self: DataTable, reader: IDataReader, loadOption: LoadOption)Load(self: DataTable, reader: IDataReader, loadOption: LoadOption, errorHandler: FillErrorEventHandler) """
        ...

    def LoadDataRow(self, values:Array, *__args:bool) -> DataRow:
        """
        LoadDataRow(self: DataTable, values: Array[object], fAcceptChanges: bool) -> DataRow
        LoadDataRow(self: DataTable, values: Array[object], loadOption: LoadOption) -> DataRow
        """
        ...

    def Merge(self, table:DataTable, preserveChanges:bool = ..., missingSchemaAction = ...): # ->  # Not found arg types: {'missingSchemaAction': 'MissingSchemaAction'}
        """ Merge(self: DataTable, table: DataTable)Merge(self: DataTable, table: DataTable, preserveChanges: bool)Merge(self: DataTable, table: DataTable, preserveChanges: bool, missingSchemaAction: MissingSchemaAction) """
        ...

    def NewRow(self) -> DataRow:
        """ NewRow(self: DataTable) -> DataRow """
        ...

    def NewRowArray(self, *args): #cannot find CLR method
        """ NewRowArray(self: DataTable, size: int) -> Array[DataRow] """
        ...

    def NewRowFromBuilder(self, *args): #cannot find CLR method
        """ NewRowFromBuilder(self: DataTable, builder: DataRowBuilder) -> DataRow """
        ...

    def OnColumnChanged(self, *args): #cannot find CLR method
        """ OnColumnChanged(self: DataTable, e: DataColumnChangeEventArgs) """
        ...

    def OnColumnChanging(self, *args): #cannot find CLR method
        """ OnColumnChanging(self: DataTable, e: DataColumnChangeEventArgs) """
        ...

    def OnPropertyChanging(self, *args): #cannot find CLR method
        """ OnPropertyChanging(self: DataTable, pcevent: PropertyChangedEventArgs) """
        ...

    def OnRemoveColumn(self, *args): #cannot find CLR method
        """ OnRemoveColumn(self: DataTable, column: DataColumn) """
        ...

    def OnRowChanged(self, *args): #cannot find CLR method
        """ OnRowChanged(self: DataTable, e: DataRowChangeEventArgs) """
        ...

    def OnRowChanging(self, *args): #cannot find CLR method
        """ OnRowChanging(self: DataTable, e: DataRowChangeEventArgs) """
        ...

    def OnRowDeleted(self, *args): #cannot find CLR method
        """ OnRowDeleted(self: DataTable, e: DataRowChangeEventArgs) """
        ...

    def OnRowDeleting(self, *args): #cannot find CLR method
        """ OnRowDeleting(self: DataTable, e: DataRowChangeEventArgs) """
        ...

    def OnTableCleared(self, *args): #cannot find CLR method
        """ OnTableCleared(self: DataTable, e: DataTableClearEventArgs) """
        ...

    def OnTableClearing(self, *args): #cannot find CLR method
        """ OnTableClearing(self: DataTable, e: DataTableClearEventArgs) """
        ...

    def OnTableNewRow(self, *args): #cannot find CLR method
        """ OnTableNewRow(self: DataTable, e: DataTableNewRowEventArgs) """
        ...

    def ReadXmlSchema(self, *__args:Stream): # -> 
        """ ReadXmlSchema(self: DataTable, stream: Stream)ReadXmlSchema(self: DataTable, reader: TextReader)ReadXmlSchema(self: DataTable, fileName: str)ReadXmlSchema(self: DataTable, reader: XmlReader) """
        ...

    def ReadXmlSerializable(self, *args): #cannot find CLR method
        """ ReadXmlSerializable(self: DataTable, reader: XmlReader) """
        ...

    def RejectChanges(self): # -> 
        """ RejectChanges(self: DataTable) """
        ...

    def Reset(self): # -> 
        """ Reset(self: DataTable) """
        ...

    def Select(self, filterExpression:str = ..., sort:str = ..., recordStates = ...) -> Array: # Not found arg types: {'recordStates': 'DataViewRowState'}
        """
        Select(self: DataTable) -> Array[DataRow]
        Select(self: DataTable, filterExpression: str) -> Array[DataRow]
        Select(self: DataTable, filterExpression: str, sort: str) -> Array[DataRow]
        Select(self: DataTable, filterExpression: str, sort: str, recordStates: DataViewRowState) -> Array[DataRow]
        """
        ...

    def WriteXmlSchema(self, *__args:Stream): # -> 
        """ WriteXmlSchema(self: DataTable, stream: Stream)WriteXmlSchema(self: DataTable, stream: Stream, writeHierarchy: bool)WriteXmlSchema(self: DataTable, writer: TextWriter)WriteXmlSchema(self: DataTable, writer: TextWriter, writeHierarchy: bool)WriteXmlSchema(self: DataTable, writer: XmlWriter)WriteXmlSchema(self: DataTable, writer: XmlWriter, writeHierarchy: bool)WriteXmlSchema(self: DataTable, fileName: str)WriteXmlSchema(self: DataTable, fileName: str, writeHierarchy: bool) """
        ...

    def __new__(cls, tableName:str = ..., tableNamespace:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, tableName: str)
        __new__(cls: type, tableName: str, tableNamespace: str)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    ColumnChanged = ...
    ColumnChanging = ...
    fInitInProgress = ...
    Initialized = ...
    RowChanged = ...
    RowChanging = ...
    RowDeleted = ...
    RowDeleting = ...
    TableCleared = ...
    TableClearing = ...
    TableNewRow = ...


class DataTableClearEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DataTableClearEventArgs(dataTable: DataTable) """
    @property
    def Table(self) -> DataTable:
        """ Get: Table(self: DataTableClearEventArgs) -> DataTable """
        ...

    @property
    def TableName(self) -> str:
        """ Get: TableName(self: DataTableClearEventArgs) -> str """
        ...

    @property
    def TableNamespace(self) -> str:
        """ Get: TableNamespace(self: DataTableClearEventArgs) -> str """
        ...


    def __new__(cls, dataTable:DataTable) -> Self:
        """ __new__(cls: type, dataTable: DataTable) """
        ...


class DataTableClearEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataTableClearEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DataTableClearEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataTableClearEventHandler, sender: object, e: DataTableClearEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DataTableClearEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DataTableClearEventArgs): # -> 
        """ Invoke(self: DataTableClearEventHandler, sender: object, e: DataTableClearEventArgs) """
        ...


class DataTableCollection(InternalDataCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Add(self, *__args:DataTable): # -> 
        """
        Add(self: DataTableCollection, table: DataTable)Add(self: DataTableCollection, name: str) -> DataTable
        Add(self: DataTableCollection, name: str, tableNamespace: str) -> DataTable
        Add(self: DataTableCollection) -> DataTable
        """
        ...

    def AddRange(self, tables:Array): # -> 
        """ AddRange(self: DataTableCollection, tables: Array[DataTable]) """
        ...

    def CanRemove(self, table:DataTable) -> bool:
        """ CanRemove(self: DataTableCollection, table: DataTable) -> bool """
        ...

    def Clear(self): # -> 
        """ Clear(self: DataTableCollection) """
        ...

    def Contains(self, name:str, tableNamespace:str = ...) -> bool:
        """
        Contains(self: DataTableCollection, name: str) -> bool
        Contains(self: DataTableCollection, name: str, tableNamespace: str) -> bool
        """
        ...

    def IndexOf(self, *__args:DataTable) -> int:
        """
        IndexOf(self: DataTableCollection, table: DataTable) -> int
        IndexOf(self: DataTableCollection, tableName: str) -> int
        IndexOf(self: DataTableCollection, tableName: str, tableNamespace: str) -> int
        """
        ...

    def Remove(self, *__args:DataTable): # -> 
        """ Remove(self: DataTableCollection, name: str, tableNamespace: str)Remove(self: DataTableCollection, table: DataTable)Remove(self: DataTableCollection, name: str) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: DataTableCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    CollectionChanged = ...
    CollectionChanging = ...


class DataTableExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AsDataView(*__args:DataTable): # -> DataView
        """
        AsDataView(table: DataTable) -> DataView
        AsDataView[T](source: EnumerableRowCollection[T]) -> DataView
        """
        ...

    @staticmethod
    def AsEnumerable(source:DataTable): # -> EnumerableRowCollection
        """ AsEnumerable(source: DataTable) -> EnumerableRowCollection[DataRow] """
        ...

    @staticmethod
    def CopyToDataTable(source:IEnumerable, table:DataTable = ..., options = ..., errorHandler = ...): # ->  # Not found arg types: {'options': 'LoadOption', 'errorHandler': 'FillErrorEventHandler'}
        """
        CopyToDataTable[T](source: IEnumerable[T]) -> DataTable
        CopyToDataTable[T](source: IEnumerable[T], table: DataTable, options: LoadOption)CopyToDataTable[T](source: IEnumerable[T], table: DataTable, options: LoadOption, errorHandler: FillErrorEventHandler)
        """
        ...

    __all__: list = ...


class DataTableNewRowEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DataTableNewRowEventArgs(dataRow: DataRow) """
    @property
    def Row(self) -> DataRow:
        """ Get: Row(self: DataTableNewRowEventArgs) -> DataRow """
        ...


    def __new__(cls, dataRow:DataRow) -> Self:
        """ __new__(cls: type, dataRow: DataRow) """
        ...


class DataTableNewRowEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataTableNewRowEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DataTableNewRowEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataTableNewRowEventHandler, sender: object, e: DataTableNewRowEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DataTableNewRowEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DataTableNewRowEventArgs): # -> 
        """ Invoke(self: DataTableNewRowEventHandler, sender: object, e: DataTableNewRowEventArgs) """
        ...


class IDataRecord: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def FieldCount(self) -> int:
        """ Get: FieldCount(self: IDataRecord) -> int """
        ...


    def GetBoolean(self, i:int) -> bool:
        """ GetBoolean(self: IDataRecord, i: int) -> bool """
        ...

    def GetByte(self, i:int) -> Byte:
        """ GetByte(self: IDataRecord, i: int) -> Byte """
        ...

    def GetBytes(self, i:int, fieldOffset:Int64, buffer:Array, bufferoffset:int, length:int) -> Int64:
        """ GetBytes(self: IDataRecord, i: int, fieldOffset: Int64, buffer: Array[Byte], bufferoffset: int, length: int) -> Int64 """
        ...

    def GetChar(self, i:int) -> Char:
        """ GetChar(self: IDataRecord, i: int) -> Char """
        ...

    def GetChars(self, i:int, fieldoffset:Int64, buffer:Array, bufferoffset:int, length:int) -> Int64:
        """ GetChars(self: IDataRecord, i: int, fieldoffset: Int64, buffer: Array[Char], bufferoffset: int, length: int) -> Int64 """
        ...

    def GetData(self, i:int): # -> IDataReader
        """ GetData(self: IDataRecord, i: int) -> IDataReader """
        ...

    def GetDataTypeName(self, i:int) -> str:
        """ GetDataTypeName(self: IDataRecord, i: int) -> str """
        ...

    def GetDateTime(self, i:int) -> DateTime:
        """ GetDateTime(self: IDataRecord, i: int) -> DateTime """
        ...

    def GetDecimal(self, i:int) -> Decimal:
        """ GetDecimal(self: IDataRecord, i: int) -> Decimal """
        ...

    def GetDouble(self, i:int) -> float:
        """ GetDouble(self: IDataRecord, i: int) -> float """
        ...

    def GetFieldType(self, i:int) -> Type:
        """ GetFieldType(self: IDataRecord, i: int) -> Type """
        ...

    def GetFloat(self, i:int) -> Single:
        """ GetFloat(self: IDataRecord, i: int) -> Single """
        ...

    def GetGuid(self, i:int) -> Guid:
        """ GetGuid(self: IDataRecord, i: int) -> Guid """
        ...

    def GetInt16(self, i:int) -> Int16:
        """ GetInt16(self: IDataRecord, i: int) -> Int16 """
        ...

    def GetInt32(self, i:int) -> int:
        """ GetInt32(self: IDataRecord, i: int) -> int """
        ...

    def GetInt64(self, i:int) -> Int64:
        """ GetInt64(self: IDataRecord, i: int) -> Int64 """
        ...

    def GetName(self, i:int) -> str:
        """ GetName(self: IDataRecord, i: int) -> str """
        ...

    def GetOrdinal(self, name:str) -> int:
        """ GetOrdinal(self: IDataRecord, name: str) -> int """
        ...

    def GetString(self, i:int) -> str:
        """ GetString(self: IDataRecord, i: int) -> str """
        ...

    def GetValue(self, i:int) -> object:
        """ GetValue(self: IDataRecord, i: int) -> object """
        ...

    def GetValues(self, values:Array) -> int:
        """ GetValues(self: IDataRecord, values: Array[object]) -> int """
        ...

    def IsDBNull(self, i:int) -> bool:
        """ IsDBNull(self: IDataRecord, i: int) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class IDataReader(IDataRecord, IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Depth(self) -> int:
        """ Get: Depth(self: IDataReader) -> int """
        ...

    @property
    def IsClosed(self) -> bool:
        """ Get: IsClosed(self: IDataReader) -> bool """
        ...

    @property
    def RecordsAffected(self) -> int:
        """ Get: RecordsAffected(self: IDataReader) -> int """
        ...


    def Close(self): # -> 
        """ Close(self: IDataReader) """
        ...

    def GetSchemaTable(self) -> DataTable:
        """ GetSchemaTable(self: IDataReader) -> DataTable """
        ...

    def NextResult(self) -> bool:
        """ NextResult(self: IDataReader) -> bool """
        ...

    def Read(self) -> bool:
        """ Read(self: IDataReader) -> bool """
        ...


class DataTableReader(DbDataReader): # skipped bases: <type 'IDisposable'>, <type 'IDataReader'>, <type 'IDataRecord'>, <type 'IEnumerable'>, <type 'object'>
    """
    DataTableReader(dataTable: DataTable)
    DataTableReader(dataTables: Array[DataTable])
    """
    def __new__(cls, *__args:DataTable) -> Self:
        """
        __new__(cls: type, dataTable: DataTable)
        __new__(cls: type, dataTables: Array[DataTable])
        """
        ...


class DataView(IBindingListView, ITypedList, ISupportInitializeNotification, MarshalByValueComponent): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IList'>, <type 'IEnumerable'>, <type 'IBindingList'>, <type 'ISupportInitialize'>, <type 'IServiceProvider'>, <type 'ICollection'>, <type 'object'>
    """
    DataView()
    DataView(table: DataTable)
    DataView(table: DataTable, RowFilter: str, Sort: str, RowState: DataViewRowState)
    """
    @property
    def AllowDelete(self) -> bool:
        """
        Get: AllowDelete(self: DataView) -> bool
        Set: AllowDelete(self: DataView) = value
        """
        ...

    @property
    def AllowEdit(self) -> bool:
        """
        Get: AllowEdit(self: DataView) -> bool
        Set: AllowEdit(self: DataView) = value
        """
        ...

    @property
    def AllowNew(self) -> bool:
        """
        Get: AllowNew(self: DataView) -> bool
        Set: AllowNew(self: DataView) = value
        """
        ...

    @property
    def ApplyDefaultSort(self) -> bool:
        """
        Get: ApplyDefaultSort(self: DataView) -> bool
        Set: ApplyDefaultSort(self: DataView) = value
        """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: DataView) -> int """
        ...

    @property
    def DataViewManager(self): # -> DataViewManager
        """ Get: DataViewManager(self: DataView) -> DataViewManager """
        ...

    @property
    def IsOpen(self):
        ...

    @property
    def RowFilter(self) -> str:
        """
        Get: RowFilter(self: DataView) -> str
        Set: RowFilter(self: DataView) = value
        """
        ...

    @property
    def RowStateFilter(self): # -> DataViewRowState
        """
        Get: RowStateFilter(self: DataView) -> DataViewRowState
        Set: RowStateFilter(self: DataView) = value
        """
        ...

    @property
    def Sort(self) -> str:
        """
        Get: Sort(self: DataView) -> str
        Set: Sort(self: DataView) = value
        """
        ...

    @property
    def Table(self) -> DataTable:
        """
        Get: Table(self: DataView) -> DataTable
        Set: Table(self: DataView) = value
        """
        ...


    def AddNew(self) -> DataRowView:
        """ AddNew(self: DataView) -> DataRowView """
        ...

    def BeginInit(self): # -> 
        """ BeginInit(self: DataView) """
        ...

    def Close(self, *args): #cannot find CLR method
        """ Close(self: DataView) """
        ...

    def ColumnCollectionChanged(self, *args): #cannot find CLR method
        """ ColumnCollectionChanged(self: DataView, sender: object, e: CollectionChangeEventArgs) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DataView, array: Array, index: int) """
        ...

    def Delete(self, index:int): # -> 
        """ Delete(self: DataView, index: int) """
        ...

    def EndInit(self): # -> 
        """ EndInit(self: DataView) """
        ...

    def Equals(self, *__args:DataView) -> bool:
        """ Equals(self: DataView, view: DataView) -> bool """
        ...

    def Find(self, key:object) -> int:
        """
        Find(self: DataView, key: object) -> int
        Find(self: DataView, key: Array[object]) -> int
        """
        ...

    def FindRows(self, key:Array) -> Array:
        """
        FindRows(self: DataView, key: Array[object]) -> Array[DataRowView]
        FindRows(self: DataView, key: object) -> Array[DataRowView]
        """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DataView) -> IEnumerator """
        ...

    def IndexListChanged(self, *args): #cannot find CLR method
        """ IndexListChanged(self: DataView, sender: object, e: ListChangedEventArgs) """
        ...

    def OnListChanged(self, *args): #cannot find CLR method
        """ OnListChanged(self: DataView, e: ListChangedEventArgs) """
        ...

    def Open(self, *args): #cannot find CLR method
        """ Open(self: DataView) """
        ...

    def Reset(self, *args): #cannot find CLR method
        """ Reset(self: DataView) """
        ...

    def ToTable(self, *__args:str) -> DataTable:
        """
        ToTable(self: DataView, distinct: bool, *columnNames: Array[str]) -> DataTable
        ToTable(self: DataView) -> DataTable
        ToTable(self: DataView, tableName: str) -> DataTable
        ToTable(self: DataView, tableName: str, distinct: bool, *columnNames: Array[str]) -> DataTable
        """
        ...

    def UpdateIndex(self, *args): #cannot find CLR method
        """ UpdateIndex(self: DataView)UpdateIndex(self: DataView, force: bool) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, table:DataTable = ..., RowFilter:str = ..., Sort:str = ..., RowState = ...) -> Self: # Not found arg types: {'RowState': 'DataViewRowState'}
        """
        __new__(cls: type)
        __new__(cls: type, table: DataTable)
        __new__(cls: type, table: DataTable, RowFilter: str, Sort: str, RowState: DataViewRowState)
        """
        ...

    Initialized = ...
    ListChanged = ...


class DataViewManager(ITypedList, IBindingList, MarshalByValueComponent): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IList'>, <type 'IEnumerable'>, <type 'IServiceProvider'>, <type 'ICollection'>, <type 'object'>
    """
    DataViewManager()
    DataViewManager(dataSet: DataSet)
    """
    @property
    def DataSet(self) -> DataSet:
        """
        Get: DataSet(self: DataViewManager) -> DataSet
        Set: DataSet(self: DataViewManager) = value
        """
        ...

    @property
    def DataViewSettingCollectionString(self) -> str:
        """
        Get: DataViewSettingCollectionString(self: DataViewManager) -> str
        Set: DataViewSettingCollectionString(self: DataViewManager) = value
        """
        ...

    @property
    def DataViewSettings(self): # -> DataViewSettingCollection
        """ Get: DataViewSettings(self: DataViewManager) -> DataViewSettingCollection """
        ...


    def CreateDataView(self, table:DataTable) -> DataView:
        """ CreateDataView(self: DataViewManager, table: DataTable) -> DataView """
        ...

    def OnListChanged(self, *args): #cannot find CLR method
        """ OnListChanged(self: DataViewManager, e: ListChangedEventArgs) """
        ...

    def RelationCollectionChanged(self, *args): #cannot find CLR method
        """ RelationCollectionChanged(self: DataViewManager, sender: object, e: CollectionChangeEventArgs) """
        ...

    def TableCollectionChanged(self, *args): #cannot find CLR method
        """ TableCollectionChanged(self: DataViewManager, sender: object, e: CollectionChangeEventArgs) """
        ...

    def __new__(cls, dataSet:DataSet = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, dataSet: DataSet)
        """
        ...

    ListChanged = ...


class DataViewRowState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DataViewRowState, values: Added (4), CurrentRows (22), Deleted (8), ModifiedCurrent (16), ModifiedOriginal (32), None (0), OriginalRows (42), Unchanged (2) """
    Added: DataViewRowState = ...
    CurrentRows: DataViewRowState = ...
    Deleted: DataViewRowState = ...
    ModifiedCurrent: DataViewRowState = ...
    ModifiedOriginal: DataViewRowState = ...
    OriginalRows: DataViewRowState = ...
    Unchanged: DataViewRowState = ...
    value__ = ...


class DataViewSetting: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ApplyDefaultSort(self) -> bool:
        """
        Get: ApplyDefaultSort(self: DataViewSetting) -> bool
        Set: ApplyDefaultSort(self: DataViewSetting) = value
        """
        ...

    @property
    def DataViewManager(self) -> DataViewManager:
        """ Get: DataViewManager(self: DataViewSetting) -> DataViewManager """
        ...

    @property
    def RowFilter(self) -> str:
        """
        Get: RowFilter(self: DataViewSetting) -> str
        Set: RowFilter(self: DataViewSetting) = value
        """
        ...

    @property
    def RowStateFilter(self) -> DataViewRowState:
        """
        Get: RowStateFilter(self: DataViewSetting) -> DataViewRowState
        Set: RowStateFilter(self: DataViewSetting) = value
        """
        ...

    @property
    def Sort(self) -> str:
        """
        Get: Sort(self: DataViewSetting) -> str
        Set: Sort(self: DataViewSetting) = value
        """
        ...

    @property
    def Table(self) -> DataTable:
        """ Get: Table(self: DataViewSetting) -> DataTable """
        ...



class DataViewSettingCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: DataViewSettingCollection) -> bool """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: DataViewSettingCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...


class DBConcurrencyException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DBConcurrencyException()
    DBConcurrencyException(message: str)
    DBConcurrencyException(message: str, inner: Exception)
    DBConcurrencyException(message: str, inner: Exception, dataRows: Array[DataRow])
    """
    @property
    def Row(self) -> DataRow:
        """
        Get: Row(self: DBConcurrencyException) -> DataRow
        Set: Row(self: DBConcurrencyException) = value
        """
        ...

    @property
    def RowCount(self) -> int:
        """ Get: RowCount(self: DBConcurrencyException) -> int """
        ...


    def CopyToRows(self, array:Array, arrayIndex:int = ...): # -> 
        """ CopyToRows(self: DBConcurrencyException, array: Array[DataRow])CopyToRows(self: DBConcurrencyException, array: Array[DataRow], arrayIndex: int) """
        ...

    SerializeObjectState = ...


class DbType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DbType, values: AnsiString (0), AnsiStringFixedLength (22), Binary (1), Boolean (3), Byte (2), Currency (4), Date (5), DateTime (6), DateTime2 (26), DateTimeOffset (27), Decimal (7), Double (8), Guid (9), Int16 (10), Int32 (11), Int64 (12), Object (13), SByte (14), Single (15), String (16), StringFixedLength (23), Time (17), UInt16 (18), UInt32 (19), UInt64 (20), VarNumeric (21), Xml (25) """
    AnsiString: DbType = ...
    AnsiStringFixedLength: DbType = ...
    Binary: DbType = ...
    Boolean: DbType = ...
    Byte: DbType = ...
    Currency: DbType = ...
    Date: DbType = ...
    DateTime: DbType = ...
    DateTime2: DbType = ...
    DateTimeOffset: DbType = ...
    Decimal: DbType = ...
    Double: DbType = ...
    Guid: DbType = ...
    Int16: DbType = ...
    Int32: DbType = ...
    Int64: DbType = ...
    Object: DbType = ...
    SByte: DbType = ...
    Single: DbType = ...
    String: DbType = ...
    StringFixedLength: DbType = ...
    Time: DbType = ...
    UInt16: DbType = ...
    UInt32: DbType = ...
    UInt64: DbType = ...
    value__ = ...
    VarNumeric: DbType = ...
    Xml: DbType = ...


class DeletedRowInaccessibleException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DeletedRowInaccessibleException()
    DeletedRowInaccessibleException(s: str)
    DeletedRowInaccessibleException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class DuplicateNameException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DuplicateNameException()
    DuplicateNameException(s: str)
    DuplicateNameException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class EntityException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EntityException()
    EntityException(message: str)
    EntityException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class EntityCommandCompilationException(EntityException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EntityCommandCompilationException()
    EntityCommandCompilationException(message: str)
    EntityCommandCompilationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class EntityCommandExecutionException(EntityException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EntityCommandExecutionException()
    EntityCommandExecutionException(message: str)
    EntityCommandExecutionException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class EntityKey(IEquatable): # skipped bases: <type 'object'>
    """
    EntityKey()
    EntityKey(qualifiedEntitySetName: str, entityKeyValues: IEnumerable[KeyValuePair[str, object]])
    EntityKey(qualifiedEntitySetName: str, entityKeyValues: IEnumerable[EntityKeyMember])
    EntityKey(qualifiedEntitySetName: str, keyName: str, keyValue: object)
    """
    @property
    def EntityContainerName(self) -> str:
        """
        Get: EntityContainerName(self: EntityKey) -> str
        Set: EntityContainerName(self: EntityKey) = value
        """
        ...

    @property
    def EntityKeyValues(self) -> Array:
        """
        Get: EntityKeyValues(self: EntityKey) -> Array[EntityKeyMember]
        Set: EntityKeyValues(self: EntityKey) = value
        """
        ...

    @property
    def EntitySetName(self) -> str:
        """
        Get: EntitySetName(self: EntityKey) -> str
        Set: EntitySetName(self: EntityKey) = value
        """
        ...

    @property
    def IsTemporary(self) -> bool:
        """ Get: IsTemporary(self: EntityKey) -> bool """
        ...


    def GetEntitySet(self, metadataWorkspace:MetadataWorkspace) -> EntitySet:
        """ GetEntitySet(self: EntityKey, metadataWorkspace: MetadataWorkspace) -> EntitySet """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: EntityKey) -> int """
        ...

    def OnDeserialized(self, context:StreamingContext): # -> 
        """ OnDeserialized(self: EntityKey, context: StreamingContext) """
        ...

    def OnDeserializing(self, context:StreamingContext): # -> 
        """ OnDeserializing(self: EntityKey, context: StreamingContext) """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    EntityNotValidKey: EntityKey = ...
    NoEntitySetKey: EntityKey = ...


class EntityKeyMember: # skipped bases: <type 'object'>, <type 'object'>
    """
    EntityKeyMember()
    EntityKeyMember(keyName: str, keyValue: object)
    """
    @property
    def Key(self) -> str:
        """
        Get: Key(self: EntityKeyMember) -> str
        Set: Key(self: EntityKeyMember) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: EntityKeyMember) -> object
        Set: Value(self: EntityKeyMember) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: EntityKeyMember) -> str """
        ...


class EntitySqlException(EntityException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EntitySqlException()
    EntitySqlException(message: str)
    EntitySqlException(message: str, innerException: Exception)
    """
    @property
    def Column(self) -> int:
        """ Get: Column(self: EntitySqlException) -> int """
        ...

    @property
    def ErrorContext(self) -> str:
        """ Get: ErrorContext(self: EntitySqlException) -> str """
        ...

    @property
    def ErrorDescription(self) -> str:
        """ Get: ErrorDescription(self: EntitySqlException) -> str """
        ...

    @property
    def Line(self) -> int:
        """ Get: Line(self: EntitySqlException) -> int """
        ...


    SerializeObjectState = ...


class EntityState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EntityState, values: Added (4), Deleted (8), Detached (1), Modified (16), Unchanged (2) """
    Added: EntityState = ...
    Deleted: EntityState = ...
    Detached: EntityState = ...
    Modified: EntityState = ...
    Unchanged: EntityState = ...
    value__ = ...


class EnumerableRowCollection: # skipped bases: <type 'object'>
    """ no doc """
    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class EnumerableRowCollectionExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Cast(source:EnumerableRowCollection) -> EnumerableRowCollection:
        """ Cast[TResult](source: EnumerableRowCollection) -> EnumerableRowCollection[TResult] """
        ...

    @staticmethod
    def OrderBy(source:EnumerableRowCollection, keySelector, comparer:IComparer = ...): # -> OrderedEnumerableRowCollection # Not found arg types: {'keySelector': 'Func'}
        """
        OrderBy[(TRow, TKey)](source: EnumerableRowCollection[TRow], keySelector: Func[TRow, TKey]) -> OrderedEnumerableRowCollection[TRow]
        OrderBy[(TRow, TKey)](source: EnumerableRowCollection[TRow], keySelector: Func[TRow, TKey], comparer: IComparer[TKey]) -> OrderedEnumerableRowCollection[TRow]
        """
        ...

    @staticmethod
    def OrderByDescending(source:EnumerableRowCollection, keySelector, comparer:IComparer = ...): # -> OrderedEnumerableRowCollection # Not found arg types: {'keySelector': 'Func'}
        """
        OrderByDescending[(TRow, TKey)](source: EnumerableRowCollection[TRow], keySelector: Func[TRow, TKey]) -> OrderedEnumerableRowCollection[TRow]
        OrderByDescending[(TRow, TKey)](source: EnumerableRowCollection[TRow], keySelector: Func[TRow, TKey], comparer: IComparer[TKey]) -> OrderedEnumerableRowCollection[TRow]
        """
        ...

    @staticmethod
    def Select(source:EnumerableRowCollection, selector) -> EnumerableRowCollection: # Not found arg types: {'selector': 'Func'}
        """ Select[(TRow, S)](source: EnumerableRowCollection[TRow], selector: Func[TRow, S]) -> EnumerableRowCollection[S] """
        ...

    @staticmethod
    def ThenBy(source, keySelector, comparer:IComparer = ...): # -> OrderedEnumerableRowCollection # Not found arg types: {'keySelector': 'Func', 'source': 'OrderedEnumerableRowCollection'}
        """
        ThenBy[(TRow, TKey)](source: OrderedEnumerableRowCollection[TRow], keySelector: Func[TRow, TKey]) -> OrderedEnumerableRowCollection[TRow]
        ThenBy[(TRow, TKey)](source: OrderedEnumerableRowCollection[TRow], keySelector: Func[TRow, TKey], comparer: IComparer[TKey]) -> OrderedEnumerableRowCollection[TRow]
        """
        ...

    @staticmethod
    def ThenByDescending(source, keySelector, comparer:IComparer = ...): # -> OrderedEnumerableRowCollection # Not found arg types: {'keySelector': 'Func', 'source': 'OrderedEnumerableRowCollection'}
        """
        ThenByDescending[(TRow, TKey)](source: OrderedEnumerableRowCollection[TRow], keySelector: Func[TRow, TKey]) -> OrderedEnumerableRowCollection[TRow]
        ThenByDescending[(TRow, TKey)](source: OrderedEnumerableRowCollection[TRow], keySelector: Func[TRow, TKey], comparer: IComparer[TKey]) -> OrderedEnumerableRowCollection[TRow]
        """
        ...

    @staticmethod
    def Where(source:EnumerableRowCollection, predicate) -> EnumerableRowCollection: # Not found arg types: {'predicate': 'Func'}
        """ Where[TRow](source: EnumerableRowCollection[TRow], predicate: Func[TRow, bool]) -> EnumerableRowCollection[TRow] """
        ...

    __all__: list = ...


class InvalidExpressionException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidExpressionException()
    InvalidExpressionException(s: str)
    InvalidExpressionException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class EvaluateException(InvalidExpressionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EvaluateException()
    EvaluateException(s: str)
    EvaluateException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class FillErrorEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ FillErrorEventArgs(dataTable: DataTable, values: Array[object]) """
    @property
    def Continue(self) -> bool:
        """
        Get: Continue(self: FillErrorEventArgs) -> bool
        Set: Continue(self: FillErrorEventArgs) = value
        """
        ...

    @property
    def DataTable(self) -> DataTable:
        """ Get: DataTable(self: FillErrorEventArgs) -> DataTable """
        ...

    @property
    def Errors(self) -> Exception:
        """
        Get: Errors(self: FillErrorEventArgs) -> Exception
        Set: Errors(self: FillErrorEventArgs) = value
        """
        ...

    @property
    def Values(self) -> Array:
        """ Get: Values(self: FillErrorEventArgs) -> Array[object] """
        ...


    def __new__(cls, dataTable:DataTable, values:Array) -> Self:
        """ __new__(cls: type, dataTable: DataTable, values: Array[object]) """
        ...


class FillErrorEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FillErrorEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:FillErrorEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: FillErrorEventHandler, sender: object, e: FillErrorEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: FillErrorEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:FillErrorEventArgs): # -> 
        """ Invoke(self: FillErrorEventHandler, sender: object, e: FillErrorEventArgs) """
        ...


class ForeignKeyConstraint(Constraint): # skipped bases: <type 'object'>
    """
    ForeignKeyConstraint(parentColumn: DataColumn, childColumn: DataColumn)
    ForeignKeyConstraint(constraintName: str, parentColumn: DataColumn, childColumn: DataColumn)
    ForeignKeyConstraint(parentColumns: Array[DataColumn], childColumns: Array[DataColumn])
    ForeignKeyConstraint(constraintName: str, parentColumns: Array[DataColumn], childColumns: Array[DataColumn])
    ForeignKeyConstraint(constraintName: str, parentTableName: str, parentColumnNames: Array[str], childColumnNames: Array[str], acceptRejectRule: AcceptRejectRule, deleteRule: Rule, updateRule: Rule)
    ForeignKeyConstraint(constraintName: str, parentTableName: str, parentTableNamespace: str, parentColumnNames: Array[str], childColumnNames: Array[str], acceptRejectRule: AcceptRejectRule, deleteRule: Rule, updateRule: Rule)
    """
    @property
    def AcceptRejectRule(self) -> AcceptRejectRule:
        """
        Get: AcceptRejectRule(self: ForeignKeyConstraint) -> AcceptRejectRule
        Set: AcceptRejectRule(self: ForeignKeyConstraint) = value
        """
        ...

    @property
    def Columns(self) -> Array:
        """ Get: Columns(self: ForeignKeyConstraint) -> Array[DataColumn] """
        ...

    @property
    def DeleteRule(self) -> Rule:
        """
        Get: DeleteRule(self: ForeignKeyConstraint) -> Rule
        Set: DeleteRule(self: ForeignKeyConstraint) = value
        """
        ...

    @property
    def RelatedColumns(self) -> Array:
        """ Get: RelatedColumns(self: ForeignKeyConstraint) -> Array[DataColumn] """
        ...

    @property
    def RelatedTable(self) -> DataTable:
        """ Get: RelatedTable(self: ForeignKeyConstraint) -> DataTable """
        ...

    @property
    def UpdateRule(self) -> Rule:
        """
        Get: UpdateRule(self: ForeignKeyConstraint) -> Rule
        Set: UpdateRule(self: ForeignKeyConstraint) = value
        """
        ...


    def Equals(self, key:object) -> bool:
        """ Equals(self: ForeignKeyConstraint, key: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ForeignKeyConstraint) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, parentColumn: DataColumn, childColumn: DataColumn)
        __new__(cls: type, constraintName: str, parentColumn: DataColumn, childColumn: DataColumn)
        __new__(cls: type, parentColumns: Array[DataColumn], childColumns: Array[DataColumn])
        __new__(cls: type, constraintName: str, parentColumns: Array[DataColumn], childColumns: Array[DataColumn])
        __new__(cls: type, constraintName: str, parentTableName: str, parentColumnNames: Array[str], childColumnNames: Array[str], acceptRejectRule: AcceptRejectRule, deleteRule: Rule, updateRule: Rule)
        __new__(cls: type, constraintName: str, parentTableName: str, parentTableNamespace: str, parentColumnNames: Array[str], childColumnNames: Array[str], acceptRejectRule: AcceptRejectRule, deleteRule: Rule, updateRule: Rule)
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class IColumnMapping: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataSetColumn(self) -> str:
        """
        Get: DataSetColumn(self: IColumnMapping) -> str
        Set: DataSetColumn(self: IColumnMapping) = value
        """
        ...

    @property
    def SourceColumn(self) -> str:
        """
        Get: SourceColumn(self: IColumnMapping) -> str
        Set: SourceColumn(self: IColumnMapping) = value
        """
        ...



class IColumnMappingCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def GetByDataSetColumn(self, dataSetColumnName:str) -> IColumnMapping:
        """ GetByDataSetColumn(self: IColumnMappingCollection, dataSetColumnName: str) -> IColumnMapping """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class IDataAdapter: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def MissingMappingAction(self): # -> MissingMappingAction
        """
        Get: MissingMappingAction(self: IDataAdapter) -> MissingMappingAction
        Set: MissingMappingAction(self: IDataAdapter) = value
        """
        ...

    @property
    def MissingSchemaAction(self): # -> MissingSchemaAction
        """
        Get: MissingSchemaAction(self: IDataAdapter) -> MissingSchemaAction
        Set: MissingSchemaAction(self: IDataAdapter) = value
        """
        ...

    @property
    def TableMappings(self): # -> ITableMappingCollection
        """ Get: TableMappings(self: IDataAdapter) -> ITableMappingCollection """
        ...


    def Fill(self, dataSet:DataSet) -> int:
        """ Fill(self: IDataAdapter, dataSet: DataSet) -> int """
        ...

    def FillSchema(self, dataSet:DataSet, schemaType) -> Array: # Not found arg types: {'schemaType': 'SchemaType'}
        """ FillSchema(self: IDataAdapter, dataSet: DataSet, schemaType: SchemaType) -> Array[DataTable] """
        ...

    def GetFillParameters(self) -> Array:
        """ GetFillParameters(self: IDataAdapter) -> Array[IDataParameter] """
        ...

    def Update(self, dataSet:DataSet) -> int:
        """ Update(self: IDataAdapter, dataSet: DataSet) -> int """
        ...


class IDataParameter: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DbType(self) -> DbType:
        """
        Get: DbType(self: IDataParameter) -> DbType
        Set: DbType(self: IDataParameter) = value
        """
        ...

    @property
    def Direction(self): # -> ParameterDirection
        """
        Get: Direction(self: IDataParameter) -> ParameterDirection
        Set: Direction(self: IDataParameter) = value
        """
        ...

    @property
    def IsNullable(self) -> bool:
        """ Get: IsNullable(self: IDataParameter) -> bool """
        ...

    @property
    def ParameterName(self) -> str:
        """
        Get: ParameterName(self: IDataParameter) -> str
        Set: ParameterName(self: IDataParameter) = value
        """
        ...

    @property
    def SourceColumn(self) -> str:
        """
        Get: SourceColumn(self: IDataParameter) -> str
        Set: SourceColumn(self: IDataParameter) = value
        """
        ...

    @property
    def SourceVersion(self) -> DataRowVersion:
        """
        Get: SourceVersion(self: IDataParameter) -> DataRowVersion
        Set: SourceVersion(self: IDataParameter) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: IDataParameter) -> object
        Set: Value(self: IDataParameter) = value
        """
        ...



class IDataParameterCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class IDbCommand(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CommandText(self) -> str:
        """
        Get: CommandText(self: IDbCommand) -> str
        Set: CommandText(self: IDbCommand) = value
        """
        ...

    @property
    def CommandTimeout(self) -> int:
        """
        Get: CommandTimeout(self: IDbCommand) -> int
        Set: CommandTimeout(self: IDbCommand) = value
        """
        ...

    @property
    def CommandType(self) -> CommandType:
        """
        Get: CommandType(self: IDbCommand) -> CommandType
        Set: CommandType(self: IDbCommand) = value
        """
        ...

    @property
    def Connection(self): # -> IDbConnection
        """
        Get: Connection(self: IDbCommand) -> IDbConnection
        Set: Connection(self: IDbCommand) = value
        """
        ...

    @property
    def Parameters(self) -> IDataParameterCollection:
        """ Get: Parameters(self: IDbCommand) -> IDataParameterCollection """
        ...

    @property
    def Transaction(self): # -> IDbTransaction
        """
        Get: Transaction(self: IDbCommand) -> IDbTransaction
        Set: Transaction(self: IDbCommand) = value
        """
        ...

    @property
    def UpdatedRowSource(self): # -> UpdateRowSource
        """
        Get: UpdatedRowSource(self: IDbCommand) -> UpdateRowSource
        Set: UpdatedRowSource(self: IDbCommand) = value
        """
        ...


    def Cancel(self): # -> 
        """ Cancel(self: IDbCommand) """
        ...

    def CreateParameter(self): # -> IDbDataParameter
        """ CreateParameter(self: IDbCommand) -> IDbDataParameter """
        ...

    def ExecuteNonQuery(self) -> int:
        """ ExecuteNonQuery(self: IDbCommand) -> int """
        ...

    def ExecuteReader(self, behavior:CommandBehavior = ...) -> IDataReader:
        """
        ExecuteReader(self: IDbCommand) -> IDataReader
        ExecuteReader(self: IDbCommand, behavior: CommandBehavior) -> IDataReader
        """
        ...

    def ExecuteScalar(self) -> object:
        """ ExecuteScalar(self: IDbCommand) -> object """
        ...

    def Prepare(self): # -> 
        """ Prepare(self: IDbCommand) """
        ...


class IDbConnection(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: IDbConnection) -> str
        Set: ConnectionString(self: IDbConnection) = value
        """
        ...

    @property
    def ConnectionTimeout(self) -> int:
        """ Get: ConnectionTimeout(self: IDbConnection) -> int """
        ...

    @property
    def Database(self) -> str:
        """ Get: Database(self: IDbConnection) -> str """
        ...

    @property
    def State(self) -> ConnectionState:
        """ Get: State(self: IDbConnection) -> ConnectionState """
        ...


    def BeginTransaction(self, il:IsolationLevel = ...): # -> IDbTransaction
        """
        BeginTransaction(self: IDbConnection) -> IDbTransaction
        BeginTransaction(self: IDbConnection, il: IsolationLevel) -> IDbTransaction
        """
        ...

    def ChangeDatabase(self, databaseName:str): # -> 
        """ ChangeDatabase(self: IDbConnection, databaseName: str) """
        ...

    def Close(self): # -> 
        """ Close(self: IDbConnection) """
        ...

    def CreateCommand(self) -> IDbCommand:
        """ CreateCommand(self: IDbConnection) -> IDbCommand """
        ...

    def Open(self): # -> 
        """ Open(self: IDbConnection) """
        ...


class IDbDataAdapter(IDataAdapter): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DeleteCommand(self) -> IDbCommand:
        """
        Get: DeleteCommand(self: IDbDataAdapter) -> IDbCommand
        Set: DeleteCommand(self: IDbDataAdapter) = value
        """
        ...

    @property
    def InsertCommand(self) -> IDbCommand:
        """
        Get: InsertCommand(self: IDbDataAdapter) -> IDbCommand
        Set: InsertCommand(self: IDbDataAdapter) = value
        """
        ...

    @property
    def SelectCommand(self) -> IDbCommand:
        """
        Get: SelectCommand(self: IDbDataAdapter) -> IDbCommand
        Set: SelectCommand(self: IDbDataAdapter) = value
        """
        ...

    @property
    def UpdateCommand(self) -> IDbCommand:
        """
        Get: UpdateCommand(self: IDbDataAdapter) -> IDbCommand
        Set: UpdateCommand(self: IDbDataAdapter) = value
        """
        ...



class IDbDataParameter(IDataParameter): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Precision(self) -> Byte:
        """
        Get: Precision(self: IDbDataParameter) -> Byte
        Set: Precision(self: IDbDataParameter) = value
        """
        ...

    @property
    def Scale(self) -> Byte:
        """
        Get: Scale(self: IDbDataParameter) -> Byte
        Set: Scale(self: IDbDataParameter) = value
        """
        ...

    @property
    def Size(self) -> int:
        """
        Get: Size(self: IDbDataParameter) -> int
        Set: Size(self: IDbDataParameter) = value
        """
        ...



class IDbTransaction(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Connection(self) -> IDbConnection:
        """ Get: Connection(self: IDbTransaction) -> IDbConnection """
        ...

    @property
    def IsolationLevel(self) -> IsolationLevel:
        """ Get: IsolationLevel(self: IDbTransaction) -> IsolationLevel """
        ...


    def Commit(self): # -> 
        """ Commit(self: IDbTransaction) """
        ...

    def Rollback(self): # -> 
        """ Rollback(self: IDbTransaction) """
        ...


class IExtendedDataRecord(IDataRecord): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataRecordInfo(self): # -> DataRecordInfo
        """ Get: DataRecordInfo(self: IExtendedDataRecord) -> DataRecordInfo """
        ...


    def GetDataReader(self, i:int) -> DbDataReader:
        """ GetDataReader(self: IExtendedDataRecord, i: int) -> DbDataReader """
        ...

    def GetDataRecord(self, i:int) -> DbDataRecord:
        """ GetDataRecord(self: IExtendedDataRecord, i: int) -> DbDataRecord """
        ...


class InRowChangingEventException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InRowChangingEventException()
    InRowChangingEventException(s: str)
    InRowChangingEventException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InvalidCommandTreeException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidCommandTreeException()
    InvalidCommandTreeException(message: str)
    InvalidCommandTreeException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InvalidConstraintException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidConstraintException()
    InvalidConstraintException(s: str)
    InvalidConstraintException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class IsolationLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum IsolationLevel, values: Chaos (16), ReadCommitted (4096), ReadUncommitted (256), RepeatableRead (65536), Serializable (1048576), Snapshot (16777216), Unspecified (-1) """
    Chaos: IsolationLevel = ...
    ReadCommitted: IsolationLevel = ...
    ReadUncommitted: IsolationLevel = ...
    RepeatableRead: IsolationLevel = ...
    Serializable: IsolationLevel = ...
    Snapshot: IsolationLevel = ...
    Unspecified: IsolationLevel = ...
    value__ = ...


class ITableMapping: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ColumnMappings(self) -> IColumnMappingCollection:
        """ Get: ColumnMappings(self: ITableMapping) -> IColumnMappingCollection """
        ...

    @property
    def DataSetTable(self) -> str:
        """
        Get: DataSetTable(self: ITableMapping) -> str
        Set: DataSetTable(self: ITableMapping) = value
        """
        ...

    @property
    def SourceTable(self) -> str:
        """
        Get: SourceTable(self: ITableMapping) -> str
        Set: SourceTable(self: ITableMapping) = value
        """
        ...



class ITableMappingCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def GetByDataSetTable(self, dataSetTableName:str) -> ITableMapping:
        """ GetByDataSetTable(self: ITableMappingCollection, dataSetTableName: str) -> ITableMapping """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class KeyRestrictionBehavior(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum KeyRestrictionBehavior, values: AllowOnly (0), PreventUsage (1) """
    AllowOnly: KeyRestrictionBehavior = ...
    PreventUsage: KeyRestrictionBehavior = ...
    value__ = ...


class LoadOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LoadOption, values: OverwriteChanges (1), PreserveChanges (2), Upsert (3) """
    OverwriteChanges: LoadOption = ...
    PreserveChanges: LoadOption = ...
    Upsert: LoadOption = ...
    value__ = ...


class MappingException(EntityException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MappingException()
    MappingException(message: str)
    MappingException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class MappingType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MappingType, values: Attribute (2), Element (1), Hidden (4), SimpleContent (3) """
    Attribute: MappingType = ...
    Element: MappingType = ...
    Hidden: MappingType = ...
    SimpleContent: MappingType = ...
    value__ = ...


class MergeFailedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ MergeFailedEventArgs(table: DataTable, conflict: str) """
    @property
    def Conflict(self) -> str:
        """ Get: Conflict(self: MergeFailedEventArgs) -> str """
        ...

    @property
    def Table(self) -> DataTable:
        """ Get: Table(self: MergeFailedEventArgs) -> DataTable """
        ...


    def __new__(cls, table:DataTable, conflict:str) -> Self:
        """ __new__(cls: type, table: DataTable, conflict: str) """
        ...


class MergeFailedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MergeFailedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:MergeFailedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: MergeFailedEventHandler, sender: object, e: MergeFailedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: MergeFailedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:MergeFailedEventArgs): # -> 
        """ Invoke(self: MergeFailedEventHandler, sender: object, e: MergeFailedEventArgs) """
        ...


class MetadataException(EntityException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MetadataException()
    MetadataException(message: str)
    MetadataException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class MissingMappingAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MissingMappingAction, values: Error (3), Ignore (2), Passthrough (1) """
    Error: MissingMappingAction = ...
    Ignore: MissingMappingAction = ...
    Passthrough: MissingMappingAction = ...
    value__ = ...


class MissingPrimaryKeyException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MissingPrimaryKeyException()
    MissingPrimaryKeyException(s: str)
    MissingPrimaryKeyException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class MissingSchemaAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MissingSchemaAction, values: Add (1), AddWithKey (4), Error (3), Ignore (2) """
    Add: MissingSchemaAction = ...
    AddWithKey: MissingSchemaAction = ...
    Error: MissingSchemaAction = ...
    Ignore: MissingSchemaAction = ...
    value__ = ...


class NoNullAllowedException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    NoNullAllowedException()
    NoNullAllowedException(s: str)
    NoNullAllowedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ObjectNotFoundException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ObjectNotFoundException()
    ObjectNotFoundException(message: str)
    ObjectNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class OperationAbortedException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    SerializeObjectState = ...


class UpdateException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    UpdateException()
    UpdateException(message: str)
    UpdateException(message: str, innerException: Exception)
    UpdateException(message: str, innerException: Exception, stateEntries: IEnumerable[ObjectStateEntry])
    """
    @property
    def StateEntries(self) -> ReadOnlyCollection:
        """ Get: StateEntries(self: UpdateException) -> ReadOnlyCollection[ObjectStateEntry] """
        ...


    SerializeObjectState = ...


class OptimisticConcurrencyException(UpdateException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    OptimisticConcurrencyException()
    OptimisticConcurrencyException(message: str)
    OptimisticConcurrencyException(message: str, innerException: Exception)
    OptimisticConcurrencyException(message: str, innerException: Exception, stateEntries: IEnumerable[ObjectStateEntry])
    """
    SerializeObjectState = ...


class OrderedEnumerableRowCollection(EnumerableRowCollection): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[TRow]'>, <type 'object'>
    """ no doc """
    pass

class ParameterDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ParameterDirection, values: Input (1), InputOutput (3), Output (2), ReturnValue (6) """
    Input: ParameterDirection = ...
    InputOutput: ParameterDirection = ...
    Output: ParameterDirection = ...
    ReturnValue: ParameterDirection = ...
    value__ = ...


class PropertyAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PropertyAttributes, values: NotSupported (0), Optional (2), Read (512), Required (1), Write (1024) """
    NotSupported: PropertyAttributes = ...
    Optional: PropertyAttributes = ...
    Read: PropertyAttributes = ...
    Required: PropertyAttributes = ...
    value__ = ...
    Write: PropertyAttributes = ...


class PropertyCollection(Hashtable): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICloneable'>, <type 'IDeserializationCallback'>, <type 'ISerializable'>, <type 'ICollection'>, <type 'object'>
    """ PropertyCollection() """
    pass

class PropertyConstraintException(ConstraintException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PropertyConstraintException()
    PropertyConstraintException(message: str)
    PropertyConstraintException(message: str, innerException: Exception)
    PropertyConstraintException(message: str, propertyName: str)
    PropertyConstraintException(message: str, propertyName: str, innerException: Exception)
    """
    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: PropertyConstraintException) -> str """
        ...


    SerializeObjectState = ...


class ProviderIncompatibleException(EntityException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ProviderIncompatibleException()
    ProviderIncompatibleException(message: str)
    ProviderIncompatibleException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ReadOnlyException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ReadOnlyException()
    ReadOnlyException(s: str)
    ReadOnlyException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class RowNotInTableException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RowNotInTableException()
    RowNotInTableException(s: str)
    RowNotInTableException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class Rule(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Rule, values: Cascade (1), None (0), SetDefault (3), SetNull (2) """
    Cascade: Rule = ...
    SetDefault: Rule = ...
    SetNull: Rule = ...
    value__ = ...


class SchemaSerializationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SchemaSerializationMode, values: ExcludeSchema (2), IncludeSchema (1) """
    ExcludeSchema: SchemaSerializationMode = ...
    IncludeSchema: SchemaSerializationMode = ...
    value__ = ...


class SchemaType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SchemaType, values: Mapped (2), Source (1) """
    Mapped: SchemaType = ...
    Source: SchemaType = ...
    value__ = ...


class SerializationFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SerializationFormat, values: Binary (1), Xml (0) """
    Binary: SerializationFormat = ...
    value__ = ...
    Xml: SerializationFormat = ...


class SqlDbType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlDbType, values: BigInt (0), Binary (1), Bit (2), Char (3), Date (31), DateTime (4), DateTime2 (33), DateTimeOffset (34), Decimal (5), Float (6), Image (7), Int (8), Money (9), NChar (10), NText (11), NVarChar (12), Real (13), SmallDateTime (15), SmallInt (16), SmallMoney (17), Structured (30), Text (18), Time (32), Timestamp (19), TinyInt (20), Udt (29), UniqueIdentifier (14), VarBinary (21), VarChar (22), Variant (23), Xml (25) """
    BigInt: SqlDbType = ...
    Binary: SqlDbType = ...
    Bit: SqlDbType = ...
    Char: SqlDbType = ...
    Date: SqlDbType = ...
    DateTime: SqlDbType = ...
    DateTime2: SqlDbType = ...
    DateTimeOffset: SqlDbType = ...
    Decimal: SqlDbType = ...
    Float: SqlDbType = ...
    Image: SqlDbType = ...
    Int: SqlDbType = ...
    Money: SqlDbType = ...
    NChar: SqlDbType = ...
    NText: SqlDbType = ...
    NVarChar: SqlDbType = ...
    Real: SqlDbType = ...
    SmallDateTime: SqlDbType = ...
    SmallInt: SqlDbType = ...
    SmallMoney: SqlDbType = ...
    Structured: SqlDbType = ...
    Text: SqlDbType = ...
    Time: SqlDbType = ...
    Timestamp: SqlDbType = ...
    TinyInt: SqlDbType = ...
    Udt: SqlDbType = ...
    UniqueIdentifier: SqlDbType = ...
    value__ = ...
    VarBinary: SqlDbType = ...
    VarChar: SqlDbType = ...
    Variant: SqlDbType = ...
    Xml: SqlDbType = ...


class StateChangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ StateChangeEventArgs(originalState: ConnectionState, currentState: ConnectionState) """
    @property
    def CurrentState(self) -> ConnectionState:
        """ Get: CurrentState(self: StateChangeEventArgs) -> ConnectionState """
        ...

    @property
    def OriginalState(self) -> ConnectionState:
        """ Get: OriginalState(self: StateChangeEventArgs) -> ConnectionState """
        ...


    def __new__(cls, originalState:ConnectionState, currentState:ConnectionState) -> Self:
        """ __new__(cls: type, originalState: ConnectionState, currentState: ConnectionState) """
        ...


class StateChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ StateChangeEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:StateChangeEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: StateChangeEventHandler, sender: object, e: StateChangeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: StateChangeEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:StateChangeEventArgs): # -> 
        """ Invoke(self: StateChangeEventHandler, sender: object, e: StateChangeEventArgs) """
        ...


class StatementCompletedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ StatementCompletedEventArgs(recordCount: int) """
    @property
    def RecordCount(self) -> int:
        """ Get: RecordCount(self: StatementCompletedEventArgs) -> int """
        ...


    def __new__(cls, recordCount:int) -> Self:
        """ __new__(cls: type, recordCount: int) """
        ...


class StatementCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ StatementCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:StatementCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: StatementCompletedEventHandler, sender: object, e: StatementCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: StatementCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:StatementCompletedEventArgs): # -> 
        """ Invoke(self: StatementCompletedEventHandler, sender: object, e: StatementCompletedEventArgs) """
        ...


class StatementType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StatementType, values: Batch (4), Delete (3), Insert (1), Select (0), Update (2) """
    Batch: StatementType = ...
    Delete: StatementType = ...
    Insert: StatementType = ...
    Select: StatementType = ...
    Update: StatementType = ...
    value__ = ...


class StrongTypingException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    StrongTypingException()
    StrongTypingException(message: str)
    StrongTypingException(s: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SyntaxErrorException(InvalidExpressionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SyntaxErrorException()
    SyntaxErrorException(s: str)
    SyntaxErrorException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class TypedDataSetGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """ TypedDataSetGenerator() """
    @staticmethod
    def Generate(dataSet:DataSet, codeNamespace:CodeNamespace, codeGen:ICodeGenerator): # -> 
        """ Generate(dataSet: DataSet, codeNamespace: CodeNamespace, codeGen: ICodeGenerator) """
        ...

    @staticmethod
    def GenerateIdName(name:str, codeGen:ICodeGenerator) -> str:
        """ GenerateIdName(name: str, codeGen: ICodeGenerator) -> str """
        ...


class TypedDataSetGeneratorException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TypedDataSetGeneratorException()
    TypedDataSetGeneratorException(message: str)
    TypedDataSetGeneratorException(message: str, innerException: Exception)
    TypedDataSetGeneratorException(list: ArrayList)
    """
    @property
    def ErrorList(self) -> ArrayList:
        """ Get: ErrorList(self: TypedDataSetGeneratorException) -> ArrayList """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: TypedDataSetGeneratorException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class TypedTableBase(IEnumerable, DataTable): # skipped bases: <type 'IDisposable'>, <type 'ISupportInitializeNotification'>, <type 'IComponent'>, <type 'IXmlSerializable'>, <type 'IEnumerable'>, <type 'ISupportInitialize'>, <type 'IListSource'>, <type 'IServiceProvider'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    def Cast(self) -> EnumerableRowCollection:
        """ Cast[TResult](self: TypedTableBase[T]) -> EnumerableRowCollection[TResult] """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        ...

    fInitInProgress = ...


class TypedTableBaseExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AsEnumerable(source:TypedTableBase) -> EnumerableRowCollection:
        """ AsEnumerable[TRow](source: TypedTableBase[TRow]) -> EnumerableRowCollection[TRow] """
        ...

    @staticmethod
    def ElementAtOrDefault(source:TypedTableBase, index:int): # -> TRow
        """ ElementAtOrDefault[TRow](source: TypedTableBase[TRow], index: int) -> TRow """
        ...

    @staticmethod
    def OrderBy(source:TypedTableBase, keySelector, comparer:IComparer = ...) -> OrderedEnumerableRowCollection: # Not found arg types: {'keySelector': 'Func'}
        """
        OrderBy[(TRow, TKey)](source: TypedTableBase[TRow], keySelector: Func[TRow, TKey]) -> OrderedEnumerableRowCollection[TRow]
        OrderBy[(TRow, TKey)](source: TypedTableBase[TRow], keySelector: Func[TRow, TKey], comparer: IComparer[TKey]) -> OrderedEnumerableRowCollection[TRow]
        """
        ...

    @staticmethod
    def OrderByDescending(source:TypedTableBase, keySelector, comparer:IComparer = ...) -> OrderedEnumerableRowCollection: # Not found arg types: {'keySelector': 'Func'}
        """
        OrderByDescending[(TRow, TKey)](source: TypedTableBase[TRow], keySelector: Func[TRow, TKey]) -> OrderedEnumerableRowCollection[TRow]
        OrderByDescending[(TRow, TKey)](source: TypedTableBase[TRow], keySelector: Func[TRow, TKey], comparer: IComparer[TKey]) -> OrderedEnumerableRowCollection[TRow]
        """
        ...

    @staticmethod
    def Select(source:TypedTableBase, selector) -> EnumerableRowCollection: # Not found arg types: {'selector': 'Func'}
        """ Select[(TRow, S)](source: TypedTableBase[TRow], selector: Func[TRow, S]) -> EnumerableRowCollection[S] """
        ...

    @staticmethod
    def Where(source:TypedTableBase, predicate) -> EnumerableRowCollection: # Not found arg types: {'predicate': 'Func'}
        """ Where[TRow](source: TypedTableBase[TRow], predicate: Func[TRow, bool]) -> EnumerableRowCollection[TRow] """
        ...

    __all__: list = ...


class UniqueConstraint(Constraint): # skipped bases: <type 'object'>
    """
    UniqueConstraint(name: str, column: DataColumn)
    UniqueConstraint(column: DataColumn)
    UniqueConstraint(name: str, columns: Array[DataColumn])
    UniqueConstraint(columns: Array[DataColumn])
    UniqueConstraint(name: str, columnNames: Array[str], isPrimaryKey: bool)
    UniqueConstraint(name: str, column: DataColumn, isPrimaryKey: bool)
    UniqueConstraint(column: DataColumn, isPrimaryKey: bool)
    UniqueConstraint(name: str, columns: Array[DataColumn], isPrimaryKey: bool)
    UniqueConstraint(columns: Array[DataColumn], isPrimaryKey: bool)
    """
    @property
    def Columns(self) -> Array:
        """ Get: Columns(self: UniqueConstraint) -> Array[DataColumn] """
        ...

    @property
    def IsPrimaryKey(self) -> bool:
        """ Get: IsPrimaryKey(self: UniqueConstraint) -> bool """
        ...


    def Equals(self, key2:object) -> bool:
        """ Equals(self: UniqueConstraint, key2: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: UniqueConstraint) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, *__args:DataColumn) -> Self:
        """
        __new__(cls: type, name: str, column: DataColumn)
        __new__(cls: type, column: DataColumn)
        __new__(cls: type, name: str, columns: Array[DataColumn])
        __new__(cls: type, columns: Array[DataColumn])
        __new__(cls: type, name: str, columnNames: Array[str], isPrimaryKey: bool)
        __new__(cls: type, name: str, column: DataColumn, isPrimaryKey: bool)
        __new__(cls: type, column: DataColumn, isPrimaryKey: bool)
        __new__(cls: type, name: str, columns: Array[DataColumn], isPrimaryKey: bool)
        __new__(cls: type, columns: Array[DataColumn], isPrimaryKey: bool)
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UpdateRowSource(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UpdateRowSource, values: Both (3), FirstReturnedRecord (2), None (0), OutputParameters (1) """
    Both: UpdateRowSource = ...
    FirstReturnedRecord: UpdateRowSource = ...
    OutputParameters: UpdateRowSource = ...
    value__ = ...


class UpdateStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UpdateStatus, values: Continue (0), ErrorsOccurred (1), SkipAllRemainingRows (3), SkipCurrentRow (2) """
    Continue: UpdateStatus = ...
    ErrorsOccurred: UpdateStatus = ...
    SkipAllRemainingRows: UpdateStatus = ...
    SkipCurrentRow: UpdateStatus = ...
    value__ = ...


class VersionNotFoundException(DataException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    VersionNotFoundException()
    VersionNotFoundException(s: str)
    VersionNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class XmlReadMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlReadMode, values: Auto (0), DiffGram (4), Fragment (5), IgnoreSchema (2), InferSchema (3), InferTypedSchema (6), ReadSchema (1) """
    Auto: XmlReadMode = ...
    DiffGram: XmlReadMode = ...
    Fragment: XmlReadMode = ...
    IgnoreSchema: XmlReadMode = ...
    InferSchema: XmlReadMode = ...
    InferTypedSchema: XmlReadMode = ...
    ReadSchema: XmlReadMode = ...
    value__ = ...


class XmlWriteMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum XmlWriteMode, values: DiffGram (2), IgnoreSchema (1), WriteSchema (0) """
    DiffGram: XmlWriteMode = ...
    IgnoreSchema: XmlWriteMode = ...
    value__ = ...
    WriteSchema: XmlWriteMode = ...


# variables with complex values

