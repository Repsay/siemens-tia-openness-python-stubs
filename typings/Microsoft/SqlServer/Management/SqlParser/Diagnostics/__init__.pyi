# encoding: utf-8
# module Microsoft.SqlServer.Management.SqlParser.Diagnostics calls itself Diagnostics
# from Microsoft.SqlServer.Management.SqlParser, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum

from System.Collections import IList

"""The following names are not found in the module: field#
"""

# no functions
# classes

class CounterId(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CounterId, values: Max (1), Min (0) """
    Max: CounterId = ...
    Min: CounterId = ...
    value__ = ...


class Counters: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def OutputFormat(self) -> Format:
        """
        Get: OutputFormat() -> Format
        Set: OutputFormat() = value
        """
        ...

    @property
    def PerfWriters(self) -> IList:
        """ Get: PerfWriters() -> IList[TextWriter] """
        ...


    @staticmethod
    def Begin(): # -> 
        """ Begin() """
        ...

    @staticmethod
    def Finish(): # -> 
        """ Finish() """
        ...

    __all__: list = ...


class Format(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Format, values: Csv (2), Text (1), Xml (0) """
    Csv: Format = ...
    Text: Format = ...
    value__ = ...
    Xml: Format = ...


class TimerId(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TimerId, values: Bind (3), Lexer (4), None (0), Parse (2), RangeMax_Refresh (10), RangeMin_Refresh (5), Refresh_Database (7), Refresh_Schema (8), Refresh_Server (6), Refresh_Table (9), Root (1), Serialize_CodeDomGen (15), Serialize_CodeSerialize (11), Serialize_Driver (12), Serialize_MetadataGen (13), Serialize_TypeCompaction (14) """
    Bind: TimerId = ...
    Lexer: TimerId = ...
    Parse: TimerId = ...
    RangeMax_Refresh: TimerId = ...
    RangeMin_Refresh: TimerId = ...
    Refresh_Database: TimerId = ...
    Refresh_Schema: TimerId = ...
    Refresh_Server: TimerId = ...
    Refresh_Table: TimerId = ...
    Root: TimerId = ...
    Serialize_CodeDomGen: TimerId = ...
    Serialize_CodeSerialize: TimerId = ...
    Serialize_Driver: TimerId = ...
    Serialize_MetadataGen: TimerId = ...
    Serialize_TypeCompaction: TimerId = ...
    value__ = ...


class Timers: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def OutputFormat(self) -> Format:
        """
        Get: OutputFormat() -> Format
        Set: OutputFormat() = value
        """
        ...

    @property
    def PerfWriters(self) -> IList:
        """ Get: PerfWriters() -> IList[TextWriter] """
        ...


    @staticmethod
    def Begin(recordCount:int): # -> 
        """ Begin(recordCount: int) """
        ...

    def EventType(self, *args): #cannot find CLR method
        """ enum EventType, values: End (2), Invalid (0), Start (1) """
        ...

    @staticmethod
    def Finish(): # -> 
        """ Finish() """
        ...

    __all__: list = ...


