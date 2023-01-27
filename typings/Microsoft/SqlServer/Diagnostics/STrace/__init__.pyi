# encoding: utf-8
# module Microsoft.SqlServer.Diagnostics.STrace calls itself STrace
# from Microsoft.SqlServer.Diagnostics.STrace, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Attribute, DateTimeOffset, Enum, Guid, ICloneable, 
    IDisposable, Int64)

from System.Collections import IEnumerable, Stack

from System.Diagnostics import (SourceSwitch, TraceEventType, TraceFilter, 
    TraceListener, TraceListenerCollection)

from System.Runtime.Serialization import ISerializable

from System.Xml import XmlNode

from typing import Self

"""The following names are not found in the module: BoundEvent, T, field#
"""

# no functions
# classes

class TraceContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def EventContext(self) -> str:
        """
        Get: EventContext(self: TraceContext) -> str
        Set: EventContext(self: TraceContext) = value
        """
        ...

    @property
    def EventSubcontext(self) -> str:
        """
        Get: EventSubcontext(self: TraceContext) -> str
        Set: EventSubcontext(self: TraceContext) = value
        """
        ...

    @property
    def IsTracingEnabled(self):
        ...

    @property
    def TraceSource(self) -> STraceSource:
        """ Get: TraceSource(self: TraceContext) -> STraceSource """
        ...


    def Assert(self, test:bool, *__args:str): # -> 
        """ Assert(self: TraceContext, test: bool)Assert(self: TraceContext, test: bool, message: str)Assert(self: TraceContext, test: bool, format: str, *args: Array[object])Assert(self: TraceContext, test: bool, id: int, message: str)Assert(self: TraceContext, test: bool, id: int, format: str, *args: Array[object]) """
        ...

    def CreateCounter(self, *args): #cannot find CLR method
        """ CreateCounter(self: TraceContext, counterName: str) """
        ...

    def DebugAssert(self, test:bool, *__args:str): # -> 
        """ DebugAssert(self: TraceContext, test: bool)DebugAssert(self: TraceContext, test: bool, message: str)DebugAssert(self: TraceContext, test: bool, format: str, *args: Array[object])DebugAssert(self: TraceContext, test: bool, id: int, message: str)DebugAssert(self: TraceContext, test: bool, id: int, format: str, *args: Array[object]) """
        ...

    def GenerateEnvironmentSummary(self, *args): #cannot find CLR method
        """ GenerateEnvironmentSummary() """
        ...

    def GenerateEvent(self, *args): #cannot find CLR method
        """ GenerateEvent(self: TraceContext, straceEvent: STraceEvent) """
        ...

    def GetActivityContext(self, activityName:str) -> ActivityTraceContext:
        """ GetActivityContext(self: TraceContext, activityName: str) -> ActivityTraceContext """
        ...

    def GetMethodContext(self, methodName:str, traceEventType:TraceEventType = ...) -> MethodTraceContext:
        """
        GetMethodContext(self: TraceContext, methodName: str) -> MethodTraceContext
        GetMethodContext(self: TraceContext, methodName: str, traceEventType: TraceEventType) -> MethodTraceContext
        """
        ...

    def GetScenarioContext(self, scenarioName:str) -> ScenarioTraceContext:
        """ GetScenarioContext(self: TraceContext, scenarioName: str) -> ScenarioTraceContext """
        ...

    @staticmethod
    def GetTraceContext(eventSourceName:str, eventContext:str, eventSubcontext:str = ...) -> TraceContext:
        """
        GetTraceContext(eventSourceName: str, eventContext: str) -> TraceContext
        GetTraceContext(eventSourceName: str, eventContext: str, eventSubcontext: str) -> TraceContext
        """
        ...

    def IncrementCounter(self, counterName:str) -> Int64:
        """ IncrementCounter(self: TraceContext, counterName: str) -> Int64 """
        ...

    def ShouldTrace(self, *args): #cannot find CLR method
        """
        ShouldTrace(self: TraceContext, eventType: Type, traceEventType: TraceEventType, id: int, name: str) -> bool
        ShouldTrace(self: TraceContext, traceSource: STraceSource, traceSourceName: str, eventType: Type, traceEventType: TraceEventType, id: int, name: str) -> bool
        """
        ...

    def TraceActivityEnd(self, *__args:str): # -> 
        """ TraceActivityEnd(self: TraceContext, activityName: str)TraceActivityEnd(self: TraceContext, id: int, activityName: str) """
        ...

    def TraceActivityStart(self, *__args:str): # -> 
        """ TraceActivityStart(self: TraceContext, activityName: str)TraceActivityStart(self: TraceContext, id: int, activityName: str) """
        ...

    def TraceAppEnd(self, applicationName:str): # -> 
        """ TraceAppEnd(self: TraceContext, applicationName: str) """
        ...

    def TraceAppStart(self, applicationName:str): # -> 
        """ TraceAppStart(self: TraceContext, applicationName: str) """
        ...

    def TraceCatch(self, exception:Exception, traceEventType:TraceEventType = ...): # -> 
        """ TraceCatch(self: TraceContext, exception: Exception)TraceCatch(self: TraceContext, exception: Exception, traceEventType: TraceEventType) """
        ...

    def TraceCounter(self, counterName:str) -> Int64:
        """ TraceCounter(self: TraceContext, counterName: str) -> Int64 """
        ...

    def TraceCounterAndResetValue(self, counterName:str) -> Int64:
        """ TraceCounterAndResetValue(self: TraceContext, counterName: str) -> Int64 """
        ...

    def TraceCriticalError(self, *__args:str): # -> 
        """ TraceCriticalError(self: TraceContext, message: str)TraceCriticalError(self: TraceContext, id: int, message: str)TraceCriticalError(self: TraceContext, format: str, *args: Array[object])TraceCriticalError(self: TraceContext, id: int, format: str, *args: Array[object]) """
        ...

    def TraceError(self, *__args:str): # -> 
        """ TraceError(self: TraceContext, message: str)TraceError(self: TraceContext, id: int, message: str)TraceError(self: TraceContext, format: str, *args: Array[object])TraceError(self: TraceContext, id: int, format: str, *args: Array[object]) """
        ...

    def TraceHeartbeat(self): # -> 
        """ TraceHeartbeat(self: TraceContext) """
        ...

    def TraceInformation(self, *__args:str): # -> 
        """ TraceInformation(self: TraceContext, message: str)TraceInformation(self: TraceContext, id: int, message: str)TraceInformation(self: TraceContext, format: str, *args: Array[object])TraceInformation(self: TraceContext, id: int, format: str, *args: Array[object]) """
        ...

    def TraceMarker(self, id:int): # -> 
        """ TraceMarker(self: TraceContext, id: int) """
        ...

    def TraceMethodEnter(self, methodName:str): # -> 
        """ TraceMethodEnter(self: TraceContext, methodName: str) """
        ...

    def TraceMethodExit(self, methodName:str): # -> 
        """ TraceMethodExit(self: TraceContext, methodName: str) """
        ...

    def TraceParameter(self, *args): #cannot find CLR method
        """ TraceParameter(self: TraceContext, parameterName: str, parameterValue: object, isInput: bool, traceEventType: TraceEventType) """
        ...

    def TraceParameterIn(self, parameterName:str, parameterValue:object): # -> 
        """ TraceParameterIn(self: TraceContext, parameterName: str, parameterValue: object) """
        ...

    def TraceParameterOut(self, parameterName:str, parameterValue:object): # -> 
        """ TraceParameterOut(self: TraceContext, parameterName: str, parameterValue: object) """
        ...

    def TraceParameters(self, parameterValues:Array): # -> 
        """ TraceParameters(self: TraceContext, *parameterValues: Array[object]) """
        ...

    def TraceReturnValue(self, returnValue): # -> T # Not found arg types: {'returnValue': 'T'}
        """ TraceReturnValue[T](self: TraceContext, returnValue: T) -> T """
        ...

    def TraceScenarioEnd(self, scenarioName:str): # -> 
        """ TraceScenarioEnd(self: TraceContext, scenarioName: str) """
        ...

    def TraceScenarioStart(self, scenarioName:str): # -> 
        """ TraceScenarioStart(self: TraceContext, scenarioName: str) """
        ...

    def TraceThreadEnd(self): # -> 
        """ TraceThreadEnd(self: TraceContext) """
        ...

    def TraceThreadStart(self): # -> 
        """ TraceThreadStart(self: TraceContext) """
        ...

    def TraceThrow(self, exception:Exception, traceEventType:TraceEventType = ...) -> Exception:
        """
        TraceThrow(self: TraceContext, exception: Exception) -> Exception
        TraceThrow(self: TraceContext, exception: Exception, traceEventType: TraceEventType) -> Exception
        """
        ...

    def TraceTransfer(self, *__args): # -> 
        """ TraceTransfer(self: TraceContext, relatedActivityName: str, relatedActivityId: Guid)TraceTransfer(self: TraceContext, id: int, relatedActivityName: str, relatedActivityId: Guid) """
        ...

    def TraceVerbose(self, *__args:str): # -> 
        """ TraceVerbose(self: TraceContext, message: str)TraceVerbose(self: TraceContext, id: int, message: str)TraceVerbose(self: TraceContext, format: str, *args: Array[object])TraceVerbose(self: TraceContext, id: int, format: str, *args: Array[object]) """
        ...

    def TraceWarning(self, *__args:str): # -> 
        """ TraceWarning(self: TraceContext, message: str)TraceWarning(self: TraceContext, id: int, message: str)TraceWarning(self: TraceContext, format: str, *args: Array[object])TraceWarning(self: TraceContext, id: int, format: str, *args: Array[object]) """
        ...


class DisposableTraceContext(IDisposable, TraceContext): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: DisposableTraceContext) -> str """
        ...


    def GenerateEndEvent(self, *args): #cannot find CLR method
        """ GenerateEndEvent(self: DisposableTraceContext, source: str, context: str, subcontext: str, traceEventType: TraceEventType) -> STraceEvent """
        ...

    def GenerateStartEvent(self, *args): #cannot find CLR method
        """ GenerateStartEvent(self: DisposableTraceContext, source: str, context: str, subcontext: str, traceEventType: TraceEventType) -> STraceEvent """
        ...

    def OnEnded(self, *args): #cannot find CLR method
        """ OnEnded(self: DisposableTraceContext, e: EventArgs) """
        ...

    def OnStarting(self, *args): #cannot find CLR method
        """ OnStarting(self: DisposableTraceContext, e: EventArgs) """
        ...

    Ended = ...
    Starting = ...


class ActivityTraceContext(DisposableTraceContext): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    Ended = ...
    Starting = ...


class STraceListener(TraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def ConfigurationAttributes(self):
        ...

    @property
    def DefaultTraceOutputFormat(self):
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: STraceListener) -> bool
        Set: Enabled(self: STraceListener) = value
        """
        ...

    @property
    def TraceOutputFields(self) -> TraceOutputFields:
        """
        Get: TraceOutputFields(self: STraceListener) -> TraceOutputFields
        Set: TraceOutputFields(self: STraceListener) = value
        """
        ...

    @property
    def TraceOutputFormat(self) -> TraceOutputFormat:
        """
        Get: TraceOutputFormat(self: STraceListener) -> TraceOutputFormat
        Set: TraceOutputFormat(self: STraceListener) = value
        """
        ...


    def GetCustomAttributes(self, *args): #cannot find CLR method
        """ GetCustomAttributes(self: STraceListener) -> Array[str] """
        ...

    def GetTraceConfigurationXml(self) -> XmlNode:
        """ GetTraceConfigurationXml(self: STraceListener) -> XmlNode """
        ...

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: STraceListener) """
        ...

    def ProcessTraceEvent(self, *args): #cannot find CLR method
        """ ProcessTraceEvent(self: STraceListener, eventCache: TraceEventCache, straceEvent: STraceEvent) """
        ...

    def ShouldTrace(self, *args): #cannot find CLR method
        """ ShouldTrace(self: STraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, *data: Array[object]) -> bool """
        ...


class AssertFailureTraceListener(STraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    AssertFailureTraceListener(name: str)
    AssertFailureTraceListener()
    """
    @property
    def AssertUiEnabled(self) -> bool:
        """
        Get: AssertUiEnabled() -> bool
        Set: AssertUiEnabled() = value
        """
        ...

    @property
    def IsThreadSafe(self) -> bool:
        """ Get: IsThreadSafe(self: AssertFailureTraceListener) -> bool """
        ...


    def Fail(self, message:str, detailMessage:str = ...): # -> 
        """ Fail(self: AssertFailureTraceListener, message: str)Fail(self: AssertFailureTraceListener, message: str, detailMessage: str) """
        ...



class BlackBox: # skipped bases: <type 'object'>, <type 'object'>
    """ BlackBox() """
    @property
    def BlackBoxConfiguration(self) -> BlackBoxConfiguration:
        """ Get: BlackBoxConfiguration(self: BlackBox) -> BlackBoxConfiguration """
        ...

    @property
    def GenerateOnCollectionThread(self) -> bool:
        """ Get: GenerateOnCollectionThread(self: BlackBox) -> bool """
        ...

    @property
    def Instance(self) -> BlackBox:
        """ Get: Instance() -> BlackBox """
        ...

    @property
    def MaxWaitInMilliseconds(self) -> int:
        """ Get: MaxWaitInMilliseconds(self: BlackBox) -> int """
        ...

    @property
    def UseBackgroundThread(self) -> bool:
        """ Get: UseBackgroundThread(self: BlackBox) -> bool """
        ...


    def BlackBoxSetting(self, *args): #cannot find CLR method
        """ enum BlackBoxSetting, values: GenerateOnCollectionThread (1), MaxWaitInMilliseconds (2), UseBackgroundThread (0) """
        ...

    def CollectBlackBoxData(self, filePath:str, removeIndividualFiles:bool = ..., maxCompressedBlackBoxDumpFiles:int = ..., encrypt:bool = ...) -> str:
        """
        CollectBlackBoxData(self: BlackBox, filePath: str) -> str
        CollectBlackBoxData(self: BlackBox, filePath: str, removeIndividualFiles: bool, maxCompressedBlackBoxDumpFiles: int, encrypt: bool) -> str
        """
        ...

    def ConfigureBlackBoxTracing(self, configuration:BlackBoxConfiguration, encrypt:bool = ...): # -> 
        """ ConfigureBlackBoxTracing(self: BlackBox, configuration: BlackBoxConfiguration)ConfigureBlackBoxTracing(self: BlackBox, configuration: BlackBoxConfiguration, encrypt: bool) """
        ...

    def RegisterCustomBlackBoxListener(self, traceListener:TraceListener): # -> 
        """ RegisterCustomBlackBoxListener(self: BlackBox, traceListener: TraceListener) """
        ...

    def RegisterDataProvider(self, dataProvider:IBlackBoxDataProvider): # -> 
        """ RegisterDataProvider(self: BlackBox, dataProvider: IBlackBoxDataProvider) """
        ...

    def UnregisterDataProvider(self, dataProvider:IBlackBoxDataProvider): # -> 
        """ UnregisterDataProvider(self: BlackBox, dataProvider: IBlackBoxDataProvider) """
        ...



class BlackBoxConfiguration(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BlackBoxConfiguration, values: Custom (4), Detailed (3), Medium (2), Minimal (1), Off (0) """
    Custom: BlackBoxConfiguration = ...
    Detailed: BlackBoxConfiguration = ...
    Medium: BlackBoxConfiguration = ...
    Minimal: BlackBoxConfiguration = ...
    Off: BlackBoxConfiguration = ...
    value__ = ...


class BlackBoxFileDataProvider(IBlackBoxDataProvider): # skipped bases: <type 'object'>
    """ BlackBoxFileDataProvider(name: str, fileNames: Array[str], timingSensitive: bool) """
    pass

class ConsoleTraceListener(STraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    ConsoleTraceListener()
    ConsoleTraceListener(name: str)
    ConsoleTraceListener(name: str, traceOutputFields: TraceOutputFields, traceOutputFormat: TraceOutputFormat)
    ConsoleTraceListener(name: str, stream: Stream, traceOutputFields: TraceOutputFields, traceOutputFormat: TraceOutputFormat)
    """
    @property
    def IsThreadSafe(self) -> bool:
        """ Get: IsThreadSafe(self: ConsoleTraceListener) -> bool """
        ...



class FailpointAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FailpointAction, values: CollectBlackBox (5), DebugBreak (2), GenerateFullDump (4), GenerateMiniDump (3), ShowDialog (1), ThrowException (0) """
    CollectBlackBox: FailpointAction = ...
    DebugBreak: FailpointAction = ...
    GenerateFullDump: FailpointAction = ...
    GenerateMiniDump: FailpointAction = ...
    ShowDialog: FailpointAction = ...
    ThrowException: FailpointAction = ...
    value__ = ...


class FailpointTraceListener(STraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    FailpointTraceListener(name: str)
    FailpointTraceListener()
    FailpointTraceListener(name: str, logPath: str, encrypt: bool, actions: ReadOnlyCollection[FailpointAction], exceptionType: Type, maxFailpoints: int)
    """
    @property
    def IsThreadSafe(self) -> bool:
        """ Get: IsThreadSafe(self: FailpointTraceListener) -> bool """
        ...


    def ListenerSetting(self, *args): #cannot find CLR method
        """ enum ListenerSetting, values: actions (1), encrypt (4), exceptionType (2), logPath (0), maxFailpoints (3) """
        ...

    def ShowFailpointDialog(self, *args): #cannot find CLR method
        """ ShowFailpointDialog(internalTraceContext: TraceContext, straceEvent: STraceEvent) """
        ...

    def TracePoint(self, *args): #cannot find CLR method
        """ enum TracePoint, values: BlackBoxDumpAction (106), BlackBoxDumpActionGeneralException (205), BlackBoxDumpActionSecurityException (204), DebugBreakAction (102), DebugBreakActionSecurityException (202), DumpActionComplete (105), DumpActionGeneralException (201), DumpActionSecurityException (200), FailpointTriggered (2), FullDumpAction (104), MaxFailpointsExceeded (1), MiniDumpAction (103), NotUsed (0), ShowDialogAction (101), ShowDialogActionSecurityException (203), ThrowExceptionAction (100) """
        ...



class FlightRecorderTraceListener(IBlackBoxDataProvider, STraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    FlightRecorderTraceListener(name: str)
    FlightRecorderTraceListener()
    FlightRecorderTraceListener(name: str, startupEventCacheSize: int, ringBufferEventCacheSize: int, traceOutputFields: TraceOutputFields, traceOutputFormat: TraceOutputFormat)
    """
    @property
    def IsThreadSafe(self) -> bool:
        """ Get: IsThreadSafe(self: FlightRecorderTraceListener) -> bool """
        ...


    def Close(self): # -> 
        """ Close(self: FlightRecorderTraceListener) """
        ...

    def ListenerSetting(self, *args): #cannot find CLR method
        """ enum ListenerSetting, values: ringBufferEventCacheSize (1), startupEventCacheSize (0) """
        ...



class IBlackBoxDataProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: IBlackBoxDataProvider) -> str """
        ...

    @property
    def TimingSensitive(self) -> bool:
        """ Get: TimingSensitive(self: IBlackBoxDataProvider) -> bool """
        ...


    def WriteBlackBoxData(self, filePath:str) -> Array:
        """ WriteBlackBoxData(self: IBlackBoxDataProvider, filePath: str) -> Array[str] """
        ...


class ISTraceEndEvent: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ElapsedMilliseconds(self) -> Int64:
        """
        Get: ElapsedMilliseconds(self: ISTraceEndEvent) -> Int64
        Set: ElapsedMilliseconds(self: ISTraceEndEvent) = value
        """
        ...



class ISTraceNamedEvent: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: ISTraceNamedEvent) -> str
        Set: Name(self: ISTraceNamedEvent) = value
        """
        ...



class ISTraceStartEvent: # skipped bases: <type 'object'>
    """ no doc """
    pass

class ISTraceValueEvent: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Value(self) -> object:
        """
        Get: Value(self: ISTraceValueEvent) -> object
        Set: Value(self: ISTraceValueEvent) = value
        """
        ...



class LogFileTraceListener(IBlackBoxDataProvider, STraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    LogFileTraceListener(name: str)
    LogFileTraceListener()
    LogFileTraceListener(name: str, logPath: str, logFilesToRetain: int, encrypt: bool, registerWithBlackBox: bool, traceOutputFields: TraceOutputFields, traceOutputFormat: TraceOutputFormat)
    """
    @property
    def IsThreadSafe(self) -> bool:
        """ Get: IsThreadSafe(self: LogFileTraceListener) -> bool """
        ...

    @property
    def LogFile(self) -> str:
        """ Get: LogFile(self: LogFileTraceListener) -> str """
        ...


    def CleanUpOldTraceFiles(self, *args): #cannot find CLR method
        """ CleanUpOldTraceFiles(self: LogFileTraceListener) """
        ...

    def Close(self): # -> 
        """ Close(self: LogFileTraceListener) """
        ...

    def Flush(self): # -> 
        """ Flush(self: LogFileTraceListener) """
        ...

    def OpenLogFile(self, *args): #cannot find CLR method
        """ OpenLogFile(self: LogFileTraceListener) """
        ...


class MethodTraceContext(DisposableTraceContext): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    Ended = ...
    Starting = ...


class ScenarioTraceContext(DisposableTraceContext): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    Ended = ...
    Starting = ...


class STraceAssertFailureException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    STraceAssertFailureException(message: str)
    STraceAssertFailureException()
    STraceAssertFailureException(message: str, exception: Exception)
    """
    SerializeObjectState = ...


class STraceConfiguration: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AutoFlush(self) -> bool:
        """
        Get: AutoFlush() -> bool
        Set: AutoFlush() = value
        """
        ...

    @property
    def NonSTraceListenerTraceOutputFields(self) -> TraceOutputFields:
        """
        Get: NonSTraceListenerTraceOutputFields() -> TraceOutputFields
        Set: NonSTraceListenerTraceOutputFields() = value
        """
        ...

    @property
    def NonSTraceListenerTraceOutputFormat(self) -> TraceOutputFormat:
        """
        Get: NonSTraceListenerTraceOutputFormat() -> TraceOutputFormat
        Set: NonSTraceListenerTraceOutputFormat() = value
        """
        ...


    __all__: list = ...


class STraceConfigurationAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ STraceConfigurationAttribute() """
    @property
    def SkipAutoTrace(self) -> bool:
        """
        Get: SkipAutoTrace(self: STraceConfigurationAttribute) -> bool
        Set: SkipAutoTrace(self: STraceConfigurationAttribute) = value
        """
        ...



class STraceConstants: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    MethodEnterEventId: int = ...
    MethodExitEventId: int = ...
    ParameterEventId: int = ...
    __all__: list = ...


class STraceEvent(ISerializable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActivityId(self) -> Guid:
        """ Get: ActivityId(self: STraceEvent) -> Guid """
        ...

    @property
    def Callstack(self) -> str:
        """
        Get: Callstack(self: STraceEvent) -> str
        Set: Callstack(self: STraceEvent) = value
        """
        ...

    @property
    def DateTimeOffset(self) -> DateTimeOffset:
        """ Get: DateTimeOffset(self: STraceEvent) -> DateTimeOffset """
        ...

    @property
    def DateTimeOffsetUtc(self) -> DateTimeOffset:
        """ Get: DateTimeOffsetUtc(self: STraceEvent) -> DateTimeOffset """
        ...

    @property
    def EventContext(self) -> str:
        """ Get: EventContext(self: STraceEvent) -> str """
        ...

    @property
    def EventSubcontext(self) -> str:
        """ Get: EventSubcontext(self: STraceEvent) -> str """
        ...

    @property
    def FormattedMessage(self) -> str:
        """ Get: FormattedMessage(self: STraceEvent) -> str """
        ...

    @property
    def Id(self) -> int:
        """
        Get: Id(self: STraceEvent) -> int
        Set: Id(self: STraceEvent) = value
        """
        ...

    @property
    def IsError(self):
        ...

    @property
    def KernelThreadId(self) -> int:
        """ Get: KernelThreadId(self: STraceEvent) -> int """
        ...

    @property
    def LogicalOperationStack(self) -> Stack:
        """ Get: LogicalOperationStack(self: STraceEvent) -> Stack """
        ...

    @property
    def MessageArgs(self) -> Array:
        """ Get: MessageArgs(self: STraceEvent) -> Array[object] """
        ...

    @property
    def MessageOrFormatString(self) -> str:
        """
        Get: MessageOrFormatString(self: STraceEvent) -> str
        Set: MessageOrFormatString(self: STraceEvent) = value
        """
        ...

    @property
    def NestingLevel(self) -> int:
        """ Get: NestingLevel(self: STraceEvent) -> int """
        ...

    @property
    def ProcessId(self) -> int:
        """ Get: ProcessId(self: STraceEvent) -> int """
        ...

    @property
    def Source(self) -> str:
        """ Get: Source(self: STraceEvent) -> str """
        ...

    @property
    def TraceEventType(self) -> TraceEventType:
        """
        Get: TraceEventType(self: STraceEvent) -> TraceEventType
        Set: TraceEventType(self: STraceEvent) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: STraceEvent) -> str """
        ...


    def CurrentThreadIndent(self, *args): #cannot find CLR method
        """ CurrentThreadIndent(self: STraceEvent) -> str """
        ...

    def ToString(self, traceOutputFields:TraceOutputFields = ..., traceOutputFormat:TraceOutputFormat = ...) -> str:
        """
        ToString(self: STraceEvent) -> str
        ToString(self: STraceEvent, traceOutputFields: TraceOutputFields, traceOutputFormat: TraceOutputFormat) -> str
        """
        ...

    ErrorIndicator: str = ...
    indentLevelWrap: int = ...


class STraceEventActivityEnd(STraceEvent, ISTraceEndEvent, ISTraceNamedEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventActivityEnd(source: str, eventContext: str, activityName: str, id: int) """
    pass

class STraceEventActivityStart(ISTraceStartEvent, STraceEvent, ISTraceNamedEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventActivityStart(source: str, eventContext: str, activityName: str, id: int) """
    pass

class STraceEventAppEnd(STraceEvent, ISTraceEndEvent, ISTraceNamedEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventAppEnd(source: str, applicationName: str) """
    pass

class STraceEventAppStart(ISTraceStartEvent, STraceEvent, ISTraceNamedEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventAppStart(source: str, applicationName: str) """
    pass

class STraceEventAssertFailure(STraceEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventAssertFailure(source: str, eventContext: str, eventSubcontext: str, id: int, messageOrFormat: str, *args: Array[object]) """
    pass

class STraceEventCatch(STraceEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """
    STraceEventCatch(source: str, eventContext: str, eventSubcontext: str, exception: Exception, traceEventType: TraceEventType)
    STraceEventCatch(source: str, eventContext: str, eventSubcontext: str, exception: Exception)
    """
    @property
    def Exception(self) -> Exception:
        """
        Get: Exception(self: STraceEventCatch) -> Exception
        Set: Exception(self: STraceEventCatch) = value
        """
        ...



class STraceEventCounter(STraceEvent, ISTraceNamedEvent, ISTraceValueEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventCounter(source: str, eventContext: str, eventSubcontext: str, counterName: str, counterValue: Int64) """
    pass

class STraceEventCriticalError(STraceEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventCriticalError(source: str, eventContext: str, eventSubcontext: str, id: int, messageOrFormat: str, *args: Array[object]) """
    pass

class STraceEventError(STraceEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventError(source: str, eventContext: str, eventSubcontext: str, id: int, messageOrFormat: str, *args: Array[object]) """
    pass

class STraceEventHeartbeat(STraceEvent, ISTraceNamedEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventHeartbeat(source: str, eventContext: str) """
    pass

class STraceEventInformation(STraceEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventInformation(source: str, eventContext: str, eventSubcontext: str, id: int, messageOrFormat: str, *args: Array[object]) """
    pass

class STraceEventMarker(STraceEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventMarker(source: str, eventContext: str, eventSubcontext: str, id: int) """
    pass

class STraceEventMethodEnter(ISTraceStartEvent, STraceEvent, ISTraceNamedEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventMethodEnter(source: str, eventContext: str, methodName: str, traceEventType: TraceEventType) """
    pass

class STraceEventMethodExit(STraceEvent, ISTraceEndEvent, ISTraceNamedEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventMethodExit(source: str, eventContext: str, methodName: str, traceEventType: TraceEventType) """
    pass

class STraceEventParameter(STraceEvent, ISTraceNamedEvent, ISTraceValueEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventParameter(source: str, eventContext: str, eventSubcontext: str, isInput: bool, parameterName: str, parameterValue: object, traceEventType: TraceEventType) """
    @property
    def IsInputParameter(self) -> bool:
        """ Get: IsInputParameter(self: STraceEventParameter) -> bool """
        ...



class STraceEventScenarioEnd(STraceEvent, ISTraceEndEvent, ISTraceNamedEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventScenarioEnd(source: str, eventContext: str, scenarioName: str) """
    pass

class STraceEventScenarioStart(ISTraceStartEvent, STraceEvent, ISTraceNamedEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventScenarioStart(source: str, eventContext: str, scenarioName: str) """
    pass

class STraceEventThreadEnd(STraceEvent, ISTraceEndEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventThreadEnd(source: str, eventContext: str, eventSubcontext: str) """
    pass

class STraceEventThreadStart(STraceEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventThreadStart(source: str, eventContext: str, eventSubcontext: str) """
    pass

class STraceEventThrow(STraceEventCatch): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """
    STraceEventThrow(source: str, eventContext: str, eventSubcontext: str, exception: Exception, traceEventType: TraceEventType)
    STraceEventThrow(source: str, eventContext: str, eventSubcontext: str, exception: Exception)
    """
    pass

class STraceEventTransfer(STraceEvent, ISTraceNamedEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventTransfer(source: str, eventContext: str, eventSubcontext: str, id: int, relatedActivityName: str, relatedActivityId: Guid) """
    @property
    def RelatedActivityId(self) -> Guid:
        """
        Get: RelatedActivityId(self: STraceEventTransfer) -> Guid
        Set: RelatedActivityId(self: STraceEventTransfer) = value
        """
        ...



class STraceEventVerbose(STraceEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventVerbose(source: str, eventContext: str, eventSubcontext: str, id: int, messageOrFormat: str, *args: Array[object]) """
    pass

class STraceEventWarning(STraceEvent): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ STraceEventWarning(source: str, eventContext: str, eventSubcontext: str, id: int, messageOrFormat: str, *args: Array[object]) """
    pass

class STraceFilter(TraceFilter, ICloneable): # skipped bases: <type 'object'>
    """ STraceFilter(initializeData: str) """
    @property
    def SupplementalTraceFilter(self) -> TraceFilter:
        """
        Get: SupplementalTraceFilter(self: STraceFilter) -> TraceFilter
        Set: SupplementalTraceFilter(self: STraceFilter) = value
        """
        ...


    def GetTraceConfigurationXml(self) -> XmlNode:
        """ GetTraceConfigurationXml(self: STraceFilter) -> XmlNode """
        ...

    def __new__(cls, initializeData:str) -> Self:
        """ __new__(cls: type, initializeData: str) """
        ...


class STraceSimulatedException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    STraceSimulatedException(simulatedException: Exception)
    STraceSimulatedException(message: str, simulatedException: Exception)
    STraceSimulatedException()
    STraceSimulatedException(message: str)
    """
    SerializeObjectState = ...


class STraceSource: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def GlobalTraceSource(self) -> STraceSource:
        """ Get: GlobalTraceSource() -> STraceSource """
        ...

    @property
    def IsGlobalTraceSourceConfigured(self):
        ...

    @property
    def IsTracingEnabled(self) -> bool:
        """
        Get: IsTracingEnabled() -> bool
        Set: IsTracingEnabled() = value
        """
        ...

    @property
    def Listeners(self) -> TraceListenerCollection:
        """ Get: Listeners(self: STraceSource) -> TraceListenerCollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: STraceSource) -> str """
        ...

    @property
    def SuppressExceptions(self) -> bool:
        """
        Get: SuppressExceptions() -> bool
        Set: SuppressExceptions() = value
        """
        ...

    @property
    def Switch(self) -> SourceSwitch:
        """
        Get: Switch(self: STraceSource) -> SourceSwitch
        Set: Switch(self: STraceSource) = value
        """
        ...

    @property
    def ThreadNestingLevel(self) -> int:
        """
        Get: ThreadNestingLevel() -> int
        Set: ThreadNestingLevel() = value
        """
        ...

    @property
    def TraceSources(self) -> STraceSourceCollection:
        """ Get: TraceSources() -> STraceSourceCollection """
        ...


    def Close(self): # -> 
        """ Close(self: STraceSource) """
        ...

    def Flush(self): # -> 
        """ Flush(self: STraceSource) """
        ...

    def GetTraceConfigurationXml(self) -> XmlNode:
        """ GetTraceConfigurationXml(self: STraceSource) -> XmlNode """
        ...

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: STraceSource) """
        ...

    def SetGlobalSourceSwitch(self, *args): #cannot find CLR method
        """ SetGlobalSourceSwitch(self: STraceSource) """
        ...

    def TraceData(self, straceEvent:STraceEvent): # -> 
        """ TraceData(self: STraceSource, straceEvent: STraceEvent) """
        ...



class STraceSourceCollection(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ STraceSourceCollection() """
    def Clear(self): # -> 
        """ Clear(self: STraceSourceCollection) """
        ...

    def GetTraceConfigurationXml(self) -> XmlNode:
        """ GetTraceConfigurationXml(self: STraceSourceCollection) -> XmlNode """
        ...

    def Remove(self, sourceName:str): # -> 
        """ Remove(self: STraceSourceCollection, sourceName: str) """
        ...

    def SaveTraceConfigurationForApplication(self, fullExeFileName:str): # -> 
        """ SaveTraceConfigurationForApplication(self: STraceSourceCollection, fullExeFileName: str) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[STraceSource](enumerable: IEnumerable[STraceSource], value: STraceSource) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class TraceOutputFields(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TraceOutputFields, values: ActivityId (8192), All (268435451), Callstack (1), DateTimeOffset (2), DateTimeOffsetUtc (4), Default (5978), ErrorIndicator (8), EventContext (16), EventSubcontext (32), EventType (64), Id (128), Indentation (256), KernelThreadId (512), LogicalOperationStack (16384), Message (1024), None (0), ProcessId (2048), Source (4096) """
    ActivityId: TraceOutputFields = ...
    All: TraceOutputFields = ...
    Callstack: TraceOutputFields = ...
    DateTimeOffset: TraceOutputFields = ...
    DateTimeOffsetUtc: TraceOutputFields = ...
    Default: TraceOutputFields = ...
    ErrorIndicator: TraceOutputFields = ...
    EventContext: TraceOutputFields = ...
    EventSubcontext: TraceOutputFields = ...
    EventType: TraceOutputFields = ...
    Id: TraceOutputFields = ...
    Indentation: TraceOutputFields = ...
    KernelThreadId: TraceOutputFields = ...
    LogicalOperationStack: TraceOutputFields = ...
    Message: TraceOutputFields = ...
    ProcessId: TraceOutputFields = ...
    Source: TraceOutputFields = ...
    value__ = ...


class TraceOutputFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TraceOutputFormat, values: FixedWidth (0), VariableWidth (1) """
    FixedWidth: TraceOutputFormat = ...
    value__ = ...
    VariableWidth: TraceOutputFormat = ...


