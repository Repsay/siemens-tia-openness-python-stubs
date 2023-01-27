# encoding: utf-8
# module Microsoft.StylusInput.PluginData calls itself PluginData
# from Microsoft.Ink, Version=6.1.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Ink import (ApplicationGesture, RecognitionConfidence, 
    SystemGesture, Tablet)

from Microsoft.StylusInput import DataInterestMask, DynamicRenderer, Stylus

from System import Array, Char, Guid

from System.Collections import IEnumerable

from typing import Self

from Windows.Foundation import Point


# no functions
# classes

class CustomStylusData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CustomDataId(self) -> Guid:
        """ Get: CustomDataId(self: CustomStylusData) -> Guid """
        ...

    @property
    def Data(self) -> object:
        """ Get: Data(self: CustomStylusData) -> object """
        ...



class DynamicRendererCachedData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CachedDataId(self) -> int:
        """ Get: CachedDataId(self: DynamicRendererCachedData) -> int """
        ...

    @property
    def DynamicRenderer(self) -> DynamicRenderer:
        """ Get: DynamicRenderer(self: DynamicRendererCachedData) -> DynamicRenderer """
        ...



class ErrorData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DataId(self) -> DataInterestMask:
        """ Get: DataId(self: ErrorData) -> DataInterestMask """
        ...

    @property
    def InnerException(self) -> Exception:
        """ Get: InnerException(self: ErrorData) -> Exception """
        ...

    @property
    def Plugin(self) -> object:
        """ Get: Plugin(self: ErrorData) -> object """
        ...



class GestureAlternate: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Confidence(self) -> RecognitionConfidence:
        """ Get: Confidence(self: GestureAlternate) -> RecognitionConfidence """
        ...

    @property
    def Id(self) -> ApplicationGesture:
        """ Get: Id(self: GestureAlternate) -> ApplicationGesture """
        ...

    @property
    def StrokeCount(self) -> int:
        """ Get: StrokeCount(self: GestureAlternate) -> int """
        ...



class GestureRecognitionData(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: GestureRecognitionData) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class StylusDataBase(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: StylusDataBase) -> int """
        ...

    @property
    def PacketPropertyCount(self) -> int:
        """ Get: PacketPropertyCount(self: StylusDataBase) -> int """
        ...

    @property
    def Stylus(self) -> Stylus:
        """ Get: Stylus(self: StylusDataBase) -> Stylus """
        ...


    def GetData(self) -> Array:
        """ GetData(self: StylusDataBase) -> Array[int] """
        ...

    def SetData(self, value:Array): # -> 
        """ SetData(self: StylusDataBase, value: Array[int]) """
        ...

    def VerifyPacketData(self, *args): #cannot find CLR method
        """ VerifyPacketData(self: StylusDataBase, packetPropertyCount: int, packetData: Array[int]) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class InAirPacketsData(StylusDataBase): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ InAirPacketsData(stylus: Stylus, packetPropertyCount: int, packetData: Array[int]) """
    def __new__(cls, stylus:Stylus, packetPropertyCount:int, packetData:Array) -> Self:
        """ __new__(cls: type, stylus: Stylus, packetPropertyCount: int, packetData: Array[int]) """
        ...


class PacketsData(StylusDataBase): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ PacketsData(stylus: Stylus, packetPropertyCount: int, packetData: Array[int]) """
    def __new__(cls, stylus:Stylus, packetPropertyCount:int, packetData:Array) -> Self:
        """ __new__(cls: type, stylus: Stylus, packetPropertyCount: int, packetData: Array[int]) """
        ...


class RealTimeStylusDisabledData(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: RealTimeStylusDisabledData) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class RealTimeStylusEnabledData(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: RealTimeStylusEnabledData) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class StylusButtonDataBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ButtonIndex(self) -> int:
        """ Get: ButtonIndex(self: StylusButtonDataBase) -> int """
        ...

    @property
    def Stylus(self) -> Stylus:
        """ Get: Stylus(self: StylusButtonDataBase) -> Stylus """
        ...



class StylusButtonDownData(StylusButtonDataBase): # skipped bases: <type 'object'>
    """ StylusButtonDownData(stylus: Stylus, buttonIndex: int) """
    def __new__(cls, stylus:Stylus, buttonIndex:int) -> Self:
        """ __new__(cls: type, stylus: Stylus, buttonIndex: int) """
        ...


class StylusButtonUpData(StylusButtonDataBase): # skipped bases: <type 'object'>
    """ StylusButtonUpData(stylus: Stylus, buttonIndex: int) """
    def __new__(cls, stylus:Stylus, buttonIndex:int) -> Self:
        """ __new__(cls: type, stylus: Stylus, buttonIndex: int) """
        ...


class StylusDownData(StylusDataBase): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ StylusDownData(stylus: Stylus, packetPropertyCount: int, packetData: Array[int]) """
    def __new__(cls, stylus:Stylus, packetPropertyCount:int, packetData:Array) -> Self:
        """ __new__(cls: type, stylus: Stylus, packetPropertyCount: int, packetData: Array[int]) """
        ...


class StylusInRangeData: # skipped bases: <type 'object'>, <type 'object'>
    """ StylusInRangeData(stylus: Stylus) """
    @property
    def Stylus(self) -> Stylus:
        """ Get: Stylus(self: StylusInRangeData) -> Stylus """
        ...



class StylusOutOfRangeData: # skipped bases: <type 'object'>, <type 'object'>
    """ StylusOutOfRangeData(stylus: Stylus) """
    @property
    def Stylus(self) -> Stylus:
        """ Get: Stylus(self: StylusOutOfRangeData) -> Stylus """
        ...



class StylusUpData(StylusDataBase): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ StylusUpData(stylus: Stylus, packetPropertyCount: int, packetData: Array[int]) """
    def __new__(cls, stylus:Stylus, packetPropertyCount:int, packetData:Array) -> Self:
        """ __new__(cls: type, stylus: Stylus, packetPropertyCount: int, packetData: Array[int]) """
        ...


class SystemGestureData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Character(self) -> Char:
        """ Get: Character(self: SystemGestureData) -> Char """
        ...

    @property
    def Id(self) -> SystemGesture:
        """ Get: Id(self: SystemGestureData) -> SystemGesture """
        ...

    @property
    def Modifier(self) -> int:
        """ Get: Modifier(self: SystemGestureData) -> int """
        ...

    @property
    def Point(self) -> Point:
        """ Get: Point(self: SystemGestureData) -> Point """
        ...

    @property
    def Stylus(self) -> Stylus:
        """ Get: Stylus(self: SystemGestureData) -> Stylus """
        ...

    @property
    def StylusMode(self) -> int:
        """ Get: StylusMode(self: SystemGestureData) -> int """
        ...



class TabletAddedData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Tablet(self) -> Tablet:
        """ Get: Tablet(self: TabletAddedData) -> Tablet """
        ...



class TabletRemovedData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def TabletIndex(self) -> int:
        """ Get: TabletIndex(self: TabletRemovedData) -> int """
        ...



