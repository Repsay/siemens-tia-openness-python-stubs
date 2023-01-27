# encoding: utf-8
# module System.Workflow.Runtime.DebugEngine calls itself DebugEngine
# from System.Workflow.Runtime, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (AsyncCallback, Attribute, Delegate, Enum, Guid, 
    IAsyncResult, MarshalByRefObject, MulticastDelegate, Uri)

from System.Collections.Generic import List

from System.EnterpriseServices import Activity

from System.Workflow.ComponentModel import ActivityExecutionStatus

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ActivityHandlerDescriptor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Name = ...
    Token = ...


class DebugController(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    def AttachToConduit(self, url:Uri): # -> 
        """ AttachToConduit(self: DebugController, url: Uri) """
        ...


class DebugEngineCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DebugEngineCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DebugEngineCallback, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DebugEngineCallback, result: IAsyncResult) """
        ...

    def Invoke(self): # -> 
        """ Invoke(self: DebugEngineCallback) """
        ...


class IExpressionEvaluationFrame: # skipped bases: <type 'object'>
    """ no doc """
    def CreateEvaluationFrame(self, instanceTable:IInstanceTable, callback:DebugEngineCallback): # -> 
        """ CreateEvaluationFrame(self: IExpressionEvaluationFrame, instanceTable: IInstanceTable, callback: DebugEngineCallback) """
        ...


class IInstanceTable: # skipped bases: <type 'object'>
    """ no doc """
    def GetActivity(self, instanceId:str, activityName:str) -> Activity:
        """ GetActivity(self: IInstanceTable, instanceId: str, activityName: str) -> Activity """
        ...


class IWorkflowDebugger: # skipped bases: <type 'object'>
    """ no doc """
    def ActivityStatusChanged(self, programId:Guid, scheduleTypeId:Guid, instanceId:Guid, activityQualifiedName:str, hierarchicalActivityId:str, status:ActivityExecutionStatus, stateReaderId:int): # -> 
        """ ActivityStatusChanged(self: IWorkflowDebugger, programId: Guid, scheduleTypeId: Guid, instanceId: Guid, activityQualifiedName: str, hierarchicalActivityId: str, status: ActivityExecutionStatus, stateReaderId: int) """
        ...

    def AssemblyLoaded(self, programId:Guid, assemblyPath:str, fromGlobalAssemblyCache:bool): # -> 
        """ AssemblyLoaded(self: IWorkflowDebugger, programId: Guid, assemblyPath: str, fromGlobalAssemblyCache: bool) """
        ...

    def BeforeActivityStatusChanged(self, programId:Guid, scheduleTypeId:Guid, instanceId:Guid, activityQualifiedName:str, hierarchicalActivityId:str, status:ActivityExecutionStatus, stateReaderId:int): # -> 
        """ BeforeActivityStatusChanged(self: IWorkflowDebugger, programId: Guid, scheduleTypeId: Guid, instanceId: Guid, activityQualifiedName: str, hierarchicalActivityId: str, status: ActivityExecutionStatus, stateReaderId: int) """
        ...

    def BeforeHandlerInvoked(self, programId:Guid, scheduleTypeId:Guid, activityQualifiedName:str, handlerMethod:ActivityHandlerDescriptor): # -> 
        """ BeforeHandlerInvoked(self: IWorkflowDebugger, programId: Guid, scheduleTypeId: Guid, activityQualifiedName: str, handlerMethod: ActivityHandlerDescriptor) """
        ...

    def HandlerInvoked(self, programId:Guid, instanceId:Guid, threadId:int, activityQualifiedName:str): # -> 
        """ HandlerInvoked(self: IWorkflowDebugger, programId: Guid, instanceId: Guid, threadId: int, activityQualifiedName: str) """
        ...

    def InstanceCompleted(self, programId:Guid, instanceId:Guid): # -> 
        """ InstanceCompleted(self: IWorkflowDebugger, programId: Guid, instanceId: Guid) """
        ...

    def InstanceCreated(self, programId:Guid, instanceId:Guid, scheduleTypeId:Guid): # -> 
        """ InstanceCreated(self: IWorkflowDebugger, programId: Guid, instanceId: Guid, scheduleTypeId: Guid) """
        ...

    def InstanceDynamicallyUpdated(self, programId:Guid, instanceId:Guid, scheduleTypeId:Guid): # -> 
        """ InstanceDynamicallyUpdated(self: IWorkflowDebugger, programId: Guid, instanceId: Guid, scheduleTypeId: Guid) """
        ...

    def ScheduleTypeLoaded(self, programId:Guid, scheduleTypeId:Guid, assemblyFullName:str, fileName:str, md5Digest:str, isDynamic:bool, scheduleNamespace:str, scheduleName:str, workflowMarkup:str): # -> 
        """ ScheduleTypeLoaded(self: IWorkflowDebugger, programId: Guid, scheduleTypeId: Guid, assemblyFullName: str, fileName: str, md5Digest: str, isDynamic: bool, scheduleNamespace: str, scheduleName: str, workflowMarkup: str) """
        ...

    def SetInitialActivityStatus(self, programId:Guid, scheduleTypeId:Guid, instanceId:Guid, activityQualifiedName:str, hierarchicalActivityId:str, status:ActivityExecutionStatus, stateReaderId:int): # -> 
        """ SetInitialActivityStatus(self: IWorkflowDebugger, programId: Guid, scheduleTypeId: Guid, instanceId: Guid, activityQualifiedName: str, hierarchicalActivityId: str, status: ActivityExecutionStatus, stateReaderId: int) """
        ...

    def UpdateHandlerMethodsForActivity(self, programId:Guid, scheduleTypeId:Guid, activityQualifiedName:str, handlerMethods:List): # -> 
        """ UpdateHandlerMethodsForActivity(self: IWorkflowDebugger, programId: Guid, scheduleTypeId: Guid, activityQualifiedName: str, handlerMethods: List[ActivityHandlerDescriptor]) """
        ...


class IWorkflowDebuggerService: # skipped bases: <type 'object'>
    """ no doc """
    def NotifyHandlerInvoked(self): # -> 
        """ NotifyHandlerInvoked(self: IWorkflowDebuggerService) """
        ...

    def NotifyHandlerInvoking(self, delegateHandler:Delegate): # -> 
        """ NotifyHandlerInvoking(self: IWorkflowDebuggerService, delegateHandler: Delegate) """
        ...


class WorkflowDebuggerSteppingAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ WorkflowDebuggerSteppingAttribute(steppingOption: WorkflowDebuggerSteppingOption) """
    @property
    def SteppingOption(self) -> WorkflowDebuggerSteppingOption:
        """ Get: SteppingOption(self: WorkflowDebuggerSteppingAttribute) -> WorkflowDebuggerSteppingOption """
        ...


    def __new__(cls, steppingOption:WorkflowDebuggerSteppingOption) -> Self:
        """ __new__(cls: type, steppingOption: WorkflowDebuggerSteppingOption) """
        ...


class WorkflowDebuggerSteppingOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WorkflowDebuggerSteppingOption, values: Concurrent (1), Sequential (0) """
    Concurrent: WorkflowDebuggerSteppingOption = ...
    Sequential: WorkflowDebuggerSteppingOption = ...
    value__ = ...


