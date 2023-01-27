# encoding: utf-8
# module System.Web.ClientServices calls itself ClientServices
# from System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import IDisposable

from System.Net import CookieContainer

from System.Security.Principal import IIdentity, IPrincipal

from System.Web.Security import MembershipProvider


# no functions
# classes

class ClientFormsIdentity(IDisposable, IIdentity): # skipped bases: <type 'object'>
    """ ClientFormsIdentity(name: str, password: str, provider: MembershipProvider, authenticationType: str, isAuthenticated: bool, authenticationCookies: CookieContainer) """
    @property
    def AuthenticationCookies(self) -> CookieContainer:
        """ Get: AuthenticationCookies(self: ClientFormsIdentity) -> CookieContainer """
        ...

    @property
    def Provider(self) -> MembershipProvider:
        """ Get: Provider(self: ClientFormsIdentity) -> MembershipProvider """
        ...


    def RevalidateUser(self): # -> 
        """ RevalidateUser(self: ClientFormsIdentity) """
        ...


class ClientRolePrincipal(IPrincipal): # skipped bases: <type 'object'>
    """ ClientRolePrincipal(identity: IIdentity) """
    pass

class ConnectivityStatus: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsOffline(self) -> bool:
        """
        Get: IsOffline() -> bool
        Set: IsOffline() = value
        """
        ...


    __all__: list = ...


# variables with complex values

