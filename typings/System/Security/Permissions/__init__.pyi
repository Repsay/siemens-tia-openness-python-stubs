# encoding: utf-8
# module System.Security.Permissions calls itself Permissions
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Security, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Attribute, Enum, Int64, Version

from System.Collections import ICollection, IEnumerator

from System.Security import (CodeAccessPermission, IPermission, PermissionSet, 
    SecurityElement, SecurityZone)

from System.Security.Cryptography.X509Certificates import X509Certificate

from typing import Self

"""The following names are not found in the module: (
    DataProtectionPermissionFlags, IBuiltInPermission, field#)
"""

# no functions
# classes

class SecurityAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    @property
    def Action(self) -> SecurityAction:
        """
        Get: Action(self: SecurityAttribute) -> SecurityAction
        Set: Action(self: SecurityAttribute) = value
        """
        ...

    @property
    def Unrestricted(self) -> bool:
        """
        Get: Unrestricted(self: SecurityAttribute) -> bool
        Set: Unrestricted(self: SecurityAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: SecurityAttribute) -> IPermission """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, action: SecurityAction) """
        ...


class CodeAccessSecurityAttribute(SecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    pass

class DataProtectionPermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    DataProtectionPermission(state: PermissionState)
    DataProtectionPermission(flag: DataProtectionPermissionFlags)
    """
    @property
    def Flags(self): # -> DataProtectionPermissionFlags
        """
        Get: Flags(self: DataProtectionPermission) -> DataProtectionPermissionFlags
        Set: Flags(self: DataProtectionPermission) = value
        """
        ...


    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, flag: DataProtectionPermissionFlags)
        """
        ...


class DataProtectionPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DataProtectionPermissionAttribute(action: SecurityAction) """
    @property
    def Flags(self): # -> DataProtectionPermissionFlags
        """
        Get: Flags(self: DataProtectionPermissionAttribute) -> DataProtectionPermissionFlags
        Set: Flags(self: DataProtectionPermissionAttribute) = value
        """
        ...

    @property
    def ProtectData(self) -> bool:
        """
        Get: ProtectData(self: DataProtectionPermissionAttribute) -> bool
        Set: ProtectData(self: DataProtectionPermissionAttribute) = value
        """
        ...

    @property
    def ProtectMemory(self) -> bool:
        """
        Get: ProtectMemory(self: DataProtectionPermissionAttribute) -> bool
        Set: ProtectMemory(self: DataProtectionPermissionAttribute) = value
        """
        ...

    @property
    def UnprotectData(self) -> bool:
        """
        Get: UnprotectData(self: DataProtectionPermissionAttribute) -> bool
        Set: UnprotectData(self: DataProtectionPermissionAttribute) = value
        """
        ...

    @property
    def UnprotectMemory(self) -> bool:
        """
        Get: UnprotectMemory(self: DataProtectionPermissionAttribute) -> bool
        Set: UnprotectMemory(self: DataProtectionPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: DataProtectionPermissionAttribute) -> IPermission """
        ...


class DataProtectionPermissionFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DataProtectionPermissionFlags, values: AllFlags (15), NoFlags (0), ProtectData (1), ProtectMemory (4), UnprotectData (2), UnprotectMemory (8) """
    AllFlags: DataProtectionPermissionFlags = ...
    NoFlags: DataProtectionPermissionFlags = ...
    ProtectData: DataProtectionPermissionFlags = ...
    ProtectMemory: DataProtectionPermissionFlags = ...
    UnprotectData: DataProtectionPermissionFlags = ...
    UnprotectMemory: DataProtectionPermissionFlags = ...
    value__ = ...


class IUnrestrictedPermission: # skipped bases: <type 'object'>
    """ no doc """
    def IsUnrestricted(self) -> bool:
        """ IsUnrestricted(self: IUnrestrictedPermission) -> bool """
        ...


class EnvironmentPermission(IUnrestrictedPermission, CodeAccessPermission, IBuiltInPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    EnvironmentPermission(state: PermissionState)
    EnvironmentPermission(flag: EnvironmentPermissionAccess, pathList: str)
    """
    def AddPathList(self, flag:EnvironmentPermissionAccess, pathList:str): # -> 
        """ AddPathList(self: EnvironmentPermission, flag: EnvironmentPermissionAccess, pathList: str) """
        ...

    def GetPathList(self, flag:EnvironmentPermissionAccess) -> str:
        """ GetPathList(self: EnvironmentPermission, flag: EnvironmentPermissionAccess) -> str """
        ...

    def SetPathList(self, flag:EnvironmentPermissionAccess, pathList:str): # -> 
        """ SetPathList(self: EnvironmentPermission, flag: EnvironmentPermissionAccess, pathList: str) """
        ...

    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, flag: EnvironmentPermissionAccess, pathList: str)
        """
        ...


class EnvironmentPermissionAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EnvironmentPermissionAccess, values: AllAccess (3), NoAccess (0), Read (1), Write (2) """
    AllAccess: EnvironmentPermissionAccess = ...
    NoAccess: EnvironmentPermissionAccess = ...
    Read: EnvironmentPermissionAccess = ...
    value__ = ...
    Write: EnvironmentPermissionAccess = ...


class EnvironmentPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EnvironmentPermissionAttribute(action: SecurityAction) """
    @property
    def All(self) -> str:
        """
        Get: All(self: EnvironmentPermissionAttribute) -> str
        Set: All(self: EnvironmentPermissionAttribute) = value
        """
        ...

    @property
    def Read(self) -> str:
        """
        Get: Read(self: EnvironmentPermissionAttribute) -> str
        Set: Read(self: EnvironmentPermissionAttribute) = value
        """
        ...

    @property
    def Write(self) -> str:
        """
        Get: Write(self: EnvironmentPermissionAttribute) -> str
        Set: Write(self: EnvironmentPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: EnvironmentPermissionAttribute) -> IPermission """
        ...


class FileDialogPermission(IUnrestrictedPermission, CodeAccessPermission, IBuiltInPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    FileDialogPermission(state: PermissionState)
    FileDialogPermission(access: FileDialogPermissionAccess)
    """
    @property
    def Access(self) -> FileDialogPermissionAccess:
        """
        Get: Access(self: FileDialogPermission) -> FileDialogPermissionAccess
        Set: Access(self: FileDialogPermission) = value
        """
        ...


    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, access: FileDialogPermissionAccess)
        """
        ...


class FileDialogPermissionAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) FileDialogPermissionAccess, values: None (0), Open (1), OpenSave (3), Save (2) """
    Open: FileDialogPermissionAccess = ...
    OpenSave: FileDialogPermissionAccess = ...
    Save: FileDialogPermissionAccess = ...
    value__ = ...


class FileDialogPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ FileDialogPermissionAttribute(action: SecurityAction) """
    @property
    def Open(self) -> bool:
        """
        Get: Open(self: FileDialogPermissionAttribute) -> bool
        Set: Open(self: FileDialogPermissionAttribute) = value
        """
        ...

    @property
    def Save(self) -> bool:
        """
        Get: Save(self: FileDialogPermissionAttribute) -> bool
        Set: Save(self: FileDialogPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: FileDialogPermissionAttribute) -> IPermission """
        ...


class FileIOPermission(IUnrestrictedPermission, CodeAccessPermission, IBuiltInPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    FileIOPermission(state: PermissionState)
    FileIOPermission(access: FileIOPermissionAccess, path: str)
    FileIOPermission(access: FileIOPermissionAccess, pathList: Array[str])
    FileIOPermission(access: FileIOPermissionAccess, control: AccessControlActions, path: str)
    FileIOPermission(access: FileIOPermissionAccess, control: AccessControlActions, pathList: Array[str])
    """
    @property
    def AllFiles(self) -> FileIOPermissionAccess:
        """
        Get: AllFiles(self: FileIOPermission) -> FileIOPermissionAccess
        Set: AllFiles(self: FileIOPermission) = value
        """
        ...

    @property
    def AllLocalFiles(self) -> FileIOPermissionAccess:
        """
        Get: AllLocalFiles(self: FileIOPermission) -> FileIOPermissionAccess
        Set: AllLocalFiles(self: FileIOPermission) = value
        """
        ...


    def AddPathList(self, access:FileIOPermissionAccess, *__args:str): # -> 
        """ AddPathList(self: FileIOPermission, access: FileIOPermissionAccess, path: str)AddPathList(self: FileIOPermission, access: FileIOPermissionAccess, pathList: Array[str]) """
        ...

    def GetPathList(self, access:FileIOPermissionAccess) -> Array:
        """ GetPathList(self: FileIOPermission, access: FileIOPermissionAccess) -> Array[str] """
        ...

    def SetPathList(self, access:FileIOPermissionAccess, *__args:str): # -> 
        """ SetPathList(self: FileIOPermission, access: FileIOPermissionAccess, path: str)SetPathList(self: FileIOPermission, access: FileIOPermissionAccess, pathList: Array[str]) """
        ...

    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, access: FileIOPermissionAccess, path: str)
        __new__(cls: type, access: FileIOPermissionAccess, pathList: Array[str])
        __new__(cls: type, access: FileIOPermissionAccess, control: AccessControlActions, path: str)
        __new__(cls: type, access: FileIOPermissionAccess, control: AccessControlActions, pathList: Array[str])
        """
        ...


class FileIOPermissionAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) FileIOPermissionAccess, values: AllAccess (15), Append (4), NoAccess (0), PathDiscovery (8), Read (1), Write (2) """
    AllAccess: FileIOPermissionAccess = ...
    Append: FileIOPermissionAccess = ...
    NoAccess: FileIOPermissionAccess = ...
    PathDiscovery: FileIOPermissionAccess = ...
    Read: FileIOPermissionAccess = ...
    value__ = ...
    Write: FileIOPermissionAccess = ...


class FileIOPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ FileIOPermissionAttribute(action: SecurityAction) """
    @property
    def All(self) -> str:
        """
        Get: All(self: FileIOPermissionAttribute) -> str
        Set: All(self: FileIOPermissionAttribute) = value
        """
        ...

    @property
    def AllFiles(self) -> FileIOPermissionAccess:
        """
        Get: AllFiles(self: FileIOPermissionAttribute) -> FileIOPermissionAccess
        Set: AllFiles(self: FileIOPermissionAttribute) = value
        """
        ...

    @property
    def AllLocalFiles(self) -> FileIOPermissionAccess:
        """
        Get: AllLocalFiles(self: FileIOPermissionAttribute) -> FileIOPermissionAccess
        Set: AllLocalFiles(self: FileIOPermissionAttribute) = value
        """
        ...

    @property
    def Append(self) -> str:
        """
        Get: Append(self: FileIOPermissionAttribute) -> str
        Set: Append(self: FileIOPermissionAttribute) = value
        """
        ...

    @property
    def ChangeAccessControl(self) -> str:
        """
        Get: ChangeAccessControl(self: FileIOPermissionAttribute) -> str
        Set: ChangeAccessControl(self: FileIOPermissionAttribute) = value
        """
        ...

    @property
    def PathDiscovery(self) -> str:
        """
        Get: PathDiscovery(self: FileIOPermissionAttribute) -> str
        Set: PathDiscovery(self: FileIOPermissionAttribute) = value
        """
        ...

    @property
    def Read(self) -> str:
        """
        Get: Read(self: FileIOPermissionAttribute) -> str
        Set: Read(self: FileIOPermissionAttribute) = value
        """
        ...

    @property
    def ViewAccessControl(self) -> str:
        """
        Get: ViewAccessControl(self: FileIOPermissionAttribute) -> str
        Set: ViewAccessControl(self: FileIOPermissionAttribute) = value
        """
        ...

    @property
    def ViewAndModify(self) -> str:
        """
        Get: ViewAndModify(self: FileIOPermissionAttribute) -> str
        Set: ViewAndModify(self: FileIOPermissionAttribute) = value
        """
        ...

    @property
    def Write(self) -> str:
        """
        Get: Write(self: FileIOPermissionAttribute) -> str
        Set: Write(self: FileIOPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: FileIOPermissionAttribute) -> IPermission """
        ...


class GacIdentityPermission(CodeAccessPermission, IBuiltInPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    GacIdentityPermission(state: PermissionState)
    GacIdentityPermission()
    """
    def __new__(cls, state:PermissionState = ...) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type)
        """
        ...


class GacIdentityPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ GacIdentityPermissionAttribute(action: SecurityAction) """
    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: GacIdentityPermissionAttribute) -> IPermission """
        ...


class HostProtectionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    HostProtectionAttribute()
    HostProtectionAttribute(action: SecurityAction)
    """
    @property
    def ExternalProcessMgmt(self) -> bool:
        """
        Get: ExternalProcessMgmt(self: HostProtectionAttribute) -> bool
        Set: ExternalProcessMgmt(self: HostProtectionAttribute) = value
        """
        ...

    @property
    def ExternalThreading(self) -> bool:
        """
        Get: ExternalThreading(self: HostProtectionAttribute) -> bool
        Set: ExternalThreading(self: HostProtectionAttribute) = value
        """
        ...

    @property
    def MayLeakOnAbort(self) -> bool:
        """
        Get: MayLeakOnAbort(self: HostProtectionAttribute) -> bool
        Set: MayLeakOnAbort(self: HostProtectionAttribute) = value
        """
        ...

    @property
    def Resources(self) -> HostProtectionResource:
        """
        Get: Resources(self: HostProtectionAttribute) -> HostProtectionResource
        Set: Resources(self: HostProtectionAttribute) = value
        """
        ...

    @property
    def SecurityInfrastructure(self) -> bool:
        """
        Get: SecurityInfrastructure(self: HostProtectionAttribute) -> bool
        Set: SecurityInfrastructure(self: HostProtectionAttribute) = value
        """
        ...

    @property
    def SelfAffectingProcessMgmt(self) -> bool:
        """
        Get: SelfAffectingProcessMgmt(self: HostProtectionAttribute) -> bool
        Set: SelfAffectingProcessMgmt(self: HostProtectionAttribute) = value
        """
        ...

    @property
    def SelfAffectingThreading(self) -> bool:
        """
        Get: SelfAffectingThreading(self: HostProtectionAttribute) -> bool
        Set: SelfAffectingThreading(self: HostProtectionAttribute) = value
        """
        ...

    @property
    def SharedState(self) -> bool:
        """
        Get: SharedState(self: HostProtectionAttribute) -> bool
        Set: SharedState(self: HostProtectionAttribute) = value
        """
        ...

    @property
    def Synchronization(self) -> bool:
        """
        Get: Synchronization(self: HostProtectionAttribute) -> bool
        Set: Synchronization(self: HostProtectionAttribute) = value
        """
        ...

    @property
    def UI(self) -> bool:
        """
        Get: UI(self: HostProtectionAttribute) -> bool
        Set: UI(self: HostProtectionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: HostProtectionAttribute) -> IPermission """
        ...


class HostProtectionResource(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) HostProtectionResource, values: All (511), ExternalProcessMgmt (4), ExternalThreading (16), MayLeakOnAbort (256), None (0), SecurityInfrastructure (64), SelfAffectingProcessMgmt (8), SelfAffectingThreading (32), SharedState (2), Synchronization (1), UI (128) """
    All: HostProtectionResource = ...
    ExternalProcessMgmt: HostProtectionResource = ...
    ExternalThreading: HostProtectionResource = ...
    MayLeakOnAbort: HostProtectionResource = ...
    SecurityInfrastructure: HostProtectionResource = ...
    SelfAffectingProcessMgmt: HostProtectionResource = ...
    SelfAffectingThreading: HostProtectionResource = ...
    SharedState: HostProtectionResource = ...
    Synchronization: HostProtectionResource = ...
    UI: HostProtectionResource = ...
    value__ = ...


class IsolatedStorageContainment(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum IsolatedStorageContainment, values: AdministerIsolatedStorageByUser (112), ApplicationIsolationByMachine (69), ApplicationIsolationByRoamingUser (101), ApplicationIsolationByUser (21), AssemblyIsolationByMachine (64), AssemblyIsolationByRoamingUser (96), AssemblyIsolationByUser (32), DomainIsolationByMachine (48), DomainIsolationByRoamingUser (80), DomainIsolationByUser (16), None (0), UnrestrictedIsolatedStorage (240) """
    AdministerIsolatedStorageByUser: IsolatedStorageContainment = ...
    ApplicationIsolationByMachine: IsolatedStorageContainment = ...
    ApplicationIsolationByRoamingUser: IsolatedStorageContainment = ...
    ApplicationIsolationByUser: IsolatedStorageContainment = ...
    AssemblyIsolationByMachine: IsolatedStorageContainment = ...
    AssemblyIsolationByRoamingUser: IsolatedStorageContainment = ...
    AssemblyIsolationByUser: IsolatedStorageContainment = ...
    DomainIsolationByMachine: IsolatedStorageContainment = ...
    DomainIsolationByRoamingUser: IsolatedStorageContainment = ...
    DomainIsolationByUser: IsolatedStorageContainment = ...
    UnrestrictedIsolatedStorage: IsolatedStorageContainment = ...
    value__ = ...


class IsolatedStoragePermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """ no doc """
    @property
    def UsageAllowed(self) -> IsolatedStorageContainment:
        """
        Get: UsageAllowed(self: IsolatedStoragePermission) -> IsolatedStorageContainment
        Set: UsageAllowed(self: IsolatedStoragePermission) = value
        """
        ...

    @property
    def UserQuota(self) -> Int64:
        """
        Get: UserQuota(self: IsolatedStoragePermission) -> Int64
        Set: UserQuota(self: IsolatedStoragePermission) = value
        """
        ...


    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, state: PermissionState) """
        ...


class IsolatedStorageFilePermission(IBuiltInPermission, IsolatedStoragePermission): # skipped bases: <type 'IPermission'>, <type 'IUnrestrictedPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """ IsolatedStorageFilePermission(state: PermissionState) """
    pass

class IsolatedStoragePermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    @property
    def UsageAllowed(self) -> IsolatedStorageContainment:
        """
        Get: UsageAllowed(self: IsolatedStoragePermissionAttribute) -> IsolatedStorageContainment
        Set: UsageAllowed(self: IsolatedStoragePermissionAttribute) = value
        """
        ...

    @property
    def UserQuota(self) -> Int64:
        """
        Get: UserQuota(self: IsolatedStoragePermissionAttribute) -> Int64
        Set: UserQuota(self: IsolatedStoragePermissionAttribute) = value
        """
        ...



class IsolatedStorageFilePermissionAttribute(IsolatedStoragePermissionAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ IsolatedStorageFilePermissionAttribute(action: SecurityAction) """
    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: IsolatedStorageFilePermissionAttribute) -> IPermission """
        ...


class KeyContainerPermission(IUnrestrictedPermission, CodeAccessPermission, IBuiltInPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    KeyContainerPermission(state: PermissionState)
    KeyContainerPermission(flags: KeyContainerPermissionFlags)
    KeyContainerPermission(flags: KeyContainerPermissionFlags, accessList: Array[KeyContainerPermissionAccessEntry])
    """
    @property
    def AccessEntries(self) -> KeyContainerPermissionAccessEntryCollection:
        """ Get: AccessEntries(self: KeyContainerPermission) -> KeyContainerPermissionAccessEntryCollection """
        ...

    @property
    def Flags(self) -> KeyContainerPermissionFlags:
        """ Get: Flags(self: KeyContainerPermission) -> KeyContainerPermissionFlags """
        ...


    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, flags: KeyContainerPermissionFlags)
        __new__(cls: type, flags: KeyContainerPermissionFlags, accessList: Array[KeyContainerPermissionAccessEntry])
        """
        ...


class KeyContainerPermissionAccessEntry: # skipped bases: <type 'object'>, <type 'object'>
    """
    KeyContainerPermissionAccessEntry(keyContainerName: str, flags: KeyContainerPermissionFlags)
    KeyContainerPermissionAccessEntry(parameters: CspParameters, flags: KeyContainerPermissionFlags)
    KeyContainerPermissionAccessEntry(keyStore: str, providerName: str, providerType: int, keyContainerName: str, keySpec: int, flags: KeyContainerPermissionFlags)
    """
    @property
    def Flags(self) -> KeyContainerPermissionFlags:
        """
        Get: Flags(self: KeyContainerPermissionAccessEntry) -> KeyContainerPermissionFlags
        Set: Flags(self: KeyContainerPermissionAccessEntry) = value
        """
        ...

    @property
    def KeyContainerName(self) -> str:
        """
        Get: KeyContainerName(self: KeyContainerPermissionAccessEntry) -> str
        Set: KeyContainerName(self: KeyContainerPermissionAccessEntry) = value
        """
        ...

    @property
    def KeySpec(self) -> int:
        """
        Get: KeySpec(self: KeyContainerPermissionAccessEntry) -> int
        Set: KeySpec(self: KeyContainerPermissionAccessEntry) = value
        """
        ...

    @property
    def KeyStore(self) -> str:
        """
        Get: KeyStore(self: KeyContainerPermissionAccessEntry) -> str
        Set: KeyStore(self: KeyContainerPermissionAccessEntry) = value
        """
        ...

    @property
    def ProviderName(self) -> str:
        """
        Get: ProviderName(self: KeyContainerPermissionAccessEntry) -> str
        Set: ProviderName(self: KeyContainerPermissionAccessEntry) = value
        """
        ...

    @property
    def ProviderType(self) -> int:
        """
        Get: ProviderType(self: KeyContainerPermissionAccessEntry) -> int
        Set: ProviderType(self: KeyContainerPermissionAccessEntry) = value
        """
        ...


    def Equals(self, o:object) -> bool:
        """ Equals(self: KeyContainerPermissionAccessEntry, o: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: KeyContainerPermissionAccessEntry) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class KeyContainerPermissionAccessEntryCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Add(self, accessEntry:KeyContainerPermissionAccessEntry) -> int:
        """ Add(self: KeyContainerPermissionAccessEntryCollection, accessEntry: KeyContainerPermissionAccessEntry) -> int """
        ...

    def Clear(self): # -> 
        """ Clear(self: KeyContainerPermissionAccessEntryCollection) """
        ...

    def GetEnumerator(self) -> KeyContainerPermissionAccessEntryEnumerator:
        """ GetEnumerator(self: KeyContainerPermissionAccessEntryCollection) -> KeyContainerPermissionAccessEntryEnumerator """
        ...

    def IndexOf(self, accessEntry:KeyContainerPermissionAccessEntry) -> int:
        """ IndexOf(self: KeyContainerPermissionAccessEntryCollection, accessEntry: KeyContainerPermissionAccessEntry) -> int """
        ...

    def Remove(self, accessEntry:KeyContainerPermissionAccessEntry): # -> 
        """ Remove(self: KeyContainerPermissionAccessEntryCollection, accessEntry: KeyContainerPermissionAccessEntry) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class KeyContainerPermissionAccessEntryEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    pass

class KeyContainerPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ KeyContainerPermissionAttribute(action: SecurityAction) """
    @property
    def Flags(self) -> KeyContainerPermissionFlags:
        """
        Get: Flags(self: KeyContainerPermissionAttribute) -> KeyContainerPermissionFlags
        Set: Flags(self: KeyContainerPermissionAttribute) = value
        """
        ...

    @property
    def KeyContainerName(self) -> str:
        """
        Get: KeyContainerName(self: KeyContainerPermissionAttribute) -> str
        Set: KeyContainerName(self: KeyContainerPermissionAttribute) = value
        """
        ...

    @property
    def KeySpec(self) -> int:
        """
        Get: KeySpec(self: KeyContainerPermissionAttribute) -> int
        Set: KeySpec(self: KeyContainerPermissionAttribute) = value
        """
        ...

    @property
    def KeyStore(self) -> str:
        """
        Get: KeyStore(self: KeyContainerPermissionAttribute) -> str
        Set: KeyStore(self: KeyContainerPermissionAttribute) = value
        """
        ...

    @property
    def ProviderName(self) -> str:
        """
        Get: ProviderName(self: KeyContainerPermissionAttribute) -> str
        Set: ProviderName(self: KeyContainerPermissionAttribute) = value
        """
        ...

    @property
    def ProviderType(self) -> int:
        """
        Get: ProviderType(self: KeyContainerPermissionAttribute) -> int
        Set: ProviderType(self: KeyContainerPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: KeyContainerPermissionAttribute) -> IPermission """
        ...


class KeyContainerPermissionFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) KeyContainerPermissionFlags, values: AllFlags (13111), ChangeAcl (8192), Create (1), Decrypt (512), Delete (4), Export (32), Import (16), NoFlags (0), Open (2), Sign (256), ViewAcl (4096) """
    AllFlags: KeyContainerPermissionFlags = ...
    ChangeAcl: KeyContainerPermissionFlags = ...
    Create: KeyContainerPermissionFlags = ...
    Decrypt: KeyContainerPermissionFlags = ...
    Delete: KeyContainerPermissionFlags = ...
    Export: KeyContainerPermissionFlags = ...
    Import: KeyContainerPermissionFlags = ...
    NoFlags: KeyContainerPermissionFlags = ...
    Open: KeyContainerPermissionFlags = ...
    Sign: KeyContainerPermissionFlags = ...
    value__ = ...
    ViewAcl: KeyContainerPermissionFlags = ...


class PermissionSetAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PermissionSetAttribute(action: SecurityAction) """
    @property
    def File(self) -> str:
        """
        Get: File(self: PermissionSetAttribute) -> str
        Set: File(self: PermissionSetAttribute) = value
        """
        ...

    @property
    def Hex(self) -> str:
        """
        Get: Hex(self: PermissionSetAttribute) -> str
        Set: Hex(self: PermissionSetAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: PermissionSetAttribute) -> str
        Set: Name(self: PermissionSetAttribute) = value
        """
        ...

    @property
    def UnicodeEncoded(self) -> bool:
        """
        Get: UnicodeEncoded(self: PermissionSetAttribute) -> bool
        Set: UnicodeEncoded(self: PermissionSetAttribute) = value
        """
        ...

    @property
    def XML(self) -> str:
        """
        Get: XML(self: PermissionSetAttribute) -> str
        Set: XML(self: PermissionSetAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: PermissionSetAttribute) -> IPermission """
        ...

    def CreatePermissionSet(self) -> PermissionSet:
        """ CreatePermissionSet(self: PermissionSetAttribute) -> PermissionSet """
        ...


class PermissionState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PermissionState, values: None (0), Unrestricted (1) """
    Unrestricted: PermissionState = ...
    value__ = ...


class PrincipalPermission(IUnrestrictedPermission, IPermission, IBuiltInPermission): # skipped bases: <type 'ISecurityEncodable'>, <type 'object'>
    """
    PrincipalPermission(state: PermissionState)
    PrincipalPermission(name: str, role: str)
    PrincipalPermission(name: str, role: str, isAuthenticated: bool)
    """
    def Equals(self, obj:object) -> bool:
        """ Equals(self: PrincipalPermission, obj: object) -> bool """
        ...

    def FromXml(self, elem:SecurityElement): # -> 
        """ FromXml(self: PrincipalPermission, elem: SecurityElement) """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: PrincipalPermission) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: PrincipalPermission) -> str """
        ...

    def ToXml(self) -> SecurityElement:
        """ ToXml(self: PrincipalPermission) -> SecurityElement """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PrincipalPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PrincipalPermissionAttribute(action: SecurityAction) """
    @property
    def Authenticated(self) -> bool:
        """
        Get: Authenticated(self: PrincipalPermissionAttribute) -> bool
        Set: Authenticated(self: PrincipalPermissionAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: PrincipalPermissionAttribute) -> str
        Set: Name(self: PrincipalPermissionAttribute) = value
        """
        ...

    @property
    def Role(self) -> str:
        """
        Get: Role(self: PrincipalPermissionAttribute) -> str
        Set: Role(self: PrincipalPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: PrincipalPermissionAttribute) -> IPermission """
        ...


class PublisherIdentityPermission(CodeAccessPermission, IBuiltInPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    PublisherIdentityPermission(state: PermissionState)
    PublisherIdentityPermission(certificate: X509Certificate)
    """
    @property
    def Certificate(self) -> X509Certificate:
        """
        Get: Certificate(self: PublisherIdentityPermission) -> X509Certificate
        Set: Certificate(self: PublisherIdentityPermission) = value
        """
        ...


    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, certificate: X509Certificate)
        """
        ...


class PublisherIdentityPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PublisherIdentityPermissionAttribute(action: SecurityAction) """
    @property
    def CertFile(self) -> str:
        """
        Get: CertFile(self: PublisherIdentityPermissionAttribute) -> str
        Set: CertFile(self: PublisherIdentityPermissionAttribute) = value
        """
        ...

    @property
    def SignedFile(self) -> str:
        """
        Get: SignedFile(self: PublisherIdentityPermissionAttribute) -> str
        Set: SignedFile(self: PublisherIdentityPermissionAttribute) = value
        """
        ...

    @property
    def X509Certificate(self) -> str:
        """
        Get: X509Certificate(self: PublisherIdentityPermissionAttribute) -> str
        Set: X509Certificate(self: PublisherIdentityPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: PublisherIdentityPermissionAttribute) -> IPermission """
        ...


class ReflectionPermission(IUnrestrictedPermission, CodeAccessPermission, IBuiltInPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    ReflectionPermission(state: PermissionState)
    ReflectionPermission(flag: ReflectionPermissionFlag)
    """
    @property
    def Flags(self) -> ReflectionPermissionFlag:
        """
        Get: Flags(self: ReflectionPermission) -> ReflectionPermissionFlag
        Set: Flags(self: ReflectionPermission) = value
        """
        ...


    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, flag: ReflectionPermissionFlag)
        """
        ...


class ReflectionPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ReflectionPermissionAttribute(action: SecurityAction) """
    @property
    def Flags(self) -> ReflectionPermissionFlag:
        """
        Get: Flags(self: ReflectionPermissionAttribute) -> ReflectionPermissionFlag
        Set: Flags(self: ReflectionPermissionAttribute) = value
        """
        ...

    @property
    def MemberAccess(self) -> bool:
        """
        Get: MemberAccess(self: ReflectionPermissionAttribute) -> bool
        Set: MemberAccess(self: ReflectionPermissionAttribute) = value
        """
        ...

    @property
    def ReflectionEmit(self) -> bool:
        """
        Get: ReflectionEmit(self: ReflectionPermissionAttribute) -> bool
        Set: ReflectionEmit(self: ReflectionPermissionAttribute) = value
        """
        ...

    @property
    def RestrictedMemberAccess(self) -> bool:
        """
        Get: RestrictedMemberAccess(self: ReflectionPermissionAttribute) -> bool
        Set: RestrictedMemberAccess(self: ReflectionPermissionAttribute) = value
        """
        ...

    @property
    def TypeInformation(self) -> bool:
        """
        Get: TypeInformation(self: ReflectionPermissionAttribute) -> bool
        Set: TypeInformation(self: ReflectionPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: ReflectionPermissionAttribute) -> IPermission """
        ...


class ReflectionPermissionFlag(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ReflectionPermissionFlag, values: AllFlags (7), MemberAccess (2), NoFlags (0), ReflectionEmit (4), RestrictedMemberAccess (8), TypeInformation (1) """
    AllFlags: ReflectionPermissionFlag = ...
    MemberAccess: ReflectionPermissionFlag = ...
    NoFlags: ReflectionPermissionFlag = ...
    ReflectionEmit: ReflectionPermissionFlag = ...
    RestrictedMemberAccess: ReflectionPermissionFlag = ...
    TypeInformation: ReflectionPermissionFlag = ...
    value__ = ...


class RegistryPermission(IUnrestrictedPermission, CodeAccessPermission, IBuiltInPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    RegistryPermission(state: PermissionState)
    RegistryPermission(access: RegistryPermissionAccess, pathList: str)
    RegistryPermission(access: RegistryPermissionAccess, control: AccessControlActions, pathList: str)
    """
    def AddPathList(self, access:RegistryPermissionAccess, *__args:str): # -> 
        """ AddPathList(self: RegistryPermission, access: RegistryPermissionAccess, pathList: str)AddPathList(self: RegistryPermission, access: RegistryPermissionAccess, control: AccessControlActions, pathList: str) """
        ...

    def GetPathList(self, access:RegistryPermissionAccess) -> str:
        """ GetPathList(self: RegistryPermission, access: RegistryPermissionAccess) -> str """
        ...

    def SetPathList(self, access:RegistryPermissionAccess, pathList:str): # -> 
        """ SetPathList(self: RegistryPermission, access: RegistryPermissionAccess, pathList: str) """
        ...

    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, access: RegistryPermissionAccess, pathList: str)
        __new__(cls: type, access: RegistryPermissionAccess, control: AccessControlActions, pathList: str)
        """
        ...


class RegistryPermissionAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) RegistryPermissionAccess, values: AllAccess (7), Create (4), NoAccess (0), Read (1), Write (2) """
    AllAccess: RegistryPermissionAccess = ...
    Create: RegistryPermissionAccess = ...
    NoAccess: RegistryPermissionAccess = ...
    Read: RegistryPermissionAccess = ...
    value__ = ...
    Write: RegistryPermissionAccess = ...


class RegistryPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ RegistryPermissionAttribute(action: SecurityAction) """
    @property
    def All(self) -> str:
        """
        Get: All(self: RegistryPermissionAttribute) -> str
        Set: All(self: RegistryPermissionAttribute) = value
        """
        ...

    @property
    def ChangeAccessControl(self) -> str:
        """
        Get: ChangeAccessControl(self: RegistryPermissionAttribute) -> str
        Set: ChangeAccessControl(self: RegistryPermissionAttribute) = value
        """
        ...

    @property
    def Create(self) -> str:
        """
        Get: Create(self: RegistryPermissionAttribute) -> str
        Set: Create(self: RegistryPermissionAttribute) = value
        """
        ...

    @property
    def Read(self) -> str:
        """
        Get: Read(self: RegistryPermissionAttribute) -> str
        Set: Read(self: RegistryPermissionAttribute) = value
        """
        ...

    @property
    def ViewAccessControl(self) -> str:
        """
        Get: ViewAccessControl(self: RegistryPermissionAttribute) -> str
        Set: ViewAccessControl(self: RegistryPermissionAttribute) = value
        """
        ...

    @property
    def ViewAndModify(self) -> str:
        """
        Get: ViewAndModify(self: RegistryPermissionAttribute) -> str
        Set: ViewAndModify(self: RegistryPermissionAttribute) = value
        """
        ...

    @property
    def Write(self) -> str:
        """
        Get: Write(self: RegistryPermissionAttribute) -> str
        Set: Write(self: RegistryPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: RegistryPermissionAttribute) -> IPermission """
        ...


class ResourcePermissionBase(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """ no doc """
    @property
    def PermissionAccessType(self):
        ...

    @property
    def TagNames(self):
        ...


    def AddPermissionAccess(self, *args): #cannot find CLR method
        """ AddPermissionAccess(self: ResourcePermissionBase, entry: ResourcePermissionBaseEntry) """
        ...

    def Clear(self, *args): #cannot find CLR method
        """ Clear(self: ResourcePermissionBase) """
        ...

    def GetPermissionEntries(self, *args): #cannot find CLR method
        """ GetPermissionEntries(self: ResourcePermissionBase) -> Array[ResourcePermissionBaseEntry] """
        ...

    def RemovePermissionAccess(self, *args): #cannot find CLR method
        """ RemovePermissionAccess(self: ResourcePermissionBase, entry: ResourcePermissionBaseEntry) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, state: PermissionState)
        """
        ...

    Any: str = ...
    Local: str = ...


class ResourcePermissionBaseEntry: # skipped bases: <type 'object'>, <type 'object'>
    """
    ResourcePermissionBaseEntry()
    ResourcePermissionBaseEntry(permissionAccess: int, permissionAccessPath: Array[str])
    """
    @property
    def PermissionAccess(self) -> int:
        """ Get: PermissionAccess(self: ResourcePermissionBaseEntry) -> int """
        ...

    @property
    def PermissionAccessPath(self) -> Array:
        """ Get: PermissionAccessPath(self: ResourcePermissionBaseEntry) -> Array[str] """
        ...



class SecurityAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SecurityAction, values: Assert (3), Demand (2), Deny (4), InheritanceDemand (7), LinkDemand (6), PermitOnly (5), RequestMinimum (8), RequestOptional (9), RequestRefuse (10) """
    Assert: SecurityAction = ...
    Demand: SecurityAction = ...
    Deny: SecurityAction = ...
    InheritanceDemand: SecurityAction = ...
    LinkDemand: SecurityAction = ...
    PermitOnly: SecurityAction = ...
    RequestMinimum: SecurityAction = ...
    RequestOptional: SecurityAction = ...
    RequestRefuse: SecurityAction = ...
    value__ = ...


class SecurityPermission(IUnrestrictedPermission, CodeAccessPermission, IBuiltInPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    SecurityPermission(state: PermissionState)
    SecurityPermission(flag: SecurityPermissionFlag)
    """
    @property
    def Flags(self) -> SecurityPermissionFlag:
        """
        Get: Flags(self: SecurityPermission) -> SecurityPermissionFlag
        Set: Flags(self: SecurityPermission) = value
        """
        ...


    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, flag: SecurityPermissionFlag)
        """
        ...


class SecurityPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SecurityPermissionAttribute(action: SecurityAction) """
    @property
    def Assertion(self) -> bool:
        """
        Get: Assertion(self: SecurityPermissionAttribute) -> bool
        Set: Assertion(self: SecurityPermissionAttribute) = value
        """
        ...

    @property
    def BindingRedirects(self) -> bool:
        """
        Get: BindingRedirects(self: SecurityPermissionAttribute) -> bool
        Set: BindingRedirects(self: SecurityPermissionAttribute) = value
        """
        ...

    @property
    def ControlAppDomain(self) -> bool:
        """
        Get: ControlAppDomain(self: SecurityPermissionAttribute) -> bool
        Set: ControlAppDomain(self: SecurityPermissionAttribute) = value
        """
        ...

    @property
    def ControlDomainPolicy(self) -> bool:
        """
        Get: ControlDomainPolicy(self: SecurityPermissionAttribute) -> bool
        Set: ControlDomainPolicy(self: SecurityPermissionAttribute) = value
        """
        ...

    @property
    def ControlEvidence(self) -> bool:
        """
        Get: ControlEvidence(self: SecurityPermissionAttribute) -> bool
        Set: ControlEvidence(self: SecurityPermissionAttribute) = value
        """
        ...

    @property
    def ControlPolicy(self) -> bool:
        """
        Get: ControlPolicy(self: SecurityPermissionAttribute) -> bool
        Set: ControlPolicy(self: SecurityPermissionAttribute) = value
        """
        ...

    @property
    def ControlPrincipal(self) -> bool:
        """
        Get: ControlPrincipal(self: SecurityPermissionAttribute) -> bool
        Set: ControlPrincipal(self: SecurityPermissionAttribute) = value
        """
        ...

    @property
    def ControlThread(self) -> bool:
        """
        Get: ControlThread(self: SecurityPermissionAttribute) -> bool
        Set: ControlThread(self: SecurityPermissionAttribute) = value
        """
        ...

    @property
    def Execution(self) -> bool:
        """
        Get: Execution(self: SecurityPermissionAttribute) -> bool
        Set: Execution(self: SecurityPermissionAttribute) = value
        """
        ...

    @property
    def Flags(self) -> SecurityPermissionFlag:
        """
        Get: Flags(self: SecurityPermissionAttribute) -> SecurityPermissionFlag
        Set: Flags(self: SecurityPermissionAttribute) = value
        """
        ...

    @property
    def Infrastructure(self) -> bool:
        """
        Get: Infrastructure(self: SecurityPermissionAttribute) -> bool
        Set: Infrastructure(self: SecurityPermissionAttribute) = value
        """
        ...

    @property
    def RemotingConfiguration(self) -> bool:
        """
        Get: RemotingConfiguration(self: SecurityPermissionAttribute) -> bool
        Set: RemotingConfiguration(self: SecurityPermissionAttribute) = value
        """
        ...

    @property
    def SerializationFormatter(self) -> bool:
        """
        Get: SerializationFormatter(self: SecurityPermissionAttribute) -> bool
        Set: SerializationFormatter(self: SecurityPermissionAttribute) = value
        """
        ...

    @property
    def SkipVerification(self) -> bool:
        """
        Get: SkipVerification(self: SecurityPermissionAttribute) -> bool
        Set: SkipVerification(self: SecurityPermissionAttribute) = value
        """
        ...

    @property
    def UnmanagedCode(self) -> bool:
        """
        Get: UnmanagedCode(self: SecurityPermissionAttribute) -> bool
        Set: UnmanagedCode(self: SecurityPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: SecurityPermissionAttribute) -> IPermission """
        ...


class SecurityPermissionFlag(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SecurityPermissionFlag, values: AllFlags (16383), Assertion (1), BindingRedirects (8192), ControlAppDomain (1024), ControlDomainPolicy (256), ControlEvidence (32), ControlPolicy (64), ControlPrincipal (512), ControlThread (16), Execution (8), Infrastructure (4096), NoFlags (0), RemotingConfiguration (2048), SerializationFormatter (128), SkipVerification (4), UnmanagedCode (2) """
    AllFlags: SecurityPermissionFlag = ...
    Assertion: SecurityPermissionFlag = ...
    BindingRedirects: SecurityPermissionFlag = ...
    ControlAppDomain: SecurityPermissionFlag = ...
    ControlDomainPolicy: SecurityPermissionFlag = ...
    ControlEvidence: SecurityPermissionFlag = ...
    ControlPolicy: SecurityPermissionFlag = ...
    ControlPrincipal: SecurityPermissionFlag = ...
    ControlThread: SecurityPermissionFlag = ...
    Execution: SecurityPermissionFlag = ...
    Infrastructure: SecurityPermissionFlag = ...
    NoFlags: SecurityPermissionFlag = ...
    RemotingConfiguration: SecurityPermissionFlag = ...
    SerializationFormatter: SecurityPermissionFlag = ...
    SkipVerification: SecurityPermissionFlag = ...
    UnmanagedCode: SecurityPermissionFlag = ...
    value__ = ...


class SiteIdentityPermission(CodeAccessPermission, IBuiltInPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    SiteIdentityPermission(state: PermissionState)
    SiteIdentityPermission(site: str)
    """
    @property
    def Site(self) -> str:
        """
        Get: Site(self: SiteIdentityPermission) -> str
        Set: Site(self: SiteIdentityPermission) = value
        """
        ...


    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, site: str)
        """
        ...


class SiteIdentityPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SiteIdentityPermissionAttribute(action: SecurityAction) """
    @property
    def Site(self) -> str:
        """
        Get: Site(self: SiteIdentityPermissionAttribute) -> str
        Set: Site(self: SiteIdentityPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: SiteIdentityPermissionAttribute) -> IPermission """
        ...


class StorePermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    StorePermission(state: PermissionState)
    StorePermission(flag: StorePermissionFlags)
    """
    @property
    def Flags(self) -> StorePermissionFlags:
        """
        Get: Flags(self: StorePermission) -> StorePermissionFlags
        Set: Flags(self: StorePermission) = value
        """
        ...


    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, flag: StorePermissionFlags)
        """
        ...


class StorePermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ StorePermissionAttribute(action: SecurityAction) """
    @property
    def AddToStore(self) -> bool:
        """
        Get: AddToStore(self: StorePermissionAttribute) -> bool
        Set: AddToStore(self: StorePermissionAttribute) = value
        """
        ...

    @property
    def CreateStore(self) -> bool:
        """
        Get: CreateStore(self: StorePermissionAttribute) -> bool
        Set: CreateStore(self: StorePermissionAttribute) = value
        """
        ...

    @property
    def DeleteStore(self) -> bool:
        """
        Get: DeleteStore(self: StorePermissionAttribute) -> bool
        Set: DeleteStore(self: StorePermissionAttribute) = value
        """
        ...

    @property
    def EnumerateCertificates(self) -> bool:
        """
        Get: EnumerateCertificates(self: StorePermissionAttribute) -> bool
        Set: EnumerateCertificates(self: StorePermissionAttribute) = value
        """
        ...

    @property
    def EnumerateStores(self) -> bool:
        """
        Get: EnumerateStores(self: StorePermissionAttribute) -> bool
        Set: EnumerateStores(self: StorePermissionAttribute) = value
        """
        ...

    @property
    def Flags(self) -> StorePermissionFlags:
        """
        Get: Flags(self: StorePermissionAttribute) -> StorePermissionFlags
        Set: Flags(self: StorePermissionAttribute) = value
        """
        ...

    @property
    def OpenStore(self) -> bool:
        """
        Get: OpenStore(self: StorePermissionAttribute) -> bool
        Set: OpenStore(self: StorePermissionAttribute) = value
        """
        ...

    @property
    def RemoveFromStore(self) -> bool:
        """
        Get: RemoveFromStore(self: StorePermissionAttribute) -> bool
        Set: RemoveFromStore(self: StorePermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: StorePermissionAttribute) -> IPermission """
        ...


class StorePermissionFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) StorePermissionFlags, values: AddToStore (32), AllFlags (247), CreateStore (1), DeleteStore (2), EnumerateCertificates (128), EnumerateStores (4), NoFlags (0), OpenStore (16), RemoveFromStore (64) """
    AddToStore: StorePermissionFlags = ...
    AllFlags: StorePermissionFlags = ...
    CreateStore: StorePermissionFlags = ...
    DeleteStore: StorePermissionFlags = ...
    EnumerateCertificates: StorePermissionFlags = ...
    EnumerateStores: StorePermissionFlags = ...
    NoFlags: StorePermissionFlags = ...
    OpenStore: StorePermissionFlags = ...
    RemoveFromStore: StorePermissionFlags = ...
    value__ = ...


class StrongNameIdentityPermission(CodeAccessPermission, IBuiltInPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    StrongNameIdentityPermission(state: PermissionState)
    StrongNameIdentityPermission(blob: StrongNamePublicKeyBlob, name: str, version: Version)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: StrongNameIdentityPermission) -> str
        Set: Name(self: StrongNameIdentityPermission) = value
        """
        ...

    @property
    def PublicKey(self) -> StrongNamePublicKeyBlob:
        """
        Get: PublicKey(self: StrongNameIdentityPermission) -> StrongNamePublicKeyBlob
        Set: PublicKey(self: StrongNameIdentityPermission) = value
        """
        ...

    @property
    def Version(self) -> Version:
        """
        Get: Version(self: StrongNameIdentityPermission) -> Version
        Set: Version(self: StrongNameIdentityPermission) = value
        """
        ...


    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, blob: StrongNamePublicKeyBlob, name: str, version: Version)
        """
        ...


class StrongNameIdentityPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ StrongNameIdentityPermissionAttribute(action: SecurityAction) """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: StrongNameIdentityPermissionAttribute) -> str
        Set: Name(self: StrongNameIdentityPermissionAttribute) = value
        """
        ...

    @property
    def PublicKey(self) -> str:
        """
        Get: PublicKey(self: StrongNameIdentityPermissionAttribute) -> str
        Set: PublicKey(self: StrongNameIdentityPermissionAttribute) = value
        """
        ...

    @property
    def Version(self) -> str:
        """
        Get: Version(self: StrongNameIdentityPermissionAttribute) -> str
        Set: Version(self: StrongNameIdentityPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: StrongNameIdentityPermissionAttribute) -> IPermission """
        ...


class StrongNamePublicKeyBlob: # skipped bases: <type 'object'>, <type 'object'>
    """ StrongNamePublicKeyBlob(publicKey: Array[Byte]) """
    def Equals(self, obj:object) -> bool:
        """ Equals(self: StrongNamePublicKeyBlob, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: StrongNamePublicKeyBlob) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: StrongNamePublicKeyBlob) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TypeDescriptorPermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    TypeDescriptorPermission(state: PermissionState)
    TypeDescriptorPermission(flag: TypeDescriptorPermissionFlags)
    """
    @property
    def Flags(self) -> TypeDescriptorPermissionFlags:
        """
        Get: Flags(self: TypeDescriptorPermission) -> TypeDescriptorPermissionFlags
        Set: Flags(self: TypeDescriptorPermission) = value
        """
        ...


    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, flag: TypeDescriptorPermissionFlags)
        """
        ...


class TypeDescriptorPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TypeDescriptorPermissionAttribute(action: SecurityAction) """
    @property
    def Flags(self) -> TypeDescriptorPermissionFlags:
        """
        Get: Flags(self: TypeDescriptorPermissionAttribute) -> TypeDescriptorPermissionFlags
        Set: Flags(self: TypeDescriptorPermissionAttribute) = value
        """
        ...

    @property
    def RestrictedRegistrationAccess(self) -> bool:
        """
        Get: RestrictedRegistrationAccess(self: TypeDescriptorPermissionAttribute) -> bool
        Set: RestrictedRegistrationAccess(self: TypeDescriptorPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: TypeDescriptorPermissionAttribute) -> IPermission """
        ...


class TypeDescriptorPermissionFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TypeDescriptorPermissionFlags, values: NoFlags (0), RestrictedRegistrationAccess (1) """
    NoFlags: TypeDescriptorPermissionFlags = ...
    RestrictedRegistrationAccess: TypeDescriptorPermissionFlags = ...
    value__ = ...


class UIPermission(IUnrestrictedPermission, CodeAccessPermission, IBuiltInPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    UIPermission(state: PermissionState)
    UIPermission(windowFlag: UIPermissionWindow, clipboardFlag: UIPermissionClipboard)
    UIPermission(windowFlag: UIPermissionWindow)
    UIPermission(clipboardFlag: UIPermissionClipboard)
    """
    @property
    def Clipboard(self) -> UIPermissionClipboard:
        """
        Get: Clipboard(self: UIPermission) -> UIPermissionClipboard
        Set: Clipboard(self: UIPermission) = value
        """
        ...

    @property
    def Window(self) -> UIPermissionWindow:
        """
        Get: Window(self: UIPermission) -> UIPermissionWindow
        Set: Window(self: UIPermission) = value
        """
        ...


    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, windowFlag: UIPermissionWindow, clipboardFlag: UIPermissionClipboard)
        __new__(cls: type, windowFlag: UIPermissionWindow)
        __new__(cls: type, clipboardFlag: UIPermissionClipboard)
        """
        ...


class UIPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ UIPermissionAttribute(action: SecurityAction) """
    @property
    def Clipboard(self) -> UIPermissionClipboard:
        """
        Get: Clipboard(self: UIPermissionAttribute) -> UIPermissionClipboard
        Set: Clipboard(self: UIPermissionAttribute) = value
        """
        ...

    @property
    def Window(self) -> UIPermissionWindow:
        """
        Get: Window(self: UIPermissionAttribute) -> UIPermissionWindow
        Set: Window(self: UIPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: UIPermissionAttribute) -> IPermission """
        ...


class UIPermissionClipboard(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UIPermissionClipboard, values: AllClipboard (2), NoClipboard (0), OwnClipboard (1) """
    AllClipboard: UIPermissionClipboard = ...
    NoClipboard: UIPermissionClipboard = ...
    OwnClipboard: UIPermissionClipboard = ...
    value__ = ...


class UIPermissionWindow(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UIPermissionWindow, values: AllWindows (3), NoWindows (0), SafeSubWindows (1), SafeTopLevelWindows (2) """
    AllWindows: UIPermissionWindow = ...
    NoWindows: UIPermissionWindow = ...
    SafeSubWindows: UIPermissionWindow = ...
    SafeTopLevelWindows: UIPermissionWindow = ...
    value__ = ...


class UrlIdentityPermission(CodeAccessPermission, IBuiltInPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    UrlIdentityPermission(state: PermissionState)
    UrlIdentityPermission(site: str)
    """
    @property
    def Url(self) -> str:
        """
        Get: Url(self: UrlIdentityPermission) -> str
        Set: Url(self: UrlIdentityPermission) = value
        """
        ...


    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, site: str)
        """
        ...


class UrlIdentityPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ UrlIdentityPermissionAttribute(action: SecurityAction) """
    @property
    def Url(self) -> str:
        """
        Get: Url(self: UrlIdentityPermissionAttribute) -> str
        Set: Url(self: UrlIdentityPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: UrlIdentityPermissionAttribute) -> IPermission """
        ...


class ZoneIdentityPermission(CodeAccessPermission, IBuiltInPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    ZoneIdentityPermission(state: PermissionState)
    ZoneIdentityPermission(zone: SecurityZone)
    """
    @property
    def SecurityZone(self) -> SecurityZone:
        """
        Get: SecurityZone(self: ZoneIdentityPermission) -> SecurityZone
        Set: SecurityZone(self: ZoneIdentityPermission) = value
        """
        ...


    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, zone: SecurityZone)
        """
        ...


class ZoneIdentityPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ZoneIdentityPermissionAttribute(action: SecurityAction) """
    @property
    def Zone(self) -> SecurityZone:
        """
        Get: Zone(self: ZoneIdentityPermissionAttribute) -> SecurityZone
        Set: Zone(self: ZoneIdentityPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: ZoneIdentityPermissionAttribute) -> IPermission """
        ...


