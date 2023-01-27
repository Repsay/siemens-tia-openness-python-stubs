# encoding: utf-8
# module Microsoft.StylusInput calls itself StylusInput
# from Microsoft.Ink, Version=6.1.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Ink import (DrawingAttributes, Tablet, 
    TabletPropertyDescriptionCollection)

from Microsoft.StylusInput.PluginData import (CustomStylusData, ErrorData, 
    InAirPacketsData, PacketsData, RealTimeStylusDisabledData, 
    RealTimeStylusEnabledData, StylusButtonDownData, StylusButtonUpData, 
    StylusDownData, StylusInRangeData, StylusOutOfRangeData, StylusUpData, 
    SystemGestureData, TabletAddedData, TabletRemovedData)

from System import Array, Enum, Guid, IDisposable

from System.Collections import ICollection

from System.Drawing import Graphics, Rectangle

"""The following names are not found in the module: (
    INativeImplementationWrapper, field#)
"""

# no functions
# classes

class DataInterestMask(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DataInterestMask, values: AllStylusData (-1), CustomStylusDataAdded (32768), DefaultStylusData (37766), Error (1), InAirPackets (32), Packets (256), RealTimeStylusDisabled (4), RealTimeStylusEnabled (2), StylusButtonDown (2048), StylusButtonUp (1024), StylusDown (128), StylusInRange (16), StylusOutOfRange (64), StylusUp (512), SystemGesture (4096), TabletAdded (8192), TabletRemoved (16384) """
    AllStylusData: DataInterestMask = ...
    CustomStylusDataAdded: DataInterestMask = ...
    DefaultStylusData: DataInterestMask = ...
    Error: DataInterestMask = ...
    InAirPackets: DataInterestMask = ...
    Packets: DataInterestMask = ...
    RealTimeStylusDisabled: DataInterestMask = ...
    RealTimeStylusEnabled: DataInterestMask = ...
    StylusButtonDown: DataInterestMask = ...
    StylusButtonUp: DataInterestMask = ...
    StylusDown: DataInterestMask = ...
    StylusInRange: DataInterestMask = ...
    StylusOutOfRange: DataInterestMask = ...
    StylusUp: DataInterestMask = ...
    SystemGesture: DataInterestMask = ...
    TabletAdded: DataInterestMask = ...
    TabletRemoved: DataInterestMask = ...
    value__ = ...


class IStylusSyncPlugin: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataInterest(self) -> DataInterestMask:
        """ Get: DataInterest(self: IStylusSyncPlugin) -> DataInterestMask """
        ...


    def CustomStylusDataAdded(self, sender:RealTimeStylus, data:CustomStylusData): # -> 
        """ CustomStylusDataAdded(self: IStylusSyncPlugin, sender: RealTimeStylus, data: CustomStylusData) """
        ...

    def Error(self, sender:RealTimeStylus, data:ErrorData): # -> 
        """ Error(self: IStylusSyncPlugin, sender: RealTimeStylus, data: ErrorData) """
        ...

    def InAirPackets(self, sender:RealTimeStylus, data:InAirPacketsData): # -> 
        """ InAirPackets(self: IStylusSyncPlugin, sender: RealTimeStylus, data: InAirPacketsData) """
        ...

    def Packets(self, sender:RealTimeStylus, data:PacketsData): # -> 
        """ Packets(self: IStylusSyncPlugin, sender: RealTimeStylus, data: PacketsData) """
        ...

    def RealTimeStylusDisabled(self, sender:RealTimeStylus, data:RealTimeStylusDisabledData): # -> 
        """ RealTimeStylusDisabled(self: IStylusSyncPlugin, sender: RealTimeStylus, data: RealTimeStylusDisabledData) """
        ...

    def RealTimeStylusEnabled(self, sender:RealTimeStylus, data:RealTimeStylusEnabledData): # -> 
        """ RealTimeStylusEnabled(self: IStylusSyncPlugin, sender: RealTimeStylus, data: RealTimeStylusEnabledData) """
        ...

    def StylusButtonDown(self, sender:RealTimeStylus, data:StylusButtonDownData): # -> 
        """ StylusButtonDown(self: IStylusSyncPlugin, sender: RealTimeStylus, data: StylusButtonDownData) """
        ...

    def StylusButtonUp(self, sender:RealTimeStylus, data:StylusButtonUpData): # -> 
        """ StylusButtonUp(self: IStylusSyncPlugin, sender: RealTimeStylus, data: StylusButtonUpData) """
        ...

    def StylusDown(self, sender:RealTimeStylus, data:StylusDownData): # -> 
        """ StylusDown(self: IStylusSyncPlugin, sender: RealTimeStylus, data: StylusDownData) """
        ...

    def StylusInRange(self, sender:RealTimeStylus, data:StylusInRangeData): # -> 
        """ StylusInRange(self: IStylusSyncPlugin, sender: RealTimeStylus, data: StylusInRangeData) """
        ...

    def StylusOutOfRange(self, sender:RealTimeStylus, data:StylusOutOfRangeData): # -> 
        """ StylusOutOfRange(self: IStylusSyncPlugin, sender: RealTimeStylus, data: StylusOutOfRangeData) """
        ...

    def StylusUp(self, sender:RealTimeStylus, data:StylusUpData): # -> 
        """ StylusUp(self: IStylusSyncPlugin, sender: RealTimeStylus, data: StylusUpData) """
        ...

    def SystemGesture(self, sender:RealTimeStylus, data:SystemGestureData): # -> 
        """ SystemGesture(self: IStylusSyncPlugin, sender: RealTimeStylus, data: SystemGestureData) """
        ...

    def TabletAdded(self, sender:RealTimeStylus, data:TabletAddedData): # -> 
        """ TabletAdded(self: IStylusSyncPlugin, sender: RealTimeStylus, data: TabletAddedData) """
        ...

    def TabletRemoved(self, sender:RealTimeStylus, data:TabletRemovedData): # -> 
        """ TabletRemoved(self: IStylusSyncPlugin, sender: RealTimeStylus, data: TabletRemovedData) """
        ...


class DynamicRenderer(INativeImplementationWrapper, IDisposable, IStylusSyncPlugin): # skipped bases: <type 'object'>
    """
    DynamicRenderer(control: Control)
    DynamicRenderer(handle: IntPtr)
    """
    @property
    def ClipRectangle(self) -> Rectangle:
        """
        Get: ClipRectangle(self: DynamicRenderer) -> Rectangle
        Set: ClipRectangle(self: DynamicRenderer) = value
        """
        ...

    @property
    def DrawingAttributes(self) -> DrawingAttributes:
        """
        Get: DrawingAttributes(self: DynamicRenderer) -> DrawingAttributes
        Set: DrawingAttributes(self: DynamicRenderer) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: DynamicRenderer) -> bool
        Set: Enabled(self: DynamicRenderer) = value
        """
        ...

    @property
    def EnableDataCache(self) -> bool:
        """
        Get: EnableDataCache(self: DynamicRenderer) -> bool
        Set: EnableDataCache(self: DynamicRenderer) = value
        """
        ...


    def Draw(self, g:Graphics): # -> 
        """ Draw(self: DynamicRenderer, g: Graphics) """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: DynamicRenderer) """
        ...

    def ReleaseCachedData(self, cachedDataId:int): # -> 
        """ ReleaseCachedData(self: DynamicRenderer, cachedDataId: int) """
        ...

    DynamicRendererCachedDataGuid: Guid = ...


class GestureRecognizer(INativeImplementationWrapper, IStylusAsyncPlugin, IDisposable, IStylusSyncPlugin): # skipped bases: <type 'object'>
    """ GestureRecognizer() """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: GestureRecognizer) -> bool
        Set: Enabled(self: GestureRecognizer) = value
        """
        ...

    @property
    def MaxStrokeCount(self) -> int:
        """
        Get: MaxStrokeCount(self: GestureRecognizer) -> int
        Set: MaxStrokeCount(self: GestureRecognizer) = value
        """
        ...


    def EnableGestures(self, gestures:Array): # -> 
        """ EnableGestures(self: GestureRecognizer, gestures: Array[ApplicationGesture]) """
        ...

    def Reset(self): # -> 
        """ Reset(self: GestureRecognizer) """
        ...

    GestureRecognitionDataGuid: Guid = ...


class IStylusAsyncPlugin: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DataInterest(self) -> DataInterestMask:
        """ Get: DataInterest(self: IStylusAsyncPlugin) -> DataInterestMask """
        ...


    def CustomStylusDataAdded(self, sender:RealTimeStylus, data:CustomStylusData): # -> 
        """ CustomStylusDataAdded(self: IStylusAsyncPlugin, sender: RealTimeStylus, data: CustomStylusData) """
        ...

    def Error(self, sender:RealTimeStylus, data:ErrorData): # -> 
        """ Error(self: IStylusAsyncPlugin, sender: RealTimeStylus, data: ErrorData) """
        ...

    def InAirPackets(self, sender:RealTimeStylus, data:InAirPacketsData): # -> 
        """ InAirPackets(self: IStylusAsyncPlugin, sender: RealTimeStylus, data: InAirPacketsData) """
        ...

    def Packets(self, sender:RealTimeStylus, data:PacketsData): # -> 
        """ Packets(self: IStylusAsyncPlugin, sender: RealTimeStylus, data: PacketsData) """
        ...

    def RealTimeStylusDisabled(self, sender:RealTimeStylus, data:RealTimeStylusDisabledData): # -> 
        """ RealTimeStylusDisabled(self: IStylusAsyncPlugin, sender: RealTimeStylus, data: RealTimeStylusDisabledData) """
        ...

    def RealTimeStylusEnabled(self, sender:RealTimeStylus, data:RealTimeStylusEnabledData): # -> 
        """ RealTimeStylusEnabled(self: IStylusAsyncPlugin, sender: RealTimeStylus, data: RealTimeStylusEnabledData) """
        ...

    def StylusButtonDown(self, sender:RealTimeStylus, data:StylusButtonDownData): # -> 
        """ StylusButtonDown(self: IStylusAsyncPlugin, sender: RealTimeStylus, data: StylusButtonDownData) """
        ...

    def StylusButtonUp(self, sender:RealTimeStylus, data:StylusButtonUpData): # -> 
        """ StylusButtonUp(self: IStylusAsyncPlugin, sender: RealTimeStylus, data: StylusButtonUpData) """
        ...

    def StylusDown(self, sender:RealTimeStylus, data:StylusDownData): # -> 
        """ StylusDown(self: IStylusAsyncPlugin, sender: RealTimeStylus, data: StylusDownData) """
        ...

    def StylusInRange(self, sender:RealTimeStylus, data:StylusInRangeData): # -> 
        """ StylusInRange(self: IStylusAsyncPlugin, sender: RealTimeStylus, data: StylusInRangeData) """
        ...

    def StylusOutOfRange(self, sender:RealTimeStylus, data:StylusOutOfRangeData): # -> 
        """ StylusOutOfRange(self: IStylusAsyncPlugin, sender: RealTimeStylus, data: StylusOutOfRangeData) """
        ...

    def StylusUp(self, sender:RealTimeStylus, data:StylusUpData): # -> 
        """ StylusUp(self: IStylusAsyncPlugin, sender: RealTimeStylus, data: StylusUpData) """
        ...

    def SystemGesture(self, sender:RealTimeStylus, data:SystemGestureData): # -> 
        """ SystemGesture(self: IStylusAsyncPlugin, sender: RealTimeStylus, data: SystemGestureData) """
        ...

    def TabletAdded(self, sender:RealTimeStylus, data:TabletAddedData): # -> 
        """ TabletAdded(self: IStylusAsyncPlugin, sender: RealTimeStylus, data: TabletAddedData) """
        ...

    def TabletRemoved(self, sender:RealTimeStylus, data:TabletRemovedData): # -> 
        """ TabletRemoved(self: IStylusAsyncPlugin, sender: RealTimeStylus, data: TabletRemovedData) """
        ...


class RealTimeStylus(IDisposable, IStylusAsyncPlugin, INativeImplementationWrapper): # skipped bases: <type 'object'>
    """
    RealTimeStylus()
    RealTimeStylus(handle: IntPtr)
    RealTimeStylus(handle: IntPtr, useMouseForInput: bool)
    RealTimeStylus(handle: IntPtr, tablet: Tablet)
    RealTimeStylus(attachedControl: Control)
    RealTimeStylus(attachedControl: Control, useMouseForInput: bool)
    RealTimeStylus(attachedControl: Control, tablet: Tablet)
    """
    @property
    def AllTouchEnabled(self) -> bool:
        """
        Get: AllTouchEnabled(self: RealTimeStylus) -> bool
        Set: AllTouchEnabled(self: RealTimeStylus) = value
        """
        ...

    @property
    def AsyncPluginCollection(self) -> StylusAsyncPluginCollection:
        """ Get: AsyncPluginCollection(self: RealTimeStylus) -> StylusAsyncPluginCollection """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: RealTimeStylus) -> bool
        Set: Enabled(self: RealTimeStylus) = value
        """
        ...

    @property
    def FlicksEnabled(self) -> bool:
        """
        Get: FlicksEnabled(self: RealTimeStylus) -> bool
        Set: FlicksEnabled(self: RealTimeStylus) = value
        """
        ...

    @property
    def MultiTouchEnabled(self) -> bool:
        """
        Get: MultiTouchEnabled(self: RealTimeStylus) -> bool
        Set: MultiTouchEnabled(self: RealTimeStylus) = value
        """
        ...

    @property
    def SyncPluginCollection(self) -> StylusSyncPluginCollection:
        """ Get: SyncPluginCollection(self: RealTimeStylus) -> StylusSyncPluginCollection """
        ...

    @property
    def WindowInputRectangle(self) -> Rectangle:
        """
        Get: WindowInputRectangle(self: RealTimeStylus) -> Rectangle
        Set: WindowInputRectangle(self: RealTimeStylus) = value
        """
        ...


    def AddCustomStylusDataToQueue(self, queue:StylusQueues, guid:Guid, data:object): # -> 
        """ AddCustomStylusDataToQueue(self: RealTimeStylus, queue: StylusQueues, guid: Guid, data: object) """
        ...

    def ClearStylusQueues(self): # -> 
        """ ClearStylusQueues(self: RealTimeStylus) """
        ...

    def GetDesiredPacketDescription(self) -> Array:
        """ GetDesiredPacketDescription(self: RealTimeStylus) -> Array[Guid] """
        ...

    def GetStyluses(self) -> Array:
        """ GetStyluses(self: RealTimeStylus) -> Array[Stylus] """
        ...

    def GetTabletContextIdFromTablet(self, tablet:Tablet) -> int:
        """ GetTabletContextIdFromTablet(self: RealTimeStylus, tablet: Tablet) -> int """
        ...

    def GetTabletFromTabletContextId(self, tabletContextId:int) -> Tablet:
        """ GetTabletFromTabletContextId(self: RealTimeStylus, tabletContextId: int) -> Tablet """
        ...

    def GetTabletPropertyDescriptionCollection(self, tabletContextId:int) -> TabletPropertyDescriptionCollection:
        """ GetTabletPropertyDescriptionCollection(self: RealTimeStylus, tabletContextId: int) -> TabletPropertyDescriptionCollection """
        ...

    def SetDesiredPacketDescription(self, value:Array): # -> 
        """ SetDesiredPacketDescription(self: RealTimeStylus, value: Array[Guid]) """
        ...


class Stylus: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Buttons(self) -> StylusButtons:
        """ Get: Buttons(self: Stylus) -> StylusButtons """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: Stylus) -> int """
        ...

    @property
    def Inverted(self) -> bool:
        """ Get: Inverted(self: Stylus) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Stylus) -> str """
        ...

    @property
    def TabletContextId(self) -> int:
        """ Get: TabletContextId(self: Stylus) -> int """
        ...



class StylusAsyncPluginCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: StylusAsyncPluginCollection) -> bool """
        ...


    def Add(self, item:IStylusAsyncPlugin): # -> 
        """ Add(self: StylusAsyncPluginCollection, item: IStylusAsyncPlugin) """
        ...

    def Clear(self): # -> 
        """ Clear(self: StylusAsyncPluginCollection) """
        ...

    def Contains(self, plugin:IStylusAsyncPlugin) -> bool:
        """ Contains(self: StylusAsyncPluginCollection, plugin: IStylusAsyncPlugin) -> bool """
        ...

    def IndexOf(self, plugin:IStylusAsyncPlugin) -> int:
        """ IndexOf(self: StylusAsyncPluginCollection, plugin: IStylusAsyncPlugin) -> int """
        ...

    def Insert(self, index:int, item:IStylusAsyncPlugin): # -> 
        """ Insert(self: StylusAsyncPluginCollection, index: int, item: IStylusAsyncPlugin) """
        ...

    def Remove(self, item:IStylusAsyncPlugin): # -> 
        """ Remove(self: StylusAsyncPluginCollection, item: IStylusAsyncPlugin) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: StylusAsyncPluginCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class StylusButtons: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: StylusButtons) -> int """
        ...


    def GetId(self, index:int) -> Guid:
        """ GetId(self: StylusButtons, index: int) -> Guid """
        ...

    def GetName(self, index:int) -> str:
        """ GetName(self: StylusButtons, index: int) -> str """
        ...


class StylusQueues(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StylusQueues, values: Input (0), Output (2), OutputImmediate (1) """
    Input: StylusQueues = ...
    Output: StylusQueues = ...
    OutputImmediate: StylusQueues = ...
    value__ = ...


class StylusSyncPluginCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: StylusSyncPluginCollection) -> bool """
        ...


    def Add(self, item:IStylusSyncPlugin): # -> 
        """ Add(self: StylusSyncPluginCollection, item: IStylusSyncPlugin) """
        ...

    def Clear(self): # -> 
        """ Clear(self: StylusSyncPluginCollection) """
        ...

    def Contains(self, plugin:IStylusSyncPlugin) -> bool:
        """ Contains(self: StylusSyncPluginCollection, plugin: IStylusSyncPlugin) -> bool """
        ...

    def IndexOf(self, plugin:IStylusSyncPlugin) -> int:
        """ IndexOf(self: StylusSyncPluginCollection, plugin: IStylusSyncPlugin) -> int """
        ...

    def Insert(self, index:int, item:IStylusSyncPlugin): # -> 
        """ Insert(self: StylusSyncPluginCollection, index: int, item: IStylusSyncPlugin) """
        ...

    def Remove(self, item:IStylusSyncPlugin): # -> 
        """ Remove(self: StylusSyncPluginCollection, item: IStylusSyncPlugin) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: StylusSyncPluginCollection, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


# variables with complex values

