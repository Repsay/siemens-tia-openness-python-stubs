# encoding: utf-8
# module System.Diagnostics.Eventing.Reader calls itself Reader
# from System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Byte, Enum, EventArgs, Guid, IDisposable, Int64, Nullable, 
    TimeSpan, Uri)

from System.Collections import IEnumerable, IList

from System.Globalization import CultureInfo

from System.Runtime.Serialization import ISerializable

from System.Security.Principal import SecurityIdentifier

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class EventBookmark(ISerializable): # skipped bases: <type 'object'>
    """ no doc """
    pass

class EventKeyword: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: EventKeyword) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: EventKeyword) -> str """
        ...

    @property
    def Value(self) -> Int64:
        """ Get: Value(self: EventKeyword) -> Int64 """
        ...



class EventLevel: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: EventLevel) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: EventLevel) -> str """
        ...

    @property
    def Value(self) -> int:
        """ Get: Value(self: EventLevel) -> int """
        ...



class EventLogConfiguration(IDisposable): # skipped bases: <type 'object'>
    """
    EventLogConfiguration(logName: str)
    EventLogConfiguration(logName: str, session: EventLogSession)
    """
    @property
    def IsClassicLog(self) -> bool:
        """ Get: IsClassicLog(self: EventLogConfiguration) -> bool """
        ...

    @property
    def IsEnabled(self) -> bool:
        """
        Get: IsEnabled(self: EventLogConfiguration) -> bool
        Set: IsEnabled(self: EventLogConfiguration) = value
        """
        ...

    @property
    def LogFilePath(self) -> str:
        """
        Get: LogFilePath(self: EventLogConfiguration) -> str
        Set: LogFilePath(self: EventLogConfiguration) = value
        """
        ...

    @property
    def LogIsolation(self) -> EventLogIsolation:
        """ Get: LogIsolation(self: EventLogConfiguration) -> EventLogIsolation """
        ...

    @property
    def LogMode(self) -> EventLogMode:
        """
        Get: LogMode(self: EventLogConfiguration) -> EventLogMode
        Set: LogMode(self: EventLogConfiguration) = value
        """
        ...

    @property
    def LogName(self) -> str:
        """ Get: LogName(self: EventLogConfiguration) -> str """
        ...

    @property
    def LogType(self) -> EventLogType:
        """ Get: LogType(self: EventLogConfiguration) -> EventLogType """
        ...

    @property
    def MaximumSizeInBytes(self) -> Int64:
        """
        Get: MaximumSizeInBytes(self: EventLogConfiguration) -> Int64
        Set: MaximumSizeInBytes(self: EventLogConfiguration) = value
        """
        ...

    @property
    def OwningProviderName(self) -> str:
        """ Get: OwningProviderName(self: EventLogConfiguration) -> str """
        ...

    @property
    def ProviderBufferSize(self) -> Nullable:
        """ Get: ProviderBufferSize(self: EventLogConfiguration) -> Nullable[int] """
        ...

    @property
    def ProviderControlGuid(self) -> Nullable:
        """ Get: ProviderControlGuid(self: EventLogConfiguration) -> Nullable[Guid] """
        ...

    @property
    def ProviderKeywords(self) -> Nullable:
        """
        Get: ProviderKeywords(self: EventLogConfiguration) -> Nullable[Int64]
        Set: ProviderKeywords(self: EventLogConfiguration) = value
        """
        ...

    @property
    def ProviderLatency(self) -> Nullable:
        """ Get: ProviderLatency(self: EventLogConfiguration) -> Nullable[int] """
        ...

    @property
    def ProviderLevel(self) -> Nullable:
        """
        Get: ProviderLevel(self: EventLogConfiguration) -> Nullable[int]
        Set: ProviderLevel(self: EventLogConfiguration) = value
        """
        ...

    @property
    def ProviderMaximumNumberOfBuffers(self) -> Nullable:
        """ Get: ProviderMaximumNumberOfBuffers(self: EventLogConfiguration) -> Nullable[int] """
        ...

    @property
    def ProviderMinimumNumberOfBuffers(self) -> Nullable:
        """ Get: ProviderMinimumNumberOfBuffers(self: EventLogConfiguration) -> Nullable[int] """
        ...

    @property
    def ProviderNames(self) -> IEnumerable:
        """ Get: ProviderNames(self: EventLogConfiguration) -> IEnumerable[str] """
        ...

    @property
    def SecurityDescriptor(self) -> str:
        """
        Get: SecurityDescriptor(self: EventLogConfiguration) -> str
        Set: SecurityDescriptor(self: EventLogConfiguration) = value
        """
        ...


    def SaveChanges(self): # -> 
        """ SaveChanges(self: EventLogConfiguration) """
        ...


class EventLogException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EventLogException()
    EventLogException(message: str)
    EventLogException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class EventLogInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> Nullable:
        """ Get: Attributes(self: EventLogInformation) -> Nullable[int] """
        ...

    @property
    def CreationTime(self) -> Nullable:
        """ Get: CreationTime(self: EventLogInformation) -> Nullable[DateTime] """
        ...

    @property
    def FileSize(self) -> Nullable:
        """ Get: FileSize(self: EventLogInformation) -> Nullable[Int64] """
        ...

    @property
    def IsLogFull(self) -> Nullable:
        """ Get: IsLogFull(self: EventLogInformation) -> Nullable[bool] """
        ...

    @property
    def LastAccessTime(self) -> Nullable:
        """ Get: LastAccessTime(self: EventLogInformation) -> Nullable[DateTime] """
        ...

    @property
    def LastWriteTime(self) -> Nullable:
        """ Get: LastWriteTime(self: EventLogInformation) -> Nullable[DateTime] """
        ...

    @property
    def OldestRecordNumber(self) -> Nullable:
        """ Get: OldestRecordNumber(self: EventLogInformation) -> Nullable[Int64] """
        ...

    @property
    def RecordCount(self) -> Nullable:
        """ Get: RecordCount(self: EventLogInformation) -> Nullable[Int64] """
        ...



class EventLogInvalidDataException(EventLogException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EventLogInvalidDataException()
    EventLogInvalidDataException(message: str)
    EventLogInvalidDataException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class EventLogIsolation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EventLogIsolation, values: Application (0), Custom (2), System (1) """
    Application: EventLogIsolation = ...
    Custom: EventLogIsolation = ...
    System: EventLogIsolation = ...
    value__ = ...


class EventLogLink: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: EventLogLink) -> str """
        ...

    @property
    def IsImported(self) -> bool:
        """ Get: IsImported(self: EventLogLink) -> bool """
        ...

    @property
    def LogName(self) -> str:
        """ Get: LogName(self: EventLogLink) -> str """
        ...



class EventLogMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EventLogMode, values: AutoBackup (1), Circular (0), Retain (2) """
    AutoBackup: EventLogMode = ...
    Circular: EventLogMode = ...
    Retain: EventLogMode = ...
    value__ = ...


class EventLogNotFoundException(EventLogException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EventLogNotFoundException()
    EventLogNotFoundException(message: str)
    EventLogNotFoundException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class EventLogPropertySelector(IDisposable): # skipped bases: <type 'object'>
    """ EventLogPropertySelector(propertyQueries: IEnumerable[str]) """
    pass

class EventLogProviderDisabledException(EventLogException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EventLogProviderDisabledException()
    EventLogProviderDisabledException(message: str)
    EventLogProviderDisabledException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class EventLogQuery: # skipped bases: <type 'object'>, <type 'object'>
    """
    EventLogQuery(path: str, pathType: PathType)
    EventLogQuery(path: str, pathType: PathType, query: str)
    """
    @property
    def ReverseDirection(self) -> bool:
        """
        Get: ReverseDirection(self: EventLogQuery) -> bool
        Set: ReverseDirection(self: EventLogQuery) = value
        """
        ...

    @property
    def Session(self) -> EventLogSession:
        """
        Get: Session(self: EventLogQuery) -> EventLogSession
        Set: Session(self: EventLogQuery) = value
        """
        ...

    @property
    def TolerateQueryErrors(self) -> bool:
        """
        Get: TolerateQueryErrors(self: EventLogQuery) -> bool
        Set: TolerateQueryErrors(self: EventLogQuery) = value
        """
        ...



class EventLogReader(IDisposable): # skipped bases: <type 'object'>
    """
    EventLogReader(path: str)
    EventLogReader(path: str, pathType: PathType)
    EventLogReader(eventQuery: EventLogQuery)
    EventLogReader(eventQuery: EventLogQuery, bookmark: EventBookmark)
    """
    @property
    def BatchSize(self) -> int:
        """
        Get: BatchSize(self: EventLogReader) -> int
        Set: BatchSize(self: EventLogReader) = value
        """
        ...

    @property
    def LogStatus(self) -> IList:
        """ Get: LogStatus(self: EventLogReader) -> IList[EventLogStatus] """
        ...


    def CancelReading(self): # -> 
        """ CancelReading(self: EventLogReader) """
        ...

    def ReadEvent(self, timeout:TimeSpan = ...) -> EventRecord:
        """
        ReadEvent(self: EventLogReader) -> EventRecord
        ReadEvent(self: EventLogReader, timeout: TimeSpan) -> EventRecord
        """
        ...

    def Seek(self, *__args:EventBookmark): # -> 
        """ Seek(self: EventLogReader, bookmark: EventBookmark)Seek(self: EventLogReader, bookmark: EventBookmark, offset: Int64)Seek(self: EventLogReader, origin: SeekOrigin, offset: Int64) """
        ...


class EventLogReadingException(EventLogException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EventLogReadingException()
    EventLogReadingException(message: str)
    EventLogReadingException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class EventRecord(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActivityId(self) -> Nullable:
        """ Get: ActivityId(self: EventRecord) -> Nullable[Guid] """
        ...

    @property
    def Bookmark(self) -> EventBookmark:
        """ Get: Bookmark(self: EventRecord) -> EventBookmark """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: EventRecord) -> int """
        ...

    @property
    def Keywords(self) -> Nullable:
        """ Get: Keywords(self: EventRecord) -> Nullable[Int64] """
        ...

    @property
    def KeywordsDisplayNames(self) -> IEnumerable:
        """ Get: KeywordsDisplayNames(self: EventRecord) -> IEnumerable[str] """
        ...

    @property
    def Level(self) -> Nullable:
        """ Get: Level(self: EventRecord) -> Nullable[Byte] """
        ...

    @property
    def LevelDisplayName(self) -> str:
        """ Get: LevelDisplayName(self: EventRecord) -> str """
        ...

    @property
    def LogName(self) -> str:
        """ Get: LogName(self: EventRecord) -> str """
        ...

    @property
    def MachineName(self) -> str:
        """ Get: MachineName(self: EventRecord) -> str """
        ...

    @property
    def Opcode(self) -> Nullable:
        """ Get: Opcode(self: EventRecord) -> Nullable[Int16] """
        ...

    @property
    def OpcodeDisplayName(self) -> str:
        """ Get: OpcodeDisplayName(self: EventRecord) -> str """
        ...

    @property
    def ProcessId(self) -> Nullable:
        """ Get: ProcessId(self: EventRecord) -> Nullable[int] """
        ...

    @property
    def Properties(self) -> IList:
        """ Get: Properties(self: EventRecord) -> IList[EventProperty] """
        ...

    @property
    def ProviderId(self) -> Nullable:
        """ Get: ProviderId(self: EventRecord) -> Nullable[Guid] """
        ...

    @property
    def ProviderName(self) -> str:
        """ Get: ProviderName(self: EventRecord) -> str """
        ...

    @property
    def Qualifiers(self) -> Nullable:
        """ Get: Qualifiers(self: EventRecord) -> Nullable[int] """
        ...

    @property
    def RecordId(self) -> Nullable:
        """ Get: RecordId(self: EventRecord) -> Nullable[Int64] """
        ...

    @property
    def RelatedActivityId(self) -> Nullable:
        """ Get: RelatedActivityId(self: EventRecord) -> Nullable[Guid] """
        ...

    @property
    def Task(self) -> Nullable:
        """ Get: Task(self: EventRecord) -> Nullable[int] """
        ...

    @property
    def TaskDisplayName(self) -> str:
        """ Get: TaskDisplayName(self: EventRecord) -> str """
        ...

    @property
    def ThreadId(self) -> Nullable:
        """ Get: ThreadId(self: EventRecord) -> Nullable[int] """
        ...

    @property
    def TimeCreated(self) -> Nullable:
        """ Get: TimeCreated(self: EventRecord) -> Nullable[DateTime] """
        ...

    @property
    def UserId(self) -> SecurityIdentifier:
        """ Get: UserId(self: EventRecord) -> SecurityIdentifier """
        ...

    @property
    def Version(self) -> Nullable:
        """ Get: Version(self: EventRecord) -> Nullable[Byte] """
        ...


    def FormatDescription(self, values:IEnumerable = ...) -> str:
        """
        FormatDescription(self: EventRecord) -> str
        FormatDescription(self: EventRecord, values: IEnumerable[object]) -> str
        """
        ...

    def ToXml(self) -> str:
        """ ToXml(self: EventRecord) -> str """
        ...


class EventLogRecord(EventRecord): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def ContainerLog(self) -> str:
        """ Get: ContainerLog(self: EventLogRecord) -> str """
        ...

    @property
    def MatchedQueryIds(self) -> IEnumerable:
        """ Get: MatchedQueryIds(self: EventLogRecord) -> IEnumerable[int] """
        ...


    def GetPropertyValues(self, propertySelector:EventLogPropertySelector) -> IList:
        """ GetPropertyValues(self: EventLogRecord, propertySelector: EventLogPropertySelector) -> IList[object] """
        ...


class EventLogSession(IDisposable): # skipped bases: <type 'object'>
    """
    EventLogSession()
    EventLogSession(server: str)
    EventLogSession(server: str, domain: str, user: str, password: SecureString, logOnType: SessionAuthentication)
    """
    @property
    def GlobalSession(self) -> EventLogSession:
        """ Get: GlobalSession() -> EventLogSession """
        ...


    def CancelCurrentOperations(self): # -> 
        """ CancelCurrentOperations(self: EventLogSession) """
        ...

    def ClearLog(self, logName:str, backupPath:str = ...): # -> 
        """ ClearLog(self: EventLogSession, logName: str)ClearLog(self: EventLogSession, logName: str, backupPath: str) """
        ...

    def ExportLog(self, path:str, pathType:PathType, query:str, targetFilePath:str, tolerateQueryErrors:bool = ...): # -> 
        """ ExportLog(self: EventLogSession, path: str, pathType: PathType, query: str, targetFilePath: str)ExportLog(self: EventLogSession, path: str, pathType: PathType, query: str, targetFilePath: str, tolerateQueryErrors: bool) """
        ...

    def ExportLogAndMessages(self, path:str, pathType:PathType, query:str, targetFilePath:str, tolerateQueryErrors:bool = ..., targetCultureInfo:CultureInfo = ...): # -> 
        """ ExportLogAndMessages(self: EventLogSession, path: str, pathType: PathType, query: str, targetFilePath: str)ExportLogAndMessages(self: EventLogSession, path: str, pathType: PathType, query: str, targetFilePath: str, tolerateQueryErrors: bool, targetCultureInfo: CultureInfo) """
        ...

    def GetLogInformation(self, logName:str, pathType:PathType) -> EventLogInformation:
        """ GetLogInformation(self: EventLogSession, logName: str, pathType: PathType) -> EventLogInformation """
        ...

    def GetLogNames(self) -> IEnumerable:
        """ GetLogNames(self: EventLogSession) -> IEnumerable[str] """
        ...

    def GetProviderNames(self) -> IEnumerable:
        """ GetProviderNames(self: EventLogSession) -> IEnumerable[str] """
        ...



class EventLogStatus: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def LogName(self) -> str:
        """ Get: LogName(self: EventLogStatus) -> str """
        ...

    @property
    def StatusCode(self) -> int:
        """ Get: StatusCode(self: EventLogStatus) -> int """
        ...



class EventLogType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EventLogType, values: Administrative (0), Analytical (2), Debug (3), Operational (1) """
    Administrative: EventLogType = ...
    Analytical: EventLogType = ...
    Debug: EventLogType = ...
    Operational: EventLogType = ...
    value__ = ...


class EventLogWatcher(IDisposable): # skipped bases: <type 'object'>
    """
    EventLogWatcher(path: str)
    EventLogWatcher(eventQuery: EventLogQuery)
    EventLogWatcher(eventQuery: EventLogQuery, bookmark: EventBookmark)
    EventLogWatcher(eventQuery: EventLogQuery, bookmark: EventBookmark, readExistingEvents: bool)
    """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: EventLogWatcher) -> bool
        Set: Enabled(self: EventLogWatcher) = value
        """
        ...


    EventRecordWritten = ...


class EventMetadata: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """ Get: Description(self: EventMetadata) -> str """
        ...

    @property
    def Id(self) -> Int64:
        """ Get: Id(self: EventMetadata) -> Int64 """
        ...

    @property
    def Keywords(self) -> IEnumerable:
        """ Get: Keywords(self: EventMetadata) -> IEnumerable[EventKeyword] """
        ...

    @property
    def Level(self) -> EventLevel:
        """ Get: Level(self: EventMetadata) -> EventLevel """
        ...

    @property
    def LogLink(self) -> EventLogLink:
        """ Get: LogLink(self: EventMetadata) -> EventLogLink """
        ...

    @property
    def Opcode(self) -> EventOpcode:
        """ Get: Opcode(self: EventMetadata) -> EventOpcode """
        ...

    @property
    def Task(self) -> EventTask:
        """ Get: Task(self: EventMetadata) -> EventTask """
        ...

    @property
    def Template(self) -> str:
        """ Get: Template(self: EventMetadata) -> str """
        ...

    @property
    def Version(self) -> Byte:
        """ Get: Version(self: EventMetadata) -> Byte """
        ...



class EventOpcode: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: EventOpcode) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: EventOpcode) -> str """
        ...

    @property
    def Value(self) -> int:
        """ Get: Value(self: EventOpcode) -> int """
        ...



class EventProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Value(self) -> object:
        """ Get: Value(self: EventProperty) -> object """
        ...



class EventRecordWrittenEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EventException(self) -> Exception:
        """ Get: EventException(self: EventRecordWrittenEventArgs) -> Exception """
        ...

    @property
    def EventRecord(self) -> EventRecord:
        """ Get: EventRecord(self: EventRecordWrittenEventArgs) -> EventRecord """
        ...



class EventTask: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: EventTask) -> str """
        ...

    @property
    def EventGuid(self) -> Guid:
        """ Get: EventGuid(self: EventTask) -> Guid """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: EventTask) -> str """
        ...

    @property
    def Value(self) -> int:
        """ Get: Value(self: EventTask) -> int """
        ...



class PathType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PathType, values: FilePath (2), LogName (1) """
    FilePath: PathType = ...
    LogName: PathType = ...
    value__ = ...


class ProviderMetadata(IDisposable): # skipped bases: <type 'object'>
    """
    ProviderMetadata(providerName: str)
    ProviderMetadata(providerName: str, session: EventLogSession, targetCultureInfo: CultureInfo)
    """
    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: ProviderMetadata) -> str """
        ...

    @property
    def Events(self) -> IEnumerable:
        """ Get: Events(self: ProviderMetadata) -> IEnumerable[EventMetadata] """
        ...

    @property
    def HelpLink(self) -> Uri:
        """ Get: HelpLink(self: ProviderMetadata) -> Uri """
        ...

    @property
    def Id(self) -> Guid:
        """ Get: Id(self: ProviderMetadata) -> Guid """
        ...

    @property
    def Keywords(self) -> IList:
        """ Get: Keywords(self: ProviderMetadata) -> IList[EventKeyword] """
        ...

    @property
    def Levels(self) -> IList:
        """ Get: Levels(self: ProviderMetadata) -> IList[EventLevel] """
        ...

    @property
    def LogLinks(self) -> IList:
        """ Get: LogLinks(self: ProviderMetadata) -> IList[EventLogLink] """
        ...

    @property
    def MessageFilePath(self) -> str:
        """ Get: MessageFilePath(self: ProviderMetadata) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ProviderMetadata) -> str """
        ...

    @property
    def Opcodes(self) -> IList:
        """ Get: Opcodes(self: ProviderMetadata) -> IList[EventOpcode] """
        ...

    @property
    def ParameterFilePath(self) -> str:
        """ Get: ParameterFilePath(self: ProviderMetadata) -> str """
        ...

    @property
    def ResourceFilePath(self) -> str:
        """ Get: ResourceFilePath(self: ProviderMetadata) -> str """
        ...

    @property
    def Tasks(self) -> IList:
        """ Get: Tasks(self: ProviderMetadata) -> IList[EventTask] """
        ...



class SessionAuthentication(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SessionAuthentication, values: Default (0), Kerberos (2), Negotiate (1), Ntlm (3) """
    Default: SessionAuthentication = ...
    Kerberos: SessionAuthentication = ...
    Negotiate: SessionAuthentication = ...
    Ntlm: SessionAuthentication = ...
    value__ = ...


class StandardEventKeywords(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) StandardEventKeywords, values: AuditFailure (4503599627370496), AuditSuccess (9007199254740992), CorrelationHint (4503599627370496), CorrelationHint2 (18014398509481984), EventLogClassic (36028797018963968), None (0), ResponseTime (281474976710656), Sqm (2251799813685248), WdiContext (562949953421312), WdiDiagnostic (1125899906842624) """
    AuditFailure: StandardEventKeywords = ...
    AuditSuccess: StandardEventKeywords = ...
    CorrelationHint: StandardEventKeywords = ...
    CorrelationHint2: StandardEventKeywords = ...
    EventLogClassic: StandardEventKeywords = ...
    ResponseTime: StandardEventKeywords = ...
    Sqm: StandardEventKeywords = ...
    value__ = ...
    WdiContext: StandardEventKeywords = ...
    WdiDiagnostic: StandardEventKeywords = ...


class StandardEventLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StandardEventLevel, values: Critical (1), Error (2), Informational (4), LogAlways (0), Verbose (5), Warning (3) """
    Critical: StandardEventLevel = ...
    Error: StandardEventLevel = ...
    Informational: StandardEventLevel = ...
    LogAlways: StandardEventLevel = ...
    value__ = ...
    Verbose: StandardEventLevel = ...
    Warning: StandardEventLevel = ...


class StandardEventOpcode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StandardEventOpcode, values: DataCollectionStart (3), DataCollectionStop (4), Extension (5), Info (0), Receive (240), Reply (6), Resume (7), Send (9), Start (1), Stop (2), Suspend (8) """
    DataCollectionStart: StandardEventOpcode = ...
    DataCollectionStop: StandardEventOpcode = ...
    Extension: StandardEventOpcode = ...
    Info: StandardEventOpcode = ...
    Receive: StandardEventOpcode = ...
    Reply: StandardEventOpcode = ...
    Resume: StandardEventOpcode = ...
    Send: StandardEventOpcode = ...
    Start: StandardEventOpcode = ...
    Stop: StandardEventOpcode = ...
    Suspend: StandardEventOpcode = ...
    value__ = ...


class StandardEventTask(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StandardEventTask, values: None (0) """
    value__ = ...


