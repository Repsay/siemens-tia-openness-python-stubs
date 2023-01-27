# encoding: utf-8
# module System.Web.Caching calls itself Caching
# from System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Action, Array, AsyncCallback, DateTime, Enum, 
    IAsyncResult, IDisposable, Int64, MulticastDelegate, SystemException, 
    TimeSpan)

from System.Collections import ArrayList, IDictionaryEnumerator, IEnumerable

from System.Collections.Generic import List

from System.Configuration.Provider import ProviderBase, ProviderCollection

from System.IO import Stream

from System.Threading.Tasks import Task

from System.Web import HttpResponse, HttpResponseSubstitutionCallback

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class CacheDependency(IDisposable): # skipped bases: <type 'object'>
    """
    CacheDependency(filename: str)
    CacheDependency(filename: str, start: DateTime)
    CacheDependency(filenames: Array[str])
    CacheDependency(filenames: Array[str], start: DateTime)
    CacheDependency(filenames: Array[str], cachekeys: Array[str])
    CacheDependency(filenames: Array[str], cachekeys: Array[str], start: DateTime)
    CacheDependency(filenames: Array[str], cachekeys: Array[str], dependency: CacheDependency)
    CacheDependency(filenames: Array[str], cachekeys: Array[str], dependency: CacheDependency, start: DateTime)
    """
    @property
    def HasChanged(self) -> bool:
        """ Get: HasChanged(self: CacheDependency) -> bool """
        ...

    @property
    def UtcLastModified(self) -> DateTime:
        """ Get: UtcLastModified(self: CacheDependency) -> DateTime """
        ...


    def DependencyDispose(self, *args): #cannot find CLR method
        """ DependencyDispose(self: CacheDependency) """
        ...

    def FinishInit(self, *args): #cannot find CLR method
        """ FinishInit(self: CacheDependency) """
        ...

    def GetFileDependencies(self) -> Array:
        """ GetFileDependencies(self: CacheDependency) -> Array[str] """
        ...

    def GetUniqueID(self) -> str:
        """ GetUniqueID(self: CacheDependency) -> str """
        ...

    def ItemRemoved(self): # -> 
        """ ItemRemoved(self: CacheDependency) """
        ...

    def KeepDependenciesAlive(self): # -> 
        """ KeepDependenciesAlive(self: CacheDependency) """
        ...

    def NotifyDependencyChanged(self, *args): #cannot find CLR method
        """ NotifyDependencyChanged(self: CacheDependency, sender: object, e: EventArgs) """
        ...

    def SetCacheDependencyChanged(self, dependencyChangedAction:Action): # -> 
        """ SetCacheDependencyChanged(self: CacheDependency, dependencyChangedAction: Action[object, EventArgs]) """
        ...

    def SetUtcLastModified(self, *args): #cannot find CLR method
        """ SetUtcLastModified(self: CacheDependency, utcLastModified: DateTime) """
        ...

    def TakeOwnership(self) -> bool:
        """ TakeOwnership(self: CacheDependency) -> bool """
        ...


class AggregateCacheDependency(CacheDependency): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ AggregateCacheDependency() """
    def Add(self, dependencies:Array): # -> 
        """ Add(self: AggregateCacheDependency, *dependencies: Array[CacheDependency]) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class Cache(IEnumerable): # skipped bases: <type 'object'>
    """ Cache() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: Cache) -> int """
        ...

    @property
    def EffectivePercentagePhysicalMemoryLimit(self) -> Int64:
        """ Get: EffectivePercentagePhysicalMemoryLimit(self: Cache) -> Int64 """
        ...

    @property
    def EffectivePrivateBytesLimit(self) -> Int64:
        """ Get: EffectivePrivateBytesLimit(self: Cache) -> Int64 """
        ...


    def Add(self, key:str, value:object, dependencies:CacheDependency, absoluteExpiration:DateTime, slidingExpiration:TimeSpan, priority:CacheItemPriority, onRemoveCallback:CacheItemRemovedCallback) -> object:
        """ Add(self: Cache, key: str, value: object, dependencies: CacheDependency, absoluteExpiration: DateTime, slidingExpiration: TimeSpan, priority: CacheItemPriority, onRemoveCallback: CacheItemRemovedCallback) -> object """
        ...

    def Get(self, key:str) -> object:
        """ Get(self: Cache, key: str) -> object """
        ...

    def Insert(self, key:str, value:object, dependencies:CacheDependency = ..., absoluteExpiration:DateTime = ..., slidingExpiration:TimeSpan = ..., *__args:CacheItemUpdateCallback): # -> 
        """ Insert(self: Cache, key: str, value: object)Insert(self: Cache, key: str, value: object, dependencies: CacheDependency)Insert(self: Cache, key: str, value: object, dependencies: CacheDependency, absoluteExpiration: DateTime, slidingExpiration: TimeSpan)Insert(self: Cache, key: str, value: object, dependencies: CacheDependency, absoluteExpiration: DateTime, slidingExpiration: TimeSpan, onUpdateCallback: CacheItemUpdateCallback)Insert(self: Cache, key: str, value: object, dependencies: CacheDependency, absoluteExpiration: DateTime, slidingExpiration: TimeSpan, priority: CacheItemPriority, onRemoveCallback: CacheItemRemovedCallback) """
        ...

    def Remove(self, key:str) -> object:
        """ Remove(self: Cache, key: str) -> object """
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

    NoAbsoluteExpiration: DateTime = ...
    NoSlidingExpiration: TimeSpan = ...


class CacheInsertOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ CacheInsertOptions() """
    @property
    def AbsoluteExpiration(self) -> DateTime:
        """
        Get: AbsoluteExpiration(self: CacheInsertOptions) -> DateTime
        Set: AbsoluteExpiration(self: CacheInsertOptions) = value
        """
        ...

    @property
    def Dependencies(self) -> CacheDependency:
        """
        Get: Dependencies(self: CacheInsertOptions) -> CacheDependency
        Set: Dependencies(self: CacheInsertOptions) = value
        """
        ...

    @property
    def OnRemovedCallback(self) -> CacheItemRemovedCallback:
        """
        Get: OnRemovedCallback(self: CacheInsertOptions) -> CacheItemRemovedCallback
        Set: OnRemovedCallback(self: CacheInsertOptions) = value
        """
        ...

    @property
    def Priority(self) -> CacheItemPriority:
        """
        Get: Priority(self: CacheInsertOptions) -> CacheItemPriority
        Set: Priority(self: CacheInsertOptions) = value
        """
        ...

    @property
    def SlidingExpiration(self) -> TimeSpan:
        """
        Get: SlidingExpiration(self: CacheInsertOptions) -> TimeSpan
        Set: SlidingExpiration(self: CacheInsertOptions) = value
        """
        ...



class CacheItemPriority(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CacheItemPriority, values: AboveNormal (4), BelowNormal (2), Default (3), High (5), Low (1), Normal (3), NotRemovable (6) """
    AboveNormal: CacheItemPriority = ...
    BelowNormal: CacheItemPriority = ...
    Default: CacheItemPriority = ...
    High: CacheItemPriority = ...
    Low: CacheItemPriority = ...
    Normal: CacheItemPriority = ...
    NotRemovable: CacheItemPriority = ...
    value__ = ...


class CacheItemRemovedCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CacheItemRemovedCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, key:str, value:object, reason:CacheItemRemovedReason, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: CacheItemRemovedCallback, key: str, value: object, reason: CacheItemRemovedReason, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: CacheItemRemovedCallback, result: IAsyncResult) """
        ...

    def Invoke(self, key:str, value:object, reason:CacheItemRemovedReason): # -> 
        """ Invoke(self: CacheItemRemovedCallback, key: str, value: object, reason: CacheItemRemovedReason) """
        ...


class CacheItemRemovedReason(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CacheItemRemovedReason, values: DependencyChanged (4), Expired (2), Removed (1), Underused (3) """
    DependencyChanged: CacheItemRemovedReason = ...
    Expired: CacheItemRemovedReason = ...
    Removed: CacheItemRemovedReason = ...
    Underused: CacheItemRemovedReason = ...
    value__ = ...


class CacheItemUpdateCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CacheItemUpdateCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, key, reason, expensiveObject, dependency, absoluteExpiration, slidingExpiration, callback, object) -> Tuple_[IAsyncResult, object, CacheDependency, DateTime, TimeSpan]:
        """ BeginInvoke(self: CacheItemUpdateCallback, key: str, reason: CacheItemUpdateReason, callback: AsyncCallback, object: object) -> (IAsyncResult, object, CacheDependency, DateTime, TimeSpan) """
        ...

    def EndInvoke(self, expensiveObject, dependency, absoluteExpiration, slidingExpiration, result) -> Tuple_[object, CacheDependency, DateTime, TimeSpan]:
        """ EndInvoke(self: CacheItemUpdateCallback, result: IAsyncResult) -> (object, CacheDependency, DateTime, TimeSpan) """
        ...

    def Invoke(self, key, reason, expensiveObject, dependency, absoluteExpiration, slidingExpiration) -> Tuple_[object, CacheDependency, DateTime, TimeSpan]:
        """ Invoke(self: CacheItemUpdateCallback, key: str, reason: CacheItemUpdateReason) -> (object, CacheDependency, DateTime, TimeSpan) """
        ...


class CacheItemUpdateReason(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CacheItemUpdateReason, values: DependencyChanged (2), Expired (1) """
    DependencyChanged: CacheItemUpdateReason = ...
    Expired: CacheItemUpdateReason = ...
    value__ = ...


class CacheStoreProvider(IDisposable, ProviderBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ItemCount(self) -> Int64:
        """ Get: ItemCount(self: CacheStoreProvider) -> Int64 """
        ...

    @property
    def SizeInBytes(self) -> Int64:
        """ Get: SizeInBytes(self: CacheStoreProvider) -> Int64 """
        ...


    def Add(self, key:str, item:object, options:CacheInsertOptions) -> object:
        """ Add(self: CacheStoreProvider, key: str, item: object, options: CacheInsertOptions) -> object """
        ...

    def AddDependent(self, key, dependency, utcLastUpdated) -> Tuple_[bool, DateTime]:
        """ AddDependent(self: CacheStoreProvider, key: str, dependency: CacheDependency) -> (bool, DateTime) """
        ...

    def Get(self, key:str) -> object:
        """ Get(self: CacheStoreProvider, key: str) -> object """
        ...

    def GetEnumerator(self) -> IDictionaryEnumerator:
        """ GetEnumerator(self: CacheStoreProvider) -> IDictionaryEnumerator """
        ...

    def Insert(self, key:str, item:object, options:CacheInsertOptions): # -> 
        """ Insert(self: CacheStoreProvider, key: str, item: object, options: CacheInsertOptions) """
        ...

    def Remove(self, key:str, reason:CacheItemRemovedReason = ...) -> object:
        """
        Remove(self: CacheStoreProvider, key: str, reason: CacheItemRemovedReason) -> object
        Remove(self: CacheStoreProvider, key: str) -> object
        """
        ...

    def RemoveDependent(self, key:str, dependency:CacheDependency): # -> 
        """ RemoveDependent(self: CacheStoreProvider, key: str, dependency: CacheDependency) """
        ...

    def Trim(self, percent:int) -> Int64:
        """ Trim(self: CacheStoreProvider, percent: int) -> Int64 """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class DatabaseNotEnabledForNotificationException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    DatabaseNotEnabledForNotificationException()
    DatabaseNotEnabledForNotificationException(message: str)
    DatabaseNotEnabledForNotificationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ResponseElement: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class FileResponseElement(ResponseElement): # skipped bases: <type 'object'>
    """ FileResponseElement(path: str, offset: Int64, length: Int64) """
    @property
    def Length(self) -> Int64:
        """ Get: Length(self: FileResponseElement) -> Int64 """
        ...

    @property
    def Offset(self) -> Int64:
        """ Get: Offset(self: FileResponseElement) -> Int64 """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: FileResponseElement) -> str """
        ...


    def __new__(cls, path:str, offset:Int64, length:Int64) -> Self:
        """ __new__(cls: type, path: str, offset: Int64, length: Int64) """
        ...


class HeaderElement: # skipped bases: <type 'object'>, <type 'object'>
    """ HeaderElement(name: str, value: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: HeaderElement) -> str """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: HeaderElement) -> str """
        ...



class IOutputCacheEntry: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def HeaderElements(self) -> List:
        """
        Get: HeaderElements(self: IOutputCacheEntry) -> List[HeaderElement]
        Set: HeaderElements(self: IOutputCacheEntry) = value
        """
        ...

    @property
    def ResponseElements(self) -> List:
        """
        Get: ResponseElements(self: IOutputCacheEntry) -> List[ResponseElement]
        Set: ResponseElements(self: IOutputCacheEntry) = value
        """
        ...



class MemoryResponseElement(ResponseElement): # skipped bases: <type 'object'>
    """ MemoryResponseElement(buffer: Array[Byte], length: Int64) """
    @property
    def Buffer(self) -> Array:
        """ Get: Buffer(self: MemoryResponseElement) -> Array[Byte] """
        ...

    @property
    def Length(self) -> Int64:
        """ Get: Length(self: MemoryResponseElement) -> Int64 """
        ...


    def __new__(cls, buffer:Array, length:Int64) -> Self:
        """ __new__(cls: type, buffer: Array[Byte], length: Int64) """
        ...


class OutputCache: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DefaultProviderName(self) -> str:
        """ Get: DefaultProviderName() -> str """
        ...

    @property
    def Providers(self) -> OutputCacheProviderCollection:
        """ Get: Providers() -> OutputCacheProviderCollection """
        ...


    @staticmethod
    def Deserialize(stream:Stream) -> object:
        """ Deserialize(stream: Stream) -> object """
        ...

    @staticmethod
    def Serialize(stream:Stream, data:object): # -> 
        """ Serialize(stream: Stream, data: object) """
        ...

    __all__: list = ...


class OutputCacheProvider(ProviderBase): # skipped bases: <type 'object'>
    """ no doc """
    def Add(self, key:str, entry:object, utcExpiry:DateTime) -> object:
        """ Add(self: OutputCacheProvider, key: str, entry: object, utcExpiry: DateTime) -> object """
        ...

    def Get(self, key:str) -> object:
        """ Get(self: OutputCacheProvider, key: str) -> object """
        ...

    def Remove(self, key:str): # -> 
        """ Remove(self: OutputCacheProvider, key: str) """
        ...

    def Set(self, key:str, entry:object, utcExpiry:DateTime): # -> 
        """ Set(self: OutputCacheProvider, key: str, entry: object, utcExpiry: DateTime) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class OutputCacheProviderAsync(OutputCacheProvider): # skipped bases: <type 'object'>
    """ no doc """
    def AddAsync(self, key:str, entry:object, utcExpiry:DateTime) -> Task:
        """ AddAsync(self: OutputCacheProviderAsync, key: str, entry: object, utcExpiry: DateTime) -> Task[object] """
        ...

    def GetAsync(self, key:str) -> Task:
        """ GetAsync(self: OutputCacheProviderAsync, key: str) -> Task[object] """
        ...

    def RemoveAsync(self, key:str) -> Task:
        """ RemoveAsync(self: OutputCacheProviderAsync, key: str) -> Task """
        ...

    def SetAsync(self, key:str, entry:object, utcExpiry:DateTime) -> Task:
        """ SetAsync(self: OutputCacheProviderAsync, key: str, entry: object, utcExpiry: DateTime) -> Task """
        ...


class OutputCacheProviderCollection(ProviderCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ OutputCacheProviderCollection() """
    pass

class OutputCacheUtility: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateCacheDependency(response:HttpResponse) -> CacheDependency:
        """ CreateCacheDependency(response: HttpResponse) -> CacheDependency """
        ...

    @staticmethod
    def FlushKernelCache(cacheKey:str): # -> 
        """ FlushKernelCache(cacheKey: str) """
        ...

    @staticmethod
    def GetContentBuffers(response:HttpResponse) -> ArrayList:
        """ GetContentBuffers(response: HttpResponse) -> ArrayList """
        ...

    @staticmethod
    def GetValidationCallbacks(response:HttpResponse) -> IEnumerable:
        """ GetValidationCallbacks(response: HttpResponse) -> IEnumerable[KeyValuePair[HttpCacheValidateHandler, object]] """
        ...

    @staticmethod
    def SetContentBuffers(response:HttpResponse, buffers:ArrayList): # -> 
        """ SetContentBuffers(response: HttpResponse, buffers: ArrayList) """
        ...

    @staticmethod
    def SetupKernelCaching(originalCacheUrl:str, response:HttpResponse) -> str:
        """ SetupKernelCaching(originalCacheUrl: str, response: HttpResponse) -> str """
        ...

    __all__: list = ...


class SqlCacheDependency(CacheDependency): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    SqlCacheDependency(databaseEntryName: str, tableName: str)
    SqlCacheDependency(sqlCmd: SqlCommand)
    """
    @staticmethod
    def CreateOutputCacheDependency(dependency:str) -> CacheDependency:
        """ CreateOutputCacheDependency(dependency: str) -> CacheDependency """
        ...


class SqlCacheDependencyAdmin: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def DisableNotifications(connectionString:str): # -> 
        """ DisableNotifications(connectionString: str) """
        ...

    @staticmethod
    def DisableTableForNotifications(connectionString:str, *__args:str): # -> 
        """ DisableTableForNotifications(connectionString: str, table: str)DisableTableForNotifications(connectionString: str, tables: Array[str]) """
        ...

    @staticmethod
    def EnableNotifications(connectionString:str): # -> 
        """ EnableNotifications(connectionString: str) """
        ...

    @staticmethod
    def EnableTableForNotifications(connectionString:str, *__args:str): # -> 
        """ EnableTableForNotifications(connectionString: str, table: str)EnableTableForNotifications(connectionString: str, tables: Array[str]) """
        ...

    @staticmethod
    def GetTablesEnabledForNotifications(connectionString:str) -> Array:
        """ GetTablesEnabledForNotifications(connectionString: str) -> Array[str] """
        ...

    __all__: list = ...


class SubstitutionResponseElement(ResponseElement): # skipped bases: <type 'object'>
    """ SubstitutionResponseElement(callback: HttpResponseSubstitutionCallback) """
    @property
    def Callback(self) -> HttpResponseSubstitutionCallback:
        """ Get: Callback(self: SubstitutionResponseElement) -> HttpResponseSubstitutionCallback """
        ...


    def __new__(cls, callback:HttpResponseSubstitutionCallback) -> Self:
        """ __new__(cls: type, callback: HttpResponseSubstitutionCallback) """
        ...


class TableNotEnabledForNotificationException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TableNotEnabledForNotificationException()
    TableNotEnabledForNotificationException(message: str)
    TableNotEnabledForNotificationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


