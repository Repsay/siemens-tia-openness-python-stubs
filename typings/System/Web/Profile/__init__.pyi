# encoding: utf-8
# module System.Web.Profile calls itself Profile
# from System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (AsyncCallback, Attribute, DateTime, Enum, EventArgs, 
    IAsyncResult, MulticastDelegate)

from System.Collections import ICollection, IEnumerator

from System.Collections.Specialized import NameValueCollection

from System.Configuration import (SettingsBase, SettingsContext, 
    SettingsPropertyCollection, SettingsPropertyValueCollection, 
    SettingsProvider, SettingsProviderCollection)

from System.Web import HttpContext, IHttpModule

from System.Web.Configuration import ProfilePropertySettings

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class CustomProviderDataAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CustomProviderDataAttribute(customProviderData: str) """
    @property
    def CustomProviderData(self) -> str:
        """ Get: CustomProviderData(self: CustomProviderDataAttribute) -> str """
        ...


    def __new__(cls, customProviderData:str) -> Self:
        """ __new__(cls: type, customProviderData: str) """
        ...


class ProfileBase(SettingsBase): # skipped bases: <type 'object'>
    """ ProfileBase() """
    @property
    def IsAnonymous(self) -> bool:
        """ Get: IsAnonymous(self: ProfileBase) -> bool """
        ...

    @property
    def IsDirty(self) -> bool:
        """ Get: IsDirty(self: ProfileBase) -> bool """
        ...

    @property
    def LastActivityDate(self) -> DateTime:
        """ Get: LastActivityDate(self: ProfileBase) -> DateTime """
        ...

    @property
    def LastUpdatedDate(self) -> DateTime:
        """ Get: LastUpdatedDate(self: ProfileBase) -> DateTime """
        ...

    @property
    def UserName(self) -> str:
        """ Get: UserName(self: ProfileBase) -> str """
        ...


    @staticmethod
    def Create(username:str, isAuthenticated:bool = ...) -> ProfileBase:
        """
        Create(username: str) -> ProfileBase
        Create(username: str, isAuthenticated: bool) -> ProfileBase
        """
        ...

    def GetProfileGroup(self, groupName:str) -> ProfileGroupBase:
        """ GetProfileGroup(self: ProfileBase, groupName: str) -> ProfileGroupBase """
        ...

    def GetPropertyValue(self, propertyName:str) -> object:
        """ GetPropertyValue(self: ProfileBase, propertyName: str) -> object """
        ...

    def SetPropertyValue(self, propertyName:str, propertyValue:object): # -> 
        """ SetPropertyValue(self: ProfileBase, propertyName: str, propertyValue: object) """
        ...

    Properties: SettingsPropertyCollection = ...


class DefaultProfile(ProfileBase): # skipped bases: <type 'object'>
    """ DefaultProfile() """
    pass

class ProfileAuthenticationOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProfileAuthenticationOption, values: All (2), Anonymous (0), Authenticated (1) """
    All: ProfileAuthenticationOption = ...
    Anonymous: ProfileAuthenticationOption = ...
    Authenticated: ProfileAuthenticationOption = ...
    value__ = ...


class ProfileAutoSaveEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ProfileAutoSaveEventArgs(context: HttpContext) """
    @property
    def Context(self) -> HttpContext:
        """ Get: Context(self: ProfileAutoSaveEventArgs) -> HttpContext """
        ...

    @property
    def ContinueWithProfileAutoSave(self) -> bool:
        """
        Get: ContinueWithProfileAutoSave(self: ProfileAutoSaveEventArgs) -> bool
        Set: ContinueWithProfileAutoSave(self: ProfileAutoSaveEventArgs) = value
        """
        ...


    def __new__(cls, context:HttpContext) -> Self:
        """ __new__(cls: type, context: HttpContext) """
        ...


class ProfileAutoSaveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ProfileAutoSaveEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ProfileAutoSaveEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ProfileAutoSaveEventHandler, sender: object, e: ProfileAutoSaveEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ProfileAutoSaveEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ProfileAutoSaveEventArgs): # -> 
        """ Invoke(self: ProfileAutoSaveEventHandler, sender: object, e: ProfileAutoSaveEventArgs) """
        ...


class ProfileEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ProfileEventArgs(context: HttpContext) """
    @property
    def Context(self) -> HttpContext:
        """ Get: Context(self: ProfileEventArgs) -> HttpContext """
        ...

    @property
    def Profile(self) -> ProfileBase:
        """
        Get: Profile(self: ProfileEventArgs) -> ProfileBase
        Set: Profile(self: ProfileEventArgs) = value
        """
        ...


    def __new__(cls, context:HttpContext) -> Self:
        """ __new__(cls: type, context: HttpContext) """
        ...


class ProfileEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ProfileEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ProfileEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ProfileEventHandler, sender: object, e: ProfileEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ProfileEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ProfileEventArgs): # -> 
        """ Invoke(self: ProfileEventHandler, sender: object, e: ProfileEventArgs) """
        ...


class ProfileGroupBase: # skipped bases: <type 'object'>, <type 'object'>
    """ ProfileGroupBase() """
    def GetPropertyValue(self, propertyName:str) -> object:
        """ GetPropertyValue(self: ProfileGroupBase, propertyName: str) -> object """
        ...

    def Init(self, parent:ProfileBase, myName:str): # -> 
        """ Init(self: ProfileGroupBase, parent: ProfileBase, myName: str) """
        ...

    def SetPropertyValue(self, propertyName:str, propertyValue:object): # -> 
        """ SetPropertyValue(self: ProfileGroupBase, propertyName: str, propertyValue: object) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ProfileInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ ProfileInfo(username: str, isAnonymous: bool, lastActivityDate: DateTime, lastUpdatedDate: DateTime, size: int) """
    @property
    def IsAnonymous(self) -> bool:
        """ Get: IsAnonymous(self: ProfileInfo) -> bool """
        ...

    @property
    def LastActivityDate(self) -> DateTime:
        """ Get: LastActivityDate(self: ProfileInfo) -> DateTime """
        ...

    @property
    def LastUpdatedDate(self) -> DateTime:
        """ Get: LastUpdatedDate(self: ProfileInfo) -> DateTime """
        ...

    @property
    def Size(self) -> int:
        """ Get: Size(self: ProfileInfo) -> int """
        ...

    @property
    def UserName(self) -> str:
        """ Get: UserName(self: ProfileInfo) -> str """
        ...



class ProfileInfoCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ ProfileInfoCollection() """
    def Add(self, profileInfo:ProfileInfo): # -> 
        """ Add(self: ProfileInfoCollection, profileInfo: ProfileInfo) """
        ...

    def Clear(self): # -> 
        """ Clear(self: ProfileInfoCollection) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ProfileInfoCollection) -> IEnumerator """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: ProfileInfoCollection, name: str) """
        ...

    def SetReadOnly(self): # -> 
        """ SetReadOnly(self: ProfileInfoCollection) """
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


class ProfileManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName() -> str
        Set: ApplicationName() = value
        """
        ...

    @property
    def AutomaticSaveEnabled(self) -> bool:
        """ Get: AutomaticSaveEnabled() -> bool """
        ...

    @property
    def Enabled(self) -> bool:
        """ Get: Enabled() -> bool """
        ...

    @property
    def Provider(self) -> ProfileProvider:
        """ Get: Provider() -> ProfileProvider """
        ...

    @property
    def Providers(self) -> ProfileProviderCollection:
        """ Get: Providers() -> ProfileProviderCollection """
        ...


    @staticmethod
    def AddDynamicProfileProperty(property:ProfilePropertySettings): # -> 
        """ AddDynamicProfileProperty(property: ProfilePropertySettings) """
        ...

    @staticmethod
    def DeleteInactiveProfiles(authenticationOption:ProfileAuthenticationOption, userInactiveSinceDate:DateTime) -> int:
        """ DeleteInactiveProfiles(authenticationOption: ProfileAuthenticationOption, userInactiveSinceDate: DateTime) -> int """
        ...

    @staticmethod
    def DeleteProfile(username:str) -> bool:
        """ DeleteProfile(username: str) -> bool """
        ...

    @staticmethod
    def DeleteProfiles(*__args:ProfileInfoCollection) -> int:
        """
        DeleteProfiles(profiles: ProfileInfoCollection) -> int
        DeleteProfiles(usernames: Array[str]) -> int
        """
        ...

    @staticmethod
    def FindInactiveProfilesByUserName(authenticationOption, usernameToMatch, userInactiveSinceDate, pageIndex=None, pageSize=None, totalRecords=None) -> ProfileInfoCollection:
        """
        FindInactiveProfilesByUserName(authenticationOption: ProfileAuthenticationOption, usernameToMatch: str, userInactiveSinceDate: DateTime) -> ProfileInfoCollection
        FindInactiveProfilesByUserName(authenticationOption: ProfileAuthenticationOption, usernameToMatch: str, userInactiveSinceDate: DateTime, pageIndex: int, pageSize: int) -> (ProfileInfoCollection, int)
        """
        ...

    @staticmethod
    def FindProfilesByUserName(authenticationOption, usernameToMatch, pageIndex=None, pageSize=None, totalRecords=None) -> ProfileInfoCollection:
        """
        FindProfilesByUserName(authenticationOption: ProfileAuthenticationOption, usernameToMatch: str) -> ProfileInfoCollection
        FindProfilesByUserName(authenticationOption: ProfileAuthenticationOption, usernameToMatch: str, pageIndex: int, pageSize: int) -> (ProfileInfoCollection, int)
        """
        ...

    @staticmethod
    def GetAllInactiveProfiles(authenticationOption, userInactiveSinceDate, pageIndex=None, pageSize=None, totalRecords=None) -> ProfileInfoCollection:
        """
        GetAllInactiveProfiles(authenticationOption: ProfileAuthenticationOption, userInactiveSinceDate: DateTime) -> ProfileInfoCollection
        GetAllInactiveProfiles(authenticationOption: ProfileAuthenticationOption, userInactiveSinceDate: DateTime, pageIndex: int, pageSize: int) -> (ProfileInfoCollection, int)
        """
        ...

    @staticmethod
    def GetAllProfiles(authenticationOption, pageIndex=None, pageSize=None, totalRecords=None) -> ProfileInfoCollection:
        """
        GetAllProfiles(authenticationOption: ProfileAuthenticationOption) -> ProfileInfoCollection
        GetAllProfiles(authenticationOption: ProfileAuthenticationOption, pageIndex: int, pageSize: int) -> (ProfileInfoCollection, int)
        """
        ...

    @staticmethod
    def GetNumberOfInactiveProfiles(authenticationOption:ProfileAuthenticationOption, userInactiveSinceDate:DateTime) -> int:
        """ GetNumberOfInactiveProfiles(authenticationOption: ProfileAuthenticationOption, userInactiveSinceDate: DateTime) -> int """
        ...

    @staticmethod
    def GetNumberOfProfiles(authenticationOption:ProfileAuthenticationOption) -> int:
        """ GetNumberOfProfiles(authenticationOption: ProfileAuthenticationOption) -> int """
        ...

    __all__: list = ...


class ProfileMigrateEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ProfileMigrateEventArgs(context: HttpContext, anonymousId: str) """
    @property
    def AnonymousID(self) -> str:
        """ Get: AnonymousID(self: ProfileMigrateEventArgs) -> str """
        ...

    @property
    def Context(self) -> HttpContext:
        """ Get: Context(self: ProfileMigrateEventArgs) -> HttpContext """
        ...


    def __new__(cls, context:HttpContext, anonymousId:str) -> Self:
        """ __new__(cls: type, context: HttpContext, anonymousId: str) """
        ...


class ProfileMigrateEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ProfileMigrateEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ProfileMigrateEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ProfileMigrateEventHandler, sender: object, e: ProfileMigrateEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ProfileMigrateEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ProfileMigrateEventArgs): # -> 
        """ Invoke(self: ProfileMigrateEventHandler, sender: object, e: ProfileMigrateEventArgs) """
        ...


class ProfileModule(IHttpModule): # skipped bases: <type 'object'>
    """ ProfileModule() """
    MigrateAnonymous = ...
    Personalize = ...
    ProfileAutoSaving = ...


class ProfileProvider(SettingsProvider): # skipped bases: <type 'object'>
    """ no doc """
    def DeleteInactiveProfiles(self, authenticationOption:ProfileAuthenticationOption, userInactiveSinceDate:DateTime) -> int:
        """ DeleteInactiveProfiles(self: ProfileProvider, authenticationOption: ProfileAuthenticationOption, userInactiveSinceDate: DateTime) -> int """
        ...

    def DeleteProfiles(self, *__args:ProfileInfoCollection) -> int:
        """
        DeleteProfiles(self: ProfileProvider, profiles: ProfileInfoCollection) -> int
        DeleteProfiles(self: ProfileProvider, usernames: Array[str]) -> int
        """
        ...

    def FindInactiveProfilesByUserName(self, authenticationOption, usernameToMatch, userInactiveSinceDate, pageIndex, pageSize, totalRecords) -> Tuple_[ProfileInfoCollection, int]:
        """ FindInactiveProfilesByUserName(self: ProfileProvider, authenticationOption: ProfileAuthenticationOption, usernameToMatch: str, userInactiveSinceDate: DateTime, pageIndex: int, pageSize: int) -> (ProfileInfoCollection, int) """
        ...

    def FindProfilesByUserName(self, authenticationOption, usernameToMatch, pageIndex, pageSize, totalRecords) -> Tuple_[ProfileInfoCollection, int]:
        """ FindProfilesByUserName(self: ProfileProvider, authenticationOption: ProfileAuthenticationOption, usernameToMatch: str, pageIndex: int, pageSize: int) -> (ProfileInfoCollection, int) """
        ...

    def GetAllInactiveProfiles(self, authenticationOption, userInactiveSinceDate, pageIndex, pageSize, totalRecords) -> Tuple_[ProfileInfoCollection, int]:
        """ GetAllInactiveProfiles(self: ProfileProvider, authenticationOption: ProfileAuthenticationOption, userInactiveSinceDate: DateTime, pageIndex: int, pageSize: int) -> (ProfileInfoCollection, int) """
        ...

    def GetAllProfiles(self, authenticationOption, pageIndex, pageSize, totalRecords) -> Tuple_[ProfileInfoCollection, int]:
        """ GetAllProfiles(self: ProfileProvider, authenticationOption: ProfileAuthenticationOption, pageIndex: int, pageSize: int) -> (ProfileInfoCollection, int) """
        ...

    def GetNumberOfInactiveProfiles(self, authenticationOption:ProfileAuthenticationOption, userInactiveSinceDate:DateTime) -> int:
        """ GetNumberOfInactiveProfiles(self: ProfileProvider, authenticationOption: ProfileAuthenticationOption, userInactiveSinceDate: DateTime) -> int """
        ...


class ProfileProviderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ProfileProviderAttribute(providerName: str) """
    @property
    def ProviderName(self) -> str:
        """ Get: ProviderName(self: ProfileProviderAttribute) -> str """
        ...


    def __new__(cls, providerName:str) -> Self:
        """ __new__(cls: type, providerName: str) """
        ...


class ProfileProviderCollection(SettingsProviderCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ProfileProviderCollection() """
    pass

class SettingsAllowAnonymousAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SettingsAllowAnonymousAttribute(allow: bool) """
    @property
    def Allow(self) -> bool:
        """ Get: Allow(self: SettingsAllowAnonymousAttribute) -> bool """
        ...


    def __new__(cls, allow:bool) -> Self:
        """ __new__(cls: type, allow: bool) """
        ...


class SqlProfileProvider(ProfileProvider): # skipped bases: <type 'object'>
    """ SqlProfileProvider() """
    @property
    def ApplicationName(self) -> str:
        """
        Get: ApplicationName(self: SqlProfileProvider) -> str
        Set: ApplicationName(self: SqlProfileProvider) = value
        """
        ...


    def GetPropertyValues(self, sc:SettingsContext, properties:SettingsPropertyCollection) -> SettingsPropertyValueCollection:
        """ GetPropertyValues(self: SqlProfileProvider, sc: SettingsContext, properties: SettingsPropertyCollection) -> SettingsPropertyValueCollection """
        ...

    def Initialize(self, name:str, config:NameValueCollection): # -> 
        """ Initialize(self: SqlProfileProvider, name: str, config: NameValueCollection) """
        ...

    def SetPropertyValues(self, sc:SettingsContext, properties:SettingsPropertyValueCollection): # -> 
        """ SetPropertyValues(self: SqlProfileProvider, sc: SettingsContext, properties: SettingsPropertyValueCollection) """
        ...


