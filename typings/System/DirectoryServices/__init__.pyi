# encoding: utf-8
# module System.DirectoryServices calls itself DirectoryServices
# from System.DirectoryServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.DirectoryServices.Protocols, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.DirectoryServices.AccountManagement, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Enum, Guid, IDisposable, IntPtr, 
    MarshalByRefObject, TimeSpan, Type)

from System.Collections import (CollectionBase, DictionaryBase, ICollection, 
    IDictionary, IEnumerable, IEnumerator, IList, ReadOnlyCollectionBase)

from System.Collections.Specialized import StringCollection

from System.ComponentModel import Component

from System.EnterpriseServices import DescriptionAttribute

from System.Runtime.InteropServices import COMException

from System.Security import IPermission

from System.Security.AccessControl import (AccessControlModification, 
    AccessControlType, AccessRule, AuditRule, DirectoryObjectSecurity, 
    ObjectAccessRule, ObjectAuditRule)

from System.Security.Permissions import (CodeAccessSecurityAttribute, 
    ResourcePermissionBase)

from System.Security.Principal import IdentityReference

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class ActiveDirectoryAccessRule(ObjectAccessRule): # skipped bases: <type 'object'>
    """
    ActiveDirectoryAccessRule(identity: IdentityReference, adRights: ActiveDirectoryRights, type: AccessControlType)
    ActiveDirectoryAccessRule(identity: IdentityReference, adRights: ActiveDirectoryRights, type: AccessControlType, objectType: Guid)
    ActiveDirectoryAccessRule(identity: IdentityReference, adRights: ActiveDirectoryRights, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance)
    ActiveDirectoryAccessRule(identity: IdentityReference, adRights: ActiveDirectoryRights, type: AccessControlType, objectType: Guid, inheritanceType: ActiveDirectorySecurityInheritance)
    ActiveDirectoryAccessRule(identity: IdentityReference, adRights: ActiveDirectoryRights, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid)
    ActiveDirectoryAccessRule(identity: IdentityReference, adRights: ActiveDirectoryRights, type: AccessControlType, objectType: Guid, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid)
    """
    @property
    def ActiveDirectoryRights(self) -> ActiveDirectoryRights:
        """ Get: ActiveDirectoryRights(self: ActiveDirectoryAccessRule) -> ActiveDirectoryRights """
        ...

    @property
    def InheritanceType(self) -> ActiveDirectorySecurityInheritance:
        """ Get: InheritanceType(self: ActiveDirectoryAccessRule) -> ActiveDirectorySecurityInheritance """
        ...



class ActiveDirectoryAuditRule(ObjectAuditRule): # skipped bases: <type 'object'>
    """
    ActiveDirectoryAuditRule(identity: IdentityReference, adRights: ActiveDirectoryRights, auditFlags: AuditFlags)
    ActiveDirectoryAuditRule(identity: IdentityReference, adRights: ActiveDirectoryRights, auditFlags: AuditFlags, objectType: Guid)
    ActiveDirectoryAuditRule(identity: IdentityReference, adRights: ActiveDirectoryRights, auditFlags: AuditFlags, inheritanceType: ActiveDirectorySecurityInheritance)
    ActiveDirectoryAuditRule(identity: IdentityReference, adRights: ActiveDirectoryRights, auditFlags: AuditFlags, objectType: Guid, inheritanceType: ActiveDirectorySecurityInheritance)
    ActiveDirectoryAuditRule(identity: IdentityReference, adRights: ActiveDirectoryRights, auditFlags: AuditFlags, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid)
    ActiveDirectoryAuditRule(identity: IdentityReference, adRights: ActiveDirectoryRights, auditFlags: AuditFlags, objectType: Guid, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid)
    """
    @property
    def ActiveDirectoryRights(self) -> ActiveDirectoryRights:
        """ Get: ActiveDirectoryRights(self: ActiveDirectoryAuditRule) -> ActiveDirectoryRights """
        ...

    @property
    def InheritanceType(self) -> ActiveDirectorySecurityInheritance:
        """ Get: InheritanceType(self: ActiveDirectoryAuditRule) -> ActiveDirectorySecurityInheritance """
        ...



class ActiveDirectoryRights(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ActiveDirectoryRights, values: AccessSystemSecurity (16777216), CreateChild (1), Delete (65536), DeleteChild (2), DeleteTree (64), ExtendedRight (256), GenericAll (983551), GenericExecute (131076), GenericRead (131220), GenericWrite (131112), ListChildren (4), ListObject (128), ReadControl (131072), ReadProperty (16), Self (8), Synchronize (1048576), WriteDacl (262144), WriteOwner (524288), WriteProperty (32) """
    AccessSystemSecurity: ActiveDirectoryRights = ...
    CreateChild: ActiveDirectoryRights = ...
    Delete: ActiveDirectoryRights = ...
    DeleteChild: ActiveDirectoryRights = ...
    DeleteTree: ActiveDirectoryRights = ...
    ExtendedRight: ActiveDirectoryRights = ...
    GenericAll: ActiveDirectoryRights = ...
    GenericExecute: ActiveDirectoryRights = ...
    GenericRead: ActiveDirectoryRights = ...
    GenericWrite: ActiveDirectoryRights = ...
    ListChildren: ActiveDirectoryRights = ...
    ListObject: ActiveDirectoryRights = ...
    ReadControl: ActiveDirectoryRights = ...
    ReadProperty: ActiveDirectoryRights = ...
    Self: ActiveDirectoryRights = ...
    Synchronize: ActiveDirectoryRights = ...
    value__ = ...
    WriteDacl: ActiveDirectoryRights = ...
    WriteOwner: ActiveDirectoryRights = ...
    WriteProperty: ActiveDirectoryRights = ...


class ActiveDirectorySecurity(DirectoryObjectSecurity): # skipped bases: <type 'object'>
    """ ActiveDirectorySecurity() """
    @property
    def AccessRightType(self) -> Type:
        """ Get: AccessRightType(self: ActiveDirectorySecurity) -> Type """
        ...

    @property
    def AccessRuleType(self) -> Type:
        """ Get: AccessRuleType(self: ActiveDirectorySecurity) -> Type """
        ...

    @property
    def AuditRuleType(self) -> Type:
        """ Get: AuditRuleType(self: ActiveDirectorySecurity) -> Type """
        ...


    def ModifyAccessRule(self, modification, rule, modified) -> Tuple_[bool, bool]:
        """ ModifyAccessRule(self: ActiveDirectorySecurity, modification: AccessControlModification, rule: AccessRule) -> (bool, bool) """
        ...

    def ModifyAuditRule(self, modification, rule, modified) -> Tuple_[bool, bool]:
        """ ModifyAuditRule(self: ActiveDirectorySecurity, modification: AccessControlModification, rule: AuditRule) -> (bool, bool) """
        ...

    def PurgeAccessRules(self, identity:IdentityReference): # -> 
        """ PurgeAccessRules(self: ActiveDirectorySecurity, identity: IdentityReference) """
        ...

    def PurgeAuditRules(self, identity:IdentityReference): # -> 
        """ PurgeAuditRules(self: ActiveDirectorySecurity, identity: IdentityReference) """
        ...

    def RemoveAccess(self, identity:IdentityReference, type:AccessControlType): # -> 
        """ RemoveAccess(self: ActiveDirectorySecurity, identity: IdentityReference, type: AccessControlType) """
        ...

    def RemoveAudit(self, identity:IdentityReference): # -> 
        """ RemoveAudit(self: ActiveDirectorySecurity, identity: IdentityReference) """
        ...


class ActiveDirectorySecurityInheritance(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ActiveDirectorySecurityInheritance, values: All (1), Children (4), Descendents (2), None (0), SelfAndChildren (3) """
    All: ActiveDirectorySecurityInheritance = ...
    Children: ActiveDirectorySecurityInheritance = ...
    Descendents: ActiveDirectorySecurityInheritance = ...
    SelfAndChildren: ActiveDirectorySecurityInheritance = ...
    value__ = ...


class AuthenticationTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) AuthenticationTypes, values: Anonymous (16), Delegation (256), Encryption (2), FastBind (32), None (0), ReadonlyServer (4), Sealing (128), Secure (1), SecureSocketsLayer (2), ServerBind (512), Signing (64) """
    Anonymous: AuthenticationTypes = ...
    Delegation: AuthenticationTypes = ...
    Encryption: AuthenticationTypes = ...
    FastBind: AuthenticationTypes = ...
    ReadonlyServer: AuthenticationTypes = ...
    Sealing: AuthenticationTypes = ...
    Secure: AuthenticationTypes = ...
    SecureSocketsLayer: AuthenticationTypes = ...
    ServerBind: AuthenticationTypes = ...
    Signing: AuthenticationTypes = ...
    value__ = ...


class CreateChildAccessRule(ActiveDirectoryAccessRule): # skipped bases: <type 'object'>
    """
    CreateChildAccessRule(identity: IdentityReference, type: AccessControlType)
    CreateChildAccessRule(identity: IdentityReference, type: AccessControlType, childType: Guid)
    CreateChildAccessRule(identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance)
    CreateChildAccessRule(identity: IdentityReference, type: AccessControlType, childType: Guid, inheritanceType: ActiveDirectorySecurityInheritance)
    CreateChildAccessRule(identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid)
    CreateChildAccessRule(identity: IdentityReference, type: AccessControlType, childType: Guid, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid)
    """
    pass

class DeleteChildAccessRule(ActiveDirectoryAccessRule): # skipped bases: <type 'object'>
    """
    DeleteChildAccessRule(identity: IdentityReference, type: AccessControlType)
    DeleteChildAccessRule(identity: IdentityReference, type: AccessControlType, childType: Guid)
    DeleteChildAccessRule(identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance)
    DeleteChildAccessRule(identity: IdentityReference, type: AccessControlType, childType: Guid, inheritanceType: ActiveDirectorySecurityInheritance)
    DeleteChildAccessRule(identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid)
    DeleteChildAccessRule(identity: IdentityReference, type: AccessControlType, childType: Guid, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid)
    """
    pass

class DeleteTreeAccessRule(ActiveDirectoryAccessRule): # skipped bases: <type 'object'>
    """
    DeleteTreeAccessRule(identity: IdentityReference, type: AccessControlType)
    DeleteTreeAccessRule(identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance)
    DeleteTreeAccessRule(identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid)
    """
    pass

class DereferenceAlias(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DereferenceAlias, values: Always (3), FindingBaseObject (2), InSearching (1), Never (0) """
    Always: DereferenceAlias = ...
    FindingBaseObject: DereferenceAlias = ...
    InSearching: DereferenceAlias = ...
    Never: DereferenceAlias = ...
    value__ = ...


class DirectoryEntries(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SchemaFilter(self) -> SchemaNameCollection:
        """ Get: SchemaFilter(self: DirectoryEntries) -> SchemaNameCollection """
        ...


    def Add(self, name:str, schemaClassName:str) -> DirectoryEntry:
        """ Add(self: DirectoryEntries, name: str, schemaClassName: str) -> DirectoryEntry """
        ...

    def Find(self, name:str, schemaClassName:str = ...) -> DirectoryEntry:
        """
        Find(self: DirectoryEntries, name: str) -> DirectoryEntry
        Find(self: DirectoryEntries, name: str, schemaClassName: str) -> DirectoryEntry
        """
        ...

    def Remove(self, entry:DirectoryEntry): # -> 
        """ Remove(self: DirectoryEntries, entry: DirectoryEntry) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class DirectoryEntry(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    DirectoryEntry()
    DirectoryEntry(path: str)
    DirectoryEntry(path: str, username: str, password: str)
    DirectoryEntry(path: str, username: str, password: str, authenticationType: AuthenticationTypes)
    DirectoryEntry(adsObject: object)
    """
    @property
    def AuthenticationType(self) -> AuthenticationTypes:
        """
        Get: AuthenticationType(self: DirectoryEntry) -> AuthenticationTypes
        Set: AuthenticationType(self: DirectoryEntry) = value
        """
        ...

    @property
    def Children(self) -> DirectoryEntries:
        """ Get: Children(self: DirectoryEntry) -> DirectoryEntries """
        ...

    @property
    def Guid(self) -> Guid:
        """ Get: Guid(self: DirectoryEntry) -> Guid """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DirectoryEntry) -> str """
        ...

    @property
    def NativeGuid(self) -> str:
        """ Get: NativeGuid(self: DirectoryEntry) -> str """
        ...

    @property
    def NativeObject(self) -> object:
        """ Get: NativeObject(self: DirectoryEntry) -> object """
        ...

    @property
    def ObjectSecurity(self) -> ActiveDirectorySecurity:
        """
        Get: ObjectSecurity(self: DirectoryEntry) -> ActiveDirectorySecurity
        Set: ObjectSecurity(self: DirectoryEntry) = value
        """
        ...

    @property
    def Options(self) -> DirectoryEntryConfiguration:
        """ Get: Options(self: DirectoryEntry) -> DirectoryEntryConfiguration """
        ...

    @property
    def Parent(self) -> DirectoryEntry:
        """ Get: Parent(self: DirectoryEntry) -> DirectoryEntry """
        ...

    @property
    def Password(self): # -> 
        """ Set: Password(self: DirectoryEntry) = value """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: DirectoryEntry) -> str
        Set: Path(self: DirectoryEntry) = value
        """
        ...

    @property
    def Properties(self) -> PropertyCollection:
        """ Get: Properties(self: DirectoryEntry) -> PropertyCollection """
        ...

    @property
    def SchemaClassName(self) -> str:
        """ Get: SchemaClassName(self: DirectoryEntry) -> str """
        ...

    @property
    def SchemaEntry(self) -> DirectoryEntry:
        """ Get: SchemaEntry(self: DirectoryEntry) -> DirectoryEntry """
        ...

    @property
    def UsePropertyCache(self) -> bool:
        """
        Get: UsePropertyCache(self: DirectoryEntry) -> bool
        Set: UsePropertyCache(self: DirectoryEntry) = value
        """
        ...

    @property
    def Username(self) -> str:
        """
        Get: Username(self: DirectoryEntry) -> str
        Set: Username(self: DirectoryEntry) = value
        """
        ...


    def Close(self): # -> 
        """ Close(self: DirectoryEntry) """
        ...

    def CommitChanges(self): # -> 
        """ CommitChanges(self: DirectoryEntry) """
        ...

    def CopyTo(self, newParent:DirectoryEntry, newName:str = ...) -> DirectoryEntry:
        """
        CopyTo(self: DirectoryEntry, newParent: DirectoryEntry) -> DirectoryEntry
        CopyTo(self: DirectoryEntry, newParent: DirectoryEntry, newName: str) -> DirectoryEntry
        """
        ...

    def DeleteTree(self): # -> 
        """ DeleteTree(self: DirectoryEntry) """
        ...

    @staticmethod
    def Exists(path:str) -> bool:
        """ Exists(path: str) -> bool """
        ...

    def Invoke(self, methodName:str, args:Array) -> object:
        """ Invoke(self: DirectoryEntry, methodName: str, *args: Array[object]) -> object """
        ...

    def InvokeGet(self, propertyName:str) -> object:
        """ InvokeGet(self: DirectoryEntry, propertyName: str) -> object """
        ...

    def InvokeSet(self, propertyName:str, args:Array): # -> 
        """ InvokeSet(self: DirectoryEntry, propertyName: str, *args: Array[object]) """
        ...

    def MoveTo(self, newParent:DirectoryEntry, newName:str = ...): # -> 
        """ MoveTo(self: DirectoryEntry, newParent: DirectoryEntry)MoveTo(self: DirectoryEntry, newParent: DirectoryEntry, newName: str) """
        ...

    def RefreshCache(self, propertyNames:Array = ...): # -> 
        """ RefreshCache(self: DirectoryEntry)RefreshCache(self: DirectoryEntry, propertyNames: Array[str]) """
        ...

    def Rename(self, newName:str): # -> 
        """ Rename(self: DirectoryEntry, newName: str) """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, path: str)
        __new__(cls: type, path: str, username: str, password: str)
        __new__(cls: type, path: str, username: str, password: str, authenticationType: AuthenticationTypes)
        __new__(cls: type, adsObject: object)
        """
        ...


class DirectoryEntryConfiguration: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def PageSize(self) -> int:
        """
        Get: PageSize(self: DirectoryEntryConfiguration) -> int
        Set: PageSize(self: DirectoryEntryConfiguration) = value
        """
        ...

    @property
    def PasswordEncoding(self) -> PasswordEncodingMethod:
        """
        Get: PasswordEncoding(self: DirectoryEntryConfiguration) -> PasswordEncodingMethod
        Set: PasswordEncoding(self: DirectoryEntryConfiguration) = value
        """
        ...

    @property
    def PasswordPort(self) -> int:
        """
        Get: PasswordPort(self: DirectoryEntryConfiguration) -> int
        Set: PasswordPort(self: DirectoryEntryConfiguration) = value
        """
        ...

    @property
    def Referral(self) -> ReferralChasingOption:
        """
        Get: Referral(self: DirectoryEntryConfiguration) -> ReferralChasingOption
        Set: Referral(self: DirectoryEntryConfiguration) = value
        """
        ...

    @property
    def SecurityMasks(self) -> SecurityMasks:
        """
        Get: SecurityMasks(self: DirectoryEntryConfiguration) -> SecurityMasks
        Set: SecurityMasks(self: DirectoryEntryConfiguration) = value
        """
        ...


    def GetCurrentServerName(self) -> str:
        """ GetCurrentServerName(self: DirectoryEntryConfiguration) -> str """
        ...

    def IsMutuallyAuthenticated(self) -> bool:
        """ IsMutuallyAuthenticated(self: DirectoryEntryConfiguration) -> bool """
        ...

    def SetUserNameQueryQuota(self, accountName:str): # -> 
        """ SetUserNameQueryQuota(self: DirectoryEntryConfiguration, accountName: str) """
        ...


class DirectorySearcher(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    DirectorySearcher()
    DirectorySearcher(searchRoot: DirectoryEntry)
    DirectorySearcher(searchRoot: DirectoryEntry, filter: str)
    DirectorySearcher(searchRoot: DirectoryEntry, filter: str, propertiesToLoad: Array[str])
    DirectorySearcher(filter: str)
    DirectorySearcher(filter: str, propertiesToLoad: Array[str])
    DirectorySearcher(filter: str, propertiesToLoad: Array[str], scope: SearchScope)
    DirectorySearcher(searchRoot: DirectoryEntry, filter: str, propertiesToLoad: Array[str], scope: SearchScope)
    """
    @property
    def Asynchronous(self) -> bool:
        """
        Get: Asynchronous(self: DirectorySearcher) -> bool
        Set: Asynchronous(self: DirectorySearcher) = value
        """
        ...

    @property
    def AttributeScopeQuery(self) -> str:
        """
        Get: AttributeScopeQuery(self: DirectorySearcher) -> str
        Set: AttributeScopeQuery(self: DirectorySearcher) = value
        """
        ...

    @property
    def CacheResults(self) -> bool:
        """
        Get: CacheResults(self: DirectorySearcher) -> bool
        Set: CacheResults(self: DirectorySearcher) = value
        """
        ...

    @property
    def ClientTimeout(self) -> TimeSpan:
        """
        Get: ClientTimeout(self: DirectorySearcher) -> TimeSpan
        Set: ClientTimeout(self: DirectorySearcher) = value
        """
        ...

    @property
    def DerefAlias(self) -> DereferenceAlias:
        """
        Get: DerefAlias(self: DirectorySearcher) -> DereferenceAlias
        Set: DerefAlias(self: DirectorySearcher) = value
        """
        ...

    @property
    def DirectorySynchronization(self) -> DirectorySynchronization:
        """
        Get: DirectorySynchronization(self: DirectorySearcher) -> DirectorySynchronization
        Set: DirectorySynchronization(self: DirectorySearcher) = value
        """
        ...

    @property
    def ExtendedDN(self) -> ExtendedDN:
        """
        Get: ExtendedDN(self: DirectorySearcher) -> ExtendedDN
        Set: ExtendedDN(self: DirectorySearcher) = value
        """
        ...

    @property
    def Filter(self) -> str:
        """
        Get: Filter(self: DirectorySearcher) -> str
        Set: Filter(self: DirectorySearcher) = value
        """
        ...

    @property
    def PageSize(self) -> int:
        """
        Get: PageSize(self: DirectorySearcher) -> int
        Set: PageSize(self: DirectorySearcher) = value
        """
        ...

    @property
    def PropertiesToLoad(self) -> StringCollection:
        """ Get: PropertiesToLoad(self: DirectorySearcher) -> StringCollection """
        ...

    @property
    def PropertyNamesOnly(self) -> bool:
        """
        Get: PropertyNamesOnly(self: DirectorySearcher) -> bool
        Set: PropertyNamesOnly(self: DirectorySearcher) = value
        """
        ...

    @property
    def ReferralChasing(self) -> ReferralChasingOption:
        """
        Get: ReferralChasing(self: DirectorySearcher) -> ReferralChasingOption
        Set: ReferralChasing(self: DirectorySearcher) = value
        """
        ...

    @property
    def SearchRoot(self) -> DirectoryEntry:
        """
        Get: SearchRoot(self: DirectorySearcher) -> DirectoryEntry
        Set: SearchRoot(self: DirectorySearcher) = value
        """
        ...

    @property
    def SearchScope(self) -> SearchScope:
        """
        Get: SearchScope(self: DirectorySearcher) -> SearchScope
        Set: SearchScope(self: DirectorySearcher) = value
        """
        ...

    @property
    def SecurityMasks(self) -> SecurityMasks:
        """
        Get: SecurityMasks(self: DirectorySearcher) -> SecurityMasks
        Set: SecurityMasks(self: DirectorySearcher) = value
        """
        ...

    @property
    def ServerPageTimeLimit(self) -> TimeSpan:
        """
        Get: ServerPageTimeLimit(self: DirectorySearcher) -> TimeSpan
        Set: ServerPageTimeLimit(self: DirectorySearcher) = value
        """
        ...

    @property
    def ServerTimeLimit(self) -> TimeSpan:
        """
        Get: ServerTimeLimit(self: DirectorySearcher) -> TimeSpan
        Set: ServerTimeLimit(self: DirectorySearcher) = value
        """
        ...

    @property
    def SizeLimit(self) -> int:
        """
        Get: SizeLimit(self: DirectorySearcher) -> int
        Set: SizeLimit(self: DirectorySearcher) = value
        """
        ...

    @property
    def Sort(self) -> SortOption:
        """
        Get: Sort(self: DirectorySearcher) -> SortOption
        Set: Sort(self: DirectorySearcher) = value
        """
        ...

    @property
    def Tombstone(self) -> bool:
        """
        Get: Tombstone(self: DirectorySearcher) -> bool
        Set: Tombstone(self: DirectorySearcher) = value
        """
        ...

    @property
    def VirtualListView(self) -> DirectoryVirtualListView:
        """
        Get: VirtualListView(self: DirectorySearcher) -> DirectoryVirtualListView
        Set: VirtualListView(self: DirectorySearcher) = value
        """
        ...


    def FindAll(self) -> SearchResultCollection:
        """ FindAll(self: DirectorySearcher) -> SearchResultCollection """
        ...

    def FindOne(self) -> SearchResult:
        """ FindOne(self: DirectorySearcher) -> SearchResult """
        ...

    def __new__(cls, *__args:DirectoryEntry) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, searchRoot: DirectoryEntry)
        __new__(cls: type, searchRoot: DirectoryEntry, filter: str)
        __new__(cls: type, searchRoot: DirectoryEntry, filter: str, propertiesToLoad: Array[str])
        __new__(cls: type, filter: str)
        __new__(cls: type, filter: str, propertiesToLoad: Array[str])
        __new__(cls: type, filter: str, propertiesToLoad: Array[str], scope: SearchScope)
        __new__(cls: type, searchRoot: DirectoryEntry, filter: str, propertiesToLoad: Array[str], scope: SearchScope)
        """
        ...


class DirectoryServicesCOMException(COMException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DirectoryServicesCOMException()
    DirectoryServicesCOMException(message: str)
    DirectoryServicesCOMException(message: str, inner: Exception)
    """
    @property
    def ExtendedError(self) -> int:
        """ Get: ExtendedError(self: DirectoryServicesCOMException) -> int """
        ...

    @property
    def ExtendedErrorMessage(self) -> str:
        """ Get: ExtendedErrorMessage(self: DirectoryServicesCOMException) -> str """
        ...


    SerializeObjectState = ...


class DirectoryServicesPermission(ResourcePermissionBase): # skipped bases: <type 'IPermission'>, <type 'IUnrestrictedPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    DirectoryServicesPermission()
    DirectoryServicesPermission(state: PermissionState)
    DirectoryServicesPermission(permissionAccess: DirectoryServicesPermissionAccess, path: str)
    DirectoryServicesPermission(permissionAccessEntries: Array[DirectoryServicesPermissionEntry])
    """
    @property
    def PermissionEntries(self) -> DirectoryServicesPermissionEntryCollection:
        """ Get: PermissionEntries(self: DirectoryServicesPermission) -> DirectoryServicesPermissionEntryCollection """
        ...



class DirectoryServicesPermissionAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DirectoryServicesPermissionAccess, values: Browse (2), None (0), Write (6) """
    Browse: DirectoryServicesPermissionAccess = ...
    value__ = ...
    Write: DirectoryServicesPermissionAccess = ...


class DirectoryServicesPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DirectoryServicesPermissionAttribute(action: SecurityAction) """
    @property
    def Path(self) -> str:
        """
        Get: Path(self: DirectoryServicesPermissionAttribute) -> str
        Set: Path(self: DirectoryServicesPermissionAttribute) = value
        """
        ...

    @property
    def PermissionAccess(self) -> DirectoryServicesPermissionAccess:
        """
        Get: PermissionAccess(self: DirectoryServicesPermissionAttribute) -> DirectoryServicesPermissionAccess
        Set: PermissionAccess(self: DirectoryServicesPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: DirectoryServicesPermissionAttribute) -> IPermission """
        ...


class DirectoryServicesPermissionEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ DirectoryServicesPermissionEntry(permissionAccess: DirectoryServicesPermissionAccess, path: str) """
    @property
    def Path(self) -> str:
        """ Get: Path(self: DirectoryServicesPermissionEntry) -> str """
        ...

    @property
    def PermissionAccess(self) -> DirectoryServicesPermissionAccess:
        """ Get: PermissionAccess(self: DirectoryServicesPermissionEntry) -> DirectoryServicesPermissionAccess """
        ...



class DirectoryServicesPermissionEntryCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, value:DirectoryServicesPermissionEntry) -> int:
        """ Add(self: DirectoryServicesPermissionEntryCollection, value: DirectoryServicesPermissionEntry) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: DirectoryServicesPermissionEntryCollection, value: Array[DirectoryServicesPermissionEntry])AddRange(self: DirectoryServicesPermissionEntryCollection, value: DirectoryServicesPermissionEntryCollection) """
        ...

    def Contains(self, value:DirectoryServicesPermissionEntry) -> bool:
        """ Contains(self: DirectoryServicesPermissionEntryCollection, value: DirectoryServicesPermissionEntry) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: DirectoryServicesPermissionEntryCollection, array: Array[DirectoryServicesPermissionEntry], index: int) """
        ...

    def IndexOf(self, value:DirectoryServicesPermissionEntry) -> int:
        """ IndexOf(self: DirectoryServicesPermissionEntryCollection, value: DirectoryServicesPermissionEntry) -> int """
        ...

    def Insert(self, index:int, value:DirectoryServicesPermissionEntry): # -> 
        """ Insert(self: DirectoryServicesPermissionEntryCollection, index: int, value: DirectoryServicesPermissionEntry) """
        ...

    def Remove(self, value:DirectoryServicesPermissionEntry): # -> 
        """ Remove(self: DirectoryServicesPermissionEntryCollection, value: DirectoryServicesPermissionEntry) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class DirectorySynchronization: # skipped bases: <type 'object'>, <type 'object'>
    """
    DirectorySynchronization()
    DirectorySynchronization(option: DirectorySynchronizationOptions)
    DirectorySynchronization(sync: DirectorySynchronization)
    DirectorySynchronization(cookie: Array[Byte])
    DirectorySynchronization(option: DirectorySynchronizationOptions, cookie: Array[Byte])
    """
    @property
    def Option(self) -> DirectorySynchronizationOptions:
        """
        Get: Option(self: DirectorySynchronization) -> DirectorySynchronizationOptions
        Set: Option(self: DirectorySynchronization) = value
        """
        ...


    def Copy(self) -> DirectorySynchronization:
        """ Copy(self: DirectorySynchronization) -> DirectorySynchronization """
        ...

    def GetDirectorySynchronizationCookie(self) -> Array:
        """ GetDirectorySynchronizationCookie(self: DirectorySynchronization) -> Array[Byte] """
        ...

    def ResetDirectorySynchronizationCookie(self, cookie:Array = ...): # -> 
        """ ResetDirectorySynchronizationCookie(self: DirectorySynchronization)ResetDirectorySynchronizationCookie(self: DirectorySynchronization, cookie: Array[Byte]) """
        ...


class DirectorySynchronizationOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DirectorySynchronizationOptions, values: IncrementalValues (2147483648), None (0), ObjectSecurity (1), ParentsFirst (2048), PublicDataOnly (8192) """
    IncrementalValues: DirectorySynchronizationOptions = ...
    ObjectSecurity: DirectorySynchronizationOptions = ...
    ParentsFirst: DirectorySynchronizationOptions = ...
    PublicDataOnly: DirectorySynchronizationOptions = ...
    value__ = ...


class DirectoryVirtualListView: # skipped bases: <type 'object'>, <type 'object'>
    """
    DirectoryVirtualListView()
    DirectoryVirtualListView(afterCount: int)
    DirectoryVirtualListView(beforeCount: int, afterCount: int, offset: int)
    DirectoryVirtualListView(beforeCount: int, afterCount: int, target: str)
    DirectoryVirtualListView(beforeCount: int, afterCount: int, offset: int, context: DirectoryVirtualListViewContext)
    DirectoryVirtualListView(beforeCount: int, afterCount: int, target: str, context: DirectoryVirtualListViewContext)
    """
    @property
    def AfterCount(self) -> int:
        """
        Get: AfterCount(self: DirectoryVirtualListView) -> int
        Set: AfterCount(self: DirectoryVirtualListView) = value
        """
        ...

    @property
    def ApproximateTotal(self) -> int:
        """
        Get: ApproximateTotal(self: DirectoryVirtualListView) -> int
        Set: ApproximateTotal(self: DirectoryVirtualListView) = value
        """
        ...

    @property
    def BeforeCount(self) -> int:
        """
        Get: BeforeCount(self: DirectoryVirtualListView) -> int
        Set: BeforeCount(self: DirectoryVirtualListView) = value
        """
        ...

    @property
    def DirectoryVirtualListViewContext(self) -> DirectoryVirtualListViewContext:
        """
        Get: DirectoryVirtualListViewContext(self: DirectoryVirtualListView) -> DirectoryVirtualListViewContext
        Set: DirectoryVirtualListViewContext(self: DirectoryVirtualListView) = value
        """
        ...

    @property
    def Offset(self) -> int:
        """
        Get: Offset(self: DirectoryVirtualListView) -> int
        Set: Offset(self: DirectoryVirtualListView) = value
        """
        ...

    @property
    def Target(self) -> str:
        """
        Get: Target(self: DirectoryVirtualListView) -> str
        Set: Target(self: DirectoryVirtualListView) = value
        """
        ...

    @property
    def TargetPercentage(self) -> int:
        """
        Get: TargetPercentage(self: DirectoryVirtualListView) -> int
        Set: TargetPercentage(self: DirectoryVirtualListView) = value
        """
        ...



class DirectoryVirtualListViewContext: # skipped bases: <type 'object'>, <type 'object'>
    """ DirectoryVirtualListViewContext() """
    def Copy(self) -> DirectoryVirtualListViewContext:
        """ Copy(self: DirectoryVirtualListViewContext) -> DirectoryVirtualListViewContext """
        ...


class DSDescriptionAttribute(DescriptionAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DSDescriptionAttribute(description: str) """
    pass

class ExtendedDN(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ExtendedDN, values: HexString (0), None (-1), Standard (1) """
    HexString: ExtendedDN = ...
    Standard: ExtendedDN = ...
    value__ = ...


class ExtendedRightAccessRule(ActiveDirectoryAccessRule): # skipped bases: <type 'object'>
    """
    ExtendedRightAccessRule(identity: IdentityReference, type: AccessControlType)
    ExtendedRightAccessRule(identity: IdentityReference, type: AccessControlType, extendedRightType: Guid)
    ExtendedRightAccessRule(identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance)
    ExtendedRightAccessRule(identity: IdentityReference, type: AccessControlType, extendedRightType: Guid, inheritanceType: ActiveDirectorySecurityInheritance)
    ExtendedRightAccessRule(identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid)
    ExtendedRightAccessRule(identity: IdentityReference, type: AccessControlType, extendedRightType: Guid, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid)
    """
    pass

class ListChildrenAccessRule(ActiveDirectoryAccessRule): # skipped bases: <type 'object'>
    """
    ListChildrenAccessRule(identity: IdentityReference, type: AccessControlType)
    ListChildrenAccessRule(identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance)
    ListChildrenAccessRule(identity: IdentityReference, type: AccessControlType, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid)
    """
    pass

class PasswordEncodingMethod(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PasswordEncodingMethod, values: PasswordEncodingClear (1), PasswordEncodingSsl (0) """
    PasswordEncodingClear: PasswordEncodingMethod = ...
    PasswordEncodingSsl: PasswordEncodingMethod = ...
    value__ = ...


class PropertyAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PropertyAccess, values: Read (0), Write (1) """
    Read: PropertyAccess = ...
    value__ = ...
    Write: PropertyAccess = ...


class PropertyAccessRule(ActiveDirectoryAccessRule): # skipped bases: <type 'object'>
    """
    PropertyAccessRule(identity: IdentityReference, type: AccessControlType, access: PropertyAccess)
    PropertyAccessRule(identity: IdentityReference, type: AccessControlType, access: PropertyAccess, propertyType: Guid)
    PropertyAccessRule(identity: IdentityReference, type: AccessControlType, access: PropertyAccess, inheritanceType: ActiveDirectorySecurityInheritance)
    PropertyAccessRule(identity: IdentityReference, type: AccessControlType, access: PropertyAccess, propertyType: Guid, inheritanceType: ActiveDirectorySecurityInheritance)
    PropertyAccessRule(identity: IdentityReference, type: AccessControlType, access: PropertyAccess, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid)
    PropertyAccessRule(identity: IdentityReference, type: AccessControlType, access: PropertyAccess, propertyType: Guid, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid)
    """
    pass

class PropertyCollection(IDictionary): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: PropertyCollection) -> int """
        ...

    @property
    def PropertyNames(self) -> ICollection:
        """ Get: PropertyNames(self: PropertyCollection) -> ICollection """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: PropertyCollection, array: Array[PropertyValueCollection], index: int) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary, key: object) -> bool """
        ...


class PropertySetAccessRule(ActiveDirectoryAccessRule): # skipped bases: <type 'object'>
    """
    PropertySetAccessRule(identity: IdentityReference, type: AccessControlType, access: PropertyAccess, propertySetType: Guid)
    PropertySetAccessRule(identity: IdentityReference, type: AccessControlType, access: PropertyAccess, propertySetType: Guid, inheritanceType: ActiveDirectorySecurityInheritance)
    PropertySetAccessRule(identity: IdentityReference, type: AccessControlType, access: PropertyAccess, propertySetType: Guid, inheritanceType: ActiveDirectorySecurityInheritance, inheritedObjectType: Guid)
    """
    pass

class PropertyValueCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: PropertyValueCollection) -> str """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: PropertyValueCollection) -> object
        Set: Value(self: PropertyValueCollection) = value
        """
        ...


    def Add(self, value:object) -> int:
        """ Add(self: PropertyValueCollection, value: object) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: PropertyValueCollection, value: Array[object])AddRange(self: PropertyValueCollection, value: PropertyValueCollection) """
        ...

    def Contains(self, value:object) -> bool:
        """ Contains(self: PropertyValueCollection, value: object) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: PropertyValueCollection, array: Array[object], index: int) """
        ...

    def IndexOf(self, value:object) -> int:
        """ IndexOf(self: PropertyValueCollection, value: object) -> int """
        ...

    def Insert(self, index:int, value:object): # -> 
        """ Insert(self: PropertyValueCollection, index: int, value: object) """
        ...

    def Remove(self, value:object): # -> 
        """ Remove(self: PropertyValueCollection, value: object) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ReferralChasingOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ReferralChasingOption, values: All (96), External (64), None (0), Subordinate (32) """
    All: ReferralChasingOption = ...
    External: ReferralChasingOption = ...
    Subordinate: ReferralChasingOption = ...
    value__ = ...


class ResultPropertyCollection(DictionaryBase): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def PropertyNames(self) -> ICollection:
        """ Get: PropertyNames(self: ResultPropertyCollection) -> ICollection """
        ...

    @property
    def Values(self) -> ICollection:
        """ Get: Values(self: ResultPropertyCollection) -> ICollection """
        ...


    def Contains(self, propertyName:str) -> bool:
        """ Contains(self: ResultPropertyCollection, propertyName: str) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ResultPropertyValueCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def Contains(self, value:object) -> bool:
        """ Contains(self: ResultPropertyValueCollection, value: object) -> bool """
        ...

    def CopyTo(self, values:Array, index:int): # -> 
        """ CopyTo(self: ResultPropertyValueCollection, values: Array[object], index: int) """
        ...

    def IndexOf(self, value:object) -> int:
        """ IndexOf(self: ResultPropertyValueCollection, value: object) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class SchemaNameCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: SchemaNameCollection) -> int """
        ...


    def AddRange(self, value:Array): # -> 
        """ AddRange(self: SchemaNameCollection, value: Array[str])AddRange(self: SchemaNameCollection, value: SchemaNameCollection) """
        ...

    def CopyTo(self, stringArray:Array, index:int): # -> 
        """ CopyTo(self: SchemaNameCollection, stringArray: Array[str], index: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SchemaNameCollection) -> IEnumerator """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class SearchResult: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Path(self) -> str:
        """ Get: Path(self: SearchResult) -> str """
        ...

    @property
    def Properties(self) -> ResultPropertyCollection:
        """ Get: Properties(self: SearchResult) -> ResultPropertyCollection """
        ...


    def GetDirectoryEntry(self) -> DirectoryEntry:
        """ GetDirectoryEntry(self: SearchResult) -> DirectoryEntry """
        ...


class SearchResultCollection(IDisposable, MarshalByRefObject, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Handle(self) -> IntPtr:
        """ Get: Handle(self: SearchResultCollection) -> IntPtr """
        ...

    @property
    def PropertiesLoaded(self) -> Array:
        """ Get: PropertiesLoaded(self: SearchResultCollection) -> Array[str] """
        ...


    def Contains(self, result:SearchResult) -> bool:
        """ Contains(self: SearchResultCollection, result: SearchResult) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SearchResultCollection) -> IEnumerator """
        ...

    def IndexOf(self, result:SearchResult) -> int:
        """ IndexOf(self: SearchResultCollection, result: SearchResult) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class SearchScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SearchScope, values: Base (0), OneLevel (1), Subtree (2) """
    Base: SearchScope = ...
    OneLevel: SearchScope = ...
    Subtree: SearchScope = ...
    value__ = ...


class SecurityMasks(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SecurityMasks, values: Dacl (4), Group (2), None (0), Owner (1), Sacl (8) """
    Dacl: SecurityMasks = ...
    Group: SecurityMasks = ...
    Owner: SecurityMasks = ...
    Sacl: SecurityMasks = ...
    value__ = ...


class SortDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SortDirection, values: Ascending (0), Descending (1) """
    Ascending: SortDirection = ...
    Descending: SortDirection = ...
    value__ = ...


class SortOption: # skipped bases: <type 'object'>, <type 'object'>
    """
    SortOption()
    SortOption(propertyName: str, direction: SortDirection)
    """
    @property
    def Direction(self) -> SortDirection:
        """
        Get: Direction(self: SortOption) -> SortDirection
        Set: Direction(self: SortOption) = value
        """
        ...

    @property
    def PropertyName(self) -> str:
        """
        Get: PropertyName(self: SortOption) -> str
        Set: PropertyName(self: SortOption) = value
        """
        ...



# variables with complex values

