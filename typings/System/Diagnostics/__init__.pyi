# encoding: utf-8
# module System.Diagnostics calls itself Diagnostics
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Configuration.Install, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Diagnostics.Tracing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Win32.SafeHandles import SafeProcessHandle

from System import (Array, AsyncCallback, Attribute, DateTime, Enum, 
    EventArgs, Guid, IAsyncResult, IDisposable, Int16, Int64, IntPtr, 
    MarshalByRefObject, MulticastDelegate, Single, TimeSpan, Type)

from System.Collections import (CollectionBase, DictionaryBase, ICollection, 
    IDictionary, IEnumerator, IList, ReadOnlyCollectionBase, Stack)

from System.Collections.Specialized import StringDictionary

from System.ComponentModel import (Component, ISupportInitialize, 
    ISynchronizeInvoke)

from System.Configuration import IConfigurationSectionHandler

from System.Configuration.Install import ComponentInstaller, UninstallAction

from System.EnterpriseServices import DescriptionAttribute

from System.IO import StreamReader, StreamWriter, TextWriter

from System.Reflection import Assembly, MethodBase

from System.Runtime.Serialization import ISerializable

from System.Security import IPermission, SecureString

from System.Security.Permissions import (CodeAccessSecurityAttribute, 
    ResourcePermissionBase)

from System.Text import Encoding

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    DebuggingModes, TraceLogRetentionOption, field#)
"""

# no functions
# classes

class Switch: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> StringDictionary:
        """ Get: Attributes(self: Switch) -> StringDictionary """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: Switch) -> str """
        ...

    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: Switch) -> str """
        ...

    @property
    def SwitchSetting(self):
        ...

    @property
    def Value(self):
        ...


    def GetSupportedAttributes(self, *args): #cannot find CLR method
        """ GetSupportedAttributes(self: Switch) -> Array[str] """
        ...

    def OnSwitchSettingChanged(self, *args): #cannot find CLR method
        """ OnSwitchSettingChanged(self: Switch) """
        ...

    def OnValueChanged(self, *args): #cannot find CLR method
        """ OnValueChanged(self: Switch) """
        ...


class BooleanSwitch(Switch): # skipped bases: <type 'object'>
    """
    BooleanSwitch(displayName: str, description: str)
    BooleanSwitch(displayName: str, description: str, defaultSwitchValue: str)
    """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: BooleanSwitch) -> bool
        Set: Enabled(self: BooleanSwitch) = value
        """
        ...



class ConditionalAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ConditionalAttribute(conditionString: str) """
    @property
    def ConditionString(self) -> str:
        """ Get: ConditionString(self: ConditionalAttribute) -> str """
        ...


    def __new__(cls, conditionString:str) -> Self:
        """ __new__(cls: type, conditionString: str) """
        ...


class TraceListener(IDisposable, MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> StringDictionary:
        """ Get: Attributes(self: TraceListener) -> StringDictionary """
        ...

    @property
    def Filter(self) -> TraceFilter:
        """
        Get: Filter(self: TraceListener) -> TraceFilter
        Set: Filter(self: TraceListener) = value
        """
        ...

    @property
    def IndentLevel(self) -> int:
        """
        Get: IndentLevel(self: TraceListener) -> int
        Set: IndentLevel(self: TraceListener) = value
        """
        ...

    @property
    def IndentSize(self) -> int:
        """
        Get: IndentSize(self: TraceListener) -> int
        Set: IndentSize(self: TraceListener) = value
        """
        ...

    @property
    def IsThreadSafe(self) -> bool:
        """ Get: IsThreadSafe(self: TraceListener) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: TraceListener) -> str
        Set: Name(self: TraceListener) = value
        """
        ...

    @property
    def NeedIndent(self):
        ...

    @property
    def TraceOutputOptions(self) -> TraceOptions:
        """
        Get: TraceOutputOptions(self: TraceListener) -> TraceOptions
        Set: TraceOutputOptions(self: TraceListener) = value
        """
        ...


    def Close(self): # -> 
        """ Close(self: TraceListener) """
        ...

    def Fail(self, message:str, detailMessage:str = ...): # -> 
        """ Fail(self: TraceListener, message: str)Fail(self: TraceListener, message: str, detailMessage: str) """
        ...

    def Flush(self): # -> 
        """ Flush(self: TraceListener) """
        ...

    def GetSupportedAttributes(self, *args): #cannot find CLR method
        """ GetSupportedAttributes(self: TraceListener) -> Array[str] """
        ...

    def TraceData(self, eventCache:TraceEventCache, source:str, eventType:TraceEventType, id:int, data:object): # -> 
        """ TraceData(self: TraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, data: object)TraceData(self: TraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, *data: Array[object]) """
        ...

    def TraceEvent(self, eventCache:TraceEventCache, source:str, eventType:TraceEventType, id:int, *__args:str): # -> 
        """ TraceEvent(self: TraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int)TraceEvent(self: TraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, message: str)TraceEvent(self: TraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, format: str, *args: Array[object]) """
        ...

    def TraceTransfer(self, eventCache:TraceEventCache, source:str, id:int, message:str, relatedActivityId:Guid): # -> 
        """ TraceTransfer(self: TraceListener, eventCache: TraceEventCache, source: str, id: int, message: str, relatedActivityId: Guid) """
        ...

    def Write(self, *__args:object): # -> 
        """ Write(self: TraceListener, o: object)Write(self: TraceListener, o: object, category: str)Write(self: TraceListener, message: str)Write(self: TraceListener, message: str, category: str) """
        ...

    def WriteIndent(self, *args): #cannot find CLR method
        """ WriteIndent(self: TraceListener) """
        ...

    def WriteLine(self, *__args:object): # -> 
        """ WriteLine(self: TraceListener, o: object)WriteLine(self: TraceListener, o: object, category: str)WriteLine(self: TraceListener, message: str)WriteLine(self: TraceListener, message: str, category: str) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...


class TextWriterTraceListener(TraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    TextWriterTraceListener()
    TextWriterTraceListener(stream: Stream)
    TextWriterTraceListener(stream: Stream, name: str)
    TextWriterTraceListener(writer: TextWriter)
    TextWriterTraceListener(writer: TextWriter, name: str)
    TextWriterTraceListener(fileName: str)
    TextWriterTraceListener(fileName: str, name: str)
    """
    @property
    def Writer(self) -> TextWriter:
        """
        Get: Writer(self: TextWriterTraceListener) -> TextWriter
        Set: Writer(self: TextWriterTraceListener) = value
        """
        ...



class ConsoleTraceListener(TextWriterTraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    ConsoleTraceListener()
    ConsoleTraceListener(useErrorStream: bool)
    """
    pass

class CorrelationManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ActivityId(self) -> Guid:
        """
        Get: ActivityId(self: CorrelationManager) -> Guid
        Set: ActivityId(self: CorrelationManager) = value
        """
        ...

    @property
    def LogicalOperationStack(self) -> Stack:
        """ Get: LogicalOperationStack(self: CorrelationManager) -> Stack """
        ...


    def StartLogicalOperation(self, operationId:object = ...): # -> 
        """ StartLogicalOperation(self: CorrelationManager, operationId: object)StartLogicalOperation(self: CorrelationManager) """
        ...

    def StopLogicalOperation(self): # -> 
        """ StopLogicalOperation(self: CorrelationManager) """
        ...


class CounterCreationData: # skipped bases: <type 'object'>, <type 'object'>
    """
    CounterCreationData()
    CounterCreationData(counterName: str, counterHelp: str, counterType: PerformanceCounterType)
    """
    @property
    def CounterHelp(self) -> str:
        """
        Get: CounterHelp(self: CounterCreationData) -> str
        Set: CounterHelp(self: CounterCreationData) = value
        """
        ...

    @property
    def CounterName(self) -> str:
        """
        Get: CounterName(self: CounterCreationData) -> str
        Set: CounterName(self: CounterCreationData) = value
        """
        ...

    @property
    def CounterType(self) -> PerformanceCounterType:
        """
        Get: CounterType(self: CounterCreationData) -> PerformanceCounterType
        Set: CounterType(self: CounterCreationData) = value
        """
        ...



class CounterCreationDataCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    CounterCreationDataCollection()
    CounterCreationDataCollection(value: CounterCreationDataCollection)
    CounterCreationDataCollection(value: Array[CounterCreationData])
    """
    def Add(self, value:CounterCreationData) -> int:
        """ Add(self: CounterCreationDataCollection, value: CounterCreationData) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: CounterCreationDataCollection, value: Array[CounterCreationData])AddRange(self: CounterCreationDataCollection, value: CounterCreationDataCollection) """
        ...

    def Contains(self, value:CounterCreationData) -> bool:
        """ Contains(self: CounterCreationDataCollection, value: CounterCreationData) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: CounterCreationDataCollection, array: Array[CounterCreationData], index: int) """
        ...

    def IndexOf(self, value:CounterCreationData) -> int:
        """ IndexOf(self: CounterCreationDataCollection, value: CounterCreationData) -> int """
        ...

    def Insert(self, index:int, value:CounterCreationData): # -> 
        """ Insert(self: CounterCreationDataCollection, index: int, value: CounterCreationData) """
        ...

    def Remove(self, value:CounterCreationData): # -> 
        """ Remove(self: CounterCreationDataCollection, value: CounterCreationData) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class CounterSample: # skipped bases: <type 'object'>, <type 'object'>
    """
    CounterSample(rawValue: Int64, baseValue: Int64, counterFrequency: Int64, systemFrequency: Int64, timeStamp: Int64, timeStamp100nSec: Int64, counterType: PerformanceCounterType)
    CounterSample(rawValue: Int64, baseValue: Int64, counterFrequency: Int64, systemFrequency: Int64, timeStamp: Int64, timeStamp100nSec: Int64, counterType: PerformanceCounterType, counterTimeStamp: Int64)
    """
    @property
    def BaseValue(self) -> Int64:
        """ Get: BaseValue(self: CounterSample) -> Int64 """
        ...

    @property
    def CounterFrequency(self) -> Int64:
        """ Get: CounterFrequency(self: CounterSample) -> Int64 """
        ...

    @property
    def CounterTimeStamp(self) -> Int64:
        """ Get: CounterTimeStamp(self: CounterSample) -> Int64 """
        ...

    @property
    def CounterType(self) -> PerformanceCounterType:
        """ Get: CounterType(self: CounterSample) -> PerformanceCounterType """
        ...

    @property
    def RawValue(self) -> Int64:
        """ Get: RawValue(self: CounterSample) -> Int64 """
        ...

    @property
    def SystemFrequency(self) -> Int64:
        """ Get: SystemFrequency(self: CounterSample) -> Int64 """
        ...

    @property
    def TimeStamp(self) -> Int64:
        """ Get: TimeStamp(self: CounterSample) -> Int64 """
        ...

    @property
    def TimeStamp100nSec(self) -> Int64:
        """ Get: TimeStamp100nSec(self: CounterSample) -> Int64 """
        ...


    @staticmethod
    def Calculate(counterSample:CounterSample, nextCounterSample:CounterSample = ...) -> Single:
        """
        Calculate(counterSample: CounterSample) -> Single
        Calculate(counterSample: CounterSample, nextCounterSample: CounterSample) -> Single
        """
        ...

    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: CounterSample, o: object) -> bool
        Equals(self: CounterSample, sample: CounterSample) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CounterSample) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Empty: CounterSample = ...


class CounterSampleCalculator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ComputeCounterValue(*__args:CounterSample) -> Single:
        """
        ComputeCounterValue(newSample: CounterSample) -> Single
        ComputeCounterValue(oldSample: CounterSample, newSample: CounterSample) -> Single
        """
        ...

    __all__: list = ...


class DataReceivedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Data(self) -> str:
        """ Get: Data(self: DataReceivedEventArgs) -> str """
        ...



class DataReceivedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DataReceivedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DataReceivedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DataReceivedEventHandler, sender: object, e: DataReceivedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DataReceivedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DataReceivedEventArgs): # -> 
        """ Invoke(self: DataReceivedEventHandler, sender: object, e: DataReceivedEventArgs) """
        ...


class Debug: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AutoFlush(self) -> bool:
        """
        Get: AutoFlush() -> bool
        Set: AutoFlush() = value
        """
        ...

    @property
    def IndentLevel(self) -> int:
        """
        Get: IndentLevel() -> int
        Set: IndentLevel() = value
        """
        ...

    @property
    def IndentSize(self) -> int:
        """
        Get: IndentSize() -> int
        Set: IndentSize() = value
        """
        ...

    @property
    def Listeners(self) -> TraceListenerCollection:
        """ Get: Listeners() -> TraceListenerCollection """
        ...


    @staticmethod
    def Assert(condition:bool, message:str = ..., *__args:str): # -> 
        """ Assert(condition: bool)Assert(condition: bool, message: str)Assert(condition: bool, message: str, detailMessage: str)Assert(condition: bool, message: str, detailMessageFormat: str, *args: Array[object]) """
        ...

    @staticmethod
    def Close(): # -> 
        """ Close() """
        ...

    @staticmethod
    def Fail(message:str, detailMessage:str = ...): # -> 
        """ Fail(message: str)Fail(message: str, detailMessage: str) """
        ...

    @staticmethod
    def Flush(): # -> 
        """ Flush() """
        ...

    @staticmethod
    def Indent(): # -> 
        """ Indent() """
        ...

    @staticmethod
    def Print(*__args:str): # -> 
        """ Print(message: str)Print(format: str, *args: Array[object]) """
        ...

    @staticmethod
    def Unindent(): # -> 
        """ Unindent() """
        ...

    @staticmethod
    def Write(*__args:str): # -> 
        """ Write(message: str)Write(value: object)Write(message: str, category: str)Write(value: object, category: str) """
        ...

    @staticmethod
    def WriteIf(condition:bool, *__args:str): # -> 
        """ WriteIf(condition: bool, message: str)WriteIf(condition: bool, value: object)WriteIf(condition: bool, message: str, category: str)WriteIf(condition: bool, value: object, category: str) """
        ...

    @staticmethod
    def WriteLine(*__args:str): # -> 
        """ WriteLine(message: str)WriteLine(value: object)WriteLine(message: str, category: str)WriteLine(value: object, category: str)WriteLine(format: str, *args: Array[object]) """
        ...

    @staticmethod
    def WriteLineIf(condition:bool, *__args:str): # -> 
        """ WriteLineIf(condition: bool, message: str)WriteLineIf(condition: bool, value: object)WriteLineIf(condition: bool, message: str, category: str)WriteLineIf(condition: bool, value: object, category: str) """
        ...

    __all__: list = ...


class DebuggableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DebuggableAttribute(isJITTrackingEnabled: bool, isJITOptimizerDisabled: bool)
    DebuggableAttribute(modes: DebuggingModes)
    """
    @property
    def DebuggingFlags(self): # -> DebuggingModes
        """ Get: DebuggingFlags(self: DebuggableAttribute) -> DebuggingModes """
        ...

    @property
    def IsJITOptimizerDisabled(self) -> bool:
        """ Get: IsJITOptimizerDisabled(self: DebuggableAttribute) -> bool """
        ...

    @property
    def IsJITTrackingEnabled(self) -> bool:
        """ Get: IsJITTrackingEnabled(self: DebuggableAttribute) -> bool """
        ...


    def DebuggingModes(self, *args): #cannot find CLR method
        """ enum (flags) DebuggingModes, values: Default (1), DisableOptimizations (256), EnableEditAndContinue (4), IgnoreSymbolStoreSequencePoints (2), None (0) """
        ...

    def __new__(cls, *__args) -> Self: # Not found arg types: {'*__args': 'DebuggingModes'}
        """
        __new__(cls: type, isJITTrackingEnabled: bool, isJITOptimizerDisabled: bool)
        __new__(cls: type, modes: DebuggingModes)
        """
        ...



class Debugger: # skipped bases: <type 'object'>, <type 'object'>
    """ Debugger() """
    @property
    def IsAttached(self) -> bool:
        """ Get: IsAttached() -> bool """
        ...


    @staticmethod
    def Break(): # -> 
        """ Break() """
        ...

    @staticmethod
    def IsLogging() -> bool:
        """ IsLogging() -> bool """
        ...

    @staticmethod
    def Launch() -> bool:
        """ Launch() -> bool """
        ...

    @staticmethod
    def Log(level:int, category:str, message:str): # -> 
        """ Log(level: int, category: str, message: str) """
        ...

    @staticmethod
    def NotifyOfCrossThreadDependency(): # -> 
        """ NotifyOfCrossThreadDependency() """
        ...



class DebuggerBrowsableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DebuggerBrowsableAttribute(state: DebuggerBrowsableState) """
    @property
    def State(self) -> DebuggerBrowsableState:
        """ Get: State(self: DebuggerBrowsableAttribute) -> DebuggerBrowsableState """
        ...


    def __new__(cls, state:DebuggerBrowsableState) -> Self:
        """ __new__(cls: type, state: DebuggerBrowsableState) """
        ...


class DebuggerBrowsableState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DebuggerBrowsableState, values: Collapsed (2), Never (0), RootHidden (3) """
    Collapsed: DebuggerBrowsableState = ...
    Never: DebuggerBrowsableState = ...
    RootHidden: DebuggerBrowsableState = ...
    value__ = ...


class DebuggerDisplayAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DebuggerDisplayAttribute(value: str) """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: DebuggerDisplayAttribute) -> str
        Set: Name(self: DebuggerDisplayAttribute) = value
        """
        ...

    @property
    def Target(self) -> Type:
        """
        Get: Target(self: DebuggerDisplayAttribute) -> Type
        Set: Target(self: DebuggerDisplayAttribute) = value
        """
        ...

    @property
    def TargetTypeName(self) -> str:
        """
        Get: TargetTypeName(self: DebuggerDisplayAttribute) -> str
        Set: TargetTypeName(self: DebuggerDisplayAttribute) = value
        """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: DebuggerDisplayAttribute) -> str
        Set: Type(self: DebuggerDisplayAttribute) = value
        """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: DebuggerDisplayAttribute) -> str """
        ...


    def __new__(cls, value:str) -> Self:
        """ __new__(cls: type, value: str) """
        ...


class DebuggerHiddenAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DebuggerHiddenAttribute() """
    pass

class DebuggerNonUserCodeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DebuggerNonUserCodeAttribute() """
    pass

class DebuggerStepperBoundaryAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DebuggerStepperBoundaryAttribute() """
    pass

class DebuggerStepThroughAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DebuggerStepThroughAttribute() """
    pass

class DebuggerTypeProxyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DebuggerTypeProxyAttribute(type: Type)
    DebuggerTypeProxyAttribute(typeName: str)
    """
    @property
    def ProxyTypeName(self) -> str:
        """ Get: ProxyTypeName(self: DebuggerTypeProxyAttribute) -> str """
        ...

    @property
    def Target(self) -> Type:
        """
        Get: Target(self: DebuggerTypeProxyAttribute) -> Type
        Set: Target(self: DebuggerTypeProxyAttribute) = value
        """
        ...

    @property
    def TargetTypeName(self) -> str:
        """
        Get: TargetTypeName(self: DebuggerTypeProxyAttribute) -> str
        Set: TargetTypeName(self: DebuggerTypeProxyAttribute) = value
        """
        ...


    def __new__(cls, *__args:Type) -> Self:
        """
        __new__(cls: type, type: Type)
        __new__(cls: type, typeName: str)
        """
        ...


class DebuggerVisualizerAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DebuggerVisualizerAttribute(visualizerTypeName: str)
    DebuggerVisualizerAttribute(visualizerTypeName: str, visualizerObjectSourceTypeName: str)
    DebuggerVisualizerAttribute(visualizerTypeName: str, visualizerObjectSource: Type)
    DebuggerVisualizerAttribute(visualizer: Type)
    DebuggerVisualizerAttribute(visualizer: Type, visualizerObjectSource: Type)
    DebuggerVisualizerAttribute(visualizer: Type, visualizerObjectSourceTypeName: str)
    """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: DebuggerVisualizerAttribute) -> str
        Set: Description(self: DebuggerVisualizerAttribute) = value
        """
        ...

    @property
    def Target(self) -> Type:
        """
        Get: Target(self: DebuggerVisualizerAttribute) -> Type
        Set: Target(self: DebuggerVisualizerAttribute) = value
        """
        ...

    @property
    def TargetTypeName(self) -> str:
        """
        Get: TargetTypeName(self: DebuggerVisualizerAttribute) -> str
        Set: TargetTypeName(self: DebuggerVisualizerAttribute) = value
        """
        ...

    @property
    def VisualizerObjectSourceTypeName(self) -> str:
        """ Get: VisualizerObjectSourceTypeName(self: DebuggerVisualizerAttribute) -> str """
        ...

    @property
    def VisualizerTypeName(self) -> str:
        """ Get: VisualizerTypeName(self: DebuggerVisualizerAttribute) -> str """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, visualizerTypeName: str)
        __new__(cls: type, visualizerTypeName: str, visualizerObjectSourceTypeName: str)
        __new__(cls: type, visualizerTypeName: str, visualizerObjectSource: Type)
        __new__(cls: type, visualizer: Type)
        __new__(cls: type, visualizer: Type, visualizerObjectSource: Type)
        __new__(cls: type, visualizer: Type, visualizerObjectSourceTypeName: str)
        """
        ...


class DefaultTraceListener(TraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ DefaultTraceListener() """
    @property
    def AssertUiEnabled(self) -> bool:
        """
        Get: AssertUiEnabled(self: DefaultTraceListener) -> bool
        Set: AssertUiEnabled(self: DefaultTraceListener) = value
        """
        ...

    @property
    def LogFileName(self) -> str:
        """
        Get: LogFileName(self: DefaultTraceListener) -> str
        Set: LogFileName(self: DefaultTraceListener) = value
        """
        ...



class DelimitedListTraceListener(TextWriterTraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    DelimitedListTraceListener(stream: Stream)
    DelimitedListTraceListener(stream: Stream, name: str)
    DelimitedListTraceListener(writer: TextWriter)
    DelimitedListTraceListener(writer: TextWriter, name: str)
    DelimitedListTraceListener(fileName: str)
    DelimitedListTraceListener(fileName: str, name: str)
    """
    @property
    def Delimiter(self) -> str:
        """
        Get: Delimiter(self: DelimitedListTraceListener) -> str
        Set: Delimiter(self: DelimitedListTraceListener) = value
        """
        ...


    def TraceData(self, eventCache:TraceEventCache, source:str, eventType:TraceEventType, id:int, data:object): # -> 
        """ TraceData(self: DelimitedListTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, data: object)TraceData(self: DelimitedListTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, *data: Array[object]) """
        ...

    def TraceEvent(self, eventCache:TraceEventCache, source:str, eventType:TraceEventType, id:int, *__args:str): # -> 
        """ TraceEvent(self: DelimitedListTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, format: str, *args: Array[object])TraceEvent(self: DelimitedListTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, message: str) """
        ...


class DiagnosticsConfigurationHandler(IConfigurationSectionHandler): # skipped bases: <type 'object'>
    """ DiagnosticsConfigurationHandler() """
    pass

class EntryWrittenEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    EntryWrittenEventArgs()
    EntryWrittenEventArgs(entry: EventLogEntry)
    """
    @property
    def Entry(self) -> EventLogEntry:
        """ Get: Entry(self: EntryWrittenEventArgs) -> EventLogEntry """
        ...


    def __new__(cls, entry:EventLogEntry = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, entry: EventLogEntry)
        """
        ...


class EntryWrittenEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EntryWrittenEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:EntryWrittenEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: EntryWrittenEventHandler, sender: object, e: EntryWrittenEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: EntryWrittenEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:EntryWrittenEventArgs): # -> 
        """ Invoke(self: EntryWrittenEventHandler, sender: object, e: EntryWrittenEventArgs) """
        ...


class EventInstance: # skipped bases: <type 'object'>, <type 'object'>
    """
    EventInstance(instanceId: Int64, categoryId: int)
    EventInstance(instanceId: Int64, categoryId: int, entryType: EventLogEntryType)
    """
    @property
    def CategoryId(self) -> int:
        """
        Get: CategoryId(self: EventInstance) -> int
        Set: CategoryId(self: EventInstance) = value
        """
        ...

    @property
    def EntryType(self) -> EventLogEntryType:
        """
        Get: EntryType(self: EventInstance) -> EventLogEntryType
        Set: EntryType(self: EventInstance) = value
        """
        ...

    @property
    def InstanceId(self) -> Int64:
        """
        Get: InstanceId(self: EventInstance) -> Int64
        Set: InstanceId(self: EventInstance) = value
        """
        ...



class EventLog(ISupportInitialize, Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    EventLog()
    EventLog(logName: str)
    EventLog(logName: str, machineName: str)
    EventLog(logName: str, machineName: str, source: str)
    """
    @property
    def EnableRaisingEvents(self) -> bool:
        """
        Get: EnableRaisingEvents(self: EventLog) -> bool
        Set: EnableRaisingEvents(self: EventLog) = value
        """
        ...

    @property
    def Entries(self) -> EventLogEntryCollection:
        """ Get: Entries(self: EventLog) -> EventLogEntryCollection """
        ...

    @property
    def Log(self) -> str:
        """
        Get: Log(self: EventLog) -> str
        Set: Log(self: EventLog) = value
        """
        ...

    @property
    def LogDisplayName(self) -> str:
        """ Get: LogDisplayName(self: EventLog) -> str """
        ...

    @property
    def MachineName(self) -> str:
        """
        Get: MachineName(self: EventLog) -> str
        Set: MachineName(self: EventLog) = value
        """
        ...

    @property
    def MaximumKilobytes(self) -> Int64:
        """
        Get: MaximumKilobytes(self: EventLog) -> Int64
        Set: MaximumKilobytes(self: EventLog) = value
        """
        ...

    @property
    def MinimumRetentionDays(self) -> int:
        """ Get: MinimumRetentionDays(self: EventLog) -> int """
        ...

    @property
    def OverflowAction(self) -> OverflowAction:
        """ Get: OverflowAction(self: EventLog) -> OverflowAction """
        ...

    @property
    def Source(self) -> str:
        """
        Get: Source(self: EventLog) -> str
        Set: Source(self: EventLog) = value
        """
        ...

    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """
        Get: SynchronizingObject(self: EventLog) -> ISynchronizeInvoke
        Set: SynchronizingObject(self: EventLog) = value
        """
        ...


    def Clear(self): # -> 
        """ Clear(self: EventLog) """
        ...

    def Close(self): # -> 
        """ Close(self: EventLog) """
        ...

    @staticmethod
    def CreateEventSource(*__args:EventSourceCreationData): # -> 
        """ CreateEventSource(source: str, logName: str, machineName: str)CreateEventSource(source: str, logName: str)CreateEventSource(sourceData: EventSourceCreationData) """
        ...

    @staticmethod
    def Delete(logName:str, machineName:str = ...): # -> 
        """ Delete(logName: str)Delete(logName: str, machineName: str) """
        ...

    @staticmethod
    def DeleteEventSource(source:str, machineName:str = ...): # -> 
        """ DeleteEventSource(source: str)DeleteEventSource(source: str, machineName: str) """
        ...

    @staticmethod
    def Exists(logName:str, machineName:str = ...) -> bool:
        """
        Exists(logName: str) -> bool
        Exists(logName: str, machineName: str) -> bool
        """
        ...

    @staticmethod
    def GetEventLogs(machineName=None) -> Array:
        """
        GetEventLogs() -> Array[EventLog]
        GetEventLogs(machineName: str) -> Array[EventLog]
        """
        ...

    @staticmethod
    def LogNameFromSourceName(source:str, machineName:str) -> str:
        """ LogNameFromSourceName(source: str, machineName: str) -> str """
        ...

    def ModifyOverflowPolicy(self, action:OverflowAction, retentionDays:int): # -> 
        """ ModifyOverflowPolicy(self: EventLog, action: OverflowAction, retentionDays: int) """
        ...

    def RegisterDisplayName(self, resourceFile:str, resourceId:Int64): # -> 
        """ RegisterDisplayName(self: EventLog, resourceFile: str, resourceId: Int64) """
        ...

    @staticmethod
    def SourceExists(source:str, machineName:str = ...) -> bool:
        """
        SourceExists(source: str, machineName: str) -> bool
        SourceExists(source: str) -> bool
        """
        ...

    @staticmethod
    def WriteEntry(*__args): # -> 
        """ WriteEntry(source: str, message: str)WriteEntry(source: str, message: str, type: EventLogEntryType)WriteEntry(source: str, message: str, type: EventLogEntryType, eventID: int)WriteEntry(source: str, message: str, type: EventLogEntryType, eventID: int, category: Int16)WriteEntry(self: EventLog, message: str)WriteEntry(self: EventLog, message: str, type: EventLogEntryType)WriteEntry(self: EventLog, message: str, type: EventLogEntryType, eventID: int)WriteEntry(self: EventLog, message: str, type: EventLogEntryType, eventID: int, category: Int16)WriteEntry(source: str, message: str, type: EventLogEntryType, eventID: int, category: Int16, rawData: Array[Byte])WriteEntry(self: EventLog, message: str, type: EventLogEntryType, eventID: int, category: Int16, rawData: Array[Byte]) """
        ...

    def WriteEvent(self, *__args): # -> 
        """ WriteEvent(self: EventLog, instance: EventInstance, *values: Array[object])WriteEvent(self: EventLog, instance: EventInstance, data: Array[Byte], *values: Array[object])WriteEvent(source: str, instance: EventInstance, *values: Array[object])WriteEvent(source: str, instance: EventInstance, data: Array[Byte], *values: Array[object]) """
        ...

    def __new__(cls, logName:str = ..., machineName:str = ..., source:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, logName: str)
        __new__(cls: type, logName: str, machineName: str)
        __new__(cls: type, logName: str, machineName: str, source: str)
        """
        ...

    EntryWritten = ...


class EventLogEntry(ISerializable, Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def Category(self) -> str:
        """ Get: Category(self: EventLogEntry) -> str """
        ...

    @property
    def CategoryNumber(self) -> Int16:
        """ Get: CategoryNumber(self: EventLogEntry) -> Int16 """
        ...

    @property
    def Data(self) -> Array:
        """ Get: Data(self: EventLogEntry) -> Array[Byte] """
        ...

    @property
    def EntryType(self) -> EventLogEntryType:
        """ Get: EntryType(self: EventLogEntry) -> EventLogEntryType """
        ...

    @property
    def EventID(self) -> int:
        """ Get: EventID(self: EventLogEntry) -> int """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: EventLogEntry) -> int """
        ...

    @property
    def InstanceId(self) -> Int64:
        """ Get: InstanceId(self: EventLogEntry) -> Int64 """
        ...

    @property
    def MachineName(self) -> str:
        """ Get: MachineName(self: EventLogEntry) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: EventLogEntry) -> str """
        ...

    @property
    def ReplacementStrings(self) -> Array:
        """ Get: ReplacementStrings(self: EventLogEntry) -> Array[str] """
        ...

    @property
    def Source(self) -> str:
        """ Get: Source(self: EventLogEntry) -> str """
        ...

    @property
    def TimeGenerated(self) -> DateTime:
        """ Get: TimeGenerated(self: EventLogEntry) -> DateTime """
        ...

    @property
    def TimeWritten(self) -> DateTime:
        """ Get: TimeWritten(self: EventLogEntry) -> DateTime """
        ...

    @property
    def UserName(self) -> str:
        """ Get: UserName(self: EventLogEntry) -> str """
        ...


    def Equals(self, *__args:EventLogEntry) -> bool:
        """ Equals(self: EventLogEntry, otherEntry: EventLogEntry) -> bool """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...


class EventLogEntryCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: EventLogEntryCollection) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class EventLogEntryType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EventLogEntryType, values: Error (1), FailureAudit (16), Information (4), SuccessAudit (8), Warning (2) """
    Error: EventLogEntryType = ...
    FailureAudit: EventLogEntryType = ...
    Information: EventLogEntryType = ...
    SuccessAudit: EventLogEntryType = ...
    value__ = ...
    Warning: EventLogEntryType = ...


class EventLogInstaller(ComponentInstaller): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ EventLogInstaller() """
    @property
    def CategoryCount(self) -> int:
        """
        Get: CategoryCount(self: EventLogInstaller) -> int
        Set: CategoryCount(self: EventLogInstaller) = value
        """
        ...

    @property
    def CategoryResourceFile(self) -> str:
        """
        Get: CategoryResourceFile(self: EventLogInstaller) -> str
        Set: CategoryResourceFile(self: EventLogInstaller) = value
        """
        ...

    @property
    def Log(self) -> str:
        """
        Get: Log(self: EventLogInstaller) -> str
        Set: Log(self: EventLogInstaller) = value
        """
        ...

    @property
    def MessageResourceFile(self) -> str:
        """
        Get: MessageResourceFile(self: EventLogInstaller) -> str
        Set: MessageResourceFile(self: EventLogInstaller) = value
        """
        ...

    @property
    def ParameterResourceFile(self) -> str:
        """
        Get: ParameterResourceFile(self: EventLogInstaller) -> str
        Set: ParameterResourceFile(self: EventLogInstaller) = value
        """
        ...

    @property
    def Source(self) -> str:
        """
        Get: Source(self: EventLogInstaller) -> str
        Set: Source(self: EventLogInstaller) = value
        """
        ...

    @property
    def UninstallAction(self) -> UninstallAction:
        """
        Get: UninstallAction(self: EventLogInstaller) -> UninstallAction
        Set: UninstallAction(self: EventLogInstaller) = value
        """
        ...


    def Install(self, stateSaver:IDictionary): # -> 
        """ Install(self: EventLogInstaller, stateSaver: IDictionary) """
        ...

    def Rollback(self, savedState:IDictionary): # -> 
        """ Rollback(self: EventLogInstaller, savedState: IDictionary) """
        ...

    def Uninstall(self, savedState:IDictionary): # -> 
        """ Uninstall(self: EventLogInstaller, savedState: IDictionary) """
        ...


class EventLogPermission(ResourcePermissionBase): # skipped bases: <type 'IPermission'>, <type 'IUnrestrictedPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    EventLogPermission()
    EventLogPermission(state: PermissionState)
    EventLogPermission(permissionAccess: EventLogPermissionAccess, machineName: str)
    EventLogPermission(permissionAccessEntries: Array[EventLogPermissionEntry])
    """
    @property
    def PermissionEntries(self) -> EventLogPermissionEntryCollection:
        """ Get: PermissionEntries(self: EventLogPermission) -> EventLogPermissionEntryCollection """
        ...



class EventLogPermissionAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EventLogPermissionAccess, values: Administer (48), Audit (10), Browse (2), Instrument (6), None (0), Write (16) """
    Administer: EventLogPermissionAccess = ...
    Audit: EventLogPermissionAccess = ...
    Browse: EventLogPermissionAccess = ...
    Instrument: EventLogPermissionAccess = ...
    value__ = ...
    Write: EventLogPermissionAccess = ...


class EventLogPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EventLogPermissionAttribute(action: SecurityAction) """
    @property
    def MachineName(self) -> str:
        """
        Get: MachineName(self: EventLogPermissionAttribute) -> str
        Set: MachineName(self: EventLogPermissionAttribute) = value
        """
        ...

    @property
    def PermissionAccess(self) -> EventLogPermissionAccess:
        """
        Get: PermissionAccess(self: EventLogPermissionAttribute) -> EventLogPermissionAccess
        Set: PermissionAccess(self: EventLogPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: EventLogPermissionAttribute) -> IPermission """
        ...


class EventLogPermissionEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ EventLogPermissionEntry(permissionAccess: EventLogPermissionAccess, machineName: str) """
    @property
    def MachineName(self) -> str:
        """ Get: MachineName(self: EventLogPermissionEntry) -> str """
        ...

    @property
    def PermissionAccess(self) -> EventLogPermissionAccess:
        """ Get: PermissionAccess(self: EventLogPermissionEntry) -> EventLogPermissionAccess """
        ...



class EventLogPermissionEntryCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, value:EventLogPermissionEntry) -> int:
        """ Add(self: EventLogPermissionEntryCollection, value: EventLogPermissionEntry) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: EventLogPermissionEntryCollection, value: Array[EventLogPermissionEntry])AddRange(self: EventLogPermissionEntryCollection, value: EventLogPermissionEntryCollection) """
        ...

    def Contains(self, value:EventLogPermissionEntry) -> bool:
        """ Contains(self: EventLogPermissionEntryCollection, value: EventLogPermissionEntry) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: EventLogPermissionEntryCollection, array: Array[EventLogPermissionEntry], index: int) """
        ...

    def IndexOf(self, value:EventLogPermissionEntry) -> int:
        """ IndexOf(self: EventLogPermissionEntryCollection, value: EventLogPermissionEntry) -> int """
        ...

    def Insert(self, index:int, value:EventLogPermissionEntry): # -> 
        """ Insert(self: EventLogPermissionEntryCollection, index: int, value: EventLogPermissionEntry) """
        ...

    def Remove(self, value:EventLogPermissionEntry): # -> 
        """ Remove(self: EventLogPermissionEntryCollection, value: EventLogPermissionEntry) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class EventLogTraceListener(TraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    EventLogTraceListener()
    EventLogTraceListener(eventLog: EventLog)
    EventLogTraceListener(source: str)
    """
    @property
    def EventLog(self) -> EventLog:
        """
        Get: EventLog(self: EventLogTraceListener) -> EventLog
        Set: EventLog(self: EventLogTraceListener) = value
        """
        ...



class EventSchemaTraceListener(TextWriterTraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    EventSchemaTraceListener(fileName: str)
    EventSchemaTraceListener(fileName: str, name: str)
    EventSchemaTraceListener(fileName: str, name: str, bufferSize: int)
    EventSchemaTraceListener(fileName: str, name: str, bufferSize: int, logRetentionOption: TraceLogRetentionOption)
    EventSchemaTraceListener(fileName: str, name: str, bufferSize: int, logRetentionOption: TraceLogRetentionOption, maximumFileSize: Int64)
    EventSchemaTraceListener(fileName: str, name: str, bufferSize: int, logRetentionOption: TraceLogRetentionOption, maximumFileSize: Int64, maximumNumberOfFiles: int)
    """
    @property
    def BufferSize(self) -> int:
        """ Get: BufferSize(self: EventSchemaTraceListener) -> int """
        ...

    @property
    def IsThreadSafe(self) -> bool:
        """ Get: IsThreadSafe(self: EventSchemaTraceListener) -> bool """
        ...

    @property
    def MaximumFileSize(self) -> Int64:
        """ Get: MaximumFileSize(self: EventSchemaTraceListener) -> Int64 """
        ...

    @property
    def MaximumNumberOfFiles(self) -> int:
        """ Get: MaximumNumberOfFiles(self: EventSchemaTraceListener) -> int """
        ...

    @property
    def TraceLogRetentionOption(self): # -> TraceLogRetentionOption
        """ Get: TraceLogRetentionOption(self: EventSchemaTraceListener) -> TraceLogRetentionOption """
        ...


    def Fail(self, message:str, detailMessage:str = ...): # -> 
        """ Fail(self: EventSchemaTraceListener, message: str, detailMessage: str) """
        ...

    def TraceData(self, eventCache:TraceEventCache, source:str, eventType:TraceEventType, id:int, data:object): # -> 
        """ TraceData(self: EventSchemaTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, data: object)TraceData(self: EventSchemaTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, *data: Array[object]) """
        ...

    def TraceEvent(self, eventCache:TraceEventCache, source:str, eventType:TraceEventType, id:int, *__args:str): # -> 
        """ TraceEvent(self: EventSchemaTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, format: str, *args: Array[object])TraceEvent(self: EventSchemaTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, message: str) """
        ...

    def TraceTransfer(self, eventCache:TraceEventCache, source:str, id:int, message:str, relatedActivityId:Guid): # -> 
        """ TraceTransfer(self: EventSchemaTraceListener, eventCache: TraceEventCache, source: str, id: int, message: str, relatedActivityId: Guid) """
        ...


class EventSourceCreationData: # skipped bases: <type 'object'>, <type 'object'>
    """ EventSourceCreationData(source: str, logName: str) """
    @property
    def CategoryCount(self) -> int:
        """
        Get: CategoryCount(self: EventSourceCreationData) -> int
        Set: CategoryCount(self: EventSourceCreationData) = value
        """
        ...

    @property
    def CategoryResourceFile(self) -> str:
        """
        Get: CategoryResourceFile(self: EventSourceCreationData) -> str
        Set: CategoryResourceFile(self: EventSourceCreationData) = value
        """
        ...

    @property
    def LogName(self) -> str:
        """
        Get: LogName(self: EventSourceCreationData) -> str
        Set: LogName(self: EventSourceCreationData) = value
        """
        ...

    @property
    def MachineName(self) -> str:
        """
        Get: MachineName(self: EventSourceCreationData) -> str
        Set: MachineName(self: EventSourceCreationData) = value
        """
        ...

    @property
    def MessageResourceFile(self) -> str:
        """
        Get: MessageResourceFile(self: EventSourceCreationData) -> str
        Set: MessageResourceFile(self: EventSourceCreationData) = value
        """
        ...

    @property
    def ParameterResourceFile(self) -> str:
        """
        Get: ParameterResourceFile(self: EventSourceCreationData) -> str
        Set: ParameterResourceFile(self: EventSourceCreationData) = value
        """
        ...

    @property
    def Source(self) -> str:
        """
        Get: Source(self: EventSourceCreationData) -> str
        Set: Source(self: EventSourceCreationData) = value
        """
        ...



class TraceFilter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def ShouldTrace(self, cache:TraceEventCache, source:str, eventType:TraceEventType, id:int, formatOrMessage:str, args:Array, data1:object, data:Array) -> bool:
        """ ShouldTrace(self: TraceFilter, cache: TraceEventCache, source: str, eventType: TraceEventType, id: int, formatOrMessage: str, args: Array[object], data1: object, data: Array[object]) -> bool """
        ...


class EventTypeFilter(TraceFilter): # skipped bases: <type 'object'>
    """ EventTypeFilter(level: SourceLevels) """
    @property
    def EventType(self) -> SourceLevels:
        """
        Get: EventType(self: EventTypeFilter) -> SourceLevels
        Set: EventType(self: EventTypeFilter) = value
        """
        ...


    def __new__(cls, level:SourceLevels) -> Self:
        """ __new__(cls: type, level: SourceLevels) """
        ...


class FileVersionInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Comments(self) -> str:
        """ Get: Comments(self: FileVersionInfo) -> str """
        ...

    @property
    def CompanyName(self) -> str:
        """ Get: CompanyName(self: FileVersionInfo) -> str """
        ...

    @property
    def FileBuildPart(self) -> int:
        """ Get: FileBuildPart(self: FileVersionInfo) -> int """
        ...

    @property
    def FileDescription(self) -> str:
        """ Get: FileDescription(self: FileVersionInfo) -> str """
        ...

    @property
    def FileMajorPart(self) -> int:
        """ Get: FileMajorPart(self: FileVersionInfo) -> int """
        ...

    @property
    def FileMinorPart(self) -> int:
        """ Get: FileMinorPart(self: FileVersionInfo) -> int """
        ...

    @property
    def FileName(self) -> str:
        """ Get: FileName(self: FileVersionInfo) -> str """
        ...

    @property
    def FilePrivatePart(self) -> int:
        """ Get: FilePrivatePart(self: FileVersionInfo) -> int """
        ...

    @property
    def FileVersion(self) -> str:
        """ Get: FileVersion(self: FileVersionInfo) -> str """
        ...

    @property
    def InternalName(self) -> str:
        """ Get: InternalName(self: FileVersionInfo) -> str """
        ...

    @property
    def IsDebug(self) -> bool:
        """ Get: IsDebug(self: FileVersionInfo) -> bool """
        ...

    @property
    def IsPatched(self) -> bool:
        """ Get: IsPatched(self: FileVersionInfo) -> bool """
        ...

    @property
    def IsPreRelease(self) -> bool:
        """ Get: IsPreRelease(self: FileVersionInfo) -> bool """
        ...

    @property
    def IsPrivateBuild(self) -> bool:
        """ Get: IsPrivateBuild(self: FileVersionInfo) -> bool """
        ...

    @property
    def IsSpecialBuild(self) -> bool:
        """ Get: IsSpecialBuild(self: FileVersionInfo) -> bool """
        ...

    @property
    def Language(self) -> str:
        """ Get: Language(self: FileVersionInfo) -> str """
        ...

    @property
    def LegalCopyright(self) -> str:
        """ Get: LegalCopyright(self: FileVersionInfo) -> str """
        ...

    @property
    def LegalTrademarks(self) -> str:
        """ Get: LegalTrademarks(self: FileVersionInfo) -> str """
        ...

    @property
    def OriginalFilename(self) -> str:
        """ Get: OriginalFilename(self: FileVersionInfo) -> str """
        ...

    @property
    def PrivateBuild(self) -> str:
        """ Get: PrivateBuild(self: FileVersionInfo) -> str """
        ...

    @property
    def ProductBuildPart(self) -> int:
        """ Get: ProductBuildPart(self: FileVersionInfo) -> int """
        ...

    @property
    def ProductMajorPart(self) -> int:
        """ Get: ProductMajorPart(self: FileVersionInfo) -> int """
        ...

    @property
    def ProductMinorPart(self) -> int:
        """ Get: ProductMinorPart(self: FileVersionInfo) -> int """
        ...

    @property
    def ProductName(self) -> str:
        """ Get: ProductName(self: FileVersionInfo) -> str """
        ...

    @property
    def ProductPrivatePart(self) -> int:
        """ Get: ProductPrivatePart(self: FileVersionInfo) -> int """
        ...

    @property
    def ProductVersion(self) -> str:
        """ Get: ProductVersion(self: FileVersionInfo) -> str """
        ...

    @property
    def SpecialBuild(self) -> str:
        """ Get: SpecialBuild(self: FileVersionInfo) -> str """
        ...


    @staticmethod
    def GetVersionInfo(fileName:str) -> FileVersionInfo:
        """ GetVersionInfo(fileName: str) -> FileVersionInfo """
        ...

    def ToString(self) -> str:
        """ ToString(self: FileVersionInfo) -> str """
        ...


class ICollectData: # skipped bases: <type 'object'>
    """ no doc """
    def CloseData(self): # -> 
        """ CloseData(self: ICollectData) """
        ...

    def CollectData(self, id, valueName, data, totalBytes, res) -> IntPtr:
        """ CollectData(self: ICollectData, id: int, valueName: IntPtr, data: IntPtr, totalBytes: int) -> IntPtr """
        ...


class InstanceData: # skipped bases: <type 'object'>, <type 'object'>
    """ InstanceData(instanceName: str, sample: CounterSample) """
    @property
    def InstanceName(self) -> str:
        """ Get: InstanceName(self: InstanceData) -> str """
        ...

    @property
    def RawValue(self) -> Int64:
        """ Get: RawValue(self: InstanceData) -> Int64 """
        ...

    @property
    def Sample(self) -> CounterSample:
        """ Get: Sample(self: InstanceData) -> CounterSample """
        ...



class InstanceDataCollection(DictionaryBase): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ InstanceDataCollection(counterName: str) """
    @property
    def CounterName(self) -> str:
        """ Get: CounterName(self: InstanceDataCollection) -> str """
        ...

    @property
    def Keys(self) -> ICollection:
        """ Get: Keys(self: InstanceDataCollection) -> ICollection """
        ...

    @property
    def Values(self) -> ICollection:
        """ Get: Values(self: InstanceDataCollection) -> ICollection """
        ...


    def Contains(self, instanceName:str) -> bool:
        """ Contains(self: InstanceDataCollection, instanceName: str) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, counterName:str) -> Self:
        """ __new__(cls: type, counterName: str) """
        ...


class InstanceDataCollectionCollection(DictionaryBase): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ InstanceDataCollectionCollection() """
    @property
    def Keys(self) -> ICollection:
        """ Get: Keys(self: InstanceDataCollectionCollection) -> ICollection """
        ...

    @property
    def Values(self) -> ICollection:
        """ Get: Values(self: InstanceDataCollectionCollection) -> ICollection """
        ...


    def Contains(self, counterName:str) -> bool:
        """ Contains(self: InstanceDataCollectionCollection, counterName: str) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class MonitoringDescriptionAttribute(DescriptionAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MonitoringDescriptionAttribute(description: str) """
    pass

class OverflowAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OverflowAction, values: DoNotOverwrite (-1), OverwriteAsNeeded (0), OverwriteOlder (1) """
    DoNotOverwrite: OverflowAction = ...
    OverwriteAsNeeded: OverflowAction = ...
    OverwriteOlder: OverflowAction = ...
    value__ = ...


class PerformanceCounter(ISupportInitialize, Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    PerformanceCounter()
    PerformanceCounter(categoryName: str, counterName: str, instanceName: str, machineName: str)
    PerformanceCounter(categoryName: str, counterName: str, instanceName: str)
    PerformanceCounter(categoryName: str, counterName: str, instanceName: str, readOnly: bool)
    PerformanceCounter(categoryName: str, counterName: str)
    PerformanceCounter(categoryName: str, counterName: str, readOnly: bool)
    """
    @property
    def CategoryName(self) -> str:
        """
        Get: CategoryName(self: PerformanceCounter) -> str
        Set: CategoryName(self: PerformanceCounter) = value
        """
        ...

    @property
    def CounterHelp(self) -> str:
        """ Get: CounterHelp(self: PerformanceCounter) -> str """
        ...

    @property
    def CounterName(self) -> str:
        """
        Get: CounterName(self: PerformanceCounter) -> str
        Set: CounterName(self: PerformanceCounter) = value
        """
        ...

    @property
    def CounterType(self) -> PerformanceCounterType:
        """ Get: CounterType(self: PerformanceCounter) -> PerformanceCounterType """
        ...

    @property
    def InstanceLifetime(self) -> PerformanceCounterInstanceLifetime:
        """
        Get: InstanceLifetime(self: PerformanceCounter) -> PerformanceCounterInstanceLifetime
        Set: InstanceLifetime(self: PerformanceCounter) = value
        """
        ...

    @property
    def InstanceName(self) -> str:
        """
        Get: InstanceName(self: PerformanceCounter) -> str
        Set: InstanceName(self: PerformanceCounter) = value
        """
        ...

    @property
    def MachineName(self) -> str:
        """
        Get: MachineName(self: PerformanceCounter) -> str
        Set: MachineName(self: PerformanceCounter) = value
        """
        ...

    @property
    def RawValue(self) -> Int64:
        """
        Get: RawValue(self: PerformanceCounter) -> Int64
        Set: RawValue(self: PerformanceCounter) = value
        """
        ...

    @property
    def ReadOnly(self) -> bool:
        """
        Get: ReadOnly(self: PerformanceCounter) -> bool
        Set: ReadOnly(self: PerformanceCounter) = value
        """
        ...


    def Close(self): # -> 
        """ Close(self: PerformanceCounter) """
        ...

    @staticmethod
    def CloseSharedResources(): # -> 
        """ CloseSharedResources() """
        ...

    def Decrement(self) -> Int64:
        """ Decrement(self: PerformanceCounter) -> Int64 """
        ...

    def Increment(self) -> Int64:
        """ Increment(self: PerformanceCounter) -> Int64 """
        ...

    def IncrementBy(self, value:Int64) -> Int64:
        """ IncrementBy(self: PerformanceCounter, value: Int64) -> Int64 """
        ...

    def NextSample(self) -> CounterSample:
        """ NextSample(self: PerformanceCounter) -> CounterSample """
        ...

    def NextValue(self) -> Single:
        """ NextValue(self: PerformanceCounter) -> Single """
        ...

    def RemoveInstance(self): # -> 
        """ RemoveInstance(self: PerformanceCounter) """
        ...

    def __new__(cls, categoryName:str = ..., counterName:str = ..., *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, categoryName: str, counterName: str, instanceName: str, machineName: str)
        __new__(cls: type, categoryName: str, counterName: str, instanceName: str)
        __new__(cls: type, categoryName: str, counterName: str, instanceName: str, readOnly: bool)
        __new__(cls: type, categoryName: str, counterName: str)
        __new__(cls: type, categoryName: str, counterName: str, readOnly: bool)
        """
        ...

    DefaultFileMappingSize: int = ...


class PerformanceCounterCategory: # skipped bases: <type 'object'>, <type 'object'>
    """
    PerformanceCounterCategory()
    PerformanceCounterCategory(categoryName: str)
    PerformanceCounterCategory(categoryName: str, machineName: str)
    """
    @property
    def CategoryHelp(self) -> str:
        """ Get: CategoryHelp(self: PerformanceCounterCategory) -> str """
        ...

    @property
    def CategoryName(self) -> str:
        """
        Get: CategoryName(self: PerformanceCounterCategory) -> str
        Set: CategoryName(self: PerformanceCounterCategory) = value
        """
        ...

    @property
    def CategoryType(self) -> PerformanceCounterCategoryType:
        """ Get: CategoryType(self: PerformanceCounterCategory) -> PerformanceCounterCategoryType """
        ...

    @property
    def MachineName(self) -> str:
        """
        Get: MachineName(self: PerformanceCounterCategory) -> str
        Set: MachineName(self: PerformanceCounterCategory) = value
        """
        ...


    def CounterExists(self, counterName, categoryName=None, machineName=None) -> bool:
        """
        CounterExists(self: PerformanceCounterCategory, counterName: str) -> bool
        CounterExists(counterName: str, categoryName: str) -> bool
        CounterExists(counterName: str, categoryName: str, machineName: str) -> bool
        """
        ...

    @staticmethod
    def Create(categoryName:str, categoryHelp:str, *__args:CounterCreationDataCollection) -> PerformanceCounterCategory:
        """
        Create(categoryName: str, categoryHelp: str, counterData: CounterCreationDataCollection) -> PerformanceCounterCategory
        Create(categoryName: str, categoryHelp: str, counterName: str, counterHelp: str) -> PerformanceCounterCategory
        Create(categoryName: str, categoryHelp: str, categoryType: PerformanceCounterCategoryType, counterName: str, counterHelp: str) -> PerformanceCounterCategory
        Create(categoryName: str, categoryHelp: str, categoryType: PerformanceCounterCategoryType, counterData: CounterCreationDataCollection) -> PerformanceCounterCategory
        """
        ...

    @staticmethod
    def Delete(categoryName:str): # -> 
        """ Delete(categoryName: str) """
        ...

    @staticmethod
    def Exists(categoryName:str, machineName:str = ...) -> bool:
        """
        Exists(categoryName: str) -> bool
        Exists(categoryName: str, machineName: str) -> bool
        """
        ...

    @staticmethod
    def GetCategories(machineName=None) -> Array:
        """
        GetCategories() -> Array[PerformanceCounterCategory]
        GetCategories(machineName: str) -> Array[PerformanceCounterCategory]
        """
        ...

    def GetCounters(self, instanceName:str = ...) -> Array:
        """
        GetCounters(self: PerformanceCounterCategory) -> Array[PerformanceCounter]
        GetCounters(self: PerformanceCounterCategory, instanceName: str) -> Array[PerformanceCounter]
        """
        ...

    def GetInstanceNames(self) -> Array:
        """ GetInstanceNames(self: PerformanceCounterCategory) -> Array[str] """
        ...

    def InstanceExists(self, instanceName, categoryName=None, machineName=None) -> bool:
        """
        InstanceExists(self: PerformanceCounterCategory, instanceName: str) -> bool
        InstanceExists(instanceName: str, categoryName: str) -> bool
        InstanceExists(instanceName: str, categoryName: str, machineName: str) -> bool
        """
        ...

    def ReadCategory(self) -> InstanceDataCollectionCollection:
        """ ReadCategory(self: PerformanceCounterCategory) -> InstanceDataCollectionCollection """
        ...


class PerformanceCounterCategoryType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PerformanceCounterCategoryType, values: MultiInstance (1), SingleInstance (0), Unknown (-1) """
    MultiInstance: PerformanceCounterCategoryType = ...
    SingleInstance: PerformanceCounterCategoryType = ...
    Unknown: PerformanceCounterCategoryType = ...
    value__ = ...


class PerformanceCounterInstaller(ComponentInstaller): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ PerformanceCounterInstaller() """
    @property
    def CategoryHelp(self) -> str:
        """
        Get: CategoryHelp(self: PerformanceCounterInstaller) -> str
        Set: CategoryHelp(self: PerformanceCounterInstaller) = value
        """
        ...

    @property
    def CategoryName(self) -> str:
        """
        Get: CategoryName(self: PerformanceCounterInstaller) -> str
        Set: CategoryName(self: PerformanceCounterInstaller) = value
        """
        ...

    @property
    def CategoryType(self) -> PerformanceCounterCategoryType:
        """
        Get: CategoryType(self: PerformanceCounterInstaller) -> PerformanceCounterCategoryType
        Set: CategoryType(self: PerformanceCounterInstaller) = value
        """
        ...

    @property
    def Counters(self) -> CounterCreationDataCollection:
        """ Get: Counters(self: PerformanceCounterInstaller) -> CounterCreationDataCollection """
        ...

    @property
    def UninstallAction(self) -> UninstallAction:
        """
        Get: UninstallAction(self: PerformanceCounterInstaller) -> UninstallAction
        Set: UninstallAction(self: PerformanceCounterInstaller) = value
        """
        ...


    def Install(self, stateSaver:IDictionary): # -> 
        """ Install(self: PerformanceCounterInstaller, stateSaver: IDictionary) """
        ...

    def Rollback(self, savedState:IDictionary): # -> 
        """ Rollback(self: PerformanceCounterInstaller, savedState: IDictionary) """
        ...

    def Uninstall(self, savedState:IDictionary): # -> 
        """ Uninstall(self: PerformanceCounterInstaller, savedState: IDictionary) """
        ...


class PerformanceCounterInstanceLifetime(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PerformanceCounterInstanceLifetime, values: Global (0), Process (1) """
    Global: PerformanceCounterInstanceLifetime = ...
    Process: PerformanceCounterInstanceLifetime = ...
    value__ = ...


class PerformanceCounterManager(ICollectData): # skipped bases: <type 'object'>
    """ PerformanceCounterManager() """
    pass

class PerformanceCounterPermission(ResourcePermissionBase): # skipped bases: <type 'IPermission'>, <type 'IUnrestrictedPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    PerformanceCounterPermission()
    PerformanceCounterPermission(state: PermissionState)
    PerformanceCounterPermission(permissionAccess: PerformanceCounterPermissionAccess, machineName: str, categoryName: str)
    PerformanceCounterPermission(permissionAccessEntries: Array[PerformanceCounterPermissionEntry])
    """
    @property
    def PermissionEntries(self) -> PerformanceCounterPermissionEntryCollection:
        """ Get: PermissionEntries(self: PerformanceCounterPermission) -> PerformanceCounterPermissionEntryCollection """
        ...



class PerformanceCounterPermissionAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PerformanceCounterPermissionAccess, values: Administer (7), Browse (1), Instrument (3), None (0), Read (1), Write (2) """
    Administer: PerformanceCounterPermissionAccess = ...
    Browse: PerformanceCounterPermissionAccess = ...
    Instrument: PerformanceCounterPermissionAccess = ...
    Read: PerformanceCounterPermissionAccess = ...
    value__ = ...
    Write: PerformanceCounterPermissionAccess = ...


class PerformanceCounterPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PerformanceCounterPermissionAttribute(action: SecurityAction) """
    @property
    def CategoryName(self) -> str:
        """
        Get: CategoryName(self: PerformanceCounterPermissionAttribute) -> str
        Set: CategoryName(self: PerformanceCounterPermissionAttribute) = value
        """
        ...

    @property
    def MachineName(self) -> str:
        """
        Get: MachineName(self: PerformanceCounterPermissionAttribute) -> str
        Set: MachineName(self: PerformanceCounterPermissionAttribute) = value
        """
        ...

    @property
    def PermissionAccess(self) -> PerformanceCounterPermissionAccess:
        """
        Get: PermissionAccess(self: PerformanceCounterPermissionAttribute) -> PerformanceCounterPermissionAccess
        Set: PermissionAccess(self: PerformanceCounterPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: PerformanceCounterPermissionAttribute) -> IPermission """
        ...


class PerformanceCounterPermissionEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ PerformanceCounterPermissionEntry(permissionAccess: PerformanceCounterPermissionAccess, machineName: str, categoryName: str) """
    @property
    def CategoryName(self) -> str:
        """ Get: CategoryName(self: PerformanceCounterPermissionEntry) -> str """
        ...

    @property
    def MachineName(self) -> str:
        """ Get: MachineName(self: PerformanceCounterPermissionEntry) -> str """
        ...

    @property
    def PermissionAccess(self) -> PerformanceCounterPermissionAccess:
        """ Get: PermissionAccess(self: PerformanceCounterPermissionEntry) -> PerformanceCounterPermissionAccess """
        ...



class PerformanceCounterPermissionEntryCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, value:PerformanceCounterPermissionEntry) -> int:
        """ Add(self: PerformanceCounterPermissionEntryCollection, value: PerformanceCounterPermissionEntry) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: PerformanceCounterPermissionEntryCollection, value: Array[PerformanceCounterPermissionEntry])AddRange(self: PerformanceCounterPermissionEntryCollection, value: PerformanceCounterPermissionEntryCollection) """
        ...

    def Contains(self, value:PerformanceCounterPermissionEntry) -> bool:
        """ Contains(self: PerformanceCounterPermissionEntryCollection, value: PerformanceCounterPermissionEntry) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: PerformanceCounterPermissionEntryCollection, array: Array[PerformanceCounterPermissionEntry], index: int) """
        ...

    def IndexOf(self, value:PerformanceCounterPermissionEntry) -> int:
        """ IndexOf(self: PerformanceCounterPermissionEntryCollection, value: PerformanceCounterPermissionEntry) -> int """
        ...

    def Insert(self, index:int, value:PerformanceCounterPermissionEntry): # -> 
        """ Insert(self: PerformanceCounterPermissionEntryCollection, index: int, value: PerformanceCounterPermissionEntry) """
        ...

    def Remove(self, value:PerformanceCounterPermissionEntry): # -> 
        """ Remove(self: PerformanceCounterPermissionEntryCollection, value: PerformanceCounterPermissionEntry) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class PerformanceCounterType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PerformanceCounterType, values: AverageBase (1073939458), AverageCount64 (1073874176), AverageTimer32 (805438464), CounterDelta32 (4195328), CounterDelta64 (4195584), CounterMultiBase (1107494144), CounterMultiTimer (574686464), CounterMultiTimer100Ns (575735040), CounterMultiTimer100NsInverse (592512256), CounterMultiTimerInverse (591463680), CounterTimer (541132032), CounterTimerInverse (557909248), CountPerTimeInterval32 (4523008), CountPerTimeInterval64 (4523264), ElapsedTime (807666944), NumberOfItems32 (65536), NumberOfItems64 (65792), NumberOfItemsHEX32 (0), NumberOfItemsHEX64 (256), RateOfCountsPerSecond32 (272696320), RateOfCountsPerSecond64 (272696576), RawBase (1073939459), RawFraction (537003008), SampleBase (1073939457), SampleCounter (4260864), SampleFraction (549585920), Timer100Ns (542180608), Timer100NsInverse (558957824) """
    AverageBase: PerformanceCounterType = ...
    AverageCount64: PerformanceCounterType = ...
    AverageTimer32: PerformanceCounterType = ...
    CounterDelta32: PerformanceCounterType = ...
    CounterDelta64: PerformanceCounterType = ...
    CounterMultiBase: PerformanceCounterType = ...
    CounterMultiTimer: PerformanceCounterType = ...
    CounterMultiTimer100Ns: PerformanceCounterType = ...
    CounterMultiTimer100NsInverse: PerformanceCounterType = ...
    CounterMultiTimerInverse: PerformanceCounterType = ...
    CounterTimer: PerformanceCounterType = ...
    CounterTimerInverse: PerformanceCounterType = ...
    CountPerTimeInterval32: PerformanceCounterType = ...
    CountPerTimeInterval64: PerformanceCounterType = ...
    ElapsedTime: PerformanceCounterType = ...
    NumberOfItems32: PerformanceCounterType = ...
    NumberOfItems64: PerformanceCounterType = ...
    NumberOfItemsHEX32: PerformanceCounterType = ...
    NumberOfItemsHEX64: PerformanceCounterType = ...
    RateOfCountsPerSecond32: PerformanceCounterType = ...
    RateOfCountsPerSecond64: PerformanceCounterType = ...
    RawBase: PerformanceCounterType = ...
    RawFraction: PerformanceCounterType = ...
    SampleBase: PerformanceCounterType = ...
    SampleCounter: PerformanceCounterType = ...
    SampleFraction: PerformanceCounterType = ...
    Timer100Ns: PerformanceCounterType = ...
    Timer100NsInverse: PerformanceCounterType = ...
    value__ = ...


class Process(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ Process() """
    @property
    def BasePriority(self) -> int:
        """ Get: BasePriority(self: Process) -> int """
        ...

    @property
    def EnableRaisingEvents(self) -> bool:
        """
        Get: EnableRaisingEvents(self: Process) -> bool
        Set: EnableRaisingEvents(self: Process) = value
        """
        ...

    @property
    def ExitCode(self) -> int:
        """ Get: ExitCode(self: Process) -> int """
        ...

    @property
    def ExitTime(self) -> DateTime:
        """ Get: ExitTime(self: Process) -> DateTime """
        ...

    @property
    def Handle(self) -> IntPtr:
        """ Get: Handle(self: Process) -> IntPtr """
        ...

    @property
    def HandleCount(self) -> int:
        """ Get: HandleCount(self: Process) -> int """
        ...

    @property
    def HasExited(self) -> bool:
        """ Get: HasExited(self: Process) -> bool """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: Process) -> int """
        ...

    @property
    def MachineName(self) -> str:
        """ Get: MachineName(self: Process) -> str """
        ...

    @property
    def MainModule(self) -> ProcessModule:
        """ Get: MainModule(self: Process) -> ProcessModule """
        ...

    @property
    def MainWindowHandle(self) -> IntPtr:
        """ Get: MainWindowHandle(self: Process) -> IntPtr """
        ...

    @property
    def MainWindowTitle(self) -> str:
        """ Get: MainWindowTitle(self: Process) -> str """
        ...

    @property
    def MaxWorkingSet(self) -> IntPtr:
        """
        Get: MaxWorkingSet(self: Process) -> IntPtr
        Set: MaxWorkingSet(self: Process) = value
        """
        ...

    @property
    def MinWorkingSet(self) -> IntPtr:
        """
        Get: MinWorkingSet(self: Process) -> IntPtr
        Set: MinWorkingSet(self: Process) = value
        """
        ...

    @property
    def Modules(self) -> ProcessModuleCollection:
        """ Get: Modules(self: Process) -> ProcessModuleCollection """
        ...

    @property
    def NonpagedSystemMemorySize(self) -> int:
        """ Get: NonpagedSystemMemorySize(self: Process) -> int """
        ...

    @property
    def NonpagedSystemMemorySize64(self) -> Int64:
        """ Get: NonpagedSystemMemorySize64(self: Process) -> Int64 """
        ...

    @property
    def PagedMemorySize(self) -> int:
        """ Get: PagedMemorySize(self: Process) -> int """
        ...

    @property
    def PagedMemorySize64(self) -> Int64:
        """ Get: PagedMemorySize64(self: Process) -> Int64 """
        ...

    @property
    def PagedSystemMemorySize(self) -> int:
        """ Get: PagedSystemMemorySize(self: Process) -> int """
        ...

    @property
    def PagedSystemMemorySize64(self) -> Int64:
        """ Get: PagedSystemMemorySize64(self: Process) -> Int64 """
        ...

    @property
    def PeakPagedMemorySize(self) -> int:
        """ Get: PeakPagedMemorySize(self: Process) -> int """
        ...

    @property
    def PeakPagedMemorySize64(self) -> Int64:
        """ Get: PeakPagedMemorySize64(self: Process) -> Int64 """
        ...

    @property
    def PeakVirtualMemorySize(self) -> int:
        """ Get: PeakVirtualMemorySize(self: Process) -> int """
        ...

    @property
    def PeakVirtualMemorySize64(self) -> Int64:
        """ Get: PeakVirtualMemorySize64(self: Process) -> Int64 """
        ...

    @property
    def PeakWorkingSet(self) -> int:
        """ Get: PeakWorkingSet(self: Process) -> int """
        ...

    @property
    def PeakWorkingSet64(self) -> Int64:
        """ Get: PeakWorkingSet64(self: Process) -> Int64 """
        ...

    @property
    def PriorityBoostEnabled(self) -> bool:
        """
        Get: PriorityBoostEnabled(self: Process) -> bool
        Set: PriorityBoostEnabled(self: Process) = value
        """
        ...

    @property
    def PriorityClass(self) -> ProcessPriorityClass:
        """
        Get: PriorityClass(self: Process) -> ProcessPriorityClass
        Set: PriorityClass(self: Process) = value
        """
        ...

    @property
    def PrivateMemorySize(self) -> int:
        """ Get: PrivateMemorySize(self: Process) -> int """
        ...

    @property
    def PrivateMemorySize64(self) -> Int64:
        """ Get: PrivateMemorySize64(self: Process) -> Int64 """
        ...

    @property
    def PrivilegedProcessorTime(self) -> TimeSpan:
        """ Get: PrivilegedProcessorTime(self: Process) -> TimeSpan """
        ...

    @property
    def ProcessName(self) -> str:
        """ Get: ProcessName(self: Process) -> str """
        ...

    @property
    def ProcessorAffinity(self) -> IntPtr:
        """
        Get: ProcessorAffinity(self: Process) -> IntPtr
        Set: ProcessorAffinity(self: Process) = value
        """
        ...

    @property
    def Responding(self) -> bool:
        """ Get: Responding(self: Process) -> bool """
        ...

    @property
    def SafeHandle(self) -> SafeProcessHandle:
        """ Get: SafeHandle(self: Process) -> SafeProcessHandle """
        ...

    @property
    def SessionId(self) -> int:
        """ Get: SessionId(self: Process) -> int """
        ...

    @property
    def StandardError(self) -> StreamReader:
        """ Get: StandardError(self: Process) -> StreamReader """
        ...

    @property
    def StandardInput(self) -> StreamWriter:
        """ Get: StandardInput(self: Process) -> StreamWriter """
        ...

    @property
    def StandardOutput(self) -> StreamReader:
        """ Get: StandardOutput(self: Process) -> StreamReader """
        ...

    @property
    def StartInfo(self) -> ProcessStartInfo:
        """
        Get: StartInfo(self: Process) -> ProcessStartInfo
        Set: StartInfo(self: Process) = value
        """
        ...

    @property
    def StartTime(self) -> DateTime:
        """ Get: StartTime(self: Process) -> DateTime """
        ...

    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """
        Get: SynchronizingObject(self: Process) -> ISynchronizeInvoke
        Set: SynchronizingObject(self: Process) = value
        """
        ...

    @property
    def Threads(self) -> ProcessThreadCollection:
        """ Get: Threads(self: Process) -> ProcessThreadCollection """
        ...

    @property
    def TotalProcessorTime(self) -> TimeSpan:
        """ Get: TotalProcessorTime(self: Process) -> TimeSpan """
        ...

    @property
    def UserProcessorTime(self) -> TimeSpan:
        """ Get: UserProcessorTime(self: Process) -> TimeSpan """
        ...

    @property
    def VirtualMemorySize(self) -> int:
        """ Get: VirtualMemorySize(self: Process) -> int """
        ...

    @property
    def VirtualMemorySize64(self) -> Int64:
        """ Get: VirtualMemorySize64(self: Process) -> Int64 """
        ...

    @property
    def WorkingSet(self) -> int:
        """ Get: WorkingSet(self: Process) -> int """
        ...

    @property
    def WorkingSet64(self) -> Int64:
        """ Get: WorkingSet64(self: Process) -> Int64 """
        ...


    def BeginErrorReadLine(self): # -> 
        """ BeginErrorReadLine(self: Process) """
        ...

    def BeginOutputReadLine(self): # -> 
        """ BeginOutputReadLine(self: Process) """
        ...

    def CancelErrorRead(self): # -> 
        """ CancelErrorRead(self: Process) """
        ...

    def CancelOutputRead(self): # -> 
        """ CancelOutputRead(self: Process) """
        ...

    def Close(self): # -> 
        """ Close(self: Process) """
        ...

    def CloseMainWindow(self) -> bool:
        """ CloseMainWindow(self: Process) -> bool """
        ...

    @staticmethod
    def EnterDebugMode(): # -> 
        """ EnterDebugMode() """
        ...

    @staticmethod
    def GetCurrentProcess() -> Process:
        """ GetCurrentProcess() -> Process """
        ...

    @staticmethod
    def GetProcessById(processId:int, machineName:str = ...) -> Process:
        """
        GetProcessById(processId: int, machineName: str) -> Process
        GetProcessById(processId: int) -> Process
        """
        ...

    @staticmethod
    def GetProcesses(machineName=None) -> Array:
        """
        GetProcesses() -> Array[Process]
        GetProcesses(machineName: str) -> Array[Process]
        """
        ...

    @staticmethod
    def GetProcessesByName(processName:str, machineName:str = ...) -> Array:
        """
        GetProcessesByName(processName: str) -> Array[Process]
        GetProcessesByName(processName: str, machineName: str) -> Array[Process]
        """
        ...

    def Kill(self): # -> 
        """ Kill(self: Process) """
        ...

    @staticmethod
    def LeaveDebugMode(): # -> 
        """ LeaveDebugMode() """
        ...

    def OnExited(self, *args): #cannot find CLR method
        """ OnExited(self: Process) """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: Process) """
        ...

    @staticmethod
    def Start(*__args:str) -> Process:
        """
        Start(fileName: str, userName: str, password: SecureString, domain: str) -> Process
        Start(fileName: str, arguments: str, userName: str, password: SecureString, domain: str) -> Process
        Start(fileName: str) -> Process
        Start(fileName: str, arguments: str) -> Process
        Start(startInfo: ProcessStartInfo) -> Process
        Start(self: Process) -> bool
        """
        ...

    def WaitForExit(self, milliseconds:int = ...) -> bool:
        """
        WaitForExit(self: Process, milliseconds: int) -> bool
        WaitForExit(self: Process)
        """
        ...

    def WaitForInputIdle(self, milliseconds:int = ...) -> bool:
        """
        WaitForInputIdle(self: Process, milliseconds: int) -> bool
        WaitForInputIdle(self: Process) -> bool
        """
        ...

    ErrorDataReceived = ...
    Exited = ...
    OutputDataReceived = ...


class ProcessModule(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def BaseAddress(self) -> IntPtr:
        """ Get: BaseAddress(self: ProcessModule) -> IntPtr """
        ...

    @property
    def EntryPointAddress(self) -> IntPtr:
        """ Get: EntryPointAddress(self: ProcessModule) -> IntPtr """
        ...

    @property
    def FileName(self) -> str:
        """ Get: FileName(self: ProcessModule) -> str """
        ...

    @property
    def FileVersionInfo(self) -> FileVersionInfo:
        """ Get: FileVersionInfo(self: ProcessModule) -> FileVersionInfo """
        ...

    @property
    def ModuleMemorySize(self) -> int:
        """ Get: ModuleMemorySize(self: ProcessModule) -> int """
        ...

    @property
    def ModuleName(self) -> str:
        """ Get: ModuleName(self: ProcessModule) -> str """
        ...



class ProcessModuleCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ProcessModuleCollection(processModules: Array[ProcessModule]) """
    def Contains(self, module:ProcessModule) -> bool:
        """ Contains(self: ProcessModuleCollection, module: ProcessModule) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ProcessModuleCollection, array: Array[ProcessModule], index: int) """
        ...

    def IndexOf(self, module:ProcessModule) -> int:
        """ IndexOf(self: ProcessModuleCollection, module: ProcessModule) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, processModules:Array) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, processModules: Array[ProcessModule])
        """
        ...


class ProcessPriorityClass(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProcessPriorityClass, values: AboveNormal (32768), BelowNormal (16384), High (128), Idle (64), Normal (32), RealTime (256) """
    AboveNormal: ProcessPriorityClass = ...
    BelowNormal: ProcessPriorityClass = ...
    High: ProcessPriorityClass = ...
    Idle: ProcessPriorityClass = ...
    Normal: ProcessPriorityClass = ...
    RealTime: ProcessPriorityClass = ...
    value__ = ...


class ProcessStartInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    ProcessStartInfo()
    ProcessStartInfo(fileName: str)
    ProcessStartInfo(fileName: str, arguments: str)
    """
    @property
    def Arguments(self) -> str:
        """
        Get: Arguments(self: ProcessStartInfo) -> str
        Set: Arguments(self: ProcessStartInfo) = value
        """
        ...

    @property
    def CreateNoWindow(self) -> bool:
        """
        Get: CreateNoWindow(self: ProcessStartInfo) -> bool
        Set: CreateNoWindow(self: ProcessStartInfo) = value
        """
        ...

    @property
    def Domain(self) -> str:
        """
        Get: Domain(self: ProcessStartInfo) -> str
        Set: Domain(self: ProcessStartInfo) = value
        """
        ...

    @property
    def Environment(self) -> IDictionary:
        """ Get: Environment(self: ProcessStartInfo) -> IDictionary[str, str] """
        ...

    @property
    def EnvironmentVariables(self) -> StringDictionary:
        """ Get: EnvironmentVariables(self: ProcessStartInfo) -> StringDictionary """
        ...

    @property
    def ErrorDialog(self) -> bool:
        """
        Get: ErrorDialog(self: ProcessStartInfo) -> bool
        Set: ErrorDialog(self: ProcessStartInfo) = value
        """
        ...

    @property
    def ErrorDialogParentHandle(self) -> IntPtr:
        """
        Get: ErrorDialogParentHandle(self: ProcessStartInfo) -> IntPtr
        Set: ErrorDialogParentHandle(self: ProcessStartInfo) = value
        """
        ...

    @property
    def FileName(self) -> str:
        """
        Get: FileName(self: ProcessStartInfo) -> str
        Set: FileName(self: ProcessStartInfo) = value
        """
        ...

    @property
    def LoadUserProfile(self) -> bool:
        """
        Get: LoadUserProfile(self: ProcessStartInfo) -> bool
        Set: LoadUserProfile(self: ProcessStartInfo) = value
        """
        ...

    @property
    def Password(self) -> SecureString:
        """
        Get: Password(self: ProcessStartInfo) -> SecureString
        Set: Password(self: ProcessStartInfo) = value
        """
        ...

    @property
    def PasswordInClearText(self) -> str:
        """
        Get: PasswordInClearText(self: ProcessStartInfo) -> str
        Set: PasswordInClearText(self: ProcessStartInfo) = value
        """
        ...

    @property
    def RedirectStandardError(self) -> bool:
        """
        Get: RedirectStandardError(self: ProcessStartInfo) -> bool
        Set: RedirectStandardError(self: ProcessStartInfo) = value
        """
        ...

    @property
    def RedirectStandardInput(self) -> bool:
        """
        Get: RedirectStandardInput(self: ProcessStartInfo) -> bool
        Set: RedirectStandardInput(self: ProcessStartInfo) = value
        """
        ...

    @property
    def RedirectStandardOutput(self) -> bool:
        """
        Get: RedirectStandardOutput(self: ProcessStartInfo) -> bool
        Set: RedirectStandardOutput(self: ProcessStartInfo) = value
        """
        ...

    @property
    def StandardErrorEncoding(self) -> Encoding:
        """
        Get: StandardErrorEncoding(self: ProcessStartInfo) -> Encoding
        Set: StandardErrorEncoding(self: ProcessStartInfo) = value
        """
        ...

    @property
    def StandardOutputEncoding(self) -> Encoding:
        """
        Get: StandardOutputEncoding(self: ProcessStartInfo) -> Encoding
        Set: StandardOutputEncoding(self: ProcessStartInfo) = value
        """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: ProcessStartInfo) -> str
        Set: UserName(self: ProcessStartInfo) = value
        """
        ...

    @property
    def UseShellExecute(self) -> bool:
        """
        Get: UseShellExecute(self: ProcessStartInfo) -> bool
        Set: UseShellExecute(self: ProcessStartInfo) = value
        """
        ...

    @property
    def Verb(self) -> str:
        """
        Get: Verb(self: ProcessStartInfo) -> str
        Set: Verb(self: ProcessStartInfo) = value
        """
        ...

    @property
    def Verbs(self) -> Array:
        """ Get: Verbs(self: ProcessStartInfo) -> Array[str] """
        ...

    @property
    def WindowStyle(self) -> ProcessWindowStyle:
        """
        Get: WindowStyle(self: ProcessStartInfo) -> ProcessWindowStyle
        Set: WindowStyle(self: ProcessStartInfo) = value
        """
        ...

    @property
    def WorkingDirectory(self) -> str:
        """
        Get: WorkingDirectory(self: ProcessStartInfo) -> str
        Set: WorkingDirectory(self: ProcessStartInfo) = value
        """
        ...



class ProcessThread(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def BasePriority(self) -> int:
        """ Get: BasePriority(self: ProcessThread) -> int """
        ...

    @property
    def CurrentPriority(self) -> int:
        """ Get: CurrentPriority(self: ProcessThread) -> int """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: ProcessThread) -> int """
        ...

    @property
    def IdealProcessor(self): # -> 
        """ Set: IdealProcessor(self: ProcessThread) = value """
        ...

    @property
    def PriorityBoostEnabled(self) -> bool:
        """
        Get: PriorityBoostEnabled(self: ProcessThread) -> bool
        Set: PriorityBoostEnabled(self: ProcessThread) = value
        """
        ...

    @property
    def PriorityLevel(self) -> ThreadPriorityLevel:
        """
        Get: PriorityLevel(self: ProcessThread) -> ThreadPriorityLevel
        Set: PriorityLevel(self: ProcessThread) = value
        """
        ...

    @property
    def PrivilegedProcessorTime(self) -> TimeSpan:
        """ Get: PrivilegedProcessorTime(self: ProcessThread) -> TimeSpan """
        ...

    @property
    def ProcessorAffinity(self): # -> 
        """ Set: ProcessorAffinity(self: ProcessThread) = value """
        ...

    @property
    def StartAddress(self) -> IntPtr:
        """ Get: StartAddress(self: ProcessThread) -> IntPtr """
        ...

    @property
    def StartTime(self) -> DateTime:
        """ Get: StartTime(self: ProcessThread) -> DateTime """
        ...

    @property
    def ThreadState(self) -> ThreadState:
        """ Get: ThreadState(self: ProcessThread) -> ThreadState """
        ...

    @property
    def TotalProcessorTime(self) -> TimeSpan:
        """ Get: TotalProcessorTime(self: ProcessThread) -> TimeSpan """
        ...

    @property
    def UserProcessorTime(self) -> TimeSpan:
        """ Get: UserProcessorTime(self: ProcessThread) -> TimeSpan """
        ...

    @property
    def WaitReason(self) -> ThreadWaitReason:
        """ Get: WaitReason(self: ProcessThread) -> ThreadWaitReason """
        ...


    def ResetIdealProcessor(self): # -> 
        """ ResetIdealProcessor(self: ProcessThread) """
        ...


class ProcessThreadCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ProcessThreadCollection(processThreads: Array[ProcessThread]) """
    def Add(self, thread:ProcessThread) -> int:
        """ Add(self: ProcessThreadCollection, thread: ProcessThread) -> int """
        ...

    def Contains(self, thread:ProcessThread) -> bool:
        """ Contains(self: ProcessThreadCollection, thread: ProcessThread) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ProcessThreadCollection, array: Array[ProcessThread], index: int) """
        ...

    def IndexOf(self, thread:ProcessThread) -> int:
        """ IndexOf(self: ProcessThreadCollection, thread: ProcessThread) -> int """
        ...

    def Insert(self, index:int, thread:ProcessThread): # -> 
        """ Insert(self: ProcessThreadCollection, index: int, thread: ProcessThread) """
        ...

    def Remove(self, thread:ProcessThread): # -> 
        """ Remove(self: ProcessThreadCollection, thread: ProcessThread) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, processThreads:Array) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, processThreads: Array[ProcessThread])
        """
        ...


class ProcessWindowStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProcessWindowStyle, values: Hidden (1), Maximized (3), Minimized (2), Normal (0) """
    Hidden: ProcessWindowStyle = ...
    Maximized: ProcessWindowStyle = ...
    Minimized: ProcessWindowStyle = ...
    Normal: ProcessWindowStyle = ...
    value__ = ...


class SourceFilter(TraceFilter): # skipped bases: <type 'object'>
    """ SourceFilter(source: str) """
    @property
    def Source(self) -> str:
        """
        Get: Source(self: SourceFilter) -> str
        Set: Source(self: SourceFilter) = value
        """
        ...


    def __new__(cls, source:str) -> Self:
        """ __new__(cls: type, source: str) """
        ...


class SourceLevels(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SourceLevels, values: ActivityTracing (65280), All (-1), Critical (1), Error (3), Information (15), Off (0), Verbose (31), Warning (7) """
    ActivityTracing: SourceLevels = ...
    All: SourceLevels = ...
    Critical: SourceLevels = ...
    Error: SourceLevels = ...
    Information: SourceLevels = ...
    Off: SourceLevels = ...
    value__ = ...
    Verbose: SourceLevels = ...
    Warning: SourceLevels = ...


class SourceSwitch(Switch): # skipped bases: <type 'object'>
    """
    SourceSwitch(name: str)
    SourceSwitch(displayName: str, defaultSwitchValue: str)
    """
    @property
    def Level(self) -> SourceLevels:
        """
        Get: Level(self: SourceSwitch) -> SourceLevels
        Set: Level(self: SourceSwitch) = value
        """
        ...


    def ShouldTrace(self, eventType:TraceEventType) -> bool:
        """ ShouldTrace(self: SourceSwitch, eventType: TraceEventType) -> bool """
        ...


class StackFrame: # skipped bases: <type 'object'>, <type 'object'>
    """
    StackFrame()
    StackFrame(fNeedFileInfo: bool)
    StackFrame(skipFrames: int)
    StackFrame(skipFrames: int, fNeedFileInfo: bool)
    StackFrame(fileName: str, lineNumber: int)
    StackFrame(fileName: str, lineNumber: int, colNumber: int)
    """
    def GetFileColumnNumber(self) -> int:
        """ GetFileColumnNumber(self: StackFrame) -> int """
        ...

    def GetFileLineNumber(self) -> int:
        """ GetFileLineNumber(self: StackFrame) -> int """
        ...

    def GetFileName(self) -> str:
        """ GetFileName(self: StackFrame) -> str """
        ...

    def GetILOffset(self) -> int:
        """ GetILOffset(self: StackFrame) -> int """
        ...

    def GetMethod(self) -> MethodBase:
        """ GetMethod(self: StackFrame) -> MethodBase """
        ...

    def GetNativeOffset(self) -> int:
        """ GetNativeOffset(self: StackFrame) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: StackFrame) -> str """
        ...

    OFFSET_UNKNOWN: int = ...


class StackFrameExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetNativeImageBase(stackFrame:StackFrame) -> IntPtr:
        """ GetNativeImageBase(stackFrame: StackFrame) -> IntPtr """
        ...

    @staticmethod
    def GetNativeIP(stackFrame:StackFrame) -> IntPtr:
        """ GetNativeIP(stackFrame: StackFrame) -> IntPtr """
        ...

    @staticmethod
    def HasILOffset(stackFrame:StackFrame) -> bool:
        """ HasILOffset(stackFrame: StackFrame) -> bool """
        ...

    @staticmethod
    def HasMethod(stackFrame:StackFrame) -> bool:
        """ HasMethod(stackFrame: StackFrame) -> bool """
        ...

    @staticmethod
    def HasNativeImage(stackFrame:StackFrame) -> bool:
        """ HasNativeImage(stackFrame: StackFrame) -> bool """
        ...

    @staticmethod
    def HasSource(stackFrame:StackFrame) -> bool:
        """ HasSource(stackFrame: StackFrame) -> bool """
        ...

    __all__: list = ...


class StackTrace: # skipped bases: <type 'object'>, <type 'object'>
    """
    StackTrace()
    StackTrace(fNeedFileInfo: bool)
    StackTrace(skipFrames: int)
    StackTrace(skipFrames: int, fNeedFileInfo: bool)
    StackTrace(e: Exception)
    StackTrace(e: Exception, fNeedFileInfo: bool)
    StackTrace(e: Exception, skipFrames: int)
    StackTrace(e: Exception, skipFrames: int, fNeedFileInfo: bool)
    StackTrace(frame: StackFrame)
    StackTrace(targetThread: Thread, needFileInfo: bool)
    """
    @property
    def FrameCount(self) -> int:
        """ Get: FrameCount(self: StackTrace) -> int """
        ...


    def GetFrame(self, index:int) -> StackFrame:
        """ GetFrame(self: StackTrace, index: int) -> StackFrame """
        ...

    def GetFrames(self) -> Array:
        """ GetFrames(self: StackTrace) -> Array[StackFrame] """
        ...

    def ToString(self) -> str:
        """ ToString(self: StackTrace) -> str """
        ...

    METHODS_TO_SKIP: int = ...


class Stopwatch: # skipped bases: <type 'object'>, <type 'object'>
    """ Stopwatch() """
    @property
    def Elapsed(self) -> TimeSpan:
        """ Get: Elapsed(self: Stopwatch) -> TimeSpan """
        ...

    @property
    def ElapsedMilliseconds(self) -> Int64:
        """ Get: ElapsedMilliseconds(self: Stopwatch) -> Int64 """
        ...

    @property
    def ElapsedTicks(self) -> Int64:
        """ Get: ElapsedTicks(self: Stopwatch) -> Int64 """
        ...

    @property
    def IsRunning(self) -> bool:
        """ Get: IsRunning(self: Stopwatch) -> bool """
        ...


    @staticmethod
    def GetTimestamp() -> Int64:
        """ GetTimestamp() -> Int64 """
        ...

    def Reset(self): # -> 
        """ Reset(self: Stopwatch) """
        ...

    def Restart(self): # -> 
        """ Restart(self: Stopwatch) """
        ...

    def Start(self): # -> 
        """ Start(self: Stopwatch) """
        ...

    @staticmethod
    def StartNew() -> Stopwatch:
        """ StartNew() -> Stopwatch """
        ...

    def Stop(self): # -> 
        """ Stop(self: Stopwatch) """
        ...

    Frequency: Int64 = ...
    IsHighResolution: bool = ...


class SwitchAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SwitchAttribute(switchName: str, switchType: Type) """
    @property
    def SwitchDescription(self) -> str:
        """
        Get: SwitchDescription(self: SwitchAttribute) -> str
        Set: SwitchDescription(self: SwitchAttribute) = value
        """
        ...

    @property
    def SwitchName(self) -> str:
        """
        Get: SwitchName(self: SwitchAttribute) -> str
        Set: SwitchName(self: SwitchAttribute) = value
        """
        ...

    @property
    def SwitchType(self) -> Type:
        """
        Get: SwitchType(self: SwitchAttribute) -> Type
        Set: SwitchType(self: SwitchAttribute) = value
        """
        ...


    @staticmethod
    def GetAll(assembly:Assembly) -> Array:
        """ GetAll(assembly: Assembly) -> Array[SwitchAttribute] """
        ...

    def __new__(cls, switchName:str, switchType:Type) -> Self:
        """ __new__(cls: type, switchName: str, switchType: Type) """
        ...


class SwitchLevelAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SwitchLevelAttribute(switchLevelType: Type) """
    @property
    def SwitchLevelType(self) -> Type:
        """
        Get: SwitchLevelType(self: SwitchLevelAttribute) -> Type
        Set: SwitchLevelType(self: SwitchLevelAttribute) = value
        """
        ...


    def __new__(cls, switchLevelType:Type) -> Self:
        """ __new__(cls: type, switchLevelType: Type) """
        ...


class ThreadPriorityLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ThreadPriorityLevel, values: AboveNormal (1), BelowNormal (-1), Highest (2), Idle (-15), Lowest (-2), Normal (0), TimeCritical (15) """
    AboveNormal: ThreadPriorityLevel = ...
    BelowNormal: ThreadPriorityLevel = ...
    Highest: ThreadPriorityLevel = ...
    Idle: ThreadPriorityLevel = ...
    Lowest: ThreadPriorityLevel = ...
    Normal: ThreadPriorityLevel = ...
    TimeCritical: ThreadPriorityLevel = ...
    value__ = ...


class ThreadState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ThreadState, values: Initialized (0), Ready (1), Running (2), Standby (3), Terminated (4), Transition (6), Unknown (7), Wait (5) """
    Initialized: ThreadState = ...
    Ready: ThreadState = ...
    Running: ThreadState = ...
    Standby: ThreadState = ...
    Terminated: ThreadState = ...
    Transition: ThreadState = ...
    Unknown: ThreadState = ...
    value__ = ...
    Wait: ThreadState = ...


class ThreadWaitReason(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ThreadWaitReason, values: EventPairHigh (7), EventPairLow (8), ExecutionDelay (4), Executive (0), FreePage (1), LpcReceive (9), LpcReply (10), PageIn (2), PageOut (12), Suspended (5), SystemAllocation (3), Unknown (13), UserRequest (6), VirtualMemory (11) """
    EventPairHigh: ThreadWaitReason = ...
    EventPairLow: ThreadWaitReason = ...
    ExecutionDelay: ThreadWaitReason = ...
    Executive: ThreadWaitReason = ...
    FreePage: ThreadWaitReason = ...
    LpcReceive: ThreadWaitReason = ...
    LpcReply: ThreadWaitReason = ...
    PageIn: ThreadWaitReason = ...
    PageOut: ThreadWaitReason = ...
    Suspended: ThreadWaitReason = ...
    SystemAllocation: ThreadWaitReason = ...
    Unknown: ThreadWaitReason = ...
    UserRequest: ThreadWaitReason = ...
    value__ = ...
    VirtualMemory: ThreadWaitReason = ...


class Trace: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AutoFlush(self) -> bool:
        """
        Get: AutoFlush() -> bool
        Set: AutoFlush() = value
        """
        ...

    @property
    def CorrelationManager(self) -> CorrelationManager:
        """ Get: CorrelationManager() -> CorrelationManager """
        ...

    @property
    def IndentLevel(self) -> int:
        """
        Get: IndentLevel() -> int
        Set: IndentLevel() = value
        """
        ...

    @property
    def IndentSize(self) -> int:
        """
        Get: IndentSize() -> int
        Set: IndentSize() = value
        """
        ...

    @property
    def Listeners(self) -> TraceListenerCollection:
        """ Get: Listeners() -> TraceListenerCollection """
        ...

    @property
    def UseGlobalLock(self) -> bool:
        """
        Get: UseGlobalLock() -> bool
        Set: UseGlobalLock() = value
        """
        ...


    @staticmethod
    def Assert(condition:bool, message:str = ..., detailMessage:str = ...): # -> 
        """ Assert(condition: bool)Assert(condition: bool, message: str)Assert(condition: bool, message: str, detailMessage: str) """
        ...

    @staticmethod
    def Close(): # -> 
        """ Close() """
        ...

    @staticmethod
    def Fail(message:str, detailMessage:str = ...): # -> 
        """ Fail(message: str)Fail(message: str, detailMessage: str) """
        ...

    @staticmethod
    def Flush(): # -> 
        """ Flush() """
        ...

    @staticmethod
    def Indent(): # -> 
        """ Indent() """
        ...

    @staticmethod
    def Refresh(): # -> 
        """ Refresh() """
        ...

    @staticmethod
    def TraceError(*__args:str): # -> 
        """ TraceError(message: str)TraceError(format: str, *args: Array[object]) """
        ...

    @staticmethod
    def TraceInformation(*__args:str): # -> 
        """ TraceInformation(message: str)TraceInformation(format: str, *args: Array[object]) """
        ...

    @staticmethod
    def TraceWarning(*__args:str): # -> 
        """ TraceWarning(message: str)TraceWarning(format: str, *args: Array[object]) """
        ...

    @staticmethod
    def Unindent(): # -> 
        """ Unindent() """
        ...

    @staticmethod
    def Write(*__args:str): # -> 
        """ Write(message: str)Write(value: object)Write(message: str, category: str)Write(value: object, category: str) """
        ...

    @staticmethod
    def WriteIf(condition:bool, *__args:str): # -> 
        """ WriteIf(condition: bool, message: str)WriteIf(condition: bool, value: object)WriteIf(condition: bool, message: str, category: str)WriteIf(condition: bool, value: object, category: str) """
        ...

    @staticmethod
    def WriteLine(*__args:str): # -> 
        """ WriteLine(message: str)WriteLine(value: object)WriteLine(message: str, category: str)WriteLine(value: object, category: str) """
        ...

    @staticmethod
    def WriteLineIf(condition:bool, *__args:str): # -> 
        """ WriteLineIf(condition: bool, message: str)WriteLineIf(condition: bool, value: object)WriteLineIf(condition: bool, message: str, category: str)WriteLineIf(condition: bool, value: object, category: str) """
        ...



class TraceEventCache: # skipped bases: <type 'object'>, <type 'object'>
    """ TraceEventCache() """
    @property
    def Callstack(self) -> str:
        """ Get: Callstack(self: TraceEventCache) -> str """
        ...

    @property
    def DateTime(self) -> DateTime:
        """ Get: DateTime(self: TraceEventCache) -> DateTime """
        ...

    @property
    def LogicalOperationStack(self) -> Stack:
        """ Get: LogicalOperationStack(self: TraceEventCache) -> Stack """
        ...

    @property
    def ProcessId(self) -> int:
        """ Get: ProcessId(self: TraceEventCache) -> int """
        ...

    @property
    def ThreadId(self) -> str:
        """ Get: ThreadId(self: TraceEventCache) -> str """
        ...

    @property
    def Timestamp(self) -> Int64:
        """ Get: Timestamp(self: TraceEventCache) -> Int64 """
        ...



class TraceEventType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TraceEventType, values: Critical (1), Error (2), Information (8), Resume (2048), Start (256), Stop (512), Suspend (1024), Transfer (4096), Verbose (16), Warning (4) """
    Critical: TraceEventType = ...
    Error: TraceEventType = ...
    Information: TraceEventType = ...
    Resume: TraceEventType = ...
    Start: TraceEventType = ...
    Stop: TraceEventType = ...
    Suspend: TraceEventType = ...
    Transfer: TraceEventType = ...
    value__ = ...
    Verbose: TraceEventType = ...
    Warning: TraceEventType = ...


class TraceLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TraceLevel, values: Error (1), Info (3), Off (0), Verbose (4), Warning (2) """
    Error: TraceLevel = ...
    Info: TraceLevel = ...
    Off: TraceLevel = ...
    value__ = ...
    Verbose: TraceLevel = ...
    Warning: TraceLevel = ...


class TraceListenerCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: TraceListenerCollection) -> int """
        ...


    def AddRange(self, value:Array): # -> 
        """ AddRange(self: TraceListenerCollection, value: Array[TraceListener])AddRange(self: TraceListenerCollection, value: TraceListenerCollection) """
        ...

    def CopyTo(self, listeners:Array, index:int): # -> 
        """ CopyTo(self: TraceListenerCollection, listeners: Array[TraceListener], index: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: TraceListenerCollection) -> IEnumerator """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class TraceLogRetentionOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TraceLogRetentionOption, values: LimitedCircularFiles (1), LimitedSequentialFiles (3), SingleFileBoundedSize (4), SingleFileUnboundedSize (2), UnlimitedSequentialFiles (0) """
    LimitedCircularFiles: TraceLogRetentionOption = ...
    LimitedSequentialFiles: TraceLogRetentionOption = ...
    SingleFileBoundedSize: TraceLogRetentionOption = ...
    SingleFileUnboundedSize: TraceLogRetentionOption = ...
    UnlimitedSequentialFiles: TraceLogRetentionOption = ...
    value__ = ...


class TraceOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TraceOptions, values: Callstack (32), DateTime (2), LogicalOperationStack (1), None (0), ProcessId (8), ThreadId (16), Timestamp (4) """
    Callstack: TraceOptions = ...
    DateTime: TraceOptions = ...
    LogicalOperationStack: TraceOptions = ...
    ProcessId: TraceOptions = ...
    ThreadId: TraceOptions = ...
    Timestamp: TraceOptions = ...
    value__ = ...


class TraceSource: # skipped bases: <type 'object'>, <type 'object'>
    """
    TraceSource(name: str)
    TraceSource(name: str, defaultLevel: SourceLevels)
    """
    @property
    def Attributes(self) -> StringDictionary:
        """ Get: Attributes(self: TraceSource) -> StringDictionary """
        ...

    @property
    def Listeners(self) -> TraceListenerCollection:
        """ Get: Listeners(self: TraceSource) -> TraceListenerCollection """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: TraceSource) -> str """
        ...

    @property
    def Switch(self) -> SourceSwitch:
        """
        Get: Switch(self: TraceSource) -> SourceSwitch
        Set: Switch(self: TraceSource) = value
        """
        ...


    def Close(self): # -> 
        """ Close(self: TraceSource) """
        ...

    def Flush(self): # -> 
        """ Flush(self: TraceSource) """
        ...

    def GetSupportedAttributes(self, *args): #cannot find CLR method
        """ GetSupportedAttributes(self: TraceSource) -> Array[str] """
        ...

    def TraceData(self, eventType:TraceEventType, id:int, data:object): # -> 
        """ TraceData(self: TraceSource, eventType: TraceEventType, id: int, data: object)TraceData(self: TraceSource, eventType: TraceEventType, id: int, *data: Array[object]) """
        ...

    def TraceEvent(self, eventType:TraceEventType, id:int, *__args:str): # -> 
        """ TraceEvent(self: TraceSource, eventType: TraceEventType, id: int)TraceEvent(self: TraceSource, eventType: TraceEventType, id: int, message: str)TraceEvent(self: TraceSource, eventType: TraceEventType, id: int, format: str, *args: Array[object]) """
        ...

    def TraceInformation(self, *__args:str): # -> 
        """ TraceInformation(self: TraceSource, message: str)TraceInformation(self: TraceSource, format: str, *args: Array[object]) """
        ...

    def TraceTransfer(self, id:int, message:str, relatedActivityId:Guid): # -> 
        """ TraceTransfer(self: TraceSource, id: int, message: str, relatedActivityId: Guid) """
        ...


class TraceSwitch(Switch): # skipped bases: <type 'object'>
    """
    TraceSwitch(displayName: str, description: str)
    TraceSwitch(displayName: str, description: str, defaultSwitchValue: str)
    """
    @property
    def Level(self) -> TraceLevel:
        """
        Get: Level(self: TraceSwitch) -> TraceLevel
        Set: Level(self: TraceSwitch) = value
        """
        ...

    @property
    def TraceError(self) -> bool:
        """ Get: TraceError(self: TraceSwitch) -> bool """
        ...

    @property
    def TraceInfo(self) -> bool:
        """ Get: TraceInfo(self: TraceSwitch) -> bool """
        ...

    @property
    def TraceVerbose(self) -> bool:
        """ Get: TraceVerbose(self: TraceSwitch) -> bool """
        ...

    @property
    def TraceWarning(self) -> bool:
        """ Get: TraceWarning(self: TraceSwitch) -> bool """
        ...



class UnescapedXmlDiagnosticData: # skipped bases: <type 'object'>, <type 'object'>
    """ UnescapedXmlDiagnosticData(xmlPayload: str) """
    @property
    def UnescapedXml(self) -> str:
        """
        Get: UnescapedXml(self: UnescapedXmlDiagnosticData) -> str
        Set: UnescapedXml(self: UnescapedXmlDiagnosticData) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: UnescapedXmlDiagnosticData) -> str """
        ...


class XmlWriterTraceListener(TextWriterTraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    XmlWriterTraceListener(stream: Stream)
    XmlWriterTraceListener(stream: Stream, name: str)
    XmlWriterTraceListener(writer: TextWriter)
    XmlWriterTraceListener(writer: TextWriter, name: str)
    XmlWriterTraceListener(filename: str)
    XmlWriterTraceListener(filename: str, name: str)
    """
    def Fail(self, message:str, detailMessage:str = ...): # -> 
        """ Fail(self: XmlWriterTraceListener, message: str, detailMessage: str) """
        ...

    def TraceData(self, eventCache:TraceEventCache, source:str, eventType:TraceEventType, id:int, data:object): # -> 
        """ TraceData(self: XmlWriterTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, data: object)TraceData(self: XmlWriterTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, *data: Array[object]) """
        ...

    def TraceEvent(self, eventCache:TraceEventCache, source:str, eventType:TraceEventType, id:int, *__args:str): # -> 
        """ TraceEvent(self: XmlWriterTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, format: str, *args: Array[object])TraceEvent(self: XmlWriterTraceListener, eventCache: TraceEventCache, source: str, eventType: TraceEventType, id: int, message: str) """
        ...

    def TraceTransfer(self, eventCache:TraceEventCache, source:str, id:int, message:str, relatedActivityId:Guid): # -> 
        """ TraceTransfer(self: XmlWriterTraceListener, eventCache: TraceEventCache, source: str, id: int, message: str, relatedActivityId: Guid) """
        ...


# variables with complex values

