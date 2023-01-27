# encoding: utf-8
# module StdFormat
# from Microsoft.StdFormat, Version=7.0.3300.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, MulticastDelegate

from System.Collections import IEnumerable, IEnumerator

"""The following names are not found in the module: (BoundEvent, __ComObject, 
    field#)
"""

# no functions
# classes

class DataFormat: # skipped bases: <type 'object'>
    """ no doc """
    pass

class DataFormats: # skipped bases: <type 'object'>
    """ no doc """
    pass

class FirstDayOfWeek(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FirstDayOfWeek, values: fmtDayUseSystem (0), fmtFriday (6), fmtMonday (2), fmtSaturday (7), fmtSunday (1), fmtThursday (5), fmtTuesday (3), fmtWednesday (4) """
    fmtDayUseSystem: FirstDayOfWeek = ...
    fmtFriday: FirstDayOfWeek = ...
    fmtMonday: FirstDayOfWeek = ...
    fmtSaturday: FirstDayOfWeek = ...
    fmtSunday: FirstDayOfWeek = ...
    fmtThursday: FirstDayOfWeek = ...
    fmtTuesday: FirstDayOfWeek = ...
    fmtWednesday: FirstDayOfWeek = ...
    value__ = ...


class FirstWeekOfYear(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FirstWeekOfYear, values: fmtFirstFourDays (2), fmtFirstFullWeek (3), fmtFirstJan1 (1), fmtWeekUseSystem (0) """
    fmtFirstFourDays: FirstWeekOfYear = ...
    fmtFirstFullWeek: FirstWeekOfYear = ...
    fmtFirstJan1: FirstWeekOfYear = ...
    fmtWeekUseSystem: FirstWeekOfYear = ...
    value__ = ...


class FormatType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FormatType, values: fmtBoolean (5), fmtBytes (6), fmtCheckbox (4), fmtCustom (1), fmtGeneral (0), fmtObject (3), fmtPicture (2) """
    fmtBoolean: FormatType = ...
    fmtBytes: FormatType = ...
    fmtCheckbox: FormatType = ...
    fmtCustom: FormatType = ...
    fmtGeneral: FormatType = ...
    fmtObject: FormatType = ...
    fmtPicture: FormatType = ...
    value__ = ...


class IDataFormatDisp: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IDataFormatsDisp: # skipped bases: <type 'object'>
    """ no doc """
    pass

class IStdDataFormatDisp(IDataFormatDisp): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def FalseValue(self) -> object:
        """
        Get: FalseValue(self: IStdDataFormatDisp) -> object
        Set: FalseValue(self: IStdDataFormatDisp) = value
        """
        ...

    @property
    def FirstDayOfWeek(self) -> FirstDayOfWeek:
        """
        Get: FirstDayOfWeek(self: IStdDataFormatDisp) -> FirstDayOfWeek
        Set: FirstDayOfWeek(self: IStdDataFormatDisp) = value
        """
        ...

    @property
    def FirstWeekOfYear(self) -> FirstWeekOfYear:
        """
        Get: FirstWeekOfYear(self: IStdDataFormatDisp) -> FirstWeekOfYear
        Set: FirstWeekOfYear(self: IStdDataFormatDisp) = value
        """
        ...

    @property
    def Format(self) -> str:
        """
        Get: Format(self: IStdDataFormatDisp) -> str
        Set: Format(self: IStdDataFormatDisp) = value
        """
        ...

    @property
    def NullValue(self) -> object:
        """
        Get: NullValue(self: IStdDataFormatDisp) -> object
        Set: NullValue(self: IStdDataFormatDisp) = value
        """
        ...

    @property
    def TrueValue(self) -> object:
        """
        Get: TrueValue(self: IStdDataFormatDisp) -> object
        Set: TrueValue(self: IStdDataFormatDisp) = value
        """
        ...

    @property
    def Type(self) -> FormatType:
        """
        Get: Type(self: IStdDataFormatDisp) -> FormatType
        Set: Type(self: IStdDataFormatDisp) = value
        """
        ...



class IStdDataFormatEvents: # skipped bases: <type 'object'>
    """ no doc """
    def Changed(self): # -> 
        """ Changed(self: IStdDataFormatEvents) """
        ...

    def Format(self, DataValue:StdDataValue): # -> 
        """ Format(self: IStdDataFormatEvents, DataValue: StdDataValue) """
        ...

    def UnFormat(self, DataValue:StdDataValue): # -> 
        """ UnFormat(self: IStdDataFormatEvents, DataValue: StdDataValue) """
        ...


class IStdDataFormatEvents_ChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ IStdDataFormatEvents_ChangedEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self): # -> 
        """ Invoke(self: IStdDataFormatEvents_ChangedEventHandler) """
        ...


class IStdDataFormatEvents_Event: # skipped bases: <type 'object'>
    """ no doc """
    def add_Changed(self, A_1:IStdDataFormatEvents_ChangedEventHandler): # -> 
        """ add_Changed(self: IStdDataFormatEvents_Event, A_1: IStdDataFormatEvents_ChangedEventHandler) """
        ...

    def add_Format(self, A_1:IStdDataFormatEvents_FormatEventHandler): # -> 
        """ add_Format(self: IStdDataFormatEvents_Event, A_1: IStdDataFormatEvents_FormatEventHandler) """
        ...

    def add_UnFormat(self, A_1:IStdDataFormatEvents_UnFormatEventHandler): # -> 
        """ add_UnFormat(self: IStdDataFormatEvents_Event, A_1: IStdDataFormatEvents_UnFormatEventHandler) """
        ...

    def remove_Changed(self, A_1:IStdDataFormatEvents_ChangedEventHandler): # -> 
        """ remove_Changed(self: IStdDataFormatEvents_Event, A_1: IStdDataFormatEvents_ChangedEventHandler) """
        ...

    def remove_Format(self, A_1:IStdDataFormatEvents_FormatEventHandler): # -> 
        """ remove_Format(self: IStdDataFormatEvents_Event, A_1: IStdDataFormatEvents_FormatEventHandler) """
        ...

    def remove_UnFormat(self, A_1:IStdDataFormatEvents_UnFormatEventHandler): # -> 
        """ remove_UnFormat(self: IStdDataFormatEvents_Event, A_1: IStdDataFormatEvents_UnFormatEventHandler) """
        ...

    Changed = ...
    Format = ...
    UnFormat = ...


class IStdDataFormatEvents_FormatEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ IStdDataFormatEvents_FormatEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, DataValue:StdDataValue): # -> 
        """ Invoke(self: IStdDataFormatEvents_FormatEventHandler, DataValue: StdDataValue) """
        ...


class IStdDataFormatEvents_UnFormatEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ IStdDataFormatEvents_UnFormatEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, DataValue:StdDataValue): # -> 
        """ Invoke(self: IStdDataFormatEvents_UnFormatEventHandler, DataValue: StdDataValue) """
        ...


class IStdDataFormatsDisp(IEnumerable, IDataFormatsDisp): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: IStdDataFormatsDisp) -> int """
        ...


    def Add(self, pFormat:DataFormat, Index:object): # -> 
        """ Add(self: IStdDataFormatsDisp, pFormat: DataFormat, Index: object) """
        ...

    def Clear(self): # -> 
        """ Clear(self: IStdDataFormatsDisp) """
        ...

    def Remove(self, Index:object): # -> 
        """ Remove(self: IStdDataFormatsDisp, Index: object) """
        ...

    def _ItemField(self, Field:object) -> str:
        """ _ItemField(self: IStdDataFormatsDisp, Field: object) -> str """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IStdDataValueDisp: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def TargetObject(self) -> object:
        """
        Get: TargetObject(self: IStdDataValueDisp) -> object
        Set: TargetObject(self: IStdDataValueDisp) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: IStdDataValueDisp) -> object
        Set: Value(self: IStdDataValueDisp) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class StdDataFormat(IStdDataFormatDisp, IStdDataFormatEvents_Event): # skipped bases: <type 'IDataFormatDisp'>, <type 'object'>
    """ no doc """
    pass

class StdDataFormatClass(StdDataFormat, __ComObject): # skipped bases: <type 'IDataFormatDisp'>, <type 'IStdDataFormatDisp'>, <type 'IStdDataFormatEvents_Event'>, <type 'object'>
    """ StdDataFormatClass() """
    @property
    def FalseValue(self) -> object:
        """
        Get: FalseValue(self: StdDataFormatClass) -> object
        Set: FalseValue(self: StdDataFormatClass) = value
        """
        ...

    @property
    def FirstDayOfWeek(self) -> FirstDayOfWeek:
        """
        Get: FirstDayOfWeek(self: StdDataFormatClass) -> FirstDayOfWeek
        Set: FirstDayOfWeek(self: StdDataFormatClass) = value
        """
        ...

    @property
    def FirstWeekOfYear(self) -> FirstWeekOfYear:
        """
        Get: FirstWeekOfYear(self: StdDataFormatClass) -> FirstWeekOfYear
        Set: FirstWeekOfYear(self: StdDataFormatClass) = value
        """
        ...

    @property
    def Format(self) -> str:
        """
        Get: Format(self: StdDataFormatClass) -> str
        Set: Format(self: StdDataFormatClass) = value
        """
        ...

    @property
    def NullValue(self) -> object:
        """
        Get: NullValue(self: StdDataFormatClass) -> object
        Set: NullValue(self: StdDataFormatClass) = value
        """
        ...

    @property
    def TrueValue(self) -> object:
        """
        Get: TrueValue(self: StdDataFormatClass) -> object
        Set: TrueValue(self: StdDataFormatClass) = value
        """
        ...

    @property
    def Type(self) -> FormatType:
        """
        Get: Type(self: StdDataFormatClass) -> FormatType
        Set: Type(self: StdDataFormatClass) = value
        """
        ...


    def add_Changed(self, A_1:IStdDataFormatEvents_ChangedEventHandler): # -> 
        """ add_Changed(self: StdDataFormatClass, A_1: IStdDataFormatEvents_ChangedEventHandler) """
        ...

    def add_Format(self, A_1:IStdDataFormatEvents_FormatEventHandler): # -> 
        """ add_Format(self: StdDataFormatClass, A_1: IStdDataFormatEvents_FormatEventHandler) """
        ...

    def add_UnFormat(self, A_1:IStdDataFormatEvents_UnFormatEventHandler): # -> 
        """ add_UnFormat(self: StdDataFormatClass, A_1: IStdDataFormatEvents_UnFormatEventHandler) """
        ...

    def remove_Changed(self, A_1:IStdDataFormatEvents_ChangedEventHandler): # -> 
        """ remove_Changed(self: StdDataFormatClass, A_1: IStdDataFormatEvents_ChangedEventHandler) """
        ...

    def remove_Format(self, A_1:IStdDataFormatEvents_FormatEventHandler): # -> 
        """ remove_Format(self: StdDataFormatClass, A_1: IStdDataFormatEvents_FormatEventHandler) """
        ...

    def remove_UnFormat(self, A_1:IStdDataFormatEvents_UnFormatEventHandler): # -> 
        """ remove_UnFormat(self: StdDataFormatClass, A_1: IStdDataFormatEvents_UnFormatEventHandler) """
        ...

    Changed = ...
    IStdDataFormatEvents_Event_Format = ...
    UnFormat = ...


class StdDataFormats(IStdDataFormatsDisp): # skipped bases: <type 'IDataFormatsDisp'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    pass

class StdDataFormatsClass(__ComObject, StdDataFormats): # skipped bases: <type 'IStdDataFormatsDisp'>, <type 'IDataFormatsDisp'>, <type 'IEnumerable'>, <type 'object'>
    """ StdDataFormatsClass() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: StdDataFormatsClass) -> int """
        ...


    def Add(self, pFormat:DataFormat, Index:object): # -> 
        """ Add(self: StdDataFormatsClass, pFormat: DataFormat, Index: object) """
        ...

    def Clear(self): # -> 
        """ Clear(self: StdDataFormatsClass) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: StdDataFormatsClass) -> IEnumerator """
        ...

    def Remove(self, Index:object): # -> 
        """ Remove(self: StdDataFormatsClass, Index: object) """
        ...

    def _ItemField(self, Field:object) -> str:
        """ _ItemField(self: StdDataFormatsClass, Field: object) -> str """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class StdDataValue(IStdDataValueDisp): # skipped bases: <type 'object'>
    """ no doc """
    pass

class StdDataValueClass(StdDataValue, __ComObject): # skipped bases: <type 'IStdDataValueDisp'>, <type 'object'>
    """ no doc """
    @property
    def TargetObject(self) -> object:
        """
        Get: TargetObject(self: StdDataValueClass) -> object
        Set: TargetObject(self: StdDataValueClass) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: StdDataValueClass) -> object
        Set: Value(self: StdDataValueClass) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


