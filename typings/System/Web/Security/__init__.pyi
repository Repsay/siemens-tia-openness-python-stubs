# encoding: utf-8
# module System.Web.Security calls itself Security
# from System.Web.ApplicationServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, DateTime, Enum, EventArgs, 
    IAsyncResult, IDisposable, IntPtr, MulticastDelegate, Nullable, TimeSpan, 
    Type)

from System.Collections import ICollection, IEnumerator

from System.Collections.Specialized import NameValueCollection

from System.ComponentModel.DataAnnotations import ValidationAttribute

from System.Configuration.Provider import ProviderBase, ProviderCollection

from System.Runtime.Serialization import ISerializable

from System.Security.Claims import ClaimsIdentity, ClaimsPrincipal

from System.Security.Principal import (GenericPrincipal, IIdentity, 
    IPrincipal, WindowsIdentity)

from System.Web import (HttpContext, HttpCookie, HttpCookieMode, IHttpModule, 
    SameSiteMode)

from System.Web.Configuration import TicketCompatibilityMode

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    FormsAuthenticationTicket, MachineKeyProtection, PassportIdentity, field#)
"""

# no functions
# classes

class ActiveDirectoryConnectionProtection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ActiveDirectoryConnectionProtection, values: None (0), SignAndSeal (2), Ssl (1) """
    SignAndSeal: ActiveDirectoryConnectionProtection = ...
    Ssl: ActiveDirectoryConnectionProtection = ...
    value__ = ...


class MembershipProvider(ProviderBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: MembershipProvider) -> str
        Set: ApplicationName(self: MembershipProvider) = value
        """
        ...

    @property
    def EnablePasswordReset(self) -> bool:
        """ Get: EnablePasswordReset(self: MembershipProvider) -> bool """
        ...

    @property
    def EnablePasswordRetrieval(self) -> bool:
        """ Get: EnablePasswordRetrieval(self: MembershipProvider) -> bool """
        ...

    @property
    def MaxInvalidPasswordAttempts(self) -> int:
        """ Get: MaxInvalidPasswordAttempts(self: MembershipProvider) -> int """
        ...

    @property
    def MinRequiredNonAlphanumericCharacters(self) -> int:
        """ Get: MinRequiredNonAlphanumericCharacters(self: MembershipProvider) -> int """
        ...

    @property
    def MinRequiredPasswordLength(self) -> int:
        """ Get: MinRequiredPasswordLength(self: MembershipProvider) -> int """
        ...

    @property
    def PasswordAttemptWindow(self) -> int:
        """ Get: PasswordAttemptWindow(self: MembershipProvider) -> int """
        ...

    @property
    def PasswordFormat(self) -> MembershipPasswordFormat:
        """ Get: PasswordFormat(self: MembershipProvider) -> MembershipPasswordFormat """
        ...

    @property
    def PasswordStrengthRegularExpression(self) -> str:
        """ Get: PasswordStrengthRegularExpression(self: MembershipProvider) -> str """
        ...

    @property
    def RequiresQuestionAndAnswer(self) -> bool:
        """ Get: RequiresQuestionAndAnswer(self: MembershipProvider) -> bool """
        ...

    @property
    def RequiresUniqueEmail(self) -> bool:
        """ Get: RequiresUniqueEmail(self: MembershipProvider) -> bool """
        ...


    def ChangePassword(self, username:str, oldPassword:str, newPassword:str) -> bool:
        """ ChangePassword(self: MembershipProvider, username: str, oldPassword: str, newPassword: str) -> bool """
        ...

    def ChangePasswordQuestionAndAnswer(self, username:str, password:str, newPasswordQuestion:str, newPasswordAnswer:str) -> bool:
        """ ChangePasswordQuestionAndAnswer(self: MembershipProvider, username: str, password: str, newPasswordQuestion: str, newPasswordAnswer: str) -> bool """
        ...

    def CreateUser(self, username, password, email, passwordQuestion, passwordAnswer, isApproved, providerUserKey, status) -> Tuple_[MembershipUser, MembershipCreateStatus]:
        """ CreateUser(self: MembershipProvider, username: str, password: str, email: str, passwordQuestion: str, passwordAnswer: str, isApproved: bool, providerUserKey: object) -> (MembershipUser, MembershipCreateStatus) """
        ...

    def DecryptPassword(self, *args): #cannot find CLR method
        """ DecryptPassword(self: MembershipProvider, encodedPassword: Array[Byte]) -> Array[Byte] """
        ...

    def DeleteUser(self, username:str, deleteAllRelatedData:bool) -> bool:
        """ DeleteUser(self: MembershipProvider, username: str, deleteAllRelatedData: bool) -> bool """
        ...

    def EncryptPassword(self, *args): #cannot find CLR method
        """
        EncryptPassword(self: MembershipProvider, password: Array[Byte]) -> Array[Byte]
        EncryptPassword(self: MembershipProvider, password: Array[Byte], legacyPasswordCompatibilityMode: MembershipPasswordCompatibilityMode) -> Array[Byte]
        """
        ...

    def FindUsersByEmail(self, emailToMatch, pageIndex, pageSize, totalRecords) -> Tuple_[MembershipUserCollection, int]:
        """ FindUsersByEmail(self: MembershipProvider, emailToMatch: str, pageIndex: int, pageSize: int) -> (MembershipUserCollection, int) """
        ...

    def FindUsersByName(self, usernameToMatch, pageIndex, pageSize, totalRecords) -> Tuple_[MembershipUserCollection, int]:
        """ FindUsersByName(self: MembershipProvider, usernameToMatch: str, pageIndex: int, pageSize: int) -> (MembershipUserCollection, int) """
        ...

    def GetAllUsers(self, pageIndex, pageSize, totalRecords) -> Tuple_[MembershipUserCollection, int]:
        """ GetAllUsers(self: MembershipProvider, pageIndex: int, pageSize: int) -> (MembershipUserCollection, int) """
        ...

    def GetNumberOfUsersOnline(self) -> int:
        """ GetNumberOfUsersOnline(self: MembershipProvider) -> int """
        ...

    def GetPassword(self, username:str, answer:str) -> str:
        """ GetPassword(self: MembershipProvider, username: str, answer: str) -> str """
        ...

    def GetUser(self, *__args) -> MembershipUser:
        """
        GetUser(self: MembershipProvider, providerUserKey: object, userIsOnline: bool) -> MembershipUser
        GetUser(self: MembershipProvider, username: str, userIsOnline: bool) -> MembershipUser
        """
        ...

    def GetUserNameByEmail(self, email:str) -> str:
        """ GetUserNameByEmail(self: MembershipProvider, email: str) -> str """
        ...

    def OnValidatingPassword(self, *args): #cannot find CLR method
        """ OnValidatingPassword(self: MembershipProvider, e: ValidatePasswordEventArgs) """
        ...

    def ResetPassword(self, username:str, answer:str) -> str:
        """ ResetPassword(self: MembershipProvider, username: str, answer: str) -> str """
        ...

    def UnlockUser(self, userName:str) -> bool:
        """ UnlockUser(self: MembershipProvider, userName: str) -> bool """
        ...

    def UpdateUser(self, user:MembershipUser): # -> 
        """ UpdateUser(self: MembershipProvider, user: MembershipUser) """
        ...

    def ValidateUser(self, username:str, password:str) -> bool:
        """ ValidateUser(self: MembershipProvider, username: str, password: str) -> bool """
        ...

    ValidatingPassword = ...


class ActiveDirectoryMembershipProvider(MembershipProvider): # skipped bases: <type 'object'>
    """ ActiveDirectoryMembershipProvider() """
    @property
    def CurrentConnectionProtection(self) -> ActiveDirectoryConnectionProtection:
        """ Get: CurrentConnectionProtection(self: ActiveDirectoryMembershipProvider) -> ActiveDirectoryConnectionProtection """
        ...

    @property
    def EnableSearchMethods(self) -> bool:
        """ Get: EnableSearchMethods(self: ActiveDirectoryMembershipProvider) -> bool """
        ...

    @property
    def PasswordAnswerAttemptLockoutDuration(self) -> int:
        """ Get: PasswordAnswerAttemptLockoutDuration(self: ActiveDirectoryMembershipProvider) -> int """
        ...


    def GeneratePassword(self) -> str:
        """ GeneratePassword(self: ActiveDirectoryMembershipProvider) -> str """
        ...

    def Initialize(self, name:str, config:NameValueCollection): # -> 
        """ Initialize(self: ActiveDirectoryMembershipProvider, name: str, config: NameValueCollection) """
        ...


class MembershipUser: # skipped bases: <type 'object'>, <type 'object'>
    """ MembershipUser(providerName: str, name: str, providerUserKey: object, email: str, passwordQuestion: str, comment: str, isApproved: bool, isLockedOut: bool, creationDate: DateTime, lastLoginDate: DateTime, lastActivityDate: DateTime, lastPasswordChangedDate: DateTime, lastLockoutDate: DateTime) """
    @property
    def Comment(self) -> str:
        """
        Get: Comment(self: MembershipUser) -> str
        Set: Comment(self: MembershipUser) = value
        """
        ...

    @property
    def CreationDate(self) -> DateTime:
        """ Get: CreationDate(self: MembershipUser) -> DateTime """
        ...

    @property
    def Email(self) -> str:
        """
        Get: Email(self: MembershipUser) -> str
        Set: Email(self: MembershipUser) = value
        """
        ...

    @property
    def IsApproved(self) -> bool:
        """
        Get: IsApproved(self: MembershipUser) -> bool
        Set: IsApproved(self: MembershipUser) = value
        """
        ...

    @property
    def IsLockedOut(self) -> bool:
        """ Get: IsLockedOut(self: MembershipUser) -> bool """
        ...

    @property
    def IsOnline(self) -> bool:
        """ Get: IsOnline(self: MembershipUser) -> bool """
        ...

    @property
    def LastActivityDate(self) -> DateTime:
        """
        Get: LastActivityDate(self: MembershipUser) -> DateTime
        Set: LastActivityDate(self: MembershipUser) = value
        """
        ...

    @property
    def LastLockoutDate(self) -> DateTime:
        """ Get: LastLockoutDate(self: MembershipUser) -> DateTime """
        ...

    @property
    def LastLoginDate(self) -> DateTime:
        """
        Get: LastLoginDate(self: MembershipUser) -> DateTime
        Set: LastLoginDate(self: MembershipUser) = value
        """
        ...

    @property
    def LastPasswordChangedDate(self) -> DateTime:
        """ Get: LastPasswordChangedDate(self: MembershipUser) -> DateTime """
        ...

    @property
    def PasswordQuestion(self) -> str:
        """ Get: PasswordQuestion(self: MembershipUser) -> str """
        ...

    @property
    def ProviderName(self) -> str:
        """ Get: ProviderName(self: MembershipUser) -> str """
        ...

    @property
    def ProviderUserKey(self) -> object:
        """ Get: ProviderUserKey(self: MembershipUser) -> object """
        ...

    @property
    def UserName(self) -> str:
        """ Get: UserName(self: MembershipUser) -> str """
        ...


    def ChangePassword(self, oldPassword:str, newPassword:str) -> bool:
        """ ChangePassword(self: MembershipUser, oldPassword: str, newPassword: str) -> bool """
        ...

    def ChangePasswordQuestionAndAnswer(self, password:str, newPasswordQuestion:str, newPasswordAnswer:str) -> bool:
        """ ChangePasswordQuestionAndAnswer(self: MembershipUser, password: str, newPasswordQuestion: str, newPasswordAnswer: str) -> bool """
        ...

    def GetPassword(self, passwordAnswer:str = ...) -> str:
        """
        GetPassword(self: MembershipUser) -> str
        GetPassword(self: MembershipUser, passwordAnswer: str) -> str
        """
        ...

    def ResetPassword(self, passwordAnswer:str = ...) -> str:
        """
        ResetPassword(self: MembershipUser) -> str
        ResetPassword(self: MembershipUser, passwordAnswer: str) -> str
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: MembershipUser) -> str """
        ...

    def UnlockUser(self) -> bool:
        """ UnlockUser(self: MembershipUser) -> bool """
        ...


class ActiveDirectoryMembershipUser(MembershipUser): # skipped bases: <type 'object'>
    """ ActiveDirectoryMembershipUser(providerName: str, name: str, providerUserKey: object, email: str, passwordQuestion: str, comment: str, isApproved: bool, isLockedOut: bool, creationDate: DateTime, lastLoginDate: DateTime, lastActivityDate: DateTime, lastPasswordChangedDate: DateTime, lastLockoutDate: DateTime) """
    pass

class AnonymousIdentificationEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ AnonymousIdentificationEventArgs(context: HttpContext) """
    @property
    def AnonymousID(self) -> str:
        """
        Get: AnonymousID(self: AnonymousIdentificationEventArgs) -> str
        Set: AnonymousID(self: AnonymousIdentificationEventArgs) = value
        """
        ...

    @property
    def Context(self) -> HttpContext:
        """ Get: Context(self: AnonymousIdentificationEventArgs) -> HttpContext """
        ...


    def __new__(cls, context:HttpContext) -> Self:
        """ __new__(cls: type, context: HttpContext) """
        ...


class AnonymousIdentificationEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ AnonymousIdentificationEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:AnonymousIdentificationEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: AnonymousIdentificationEventHandler, sender: object, e: AnonymousIdentificationEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: AnonymousIdentificationEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:AnonymousIdentificationEventArgs): # -> 
        """ Invoke(self: AnonymousIdentificationEventHandler, sender: object, e: AnonymousIdentificationEventArgs) """
        ...


class AnonymousIdentificationModule(IHttpModule): # skipped bases: <type 'object'>
    """ AnonymousIdentificationModule() """
    @property
    def Enabled(self) -> bool:
        """ Get: Enabled() -> bool """
        ...


    @staticmethod
    def ClearAnonymousIdentifier(): # -> 
        """ ClearAnonymousIdentifier() """
        ...

    Creating = ...


class RoleProvider(ProviderBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: RoleProvider) -> str
        Set: ApplicationName(self: RoleProvider) = value
        """
        ...


    def AddUsersToRoles(self, usernames:Array, roleNames:Array): # -> 
        """ AddUsersToRoles(self: RoleProvider, usernames: Array[str], roleNames: Array[str]) """
        ...

    def CreateRole(self, roleName:str): # -> 
        """ CreateRole(self: RoleProvider, roleName: str) """
        ...

    def DeleteRole(self, roleName:str, throwOnPopulatedRole:bool) -> bool:
        """ DeleteRole(self: RoleProvider, roleName: str, throwOnPopulatedRole: bool) -> bool """
        ...

    def FindUsersInRole(self, roleName:str, usernameToMatch:str) -> Array:
        """ FindUsersInRole(self: RoleProvider, roleName: str, usernameToMatch: str) -> Array[str] """
        ...

    def GetAllRoles(self) -> Array:
        """ GetAllRoles(self: RoleProvider) -> Array[str] """
        ...

    def GetRolesForUser(self, username:str) -> Array:
        """ GetRolesForUser(self: RoleProvider, username: str) -> Array[str] """
        ...

    def GetUsersInRole(self, roleName:str) -> Array:
        """ GetUsersInRole(self: RoleProvider, roleName: str) -> Array[str] """
        ...

    def IsUserInRole(self, username:str, roleName:str) -> bool:
        """ IsUserInRole(self: RoleProvider, username: str, roleName: str) -> bool """
        ...

    def RemoveUsersFromRoles(self, usernames:Array, roleNames:Array): # -> 
        """ RemoveUsersFromRoles(self: RoleProvider, usernames: Array[str], roleNames: Array[str]) """
        ...

    def RoleExists(self, roleName:str) -> bool:
        """ RoleExists(self: RoleProvider, roleName: str) -> bool """
        ...


class AuthorizationStoreRoleProvider(RoleProvider): # skipped bases: <type 'object'>
    """ AuthorizationStoreRoleProvider() """
    @property
    def CacheRefreshInterval(self) -> int:
        """ Get: CacheRefreshInterval(self: AuthorizationStoreRoleProvider) -> int """
        ...

    @property
    def ScopeName(self) -> str:
        """
        Get: ScopeName(self: AuthorizationStoreRoleProvider) -> str
        Set: ScopeName(self: AuthorizationStoreRoleProvider) = value
        """
        ...


    def Initialize(self, name:str, config:NameValueCollection): # -> 
        """ Initialize(self: AuthorizationStoreRoleProvider, name: str, config: NameValueCollection) """
        ...


class CookieProtection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CookieProtection, values: All (3), Encryption (2), None (0), Validation (1) """
    All: CookieProtection = ...
    Encryption: CookieProtection = ...
    Validation: CookieProtection = ...
    value__ = ...


class DefaultAuthenticationEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DefaultAuthenticationEventArgs(context: HttpContext) """
    @property
    def Context(self) -> HttpContext:
        """ Get: Context(self: DefaultAuthenticationEventArgs) -> HttpContext """
        ...


    def __new__(cls, context:HttpContext) -> Self:
        """ __new__(cls: type, context: HttpContext) """
        ...


class DefaultAuthenticationEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DefaultAuthenticationEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DefaultAuthenticationEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DefaultAuthenticationEventHandler, sender: object, e: DefaultAuthenticationEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DefaultAuthenticationEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DefaultAuthenticationEventArgs): # -> 
        """ Invoke(self: DefaultAuthenticationEventHandler, sender: object, e: DefaultAuthenticationEventArgs) """
        ...


class DefaultAuthenticationModule(IHttpModule): # skipped bases: <type 'object'>
    """ DefaultAuthenticationModule() """
    Authenticate = ...


class FileAuthorizationModule(IHttpModule): # skipped bases: <type 'object'>
    """ FileAuthorizationModule() """
    @staticmethod
    def CheckFileAccessForUser(virtualPath:str, token:IntPtr, verb:str) -> bool:
        """ CheckFileAccessForUser(virtualPath: str, token: IntPtr, verb: str) -> bool """
        ...


class FormsAuthentication: # skipped bases: <type 'object'>, <type 'object'>
    """ FormsAuthentication() """
    @property
    def CookieDomain(self) -> str:
        """ Get: CookieDomain() -> str """
        ...

    @property
    def CookieMode(self) -> HttpCookieMode:
        """ Get: CookieMode() -> HttpCookieMode """
        ...

    @property
    def CookieSameSite(self) -> SameSiteMode:
        """ Get: CookieSameSite() -> SameSiteMode """
        ...

    @property
    def CookiesSupported(self) -> bool:
        """ Get: CookiesSupported() -> bool """
        ...

    @property
    def DefaultUrl(self) -> str:
        """ Get: DefaultUrl() -> str """
        ...

    @property
    def EnableCrossAppRedirects(self) -> bool:
        """ Get: EnableCrossAppRedirects() -> bool """
        ...

    @property
    def FormsCookieName(self) -> str:
        """ Get: FormsCookieName() -> str """
        ...

    @property
    def FormsCookiePath(self) -> str:
        """ Get: FormsCookiePath() -> str """
        ...

    @property
    def IsEnabled(self) -> bool:
        """ Get: IsEnabled() -> bool """
        ...

    @property
    def LoginUrl(self) -> str:
        """ Get: LoginUrl() -> str """
        ...

    @property
    def RequireSSL(self) -> bool:
        """ Get: RequireSSL() -> bool """
        ...

    @property
    def SlidingExpiration(self) -> bool:
        """ Get: SlidingExpiration() -> bool """
        ...

    @property
    def TicketCompatibilityMode(self) -> TicketCompatibilityMode:
        """ Get: TicketCompatibilityMode() -> TicketCompatibilityMode """
        ...

    @property
    def Timeout(self) -> TimeSpan:
        """ Get: Timeout() -> TimeSpan """
        ...


    @staticmethod
    def Authenticate(name:str, password:str) -> bool:
        """ Authenticate(name: str, password: str) -> bool """
        ...

    @staticmethod
    def Decrypt(encryptedTicket:str): # -> FormsAuthenticationTicket
        """ Decrypt(encryptedTicket: str) -> FormsAuthenticationTicket """
        ...

    @staticmethod
    def EnableFormsAuthentication(configurationData:NameValueCollection): # -> 
        """ EnableFormsAuthentication(configurationData: NameValueCollection) """
        ...

    @staticmethod
    def Encrypt(ticket) -> str: # Not found arg types: {'ticket': 'FormsAuthenticationTicket'}
        """ Encrypt(ticket: FormsAuthenticationTicket) -> str """
        ...

    @staticmethod
    def GetAuthCookie(userName:str, createPersistentCookie:bool, strCookiePath:str = ...) -> HttpCookie:
        """
        GetAuthCookie(userName: str, createPersistentCookie: bool) -> HttpCookie
        GetAuthCookie(userName: str, createPersistentCookie: bool, strCookiePath: str) -> HttpCookie
        """
        ...

    @staticmethod
    def GetRedirectUrl(userName:str, createPersistentCookie:bool) -> str:
        """ GetRedirectUrl(userName: str, createPersistentCookie: bool) -> str """
        ...

    @staticmethod
    def HashPasswordForStoringInConfigFile(password:str, passwordFormat:str) -> str:
        """ HashPasswordForStoringInConfigFile(password: str, passwordFormat: str) -> str """
        ...

    @staticmethod
    def Initialize(): # -> 
        """ Initialize() """
        ...

    @staticmethod
    def RedirectFromLoginPage(userName:str, createPersistentCookie:bool, strCookiePath:str = ...): # -> 
        """ RedirectFromLoginPage(userName: str, createPersistentCookie: bool)RedirectFromLoginPage(userName: str, createPersistentCookie: bool, strCookiePath: str) """
        ...

    @staticmethod
    def RedirectToLoginPage(extraQueryString=None): # -> 
        """ RedirectToLoginPage()RedirectToLoginPage(extraQueryString: str) """
        ...

    @staticmethod
    def RenewTicketIfOld(tOld): # -> FormsAuthenticationTicket # Not found arg types: {'tOld': 'FormsAuthenticationTicket'}
        """ RenewTicketIfOld(tOld: FormsAuthenticationTicket) -> FormsAuthenticationTicket """
        ...

    @staticmethod
    def SetAuthCookie(userName:str, createPersistentCookie:bool, strCookiePath:str = ...): # -> 
        """ SetAuthCookie(userName: str, createPersistentCookie: bool)SetAuthCookie(userName: str, createPersistentCookie: bool, strCookiePath: str) """
        ...

    @staticmethod
    def SignOut(): # -> 
        """ SignOut() """
        ...



class FormsAuthenticationEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ FormsAuthenticationEventArgs(context: HttpContext) """
    @property
    def Context(self) -> HttpContext:
        """ Get: Context(self: FormsAuthenticationEventArgs) -> HttpContext """
        ...

    @property
    def User(self) -> IPrincipal:
        """
        Get: User(self: FormsAuthenticationEventArgs) -> IPrincipal
        Set: User(self: FormsAuthenticationEventArgs) = value
        """
        ...


    def __new__(cls, context:HttpContext) -> Self:
        """ __new__(cls: type, context: HttpContext) """
        ...


class FormsAuthenticationEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ FormsAuthenticationEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:FormsAuthenticationEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: FormsAuthenticationEventHandler, sender: object, e: FormsAuthenticationEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: FormsAuthenticationEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:FormsAuthenticationEventArgs): # -> 
        """ Invoke(self: FormsAuthenticationEventHandler, sender: object, e: FormsAuthenticationEventArgs) """
        ...


class FormsAuthenticationModule(IHttpModule): # skipped bases: <type 'object'>
    """ FormsAuthenticationModule() """
    Authenticate = ...


class FormsAuthenticationTicket: # skipped bases: <type 'object'>, <type 'object'>
    """
    FormsAuthenticationTicket(version: int, name: str, issueDate: DateTime, expiration: DateTime, isPersistent: bool, userData: str)
    FormsAuthenticationTicket(version: int, name: str, issueDate: DateTime, expiration: DateTime, isPersistent: bool, userData: str, cookiePath: str)
    FormsAuthenticationTicket(name: str, isPersistent: bool, timeout: int)
    """
    @property
    def CookiePath(self) -> str:
        """ Get: CookiePath(self: FormsAuthenticationTicket) -> str """
        ...

    @property
    def Expiration(self) -> DateTime:
        """ Get: Expiration(self: FormsAuthenticationTicket) -> DateTime """
        ...

    @property
    def Expired(self) -> bool:
        """ Get: Expired(self: FormsAuthenticationTicket) -> bool """
        ...

    @property
    def IsPersistent(self) -> bool:
        """ Get: IsPersistent(self: FormsAuthenticationTicket) -> bool """
        ...

    @property
    def IssueDate(self) -> DateTime:
        """ Get: IssueDate(self: FormsAuthenticationTicket) -> DateTime """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: FormsAuthenticationTicket) -> str """
        ...

    @property
    def UserData(self) -> str:
        """ Get: UserData(self: FormsAuthenticationTicket) -> str """
        ...

    @property
    def Version(self) -> int:
        """ Get: Version(self: FormsAuthenticationTicket) -> int """
        ...



class FormsIdentity(ClaimsIdentity): # skipped bases: <type 'IIdentity'>, <type 'object'>
    """ FormsIdentity(ticket: FormsAuthenticationTicket) """
    @property
    def Ticket(self) -> FormsAuthenticationTicket:
        """ Get: Ticket(self: FormsIdentity) -> FormsAuthenticationTicket """
        ...



class MachineKey: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Decode(encodedData:str, protectionOption) -> Array: # Not found arg types: {'protectionOption': 'MachineKeyProtection'}
        """ Decode(encodedData: str, protectionOption: MachineKeyProtection) -> Array[Byte] """
        ...

    @staticmethod
    def Encode(data:Array, protectionOption) -> str: # Not found arg types: {'protectionOption': 'MachineKeyProtection'}
        """ Encode(data: Array[Byte], protectionOption: MachineKeyProtection) -> str """
        ...

    @staticmethod
    def Protect(userData:Array, purposes:Array) -> Array:
        """ Protect(userData: Array[Byte], *purposes: Array[str]) -> Array[Byte] """
        ...

    @staticmethod
    def Unprotect(protectedData:Array, purposes:Array) -> Array:
        """ Unprotect(protectedData: Array[Byte], *purposes: Array[str]) -> Array[Byte] """
        ...

    __all__: list = ...


class MachineKeyProtection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MachineKeyProtection, values: All (0), Encryption (1), Validation (2) """
    All: MachineKeyProtection = ...
    Encryption: MachineKeyProtection = ...
    Validation: MachineKeyProtection = ...
    value__ = ...


class Membership: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName() -> str
        Set: ApplicationName() = value
        """
        ...

    @property
    def EnablePasswordReset(self) -> bool:
        """ Get: EnablePasswordReset() -> bool """
        ...

    @property
    def EnablePasswordRetrieval(self) -> bool:
        """ Get: EnablePasswordRetrieval() -> bool """
        ...

    @property
    def HashAlgorithmType(self) -> str:
        """ Get: HashAlgorithmType() -> str """
        ...

    @property
    def MaxInvalidPasswordAttempts(self) -> int:
        """ Get: MaxInvalidPasswordAttempts() -> int """
        ...

    @property
    def MinRequiredNonAlphanumericCharacters(self) -> int:
        """ Get: MinRequiredNonAlphanumericCharacters() -> int """
        ...

    @property
    def MinRequiredPasswordLength(self) -> int:
        """ Get: MinRequiredPasswordLength() -> int """
        ...

    @property
    def PasswordAttemptWindow(self) -> int:
        """ Get: PasswordAttemptWindow() -> int """
        ...

    @property
    def PasswordStrengthRegularExpression(self) -> str:
        """ Get: PasswordStrengthRegularExpression() -> str """
        ...

    @property
    def Provider(self) -> MembershipProvider:
        """ Get: Provider() -> MembershipProvider """
        ...

    @property
    def Providers(self) -> MembershipProviderCollection:
        """ Get: Providers() -> MembershipProviderCollection """
        ...

    @property
    def RequiresQuestionAndAnswer(self) -> bool:
        """ Get: RequiresQuestionAndAnswer() -> bool """
        ...

    @property
    def UserIsOnlineTimeWindow(self) -> int:
        """ Get: UserIsOnlineTimeWindow() -> int """
        ...


    @staticmethod
    def CreateUser(username:str, password:str, email:str = ..., passwordQuestion:str = ..., passwordAnswer:str = ..., isApproved:bool = ..., *__args:object) -> Tuple_[MembershipUser, MembershipCreateStatus]:
        """
        CreateUser(username: str, password: str) -> MembershipUser
        CreateUser(username: str, password: str, email: str, passwordQuestion: str, passwordAnswer: str, isApproved: bool) -> (MembershipUser, MembershipCreateStatus)
        CreateUser(username: str, password: str, email: str) -> MembershipUser
        CreateUser(username: str, password: str, email: str, passwordQuestion: str, passwordAnswer: str, isApproved: bool, providerUserKey: object) -> (MembershipUser, MembershipCreateStatus)
        """
        ...

    @staticmethod
    def DeleteUser(username:str, deleteAllRelatedData:bool = ...) -> bool:
        """
        DeleteUser(username: str) -> bool
        DeleteUser(username: str, deleteAllRelatedData: bool) -> bool
        """
        ...

    @staticmethod
    def FindUsersByEmail(emailToMatch, pageIndex=None, pageSize=None, totalRecords=None) -> Tuple_[MembershipUserCollection, int]:
        """
        FindUsersByEmail(emailToMatch: str, pageIndex: int, pageSize: int) -> (MembershipUserCollection, int)
        FindUsersByEmail(emailToMatch: str) -> MembershipUserCollection
        """
        ...

    @staticmethod
    def FindUsersByName(usernameToMatch, pageIndex=None, pageSize=None, totalRecords=None) -> Tuple_[MembershipUserCollection, int]:
        """
        FindUsersByName(usernameToMatch: str, pageIndex: int, pageSize: int) -> (MembershipUserCollection, int)
        FindUsersByName(usernameToMatch: str) -> MembershipUserCollection
        """
        ...

    @staticmethod
    def GeneratePassword(length:int, numberOfNonAlphanumericCharacters:int) -> str:
        """ GeneratePassword(length: int, numberOfNonAlphanumericCharacters: int) -> str """
        ...

    @staticmethod
    def GetAllUsers(pageIndex=None, pageSize=None, totalRecords=None) -> MembershipUserCollection:
        """
        GetAllUsers() -> MembershipUserCollection
        GetAllUsers(pageIndex: int, pageSize: int) -> (MembershipUserCollection, int)
        """
        ...

    @staticmethod
    def GetNumberOfUsersOnline() -> int:
        """ GetNumberOfUsersOnline() -> int """
        ...

    @staticmethod
    def GetUser(*__args) -> MembershipUser:
        """
        GetUser() -> MembershipUser
        GetUser(userIsOnline: bool) -> MembershipUser
        GetUser(username: str) -> MembershipUser
        GetUser(providerUserKey: object) -> MembershipUser
        GetUser(username: str, userIsOnline: bool) -> MembershipUser
        GetUser(providerUserKey: object, userIsOnline: bool) -> MembershipUser
        """
        ...

    @staticmethod
    def GetUserNameByEmail(emailToMatch:str) -> str:
        """ GetUserNameByEmail(emailToMatch: str) -> str """
        ...

    @staticmethod
    def UpdateUser(user:MembershipUser): # -> 
        """ UpdateUser(user: MembershipUser) """
        ...

    @staticmethod
    def ValidateUser(username:str, password:str) -> bool:
        """ ValidateUser(username: str, password: str) -> bool """
        ...

    ValidatingPassword = ...
    __all__: list = ...


class MembershipCreateStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MembershipCreateStatus, values: DuplicateEmail (7), DuplicateProviderUserKey (10), DuplicateUserName (6), InvalidAnswer (4), InvalidEmail (5), InvalidPassword (2), InvalidProviderUserKey (9), InvalidQuestion (3), InvalidUserName (1), ProviderError (11), Success (0), UserRejected (8) """
    DuplicateEmail: MembershipCreateStatus = ...
    DuplicateProviderUserKey: MembershipCreateStatus = ...
    DuplicateUserName: MembershipCreateStatus = ...
    InvalidAnswer: MembershipCreateStatus = ...
    InvalidEmail: MembershipCreateStatus = ...
    InvalidPassword: MembershipCreateStatus = ...
    InvalidProviderUserKey: MembershipCreateStatus = ...
    InvalidQuestion: MembershipCreateStatus = ...
    InvalidUserName: MembershipCreateStatus = ...
    ProviderError: MembershipCreateStatus = ...
    Success: MembershipCreateStatus = ...
    UserRejected: MembershipCreateStatus = ...
    value__ = ...


class MembershipCreateUserException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MembershipCreateUserException(statusCode: MembershipCreateStatus)
    MembershipCreateUserException(message: str)
    MembershipCreateUserException()
    MembershipCreateUserException(message: str, innerException: Exception)
    """
    @property
    def StatusCode(self) -> MembershipCreateStatus:
        """ Get: StatusCode(self: MembershipCreateUserException) -> MembershipCreateStatus """
        ...


    SerializeObjectState = ...


class MembershipPasswordAttribute(ValidationAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MembershipPasswordAttribute() """
    @property
    def MinNonAlphanumericCharactersError(self) -> str:
        """
        Get: MinNonAlphanumericCharactersError(self: MembershipPasswordAttribute) -> str
        Set: MinNonAlphanumericCharactersError(self: MembershipPasswordAttribute) = value
        """
        ...

    @property
    def MinPasswordLengthError(self) -> str:
        """
        Get: MinPasswordLengthError(self: MembershipPasswordAttribute) -> str
        Set: MinPasswordLengthError(self: MembershipPasswordAttribute) = value
        """
        ...

    @property
    def MinRequiredNonAlphanumericCharacters(self) -> int:
        """
        Get: MinRequiredNonAlphanumericCharacters(self: MembershipPasswordAttribute) -> int
        Set: MinRequiredNonAlphanumericCharacters(self: MembershipPasswordAttribute) = value
        """
        ...

    @property
    def MinRequiredPasswordLength(self) -> int:
        """
        Get: MinRequiredPasswordLength(self: MembershipPasswordAttribute) -> int
        Set: MinRequiredPasswordLength(self: MembershipPasswordAttribute) = value
        """
        ...

    @property
    def PasswordStrengthError(self) -> str:
        """
        Get: PasswordStrengthError(self: MembershipPasswordAttribute) -> str
        Set: PasswordStrengthError(self: MembershipPasswordAttribute) = value
        """
        ...

    @property
    def PasswordStrengthRegexTimeout(self) -> Nullable:
        """
        Get: PasswordStrengthRegexTimeout(self: MembershipPasswordAttribute) -> Nullable[int]
        Set: PasswordStrengthRegexTimeout(self: MembershipPasswordAttribute) = value
        """
        ...

    @property
    def PasswordStrengthRegularExpression(self) -> str:
        """
        Get: PasswordStrengthRegularExpression(self: MembershipPasswordAttribute) -> str
        Set: PasswordStrengthRegularExpression(self: MembershipPasswordAttribute) = value
        """
        ...

    @property
    def ResourceType(self) -> Type:
        """
        Get: ResourceType(self: MembershipPasswordAttribute) -> Type
        Set: ResourceType(self: MembershipPasswordAttribute) = value
        """
        ...



class MembershipPasswordException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MembershipPasswordException(message: str)
    MembershipPasswordException()
    MembershipPasswordException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class MembershipPasswordFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MembershipPasswordFormat, values: Clear (0), Encrypted (2), Hashed (1) """
    Clear: MembershipPasswordFormat = ...
    Encrypted: MembershipPasswordFormat = ...
    Hashed: MembershipPasswordFormat = ...
    value__ = ...


class MembershipProviderCollection(ProviderCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ MembershipProviderCollection() """
    pass

class MembershipUserCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ MembershipUserCollection() """
    def Add(self, user:MembershipUser): # -> 
        """ Add(self: MembershipUserCollection, user: MembershipUser) """
        ...

    def Clear(self): # -> 
        """ Clear(self: MembershipUserCollection) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: MembershipUserCollection) -> IEnumerator """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: MembershipUserCollection, name: str) """
        ...

    def SetReadOnly(self): # -> 
        """ SetReadOnly(self: MembershipUserCollection) """
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


class MembershipValidatePasswordEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MembershipValidatePasswordEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ValidatePasswordEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: MembershipValidatePasswordEventHandler, sender: object, e: ValidatePasswordEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: MembershipValidatePasswordEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ValidatePasswordEventArgs): # -> 
        """ Invoke(self: MembershipValidatePasswordEventHandler, sender: object, e: ValidatePasswordEventArgs) """
        ...


class PassportAuthenticationEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ PassportAuthenticationEventArgs(identity: PassportIdentity, context: HttpContext) """
    @property
    def Context(self) -> HttpContext:
        """ Get: Context(self: PassportAuthenticationEventArgs) -> HttpContext """
        ...

    @property
    def Identity(self): # -> PassportIdentity
        """ Get: Identity(self: PassportAuthenticationEventArgs) -> PassportIdentity """
        ...

    @property
    def User(self) -> IPrincipal:
        """
        Get: User(self: PassportAuthenticationEventArgs) -> IPrincipal
        Set: User(self: PassportAuthenticationEventArgs) = value
        """
        ...


    def __new__(cls, identity, context:HttpContext) -> Self: # Not found arg types: {'identity': 'PassportIdentity'}
        """ __new__(cls: type, identity: PassportIdentity, context: HttpContext) """
        ...


class PassportAuthenticationEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PassportAuthenticationEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:PassportAuthenticationEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PassportAuthenticationEventHandler, sender: object, e: PassportAuthenticationEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PassportAuthenticationEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:PassportAuthenticationEventArgs): # -> 
        """ Invoke(self: PassportAuthenticationEventHandler, sender: object, e: PassportAuthenticationEventArgs) """
        ...


class PassportAuthenticationModule(IHttpModule): # skipped bases: <type 'object'>
    """ PassportAuthenticationModule() """
    Authenticate = ...


class PassportIdentity(IDisposable, IIdentity): # skipped bases: <type 'object'>
    """ PassportIdentity() """
    @property
    def Error(self) -> int:
        """ Get: Error(self: PassportIdentity) -> int """
        ...

    @property
    def GetFromNetworkServer(self) -> bool:
        """ Get: GetFromNetworkServer(self: PassportIdentity) -> bool """
        ...

    @property
    def HasSavedPassword(self) -> bool:
        """ Get: HasSavedPassword(self: PassportIdentity) -> bool """
        ...

    @property
    def HasTicket(self) -> bool:
        """ Get: HasTicket(self: PassportIdentity) -> bool """
        ...

    @property
    def HexPUID(self) -> str:
        """ Get: HexPUID(self: PassportIdentity) -> str """
        ...

    @property
    def TicketAge(self) -> int:
        """ Get: TicketAge(self: PassportIdentity) -> int """
        ...

    @property
    def TimeSinceSignIn(self) -> int:
        """ Get: TimeSinceSignIn(self: PassportIdentity) -> int """
        ...


    def AuthUrl(self, strReturnUrl=None, iTimeWindow=None, *__args) -> str:
        """
        AuthUrl(self: PassportIdentity) -> str
        AuthUrl(self: PassportIdentity, strReturnUrl: str) -> str
        AuthUrl(self: PassportIdentity, strReturnUrl: str, iTimeWindow: int, fForceLogin: bool, strCoBrandedArgs: str, iLangID: int, strNameSpace: str, iKPP: int, bUseSecureAuth: bool) -> str
        AuthUrl(self: PassportIdentity, strReturnUrl: str, iTimeWindow: int, iForceLogin: int, strCoBrandedArgs: str, iLangID: int, strNameSpace: str, iKPP: int, iUseSecureAuth: int) -> str
        """
        ...

    def AuthUrl2(self, strReturnUrl=None, iTimeWindow=None, *__args) -> str:
        """
        AuthUrl2(self: PassportIdentity) -> str
        AuthUrl2(self: PassportIdentity, strReturnUrl: str) -> str
        AuthUrl2(self: PassportIdentity, strReturnUrl: str, iTimeWindow: int, fForceLogin: bool, strCoBrandedArgs: str, iLangID: int, strNameSpace: str, iKPP: int, bUseSecureAuth: bool) -> str
        AuthUrl2(self: PassportIdentity, strReturnUrl: str, iTimeWindow: int, iForceLogin: int, strCoBrandedArgs: str, iLangID: int, strNameSpace: str, iKPP: int, iUseSecureAuth: int) -> str
        """
        ...

    @staticmethod
    def Compress(strData:str) -> str:
        """ Compress(strData: str) -> str """
        ...

    @staticmethod
    def CryptIsValid() -> bool:
        """ CryptIsValid() -> bool """
        ...

    @staticmethod
    def CryptPutHost(strHost:str) -> int:
        """ CryptPutHost(strHost: str) -> int """
        ...

    @staticmethod
    def CryptPutSite(strSite:str) -> int:
        """ CryptPutSite(strSite: str) -> int """
        ...

    @staticmethod
    def Decompress(strData:str) -> str:
        """ Decompress(strData: str) -> str """
        ...

    @staticmethod
    def Decrypt(strData:str) -> str:
        """ Decrypt(strData: str) -> str """
        ...

    @staticmethod
    def Encrypt(strData:str) -> str:
        """ Encrypt(strData: str) -> str """
        ...

    def GetCurrentConfig(self, strAttribute:str) -> object:
        """ GetCurrentConfig(self: PassportIdentity, strAttribute: str) -> object """
        ...

    def GetDomainAttribute(self, strAttribute:str, iLCID:int, strDomain:str) -> str:
        """ GetDomainAttribute(self: PassportIdentity, strAttribute: str, iLCID: int, strDomain: str) -> str """
        ...

    def GetDomainFromMemberName(self, strMemberName:str) -> str:
        """ GetDomainFromMemberName(self: PassportIdentity, strMemberName: str) -> str """
        ...

    def GetIsAuthenticated(self, iTimeWindow, *__args) -> bool:
        """
        GetIsAuthenticated(self: PassportIdentity, iTimeWindow: int, bForceLogin: bool, bCheckSecure: bool) -> bool
        GetIsAuthenticated(self: PassportIdentity, iTimeWindow: int, iForceLogin: int, iCheckSecure: int) -> bool
        """
        ...

    def GetLoginChallenge(self, *__args:str) -> str:
        """
        GetLoginChallenge(self: PassportIdentity) -> str
        GetLoginChallenge(self: PassportIdentity, strReturnUrl: str) -> str
        GetLoginChallenge(self: PassportIdentity, szRetURL: str, iTimeWindow: int, fForceLogin: int, szCOBrandArgs: str, iLangID: int, strNameSpace: str, iKPP: int, iUseSecureAuth: int, oExtraParams: object) -> str
        """
        ...

    def GetOption(self, strOpt:str) -> object:
        """ GetOption(self: PassportIdentity, strOpt: str) -> object """
        ...

    def GetProfileObject(self, strProfileName:str) -> object:
        """ GetProfileObject(self: PassportIdentity, strProfileName: str) -> object """
        ...

    def HasFlag(self, iFlagMask:int) -> bool:
        """ HasFlag(self: PassportIdentity, iFlagMask: int) -> bool """
        ...

    def HasProfile(self, strProfile:str) -> bool:
        """ HasProfile(self: PassportIdentity, strProfile: str) -> bool """
        ...

    def HaveConsent(self, bNeedFullConsent:bool, bNeedBirthdate:bool) -> bool:
        """ HaveConsent(self: PassportIdentity, bNeedFullConsent: bool, bNeedBirthdate: bool) -> bool """
        ...

    def LoginUser(self, *__args:str) -> int:
        """
        LoginUser(self: PassportIdentity, szRetURL: str, iTimeWindow: int, fForceLogin: bool, szCOBrandArgs: str, iLangID: int, strNameSpace: str, iKPP: int, fUseSecureAuth: bool, oExtraParams: object) -> int
        LoginUser(self: PassportIdentity) -> int
        LoginUser(self: PassportIdentity, strReturnUrl: str) -> int
        LoginUser(self: PassportIdentity, szRetURL: str, iTimeWindow: int, fForceLogin: int, szCOBrandArgs: str, iLangID: int, strNameSpace: str, iKPP: int, iUseSecureAuth: int, oExtraParams: object) -> int
        """
        ...

    def LogoTag(self, strReturnUrl=None, iTimeWindow=None, *__args) -> str:
        """
        LogoTag(self: PassportIdentity) -> str
        LogoTag(self: PassportIdentity, strReturnUrl: str) -> str
        LogoTag(self: PassportIdentity, strReturnUrl: str, iTimeWindow: int, fForceLogin: bool, strCoBrandedArgs: str, iLangID: int, fSecure: bool, strNameSpace: str, iKPP: int, bUseSecureAuth: bool) -> str
        LogoTag(self: PassportIdentity, strReturnUrl: str, iTimeWindow: int, iForceLogin: int, strCoBrandedArgs: str, iLangID: int, iSecure: int, strNameSpace: str, iKPP: int, iUseSecureAuth: int) -> str
        """
        ...

    def LogoTag2(self, strReturnUrl=None, iTimeWindow=None, *__args) -> str:
        """
        LogoTag2(self: PassportIdentity) -> str
        LogoTag2(self: PassportIdentity, strReturnUrl: str) -> str
        LogoTag2(self: PassportIdentity, strReturnUrl: str, iTimeWindow: int, fForceLogin: bool, strCoBrandedArgs: str, iLangID: int, fSecure: bool, strNameSpace: str, iKPP: int, bUseSecureAuth: bool) -> str
        LogoTag2(self: PassportIdentity, strReturnUrl: str, iTimeWindow: int, iForceLogin: int, strCoBrandedArgs: str, iLangID: int, iSecure: int, strNameSpace: str, iKPP: int, iUseSecureAuth: int) -> str
        """
        ...

    def LogoutURL(self, szReturnURL:str = ..., szCOBrandArgs:str = ..., iLangID:int = ..., strDomain:str = ..., iUseSecureAuth:int = ...) -> str:
        """
        LogoutURL(self: PassportIdentity) -> str
        LogoutURL(self: PassportIdentity, szReturnURL: str, szCOBrandArgs: str, iLangID: int, strDomain: str, iUseSecureAuth: int) -> str
        """
        ...

    def SetOption(self, strOpt:str, vOpt:object): # -> 
        """ SetOption(self: PassportIdentity, strOpt: str, vOpt: object) """
        ...

    @staticmethod
    def SignOut(strSignOutDotGifFileName:str): # -> 
        """ SignOut(strSignOutDotGifFileName: str) """
        ...

    def Ticket(self, strAttribute:str) -> object:
        """ Ticket(self: PassportIdentity, strAttribute: str) -> object """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class PassportPrincipal(GenericPrincipal): # skipped bases: <type 'IPrincipal'>, <type 'object'>
    """ PassportPrincipal(identity: PassportIdentity, roles: Array[str]) """
    pass

class RoleManagerEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ RoleManagerEventArgs(context: HttpContext) """
    @property
    def Context(self) -> HttpContext:
        """ Get: Context(self: RoleManagerEventArgs) -> HttpContext """
        ...

    @property
    def RolesPopulated(self) -> bool:
        """
        Get: RolesPopulated(self: RoleManagerEventArgs) -> bool
        Set: RolesPopulated(self: RoleManagerEventArgs) = value
        """
        ...


    def __new__(cls, context:HttpContext) -> Self:
        """ __new__(cls: type, context: HttpContext) """
        ...


class RoleManagerEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ RoleManagerEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:RoleManagerEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: RoleManagerEventHandler, sender: object, e: RoleManagerEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: RoleManagerEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:RoleManagerEventArgs): # -> 
        """ Invoke(self: RoleManagerEventHandler, sender: object, e: RoleManagerEventArgs) """
        ...


class RoleManagerModule(IHttpModule): # skipped bases: <type 'object'>
    """ RoleManagerModule() """
    GetRoles = ...


class RolePrincipal(ISerializable, ClaimsPrincipal): # skipped bases: <type 'IPrincipal'>, <type 'object'>
    """
    RolePrincipal(identity: IIdentity, encryptedTicket: str)
    RolePrincipal(identity: IIdentity)
    RolePrincipal(providerName: str, identity: IIdentity)
    RolePrincipal(providerName: str, identity: IIdentity, encryptedTicket: str)
    """
    @property
    def CachedListChanged(self) -> bool:
        """ Get: CachedListChanged(self: RolePrincipal) -> bool """
        ...

    @property
    def CookiePath(self) -> str:
        """ Get: CookiePath(self: RolePrincipal) -> str """
        ...

    @property
    def Expired(self) -> bool:
        """ Get: Expired(self: RolePrincipal) -> bool """
        ...

    @property
    def ExpireDate(self) -> DateTime:
        """ Get: ExpireDate(self: RolePrincipal) -> DateTime """
        ...

    @property
    def IsRoleListCached(self) -> bool:
        """ Get: IsRoleListCached(self: RolePrincipal) -> bool """
        ...

    @property
    def IssueDate(self) -> DateTime:
        """ Get: IssueDate(self: RolePrincipal) -> DateTime """
        ...

    @property
    def ProviderName(self) -> str:
        """ Get: ProviderName(self: RolePrincipal) -> str """
        ...

    @property
    def Version(self) -> int:
        """ Get: Version(self: RolePrincipal) -> int """
        ...


    def GetRoles(self) -> Array:
        """ GetRoles(self: RolePrincipal) -> Array[str] """
        ...

    def SetDirty(self): # -> 
        """ SetDirty(self: RolePrincipal) """
        ...

    def ToEncryptedTicket(self) -> str:
        """ ToEncryptedTicket(self: RolePrincipal) -> str """
        ...


class RoleProviderCollection(ProviderCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ RoleProviderCollection() """
    pass

class Roles: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName() -> str
        Set: ApplicationName() = value
        """
        ...

    @property
    def CacheRolesInCookie(self) -> bool:
        """ Get: CacheRolesInCookie() -> bool """
        ...

    @property
    def CookieName(self) -> str:
        """ Get: CookieName() -> str """
        ...

    @property
    def CookiePath(self) -> str:
        """ Get: CookiePath() -> str """
        ...

    @property
    def CookieProtectionValue(self) -> CookieProtection:
        """ Get: CookieProtectionValue() -> CookieProtection """
        ...

    @property
    def CookieRequireSSL(self) -> bool:
        """ Get: CookieRequireSSL() -> bool """
        ...

    @property
    def CookieSlidingExpiration(self) -> bool:
        """ Get: CookieSlidingExpiration() -> bool """
        ...

    @property
    def CookieTimeout(self) -> int:
        """ Get: CookieTimeout() -> int """
        ...

    @property
    def CreatePersistentCookie(self) -> bool:
        """ Get: CreatePersistentCookie() -> bool """
        ...

    @property
    def Domain(self) -> str:
        """ Get: Domain() -> str """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled() -> bool
        Set: Enabled() = value
        """
        ...

    @property
    def MaxCachedResults(self) -> int:
        """ Get: MaxCachedResults() -> int """
        ...

    @property
    def Provider(self) -> RoleProvider:
        """ Get: Provider() -> RoleProvider """
        ...

    @property
    def Providers(self) -> RoleProviderCollection:
        """ Get: Providers() -> RoleProviderCollection """
        ...


    @staticmethod
    def AddUsersToRole(usernames:Array, roleName:str): # -> 
        """ AddUsersToRole(usernames: Array[str], roleName: str) """
        ...

    @staticmethod
    def AddUsersToRoles(usernames:Array, roleNames:Array): # -> 
        """ AddUsersToRoles(usernames: Array[str], roleNames: Array[str]) """
        ...

    @staticmethod
    def AddUserToRole(username:str, roleName:str): # -> 
        """ AddUserToRole(username: str, roleName: str) """
        ...

    @staticmethod
    def AddUserToRoles(username:str, roleNames:Array): # -> 
        """ AddUserToRoles(username: str, roleNames: Array[str]) """
        ...

    @staticmethod
    def CreateRole(roleName:str): # -> 
        """ CreateRole(roleName: str) """
        ...

    @staticmethod
    def DeleteCookie(): # -> 
        """ DeleteCookie() """
        ...

    @staticmethod
    def DeleteRole(roleName:str, throwOnPopulatedRole:bool = ...) -> bool:
        """
        DeleteRole(roleName: str) -> bool
        DeleteRole(roleName: str, throwOnPopulatedRole: bool) -> bool
        """
        ...

    @staticmethod
    def FindUsersInRole(roleName:str, usernameToMatch:str) -> Array:
        """ FindUsersInRole(roleName: str, usernameToMatch: str) -> Array[str] """
        ...

    @staticmethod
    def GetAllRoles() -> Array:
        """ GetAllRoles() -> Array[str] """
        ...

    @staticmethod
    def GetRolesForUser(username=None) -> Array:
        """
        GetRolesForUser() -> Array[str]
        GetRolesForUser(username: str) -> Array[str]
        """
        ...

    @staticmethod
    def GetUsersInRole(roleName:str) -> Array:
        """ GetUsersInRole(roleName: str) -> Array[str] """
        ...

    @staticmethod
    def IsUserInRole(*__args:str) -> bool:
        """
        IsUserInRole(roleName: str) -> bool
        IsUserInRole(username: str, roleName: str) -> bool
        """
        ...

    @staticmethod
    def RemoveUserFromRole(username:str, roleName:str): # -> 
        """ RemoveUserFromRole(username: str, roleName: str) """
        ...

    @staticmethod
    def RemoveUserFromRoles(username:str, roleNames:Array): # -> 
        """ RemoveUserFromRoles(username: str, roleNames: Array[str]) """
        ...

    @staticmethod
    def RemoveUsersFromRole(usernames:Array, roleName:str): # -> 
        """ RemoveUsersFromRole(usernames: Array[str], roleName: str) """
        ...

    @staticmethod
    def RemoveUsersFromRoles(usernames:Array, roleNames:Array): # -> 
        """ RemoveUsersFromRoles(usernames: Array[str], roleNames: Array[str]) """
        ...

    @staticmethod
    def RoleExists(roleName:str) -> bool:
        """ RoleExists(roleName: str) -> bool """
        ...

    __all__: list = ...


class SqlMembershipProvider(MembershipProvider): # skipped bases: <type 'object'>
    """ SqlMembershipProvider() """
    def GeneratePassword(self) -> str:
        """ GeneratePassword(self: SqlMembershipProvider) -> str """
        ...

    def Initialize(self, name:str, config:NameValueCollection): # -> 
        """ Initialize(self: SqlMembershipProvider, name: str, config: NameValueCollection) """
        ...


class SqlRoleProvider(RoleProvider): # skipped bases: <type 'object'>
    """ SqlRoleProvider() """
    def Initialize(self, name:str, config:NameValueCollection): # -> 
        """ Initialize(self: SqlRoleProvider, name: str, config: NameValueCollection) """
        ...


class UrlAuthorizationModule(IHttpModule): # skipped bases: <type 'object'>
    """ UrlAuthorizationModule() """
    @staticmethod
    def CheckUrlAccessForPrincipal(virtualPath:str, user:IPrincipal, verb:str) -> bool:
        """ CheckUrlAccessForPrincipal(virtualPath: str, user: IPrincipal, verb: str) -> bool """
        ...


class ValidatePasswordEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ValidatePasswordEventArgs(userName: str, password: str, isNewUser: bool) """
    @property
    def Cancel(self) -> bool:
        """
        Get: Cancel(self: ValidatePasswordEventArgs) -> bool
        Set: Cancel(self: ValidatePasswordEventArgs) = value
        """
        ...

    @property
    def FailureInformation(self) -> Exception:
        """
        Get: FailureInformation(self: ValidatePasswordEventArgs) -> Exception
        Set: FailureInformation(self: ValidatePasswordEventArgs) = value
        """
        ...

    @property
    def IsNewUser(self) -> bool:
        """ Get: IsNewUser(self: ValidatePasswordEventArgs) -> bool """
        ...

    @property
    def Password(self) -> str:
        """ Get: Password(self: ValidatePasswordEventArgs) -> str """
        ...

    @property
    def UserName(self) -> str:
        """ Get: UserName(self: ValidatePasswordEventArgs) -> str """
        ...


    def __new__(cls, userName:str, password:str, isNewUser:bool) -> Self:
        """ __new__(cls: type, userName: str, password: str, isNewUser: bool) """
        ...


class WindowsAuthenticationEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ WindowsAuthenticationEventArgs(identity: WindowsIdentity, context: HttpContext) """
    @property
    def Context(self) -> HttpContext:
        """ Get: Context(self: WindowsAuthenticationEventArgs) -> HttpContext """
        ...

    @property
    def Identity(self) -> WindowsIdentity:
        """ Get: Identity(self: WindowsAuthenticationEventArgs) -> WindowsIdentity """
        ...

    @property
    def User(self) -> IPrincipal:
        """
        Get: User(self: WindowsAuthenticationEventArgs) -> IPrincipal
        Set: User(self: WindowsAuthenticationEventArgs) = value
        """
        ...


    def __new__(cls, identity:WindowsIdentity, context:HttpContext) -> Self:
        """ __new__(cls: type, identity: WindowsIdentity, context: HttpContext) """
        ...


class WindowsAuthenticationEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WindowsAuthenticationEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:WindowsAuthenticationEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WindowsAuthenticationEventHandler, sender: object, e: WindowsAuthenticationEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WindowsAuthenticationEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:WindowsAuthenticationEventArgs): # -> 
        """ Invoke(self: WindowsAuthenticationEventHandler, sender: object, e: WindowsAuthenticationEventArgs) """
        ...


class WindowsAuthenticationModule(IHttpModule): # skipped bases: <type 'object'>
    """ WindowsAuthenticationModule() """
    Authenticate = ...


class WindowsTokenRoleProvider(RoleProvider): # skipped bases: <type 'object'>
    """ WindowsTokenRoleProvider() """
    def Initialize(self, name:str, config:NameValueCollection): # -> 
        """ Initialize(self: WindowsTokenRoleProvider, name: str, config: NameValueCollection) """
        ...


# variables with complex values

