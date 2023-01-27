# encoding: utf-8
# module System.Web.Mobile calls itself Mobile
# from System.Web.Mobile, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Type

from System.Collections.Specialized import HybridDictionary

from System.Configuration import (ConfigurationElement, 
    ConfigurationElementCollection, ConfigurationSection, 
    IConfigurationSectionHandler)

from System.Web import HttpBrowserCapabilities, IHttpModule

from typing import Self


# no functions
# classes

class CookielessData(HybridDictionary): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ CookielessData() """
    pass

class DeviceFilterElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    DeviceFilterElement(name: str, filterClass: Type, method: str)
    DeviceFilterElement(name: str, compareName: str, argument: str)
    """
    @property
    def Argument(self) -> str:
        """
        Get: Argument(self: DeviceFilterElement) -> str
        Set: Argument(self: DeviceFilterElement) = value
        """
        ...

    @property
    def Compare(self) -> str:
        """
        Get: Compare(self: DeviceFilterElement) -> str
        Set: Compare(self: DeviceFilterElement) = value
        """
        ...

    @property
    def FilterClass(self) -> Type:
        """
        Get: FilterClass(self: DeviceFilterElement) -> Type
        Set: FilterClass(self: DeviceFilterElement) = value
        """
        ...

    @property
    def Method(self) -> str:
        """
        Get: Method(self: DeviceFilterElement) -> str
        Set: Method(self: DeviceFilterElement) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DeviceFilterElement) -> str """
        ...


    def __new__(cls, name, *__args) -> Self:
        """
        __new__(cls: type, name: str, filterClass: Type, method: str)
        __new__(cls: type, name: str, compareName: str, argument: str)
        """
        ...


class DeviceFilterElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ DeviceFilterElementCollection() """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: DeviceFilterElementCollection) -> Array[object] """
        ...


    def Add(self, deviceFilter:DeviceFilterElement): # -> 
        """ Add(self: DeviceFilterElementCollection, deviceFilter: DeviceFilterElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: DeviceFilterElementCollection) """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: DeviceFilterElementCollection, name: str)Remove(self: DeviceFilterElementCollection, deviceFilter: DeviceFilterElement) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: DeviceFilterElementCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class DeviceFiltersSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ DeviceFiltersSection() """
    @property
    def Filters(self) -> DeviceFilterElementCollection:
        """ Get: Filters(self: DeviceFiltersSection) -> DeviceFilterElementCollection """
        ...



class ErrorHandlerModule(IHttpModule): # skipped bases: <type 'object'>
    """ ErrorHandlerModule() """
    pass

class MobileCapabilities(HttpBrowserCapabilities): # skipped bases: <type 'IFilterResolutionService'>, <type 'object'>
    """ MobileCapabilities() """
    def HasCapability(self, delegateName:str, optionalParameter:str) -> bool:
        """ HasCapability(self: MobileCapabilities, delegateName: str, optionalParameter: str) -> bool """
        ...

    PreferredRenderingTypeChtml10: str = ...
    PreferredRenderingTypeHtml32: str = ...
    PreferredRenderingTypeWml11: str = ...
    PreferredRenderingTypeWml12: str = ...


class MobileDeviceCapabilitiesSectionHandler(IConfigurationSectionHandler): # skipped bases: <type 'object'>
    """ MobileDeviceCapabilitiesSectionHandler() """
    pass

class MobileErrorInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: MobileErrorInfo) -> str
        Set: Description(self: MobileErrorInfo) = value
        """
        ...

    @property
    def File(self) -> str:
        """
        Get: File(self: MobileErrorInfo) -> str
        Set: File(self: MobileErrorInfo) = value
        """
        ...

    @property
    def LineNumber(self) -> str:
        """
        Get: LineNumber(self: MobileErrorInfo) -> str
        Set: LineNumber(self: MobileErrorInfo) = value
        """
        ...

    @property
    def MiscText(self) -> str:
        """
        Get: MiscText(self: MobileErrorInfo) -> str
        Set: MiscText(self: MobileErrorInfo) = value
        """
        ...

    @property
    def MiscTitle(self) -> str:
        """
        Get: MiscTitle(self: MobileErrorInfo) -> str
        Set: MiscTitle(self: MobileErrorInfo) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: MobileErrorInfo) -> str
        Set: Type(self: MobileErrorInfo) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    ContextKey: str = ...


class MobileFormsAuthentication: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def RedirectFromLoginPage(userName:str, createPersistentCookie:bool, strCookiePath:str = ...): # -> 
        """ RedirectFromLoginPage(userName: str, createPersistentCookie: bool)RedirectFromLoginPage(userName: str, createPersistentCookie: bool, strCookiePath: str) """
        ...

    @staticmethod
    def SignOut(): # -> 
        """ SignOut() """
        ...


