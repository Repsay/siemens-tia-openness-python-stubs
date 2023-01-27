# encoding: utf-8
# module System.Web.ApplicationServices calls itself ApplicationServices
# from System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import Array, EventArgs

from System.Collections import IDictionary, IEnumerable

from System.Collections.Generic import Dictionary

from System.Reflection import ICustomAttributeProvider

from System.Security.Principal import IPrincipal

"""The following names are not found in the module: (BoundEvent, 
    IExtensibleDataObject, ServiceHostFactory)
"""

# no functions
# classes

class ApplicationServicesHostFactory(ServiceHostFactory): # skipped bases: <type 'object'>
    """ ApplicationServicesHostFactory() """
    pass

class AuthenticatingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Authenticated(self) -> bool:
        """
        Get: Authenticated(self: AuthenticatingEventArgs) -> bool
        Set: Authenticated(self: AuthenticatingEventArgs) = value
        """
        ...

    @property
    def AuthenticationIsComplete(self) -> bool:
        """
        Get: AuthenticationIsComplete(self: AuthenticatingEventArgs) -> bool
        Set: AuthenticationIsComplete(self: AuthenticatingEventArgs) = value
        """
        ...

    @property
    def CustomCredential(self) -> str:
        """ Get: CustomCredential(self: AuthenticatingEventArgs) -> str """
        ...

    @property
    def Password(self) -> str:
        """ Get: Password(self: AuthenticatingEventArgs) -> str """
        ...

    @property
    def UserName(self) -> str:
        """ Get: UserName(self: AuthenticatingEventArgs) -> str """
        ...



class AuthenticationService: # skipped bases: <type 'object'>, <type 'object'>
    """ AuthenticationService() """
    def IsLoggedIn(self) -> bool:
        """ IsLoggedIn(self: AuthenticationService) -> bool """
        ...

    def Login(self, username:str, password:str, customCredential:str, isPersistent:bool) -> bool:
        """ Login(self: AuthenticationService, username: str, password: str, customCredential: str, isPersistent: bool) -> bool """
        ...

    def Logout(self): # -> 
        """ Logout(self: AuthenticationService) """
        ...

    def ValidateUser(self, username:str, password:str, customCredential:str) -> bool:
        """ ValidateUser(self: AuthenticationService, username: str, password: str, customCredential: str) -> bool """
        ...

    Authenticating = ...
    CreatingCookie = ...


class CreatingCookieEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CookieIsSet(self) -> bool:
        """
        Get: CookieIsSet(self: CreatingCookieEventArgs) -> bool
        Set: CookieIsSet(self: CreatingCookieEventArgs) = value
        """
        ...

    @property
    def CustomCredential(self) -> str:
        """ Get: CustomCredential(self: CreatingCookieEventArgs) -> str """
        ...

    @property
    def IsPersistent(self) -> bool:
        """ Get: IsPersistent(self: CreatingCookieEventArgs) -> bool """
        ...

    @property
    def Password(self) -> str:
        """ Get: Password(self: CreatingCookieEventArgs) -> str """
        ...

    @property
    def UserName(self) -> str:
        """ Get: UserName(self: CreatingCookieEventArgs) -> str """
        ...



class KnownTypesProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetKnownTypes(knownTypeAttributeTarget:ICustomAttributeProvider) -> Array:
        """ GetKnownTypes(knownTypeAttributeTarget: ICustomAttributeProvider) -> Array[Type] """
        ...

    __all__: list = ...


class ProfilePropertyMetadata(IExtensibleDataObject): # skipped bases: <type 'object'>
    """ ProfilePropertyMetadata() """
    @property
    def AllowAnonymousAccess(self) -> bool:
        """
        Get: AllowAnonymousAccess(self: ProfilePropertyMetadata) -> bool
        Set: AllowAnonymousAccess(self: ProfilePropertyMetadata) = value
        """
        ...

    @property
    def DefaultValue(self) -> str:
        """
        Get: DefaultValue(self: ProfilePropertyMetadata) -> str
        Set: DefaultValue(self: ProfilePropertyMetadata) = value
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """
        Get: IsReadOnly(self: ProfilePropertyMetadata) -> bool
        Set: IsReadOnly(self: ProfilePropertyMetadata) = value
        """
        ...

    @property
    def PropertyName(self) -> str:
        """
        Get: PropertyName(self: ProfilePropertyMetadata) -> str
        Set: PropertyName(self: ProfilePropertyMetadata) = value
        """
        ...

    @property
    def SerializeAs(self) -> int:
        """
        Get: SerializeAs(self: ProfilePropertyMetadata) -> int
        Set: SerializeAs(self: ProfilePropertyMetadata) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: ProfilePropertyMetadata) -> str
        Set: TypeName(self: ProfilePropertyMetadata) = value
        """
        ...



class ProfileService: # skipped bases: <type 'object'>, <type 'object'>
    """ ProfileService() """
    def GetAllPropertiesForCurrentUser(self, authenticatedUserOnly:bool) -> Dictionary:
        """ GetAllPropertiesForCurrentUser(self: ProfileService, authenticatedUserOnly: bool) -> Dictionary[str, object] """
        ...

    def GetPropertiesForCurrentUser(self, properties:IEnumerable, authenticatedUserOnly:bool) -> Dictionary:
        """ GetPropertiesForCurrentUser(self: ProfileService, properties: IEnumerable[str], authenticatedUserOnly: bool) -> Dictionary[str, object] """
        ...

    def GetPropertiesMetadata(self) -> Array:
        """ GetPropertiesMetadata(self: ProfileService) -> Array[ProfilePropertyMetadata] """
        ...

    def SetPropertiesForCurrentUser(self, values:IDictionary, authenticatedUserOnly:bool) -> Collection:
        """ SetPropertiesForCurrentUser(self: ProfileService, values: IDictionary[str, object], authenticatedUserOnly: bool) -> Collection[str] """
        ...

    ValidatingProperties = ...


class RoleService: # skipped bases: <type 'object'>, <type 'object'>
    """ RoleService() """
    def GetRolesForCurrentUser(self) -> Array:
        """ GetRolesForCurrentUser(self: RoleService) -> Array[str] """
        ...

    def IsCurrentUserInRole(self, role:str) -> bool:
        """ IsCurrentUserInRole(self: RoleService, role: str) -> bool """
        ...

    SelectingProvider = ...


class SelectingProviderEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ProviderName(self) -> str:
        """
        Get: ProviderName(self: SelectingProviderEventArgs) -> str
        Set: ProviderName(self: SelectingProviderEventArgs) = value
        """
        ...

    @property
    def User(self) -> IPrincipal:
        """ Get: User(self: SelectingProviderEventArgs) -> IPrincipal """
        ...



class ValidatingPropertiesEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def FailedProperties(self) -> Collection:
        """ Get: FailedProperties(self: ValidatingPropertiesEventArgs) -> Collection[str] """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: ValidatingPropertiesEventArgs) -> IDictionary[str, object] """
        ...



