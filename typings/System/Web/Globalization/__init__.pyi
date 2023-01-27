# encoding: utf-8
# module System.Web.Globalization calls itself Globalization
# from System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array

from System.Globalization import CultureInfo


# no functions
# classes

class IStringLocalizerProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetLocalizedString(self, culture:CultureInfo, name:str, arguments:Array) -> str:
        """ GetLocalizedString(self: IStringLocalizerProvider, culture: CultureInfo, name: str, *arguments: Array[object]) -> str """
        ...


class ResourceFileStringLocalizerProvider(IStringLocalizerProvider): # skipped bases: <type 'object'>
    """ ResourceFileStringLocalizerProvider() """
    ResourceFileName: str = ...


class StringLocalizerProviders: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DataAnnotationStringLocalizerProvider(self) -> IStringLocalizerProvider:
        """
        Get: DataAnnotationStringLocalizerProvider() -> IStringLocalizerProvider
        Set: DataAnnotationStringLocalizerProvider() = value
        """
        ...


    __all__: list = ...


