# encoding: utf-8
# module System.IO.Log calls itself Log
# from System.IO.Log, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Win32.SafeHandles import SafeFileHandle

from System import (ArgumentException, Array, ArraySegment, AsyncCallback, 
    Enum, EventArgs, IAsyncResult, IComparable, IDisposable, Int64)

from System.Collections import ICollection, IEnumerable, IEnumerator

from System.IO import Stream

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class FileRecordSequence(IRecordSequence): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    FileRecordSequence(path: str)
    FileRecordSequence(path: str, access: FileAccess)
    FileRecordSequence(path: str, access: FileAccess, size: int)
    """
    def Dispose(self): # -> 
        """ Dispose(self: FileRecordSequence) """
        ...

    TailPinned = ...


class FileRegion: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def FileLength(self) -> Int64:
        """ Get: FileLength(self: FileRegion) -> Int64 """
        ...

    @property
    def Offset(self) -> Int64:
        """ Get: Offset(self: FileRegion) -> Int64 """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: FileRegion) -> str """
        ...


    def GetStream(self) -> Stream:
        """ GetStream(self: FileRegion) -> Stream """
        ...


class IRecordSequence(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BaseSequenceNumber(self) -> SequenceNumber:
        """ Get: BaseSequenceNumber(self: IRecordSequence) -> SequenceNumber """
        ...

    @property
    def LastSequenceNumber(self) -> SequenceNumber:
        """ Get: LastSequenceNumber(self: IRecordSequence) -> SequenceNumber """
        ...

    @property
    def MaximumRecordLength(self) -> Int64:
        """ Get: MaximumRecordLength(self: IRecordSequence) -> Int64 """
        ...

    @property
    def ReservedBytes(self) -> Int64:
        """ Get: ReservedBytes(self: IRecordSequence) -> Int64 """
        ...

    @property
    def RestartSequenceNumber(self) -> SequenceNumber:
        """ Get: RestartSequenceNumber(self: IRecordSequence) -> SequenceNumber """
        ...

    @property
    def RetryAppend(self) -> bool:
        """
        Get: RetryAppend(self: IRecordSequence) -> bool
        Set: RetryAppend(self: IRecordSequence) = value
        """
        ...


    def AdvanceBaseSequenceNumber(self, newBaseSequenceNumber:SequenceNumber): # -> 
        """ AdvanceBaseSequenceNumber(self: IRecordSequence, newBaseSequenceNumber: SequenceNumber) """
        ...

    def Append(self, data:ArraySegment, nextUndoRecord:SequenceNumber, previousRecord:SequenceNumber, recordAppendOptions:RecordAppendOptions, reservations:ReservationCollection = ...) -> SequenceNumber:
        """
        Append(self: IRecordSequence, data: ArraySegment[Byte], nextUndoRecord: SequenceNumber, previousRecord: SequenceNumber, recordAppendOptions: RecordAppendOptions) -> SequenceNumber
        Append(self: IRecordSequence, data: ArraySegment[Byte], nextUndoRecord: SequenceNumber, previousRecord: SequenceNumber, recordAppendOptions: RecordAppendOptions, reservations: ReservationCollection) -> SequenceNumber
        Append(self: IRecordSequence, data: IList[ArraySegment[Byte]], nextUndoRecord: SequenceNumber, previousRecord: SequenceNumber, recordAppendOptions: RecordAppendOptions) -> SequenceNumber
        Append(self: IRecordSequence, data: IList[ArraySegment[Byte]], nextUndoRecord: SequenceNumber, previousRecord: SequenceNumber, recordAppendOptions: RecordAppendOptions, reservations: ReservationCollection) -> SequenceNumber
        """
        ...

    def BeginAppend(self, data, nextUndoRecord, *__args) -> IAsyncResult:
        """
        BeginAppend(self: IRecordSequence, data: ArraySegment[Byte], nextUndoRecord: SequenceNumber, previousRecord: SequenceNumber, recordAppendOptions: RecordAppendOptions, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginAppend(self: IRecordSequence, data: ArraySegment[Byte], nextUndoRecord: SequenceNumber, previousRecord: SequenceNumber, recordAppendOptions: RecordAppendOptions, reservations: ReservationCollection, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginAppend(self: IRecordSequence, data: IList[ArraySegment[Byte]], nextUndoRecord: SequenceNumber, previousRecord: SequenceNumber, recordAppendOptions: RecordAppendOptions, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginAppend(self: IRecordSequence, data: IList[ArraySegment[Byte]], nextUndoRecord: SequenceNumber, previousUndoRecord: SequenceNumber, recordAppendOptions: RecordAppendOptions, reservations: ReservationCollection, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginFlush(self, sequenceNumber:SequenceNumber, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginFlush(self: IRecordSequence, sequenceNumber: SequenceNumber, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginReserveAndAppend(self, data:ArraySegment, nextUndoRecord:SequenceNumber, previousRecord:SequenceNumber, recordAppendOptions:RecordAppendOptions, reservationCollection:ReservationCollection, reservations:Array, callback:AsyncCallback, state:object) -> IAsyncResult:
        """
        BeginReserveAndAppend(self: IRecordSequence, data: ArraySegment[Byte], nextUndoRecord: SequenceNumber, previousRecord: SequenceNumber, recordAppendOptions: RecordAppendOptions, reservationCollection: ReservationCollection, reservations: Array[Int64], callback: AsyncCallback, state: object) -> IAsyncResult
        BeginReserveAndAppend(self: IRecordSequence, data: IList[ArraySegment[Byte]], nextUndoRecord: SequenceNumber, previousRecord: SequenceNumber, recordAppendOptions: RecordAppendOptions, reservationCollection: ReservationCollection, reservations: Array[Int64], callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def BeginWriteRestartArea(self, data:ArraySegment, newBaseSequenceNumber:SequenceNumber, reservation:ReservationCollection, callback:AsyncCallback, state:object) -> IAsyncResult:
        """
        BeginWriteRestartArea(self: IRecordSequence, data: ArraySegment[Byte], newBaseSequenceNumber: SequenceNumber, reservation: ReservationCollection, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginWriteRestartArea(self: IRecordSequence, data: IList[ArraySegment[Byte]], newBaseSequenceNumber: SequenceNumber, reservation: ReservationCollection, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def CreateReservationCollection(self) -> ReservationCollection:
        """ CreateReservationCollection(self: IRecordSequence) -> ReservationCollection """
        ...

    def EndAppend(self, result:IAsyncResult) -> SequenceNumber:
        """ EndAppend(self: IRecordSequence, result: IAsyncResult) -> SequenceNumber """
        ...

    def EndFlush(self, result:IAsyncResult) -> SequenceNumber:
        """ EndFlush(self: IRecordSequence, result: IAsyncResult) -> SequenceNumber """
        ...

    def EndReserveAndAppend(self, result:IAsyncResult) -> SequenceNumber:
        """ EndReserveAndAppend(self: IRecordSequence, result: IAsyncResult) -> SequenceNumber """
        ...

    def EndWriteRestartArea(self, result:IAsyncResult) -> SequenceNumber:
        """ EndWriteRestartArea(self: IRecordSequence, result: IAsyncResult) -> SequenceNumber """
        ...

    def Flush(self, sequenceNumber:SequenceNumber = ...) -> SequenceNumber:
        """
        Flush(self: IRecordSequence) -> SequenceNumber
        Flush(self: IRecordSequence, sequenceNumber: SequenceNumber) -> SequenceNumber
        """
        ...

    def ReadLogRecords(self, start:SequenceNumber, logRecordEnum:LogRecordEnumeratorType) -> IEnumerable:
        """ ReadLogRecords(self: IRecordSequence, start: SequenceNumber, logRecordEnum: LogRecordEnumeratorType) -> IEnumerable[LogRecord] """
        ...

    def ReadRestartAreas(self) -> IEnumerable:
        """ ReadRestartAreas(self: IRecordSequence) -> IEnumerable[LogRecord] """
        ...

    def ReserveAndAppend(self, data:ArraySegment, nextUndoRecord:SequenceNumber, previousRecord:SequenceNumber, recordAppendOptions:RecordAppendOptions, reservationCollection:ReservationCollection, reservations:Array) -> SequenceNumber:
        """
        ReserveAndAppend(self: IRecordSequence, data: ArraySegment[Byte], nextUndoRecord: SequenceNumber, previousRecord: SequenceNumber, recordAppendOptions: RecordAppendOptions, reservationCollection: ReservationCollection, *reservations: Array[Int64]) -> SequenceNumber
        ReserveAndAppend(self: IRecordSequence, data: IList[ArraySegment[Byte]], nextUndoRecord: SequenceNumber, previousRecord: SequenceNumber, recordAppendOptions: RecordAppendOptions, reservationCollection: ReservationCollection, *reservations: Array[Int64]) -> SequenceNumber
        """
        ...

    def WriteRestartArea(self, data:ArraySegment, newBaseSequenceNumber:SequenceNumber = ..., reservation:ReservationCollection = ...) -> SequenceNumber:
        """
        WriteRestartArea(self: IRecordSequence, data: ArraySegment[Byte]) -> SequenceNumber
        WriteRestartArea(self: IRecordSequence, data: IList[ArraySegment[Byte]]) -> SequenceNumber
        WriteRestartArea(self: IRecordSequence, data: ArraySegment[Byte], newBaseSequenceNumber: SequenceNumber) -> SequenceNumber
        WriteRestartArea(self: IRecordSequence, data: IList[ArraySegment[Byte]], newBaseSequenceNumber: SequenceNumber) -> SequenceNumber
        WriteRestartArea(self: IRecordSequence, data: ArraySegment[Byte], newBaseSequenceNumber: SequenceNumber, reservation: ReservationCollection) -> SequenceNumber
        WriteRestartArea(self: IRecordSequence, data: IList[ArraySegment[Byte]], newBaseSequenceNumber: SequenceNumber, reservation: ReservationCollection) -> SequenceNumber
        """
        ...

    TailPinned = ...


class LogArchiveSnapshot: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ArchiveRegions(self) -> IEnumerable:
        """ Get: ArchiveRegions(self: LogArchiveSnapshot) -> IEnumerable[FileRegion] """
        ...

    @property
    def ArchiveTail(self) -> SequenceNumber:
        """ Get: ArchiveTail(self: LogArchiveSnapshot) -> SequenceNumber """
        ...

    @property
    def BaseSequenceNumber(self) -> SequenceNumber:
        """ Get: BaseSequenceNumber(self: LogArchiveSnapshot) -> SequenceNumber """
        ...

    @property
    def LastSequenceNumber(self) -> SequenceNumber:
        """ Get: LastSequenceNumber(self: LogArchiveSnapshot) -> SequenceNumber """
        ...



class LogExtent: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Path(self) -> str:
        """ Get: Path(self: LogExtent) -> str """
        ...

    @property
    def Size(self) -> Int64:
        """ Get: Size(self: LogExtent) -> Int64 """
        ...

    @property
    def State(self) -> LogExtentState:
        """ Get: State(self: LogExtent) -> LogExtentState """
        ...



class LogExtentCollection(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: LogExtentCollection) -> int """
        ...

    @property
    def FreeCount(self) -> int:
        """ Get: FreeCount(self: LogExtentCollection) -> int """
        ...


    def Add(self, path:str, size:Int64 = ...): # -> 
        """ Add(self: LogExtentCollection, path: str)Add(self: LogExtentCollection, path: str, size: Int64) """
        ...

    def Remove(self, *__args): # -> 
        """ Remove(self: LogExtentCollection, path: str, force: bool)Remove(self: LogExtentCollection, extent: LogExtent, force: bool) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[LogExtent](enumerable: IEnumerable[LogExtent], value: LogExtent) -> bool """
        ...


class LogExtentState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LogExtentState, values: Active (4), ActivePendingDelete (8), Inactive (2), Initializing (1), PendingArchive (16), PendingArchiveAndDelete (32), Unknown (0) """
    Active: LogExtentState = ...
    ActivePendingDelete: LogExtentState = ...
    Inactive: LogExtentState = ...
    Initializing: LogExtentState = ...
    PendingArchive: LogExtentState = ...
    PendingArchiveAndDelete: LogExtentState = ...
    Unknown: LogExtentState = ...
    value__ = ...


class LogPolicy: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AutoGrow(self) -> bool:
        """
        Get: AutoGrow(self: LogPolicy) -> bool
        Set: AutoGrow(self: LogPolicy) = value
        """
        ...

    @property
    def AutoShrinkPercentage(self) -> int:
        """
        Get: AutoShrinkPercentage(self: LogPolicy) -> int
        Set: AutoShrinkPercentage(self: LogPolicy) = value
        """
        ...

    @property
    def GrowthRate(self) -> PolicyUnit:
        """
        Get: GrowthRate(self: LogPolicy) -> PolicyUnit
        Set: GrowthRate(self: LogPolicy) = value
        """
        ...

    @property
    def MaximumExtentCount(self) -> int:
        """
        Get: MaximumExtentCount(self: LogPolicy) -> int
        Set: MaximumExtentCount(self: LogPolicy) = value
        """
        ...

    @property
    def MinimumExtentCount(self) -> int:
        """
        Get: MinimumExtentCount(self: LogPolicy) -> int
        Set: MinimumExtentCount(self: LogPolicy) = value
        """
        ...

    @property
    def NewExtentPrefix(self) -> str:
        """
        Get: NewExtentPrefix(self: LogPolicy) -> str
        Set: NewExtentPrefix(self: LogPolicy) = value
        """
        ...

    @property
    def NextExtentSuffix(self) -> Int64:
        """
        Get: NextExtentSuffix(self: LogPolicy) -> Int64
        Set: NextExtentSuffix(self: LogPolicy) = value
        """
        ...

    @property
    def PinnedTailThreshold(self) -> PolicyUnit:
        """
        Get: PinnedTailThreshold(self: LogPolicy) -> PolicyUnit
        Set: PinnedTailThreshold(self: LogPolicy) = value
        """
        ...


    def Commit(self): # -> 
        """ Commit(self: LogPolicy) """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: LogPolicy) """
        ...


class LogRecord(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Data(self) -> Stream:
        """ Get: Data(self: LogRecord) -> Stream """
        ...

    @property
    def Previous(self) -> SequenceNumber:
        """ Get: Previous(self: LogRecord) -> SequenceNumber """
        ...

    @property
    def SequenceNumber(self) -> SequenceNumber:
        """ Get: SequenceNumber(self: LogRecord) -> SequenceNumber """
        ...

    @property
    def User(self) -> SequenceNumber:
        """ Get: User(self: LogRecord) -> SequenceNumber """
        ...



class LogRecordEnumeratorType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LogRecordEnumeratorType, values: Next (2), Previous (1), User (0) """
    Next: LogRecordEnumeratorType = ...
    Previous: LogRecordEnumeratorType = ...
    User: LogRecordEnumeratorType = ...
    value__ = ...


class LogRecordSequence(IRecordSequence): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    LogRecordSequence(path: str, mode: FileMode)
    LogRecordSequence(path: str, mode: FileMode, access: FileAccess)
    LogRecordSequence(path: str, mode: FileMode, access: FileAccess, share: FileShare)
    LogRecordSequence(path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, bufferCount: int)
    LogRecordSequence(path: str, mode: FileMode, access: FileAccess, share: FileShare, bufferSize: int, bufferCount: int, fileSecurity: FileSecurity)
    LogRecordSequence(logStore: LogStore)
    LogRecordSequence(logStore: LogStore, bufferSize: int, bufferCount: int)
    """
    @property
    def LogStore(self) -> LogStore:
        """ Get: LogStore(self: LogRecordSequence) -> LogStore """
        ...


    def Dispose(self): # -> 
        """ Dispose(self: LogRecordSequence) """
        ...

    def SetLastRecord(self, sequenceNumber:SequenceNumber): # -> 
        """ SetLastRecord(self: LogRecordSequence, sequenceNumber: SequenceNumber) """
        ...

    TailPinned = ...


class LogStore(IDisposable): # skipped bases: <type 'object'>
    """
    LogStore(path: str, mode: FileMode)
    LogStore(path: str, mode: FileMode, access: FileAccess)
    LogStore(path: str, mode: FileMode, access: FileAccess, share: FileShare)
    LogStore(path: str, mode: FileMode, access: FileAccess, share: FileShare, fileSecurity: FileSecurity)
    LogStore(handle: SafeFileHandle)
    """
    @property
    def Archivable(self) -> bool:
        """
        Get: Archivable(self: LogStore) -> bool
        Set: Archivable(self: LogStore) = value
        """
        ...

    @property
    def BaseSequenceNumber(self) -> SequenceNumber:
        """ Get: BaseSequenceNumber(self: LogStore) -> SequenceNumber """
        ...

    @property
    def Extents(self) -> LogExtentCollection:
        """ Get: Extents(self: LogStore) -> LogExtentCollection """
        ...

    @property
    def FreeBytes(self) -> Int64:
        """ Get: FreeBytes(self: LogStore) -> Int64 """
        ...

    @property
    def Handle(self) -> SafeFileHandle:
        """ Get: Handle(self: LogStore) -> SafeFileHandle """
        ...

    @property
    def LastSequenceNumber(self) -> SequenceNumber:
        """ Get: LastSequenceNumber(self: LogStore) -> SequenceNumber """
        ...

    @property
    def Length(self) -> Int64:
        """ Get: Length(self: LogStore) -> Int64 """
        ...

    @property
    def Policy(self) -> LogPolicy:
        """ Get: Policy(self: LogStore) -> LogPolicy """
        ...

    @property
    def StreamCount(self) -> int:
        """ Get: StreamCount(self: LogStore) -> int """
        ...


    def CreateLogArchiveSnapshot(self, first:SequenceNumber = ..., last:SequenceNumber = ...) -> LogArchiveSnapshot:
        """
        CreateLogArchiveSnapshot(self: LogStore) -> LogArchiveSnapshot
        CreateLogArchiveSnapshot(self: LogStore, first: SequenceNumber, last: SequenceNumber) -> LogArchiveSnapshot
        """
        ...

    @staticmethod
    def Delete(path:str): # -> 
        """ Delete(path: str) """
        ...

    def SetArchiveTail(self, archiveTail:SequenceNumber): # -> 
        """ SetArchiveTail(self: LogStore, archiveTail: SequenceNumber) """
        ...


class PolicyUnit: # skipped bases: <type 'object'>, <type 'object'>
    """ PolicyUnit(value: Int64, type: PolicyUnitType) """
    @property
    def Type(self) -> PolicyUnitType:
        """ Get: Type(self: PolicyUnit) -> PolicyUnitType """
        ...

    @property
    def Value(self) -> Int64:
        """ Get: Value(self: PolicyUnit) -> Int64 """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: PolicyUnit, obj: object) -> bool """
        ...

    @staticmethod
    def Extents(value:Int64) -> PolicyUnit:
        """ Extents(value: Int64) -> PolicyUnit """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: PolicyUnit) -> int """
        ...

    @staticmethod
    def Percentage(value:Int64) -> PolicyUnit:
        """ Percentage(value: Int64) -> PolicyUnit """
        ...

    def ToString(self) -> str:
        """ ToString(self: PolicyUnit) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PolicyUnitType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PolicyUnitType, values: Extents (0), Percentage (1) """
    Extents: PolicyUnitType = ...
    Percentage: PolicyUnitType = ...
    value__ = ...


class RecordAppendOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) RecordAppendOptions, values: ForceAppend (1), ForceFlush (2), None (0) """
    ForceAppend: RecordAppendOptions = ...
    ForceFlush: RecordAppendOptions = ...
    value__ = ...


class ReservationCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[Int64]'>, <type 'object'>
    """ no doc """
    def FreeReservation(self, *args): #cannot find CLR method
        """ FreeReservation(self: ReservationCollection, size: Int64) """
        ...

    def GetBestMatchingReservation(self, *args): #cannot find CLR method
        """ GetBestMatchingReservation(self: ReservationCollection, size: Int64) -> Int64 """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ReservationCollection) -> IEnumerator[Int64] """
        ...

    def MakeReservation(self, *args): #cannot find CLR method
        """ MakeReservation(self: ReservationCollection, size: Int64) """
        ...

    def ReservationFreed(self, *args): #cannot find CLR method
        """ ReservationFreed(self: ReservationCollection, size: Int64) """
        ...

    def ReservationMade(self, *args): #cannot find CLR method
        """ ReservationMade(self: ReservationCollection, size: Int64) """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class ReservationNotFoundException(ArgumentException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ReservationNotFoundException()
    ReservationNotFoundException(message: str)
    ReservationNotFoundException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class SequenceFullException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SequenceFullException()
    SequenceFullException(message: str)
    SequenceFullException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class SequenceNumber(IComparable): # skipped bases: <type 'object'>
    """ SequenceNumber(sequenceNumber: Array[Byte]) """
    @property
    def Invalid(self) -> SequenceNumber:
        """ Get: Invalid() -> SequenceNumber """
        ...


    def Equals(self, other:SequenceNumber) -> bool:
        """
        Equals(self: SequenceNumber, other: SequenceNumber) -> bool
        Equals(self: SequenceNumber, other: object) -> bool
        """
        ...

    def GetBytes(self) -> Array:
        """ GetBytes(self: SequenceNumber) -> Array[Byte] """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SequenceNumber) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ge__(self, *args): #cannot find CLR method
        ...

    def __gt__(self, *args): #cannot find CLR method
        ...

    def __le__(self, *args): #cannot find CLR method
        ...

    def __lt__(self, *args): #cannot find CLR method
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class TailPinnedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ TailPinnedEventArgs(sequenceNumber: SequenceNumber) """
    @property
    def TargetSequenceNumber(self) -> SequenceNumber:
        """ Get: TargetSequenceNumber(self: TailPinnedEventArgs) -> SequenceNumber """
        ...


    def __new__(cls, sequenceNumber:SequenceNumber) -> Self:
        """ __new__(cls: type, sequenceNumber: SequenceNumber) """
        ...


