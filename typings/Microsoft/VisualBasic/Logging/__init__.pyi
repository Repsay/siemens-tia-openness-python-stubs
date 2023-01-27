# encoding: utf-8
# module Microsoft.VisualBasic.Logging calls itself Logging
# from Microsoft.VisualBasic, Version=10.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, Int64

from System.Diagnostics import TraceEventType, TraceListener, TraceSource

from System.Text import Encoding

"""The following names are not found in the module: field#
"""

# no functions
# classes

class Log: # skipped bases: <type 'object'>, <type 'object'>
    """
    Log()
    Log(name: str)
    """
    @property
    def DefaultFileLogWriter(self) -> FileLogTraceListener:
        """ Get: DefaultFileLogWriter(self: Log) -> FileLogTraceListener """
        ...

    @property
    def TraceSource(self) -> TraceSource:
        """ Get: TraceSource(self: Log) -> TraceSource """
        ...


    def InitializeWithDefaultsSinceNoConfigExists(self, *args): #cannot find CLR method
        """ InitializeWithDefaultsSinceNoConfigExists(self: Log) """
        ...

    def WriteEntry(self, message:str, severity:TraceEventType = ..., id:int = ...): # -> 
        """ WriteEntry(self: Log, message: str)WriteEntry(self: Log, message: str, severity: TraceEventType)WriteEntry(self: Log, message: str, severity: TraceEventType, id: int) """
        ...

    def WriteException(self, ex:Exception, severity:TraceEventType = ..., additionalInfo:str = ..., id:int = ...): # -> 
        """ WriteException(self: Log, ex: Exception)WriteException(self: Log, ex: Exception, severity: TraceEventType, additionalInfo: str)WriteException(self: Log, ex: Exception, severity: TraceEventType, additionalInfo: str, id: int) """
        ...


class AspLog(Log): # skipped bases: <type 'object'>
    """
    AspLog()
    AspLog(name: str)
    """
    pass

class DiskSpaceExhaustedOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DiskSpaceExhaustedOption, values: DiscardMessages (1), ThrowException (0) """
    DiscardMessages: DiskSpaceExhaustedOption = ...
    ThrowException: DiskSpaceExhaustedOption = ...
    value__ = ...


class FileLogTraceListener(TraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    FileLogTraceListener(name: str)
    FileLogTraceListener()
    """
    @property
    def Append(self) -> bool:
        """
        Get: Append(self: FileLogTraceListener) -> bool
        Set: Append(self: FileLogTraceListener) = value
        """
        ...

    @property
    def AutoFlush(self) -> bool:
        """
        Get: AutoFlush(self: FileLogTraceListener) -> bool
        Set: AutoFlush(self: FileLogTraceListener) = value
        """
        ...

    @property
    def BaseFileName(self) -> str:
        """
        Get: BaseFileName(self: FileLogTraceListener) -> str
        Set: BaseFileName(self: FileLogTraceListener) = value
        """
        ...

    @property
    def CustomLocation(self) -> str:
        """
        Get: CustomLocation(self: FileLogTraceListener) -> str
        Set: CustomLocation(self: FileLogTraceListener) = value
        """
        ...

    @property
    def Delimiter(self) -> str:
        """
        Get: Delimiter(self: FileLogTraceListener) -> str
        Set: Delimiter(self: FileLogTraceListener) = value
        """
        ...

    @property
    def DiskSpaceExhaustedBehavior(self) -> DiskSpaceExhaustedOption:
        """
        Get: DiskSpaceExhaustedBehavior(self: FileLogTraceListener) -> DiskSpaceExhaustedOption
        Set: DiskSpaceExhaustedBehavior(self: FileLogTraceListener) = value
        """
        ...

    @property
    def Encoding(self) -> Encoding:
        """
        Get: Encoding(self: FileLogTraceListener) -> Encoding
        Set: Encoding(self: FileLogTraceListener) = value
        """
        ...

    @property
    def FullLogFileName(self) -> str:
        """ Get: FullLogFileName(self: FileLogTraceListener) -> str """
        ...

    @property
    def IncludeHostName(self) -> bool:
        """
        Get: IncludeHostName(self: FileLogTraceListener) -> bool
        Set: IncludeHostName(self: FileLogTraceListener) = value
        """
        ...

    @property
    def Location(self) -> LogFileLocation:
        """
        Get: Location(self: FileLogTraceListener) -> LogFileLocation
        Set: Location(self: FileLogTraceListener) = value
        """
        ...

    @property
    def LogFileCreationSchedule(self) -> LogFileCreationScheduleOption:
        """
        Get: LogFileCreationSchedule(self: FileLogTraceListener) -> LogFileCreationScheduleOption
        Set: LogFileCreationSchedule(self: FileLogTraceListener) = value
        """
        ...

    @property
    def MaxFileSize(self) -> Int64:
        """
        Get: MaxFileSize(self: FileLogTraceListener) -> Int64
        Set: MaxFileSize(self: FileLogTraceListener) = value
        """
        ...

    @property
    def ReserveDiskSpace(self) -> Int64:
        """
        Get: ReserveDiskSpace(self: FileLogTraceListener) -> Int64
        Set: ReserveDiskSpace(self: FileLogTraceListener) = value
        """
        ...



class LogFileCreationScheduleOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LogFileCreationScheduleOption, values: Daily (1), None (0), Weekly (2) """
    Daily: LogFileCreationScheduleOption = ...
    value__ = ...
    Weekly: LogFileCreationScheduleOption = ...


class LogFileLocation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LogFileLocation, values: CommonApplicationDirectory (2), Custom (4), ExecutableDirectory (3), LocalUserApplicationDirectory (1), TempDirectory (0) """
    CommonApplicationDirectory: LogFileLocation = ...
    Custom: LogFileLocation = ...
    ExecutableDirectory: LogFileLocation = ...
    LocalUserApplicationDirectory: LogFileLocation = ...
    TempDirectory: LogFileLocation = ...
    value__ = ...


