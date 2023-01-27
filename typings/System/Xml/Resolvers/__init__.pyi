# encoding: utf-8
# module System.Xml.Resolvers calls itself Resolvers
# from System.Xml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, Uri

from System.Collections import IEnumerable

from System.Xml import XmlResolver

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class XmlKnownDtds(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) XmlKnownDtds, values: All (65535), None (0), Rss091 (2), Xhtml10 (1) """
    All: XmlKnownDtds = ...
    Rss091: XmlKnownDtds = ...
    value__ = ...
    Xhtml10: XmlKnownDtds = ...


class XmlPreloadedResolver(XmlResolver): # skipped bases: <type 'object'>
    """
    XmlPreloadedResolver()
    XmlPreloadedResolver(preloadedDtds: XmlKnownDtds)
    XmlPreloadedResolver(fallbackResolver: XmlResolver)
    XmlPreloadedResolver(fallbackResolver: XmlResolver, preloadedDtds: XmlKnownDtds)
    XmlPreloadedResolver(fallbackResolver: XmlResolver, preloadedDtds: XmlKnownDtds, uriComparer: IEqualityComparer[Uri])
    """
    @property
    def PreloadedUris(self) -> IEnumerable:
        """ Get: PreloadedUris(self: XmlPreloadedResolver) -> IEnumerable[Uri] """
        ...


    def Add(self, uri:Uri, value:Array, offset:int = ..., count:int = ...): # -> 
        """ Add(self: XmlPreloadedResolver, uri: Uri, value: Array[Byte])Add(self: XmlPreloadedResolver, uri: Uri, value: Array[Byte], offset: int, count: int)Add(self: XmlPreloadedResolver, uri: Uri, value: str)Add(self: XmlPreloadedResolver, uri: Uri, value: Stream) """
        ...

    def Remove(self, uri:Uri): # -> 
        """ Remove(self: XmlPreloadedResolver, uri: Uri) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __new__(cls, *__args:XmlKnownDtds) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, preloadedDtds: XmlKnownDtds)
        __new__(cls: type, fallbackResolver: XmlResolver)
        __new__(cls: type, fallbackResolver: XmlResolver, preloadedDtds: XmlKnownDtds)
        __new__(cls: type, fallbackResolver: XmlResolver, preloadedDtds: XmlKnownDtds, uriComparer: IEqualityComparer[Uri])
        """
        ...


