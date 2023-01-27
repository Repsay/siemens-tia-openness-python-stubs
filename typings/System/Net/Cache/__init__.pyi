# encoding: utf-8
# module System.Net.Cache calls itself Cache
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import DateTime, Enum, TimeSpan

"""The following names are not found in the module: field#
"""

# no functions
# classes

class HttpCacheAgeControl(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HttpCacheAgeControl, values: MaxAge (2), MaxAgeAndMaxStale (6), MaxAgeAndMinFresh (3), MaxStale (4), MinFresh (1), None (0) """
    MaxAge: HttpCacheAgeControl = ...
    MaxAgeAndMaxStale: HttpCacheAgeControl = ...
    MaxAgeAndMinFresh: HttpCacheAgeControl = ...
    MaxStale: HttpCacheAgeControl = ...
    MinFresh: HttpCacheAgeControl = ...
    value__ = ...


class HttpRequestCacheLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HttpRequestCacheLevel, values: BypassCache (1), CacheIfAvailable (3), CacheOnly (2), CacheOrNextCacheOnly (7), Default (0), NoCacheNoStore (6), Refresh (8), Reload (5), Revalidate (4) """
    BypassCache: HttpRequestCacheLevel = ...
    CacheIfAvailable: HttpRequestCacheLevel = ...
    CacheOnly: HttpRequestCacheLevel = ...
    CacheOrNextCacheOnly: HttpRequestCacheLevel = ...
    Default: HttpRequestCacheLevel = ...
    NoCacheNoStore: HttpRequestCacheLevel = ...
    Refresh: HttpRequestCacheLevel = ...
    Reload: HttpRequestCacheLevel = ...
    Revalidate: HttpRequestCacheLevel = ...
    value__ = ...


class RequestCachePolicy: # skipped bases: <type 'object'>, <type 'object'>
    """
    RequestCachePolicy()
    RequestCachePolicy(level: RequestCacheLevel)
    """
    @property
    def Level(self) -> RequestCacheLevel:
        """ Get: Level(self: RequestCachePolicy) -> RequestCacheLevel """
        ...


    def ToString(self) -> str:
        """ ToString(self: RequestCachePolicy) -> str """
        ...


class HttpRequestCachePolicy(RequestCachePolicy): # skipped bases: <type 'object'>
    """
    HttpRequestCachePolicy()
    HttpRequestCachePolicy(level: HttpRequestCacheLevel)
    HttpRequestCachePolicy(cacheAgeControl: HttpCacheAgeControl, ageOrFreshOrStale: TimeSpan)
    HttpRequestCachePolicy(cacheAgeControl: HttpCacheAgeControl, maxAge: TimeSpan, freshOrStale: TimeSpan)
    HttpRequestCachePolicy(cacheSyncDate: DateTime)
    HttpRequestCachePolicy(cacheAgeControl: HttpCacheAgeControl, maxAge: TimeSpan, freshOrStale: TimeSpan, cacheSyncDate: DateTime)
    """
    @property
    def CacheSyncDate(self) -> DateTime:
        """ Get: CacheSyncDate(self: HttpRequestCachePolicy) -> DateTime """
        ...

    @property
    def MaxAge(self) -> TimeSpan:
        """ Get: MaxAge(self: HttpRequestCachePolicy) -> TimeSpan """
        ...

    @property
    def MaxStale(self) -> TimeSpan:
        """ Get: MaxStale(self: HttpRequestCachePolicy) -> TimeSpan """
        ...

    @property
    def MinFresh(self) -> TimeSpan:
        """ Get: MinFresh(self: HttpRequestCachePolicy) -> TimeSpan """
        ...



class RequestCacheLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RequestCacheLevel, values: BypassCache (1), CacheIfAvailable (3), CacheOnly (2), Default (0), NoCacheNoStore (6), Reload (5), Revalidate (4) """
    BypassCache: RequestCacheLevel = ...
    CacheIfAvailable: RequestCacheLevel = ...
    CacheOnly: RequestCacheLevel = ...
    Default: RequestCacheLevel = ...
    NoCacheNoStore: RequestCacheLevel = ...
    Reload: RequestCacheLevel = ...
    Revalidate: RequestCacheLevel = ...
    value__ = ...


