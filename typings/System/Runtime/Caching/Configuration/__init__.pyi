# encoding: utf-8
# module System.Runtime.Caching.Configuration calls itself Configuration
# from System.Runtime.Caching, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import TimeSpan

from System.Configuration import (ConfigurationElement, 
    ConfigurationElementCollection, ConfigurationSection, 
    ConfigurationSectionGroup)

from typing import Self


# no functions
# classes

class CachingSectionGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ CachingSectionGroup() """
    @property
    def MemoryCaches(self) -> MemoryCacheSection:
        """ Get: MemoryCaches(self: CachingSectionGroup) -> MemoryCacheSection """
        ...



class MemoryCacheElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ MemoryCacheElement(name: str) """
    @property
    def CacheMemoryLimitMegabytes(self) -> int:
        """
        Get: CacheMemoryLimitMegabytes(self: MemoryCacheElement) -> int
        Set: CacheMemoryLimitMegabytes(self: MemoryCacheElement) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: MemoryCacheElement) -> str
        Set: Name(self: MemoryCacheElement) = value
        """
        ...

    @property
    def PhysicalMemoryLimitPercentage(self) -> int:
        """
        Get: PhysicalMemoryLimitPercentage(self: MemoryCacheElement) -> int
        Set: PhysicalMemoryLimitPercentage(self: MemoryCacheElement) = value
        """
        ...

    @property
    def PollingInterval(self) -> TimeSpan:
        """
        Get: PollingInterval(self: MemoryCacheElement) -> TimeSpan
        Set: PollingInterval(self: MemoryCacheElement) = value
        """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class MemoryCacheSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ MemoryCacheSection() """
    @property
    def NamedCaches(self) -> MemoryCacheSettingsCollection:
        """ Get: NamedCaches(self: MemoryCacheSection) -> MemoryCacheSettingsCollection """
        ...



class MemoryCacheSettingsCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ MemoryCacheSettingsCollection() """
    def Add(self, cache:MemoryCacheElement): # -> 
        """ Add(self: MemoryCacheSettingsCollection, cache: MemoryCacheElement) """
        ...

    def Clear(self): # -> 
        """ Clear(self: MemoryCacheSettingsCollection) """
        ...

    def IndexOf(self, cache:MemoryCacheElement) -> int:
        """ IndexOf(self: MemoryCacheSettingsCollection, cache: MemoryCacheElement) -> int """
        ...

    def Remove(self, cache:MemoryCacheElement): # -> 
        """ Remove(self: MemoryCacheSettingsCollection, cache: MemoryCacheElement) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: MemoryCacheSettingsCollection, index: int) """
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


