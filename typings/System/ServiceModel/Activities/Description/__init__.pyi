# encoding: utf-8
# module System.ServiceModel.Activities.Description calls itself Description
# from System.ServiceModel.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.WorkflowServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.JScript import Binding

from System import Attribute, Enum, TimeSpan, Type

from System.Collections import IEnumerable

from System.ServiceModel.Activities import WorkflowHostingEndpoint

"""The following names are not found in the module: (IContractBehavior, 
    IServiceBehavior, InstanceCompletionAction, InstanceEncodingOption, 
    InstanceLockedExceptionAction, field#)
"""

# no functions
# classes

class BufferedReceiveServiceBehavior(IServiceBehavior): # skipped bases: <type 'object'>
    """ BufferedReceiveServiceBehavior() """
    @property
    def MaxPendingMessagesPerChannel(self) -> int:
        """
        Get: MaxPendingMessagesPerChannel(self: BufferedReceiveServiceBehavior) -> int
        Set: MaxPendingMessagesPerChannel(self: BufferedReceiveServiceBehavior) = value
        """
        ...



class EtwTrackingBehavior(IServiceBehavior): # skipped bases: <type 'object'>
    """ EtwTrackingBehavior() """
    @property
    def ProfileName(self) -> str:
        """
        Get: ProfileName(self: EtwTrackingBehavior) -> str
        Set: ProfileName(self: EtwTrackingBehavior) = value
        """
        ...



class SqlWorkflowInstanceStoreBehavior(IServiceBehavior): # skipped bases: <type 'object'>
    """
    SqlWorkflowInstanceStoreBehavior()
    SqlWorkflowInstanceStoreBehavior(connectionString: str)
    """
    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: SqlWorkflowInstanceStoreBehavior) -> str
        Set: ConnectionString(self: SqlWorkflowInstanceStoreBehavior) = value
        """
        ...

    @property
    def HostLockRenewalPeriod(self) -> TimeSpan:
        """
        Get: HostLockRenewalPeriod(self: SqlWorkflowInstanceStoreBehavior) -> TimeSpan
        Set: HostLockRenewalPeriod(self: SqlWorkflowInstanceStoreBehavior) = value
        """
        ...

    @property
    def InstanceCompletionAction(self): # -> InstanceCompletionAction
        """
        Get: InstanceCompletionAction(self: SqlWorkflowInstanceStoreBehavior) -> InstanceCompletionAction
        Set: InstanceCompletionAction(self: SqlWorkflowInstanceStoreBehavior) = value
        """
        ...

    @property
    def InstanceEncodingOption(self): # -> InstanceEncodingOption
        """
        Get: InstanceEncodingOption(self: SqlWorkflowInstanceStoreBehavior) -> InstanceEncodingOption
        Set: InstanceEncodingOption(self: SqlWorkflowInstanceStoreBehavior) = value
        """
        ...

    @property
    def InstanceLockedExceptionAction(self): # -> InstanceLockedExceptionAction
        """
        Get: InstanceLockedExceptionAction(self: SqlWorkflowInstanceStoreBehavior) -> InstanceLockedExceptionAction
        Set: InstanceLockedExceptionAction(self: SqlWorkflowInstanceStoreBehavior) = value
        """
        ...

    @property
    def MaxConnectionRetries(self) -> int:
        """
        Get: MaxConnectionRetries(self: SqlWorkflowInstanceStoreBehavior) -> int
        Set: MaxConnectionRetries(self: SqlWorkflowInstanceStoreBehavior) = value
        """
        ...

    @property
    def RunnableInstancesDetectionPeriod(self) -> TimeSpan:
        """
        Get: RunnableInstancesDetectionPeriod(self: SqlWorkflowInstanceStoreBehavior) -> TimeSpan
        Set: RunnableInstancesDetectionPeriod(self: SqlWorkflowInstanceStoreBehavior) = value
        """
        ...


    def Promote(self, name:str, promoteAsSqlVariant:IEnumerable, promoteAsBinary:IEnumerable): # -> 
        """ Promote(self: SqlWorkflowInstanceStoreBehavior, name: str, promoteAsSqlVariant: IEnumerable[XName], promoteAsBinary: IEnumerable[XName]) """
        ...


class WorkflowContractBehaviorAttribute(Attribute, IContractBehavior): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ WorkflowContractBehaviorAttribute() """
    pass

class WorkflowIdleBehavior(IServiceBehavior): # skipped bases: <type 'object'>
    """ WorkflowIdleBehavior() """
    @property
    def TimeToPersist(self) -> TimeSpan:
        """
        Get: TimeToPersist(self: WorkflowIdleBehavior) -> TimeSpan
        Set: TimeToPersist(self: WorkflowIdleBehavior) = value
        """
        ...

    @property
    def TimeToUnload(self) -> TimeSpan:
        """
        Get: TimeToUnload(self: WorkflowIdleBehavior) -> TimeSpan
        Set: TimeToUnload(self: WorkflowIdleBehavior) = value
        """
        ...



class WorkflowInstanceManagementBehavior(IServiceBehavior): # skipped bases: <type 'object'>
    """ WorkflowInstanceManagementBehavior() """
    @property
    def HttpControlEndpointBinding(self) -> Binding:
        """ Get: HttpControlEndpointBinding() -> Binding """
        ...

    @property
    def NamedPipeControlEndpointBinding(self) -> Binding:
        """ Get: NamedPipeControlEndpointBinding() -> Binding """
        ...

    @property
    def WindowsGroup(self) -> str:
        """
        Get: WindowsGroup(self: WorkflowInstanceManagementBehavior) -> str
        Set: WindowsGroup(self: WorkflowInstanceManagementBehavior) = value
        """
        ...


    ControlEndpointAddress: str = ...


class WorkflowRuntimeEndpoint(WorkflowHostingEndpoint): # skipped bases: <type 'object'>
    """ WorkflowRuntimeEndpoint() """
    def AddService(self, service:object): # -> 
        """ AddService(self: WorkflowRuntimeEndpoint, service: object) """
        ...

    def GetService(self, serviceType:Type = ...) -> object:
        """
        GetService(self: WorkflowRuntimeEndpoint, serviceType: Type) -> object
        GetService[T](self: WorkflowRuntimeEndpoint) -> T
        """
        ...

    def RemoveService(self, service:object): # -> 
        """ RemoveService(self: WorkflowRuntimeEndpoint, service: object) """
        ...


class WorkflowUnhandledExceptionAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WorkflowUnhandledExceptionAction, values: Abandon (0), AbandonAndSuspend (3), Cancel (1), Terminate (2) """
    Abandon: WorkflowUnhandledExceptionAction = ...
    AbandonAndSuspend: WorkflowUnhandledExceptionAction = ...
    Cancel: WorkflowUnhandledExceptionAction = ...
    Terminate: WorkflowUnhandledExceptionAction = ...
    value__ = ...


class WorkflowUnhandledExceptionBehavior(IServiceBehavior): # skipped bases: <type 'object'>
    """ WorkflowUnhandledExceptionBehavior() """
    @property
    def Action(self) -> WorkflowUnhandledExceptionAction:
        """
        Get: Action(self: WorkflowUnhandledExceptionBehavior) -> WorkflowUnhandledExceptionAction
        Set: Action(self: WorkflowUnhandledExceptionBehavior) = value
        """
        ...



