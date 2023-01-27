# encoding: utf-8
# module System.Data.OracleClient calls itself OracleClient
# from System.Data.OracleClient, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, DateTime, Decimal, Enum, EventArgs, 
    IAsyncResult, ICloneable, IComparable, Int64, MulticastDelegate, TimeSpan)

from System.Data import KeyRestrictionBehavior

from System.Data.Common import (DbCommand, DbCommandBuilder, DbConnection, 
    DbConnectionStringBuilder, DbDataAdapter, DbDataReader, DbException, 
    DbParameter, DbParameterCollection, DbProviderFactory, DbTransaction, 
    RowUpdatedEventArgs, RowUpdatingEventArgs)

from System.Data.SqlTypes import INullable

from System.EnterpriseServices import ITransaction

from System.IO import Stream

from System.Security import CodeAccessPermission, IPermission

from System.Security.Permissions import (CodeAccessSecurityAttribute, 
    IUnrestrictedPermission, PermissionState)

from typing import Self, Tuple as Tuple_


# no functions
# classes

class OracleBFile(Stream, ICloneable, INullable): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def Connection(self) -> OracleConnection:
        """ Get: Connection(self: OracleBFile) -> OracleConnection """
        ...

    @property
    def DirectoryName(self) -> str:
        """ Get: DirectoryName(self: OracleBFile) -> str """
        ...

    @property
    def FileExists(self) -> bool:
        """ Get: FileExists(self: OracleBFile) -> bool """
        ...

    @property
    def FileName(self) -> str:
        """ Get: FileName(self: OracleBFile) -> str """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: OracleBFile) -> object """
        ...


    def SetFileName(self, directory:str, file:str):
        """ SetFileName(self: OracleBFile, directory: str, file: str) """
        ...

    Null = None


class OracleBinary(IComparable, INullable): # skipped bases: <type 'object'>
    """ OracleBinary(b: Array[Byte]) """
    @property
    def Length(self) -> int:
        """ Get: Length(self: OracleBinary) -> int """
        ...

    @property
    def Value(self) -> Array:
        """ Get: Value(self: OracleBinary) -> Array[Byte] """
        ...


    @staticmethod
    def Concat(x:OracleBinary, y:OracleBinary) -> OracleBinary:
        """ Concat(x: OracleBinary, y: OracleBinary) -> OracleBinary """
        ...

    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: OracleBinary, value: object) -> bool
        Equals(x: OracleBinary, y: OracleBinary) -> OracleBoolean
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: OracleBinary) -> int """
        ...

    @staticmethod
    def GreaterThan(x:OracleBinary, y:OracleBinary) -> OracleBoolean:
        """ GreaterThan(x: OracleBinary, y: OracleBinary) -> OracleBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:OracleBinary, y:OracleBinary) -> OracleBoolean:
        """ GreaterThanOrEqual(x: OracleBinary, y: OracleBinary) -> OracleBoolean """
        ...

    @staticmethod
    def LessThan(x:OracleBinary, y:OracleBinary) -> OracleBoolean:
        """ LessThan(x: OracleBinary, y: OracleBinary) -> OracleBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:OracleBinary, y:OracleBinary) -> OracleBoolean:
        """ LessThanOrEqual(x: OracleBinary, y: OracleBinary) -> OracleBoolean """
        ...

    @staticmethod
    def NotEquals(x:OracleBinary, y:OracleBinary) -> OracleBoolean:
        """ NotEquals(x: OracleBinary, y: OracleBinary) -> OracleBoolean """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: OracleBinary, y: OracleBinary) -> OracleBinary """
        ...

    Null = None


class OracleBoolean(IComparable): # skipped bases: <type 'object'>
    """
    OracleBoolean(value: bool)
    OracleBoolean(value: int)
    """
    @property
    def IsFalse(self) -> bool:
        """ Get: IsFalse(self: OracleBoolean) -> bool """
        ...

    @property
    def IsNull(self) -> bool:
        """ Get: IsNull(self: OracleBoolean) -> bool """
        ...

    @property
    def IsTrue(self) -> bool:
        """ Get: IsTrue(self: OracleBoolean) -> bool """
        ...

    @property
    def Value(self) -> bool:
        """ Get: Value(self: OracleBoolean) -> bool """
        ...


    @staticmethod
    def And(x:OracleBoolean, y:OracleBoolean) -> OracleBoolean:
        """ And(x: OracleBoolean, y: OracleBoolean) -> OracleBoolean """
        ...

    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: OracleBoolean, value: object) -> bool
        Equals(x: OracleBoolean, y: OracleBoolean) -> OracleBoolean
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: OracleBoolean) -> int """
        ...

    @staticmethod
    def NotEquals(x:OracleBoolean, y:OracleBoolean) -> OracleBoolean:
        """ NotEquals(x: OracleBoolean, y: OracleBoolean) -> OracleBoolean """
        ...

    @staticmethod
    def OnesComplement(x:OracleBoolean) -> OracleBoolean:
        """ OnesComplement(x: OracleBoolean) -> OracleBoolean """
        ...

    @staticmethod
    def Or(x:OracleBoolean, y:OracleBoolean) -> OracleBoolean:
        """ Or(x: OracleBoolean, y: OracleBoolean) -> OracleBoolean """
        ...

    @staticmethod
    def Parse(s:str) -> OracleBoolean:
        """ Parse(s: str) -> OracleBoolean """
        ...

    def ToString(self) -> str:
        """ ToString(self: OracleBoolean) -> str """
        ...

    @staticmethod
    def Xor(x:OracleBoolean, y:OracleBoolean) -> OracleBoolean:
        """ Xor(x: OracleBoolean, y: OracleBoolean) -> OracleBoolean """
        ...

    def __and__(self, *args): #cannot find CLR method
        """ __and__(x: OracleBoolean, y: OracleBoolean) -> OracleBoolean """
        ...

    def __invert__(self, *args): #cannot find CLR method
        """ __invert__(x: OracleBoolean) -> OracleBoolean """
        ...

    def __or__(self, *args): #cannot find CLR method
        """ __or__(x: OracleBoolean, y: OracleBoolean) -> OracleBoolean """
        ...

    def __rand__(self, *args): #cannot find CLR method
        """ __rand__(x: OracleBoolean, y: OracleBoolean) -> OracleBoolean """
        ...

    def __ror__(self, *args): #cannot find CLR method
        """ __ror__(x: OracleBoolean, y: OracleBoolean) -> OracleBoolean """
        ...

    def __rxor__(self, *args): #cannot find CLR method
        """ __rxor__(x: OracleBoolean, y: OracleBoolean) -> OracleBoolean """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """ __xor__(x: OracleBoolean, y: OracleBoolean) -> OracleBoolean """
        ...

    Null = None
    One = None
    Zero = None


class OracleClientFactory(DbProviderFactory): # skipped bases: <type 'object'>
    """ no doc """
    Instance = None


class OracleCommand(DbCommand, ICloneable): # skipped bases: <type 'IDisposable'>, <type 'IDbCommand'>, <type 'IComponent'>, <type 'object'>
    """
    OracleCommand()
    OracleCommand(commandText: str)
    OracleCommand(commandText: str, connection: OracleConnection)
    OracleCommand(commandText: str, connection: OracleConnection, tx: OracleTransaction)
    """
    def ExecuteOracleNonQuery(self, rowid) -> Tuple_[int, OracleString]:
        """ ExecuteOracleNonQuery(self: OracleCommand) -> (int, OracleString) """
        ...

    def ExecuteOracleScalar(self) -> object:
        """ ExecuteOracleScalar(self: OracleCommand) -> object """
        ...

    def ResetCommandTimeout(self):
        """ ResetCommandTimeout(self: OracleCommand) """
        ...

    def __new__(cls, commandText=None, connection=None, tx=None) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, commandText: str)
        __new__(cls: type, commandText: str, connection: OracleConnection)
        __new__(cls: type, commandText: str, connection: OracleConnection, tx: OracleTransaction)
        """
        ...


class OracleCommandBuilder(DbCommandBuilder): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    OracleCommandBuilder()
    OracleCommandBuilder(adapter: OracleDataAdapter)
    """
    @staticmethod
    def DeriveParameters(command:OracleCommand):
        """ DeriveParameters(command: OracleCommand) """
        ...

    def __new__(cls, adapter=None) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, adapter: OracleDataAdapter)
        """
        ...


class OracleConnection(ICloneable, DbConnection): # skipped bases: <type 'IDbConnection'>, <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    OracleConnection(connectionString: str)
    OracleConnection()
    """
    @staticmethod
    def ClearAllPools():
        """ ClearAllPools() """
        ...

    @staticmethod
    def ClearPool(connection:OracleConnection):
        """ ClearPool(connection: OracleConnection) """
        ...

    def EnlistDistributedTransaction(self, distributedTransaction:ITransaction):
        """ EnlistDistributedTransaction(self: OracleConnection, distributedTransaction: ITransaction) """
        ...

    def __new__(cls, connectionString:str = ...) -> Self:
        """
        __new__(cls: type, connectionString: str)
        __new__(cls: type)
        """
        ...

    InfoMessage = None


class OracleConnectionStringBuilder(DbConnectionStringBuilder): # skipped bases: <type 'IDictionary'>, <type 'ICollection'>, <type 'ICustomTypeDescriptor'>, <type 'IEnumerable'>, <type 'object'>
    """
    OracleConnectionStringBuilder()
    OracleConnectionStringBuilder(connectionString: str)
    """
    @property
    def DataSource(self) -> str:
        """
        Get: DataSource(self: OracleConnectionStringBuilder) -> str
        Set: DataSource(self: OracleConnectionStringBuilder) = value
        """
        ...

    @property
    def Enlist(self) -> bool:
        """
        Get: Enlist(self: OracleConnectionStringBuilder) -> bool
        Set: Enlist(self: OracleConnectionStringBuilder) = value
        """
        ...

    @property
    def IntegratedSecurity(self) -> bool:
        """
        Get: IntegratedSecurity(self: OracleConnectionStringBuilder) -> bool
        Set: IntegratedSecurity(self: OracleConnectionStringBuilder) = value
        """
        ...

    @property
    def LoadBalanceTimeout(self) -> int:
        """
        Get: LoadBalanceTimeout(self: OracleConnectionStringBuilder) -> int
        Set: LoadBalanceTimeout(self: OracleConnectionStringBuilder) = value
        """
        ...

    @property
    def MaxPoolSize(self) -> int:
        """
        Get: MaxPoolSize(self: OracleConnectionStringBuilder) -> int
        Set: MaxPoolSize(self: OracleConnectionStringBuilder) = value
        """
        ...

    @property
    def MinPoolSize(self) -> int:
        """
        Get: MinPoolSize(self: OracleConnectionStringBuilder) -> int
        Set: MinPoolSize(self: OracleConnectionStringBuilder) = value
        """
        ...

    @property
    def OmitOracleConnectionName(self) -> bool:
        """
        Get: OmitOracleConnectionName(self: OracleConnectionStringBuilder) -> bool
        Set: OmitOracleConnectionName(self: OracleConnectionStringBuilder) = value
        """
        ...

    @property
    def Password(self) -> str:
        """
        Get: Password(self: OracleConnectionStringBuilder) -> str
        Set: Password(self: OracleConnectionStringBuilder) = value
        """
        ...

    @property
    def PersistSecurityInfo(self) -> bool:
        """
        Get: PersistSecurityInfo(self: OracleConnectionStringBuilder) -> bool
        Set: PersistSecurityInfo(self: OracleConnectionStringBuilder) = value
        """
        ...

    @property
    def Pooling(self) -> bool:
        """
        Get: Pooling(self: OracleConnectionStringBuilder) -> bool
        Set: Pooling(self: OracleConnectionStringBuilder) = value
        """
        ...

    @property
    def Unicode(self) -> bool:
        """
        Get: Unicode(self: OracleConnectionStringBuilder) -> bool
        Set: Unicode(self: OracleConnectionStringBuilder) = value
        """
        ...

    @property
    def UserID(self) -> str:
        """
        Get: UserID(self: OracleConnectionStringBuilder) -> str
        Set: UserID(self: OracleConnectionStringBuilder) = value
        """
        ...



class OracleDataAdapter(DbDataAdapter): # skipped bases: <type 'IDisposable'>, <type 'ICloneable'>, <type 'IDbDataAdapter'>, <type 'IComponent'>, <type 'IDataAdapter'>, <type 'object'>
    """
    OracleDataAdapter()
    OracleDataAdapter(selectCommand: OracleCommand)
    OracleDataAdapter(selectCommandText: str, selectConnectionString: str)
    OracleDataAdapter(selectCommandText: str, selectConnection: OracleConnection)
    """
    RowUpdated = None
    RowUpdating = None


class OracleDataReader(DbDataReader): # skipped bases: <type 'IDisposable'>, <type 'IDataReader'>, <type 'IDataRecord'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetOracleBFile(self, i:int) -> OracleBFile:
        """ GetOracleBFile(self: OracleDataReader, i: int) -> OracleBFile """
        ...

    def GetOracleBinary(self, i:int) -> OracleBinary:
        """ GetOracleBinary(self: OracleDataReader, i: int) -> OracleBinary """
        ...

    def GetOracleDateTime(self, i:int) -> OracleDateTime:
        """ GetOracleDateTime(self: OracleDataReader, i: int) -> OracleDateTime """
        ...

    def GetOracleLob(self, i:int) -> OracleLob:
        """ GetOracleLob(self: OracleDataReader, i: int) -> OracleLob """
        ...

    def GetOracleMonthSpan(self, i:int) -> OracleMonthSpan:
        """ GetOracleMonthSpan(self: OracleDataReader, i: int) -> OracleMonthSpan """
        ...

    def GetOracleNumber(self, i:int) -> OracleNumber:
        """ GetOracleNumber(self: OracleDataReader, i: int) -> OracleNumber """
        ...

    def GetOracleString(self, i:int) -> OracleString:
        """ GetOracleString(self: OracleDataReader, i: int) -> OracleString """
        ...

    def GetOracleTimeSpan(self, i:int) -> OracleTimeSpan:
        """ GetOracleTimeSpan(self: OracleDataReader, i: int) -> OracleTimeSpan """
        ...

    def GetOracleValue(self, i:int) -> object:
        """ GetOracleValue(self: OracleDataReader, i: int) -> object """
        ...

    def GetOracleValues(self, values:Array) -> int:
        """ GetOracleValues(self: OracleDataReader, values: Array[object]) -> int """
        ...

    def GetTimeSpan(self, i:int) -> TimeSpan:
        """ GetTimeSpan(self: OracleDataReader, i: int) -> TimeSpan """
        ...


class OracleDateTime(IComparable, INullable): # skipped bases: <type 'object'>
    """
    OracleDateTime(dt: DateTime)
    OracleDateTime(ticks: Int64)
    OracleDateTime(year: int, month: int, day: int)
    OracleDateTime(year: int, month: int, day: int, calendar: Calendar)
    OracleDateTime(year: int, month: int, day: int, hour: int, minute: int, second: int)
    OracleDateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, calendar: Calendar)
    OracleDateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int)
    OracleDateTime(year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: Calendar)
    OracleDateTime(from: OracleDateTime)
    """
    @property
    def Day(self) -> int:
        """ Get: Day(self: OracleDateTime) -> int """
        ...

    @property
    def Hour(self) -> int:
        """ Get: Hour(self: OracleDateTime) -> int """
        ...

    @property
    def Millisecond(self) -> int:
        """ Get: Millisecond(self: OracleDateTime) -> int """
        ...

    @property
    def Minute(self) -> int:
        """ Get: Minute(self: OracleDateTime) -> int """
        ...

    @property
    def Month(self) -> int:
        """ Get: Month(self: OracleDateTime) -> int """
        ...

    @property
    def Second(self) -> int:
        """ Get: Second(self: OracleDateTime) -> int """
        ...

    @property
    def Value(self) -> DateTime:
        """ Get: Value(self: OracleDateTime) -> DateTime """
        ...

    @property
    def Year(self) -> int:
        """ Get: Year(self: OracleDateTime) -> int """
        ...


    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: OracleDateTime, value: object) -> bool
        Equals(x: OracleDateTime, y: OracleDateTime) -> OracleBoolean
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: OracleDateTime) -> int """
        ...

    @staticmethod
    def GreaterThan(x:OracleDateTime, y:OracleDateTime) -> OracleBoolean:
        """ GreaterThan(x: OracleDateTime, y: OracleDateTime) -> OracleBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:OracleDateTime, y:OracleDateTime) -> OracleBoolean:
        """ GreaterThanOrEqual(x: OracleDateTime, y: OracleDateTime) -> OracleBoolean """
        ...

    @staticmethod
    def LessThan(x:OracleDateTime, y:OracleDateTime) -> OracleBoolean:
        """ LessThan(x: OracleDateTime, y: OracleDateTime) -> OracleBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:OracleDateTime, y:OracleDateTime) -> OracleBoolean:
        """ LessThanOrEqual(x: OracleDateTime, y: OracleDateTime) -> OracleBoolean """
        ...

    @staticmethod
    def NotEquals(x:OracleDateTime, y:OracleDateTime) -> OracleBoolean:
        """ NotEquals(x: OracleDateTime, y: OracleDateTime) -> OracleBoolean """
        ...

    @staticmethod
    def Parse(s:str) -> OracleDateTime:
        """ Parse(s: str) -> OracleDateTime """
        ...

    def ToString(self) -> str:
        """ ToString(self: OracleDateTime) -> str """
        ...

    MaxValue = None
    MinValue = None
    Null = None


class OracleException(DbException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>, <type 'object'>
    """ no doc """
    @property
    def Code(self) -> int:
        """ Get: Code(self: OracleException) -> int """
        ...


    SerializeObjectState = None


class OracleInfoMessageEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Code(self) -> int:
        """ Get: Code(self: OracleInfoMessageEventArgs) -> int """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: OracleInfoMessageEventArgs) -> str """
        ...

    @property
    def Source(self) -> str:
        """ Get: Source(self: OracleInfoMessageEventArgs) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: OracleInfoMessageEventArgs) -> str """
        ...


class OracleInfoMessageEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>, <type 'object'>
    """ OracleInfoMessageEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:OracleInfoMessageEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: OracleInfoMessageEventHandler, sender: object, e: OracleInfoMessageEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult):
        """ EndInvoke(self: OracleInfoMessageEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:OracleInfoMessageEventArgs):
        """ Invoke(self: OracleInfoMessageEventHandler, sender: object, e: OracleInfoMessageEventArgs) """
        ...


class OracleLob(Stream, ICloneable, INullable): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def ChunkSize(self) -> int:
        """ Get: ChunkSize(self: OracleLob) -> int """
        ...

    @property
    def Connection(self) -> OracleConnection:
        """ Get: Connection(self: OracleLob) -> OracleConnection """
        ...

    @property
    def IsBatched(self) -> bool:
        """ Get: IsBatched(self: OracleLob) -> bool """
        ...

    @property
    def IsTemporary(self) -> bool:
        """ Get: IsTemporary(self: OracleLob) -> bool """
        ...

    @property
    def LobType(self) -> OracleType:
        """ Get: LobType(self: OracleLob) -> OracleType """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: OracleLob) -> object """
        ...


    def Append(self, source:OracleLob):
        """ Append(self: OracleLob, source: OracleLob) """
        ...

    def BeginBatch(self, mode=None):
        """ BeginBatch(self: OracleLob)BeginBatch(self: OracleLob, mode: OracleLobOpenMode) """
        ...

    def EndBatch(self):
        """ EndBatch(self: OracleLob) """
        ...

    def Erase(self, offset=None, amount=None) -> Int64:
        """
        Erase(self: OracleLob) -> Int64
        Erase(self: OracleLob, offset: Int64, amount: Int64) -> Int64
        """
        ...

    Null = None


class OracleLobOpenMode(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """ enum OracleLobOpenMode, values: ReadOnly (1), ReadWrite (2) """
    ReadOnly = None
    ReadWrite = None
    value__ = None


class OracleMonthSpan(IComparable, INullable): # skipped bases: <type 'object'>
    """
    OracleMonthSpan(months: int)
    OracleMonthSpan(years: int, months: int)
    OracleMonthSpan(from: OracleMonthSpan)
    """
    @property
    def Value(self) -> int:
        """ Get: Value(self: OracleMonthSpan) -> int """
        ...


    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: OracleMonthSpan, value: object) -> bool
        Equals(x: OracleMonthSpan, y: OracleMonthSpan) -> OracleBoolean
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: OracleMonthSpan) -> int """
        ...

    @staticmethod
    def GreaterThan(x:OracleMonthSpan, y:OracleMonthSpan) -> OracleBoolean:
        """ GreaterThan(x: OracleMonthSpan, y: OracleMonthSpan) -> OracleBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:OracleMonthSpan, y:OracleMonthSpan) -> OracleBoolean:
        """ GreaterThanOrEqual(x: OracleMonthSpan, y: OracleMonthSpan) -> OracleBoolean """
        ...

    @staticmethod
    def LessThan(x:OracleMonthSpan, y:OracleMonthSpan) -> OracleBoolean:
        """ LessThan(x: OracleMonthSpan, y: OracleMonthSpan) -> OracleBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:OracleMonthSpan, y:OracleMonthSpan) -> OracleBoolean:
        """ LessThanOrEqual(x: OracleMonthSpan, y: OracleMonthSpan) -> OracleBoolean """
        ...

    @staticmethod
    def NotEquals(x:OracleMonthSpan, y:OracleMonthSpan) -> OracleBoolean:
        """ NotEquals(x: OracleMonthSpan, y: OracleMonthSpan) -> OracleBoolean """
        ...

    @staticmethod
    def Parse(s:str) -> OracleMonthSpan:
        """ Parse(s: str) -> OracleMonthSpan """
        ...

    def ToString(self) -> str:
        """ ToString(self: OracleMonthSpan) -> str """
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: OracleMonthSpan) -> int """
        ...

    def __long__(self, *args): #cannot find CLR method
        """ __int__(x: OracleMonthSpan) -> int """
        ...

    MaxValue = None
    MinValue = None
    Null = None


class OracleNumber(IComparable, INullable): # skipped bases: <type 'object'>
    """
    OracleNumber(decValue: Decimal)
    OracleNumber(dblValue: float)
    OracleNumber(intValue: int)
    OracleNumber(longValue: Int64)
    OracleNumber(from: OracleNumber)
    """
    @property
    def Value(self) -> Decimal:
        """ Get: Value(self: OracleNumber) -> Decimal """
        ...


    @staticmethod
    def Abs(n:OracleNumber) -> OracleNumber:
        """ Abs(n: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Acos(n:OracleNumber) -> OracleNumber:
        """ Acos(n: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Add(x:OracleNumber, y:OracleNumber) -> OracleNumber:
        """ Add(x: OracleNumber, y: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Asin(n:OracleNumber) -> OracleNumber:
        """ Asin(n: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Atan(n:OracleNumber) -> OracleNumber:
        """ Atan(n: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Atan2(y:OracleNumber, x:OracleNumber) -> OracleNumber:
        """ Atan2(y: OracleNumber, x: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Ceiling(n:OracleNumber) -> OracleNumber:
        """ Ceiling(n: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Cos(n:OracleNumber) -> OracleNumber:
        """ Cos(n: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Cosh(n:OracleNumber) -> OracleNumber:
        """ Cosh(n: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Divide(x:OracleNumber, y:OracleNumber) -> OracleNumber:
        """ Divide(x: OracleNumber, y: OracleNumber) -> OracleNumber """
        ...

    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: OracleNumber, value: object) -> bool
        Equals(x: OracleNumber, y: OracleNumber) -> OracleBoolean
        """
        ...

    @staticmethod
    def Exp(p:OracleNumber) -> OracleNumber:
        """ Exp(p: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Floor(n:OracleNumber) -> OracleNumber:
        """ Floor(n: OracleNumber) -> OracleNumber """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: OracleNumber) -> int """
        ...

    @staticmethod
    def GreaterThan(x:OracleNumber, y:OracleNumber) -> OracleBoolean:
        """ GreaterThan(x: OracleNumber, y: OracleNumber) -> OracleBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:OracleNumber, y:OracleNumber) -> OracleBoolean:
        """ GreaterThanOrEqual(x: OracleNumber, y: OracleNumber) -> OracleBoolean """
        ...

    @staticmethod
    def LessThan(x:OracleNumber, y:OracleNumber) -> OracleBoolean:
        """ LessThan(x: OracleNumber, y: OracleNumber) -> OracleBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:OracleNumber, y:OracleNumber) -> OracleBoolean:
        """ LessThanOrEqual(x: OracleNumber, y: OracleNumber) -> OracleBoolean """
        ...

    @staticmethod
    def Log(n, newBase=None) -> OracleNumber:
        """
        Log(n: OracleNumber) -> OracleNumber
        Log(n: OracleNumber, newBase: int) -> OracleNumber
        Log(n: OracleNumber, newBase: OracleNumber) -> OracleNumber
        """
        ...

    @staticmethod
    def Log10(n:OracleNumber) -> OracleNumber:
        """ Log10(n: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Max(x:OracleNumber, y:OracleNumber) -> OracleNumber:
        """ Max(x: OracleNumber, y: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Min(x:OracleNumber, y:OracleNumber) -> OracleNumber:
        """ Min(x: OracleNumber, y: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Modulo(x:OracleNumber, y:OracleNumber) -> OracleNumber:
        """ Modulo(x: OracleNumber, y: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Multiply(x:OracleNumber, y:OracleNumber) -> OracleNumber:
        """ Multiply(x: OracleNumber, y: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Negate(x:OracleNumber) -> OracleNumber:
        """ Negate(x: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def NotEquals(x:OracleNumber, y:OracleNumber) -> OracleBoolean:
        """ NotEquals(x: OracleNumber, y: OracleNumber) -> OracleBoolean """
        ...

    @staticmethod
    def Parse(s:str) -> OracleNumber:
        """ Parse(s: str) -> OracleNumber """
        ...

    @staticmethod
    def Pow(x:OracleNumber, y:int) -> OracleNumber:
        """
        Pow(x: OracleNumber, y: int) -> OracleNumber
        Pow(x: OracleNumber, y: OracleNumber) -> OracleNumber
        """
        ...

    @staticmethod
    def Round(n:OracleNumber, position:int) -> OracleNumber:
        """ Round(n: OracleNumber, position: int) -> OracleNumber """
        ...

    @staticmethod
    def Shift(n:OracleNumber, digits:int) -> OracleNumber:
        """ Shift(n: OracleNumber, digits: int) -> OracleNumber """
        ...

    @staticmethod
    def Sign(n:OracleNumber) -> OracleNumber:
        """ Sign(n: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Sin(n:OracleNumber) -> OracleNumber:
        """ Sin(n: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Sinh(n:OracleNumber) -> OracleNumber:
        """ Sinh(n: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Sqrt(n:OracleNumber) -> OracleNumber:
        """ Sqrt(n: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Subtract(x:OracleNumber, y:OracleNumber) -> OracleNumber:
        """ Subtract(x: OracleNumber, y: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Tan(n:OracleNumber) -> OracleNumber:
        """ Tan(n: OracleNumber) -> OracleNumber """
        ...

    @staticmethod
    def Tanh(n:OracleNumber) -> OracleNumber:
        """ Tanh(n: OracleNumber) -> OracleNumber """
        ...

    def ToString(self) -> str:
        """ ToString(self: OracleNumber) -> str """
        ...

    @staticmethod
    def Truncate(n:OracleNumber, position:int) -> OracleNumber:
        """ Truncate(n: OracleNumber, position: int) -> OracleNumber """
        ...

    def __abs__(self, *args): #cannot find CLR method
        """ x.__abs__() <==> abs(x) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __complex__(self, *args): #cannot find CLR method
        """ __complex__(x: OracleNumber) -> float """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/y """
        ...

    def __float__(self, *args): #cannot find CLR method
        """ __complex__(x: OracleNumber) -> float """
        ...

    def __int__(self, *args): #cannot find CLR method
        """ __int__(x: OracleNumber) -> int """
        ...

    def __long__(self, *args): #cannot find CLR method
        """ __int__(x: OracleNumber) -> int """
        ...

    def __mod__(self, *args): #cannot find CLR method
        """ x.__mod__(y) <==> x%y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: OracleNumber, y: OracleNumber) -> OracleNumber """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """ __rdiv__(x: OracleNumber, y: OracleNumber) -> OracleNumber """
        ...

    def __rmod__(self, *args): #cannot find CLR method
        """ __rmod__(x: OracleNumber, y: OracleNumber) -> OracleNumber """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(x: OracleNumber, y: OracleNumber) -> OracleNumber """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(x: OracleNumber, y: OracleNumber) -> OracleNumber """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...

    E = None
    MaxPrecision = 38
    MaxScale = 127
    MaxValue = None
    MinScale = -84
    MinusOne = None
    MinValue = None
    Null = None
    One = None
    PI = None
    Zero = None


class OracleParameter(ICloneable, DbParameter): # skipped bases: <type 'IDbDataParameter'>, <type 'IDataParameter'>, <type 'object'>
    """
    OracleParameter()
    OracleParameter(name: str, value: object)
    OracleParameter(name: str, oracleType: OracleType)
    OracleParameter(name: str, oracleType: OracleType, size: int)
    OracleParameter(name: str, oracleType: OracleType, size: int, srcColumn: str)
    OracleParameter(name: str, oracleType: OracleType, size: int, direction: ParameterDirection, isNullable: bool, precision: Byte, scale: Byte, srcColumn: str, srcVersion: DataRowVersion, value: object)
    OracleParameter(name: str, oracleType: OracleType, size: int, direction: ParameterDirection, sourceColumn: str, sourceVersion: DataRowVersion, sourceColumnNullMapping: bool, value: object)
    """
    @property
    def Offset(self) -> int:
        """
        Get: Offset(self: OracleParameter) -> int
        Set: Offset(self: OracleParameter) = value
        """
        ...

    @property
    def OracleType(self) -> OracleType:
        """
        Get: OracleType(self: OracleParameter) -> OracleType
        Set: OracleType(self: OracleParameter) = value
        """
        ...


    def ResetOracleType(self):
        """ ResetOracleType(self: OracleParameter) """
        ...

    def ToString(self) -> str:
        """ ToString(self: OracleParameter) -> str """
        ...

    def __new__(cls, name=None, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str, value: object)
        __new__(cls: type, name: str, oracleType: OracleType)
        __new__(cls: type, name: str, oracleType: OracleType, size: int)
        __new__(cls: type, name: str, oracleType: OracleType, size: int, srcColumn: str)
        __new__(cls: type, name: str, oracleType: OracleType, size: int, direction: ParameterDirection, isNullable: bool, precision: Byte, scale: Byte, srcColumn: str, srcVersion: DataRowVersion, value: object)
        __new__(cls: type, name: str, oracleType: OracleType, size: int, direction: ParameterDirection, sourceColumn: str, sourceVersion: DataRowVersion, sourceColumnNullMapping: bool, value: object)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class OracleParameterCollection(DbParameterCollection): # skipped bases: <type 'IDataParameterCollection'>, <type 'IList'>, <type 'ICollection'>, <type 'IEnumerable'>, <type 'object'>
    """ OracleParameterCollection() """
    def AddWithValue(self, parameterName:str, value:object) -> OracleParameter:
        """ AddWithValue(self: OracleParameterCollection, parameterName: str, value: object) -> OracleParameter """
        ...


class OraclePermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'IStackWalk'>, <type 'ISecurityEncodable'>, <type 'object'>
    """ OraclePermission(state: PermissionState) """
    @property
    def AllowBlankPassword(self) -> bool:
        """
        Get: AllowBlankPassword(self: OraclePermission) -> bool
        Set: AllowBlankPassword(self: OraclePermission) = value
        """
        ...


    def Add(self, connectionString:str, restrictions:str, behavior:KeyRestrictionBehavior):
        """ Add(self: OraclePermission, connectionString: str, restrictions: str, behavior: KeyRestrictionBehavior) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __new__(cls, state:PermissionState) -> Self:
        """ __new__(cls: type, state: PermissionState) """
        ...


class OraclePermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ OraclePermissionAttribute(action: SecurityAction) """
    @property
    def AllowBlankPassword(self) -> bool:
        """
        Get: AllowBlankPassword(self: OraclePermissionAttribute) -> bool
        Set: AllowBlankPassword(self: OraclePermissionAttribute) = value
        """
        ...

    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: OraclePermissionAttribute) -> str
        Set: ConnectionString(self: OraclePermissionAttribute) = value
        """
        ...

    @property
    def KeyRestrictionBehavior(self) -> KeyRestrictionBehavior:
        """
        Get: KeyRestrictionBehavior(self: OraclePermissionAttribute) -> KeyRestrictionBehavior
        Set: KeyRestrictionBehavior(self: OraclePermissionAttribute) = value
        """
        ...

    @property
    def KeyRestrictions(self) -> str:
        """
        Get: KeyRestrictions(self: OraclePermissionAttribute) -> str
        Set: KeyRestrictions(self: OraclePermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: OraclePermissionAttribute) -> IPermission """
        ...

    def ShouldSerializeConnectionString(self) -> bool:
        """ ShouldSerializeConnectionString(self: OraclePermissionAttribute) -> bool """
        ...

    def ShouldSerializeKeyRestrictions(self) -> bool:
        """ ShouldSerializeKeyRestrictions(self: OraclePermissionAttribute) -> bool """
        ...


class OracleRowUpdatedEventArgs(RowUpdatedEventArgs): # skipped bases: <type 'object'>
    """ OracleRowUpdatedEventArgs(row: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping) """
    pass

class OracleRowUpdatedEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>, <type 'object'>
    """ OracleRowUpdatedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:OracleRowUpdatedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: OracleRowUpdatedEventHandler, sender: object, e: OracleRowUpdatedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult):
        """ EndInvoke(self: OracleRowUpdatedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:OracleRowUpdatedEventArgs):
        """ Invoke(self: OracleRowUpdatedEventHandler, sender: object, e: OracleRowUpdatedEventArgs) """
        ...


class OracleRowUpdatingEventArgs(RowUpdatingEventArgs): # skipped bases: <type 'object'>
    """ OracleRowUpdatingEventArgs(row: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping) """
    pass

class OracleRowUpdatingEventHandler(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>, <type 'object'>
    """ OracleRowUpdatingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:OracleRowUpdatingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: OracleRowUpdatingEventHandler, sender: object, e: OracleRowUpdatingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult):
        """ EndInvoke(self: OracleRowUpdatingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:OracleRowUpdatingEventArgs):
        """ Invoke(self: OracleRowUpdatingEventHandler, sender: object, e: OracleRowUpdatingEventArgs) """
        ...


class OracleString(IComparable, INullable): # skipped bases: <type 'object'>
    """ OracleString(s: str) """
    @property
    def Length(self) -> int:
        """ Get: Length(self: OracleString) -> int """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: OracleString) -> str """
        ...


    @staticmethod
    def Concat(x:OracleString, y:OracleString) -> OracleString:
        """ Concat(x: OracleString, y: OracleString) -> OracleString """
        ...

    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: OracleString, value: object) -> bool
        Equals(x: OracleString, y: OracleString) -> OracleBoolean
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: OracleString) -> int """
        ...

    @staticmethod
    def GreaterThan(x:OracleString, y:OracleString) -> OracleBoolean:
        """ GreaterThan(x: OracleString, y: OracleString) -> OracleBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:OracleString, y:OracleString) -> OracleBoolean:
        """ GreaterThanOrEqual(x: OracleString, y: OracleString) -> OracleBoolean """
        ...

    @staticmethod
    def LessThan(x:OracleString, y:OracleString) -> OracleBoolean:
        """ LessThan(x: OracleString, y: OracleString) -> OracleBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:OracleString, y:OracleString) -> OracleBoolean:
        """ LessThanOrEqual(x: OracleString, y: OracleString) -> OracleBoolean """
        ...

    @staticmethod
    def NotEquals(x:OracleString, y:OracleString) -> OracleBoolean:
        """ NotEquals(x: OracleString, y: OracleString) -> OracleBoolean """
        ...

    def ToString(self) -> str:
        """ ToString(self: OracleString) -> str """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(x: OracleString, y: OracleString) -> OracleString """
        ...

    Empty = None
    Null = None


class OracleTimeSpan(IComparable, INullable): # skipped bases: <type 'object'>
    """
    OracleTimeSpan(ts: TimeSpan)
    OracleTimeSpan(ticks: Int64)
    OracleTimeSpan(hours: int, minutes: int, seconds: int)
    OracleTimeSpan(days: int, hours: int, minutes: int, seconds: int)
    OracleTimeSpan(days: int, hours: int, minutes: int, seconds: int, milliseconds: int)
    OracleTimeSpan(from: OracleTimeSpan)
    """
    @property
    def Days(self) -> int:
        """ Get: Days(self: OracleTimeSpan) -> int """
        ...

    @property
    def Hours(self) -> int:
        """ Get: Hours(self: OracleTimeSpan) -> int """
        ...

    @property
    def Milliseconds(self) -> int:
        """ Get: Milliseconds(self: OracleTimeSpan) -> int """
        ...

    @property
    def Minutes(self) -> int:
        """ Get: Minutes(self: OracleTimeSpan) -> int """
        ...

    @property
    def Seconds(self) -> int:
        """ Get: Seconds(self: OracleTimeSpan) -> int """
        ...

    @property
    def Value(self) -> TimeSpan:
        """ Get: Value(self: OracleTimeSpan) -> TimeSpan """
        ...


    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: OracleTimeSpan, value: object) -> bool
        Equals(x: OracleTimeSpan, y: OracleTimeSpan) -> OracleBoolean
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: OracleTimeSpan) -> int """
        ...

    @staticmethod
    def GreaterThan(x:OracleTimeSpan, y:OracleTimeSpan) -> OracleBoolean:
        """ GreaterThan(x: OracleTimeSpan, y: OracleTimeSpan) -> OracleBoolean """
        ...

    @staticmethod
    def GreaterThanOrEqual(x:OracleTimeSpan, y:OracleTimeSpan) -> OracleBoolean:
        """ GreaterThanOrEqual(x: OracleTimeSpan, y: OracleTimeSpan) -> OracleBoolean """
        ...

    @staticmethod
    def LessThan(x:OracleTimeSpan, y:OracleTimeSpan) -> OracleBoolean:
        """ LessThan(x: OracleTimeSpan, y: OracleTimeSpan) -> OracleBoolean """
        ...

    @staticmethod
    def LessThanOrEqual(x:OracleTimeSpan, y:OracleTimeSpan) -> OracleBoolean:
        """ LessThanOrEqual(x: OracleTimeSpan, y: OracleTimeSpan) -> OracleBoolean """
        ...

    @staticmethod
    def NotEquals(x:OracleTimeSpan, y:OracleTimeSpan) -> OracleBoolean:
        """ NotEquals(x: OracleTimeSpan, y: OracleTimeSpan) -> OracleBoolean """
        ...

    @staticmethod
    def Parse(s:str) -> OracleTimeSpan:
        """ Parse(s: str) -> OracleTimeSpan """
        ...

    def ToString(self) -> str:
        """ ToString(self: OracleTimeSpan) -> str """
        ...

    MaxValue = None
    MinValue = None
    Null = None


class OracleTransaction(DbTransaction): # skipped bases: <type 'IDisposable'>, <type 'IDbTransaction'>, <type 'object'>
    """ no doc """
    pass

class OracleType(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """ enum OracleType, values: BFile (1), Blob (2), Byte (23), Char (3), Clob (4), Cursor (5), DateTime (6), Double (30), Float (29), Int16 (27), Int32 (28), IntervalDayToSecond (7), IntervalYearToMonth (8), LongRaw (9), LongVarChar (10), NChar (11), NClob (12), Number (13), NVarChar (14), Raw (15), RowId (16), SByte (26), Timestamp (18), TimestampLocal (19), TimestampWithTZ (20), UInt16 (24), UInt32 (25), VarChar (22) """
    BFile = None
    Blob = None
    Byte = None
    Char = None
    Clob = None
    Cursor = None
    DateTime = None
    Double = None
    Float = None
    Int16 = None
    Int32 = None
    IntervalDayToSecond = None
    IntervalYearToMonth = None
    LongRaw = None
    LongVarChar = None
    NChar = None
    NClob = None
    Number = None
    NVarChar = None
    Raw = None
    RowId = None
    SByte = None
    Timestamp = None
    TimestampLocal = None
    TimestampWithTZ = None
    UInt16 = None
    UInt32 = None
    value__ = None
    VarChar = None


