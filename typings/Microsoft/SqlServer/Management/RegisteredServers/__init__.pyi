# encoding: utf-8
# module Microsoft.SqlServer.Management.RegisteredServers calls itself RegisteredServers
# from Microsoft.SqlServer.Management.RegisteredServers, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Common import SqlSecureString

from Microsoft.SqlServer.Management.Common import (IRenamable, ISfcConnection, 
    ServerConnection, ServerType, SqlServerManagementException)

from Microsoft.SqlServer.Management.Sdk.Sfc import (ISfcAlterable, 
    ISfcCreatable, ISfcDomain, ISfcDroppable, ISfcMovable, ISfcRenamable, 
    ISfcValidate, SfcCollatedDictionaryCollection, SfcInstance, 
    SfcObjectFactory)

from System import Enum, EventArgs

from System.Collections.Generic import List

from typing import Self

"""The following names are not found in the module: BoundEvent, Key, field#
"""

# no functions
# classes

class CredentialPersistenceType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CredentialPersistenceType, values: None (0), PersistLoginName (1), PersistLoginNameAndPassword (2) """
    PersistLoginName: CredentialPersistenceType = ...
    PersistLoginNameAndPassword: CredentialPersistenceType = ...
    value__ = ...


class DuplicateFoundEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DuplicateFoundEventArgs() """
    @property
    def ApplyToAll(self) -> bool:
        """
        Get: ApplyToAll(self: DuplicateFoundEventArgs) -> bool
        Set: ApplyToAll(self: DuplicateFoundEventArgs) = value
        """
        ...

    @property
    def Cancel(self) -> bool:
        """
        Get: Cancel(self: DuplicateFoundEventArgs) -> bool
        Set: Cancel(self: DuplicateFoundEventArgs) = value
        """
        ...

    @property
    def Confirm(self) -> bool:
        """
        Get: Confirm(self: DuplicateFoundEventArgs) -> bool
        Set: Confirm(self: DuplicateFoundEventArgs) = value
        """
        ...



class RegisteredServerException(SqlServerManagementException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RegisteredServerException()
    RegisteredServerException(message: str)
    RegisteredServerException(message: str, innerException: Exception)
    """
    @property
    def ProdVer(self):
        ...

    @property
    def RegisteredServerExceptionType(self) -> RegisteredServerExceptionType:
        """ Get: RegisteredServerExceptionType(self: RegisteredServerException) -> RegisteredServerExceptionType """
        ...


    def Init(self, *args): #cannot find CLR method
        """ Init(self: RegisteredServerException) """
        ...

    def SetHelpContext(self, *args): #cannot find CLR method
        """ SetHelpContext(self: RegisteredServerException, resource: str) -> RegisteredServerException """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    SerializeObjectState = ...


class InvalidSqlServer2005StoreFormatException(RegisteredServerException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidSqlServer2005StoreFormatException()
    InvalidSqlServer2005StoreFormatException(message: str)
    InvalidSqlServer2005StoreFormatException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class RegisteredServer(IRenamable, ISfcCreatable, ISfcDroppable, ISfcRenamable, ISfcMovable, SfcInstance, ISfcValidate, ISfcAlterable): # skipped bases: <type 'ICreatable'>, <type 'IAlterable'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'INotifyPropertyChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'IDroppable'>, <type 'object'>
    """
    RegisteredServer()
    RegisteredServer(name: str)
    RegisteredServer(parent: ServerGroup, name: str)
    """
    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: RegisteredServer) -> str
        Set: ConnectionString(self: RegisteredServer) = value
        """
        ...

    @property
    def ConnectionStringWithEncryptedPassword(self) -> str:
        """ Get: ConnectionStringWithEncryptedPassword(self: RegisteredServer) -> str """
        ...

    @property
    def CredentialPersistenceType(self) -> CredentialPersistenceType:
        """
        Get: CredentialPersistenceType(self: RegisteredServer) -> CredentialPersistenceType
        Set: CredentialPersistenceType(self: RegisteredServer) = value
        """
        ...

    @property
    def CustomConnectionColorArgb(self) -> int:
        """
        Get: CustomConnectionColorArgb(self: RegisteredServer) -> int
        Set: CustomConnectionColorArgb(self: RegisteredServer) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: RegisteredServer) -> str
        Set: Description(self: RegisteredServer) = value
        """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: RegisteredServer) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: RegisteredServer) -> Key """
        ...

    @property
    def IsDropped(self) -> bool:
        """ Get: IsDropped(self: RegisteredServer) -> bool """
        ...

    @property
    def IsLocal(self) -> bool:
        """ Get: IsLocal(self: RegisteredServer) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: RegisteredServer) -> str """
        ...

    @property
    def OtherParams(self) -> str:
        """
        Get: OtherParams(self: RegisteredServer) -> str
        Set: OtherParams(self: RegisteredServer) = value
        """
        ...

    @property
    def SecureConnectionString(self) -> SqlSecureString:
        """
        Get: SecureConnectionString(self: RegisteredServer) -> SqlSecureString
        Set: SecureConnectionString(self: RegisteredServer) = value
        """
        ...

    @property
    def ServerName(self) -> str:
        """
        Get: ServerName(self: RegisteredServer) -> str
        Set: ServerName(self: RegisteredServer) = value
        """
        ...

    @property
    def ServerType(self) -> ServerType:
        """ Get: ServerType(self: RegisteredServer) -> ServerType """
        ...

    @property
    def UseCustomConnectionColor(self) -> bool:
        """
        Get: UseCustomConnectionColor(self: RegisteredServer) -> bool
        Set: UseCustomConnectionColor(self: RegisteredServer) = value
        """
        ...


    def Alter(self): # -> 
        """ Alter(self: RegisteredServer) """
        ...

    def Create(self): # -> 
        """ Create(self: RegisteredServer) """
        ...

    def Drop(self): # -> 
        """ Drop(self: RegisteredServer) """
        ...

    def Export(self, file:str, cpt:CredentialPersistenceType): # -> 
        """ Export(self: RegisteredServer, file: str, cpt: CredentialPersistenceType) """
        ...

    def GetConnectionObject(self) -> ISfcConnection:
        """ GetConnectionObject(self: RegisteredServer) -> ISfcConnection """
        ...

    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        __new__(cls: type, parent: ServerGroup, name: str)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class RegisteredServerCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection[RegisteredServer]'>, <type 'ISfcCollection'>, <type 'IEnumerable[RegisteredServer]'>, <type 'IListSource'>, <type 'ICollection'>, <type 'IComparer[Key]'>, <type 'object'>
    """ RegisteredServerCollection(parent: ServerGroup, customComparer: IComparer[str]) """
    pass

class RegisteredServerExceptionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RegisteredServerExceptionType, values: RegisteredServerException (0) """
    RegisteredServerException: RegisteredServerExceptionType = ...
    value__ = ...


class ServerGroupParent(SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ no doc """
    propertyChanged = ...
    propertyMetadataChanged = ...


class RegisteredServersStore(ISfcDomain, ServerGroupParent): # skipped bases: <type 'ISfcDomainLite'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'INotifyPropertyChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'ISfcHasConnection'>, <type 'object'>
    """
    RegisteredServersStore()
    RegisteredServersStore(sharedRegisteredServersStoreConnection: ServerConnection)
    """
    @property
    def AnalysisServicesServerGroup(self) -> ServerGroup:
        """ Get: AnalysisServicesServerGroup(self: RegisteredServersStore) -> ServerGroup """
        ...

    @property
    def AnalysisServicesServerGroupName(self) -> str:
        """ Get: AnalysisServicesServerGroupName(self: RegisteredServersStore) -> str """
        ...

    @property
    def CentralManagementServerGroup(self) -> ServerGroup:
        """ Get: CentralManagementServerGroup(self: RegisteredServersStore) -> ServerGroup """
        ...

    @property
    def CentralManagementServerGroupName(self) -> str:
        """ Get: CentralManagementServerGroupName(self: RegisteredServersStore) -> str """
        ...

    @property
    def CentralManagementServersDisplayName(self) -> str:
        """ Get: CentralManagementServersDisplayName() -> str """
        ...

    @property
    def DatabaseEngineServerGroup(self) -> ServerGroup:
        """ Get: DatabaseEngineServerGroup(self: RegisteredServersStore) -> ServerGroup """
        ...

    @property
    def DatabaseEngineServerGroupName(self) -> str:
        """ Get: DatabaseEngineServerGroupName(self: RegisteredServersStore) -> str """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: RegisteredServersStore) -> str """
        ...

    @property
    def DomainInstanceName(self) -> str:
        """ Get: DomainInstanceName(self: RegisteredServersStore) -> str """
        ...

    @property
    def DomainName(self) -> str:
        """ Get: DomainName(self: RegisteredServersStore) -> str """
        ...

    @property
    def IntegrationServicesServerGroup(self) -> ServerGroup:
        """ Get: IntegrationServicesServerGroup(self: RegisteredServersStore) -> ServerGroup """
        ...

    @property
    def IntegrationServicesServerGroupName(self) -> str:
        """ Get: IntegrationServicesServerGroupName(self: RegisteredServersStore) -> str """
        ...

    @property
    def IsLocal(self) -> bool:
        """ Get: IsLocal(self: RegisteredServersStore) -> bool """
        ...

    @property
    def LocalFileStore(self) -> RegisteredServersStore:
        """ Get: LocalFileStore() -> RegisteredServersStore """
        ...

    @property
    def LocalServerStoreDisplayName(self) -> str:
        """ Get: LocalServerStoreDisplayName() -> str """
        ...

    @property
    def ReportingServicesServerGroup(self) -> ServerGroup:
        """ Get: ReportingServicesServerGroup(self: RegisteredServersStore) -> ServerGroup """
        ...

    @property
    def ReportingServicesServerGroupName(self) -> str:
        """ Get: ReportingServicesServerGroupName(self: RegisteredServersStore) -> str """
        ...

    @property
    def ServerConnection(self) -> ServerConnection:
        """ Get: ServerConnection(self: RegisteredServersStore) -> ServerConnection """
        ...

    @property
    def ServerGroups(self) -> ServerGroupCollection:
        """ Get: ServerGroups(self: RegisteredServersStore) -> ServerGroupCollection """
        ...

    @property
    def SqlServerCompactEditionServerGroup(self) -> ServerGroup:
        """ Get: SqlServerCompactEditionServerGroup(self: RegisteredServersStore) -> ServerGroup """
        ...

    @property
    def SqlServerCompactEditionServerGroupName(self) -> str:
        """ Get: SqlServerCompactEditionServerGroupName(self: RegisteredServersStore) -> str """
        ...


    def ExceptionDelegate(self, *args): #cannot find CLR method
        """ ExceptionDelegate(object: object, method: IntPtr) """
        ...

    def Key(self, *args): #cannot find CLR method
        """ Key() """
        ...

    @staticmethod
    def ReloadLocalFileStore(): # -> 
        """ ReloadLocalFileStore() """
        ...

    def UpgradeFromSqlServer2005(self, downlevelFile:str): # -> 
        """ UpgradeFromSqlServer2005(self: RegisteredServersStore, downlevelFile: str) """
        ...

    def __new__(cls, sharedRegisteredServersStoreConnection:ServerConnection = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, sharedRegisteredServersStoreConnection: ServerConnection)
        """
        ...

    LocalFileStoreReloaded = ...
    propertyChanged = ...
    propertyMetadataChanged = ...


class ServerGroup(ServerGroupParent, IRenamable, ISfcCreatable, ISfcDroppable, ISfcRenamable, ISfcMovable, ISfcValidate, ISfcAlterable): # skipped bases: <type 'ICreatable'>, <type 'IAlterable'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'INotifyPropertyChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'IDroppable'>, <type 'object'>
    """
    ServerGroup()
    ServerGroup(name: str)
    ServerGroup(parent: ServerGroup, name: str)
    """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: ServerGroup) -> str
        Set: Description(self: ServerGroup) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: ServerGroup) -> str """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: ServerGroup) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: ServerGroup) -> Key """
        ...

    @property
    def IsDropped(self) -> bool:
        """ Get: IsDropped(self: ServerGroup) -> bool """
        ...

    @property
    def IsLocal(self) -> bool:
        """ Get: IsLocal(self: ServerGroup) -> bool """
        ...

    @property
    def IsSystemServerGroup(self) -> bool:
        """ Get: IsSystemServerGroup(self: ServerGroup) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ServerGroup) -> str """
        ...

    @property
    def Parent(self) -> ServerGroupParent:
        """
        Get: Parent(self: ServerGroup) -> ServerGroupParent
        Set: Parent(self: ServerGroup) = value
        """
        ...

    @property
    def RegisteredServers(self) -> RegisteredServerCollection:
        """ Get: RegisteredServers(self: ServerGroup) -> RegisteredServerCollection """
        ...

    @property
    def ServerGroups(self) -> ServerGroupCollection:
        """ Get: ServerGroups(self: ServerGroup) -> ServerGroupCollection """
        ...

    @property
    def ServerType(self) -> ServerType:
        """ Get: ServerType(self: ServerGroup) -> ServerType """
        ...


    def Alter(self): # -> 
        """ Alter(self: ServerGroup) """
        ...

    def Create(self): # -> 
        """ Create(self: ServerGroup) """
        ...

    def Drop(self): # -> 
        """ Drop(self: ServerGroup) """
        ...

    def Export(self, file:str, cpt:CredentialPersistenceType): # -> 
        """ Export(self: ServerGroup, file: str, cpt: CredentialPersistenceType) """
        ...

    def GetDescendantRegisteredServers(self) -> List:
        """ GetDescendantRegisteredServers(self: ServerGroup) -> List[RegisteredServer] """
        ...

    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Import(self, file:str): # -> 
        """ Import(self: ServerGroup, file: str) """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        __new__(cls: type, parent: ServerGroup, name: str)
        """
        ...

    DuplicateFound = ...
    propertyChanged = ...
    propertyMetadataChanged = ...


class ServerGroupCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'IEnumerable'>, <type 'IComparer[Key]'>, <type 'ISfcCollection'>, <type 'IEnumerable[ServerGroup]'>, <type 'IListSource'>, <type 'ICollection'>, <type 'ICollection[ServerGroup]'>, <type 'object'>
    """ ServerGroupCollection(parent: ServerGroupParent, customComparer: IComparer[str]) """
    pass

