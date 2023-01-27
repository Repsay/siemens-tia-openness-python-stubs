# encoding: utf-8
# module System.Data.OleDb calls itself OleDb
# from System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Enum, EventArgs, Guid, IAsyncResult, 
    ICloneable, MulticastDelegate, TimeSpan, Type)

from System.Collections import ICollection, IEnumerator

from System.Data import DataTable, IsolationLevel

from System.Data.Common import (DBDataPermission, DBDataPermissionAttribute, 
    DbCommand, DbCommandBuilder, DbConnection, DbConnectionStringBuilder, 
    DbDataAdapter, DbDataReader, DbException, DbParameter, 
    DbParameterCollection, DbProviderFactory, DbTransaction, 
    RowUpdatedEventArgs, RowUpdatingEventArgs)

from System.EnterpriseServices import ITransaction

from System.Security import IPermission

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class OleDbCommand(DbCommand, ICloneable): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDbCommand'>, <type 'object'>
    """
    OleDbCommand()
    OleDbCommand(cmdText: str)
    OleDbCommand(cmdText: str, connection: OleDbConnection)
    OleDbCommand(cmdText: str, connection: OleDbConnection, transaction: OleDbTransaction)
    """
    def ResetCommandTimeout(self): # -> 
        """ ResetCommandTimeout(self: OleDbCommand) """
        ...

    def __new__(cls, cmdText:str = ..., connection:OleDbConnection = ..., transaction:OleDbTransaction = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, cmdText: str)
        __new__(cls: type, cmdText: str, connection: OleDbConnection)
        __new__(cls: type, cmdText: str, connection: OleDbConnection, transaction: OleDbTransaction)
        """
        ...


class OleDbCommandBuilder(DbCommandBuilder): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    OleDbCommandBuilder()
    OleDbCommandBuilder(adapter: OleDbDataAdapter)
    """
    @staticmethod
    def DeriveParameters(command:OleDbCommand): # -> 
        """ DeriveParameters(command: OleDbCommand) """
        ...

    def __new__(cls, adapter:OleDbDataAdapter = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, adapter: OleDbDataAdapter)
        """
        ...


class OleDbConnection(ICloneable, DbConnection): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDbConnection'>, <type 'object'>
    """
    OleDbConnection(connectionString: str)
    OleDbConnection()
    """
    @property
    def Provider(self) -> str:
        """ Get: Provider(self: OleDbConnection) -> str """
        ...


    def EnlistDistributedTransaction(self, transaction:ITransaction): # -> 
        """ EnlistDistributedTransaction(self: OleDbConnection, transaction: ITransaction) """
        ...

    def GetOleDbSchemaTable(self, schema:Guid, restrictions:Array) -> DataTable:
        """ GetOleDbSchemaTable(self: OleDbConnection, schema: Guid, restrictions: Array[object]) -> DataTable """
        ...

    @staticmethod
    def ReleaseObjectPool(): # -> 
        """ ReleaseObjectPool() """
        ...

    def ResetState(self): # -> 
        """ ResetState(self: OleDbConnection) """
        ...

    def __new__(cls, connectionString:str = ...) -> Self:
        """
        __new__(cls: type, connectionString: str)
        __new__(cls: type)
        """
        ...

    InfoMessage = ...


class OleDbConnectionStringBuilder(DbConnectionStringBuilder): # skipped bases: <type 'ICustomTypeDescriptor'>, <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    OleDbConnectionStringBuilder()
    OleDbConnectionStringBuilder(connectionString: str)
    """
    @property
    def DataSource(self) -> str:
        """
        Get: DataSource(self: OleDbConnectionStringBuilder) -> str
        Set: DataSource(self: OleDbConnectionStringBuilder) = value
        """
        ...

    @property
    def FileName(self) -> str:
        """
        Get: FileName(self: OleDbConnectionStringBuilder) -> str
        Set: FileName(self: OleDbConnectionStringBuilder) = value
        """
        ...

    @property
    def OleDbServices(self) -> int:
        """
        Get: OleDbServices(self: OleDbConnectionStringBuilder) -> int
        Set: OleDbServices(self: OleDbConnectionStringBuilder) = value
        """
        ...

    @property
    def PersistSecurityInfo(self) -> bool:
        """
        Get: PersistSecurityInfo(self: OleDbConnectionStringBuilder) -> bool
        Set: PersistSecurityInfo(self: OleDbConnectionStringBuilder) = value
        """
        ...

    @property
    def Provider(self) -> str:
        """
        Get: Provider(self: OleDbConnectionStringBuilder) -> str
        Set: Provider(self: OleDbConnectionStringBuilder) = value
        """
        ...



class OleDbDataAdapter(DbDataAdapter): # skipped bases: <type 'IDataAdapter'>, <type 'IDisposable'>, <type 'IComponent'>, <type 'ICloneable'>, <type 'IDbDataAdapter'>, <type 'object'>
    """
    OleDbDataAdapter()
    OleDbDataAdapter(selectCommand: OleDbCommand)
    OleDbDataAdapter(selectCommandText: str, selectConnectionString: str)
    OleDbDataAdapter(selectCommandText: str, selectConnection: OleDbConnection)
    """
    RowUpdated = ...
    RowUpdating = ...


class OleDbDataReader(DbDataReader): # skipped bases: <type 'IDisposable'>, <type 'IDataReader'>, <type 'IDataRecord'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetTimeSpan(self, ordinal:int) -> TimeSpan:
        """ GetTimeSpan(self: OleDbDataReader, ordinal: int) -> TimeSpan """
        ...


class OleDbEnumerator: # skipped bases: <type 'object'>, <type 'object'>
    """ OleDbEnumerator() """
    def GetElements(self) -> DataTable:
        """ GetElements(self: OleDbEnumerator) -> DataTable """
        ...

    @staticmethod
    def GetEnumerator(type:Type) -> OleDbDataReader:
        """ GetEnumerator(type: Type) -> OleDbDataReader """
        ...

    @staticmethod
    def GetRootEnumerator() -> OleDbDataReader:
        """ GetRootEnumerator() -> OleDbDataReader """
        ...


class OleDbError: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Message(self) -> str:
        """ Get: Message(self: OleDbError) -> str """
        ...

    @property
    def NativeError(self) -> int:
        """ Get: NativeError(self: OleDbError) -> int """
        ...

    @property
    def Source(self) -> str:
        """ Get: Source(self: OleDbError) -> str """
        ...

    @property
    def SQLState(self) -> str:
        """ Get: SQLState(self: OleDbError) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: OleDbError) -> str """
        ...


class OleDbErrorCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: OleDbErrorCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class OleDbException(DbException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: OleDbException) -> int """
        ...

    @property
    def Errors(self) -> OleDbErrorCollection:
        """ Get: Errors(self: OleDbException) -> OleDbErrorCollection """
        ...


    SerializeObjectState = ...


class OleDbFactory(DbProviderFactory): # skipped bases: <type 'object'>
    """ no doc """
    Instance: OleDbFactory = ...


class OleDbInfoMessageEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: OleDbInfoMessageEventArgs) -> int """
        ...

    @property
    def Errors(self) -> OleDbErrorCollection:
        """ Get: Errors(self: OleDbInfoMessageEventArgs) -> OleDbErrorCollection """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: OleDbInfoMessageEventArgs) -> str """
        ...

    @property
    def Source(self) -> str:
        """ Get: Source(self: OleDbInfoMessageEventArgs) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: OleDbInfoMessageEventArgs) -> str """
        ...


class OleDbInfoMessageEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OleDbInfoMessageEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:OleDbInfoMessageEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: OleDbInfoMessageEventHandler, sender: object, e: OleDbInfoMessageEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: OleDbInfoMessageEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:OleDbInfoMessageEventArgs): # -> 
        """ Invoke(self: OleDbInfoMessageEventHandler, sender: object, e: OleDbInfoMessageEventArgs) """
        ...


class OleDbLiteral(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OleDbLiteral, values: Binary_Literal (1), Catalog_Name (2), Catalog_Separator (3), Char_Literal (4), Column_Alias (5), Column_Name (6), Correlation_Name (7), Cube_Name (21), Cursor_Name (8), Dimension_Name (22), Escape_Percent_Prefix (9), Escape_Percent_Suffix (29), Escape_Underscore_Prefix (10), Escape_Underscore_Suffix (30), Hierarchy_Name (23), Index_Name (11), Invalid (0), Level_Name (24), Like_Percent (12), Like_Underscore (13), Member_Name (25), Procedure_Name (14), Property_Name (26), Quote_Prefix (15), Quote_Suffix (28), Schema_Name (16), Schema_Separator (27), Table_Name (17), Text_Command (18), User_Name (19), View_Name (20) """
    Binary_Literal: OleDbLiteral = ...
    Catalog_Name: OleDbLiteral = ...
    Catalog_Separator: OleDbLiteral = ...
    Char_Literal: OleDbLiteral = ...
    Column_Alias: OleDbLiteral = ...
    Column_Name: OleDbLiteral = ...
    Correlation_Name: OleDbLiteral = ...
    Cube_Name: OleDbLiteral = ...
    Cursor_Name: OleDbLiteral = ...
    Dimension_Name: OleDbLiteral = ...
    Escape_Percent_Prefix: OleDbLiteral = ...
    Escape_Percent_Suffix: OleDbLiteral = ...
    Escape_Underscore_Prefix: OleDbLiteral = ...
    Escape_Underscore_Suffix: OleDbLiteral = ...
    Hierarchy_Name: OleDbLiteral = ...
    Index_Name: OleDbLiteral = ...
    Invalid: OleDbLiteral = ...
    Level_Name: OleDbLiteral = ...
    Like_Percent: OleDbLiteral = ...
    Like_Underscore: OleDbLiteral = ...
    Member_Name: OleDbLiteral = ...
    Procedure_Name: OleDbLiteral = ...
    Property_Name: OleDbLiteral = ...
    Quote_Prefix: OleDbLiteral = ...
    Quote_Suffix: OleDbLiteral = ...
    Schema_Name: OleDbLiteral = ...
    Schema_Separator: OleDbLiteral = ...
    Table_Name: OleDbLiteral = ...
    Text_Command: OleDbLiteral = ...
    User_Name: OleDbLiteral = ...
    value__ = ...
    View_Name: OleDbLiteral = ...


class OleDbMetaDataCollectionNames: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Catalogs: str = ...
    Collations: str = ...
    Columns: str = ...
    Indexes: str = ...
    ProcedureColumns: str = ...
    ProcedureParameters: str = ...
    Procedures: str = ...
    Tables: str = ...
    Views: str = ...
    __all__: list = ...


class OleDbMetaDataColumnNames: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    BooleanFalseLiteral: str = ...
    BooleanTrueLiteral: str = ...
    DateTimeDigits: str = ...
    NativeDataType: str = ...
    __all__: list = ...


class OleDbParameter(ICloneable, DbParameter): # skipped bases: <type 'IDataParameter'>, <type 'IDbDataParameter'>, <type 'object'>
    """
    OleDbParameter()
    OleDbParameter(name: str, value: object)
    OleDbParameter(name: str, dataType: OleDbType)
    OleDbParameter(name: str, dataType: OleDbType, size: int)
    OleDbParameter(name: str, dataType: OleDbType, size: int, srcColumn: str)
    OleDbParameter(parameterName: str, dbType: OleDbType, size: int, direction: ParameterDirection, isNullable: bool, precision: Byte, scale: Byte, srcColumn: str, srcVersion: DataRowVersion, value: object)
    OleDbParameter(parameterName: str, dbType: OleDbType, size: int, direction: ParameterDirection, precision: Byte, scale: Byte, sourceColumn: str, sourceVersion: DataRowVersion, sourceColumnNullMapping: bool, value: object)
    """
    @property
    def OleDbType(self) -> OleDbType:
        """
        Get: OleDbType(self: OleDbParameter) -> OleDbType
        Set: OleDbType(self: OleDbParameter) = value
        """
        ...


    def ResetOleDbType(self): # -> 
        """ ResetOleDbType(self: OleDbParameter) """
        ...

    def ToString(self) -> str:
        """ ToString(self: OleDbParameter) -> str """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str, value: object)
        __new__(cls: type, name: str, dataType: OleDbType)
        __new__(cls: type, name: str, dataType: OleDbType, size: int)
        __new__(cls: type, name: str, dataType: OleDbType, size: int, srcColumn: str)
        __new__(cls: type, parameterName: str, dbType: OleDbType, size: int, direction: ParameterDirection, isNullable: bool, precision: Byte, scale: Byte, srcColumn: str, srcVersion: DataRowVersion, value: object)
        __new__(cls: type, parameterName: str, dbType: OleDbType, size: int, direction: ParameterDirection, precision: Byte, scale: Byte, sourceColumn: str, sourceVersion: DataRowVersion, sourceColumnNullMapping: bool, value: object)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class OleDbParameterCollection(DbParameterCollection): # skipped bases: <type 'IDataParameterCollection'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def AddWithValue(self, parameterName:str, value:object) -> OleDbParameter:
        """ AddWithValue(self: OleDbParameterCollection, parameterName: str, value: object) -> OleDbParameter """
        ...


class OleDbPermission(DBDataPermission): # skipped bases: <type 'IPermission'>, <type 'IUnrestrictedPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    OleDbPermission()
    OleDbPermission(state: PermissionState)
    OleDbPermission(state: PermissionState, allowBlankPassword: bool)
    """
    @property
    def Provider(self) -> str:
        """
        Get: Provider(self: OleDbPermission) -> str
        Set: Provider(self: OleDbPermission) = value
        """
        ...



class OleDbPermissionAttribute(DBDataPermissionAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ OleDbPermissionAttribute(action: SecurityAction) """
    @property
    def Provider(self) -> str:
        """
        Get: Provider(self: OleDbPermissionAttribute) -> str
        Set: Provider(self: OleDbPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: OleDbPermissionAttribute) -> IPermission """
        ...


class OleDbRowUpdatedEventArgs(RowUpdatedEventArgs): # skipped bases: <type 'object'>
    """ OleDbRowUpdatedEventArgs(dataRow: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping) """
    pass

class OleDbRowUpdatedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OleDbRowUpdatedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:OleDbRowUpdatedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: OleDbRowUpdatedEventHandler, sender: object, e: OleDbRowUpdatedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: OleDbRowUpdatedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:OleDbRowUpdatedEventArgs): # -> 
        """ Invoke(self: OleDbRowUpdatedEventHandler, sender: object, e: OleDbRowUpdatedEventArgs) """
        ...


class OleDbRowUpdatingEventArgs(RowUpdatingEventArgs): # skipped bases: <type 'object'>
    """ OleDbRowUpdatingEventArgs(dataRow: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping) """
    pass

class OleDbRowUpdatingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OleDbRowUpdatingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:OleDbRowUpdatingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: OleDbRowUpdatingEventHandler, sender: object, e: OleDbRowUpdatingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: OleDbRowUpdatingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:OleDbRowUpdatingEventArgs): # -> 
        """ Invoke(self: OleDbRowUpdatingEventHandler, sender: object, e: OleDbRowUpdatingEventArgs) """
        ...


class OleDbSchemaGuid: # skipped bases: <type 'object'>, <type 'object'>
    """ OleDbSchemaGuid() """
    Assertions: Guid = ...
    Catalogs: Guid = ...
    Character_Sets: Guid = ...
    Check_Constraints: Guid = ...
    Check_Constraints_By_Table: Guid = ...
    Collations: Guid = ...
    Columns: Guid = ...
    Column_Domain_Usage: Guid = ...
    Column_Privileges: Guid = ...
    Constraint_Column_Usage: Guid = ...
    Constraint_Table_Usage: Guid = ...
    DbInfoKeywords: Guid = ...
    DbInfoLiterals: Guid = ...
    Foreign_Keys: Guid = ...
    Indexes: Guid = ...
    Key_Column_Usage: Guid = ...
    Primary_Keys: Guid = ...
    Procedures: Guid = ...
    Procedure_Columns: Guid = ...
    Procedure_Parameters: Guid = ...
    Provider_Types: Guid = ...
    Referential_Constraints: Guid = ...
    SchemaGuids: Guid = ...
    Schemata: Guid = ...
    Sql_Languages: Guid = ...
    Statistics: Guid = ...
    Tables: Guid = ...
    Tables_Info: Guid = ...
    Table_Constraints: Guid = ...
    Table_Privileges: Guid = ...
    Table_Statistics: Guid = ...
    Translations: Guid = ...
    Trustee: Guid = ...
    Usage_Privileges: Guid = ...
    Views: Guid = ...
    View_Column_Usage: Guid = ...
    View_Table_Usage: Guid = ...


class OleDbTransaction(DbTransaction): # skipped bases: <type 'IDisposable'>, <type 'IDbTransaction'>, <type 'object'>
    """ no doc """
    def Begin(self, isolevel:IsolationLevel = ...) -> OleDbTransaction:
        """
        Begin(self: OleDbTransaction, isolevel: IsolationLevel) -> OleDbTransaction
        Begin(self: OleDbTransaction) -> OleDbTransaction
        """
        ...


class OleDbType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OleDbType, values: BigInt (20), Binary (128), Boolean (11), BSTR (8), Char (129), Currency (6), Date (7), DBDate (133), DBTime (134), DBTimeStamp (135), Decimal (14), Double (5), Empty (0), Error (10), Filetime (64), Guid (72), IDispatch (9), Integer (3), IUnknown (13), LongVarBinary (205), LongVarChar (201), LongVarWChar (203), Numeric (131), PropVariant (138), Single (4), SmallInt (2), TinyInt (16), UnsignedBigInt (21), UnsignedInt (19), UnsignedSmallInt (18), UnsignedTinyInt (17), VarBinary (204), VarChar (200), Variant (12), VarNumeric (139), VarWChar (202), WChar (130) """
    BigInt: OleDbType = ...
    Binary: OleDbType = ...
    Boolean: OleDbType = ...
    BSTR: OleDbType = ...
    Char: OleDbType = ...
    Currency: OleDbType = ...
    Date: OleDbType = ...
    DBDate: OleDbType = ...
    DBTime: OleDbType = ...
    DBTimeStamp: OleDbType = ...
    Decimal: OleDbType = ...
    Double: OleDbType = ...
    Empty: OleDbType = ...
    Error: OleDbType = ...
    Filetime: OleDbType = ...
    Guid: OleDbType = ...
    IDispatch: OleDbType = ...
    Integer: OleDbType = ...
    IUnknown: OleDbType = ...
    LongVarBinary: OleDbType = ...
    LongVarChar: OleDbType = ...
    LongVarWChar: OleDbType = ...
    Numeric: OleDbType = ...
    PropVariant: OleDbType = ...
    Single: OleDbType = ...
    SmallInt: OleDbType = ...
    TinyInt: OleDbType = ...
    UnsignedBigInt: OleDbType = ...
    UnsignedInt: OleDbType = ...
    UnsignedSmallInt: OleDbType = ...
    UnsignedTinyInt: OleDbType = ...
    value__ = ...
    VarBinary: OleDbType = ...
    VarChar: OleDbType = ...
    Variant: OleDbType = ...
    VarNumeric: OleDbType = ...
    VarWChar: OleDbType = ...
    WChar: OleDbType = ...


