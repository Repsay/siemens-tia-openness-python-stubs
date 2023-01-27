# encoding: utf-8
# module System.Globalization calls itself Globalization
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, sysglobl, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (ArgumentException, Array, Char, DateTime, DayOfWeek, Enum, 
    Guid, ICloneable, IEquatable, IFormatProvider, Nullable, StringComparer, 
    TimeSpan)

from System.Collections import IEnumerator

from System.Runtime.Serialization import IDeserializationCallback

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class Calendar(ICloneable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AlgorithmType(self) -> CalendarAlgorithmType:
        """ Get: AlgorithmType(self: Calendar) -> CalendarAlgorithmType """
        ...

    @property
    def DaysInYearBeforeMinSupportedYear(self):
        ...

    @property
    def Eras(self) -> Array:
        """ Get: Eras(self: Calendar) -> Array[int] """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: Calendar) -> bool """
        ...

    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """ Get: MaxSupportedDateTime(self: Calendar) -> DateTime """
        ...

    @property
    def MinSupportedDateTime(self) -> DateTime:
        """ Get: MinSupportedDateTime(self: Calendar) -> DateTime """
        ...

    @property
    def TwoDigitYearMax(self) -> int:
        """
        Get: TwoDigitYearMax(self: Calendar) -> int
        Set: TwoDigitYearMax(self: Calendar) = value
        """
        ...


    def AddDays(self, time:DateTime, days:int) -> DateTime:
        """ AddDays(self: Calendar, time: DateTime, days: int) -> DateTime """
        ...

    def AddHours(self, time:DateTime, hours:int) -> DateTime:
        """ AddHours(self: Calendar, time: DateTime, hours: int) -> DateTime """
        ...

    def AddMilliseconds(self, time:DateTime, milliseconds:float) -> DateTime:
        """ AddMilliseconds(self: Calendar, time: DateTime, milliseconds: float) -> DateTime """
        ...

    def AddMinutes(self, time:DateTime, minutes:int) -> DateTime:
        """ AddMinutes(self: Calendar, time: DateTime, minutes: int) -> DateTime """
        ...

    def AddMonths(self, time:DateTime, months:int) -> DateTime:
        """ AddMonths(self: Calendar, time: DateTime, months: int) -> DateTime """
        ...

    def AddSeconds(self, time:DateTime, seconds:int) -> DateTime:
        """ AddSeconds(self: Calendar, time: DateTime, seconds: int) -> DateTime """
        ...

    def AddWeeks(self, time:DateTime, weeks:int) -> DateTime:
        """ AddWeeks(self: Calendar, time: DateTime, weeks: int) -> DateTime """
        ...

    def AddYears(self, time:DateTime, years:int) -> DateTime:
        """ AddYears(self: Calendar, time: DateTime, years: int) -> DateTime """
        ...

    def GetDayOfMonth(self, time:DateTime) -> int:
        """ GetDayOfMonth(self: Calendar, time: DateTime) -> int """
        ...

    def GetDayOfWeek(self, time:DateTime) -> DayOfWeek:
        """ GetDayOfWeek(self: Calendar, time: DateTime) -> DayOfWeek """
        ...

    def GetDayOfYear(self, time:DateTime) -> int:
        """ GetDayOfYear(self: Calendar, time: DateTime) -> int """
        ...

    def GetDaysInMonth(self, year:int, month:int, era:int = ...) -> int:
        """
        GetDaysInMonth(self: Calendar, year: int, month: int) -> int
        GetDaysInMonth(self: Calendar, year: int, month: int, era: int) -> int
        """
        ...

    def GetDaysInYear(self, year:int, era:int = ...) -> int:
        """
        GetDaysInYear(self: Calendar, year: int) -> int
        GetDaysInYear(self: Calendar, year: int, era: int) -> int
        """
        ...

    def GetEra(self, time:DateTime) -> int:
        """ GetEra(self: Calendar, time: DateTime) -> int """
        ...

    def GetHour(self, time:DateTime) -> int:
        """ GetHour(self: Calendar, time: DateTime) -> int """
        ...

    def GetLeapMonth(self, year:int, era:int = ...) -> int:
        """
        GetLeapMonth(self: Calendar, year: int) -> int
        GetLeapMonth(self: Calendar, year: int, era: int) -> int
        """
        ...

    def GetMilliseconds(self, time:DateTime) -> float:
        """ GetMilliseconds(self: Calendar, time: DateTime) -> float """
        ...

    def GetMinute(self, time:DateTime) -> int:
        """ GetMinute(self: Calendar, time: DateTime) -> int """
        ...

    def GetMonth(self, time:DateTime) -> int:
        """ GetMonth(self: Calendar, time: DateTime) -> int """
        ...

    def GetMonthsInYear(self, year:int, era:int = ...) -> int:
        """
        GetMonthsInYear(self: Calendar, year: int) -> int
        GetMonthsInYear(self: Calendar, year: int, era: int) -> int
        """
        ...

    def GetSecond(self, time:DateTime) -> int:
        """ GetSecond(self: Calendar, time: DateTime) -> int """
        ...

    def GetWeekOfYear(self, time:DateTime, rule:CalendarWeekRule, firstDayOfWeek:DayOfWeek) -> int:
        """ GetWeekOfYear(self: Calendar, time: DateTime, rule: CalendarWeekRule, firstDayOfWeek: DayOfWeek) -> int """
        ...

    def GetYear(self, time:DateTime) -> int:
        """ GetYear(self: Calendar, time: DateTime) -> int """
        ...

    def IsLeapDay(self, year:int, month:int, day:int, era:int = ...) -> bool:
        """
        IsLeapDay(self: Calendar, year: int, month: int, day: int) -> bool
        IsLeapDay(self: Calendar, year: int, month: int, day: int, era: int) -> bool
        """
        ...

    def IsLeapMonth(self, year:int, month:int, era:int = ...) -> bool:
        """
        IsLeapMonth(self: Calendar, year: int, month: int) -> bool
        IsLeapMonth(self: Calendar, year: int, month: int, era: int) -> bool
        """
        ...

    def IsLeapYear(self, year:int, era:int = ...) -> bool:
        """
        IsLeapYear(self: Calendar, year: int) -> bool
        IsLeapYear(self: Calendar, year: int, era: int) -> bool
        """
        ...

    @staticmethod
    def ReadOnly(calendar:Calendar) -> Calendar:
        """ ReadOnly(calendar: Calendar) -> Calendar """
        ...

    def ToDateTime(self, year:int, month:int, day:int, hour:int, minute:int, second:int, millisecond:int, era:int = ...) -> DateTime:
        """
        ToDateTime(self: Calendar, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int) -> DateTime
        ToDateTime(self: Calendar, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> DateTime
        """
        ...

    def ToFourDigitYear(self, year:int) -> int:
        """ ToFourDigitYear(self: Calendar, year: int) -> int """
        ...

    CurrentEra: int = ...


class CalendarAlgorithmType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CalendarAlgorithmType, values: LunarCalendar (2), LunisolarCalendar (3), SolarCalendar (1), Unknown (0) """
    LunarCalendar: CalendarAlgorithmType = ...
    LunisolarCalendar: CalendarAlgorithmType = ...
    SolarCalendar: CalendarAlgorithmType = ...
    Unknown: CalendarAlgorithmType = ...
    value__ = ...


class CalendarWeekRule(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CalendarWeekRule, values: FirstDay (0), FirstFourDayWeek (2), FirstFullWeek (1) """
    FirstDay: CalendarWeekRule = ...
    FirstFourDayWeek: CalendarWeekRule = ...
    FirstFullWeek: CalendarWeekRule = ...
    value__ = ...


class CharUnicodeInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetDecimalDigitValue(*__args:Char) -> int:
        """
        GetDecimalDigitValue(ch: Char) -> int
        GetDecimalDigitValue(s: str, index: int) -> int
        """
        ...

    @staticmethod
    def GetDigitValue(*__args:Char) -> int:
        """
        GetDigitValue(ch: Char) -> int
        GetDigitValue(s: str, index: int) -> int
        """
        ...

    @staticmethod
    def GetNumericValue(*__args:Char) -> float:
        """
        GetNumericValue(ch: Char) -> float
        GetNumericValue(s: str, index: int) -> float
        """
        ...

    @staticmethod
    def GetUnicodeCategory(*__args:Char) -> UnicodeCategory:
        """
        GetUnicodeCategory(ch: Char) -> UnicodeCategory
        GetUnicodeCategory(s: str, index: int) -> UnicodeCategory
        """
        ...

    __all__: list = ...


class EastAsianLunisolarCalendar(Calendar): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ no doc """
    def GetCelestialStem(self, sexagenaryYear:int) -> int:
        """ GetCelestialStem(self: EastAsianLunisolarCalendar, sexagenaryYear: int) -> int """
        ...

    def GetSexagenaryYear(self, time:DateTime) -> int:
        """ GetSexagenaryYear(self: EastAsianLunisolarCalendar, time: DateTime) -> int """
        ...

    def GetTerrestrialBranch(self, sexagenaryYear:int) -> int:
        """ GetTerrestrialBranch(self: EastAsianLunisolarCalendar, sexagenaryYear: int) -> int """
        ...


class ChineseLunisolarCalendar(EastAsianLunisolarCalendar): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ ChineseLunisolarCalendar() """
    @property
    def Eras(self) -> Array:
        """ Get: Eras(self: ChineseLunisolarCalendar) -> Array[int] """
        ...

    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """ Get: MaxSupportedDateTime(self: ChineseLunisolarCalendar) -> DateTime """
        ...

    @property
    def MinSupportedDateTime(self) -> DateTime:
        """ Get: MinSupportedDateTime(self: ChineseLunisolarCalendar) -> DateTime """
        ...


    def GetEra(self, time:DateTime) -> int:
        """ GetEra(self: ChineseLunisolarCalendar, time: DateTime) -> int """
        ...

    ChineseEra: int = ...


class CompareInfo(IDeserializationCallback): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LCID(self) -> int:
        """ Get: LCID(self: CompareInfo) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: CompareInfo) -> str """
        ...

    @property
    def Version(self) -> SortVersion:
        """ Get: Version(self: CompareInfo) -> SortVersion """
        ...


    def Compare(self, string1:str, *__args:str) -> int:
        """
        Compare(self: CompareInfo, string1: str, string2: str, options: CompareOptions) -> int
        Compare(self: CompareInfo, string1: str, offset1: int, length1: int, string2: str, offset2: int, length2: int, options: CompareOptions) -> int
        Compare(self: CompareInfo, string1: str, string2: str) -> int
        Compare(self: CompareInfo, string1: str, offset1: int, length1: int, string2: str, offset2: int, length2: int) -> int
        Compare(self: CompareInfo, string1: str, offset1: int, string2: str, offset2: int, options: CompareOptions) -> int
        Compare(self: CompareInfo, string1: str, offset1: int, string2: str, offset2: int) -> int
        """
        ...

    def Equals(self, value:object) -> bool:
        """ Equals(self: CompareInfo, value: object) -> bool """
        ...

    @staticmethod
    def GetCompareInfo(*__args:int) -> CompareInfo:
        """
        GetCompareInfo(culture: int, assembly: Assembly) -> CompareInfo
        GetCompareInfo(culture: int) -> CompareInfo
        GetCompareInfo(name: str) -> CompareInfo
        GetCompareInfo(name: str, assembly: Assembly) -> CompareInfo
        """
        ...

    def GetHashCode(self, source:str = ..., options:CompareOptions = ...) -> int:
        """
        GetHashCode(self: CompareInfo) -> int
        GetHashCode(self: CompareInfo, source: str, options: CompareOptions) -> int
        """
        ...

    def GetSortKey(self, source:str, options:CompareOptions = ...) -> SortKey:
        """
        GetSortKey(self: CompareInfo, source: str, options: CompareOptions) -> SortKey
        GetSortKey(self: CompareInfo, source: str) -> SortKey
        """
        ...

    def IndexOf(self, source:str, value:Char, *__args:CompareOptions) -> int:
        """
        IndexOf(self: CompareInfo, source: str, value: Char) -> int
        IndexOf(self: CompareInfo, source: str, value: str) -> int
        IndexOf(self: CompareInfo, source: str, value: Char, options: CompareOptions) -> int
        IndexOf(self: CompareInfo, source: str, value: str, options: CompareOptions) -> int
        IndexOf(self: CompareInfo, source: str, value: Char, startIndex: int) -> int
        IndexOf(self: CompareInfo, source: str, value: str, startIndex: int) -> int
        IndexOf(self: CompareInfo, source: str, value: Char, startIndex: int, options: CompareOptions) -> int
        IndexOf(self: CompareInfo, source: str, value: str, startIndex: int, options: CompareOptions) -> int
        IndexOf(self: CompareInfo, source: str, value: Char, startIndex: int, count: int) -> int
        IndexOf(self: CompareInfo, source: str, value: str, startIndex: int, count: int) -> int
        IndexOf(self: CompareInfo, source: str, value: Char, startIndex: int, count: int, options: CompareOptions) -> int
        IndexOf(self: CompareInfo, source: str, value: str, startIndex: int, count: int, options: CompareOptions) -> int
        """
        ...

    def IsPrefix(self, source:str, prefix:str, options:CompareOptions = ...) -> bool:
        """
        IsPrefix(self: CompareInfo, source: str, prefix: str, options: CompareOptions) -> bool
        IsPrefix(self: CompareInfo, source: str, prefix: str) -> bool
        """
        ...

    @staticmethod
    def IsSortable(*__args:Char) -> bool:
        """
        IsSortable(ch: Char) -> bool
        IsSortable(text: str) -> bool
        """
        ...

    def IsSuffix(self, source:str, suffix:str, options:CompareOptions = ...) -> bool:
        """
        IsSuffix(self: CompareInfo, source: str, suffix: str, options: CompareOptions) -> bool
        IsSuffix(self: CompareInfo, source: str, suffix: str) -> bool
        """
        ...

    def LastIndexOf(self, source:str, value:Char, *__args:CompareOptions) -> int:
        """
        LastIndexOf(self: CompareInfo, source: str, value: Char) -> int
        LastIndexOf(self: CompareInfo, source: str, value: str) -> int
        LastIndexOf(self: CompareInfo, source: str, value: Char, options: CompareOptions) -> int
        LastIndexOf(self: CompareInfo, source: str, value: str, options: CompareOptions) -> int
        LastIndexOf(self: CompareInfo, source: str, value: Char, startIndex: int) -> int
        LastIndexOf(self: CompareInfo, source: str, value: str, startIndex: int) -> int
        LastIndexOf(self: CompareInfo, source: str, value: Char, startIndex: int, options: CompareOptions) -> int
        LastIndexOf(self: CompareInfo, source: str, value: str, startIndex: int, options: CompareOptions) -> int
        LastIndexOf(self: CompareInfo, source: str, value: Char, startIndex: int, count: int) -> int
        LastIndexOf(self: CompareInfo, source: str, value: str, startIndex: int, count: int) -> int
        LastIndexOf(self: CompareInfo, source: str, value: Char, startIndex: int, count: int, options: CompareOptions) -> int
        LastIndexOf(self: CompareInfo, source: str, value: str, startIndex: int, count: int, options: CompareOptions) -> int
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: CompareInfo) -> str """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y)x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CompareOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CompareOptions, values: IgnoreCase (1), IgnoreKanaType (8), IgnoreNonSpace (2), IgnoreSymbols (4), IgnoreWidth (16), None (0), Ordinal (1073741824), OrdinalIgnoreCase (268435456), StringSort (536870912) """
    IgnoreCase: CompareOptions = ...
    IgnoreKanaType: CompareOptions = ...
    IgnoreNonSpace: CompareOptions = ...
    IgnoreSymbols: CompareOptions = ...
    IgnoreWidth: CompareOptions = ...
    Ordinal: CompareOptions = ...
    OrdinalIgnoreCase: CompareOptions = ...
    StringSort: CompareOptions = ...
    value__ = ...


class CultureAndRegionInfoBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ CultureAndRegionInfoBuilder(cultureName: str, flags: CultureAndRegionModifiers) """
    @property
    def AvailableCalendars(self) -> Array:
        """
        Get: AvailableCalendars(self: CultureAndRegionInfoBuilder) -> Array[Calendar]
        Set: AvailableCalendars(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def CompareInfo(self) -> CompareInfo:
        """
        Get: CompareInfo(self: CultureAndRegionInfoBuilder) -> CompareInfo
        Set: CompareInfo(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def ConsoleFallbackUICulture(self) -> CultureInfo:
        """
        Get: ConsoleFallbackUICulture(self: CultureAndRegionInfoBuilder) -> CultureInfo
        Set: ConsoleFallbackUICulture(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def CultureEnglishName(self) -> str:
        """
        Get: CultureEnglishName(self: CultureAndRegionInfoBuilder) -> str
        Set: CultureEnglishName(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def CultureName(self) -> str:
        """ Get: CultureName(self: CultureAndRegionInfoBuilder) -> str """
        ...

    @property
    def CultureNativeName(self) -> str:
        """
        Get: CultureNativeName(self: CultureAndRegionInfoBuilder) -> str
        Set: CultureNativeName(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def CultureTypes(self) -> CultureTypes:
        """ Get: CultureTypes(self: CultureAndRegionInfoBuilder) -> CultureTypes """
        ...

    @property
    def CurrencyEnglishName(self) -> str:
        """
        Get: CurrencyEnglishName(self: CultureAndRegionInfoBuilder) -> str
        Set: CurrencyEnglishName(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def CurrencyNativeName(self) -> str:
        """
        Get: CurrencyNativeName(self: CultureAndRegionInfoBuilder) -> str
        Set: CurrencyNativeName(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def GeoId(self) -> int:
        """
        Get: GeoId(self: CultureAndRegionInfoBuilder) -> int
        Set: GeoId(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def GregorianDateTimeFormat(self) -> DateTimeFormatInfo:
        """
        Get: GregorianDateTimeFormat(self: CultureAndRegionInfoBuilder) -> DateTimeFormatInfo
        Set: GregorianDateTimeFormat(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def IetfLanguageTag(self) -> str:
        """
        Get: IetfLanguageTag(self: CultureAndRegionInfoBuilder) -> str
        Set: IetfLanguageTag(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def IsMetric(self) -> bool:
        """
        Get: IsMetric(self: CultureAndRegionInfoBuilder) -> bool
        Set: IsMetric(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def ISOCurrencySymbol(self) -> str:
        """
        Get: ISOCurrencySymbol(self: CultureAndRegionInfoBuilder) -> str
        Set: ISOCurrencySymbol(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def IsRightToLeft(self) -> bool:
        """
        Get: IsRightToLeft(self: CultureAndRegionInfoBuilder) -> bool
        Set: IsRightToLeft(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def KeyboardLayoutId(self) -> int:
        """
        Get: KeyboardLayoutId(self: CultureAndRegionInfoBuilder) -> int
        Set: KeyboardLayoutId(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def LCID(self) -> int:
        """ Get: LCID(self: CultureAndRegionInfoBuilder) -> int """
        ...

    @property
    def NumberFormat(self) -> NumberFormatInfo:
        """
        Get: NumberFormat(self: CultureAndRegionInfoBuilder) -> NumberFormatInfo
        Set: NumberFormat(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def Parent(self) -> CultureInfo:
        """
        Get: Parent(self: CultureAndRegionInfoBuilder) -> CultureInfo
        Set: Parent(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def RegionEnglishName(self) -> str:
        """
        Get: RegionEnglishName(self: CultureAndRegionInfoBuilder) -> str
        Set: RegionEnglishName(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def RegionName(self) -> str:
        """ Get: RegionName(self: CultureAndRegionInfoBuilder) -> str """
        ...

    @property
    def RegionNativeName(self) -> str:
        """
        Get: RegionNativeName(self: CultureAndRegionInfoBuilder) -> str
        Set: RegionNativeName(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def TextInfo(self) -> TextInfo:
        """
        Get: TextInfo(self: CultureAndRegionInfoBuilder) -> TextInfo
        Set: TextInfo(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def ThreeLetterISOLanguageName(self) -> str:
        """
        Get: ThreeLetterISOLanguageName(self: CultureAndRegionInfoBuilder) -> str
        Set: ThreeLetterISOLanguageName(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def ThreeLetterISORegionName(self) -> str:
        """
        Get: ThreeLetterISORegionName(self: CultureAndRegionInfoBuilder) -> str
        Set: ThreeLetterISORegionName(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def ThreeLetterWindowsLanguageName(self) -> str:
        """
        Get: ThreeLetterWindowsLanguageName(self: CultureAndRegionInfoBuilder) -> str
        Set: ThreeLetterWindowsLanguageName(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def ThreeLetterWindowsRegionName(self) -> str:
        """
        Get: ThreeLetterWindowsRegionName(self: CultureAndRegionInfoBuilder) -> str
        Set: ThreeLetterWindowsRegionName(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def TwoLetterISOLanguageName(self) -> str:
        """
        Get: TwoLetterISOLanguageName(self: CultureAndRegionInfoBuilder) -> str
        Set: TwoLetterISOLanguageName(self: CultureAndRegionInfoBuilder) = value
        """
        ...

    @property
    def TwoLetterISORegionName(self) -> str:
        """
        Get: TwoLetterISORegionName(self: CultureAndRegionInfoBuilder) -> str
        Set: TwoLetterISORegionName(self: CultureAndRegionInfoBuilder) = value
        """
        ...


    @staticmethod
    def CreateFromLdml(xmlFileName:str) -> CultureAndRegionInfoBuilder:
        """ CreateFromLdml(xmlFileName: str) -> CultureAndRegionInfoBuilder """
        ...

    def LoadDataFromCultureInfo(self, culture:CultureInfo): # -> 
        """ LoadDataFromCultureInfo(self: CultureAndRegionInfoBuilder, culture: CultureInfo) """
        ...

    def LoadDataFromRegionInfo(self, region:RegionInfo): # -> 
        """ LoadDataFromRegionInfo(self: CultureAndRegionInfoBuilder, region: RegionInfo) """
        ...

    def Register(self): # -> 
        """ Register(self: CultureAndRegionInfoBuilder) """
        ...

    def Save(self, filename:str): # -> 
        """ Save(self: CultureAndRegionInfoBuilder, filename: str) """
        ...

    @staticmethod
    def Unregister(cultureName:str): # -> 
        """ Unregister(cultureName: str) """
        ...


class CultureAndRegionModifiers(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CultureAndRegionModifiers, values: Neutral (1), None (0), Replacement (2) """
    Neutral: CultureAndRegionModifiers = ...
    Replacement: CultureAndRegionModifiers = ...
    value__ = ...


class CultureInfo(ICloneable, IFormatProvider): # skipped bases: <type 'object'>
    """
    CultureInfo(name: str)
    CultureInfo(name: str, useUserOverride: bool)
    CultureInfo(culture: int)
    CultureInfo(culture: int, useUserOverride: bool)
    """
    @property
    def Calendar(self) -> Calendar:
        """ Get: Calendar(self: CultureInfo) -> Calendar """
        ...

    @property
    def CompareInfo(self) -> CompareInfo:
        """ Get: CompareInfo(self: CultureInfo) -> CompareInfo """
        ...

    @property
    def CultureTypes(self) -> CultureTypes:
        """ Get: CultureTypes(self: CultureInfo) -> CultureTypes """
        ...

    @property
    def CurrentCulture(self) -> CultureInfo:
        """
        Get: CurrentCulture() -> CultureInfo
        Set: CurrentCulture() = value
        """
        ...

    @property
    def CurrentUICulture(self) -> CultureInfo:
        """
        Get: CurrentUICulture() -> CultureInfo
        Set: CurrentUICulture() = value
        """
        ...

    @property
    def DateTimeFormat(self) -> DateTimeFormatInfo:
        """
        Get: DateTimeFormat(self: CultureInfo) -> DateTimeFormatInfo
        Set: DateTimeFormat(self: CultureInfo) = value
        """
        ...

    @property
    def DefaultThreadCurrentCulture(self) -> CultureInfo:
        """
        Get: DefaultThreadCurrentCulture() -> CultureInfo
        Set: DefaultThreadCurrentCulture() = value
        """
        ...

    @property
    def DefaultThreadCurrentUICulture(self) -> CultureInfo:
        """
        Get: DefaultThreadCurrentUICulture() -> CultureInfo
        Set: DefaultThreadCurrentUICulture() = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: CultureInfo) -> str """
        ...

    @property
    def EnglishName(self) -> str:
        """ Get: EnglishName(self: CultureInfo) -> str """
        ...

    @property
    def IetfLanguageTag(self) -> str:
        """ Get: IetfLanguageTag(self: CultureInfo) -> str """
        ...

    @property
    def InstalledUICulture(self) -> CultureInfo:
        """ Get: InstalledUICulture() -> CultureInfo """
        ...

    @property
    def InvariantCulture(self) -> CultureInfo:
        """ Get: InvariantCulture() -> CultureInfo """
        ...

    @property
    def IsNeutralCulture(self) -> bool:
        """ Get: IsNeutralCulture(self: CultureInfo) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: CultureInfo) -> bool """
        ...

    @property
    def KeyboardLayoutId(self) -> int:
        """ Get: KeyboardLayoutId(self: CultureInfo) -> int """
        ...

    @property
    def LCID(self) -> int:
        """ Get: LCID(self: CultureInfo) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: CultureInfo) -> str """
        ...

    @property
    def NativeName(self) -> str:
        """ Get: NativeName(self: CultureInfo) -> str """
        ...

    @property
    def NumberFormat(self) -> NumberFormatInfo:
        """
        Get: NumberFormat(self: CultureInfo) -> NumberFormatInfo
        Set: NumberFormat(self: CultureInfo) = value
        """
        ...

    @property
    def OptionalCalendars(self) -> Array:
        """ Get: OptionalCalendars(self: CultureInfo) -> Array[Calendar] """
        ...

    @property
    def Parent(self) -> CultureInfo:
        """ Get: Parent(self: CultureInfo) -> CultureInfo """
        ...

    @property
    def TextInfo(self) -> TextInfo:
        """ Get: TextInfo(self: CultureInfo) -> TextInfo """
        ...

    @property
    def ThreeLetterISOLanguageName(self) -> str:
        """ Get: ThreeLetterISOLanguageName(self: CultureInfo) -> str """
        ...

    @property
    def ThreeLetterWindowsLanguageName(self) -> str:
        """ Get: ThreeLetterWindowsLanguageName(self: CultureInfo) -> str """
        ...

    @property
    def TwoLetterISOLanguageName(self) -> str:
        """ Get: TwoLetterISOLanguageName(self: CultureInfo) -> str """
        ...

    @property
    def UseUserOverride(self) -> bool:
        """ Get: UseUserOverride(self: CultureInfo) -> bool """
        ...


    def ClearCachedData(self): # -> 
        """ ClearCachedData(self: CultureInfo) """
        ...

    @staticmethod
    def CreateSpecificCulture(name:str) -> CultureInfo:
        """ CreateSpecificCulture(name: str) -> CultureInfo """
        ...

    def Equals(self, value:object) -> bool:
        """ Equals(self: CultureInfo, value: object) -> bool """
        ...

    def GetConsoleFallbackUICulture(self) -> CultureInfo:
        """ GetConsoleFallbackUICulture(self: CultureInfo) -> CultureInfo """
        ...

    @staticmethod
    def GetCultureInfo(*__args:int) -> CultureInfo:
        """
        GetCultureInfo(culture: int) -> CultureInfo
        GetCultureInfo(name: str) -> CultureInfo
        GetCultureInfo(name: str, altName: str) -> CultureInfo
        """
        ...

    @staticmethod
    def GetCultureInfoByIetfLanguageTag(name:str) -> CultureInfo:
        """ GetCultureInfoByIetfLanguageTag(name: str) -> CultureInfo """
        ...

    @staticmethod
    def GetCultures(types:CultureTypes) -> Array:
        """ GetCultures(types: CultureTypes) -> Array[CultureInfo] """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CultureInfo) -> int """
        ...

    @staticmethod
    def ReadOnly(ci:CultureInfo) -> CultureInfo:
        """ ReadOnly(ci: CultureInfo) -> CultureInfo """
        ...

    def ToString(self) -> str:
        """ ToString(self: CultureInfo) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class CultureNotFoundException(ArgumentException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CultureNotFoundException()
    CultureNotFoundException(message: str)
    CultureNotFoundException(paramName: str, message: str)
    CultureNotFoundException(message: str, innerException: Exception)
    CultureNotFoundException(paramName: str, invalidCultureId: int, message: str)
    CultureNotFoundException(message: str, invalidCultureId: int, innerException: Exception)
    CultureNotFoundException(paramName: str, invalidCultureName: str, message: str)
    CultureNotFoundException(message: str, invalidCultureName: str, innerException: Exception)
    """
    @property
    def InvalidCultureId(self) -> Nullable:
        """ Get: InvalidCultureId(self: CultureNotFoundException) -> Nullable[int] """
        ...

    @property
    def InvalidCultureName(self) -> str:
        """ Get: InvalidCultureName(self: CultureNotFoundException) -> str """
        ...


    SerializeObjectState = ...


class CultureTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CultureTypes, values: AllCultures (7), FrameworkCultures (64), InstalledWin32Cultures (4), NeutralCultures (1), ReplacementCultures (16), SpecificCultures (2), UserCustomCulture (8), WindowsOnlyCultures (32) """
    AllCultures: CultureTypes = ...
    FrameworkCultures: CultureTypes = ...
    InstalledWin32Cultures: CultureTypes = ...
    NeutralCultures: CultureTypes = ...
    ReplacementCultures: CultureTypes = ...
    SpecificCultures: CultureTypes = ...
    UserCustomCulture: CultureTypes = ...
    value__ = ...
    WindowsOnlyCultures: CultureTypes = ...


class DateTimeFormatInfo(ICloneable, IFormatProvider): # skipped bases: <type 'object'>
    """ DateTimeFormatInfo() """
    @property
    def AbbreviatedDayNames(self) -> Array:
        """
        Get: AbbreviatedDayNames(self: DateTimeFormatInfo) -> Array[str]
        Set: AbbreviatedDayNames(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def AbbreviatedMonthGenitiveNames(self) -> Array:
        """
        Get: AbbreviatedMonthGenitiveNames(self: DateTimeFormatInfo) -> Array[str]
        Set: AbbreviatedMonthGenitiveNames(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def AbbreviatedMonthNames(self) -> Array:
        """
        Get: AbbreviatedMonthNames(self: DateTimeFormatInfo) -> Array[str]
        Set: AbbreviatedMonthNames(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def AMDesignator(self) -> str:
        """
        Get: AMDesignator(self: DateTimeFormatInfo) -> str
        Set: AMDesignator(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def Calendar(self) -> Calendar:
        """
        Get: Calendar(self: DateTimeFormatInfo) -> Calendar
        Set: Calendar(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def CalendarWeekRule(self) -> CalendarWeekRule:
        """
        Get: CalendarWeekRule(self: DateTimeFormatInfo) -> CalendarWeekRule
        Set: CalendarWeekRule(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def CurrentInfo(self) -> DateTimeFormatInfo:
        """ Get: CurrentInfo() -> DateTimeFormatInfo """
        ...

    @property
    def DateSeparator(self) -> str:
        """
        Get: DateSeparator(self: DateTimeFormatInfo) -> str
        Set: DateSeparator(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def DayNames(self) -> Array:
        """
        Get: DayNames(self: DateTimeFormatInfo) -> Array[str]
        Set: DayNames(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def FirstDayOfWeek(self) -> DayOfWeek:
        """
        Get: FirstDayOfWeek(self: DateTimeFormatInfo) -> DayOfWeek
        Set: FirstDayOfWeek(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def FullDateTimePattern(self) -> str:
        """
        Get: FullDateTimePattern(self: DateTimeFormatInfo) -> str
        Set: FullDateTimePattern(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def InvariantInfo(self) -> DateTimeFormatInfo:
        """ Get: InvariantInfo() -> DateTimeFormatInfo """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: DateTimeFormatInfo) -> bool """
        ...

    @property
    def LongDatePattern(self) -> str:
        """
        Get: LongDatePattern(self: DateTimeFormatInfo) -> str
        Set: LongDatePattern(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def LongTimePattern(self) -> str:
        """
        Get: LongTimePattern(self: DateTimeFormatInfo) -> str
        Set: LongTimePattern(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def MonthDayPattern(self) -> str:
        """
        Get: MonthDayPattern(self: DateTimeFormatInfo) -> str
        Set: MonthDayPattern(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def MonthGenitiveNames(self) -> Array:
        """
        Get: MonthGenitiveNames(self: DateTimeFormatInfo) -> Array[str]
        Set: MonthGenitiveNames(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def MonthNames(self) -> Array:
        """
        Get: MonthNames(self: DateTimeFormatInfo) -> Array[str]
        Set: MonthNames(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def NativeCalendarName(self) -> str:
        """ Get: NativeCalendarName(self: DateTimeFormatInfo) -> str """
        ...

    @property
    def PMDesignator(self) -> str:
        """
        Get: PMDesignator(self: DateTimeFormatInfo) -> str
        Set: PMDesignator(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def RFC1123Pattern(self) -> str:
        """ Get: RFC1123Pattern(self: DateTimeFormatInfo) -> str """
        ...

    @property
    def ShortDatePattern(self) -> str:
        """
        Get: ShortDatePattern(self: DateTimeFormatInfo) -> str
        Set: ShortDatePattern(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def ShortestDayNames(self) -> Array:
        """
        Get: ShortestDayNames(self: DateTimeFormatInfo) -> Array[str]
        Set: ShortestDayNames(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def ShortTimePattern(self) -> str:
        """
        Get: ShortTimePattern(self: DateTimeFormatInfo) -> str
        Set: ShortTimePattern(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def SortableDateTimePattern(self) -> str:
        """ Get: SortableDateTimePattern(self: DateTimeFormatInfo) -> str """
        ...

    @property
    def TimeSeparator(self) -> str:
        """
        Get: TimeSeparator(self: DateTimeFormatInfo) -> str
        Set: TimeSeparator(self: DateTimeFormatInfo) = value
        """
        ...

    @property
    def UniversalSortableDateTimePattern(self) -> str:
        """ Get: UniversalSortableDateTimePattern(self: DateTimeFormatInfo) -> str """
        ...

    @property
    def YearMonthPattern(self) -> str:
        """
        Get: YearMonthPattern(self: DateTimeFormatInfo) -> str
        Set: YearMonthPattern(self: DateTimeFormatInfo) = value
        """
        ...


    def GetAbbreviatedDayName(self, dayofweek:DayOfWeek) -> str:
        """ GetAbbreviatedDayName(self: DateTimeFormatInfo, dayofweek: DayOfWeek) -> str """
        ...

    def GetAbbreviatedEraName(self, era:int) -> str:
        """ GetAbbreviatedEraName(self: DateTimeFormatInfo, era: int) -> str """
        ...

    def GetAbbreviatedMonthName(self, month:int) -> str:
        """ GetAbbreviatedMonthName(self: DateTimeFormatInfo, month: int) -> str """
        ...

    def GetAllDateTimePatterns(self, format:Char = ...) -> Array:
        """
        GetAllDateTimePatterns(self: DateTimeFormatInfo, format: Char) -> Array[str]
        GetAllDateTimePatterns(self: DateTimeFormatInfo) -> Array[str]
        """
        ...

    def GetDayName(self, dayofweek:DayOfWeek) -> str:
        """ GetDayName(self: DateTimeFormatInfo, dayofweek: DayOfWeek) -> str """
        ...

    def GetEra(self, eraName:str) -> int:
        """ GetEra(self: DateTimeFormatInfo, eraName: str) -> int """
        ...

    def GetEraName(self, era:int) -> str:
        """ GetEraName(self: DateTimeFormatInfo, era: int) -> str """
        ...

    @staticmethod
    def GetInstance(provider:IFormatProvider) -> DateTimeFormatInfo:
        """ GetInstance(provider: IFormatProvider) -> DateTimeFormatInfo """
        ...

    def GetMonthName(self, month:int) -> str:
        """ GetMonthName(self: DateTimeFormatInfo, month: int) -> str """
        ...

    def GetShortestDayName(self, dayOfWeek:DayOfWeek) -> str:
        """ GetShortestDayName(self: DateTimeFormatInfo, dayOfWeek: DayOfWeek) -> str """
        ...

    @staticmethod
    def ReadOnly(dtfi:DateTimeFormatInfo) -> DateTimeFormatInfo:
        """ ReadOnly(dtfi: DateTimeFormatInfo) -> DateTimeFormatInfo """
        ...

    def SetAllDateTimePatterns(self, patterns:Array, format:Char): # -> 
        """ SetAllDateTimePatterns(self: DateTimeFormatInfo, patterns: Array[str], format: Char) """
        ...



class DateTimeStyles(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DateTimeStyles, values: AdjustToUniversal (16), AllowInnerWhite (4), AllowLeadingWhite (1), AllowTrailingWhite (2), AllowWhiteSpaces (7), AssumeLocal (32), AssumeUniversal (64), NoCurrentDateDefault (8), None (0), RoundtripKind (128) """
    AdjustToUniversal: DateTimeStyles = ...
    AllowInnerWhite: DateTimeStyles = ...
    AllowLeadingWhite: DateTimeStyles = ...
    AllowTrailingWhite: DateTimeStyles = ...
    AllowWhiteSpaces: DateTimeStyles = ...
    AssumeLocal: DateTimeStyles = ...
    AssumeUniversal: DateTimeStyles = ...
    NoCurrentDateDefault: DateTimeStyles = ...
    RoundtripKind: DateTimeStyles = ...
    value__ = ...


class DaylightTime: # skipped bases: <type 'object'>, <type 'object'>
    """ DaylightTime(start: DateTime, end: DateTime, delta: TimeSpan) """
    @property
    def Delta(self) -> TimeSpan:
        """ Get: Delta(self: DaylightTime) -> TimeSpan """
        ...

    @property
    def End(self) -> DateTime:
        """ Get: End(self: DaylightTime) -> DateTime """
        ...

    @property
    def Start(self) -> DateTime:
        """ Get: Start(self: DaylightTime) -> DateTime """
        ...



class DigitShapes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DigitShapes, values: Context (0), NativeNational (2), None (1) """
    Context: DigitShapes = ...
    NativeNational: DigitShapes = ...
    value__ = ...


class GlobalizationExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetStringComparer(compareInfo:CompareInfo, options:CompareOptions) -> StringComparer:
        """ GetStringComparer(compareInfo: CompareInfo, options: CompareOptions) -> StringComparer """
        ...

    __all__: list = ...


class GregorianCalendar(Calendar): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    GregorianCalendar()
    GregorianCalendar(type: GregorianCalendarTypes)
    """
    @property
    def CalendarType(self) -> GregorianCalendarTypes:
        """
        Get: CalendarType(self: GregorianCalendar) -> GregorianCalendarTypes
        Set: CalendarType(self: GregorianCalendar) = value
        """
        ...


    def __new__(cls, type:GregorianCalendarTypes = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, type: GregorianCalendarTypes)
        """
        ...

    ADEra: int = ...


class GregorianCalendarTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GregorianCalendarTypes, values: Arabic (10), Localized (1), MiddleEastFrench (9), TransliteratedEnglish (11), TransliteratedFrench (12), USEnglish (2) """
    Arabic: GregorianCalendarTypes = ...
    Localized: GregorianCalendarTypes = ...
    MiddleEastFrench: GregorianCalendarTypes = ...
    TransliteratedEnglish: GregorianCalendarTypes = ...
    TransliteratedFrench: GregorianCalendarTypes = ...
    USEnglish: GregorianCalendarTypes = ...
    value__ = ...


class HebrewCalendar(Calendar): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ HebrewCalendar() """
    HebrewEra: int = ...


class HijriCalendar(Calendar): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ HijriCalendar() """
    @property
    def HijriAdjustment(self) -> int:
        """
        Get: HijriAdjustment(self: HijriCalendar) -> int
        Set: HijriAdjustment(self: HijriCalendar) = value
        """
        ...


    HijriEra: int = ...


class IdnMapping: # skipped bases: <type 'object'>, <type 'object'>
    """ IdnMapping() """
    @property
    def AllowUnassigned(self) -> bool:
        """
        Get: AllowUnassigned(self: IdnMapping) -> bool
        Set: AllowUnassigned(self: IdnMapping) = value
        """
        ...

    @property
    def UseStd3AsciiRules(self) -> bool:
        """
        Get: UseStd3AsciiRules(self: IdnMapping) -> bool
        Set: UseStd3AsciiRules(self: IdnMapping) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: IdnMapping, obj: object) -> bool """
        ...

    def GetAscii(self, unicode:str, index:int = ..., count:int = ...) -> str:
        """
        GetAscii(self: IdnMapping, unicode: str) -> str
        GetAscii(self: IdnMapping, unicode: str, index: int) -> str
        GetAscii(self: IdnMapping, unicode: str, index: int, count: int) -> str
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: IdnMapping) -> int """
        ...

    def GetUnicode(self, ascii:str, index:int = ..., count:int = ...) -> str:
        """
        GetUnicode(self: IdnMapping, ascii: str) -> str
        GetUnicode(self: IdnMapping, ascii: str, index: int) -> str
        GetUnicode(self: IdnMapping, ascii: str, index: int, count: int) -> str
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class JapaneseCalendar(Calendar): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ JapaneseCalendar() """
    pass

class JapaneseLunisolarCalendar(EastAsianLunisolarCalendar): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ JapaneseLunisolarCalendar() """
    @property
    def Eras(self) -> Array:
        """ Get: Eras(self: JapaneseLunisolarCalendar) -> Array[int] """
        ...

    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """ Get: MaxSupportedDateTime(self: JapaneseLunisolarCalendar) -> DateTime """
        ...

    @property
    def MinSupportedDateTime(self) -> DateTime:
        """ Get: MinSupportedDateTime(self: JapaneseLunisolarCalendar) -> DateTime """
        ...


    def GetEra(self, time:DateTime) -> int:
        """ GetEra(self: JapaneseLunisolarCalendar, time: DateTime) -> int """
        ...

    JapaneseEra: int = ...


class JulianCalendar(Calendar): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ JulianCalendar() """
    JulianEra: int = ...


class KoreanCalendar(Calendar): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ KoreanCalendar() """
    KoreanEra: int = ...


class KoreanLunisolarCalendar(EastAsianLunisolarCalendar): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ KoreanLunisolarCalendar() """
    @property
    def Eras(self) -> Array:
        """ Get: Eras(self: KoreanLunisolarCalendar) -> Array[int] """
        ...

    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """ Get: MaxSupportedDateTime(self: KoreanLunisolarCalendar) -> DateTime """
        ...

    @property
    def MinSupportedDateTime(self) -> DateTime:
        """ Get: MinSupportedDateTime(self: KoreanLunisolarCalendar) -> DateTime """
        ...


    def GetEra(self, time:DateTime) -> int:
        """ GetEra(self: KoreanLunisolarCalendar, time: DateTime) -> int """
        ...

    GregorianEra: int = ...


class NumberFormatInfo(ICloneable, IFormatProvider): # skipped bases: <type 'object'>
    """ NumberFormatInfo() """
    @property
    def CurrencyDecimalDigits(self) -> int:
        """
        Get: CurrencyDecimalDigits(self: NumberFormatInfo) -> int
        Set: CurrencyDecimalDigits(self: NumberFormatInfo) = value
        """
        ...

    @property
    def CurrencyDecimalSeparator(self) -> str:
        """
        Get: CurrencyDecimalSeparator(self: NumberFormatInfo) -> str
        Set: CurrencyDecimalSeparator(self: NumberFormatInfo) = value
        """
        ...

    @property
    def CurrencyGroupSeparator(self) -> str:
        """
        Get: CurrencyGroupSeparator(self: NumberFormatInfo) -> str
        Set: CurrencyGroupSeparator(self: NumberFormatInfo) = value
        """
        ...

    @property
    def CurrencyGroupSizes(self) -> Array:
        """
        Get: CurrencyGroupSizes(self: NumberFormatInfo) -> Array[int]
        Set: CurrencyGroupSizes(self: NumberFormatInfo) = value
        """
        ...

    @property
    def CurrencyNegativePattern(self) -> int:
        """
        Get: CurrencyNegativePattern(self: NumberFormatInfo) -> int
        Set: CurrencyNegativePattern(self: NumberFormatInfo) = value
        """
        ...

    @property
    def CurrencyPositivePattern(self) -> int:
        """
        Get: CurrencyPositivePattern(self: NumberFormatInfo) -> int
        Set: CurrencyPositivePattern(self: NumberFormatInfo) = value
        """
        ...

    @property
    def CurrencySymbol(self) -> str:
        """
        Get: CurrencySymbol(self: NumberFormatInfo) -> str
        Set: CurrencySymbol(self: NumberFormatInfo) = value
        """
        ...

    @property
    def CurrentInfo(self) -> NumberFormatInfo:
        """ Get: CurrentInfo() -> NumberFormatInfo """
        ...

    @property
    def DigitSubstitution(self) -> DigitShapes:
        """
        Get: DigitSubstitution(self: NumberFormatInfo) -> DigitShapes
        Set: DigitSubstitution(self: NumberFormatInfo) = value
        """
        ...

    @property
    def InvariantInfo(self) -> NumberFormatInfo:
        """ Get: InvariantInfo() -> NumberFormatInfo """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: NumberFormatInfo) -> bool """
        ...

    @property
    def NaNSymbol(self) -> str:
        """
        Get: NaNSymbol(self: NumberFormatInfo) -> str
        Set: NaNSymbol(self: NumberFormatInfo) = value
        """
        ...

    @property
    def NativeDigits(self) -> Array:
        """
        Get: NativeDigits(self: NumberFormatInfo) -> Array[str]
        Set: NativeDigits(self: NumberFormatInfo) = value
        """
        ...

    @property
    def NegativeInfinitySymbol(self) -> str:
        """
        Get: NegativeInfinitySymbol(self: NumberFormatInfo) -> str
        Set: NegativeInfinitySymbol(self: NumberFormatInfo) = value
        """
        ...

    @property
    def NegativeSign(self) -> str:
        """
        Get: NegativeSign(self: NumberFormatInfo) -> str
        Set: NegativeSign(self: NumberFormatInfo) = value
        """
        ...

    @property
    def NumberDecimalDigits(self) -> int:
        """
        Get: NumberDecimalDigits(self: NumberFormatInfo) -> int
        Set: NumberDecimalDigits(self: NumberFormatInfo) = value
        """
        ...

    @property
    def NumberDecimalSeparator(self) -> str:
        """
        Get: NumberDecimalSeparator(self: NumberFormatInfo) -> str
        Set: NumberDecimalSeparator(self: NumberFormatInfo) = value
        """
        ...

    @property
    def NumberGroupSeparator(self) -> str:
        """
        Get: NumberGroupSeparator(self: NumberFormatInfo) -> str
        Set: NumberGroupSeparator(self: NumberFormatInfo) = value
        """
        ...

    @property
    def NumberGroupSizes(self) -> Array:
        """
        Get: NumberGroupSizes(self: NumberFormatInfo) -> Array[int]
        Set: NumberGroupSizes(self: NumberFormatInfo) = value
        """
        ...

    @property
    def NumberNegativePattern(self) -> int:
        """
        Get: NumberNegativePattern(self: NumberFormatInfo) -> int
        Set: NumberNegativePattern(self: NumberFormatInfo) = value
        """
        ...

    @property
    def PercentDecimalDigits(self) -> int:
        """
        Get: PercentDecimalDigits(self: NumberFormatInfo) -> int
        Set: PercentDecimalDigits(self: NumberFormatInfo) = value
        """
        ...

    @property
    def PercentDecimalSeparator(self) -> str:
        """
        Get: PercentDecimalSeparator(self: NumberFormatInfo) -> str
        Set: PercentDecimalSeparator(self: NumberFormatInfo) = value
        """
        ...

    @property
    def PercentGroupSeparator(self) -> str:
        """
        Get: PercentGroupSeparator(self: NumberFormatInfo) -> str
        Set: PercentGroupSeparator(self: NumberFormatInfo) = value
        """
        ...

    @property
    def PercentGroupSizes(self) -> Array:
        """
        Get: PercentGroupSizes(self: NumberFormatInfo) -> Array[int]
        Set: PercentGroupSizes(self: NumberFormatInfo) = value
        """
        ...

    @property
    def PercentNegativePattern(self) -> int:
        """
        Get: PercentNegativePattern(self: NumberFormatInfo) -> int
        Set: PercentNegativePattern(self: NumberFormatInfo) = value
        """
        ...

    @property
    def PercentPositivePattern(self) -> int:
        """
        Get: PercentPositivePattern(self: NumberFormatInfo) -> int
        Set: PercentPositivePattern(self: NumberFormatInfo) = value
        """
        ...

    @property
    def PercentSymbol(self) -> str:
        """
        Get: PercentSymbol(self: NumberFormatInfo) -> str
        Set: PercentSymbol(self: NumberFormatInfo) = value
        """
        ...

    @property
    def PerMilleSymbol(self) -> str:
        """
        Get: PerMilleSymbol(self: NumberFormatInfo) -> str
        Set: PerMilleSymbol(self: NumberFormatInfo) = value
        """
        ...

    @property
    def PositiveInfinitySymbol(self) -> str:
        """
        Get: PositiveInfinitySymbol(self: NumberFormatInfo) -> str
        Set: PositiveInfinitySymbol(self: NumberFormatInfo) = value
        """
        ...

    @property
    def PositiveSign(self) -> str:
        """
        Get: PositiveSign(self: NumberFormatInfo) -> str
        Set: PositiveSign(self: NumberFormatInfo) = value
        """
        ...


    @staticmethod
    def GetInstance(formatProvider:IFormatProvider) -> NumberFormatInfo:
        """ GetInstance(formatProvider: IFormatProvider) -> NumberFormatInfo """
        ...

    @staticmethod
    def ReadOnly(nfi:NumberFormatInfo) -> NumberFormatInfo:
        """ ReadOnly(nfi: NumberFormatInfo) -> NumberFormatInfo """
        ...



class NumberStyles(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) NumberStyles, values: AllowCurrencySymbol (256), AllowDecimalPoint (32), AllowExponent (128), AllowHexSpecifier (512), AllowLeadingSign (4), AllowLeadingWhite (1), AllowParentheses (16), AllowThousands (64), AllowTrailingSign (8), AllowTrailingWhite (2), Any (511), Currency (383), Float (167), HexNumber (515), Integer (7), None (0), Number (111) """
    AllowCurrencySymbol: NumberStyles = ...
    AllowDecimalPoint: NumberStyles = ...
    AllowExponent: NumberStyles = ...
    AllowHexSpecifier: NumberStyles = ...
    AllowLeadingSign: NumberStyles = ...
    AllowLeadingWhite: NumberStyles = ...
    AllowParentheses: NumberStyles = ...
    AllowThousands: NumberStyles = ...
    AllowTrailingSign: NumberStyles = ...
    AllowTrailingWhite: NumberStyles = ...
    Any: NumberStyles = ...
    Currency: NumberStyles = ...
    Float: NumberStyles = ...
    HexNumber: NumberStyles = ...
    Integer: NumberStyles = ...
    Number: NumberStyles = ...
    value__ = ...


class PersianCalendar(Calendar): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ PersianCalendar() """
    PersianEra: int = ...


class RegionInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    RegionInfo(name: str)
    RegionInfo(culture: int)
    """
    @property
    def CurrencyEnglishName(self) -> str:
        """ Get: CurrencyEnglishName(self: RegionInfo) -> str """
        ...

    @property
    def CurrencyNativeName(self) -> str:
        """ Get: CurrencyNativeName(self: RegionInfo) -> str """
        ...

    @property
    def CurrencySymbol(self) -> str:
        """ Get: CurrencySymbol(self: RegionInfo) -> str """
        ...

    @property
    def CurrentRegion(self) -> RegionInfo:
        """ Get: CurrentRegion() -> RegionInfo """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: RegionInfo) -> str """
        ...

    @property
    def EnglishName(self) -> str:
        """ Get: EnglishName(self: RegionInfo) -> str """
        ...

    @property
    def GeoId(self) -> int:
        """ Get: GeoId(self: RegionInfo) -> int """
        ...

    @property
    def IsMetric(self) -> bool:
        """ Get: IsMetric(self: RegionInfo) -> bool """
        ...

    @property
    def ISOCurrencySymbol(self) -> str:
        """ Get: ISOCurrencySymbol(self: RegionInfo) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: RegionInfo) -> str """
        ...

    @property
    def NativeName(self) -> str:
        """ Get: NativeName(self: RegionInfo) -> str """
        ...

    @property
    def ThreeLetterISORegionName(self) -> str:
        """ Get: ThreeLetterISORegionName(self: RegionInfo) -> str """
        ...

    @property
    def ThreeLetterWindowsRegionName(self) -> str:
        """ Get: ThreeLetterWindowsRegionName(self: RegionInfo) -> str """
        ...

    @property
    def TwoLetterISORegionName(self) -> str:
        """ Get: TwoLetterISORegionName(self: RegionInfo) -> str """
        ...


    def Equals(self, value:object) -> bool:
        """ Equals(self: RegionInfo, value: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RegionInfo) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: RegionInfo) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class SortKey: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def KeyData(self) -> Array:
        """ Get: KeyData(self: SortKey) -> Array[Byte] """
        ...

    @property
    def OriginalString(self) -> str:
        """ Get: OriginalString(self: SortKey) -> str """
        ...


    @staticmethod
    def Compare(sortkey1:SortKey, sortkey2:SortKey) -> int:
        """ Compare(sortkey1: SortKey, sortkey2: SortKey) -> int """
        ...

    def Equals(self, value:object) -> bool:
        """ Equals(self: SortKey, value: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SortKey) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: SortKey) -> str """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SortVersion(IEquatable): # skipped bases: <type 'object'>
    """ SortVersion(fullVersion: int, sortId: Guid) """
    @property
    def FullVersion(self) -> int:
        """ Get: FullVersion(self: SortVersion) -> int """
        ...

    @property
    def SortId(self) -> Guid:
        """ Get: SortId(self: SortVersion) -> Guid """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: SortVersion) -> int """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class StringInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    StringInfo()
    StringInfo(value: str)
    """
    @property
    def LengthInTextElements(self) -> int:
        """ Get: LengthInTextElements(self: StringInfo) -> int """
        ...

    @property
    def String(self) -> str:
        """
        Get: String(self: StringInfo) -> str
        Set: String(self: StringInfo) = value
        """
        ...


    def Equals(self, value:object) -> bool:
        """ Equals(self: StringInfo, value: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: StringInfo) -> int """
        ...

    @staticmethod
    def GetNextTextElement(str:str, index:int = ...) -> str:
        """
        GetNextTextElement(str: str) -> str
        GetNextTextElement(str: str, index: int) -> str
        """
        ...

    @staticmethod
    def GetTextElementEnumerator(str:str, index:int = ...) -> TextElementEnumerator:
        """
        GetTextElementEnumerator(str: str) -> TextElementEnumerator
        GetTextElementEnumerator(str: str, index: int) -> TextElementEnumerator
        """
        ...

    @staticmethod
    def ParseCombiningCharacters(str:str) -> Array:
        """ ParseCombiningCharacters(str: str) -> Array[int] """
        ...

    def SubstringByTextElements(self, startingTextElement:int, lengthInTextElements:int = ...) -> str:
        """
        SubstringByTextElements(self: StringInfo, startingTextElement: int) -> str
        SubstringByTextElements(self: StringInfo, startingTextElement: int, lengthInTextElements: int) -> str
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TaiwanCalendar(Calendar): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ TaiwanCalendar() """
    pass

class TaiwanLunisolarCalendar(EastAsianLunisolarCalendar): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ TaiwanLunisolarCalendar() """
    @property
    def Eras(self) -> Array:
        """ Get: Eras(self: TaiwanLunisolarCalendar) -> Array[int] """
        ...

    @property
    def MaxSupportedDateTime(self) -> DateTime:
        """ Get: MaxSupportedDateTime(self: TaiwanLunisolarCalendar) -> DateTime """
        ...

    @property
    def MinSupportedDateTime(self) -> DateTime:
        """ Get: MinSupportedDateTime(self: TaiwanLunisolarCalendar) -> DateTime """
        ...


    def GetEra(self, time:DateTime) -> int:
        """ GetEra(self: TaiwanLunisolarCalendar, time: DateTime) -> int """
        ...


class TextElementEnumerator(IEnumerator): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ElementIndex(self) -> int:
        """ Get: ElementIndex(self: TextElementEnumerator) -> int """
        ...


    def GetTextElement(self) -> str:
        """ GetTextElement(self: TextElementEnumerator) -> str """
        ...


class TextInfo(ICloneable, IDeserializationCallback): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ANSICodePage(self) -> int:
        """ Get: ANSICodePage(self: TextInfo) -> int """
        ...

    @property
    def CultureName(self) -> str:
        """ Get: CultureName(self: TextInfo) -> str """
        ...

    @property
    def EBCDICCodePage(self) -> int:
        """ Get: EBCDICCodePage(self: TextInfo) -> int """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: TextInfo) -> bool """
        ...

    @property
    def IsRightToLeft(self) -> bool:
        """ Get: IsRightToLeft(self: TextInfo) -> bool """
        ...

    @property
    def LCID(self) -> int:
        """ Get: LCID(self: TextInfo) -> int """
        ...

    @property
    def ListSeparator(self) -> str:
        """
        Get: ListSeparator(self: TextInfo) -> str
        Set: ListSeparator(self: TextInfo) = value
        """
        ...

    @property
    def MacCodePage(self) -> int:
        """ Get: MacCodePage(self: TextInfo) -> int """
        ...

    @property
    def OEMCodePage(self) -> int:
        """ Get: OEMCodePage(self: TextInfo) -> int """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: TextInfo, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: TextInfo) -> int """
        ...

    @staticmethod
    def ReadOnly(textInfo:TextInfo) -> TextInfo:
        """ ReadOnly(textInfo: TextInfo) -> TextInfo """
        ...

    def ToLower(self, *__args:Char) -> Char:
        """
        ToLower(self: TextInfo, c: Char) -> Char
        ToLower(self: TextInfo, str: str) -> str
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: TextInfo) -> str """
        ...

    def ToTitleCase(self, str:str) -> str:
        """ ToTitleCase(self: TextInfo, str: str) -> str """
        ...

    def ToUpper(self, *__args:Char) -> Char:
        """
        ToUpper(self: TextInfo, c: Char) -> Char
        ToUpper(self: TextInfo, str: str) -> str
        """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ThaiBuddhistCalendar(Calendar): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ ThaiBuddhistCalendar() """
    ThaiBuddhistEra: int = ...


class TimeSpanStyles(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TimeSpanStyles, values: AssumeNegative (1), None (0) """
    AssumeNegative: TimeSpanStyles = ...
    value__ = ...


class UmAlQuraCalendar(Calendar): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """ UmAlQuraCalendar() """
    UmAlQuraEra: int = ...


class UnicodeCategory(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UnicodeCategory, values: ClosePunctuation (21), ConnectorPunctuation (18), Control (14), CurrencySymbol (26), DashPunctuation (19), DecimalDigitNumber (8), EnclosingMark (7), FinalQuotePunctuation (23), Format (15), InitialQuotePunctuation (22), LetterNumber (9), LineSeparator (12), LowercaseLetter (1), MathSymbol (25), ModifierLetter (3), ModifierSymbol (27), NonSpacingMark (5), OpenPunctuation (20), OtherLetter (4), OtherNotAssigned (29), OtherNumber (10), OtherPunctuation (24), OtherSymbol (28), ParagraphSeparator (13), PrivateUse (17), SpaceSeparator (11), SpacingCombiningMark (6), Surrogate (16), TitlecaseLetter (2), UppercaseLetter (0) """
    ClosePunctuation: UnicodeCategory = ...
    ConnectorPunctuation: UnicodeCategory = ...
    Control: UnicodeCategory = ...
    CurrencySymbol: UnicodeCategory = ...
    DashPunctuation: UnicodeCategory = ...
    DecimalDigitNumber: UnicodeCategory = ...
    EnclosingMark: UnicodeCategory = ...
    FinalQuotePunctuation: UnicodeCategory = ...
    Format: UnicodeCategory = ...
    InitialQuotePunctuation: UnicodeCategory = ...
    LetterNumber: UnicodeCategory = ...
    LineSeparator: UnicodeCategory = ...
    LowercaseLetter: UnicodeCategory = ...
    MathSymbol: UnicodeCategory = ...
    ModifierLetter: UnicodeCategory = ...
    ModifierSymbol: UnicodeCategory = ...
    NonSpacingMark: UnicodeCategory = ...
    OpenPunctuation: UnicodeCategory = ...
    OtherLetter: UnicodeCategory = ...
    OtherNotAssigned: UnicodeCategory = ...
    OtherNumber: UnicodeCategory = ...
    OtherPunctuation: UnicodeCategory = ...
    OtherSymbol: UnicodeCategory = ...
    ParagraphSeparator: UnicodeCategory = ...
    PrivateUse: UnicodeCategory = ...
    SpaceSeparator: UnicodeCategory = ...
    SpacingCombiningMark: UnicodeCategory = ...
    Surrogate: UnicodeCategory = ...
    TitlecaseLetter: UnicodeCategory = ...
    UppercaseLetter: UnicodeCategory = ...
    value__ = ...


