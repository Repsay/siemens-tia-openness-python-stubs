# encoding: utf-8
# module System.Drawing.Text calls itself Text
# from System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, IDisposable, IntPtr

"""The following names are not found in the module: field#
"""

# no functions
# classes

class FontCollection(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Families(self) -> Array:
        """ Get: Families(self: FontCollection) -> Array[FontFamily] """
        ...



class GenericFontFamilies(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GenericFontFamilies, values: Monospace (2), SansSerif (1), Serif (0) """
    Monospace: GenericFontFamilies = ...
    SansSerif: GenericFontFamilies = ...
    Serif: GenericFontFamilies = ...
    value__ = ...


class HotkeyPrefix(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HotkeyPrefix, values: Hide (2), None (0), Show (1) """
    Hide: HotkeyPrefix = ...
    Show: HotkeyPrefix = ...
    value__ = ...


class InstalledFontCollection(FontCollection): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ InstalledFontCollection() """
    pass

class PrivateFontCollection(FontCollection): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ PrivateFontCollection() """
    def AddFontFile(self, filename:str): # -> 
        """ AddFontFile(self: PrivateFontCollection, filename: str) """
        ...

    def AddMemoryFont(self, memory:IntPtr, length:int): # -> 
        """ AddMemoryFont(self: PrivateFontCollection, memory: IntPtr, length: int) """
        ...


class TextRenderingHint(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TextRenderingHint, values: AntiAlias (4), AntiAliasGridFit (3), ClearTypeGridFit (5), SingleBitPerPixel (2), SingleBitPerPixelGridFit (1), SystemDefault (0) """
    AntiAlias: TextRenderingHint = ...
    AntiAliasGridFit: TextRenderingHint = ...
    ClearTypeGridFit: TextRenderingHint = ...
    SingleBitPerPixel: TextRenderingHint = ...
    SingleBitPerPixelGridFit: TextRenderingHint = ...
    SystemDefault: TextRenderingHint = ...
    value__ = ...


