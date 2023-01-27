# encoding: utf-8
# module Microsoft.SqlServer.Management.Trace calls itself Trace
# from Microsoft.SqlServer.ConnectionInfoExtended, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Common import (ConnectionInfoBase, 
    SqlServerManagementException)

from System import (Array, AsyncCallback, Byte, Char, DateTime, Decimal, Enum, 
    EventArgs, Guid, IAsyncResult, IDisposable, Int16, Int64, 
    MulticastDelegate, Single, TimeSpan, Type)

from System.Data import IDataReader, IDataRecord

from System.IO import Stream

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class IDataRecordChanger(IDataRecord): # skipped bases: <type 'object'>
    """ no doc """
    def SetValue(self, ordinal:int, value:object): # -> 
        """ SetValue(self: IDataRecordChanger, ordinal: int, value: object) """
        ...


class ITraceDataWriter: # skipped bases: <type 'object'>
    """ no doc """
    def Write(self) -> bool:
        """ Write(self: ITraceDataWriter) -> bool """
        ...

    WriteNotify = ...


class TraceEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CurrentRecord(self) -> IDataRecordChanger:
        """ Get: CurrentRecord(self: TraceEventArgs) -> IDataRecordChanger """
        ...

    @property
    def SkipRecord(self) -> bool:
        """
        Get: SkipRecord(self: TraceEventArgs) -> bool
        Set: SkipRecord(self: TraceEventArgs) = value
        """
        ...



class ReplayEventArgs(TraceEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RecordNumber(self) -> int:
        """ Get: RecordNumber(self: ReplayEventArgs) -> int """
        ...



class ReplayEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ReplayEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, args:ReplayEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ReplayEventHandler, sender: object, args: ReplayEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ReplayEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, args:ReplayEventArgs): # -> 
        """ Invoke(self: ReplayEventHandler, sender: object, args: ReplayEventArgs) """
        ...


class ReplayMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ReplayMode, values: ConnectionLevelSync (1), SequentialReplay (0) """
    ConnectionLevelSync: ReplayMode = ...
    SequentialReplay: ReplayMode = ...
    value__ = ...


class ReplayPauseHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ReplayPauseHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, args:EventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ReplayPauseHandler, sender: object, args: EventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ReplayPauseHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, args:EventArgs): # -> 
        """ Invoke(self: ReplayPauseHandler, sender: object, args: EventArgs) """
        ...


class ReplayResultEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ReplayResultEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, args:TraceEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ReplayResultEventHandler, sender: object, args: TraceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ReplayResultEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, args:TraceEventArgs): # -> 
        """ Invoke(self: ReplayResultEventHandler, sender: object, args: TraceEventArgs) """
        ...


class ReplayStartHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ReplayStartHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, args:EventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ReplayStartHandler, sender: object, args: EventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ReplayStartHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, args:EventArgs): # -> 
        """ Invoke(self: ReplayStartHandler, sender: object, args: EventArgs) """
        ...


class ReplayStopHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ReplayStopHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, args:EventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ReplayStopHandler, sender: object, args: EventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ReplayStopHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, args:EventArgs): # -> 
        """ Invoke(self: ReplayStopHandler, sender: object, args: EventArgs) """
        ...


class SqlTraceException(SqlServerManagementException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SqlTraceException()
    SqlTraceException(message: str)
    SqlTraceException(message: str, innerException: Exception)
    SqlTraceException(messageSource: Type, messageID: str)
    SqlTraceException(messageSource: Type, messageID: str, innerException: Exception)
    """
    @property
    def ProdVer(self):
        ...


    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    SerializeObjectState = ...


class SqlTraceFailToInstantiateTypeException(SqlTraceException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SqlTraceFailToInstantiateTypeException()
    SqlTraceFailToInstantiateTypeException(typeName: str)
    SqlTraceFailToInstantiateTypeException(typeName: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SqlTraceFailToLoadInstAPIAssemblyException(SqlTraceException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SqlTraceFailToLoadInstAPIAssemblyException()
    SqlTraceFailToLoadInstAPIAssemblyException(message: str)
    SqlTraceFailToLoadInstAPIAssemblyException(message: str, innerException: Exception)
    SqlTraceFailToLoadInstAPIAssemblyException(messageSource: Type, messageID: str)
    """
    SerializeObjectState = ...


class TraceReader(IDataReader): # skipped bases: <type 'IDisposable'>, <type 'IDataRecord'>, <type 'object'>
    """ TraceReader() """
    @property
    def FieldCount(self) -> int:
        """ Get: FieldCount(self: TraceReader) -> int """
        ...


    def Dispose(self): # -> 
        """ Dispose(self: TraceReader) """
        ...

    def GetBoolean(self, ordinal:int) -> bool:
        """ GetBoolean(self: TraceReader, ordinal: int) -> bool """
        ...

    def GetByte(self, ordinal:int) -> Byte:
        """ GetByte(self: TraceReader, ordinal: int) -> Byte """
        ...

    def GetBytes(self, ordinal:int, fieldOffset:Int64, buffer:Array, bufferoffset:int, length:int) -> Int64:
        """ GetBytes(self: TraceReader, ordinal: int, fieldOffset: Int64, buffer: Array[Byte], bufferoffset: int, length: int) -> Int64 """
        ...

    def GetChar(self, ordinal:int) -> Char:
        """ GetChar(self: TraceReader, ordinal: int) -> Char """
        ...

    def GetChars(self, ordinal, *__args) -> int:
        """
        GetChars(self: TraceReader, ordinal: int, buffer: Array[Char], length: int, bufferoffset: int, fieldoffset: int) -> int
        GetChars(self: TraceReader, ordinal: int, fieldoffset: Int64, buffer: Array[Char], bufferoffset: int, length: int) -> Int64
        """
        ...

    def GetData(self, ordinal:int) -> IDataReader:
        """ GetData(self: TraceReader, ordinal: int) -> IDataReader """
        ...

    def GetDataTypeName(self, ordinal:int) -> str:
        """ GetDataTypeName(self: TraceReader, ordinal: int) -> str """
        ...

    def GetDateTime(self, ordinal:int) -> DateTime:
        """ GetDateTime(self: TraceReader, ordinal: int) -> DateTime """
        ...

    def GetDecimal(self, ordinal:int) -> Decimal:
        """ GetDecimal(self: TraceReader, ordinal: int) -> Decimal """
        ...

    def GetDouble(self, ordinal:int) -> float:
        """ GetDouble(self: TraceReader, ordinal: int) -> float """
        ...

    def GetFieldType(self, ordinal:int) -> Type:
        """ GetFieldType(self: TraceReader, ordinal: int) -> Type """
        ...

    def GetFloat(self, ordinal:int) -> Single:
        """ GetFloat(self: TraceReader, ordinal: int) -> Single """
        ...

    def GetGuid(self, ordinal:int) -> Guid:
        """ GetGuid(self: TraceReader, ordinal: int) -> Guid """
        ...

    def GetInt16(self, ordinal:int) -> Int16:
        """ GetInt16(self: TraceReader, ordinal: int) -> Int16 """
        ...

    def GetInt32(self, ordinal:int) -> int:
        """ GetInt32(self: TraceReader, ordinal: int) -> int """
        ...

    def GetInt64(self, ordinal:int) -> Int64:
        """ GetInt64(self: TraceReader, ordinal: int) -> Int64 """
        ...

    def GetName(self, ordinal:int) -> str:
        """ GetName(self: TraceReader, ordinal: int) -> str """
        ...

    def GetOrdinal(self, name:str) -> int:
        """ GetOrdinal(self: TraceReader, name: str) -> int """
        ...

    def GetStream(self, ordinal:int) -> Stream:
        """ GetStream(self: TraceReader, ordinal: int) -> Stream """
        ...

    def GetString(self, ordinal:int) -> str:
        """ GetString(self: TraceReader, ordinal: int) -> str """
        ...

    def GetTimeSpan(self, ordinal:int) -> TimeSpan:
        """ GetTimeSpan(self: TraceReader, ordinal: int) -> TimeSpan """
        ...

    def GetValue(self, ordinal:int) -> object:
        """ GetValue(self: TraceReader, ordinal: int) -> object """
        ...

    def GetValues(self, values:Array) -> int:
        """ GetValues(self: TraceReader, values: Array[object]) -> int """
        ...

    def IsDBNull(self, ordinal:int) -> bool:
        """ IsDBNull(self: TraceReader, ordinal: int) -> bool """
        ...

    def IsNull(self, ordinal:int) -> bool:
        """ IsNull(self: TraceReader, ordinal: int) -> bool """
        ...

    def TranslateSubclass(self, eventClass:str, column:str, subclass:int) -> str:
        """ TranslateSubclass(self: TraceReader, eventClass: str, column: str, subclass: int) -> str """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    currentRow = ...


class TraceReaderWriter(TraceReader, ITraceDataWriter): # skipped bases: <type 'IDisposable'>, <type 'IDataReader'>, <type 'IDataRecord'>, <type 'object'>
    """ TraceReaderWriter() """
    currentRow = ...
    WriteNotify = ...


class TraceFile(TraceReaderWriter): # skipped bases: <type 'IDisposable'>, <type 'IDataReader'>, <type 'IDataRecord'>, <type 'ITraceDataWriter'>, <type 'object'>
    """ TraceFile() """
    def InitializeAsReader(self, fileName:str): # -> 
        """ InitializeAsReader(self: TraceFile, fileName: str) """
        ...

    def InitializeAsReplayOutputWriter(self, destinationFileName:str): # -> 
        """ InitializeAsReplayOutputWriter(self: TraceFile, destinationFileName: str) """
        ...

    def InitializeAsWriter(self, source:TraceReader, destinationFileName:str): # -> 
        """ InitializeAsWriter(self: TraceFile, source: TraceReader, destinationFileName: str) """
        ...

    currentRow = ...


class TraceReplay(IDisposable): # skipped bases: <type 'object'>
    """ TraceReplay() """
    @property
    def Connection(self) -> ConnectionInfoBase:
        """
        Get: Connection(self: TraceReplay) -> ConnectionInfoBase
        Set: Connection(self: TraceReplay) = value
        """
        ...

    @property
    def Options(self) -> TraceReplayOptions:
        """
        Get: Options(self: TraceReplay) -> TraceReplayOptions
        Set: Options(self: TraceReplay) = value
        """
        ...

    @property
    def OutputFile(self) -> TraceFile:
        """
        Get: OutputFile(self: TraceReplay) -> TraceFile
        Set: OutputFile(self: TraceReplay) = value
        """
        ...

    @property
    def OutputTable(self) -> TraceTable:
        """
        Get: OutputTable(self: TraceReplay) -> TraceTable
        Set: OutputTable(self: TraceReplay) = value
        """
        ...

    @property
    def Source(self) -> TraceReader:
        """
        Get: Source(self: TraceReplay) -> TraceReader
        Set: Source(self: TraceReplay) = value
        """
        ...


    def Pause(self): # -> 
        """ Pause(self: TraceReplay) """
        ...

    def Start(self): # -> 
        """ Start(self: TraceReplay) """
        ...

    def Stop(self): # -> 
        """ Stop(self: TraceReplay) """
        ...

    ReplayEvent = ...
    ReplayPause = ...
    ReplayResultEvent = ...
    ReplayStart = ...
    ReplayStop = ...


class TraceReplayOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ TraceReplayOptions() """
    @property
    def BlockedProcessesEnabled(self) -> bool:
        """
        Get: BlockedProcessesEnabled(self: TraceReplayOptions) -> bool
        Set: BlockedProcessesEnabled(self: TraceReplayOptions) = value
        """
        ...

    @property
    def BlockedProcessesWaitInterval(self) -> int:
        """
        Get: BlockedProcessesWaitInterval(self: TraceReplayOptions) -> int
        Set: BlockedProcessesWaitInterval(self: TraceReplayOptions) = value
        """
        ...

    @property
    def DisplayPerfEvent(self) -> bool:
        """
        Get: DisplayPerfEvent(self: TraceReplayOptions) -> bool
        Set: DisplayPerfEvent(self: TraceReplayOptions) = value
        """
        ...

    @property
    def HealthMonitorPollInterval(self) -> int:
        """
        Get: HealthMonitorPollInterval(self: TraceReplayOptions) -> int
        Set: HealthMonitorPollInterval(self: TraceReplayOptions) = value
        """
        ...

    @property
    def HealthMonitorWaitInterval(self) -> int:
        """
        Get: HealthMonitorWaitInterval(self: TraceReplayOptions) -> int
        Set: HealthMonitorWaitInterval(self: TraceReplayOptions) = value
        """
        ...

    @property
    def KeepResults(self) -> bool:
        """
        Get: KeepResults(self: TraceReplayOptions) -> bool
        Set: KeepResults(self: TraceReplayOptions) = value
        """
        ...

    @property
    def Mode(self) -> ReplayMode:
        """
        Get: Mode(self: TraceReplayOptions) -> ReplayMode
        Set: Mode(self: TraceReplayOptions) = value
        """
        ...

    @property
    def NumberOfReplayThreads(self) -> int:
        """
        Get: NumberOfReplayThreads(self: TraceReplayOptions) -> int
        Set: NumberOfReplayThreads(self: TraceReplayOptions) = value
        """
        ...



class TraceServer(TraceReader): # skipped bases: <type 'IDisposable'>, <type 'IDataReader'>, <type 'IDataRecord'>, <type 'object'>
    """ TraceServer() """
    def InitializeAsReader(self, serverConnInfo:ConnectionInfoBase, profileFileName:str): # -> 
        """ InitializeAsReader(self: TraceServer, serverConnInfo: ConnectionInfoBase, profileFileName: str) """
        ...

    def Pause(self): # -> 
        """ Pause(self: TraceServer) """
        ...

    def Restart(self): # -> 
        """ Restart(self: TraceServer) """
        ...

    def Stop(self): # -> 
        """ Stop(self: TraceServer) """
        ...

    currentRow = ...


class TraceTable(TraceReaderWriter): # skipped bases: <type 'IDisposable'>, <type 'IDataReader'>, <type 'IDataRecord'>, <type 'ITraceDataWriter'>, <type 'object'>
    """ TraceTable() """
    def InitializeAsReader(self, serverConnInfo:ConnectionInfoBase, tableName:str, tableOwner:str): # -> 
        """ InitializeAsReader(self: TraceTable, serverConnInfo: ConnectionInfoBase, tableName: str, tableOwner: str) """
        ...

    def InitializeAsReplayOutputWriter(self, serverConnInfo:ConnectionInfoBase, destinationTableName:str): # -> 
        """ InitializeAsReplayOutputWriter(self: TraceTable, serverConnInfo: ConnectionInfoBase, destinationTableName: str) """
        ...

    def InitializeAsWriter(self, source:TraceReader, serverConnInfo:ConnectionInfoBase, destinationTableName:str): # -> 
        """ InitializeAsWriter(self: TraceTable, source: TraceReader, serverConnInfo: ConnectionInfoBase, destinationTableName: str) """
        ...

    currentRow = ...


class WriteNotifyEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WriteNotifyEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, args:TraceEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WriteNotifyEventHandler, sender: object, args: TraceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WriteNotifyEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, args:TraceEventArgs): # -> 
        """ Invoke(self: WriteNotifyEventHandler, sender: object, args: TraceEventArgs) """
        ...


