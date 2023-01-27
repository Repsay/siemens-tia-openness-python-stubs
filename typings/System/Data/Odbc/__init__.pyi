# encoding: utf-8
# module System.Data.Odbc calls itself Odbc
# from System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (AsyncCallback, DateTime, Enum, EventArgs, IAsyncResult, 
    ICloneable, MulticastDelegate, TimeSpan)

from System.Collections import ICollection, IEnumerator

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

class OdbcCommand(DbCommand, ICloneable): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDbCommand'>, <type 'object'>
    """
    OdbcCommand()
    OdbcCommand(cmdText: str)
    OdbcCommand(cmdText: str, connection: OdbcConnection)
    OdbcCommand(cmdText: str, connection: OdbcConnection, transaction: OdbcTransaction)
    """
    def ResetCommandTimeout(self): # -> 
        """ ResetCommandTimeout(self: OdbcCommand) """
        ...

    def __new__(cls, cmdText:str = ..., connection:OdbcConnection = ..., transaction:OdbcTransaction = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, cmdText: str)
        __new__(cls: type, cmdText: str, connection: OdbcConnection)
        __new__(cls: type, cmdText: str, connection: OdbcConnection, transaction: OdbcTransaction)
        """
        ...


class OdbcCommandBuilder(DbCommandBuilder): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    OdbcCommandBuilder()
    OdbcCommandBuilder(adapter: OdbcDataAdapter)
    """
    @staticmethod
    def DeriveParameters(command:OdbcCommand): # -> 
        """ DeriveParameters(command: OdbcCommand) """
        ...

    def __new__(cls, adapter:OdbcDataAdapter = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, adapter: OdbcDataAdapter)
        """
        ...


class OdbcConnection(ICloneable, DbConnection): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDbConnection'>, <type 'object'>
    """
    OdbcConnection(connectionString: str)
    OdbcConnection()
    """
    @property
    def Driver(self) -> str:
        """ Get: Driver(self: OdbcConnection) -> str """
        ...


    def EnlistDistributedTransaction(self, transaction:ITransaction): # -> 
        """ EnlistDistributedTransaction(self: OdbcConnection, transaction: ITransaction) """
        ...

    @staticmethod
    def ReleaseObjectPool(): # -> 
        """ ReleaseObjectPool() """
        ...

    def __new__(cls, connectionString:str = ...) -> Self:
        """
        __new__(cls: type, connectionString: str)
        __new__(cls: type)
        """
        ...

    InfoMessage = ...


class OdbcConnectionStringBuilder(DbConnectionStringBuilder): # skipped bases: <type 'ICustomTypeDescriptor'>, <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    OdbcConnectionStringBuilder()
    OdbcConnectionStringBuilder(connectionString: str)
    """
    @property
    def Driver(self) -> str:
        """
        Get: Driver(self: OdbcConnectionStringBuilder) -> str
        Set: Driver(self: OdbcConnectionStringBuilder) = value
        """
        ...

    @property
    def Dsn(self) -> str:
        """
        Get: Dsn(self: OdbcConnectionStringBuilder) -> str
        Set: Dsn(self: OdbcConnectionStringBuilder) = value
        """
        ...



class OdbcDataAdapter(DbDataAdapter): # skipped bases: <type 'IDataAdapter'>, <type 'IDisposable'>, <type 'IComponent'>, <type 'ICloneable'>, <type 'IDbDataAdapter'>, <type 'object'>
    """
    OdbcDataAdapter()
    OdbcDataAdapter(selectCommand: OdbcCommand)
    OdbcDataAdapter(selectCommandText: str, selectConnection: OdbcConnection)
    OdbcDataAdapter(selectCommandText: str, selectConnectionString: str)
    """
    RowUpdated = ...
    RowUpdating = ...


class OdbcDataReader(DbDataReader): # skipped bases: <type 'IDisposable'>, <type 'IDataReader'>, <type 'IDataRecord'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetDate(self, i:int) -> DateTime:
        """ GetDate(self: OdbcDataReader, i: int) -> DateTime """
        ...

    def GetTime(self, i:int) -> TimeSpan:
        """ GetTime(self: OdbcDataReader, i: int) -> TimeSpan """
        ...


class OdbcError: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Message(self) -> str:
        """ Get: Message(self: OdbcError) -> str """
        ...

    @property
    def NativeError(self) -> int:
        """ Get: NativeError(self: OdbcError) -> int """
        ...

    @property
    def Source(self) -> str:
        """ Get: Source(self: OdbcError) -> str """
        ...

    @property
    def SQLState(self) -> str:
        """ Get: SQLState(self: OdbcError) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: OdbcError) -> str """
        ...


class OdbcErrorCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: OdbcErrorCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class OdbcException(DbException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def Errors(self) -> OdbcErrorCollection:
        """ Get: Errors(self: OdbcException) -> OdbcErrorCollection """
        ...


    SerializeObjectState = ...


class OdbcFactory(DbProviderFactory): # skipped bases: <type 'object'>
    """ no doc """
    Instance: OdbcFactory = ...


class OdbcInfoMessageEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Errors(self) -> OdbcErrorCollection:
        """ Get: Errors(self: OdbcInfoMessageEventArgs) -> OdbcErrorCollection """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: OdbcInfoMessageEventArgs) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: OdbcInfoMessageEventArgs) -> str """
        ...


class OdbcInfoMessageEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OdbcInfoMessageEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:OdbcInfoMessageEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: OdbcInfoMessageEventHandler, sender: object, e: OdbcInfoMessageEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: OdbcInfoMessageEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:OdbcInfoMessageEventArgs): # -> 
        """ Invoke(self: OdbcInfoMessageEventHandler, sender: object, e: OdbcInfoMessageEventArgs) """
        ...


class OdbcMetaDataCollectionNames: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Columns: str = ...
    Indexes: str = ...
    ProcedureColumns: str = ...
    ProcedureParameters: str = ...
    Procedures: str = ...
    Tables: str = ...
    Views: str = ...
    __all__: list = ...


class OdbcMetaDataColumnNames: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    BooleanFalseLiteral: str = ...
    BooleanTrueLiteral: str = ...
    SQLType: str = ...
    __all__: list = ...


class OdbcParameter(ICloneable, DbParameter): # skipped bases: <type 'IDataParameter'>, <type 'IDbDataParameter'>, <type 'object'>
    """
    OdbcParameter()
    OdbcParameter(name: str, value: object)
    OdbcParameter(name: str, type: OdbcType)
    OdbcParameter(name: str, type: OdbcType, size: int)
    OdbcParameter(name: str, type: OdbcType, size: int, sourcecolumn: str)
    OdbcParameter(parameterName: str, odbcType: OdbcType, size: int, parameterDirection: ParameterDirection, isNullable: bool, precision: Byte, scale: Byte, srcColumn: str, srcVersion: DataRowVersion, value: object)
    OdbcParameter(parameterName: str, odbcType: OdbcType, size: int, parameterDirection: ParameterDirection, precision: Byte, scale: Byte, sourceColumn: str, sourceVersion: DataRowVersion, sourceColumnNullMapping: bool, value: object)
    """
    @property
    def OdbcType(self) -> OdbcType:
        """
        Get: OdbcType(self: OdbcParameter) -> OdbcType
        Set: OdbcType(self: OdbcParameter) = value
        """
        ...


    def ResetOdbcType(self): # -> 
        """ ResetOdbcType(self: OdbcParameter) """
        ...

    def ToString(self) -> str:
        """ ToString(self: OdbcParameter) -> str """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str, value: object)
        __new__(cls: type, name: str, type: OdbcType)
        __new__(cls: type, name: str, type: OdbcType, size: int)
        __new__(cls: type, name: str, type: OdbcType, size: int, sourcecolumn: str)
        __new__(cls: type, parameterName: str, odbcType: OdbcType, size: int, parameterDirection: ParameterDirection, isNullable: bool, precision: Byte, scale: Byte, srcColumn: str, srcVersion: DataRowVersion, value: object)
        __new__(cls: type, parameterName: str, odbcType: OdbcType, size: int, parameterDirection: ParameterDirection, precision: Byte, scale: Byte, sourceColumn: str, sourceVersion: DataRowVersion, sourceColumnNullMapping: bool, value: object)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class OdbcParameterCollection(DbParameterCollection): # skipped bases: <type 'IDataParameterCollection'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def AddWithValue(self, parameterName:str, value:object) -> OdbcParameter:
        """ AddWithValue(self: OdbcParameterCollection, parameterName: str, value: object) -> OdbcParameter """
        ...


class OdbcPermission(DBDataPermission): # skipped bases: <type 'IPermission'>, <type 'IUnrestrictedPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    OdbcPermission()
    OdbcPermission(state: PermissionState)
    OdbcPermission(state: PermissionState, allowBlankPassword: bool)
    """
    pass

class OdbcPermissionAttribute(DBDataPermissionAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ OdbcPermissionAttribute(action: SecurityAction) """
    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: OdbcPermissionAttribute) -> IPermission """
        ...


class OdbcRowUpdatedEventArgs(RowUpdatedEventArgs): # skipped bases: <type 'object'>
    """ OdbcRowUpdatedEventArgs(row: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping) """
    pass

class OdbcRowUpdatedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OdbcRowUpdatedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:OdbcRowUpdatedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: OdbcRowUpdatedEventHandler, sender: object, e: OdbcRowUpdatedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: OdbcRowUpdatedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:OdbcRowUpdatedEventArgs): # -> 
        """ Invoke(self: OdbcRowUpdatedEventHandler, sender: object, e: OdbcRowUpdatedEventArgs) """
        ...


class OdbcRowUpdatingEventArgs(RowUpdatingEventArgs): # skipped bases: <type 'object'>
    """ OdbcRowUpdatingEventArgs(row: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping) """
    pass

class OdbcRowUpdatingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OdbcRowUpdatingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:OdbcRowUpdatingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: OdbcRowUpdatingEventHandler, sender: object, e: OdbcRowUpdatingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: OdbcRowUpdatingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:OdbcRowUpdatingEventArgs): # -> 
        """ Invoke(self: OdbcRowUpdatingEventHandler, sender: object, e: OdbcRowUpdatingEventArgs) """
        ...


class OdbcTransaction(DbTransaction): # skipped bases: <type 'IDisposable'>, <type 'IDbTransaction'>, <type 'object'>
    """ no doc """
    pass

class OdbcType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OdbcType, values: BigInt (1), Binary (2), Bit (3), Char (4), Date (23), DateTime (5), Decimal (6), Double (8), Image (9), Int (10), NChar (11), NText (12), Numeric (7), NVarChar (13), Real (14), SmallDateTime (16), SmallInt (17), Text (18), Time (24), Timestamp (19), TinyInt (20), UniqueIdentifier (15), VarBinary (21), VarChar (22) """
    BigInt: OdbcType = ...
    Binary: OdbcType = ...
    Bit: OdbcType = ...
    Char: OdbcType = ...
    Date: OdbcType = ...
    DateTime: OdbcType = ...
    Decimal: OdbcType = ...
    Double: OdbcType = ...
    Image: OdbcType = ...
    Int: OdbcType = ...
    NChar: OdbcType = ...
    NText: OdbcType = ...
    Numeric: OdbcType = ...
    NVarChar: OdbcType = ...
    Real: OdbcType = ...
    SmallDateTime: OdbcType = ...
    SmallInt: OdbcType = ...
    Text: OdbcType = ...
    Time: OdbcType = ...
    Timestamp: OdbcType = ...
    TinyInt: OdbcType = ...
    UniqueIdentifier: OdbcType = ...
    value__ = ...
    VarBinary: OdbcType = ...
    VarChar: OdbcType = ...


