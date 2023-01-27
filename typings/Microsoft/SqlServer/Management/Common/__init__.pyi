# encoding: utf-8
# module Microsoft.SqlServer.Management.Common calls itself Common
# from Microsoft.SqlServer.ConnectionInfo, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, DateTime, DateTimeOffset, Enum, 
    EventArgs, IAsyncResult, IDisposable, Int64, IntPtr, MulticastDelegate, 
    SystemException, Type, Version)

from System.Collections import IComparer, SortedList

from System.Collections.Specialized import StringCollection

from System.Data import DataSet, IDbConnection

from System.Data.SqlClient import (SqlConnection, SqlConnectionStringBuilder, 
    SqlDataReader, SqlError)

from System.Data.SqlTypes import SqlBoolean

from System.Globalization import CultureInfo

from System.Reflection import Assembly

from System.Security import SecureString

from typing import Self

"""The following names are not found in the module: (AuthenticationMethod, 
    BoundEvent, field#)
"""

# no functions
# classes

class AutoDisconnectMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AutoDisconnectMode, values: DisconnectIfPooled (0), NoAutoDisconnect (1) """
    DisconnectIfPooled: AutoDisconnectMode = ...
    NoAutoDisconnect: AutoDisconnectMode = ...
    value__ = ...


class CapturedSql: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Text(self) -> StringCollection:
        """ Get: Text(self: CapturedSql) -> StringCollection """
        ...


    def Add(self, sqlStatement:str): # -> 
        """ Add(self: CapturedSql, sqlStatement: str) """
        ...

    def Clear(self): # -> 
        """ Clear(self: CapturedSql) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class ConnectionException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ConnectionException()
    ConnectionException(message: str)
    ConnectionException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ChangePasswordFailureException(ConnectionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ChangePasswordFailureException()
    ChangePasswordFailureException(message: str)
    ChangePasswordFailureException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ConnectionCannotBeChangedException(ConnectionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ConnectionCannotBeChangedException()
    ConnectionCannotBeChangedException(message: str)
    ConnectionCannotBeChangedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ConnectionFailureException(ConnectionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ConnectionFailureException()
    ConnectionFailureException(message: str)
    ConnectionFailureException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ConnectionInfoBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ServerCaseSensitivity(self) -> ServerCaseSensitivity:
        """
        Get: ServerCaseSensitivity(self: ConnectionInfoBase) -> ServerCaseSensitivity
        Set: ServerCaseSensitivity(self: ConnectionInfoBase) = value
        """
        ...

    @property
    def ServerType(self) -> ConnectionType:
        """ Get: ServerType(self: ConnectionInfoBase) -> ConnectionType """
        ...

    @property
    def ServerVersion(self) -> ServerVersion:
        """
        Get: ServerVersion(self: ConnectionInfoBase) -> ServerVersion
        Set: ServerVersion(self: ConnectionInfoBase) = value
        """
        ...


    def ConnectionParmsChanged(self, *args): #cannot find CLR method
        """ ConnectionParmsChanged(self: ConnectionInfoBase) """
        ...

    def ToString(self) -> str:
        """ ToString(self: ConnectionInfoBase) -> str """
        ...


class ConnectionInfoHelper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateSqlConnection(connectionInfo:SqlConnectionInfo) -> SqlConnection:
        """ CreateSqlConnection(connectionInfo: SqlConnectionInfo) -> SqlConnection """
        ...

    @staticmethod
    def GetTokenFromSqlConnection(conn:SqlConnection) -> str:
        """ GetTokenFromSqlConnection(conn: SqlConnection) -> str """
        ...

    @staticmethod
    def SetTokenOnConnection(conn:SqlConnection, accessToken:str): # -> 
        """ SetTokenOnConnection(conn: SqlConnection, accessToken: str) """
        ...

    __all__: list = ...


class ConnectionSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AccessToken(self) -> IRenewableToken:
        """
        Get: AccessToken(self: ConnectionSettings) -> IRenewableToken
        Set: AccessToken(self: ConnectionSettings) = value
        """
        ...

    @property
    def ApplicationIntent(self) -> str:
        """
        Get: ApplicationIntent(self: ConnectionSettings) -> str
        Set: ApplicationIntent(self: ConnectionSettings) = value
        """
        ...

    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: ConnectionSettings) -> str
        Set: ApplicationName(self: ConnectionSettings) = value
        """
        ...

    @property
    def Authentication(self): # -> AuthenticationMethod
        """
        Get: Authentication(self: ConnectionSettings) -> AuthenticationMethod
        Set: Authentication(self: ConnectionSettings) = value
        """
        ...

    @property
    def ConnectAsUser(self) -> bool:
        """
        Get: ConnectAsUser(self: ConnectionSettings) -> bool
        Set: ConnectAsUser(self: ConnectionSettings) = value
        """
        ...

    @property
    def ConnectAsUserName(self) -> str:
        """
        Get: ConnectAsUserName(self: ConnectionSettings) -> str
        Set: ConnectAsUserName(self: ConnectionSettings) = value
        """
        ...

    @property
    def ConnectAsUserPassword(self) -> str:
        """
        Get: ConnectAsUserPassword(self: ConnectionSettings) -> str
        Set: ConnectAsUserPassword(self: ConnectionSettings) = value
        """
        ...

    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: ConnectionSettings) -> str
        Set: ConnectionString(self: ConnectionSettings) = value
        """
        ...

    @property
    def ConnectTimeout(self) -> int:
        """
        Get: ConnectTimeout(self: ConnectionSettings) -> int
        Set: ConnectTimeout(self: ConnectionSettings) = value
        """
        ...

    @property
    def DatabaseName(self) -> str:
        """
        Get: DatabaseName(self: ConnectionSettings) -> str
        Set: DatabaseName(self: ConnectionSettings) = value
        """
        ...

    @property
    def EncryptConnection(self) -> bool:
        """
        Get: EncryptConnection(self: ConnectionSettings) -> bool
        Set: EncryptConnection(self: ConnectionSettings) = value
        """
        ...

    @property
    def Login(self) -> str:
        """
        Get: Login(self: ConnectionSettings) -> str
        Set: Login(self: ConnectionSettings) = value
        """
        ...

    @property
    def LoginSecure(self) -> bool:
        """
        Get: LoginSecure(self: ConnectionSettings) -> bool
        Set: LoginSecure(self: ConnectionSettings) = value
        """
        ...

    @property
    def MaxPoolSize(self) -> int:
        """
        Get: MaxPoolSize(self: ConnectionSettings) -> int
        Set: MaxPoolSize(self: ConnectionSettings) = value
        """
        ...

    @property
    def MinPoolSize(self) -> int:
        """
        Get: MinPoolSize(self: ConnectionSettings) -> int
        Set: MinPoolSize(self: ConnectionSettings) = value
        """
        ...

    @property
    def MultipleActiveResultSets(self) -> bool:
        """
        Get: MultipleActiveResultSets(self: ConnectionSettings) -> bool
        Set: MultipleActiveResultSets(self: ConnectionSettings) = value
        """
        ...

    @property
    def NetworkProtocol(self) -> NetworkProtocol:
        """
        Get: NetworkProtocol(self: ConnectionSettings) -> NetworkProtocol
        Set: NetworkProtocol(self: ConnectionSettings) = value
        """
        ...

    @property
    def NonPooledConnection(self) -> bool:
        """
        Get: NonPooledConnection(self: ConnectionSettings) -> bool
        Set: NonPooledConnection(self: ConnectionSettings) = value
        """
        ...

    @property
    def PacketSize(self) -> int:
        """
        Get: PacketSize(self: ConnectionSettings) -> int
        Set: PacketSize(self: ConnectionSettings) = value
        """
        ...

    @property
    def Password(self) -> str:
        """
        Get: Password(self: ConnectionSettings) -> str
        Set: Password(self: ConnectionSettings) = value
        """
        ...

    @property
    def PooledConnectionLifetime(self) -> int:
        """
        Get: PooledConnectionLifetime(self: ConnectionSettings) -> int
        Set: PooledConnectionLifetime(self: ConnectionSettings) = value
        """
        ...

    @property
    def ResetConnectionString(self):
        ...

    @property
    def SecureConnectionString(self) -> SecureString:
        """
        Get: SecureConnectionString(self: ConnectionSettings) -> SecureString
        Set: SecureConnectionString(self: ConnectionSettings) = value
        """
        ...

    @property
    def SecurePassword(self) -> SecureString:
        """
        Get: SecurePassword(self: ConnectionSettings) -> SecureString
        Set: SecurePassword(self: ConnectionSettings) = value
        """
        ...

    @property
    def ServerInstance(self) -> str:
        """
        Get: ServerInstance(self: ConnectionSettings) -> str
        Set: ServerInstance(self: ConnectionSettings) = value
        """
        ...

    @property
    def TrustServerCertificate(self) -> bool:
        """
        Get: TrustServerCertificate(self: ConnectionSettings) -> bool
        Set: TrustServerCertificate(self: ConnectionSettings) = value
        """
        ...

    @property
    def WorkstationId(self) -> str:
        """
        Get: WorkstationId(self: ConnectionSettings) -> str
        Set: WorkstationId(self: ConnectionSettings) = value
        """
        ...


    def ThrowIfPropertyNotSet(self, *args): #cannot find CLR method
        """
        ThrowIfPropertyNotSet(self: ConnectionSettings, propertyName: str, str: str) -> str
        ThrowIfPropertyNotSet(self: ConnectionSettings, propertyName: str, str: str, checkEmpty: bool) -> str
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: ConnectionSettings) -> str """
        ...

    NoConnectionTimeout: int = ...


class ConnectionManager(ConnectionSettings): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AutoDisconnectMode(self) -> AutoDisconnectMode:
        """
        Get: AutoDisconnectMode(self: ConnectionManager) -> AutoDisconnectMode
        Set: AutoDisconnectMode(self: ConnectionManager) = value
        """
        ...

    @property
    def CapturedSql(self) -> CapturedSql:
        """ Get: CapturedSql(self: ConnectionManager) -> CapturedSql """
        ...

    @property
    def DatabaseEngineEdition(self) -> DatabaseEngineEdition:
        """ Get: DatabaseEngineEdition(self: ConnectionManager) -> DatabaseEngineEdition """
        ...

    @property
    def DatabaseEngineType(self) -> DatabaseEngineType:
        """ Get: DatabaseEngineType(self: ConnectionManager) -> DatabaseEngineType """
        ...

    @property
    def HostPlatform(self) -> str:
        """ Get: HostPlatform(self: ConnectionManager) -> str """
        ...

    @property
    def InUse(self) -> bool:
        """
        Get: InUse(self: ConnectionManager) -> bool
        Set: InUse(self: ConnectionManager) = value
        """
        ...

    @property
    def IsForceDisconnected(self) -> bool:
        """ Get: IsForceDisconnected(self: ConnectionManager) -> bool """
        ...

    @property
    def IsOpen(self) -> bool:
        """ Get: IsOpen(self: ConnectionManager) -> bool """
        ...

    @property
    def LockTimeout(self) -> int:
        """
        Get: LockTimeout(self: ConnectionManager) -> int
        Set: LockTimeout(self: ConnectionManager) = value
        """
        ...

    @property
    def ServerVersion(self) -> ServerVersion:
        """
        Get: ServerVersion(self: ConnectionManager) -> ServerVersion
        Set: ServerVersion(self: ConnectionManager) = value
        """
        ...

    @property
    def SqlConnectionObject(self) -> SqlConnection:
        """ Get: SqlConnectionObject(self: ConnectionManager) -> SqlConnection """
        ...


    def CheckServerVersion(self, *args): #cannot find CLR method
        """ CheckServerVersion(self: ConnectionManager, version: ServerVersion) """
        ...

    def Connect(self): # -> 
        """ Connect(self: ConnectionManager) """
        ...

    def Disconnect(self): # -> 
        """ Disconnect(self: ConnectionManager) """
        ...

    def ExecuteTSql(self, *args): #cannot find CLR method
        """ ExecuteTSql(self: ConnectionManager, action: ExecuteTSqlAction, execObject: object, fillDataSet: DataSet, catchException: bool) -> object """
        ...

    def ExecuteTSqlAction(self, *args): #cannot find CLR method
        """ enum ExecuteTSqlAction, values: ExecuteNonQuery (1), ExecuteReader (2), ExecuteScalar (3), FillDataSet (4), Unknown (0) """
        ...

    def ForceDisconnected(self): # -> 
        """ ForceDisconnected(self: ConnectionManager) """
        ...

    InfoMessage = ...
    RemoteLoginFailed = ...
    ServerMessage = ...
    StateChange = ...
    StatementExecuted = ...


class ConnectionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConnectionType, values: AzureAccount (8), AzureStorage (7), IntegrationServer (6), Olap (1), ReportServer (5), Sql (0), SqlCE (4), SqlConnection (2), WmiManagementScope (3) """
    AzureAccount: ConnectionType = ...
    AzureStorage: ConnectionType = ...
    IntegrationServer: ConnectionType = ...
    Olap: ConnectionType = ...
    ReportServer: ConnectionType = ...
    Sql: ConnectionType = ...
    SqlCE: ConnectionType = ...
    SqlConnection: ConnectionType = ...
    value__ = ...
    WmiManagementScope: ConnectionType = ...


class DatabaseEngineEdition(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DatabaseEngineEdition, values: Enterprise (3), Express (4), Personal (1), SqlDatabase (5), SqlDataWarehouse (6), SqlStretchDatabase (7), Standard (2), Unknown (0) """
    Enterprise: DatabaseEngineEdition = ...
    Express: DatabaseEngineEdition = ...
    Personal: DatabaseEngineEdition = ...
    SqlDatabase: DatabaseEngineEdition = ...
    SqlDataWarehouse: DatabaseEngineEdition = ...
    SqlStretchDatabase: DatabaseEngineEdition = ...
    Standard: DatabaseEngineEdition = ...
    Unknown: DatabaseEngineEdition = ...
    value__ = ...


class DatabaseEngineType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DatabaseEngineType, values: SqlAzureDatabase (2), Standalone (1), Unknown (0) """
    SqlAzureDatabase: DatabaseEngineType = ...
    Standalone: DatabaseEngineType = ...
    Unknown: DatabaseEngineType = ...
    value__ = ...


class DataTransferEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DataTransferEventArgs(eventType: DataTransferEventType, message: str) """
    @property
    def DataTransferEventType(self) -> DataTransferEventType:
        """ Get: DataTransferEventType(self: DataTransferEventArgs) -> DataTransferEventType """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: DataTransferEventArgs) -> str """
        ...


    def __new__(cls, eventType:DataTransferEventType, message:str) -> Self:
        """ __new__(cls: type, eventType: DataTransferEventType, message: str) """
        ...


class DataTransferEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataTransferEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DataTransferEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataTransferEventHandler, sender: object, e: DataTransferEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DataTransferEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DataTransferEventArgs): # -> 
        """ Invoke(self: DataTransferEventHandler, sender: object, e: DataTransferEventArgs) """
        ...


class DataTransferEventType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataTransferEventType, values: Information (1), Progress (0), Warning (2) """
    Information: DataTransferEventType = ...
    Progress: DataTransferEventType = ...
    value__ = ...
    Warning: DataTransferEventType = ...


class DataTransferProgressEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DataTransferProgressEventArgs(eventType: DataTransferProgressEventType, transferId: str, progressCount: Int64, ex: Exception) """
    @property
    def DataTransferProgressEventType(self) -> DataTransferProgressEventType:
        """ Get: DataTransferProgressEventType(self: DataTransferProgressEventArgs) -> DataTransferProgressEventType """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: DataTransferProgressEventArgs) -> Exception """
        ...

    @property
    def ProgressCount(self) -> Int64:
        """ Get: ProgressCount(self: DataTransferProgressEventArgs) -> Int64 """
        ...

    @property
    def TransferId(self) -> str:
        """ Get: TransferId(self: DataTransferProgressEventArgs) -> str """
        ...


    def __new__(cls, eventType:DataTransferProgressEventType, transferId:str, progressCount:Int64, ex:Exception) -> Self:
        """ __new__(cls: type, eventType: DataTransferProgressEventType, transferId: str, progressCount: Int64, ex: Exception) """
        ...


class DataTransferProgressEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataTransferProgressEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DataTransferProgressEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataTransferProgressEventHandler, sender: object, e: DataTransferProgressEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: DataTransferProgressEventHandler, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, sender:object, e:DataTransferProgressEventArgs) -> bool:
        """ Invoke(self: DataTransferProgressEventHandler, sender: object, e: DataTransferProgressEventArgs) -> bool """
        ...


class DataTransferProgressEventType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataTransferProgressEventType, values: AllowedToFailPrologueSql (2), CancelQuery (11), CommitTransaction (8), Error (12), ExecuteCompensatingSql (10), ExecuteEpilogueSql (7), ExecuteNonTransactableSql (0), ExecutePrologueSql (3), ExecutingDataFlow (5), GenerateDataFlow (4), RollbackTransaction (9), StartTransaction (1), TransferringRows (6) """
    AllowedToFailPrologueSql: DataTransferProgressEventType = ...
    CancelQuery: DataTransferProgressEventType = ...
    CommitTransaction: DataTransferProgressEventType = ...
    Error: DataTransferProgressEventType = ...
    ExecuteCompensatingSql: DataTransferProgressEventType = ...
    ExecuteEpilogueSql: DataTransferProgressEventType = ...
    ExecuteNonTransactableSql: DataTransferProgressEventType = ...
    ExecutePrologueSql: DataTransferProgressEventType = ...
    ExecutingDataFlow: DataTransferProgressEventType = ...
    GenerateDataFlow: DataTransferProgressEventType = ...
    RollbackTransaction: DataTransferProgressEventType = ...
    StartTransaction: DataTransferProgressEventType = ...
    TransferringRows: DataTransferProgressEventType = ...
    value__ = ...


class DeferredUseMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DeferredUseMode, values: CollapseRedundant (1), MergeSql (2), None (0) """
    CollapseRedundant: DeferredUseMode = ...
    MergeSql: DeferredUseMode = ...
    value__ = ...


class DisconnectedConnectionException(ConnectionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DisconnectedConnectionException()
    DisconnectedConnectionException(message: str)
    DisconnectedConnectionException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ExecutionFailureException(ConnectionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ExecutionFailureException()
    ExecutionFailureException(message: str)
    ExecutionFailureException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ExecutionTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ExecutionTypes, values: ContinueOnError (2), Default (0), NoCommands (1), NoExec (4), ParseOnly (8), QuotedIdentifierOn (16) """
    ContinueOnError: ExecutionTypes = ...
    Default: ExecutionTypes = ...
    NoCommands: ExecutionTypes = ...
    NoExec: ExecutionTypes = ...
    ParseOnly: ExecutionTypes = ...
    QuotedIdentifierOn: ExecutionTypes = ...
    value__ = ...


class FixedServerRoles(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) FixedServerRoles, values: BulkAdmin (128), DBCreator (32), DiskAdmin (64), None (0), ProcessAdmin (16), SecurityAdmin (8), ServerAdmin (2), SetupAdmin (4), SysAdmin (1) """
    BulkAdmin: FixedServerRoles = ...
    DBCreator: FixedServerRoles = ...
    DiskAdmin: FixedServerRoles = ...
    ProcessAdmin: FixedServerRoles = ...
    SecurityAdmin: FixedServerRoles = ...
    ServerAdmin: FixedServerRoles = ...
    SetupAdmin: FixedServerRoles = ...
    SysAdmin: FixedServerRoles = ...
    value__ = ...


class HostPlatformNames: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Linux: str = ...
    Windows: str = ...
    __all__: list = ...


class IAlterable: # skipped bases: <type 'object'>
    """ no doc """
    def Alter(self): # -> 
        """ Alter(self: IAlterable) """
        ...


class ICreatable: # skipped bases: <type 'object'>
    """ no doc """
    def Create(self): # -> 
        """ Create(self: ICreatable) """
        ...


class ICreateOrAlterable: # skipped bases: <type 'object'>
    """ no doc """
    def CreateOrAlter(self): # -> 
        """ CreateOrAlter(self: ICreateOrAlterable) """
        ...


class IDataTransferProvider: # skipped bases: <type 'object'>
    """ no doc """
    def Configure(self, metadataProvider:ITransferMetadataProvider): # -> 
        """ Configure(self: IDataTransferProvider, metadataProvider: ITransferMetadataProvider) """
        ...

    def ExecuteTransfer(self): # -> 
        """ ExecuteTransfer(self: IDataTransferProvider) """
        ...

    TransferEvent = ...


class IDropIfExists: # skipped bases: <type 'object'>
    """ no doc """
    def DropIfExists(self): # -> 
        """ DropIfExists(self: IDropIfExists) """
        ...


class IDroppable: # skipped bases: <type 'object'>
    """ no doc """
    def Drop(self): # -> 
        """ Drop(self: IDroppable) """
        ...


class IMarkForDrop: # skipped bases: <type 'object'>
    """ no doc """
    def MarkForDrop(self, dropOnAlter:bool): # -> 
        """ MarkForDrop(self: IMarkForDrop, dropOnAlter: bool) """
        ...


class InvalidArgumentException(ConnectionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidArgumentException()
    InvalidArgumentException(message: str)
    InvalidArgumentException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InvalidPropertyValueException(ConnectionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidPropertyValueException()
    InvalidPropertyValueException(message: str)
    InvalidPropertyValueException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class IRefreshable: # skipped bases: <type 'object'>
    """ no doc """
    def Refresh(self): # -> 
        """ Refresh(self: IRefreshable) """
        ...


class IRenamable: # skipped bases: <type 'object'>
    """ no doc """
    def Rename(self, newname:str): # -> 
        """ Rename(self: IRenamable, newname: str) """
        ...


class IRenewableToken: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Resource(self) -> str:
        """ Get: Resource(self: IRenewableToken) -> str """
        ...

    @property
    def Tenant(self) -> str:
        """ Get: Tenant(self: IRenewableToken) -> str """
        ...

    @property
    def TokenExpiry(self) -> DateTimeOffset:
        """ Get: TokenExpiry(self: IRenewableToken) -> DateTimeOffset """
        ...

    @property
    def UserId(self) -> str:
        """ Get: UserId(self: IRenewableToken) -> str """
        ...


    def GetAccessToken(self) -> str:
        """ GetAccessToken(self: IRenewableToken) -> str """
        ...


class IRestrictedAccess: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SingleConnection(self) -> bool:
        """
        Get: SingleConnection(self: IRestrictedAccess) -> bool
        Set: SingleConnection(self: IRestrictedAccess) = value
        """
        ...



class ISafeRenamable(IRenamable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def WarnOnRename(self) -> bool:
        """ Get: WarnOnRename(self: ISafeRenamable) -> bool """
        ...



class ISfcConnection: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsForceDisconnected(self) -> bool:
        """ Get: IsForceDisconnected(self: ISfcConnection) -> bool """
        ...

    @property
    def IsOpen(self) -> bool:
        """ Get: IsOpen(self: ISfcConnection) -> bool """
        ...

    @property
    def ServerInstance(self) -> str:
        """
        Get: ServerInstance(self: ISfcConnection) -> str
        Set: ServerInstance(self: ISfcConnection) = value
        """
        ...

    @property
    def ServerVersion(self) -> Version:
        """ Get: ServerVersion(self: ISfcConnection) -> Version """
        ...


    def Connect(self) -> bool:
        """ Connect(self: ISfcConnection) -> bool """
        ...

    def Copy(self) -> ISfcConnection:
        """ Copy(self: ISfcConnection) -> ISfcConnection """
        ...

    def Disconnect(self) -> bool:
        """ Disconnect(self: ISfcConnection) -> bool """
        ...

    def ForceDisconnected(self): # -> 
        """ ForceDisconnected(self: ISfcConnection) """
        ...

    def ToEnumeratorObject(self) -> object:
        """ ToEnumeratorObject(self: ISfcConnection) -> object """
        ...


class ITransferMetadataProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetOptions(self) -> SortedList:
        """ GetOptions(self: ITransferMetadataProvider) -> SortedList """
        ...

    def SaveMetadata(self): # -> 
        """ SaveMetadata(self: ITransferMetadataProvider) """
        ...


class NetCoreHelpers: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ConvertSecureStringToBSTR(ss:SecureString) -> IntPtr:
        """ ConvertSecureStringToBSTR(ss: SecureString) -> IntPtr """
        ...

    @staticmethod
    def GetAssembly(type:Type) -> Assembly:
        """ GetAssembly(type: Type) -> Assembly """
        ...

    @staticmethod
    def GetNewCultureInfo(lcid:int) -> CultureInfo:
        """ GetNewCultureInfo(lcid: int) -> CultureInfo """
        ...

    @staticmethod
    def LoadAssembly(assemblyName:str) -> Assembly:
        """ LoadAssembly(assemblyName: str) -> Assembly """
        ...

    @staticmethod
    def StringCompare(firstString:str, secondString:str, ignoreCase:bool, culture:CultureInfo) -> int:
        """ StringCompare(firstString: str, secondString: str, ignoreCase: bool, culture: CultureInfo) -> int """
        ...

    @staticmethod
    def StringToUpper(str:str, culture:CultureInfo) -> str:
        """ StringToUpper(str: str, culture: CultureInfo) -> str """
        ...

    @staticmethod
    def ZeroFreeBSTR(ps:IntPtr): # -> 
        """ ZeroFreeBSTR(ps: IntPtr) """
        ...

    __all__: list = ...


class NetworkProtocol(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NetworkProtocol, values: AppleTalk (3), BanyanVines (4), Multiprotocol (2), NamedPipes (1), NotSpecified (8), NWLinkIpxSpx (7), SharedMemory (6), TcpIp (0), Via (5) """
    AppleTalk: NetworkProtocol = ...
    BanyanVines: NetworkProtocol = ...
    Multiprotocol: NetworkProtocol = ...
    NamedPipes: NetworkProtocol = ...
    NotSpecified: NetworkProtocol = ...
    NWLinkIpxSpx: NetworkProtocol = ...
    SharedMemory: NetworkProtocol = ...
    TcpIp: NetworkProtocol = ...
    value__ = ...
    Via: NetworkProtocol = ...


class NotInTransactionException(ConnectionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    NotInTransactionException()
    NotInTransactionException(message: str)
    NotInTransactionException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SqlOlapConnectionInfoBase(ConnectionInfoBase): # skipped bases: <type 'object'>
    """ SqlOlapConnectionInfoBase(serverName: str, userName: str, password: str, serverType: ConnectionType) """
    @property
    def ConnectionString(self) -> str:
        """ Get: ConnectionString(self: SqlOlapConnectionInfoBase) -> str """
        ...

    @property
    def ConnectionStringInternal(self):
        ...

    @property
    def ConnectionTimeout(self) -> int:
        """
        Get: ConnectionTimeout(self: SqlOlapConnectionInfoBase) -> int
        Set: ConnectionTimeout(self: SqlOlapConnectionInfoBase) = value
        """
        ...

    @property
    def ConnectionTimeoutInternal(self):
        ...

    @property
    def DatabaseName(self) -> str:
        """
        Get: DatabaseName(self: SqlOlapConnectionInfoBase) -> str
        Set: DatabaseName(self: SqlOlapConnectionInfoBase) = value
        """
        ...

    @property
    def DatabaseNameInternal(self):
        ...

    @property
    def IntegratedSecurityInternal(self):
        ...

    @property
    def Password(self) -> str:
        """
        Get: Password(self: SqlOlapConnectionInfoBase) -> str
        Set: Password(self: SqlOlapConnectionInfoBase) = value
        """
        ...

    @property
    def QueryTimeout(self) -> int:
        """
        Get: QueryTimeout(self: SqlOlapConnectionInfoBase) -> int
        Set: QueryTimeout(self: SqlOlapConnectionInfoBase) = value
        """
        ...

    @property
    def QueryTimeoutInternal(self):
        ...

    @property
    def RebuildConnectionStringInternal(self):
        ...

    @property
    def SecurePassword(self) -> SecureString:
        """
        Get: SecurePassword(self: SqlOlapConnectionInfoBase) -> SecureString
        Set: SecurePassword(self: SqlOlapConnectionInfoBase) = value
        """
        ...

    @property
    def ServerName(self) -> str:
        """
        Get: ServerName(self: SqlOlapConnectionInfoBase) -> str
        Set: ServerName(self: SqlOlapConnectionInfoBase) = value
        """
        ...

    @property
    def ServerNameInternal(self):
        ...

    @property
    def UseIntegratedSecurity(self) -> bool:
        """
        Get: UseIntegratedSecurity(self: SqlOlapConnectionInfoBase) -> bool
        Set: UseIntegratedSecurity(self: SqlOlapConnectionInfoBase) = value
        """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: SqlOlapConnectionInfoBase) -> str
        Set: UserName(self: SqlOlapConnectionInfoBase) = value
        """
        ...


    def CreateConnectionObject(self) -> IDbConnection:
        """ CreateConnectionObject(self: SqlOlapConnectionInfoBase) -> IDbConnection """
        ...

    DefaultConnTimeout: int = ...
    DefaultQueryTimeout: int = ...
    NoTimeOut: int = ...


class OlapConnectionInfo(SqlOlapConnectionInfoBase): # skipped bases: <type 'object'>
    """
    OlapConnectionInfo()
    OlapConnectionInfo(conn: OlapConnectionInfo)
    """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: OlapConnectionInfo) -> str
        Set: ApplicationName(self: OlapConnectionInfo) = value
        """
        ...

    @property
    def EncryptConnection(self) -> bool:
        """
        Get: EncryptConnection(self: OlapConnectionInfo) -> bool
        Set: EncryptConnection(self: OlapConnectionInfo) = value
        """
        ...

    @property
    def IntegratedSecurity(self) -> str:
        """
        Get: IntegratedSecurity(self: OlapConnectionInfo) -> str
        Set: IntegratedSecurity(self: OlapConnectionInfo) = value
        """
        ...

    @property
    def OtherParameters(self) -> str:
        """
        Get: OtherParameters(self: OlapConnectionInfo) -> str
        Set: OtherParameters(self: OlapConnectionInfo) = value
        """
        ...


    def Copy(self) -> OlapConnectionInfo:
        """ Copy(self: OlapConnectionInfo) -> OlapConnectionInfo """
        ...


class PropertyNotAvailableException(ConnectionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PropertyNotAvailableException()
    PropertyNotAvailableException(message: str)
    PropertyNotAvailableException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class PropertyNotSetException(ConnectionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PropertyNotSetException()
    PropertyNotSetException(message: str)
    PropertyNotSetException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class QueryParameterizationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum QueryParameterizationMode, values: ForcedParameterization (1), None (0), ParameterizeLiterals (2) """
    ForcedParameterization: QueryParameterizationMode = ...
    ParameterizeLiterals: QueryParameterizationMode = ...
    value__ = ...


class ServerCaseSensitivity(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ServerCaseSensitivity, values: CaseInsensitive (2), CaseSensitive (1), Unknown (0) """
    CaseInsensitive: ServerCaseSensitivity = ...
    CaseSensitive: ServerCaseSensitivity = ...
    Unknown: ServerCaseSensitivity = ...
    value__ = ...


class ServerComparer(IComparer): # skipped bases: <type 'object'>
    """
    ServerComparer(conn: ServerConnection)
    ServerComparer(conn: ServerConnection, databaseName: str)
    """
    pass

class ServerConnection(ConnectionManager, ISfcConnection): # skipped bases: <type 'object'>
    """
    ServerConnection()
    ServerConnection(token: IRenewableToken)
    ServerConnection(sci: SqlConnectionInfo)
    ServerConnection(sqlConnection: SqlConnection)
    ServerConnection(sqlConnection: SqlConnection, accessToken: IRenewableToken)
    ServerConnection(serverInstance: str)
    ServerConnection(serverInstance: str, userName: str, password: str)
    ServerConnection(serverInstance: str, userName: str, password: SecureString)
    """
    @property
    def BatchSeparator(self) -> str:
        """
        Get: BatchSeparator(self: ServerConnection) -> str
        Set: BatchSeparator(self: ServerConnection) = value
        """
        ...

    @property
    def ConnectionType(self) -> ServerType:
        """ Get: ConnectionType(self: ServerConnection) -> ServerType """
        ...

    @property
    def FixedServerRoles(self) -> FixedServerRoles:
        """ Get: FixedServerRoles(self: ServerConnection) -> FixedServerRoles """
        ...

    @property
    def ParameterizationMode(self) -> QueryParameterizationMode:
        """
        Get: ParameterizationMode() -> QueryParameterizationMode
        Set: ParameterizationMode() = value
        """
        ...

    @property
    def ProcessID(self) -> int:
        """ Get: ProcessID(self: ServerConnection) -> int """
        ...

    @property
    def SqlExecutionModes(self) -> SqlExecutionModes:
        """
        Get: SqlExecutionModes(self: ServerConnection) -> SqlExecutionModes
        Set: SqlExecutionModes(self: ServerConnection) = value
        """
        ...

    @property
    def StatementTimeout(self) -> int:
        """
        Get: StatementTimeout(self: ServerConnection) -> int
        Set: StatementTimeout(self: ServerConnection) = value
        """
        ...

    @property
    def TransactionDepth(self) -> int:
        """ Get: TransactionDepth(self: ServerConnection) -> int """
        ...

    @property
    def TrueLogin(self) -> str:
        """ Get: TrueLogin(self: ServerConnection) -> str """
        ...

    @property
    def TrueName(self) -> str:
        """
        Get: TrueName(self: ServerConnection) -> str
        Set: TrueName(self: ServerConnection) = value
        """
        ...

    @property
    def UseMode(self) -> DeferredUseMode:
        """
        Get: UseMode() -> DeferredUseMode
        Set: UseMode() = value
        """
        ...

    @property
    def UserProfile(self) -> ServerUserProfiles:
        """ Get: UserProfile(self: ServerConnection) -> ServerUserProfiles """
        ...


    def BeginTransaction(self): # -> 
        """ BeginTransaction(self: ServerConnection) """
        ...

    def Cancel(self): # -> 
        """ Cancel(self: ServerConnection) """
        ...

    def ChangePassword(self, newPassword:SecureString): # -> 
        """ ChangePassword(self: ServerConnection, newPassword: SecureString)ChangePassword(self: ServerConnection, newPassword: str) """
        ...

    def CommitTransaction(self): # -> 
        """ CommitTransaction(self: ServerConnection) """
        ...

    def ExecuteNonQuery(self, *__args:StringCollection) -> Array:
        """
        ExecuteNonQuery(self: ServerConnection, sqlCommands: StringCollection) -> Array[int]
        ExecuteNonQuery(self: ServerConnection, sqlCommands: StringCollection, executionType: ExecutionTypes) -> Array[int]
        ExecuteNonQuery(self: ServerConnection, sqlCommand: str) -> int
        ExecuteNonQuery(self: ServerConnection, sqlCommand: str, executionType: ExecutionTypes) -> int
        ExecuteNonQuery(self: ServerConnection, sqlCommands: StringCollection, executionType: ExecutionTypes, retry: bool) -> Array[int]
        ExecuteNonQuery(self: ServerConnection, sqlCommand: str, executionType: ExecutionTypes, retry: bool) -> int
        """
        ...

    def ExecuteReader(self, sqlCommand, command=None) -> SqlDataReader:
        """
        ExecuteReader(self: ServerConnection, sqlCommand: str) -> SqlDataReader
        ExecuteReader(self: ServerConnection, sqlCommand: str) -> (SqlDataReader, SqlCommand)
        """
        ...

    def ExecuteScalar(self, *__args:StringCollection) -> Array:
        """
        ExecuteScalar(self: ServerConnection, sqlCommands: StringCollection) -> Array[object]
        ExecuteScalar(self: ServerConnection, sqlCommand: str) -> object
        """
        ...

    def ExecuteWithResults(self, *__args:str) -> DataSet:
        """
        ExecuteWithResults(self: ServerConnection, sqlCommand: str) -> DataSet
        ExecuteWithResults(self: ServerConnection, sqlCommands: StringCollection) -> Array[DataSet]
        ExecuteWithResults(self: ServerConnection, sqlCommand: str, retry: bool) -> DataSet
        """
        ...

    def IsInFixedServerRole(self, fixedServerRole:FixedServerRoles) -> bool:
        """ IsInFixedServerRole(self: ServerConnection, fixedServerRole: FixedServerRoles) -> bool """
        ...

    @staticmethod
    def NormalizeQuery(QueryText:str, QuotedIdentifiers:bool = ...) -> str:
        """
        NormalizeQuery(QueryText: str) -> str
        NormalizeQuery(QueryText: str, QuotedIdentifiers: bool) -> str
        """
        ...

    def RollBackTransaction(self): # -> 
        """ RollBackTransaction(self: ServerConnection) """
        ...

    def __new__(cls, *__args:IRenewableToken) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, token: IRenewableToken)
        __new__(cls: type, sci: SqlConnectionInfo)
        __new__(cls: type, sqlConnection: SqlConnection)
        __new__(cls: type, sqlConnection: SqlConnection, accessToken: IRenewableToken)
        __new__(cls: type, serverInstance: str)
        __new__(cls: type, serverInstance: str, userName: str, password: str)
        __new__(cls: type, serverInstance: str, userName: str, password: SecureString)
        """
        ...



class ServerMessageEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ServerMessageEventArgs(sqlError: SqlError) """
    @property
    def Error(self) -> SqlError:
        """ Get: Error(self: ServerMessageEventArgs) -> SqlError """
        ...


    def ToString(self) -> str:
        """ ToString(self: ServerMessageEventArgs) -> str """
        ...

    def __new__(cls, sqlError:SqlError) -> Self:
        """ __new__(cls: type, sqlError: SqlError) """
        ...


class ServerMessageEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ServerMessageEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ServerMessageEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ServerMessageEventHandler, sender: object, e: ServerMessageEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ServerMessageEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ServerMessageEventArgs): # -> 
        """ Invoke(self: ServerMessageEventHandler, sender: object, e: ServerMessageEventArgs) """
        ...


class ServerType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ServerType, values: AnalysisServices (1), DatabaseEngine (0), IntegrationServices (3), ReportingServices (2), SqlServerCompactEdition (4), SqlServerEverywhere (4) """
    AnalysisServices: ServerType = ...
    DatabaseEngine: ServerType = ...
    IntegrationServices: ServerType = ...
    ReportingServices: ServerType = ...
    SqlServerCompactEdition: ServerType = ...
    SqlServerEverywhere: ServerType = ...
    value__ = ...


class ServerUserProfiles(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ServerUserProfiles, values: All (7), CreateDatabase (2), CreateXP (4), None (0), SALogin (1) """
    All: ServerUserProfiles = ...
    CreateDatabase: ServerUserProfiles = ...
    CreateXP: ServerUserProfiles = ...
    SALogin: ServerUserProfiles = ...
    value__ = ...


class ServerVersion: # skipped bases: <type 'object'>, <type 'object'>
    """
    ServerVersion(major: int, minor: int)
    ServerVersion(major: int, minor: int, buildNumber: int)
    """
    @property
    def BuildNumber(self) -> int:
        """ Get: BuildNumber(self: ServerVersion) -> int """
        ...

    @property
    def Major(self) -> int:
        """ Get: Major(self: ServerVersion) -> int """
        ...

    @property
    def Minor(self) -> int:
        """ Get: Minor(self: ServerVersion) -> int """
        ...


    def ToString(self) -> str:
        """ ToString(self: ServerVersion) -> str """
        ...


class SqlConnectionInfo(SqlOlapConnectionInfoBase): # skipped bases: <type 'object'>
    """
    SqlConnectionInfo()
    SqlConnectionInfo(serverName: str)
    SqlConnectionInfo(serverName: str, userName: str, password: str)
    SqlConnectionInfo(conn: SqlConnectionInfo)
    SqlConnectionInfo(serverConnection: ServerConnection, connectionType: ConnectionType)
    """
    @property
    def AccessToken(self) -> IRenewableToken:
        """
        Get: AccessToken(self: SqlConnectionInfo) -> IRenewableToken
        Set: AccessToken(self: SqlConnectionInfo) = value
        """
        ...

    @property
    def AdditionalParameters(self) -> str:
        """
        Get: AdditionalParameters(self: SqlConnectionInfo) -> str
        Set: AdditionalParameters(self: SqlConnectionInfo) = value
        """
        ...

    @property
    def ApplicationIntent(self) -> str:
        """
        Get: ApplicationIntent(self: SqlConnectionInfo) -> str
        Set: ApplicationIntent(self: SqlConnectionInfo) = value
        """
        ...

    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: SqlConnectionInfo) -> str
        Set: ApplicationName(self: SqlConnectionInfo) = value
        """
        ...

    @property
    def Authentication(self): # -> AuthenticationMethod
        """
        Get: Authentication(self: SqlConnectionInfo) -> AuthenticationMethod
        Set: Authentication(self: SqlConnectionInfo) = value
        """
        ...

    @property
    def ConnectionProtocol(self) -> NetworkProtocol:
        """
        Get: ConnectionProtocol(self: SqlConnectionInfo) -> NetworkProtocol
        Set: ConnectionProtocol(self: SqlConnectionInfo) = value
        """
        ...

    @property
    def EncryptConnection(self) -> bool:
        """
        Get: EncryptConnection(self: SqlConnectionInfo) -> bool
        Set: EncryptConnection(self: SqlConnectionInfo) = value
        """
        ...

    @property
    def MaxPoolSize(self) -> int:
        """
        Get: MaxPoolSize(self: SqlConnectionInfo) -> int
        Set: MaxPoolSize(self: SqlConnectionInfo) = value
        """
        ...

    @property
    def MinPoolSize(self) -> int:
        """
        Get: MinPoolSize(self: SqlConnectionInfo) -> int
        Set: MinPoolSize(self: SqlConnectionInfo) = value
        """
        ...

    @property
    def PacketSize(self) -> int:
        """
        Get: PacketSize(self: SqlConnectionInfo) -> int
        Set: PacketSize(self: SqlConnectionInfo) = value
        """
        ...

    @property
    def PoolConnectionLifeTime(self) -> int:
        """
        Get: PoolConnectionLifeTime(self: SqlConnectionInfo) -> int
        Set: PoolConnectionLifeTime(self: SqlConnectionInfo) = value
        """
        ...

    @property
    def Pooled(self) -> SqlBoolean:
        """
        Get: Pooled(self: SqlConnectionInfo) -> SqlBoolean
        Set: Pooled(self: SqlConnectionInfo) = value
        """
        ...

    @property
    def TrustServerCertificate(self) -> bool:
        """
        Get: TrustServerCertificate(self: SqlConnectionInfo) -> bool
        Set: TrustServerCertificate(self: SqlConnectionInfo) = value
        """
        ...

    @property
    def WorkstationId(self) -> str:
        """
        Get: WorkstationId(self: SqlConnectionInfo) -> str
        Set: WorkstationId(self: SqlConnectionInfo) = value
        """
        ...


    def AuthenticationMethod(self, *args): #cannot find CLR method
        """ enum AuthenticationMethod, values: ActiveDirectoryIntegrated (3), ActiveDirectoryPassword (2), NotSpecified (0), SqlPassword (1) """
        ...

    def Copy(self) -> SqlConnectionInfo:
        """ Copy(self: SqlConnectionInfo) -> SqlConnectionInfo """
        ...

    @staticmethod
    def GetAuthenticationMethod(connectionStringBuilder:SqlConnectionStringBuilder): # -> AuthenticationMethod
        """ GetAuthenticationMethod(connectionStringBuilder: SqlConnectionStringBuilder) -> AuthenticationMethod """
        ...

    @staticmethod
    def IsApplicationIntentKeywordSupported() -> bool:
        """ IsApplicationIntentKeywordSupported() -> bool """
        ...

    @staticmethod
    def IsAuthenticationKeywordSupported() -> bool:
        """ IsAuthenticationKeywordSupported() -> bool """
        ...

    DefaultNetworkProtocol: NetworkProtocol = ...


class SqlConnectionInfoWithConnection(IDisposable, SqlConnectionInfo, IRestrictedAccess): # skipped bases: <type 'object'>
    """
    SqlConnectionInfoWithConnection()
    SqlConnectionInfoWithConnection(serverName: str)
    SqlConnectionInfoWithConnection(serverName: str, userName: str, password: str)
    SqlConnectionInfoWithConnection(sqlConnection: SqlConnection)
    """
    @property
    def ServerConnection(self) -> ServerConnection:
        """
        Get: ServerConnection(self: SqlConnectionInfoWithConnection) -> ServerConnection
        Set: ServerConnection(self: SqlConnectionInfoWithConnection) = value
        """
        ...


    ConnectionClosed = ...


class SqlExecutionModes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SqlExecutionModes, values: CaptureSql (2), ExecuteAndCaptureSql (3), ExecuteSql (1) """
    CaptureSql: SqlExecutionModes = ...
    ExecuteAndCaptureSql: SqlExecutionModes = ...
    ExecuteSql: SqlExecutionModes = ...
    value__ = ...


class SqlServerManagementException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SqlServerManagementException()
    SqlServerManagementException(message: str)
    SqlServerManagementException(message: str, innerException: Exception)
    """
    @property
    def ProductName(self) -> str:
        """ Get: ProductName() -> str """
        ...


    SerializeObjectState = ...


class StatementEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ StatementEventArgs(sqlStatement: str, timeStamp: DateTime) """
    @property
    def SqlStatement(self) -> str:
        """ Get: SqlStatement(self: StatementEventArgs) -> str """
        ...

    @property
    def TimeStamp(self) -> DateTime:
        """ Get: TimeStamp(self: StatementEventArgs) -> DateTime """
        ...


    def ToString(self) -> str:
        """ ToString(self: StatementEventArgs) -> str """
        ...

    def __new__(cls, sqlStatement:str, timeStamp:DateTime) -> Self:
        """ __new__(cls: type, sqlStatement: str, timeStamp: DateTime) """
        ...


class StatementEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ StatementEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:StatementEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: StatementEventHandler, sender: object, e: StatementEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: StatementEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:StatementEventArgs): # -> 
        """ Invoke(self: StatementEventHandler, sender: object, e: StatementEventArgs) """
        ...


class TransferException(SqlServerManagementException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TransferException()
    TransferException(message: str)
    TransferException(message: str, innerException: Exception)
    """
    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    SerializeObjectState = ...


