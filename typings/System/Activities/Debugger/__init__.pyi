# encoding: utf-8
# module System.Activities.Debugger calls itself Debugger
# from System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import EventArgs, IDisposable, Type

from System.Activities.Debugger.Symbol import WorkflowSymbol

from System.Collections import ICollection, IDictionary

from System.Collections.Generic import Dictionary

from System.EnterpriseServices import Activity

from System.IO import TextReader

from System.Xaml import (AttachableMemberIdentifier, IXamlLineInfo, 
    XamlReader)

from typing import Self

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class DebugInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class IDebuggableWorkflowTree: # skipped bases: <type 'object'>
    """ no doc """
    def GetWorkflowRoot(self) -> Activity:
        """ GetWorkflowRoot(self: IDebuggableWorkflowTree) -> Activity """
        ...


class LocalsItemDescription: # skipped bases: <type 'object'>, <type 'object'>
    """ LocalsItemDescription(name: str, type: Type) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: LocalsItemDescription) -> str """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: LocalsItemDescription) -> Type """
        ...


    def ToString(self) -> str:
        """ ToString(self: LocalsItemDescription) -> str """
        ...


class SourceLocation: # skipped bases: <type 'object'>, <type 'object'>
    """
    SourceLocation(fileName: str, line: int)
    SourceLocation(fileName: str, startLine: int, startColumn: int, endLine: int, endColumn: int)
    """
    @property
    def EndColumn(self) -> int:
        """ Get: EndColumn(self: SourceLocation) -> int """
        ...

    @property
    def EndLine(self) -> int:
        """ Get: EndLine(self: SourceLocation) -> int """
        ...

    @property
    def FileName(self) -> str:
        """ Get: FileName(self: SourceLocation) -> str """
        ...

    @property
    def IsSingleWholeLine(self) -> bool:
        """ Get: IsSingleWholeLine(self: SourceLocation) -> bool """
        ...

    @property
    def StartColumn(self) -> int:
        """ Get: StartColumn(self: SourceLocation) -> int """
        ...

    @property
    def StartLine(self) -> int:
        """ Get: StartLine(self: SourceLocation) -> int """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: SourceLocation, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SourceLocation) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SourceLocationFoundEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SourceLocationFoundEventArgs(target: object, sourceLocation: SourceLocation) """
    @property
    def SourceLocation(self) -> SourceLocation:
        """ Get: SourceLocation(self: SourceLocationFoundEventArgs) -> SourceLocation """
        ...

    @property
    def Target(self) -> object:
        """ Get: Target(self: SourceLocationFoundEventArgs) -> object """
        ...


    def __new__(cls, target:object, sourceLocation:SourceLocation) -> Self:
        """ __new__(cls: type, target: object, sourceLocation: SourceLocation) """
        ...


class SourceLocationProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CollectMapping(rootActivity1:Activity, rootActivity2:Activity, mapping:Dictionary, path:str): # -> 
        """ CollectMapping(rootActivity1: Activity, rootActivity2: Activity, mapping: Dictionary[object, SourceLocation], path: str) """
        ...

    @staticmethod
    def GetSourceLocations(rootActivity:Activity, symbol:WorkflowSymbol) -> Dictionary:
        """ GetSourceLocations(rootActivity: Activity, symbol: WorkflowSymbol) -> Dictionary[object, SourceLocation] """
        ...

    @staticmethod
    def GetSymbols(rootActivity:Activity, sourceLocations:Dictionary) -> ICollection:
        """ GetSymbols(rootActivity: Activity, sourceLocations: Dictionary[object, SourceLocation]) -> ICollection[ActivitySymbol] """
        ...

    __all__: list = ...


class State: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class StateManager(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def Exit(self, threadIndex:int): # -> 
        """ Exit(self: StateManager, threadIndex: int) """
        ...


class ThreadWorkerController: # skipped bases: <type 'object'>, <type 'object'>
    """ ThreadWorkerController() """
    @staticmethod
    def IslandWorker(controller:ThreadWorkerController): # -> 
        """ IslandWorker(controller: ThreadWorkerController) """
        ...


class VirtualStackFrame: # skipped bases: <type 'object'>, <type 'object'>
    """
    VirtualStackFrame(state: State, locals: IDictionary[str, object])
    VirtualStackFrame(state: State)
    """
    @property
    def Locals(self) -> IDictionary:
        """ Get: Locals(self: VirtualStackFrame) -> IDictionary[str, object] """
        ...

    @property
    def State(self) -> State:
        """ Get: State(self: VirtualStackFrame) -> State """
        ...


    def ToString(self) -> str:
        """ ToString(self: VirtualStackFrame) -> str """
        ...


class XamlDebuggerXmlReader(XamlReader, IXamlLineInfo): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    XamlDebuggerXmlReader(underlyingTextReader: TextReader)
    XamlDebuggerXmlReader(underlyingTextReader: TextReader, schemaContext: XamlSchemaContext)
    XamlDebuggerXmlReader(underlyingReader: XamlReader, textReader: TextReader)
    XamlDebuggerXmlReader(underlyingReader: XamlReader, xamlLineInfo: IXamlLineInfo, textReader: TextReader)
    """
    @property
    def CollectNonActivitySourceLocation(self) -> bool:
        """
        Get: CollectNonActivitySourceLocation(self: XamlDebuggerXmlReader) -> bool
        Set: CollectNonActivitySourceLocation(self: XamlDebuggerXmlReader) = value
        """
        ...


    @staticmethod
    def CopyAttachedSourceLocation(source:object, destination:object): # -> 
        """ CopyAttachedSourceLocation(source: object, destination: object) """
        ...

    @staticmethod
    def GetEndColumn(instance:object) -> object:
        """ GetEndColumn(instance: object) -> object """
        ...

    @staticmethod
    def GetEndLine(instance:object) -> object:
        """ GetEndLine(instance: object) -> object """
        ...

    @staticmethod
    def GetFileName(instance:object) -> object:
        """ GetFileName(instance: object) -> object """
        ...

    @staticmethod
    def GetStartColumn(instance:object) -> object:
        """ GetStartColumn(instance: object) -> object """
        ...

    @staticmethod
    def GetStartLine(instance:object) -> object:
        """ GetStartLine(instance: object) -> object """
        ...

    @staticmethod
    def SetEndColumn(instance:object, value:object): # -> 
        """ SetEndColumn(instance: object, value: object) """
        ...

    @staticmethod
    def SetEndLine(instance:object, value:object): # -> 
        """ SetEndLine(instance: object, value: object) """
        ...

    @staticmethod
    def SetFileName(instance:object, value:object): # -> 
        """ SetFileName(instance: object, value: object) """
        ...

    @staticmethod
    def SetStartColumn(instance:object, value:object): # -> 
        """ SetStartColumn(instance: object, value: object) """
        ...

    @staticmethod
    def SetStartLine(instance:object, value:object): # -> 
        """ SetStartLine(instance: object, value: object) """
        ...

    def __new__(cls, *__args:TextReader) -> Self:
        """
        __new__(cls: type, underlyingTextReader: TextReader)
        __new__(cls: type, underlyingTextReader: TextReader, schemaContext: XamlSchemaContext)
        __new__(cls: type, underlyingReader: XamlReader, textReader: TextReader)
        __new__(cls: type, underlyingReader: XamlReader, xamlLineInfo: IXamlLineInfo, textReader: TextReader)
        """
        ...

    EndColumnName: AttachableMemberIdentifier = ...
    EndLineName: AttachableMemberIdentifier = ...
    FileNameName: AttachableMemberIdentifier = ...
    SourceLocationFound = ...
    StartColumnName: AttachableMemberIdentifier = ...
    StartLineName: AttachableMemberIdentifier = ...


# variables with complex values

