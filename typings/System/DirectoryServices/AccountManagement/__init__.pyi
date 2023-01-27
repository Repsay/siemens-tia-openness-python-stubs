# encoding: utf-8
# module System.DirectoryServices.AccountManagement calls itself AccountManagement
# from System.DirectoryServices.AccountManagement, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Attribute, DateTime, Enum, IDisposable, Nullable, 
    SystemException, Type)

from System.Collections import ICollection, IEnumerable, IEnumerator, IList

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from System.Security.Cryptography.X509Certificates import (
    X509Certificate2Collection)

from System.Security.Principal import SecurityIdentifier

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class AdvancedFilters: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def AccountExpirationDate(self, expirationTime:DateTime, match:MatchType): # -> 
        """ AccountExpirationDate(self: AdvancedFilters, expirationTime: DateTime, match: MatchType) """
        ...

    def AccountLockoutTime(self, lockoutTime:DateTime, match:MatchType): # -> 
        """ AccountLockoutTime(self: AdvancedFilters, lockoutTime: DateTime, match: MatchType) """
        ...

    def AdvancedFilterSet(self, *args): #cannot find CLR method
        """ AdvancedFilterSet(self: AdvancedFilters, attribute: str, value: object, objectType: Type, mt: MatchType) """
        ...

    def BadLogonCount(self, badLogonCount:int, match:MatchType): # -> 
        """ BadLogonCount(self: AdvancedFilters, badLogonCount: int, match: MatchType) """
        ...

    def LastBadPasswordAttempt(self, lastAttempt:DateTime, match:MatchType): # -> 
        """ LastBadPasswordAttempt(self: AdvancedFilters, lastAttempt: DateTime, match: MatchType) """
        ...

    def LastLogonTime(self, logonTime:DateTime, match:MatchType): # -> 
        """ LastLogonTime(self: AdvancedFilters, logonTime: DateTime, match: MatchType) """
        ...

    def LastPasswordSetTime(self, passwordSetTime:DateTime, match:MatchType): # -> 
        """ LastPasswordSetTime(self: AdvancedFilters, passwordSetTime: DateTime, match: MatchType) """
        ...


class Principal(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Context(self) -> PrincipalContext:
        """ Get: Context(self: Principal) -> PrincipalContext """
        ...

    @property
    def ContextRaw(self):
        ...

    @property
    def ContextType(self) -> ContextType:
        """ Get: ContextType(self: Principal) -> ContextType """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: Principal) -> str
        Set: Description(self: Principal) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: Principal) -> str
        Set: DisplayName(self: Principal) = value
        """
        ...

    @property
    def DistinguishedName(self) -> str:
        """ Get: DistinguishedName(self: Principal) -> str """
        ...

    @property
    def Guid(self) -> Nullable:
        """ Get: Guid(self: Principal) -> Nullable[Guid] """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Principal) -> str
        Set: Name(self: Principal) = value
        """
        ...

    @property
    def SamAccountName(self) -> str:
        """
        Get: SamAccountName(self: Principal) -> str
        Set: SamAccountName(self: Principal) = value
        """
        ...

    @property
    def Sid(self) -> SecurityIdentifier:
        """ Get: Sid(self: Principal) -> SecurityIdentifier """
        ...

    @property
    def StructuralObjectClass(self) -> str:
        """ Get: StructuralObjectClass(self: Principal) -> str """
        ...

    @property
    def UserPrincipalName(self) -> str:
        """
        Get: UserPrincipalName(self: Principal) -> str
        Set: UserPrincipalName(self: Principal) = value
        """
        ...


    def CheckDisposedOrDeleted(self, *args): #cannot find CLR method
        """ CheckDisposedOrDeleted(self: Principal) """
        ...

    def Delete(self): # -> 
        """ Delete(self: Principal) """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: Principal, o: object) -> bool """
        ...

    def ExtensionGet(self, *args): #cannot find CLR method
        """ ExtensionGet(self: Principal, attribute: str) -> Array[object] """
        ...

    def ExtensionSet(self, *args): #cannot find CLR method
        """ ExtensionSet(self: Principal, attribute: str, value: object) """
        ...

    @staticmethod
    def FindByIdentity(context:PrincipalContext, *__args:str) -> Principal:
        """
        FindByIdentity(context: PrincipalContext, identityValue: str) -> Principal
        FindByIdentity(context: PrincipalContext, identityType: IdentityType, identityValue: str) -> Principal
        """
        ...

    def FindByIdentityWithType(self, *args): #cannot find CLR method
        """
        FindByIdentityWithType(context: PrincipalContext, principalType: Type, identityValue: str) -> Principal
        FindByIdentityWithType(context: PrincipalContext, principalType: Type, identityType: IdentityType, identityValue: str) -> Principal
        """
        ...

    def GetGroups(self, contextToQuery:PrincipalContext = ...) -> PrincipalSearchResult:
        """
        GetGroups(self: Principal) -> PrincipalSearchResult[Principal]
        GetGroups(self: Principal, contextToQuery: PrincipalContext) -> PrincipalSearchResult[Principal]
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Principal) -> int """
        ...

    def GetUnderlyingObject(self) -> object:
        """ GetUnderlyingObject(self: Principal) -> object """
        ...

    def GetUnderlyingObjectType(self) -> Type:
        """ GetUnderlyingObjectType(self: Principal) -> Type """
        ...

    def IsMemberOf(self, *__args:GroupPrincipal) -> bool:
        """
        IsMemberOf(self: Principal, group: GroupPrincipal) -> bool
        IsMemberOf(self: Principal, context: PrincipalContext, identityType: IdentityType, identityValue: str) -> bool
        """
        ...

    def Save(self, context:PrincipalContext = ...): # -> 
        """ Save(self: Principal)Save(self: Principal, context: PrincipalContext) """
        ...

    def ToString(self) -> str:
        """ ToString(self: Principal) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AuthenticablePrincipal(Principal): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def AccountExpirationDate(self) -> Nullable:
        """
        Get: AccountExpirationDate(self: AuthenticablePrincipal) -> Nullable[DateTime]
        Set: AccountExpirationDate(self: AuthenticablePrincipal) = value
        """
        ...

    @property
    def AccountLockoutTime(self) -> Nullable:
        """ Get: AccountLockoutTime(self: AuthenticablePrincipal) -> Nullable[DateTime] """
        ...

    @property
    def AdvancedSearchFilter(self) -> AdvancedFilters:
        """ Get: AdvancedSearchFilter(self: AuthenticablePrincipal) -> AdvancedFilters """
        ...

    @property
    def AllowReversiblePasswordEncryption(self) -> bool:
        """
        Get: AllowReversiblePasswordEncryption(self: AuthenticablePrincipal) -> bool
        Set: AllowReversiblePasswordEncryption(self: AuthenticablePrincipal) = value
        """
        ...

    @property
    def BadLogonCount(self) -> int:
        """ Get: BadLogonCount(self: AuthenticablePrincipal) -> int """
        ...

    @property
    def Certificates(self) -> X509Certificate2Collection:
        """ Get: Certificates(self: AuthenticablePrincipal) -> X509Certificate2Collection """
        ...

    @property
    def DelegationPermitted(self) -> bool:
        """
        Get: DelegationPermitted(self: AuthenticablePrincipal) -> bool
        Set: DelegationPermitted(self: AuthenticablePrincipal) = value
        """
        ...

    @property
    def Enabled(self) -> Nullable:
        """
        Get: Enabled(self: AuthenticablePrincipal) -> Nullable[bool]
        Set: Enabled(self: AuthenticablePrincipal) = value
        """
        ...

    @property
    def HomeDirectory(self) -> str:
        """
        Get: HomeDirectory(self: AuthenticablePrincipal) -> str
        Set: HomeDirectory(self: AuthenticablePrincipal) = value
        """
        ...

    @property
    def HomeDrive(self) -> str:
        """
        Get: HomeDrive(self: AuthenticablePrincipal) -> str
        Set: HomeDrive(self: AuthenticablePrincipal) = value
        """
        ...

    @property
    def LastBadPasswordAttempt(self) -> Nullable:
        """ Get: LastBadPasswordAttempt(self: AuthenticablePrincipal) -> Nullable[DateTime] """
        ...

    @property
    def LastLogon(self) -> Nullable:
        """ Get: LastLogon(self: AuthenticablePrincipal) -> Nullable[DateTime] """
        ...

    @property
    def LastPasswordSet(self) -> Nullable:
        """ Get: LastPasswordSet(self: AuthenticablePrincipal) -> Nullable[DateTime] """
        ...

    @property
    def PasswordNeverExpires(self) -> bool:
        """
        Get: PasswordNeverExpires(self: AuthenticablePrincipal) -> bool
        Set: PasswordNeverExpires(self: AuthenticablePrincipal) = value
        """
        ...

    @property
    def PasswordNotRequired(self) -> bool:
        """
        Get: PasswordNotRequired(self: AuthenticablePrincipal) -> bool
        Set: PasswordNotRequired(self: AuthenticablePrincipal) = value
        """
        ...

    @property
    def PermittedLogonTimes(self) -> Array:
        """
        Get: PermittedLogonTimes(self: AuthenticablePrincipal) -> Array[Byte]
        Set: PermittedLogonTimes(self: AuthenticablePrincipal) = value
        """
        ...

    @property
    def PermittedWorkstations(self) -> PrincipalValueCollection:
        """ Get: PermittedWorkstations(self: AuthenticablePrincipal) -> PrincipalValueCollection[str] """
        ...

    @property
    def ScriptPath(self) -> str:
        """
        Get: ScriptPath(self: AuthenticablePrincipal) -> str
        Set: ScriptPath(self: AuthenticablePrincipal) = value
        """
        ...

    @property
    def SmartcardLogonRequired(self) -> bool:
        """
        Get: SmartcardLogonRequired(self: AuthenticablePrincipal) -> bool
        Set: SmartcardLogonRequired(self: AuthenticablePrincipal) = value
        """
        ...

    @property
    def UserCannotChangePassword(self) -> bool:
        """
        Get: UserCannotChangePassword(self: AuthenticablePrincipal) -> bool
        Set: UserCannotChangePassword(self: AuthenticablePrincipal) = value
        """
        ...


    def ChangePassword(self, oldPassword:str, newPassword:str): # -> 
        """ ChangePassword(self: AuthenticablePrincipal, oldPassword: str, newPassword: str) """
        ...

    def ExpirePasswordNow(self): # -> 
        """ ExpirePasswordNow(self: AuthenticablePrincipal) """
        ...

    @staticmethod
    def FindByBadPasswordAttempt(context:PrincipalContext, time:DateTime, type:MatchType) -> PrincipalSearchResult:
        """ FindByBadPasswordAttempt(context: PrincipalContext, time: DateTime, type: MatchType) -> PrincipalSearchResult[AuthenticablePrincipal] """
        ...

    @staticmethod
    def FindByExpirationTime(context:PrincipalContext, time:DateTime, type:MatchType) -> PrincipalSearchResult:
        """ FindByExpirationTime(context: PrincipalContext, time: DateTime, type: MatchType) -> PrincipalSearchResult[AuthenticablePrincipal] """
        ...

    @staticmethod
    def FindByLockoutTime(context:PrincipalContext, time:DateTime, type:MatchType) -> PrincipalSearchResult:
        """ FindByLockoutTime(context: PrincipalContext, time: DateTime, type: MatchType) -> PrincipalSearchResult[AuthenticablePrincipal] """
        ...

    @staticmethod
    def FindByLogonTime(context:PrincipalContext, time:DateTime, type:MatchType) -> PrincipalSearchResult:
        """ FindByLogonTime(context: PrincipalContext, time: DateTime, type: MatchType) -> PrincipalSearchResult[AuthenticablePrincipal] """
        ...

    @staticmethod
    def FindByPasswordSetTime(context:PrincipalContext, time:DateTime, type:MatchType) -> PrincipalSearchResult:
        """ FindByPasswordSetTime(context: PrincipalContext, time: DateTime, type: MatchType) -> PrincipalSearchResult[AuthenticablePrincipal] """
        ...

    def IsAccountLockedOut(self) -> bool:
        """ IsAccountLockedOut(self: AuthenticablePrincipal) -> bool """
        ...

    def RefreshExpiredPassword(self): # -> 
        """ RefreshExpiredPassword(self: AuthenticablePrincipal) """
        ...

    def SetPassword(self, newPassword:str): # -> 
        """ SetPassword(self: AuthenticablePrincipal, newPassword: str) """
        ...

    def UnlockAccount(self): # -> 
        """ UnlockAccount(self: AuthenticablePrincipal) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type, context: PrincipalContext)
        __new__(cls: type, context: PrincipalContext, samAccountName: str, password: str, enabled: bool)
        """
        ...


class ComputerPrincipal(AuthenticablePrincipal): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    ComputerPrincipal(context: PrincipalContext)
    ComputerPrincipal(context: PrincipalContext, samAccountName: str, password: str, enabled: bool)
    """
    @property
    def ServicePrincipalNames(self) -> PrincipalValueCollection:
        """ Get: ServicePrincipalNames(self: ComputerPrincipal) -> PrincipalValueCollection[str] """
        ...


    @staticmethod
    def FindByIdentity(context:PrincipalContext, *__args:str) -> ComputerPrincipal:
        """
        FindByIdentity(context: PrincipalContext, identityValue: str) -> ComputerPrincipal
        FindByIdentity(context: PrincipalContext, identityType: IdentityType, identityValue: str) -> ComputerPrincipal
        """
        ...


class ContextOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ContextOptions, values: Negotiate (1), Sealing (16), SecureSocketLayer (4), ServerBind (32), Signing (8), SimpleBind (2) """
    Negotiate: ContextOptions = ...
    Sealing: ContextOptions = ...
    SecureSocketLayer: ContextOptions = ...
    ServerBind: ContextOptions = ...
    Signing: ContextOptions = ...
    SimpleBind: ContextOptions = ...
    value__ = ...


class ContextType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ContextType, values: ApplicationDirectory (2), Domain (1), Machine (0) """
    ApplicationDirectory: ContextType = ...
    Domain: ContextType = ...
    Machine: ContextType = ...
    value__ = ...


class DirectoryObjectClassAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DirectoryObjectClassAttribute(objectClass: str) """
    @property
    def Context(self) -> Nullable:
        """ Get: Context(self: DirectoryObjectClassAttribute) -> Nullable[ContextType] """
        ...

    @property
    def ObjectClass(self) -> str:
        """ Get: ObjectClass(self: DirectoryObjectClassAttribute) -> str """
        ...


    def __new__(cls, objectClass:str) -> Self:
        """ __new__(cls: type, objectClass: str) """
        ...


class DirectoryPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DirectoryPropertyAttribute(schemaAttributeName: str) """
    @property
    def Context(self) -> Nullable:
        """
        Get: Context(self: DirectoryPropertyAttribute) -> Nullable[ContextType]
        Set: Context(self: DirectoryPropertyAttribute) = value
        """
        ...

    @property
    def SchemaAttributeName(self) -> str:
        """ Get: SchemaAttributeName(self: DirectoryPropertyAttribute) -> str """
        ...


    def __new__(cls, schemaAttributeName:str) -> Self:
        """ __new__(cls: type, schemaAttributeName: str) """
        ...


class DirectoryRdnPrefixAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DirectoryRdnPrefixAttribute(rdnPrefix: str) """
    @property
    def Context(self) -> Nullable:
        """ Get: Context(self: DirectoryRdnPrefixAttribute) -> Nullable[ContextType] """
        ...

    @property
    def RdnPrefix(self) -> str:
        """ Get: RdnPrefix(self: DirectoryRdnPrefixAttribute) -> str """
        ...


    def __new__(cls, rdnPrefix:str) -> Self:
        """ __new__(cls: type, rdnPrefix: str) """
        ...


class GroupPrincipal(Principal): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    GroupPrincipal(context: PrincipalContext)
    GroupPrincipal(context: PrincipalContext, samAccountName: str)
    """
    @property
    def GroupScope(self) -> Nullable:
        """
        Get: GroupScope(self: GroupPrincipal) -> Nullable[GroupScope]
        Set: GroupScope(self: GroupPrincipal) = value
        """
        ...

    @property
    def IsSecurityGroup(self) -> Nullable:
        """
        Get: IsSecurityGroup(self: GroupPrincipal) -> Nullable[bool]
        Set: IsSecurityGroup(self: GroupPrincipal) = value
        """
        ...

    @property
    def Members(self) -> PrincipalCollection:
        """ Get: Members(self: GroupPrincipal) -> PrincipalCollection """
        ...


    def GetMembers(self, recursive:bool = ...) -> PrincipalSearchResult:
        """
        GetMembers(self: GroupPrincipal) -> PrincipalSearchResult[Principal]
        GetMembers(self: GroupPrincipal, recursive: bool) -> PrincipalSearchResult[Principal]
        """
        ...

    def __new__(cls, context:PrincipalContext, samAccountName:str = ...) -> Self:
        """
        __new__(cls: type, context: PrincipalContext)
        __new__(cls: type, context: PrincipalContext, samAccountName: str)
        """
        ...


class GroupScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GroupScope, values: Global (1), Local (0), Universal (2) """
    Global: GroupScope = ...
    Local: GroupScope = ...
    Universal: GroupScope = ...
    value__ = ...


class IdentityType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum IdentityType, values: DistinguishedName (3), Guid (5), Name (1), SamAccountName (0), Sid (4), UserPrincipalName (2) """
    DistinguishedName: IdentityType = ...
    Guid: IdentityType = ...
    Name: IdentityType = ...
    SamAccountName: IdentityType = ...
    Sid: IdentityType = ...
    UserPrincipalName: IdentityType = ...
    value__ = ...


class MatchType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MatchType, values: Equals (0), GreaterThan (2), GreaterThanOrEquals (3), LessThan (4), LessThanOrEquals (5), NotEquals (1) """
    Equals: MatchType = ...
    GreaterThan: MatchType = ...
    GreaterThanOrEquals: MatchType = ...
    LessThan: MatchType = ...
    LessThanOrEquals: MatchType = ...
    NotEquals: MatchType = ...
    value__ = ...


class PrincipalException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    SerializeObjectState = ...


class MultipleMatchesException(PrincipalException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MultipleMatchesException()
    MultipleMatchesException(message: str)
    MultipleMatchesException(message: str, innerException: Exception)
    """
    def __new__(cls, message:str = ..., innerException:Exception = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        ...

    SerializeObjectState = ...


class NoMatchingPrincipalException(PrincipalException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    NoMatchingPrincipalException()
    NoMatchingPrincipalException(message: str)
    NoMatchingPrincipalException(message: str, innerException: Exception)
    """
    def __new__(cls, message:str = ..., innerException:Exception = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        ...

    SerializeObjectState = ...


class PasswordException(PrincipalException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PasswordException()
    PasswordException(message: str)
    PasswordException(message: str, innerException: Exception)
    """
    def __new__(cls, message:str = ..., innerException:Exception = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        ...

    SerializeObjectState = ...


class PrincipalCollection(ICollection): # skipped bases: <type 'IEnumerable[Principal]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: PrincipalCollection) -> IEnumerator[Principal] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class PrincipalContext(IDisposable): # skipped bases: <type 'object'>
    """
    PrincipalContext(contextType: ContextType)
    PrincipalContext(contextType: ContextType, name: str)
    PrincipalContext(contextType: ContextType, name: str, container: str)
    PrincipalContext(contextType: ContextType, name: str, container: str, options: ContextOptions)
    PrincipalContext(contextType: ContextType, name: str, userName: str, password: str)
    PrincipalContext(contextType: ContextType, name: str, container: str, userName: str, password: str)
    PrincipalContext(contextType: ContextType, name: str, container: str, options: ContextOptions, userName: str, password: str)
    """
    @property
    def ConnectedServer(self) -> str:
        """ Get: ConnectedServer(self: PrincipalContext) -> str """
        ...

    @property
    def Container(self) -> str:
        """ Get: Container(self: PrincipalContext) -> str """
        ...

    @property
    def ContextType(self) -> ContextType:
        """ Get: ContextType(self: PrincipalContext) -> ContextType """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PrincipalContext) -> str """
        ...

    @property
    def Options(self) -> ContextOptions:
        """ Get: Options(self: PrincipalContext) -> ContextOptions """
        ...

    @property
    def UserName(self) -> str:
        """ Get: UserName(self: PrincipalContext) -> str """
        ...


    def ValidateCredentials(self, userName:str, password:str, options:ContextOptions = ...) -> bool:
        """
        ValidateCredentials(self: PrincipalContext, userName: str, password: str) -> bool
        ValidateCredentials(self: PrincipalContext, userName: str, password: str, options: ContextOptions) -> bool
        """
        ...


class PrincipalExistsException(PrincipalException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PrincipalExistsException()
    PrincipalExistsException(message: str)
    PrincipalExistsException(message: str, innerException: Exception)
    """
    def __new__(cls, message:str = ..., innerException:Exception = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        ...

    SerializeObjectState = ...


class PrincipalOperationException(PrincipalException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PrincipalOperationException()
    PrincipalOperationException(message: str)
    PrincipalOperationException(message: str, innerException: Exception)
    PrincipalOperationException(message: str, errorCode: int)
    PrincipalOperationException(message: str, innerException: Exception, errorCode: int)
    """
    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: PrincipalOperationException) -> int """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: PrincipalOperationException, info: SerializationInfo, context: StreamingContext) """
        ...

    def __new__(cls, message:str = ..., *__args:Exception) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, message: str, errorCode: int)
        __new__(cls: type, message: str, innerException: Exception, errorCode: int)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        ...

    SerializeObjectState = ...


class PrincipalSearcher(IDisposable): # skipped bases: <type 'object'>
    """
    PrincipalSearcher()
    PrincipalSearcher(queryFilter: Principal)
    """
    @property
    def Context(self) -> PrincipalContext:
        """ Get: Context(self: PrincipalSearcher) -> PrincipalContext """
        ...

    @property
    def QueryFilter(self) -> Principal:
        """
        Get: QueryFilter(self: PrincipalSearcher) -> Principal
        Set: QueryFilter(self: PrincipalSearcher) = value
        """
        ...


    def FindAll(self) -> PrincipalSearchResult:
        """ FindAll(self: PrincipalSearcher) -> PrincipalSearchResult[Principal] """
        ...

    def FindOne(self) -> Principal:
        """ FindOne(self: PrincipalSearcher) -> Principal """
        ...

    def GetUnderlyingSearcher(self) -> object:
        """ GetUnderlyingSearcher(self: PrincipalSearcher) -> object """
        ...

    def GetUnderlyingSearcherType(self) -> Type:
        """ GetUnderlyingSearcherType(self: PrincipalSearcher) -> Type """
        ...


class PrincipalSearchResult(IDisposable, IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[T](enumerable: IEnumerable[T], value: T) -> bool """
        ...


class PrincipalServerDownException(PrincipalException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PrincipalServerDownException()
    PrincipalServerDownException(message: str)
    PrincipalServerDownException(message: str, innerException: Exception)
    PrincipalServerDownException(message: str, errorCode: int)
    PrincipalServerDownException(message: str, innerException: Exception, errorCode: int)
    PrincipalServerDownException(message: str, innerException: Exception, errorCode: int, serverName: str)
    """
    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: PrincipalServerDownException, info: SerializationInfo, context: StreamingContext) """
        ...

    def __new__(cls, message:str = ..., *__args:Exception) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, message: str)
        __new__(cls: type, message: str, innerException: Exception)
        __new__(cls: type, message: str, errorCode: int)
        __new__(cls: type, message: str, innerException: Exception, errorCode: int)
        __new__(cls: type, message: str, innerException: Exception, errorCode: int, serverName: str)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        ...

    SerializeObjectState = ...


class PrincipalValueCollection(IList): # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>, <type 'IEnumerable[T]'>, <type 'ICollection[T]'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: PrincipalValueCollection[T]) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: PrincipalValueCollection[T]) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: PrincipalValueCollection[T]) -> object """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: PrincipalValueCollection[T], array: Array[T], index: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: PrincipalValueCollection[T]) -> IEnumerator[T] """
        ...


class UserPrincipal(AuthenticablePrincipal): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    UserPrincipal(context: PrincipalContext)
    UserPrincipal(context: PrincipalContext, samAccountName: str, password: str, enabled: bool)
    """
    @property
    def Current(self) -> UserPrincipal:
        """ Get: Current() -> UserPrincipal """
        ...

    @property
    def EmailAddress(self) -> str:
        """
        Get: EmailAddress(self: UserPrincipal) -> str
        Set: EmailAddress(self: UserPrincipal) = value
        """
        ...

    @property
    def EmployeeId(self) -> str:
        """
        Get: EmployeeId(self: UserPrincipal) -> str
        Set: EmployeeId(self: UserPrincipal) = value
        """
        ...

    @property
    def GivenName(self) -> str:
        """
        Get: GivenName(self: UserPrincipal) -> str
        Set: GivenName(self: UserPrincipal) = value
        """
        ...

    @property
    def MiddleName(self) -> str:
        """
        Get: MiddleName(self: UserPrincipal) -> str
        Set: MiddleName(self: UserPrincipal) = value
        """
        ...

    @property
    def Surname(self) -> str:
        """
        Get: Surname(self: UserPrincipal) -> str
        Set: Surname(self: UserPrincipal) = value
        """
        ...

    @property
    def VoiceTelephoneNumber(self) -> str:
        """
        Get: VoiceTelephoneNumber(self: UserPrincipal) -> str
        Set: VoiceTelephoneNumber(self: UserPrincipal) = value
        """
        ...


    @staticmethod
    def FindByIdentity(context:PrincipalContext, *__args:str) -> UserPrincipal:
        """
        FindByIdentity(context: PrincipalContext, identityValue: str) -> UserPrincipal
        FindByIdentity(context: PrincipalContext, identityType: IdentityType, identityValue: str) -> UserPrincipal
        """
        ...

    def GetAuthorizationGroups(self) -> PrincipalSearchResult:
        """ GetAuthorizationGroups(self: UserPrincipal) -> PrincipalSearchResult[Principal] """
        ...



