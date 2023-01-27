# encoding: utf-8
# module System.Web.ClientServices.Providers calls itself Providers
# from System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import EventArgs

from System.Collections import IEnumerable

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Collections.Specialized import NameValueCollection

from System.Configuration import (IApplicationSettingsProvider, 
    SettingsPropertyCollection, SettingsProvider)

from System.Web.Security import MembershipProvider, RoleProvider

from typing import Self

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class ClientFormsAuthenticationCredentials: # skipped bases: <type 'object'>, <type 'object'>
    """ ClientFormsAuthenticationCredentials(username: str, password: str, rememberMe: bool) """
    @property
    def Password(self) -> str:
        """
        Get: Password(self: ClientFormsAuthenticationCredentials) -> str
        Set: Password(self: ClientFormsAuthenticationCredentials) = value
        """
        ...

    @property
    def RememberMe(self) -> bool:
        """
        Get: RememberMe(self: ClientFormsAuthenticationCredentials) -> bool
        Set: RememberMe(self: ClientFormsAuthenticationCredentials) = value
        """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: ClientFormsAuthenticationCredentials) -> str
        Set: UserName(self: ClientFormsAuthenticationCredentials) = value
        """
        ...



class ClientFormsAuthenticationMembershipProvider(MembershipProvider): # skipped bases: <type 'object'>
    """ ClientFormsAuthenticationMembershipProvider() """
    @property
    def ServiceUri(self) -> str:
        """
        Get: ServiceUri(self: ClientFormsAuthenticationMembershipProvider) -> str
        Set: ServiceUri(self: ClientFormsAuthenticationMembershipProvider) = value
        """
        ...


    def Initialize(self, name:str, config:NameValueCollection): # -> 
        """ Initialize(self: ClientFormsAuthenticationMembershipProvider, name: str, config: NameValueCollection) """
        ...

    def Logout(self): # -> 
        """ Logout(self: ClientFormsAuthenticationMembershipProvider) """
        ...

    UserValidated = ...


class ClientRoleProvider(RoleProvider): # skipped bases: <type 'object'>
    """ ClientRoleProvider() """
    @property
    def ServiceUri(self) -> str:
        """
        Get: ServiceUri(self: ClientRoleProvider) -> str
        Set: ServiceUri(self: ClientRoleProvider) = value
        """
        ...


    def Initialize(self, name:str, config:NameValueCollection): # -> 
        """ Initialize(self: ClientRoleProvider, name: str, config: NameValueCollection) """
        ...

    def ResetCache(self): # -> 
        """ ResetCache(self: ClientRoleProvider) """
        ...


class ClientSettingsProvider(IApplicationSettingsProvider, SettingsProvider): # skipped bases: <type 'object'>
    """ ClientSettingsProvider() """
    @property
    def ServiceUri(self) -> str:
        """
        Get: ServiceUri() -> str
        Set: ServiceUri() = value
        """
        ...


    @staticmethod
    def GetPropertyMetadata(serviceUri:str) -> SettingsPropertyCollection:
        """ GetPropertyMetadata(serviceUri: str) -> SettingsPropertyCollection """
        ...

    def Initialize(self, name:str, config:NameValueCollection): # -> 
        """ Initialize(self: ClientSettingsProvider, name: str, config: NameValueCollection) """
        ...

    SettingsSaved = ...


class ClientWindowsAuthenticationMembershipProvider(MembershipProvider): # skipped bases: <type 'object'>
    """ ClientWindowsAuthenticationMembershipProvider() """
    def Logout(self): # -> 
        """ Logout(self: ClientWindowsAuthenticationMembershipProvider) """
        ...


class IClientFormsAuthenticationCredentialsProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetCredentials(self) -> ClientFormsAuthenticationCredentials:
        """ GetCredentials(self: IClientFormsAuthenticationCredentialsProvider) -> ClientFormsAuthenticationCredentials """
        ...


class SettingsSavedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SettingsSavedEventArgs(failedSettingsList: IEnumerable[str]) """
    @property
    def FailedSettingsList(self) -> ReadOnlyCollection:
        """ Get: FailedSettingsList(self: SettingsSavedEventArgs) -> ReadOnlyCollection[str] """
        ...


    def __new__(cls, failedSettingsList:IEnumerable) -> Self:
        """ __new__(cls: type, failedSettingsList: IEnumerable[str]) """
        ...


class UserValidatedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ UserValidatedEventArgs(username: str) """
    @property
    def UserName(self) -> str:
        """ Get: UserName(self: UserValidatedEventArgs) -> str """
        ...


    def __new__(cls, username:str) -> Self:
        """ __new__(cls: type, username: str) """
        ...


