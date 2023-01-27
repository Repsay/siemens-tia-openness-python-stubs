# encoding: utf-8
# module System.Data.SqlClient calls itself SqlClient
# from System.Data, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Data.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Byte, DateTimeOffset, Enum, 
    EventArgs, Guid, IAsyncResult, ICloneable, IDisposable, IServiceProvider, 
    Int64, MulticastDelegate, TimeSpan)

from System.Collections import (CollectionBase, ICollection, IDictionary, 
    IEnumerator)

from System.Data import CommandBehavior, SqlDbType

from System.Data.Common import (DBDataPermission, DBDataPermissionAttribute, 
    DbCommand, DbCommandBuilder, DbConnection, DbConnectionStringBuilder, 
    DbDataAdapter, DbDataReader, DbException, DbParameter, 
    DbParameterCollection, DbProviderFactory, DbTransaction, 
    RowUpdatedEventArgs, RowUpdatingEventArgs)

from System.Data.Sql import SqlNotificationRequest

from System.Data.SqlTypes import (SqlBinary, SqlBoolean, SqlByte, SqlBytes, 
    SqlChars, SqlCompareOptions, SqlDateTime, SqlDecimal, SqlDouble, SqlGuid, 
    SqlInt16, SqlInt32, SqlInt64, SqlMoney, SqlSingle, SqlString, SqlXml)

from System.EnterpriseServices import ITransaction

from System.Security import IPermission, SecureString

from System.Threading import CancellationToken

from System.Threading.Tasks import Task

from System.Xml import XmlReader

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    DbProviderServices, ECDiffieHellmanCng, ISQLDebug, field#)
"""

# no functions
# classes

class ApplicationIntent(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ApplicationIntent, values: ReadOnly (1), ReadWrite (0) """
    ReadOnly: ApplicationIntent = ...
    ReadWrite: ApplicationIntent = ...
    value__ = ...


class OnChangeEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OnChangeEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SqlNotificationEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: OnChangeEventHandler, sender: object, e: SqlNotificationEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: OnChangeEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SqlNotificationEventArgs): # -> 
        """ Invoke(self: OnChangeEventHandler, sender: object, e: SqlNotificationEventArgs) """
        ...


class PoolBlockingPeriod(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PoolBlockingPeriod, values: AlwaysBlock (1), Auto (0), NeverBlock (2) """
    AlwaysBlock: PoolBlockingPeriod = ...
    Auto: PoolBlockingPeriod = ...
    NeverBlock: PoolBlockingPeriod = ...
    value__ = ...


class SortOrder(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SortOrder, values: Ascending (0), Descending (1), Unspecified (-1) """
    Ascending: SortOrder = ...
    Descending: SortOrder = ...
    Unspecified: SortOrder = ...
    value__ = ...


class SqlAuthenticationInitializer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Initialize(self): # -> 
        """ Initialize(self: SqlAuthenticationInitializer) """
        ...


class SqlAuthenticationMethod(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlAuthenticationMethod, values: ActiveDirectoryIntegrated (3), ActiveDirectoryInteractive (4), ActiveDirectoryPassword (2), NotSpecified (0), SqlPassword (1) """
    ActiveDirectoryIntegrated: SqlAuthenticationMethod = ...
    ActiveDirectoryInteractive: SqlAuthenticationMethod = ...
    ActiveDirectoryPassword: SqlAuthenticationMethod = ...
    NotSpecified: SqlAuthenticationMethod = ...
    SqlPassword: SqlAuthenticationMethod = ...
    value__ = ...


class SqlAuthenticationParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AuthenticationMethod(self) -> SqlAuthenticationMethod:
        """ Get: AuthenticationMethod(self: SqlAuthenticationParameters) -> SqlAuthenticationMethod """
        ...

    @property
    def Authority(self) -> str:
        """ Get: Authority(self: SqlAuthenticationParameters) -> str """
        ...

    @property
    def ConnectionId(self) -> Guid:
        """ Get: ConnectionId(self: SqlAuthenticationParameters) -> Guid """
        ...

    @property
    def DatabaseName(self) -> str:
        """ Get: DatabaseName(self: SqlAuthenticationParameters) -> str """
        ...

    @property
    def Password(self) -> str:
        """ Get: Password(self: SqlAuthenticationParameters) -> str """
        ...

    @property
    def Resource(self) -> str:
        """ Get: Resource(self: SqlAuthenticationParameters) -> str """
        ...

    @property
    def ServerName(self) -> str:
        """ Get: ServerName(self: SqlAuthenticationParameters) -> str """
        ...

    @property
    def UserId(self) -> str:
        """ Get: UserId(self: SqlAuthenticationParameters) -> str """
        ...



class SqlAuthenticationProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def AcquireTokenAsync(self, parameters:SqlAuthenticationParameters) -> Task:
        """ AcquireTokenAsync(self: SqlAuthenticationProvider, parameters: SqlAuthenticationParameters) -> Task[SqlAuthenticationToken] """
        ...

    def BeforeLoad(self, authenticationMethod:SqlAuthenticationMethod): # -> 
        """ BeforeLoad(self: SqlAuthenticationProvider, authenticationMethod: SqlAuthenticationMethod) """
        ...

    def BeforeUnload(self, authenticationMethod:SqlAuthenticationMethod): # -> 
        """ BeforeUnload(self: SqlAuthenticationProvider, authenticationMethod: SqlAuthenticationMethod) """
        ...

    @staticmethod
    def GetProvider(authenticationMethod:SqlAuthenticationMethod) -> SqlAuthenticationProvider:
        """ GetProvider(authenticationMethod: SqlAuthenticationMethod) -> SqlAuthenticationProvider """
        ...

    def IsSupported(self, authenticationMethod:SqlAuthenticationMethod) -> bool:
        """ IsSupported(self: SqlAuthenticationProvider, authenticationMethod: SqlAuthenticationMethod) -> bool """
        ...

    @staticmethod
    def SetProvider(authenticationMethod:SqlAuthenticationMethod, provider:SqlAuthenticationProvider) -> bool:
        """ SetProvider(authenticationMethod: SqlAuthenticationMethod, provider: SqlAuthenticationProvider) -> bool """
        ...


class SqlAuthenticationToken: # skipped bases: <type 'object'>, <type 'object'>
    """ SqlAuthenticationToken(accessToken: str, expiresOn: DateTimeOffset) """
    @property
    def AccessToken(self) -> str:
        """ Get: AccessToken(self: SqlAuthenticationToken) -> str """
        ...

    @property
    def ExpiresOn(self) -> DateTimeOffset:
        """ Get: ExpiresOn(self: SqlAuthenticationToken) -> DateTimeOffset """
        ...



class SqlBulkCopy(IDisposable): # skipped bases: <type 'object'>
    """
    SqlBulkCopy(connection: SqlConnection)
    SqlBulkCopy(connection: SqlConnection, copyOptions: SqlBulkCopyOptions, externalTransaction: SqlTransaction)
    SqlBulkCopy(connectionString: str)
    SqlBulkCopy(connectionString: str, copyOptions: SqlBulkCopyOptions)
    """
    @property
    def BatchSize(self) -> int:
        """
        Get: BatchSize(self: SqlBulkCopy) -> int
        Set: BatchSize(self: SqlBulkCopy) = value
        """
        ...

    @property
    def BulkCopyTimeout(self) -> int:
        """
        Get: BulkCopyTimeout(self: SqlBulkCopy) -> int
        Set: BulkCopyTimeout(self: SqlBulkCopy) = value
        """
        ...

    @property
    def ColumnMappings(self) -> SqlBulkCopyColumnMappingCollection:
        """ Get: ColumnMappings(self: SqlBulkCopy) -> SqlBulkCopyColumnMappingCollection """
        ...

    @property
    def DestinationTableName(self) -> str:
        """
        Get: DestinationTableName(self: SqlBulkCopy) -> str
        Set: DestinationTableName(self: SqlBulkCopy) = value
        """
        ...

    @property
    def EnableStreaming(self) -> bool:
        """
        Get: EnableStreaming(self: SqlBulkCopy) -> bool
        Set: EnableStreaming(self: SqlBulkCopy) = value
        """
        ...

    @property
    def NotifyAfter(self) -> int:
        """
        Get: NotifyAfter(self: SqlBulkCopy) -> int
        Set: NotifyAfter(self: SqlBulkCopy) = value
        """
        ...


    def Close(self): # -> 
        """ Close(self: SqlBulkCopy) """
        ...

    def WriteToServer(self, *__args:DbDataReader): # -> 
        """ WriteToServer(self: SqlBulkCopy, reader: DbDataReader)WriteToServer(self: SqlBulkCopy, reader: IDataReader)WriteToServer(self: SqlBulkCopy, table: DataTable)WriteToServer(self: SqlBulkCopy, table: DataTable, rowState: DataRowState)WriteToServer(self: SqlBulkCopy, rows: Array[DataRow]) """
        ...

    def WriteToServerAsync(self, *__args:Array) -> Task:
        """
        WriteToServerAsync(self: SqlBulkCopy, rows: Array[DataRow]) -> Task
        WriteToServerAsync(self: SqlBulkCopy, reader: DbDataReader) -> Task
        WriteToServerAsync(self: SqlBulkCopy, reader: DbDataReader, cancellationToken: CancellationToken) -> Task
        WriteToServerAsync(self: SqlBulkCopy, reader: IDataReader) -> Task
        WriteToServerAsync(self: SqlBulkCopy, reader: IDataReader, cancellationToken: CancellationToken) -> Task
        WriteToServerAsync(self: SqlBulkCopy, table: DataTable) -> Task
        WriteToServerAsync(self: SqlBulkCopy, table: DataTable, cancellationToken: CancellationToken) -> Task
        WriteToServerAsync(self: SqlBulkCopy, table: DataTable, rowState: DataRowState) -> Task
        WriteToServerAsync(self: SqlBulkCopy, table: DataTable, rowState: DataRowState, cancellationToken: CancellationToken) -> Task
        WriteToServerAsync(self: SqlBulkCopy, rows: Array[DataRow], cancellationToken: CancellationToken) -> Task
        """
        ...

    SqlRowsCopied = ...


class SqlBulkCopyColumnMapping: # skipped bases: <type 'object'>, <type 'object'>
    """
    SqlBulkCopyColumnMapping()
    SqlBulkCopyColumnMapping(sourceColumn: str, destinationColumn: str)
    SqlBulkCopyColumnMapping(sourceColumnOrdinal: int, destinationColumn: str)
    SqlBulkCopyColumnMapping(sourceColumn: str, destinationOrdinal: int)
    SqlBulkCopyColumnMapping(sourceColumnOrdinal: int, destinationOrdinal: int)
    """
    @property
    def DestinationColumn(self) -> str:
        """
        Get: DestinationColumn(self: SqlBulkCopyColumnMapping) -> str
        Set: DestinationColumn(self: SqlBulkCopyColumnMapping) = value
        """
        ...

    @property
    def DestinationOrdinal(self) -> int:
        """
        Get: DestinationOrdinal(self: SqlBulkCopyColumnMapping) -> int
        Set: DestinationOrdinal(self: SqlBulkCopyColumnMapping) = value
        """
        ...

    @property
    def SourceColumn(self) -> str:
        """
        Get: SourceColumn(self: SqlBulkCopyColumnMapping) -> str
        Set: SourceColumn(self: SqlBulkCopyColumnMapping) = value
        """
        ...

    @property
    def SourceOrdinal(self) -> int:
        """
        Get: SourceOrdinal(self: SqlBulkCopyColumnMapping) -> int
        Set: SourceOrdinal(self: SqlBulkCopyColumnMapping) = value
        """
        ...



class SqlBulkCopyColumnMappingCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, *__args:SqlBulkCopyColumnMapping) -> SqlBulkCopyColumnMapping:
        """
        Add(self: SqlBulkCopyColumnMappingCollection, bulkCopyColumnMapping: SqlBulkCopyColumnMapping) -> SqlBulkCopyColumnMapping
        Add(self: SqlBulkCopyColumnMappingCollection, sourceColumn: str, destinationColumn: str) -> SqlBulkCopyColumnMapping
        Add(self: SqlBulkCopyColumnMappingCollection, sourceColumnIndex: int, destinationColumn: str) -> SqlBulkCopyColumnMapping
        Add(self: SqlBulkCopyColumnMappingCollection, sourceColumn: str, destinationColumnIndex: int) -> SqlBulkCopyColumnMapping
        Add(self: SqlBulkCopyColumnMappingCollection, sourceColumnIndex: int, destinationColumnIndex: int) -> SqlBulkCopyColumnMapping
        """
        ...

    def Contains(self, value:SqlBulkCopyColumnMapping) -> bool:
        """ Contains(self: SqlBulkCopyColumnMappingCollection, value: SqlBulkCopyColumnMapping) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: SqlBulkCopyColumnMappingCollection, array: Array[SqlBulkCopyColumnMapping], index: int) """
        ...

    def IndexOf(self, value:SqlBulkCopyColumnMapping) -> int:
        """ IndexOf(self: SqlBulkCopyColumnMappingCollection, value: SqlBulkCopyColumnMapping) -> int """
        ...

    def Insert(self, index:int, value:SqlBulkCopyColumnMapping): # -> 
        """ Insert(self: SqlBulkCopyColumnMappingCollection, index: int, value: SqlBulkCopyColumnMapping) """
        ...

    def Remove(self, value:SqlBulkCopyColumnMapping): # -> 
        """ Remove(self: SqlBulkCopyColumnMappingCollection, value: SqlBulkCopyColumnMapping) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class SqlBulkCopyOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SqlBulkCopyOptions, values: AllowEncryptedValueModifications (64), CheckConstraints (2), Default (0), FireTriggers (16), KeepIdentity (1), KeepNulls (8), TableLock (4), UseInternalTransaction (32) """
    AllowEncryptedValueModifications: SqlBulkCopyOptions = ...
    CheckConstraints: SqlBulkCopyOptions = ...
    Default: SqlBulkCopyOptions = ...
    FireTriggers: SqlBulkCopyOptions = ...
    KeepIdentity: SqlBulkCopyOptions = ...
    KeepNulls: SqlBulkCopyOptions = ...
    TableLock: SqlBulkCopyOptions = ...
    UseInternalTransaction: SqlBulkCopyOptions = ...
    value__ = ...


class SqlClientFactory(IServiceProvider, DbProviderFactory): # skipped bases: <type 'object'>
    """ no doc """
    Instance: SqlClientFactory = ...


class SqlClientLogger: # skipped bases: <type 'object'>, <type 'object'>
    """ SqlClientLogger() """
    @property
    def IsLoggingEnabled(self) -> bool:
        """ Get: IsLoggingEnabled(self: SqlClientLogger) -> bool """
        ...


    def LogAssert(self, value:bool, type:str, method:str, message:str) -> bool:
        """ LogAssert(self: SqlClientLogger, value: bool, type: str, method: str, message: str) -> bool """
        ...

    def LogError(self, type:str, method:str, message:str): # -> 
        """ LogError(self: SqlClientLogger, type: str, method: str, message: str) """
        ...

    def LogInfo(self, type:str, method:str, message:str): # -> 
        """ LogInfo(self: SqlClientLogger, type: str, method: str, message: str) """
        ...


class SqlClientMetaDataCollectionNames: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Columns: str = ...
    Databases: str = ...
    ForeignKeys: str = ...
    IndexColumns: str = ...
    Indexes: str = ...
    Parameters: str = ...
    ProcedureColumns: str = ...
    Procedures: str = ...
    Tables: str = ...
    UserDefinedTypes: str = ...
    Users: str = ...
    ViewColumns: str = ...
    Views: str = ...
    __all__: list = ...


class SqlClientPermission(DBDataPermission): # skipped bases: <type 'IPermission'>, <type 'IUnrestrictedPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    SqlClientPermission()
    SqlClientPermission(state: PermissionState)
    SqlClientPermission(state: PermissionState, allowBlankPassword: bool)
    """
    pass

class SqlClientPermissionAttribute(DBDataPermissionAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SqlClientPermissionAttribute(action: SecurityAction) """
    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: SqlClientPermissionAttribute) -> IPermission """
        ...


class SqlColumnEncryptionKeyStoreProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def DecryptColumnEncryptionKey(self, masterKeyPath:str, encryptionAlgorithm:str, encryptedColumnEncryptionKey:Array) -> Array:
        """ DecryptColumnEncryptionKey(self: SqlColumnEncryptionKeyStoreProvider, masterKeyPath: str, encryptionAlgorithm: str, encryptedColumnEncryptionKey: Array[Byte]) -> Array[Byte] """
        ...

    def EncryptColumnEncryptionKey(self, masterKeyPath:str, encryptionAlgorithm:str, columnEncryptionKey:Array) -> Array:
        """ EncryptColumnEncryptionKey(self: SqlColumnEncryptionKeyStoreProvider, masterKeyPath: str, encryptionAlgorithm: str, columnEncryptionKey: Array[Byte]) -> Array[Byte] """
        ...

    def SignColumnMasterKeyMetadata(self, masterKeyPath:str, allowEnclaveComputations:bool) -> Array:
        """ SignColumnMasterKeyMetadata(self: SqlColumnEncryptionKeyStoreProvider, masterKeyPath: str, allowEnclaveComputations: bool) -> Array[Byte] """
        ...

    def VerifyColumnMasterKeyMetadata(self, masterKeyPath:str, allowEnclaveComputations:bool, signature:Array) -> bool:
        """ VerifyColumnMasterKeyMetadata(self: SqlColumnEncryptionKeyStoreProvider, masterKeyPath: str, allowEnclaveComputations: bool, signature: Array[Byte]) -> bool """
        ...


class SqlColumnEncryptionCertificateStoreProvider(SqlColumnEncryptionKeyStoreProvider): # skipped bases: <type 'object'>
    """ SqlColumnEncryptionCertificateStoreProvider() """
    ProviderName: str = ...


class SqlColumnEncryptionCngProvider(SqlColumnEncryptionKeyStoreProvider): # skipped bases: <type 'object'>
    """ SqlColumnEncryptionCngProvider() """
    ProviderName: str = ...


class SqlColumnEncryptionCspProvider(SqlColumnEncryptionKeyStoreProvider): # skipped bases: <type 'object'>
    """ SqlColumnEncryptionCspProvider() """
    ProviderName: str = ...


class SqlColumnEncryptionEnclaveProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateEnclaveSession(self, enclaveAttestationInfo, clientDiffieHellmanKey, attestationUrl, servername, sqlEnclaveSession, counter) -> Tuple_[SqlEnclaveSession, Int64]:
        """ CreateEnclaveSession(self: SqlColumnEncryptionEnclaveProvider, enclaveAttestationInfo: Array[Byte], clientDiffieHellmanKey: ECDiffieHellmanCng, attestationUrl: str, servername: str) -> (SqlEnclaveSession, Int64) """
        ...

    def GetAttestationParameters(self) -> SqlEnclaveAttestationParameters:
        """ GetAttestationParameters(self: SqlColumnEncryptionEnclaveProvider) -> SqlEnclaveAttestationParameters """
        ...

    def GetEnclaveSession(self, serverName, attestationUrl, sqlEnclaveSession, counter) -> Tuple_[SqlEnclaveSession, Int64]:
        """ GetEnclaveSession(self: SqlColumnEncryptionEnclaveProvider, serverName: str, attestationUrl: str) -> (SqlEnclaveSession, Int64) """
        ...

    def InvalidateEnclaveSession(self, serverName:str, enclaveAttestationUrl:str, enclaveSession:SqlEnclaveSession): # -> 
        """ InvalidateEnclaveSession(self: SqlColumnEncryptionEnclaveProvider, serverName: str, enclaveAttestationUrl: str, enclaveSession: SqlEnclaveSession) """
        ...


class SqlCommand(DbCommand, ICloneable): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDbCommand'>, <type 'object'>
    """
    SqlCommand()
    SqlCommand(cmdText: str)
    SqlCommand(cmdText: str, connection: SqlConnection)
    SqlCommand(cmdText: str, connection: SqlConnection, transaction: SqlTransaction)
    SqlCommand(cmdText: str, connection: SqlConnection, transaction: SqlTransaction, columnEncryptionSetting: SqlCommandColumnEncryptionSetting)
    """
    @property
    def ColumnEncryptionSetting(self) -> SqlCommandColumnEncryptionSetting:
        """ Get: ColumnEncryptionSetting(self: SqlCommand) -> SqlCommandColumnEncryptionSetting """
        ...

    @property
    def Notification(self) -> SqlNotificationRequest:
        """
        Get: Notification(self: SqlCommand) -> SqlNotificationRequest
        Set: Notification(self: SqlCommand) = value
        """
        ...

    @property
    def NotificationAutoEnlist(self) -> bool:
        """
        Get: NotificationAutoEnlist(self: SqlCommand) -> bool
        Set: NotificationAutoEnlist(self: SqlCommand) = value
        """
        ...


    def BeginExecuteNonQuery(self, callback:AsyncCallback = ..., stateObject:object = ...) -> IAsyncResult:
        """
        BeginExecuteNonQuery(self: SqlCommand) -> IAsyncResult
        BeginExecuteNonQuery(self: SqlCommand, callback: AsyncCallback, stateObject: object) -> IAsyncResult
        """
        ...

    def BeginExecuteReader(self, *__args:CommandBehavior) -> IAsyncResult:
        """
        BeginExecuteReader(self: SqlCommand) -> IAsyncResult
        BeginExecuteReader(self: SqlCommand, callback: AsyncCallback, stateObject: object) -> IAsyncResult
        BeginExecuteReader(self: SqlCommand, behavior: CommandBehavior) -> IAsyncResult
        BeginExecuteReader(self: SqlCommand, callback: AsyncCallback, stateObject: object, behavior: CommandBehavior) -> IAsyncResult
        """
        ...

    def BeginExecuteXmlReader(self, callback:AsyncCallback = ..., stateObject:object = ...) -> IAsyncResult:
        """
        BeginExecuteXmlReader(self: SqlCommand) -> IAsyncResult
        BeginExecuteXmlReader(self: SqlCommand, callback: AsyncCallback, stateObject: object) -> IAsyncResult
        """
        ...

    def EndExecuteNonQuery(self, asyncResult:IAsyncResult) -> int:
        """ EndExecuteNonQuery(self: SqlCommand, asyncResult: IAsyncResult) -> int """
        ...

    def EndExecuteReader(self, asyncResult:IAsyncResult) -> SqlDataReader:
        """ EndExecuteReader(self: SqlCommand, asyncResult: IAsyncResult) -> SqlDataReader """
        ...

    def EndExecuteXmlReader(self, asyncResult:IAsyncResult) -> XmlReader:
        """ EndExecuteXmlReader(self: SqlCommand, asyncResult: IAsyncResult) -> XmlReader """
        ...

    def ExecuteXmlReader(self) -> XmlReader:
        """ ExecuteXmlReader(self: SqlCommand) -> XmlReader """
        ...

    def ExecuteXmlReaderAsync(self, cancellationToken:CancellationToken = ...) -> Task:
        """
        ExecuteXmlReaderAsync(self: SqlCommand) -> Task[XmlReader]
        ExecuteXmlReaderAsync(self: SqlCommand, cancellationToken: CancellationToken) -> Task[XmlReader]
        """
        ...

    def ResetCommandTimeout(self): # -> 
        """ ResetCommandTimeout(self: SqlCommand) """
        ...

    def __new__(cls, cmdText:str = ..., connection:SqlConnection = ..., transaction:SqlTransaction = ..., columnEncryptionSetting:SqlCommandColumnEncryptionSetting = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, cmdText: str)
        __new__(cls: type, cmdText: str, connection: SqlConnection)
        __new__(cls: type, cmdText: str, connection: SqlConnection, transaction: SqlTransaction)
        __new__(cls: type, cmdText: str, connection: SqlConnection, transaction: SqlTransaction, columnEncryptionSetting: SqlCommandColumnEncryptionSetting)
        """
        ...

    StatementCompleted = ...


class SqlCommandBuilder(DbCommandBuilder): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    SqlCommandBuilder()
    SqlCommandBuilder(adapter: SqlDataAdapter)
    """
    @staticmethod
    def DeriveParameters(command:SqlCommand): # -> 
        """ DeriveParameters(command: SqlCommand) """
        ...

    def __new__(cls, adapter:SqlDataAdapter = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, adapter: SqlDataAdapter)
        """
        ...


class SqlCommandColumnEncryptionSetting(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlCommandColumnEncryptionSetting, values: Disabled (3), Enabled (1), ResultSetOnly (2), UseConnectionSetting (0) """
    Disabled: SqlCommandColumnEncryptionSetting = ...
    Enabled: SqlCommandColumnEncryptionSetting = ...
    ResultSetOnly: SqlCommandColumnEncryptionSetting = ...
    UseConnectionSetting: SqlCommandColumnEncryptionSetting = ...
    value__ = ...


class SqlConnection(ICloneable, DbConnection): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDbConnection'>, <type 'object'>
    """
    SqlConnection(connectionString: str)
    SqlConnection(connectionString: str, credential: SqlCredential)
    SqlConnection()
    """
    @property
    def AccessToken(self) -> str:
        """
        Get: AccessToken(self: SqlConnection) -> str
        Set: AccessToken(self: SqlConnection) = value
        """
        ...

    @property
    def ClientConnectionId(self) -> Guid:
        """ Get: ClientConnectionId(self: SqlConnection) -> Guid """
        ...

    @property
    def ColumnEncryptionKeyCacheTtl(self) -> TimeSpan:
        """
        Get: ColumnEncryptionKeyCacheTtl() -> TimeSpan
        Set: ColumnEncryptionKeyCacheTtl() = value
        """
        ...

    @property
    def ColumnEncryptionQueryMetadataCacheEnabled(self) -> bool:
        """
        Get: ColumnEncryptionQueryMetadataCacheEnabled() -> bool
        Set: ColumnEncryptionQueryMetadataCacheEnabled() = value
        """
        ...

    @property
    def ColumnEncryptionTrustedMasterKeyPaths(self) -> IDictionary:
        """ Get: ColumnEncryptionTrustedMasterKeyPaths() -> IDictionary[str, IList[str]] """
        ...

    @property
    def Credential(self) -> SqlCredential:
        """
        Get: Credential(self: SqlConnection) -> SqlCredential
        Set: Credential(self: SqlConnection) = value
        """
        ...

    @property
    def FireInfoMessageEventOnUserErrors(self) -> bool:
        """
        Get: FireInfoMessageEventOnUserErrors(self: SqlConnection) -> bool
        Set: FireInfoMessageEventOnUserErrors(self: SqlConnection) = value
        """
        ...

    @property
    def PacketSize(self) -> int:
        """ Get: PacketSize(self: SqlConnection) -> int """
        ...

    @property
    def StatisticsEnabled(self) -> bool:
        """
        Get: StatisticsEnabled(self: SqlConnection) -> bool
        Set: StatisticsEnabled(self: SqlConnection) = value
        """
        ...

    @property
    def WorkstationId(self) -> str:
        """ Get: WorkstationId(self: SqlConnection) -> str """
        ...


    @staticmethod
    def ChangePassword(connectionString:str, *__args:str): # -> 
        """ ChangePassword(connectionString: str, newPassword: str)ChangePassword(connectionString: str, credential: SqlCredential, newSecurePassword: SecureString) """
        ...

    @staticmethod
    def ClearAllPools(): # -> 
        """ ClearAllPools() """
        ...

    @staticmethod
    def ClearPool(connection:SqlConnection): # -> 
        """ ClearPool(connection: SqlConnection) """
        ...

    def EnlistDistributedTransaction(self, transaction:ITransaction): # -> 
        """ EnlistDistributedTransaction(self: SqlConnection, transaction: ITransaction) """
        ...

    @staticmethod
    def RegisterColumnEncryptionKeyStoreProviders(customProviders:IDictionary): # -> 
        """ RegisterColumnEncryptionKeyStoreProviders(customProviders: IDictionary[str, SqlColumnEncryptionKeyStoreProvider]) """
        ...

    def ResetStatistics(self): # -> 
        """ ResetStatistics(self: SqlConnection) """
        ...

    def RetrieveStatistics(self) -> IDictionary:
        """ RetrieveStatistics(self: SqlConnection) -> IDictionary """
        ...

    def __new__(cls, connectionString:str = ..., credential:SqlCredential = ...) -> Self:
        """
        __new__(cls: type, connectionString: str)
        __new__(cls: type, connectionString: str, credential: SqlCredential)
        __new__(cls: type)
        """
        ...

    InfoMessage = ...


class SqlConnectionColumnEncryptionSetting(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlConnectionColumnEncryptionSetting, values: Disabled (0), Enabled (1) """
    Disabled: SqlConnectionColumnEncryptionSetting = ...
    Enabled: SqlConnectionColumnEncryptionSetting = ...
    value__ = ...


class SqlConnectionStringBuilder(DbConnectionStringBuilder): # skipped bases: <type 'ICustomTypeDescriptor'>, <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    SqlConnectionStringBuilder()
    SqlConnectionStringBuilder(connectionString: str)
    """
    @property
    def ApplicationIntent(self) -> ApplicationIntent:
        """
        Get: ApplicationIntent(self: SqlConnectionStringBuilder) -> ApplicationIntent
        Set: ApplicationIntent(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: SqlConnectionStringBuilder) -> str
        Set: ApplicationName(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def AsynchronousProcessing(self) -> bool:
        """
        Get: AsynchronousProcessing(self: SqlConnectionStringBuilder) -> bool
        Set: AsynchronousProcessing(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def AttachDBFilename(self) -> str:
        """
        Get: AttachDBFilename(self: SqlConnectionStringBuilder) -> str
        Set: AttachDBFilename(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def Authentication(self) -> SqlAuthenticationMethod:
        """
        Get: Authentication(self: SqlConnectionStringBuilder) -> SqlAuthenticationMethod
        Set: Authentication(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def ColumnEncryptionSetting(self) -> SqlConnectionColumnEncryptionSetting:
        """
        Get: ColumnEncryptionSetting(self: SqlConnectionStringBuilder) -> SqlConnectionColumnEncryptionSetting
        Set: ColumnEncryptionSetting(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def ConnectionReset(self) -> bool:
        """
        Get: ConnectionReset(self: SqlConnectionStringBuilder) -> bool
        Set: ConnectionReset(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def ConnectRetryCount(self) -> int:
        """
        Get: ConnectRetryCount(self: SqlConnectionStringBuilder) -> int
        Set: ConnectRetryCount(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def ConnectRetryInterval(self) -> int:
        """
        Get: ConnectRetryInterval(self: SqlConnectionStringBuilder) -> int
        Set: ConnectRetryInterval(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def ConnectTimeout(self) -> int:
        """
        Get: ConnectTimeout(self: SqlConnectionStringBuilder) -> int
        Set: ConnectTimeout(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def ContextConnection(self) -> bool:
        """
        Get: ContextConnection(self: SqlConnectionStringBuilder) -> bool
        Set: ContextConnection(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def CurrentLanguage(self) -> str:
        """
        Get: CurrentLanguage(self: SqlConnectionStringBuilder) -> str
        Set: CurrentLanguage(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def DataSource(self) -> str:
        """
        Get: DataSource(self: SqlConnectionStringBuilder) -> str
        Set: DataSource(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def EnclaveAttestationUrl(self) -> str:
        """
        Get: EnclaveAttestationUrl(self: SqlConnectionStringBuilder) -> str
        Set: EnclaveAttestationUrl(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def Encrypt(self) -> bool:
        """
        Get: Encrypt(self: SqlConnectionStringBuilder) -> bool
        Set: Encrypt(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def Enlist(self) -> bool:
        """
        Get: Enlist(self: SqlConnectionStringBuilder) -> bool
        Set: Enlist(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def FailoverPartner(self) -> str:
        """
        Get: FailoverPartner(self: SqlConnectionStringBuilder) -> str
        Set: FailoverPartner(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def InitialCatalog(self) -> str:
        """
        Get: InitialCatalog(self: SqlConnectionStringBuilder) -> str
        Set: InitialCatalog(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def IntegratedSecurity(self) -> bool:
        """
        Get: IntegratedSecurity(self: SqlConnectionStringBuilder) -> bool
        Set: IntegratedSecurity(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def LoadBalanceTimeout(self) -> int:
        """
        Get: LoadBalanceTimeout(self: SqlConnectionStringBuilder) -> int
        Set: LoadBalanceTimeout(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def MaxPoolSize(self) -> int:
        """
        Get: MaxPoolSize(self: SqlConnectionStringBuilder) -> int
        Set: MaxPoolSize(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def MinPoolSize(self) -> int:
        """
        Get: MinPoolSize(self: SqlConnectionStringBuilder) -> int
        Set: MinPoolSize(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def MultipleActiveResultSets(self) -> bool:
        """
        Get: MultipleActiveResultSets(self: SqlConnectionStringBuilder) -> bool
        Set: MultipleActiveResultSets(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def MultiSubnetFailover(self) -> bool:
        """
        Get: MultiSubnetFailover(self: SqlConnectionStringBuilder) -> bool
        Set: MultiSubnetFailover(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def NetworkLibrary(self) -> str:
        """
        Get: NetworkLibrary(self: SqlConnectionStringBuilder) -> str
        Set: NetworkLibrary(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def PacketSize(self) -> int:
        """
        Get: PacketSize(self: SqlConnectionStringBuilder) -> int
        Set: PacketSize(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def Password(self) -> str:
        """
        Get: Password(self: SqlConnectionStringBuilder) -> str
        Set: Password(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def PersistSecurityInfo(self) -> bool:
        """
        Get: PersistSecurityInfo(self: SqlConnectionStringBuilder) -> bool
        Set: PersistSecurityInfo(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def PoolBlockingPeriod(self) -> PoolBlockingPeriod:
        """
        Get: PoolBlockingPeriod(self: SqlConnectionStringBuilder) -> PoolBlockingPeriod
        Set: PoolBlockingPeriod(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def Pooling(self) -> bool:
        """
        Get: Pooling(self: SqlConnectionStringBuilder) -> bool
        Set: Pooling(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def Replication(self) -> bool:
        """
        Get: Replication(self: SqlConnectionStringBuilder) -> bool
        Set: Replication(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def TransactionBinding(self) -> str:
        """
        Get: TransactionBinding(self: SqlConnectionStringBuilder) -> str
        Set: TransactionBinding(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def TransparentNetworkIPResolution(self) -> bool:
        """
        Get: TransparentNetworkIPResolution(self: SqlConnectionStringBuilder) -> bool
        Set: TransparentNetworkIPResolution(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def TrustServerCertificate(self) -> bool:
        """
        Get: TrustServerCertificate(self: SqlConnectionStringBuilder) -> bool
        Set: TrustServerCertificate(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def TypeSystemVersion(self) -> str:
        """
        Get: TypeSystemVersion(self: SqlConnectionStringBuilder) -> str
        Set: TypeSystemVersion(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def UserID(self) -> str:
        """
        Get: UserID(self: SqlConnectionStringBuilder) -> str
        Set: UserID(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def UserInstance(self) -> bool:
        """
        Get: UserInstance(self: SqlConnectionStringBuilder) -> bool
        Set: UserInstance(self: SqlConnectionStringBuilder) = value
        """
        ...

    @property
    def WorkstationID(self) -> str:
        """
        Get: WorkstationID(self: SqlConnectionStringBuilder) -> str
        Set: WorkstationID(self: SqlConnectionStringBuilder) = value
        """
        ...



class SqlCredential: # skipped bases: <type 'object'>, <type 'object'>
    """ SqlCredential(userId: str, password: SecureString) """
    @property
    def Password(self) -> SecureString:
        """ Get: Password(self: SqlCredential) -> SecureString """
        ...

    @property
    def UserId(self) -> str:
        """ Get: UserId(self: SqlCredential) -> str """
        ...



class SqlDataAdapter(DbDataAdapter): # skipped bases: <type 'IDataAdapter'>, <type 'IDisposable'>, <type 'IComponent'>, <type 'ICloneable'>, <type 'IDbDataAdapter'>, <type 'object'>
    """
    SqlDataAdapter()
    SqlDataAdapter(selectCommand: SqlCommand)
    SqlDataAdapter(selectCommandText: str, selectConnectionString: str)
    SqlDataAdapter(selectCommandText: str, selectConnection: SqlConnection)
    """
    RowUpdated = ...
    RowUpdating = ...


class SqlDataReader(DbDataReader): # skipped bases: <type 'IDisposable'>, <type 'IDataReader'>, <type 'IDataRecord'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Connection(self):
        ...


    def GetDateTimeOffset(self, i:int) -> DateTimeOffset:
        """ GetDateTimeOffset(self: SqlDataReader, i: int) -> DateTimeOffset """
        ...

    def GetSqlBinary(self, i:int) -> SqlBinary:
        """ GetSqlBinary(self: SqlDataReader, i: int) -> SqlBinary """
        ...

    def GetSqlBoolean(self, i:int) -> SqlBoolean:
        """ GetSqlBoolean(self: SqlDataReader, i: int) -> SqlBoolean """
        ...

    def GetSqlByte(self, i:int) -> SqlByte:
        """ GetSqlByte(self: SqlDataReader, i: int) -> SqlByte """
        ...

    def GetSqlBytes(self, i:int) -> SqlBytes:
        """ GetSqlBytes(self: SqlDataReader, i: int) -> SqlBytes """
        ...

    def GetSqlChars(self, i:int) -> SqlChars:
        """ GetSqlChars(self: SqlDataReader, i: int) -> SqlChars """
        ...

    def GetSqlDateTime(self, i:int) -> SqlDateTime:
        """ GetSqlDateTime(self: SqlDataReader, i: int) -> SqlDateTime """
        ...

    def GetSqlDecimal(self, i:int) -> SqlDecimal:
        """ GetSqlDecimal(self: SqlDataReader, i: int) -> SqlDecimal """
        ...

    def GetSqlDouble(self, i:int) -> SqlDouble:
        """ GetSqlDouble(self: SqlDataReader, i: int) -> SqlDouble """
        ...

    def GetSqlGuid(self, i:int) -> SqlGuid:
        """ GetSqlGuid(self: SqlDataReader, i: int) -> SqlGuid """
        ...

    def GetSqlInt16(self, i:int) -> SqlInt16:
        """ GetSqlInt16(self: SqlDataReader, i: int) -> SqlInt16 """
        ...

    def GetSqlInt32(self, i:int) -> SqlInt32:
        """ GetSqlInt32(self: SqlDataReader, i: int) -> SqlInt32 """
        ...

    def GetSqlInt64(self, i:int) -> SqlInt64:
        """ GetSqlInt64(self: SqlDataReader, i: int) -> SqlInt64 """
        ...

    def GetSqlMoney(self, i:int) -> SqlMoney:
        """ GetSqlMoney(self: SqlDataReader, i: int) -> SqlMoney """
        ...

    def GetSqlSingle(self, i:int) -> SqlSingle:
        """ GetSqlSingle(self: SqlDataReader, i: int) -> SqlSingle """
        ...

    def GetSqlString(self, i:int) -> SqlString:
        """ GetSqlString(self: SqlDataReader, i: int) -> SqlString """
        ...

    def GetSqlValue(self, i:int) -> object:
        """ GetSqlValue(self: SqlDataReader, i: int) -> object """
        ...

    def GetSqlValues(self, values:Array) -> int:
        """ GetSqlValues(self: SqlDataReader, values: Array[object]) -> int """
        ...

    def GetSqlXml(self, i:int) -> SqlXml:
        """ GetSqlXml(self: SqlDataReader, i: int) -> SqlXml """
        ...

    def GetTimeSpan(self, i:int) -> TimeSpan:
        """ GetTimeSpan(self: SqlDataReader, i: int) -> TimeSpan """
        ...

    def GetXmlReader(self, i:int) -> XmlReader:
        """ GetXmlReader(self: SqlDataReader, i: int) -> XmlReader """
        ...

    def IsCommandBehavior(self, *args): #cannot find CLR method
        """ IsCommandBehavior(self: SqlDataReader, condition: CommandBehavior) -> bool """
        ...


class SQLDebugging(ISQLDebug): # skipped bases: <type 'object'>
    """ SQLDebugging() """
    pass

class SqlDependency: # skipped bases: <type 'object'>, <type 'object'>
    """
    SqlDependency()
    SqlDependency(command: SqlCommand)
    SqlDependency(command: SqlCommand, options: str, timeout: int)
    """
    @property
    def HasChanges(self) -> bool:
        """ Get: HasChanges(self: SqlDependency) -> bool """
        ...

    @property
    def Id(self) -> str:
        """ Get: Id(self: SqlDependency) -> str """
        ...


    def AddCommandDependency(self, command:SqlCommand): # -> 
        """ AddCommandDependency(self: SqlDependency, command: SqlCommand) """
        ...

    @staticmethod
    def Start(connectionString:str, queue:str = ...) -> bool:
        """
        Start(connectionString: str) -> bool
        Start(connectionString: str, queue: str) -> bool
        """
        ...

    @staticmethod
    def Stop(connectionString:str, queue:str = ...) -> bool:
        """
        Stop(connectionString: str) -> bool
        Stop(connectionString: str, queue: str) -> bool
        """
        ...

    OnChange = ...


class SqlEnclaveAttestationParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ SqlEnclaveAttestationParameters(protocol: int, input: Array[Byte], clientDiffieHellmanKey: ECDiffieHellmanCng) """
    @property
    def ClientDiffieHellmanKey(self): # -> ECDiffieHellmanCng
        """ Get: ClientDiffieHellmanKey(self: SqlEnclaveAttestationParameters) -> ECDiffieHellmanCng """
        ...

    @property
    def Protocol(self) -> int:
        """ Get: Protocol(self: SqlEnclaveAttestationParameters) -> int """
        ...


    def GetInput(self) -> Array:
        """ GetInput(self: SqlEnclaveAttestationParameters) -> Array[Byte] """
        ...


class SqlEnclaveSession: # skipped bases: <type 'object'>, <type 'object'>
    """ SqlEnclaveSession(sessionKey: Array[Byte], sessionId: Int64) """
    @property
    def SessionId(self) -> Int64:
        """ Get: SessionId(self: SqlEnclaveSession) -> Int64 """
        ...


    def GetSessionKey(self) -> Array:
        """ GetSessionKey(self: SqlEnclaveSession) -> Array[Byte] """
        ...


class SqlError: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Class(self) -> Byte:
        """ Get: Class(self: SqlError) -> Byte """
        ...

    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: SqlError) -> int """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: SqlError) -> str """
        ...

    @property
    def Number(self) -> int:
        """ Get: Number(self: SqlError) -> int """
        ...

    @property
    def Procedure(self) -> str:
        """ Get: Procedure(self: SqlError) -> str """
        ...

    @property
    def Server(self) -> str:
        """ Get: Server(self: SqlError) -> str """
        ...

    @property
    def Source(self) -> str:
        """ Get: Source(self: SqlError) -> str """
        ...

    @property
    def State(self) -> Byte:
        """ Get: State(self: SqlError) -> Byte """
        ...


    def ToString(self) -> str:
        """ ToString(self: SqlError) -> str """
        ...


class SqlErrorCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SqlErrorCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class SqlException(DbException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def Class(self) -> Byte:
        """ Get: Class(self: SqlException) -> Byte """
        ...

    @property
    def ClientConnectionId(self) -> Guid:
        """ Get: ClientConnectionId(self: SqlException) -> Guid """
        ...

    @property
    def Errors(self) -> SqlErrorCollection:
        """ Get: Errors(self: SqlException) -> SqlErrorCollection """
        ...

    @property
    def LineNumber(self) -> int:
        """ Get: LineNumber(self: SqlException) -> int """
        ...

    @property
    def Number(self) -> int:
        """ Get: Number(self: SqlException) -> int """
        ...

    @property
    def Procedure(self) -> str:
        """ Get: Procedure(self: SqlException) -> str """
        ...

    @property
    def Server(self) -> str:
        """ Get: Server(self: SqlException) -> str """
        ...

    @property
    def State(self) -> Byte:
        """ Get: State(self: SqlException) -> Byte """
        ...


    SerializeObjectState = ...


class SqlInfoMessageEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Errors(self) -> SqlErrorCollection:
        """ Get: Errors(self: SqlInfoMessageEventArgs) -> SqlErrorCollection """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: SqlInfoMessageEventArgs) -> str """
        ...

    @property
    def Source(self) -> str:
        """ Get: Source(self: SqlInfoMessageEventArgs) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: SqlInfoMessageEventArgs) -> str """
        ...


class SqlInfoMessageEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SqlInfoMessageEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SqlInfoMessageEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SqlInfoMessageEventHandler, sender: object, e: SqlInfoMessageEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SqlInfoMessageEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SqlInfoMessageEventArgs): # -> 
        """ Invoke(self: SqlInfoMessageEventHandler, sender: object, e: SqlInfoMessageEventArgs) """
        ...


class SqlNotificationEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SqlNotificationEventArgs(type: SqlNotificationType, info: SqlNotificationInfo, source: SqlNotificationSource) """
    @property
    def Info(self) -> SqlNotificationInfo:
        """ Get: Info(self: SqlNotificationEventArgs) -> SqlNotificationInfo """
        ...

    @property
    def Source(self) -> SqlNotificationSource:
        """ Get: Source(self: SqlNotificationEventArgs) -> SqlNotificationSource """
        ...

    @property
    def Type(self) -> SqlNotificationType:
        """ Get: Type(self: SqlNotificationEventArgs) -> SqlNotificationType """
        ...


    def __new__(cls, type:SqlNotificationType, info:SqlNotificationInfo, source:SqlNotificationSource) -> Self:
        """ __new__(cls: type, type: SqlNotificationType, info: SqlNotificationInfo, source: SqlNotificationSource) """
        ...


class SqlNotificationInfo(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlNotificationInfo, values: AlreadyChanged (-2), Alter (5), Delete (3), Drop (4), Error (7), Expired (12), Insert (1), Invalid (9), Isolation (11), Merge (16), Options (10), PreviousFire (14), Query (8), Resource (13), Restart (6), TemplateLimit (15), Truncate (0), Unknown (-1), Update (2) """
    AlreadyChanged: SqlNotificationInfo = ...
    Alter: SqlNotificationInfo = ...
    Delete: SqlNotificationInfo = ...
    Drop: SqlNotificationInfo = ...
    Error: SqlNotificationInfo = ...
    Expired: SqlNotificationInfo = ...
    Insert: SqlNotificationInfo = ...
    Invalid: SqlNotificationInfo = ...
    Isolation: SqlNotificationInfo = ...
    Merge: SqlNotificationInfo = ...
    Options: SqlNotificationInfo = ...
    PreviousFire: SqlNotificationInfo = ...
    Query: SqlNotificationInfo = ...
    Resource: SqlNotificationInfo = ...
    Restart: SqlNotificationInfo = ...
    TemplateLimit: SqlNotificationInfo = ...
    Truncate: SqlNotificationInfo = ...
    Unknown: SqlNotificationInfo = ...
    Update: SqlNotificationInfo = ...
    value__ = ...


class SqlNotificationSource(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlNotificationSource, values: Client (-2), Data (0), Database (3), Environment (6), Execution (7), Object (2), Owner (8), Statement (5), System (4), Timeout (1), Unknown (-1) """
    Client: SqlNotificationSource = ...
    Data: SqlNotificationSource = ...
    Database: SqlNotificationSource = ...
    Environment: SqlNotificationSource = ...
    Execution: SqlNotificationSource = ...
    Object: SqlNotificationSource = ...
    Owner: SqlNotificationSource = ...
    Statement: SqlNotificationSource = ...
    System: SqlNotificationSource = ...
    Timeout: SqlNotificationSource = ...
    Unknown: SqlNotificationSource = ...
    value__ = ...


class SqlNotificationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SqlNotificationType, values: Change (0), Subscribe (1), Unknown (-1) """
    Change: SqlNotificationType = ...
    Subscribe: SqlNotificationType = ...
    Unknown: SqlNotificationType = ...
    value__ = ...


class SqlParameter(ICloneable, DbParameter): # skipped bases: <type 'IDataParameter'>, <type 'IDbDataParameter'>, <type 'object'>
    """
    SqlParameter()
    SqlParameter(parameterName: str, dbType: SqlDbType, size: int, direction: ParameterDirection, isNullable: bool, precision: Byte, scale: Byte, sourceColumn: str, sourceVersion: DataRowVersion, value: object)
    SqlParameter(parameterName: str, dbType: SqlDbType, size: int, direction: ParameterDirection, precision: Byte, scale: Byte, sourceColumn: str, sourceVersion: DataRowVersion, sourceColumnNullMapping: bool, value: object, xmlSchemaCollectionDatabase: str, xmlSchemaCollectionOwningSchema: str, xmlSchemaCollectionName: str)
    SqlParameter(parameterName: str, dbType: SqlDbType)
    SqlParameter(parameterName: str, value: object)
    SqlParameter(parameterName: str, dbType: SqlDbType, size: int)
    SqlParameter(parameterName: str, dbType: SqlDbType, size: int, sourceColumn: str)
    """
    @property
    def CompareInfo(self) -> SqlCompareOptions:
        """
        Get: CompareInfo(self: SqlParameter) -> SqlCompareOptions
        Set: CompareInfo(self: SqlParameter) = value
        """
        ...

    @property
    def ForceColumnEncryption(self) -> bool:
        """
        Get: ForceColumnEncryption(self: SqlParameter) -> bool
        Set: ForceColumnEncryption(self: SqlParameter) = value
        """
        ...

    @property
    def LocaleId(self) -> int:
        """
        Get: LocaleId(self: SqlParameter) -> int
        Set: LocaleId(self: SqlParameter) = value
        """
        ...

    @property
    def Offset(self) -> int:
        """
        Get: Offset(self: SqlParameter) -> int
        Set: Offset(self: SqlParameter) = value
        """
        ...

    @property
    def SqlDbType(self) -> SqlDbType:
        """
        Get: SqlDbType(self: SqlParameter) -> SqlDbType
        Set: SqlDbType(self: SqlParameter) = value
        """
        ...

    @property
    def SqlValue(self) -> object:
        """
        Get: SqlValue(self: SqlParameter) -> object
        Set: SqlValue(self: SqlParameter) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: SqlParameter) -> str
        Set: TypeName(self: SqlParameter) = value
        """
        ...

    @property
    def UdtTypeName(self) -> str:
        """
        Get: UdtTypeName(self: SqlParameter) -> str
        Set: UdtTypeName(self: SqlParameter) = value
        """
        ...

    @property
    def XmlSchemaCollectionDatabase(self) -> str:
        """
        Get: XmlSchemaCollectionDatabase(self: SqlParameter) -> str
        Set: XmlSchemaCollectionDatabase(self: SqlParameter) = value
        """
        ...

    @property
    def XmlSchemaCollectionName(self) -> str:
        """
        Get: XmlSchemaCollectionName(self: SqlParameter) -> str
        Set: XmlSchemaCollectionName(self: SqlParameter) = value
        """
        ...

    @property
    def XmlSchemaCollectionOwningSchema(self) -> str:
        """
        Get: XmlSchemaCollectionOwningSchema(self: SqlParameter) -> str
        Set: XmlSchemaCollectionOwningSchema(self: SqlParameter) = value
        """
        ...


    def ResetSqlDbType(self): # -> 
        """ ResetSqlDbType(self: SqlParameter) """
        ...

    def ToString(self) -> str:
        """ ToString(self: SqlParameter) -> str """
        ...

    def __new__(cls, parameterName:str = ..., *__args:SqlDbType) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parameterName: str, dbType: SqlDbType, size: int, direction: ParameterDirection, isNullable: bool, precision: Byte, scale: Byte, sourceColumn: str, sourceVersion: DataRowVersion, value: object)
        __new__(cls: type, parameterName: str, dbType: SqlDbType, size: int, direction: ParameterDirection, precision: Byte, scale: Byte, sourceColumn: str, sourceVersion: DataRowVersion, sourceColumnNullMapping: bool, value: object, xmlSchemaCollectionDatabase: str, xmlSchemaCollectionOwningSchema: str, xmlSchemaCollectionName: str)
        __new__(cls: type, parameterName: str, dbType: SqlDbType)
        __new__(cls: type, parameterName: str, value: object)
        __new__(cls: type, parameterName: str, dbType: SqlDbType, size: int)
        __new__(cls: type, parameterName: str, dbType: SqlDbType, size: int, sourceColumn: str)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class SqlParameterCollection(DbParameterCollection): # skipped bases: <type 'IDataParameterCollection'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def AddWithValue(self, parameterName:str, value:object) -> SqlParameter:
        """ AddWithValue(self: SqlParameterCollection, parameterName: str, value: object) -> SqlParameter """
        ...


class SqlProviderServices(DbProviderServices): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SingletonInstance(self) -> SqlProviderServices:
        """ Get: SingletonInstance() -> SqlProviderServices """
        ...




class SqlRowsCopiedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SqlRowsCopiedEventArgs(rowsCopied: Int64) """
    @property
    def Abort(self) -> bool:
        """
        Get: Abort(self: SqlRowsCopiedEventArgs) -> bool
        Set: Abort(self: SqlRowsCopiedEventArgs) = value
        """
        ...

    @property
    def RowsCopied(self) -> Int64:
        """ Get: RowsCopied(self: SqlRowsCopiedEventArgs) -> Int64 """
        ...


    def __new__(cls, rowsCopied:Int64) -> Self:
        """ __new__(cls: type, rowsCopied: Int64) """
        ...


class SqlRowsCopiedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SqlRowsCopiedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SqlRowsCopiedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SqlRowsCopiedEventHandler, sender: object, e: SqlRowsCopiedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SqlRowsCopiedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SqlRowsCopiedEventArgs): # -> 
        """ Invoke(self: SqlRowsCopiedEventHandler, sender: object, e: SqlRowsCopiedEventArgs) """
        ...


class SqlRowUpdatedEventArgs(RowUpdatedEventArgs): # skipped bases: <type 'object'>
    """ SqlRowUpdatedEventArgs(row: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping) """
    pass

class SqlRowUpdatedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SqlRowUpdatedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SqlRowUpdatedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SqlRowUpdatedEventHandler, sender: object, e: SqlRowUpdatedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SqlRowUpdatedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SqlRowUpdatedEventArgs): # -> 
        """ Invoke(self: SqlRowUpdatedEventHandler, sender: object, e: SqlRowUpdatedEventArgs) """
        ...


class SqlRowUpdatingEventArgs(RowUpdatingEventArgs): # skipped bases: <type 'object'>
    """ SqlRowUpdatingEventArgs(row: DataRow, command: IDbCommand, statementType: StatementType, tableMapping: DataTableMapping) """
    pass

class SqlRowUpdatingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SqlRowUpdatingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SqlRowUpdatingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SqlRowUpdatingEventHandler, sender: object, e: SqlRowUpdatingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SqlRowUpdatingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SqlRowUpdatingEventArgs): # -> 
        """ Invoke(self: SqlRowUpdatingEventHandler, sender: object, e: SqlRowUpdatingEventArgs) """
        ...


class SqlTransaction(DbTransaction): # skipped bases: <type 'IDisposable'>, <type 'IDbTransaction'>, <type 'object'>
    """ no doc """
    def Save(self, savePointName:str): # -> 
        """ Save(self: SqlTransaction, savePointName: str) """
        ...


