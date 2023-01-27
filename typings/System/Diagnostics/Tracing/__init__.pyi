# encoding: utf-8
# module System.Diagnostics.Tracing calls itself Tracing
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Diagnostics.Tracing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Attribute, Byte, Enum, EventArgs, Guid, IDisposable, 
    Single, Type)

from System.Collections import IDictionary, IEnumerable

from System.Collections.ObjectModel import ReadOnlyCollection

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class EventActivityOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EventActivityOptions, values: Detachable (8), Disable (2), None (0), Recursive (4) """
    Detachable: EventActivityOptions = ...
    Disable: EventActivityOptions = ...
    Recursive: EventActivityOptions = ...
    value__ = ...


class EventAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EventAttribute(eventId: int) """
    @property
    def ActivityOptions(self) -> EventActivityOptions:
        """
        Get: ActivityOptions(self: EventAttribute) -> EventActivityOptions
        Set: ActivityOptions(self: EventAttribute) = value
        """
        ...

    @property
    def Channel(self) -> EventChannel:
        """
        Get: Channel(self: EventAttribute) -> EventChannel
        Set: Channel(self: EventAttribute) = value
        """
        ...

    @property
    def EventId(self) -> int:
        """ Get: EventId(self: EventAttribute) -> int """
        ...

    @property
    def Keywords(self) -> EventKeywords:
        """
        Get: Keywords(self: EventAttribute) -> EventKeywords
        Set: Keywords(self: EventAttribute) = value
        """
        ...

    @property
    def Level(self) -> EventLevel:
        """
        Get: Level(self: EventAttribute) -> EventLevel
        Set: Level(self: EventAttribute) = value
        """
        ...

    @property
    def Message(self) -> str:
        """
        Get: Message(self: EventAttribute) -> str
        Set: Message(self: EventAttribute) = value
        """
        ...

    @property
    def Opcode(self) -> EventOpcode:
        """
        Get: Opcode(self: EventAttribute) -> EventOpcode
        Set: Opcode(self: EventAttribute) = value
        """
        ...

    @property
    def Tags(self) -> EventTags:
        """
        Get: Tags(self: EventAttribute) -> EventTags
        Set: Tags(self: EventAttribute) = value
        """
        ...

    @property
    def Task(self) -> EventTask:
        """
        Get: Task(self: EventAttribute) -> EventTask
        Set: Task(self: EventAttribute) = value
        """
        ...

    @property
    def Version(self) -> Byte:
        """
        Get: Version(self: EventAttribute) -> Byte
        Set: Version(self: EventAttribute) = value
        """
        ...


    def __new__(cls, eventId:int) -> Self:
        """ __new__(cls: type, eventId: int) """
        ...


class EventChannel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EventChannel, values: Admin (16), Analytic (18), Debug (19), None (0), Operational (17) """
    Admin: EventChannel = ...
    Analytic: EventChannel = ...
    Debug: EventChannel = ...
    Operational: EventChannel = ...
    value__ = ...


class EventCommand(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EventCommand, values: Disable (-3), Enable (-2), SendManifest (-1), Update (0) """
    Disable: EventCommand = ...
    Enable: EventCommand = ...
    SendManifest: EventCommand = ...
    Update: EventCommand = ...
    value__ = ...


class EventCommandEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> IDictionary:
        """ Get: Arguments(self: EventCommandEventArgs) -> IDictionary[str, str] """
        ...

    @property
    def Command(self) -> EventCommand:
        """ Get: Command(self: EventCommandEventArgs) -> EventCommand """
        ...


    def DisableEvent(self, eventId:int) -> bool:
        """ DisableEvent(self: EventCommandEventArgs, eventId: int) -> bool """
        ...

    def EnableEvent(self, eventId:int) -> bool:
        """ EnableEvent(self: EventCommandEventArgs, eventId: int) -> bool """
        ...


class EventCounter: # skipped bases: <type 'object'>, <type 'object'>
    """ EventCounter(name: str, eventSource: EventSource) """
    def WriteMetric(self, value:Single): # -> 
        """ WriteMetric(self: EventCounter, value: Single) """
        ...


class EventDataAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EventDataAttribute() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: EventDataAttribute) -> str
        Set: Name(self: EventDataAttribute) = value
        """
        ...



class EventFieldAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EventFieldAttribute() """
    @property
    def Format(self) -> EventFieldFormat:
        """
        Get: Format(self: EventFieldAttribute) -> EventFieldFormat
        Set: Format(self: EventFieldAttribute) = value
        """
        ...

    @property
    def Tags(self) -> EventFieldTags:
        """
        Get: Tags(self: EventFieldAttribute) -> EventFieldTags
        Set: Tags(self: EventFieldAttribute) = value
        """
        ...



class EventFieldFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EventFieldFormat, values: Boolean (3), Default (0), Hexadecimal (4), HResult (15), Json (12), String (2), Xml (11) """
    Boolean: EventFieldFormat = ...
    Default: EventFieldFormat = ...
    Hexadecimal: EventFieldFormat = ...
    HResult: EventFieldFormat = ...
    Json: EventFieldFormat = ...
    String: EventFieldFormat = ...
    value__ = ...
    Xml: EventFieldFormat = ...


class EventFieldTags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EventFieldTags, values: None (0) """
    value__ = ...


class EventIgnoreAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EventIgnoreAttribute() """
    pass

class EventKeywords(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EventKeywords, values: All (-1), AuditFailure (4503599627370496), AuditSuccess (9007199254740992), CorrelationHint (4503599627370496), EventLogClassic (36028797018963968), MicrosoftTelemetry (562949953421312), None (0), Sqm (2251799813685248), WdiContext (562949953421312), WdiDiagnostic (1125899906842624) """
    All: EventKeywords = ...
    AuditFailure: EventKeywords = ...
    AuditSuccess: EventKeywords = ...
    CorrelationHint: EventKeywords = ...
    EventLogClassic: EventKeywords = ...
    MicrosoftTelemetry: EventKeywords = ...
    Sqm: EventKeywords = ...
    value__ = ...
    WdiContext: EventKeywords = ...
    WdiDiagnostic: EventKeywords = ...


class EventLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EventLevel, values: Critical (1), Error (2), Informational (4), LogAlways (0), Verbose (5), Warning (3) """
    Critical: EventLevel = ...
    Error: EventLevel = ...
    Informational: EventLevel = ...
    LogAlways: EventLevel = ...
    value__ = ...
    Verbose: EventLevel = ...
    Warning: EventLevel = ...


class EventListener(IDisposable): # skipped bases: <type 'object'>
    """ EventListener() """
    def DisableEvents(self, eventSource:EventSource): # -> 
        """ DisableEvents(self: EventListener, eventSource: EventSource) """
        ...

    def EnableEvents(self, eventSource:EventSource, level:EventLevel, matchAnyKeyword:EventKeywords = ..., arguments:IDictionary = ...): # -> 
        """ EnableEvents(self: EventListener, eventSource: EventSource, level: EventLevel)EnableEvents(self: EventListener, eventSource: EventSource, level: EventLevel, matchAnyKeyword: EventKeywords)EnableEvents(self: EventListener, eventSource: EventSource, level: EventLevel, matchAnyKeyword: EventKeywords, arguments: IDictionary[str, str]) """
        ...

    @staticmethod
    def EventSourceIndex(eventSource:EventSource) -> int:
        """ EventSourceIndex(eventSource: EventSource) -> int """
        ...

    def OnEventSourceCreated(self, *args): #cannot find CLR method
        """ OnEventSourceCreated(self: EventListener, eventSource: EventSource) """
        ...

    def OnEventWritten(self, *args): #cannot find CLR method
        """ OnEventWritten(self: EventListener, eventData: EventWrittenEventArgs) """
        ...

    EventSourceCreated = ...
    EventWritten = ...


class EventManifestOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EventManifestOptions, values: AllCultures (2), AllowEventSourceOverride (8), None (0), OnlyIfNeededForRegistration (4), Strict (1) """
    AllCultures: EventManifestOptions = ...
    AllowEventSourceOverride: EventManifestOptions = ...
    OnlyIfNeededForRegistration: EventManifestOptions = ...
    Strict: EventManifestOptions = ...
    value__ = ...


class EventOpcode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EventOpcode, values: DataCollectionStart (3), DataCollectionStop (4), Extension (5), Info (0), Receive (240), Reply (6), Resume (7), Send (9), Start (1), Stop (2), Suspend (8) """
    DataCollectionStart: EventOpcode = ...
    DataCollectionStop: EventOpcode = ...
    Extension: EventOpcode = ...
    Info: EventOpcode = ...
    Receive: EventOpcode = ...
    Reply: EventOpcode = ...
    Resume: EventOpcode = ...
    Send: EventOpcode = ...
    Start: EventOpcode = ...
    Stop: EventOpcode = ...
    Suspend: EventOpcode = ...
    value__ = ...


class EventSource(IDisposable): # skipped bases: <type 'object'>
    """
    EventSource(eventSourceName: str)
    EventSource(eventSourceName: str, config: EventSourceSettings)
    EventSource(eventSourceName: str, config: EventSourceSettings, *traits: Array[str])
    """
    @property
    def ConstructionException(self) -> Exception:
        """ Get: ConstructionException(self: EventSource) -> Exception """
        ...

    @property
    def CurrentThreadActivityId(self) -> Guid:
        """ Get: CurrentThreadActivityId() -> Guid """
        ...

    @property
    def Guid(self) -> Guid:
        """ Get: Guid(self: EventSource) -> Guid """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: EventSource) -> str """
        ...

    @property
    def Settings(self) -> EventSourceSettings:
        """ Get: Settings(self: EventSource) -> EventSourceSettings """
        ...


    def EventData(self, *args): #cannot find CLR method
        """ no doc """
        ...

    @staticmethod
    def GenerateManifest(eventSourceType:Type, assemblyPathToIncludeInManifest:str, flags:EventManifestOptions = ...) -> str:
        """
        GenerateManifest(eventSourceType: Type, assemblyPathToIncludeInManifest: str) -> str
        GenerateManifest(eventSourceType: Type, assemblyPathToIncludeInManifest: str, flags: EventManifestOptions) -> str
        """
        ...

    @staticmethod
    def GetGuid(eventSourceType:Type) -> Guid:
        """ GetGuid(eventSourceType: Type) -> Guid """
        ...

    @staticmethod
    def GetName(eventSourceType:Type) -> str:
        """ GetName(eventSourceType: Type) -> str """
        ...

    @staticmethod
    def GetSources() -> IEnumerable:
        """ GetSources() -> IEnumerable[EventSource] """
        ...

    def GetTrait(self, key:str) -> str:
        """ GetTrait(self: EventSource, key: str) -> str """
        ...

    def IsEnabled(self, level:EventLevel = ..., keywords:EventKeywords = ..., channel:EventChannel = ...) -> bool:
        """
        IsEnabled(self: EventSource) -> bool
        IsEnabled(self: EventSource, level: EventLevel, keywords: EventKeywords) -> bool
        IsEnabled(self: EventSource, level: EventLevel, keywords: EventKeywords, channel: EventChannel) -> bool
        """
        ...

    def OnEventCommand(self, *args): #cannot find CLR method
        """ OnEventCommand(self: EventSource, command: EventCommandEventArgs) """
        ...

    @staticmethod
    def SendCommand(eventSource:EventSource, command:EventCommand, commandArguments:IDictionary): # -> 
        """ SendCommand(eventSource: EventSource, command: EventCommand, commandArguments: IDictionary[str, str]) """
        ...

    @staticmethod
    def SetCurrentThreadActivityId(activityId, oldActivityThatWillContinue=None): # -> 
        """ SetCurrentThreadActivityId(activityId: Guid)SetCurrentThreadActivityId(activityId: Guid) -> Guid """
        ...

    def ToString(self) -> str:
        """ ToString(self: EventSource) -> str """
        ...

    def Write(self, eventName:str, *__args:EventSourceOptions): # -> 
        """
        Write(self: EventSource, eventName: str)Write(self: EventSource, eventName: str, options: EventSourceOptions)Write[T](self: EventSource, eventName: str, data: T)Write[T](self: EventSource, eventName: str, options: EventSourceOptions, data: T)Write[T](self: EventSource, eventName: str, options: EventSourceOptions, data: T) -> (EventSourceOptions, T)
        Write[T](self: EventSource, eventName: str, options: EventSourceOptions, activityId: Guid, relatedActivityId: Guid, data: T) -> (EventSourceOptions, Guid, Guid, T)
        """
        ...

    def WriteEvent(self, *args): #cannot find CLR method
        """ WriteEvent(self: EventSource, eventId: int)WriteEvent(self: EventSource, eventId: int, arg1: Array[Byte])WriteEvent(self: EventSource, eventId: int, arg1: int, arg2: str)WriteEvent(self: EventSource, eventId: int, arg1: Int64, arg2: str)WriteEvent(self: EventSource, eventId: int, arg1: str, arg2: Int64)WriteEvent(self: EventSource, eventId: int, arg1: str, arg2: int, arg3: int)WriteEvent(self: EventSource, eventId: int, arg1: str, arg2: int)WriteEvent(self: EventSource, eventId: int, arg1: str, arg2: str, arg3: str)WriteEvent(self: EventSource, eventId: int, arg1: str, arg2: str)WriteEvent(self: EventSource, eventId: int, arg1: str)WriteEvent(self: EventSource, eventId: int, arg1: Int64, arg2: Int64, arg3: Int64)WriteEvent(self: EventSource, eventId: int, arg1: Int64, arg2: Int64)WriteEvent(self: EventSource, eventId: int, arg1: Int64)WriteEvent(self: EventSource, eventId: int, arg1: int, arg2: int, arg3: int)WriteEvent(self: EventSource, eventId: int, arg1: int, arg2: int)WriteEvent(self: EventSource, eventId: int, arg1: int)WriteEvent(self: EventSource, eventId: int, arg1: Int64, arg2: Array[Byte])WriteEvent(self: EventSource, eventId: int, *args: Array[object]) """
        ...

    def WriteEventCore(self, *args): #cannot find CLR method
        """ WriteEventCore(self: EventSource, eventId: int, eventDataCount: int, data: EventData*) """
        ...

    def WriteEventWithRelatedActivityId(self, *args): #cannot find CLR method
        """ WriteEventWithRelatedActivityId(self: EventSource, eventId: int, relatedActivityId: Guid, *args: Array[object]) """
        ...

    def WriteEventWithRelatedActivityIdCore(self, *args): #cannot find CLR method
        """ WriteEventWithRelatedActivityIdCore(self: EventSource, eventId: int, relatedActivityId: Guid*, eventDataCount: int, data: EventData*) """
        ...

    EventCommandExecuted = ...


class EventSourceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EventSourceAttribute() """
    @property
    def Guid(self) -> str:
        """
        Get: Guid(self: EventSourceAttribute) -> str
        Set: Guid(self: EventSourceAttribute) = value
        """
        ...

    @property
    def LocalizationResources(self) -> str:
        """
        Get: LocalizationResources(self: EventSourceAttribute) -> str
        Set: LocalizationResources(self: EventSourceAttribute) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: EventSourceAttribute) -> str
        Set: Name(self: EventSourceAttribute) = value
        """
        ...



class EventSourceCreatedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ EventSourceCreatedEventArgs() """
    @property
    def EventSource(self) -> EventSource:
        """ Get: EventSource(self: EventSourceCreatedEventArgs) -> EventSource """
        ...



class EventSourceException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EventSourceException()
    EventSourceException(message: str)
    EventSourceException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class EventSourceOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ActivityOptions(self) -> EventActivityOptions:
        """
        Get: ActivityOptions(self: EventSourceOptions) -> EventActivityOptions
        Set: ActivityOptions(self: EventSourceOptions) = value
        """
        ...

    @property
    def Keywords(self) -> EventKeywords:
        """
        Get: Keywords(self: EventSourceOptions) -> EventKeywords
        Set: Keywords(self: EventSourceOptions) = value
        """
        ...

    @property
    def Level(self) -> EventLevel:
        """
        Get: Level(self: EventSourceOptions) -> EventLevel
        Set: Level(self: EventSourceOptions) = value
        """
        ...

    @property
    def Opcode(self) -> EventOpcode:
        """
        Get: Opcode(self: EventSourceOptions) -> EventOpcode
        Set: Opcode(self: EventSourceOptions) = value
        """
        ...

    @property
    def Tags(self) -> EventTags:
        """
        Get: Tags(self: EventSourceOptions) -> EventTags
        Set: Tags(self: EventSourceOptions) = value
        """
        ...



class EventSourceSettings(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EventSourceSettings, values: Default (0), EtwManifestEventFormat (4), EtwSelfDescribingEventFormat (8), ThrowOnEventWriteErrors (1) """
    Default: EventSourceSettings = ...
    EtwManifestEventFormat: EventSourceSettings = ...
    EtwSelfDescribingEventFormat: EventSourceSettings = ...
    ThrowOnEventWriteErrors: EventSourceSettings = ...
    value__ = ...


class EventTags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EventTags, values: None (0) """
    value__ = ...


class EventTask(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EventTask, values: None (0) """
    value__ = ...


class EventWrittenEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActivityId(self) -> Guid:
        """ Get: ActivityId(self: EventWrittenEventArgs) -> Guid """
        ...

    @property
    def Channel(self) -> EventChannel:
        """ Get: Channel(self: EventWrittenEventArgs) -> EventChannel """
        ...

    @property
    def EventId(self) -> int:
        """ Get: EventId(self: EventWrittenEventArgs) -> int """
        ...

    @property
    def EventName(self) -> str:
        """ Get: EventName(self: EventWrittenEventArgs) -> str """
        ...

    @property
    def EventSource(self) -> EventSource:
        """ Get: EventSource(self: EventWrittenEventArgs) -> EventSource """
        ...

    @property
    def Keywords(self) -> EventKeywords:
        """ Get: Keywords(self: EventWrittenEventArgs) -> EventKeywords """
        ...

    @property
    def Level(self) -> EventLevel:
        """ Get: Level(self: EventWrittenEventArgs) -> EventLevel """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: EventWrittenEventArgs) -> str """
        ...

    @property
    def Opcode(self) -> EventOpcode:
        """ Get: Opcode(self: EventWrittenEventArgs) -> EventOpcode """
        ...

    @property
    def Payload(self) -> ReadOnlyCollection:
        """ Get: Payload(self: EventWrittenEventArgs) -> ReadOnlyCollection[object] """
        ...

    @property
    def PayloadNames(self) -> ReadOnlyCollection:
        """ Get: PayloadNames(self: EventWrittenEventArgs) -> ReadOnlyCollection[str] """
        ...

    @property
    def RelatedActivityId(self) -> Guid:
        """ Get: RelatedActivityId(self: EventWrittenEventArgs) -> Guid """
        ...

    @property
    def Tags(self) -> EventTags:
        """ Get: Tags(self: EventWrittenEventArgs) -> EventTags """
        ...

    @property
    def Task(self) -> EventTask:
        """ Get: Task(self: EventWrittenEventArgs) -> EventTask """
        ...

    @property
    def Version(self) -> Byte:
        """ Get: Version(self: EventWrittenEventArgs) -> Byte """
        ...



class NonEventAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ NonEventAttribute() """
    pass

