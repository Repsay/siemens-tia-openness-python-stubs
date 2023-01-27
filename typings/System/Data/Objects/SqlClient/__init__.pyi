# encoding: utf-8
# module System.Data.Objects.SqlClient calls itself SqlClient
# from System.Data.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Nullable

from System.Collections import IEnumerable

from System.Data.Spatial import DbGeography, DbGeometry


# no functions
# classes

class SqlFunctions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Acos(arg1:Nullable) -> Nullable:
        """
        Acos(arg1: Nullable[float]) -> Nullable[float]
        Acos(arg1: Nullable[Decimal]) -> Nullable[float]
        """
        ...

    @staticmethod
    def Ascii(arg:str) -> Nullable:
        """ Ascii(arg: str) -> Nullable[int] """
        ...

    @staticmethod
    def Asin(arg:Nullable) -> Nullable:
        """
        Asin(arg: Nullable[float]) -> Nullable[float]
        Asin(arg: Nullable[Decimal]) -> Nullable[float]
        """
        ...

    @staticmethod
    def Atan(arg:Nullable) -> Nullable:
        """
        Atan(arg: Nullable[float]) -> Nullable[float]
        Atan(arg: Nullable[Decimal]) -> Nullable[float]
        """
        ...

    @staticmethod
    def Atan2(arg1:Nullable, arg2:Nullable) -> Nullable:
        """
        Atan2(arg1: Nullable[float], arg2: Nullable[float]) -> Nullable[float]
        Atan2(arg1: Nullable[Decimal], arg2: Nullable[Decimal]) -> Nullable[float]
        """
        ...

    @staticmethod
    def Char(arg:Nullable) -> str:
        """ Char(arg: Nullable[int]) -> str """
        ...

    @staticmethod
    def CharIndex(toSearch:str, target:str, startLocation:Nullable = ...) -> Nullable:
        """
        CharIndex(toSearch: str, target: str) -> Nullable[int]
        CharIndex(toSearch: Array[Byte], target: Array[Byte]) -> Nullable[int]
        CharIndex(toSearch: str, target: str, startLocation: Nullable[int]) -> Nullable[int]
        CharIndex(toSearch: Array[Byte], target: Array[Byte], startLocation: Nullable[int]) -> Nullable[int]
        CharIndex(toSearch: str, target: str, startLocation: Nullable[Int64]) -> Nullable[Int64]
        CharIndex(toSearch: Array[Byte], target: Array[Byte], startLocation: Nullable[Int64]) -> Nullable[Int64]
        """
        ...

    @staticmethod
    def Checksum(arg1:Nullable, arg2:Nullable = ..., arg3:Nullable = ...) -> Nullable:
        """
        Checksum(arg1: Nullable[bool]) -> Nullable[int]
        Checksum(arg1: Nullable[TimeSpan], arg2: Nullable[TimeSpan], arg3: Nullable[TimeSpan]) -> Nullable[int]
        Checksum(arg1: Nullable[DateTimeOffset], arg2: Nullable[DateTimeOffset], arg3: Nullable[DateTimeOffset]) -> Nullable[int]
        Checksum(arg1: Nullable[DateTime], arg2: Nullable[DateTime], arg3: Nullable[DateTime]) -> Nullable[int]
        Checksum(arg1: str, arg2: str, arg3: str) -> Nullable[int]
        Checksum(arg1: Nullable[Decimal], arg2: Nullable[Decimal], arg3: Nullable[Decimal]) -> Nullable[int]
        Checksum(arg1: Nullable[float], arg2: Nullable[float], arg3: Nullable[float]) -> Nullable[int]
        Checksum(arg1: Nullable[bool], arg2: Nullable[bool], arg3: Nullable[bool]) -> Nullable[int]
        Checksum(arg1: Nullable[Guid], arg2: Nullable[Guid]) -> Nullable[int]
        Checksum(arg1: Array[Byte], arg2: Array[Byte]) -> Nullable[int]
        Checksum(arg1: Nullable[DateTimeOffset], arg2: Nullable[DateTimeOffset]) -> Nullable[int]
        Checksum(arg1: Nullable[TimeSpan], arg2: Nullable[TimeSpan]) -> Nullable[int]
        Checksum(arg1: Array[Byte], arg2: Array[Byte], arg3: Array[Byte]) -> Nullable[int]
        Checksum(arg1: Nullable[DateTime], arg2: Nullable[DateTime]) -> Nullable[int]
        Checksum(arg1: Nullable[Decimal], arg2: Nullable[Decimal]) -> Nullable[int]
        Checksum(arg1: Nullable[float], arg2: Nullable[float]) -> Nullable[int]
        Checksum(arg1: Nullable[bool], arg2: Nullable[bool]) -> Nullable[int]
        Checksum(arg1: Nullable[Guid]) -> Nullable[int]
        Checksum(arg1: Array[Byte]) -> Nullable[int]
        Checksum(arg1: Nullable[DateTimeOffset]) -> Nullable[int]
        Checksum(arg1: Nullable[TimeSpan]) -> Nullable[int]
        Checksum(arg1: Nullable[DateTime]) -> Nullable[int]
        Checksum(arg1: str) -> Nullable[int]
        Checksum(arg1: Nullable[Decimal]) -> Nullable[int]
        Checksum(arg1: Nullable[float]) -> Nullable[int]
        Checksum(arg1: str, arg2: str) -> Nullable[int]
        Checksum(arg1: Nullable[Guid], arg2: Nullable[Guid], arg3: Nullable[Guid]) -> Nullable[int]
        """
        ...

    @staticmethod
    def ChecksumAggregate(arg:IEnumerable) -> Nullable:
        """
        ChecksumAggregate(arg: IEnumerable[int]) -> Nullable[int]
        ChecksumAggregate(arg: IEnumerable[Nullable[int]]) -> Nullable[int]
        """
        ...

    @staticmethod
    def Cos(arg:Nullable) -> Nullable:
        """
        Cos(arg: Nullable[float]) -> Nullable[float]
        Cos(arg: Nullable[Decimal]) -> Nullable[float]
        """
        ...

    @staticmethod
    def Cot(arg:Nullable) -> Nullable:
        """
        Cot(arg: Nullable[float]) -> Nullable[float]
        Cot(arg: Nullable[Decimal]) -> Nullable[float]
        """
        ...

    @staticmethod
    def CurrentTimestamp() -> Nullable:
        """ CurrentTimestamp() -> Nullable[DateTime] """
        ...

    @staticmethod
    def CurrentUser() -> str:
        """ CurrentUser() -> str """
        ...

    @staticmethod
    def DataLength(arg:Nullable) -> Nullable:
        """
        DataLength(arg: Nullable[bool]) -> Nullable[int]
        DataLength(arg: Nullable[float]) -> Nullable[int]
        DataLength(arg: Nullable[Decimal]) -> Nullable[int]
        DataLength(arg: Nullable[DateTime]) -> Nullable[int]
        DataLength(arg: Nullable[TimeSpan]) -> Nullable[int]
        DataLength(arg: Nullable[DateTimeOffset]) -> Nullable[int]
        DataLength(arg: str) -> Nullable[int]
        DataLength(arg: Array[Byte]) -> Nullable[int]
        DataLength(arg: Nullable[Guid]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DateAdd(datePartArg:str, number:Nullable, *__args:Nullable) -> Nullable:
        """
        DateAdd(datePartArg: str, number: Nullable[float], date: Nullable[DateTime]) -> Nullable[DateTime]
        DateAdd(datePartArg: str, number: Nullable[float], time: Nullable[TimeSpan]) -> Nullable[TimeSpan]
        DateAdd(datePartArg: str, number: Nullable[float], dateTimeOffsetArg: Nullable[DateTimeOffset]) -> Nullable[DateTimeOffset]
        DateAdd(datePartArg: str, number: Nullable[float], date: str) -> Nullable[DateTime]
        """
        ...

    @staticmethod
    def DateDiff(datePartArg:str, startDate:Nullable, endDate:Nullable) -> Nullable:
        """
        DateDiff(datePartArg: str, startDate: Nullable[DateTime], endDate: Nullable[DateTime]) -> Nullable[int]
        DateDiff(datePartArg: str, startDate: Nullable[DateTimeOffset], endDate: Nullable[DateTimeOffset]) -> Nullable[int]
        DateDiff(datePartArg: str, startDate: Nullable[TimeSpan], endDate: Nullable[TimeSpan]) -> Nullable[int]
        DateDiff(datePartArg: str, startDate: str, endDate: Nullable[DateTime]) -> Nullable[int]
        DateDiff(datePartArg: str, startDate: str, endDate: Nullable[DateTimeOffset]) -> Nullable[int]
        DateDiff(datePartArg: str, startDate: str, endDate: Nullable[TimeSpan]) -> Nullable[int]
        DateDiff(datePartArg: str, startDate: Nullable[TimeSpan], endDate: str) -> Nullable[int]
        DateDiff(datePartArg: str, startDate: Nullable[DateTime], endDate: str) -> Nullable[int]
        DateDiff(datePartArg: str, startDate: Nullable[DateTimeOffset], endDate: str) -> Nullable[int]
        DateDiff(datePartArg: str, startDate: str, endDate: str) -> Nullable[int]
        DateDiff(datePartArg: str, startDate: Nullable[TimeSpan], endDate: Nullable[DateTime]) -> Nullable[int]
        DateDiff(datePartArg: str, startDate: Nullable[TimeSpan], endDate: Nullable[DateTimeOffset]) -> Nullable[int]
        DateDiff(datePartArg: str, startDate: Nullable[DateTime], endDate: Nullable[TimeSpan]) -> Nullable[int]
        DateDiff(datePartArg: str, startDate: Nullable[DateTimeOffset], endDate: Nullable[TimeSpan]) -> Nullable[int]
        DateDiff(datePartArg: str, startDate: Nullable[DateTime], endDate: Nullable[DateTimeOffset]) -> Nullable[int]
        DateDiff(datePartArg: str, startDate: Nullable[DateTimeOffset], endDate: Nullable[DateTime]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DateName(datePartArg:str, date:Nullable) -> str:
        """
        DateName(datePartArg: str, date: Nullable[DateTime]) -> str
        DateName(datePartArg: str, date: str) -> str
        DateName(datePartArg: str, date: Nullable[TimeSpan]) -> str
        DateName(datePartArg: str, date: Nullable[DateTimeOffset]) -> str
        """
        ...

    @staticmethod
    def DatePart(datePartArg:str, date:Nullable) -> Nullable:
        """
        DatePart(datePartArg: str, date: Nullable[DateTime]) -> Nullable[int]
        DatePart(datePartArg: str, date: Nullable[DateTimeOffset]) -> Nullable[int]
        DatePart(datePartArg: str, date: str) -> Nullable[int]
        DatePart(datePartArg: str, date: Nullable[TimeSpan]) -> Nullable[int]
        """
        ...

    @staticmethod
    def Degrees(arg1:Nullable) -> Nullable:
        """
        Degrees(arg1: Nullable[int]) -> Nullable[int]
        Degrees(arg1: Nullable[Int64]) -> Nullable[Int64]
        Degrees(arg1: Nullable[Decimal]) -> Nullable[Decimal]
        Degrees(arg1: Nullable[float]) -> Nullable[float]
        """
        ...

    @staticmethod
    def Difference(string1:str, string2:str) -> Nullable:
        """ Difference(string1: str, string2: str) -> Nullable[int] """
        ...

    @staticmethod
    def Exp(arg:Nullable) -> Nullable:
        """
        Exp(arg: Nullable[float]) -> Nullable[float]
        Exp(arg: Nullable[Decimal]) -> Nullable[float]
        """
        ...

    @staticmethod
    def GetDate() -> Nullable:
        """ GetDate() -> Nullable[DateTime] """
        ...

    @staticmethod
    def GetUtcDate() -> Nullable:
        """ GetUtcDate() -> Nullable[DateTime] """
        ...

    @staticmethod
    def HostName() -> str:
        """ HostName() -> str """
        ...

    @staticmethod
    def IsDate(arg:str) -> Nullable:
        """ IsDate(arg: str) -> Nullable[int] """
        ...

    @staticmethod
    def IsNumeric(arg:str) -> Nullable:
        """ IsNumeric(arg: str) -> Nullable[int] """
        ...

    @staticmethod
    def Log(arg:Nullable) -> Nullable:
        """
        Log(arg: Nullable[float]) -> Nullable[float]
        Log(arg: Nullable[Decimal]) -> Nullable[float]
        """
        ...

    @staticmethod
    def Log10(arg:Nullable) -> Nullable:
        """
        Log10(arg: Nullable[float]) -> Nullable[float]
        Log10(arg: Nullable[Decimal]) -> Nullable[float]
        """
        ...

    @staticmethod
    def NChar(arg:Nullable) -> str:
        """ NChar(arg: Nullable[int]) -> str """
        ...

    @staticmethod
    def PatIndex(stringPattern:str, target:str) -> Nullable:
        """ PatIndex(stringPattern: str, target: str) -> Nullable[int] """
        ...

    @staticmethod
    def Pi() -> Nullable:
        """ Pi() -> Nullable[float] """
        ...

    @staticmethod
    def QuoteName(stringArg:str, quoteCharacter:str = ...) -> str:
        """
        QuoteName(stringArg: str) -> str
        QuoteName(stringArg: str, quoteCharacter: str) -> str
        """
        ...

    @staticmethod
    def Radians(arg:Nullable) -> Nullable:
        """
        Radians(arg: Nullable[int]) -> Nullable[int]
        Radians(arg: Nullable[Int64]) -> Nullable[Int64]
        Radians(arg: Nullable[Decimal]) -> Nullable[Decimal]
        Radians(arg: Nullable[float]) -> Nullable[float]
        """
        ...

    @staticmethod
    def Rand(seed=None) -> Nullable:
        """
        Rand() -> Nullable[float]
        Rand(seed: Nullable[int]) -> Nullable[float]
        """
        ...

    @staticmethod
    def Replicate(target:str, count:Nullable) -> str:
        """ Replicate(target: str, count: Nullable[int]) -> str """
        ...

    @staticmethod
    def Sign(arg:Nullable) -> Nullable:
        """
        Sign(arg: Nullable[int]) -> Nullable[int]
        Sign(arg: Nullable[Int64]) -> Nullable[Int64]
        Sign(arg: Nullable[Decimal]) -> Nullable[Decimal]
        Sign(arg: Nullable[float]) -> Nullable[float]
        """
        ...

    @staticmethod
    def Sin(arg:Nullable) -> Nullable:
        """
        Sin(arg: Nullable[Decimal]) -> Nullable[float]
        Sin(arg: Nullable[float]) -> Nullable[float]
        """
        ...

    @staticmethod
    def SoundCode(arg:str) -> str:
        """ SoundCode(arg: str) -> str """
        ...

    @staticmethod
    def Space(arg1:Nullable) -> str:
        """ Space(arg1: Nullable[int]) -> str """
        ...

    @staticmethod
    def Square(arg1:Nullable) -> Nullable:
        """
        Square(arg1: Nullable[float]) -> Nullable[float]
        Square(arg1: Nullable[Decimal]) -> Nullable[float]
        """
        ...

    @staticmethod
    def SquareRoot(arg:Nullable) -> Nullable:
        """
        SquareRoot(arg: Nullable[float]) -> Nullable[float]
        SquareRoot(arg: Nullable[Decimal]) -> Nullable[float]
        """
        ...

    @staticmethod
    def StringConvert(number:Nullable, length:Nullable = ..., decimalArg:Nullable = ...) -> str:
        """
        StringConvert(number: Nullable[float]) -> str
        StringConvert(number: Nullable[Decimal]) -> str
        StringConvert(number: Nullable[float], length: Nullable[int]) -> str
        StringConvert(number: Nullable[Decimal], length: Nullable[int]) -> str
        StringConvert(number: Nullable[float], length: Nullable[int], decimalArg: Nullable[int]) -> str
        StringConvert(number: Nullable[Decimal], length: Nullable[int], decimalArg: Nullable[int]) -> str
        """
        ...

    @staticmethod
    def Stuff(stringInput:str, start:Nullable, length:Nullable, stringReplacement:str) -> str:
        """ Stuff(stringInput: str, start: Nullable[int], length: Nullable[int], stringReplacement: str) -> str """
        ...

    @staticmethod
    def Tan(arg:Nullable) -> Nullable:
        """
        Tan(arg: Nullable[float]) -> Nullable[float]
        Tan(arg: Nullable[Decimal]) -> Nullable[float]
        """
        ...

    @staticmethod
    def Unicode(arg:str) -> Nullable:
        """ Unicode(arg: str) -> Nullable[int] """
        ...

    @staticmethod
    def UserName(arg:Nullable = ...) -> str:
        """
        UserName(arg: Nullable[int]) -> str
        UserName() -> str
        """
        ...

    __all__: list = ...


class SqlSpatialFunctions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AsTextZM(*__args:DbGeography) -> str:
        """
        AsTextZM(geographyValue: DbGeography) -> str
        AsTextZM(geometryValue: DbGeometry) -> str
        """
        ...

    @staticmethod
    def BufferWithTolerance(*__args) -> DbGeography:
        """
        BufferWithTolerance(geographyValue: DbGeography, distance: Nullable[float], tolerance: Nullable[float], relative: Nullable[bool]) -> DbGeography
        BufferWithTolerance(geometryValue: DbGeometry, distance: Nullable[float], tolerance: Nullable[float], relative: Nullable[bool]) -> DbGeometry
        """
        ...

    @staticmethod
    def EnvelopeAngle(geographyValue:DbGeography) -> Nullable:
        """ EnvelopeAngle(geographyValue: DbGeography) -> Nullable[float] """
        ...

    @staticmethod
    def EnvelopeCenter(geographyValue:DbGeography) -> DbGeography:
        """ EnvelopeCenter(geographyValue: DbGeography) -> DbGeography """
        ...

    @staticmethod
    def Filter(*__args) -> Nullable:
        """
        Filter(geographyValue: DbGeography, geographyOther: DbGeography) -> Nullable[bool]
        Filter(geometryValue: DbGeometry, geometryOther: DbGeometry) -> Nullable[bool]
        """
        ...

    @staticmethod
    def InstanceOf(*__args) -> Nullable:
        """
        InstanceOf(geographyValue: DbGeography, geometryTypeName: str) -> Nullable[bool]
        InstanceOf(geometryValue: DbGeometry, geometryTypeName: str) -> Nullable[bool]
        """
        ...

    @staticmethod
    def MakeValid(geometryValue:DbGeometry) -> DbGeometry:
        """ MakeValid(geometryValue: DbGeometry) -> DbGeometry """
        ...

    @staticmethod
    def NumRings(geographyValue:DbGeography) -> Nullable:
        """ NumRings(geographyValue: DbGeography) -> Nullable[int] """
        ...

    @staticmethod
    def PointGeography(latitude:Nullable, longitude:Nullable, spatialReferenceId:Nullable) -> DbGeography:
        """ PointGeography(latitude: Nullable[float], longitude: Nullable[float], spatialReferenceId: Nullable[int]) -> DbGeography """
        ...

    @staticmethod
    def PointGeometry(xCoordinate:Nullable, yCoordinate:Nullable, spatialReferenceId:Nullable) -> DbGeometry:
        """ PointGeometry(xCoordinate: Nullable[float], yCoordinate: Nullable[float], spatialReferenceId: Nullable[int]) -> DbGeometry """
        ...

    @staticmethod
    def Reduce(*__args) -> DbGeography:
        """
        Reduce(geographyValue: DbGeography, tolerance: Nullable[float]) -> DbGeography
        Reduce(geometryValue: DbGeometry, tolerance: Nullable[float]) -> DbGeometry
        """
        ...

    @staticmethod
    def RingN(geographyValue:DbGeography, index:Nullable) -> DbGeography:
        """ RingN(geographyValue: DbGeography, index: Nullable[int]) -> DbGeography """
        ...

    __all__: list = ...


