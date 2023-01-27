# encoding: utf-8
# module Microsoft.VisualBasic calls itself VisualBasic
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, Microsoft.VisualBasic.Compatibility, Version=10.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, Microsoft.VisualBasic.Compatibility.Data, Version=10.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, Microsoft.VisualBasic, Version=10.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, Microsoft.VisualBasic.Vsa, Version=8.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from StdFormat import FirstDayOfWeek, FirstWeekOfYear

from System import (Array, Attribute, Char, DateTime, Enum, Int16, Int64, 
    SByte, Single, Type)

from System.CodeDom.Compiler import CodeDomProvider

from System.Collections import IDictionary, IEnumerator, IList

from System.Runtime.Serialization import (IDeserializationCallback, 
    ISerializable)

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (DateFormat, DateInterval, 
    FileAttribute, MsgBoxResult, MsgBoxStyle, OpenAccess, OpenMode, OpenShare, 
    SpcInfo, TabInfo, TriState, VariantType, VbStrConv, field#)
"""

# no functions
# classes

class AppWinStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AppWinStyle, values: Hide (0), MaximizedFocus (3), MinimizedFocus (2), MinimizedNoFocus (6), NormalFocus (1), NormalNoFocus (4) """
    Hide: AppWinStyle = ...
    MaximizedFocus: AppWinStyle = ...
    MinimizedFocus: AppWinStyle = ...
    MinimizedNoFocus: AppWinStyle = ...
    NormalFocus: AppWinStyle = ...
    NormalNoFocus: AppWinStyle = ...
    value__ = ...


class AudioPlayMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AudioPlayMode, values: Background (1), BackgroundLoop (2), WaitToComplete (0) """
    Background: AudioPlayMode = ...
    BackgroundLoop: AudioPlayMode = ...
    value__ = ...
    WaitToComplete: AudioPlayMode = ...


class CallType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CallType, values: Get (2), Let (4), Method (1), Set (8) """
    Get: CallType = ...
    Let: CallType = ...
    Method: CallType = ...
    Set: CallType = ...
    value__ = ...


class Collection(IList, IDeserializationCallback, ISerializable): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ Collection() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: Collection) -> int """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: Collection) -> IEnumerator """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class ComClassAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ComClassAttribute()
    ComClassAttribute(_ClassID: str)
    ComClassAttribute(_ClassID: str, _InterfaceID: str)
    ComClassAttribute(_ClassID: str, _InterfaceID: str, _EventId: str)
    """
    @property
    def ClassID(self) -> str:
        """ Get: ClassID(self: ComClassAttribute) -> str """
        ...

    @property
    def EventID(self) -> str:
        """ Get: EventID(self: ComClassAttribute) -> str """
        ...

    @property
    def InterfaceID(self) -> str:
        """ Get: InterfaceID(self: ComClassAttribute) -> str """
        ...

    @property
    def InterfaceShadows(self) -> bool:
        """
        Get: InterfaceShadows(self: ComClassAttribute) -> bool
        Set: InterfaceShadows(self: ComClassAttribute) = value
        """
        ...


    def __new__(cls, _ClassID:str = ..., _InterfaceID:str = ..., _EventId:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, _ClassID: str)
        __new__(cls: type, _ClassID: str, _InterfaceID: str)
        __new__(cls: type, _ClassID: str, _InterfaceID: str, _EventId: str)
        """
        ...


class CompareMethod(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CompareMethod, values: Binary (0), Text (1) """
    Binary: CompareMethod = ...
    Text: CompareMethod = ...
    value__ = ...


class Constants: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    vbAbort = ...
    vbAbortRetryIgnore = ...
    vbApplicationModal = ...
    vbArchive = ...
    vbArray = ...
    vbBack: str = ...
    vbBinaryCompare: CompareMethod = ...
    vbBoolean = ...
    vbByte = ...
    vbCancel = ...
    vbCr: str = ...
    vbCritical = ...
    vbCrLf: str = ...
    vbCurrency = ...
    vbDate = ...
    vbDecimal = ...
    vbDefaultButton1 = ...
    vbDefaultButton2 = ...
    vbDefaultButton3 = ...
    vbDirectory = ...
    vbDouble = ...
    vbEmpty = ...
    vbExclamation = ...
    vbFalse = ...
    vbFirstFourDays: FirstWeekOfYear = ...
    vbFirstFullWeek: FirstWeekOfYear = ...
    vbFirstJan1: FirstWeekOfYear = ...
    vbFormFeed: str = ...
    vbFriday: FirstDayOfWeek = ...
    vbGeneralDate = ...
    vbGet: CallType = ...
    vbHidden = ...
    vbHide: AppWinStyle = ...
    vbHiragana = ...
    vbIgnore = ...
    vbInformation = ...
    vbInteger = ...
    vbKatakana = ...
    vbLet: CallType = ...
    vbLf: str = ...
    vbLinguisticCasing = ...
    vbLong = ...
    vbLongDate = ...
    vbLongTime = ...
    vbLowerCase = ...
    vbMaximizedFocus: AppWinStyle = ...
    vbMethod: CallType = ...
    vbMinimizedFocus: AppWinStyle = ...
    vbMinimizedNoFocus: AppWinStyle = ...
    vbMonday: FirstDayOfWeek = ...
    vbMsgBoxHelp = ...
    vbMsgBoxRight = ...
    vbMsgBoxRtlReading = ...
    vbMsgBoxSetForeground = ...
    vbNarrow = ...
    vbNewLine: str = ...
    vbNo = ...
    vbNormal = ...
    vbNormalFocus: AppWinStyle = ...
    vbNormalNoFocus: AppWinStyle = ...
    vbNull = ...
    vbNullChar: str = ...
    vbObject = ...
    vbObjectError: int = ...
    vbOK = ...
    vbOKCancel = ...
    vbOKOnly = ...
    vbProperCase = ...
    vbQuestion = ...
    vbReadOnly = ...
    vbRetry = ...
    vbRetryCancel = ...
    vbSaturday: FirstDayOfWeek = ...
    vbSet: CallType = ...
    vbShortDate = ...
    vbShortTime = ...
    vbSimplifiedChinese = ...
    vbSingle = ...
    vbString = ...
    vbSunday: FirstDayOfWeek = ...
    vbSystem = ...
    vbSystemModal = ...
    vbTab: str = ...
    vbTextCompare: CompareMethod = ...
    vbThursday: FirstDayOfWeek = ...
    vbTraditionalChinese = ...
    vbTrue = ...
    vbTuesday: FirstDayOfWeek = ...
    vbUpperCase = ...
    vbUseDefault = ...
    vbUserDefinedType = ...
    vbUseSystem: FirstWeekOfYear = ...
    vbUseSystemDayOfWeek: FirstDayOfWeek = ...
    vbVariant = ...
    vbVerticalTab: str = ...
    vbVolume = ...
    vbWednesday: FirstDayOfWeek = ...
    vbWide = ...
    vbYes = ...
    vbYesNo = ...
    vbYesNoCancel = ...


class ControlChars: # skipped bases: <type 'object'>, <type 'object'>
    """ ControlChars() """
    Back: Char = ...
    Cr: Char = ...
    CrLf: str = ...
    FormFeed: Char = ...
    Lf: Char = ...
    NewLine: str = ...
    NullChar: Char = ...
    Quote: Char = ...
    Tab: Char = ...
    VerticalTab: Char = ...


class Conversion: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CTypeDynamic(Expression:object, TargetType:Type = ...) -> object:
        """
        CTypeDynamic(Expression: object, TargetType: Type) -> object
        CTypeDynamic[TargetType](Expression: object) -> TargetType
        """
        ...

    @staticmethod
    def ErrorToString(ErrorNumber=None) -> str:
        """
        ErrorToString() -> str
        ErrorToString(ErrorNumber: int) -> str
        """
        ...

    @staticmethod
    def Fix(Number:Int16) -> Int16:
        """
        Fix(Number: Int16) -> Int16
        Fix(Number: int) -> int
        Fix(Number: Int64) -> Int64
        Fix(Number: float) -> float
        Fix(Number: Single) -> Single
        Fix(Number: Decimal) -> Decimal
        Fix(Number: object) -> object
        """
        ...

    @staticmethod
    def Hex(Number:SByte) -> str:
        """
        Hex(Number: SByte) -> str
        Hex(Number: Byte) -> str
        Hex(Number: Int16) -> str
        Hex(Number: UInt16) -> str
        Hex(Number: int) -> str
        Hex(Number: UInt32) -> str
        Hex(Number: Int64) -> str
        Hex(Number: UInt64) -> str
        Hex(Number: object) -> str
        """
        ...

    @staticmethod
    def Int(Number:Int16) -> Int16:
        """
        Int(Number: Int16) -> Int16
        Int(Number: int) -> int
        Int(Number: Int64) -> Int64
        Int(Number: float) -> float
        Int(Number: Single) -> Single
        Int(Number: Decimal) -> Decimal
        Int(Number: object) -> object
        """
        ...

    @staticmethod
    def Oct(Number:SByte) -> str:
        """
        Oct(Number: SByte) -> str
        Oct(Number: Byte) -> str
        Oct(Number: Int16) -> str
        Oct(Number: UInt16) -> str
        Oct(Number: int) -> str
        Oct(Number: UInt32) -> str
        Oct(Number: Int64) -> str
        Oct(Number: UInt64) -> str
        Oct(Number: object) -> str
        """
        ...

    @staticmethod
    def Str(Number:object) -> str:
        """ Str(Number: object) -> str """
        ...

    @staticmethod
    def Val(*__args:str) -> float:
        """
        Val(InputStr: str) -> float
        Val(Expression: Char) -> int
        Val(Expression: object) -> float
        """
        ...


class DateAndTime: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DateString(self) -> str:
        """
        Get: DateString() -> str
        Set: DateString() = value
        """
        ...

    @property
    def Now(self) -> DateTime:
        """ Get: Now() -> DateTime """
        ...

    @property
    def TimeOfDay(self) -> DateTime:
        """
        Get: TimeOfDay() -> DateTime
        Set: TimeOfDay() = value
        """
        ...

    @property
    def Timer(self) -> float:
        """ Get: Timer() -> float """
        ...

    @property
    def TimeString(self) -> str:
        """
        Get: TimeString() -> str
        Set: TimeString() = value
        """
        ...

    @property
    def Today(self) -> DateTime:
        """
        Get: Today() -> DateTime
        Set: Today() = value
        """
        ...


    @staticmethod
    def DateAdd(Interval, Number:float, DateValue:DateTime) -> DateTime: # Not found arg types: {'Interval': 'DateInterval'}
        """
        DateAdd(Interval: DateInterval, Number: float, DateValue: DateTime) -> DateTime
        DateAdd(Interval: str, Number: float, DateValue: object) -> DateTime
        """
        ...

    @staticmethod
    def DateDiff(Interval, Date1:DateTime, Date2:DateTime, DayOfWeek:FirstDayOfWeek, WeekOfYear:FirstWeekOfYear) -> Int64: # Not found arg types: {'Interval': 'DateInterval'}
        """
        DateDiff(Interval: DateInterval, Date1: DateTime, Date2: DateTime, DayOfWeek: FirstDayOfWeek, WeekOfYear: FirstWeekOfYear) -> Int64
        DateDiff(Interval: str, Date1: object, Date2: object, DayOfWeek: FirstDayOfWeek, WeekOfYear: FirstWeekOfYear) -> Int64
        """
        ...

    @staticmethod
    def DatePart(Interval, DateValue, *__args) -> int:
        """
        DatePart(Interval: DateInterval, DateValue: DateTime, FirstDayOfWeekValue: FirstDayOfWeek, FirstWeekOfYearValue: FirstWeekOfYear) -> int
        DatePart(Interval: str, DateValue: object, DayOfWeek: FirstDayOfWeek, WeekOfYear: FirstWeekOfYear) -> int
        """
        ...

    @staticmethod
    def DateSerial(Year:int, Month:int, Day:int) -> DateTime:
        """ DateSerial(Year: int, Month: int, Day: int) -> DateTime """
        ...

    @staticmethod
    def DateValue(StringDate:str) -> DateTime:
        """ DateValue(StringDate: str) -> DateTime """
        ...

    @staticmethod
    def Day(DateValue:DateTime) -> int:
        """ Day(DateValue: DateTime) -> int """
        ...

    @staticmethod
    def Hour(TimeValue:DateTime) -> int:
        """ Hour(TimeValue: DateTime) -> int """
        ...

    @staticmethod
    def Minute(TimeValue:DateTime) -> int:
        """ Minute(TimeValue: DateTime) -> int """
        ...

    @staticmethod
    def Month(DateValue:DateTime) -> int:
        """ Month(DateValue: DateTime) -> int """
        ...

    @staticmethod
    def MonthName(Month:int, Abbreviate:bool) -> str:
        """ MonthName(Month: int, Abbreviate: bool) -> str """
        ...

    @staticmethod
    def Second(TimeValue:DateTime) -> int:
        """ Second(TimeValue: DateTime) -> int """
        ...

    @staticmethod
    def TimeSerial(Hour:int, Minute:int, Second:int) -> DateTime:
        """ TimeSerial(Hour: int, Minute: int, Second: int) -> DateTime """
        ...

    @staticmethod
    def TimeValue(StringTime:str) -> DateTime:
        """ TimeValue(StringTime: str) -> DateTime """
        ...

    @staticmethod
    def Weekday(DateValue:DateTime, DayOfWeek:FirstDayOfWeek) -> int:
        """ Weekday(DateValue: DateTime, DayOfWeek: FirstDayOfWeek) -> int """
        ...

    @staticmethod
    def WeekdayName(Weekday:int, Abbreviate:bool, FirstDayOfWeekValue:FirstDayOfWeek) -> str:
        """ WeekdayName(Weekday: int, Abbreviate: bool, FirstDayOfWeekValue: FirstDayOfWeek) -> str """
        ...

    @staticmethod
    def Year(DateValue:DateTime) -> int:
        """ Year(DateValue: DateTime) -> int """
        ...



class DateFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DateFormat, values: GeneralDate (0), LongDate (1), LongTime (3), ShortDate (2), ShortTime (4) """
    GeneralDate: DateFormat = ...
    LongDate: DateFormat = ...
    LongTime: DateFormat = ...
    ShortDate: DateFormat = ...
    ShortTime: DateFormat = ...
    value__ = ...


class DateInterval(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DateInterval, values: Day (4), DayOfYear (3), Hour (7), Minute (8), Month (2), Quarter (1), Second (9), Weekday (6), WeekOfYear (5), Year (0) """
    Day: DateInterval = ...
    DayOfYear: DateInterval = ...
    Hour: DateInterval = ...
    Minute: DateInterval = ...
    Month: DateInterval = ...
    Quarter: DateInterval = ...
    Second: DateInterval = ...
    value__ = ...
    Weekday: DateInterval = ...
    WeekOfYear: DateInterval = ...
    Year: DateInterval = ...


class DueDate(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DueDate, values: BegOfPeriod (1), EndOfPeriod (0) """
    BegOfPeriod: DueDate = ...
    EndOfPeriod: DueDate = ...
    value__ = ...


class ErrObject: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: ErrObject) -> str
        Set: Description(self: ErrObject) = value
        """
        ...

    @property
    def Erl(self) -> int:
        """ Get: Erl(self: ErrObject) -> int """
        ...

    @property
    def HelpContext(self) -> int:
        """
        Get: HelpContext(self: ErrObject) -> int
        Set: HelpContext(self: ErrObject) = value
        """
        ...

    @property
    def HelpFile(self) -> str:
        """
        Get: HelpFile(self: ErrObject) -> str
        Set: HelpFile(self: ErrObject) = value
        """
        ...

    @property
    def LastDllError(self) -> int:
        """ Get: LastDllError(self: ErrObject) -> int """
        ...

    @property
    def Number(self) -> int:
        """
        Get: Number(self: ErrObject) -> int
        Set: Number(self: ErrObject) = value
        """
        ...

    @property
    def Source(self) -> str:
        """
        Get: Source(self: ErrObject) -> str
        Set: Source(self: ErrObject) = value
        """
        ...


    def Clear(self): # -> 
        """ Clear(self: ErrObject) """
        ...

    def GetException(self) -> Exception:
        """ GetException(self: ErrObject) -> Exception """
        ...

    def Raise(self, Number:int, Source:object, Description:object, HelpFile:object, HelpContext:object): # -> 
        """ Raise(self: ErrObject, Number: int, Source: object, Description: object, HelpFile: object, HelpContext: object) """
        ...


class FileAttribute(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) FileAttribute, values: Archive (32), Directory (16), Hidden (2), Normal (0), ReadOnly (1), System (4), Volume (8) """
    Archive: FileAttribute = ...
    Directory: FileAttribute = ...
    Hidden: FileAttribute = ...
    Normal: FileAttribute = ...
    ReadOnly: FileAttribute = ...
    System: FileAttribute = ...
    value__ = ...
    Volume: FileAttribute = ...


class FileSystem: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ChDir(Path:str): # -> 
        """ ChDir(Path: str) """
        ...

    @staticmethod
    def ChDrive(Drive:str): # -> 
        """ ChDrive(Drive: str)ChDrive(Drive: Char) """
        ...

    @staticmethod
    def CurDir(Drive=None) -> str:
        """
        CurDir() -> str
        CurDir(Drive: Char) -> str
        """
        ...

    @staticmethod
    def Dir(PathName:str = ..., Attributes:FileAttribute = ...) -> str:
        """
        Dir() -> str
        Dir(PathName: str, Attributes: FileAttribute) -> str
        """
        ...

    @staticmethod
    def EOF(FileNumber:int) -> bool:
        """ EOF(FileNumber: int) -> bool """
        ...

    @staticmethod
    def FileAttr(FileNumber:int): # -> OpenMode
        """ FileAttr(FileNumber: int) -> OpenMode """
        ...

    @staticmethod
    def FileClose(FileNumbers:Array): # -> 
        """ FileClose(*FileNumbers: Array[int]) """
        ...

    @staticmethod
    def FileCopy(Source:str, Destination:str): # -> 
        """ FileCopy(Source: str, Destination: str) """
        ...

    @staticmethod
    def FileDateTime(PathName:str) -> DateTime:
        """ FileDateTime(PathName: str) -> DateTime """
        ...

    @staticmethod
    def FileGet(FileNumber:int, Value:str, RecordNumber:Int64, *__args:bool) -> str:
        """
        FileGet(FileNumber: int, Value: ValueType, RecordNumber: Int64) -> ValueType
        FileGet(FileNumber: int, Value: Array, RecordNumber: Int64, ArrayIsDynamic: bool, StringIsFixedLength: bool) -> Array
        FileGet(FileNumber: int, Value: bool, RecordNumber: Int64) -> bool
        FileGet(FileNumber: int, Value: Byte, RecordNumber: Int64) -> Byte
        FileGet(FileNumber: int, Value: Int16, RecordNumber: Int64) -> Int16
        FileGet(FileNumber: int, Value: int, RecordNumber: Int64) -> int
        FileGet(FileNumber: int, Value: Int64, RecordNumber: Int64) -> Int64
        FileGet(FileNumber: int, Value: Char, RecordNumber: Int64) -> Char
        FileGet(FileNumber: int, Value: Single, RecordNumber: Int64) -> Single
        FileGet(FileNumber: int, Value: float, RecordNumber: Int64) -> float
        FileGet(FileNumber: int, Value: Decimal, RecordNumber: Int64) -> Decimal
        FileGet(FileNumber: int, Value: str, RecordNumber: Int64, StringIsFixedLength: bool) -> str
        FileGet(FileNumber: int, Value: DateTime, RecordNumber: Int64) -> DateTime
        """
        ...

    @staticmethod
    def FileGetObject(FileNumber:int, Value:object, RecordNumber:Int64) -> object:
        """ FileGetObject(FileNumber: int, Value: object, RecordNumber: Int64) -> object """
        ...

    @staticmethod
    def FileLen(PathName:str) -> Int64:
        """ FileLen(PathName: str) -> Int64 """
        ...

    @staticmethod
    def FileOpen(FileNumber:int, FileName:str, Mode, Access, Share, RecordLength:int): # ->  # Not found arg types: {'Mode': 'OpenMode', 'Share': 'OpenShare', 'Access': 'OpenAccess'}
        """ FileOpen(FileNumber: int, FileName: str, Mode: OpenMode, Access: OpenAccess, Share: OpenShare, RecordLength: int) """
        ...

    @staticmethod
    def FilePut(FileNumber:int, Value:str, RecordNumber:Int64, *__args:bool): # -> 
        """ FilePut(FileNumber: object, Value: object, RecordNumber: object)FilePut(FileNumber: int, Value: ValueType, RecordNumber: Int64)FilePut(FileNumber: int, Value: Array, RecordNumber: Int64, ArrayIsDynamic: bool, StringIsFixedLength: bool)FilePut(FileNumber: int, Value: bool, RecordNumber: Int64)FilePut(FileNumber: int, Value: Byte, RecordNumber: Int64)FilePut(FileNumber: int, Value: Int16, RecordNumber: Int64)FilePut(FileNumber: int, Value: int, RecordNumber: Int64)FilePut(FileNumber: int, Value: Int64, RecordNumber: Int64)FilePut(FileNumber: int, Value: Char, RecordNumber: Int64)FilePut(FileNumber: int, Value: Single, RecordNumber: Int64)FilePut(FileNumber: int, Value: float, RecordNumber: Int64)FilePut(FileNumber: int, Value: Decimal, RecordNumber: Int64)FilePut(FileNumber: int, Value: str, RecordNumber: Int64, StringIsFixedLength: bool)FilePut(FileNumber: int, Value: DateTime, RecordNumber: Int64) """
        ...

    @staticmethod
    def FilePutObject(FileNumber:int, Value:object, RecordNumber:Int64): # -> 
        """ FilePutObject(FileNumber: int, Value: object, RecordNumber: Int64) """
        ...

    @staticmethod
    def FileWidth(FileNumber:int, RecordWidth:int): # -> 
        """ FileWidth(FileNumber: int, RecordWidth: int) """
        ...

    @staticmethod
    def FreeFile() -> int:
        """ FreeFile() -> int """
        ...

    @staticmethod
    def GetAttr(PathName:str) -> FileAttribute:
        """ GetAttr(PathName: str) -> FileAttribute """
        ...

    @staticmethod
    def Input(FileNumber:int, Value:object) -> object:
        """
        Input(FileNumber: int, Value: object) -> object
        Input(FileNumber: int, Value: bool) -> bool
        Input(FileNumber: int, Value: Byte) -> Byte
        Input(FileNumber: int, Value: Int16) -> Int16
        Input(FileNumber: int, Value: int) -> int
        Input(FileNumber: int, Value: Int64) -> Int64
        Input(FileNumber: int, Value: Char) -> Char
        Input(FileNumber: int, Value: Single) -> Single
        Input(FileNumber: int, Value: float) -> float
        Input(FileNumber: int, Value: Decimal) -> Decimal
        Input(FileNumber: int, Value: str) -> str
        Input(FileNumber: int, Value: DateTime) -> DateTime
        """
        ...

    @staticmethod
    def InputString(FileNumber:int, CharCount:int) -> str:
        """ InputString(FileNumber: int, CharCount: int) -> str """
        ...

    @staticmethod
    def Kill(PathName:str): # -> 
        """ Kill(PathName: str) """
        ...

    @staticmethod
    def LineInput(FileNumber:int) -> str:
        """ LineInput(FileNumber: int) -> str """
        ...

    @staticmethod
    def Loc(FileNumber:int) -> Int64:
        """ Loc(FileNumber: int) -> Int64 """
        ...

    @staticmethod
    def Lock(FileNumber:int, *__args:Int64): # -> 
        """ Lock(FileNumber: int)Lock(FileNumber: int, Record: Int64)Lock(FileNumber: int, FromRecord: Int64, ToRecord: Int64) """
        ...

    @staticmethod
    def LOF(FileNumber:int) -> Int64:
        """ LOF(FileNumber: int) -> Int64 """
        ...

    @staticmethod
    def MkDir(Path:str): # -> 
        """ MkDir(Path: str) """
        ...

    @staticmethod
    def Print(FileNumber:int, Output:Array): # -> 
        """ Print(FileNumber: int, *Output: Array[object]) """
        ...

    @staticmethod
    def PrintLine(FileNumber:int, Output:Array): # -> 
        """ PrintLine(FileNumber: int, *Output: Array[object]) """
        ...

    @staticmethod
    def Rename(OldPath:str, NewPath:str): # -> 
        """ Rename(OldPath: str, NewPath: str) """
        ...

    @staticmethod
    def Reset(): # -> 
        """ Reset() """
        ...

    @staticmethod
    def RmDir(Path:str): # -> 
        """ RmDir(Path: str) """
        ...

    @staticmethod
    def Seek(FileNumber:int, Position:Int64 = ...): # -> 
        """ Seek(FileNumber: int, Position: Int64)Seek(FileNumber: int) -> Int64 """
        ...

    @staticmethod
    def SetAttr(PathName:str, Attributes:FileAttribute): # -> 
        """ SetAttr(PathName: str, Attributes: FileAttribute) """
        ...

    @staticmethod
    def SPC(Count:Int16): # -> SpcInfo
        """ SPC(Count: Int16) -> SpcInfo """
        ...

    @staticmethod
    def TAB(Column=None): # -> TabInfo
        """
        TAB() -> TabInfo
        TAB(Column: Int16) -> TabInfo
        """
        ...

    @staticmethod
    def Unlock(FileNumber:int, *__args:Int64): # -> 
        """ Unlock(FileNumber: int)Unlock(FileNumber: int, Record: Int64)Unlock(FileNumber: int, FromRecord: Int64, ToRecord: Int64) """
        ...

    @staticmethod
    def Write(FileNumber:int, Output:Array): # -> 
        """ Write(FileNumber: int, *Output: Array[object]) """
        ...

    @staticmethod
    def WriteLine(FileNumber:int, Output:Array): # -> 
        """ WriteLine(FileNumber: int, *Output: Array[object]) """
        ...


class Financial: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def DDB(Cost:float, Salvage:float, Life:float, Period:float, Factor:float) -> float:
        """ DDB(Cost: float, Salvage: float, Life: float, Period: float, Factor: float) -> float """
        ...

    @staticmethod
    def FV(Rate:float, NPer:float, Pmt:float, PV:float, Due:DueDate) -> float:
        """ FV(Rate: float, NPer: float, Pmt: float, PV: float, Due: DueDate) -> float """
        ...

    @staticmethod
    def IPmt(Rate:float, Per:float, NPer:float, PV:float, FV:float, Due:DueDate) -> float:
        """ IPmt(Rate: float, Per: float, NPer: float, PV: float, FV: float, Due: DueDate) -> float """
        ...

    @staticmethod
    def IRR(ValueArray:Array, Guess:float) -> Tuple_[float, Array]:
        """ IRR(ValueArray: Array[float], Guess: float) -> (float, Array[float]) """
        ...

    @staticmethod
    def MIRR(ValueArray:Array, FinanceRate:float, ReinvestRate:float) -> Tuple_[float, Array]:
        """ MIRR(ValueArray: Array[float], FinanceRate: float, ReinvestRate: float) -> (float, Array[float]) """
        ...

    @staticmethod
    def NPer(Rate:float, Pmt:float, PV:float, FV:float, Due:DueDate) -> float:
        """ NPer(Rate: float, Pmt: float, PV: float, FV: float, Due: DueDate) -> float """
        ...

    @staticmethod
    def NPV(Rate:float, ValueArray:Array) -> Tuple_[float, Array]:
        """ NPV(Rate: float, ValueArray: Array[float]) -> (float, Array[float]) """
        ...

    @staticmethod
    def Pmt(Rate:float, NPer:float, PV:float, FV:float, Due:DueDate) -> float:
        """ Pmt(Rate: float, NPer: float, PV: float, FV: float, Due: DueDate) -> float """
        ...

    @staticmethod
    def PPmt(Rate:float, Per:float, NPer:float, PV:float, FV:float, Due:DueDate) -> float:
        """ PPmt(Rate: float, Per: float, NPer: float, PV: float, FV: float, Due: DueDate) -> float """
        ...

    @staticmethod
    def PV(Rate:float, NPer:float, Pmt:float, FV:float, Due:DueDate) -> float:
        """ PV(Rate: float, NPer: float, Pmt: float, FV: float, Due: DueDate) -> float """
        ...

    @staticmethod
    def Rate(NPer:float, Pmt:float, PV:float, FV:float, Due:DueDate, Guess:float) -> float:
        """ Rate(NPer: float, Pmt: float, PV: float, FV: float, Due: DueDate, Guess: float) -> float """
        ...

    @staticmethod
    def SLN(Cost:float, Salvage:float, Life:float) -> float:
        """ SLN(Cost: float, Salvage: float, Life: float) -> float """
        ...

    @staticmethod
    def SYD(Cost:float, Salvage:float, Life:float, Period:float) -> float:
        """ SYD(Cost: float, Salvage: float, Life: float, Period: float) -> float """
        ...


class FirstDayOfWeek(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FirstDayOfWeek, values: Friday (6), Monday (2), Saturday (7), Sunday (1), System (0), Thursday (5), Tuesday (3), Wednesday (4) """
    Friday: FirstDayOfWeek = ...
    Monday: FirstDayOfWeek = ...
    Saturday: FirstDayOfWeek = ...
    Sunday: FirstDayOfWeek = ...
    System: FirstDayOfWeek = ...
    Thursday: FirstDayOfWeek = ...
    Tuesday: FirstDayOfWeek = ...
    value__ = ...
    Wednesday: FirstDayOfWeek = ...


class FirstWeekOfYear(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FirstWeekOfYear, values: FirstFourDays (2), FirstFullWeek (3), Jan1 (1), System (0) """
    FirstFourDays: FirstWeekOfYear = ...
    FirstFullWeek: FirstWeekOfYear = ...
    Jan1: FirstWeekOfYear = ...
    System: FirstWeekOfYear = ...
    value__ = ...


class Globals: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ScriptEngine(self) -> str:
        """ Get: ScriptEngine() -> str """
        ...

    @property
    def ScriptEngineBuildVersion(self) -> int:
        """ Get: ScriptEngineBuildVersion() -> int """
        ...

    @property
    def ScriptEngineMajorVersion(self) -> int:
        """ Get: ScriptEngineMajorVersion() -> int """
        ...

    @property
    def ScriptEngineMinorVersion(self) -> int:
        """ Get: ScriptEngineMinorVersion() -> int """
        ...




class HideModuleNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ HideModuleNameAttribute() """
    pass

class Information: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Erl() -> int:
        """ Erl() -> int """
        ...

    @staticmethod
    def Err() -> ErrObject:
        """ Err() -> ErrObject """
        ...

    @staticmethod
    def IsArray(VarName:object) -> bool:
        """ IsArray(VarName: object) -> bool """
        ...

    @staticmethod
    def IsDate(Expression:object) -> bool:
        """ IsDate(Expression: object) -> bool """
        ...

    @staticmethod
    def IsDBNull(Expression:object) -> bool:
        """ IsDBNull(Expression: object) -> bool """
        ...

    @staticmethod
    def IsError(Expression:object) -> bool:
        """ IsError(Expression: object) -> bool """
        ...

    @staticmethod
    def IsNothing(Expression:object) -> bool:
        """ IsNothing(Expression: object) -> bool """
        ...

    @staticmethod
    def IsNumeric(Expression:object) -> bool:
        """ IsNumeric(Expression: object) -> bool """
        ...

    @staticmethod
    def IsReference(Expression:object) -> bool:
        """ IsReference(Expression: object) -> bool """
        ...

    @staticmethod
    def LBound(Array:Array, Rank:int) -> int:
        """ LBound(Array: Array, Rank: int) -> int """
        ...

    @staticmethod
    def QBColor(Color:int) -> int:
        """ QBColor(Color: int) -> int """
        ...

    @staticmethod
    def RGB(Red:int, Green:int, Blue:int) -> int:
        """ RGB(Red: int, Green: int, Blue: int) -> int """
        ...

    @staticmethod
    def SystemTypeName(VbName:str) -> str:
        """ SystemTypeName(VbName: str) -> str """
        ...

    @staticmethod
    def TypeName(VarName:object) -> str:
        """ TypeName(VarName: object) -> str """
        ...

    @staticmethod
    def UBound(Array:Array, Rank:int) -> int:
        """ UBound(Array: Array, Rank: int) -> int """
        ...

    @staticmethod
    def VarType(VarName:object): # -> VariantType
        """ VarType(VarName: object) -> VariantType """
        ...

    @staticmethod
    def VbTypeName(UrtName:str) -> str:
        """ VbTypeName(UrtName: str) -> str """
        ...


class Interaction: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AppActivate(*__args:int): # -> 
        """ AppActivate(ProcessId: int)AppActivate(Title: str) """
        ...

    @staticmethod
    def Beep(): # -> 
        """ Beep() """
        ...

    @staticmethod
    def CallByName(ObjectRef:object, ProcName:str, UseCallType:CallType, Args:Array) -> object:
        """ CallByName(ObjectRef: object, ProcName: str, UseCallType: CallType, *Args: Array[object]) -> object """
        ...

    @staticmethod
    def Choose(Index:float, Choice:Array) -> object:
        """ Choose(Index: float, *Choice: Array[object]) -> object """
        ...

    @staticmethod
    def Command() -> str:
        """ Command() -> str """
        ...

    @staticmethod
    def CreateObject(ProgId:str, ServerName:str) -> object:
        """ CreateObject(ProgId: str, ServerName: str) -> object """
        ...

    @staticmethod
    def DeleteSetting(AppName:str, Section:str, Key:str): # -> 
        """ DeleteSetting(AppName: str, Section: str, Key: str) """
        ...

    @staticmethod
    def Environ(Expression:int) -> str:
        """
        Environ(Expression: int) -> str
        Environ(Expression: str) -> str
        """
        ...

    @staticmethod
    def GetAllSettings(AppName:str, Section:str) -> Array:
        """ GetAllSettings(AppName: str, Section: str) -> Array[str] """
        ...

    @staticmethod
    def GetObject(PathName:str, Class:str) -> object:
        """ GetObject(PathName: str, Class: str) -> object """
        ...

    @staticmethod
    def GetSetting(AppName:str, Section:str, Key:str, Default:str) -> str:
        """ GetSetting(AppName: str, Section: str, Key: str, Default: str) -> str """
        ...

    @staticmethod
    def IIf(Expression:bool, TruePart:object, FalsePart:object) -> object:
        """ IIf(Expression: bool, TruePart: object, FalsePart: object) -> object """
        ...

    @staticmethod
    def InputBox(Prompt:str, Title:str, DefaultResponse:str, XPos:int, YPos:int) -> str:
        """ InputBox(Prompt: str, Title: str, DefaultResponse: str, XPos: int, YPos: int) -> str """
        ...

    @staticmethod
    def MsgBox(Prompt:object, Buttons, Title:object): # -> MsgBoxResult # Not found arg types: {'Buttons': 'MsgBoxStyle'}
        """ MsgBox(Prompt: object, Buttons: MsgBoxStyle, Title: object) -> MsgBoxResult """
        ...

    @staticmethod
    def Partition(Number:Int64, Start:Int64, Stop:Int64, Interval:Int64) -> str:
        """ Partition(Number: Int64, Start: Int64, Stop: Int64, Interval: Int64) -> str """
        ...

    @staticmethod
    def SaveSetting(AppName:str, Section:str, Key:str, Setting:str): # -> 
        """ SaveSetting(AppName: str, Section: str, Key: str, Setting: str) """
        ...

    @staticmethod
    def Shell(PathName:str, Style:AppWinStyle, Wait:bool, Timeout:int) -> int:
        """ Shell(PathName: str, Style: AppWinStyle, Wait: bool, Timeout: int) -> int """
        ...

    @staticmethod
    def Switch(VarExpr:Array) -> object:
        """ Switch(*VarExpr: Array[object]) -> object """
        ...


class MsgBoxResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MsgBoxResult, values: Abort (3), Cancel (2), Ignore (5), No (7), Ok (1), Retry (4), Yes (6) """
    Abort: MsgBoxResult = ...
    Cancel: MsgBoxResult = ...
    Ignore: MsgBoxResult = ...
    No: MsgBoxResult = ...
    Ok: MsgBoxResult = ...
    Retry: MsgBoxResult = ...
    value__ = ...
    Yes: MsgBoxResult = ...


class MsgBoxStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) MsgBoxStyle, values: AbortRetryIgnore (2), ApplicationModal (0), Critical (16), DefaultButton1 (0), DefaultButton2 (256), DefaultButton3 (512), Exclamation (48), Information (64), MsgBoxHelp (16384), MsgBoxRight (524288), MsgBoxRtlReading (1048576), MsgBoxSetForeground (65536), OkCancel (1), OkOnly (0), Question (32), RetryCancel (5), SystemModal (4096), YesNo (4), YesNoCancel (3) """
    AbortRetryIgnore: MsgBoxStyle = ...
    ApplicationModal: MsgBoxStyle = ...
    Critical: MsgBoxStyle = ...
    DefaultButton1: MsgBoxStyle = ...
    DefaultButton2: MsgBoxStyle = ...
    DefaultButton3: MsgBoxStyle = ...
    Exclamation: MsgBoxStyle = ...
    Information: MsgBoxStyle = ...
    MsgBoxHelp: MsgBoxStyle = ...
    MsgBoxRight: MsgBoxStyle = ...
    MsgBoxRtlReading: MsgBoxStyle = ...
    MsgBoxSetForeground: MsgBoxStyle = ...
    OkCancel: MsgBoxStyle = ...
    OkOnly: MsgBoxStyle = ...
    Question: MsgBoxStyle = ...
    RetryCancel: MsgBoxStyle = ...
    SystemModal: MsgBoxStyle = ...
    value__ = ...
    YesNo: MsgBoxStyle = ...
    YesNoCancel: MsgBoxStyle = ...


class MyGroupCollectionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MyGroupCollectionAttribute(typeToCollect: str, createInstanceMethodName: str, disposeInstanceMethodName: str, defaultInstanceAlias: str) """
    @property
    def CreateMethod(self) -> str:
        """ Get: CreateMethod(self: MyGroupCollectionAttribute) -> str """
        ...

    @property
    def DefaultInstanceAlias(self) -> str:
        """ Get: DefaultInstanceAlias(self: MyGroupCollectionAttribute) -> str """
        ...

    @property
    def DisposeMethod(self) -> str:
        """ Get: DisposeMethod(self: MyGroupCollectionAttribute) -> str """
        ...

    @property
    def MyGroupName(self) -> str:
        """ Get: MyGroupName(self: MyGroupCollectionAttribute) -> str """
        ...


    def __new__(cls, typeToCollect:str, createInstanceMethodName:str, disposeInstanceMethodName:str, defaultInstanceAlias:str) -> Self:
        """ __new__(cls: type, typeToCollect: str, createInstanceMethodName: str, disposeInstanceMethodName: str, defaultInstanceAlias: str) """
        ...


class OpenAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OpenAccess, values: Default (-1), Read (1), ReadWrite (3), Write (2) """
    Default: OpenAccess = ...
    Read: OpenAccess = ...
    ReadWrite: OpenAccess = ...
    value__ = ...
    Write: OpenAccess = ...


class OpenMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OpenMode, values: Append (8), Binary (32), Input (1), Output (2), Random (4) """
    Append: OpenMode = ...
    Binary: OpenMode = ...
    Input: OpenMode = ...
    Output: OpenMode = ...
    Random: OpenMode = ...
    value__ = ...


class OpenShare(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OpenShare, values: Default (-1), LockRead (2), LockReadWrite (0), LockWrite (1), Shared (3) """
    Default: OpenShare = ...
    LockRead: OpenShare = ...
    LockReadWrite: OpenShare = ...
    LockWrite: OpenShare = ...
    Shared: OpenShare = ...
    value__ = ...


class SpcInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Count = ...


class Strings: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Asc(String:Char) -> int:
        """
        Asc(String: Char) -> int
        Asc(String: str) -> int
        """
        ...

    @staticmethod
    def AscW(String:Char) -> int:
        """
        AscW(String: Char) -> int
        AscW(String: str) -> int
        """
        ...

    @staticmethod
    def Chr(CharCode:int) -> Char:
        """ Chr(CharCode: int) -> Char """
        ...

    @staticmethod
    def ChrW(CharCode:int) -> Char:
        """ ChrW(CharCode: int) -> Char """
        ...

    @staticmethod
    def Filter(Source:Array, Match:str, Include:bool, Compare:CompareMethod) -> Array:
        """
        Filter(Source: Array[object], Match: str, Include: bool, Compare: CompareMethod) -> Array[str]
        Filter(Source: Array[str], Match: str, Include: bool, Compare: CompareMethod) -> Array[str]
        """
        ...

    @staticmethod
    def Format(Expression:object, Style:str) -> str:
        """ Format(Expression: object, Style: str) -> str """
        ...

    @staticmethod
    def FormatCurrency(Expression:object, NumDigitsAfterDecimal:int, IncludeLeadingDigit, UseParensForNegativeNumbers, GroupDigits) -> str: # Not found arg types: {'UseParensForNegativeNumbers': 'TriState', 'GroupDigits': 'TriState', 'IncludeLeadingDigit': 'TriState'}
        """ FormatCurrency(Expression: object, NumDigitsAfterDecimal: int, IncludeLeadingDigit: TriState, UseParensForNegativeNumbers: TriState, GroupDigits: TriState) -> str """
        ...

    @staticmethod
    def FormatDateTime(Expression:DateTime, NamedFormat:DateFormat) -> str:
        """ FormatDateTime(Expression: DateTime, NamedFormat: DateFormat) -> str """
        ...

    @staticmethod
    def FormatNumber(Expression:object, NumDigitsAfterDecimal:int, IncludeLeadingDigit, UseParensForNegativeNumbers, GroupDigits) -> str: # Not found arg types: {'UseParensForNegativeNumbers': 'TriState', 'GroupDigits': 'TriState', 'IncludeLeadingDigit': 'TriState'}
        """ FormatNumber(Expression: object, NumDigitsAfterDecimal: int, IncludeLeadingDigit: TriState, UseParensForNegativeNumbers: TriState, GroupDigits: TriState) -> str """
        ...

    @staticmethod
    def FormatPercent(Expression:object, NumDigitsAfterDecimal:int, IncludeLeadingDigit, UseParensForNegativeNumbers, GroupDigits) -> str: # Not found arg types: {'UseParensForNegativeNumbers': 'TriState', 'GroupDigits': 'TriState', 'IncludeLeadingDigit': 'TriState'}
        """ FormatPercent(Expression: object, NumDigitsAfterDecimal: int, IncludeLeadingDigit: TriState, UseParensForNegativeNumbers: TriState, GroupDigits: TriState) -> str """
        ...

    @staticmethod
    def GetChar(str:str, Index:int) -> Char:
        """ GetChar(str: str, Index: int) -> Char """
        ...

    @staticmethod
    def InStr(*__args) -> int:
        """
        InStr(String1: str, String2: str, Compare: CompareMethod) -> int
        InStr(Start: int, String1: str, String2: str, Compare: CompareMethod) -> int
        """
        ...

    @staticmethod
    def InStrRev(StringCheck:str, StringMatch:str, Start:int, Compare:CompareMethod) -> int:
        """ InStrRev(StringCheck: str, StringMatch: str, Start: int, Compare: CompareMethod) -> int """
        ...

    @staticmethod
    def Join(SourceArray:Array, Delimiter:str) -> str:
        """
        Join(SourceArray: Array[str], Delimiter: str) -> str
        Join(SourceArray: Array[object], Delimiter: str) -> str
        """
        ...

    @staticmethod
    def LCase(Value:str) -> str:
        """
        LCase(Value: str) -> str
        LCase(Value: Char) -> Char
        """
        ...

    @staticmethod
    def Left(str:str, Length:int) -> str:
        """ Left(str: str, Length: int) -> str """
        ...

    @staticmethod
    def Len(Expression:bool) -> int:
        """
        Len(Expression: bool) -> int
        Len(Expression: SByte) -> int
        Len(Expression: Byte) -> int
        Len(Expression: Int16) -> int
        Len(Expression: UInt16) -> int
        Len(Expression: int) -> int
        Len(Expression: UInt32) -> int
        Len(Expression: Int64) -> int
        Len(Expression: UInt64) -> int
        Len(Expression: Decimal) -> int
        Len(Expression: Single) -> int
        Len(Expression: float) -> int
        Len(Expression: DateTime) -> int
        Len(Expression: Char) -> int
        Len(Expression: str) -> int
        Len(Expression: object) -> int
        """
        ...

    @staticmethod
    def LSet(Source:str, Length:int) -> str:
        """ LSet(Source: str, Length: int) -> str """
        ...

    @staticmethod
    def LTrim(str:str) -> str:
        """ LTrim(str: str) -> str """
        ...

    @staticmethod
    def Mid(str:str, Start:int, Length:int = ...) -> str:
        """
        Mid(str: str, Start: int) -> str
        Mid(str: str, Start: int, Length: int) -> str
        """
        ...

    @staticmethod
    def Replace(Expression:str, Find:str, Replacement:str, Start:int, Count:int, Compare:CompareMethod) -> str:
        """ Replace(Expression: str, Find: str, Replacement: str, Start: int, Count: int, Compare: CompareMethod) -> str """
        ...

    @staticmethod
    def Right(str:str, Length:int) -> str:
        """ Right(str: str, Length: int) -> str """
        ...

    @staticmethod
    def RSet(Source:str, Length:int) -> str:
        """ RSet(Source: str, Length: int) -> str """
        ...

    @staticmethod
    def RTrim(str:str) -> str:
        """ RTrim(str: str) -> str """
        ...

    @staticmethod
    def Space(Number:int) -> str:
        """ Space(Number: int) -> str """
        ...

    @staticmethod
    def Split(Expression:str, Delimiter:str, Limit:int, Compare:CompareMethod) -> Array:
        """ Split(Expression: str, Delimiter: str, Limit: int, Compare: CompareMethod) -> Array[str] """
        ...

    @staticmethod
    def StrComp(String1:str, String2:str, Compare:CompareMethod) -> int:
        """ StrComp(String1: str, String2: str, Compare: CompareMethod) -> int """
        ...

    @staticmethod
    def StrConv(str:str, Conversion, LocaleID:int) -> str: # Not found arg types: {'Conversion': 'VbStrConv'}
        """ StrConv(str: str, Conversion: VbStrConv, LocaleID: int) -> str """
        ...

    @staticmethod
    def StrDup(Number:int, Character:object) -> object:
        """
        StrDup(Number: int, Character: object) -> object
        StrDup(Number: int, Character: Char) -> str
        StrDup(Number: int, Character: str) -> str
        """
        ...

    @staticmethod
    def StrReverse(Expression:str) -> str:
        """ StrReverse(Expression: str) -> str """
        ...

    @staticmethod
    def Trim(str:str) -> str:
        """ Trim(str: str) -> str """
        ...

    @staticmethod
    def UCase(Value:str) -> str:
        """
        UCase(Value: str) -> str
        UCase(Value: Char) -> Char
        """
        ...


class TabInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Column = ...


class TriState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TriState, values: False (0), True (-1), UseDefault (-2) """
    UseDefault: TriState = ...
    value__ = ...


class VariantType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum VariantType, values: Array (8192), Boolean (11), Byte (17), Char (18), Currency (6), DataObject (13), Date (7), Decimal (14), Double (5), Empty (0), Error (10), Integer (3), Long (20), Null (1), Object (9), Short (2), Single (4), String (8), UserDefinedType (36), Variant (12) """
    Array: VariantType = ...
    Boolean: VariantType = ...
    Byte: VariantType = ...
    Char: VariantType = ...
    Currency: VariantType = ...
    DataObject: VariantType = ...
    Date: VariantType = ...
    Decimal: VariantType = ...
    Double: VariantType = ...
    Empty: VariantType = ...
    Error: VariantType = ...
    Integer: VariantType = ...
    Long: VariantType = ...
    Null: VariantType = ...
    Object: VariantType = ...
    Short: VariantType = ...
    Single: VariantType = ...
    String: VariantType = ...
    UserDefinedType: VariantType = ...
    value__ = ...
    Variant: VariantType = ...


class VBCodeProvider(CodeDomProvider): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    VBCodeProvider()
    VBCodeProvider(providerOptions: IDictionary[str, str])
    """
    def __new__(cls, providerOptions:IDictionary = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, providerOptions: IDictionary[str, str])
        """
        ...


class VBFixedArrayAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    VBFixedArrayAttribute(UpperBound1: int)
    VBFixedArrayAttribute(UpperBound1: int, UpperBound2: int)
    """
    @property
    def Bounds(self) -> Array:
        """ Get: Bounds(self: VBFixedArrayAttribute) -> Array[int] """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: VBFixedArrayAttribute) -> int """
        ...


    def __new__(cls, UpperBound1:int, UpperBound2:int = ...) -> Self:
        """
        __new__(cls: type, UpperBound1: int)
        __new__(cls: type, UpperBound1: int, UpperBound2: int)
        """
        ...


class VBFixedStringAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ VBFixedStringAttribute(Length: int) """
    @property
    def Length(self) -> int:
        """ Get: Length(self: VBFixedStringAttribute) -> int """
        ...


    def __new__(cls, Length:int) -> Self:
        """ __new__(cls: type, Length: int) """
        ...


class VBMath: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Randomize(Number=None): # -> 
        """ Randomize()Randomize(Number: float) """
        ...

    @staticmethod
    def Rnd(Number=None) -> Single:
        """
        Rnd() -> Single
        Rnd(Number: Single) -> Single
        """
        ...


class VbStrConv(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) VbStrConv, values: Hiragana (32), Katakana (16), LinguisticCasing (1024), Lowercase (2), Narrow (8), None (0), ProperCase (3), SimplifiedChinese (256), TraditionalChinese (512), Uppercase (1), Wide (4) """
    Hiragana: VbStrConv = ...
    Katakana: VbStrConv = ...
    LinguisticCasing: VbStrConv = ...
    Lowercase: VbStrConv = ...
    Narrow: VbStrConv = ...
    ProperCase: VbStrConv = ...
    SimplifiedChinese: VbStrConv = ...
    TraditionalChinese: VbStrConv = ...
    Uppercase: VbStrConv = ...
    value__ = ...
    Wide: VbStrConv = ...


# variables with complex values

