# encoding: utf-8
# module System.Management.Automation.Internal calls itself Internal
# from System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Attribute, Enum, Guid, Int64, Type

from System.Collections import IEnumerable

from System.Collections.Generic import List

from System.Diagnostics import Debugger

from System.Management.Automation import (ActionPreference, CommandOrigin, 
    PSModuleInfo, PSObject, ParseException, PowerShell, SwitchParameter, 
    WorkflowInfo)

from System.Management.Automation.Language import (FunctionDefinitionAst, 
    ScriptBlockAst)

from System.Management.Automation.Runspaces import (InitialSessionState, 
    Runspace)

from System.Reflection import ConstructorInfo, MethodInfo

from typing import Tuple as Tuple_

"""The following names are not found in the module: Array[object], T, field#
"""

# no functions
# classes

class AlternateDataStreamUtilities: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    __all__: list = ...


class AlternateStreamData: # skipped bases: <type 'object'>, <type 'object'>
    """ AlternateStreamData() """
    @property
    def FileName(self) -> str:
        """
        Get: FileName(self: AlternateStreamData) -> str
        Set: FileName(self: AlternateStreamData) = value
        """
        ...

    @property
    def Length(self) -> Int64:
        """
        Get: Length(self: AlternateStreamData) -> Int64
        Set: Length(self: AlternateStreamData) = value
        """
        ...

    @property
    def Stream(self) -> str:
        """
        Get: Stream(self: AlternateStreamData) -> str
        Set: Stream(self: AlternateStreamData) = value
        """
        ...



class AutomationNull: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Value(self) -> PSObject:
        """ Get: Value() -> PSObject """
        ...


    __all__: list = ...


class ClassOps: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CallBaseCtor(target:object, ci:ConstructorInfo, args:Array): # -> 
        """ CallBaseCtor(target: object, ci: ConstructorInfo, args: Array[object]) """
        ...

    @staticmethod
    def CallMethodNonVirtually(target:object, mi:MethodInfo, args:Array) -> object:
        """ CallMethodNonVirtually(target: object, mi: MethodInfo, args: Array[object]) -> object """
        ...

    @staticmethod
    def CallVoidMethodNonVirtually(target:object, mi:MethodInfo, args:Array): # -> 
        """ CallVoidMethodNonVirtually(target: object, mi: MethodInfo, args: Array[object]) """
        ...

    @staticmethod
    def ValidateSetProperty(type:Type, propertyName:str, value:object): # -> 
        """ ValidateSetProperty(type: Type, propertyName: str, value: object) """
        ...

    __all__: list = ...


class CmdletMetadataAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    pass

class CommonParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Debug(self) -> SwitchParameter:
        """
        Get: Debug(self: CommonParameters) -> SwitchParameter
        Set: Debug(self: CommonParameters) = value
        """
        ...

    @property
    def ErrorAction(self) -> ActionPreference:
        """
        Get: ErrorAction(self: CommonParameters) -> ActionPreference
        Set: ErrorAction(self: CommonParameters) = value
        """
        ...

    @property
    def ErrorVariable(self) -> str:
        """
        Get: ErrorVariable(self: CommonParameters) -> str
        Set: ErrorVariable(self: CommonParameters) = value
        """
        ...

    @property
    def InformationAction(self) -> ActionPreference:
        """
        Get: InformationAction(self: CommonParameters) -> ActionPreference
        Set: InformationAction(self: CommonParameters) = value
        """
        ...

    @property
    def InformationVariable(self) -> str:
        """
        Get: InformationVariable(self: CommonParameters) -> str
        Set: InformationVariable(self: CommonParameters) = value
        """
        ...

    @property
    def OutBuffer(self) -> int:
        """
        Get: OutBuffer(self: CommonParameters) -> int
        Set: OutBuffer(self: CommonParameters) = value
        """
        ...

    @property
    def OutVariable(self) -> str:
        """
        Get: OutVariable(self: CommonParameters) -> str
        Set: OutVariable(self: CommonParameters) = value
        """
        ...

    @property
    def PipelineVariable(self) -> str:
        """
        Get: PipelineVariable(self: CommonParameters) -> str
        Set: PipelineVariable(self: CommonParameters) = value
        """
        ...

    @property
    def Verbose(self) -> SwitchParameter:
        """
        Get: Verbose(self: CommonParameters) -> SwitchParameter
        Set: Verbose(self: CommonParameters) = value
        """
        ...

    @property
    def WarningAction(self) -> ActionPreference:
        """
        Get: WarningAction(self: CommonParameters) -> ActionPreference
        Set: WarningAction(self: CommonParameters) = value
        """
        ...

    @property
    def WarningVariable(self) -> str:
        """
        Get: WarningVariable(self: CommonParameters) -> str
        Set: WarningVariable(self: CommonParameters) = value
        """
        ...



class DebuggerUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def EndMonitoringRunspace(debugger:Debugger, runspaceInfo:PSMonitorRunspaceInfo): # -> 
        """ EndMonitoringRunspace(debugger: Debugger, runspaceInfo: PSMonitorRunspaceInfo) """
        ...

    @staticmethod
    def GetWorkflowDebuggerFunctions() -> IEnumerable:
        """ GetWorkflowDebuggerFunctions() -> IEnumerable[str] """
        ...

    @staticmethod
    def ShouldAddCommandToHistory(command:str) -> bool:
        """ ShouldAddCommandToHistory(command: str) -> bool """
        ...

    @staticmethod
    def StartMonitoringRunspace(debugger:Debugger, runspaceInfo:PSMonitorRunspaceInfo): # -> 
        """ StartMonitoringRunspace(debugger: Debugger, runspaceInfo: PSMonitorRunspaceInfo) """
        ...

    GetPSCallStackOverrideFunction: str = ...
    RemoveVariableFunction: str = ...
    SetVariableFunction: str = ...
    __all__: list = ...


class IAstToWorkflowConverter: # skipped bases: <type 'object'>
    """ no doc """
    def CompileWorkflow(self, name:str, definition:str, initialSessionState:InitialSessionState) -> WorkflowInfo:
        """ CompileWorkflow(self: IAstToWorkflowConverter, name: str, definition: str, initialSessionState: InitialSessionState) -> WorkflowInfo """
        ...

    def CompileWorkflows(self, ast:ScriptBlockAst, definingModule:PSModuleInfo, *__args:InitialSessionState) -> Tuple_[List, ParseException]:
        """
        CompileWorkflows(self: IAstToWorkflowConverter, ast: ScriptBlockAst, definingModule: PSModuleInfo) -> List[WorkflowInfo]
        CompileWorkflows(self: IAstToWorkflowConverter, ast: ScriptBlockAst, definingModule: PSModuleInfo, initialSessionState: InitialSessionState) -> (List[WorkflowInfo], ParseException)
        CompileWorkflows(self: IAstToWorkflowConverter, ast: ScriptBlockAst, definingModule: PSModuleInfo, initialSessionState: InitialSessionState, languageMode: Nullable[PSLanguageMode]) -> (List[WorkflowInfo], ParseException)
        CompileWorkflows(self: IAstToWorkflowConverter, ast: ScriptBlockAst, definingModule: PSModuleInfo, rootWorkflowName: str) -> List[WorkflowInfo]
        CompileWorkflows(self: IAstToWorkflowConverter, ast: ScriptBlockAst, definingModule: PSModuleInfo, initialSessionState: InitialSessionState, rootWorkflowName: str) -> (List[WorkflowInfo], ParseException)
        """
        ...

    def ValidateAst(self, ast:FunctionDefinitionAst) -> List:
        """ ValidateAst(self: IAstToWorkflowConverter, ast: FunctionDefinitionAst) -> List[ParseError] """
        ...


class InternalCommand: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CommandOrigin(self) -> CommandOrigin:
        """ Get: CommandOrigin(self: InternalCommand) -> CommandOrigin """
        ...



class InternalTestHooks: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def SetTestHook(property:str, value:bool): # -> 
        """ SetTestHook(property: str, value: bool) """
        ...

    __all__: list = ...


class ParsingBaseAttribute(CmdletMetadataAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    pass

class PSMonitorRunspaceInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Runspace(self) -> Runspace:
        """ Get: Runspace(self: PSMonitorRunspaceInfo) -> Runspace """
        ...

    @property
    def RunspaceType(self) -> PSMonitorRunspaceType:
        """ Get: RunspaceType(self: PSMonitorRunspaceInfo) -> PSMonitorRunspaceType """
        ...



class PSEmbeddedMonitorRunspaceInfo(PSMonitorRunspaceInfo): # skipped bases: <type 'object'>
    """ PSEmbeddedMonitorRunspaceInfo(runspace: Runspace, runspaceType: PSMonitorRunspaceType, command: PowerShell, parentDebuggerId: Guid) """
    @property
    def Command(self) -> PowerShell:
        """ Get: Command(self: PSEmbeddedMonitorRunspaceInfo) -> PowerShell """
        ...

    @property
    def ParentDebuggerId(self) -> Guid:
        """ Get: ParentDebuggerId(self: PSEmbeddedMonitorRunspaceInfo) -> Guid """
        ...



class PSMonitorRunspaceType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PSMonitorRunspaceType, values: InvokeCommand (1), Standalone (0), WorkflowInlineScript (2) """
    InvokeCommand: PSMonitorRunspaceType = ...
    Standalone: PSMonitorRunspaceType = ...
    value__ = ...
    WorkflowInlineScript: PSMonitorRunspaceType = ...


class PSStandaloneMonitorRunspaceInfo(PSMonitorRunspaceInfo): # skipped bases: <type 'object'>
    """ PSStandaloneMonitorRunspaceInfo(runspace: Runspace) """
    pass

class ScriptBlockMemberMethodWrapper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def InvokeHelper(self, instance:object, sessionStateInternal:object, args:Array): # -> 
        """ InvokeHelper(self: ScriptBlockMemberMethodWrapper, instance: object, sessionStateInternal: object, args: Array[object]) """
        ...

    def InvokeHelperT(self, instance:object, sessionStateInternal:object, args:Array): # -> T
        """ InvokeHelperT[T](self: ScriptBlockMemberMethodWrapper, instance: object, sessionStateInternal: object, args: Array[object]) -> T """
        ...

    _emptyArgumentArray = ...


class SecuritySupport: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def IsProductBinary(file:str) -> bool:
        """ IsProductBinary(file: str) -> bool """
        ...

    __all__: list = ...


class SessionStateKeeper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetSessionState(self) -> object:
        """ GetSessionState(self: SessionStateKeeper) -> object """
        ...


class ShouldProcessParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Confirm(self) -> SwitchParameter:
        """
        Get: Confirm(self: ShouldProcessParameters) -> SwitchParameter
        Set: Confirm(self: ShouldProcessParameters) = value
        """
        ...

    @property
    def WhatIf(self) -> SwitchParameter:
        """
        Get: WhatIf(self: ShouldProcessParameters) -> SwitchParameter
        Set: WhatIf(self: ShouldProcessParameters) = value
        """
        ...



class TransactionParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def UseTransaction(self) -> SwitchParameter:
        """
        Get: UseTransaction(self: TransactionParameters) -> SwitchParameter
        Set: UseTransaction(self: TransactionParameters) = value
        """
        ...



