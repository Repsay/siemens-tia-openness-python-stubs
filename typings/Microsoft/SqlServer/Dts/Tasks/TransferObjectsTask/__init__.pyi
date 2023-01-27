# encoding: utf-8
# module Microsoft.SqlServer.Dts.Tasks.TransferObjectsTask calls itself TransferObjectsTask
# from Microsoft.SqlServer.TransferObjectsTask, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Smo import Database, Login, Server

from System import Enum, ICloneable, Int64

from System.Collections import ArrayList, IEqualityComparer

from System.Collections.Generic import Dictionary, List

from System.Collections.ObjectModel import KeyedCollection

from System.Collections.Specialized import StringCollection

from System.Threading.Tasks import Task

from typing import Tuple as Tuple_

"""The following names are not found in the module: (IDTSBreakpointSite, 
    IDTSComponentPersist, IDTSDowngradableObject, IDTSInfoEvents, field#)
"""

# no functions
# classes

class CopyingMechanism(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CopyingMechanism, values: CopyAllAtRunTime (1), CopyAllLoginsUsedBySelectedDatabase (2), CopyNone (0), CopySelected (3) """
    CopyAllAtRunTime: CopyingMechanism = ...
    CopyAllLoginsUsedBySelectedDatabase: CopyingMechanism = ...
    CopyNone: CopyingMechanism = ...
    CopySelected: CopyingMechanism = ...
    value__ = ...


class DatabaseCopyMethod(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DatabaseCopyMethod, values: CopyToDestination (2), MoveToDestination (1), None (0) """
    CopyToDestination: DatabaseCopyMethod = ...
    MoveToDestination: DatabaseCopyMethod = ...
    value__ = ...


class DatabaseFile: # skipped bases: <type 'object'>, <type 'object'>
    """ DatabaseFile() """
    @property
    def DatabaseFileSize(self) -> Int64:
        """
        Get: DatabaseFileSize(self: DatabaseFile) -> Int64
        Set: DatabaseFileSize(self: DatabaseFile) = value
        """
        ...

    @property
    def DestinationFilePath(self) -> str:
        """
        Get: DestinationFilePath(self: DatabaseFile) -> str
        Set: DestinationFilePath(self: DatabaseFile) = value
        """
        ...

    @property
    def FileType(self) -> DatabaseFileType:
        """
        Get: FileType(self: DatabaseFile) -> DatabaseFileType
        Set: FileType(self: DatabaseFile) = value
        """
        ...

    @property
    def SourceFilePath(self) -> str:
        """
        Get: SourceFilePath(self: DatabaseFile) -> str
        Set: SourceFilePath(self: DatabaseFile) = value
        """
        ...

    @property
    def SourceSharePath(self) -> str:
        """
        Get: SourceSharePath(self: DatabaseFile) -> str
        Set: SourceSharePath(self: DatabaseFile) = value
        """
        ...



class DatabaseFileCollection(ArrayList): # skipped bases: <type 'ICloneable'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DatabaseFileCollection() """
    pass

class DatabaseFileType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DatabaseFileType, values: DatabaseFile (0), FilestreamFile (2), LogFile (1), MemoryOptimizedFile (3) """
    DatabaseFile: DatabaseFileType = ...
    FilestreamFile: DatabaseFileType = ...
    LogFile: DatabaseFileType = ...
    MemoryOptimizedFile: DatabaseFileType = ...
    value__ = ...


class DatabaseInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ DatabaseInfo() """
    @property
    def DatabaseFiles(self) -> DatabaseFileCollection:
        """
        Get: DatabaseFiles(self: DatabaseInfo) -> DatabaseFileCollection
        Set: DatabaseFiles(self: DatabaseInfo) = value
        """
        ...

    @property
    def DatabaseName(self) -> str:
        """
        Get: DatabaseName(self: DatabaseInfo) -> str
        Set: DatabaseName(self: DatabaseInfo) = value
        """
        ...

    @property
    def DestinationDatabaseExists(self) -> ExistDestinationDatabase:
        """
        Get: DestinationDatabaseExists(self: DatabaseInfo) -> ExistDestinationDatabase
        Set: DestinationDatabaseExists(self: DatabaseInfo) = value
        """
        ...

    @property
    def DestinationDatabaseName(self) -> str:
        """
        Get: DestinationDatabaseName(self: DatabaseInfo) -> str
        Set: DestinationDatabaseName(self: DatabaseInfo) = value
        """
        ...

    @property
    def OverwriteDatabaseFile(self) -> bool:
        """
        Get: OverwriteDatabaseFile(self: DatabaseInfo) -> bool
        Set: OverwriteDatabaseFile(self: DatabaseInfo) = value
        """
        ...

    @property
    def TypeOfCopy(self) -> DatabaseCopyMethod:
        """
        Get: TypeOfCopy(self: DatabaseInfo) -> DatabaseCopyMethod
        Set: TypeOfCopy(self: DatabaseInfo) = value
        """
        ...



class DatabaseInfoCollection(ArrayList): # skipped bases: <type 'ICloneable'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DatabaseInfoCollection() """
    pass

class DatabaseObject: # skipped bases: <type 'object'>, <type 'object'>
    """ DatabaseObject() """
    @property
    def CopyMechanism(self) -> CopyingMechanism:
        """
        Get: CopyMechanism(self: DatabaseObject) -> CopyingMechanism
        Set: CopyMechanism(self: DatabaseObject) = value
        """
        ...

    @property
    def DuplicatePackageFolderStructureInDestination(self) -> bool:
        """
        Get: DuplicatePackageFolderStructureInDestination(self: DatabaseObject) -> bool
        Set: DuplicatePackageFolderStructureInDestination(self: DatabaseObject) = value
        """
        ...

    @property
    def Objects(self) -> StringCollection:
        """
        Get: Objects(self: DatabaseObject) -> StringCollection
        Set: Objects(self: DatabaseObject) = value
        """
        ...

    @property
    def OverWriteExisting(self) -> bool:
        """
        Get: OverWriteExisting(self: DatabaseObject) -> bool
        Set: OverWriteExisting(self: DatabaseObject) = value
        """
        ...

    @property
    def TypeOfObject(self) -> ObjectType:
        """
        Get: TypeOfObject(self: DatabaseObject) -> ObjectType
        Set: TypeOfObject(self: DatabaseObject) = value
        """
        ...



class DatabaseObjectCollection(ArrayList): # skipped bases: <type 'ICloneable'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ DatabaseObjectCollection() """
    pass

class ExistDestinationDatabase(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ExistDestinationDatabase, values: DropExistingAndContinueTransfer (2), StopTransfer (1) """
    DropExistingAndContinueTransfer: ExistDestinationDatabase = ...
    StopTransfer: ExistDestinationDatabase = ...
    value__ = ...


class IDTSTransferObjectsTask: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CopyFullTextCatalogs(self) -> bool:
        """
        Get: CopyFullTextCatalogs(self: IDTSTransferObjectsTask) -> bool
        Set: CopyFullTextCatalogs(self: IDTSTransferObjectsTask) = value
        """
        ...

    @property
    def DatabaseDetails(self) -> DatabaseInfoCollection:
        """
        Get: DatabaseDetails(self: IDTSTransferObjectsTask) -> DatabaseInfoCollection
        Set: DatabaseDetails(self: IDTSTransferObjectsTask) = value
        """
        ...

    @property
    def DatabaseObjects(self) -> DatabaseObjectCollection:
        """
        Get: DatabaseObjects(self: IDTSTransferObjectsTask) -> DatabaseObjectCollection
        Set: DatabaseObjects(self: IDTSTransferObjectsTask) = value
        """
        ...

    @property
    def DestinationServer(self) -> ServerProperty:
        """
        Get: DestinationServer(self: IDTSTransferObjectsTask) -> ServerProperty
        Set: DestinationServer(self: IDTSTransferObjectsTask) = value
        """
        ...

    @property
    def ModeOfTransfer(self) -> TransferType:
        """
        Get: ModeOfTransfer(self: IDTSTransferObjectsTask) -> TransferType
        Set: ModeOfTransfer(self: IDTSTransferObjectsTask) = value
        """
        ...

    @property
    def ReattachDatabaseOnFailure(self) -> bool:
        """
        Get: ReattachDatabaseOnFailure(self: IDTSTransferObjectsTask) -> bool
        Set: ReattachDatabaseOnFailure(self: IDTSTransferObjectsTask) = value
        """
        ...

    @property
    def SourceServer(self) -> ServerProperty:
        """
        Get: SourceServer(self: IDTSTransferObjectsTask) -> ServerProperty
        Set: SourceServer(self: IDTSTransferObjectsTask) = value
        """
        ...



class LoggingMechanismType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LoggingMechanismType, values: LogTextFile (1), LogWindowsEvent (0) """
    LogTextFile: LoggingMechanismType = ...
    LogWindowsEvent: LoggingMechanismType = ...
    value__ = ...


class LoginUsersCollection(Dictionary): # skipped bases: <type 'IReadOnlyDictionary[str, SortedStringArray]'>, <type 'IDictionary[str, SortedStringArray]'>, <type 'ICollection[KeyValuePair[str, SortedStringArray]]'>, <type 'IDictionary'>, <type 'IEnumerable'>, <type 'IEnumerable[KeyValuePair[str, SortedStringArray]]'>, <type 'IDeserializationCallback'>, <type 'IReadOnlyCollection[KeyValuePair[str, SortedStringArray]]'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ LoginUsersCollection() """
    pass

class MappedLogin: # skipped bases: <type 'object'>, <type 'object'>
    """ MappedLogin(sourceServer: Server, destServer: Server, sourceLogin: Login) """
    @property
    def AllMessagesAsString(self) -> str:
        """ Get: AllMessagesAsString(self: MappedLogin) -> str """
        ...

    @property
    def AllowExistingOption(self) -> bool:
        """
        Get: AllowExistingOption(self: MappedLogin) -> bool
        Set: AllowExistingOption(self: MappedLogin) = value
        """
        ...

    @property
    def DestDefaultLoginName(self) -> str:
        """ Get: DestDefaultLoginName(self: MappedLogin) -> str """
        ...

    @property
    def DestExists(self) -> bool:
        """ Get: DestExists(self: MappedLogin) -> bool """
        ...

    @property
    def DestLogin(self) -> Login:
        """ Get: DestLogin(self: MappedLogin) -> Login """
        ...

    @property
    def DestServer(self) -> Server:
        """ Get: DestServer(self: MappedLogin) -> Server """
        ...

    @property
    def DestUseLoginName(self) -> str:
        """
        Get: DestUseLoginName(self: MappedLogin) -> str
        Set: DestUseLoginName(self: MappedLogin) = value
        """
        ...

    @property
    def ErrorMessages(self) -> StringCollection:
        """ Get: ErrorMessages(self: MappedLogin) -> StringCollection """
        ...

    @property
    def InfoMessages(self) -> StringCollection:
        """ Get: InfoMessages(self: MappedLogin) -> StringCollection """
        ...

    @property
    def PreserveSqlSIDOption(self) -> bool:
        """
        Get: PreserveSqlSIDOption(self: MappedLogin) -> bool
        Set: PreserveSqlSIDOption(self: MappedLogin) = value
        """
        ...

    @property
    def Reason(self) -> MappedLoginReason:
        """ Get: Reason(self: MappedLogin) -> MappedLoginReason """
        ...

    @property
    def ReasonString(self) -> str:
        """ Get: ReasonString(self: MappedLogin) -> str """
        ...

    @property
    def SourceDomainName(self) -> str:
        """ Get: SourceDomainName(self: MappedLogin) -> str """
        ...

    @property
    def SourceLogin(self) -> Login:
        """ Get: SourceLogin(self: MappedLogin) -> Login """
        ...

    @property
    def SourceServer(self) -> Server:
        """ Get: SourceServer(self: MappedLogin) -> Server """
        ...

    @property
    def SourceType(self) -> MappedLoginType:
        """ Get: SourceType(self: MappedLogin) -> MappedLoginType """
        ...

    @property
    def SourceUserName(self) -> str:
        """ Get: SourceUserName(self: MappedLogin) -> str """
        ...

    @property
    def Status(self) -> MappedLoginStatus:
        """ Get: Status(self: MappedLogin) -> MappedLoginStatus """
        ...

    @property
    def UseAttachOption(self) -> bool:
        """
        Get: UseAttachOption(self: MappedLogin) -> bool
        Set: UseAttachOption(self: MappedLogin) = value
        """
        ...

    @property
    def WarningMessages(self) -> StringCollection:
        """ Get: WarningMessages(self: MappedLogin) -> StringCollection """
        ...


    @staticmethod
    def DecodeFromString(s, sourceName, destName) -> Tuple_[bool, str, str]:
        """ DecodeFromString(s: str) -> (bool, str, str) """
        ...

    @staticmethod
    def EncodeToString(sourceName:str, destName:str) -> str:
        """ EncodeToString(sourceName: str, destName: str) -> str """
        ...

    @staticmethod
    def GetDatabaseLogins(server:Server, databaseDetails:DatabaseInfoCollection) -> List:
        """ GetDatabaseLogins(server: Server, databaseDetails: DatabaseInfoCollection) -> List[Login] """
        ...

    @staticmethod
    def GetDatabaseUsersFromLogins(server:Server, database:Database, loginNames:StringMappingCollection) -> LoginUsersCollection:
        """ GetDatabaseUsersFromLogins(server: Server, database: Database, loginNames: StringMappingCollection) -> LoginUsersCollection """
        ...

    @staticmethod
    def GetServerLogins(server:Server) -> List:
        """ GetServerLogins(server: Server) -> List[Login] """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: MappedLogin) """
        ...

    def Validate(self) -> bool:
        """ Validate(self: MappedLogin) -> bool """
        ...

    def ValidateWithServerSyntaxCheck(self) -> bool:
        """ ValidateWithServerSyntaxCheck(self: MappedLogin) -> bool """
        ...


class MappedLoginReason(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MappedLoginReason, values: ErrorAttachedSidMismatch (3), ErrorLoginExists (1), ErrorManualAsymmetricKey (7), ErrorManualCertificate (6), ErrorManualCredential (8), ErrorRoleMapping (5), ErrorSidExists (2), ErrorTypeMismatch (4), None (0) """
    ErrorAttachedSidMismatch: MappedLoginReason = ...
    ErrorLoginExists: MappedLoginReason = ...
    ErrorManualAsymmetricKey: MappedLoginReason = ...
    ErrorManualCertificate: MappedLoginReason = ...
    ErrorManualCredential: MappedLoginReason = ...
    ErrorRoleMapping: MappedLoginReason = ...
    ErrorSidExists: MappedLoginReason = ...
    ErrorTypeMismatch: MappedLoginReason = ...
    value__ = ...


class MappedLoginStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MappedLoginStatus, values: Error (2), Manual (3), Ok (1), Unknown (0) """
    Error: MappedLoginStatus = ...
    Manual: MappedLoginStatus = ...
    Ok: MappedLoginStatus = ...
    Unknown: MappedLoginStatus = ...
    value__ = ...


class MappedLoginType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MappedLoginType, values: AsymmetricKey (7), Builtin (1), Certificate (6), SqlAccount (2), Unknown (0), WindowsDomainAccount (5), WindowsInstanceAccount (3), WindowsLocalAccount (4) """
    AsymmetricKey: MappedLoginType = ...
    Builtin: MappedLoginType = ...
    Certificate: MappedLoginType = ...
    SqlAccount: MappedLoginType = ...
    Unknown: MappedLoginType = ...
    value__ = ...
    WindowsDomainAccount: MappedLoginType = ...
    WindowsInstanceAccount: MappedLoginType = ...
    WindowsLocalAccount: MappedLoginType = ...


class MappedServerDistance(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MappedServerDistance, values: DifferentDomain (4), SameDomain (3), SameInstance (1), SameMachine (2), Unknown (0) """
    DifferentDomain: MappedServerDistance = ...
    SameDomain: MappedServerDistance = ...
    SameInstance: MappedServerDistance = ...
    SameMachine: MappedServerDistance = ...
    Unknown: MappedServerDistance = ...
    value__ = ...


class ObjectType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ObjectType, values: TypeCertificate (5), TypeDtsPackage (7), TypeEndPoint (4), TypeErrorMessage (3), TypeFullTextCatalog (6), TypeJob (2), TypeLogin (0), TypeStoredProcedure (1) """
    TypeCertificate: ObjectType = ...
    TypeDtsPackage: ObjectType = ...
    TypeEndPoint: ObjectType = ...
    TypeErrorMessage: ObjectType = ...
    TypeFullTextCatalog: ObjectType = ...
    TypeJob: ObjectType = ...
    TypeLogin: ObjectType = ...
    TypeStoredProcedure: ObjectType = ...
    value__ = ...


class SchedulingMechanism(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SchedulingMechanism, values: RunImmediately (0), RunOnce (1), ScheduledToRunLater (2) """
    RunImmediately: SchedulingMechanism = ...
    RunOnce: SchedulingMechanism = ...
    ScheduledToRunLater: SchedulingMechanism = ...
    value__ = ...


class ServerProperty(ICloneable): # skipped bases: <type 'object'>
    """
    ServerProperty()
    ServerProperty(serverName: str, authType: TypeOfAuthentication, loginName: str, password: str)
    """
    @property
    def AuthenticationType(self) -> TypeOfAuthentication:
        """
        Get: AuthenticationType(self: ServerProperty) -> TypeOfAuthentication
        Set: AuthenticationType(self: ServerProperty) = value
        """
        ...

    @property
    def LoginName(self) -> str:
        """
        Get: LoginName(self: ServerProperty) -> str
        Set: LoginName(self: ServerProperty) = value
        """
        ...

    @property
    def Password(self) -> str:
        """
        Get: Password(self: ServerProperty) -> str
        Set: Password(self: ServerProperty) = value
        """
        ...

    @property
    def SqlServerName(self) -> str:
        """
        Get: SqlServerName(self: ServerProperty) -> str
        Set: SqlServerName(self: ServerProperty) = value
        """
        ...



class ServerVersion(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ServerVersion, values: Denali (11), Katmai (10), SQL14 (12), Version7 (7), Version8 (8), Yukon (9) """
    Denali: ServerVersion = ...
    Katmai: ServerVersion = ...
    SQL14: ServerVersion = ...
    value__ = ...
    Version7: ServerVersion = ...
    Version8: ServerVersion = ...
    Yukon: ServerVersion = ...


class SidCompare(IEqualityComparer): # skipped bases: <type 'object'>
    """ SidCompare() """
    pass

class SidUsersCollection(Dictionary): # skipped bases: <type 'IReadOnlyDictionary[Array[Byte], SortedStringArray]'>, <type 'IDictionary[Array[Byte], SortedStringArray]'>, <type 'IEnumerable[KeyValuePair[Array[Byte], SortedStringArray]]'>, <type 'IEnumerable'>, <type 'IDictionary'>, <type 'IReadOnlyCollection[KeyValuePair[Array[Byte], SortedStringArray]]'>, <type 'IDeserializationCallback'>, <type 'ISerializable'>, <type 'ICollection'>, <type 'ICollection[KeyValuePair[Array[Byte], SortedStringArray]]'>, <type 'object'>
    """
    SidUsersCollection()
    SidUsersCollection(comparer: IEqualityComparer[Array[Byte]])
    """
    pass

class SortedStringArray(KeyedCollection): # skipped bases: <type 'IReadOnlyCollection[str]'>, <type 'IList[str]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IEnumerable[str]'>, <type 'ICollection[str]'>, <type 'IReadOnlyList[str]'>, <type 'ICollection'>, <type 'object'>
    """ SortedStringArray() """
    pass

class StringMappingCollection(Dictionary): # skipped bases: <type 'IReadOnlyDictionary[str, str]'>, <type 'IDictionary[str, str]'>, <type 'IReadOnlyCollection[KeyValuePair[str, str]]'>, <type 'IEnumerable[KeyValuePair[str, str]]'>, <type 'IEnumerable'>, <type 'IDictionary'>, <type 'ICollection[KeyValuePair[str, str]]'>, <type 'ISerializable'>, <type 'ICollection'>, <type 'IDeserializationCallback'>, <type 'object'>
    """ StringMappingCollection() """
    pass

class TransferObjectsTask(IDTSTransferObjectsTask, IDTSBreakpointSite, IDTSDowngradableObject, Task, IDTSComponentPersist): # skipped bases: <type 'IDTSManagedTask'>, <type 'IDTSSuspend'>, <type 'object'>
    """ TransferObjectsTask() """
    @property
    def LogTransferDumps(self) -> bool:
        """
        Get: LogTransferDumps(self: TransferObjectsTask) -> bool
        Set: LogTransferDumps(self: TransferObjectsTask) = value
        """
        ...

    @property
    def SuspendRequired(self) -> bool:
        """
        Get: SuspendRequired(self: TransferObjectsTask) -> bool
        Set: SuspendRequired(self: TransferObjectsTask) = value
        """
        ...


    @staticmethod
    def ExtractServerName(instanceName:str) -> str:
        """ ExtractServerName(instanceName: str) -> str """
        ...

    def OpenConnection(self, server:Server, serverProp:ServerProperty) -> Tuple_[bool, Server]:
        """ OpenConnection(self: TransferObjectsTask, server: Server, serverProp: ServerProperty) -> (bool, Server) """
        ...

    def ResumeExecution(self): # -> 
        """ ResumeExecution(self: TransferObjectsTask) """
        ...

    def SaveToCS(self, events, str:str) -> Tuple_[str, str]: # Not found arg types: {'events': 'IDTSInfoEvents'}
        """ SaveToCS(self: TransferObjectsTask, events: IDTSInfoEvents, str: str) -> (str, str) """
        ...

    def SaveToVB(self, events, persistString:str) -> Tuple_[str, str]: # Not found arg types: {'events': 'IDTSInfoEvents'}
        """ SaveToVB(self: TransferObjectsTask, events: IDTSInfoEvents, persistString: str) -> (str, str) """
        ...

    def SuspendExecution(self): # -> 
        """ SuspendExecution(self: TransferObjectsTask) """
        ...

    def TransferObjectsTaskDebug(self, *args): #cannot find CLR method
        """ enum TransferObjectsTaskDebug, values: DebugBeforeCopyingCertificate (7), DebugBeforeCopyingDatabase (1), DebugBeforeCopyingDtsPackage (9), DebugBeforeCopyingEndPoint (6), DebugBeforeCopyingFullTextCatalog (8), DebugBeforeCopyingJob (4), DebugBeforeCopyingLogin (2), DebugBeforeCopyingMessage (5), DebugBeforeCopyingStoredProcedure (3), DebugBegin (0), DebugEnd (10) """
        ...

    _logTransferDumps = ...


class TransferType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TransferType, values: DetachAttach (1), None (0), SmoTransfer (2) """
    DetachAttach: TransferType = ...
    SmoTransfer: TransferType = ...
    value__ = ...


class TypeOfAuthentication(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TypeOfAuthentication, values: SqlServerAuthentication (1), WindowsAuthentication (0) """
    SqlServerAuthentication: TypeOfAuthentication = ...
    value__ = ...
    WindowsAuthentication: TypeOfAuthentication = ...


class UserSecurityLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UserSecurityLevel, values: NotSysAdmin (1), SysAdmin (0) """
    NotSysAdmin: UserSecurityLevel = ...
    SysAdmin: UserSecurityLevel = ...
    value__ = ...


