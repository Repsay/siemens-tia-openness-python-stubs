# encoding: utf-8
# module Siemens.Engineering.Hmi calls itself Hmi
# from Siemens.Engineering, Version=16.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.Hmi, Version=16.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import IEngineeringServiceProvider, ImportOptions

from Siemens.Engineering.Hmi.Communication import ConnectionComposition

from Siemens.Engineering.Hmi.Cycle import CycleComposition

from Siemens.Engineering.Hmi.RuntimeScripting import VBScriptSystemFolder

from Siemens.Engineering.Hmi.Screen import (ScreenGlobalElements, 
    ScreenOverview, ScreenPopupSystemFolder, ScreenSlideinSystemFolder, 
    ScreenSystemFolder, ScreenTemplateSystemFolder)

from Siemens.Engineering.Hmi.Tag import TagSystemFolder

from Siemens.Engineering.Hmi.TextGraphicList import (GraphicListComposition, 
    TextListComposition)

from Siemens.Engineering.HW import Software

from Siemens.Engineering.Library.Types import (IInstanceSearchScope, 
    IUpdateProjectScope)

from System import Enum, Nullable

from System.IO import FileInfo

"""The following names are not found in the module: ILimit, field#
"""

# no functions
# classes

class ConstValue(ILimit): # skipped bases: <type 'object'>
    """
    Represents an constant value.
    ConstValue(value: object)
    """
    @property
    def Value(self) -> object:
        """
        Gets or sets the value of the Siemens.Engineering.Hmi.ConstValue.
        Get: Value(self: ConstValue) -> object
        Set: Value(self: ConstValue) = value
        """
        ...


    def ToString(self) -> str:
        """
        ToString(self: ConstValue) -> str
            Returns a String that represents the current Object.
            Returns: A String representing the current Object.
        """
        ...


class DateTimeValues(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    A value indicating the granularity of the data or time (eg. Year, Month, etc.).
    enum (flags) DateTimeValues, values: Day (4), Hour (8), Minute (16), Month (2), None (0), Second (32), Year (1)
    """
    Day: DateTimeValues = ...
    Hour: DateTimeValues = ...
    Minute: DateTimeValues = ...
    Month: DateTimeValues = ...
    Second: DateTimeValues = ...
    value__ = ...
    Year: DateTimeValues = ...


class HmiTarget(IInstanceSearchScope, IUpdateProjectScope, IEngineeringServiceProvider, Software): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IServiceProvider'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ Represents the target device """
    @property
    def Author(self) -> str:
        """
        Author of the device
        Get: Author(self: HmiTarget) -> str
        """
        ...

    @property
    def Connections(self) -> ConnectionComposition:
        """
        Composition of connections
        Get: Connections(self: HmiTarget) -> ConnectionComposition
        """
        ...

    @property
    def Cycles(self) -> CycleComposition:
        """
        Composition of cycles
        Get: Cycles(self: HmiTarget) -> CycleComposition
        """
        ...

    @property
    def GraphicLists(self) -> GraphicListComposition:
        """
        Composition of graphic lists
        Get: GraphicLists(self: HmiTarget) -> GraphicListComposition
        """
        ...

    @property
    def ScreenFolder(self) -> ScreenSystemFolder:
        """
        Gets the Hmi screen system folder
        Get: ScreenFolder(self: HmiTarget) -> ScreenSystemFolder
        """
        ...

    @property
    def ScreenGlobalElements(self) -> ScreenGlobalElements:
        """
        Gets the Hmi screen global elements
        Get: ScreenGlobalElements(self: HmiTarget) -> ScreenGlobalElements
        """
        ...

    @property
    def ScreenOverview(self) -> ScreenOverview:
        """
        Gets the Hmi screen overview
        Get: ScreenOverview(self: HmiTarget) -> ScreenOverview
        """
        ...

    @property
    def ScreenPopupFolder(self) -> ScreenPopupSystemFolder:
        """
        System folder for the HMI pop-up screens
        Get: ScreenPopupFolder(self: HmiTarget) -> ScreenPopupSystemFolder
        """
        ...

    @property
    def ScreenSlideinFolder(self) -> ScreenSlideinSystemFolder:
        """
        System folder for the HMI slide-in screens
        Get: ScreenSlideinFolder(self: HmiTarget) -> ScreenSlideinSystemFolder
        """
        ...

    @property
    def ScreenTemplateFolder(self) -> ScreenTemplateSystemFolder:
        """
        Composition of screen template folders
        Get: ScreenTemplateFolder(self: HmiTarget) -> ScreenTemplateSystemFolder
        """
        ...

    @property
    def TagFolder(self) -> TagSystemFolder:
        """
        Gets the Hmi tag system folder
        Get: TagFolder(self: HmiTarget) -> TagSystemFolder
        """
        ...

    @property
    def TextLists(self) -> TextListComposition:
        """
        Composition of text lists
        Get: TextLists(self: HmiTarget) -> TextListComposition
        """
        ...

    @property
    def VBScriptFolder(self) -> VBScriptSystemFolder:
        """
        Gets the VBScript system folder
        Get: VBScriptFolder(self: HmiTarget) -> VBScriptSystemFolder
        """
        ...


    def ImportScreenGlobalElements(self, path:FileInfo, importOptions:ImportOptions): # -> 
        """
        ImportScreenGlobalElements(self: HmiTarget, path: FileInfo, importOptions: ImportOptions)
            Simatic ML import of screen global elements
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
        """
        ...

    def ImportScreenOverview(self, path:FileInfo, importOptions:ImportOptions): # -> 
        """
        ImportScreenOverview(self: HmiTarget, path: FileInfo, importOptions: ImportOptions)
            Simatic ML import of a screen overview
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
        """
        ...


class ILimit: # skipped bases: <type 'object'>
    """ Represents an object which can serve as a limit. """
    pass

class NullableDateTime: # skipped bases: <type 'object'>, <type 'object'>
    """
    Represents an instant in time, typically expressed as a date and time
    NullableDateTime(dateTime: DateTime)
    NullableDateTime(dateTime: DateTime, dateTimeValues: DateTimeValues)
    NullableDateTime(nullableDateTime: NullableDateTime)
    NullableDateTime(value: str)
    """
    @property
    def DateTimeValues(self) -> DateTimeValues:
        """
        The granularity of the wrapped System.DateTime.
        Get: DateTimeValues(self: NullableDateTime) -> DateTimeValues
        """
        ...

    @property
    def Day(self) -> Nullable:
        """
        Day
        Get: Day(self: NullableDateTime) -> Nullable[int]
        Set: Day(self: NullableDateTime) = value
        """
        ...

    @property
    def Hour(self) -> Nullable:
        """
        Hour
        Get: Hour(self: NullableDateTime) -> Nullable[int]
        Set: Hour(self: NullableDateTime) = value
        """
        ...

    @property
    def Minute(self) -> Nullable:
        """
        Minute
        Get: Minute(self: NullableDateTime) -> Nullable[int]
        Set: Minute(self: NullableDateTime) = value
        """
        ...

    @property
    def Month(self) -> Nullable:
        """
        Month
        Get: Month(self: NullableDateTime) -> Nullable[int]
        Set: Month(self: NullableDateTime) = value
        """
        ...

    @property
    def Second(self) -> Nullable:
        """
        Second
        Get: Second(self: NullableDateTime) -> Nullable[int]
        Set: Second(self: NullableDateTime) = value
        """
        ...

    @property
    def Year(self) -> Nullable:
        """
        Year
        Get: Year(self: NullableDateTime) -> Nullable[int]
        Set: Year(self: NullableDateTime) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """
        Equals(self: NullableDateTime, obj: object) -> bool
            Indicates whether this instance and a specified object are equal.
            obj: Another object to compare to.
            Returns: true if obj and this instance are the same type and represent the same value; otherwise, false.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: NullableDateTime) -> int
            Returns the hash code for this instance.
            Returns: A 32-bit signed integer that is the hash code for this instance.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: NullableDateTime) -> str
            Converts the value of the current NullableDateTime object to its equivalent string representation.
            Returns: A string representation of the value of the current NullableDateTime object.
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


# variables with complex values

