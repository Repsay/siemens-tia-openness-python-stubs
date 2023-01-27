# encoding: utf-8
# module System.Runtime.Caching calls itself Caching
# from System.Runtime.Caching, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (AsyncCallback, DateTimeOffset, Enum, IAsyncResult, 
    IDisposable, IServiceProvider, Int64, MulticastDelegate, TimeSpan)

from System.Collections import IDictionary, IEnumerable, IList

from System.Collections.ObjectModel import Collection, ReadOnlyCollection

from System.Collections.Specialized import NameValueCollection

from System.Data.SqlClient import SqlDependency

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ChangeMonitor(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def HasChanged(self) -> bool:
        """ Get: HasChanged(self: ChangeMonitor) -> bool """
        ...

    @property
    def IsDisposed(self) -> bool:
        """ Get: IsDisposed(self: ChangeMonitor) -> bool """
        ...

    @property
    def UniqueId(self) -> str:
        """ Get: UniqueId(self: ChangeMonitor) -> str """
        ...


    def InitializationComplete(self, *args): #cannot find CLR method
        """ InitializationComplete(self: ChangeMonitor) """
        ...

    def NotifyOnChanged(self, onChangedCallback:OnChangedCallback): # -> 
        """ NotifyOnChanged(self: ChangeMonitor, onChangedCallback: OnChangedCallback) """
        ...

    def OnChanged(self, *args): #cannot find CLR method
        """ OnChanged(self: ChangeMonitor, state: object) """
        ...


class CacheEntryChangeMonitor(ChangeMonitor): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def CacheKeys(self) -> ReadOnlyCollection:
        """ Get: CacheKeys(self: CacheEntryChangeMonitor) -> ReadOnlyCollection[str] """
        ...

    @property
    def LastModified(self) -> DateTimeOffset:
        """ Get: LastModified(self: CacheEntryChangeMonitor) -> DateTimeOffset """
        ...

    @property
    def RegionName(self) -> str:
        """ Get: RegionName(self: CacheEntryChangeMonitor) -> str """
        ...



class CacheEntryRemovedArguments: # skipped bases: <type 'object'>, <type 'object'>
    """ CacheEntryRemovedArguments(source: ObjectCache, reason: CacheEntryRemovedReason, cacheItem: CacheItem) """
    @property
    def CacheItem(self) -> CacheItem:
        """ Get: CacheItem(self: CacheEntryRemovedArguments) -> CacheItem """
        ...

    @property
    def RemovedReason(self) -> CacheEntryRemovedReason:
        """ Get: RemovedReason(self: CacheEntryRemovedArguments) -> CacheEntryRemovedReason """
        ...

    @property
    def Source(self) -> ObjectCache:
        """ Get: Source(self: CacheEntryRemovedArguments) -> ObjectCache """
        ...



class CacheEntryRemovedCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CacheEntryRemovedCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, arguments:CacheEntryRemovedArguments, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: CacheEntryRemovedCallback, arguments: CacheEntryRemovedArguments, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: CacheEntryRemovedCallback, result: IAsyncResult) """
        ...

    def Invoke(self, arguments:CacheEntryRemovedArguments): # -> 
        """ Invoke(self: CacheEntryRemovedCallback, arguments: CacheEntryRemovedArguments) """
        ...


class CacheEntryRemovedReason(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CacheEntryRemovedReason, values: CacheSpecificEviction (4), ChangeMonitorChanged (3), Evicted (2), Expired (1), Removed (0) """
    CacheSpecificEviction: CacheEntryRemovedReason = ...
    ChangeMonitorChanged: CacheEntryRemovedReason = ...
    Evicted: CacheEntryRemovedReason = ...
    Expired: CacheEntryRemovedReason = ...
    Removed: CacheEntryRemovedReason = ...
    value__ = ...


class CacheEntryUpdateArguments: # skipped bases: <type 'object'>, <type 'object'>
    """ CacheEntryUpdateArguments(source: ObjectCache, reason: CacheEntryRemovedReason, key: str, regionName: str) """
    @property
    def Key(self) -> str:
        """ Get: Key(self: CacheEntryUpdateArguments) -> str """
        ...

    @property
    def RegionName(self) -> str:
        """ Get: RegionName(self: CacheEntryUpdateArguments) -> str """
        ...

    @property
    def RemovedReason(self) -> CacheEntryRemovedReason:
        """ Get: RemovedReason(self: CacheEntryUpdateArguments) -> CacheEntryRemovedReason """
        ...

    @property
    def Source(self) -> ObjectCache:
        """ Get: Source(self: CacheEntryUpdateArguments) -> ObjectCache """
        ...

    @property
    def UpdatedCacheItem(self) -> CacheItem:
        """
        Get: UpdatedCacheItem(self: CacheEntryUpdateArguments) -> CacheItem
        Set: UpdatedCacheItem(self: CacheEntryUpdateArguments) = value
        """
        ...

    @property
    def UpdatedCacheItemPolicy(self) -> CacheItemPolicy:
        """
        Get: UpdatedCacheItemPolicy(self: CacheEntryUpdateArguments) -> CacheItemPolicy
        Set: UpdatedCacheItemPolicy(self: CacheEntryUpdateArguments) = value
        """
        ...



class CacheEntryUpdateCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CacheEntryUpdateCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, arguments:CacheEntryUpdateArguments, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: CacheEntryUpdateCallback, arguments: CacheEntryUpdateArguments, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: CacheEntryUpdateCallback, result: IAsyncResult) """
        ...

    def Invoke(self, arguments:CacheEntryUpdateArguments): # -> 
        """ Invoke(self: CacheEntryUpdateCallback, arguments: CacheEntryUpdateArguments) """
        ...


class CacheItem: # skipped bases: <type 'object'>, <type 'object'>
    """
    CacheItem(key: str)
    CacheItem(key: str, value: object)
    CacheItem(key: str, value: object, regionName: str)
    """
    @property
    def Key(self) -> str:
        """
        Get: Key(self: CacheItem) -> str
        Set: Key(self: CacheItem) = value
        """
        ...

    @property
    def RegionName(self) -> str:
        """
        Get: RegionName(self: CacheItem) -> str
        Set: RegionName(self: CacheItem) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: CacheItem) -> object
        Set: Value(self: CacheItem) = value
        """
        ...



class CacheItemPolicy: # skipped bases: <type 'object'>, <type 'object'>
    """ CacheItemPolicy() """
    @property
    def AbsoluteExpiration(self) -> DateTimeOffset:
        """
        Get: AbsoluteExpiration(self: CacheItemPolicy) -> DateTimeOffset
        Set: AbsoluteExpiration(self: CacheItemPolicy) = value
        """
        ...

    @property
    def ChangeMonitors(self) -> Collection:
        """ Get: ChangeMonitors(self: CacheItemPolicy) -> Collection[ChangeMonitor] """
        ...

    @property
    def Priority(self) -> CacheItemPriority:
        """
        Get: Priority(self: CacheItemPolicy) -> CacheItemPriority
        Set: Priority(self: CacheItemPolicy) = value
        """
        ...

    @property
    def RemovedCallback(self) -> CacheEntryRemovedCallback:
        """
        Get: RemovedCallback(self: CacheItemPolicy) -> CacheEntryRemovedCallback
        Set: RemovedCallback(self: CacheItemPolicy) = value
        """
        ...

    @property
    def SlidingExpiration(self) -> TimeSpan:
        """
        Get: SlidingExpiration(self: CacheItemPolicy) -> TimeSpan
        Set: SlidingExpiration(self: CacheItemPolicy) = value
        """
        ...

    @property
    def UpdateCallback(self) -> CacheEntryUpdateCallback:
        """
        Get: UpdateCallback(self: CacheItemPolicy) -> CacheEntryUpdateCallback
        Set: UpdateCallback(self: CacheItemPolicy) = value
        """
        ...



class CacheItemPriority(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CacheItemPriority, values: Default (0), NotRemovable (1) """
    Default: CacheItemPriority = ...
    NotRemovable: CacheItemPriority = ...
    value__ = ...


class DefaultCacheCapabilities(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DefaultCacheCapabilities, values: AbsoluteExpirations (8), CacheEntryChangeMonitors (4), CacheEntryRemovedCallback (64), CacheEntryUpdateCallback (32), CacheRegions (128), InMemoryProvider (1), None (0), OutOfProcessProvider (2), SlidingExpirations (16) """
    AbsoluteExpirations: DefaultCacheCapabilities = ...
    CacheEntryChangeMonitors: DefaultCacheCapabilities = ...
    CacheEntryRemovedCallback: DefaultCacheCapabilities = ...
    CacheEntryUpdateCallback: DefaultCacheCapabilities = ...
    CacheRegions: DefaultCacheCapabilities = ...
    InMemoryProvider: DefaultCacheCapabilities = ...
    OutOfProcessProvider: DefaultCacheCapabilities = ...
    SlidingExpirations: DefaultCacheCapabilities = ...
    value__ = ...


class FileChangeMonitor(ChangeMonitor): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def FilePaths(self) -> ReadOnlyCollection:
        """ Get: FilePaths(self: FileChangeMonitor) -> ReadOnlyCollection[str] """
        ...

    @property
    def LastModified(self) -> DateTimeOffset:
        """ Get: LastModified(self: FileChangeMonitor) -> DateTimeOffset """
        ...



class HostFileChangeMonitor(FileChangeMonitor): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ HostFileChangeMonitor(filePaths: IList[str]) """
    @property
    def UniqueId(self) -> str:
        """ Get: UniqueId(self: HostFileChangeMonitor) -> str """
        ...


    def __new__(cls, filePaths:IList) -> Self:
        """ __new__(cls: type, filePaths: IList[str]) """
        ...


class ObjectCache(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def DefaultCacheCapabilities(self) -> DefaultCacheCapabilities:
        """ Get: DefaultCacheCapabilities(self: ObjectCache) -> DefaultCacheCapabilities """
        ...

    @property
    def Host(self) -> IServiceProvider:
        """
        Get: Host() -> IServiceProvider
        Set: Host() = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ObjectCache) -> str """
        ...


    def Add(self, *__args) -> bool:
        """
        Add(self: ObjectCache, key: str, value: object, absoluteExpiration: DateTimeOffset, regionName: str) -> bool
        Add(self: ObjectCache, item: CacheItem, policy: CacheItemPolicy) -> bool
        Add(self: ObjectCache, key: str, value: object, policy: CacheItemPolicy, regionName: str) -> bool
        """
        ...

    def AddOrGetExisting(self, *__args) -> object:
        """
        AddOrGetExisting(self: ObjectCache, key: str, value: object, absoluteExpiration: DateTimeOffset, regionName: str) -> object
        AddOrGetExisting(self: ObjectCache, value: CacheItem, policy: CacheItemPolicy) -> CacheItem
        AddOrGetExisting(self: ObjectCache, key: str, value: object, policy: CacheItemPolicy, regionName: str) -> object
        """
        ...

    def Contains(self, key:str, regionName:str) -> bool:
        """ Contains(self: ObjectCache, key: str, regionName: str) -> bool """
        ...

    def CreateCacheEntryChangeMonitor(self, keys:IEnumerable, regionName:str) -> CacheEntryChangeMonitor:
        """ CreateCacheEntryChangeMonitor(self: ObjectCache, keys: IEnumerable[str], regionName: str) -> CacheEntryChangeMonitor """
        ...

    def Get(self, key:str, regionName:str) -> object:
        """ Get(self: ObjectCache, key: str, regionName: str) -> object """
        ...

    def GetCacheItem(self, key:str, regionName:str) -> CacheItem:
        """ GetCacheItem(self: ObjectCache, key: str, regionName: str) -> CacheItem """
        ...

    def GetCount(self, regionName:str) -> Int64:
        """ GetCount(self: ObjectCache, regionName: str) -> Int64 """
        ...

    def GetValues(self, *__args) -> IDictionary:
        """
        GetValues(self: ObjectCache, keys: IEnumerable[str], regionName: str) -> IDictionary[str, object]
        GetValues(self: ObjectCache, regionName: str, *keys: Array[str]) -> IDictionary[str, object]
        """
        ...

    def Remove(self, key:str, regionName:str) -> object:
        """ Remove(self: ObjectCache, key: str, regionName: str) -> object """
        ...

    def Set(self, *__args): # -> 
        """ Set(self: ObjectCache, key: str, value: object, absoluteExpiration: DateTimeOffset, regionName: str)Set(self: ObjectCache, item: CacheItem, policy: CacheItemPolicy)Set(self: ObjectCache, key: str, value: object, policy: CacheItemPolicy, regionName: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[KeyValuePair[str, object]](enumerable: IEnumerable[KeyValuePair[str, object]], value: KeyValuePair[str, object]) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...

    InfiniteAbsoluteExpiration: DateTimeOffset = ...
    NoSlidingExpiration: TimeSpan = ...


class MemoryCache(ObjectCache, IDisposable): # skipped bases: <type 'IEnumerable[KeyValuePair[str, object]]'>, <type 'IEnumerable'>, <type 'object'>
    """
    MemoryCache(name: str, config: NameValueCollection)
    MemoryCache(name: str, config: NameValueCollection, ignoreConfigSection: bool)
    """
    @property
    def CacheMemoryLimit(self) -> Int64:
        """ Get: CacheMemoryLimit(self: MemoryCache) -> Int64 """
        ...

    @property
    def Default(self) -> MemoryCache:
        """ Get: Default() -> MemoryCache """
        ...

    @property
    def PhysicalMemoryLimit(self) -> Int64:
        """ Get: PhysicalMemoryLimit(self: MemoryCache) -> Int64 """
        ...

    @property
    def PollingInterval(self) -> TimeSpan:
        """ Get: PollingInterval(self: MemoryCache) -> TimeSpan """
        ...


    def GetLastSize(self, regionName:str) -> Int64:
        """ GetLastSize(self: MemoryCache, regionName: str) -> Int64 """
        ...

    def Trim(self, percent:int) -> Int64:
        """ Trim(self: MemoryCache, percent: int) -> Int64 """
        ...

    def __new__(cls, name:str, config:NameValueCollection, ignoreConfigSection:bool = ...) -> Self:
        """
        __new__(cls: type, name: str, config: NameValueCollection)
        __new__(cls: type, name: str, config: NameValueCollection, ignoreConfigSection: bool)
        """
        ...



class OnChangedCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OnChangedCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, state:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: OnChangedCallback, state: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: OnChangedCallback, result: IAsyncResult) """
        ...

    def Invoke(self, state:object): # -> 
        """ Invoke(self: OnChangedCallback, state: object) """
        ...


class SqlChangeMonitor(ChangeMonitor): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ SqlChangeMonitor(dependency: SqlDependency) """
    def __new__(cls, dependency:SqlDependency) -> Self:
        """ __new__(cls: type, dependency: SqlDependency) """
        ...


# variables with complex values

