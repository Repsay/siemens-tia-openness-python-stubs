# encoding: utf-8
# module System.Runtime.Caching.Hosting calls itself Hosting
# from System.Runtime.Caching, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import DateTimeOffset, Int64

from System.Runtime.Caching import MemoryCache, OnChangedCallback

from typing import Tuple as Tuple_


# no functions
# classes

class IApplicationIdentifier: # skipped bases: <type 'object'>
    """ no doc """
    def GetApplicationId(self) -> str:
        """ GetApplicationId(self: IApplicationIdentifier) -> str """
        ...


class IFileChangeNotificationSystem: # skipped bases: <type 'object'>
    """ no doc """
    def StartMonitoring(self, filePath, onChangedCallback, state, lastWriteTime, fileSize) -> Tuple_[object, DateTimeOffset, Int64]:
        """ StartMonitoring(self: IFileChangeNotificationSystem, filePath: str, onChangedCallback: OnChangedCallback) -> (object, DateTimeOffset, Int64) """
        ...

    def StopMonitoring(self, filePath:str, state:object): # -> 
        """ StopMonitoring(self: IFileChangeNotificationSystem, filePath: str, state: object) """
        ...


class IMemoryCacheManager: # skipped bases: <type 'object'>
    """ no doc """
    def ReleaseCache(self, cache:MemoryCache): # -> 
        """ ReleaseCache(self: IMemoryCacheManager, cache: MemoryCache) """
        ...

    def UpdateCacheSize(self, size:Int64, cache:MemoryCache): # -> 
        """ UpdateCacheSize(self: IMemoryCacheManager, size: Int64, cache: MemoryCache) """
        ...


