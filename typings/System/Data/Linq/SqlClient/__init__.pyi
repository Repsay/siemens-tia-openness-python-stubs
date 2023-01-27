# encoding: utf-8
# module System.Data.Linq.SqlClient calls itself SqlClient
# from System.Data.Linq, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Char, DateTime

"""The following names are not found in the module: (IConnectionUser, 
    IReaderProvider)
"""

# no functions
# classes

class SqlProvider(IReaderProvider, IConnectionUser): # skipped bases: <type 'IDisposable'>, <type 'IProvider'>, <type 'object'>
    """ SqlProvider() """
    def Dispose(self): # -> 
        """ Dispose(self: SqlProvider) """
        ...


class Sql2000Provider(SqlProvider): # skipped bases: <type 'IDisposable'>, <type 'IReaderProvider'>, <type 'IConnectionUser'>, <type 'IProvider'>, <type 'object'>
    """ Sql2000Provider() """
    pass

class Sql2005Provider(SqlProvider): # skipped bases: <type 'IDisposable'>, <type 'IReaderProvider'>, <type 'IConnectionUser'>, <type 'IProvider'>, <type 'object'>
    """ Sql2005Provider() """
    pass

class Sql2008Provider(SqlProvider): # skipped bases: <type 'IDisposable'>, <type 'IReaderProvider'>, <type 'IConnectionUser'>, <type 'IProvider'>, <type 'object'>
    """ Sql2008Provider() """
    pass

class SqlHelpers: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetStringContainsPattern(text:str, escape:Char) -> str:
        """ GetStringContainsPattern(text: str, escape: Char) -> str """
        ...

    @staticmethod
    def GetStringEndsWithPattern(text:str, escape:Char) -> str:
        """ GetStringEndsWithPattern(text: str, escape: Char) -> str """
        ...

    @staticmethod
    def GetStringStartsWithPattern(text:str, escape:Char) -> str:
        """ GetStringStartsWithPattern(text: str, escape: Char) -> str """
        ...

    @staticmethod
    def TranslateVBLikePattern(pattern:str, escape:Char) -> str:
        """ TranslateVBLikePattern(pattern: str, escape: Char) -> str """
        ...

    __all__: list = ...


class SqlMethods: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def DateDiffDay(startDate:DateTime, endDate:DateTime) -> int:
        """
        DateDiffDay(startDate: DateTime, endDate: DateTime) -> int
        DateDiffDay(startDate: Nullable[DateTime], endDate: Nullable[DateTime]) -> Nullable[int]
        DateDiffDay(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int
        DateDiffDay(startDate: Nullable[DateTimeOffset], endDate: Nullable[DateTimeOffset]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DateDiffHour(startDate:DateTime, endDate:DateTime) -> int:
        """
        DateDiffHour(startDate: DateTime, endDate: DateTime) -> int
        DateDiffHour(startDate: Nullable[DateTime], endDate: Nullable[DateTime]) -> Nullable[int]
        DateDiffHour(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int
        DateDiffHour(startDate: Nullable[DateTimeOffset], endDate: Nullable[DateTimeOffset]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DateDiffMicrosecond(startDate:DateTime, endDate:DateTime) -> int:
        """
        DateDiffMicrosecond(startDate: DateTime, endDate: DateTime) -> int
        DateDiffMicrosecond(startDate: Nullable[DateTime], endDate: Nullable[DateTime]) -> Nullable[int]
        DateDiffMicrosecond(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int
        DateDiffMicrosecond(startDate: Nullable[DateTimeOffset], endDate: Nullable[DateTimeOffset]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DateDiffMillisecond(startDate:DateTime, endDate:DateTime) -> int:
        """
        DateDiffMillisecond(startDate: DateTime, endDate: DateTime) -> int
        DateDiffMillisecond(startDate: Nullable[DateTime], endDate: Nullable[DateTime]) -> Nullable[int]
        DateDiffMillisecond(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int
        DateDiffMillisecond(startDate: Nullable[DateTimeOffset], endDate: Nullable[DateTimeOffset]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DateDiffMinute(startDate:DateTime, endDate:DateTime) -> int:
        """
        DateDiffMinute(startDate: DateTime, endDate: DateTime) -> int
        DateDiffMinute(startDate: Nullable[DateTime], endDate: Nullable[DateTime]) -> Nullable[int]
        DateDiffMinute(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int
        DateDiffMinute(startDate: Nullable[DateTimeOffset], endDate: Nullable[DateTimeOffset]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DateDiffMonth(startDate:DateTime, endDate:DateTime) -> int:
        """
        DateDiffMonth(startDate: DateTime, endDate: DateTime) -> int
        DateDiffMonth(startDate: Nullable[DateTime], endDate: Nullable[DateTime]) -> Nullable[int]
        DateDiffMonth(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int
        DateDiffMonth(startDate: Nullable[DateTimeOffset], endDate: Nullable[DateTimeOffset]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DateDiffNanosecond(startDate:DateTime, endDate:DateTime) -> int:
        """
        DateDiffNanosecond(startDate: DateTime, endDate: DateTime) -> int
        DateDiffNanosecond(startDate: Nullable[DateTime], endDate: Nullable[DateTime]) -> Nullable[int]
        DateDiffNanosecond(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int
        DateDiffNanosecond(startDate: Nullable[DateTimeOffset], endDate: Nullable[DateTimeOffset]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DateDiffSecond(startDate:DateTime, endDate:DateTime) -> int:
        """
        DateDiffSecond(startDate: DateTime, endDate: DateTime) -> int
        DateDiffSecond(startDate: Nullable[DateTime], endDate: Nullable[DateTime]) -> Nullable[int]
        DateDiffSecond(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int
        DateDiffSecond(startDate: Nullable[DateTimeOffset], endDate: Nullable[DateTimeOffset]) -> Nullable[int]
        """
        ...

    @staticmethod
    def DateDiffYear(startDate:DateTime, endDate:DateTime) -> int:
        """
        DateDiffYear(startDate: DateTime, endDate: DateTime) -> int
        DateDiffYear(startDate: Nullable[DateTime], endDate: Nullable[DateTime]) -> Nullable[int]
        DateDiffYear(startDate: DateTimeOffset, endDate: DateTimeOffset) -> int
        DateDiffYear(startDate: Nullable[DateTimeOffset], endDate: Nullable[DateTimeOffset]) -> Nullable[int]
        """
        ...

    @staticmethod
    def Like(matchExpression:str, pattern:str, escapeCharacter:Char = ...) -> bool:
        """
        Like(matchExpression: str, pattern: str) -> bool
        Like(matchExpression: str, pattern: str, escapeCharacter: Char) -> bool
        """
        ...

    __all__: list = ...


# variables with complex values

