# encoding: utf-8
# module Microsoft.Scripting.Debugging calls itself Debugging
# from Microsoft.Dynamic, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Scripting import SourceSpan

from Microsoft.Scripting.Debugging.CompilerServices import DebugContext

from System import Array, Delegate, Enum

from System.Collections import IEnumerator

from System.Runtime.CompilerServices import IRuntimeVariables

"""The following names are not found in the module: (BoundEvent, Func, 
    IDebugCallback, field#)
"""

# no functions
# classes

class DebugFrame: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class DebugSourceFile: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Mode(self) -> int:
        """ Get: Mode(self: DebugSourceFile) -> int """
        ...



class DebugThread: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class ForceToGeneratorLoopException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ ForceToGeneratorLoopException() """
    SerializeObjectState = ...


class FunctionInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class ITraceCallback: # skipped bases: <type 'object'>
    """ no doc """
    def OnTraceEvent(self, kind:TraceEventKind, name:str, sourceFileName:str, sourceSpan:SourceSpan, scopeCallback, payload:object, customPayload:object): # ->  # Not found arg types: {'scopeCallback': 'Func'}
        """ OnTraceEvent(self: ITraceCallback, kind: TraceEventKind, name: str, sourceFileName: str, sourceSpan: SourceSpan, scopeCallback: Func[dict], payload: object, customPayload: object) """
        ...


class ITracePipeline: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def TraceCallback(self) -> ITraceCallback:
        """
        Get: TraceCallback(self: ITracePipeline) -> ITraceCallback
        Set: TraceCallback(self: ITracePipeline) = value
        """
        ...


    def Close(self): # -> 
        """ Close(self: ITracePipeline) """
        ...

    def TrySetNextStatement(self, sourceFile:str, sourceSpan:SourceSpan) -> bool:
        """ TrySetNextStatement(self: ITracePipeline, sourceFile: str, sourceSpan: SourceSpan) -> bool """
        ...


class RuntimeOps: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateDebugGenerator(frame:DebugFrame) -> IEnumerator:
        """ CreateDebugGenerator[T](frame: DebugFrame) -> IEnumerator[T] """
        ...

    @staticmethod
    def CreateFrameForGenerator(debugContext:DebugContext, func:FunctionInfo) -> DebugFrame:
        """ CreateFrameForGenerator(debugContext: DebugContext, func: FunctionInfo) -> DebugFrame """
        ...

    @staticmethod
    def CreateFunctionInfo(generatorFactory:Delegate, name:str, locationSpanMap:object, scopedVariables:object, variables:object, customPayload:object) -> FunctionInfo:
        """ CreateFunctionInfo(generatorFactory: Delegate, name: str, locationSpanMap: object, scopedVariables: object, variables: object, customPayload: object) -> FunctionInfo """
        ...

    @staticmethod
    def GeneratorLoopProc(thread:DebugThread) -> object:
        """ GeneratorLoopProc(thread: DebugThread) -> object """
        ...

    @staticmethod
    def GetCurrentSequencePointForGeneratorFrame(frame:DebugFrame) -> int:
        """ GetCurrentSequencePointForGeneratorFrame(frame: DebugFrame) -> int """
        ...

    @staticmethod
    def GetCurrentSequencePointForLeafGeneratorFrame(thread:DebugThread) -> int:
        """ GetCurrentSequencePointForLeafGeneratorFrame(thread: DebugThread) -> int """
        ...

    @staticmethod
    def GetCurrentThread(debugContext:DebugContext) -> DebugThread:
        """ GetCurrentThread(debugContext: DebugContext) -> DebugThread """
        ...

    @staticmethod
    def GetThread(frame:DebugFrame) -> DebugThread:
        """ GetThread(frame: DebugFrame) -> DebugThread """
        ...

    @staticmethod
    def GetTraceLocations(functionInfo:FunctionInfo) -> Array:
        """ GetTraceLocations(functionInfo: FunctionInfo) -> Array[bool] """
        ...

    @staticmethod
    def IsCurrentLeafFrameRemappingToGenerator(thread:DebugThread) -> bool:
        """ IsCurrentLeafFrameRemappingToGenerator(thread: DebugThread) -> bool """
        ...

    @staticmethod
    def LiftVariables(thread:DebugThread, runtimeVariables:IRuntimeVariables): # -> 
        """ LiftVariables(thread: DebugThread, runtimeVariables: IRuntimeVariables) """
        ...

    @staticmethod
    def OnFrameEnterTraceEvent(thread:DebugThread): # -> 
        """ OnFrameEnterTraceEvent(thread: DebugThread) """
        ...

    @staticmethod
    def OnFrameExitTraceEvent(thread:DebugThread, debugMarker:int, retVal:object): # -> 
        """ OnFrameExitTraceEvent(thread: DebugThread, debugMarker: int, retVal: object) """
        ...

    @staticmethod
    def OnThreadExitEvent(thread:DebugThread): # -> 
        """ OnThreadExitEvent(thread: DebugThread) """
        ...

    @staticmethod
    def OnTraceEvent(thread:DebugThread, debugMarker:int, exception:Exception): # -> 
        """ OnTraceEvent(thread: DebugThread, debugMarker: int, exception: Exception) """
        ...

    @staticmethod
    def OnTraceEventUnwind(thread:DebugThread, debugMarker:int, exception:Exception): # -> 
        """ OnTraceEventUnwind(thread: DebugThread, debugMarker: int, exception: Exception) """
        ...

    @staticmethod
    def PopFrame(thread:DebugThread) -> bool:
        """ PopFrame(thread: DebugThread) -> bool """
        ...

    @staticmethod
    def ReplaceLiftedLocals(frame:DebugFrame, liftedLocals:IRuntimeVariables): # -> 
        """ ReplaceLiftedLocals(frame: DebugFrame, liftedLocals: IRuntimeVariables) """
        ...

    __all__: list = ...


class TraceEventKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TraceEventKind, values: Exception (4), ExceptionUnwind (5), FrameEnter (0), FrameExit (1), ThreadExit (2), TracePoint (3) """
    Exception: TraceEventKind = ...
    ExceptionUnwind: TraceEventKind = ...
    FrameEnter: TraceEventKind = ...
    FrameExit: TraceEventKind = ...
    ThreadExit: TraceEventKind = ...
    TracePoint: TraceEventKind = ...
    value__ = ...


class TracePipeline(ITracePipeline, IDebugCallback): # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def CreateInstance(debugContext:DebugContext) -> TracePipeline:
        """ CreateInstance(debugContext: DebugContext) -> TracePipeline """
        ...


# variables with complex values

