# encoding: utf-8
# module Microsoft.DataWarehouse.Interfaces.Debugger calls itself Debugger
# from Microsoft.DataWarehouse.Interfaces, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Enum, EventArgs, Guid, IAsyncResult, 
    MulticastDelegate)

from System.Collections import Hashtable, IDictionary, IEnumerable

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class BreakpointHitCountType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BreakpointHitCountType, values: HitCountEqual (2), HitCountGreaterOrEqual (3), HitCountMultiple (4), HitCountNone (1) """
    HitCountEqual: BreakpointHitCountType = ...
    HitCountGreaterOrEqual: BreakpointHitCountType = ...
    HitCountMultiple: BreakpointHitCountType = ...
    HitCountNone: BreakpointHitCountType = ...
    value__ = ...


class BreakpointInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ BreakpointInfo() """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: BreakpointInfo) -> bool
        Set: Enabled(self: BreakpointInfo) = value
        """
        ...

    @property
    def File(self) -> str:
        """
        Get: File(self: BreakpointInfo) -> str
        Set: File(self: BreakpointInfo) = value
        """
        ...

    @property
    def FileColumn(self) -> int:
        """
        Get: FileColumn(self: BreakpointInfo) -> int
        Set: FileColumn(self: BreakpointInfo) = value
        """
        ...

    @property
    def FileLine(self) -> int:
        """
        Get: FileLine(self: BreakpointInfo) -> int
        Set: FileLine(self: BreakpointInfo) = value
        """
        ...

    @property
    def FunctionName(self) -> str:
        """
        Get: FunctionName(self: BreakpointInfo) -> str
        Set: FunctionName(self: BreakpointInfo) = value
        """
        ...

    @property
    def HitCountTarget(self) -> int:
        """
        Get: HitCountTarget(self: BreakpointInfo) -> int
        Set: HitCountTarget(self: BreakpointInfo) = value
        """
        ...

    @property
    def HitCountType(self) -> BreakpointHitCountType:
        """
        Get: HitCountType(self: BreakpointInfo) -> BreakpointHitCountType
        Set: HitCountType(self: BreakpointInfo) = value
        """
        ...

    @property
    def Language(self) -> str:
        """
        Get: Language(self: BreakpointInfo) -> str
        Set: Language(self: BreakpointInfo) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: BreakpointInfo) -> str
        Set: Name(self: BreakpointInfo) = value
        """
        ...


    def Equals(self, other:object) -> bool:
        """ Equals(self: BreakpointInfo, other: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: BreakpointInfo) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DataWarehouseLanguages: # skipped bases: <type 'object'>, <type 'object'>
    """ DataWarehouseLanguages() """
    CubeCalculationsGuid: Guid = ...
    DtsPackageGuid: Guid = ...


class DebuggingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ DebuggingEventArgs() """
    pass

class DebugBreakpointsSetChangedEventArgs(DebuggingEventArgs): # skipped bases: <type 'object'>
    """ DebugBreakpointsSetChangedEventArgs() """
    pass

class DebugExecutionEventArgs(DebuggingEventArgs): # skipped bases: <type 'object'>
    """ DebugExecutionEventArgs(eventName: str) """
    @property
    def EventName(self) -> str:
        """ Get: EventName(self: DebugExecutionEventArgs) -> str """
        ...

    @property
    def Properties(self) -> Hashtable:
        """ Get: Properties(self: DebugExecutionEventArgs) -> Hashtable """
        ...


    def __new__(cls, eventName:str) -> Self:
        """ __new__(cls: type, eventName: str) """
        ...


class DebuggerMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DebuggerMode, values: Break (2), Design (1), Run (0) """
    Break: DebuggerMode = ...
    Design: DebuggerMode = ...
    Run: DebuggerMode = ...
    value__ = ...


class DebuggingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DebuggingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DebuggingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DebuggingEventHandler, sender: object, e: DebuggingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DebuggingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DebuggingEventArgs): # -> 
        """ Invoke(self: DebuggingEventHandler, sender: object, e: DebuggingEventArgs) """
        ...


class DebugSessionEndEventArgs(DebuggingEventArgs): # skipped bases: <type 'object'>
    """ DebugSessionEndEventArgs() """
    pass

class DebugSessionStartEventArgs(DebuggingEventArgs): # skipped bases: <type 'object'>
    """ DebugSessionStartEventArgs() """
    pass

class IDesignerDebuggingService: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Debuggee(self) -> object:
        """ Get: Debuggee(self: IDesignerDebuggingService) -> object """
        ...

    @property
    def IsDebugPackageInstalled(self) -> bool:
        """ Get: IsDebugPackageInstalled(self: IDesignerDebuggingService) -> bool """
        ...

    @property
    def Mode(self) -> DebuggerMode:
        """ Get: Mode(self: IDesignerDebuggingService) -> DebuggerMode """
        ...


    def GetBreakpointInfo(self, languageGuid:Guid, location:str) -> BreakpointInfo:
        """ GetBreakpointInfo(self: IDesignerDebuggingService, languageGuid: Guid, location: str) -> BreakpointInfo """
        ...

    def GetBreakpoints(self, languageGuid:Guid) -> IEnumerable:
        """ GetBreakpoints(self: IDesignerDebuggingService, languageGuid: Guid) -> IEnumerable """
        ...

    def GetRunningPrograms(self) -> Array:
        """ GetRunningPrograms(self: IDesignerDebuggingService) -> Array[ProgramInfo] """
        ...

    def RemoveBreakpoint(self, languageGuid:Guid, location:str): # -> 
        """ RemoveBreakpoint(self: IDesignerDebuggingService, languageGuid: Guid, location: str) """
        ...

    def SetBreakpoint(self, languageGuid:Guid, location:str, info:BreakpointInfo): # -> 
        """ SetBreakpoint(self: IDesignerDebuggingService, languageGuid: Guid, location: str, info: BreakpointInfo) """
        ...

    DebugEvent = ...


class IDesignerDebugSession: # skipped bases: <type 'object'>
    """ no doc """
    def ExecuteCommand(self, args:IDictionary): # -> 
        """ ExecuteCommand(self: IDesignerDebugSession, args: IDictionary) """
        ...


class ProgramInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ ProgramInfo(engine: Guid, processId: Guid, process: str, machine: str) """
    @property
    def Engine(self) -> Guid:
        """ Get: Engine(self: ProgramInfo) -> Guid """
        ...

    @property
    def Machine(self) -> str:
        """ Get: Machine(self: ProgramInfo) -> str """
        ...

    @property
    def Process(self) -> str:
        """ Get: Process(self: ProgramInfo) -> str """
        ...


    def Equals(self, other:object) -> bool:
        """ Equals(self: ProgramInfo, other: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ProgramInfo) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ShellDebugModeChangeEventArgs(DebuggingEventArgs): # skipped bases: <type 'object'>
    """ ShellDebugModeChangeEventArgs(debugMode: DebuggerMode) """
    @property
    def DebuggerMode(self) -> DebuggerMode:
        """ Get: DebuggerMode(self: ShellDebugModeChangeEventArgs) -> DebuggerMode """
        ...


    def __new__(cls, debugMode:DebuggerMode) -> Self:
        """ __new__(cls: type, debugMode: DebuggerMode) """
        ...


