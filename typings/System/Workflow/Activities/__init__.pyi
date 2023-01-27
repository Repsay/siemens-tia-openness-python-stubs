# encoding: utf-8
# module System.Workflow.Activities calls itself Activities
# from System.WorkflowServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Workflow.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Attribute, Enum, EventArgs, Guid, IComparable, 
    IDisposable, Nullable, SystemException, TimeSpan, Type)

from System.Activities.Hosting import WorkflowInstance

from System.Collections import ICollection, IDictionary, IList

from System.Collections.Generic import List

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel.DataAnnotations import Validator

from System.Configuration import ConfigurationSection

from System.DirectoryServices import DirectoryEntry

from System.DirectoryServices.ActiveDirectory import ActiveDirectoryRole

from System.EnterpriseServices import Activity

from System.Reflection import ParameterAttributes

from System.Runtime.Serialization import ISerializable

from System.Security.Principal import SecurityIdentifier

from System.ServiceModel import AddressFilterMode, FaultException

from System.Web.Services import WebService

from System.Workflow.Activities.Configuration import (
    ActiveDirectoryRoleFactoryConfiguration)

from System.Workflow.Activities.Rules import RuleSetReference

from System.Workflow.ComponentModel import (ActivityCondition, 
    ActivityExecutionContext, CompositeActivity, DependencyObject, 
    DependencyProperty, IActivityEventListener, ICompensatableActivity, 
    IDynamicPropertyTypeProvider, WorkflowParameterBindingCollection)

from System.Workflow.ComponentModel.Compiler import (ActivityValidator, 
    CompositeActivityValidator)

from System.Workflow.ComponentModel.Design import ITypeFilterProvider

from System.Workflow.Runtime.Configuration import (
    WorkflowRuntimeServiceElementCollection)

from System.Workflow.Runtime.Hosting import WorkflowRuntimeService

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    CorrelationToken, IPendingWork, IPropertyValueProvider, 
    IServiceDescriptionBuilder, IfElseBranchActivity, WorkflowRoleCollection, 
    field#)
"""

# no functions
# classes

class WorkflowRole: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: WorkflowRole) -> str
        Set: Name(self: WorkflowRole) = value
        """
        ...


    def GetIdentities(self) -> IList:
        """ GetIdentities(self: WorkflowRole) -> IList[str] """
        ...

    def IncludesIdentity(self, identity:str) -> bool:
        """ IncludesIdentity(self: WorkflowRole, identity: str) -> bool """
        ...


class ActiveDirectoryRole(IDisposable, ISerializable, WorkflowRole): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RootEntry(self) -> DirectoryEntry:
        """ Get: RootEntry(self: ActiveDirectoryRole) -> DirectoryEntry """
        ...


    def GetAllReports(self) -> ActiveDirectoryRole:
        """ GetAllReports(self: ActiveDirectoryRole) -> ActiveDirectoryRole """
        ...

    def GetDirectReports(self) -> ActiveDirectoryRole:
        """ GetDirectReports(self: ActiveDirectoryRole) -> ActiveDirectoryRole """
        ...

    def GetEntries(self) -> ICollection:
        """ GetEntries(self: ActiveDirectoryRole) -> ICollection[DirectoryEntry] """
        ...

    def GetManager(self) -> ActiveDirectoryRole:
        """ GetManager(self: ActiveDirectoryRole) -> ActiveDirectoryRole """
        ...

    def GetManagerialChain(self) -> ActiveDirectoryRole:
        """ GetManagerialChain(self: ActiveDirectoryRole) -> ActiveDirectoryRole """
        ...

    def GetPeers(self) -> ActiveDirectoryRole:
        """ GetPeers(self: ActiveDirectoryRole) -> ActiveDirectoryRole """
        ...

    def GetSecurityIdentifiers(self) -> IList:
        """ GetSecurityIdentifiers(self: ActiveDirectoryRole) -> IList[SecurityIdentifier] """
        ...


class ActiveDirectoryRoleFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Configuration(self) -> ActiveDirectoryRoleFactoryConfiguration:
        """ Get: Configuration() -> ActiveDirectoryRoleFactoryConfiguration """
        ...


    @staticmethod
    def CreateFromAlias(alias:str) -> ActiveDirectoryRole:
        """ CreateFromAlias(alias: str) -> ActiveDirectoryRole """
        ...

    @staticmethod
    def CreateFromEmailAddress(emailAddress:str) -> ActiveDirectoryRole:
        """ CreateFromEmailAddress(emailAddress: str) -> ActiveDirectoryRole """
        ...

    @staticmethod
    def CreateFromSecurityIdentifier(sid:SecurityIdentifier) -> ActiveDirectoryRole:
        """ CreateFromSecurityIdentifier(sid: SecurityIdentifier) -> ActiveDirectoryRole """
        ...

    __all__: list = ...


class CallExternalMethodActivity(IPropertyValueProvider, IDynamicPropertyTypeProvider, Activity): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    CallExternalMethodActivity()
    CallExternalMethodActivity(name: str)
    """
    @property
    def CorrelationToken(self): # -> CorrelationToken
        """
        Get: CorrelationToken(self: CallExternalMethodActivity) -> CorrelationToken
        Set: CorrelationToken(self: CallExternalMethodActivity) = value
        """
        ...

    @property
    def InterfaceType(self) -> Type:
        """
        Get: InterfaceType(self: CallExternalMethodActivity) -> Type
        Set: InterfaceType(self: CallExternalMethodActivity) = value
        """
        ...

    @property
    def MethodName(self) -> str:
        """
        Get: MethodName(self: CallExternalMethodActivity) -> str
        Set: MethodName(self: CallExternalMethodActivity) = value
        """
        ...

    @property
    def ParameterBindings(self) -> WorkflowParameterBindingCollection:
        """ Get: ParameterBindings(self: CallExternalMethodActivity) -> WorkflowParameterBindingCollection """
        ...


    def OnMethodInvoked(self, *args): #cannot find CLR method
        """ OnMethodInvoked(self: CallExternalMethodActivity, e: EventArgs) """
        ...

    def OnMethodInvoking(self, *args): #cannot find CLR method
        """ OnMethodInvoking(self: CallExternalMethodActivity, e: EventArgs) """
        ...

    CorrelationTokenProperty: DependencyProperty = ...
    InterfaceTypeProperty: DependencyProperty = ...
    MethodInvoking = ...
    MethodInvokingEvent: DependencyProperty = ...
    MethodNameProperty: DependencyProperty = ...
    ParameterBindingsProperty: DependencyProperty = ...


class CallExternalMethodActivityValidator(ActivityValidator): # skipped bases: <type 'object'>
    """ CallExternalMethodActivityValidator() """
    pass

class ChannelToken(DependencyObject, IPropertyValueProvider): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """ ChannelToken() """
    @property
    def EndpointName(self) -> str:
        """
        Get: EndpointName(self: ChannelToken) -> str
        Set: EndpointName(self: ChannelToken) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: ChannelToken) -> str
        Set: Name(self: ChannelToken) = value
        """
        ...

    @property
    def OwnerActivityName(self) -> str:
        """
        Get: OwnerActivityName(self: ChannelToken) -> str
        Set: OwnerActivityName(self: ChannelToken) = value
        """
        ...



class CodeActivity(Activity): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    CodeActivity()
    CodeActivity(name: str)
    """
    ExecuteCode = ...
    ExecuteCodeEvent: DependencyProperty = ...


class CodeCondition(ActivityCondition): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """ CodeCondition() """
    Condition = ...
    ConditionEvent: DependencyProperty = ...


class SequenceActivity(CompositeActivity, IActivityEventListener): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    SequenceActivity()
    SequenceActivity(name: str)
    """
    def OnSequenceComplete(self, *args): #cannot find CLR method
        """ OnSequenceComplete(self: SequenceActivity, executionContext: ActivityExecutionContext) """
        ...


class CompensatableSequenceActivity(SequenceActivity, ICompensatableActivity): # skipped bases: <type 'IActivityEventListener[ActivityExecutionStatusChangedEventArgs]'>, <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    CompensatableSequenceActivity()
    CompensatableSequenceActivity(name: str)
    """
    pass

class ConditionalEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    ConditionalEventArgs()
    ConditionalEventArgs(result: bool)
    """
    @property
    def Result(self) -> bool:
        """
        Get: Result(self: ConditionalEventArgs) -> bool
        Set: Result(self: ConditionalEventArgs) = value
        """
        ...


    def __new__(cls, result:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, result: bool)
        """
        ...


class ConditionedActivityGroup(CompositeActivity, IActivityEventListener): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    ConditionedActivityGroup()
    ConditionedActivityGroup(name: str)
    """
    @property
    def UntilCondition(self) -> ActivityCondition:
        """
        Get: UntilCondition(self: ConditionedActivityGroup) -> ActivityCondition
        Set: UntilCondition(self: ConditionedActivityGroup) = value
        """
        ...


    def GetChildActivityExecutedCount(self, child:Activity) -> int:
        """ GetChildActivityExecutedCount(self: ConditionedActivityGroup, child: Activity) -> int """
        ...

    def GetDynamicActivity(self, childActivityName:str) -> Activity:
        """ GetDynamicActivity(self: ConditionedActivityGroup, childActivityName: str) -> Activity """
        ...

    @staticmethod
    def GetWhenCondition(dependencyObject:object) -> object:
        """ GetWhenCondition(dependencyObject: object) -> object """
        ...

    @staticmethod
    def SetWhenCondition(dependencyObject:object, value:object): # -> 
        """ SetWhenCondition(dependencyObject: object, value: object) """
        ...

    UntilConditionProperty: DependencyProperty = ...
    WhenConditionProperty: DependencyProperty = ...


class ContextToken(DependencyObject, IPropertyValueProvider): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    ContextToken()
    ContextToken(name: str)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: ContextToken) -> str
        Set: Name(self: ContextToken) = value
        """
        ...

    @property
    def OwnerActivityName(self) -> str:
        """
        Get: OwnerActivityName(self: ContextToken) -> str
        Set: OwnerActivityName(self: ContextToken) = value
        """
        ...


    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...

    RootContextName: str = ...


class CorrelationAliasAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CorrelationAliasAttribute(name: str, path: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: CorrelationAliasAttribute) -> str """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: CorrelationAliasAttribute) -> str """
        ...


    def __new__(cls, name:str, path:str) -> Self:
        """ __new__(cls: type, name: str, path: str) """
        ...


class CorrelationInitializerAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CorrelationInitializerAttribute() """
    pass

class CorrelationParameterAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CorrelationParameterAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: CorrelationParameterAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class IEventActivity: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def QueueName(self) -> IComparable:
        """ Get: QueueName(self: IEventActivity) -> IComparable """
        ...


    def Subscribe(self, parentContext:ActivityExecutionContext, parentEventHandler:IActivityEventListener): # -> 
        """ Subscribe(self: IEventActivity, parentContext: ActivityExecutionContext, parentEventHandler: IActivityEventListener[QueueEventArgs]) """
        ...

    def Unsubscribe(self, parentContext:ActivityExecutionContext, parentEventHandler:IActivityEventListener): # -> 
        """ Unsubscribe(self: IEventActivity, parentContext: ActivityExecutionContext, parentEventHandler: IActivityEventListener[QueueEventArgs]) """
        ...


class DelayActivity(IEventActivity, IActivityEventListener, Activity): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    DelayActivity()
    DelayActivity(name: str)
    """
    @property
    def TimeoutDuration(self) -> TimeSpan:
        """
        Get: TimeoutDuration(self: DelayActivity) -> TimeSpan
        Set: TimeoutDuration(self: DelayActivity) = value
        """
        ...


    InitializeTimeoutDuration = ...
    InitializeTimeoutDurationEvent: DependencyProperty = ...
    TimeoutDurationProperty: DependencyProperty = ...


class EventDeliveryFailedException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    EventDeliveryFailedException()
    EventDeliveryFailedException(message: str)
    EventDeliveryFailedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class EventDrivenActivity(SequenceActivity): # skipped bases: <type 'IActivityEventListener[ActivityExecutionStatusChangedEventArgs]'>, <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    EventDrivenActivity()
    EventDrivenActivity(name: str)
    """
    @property
    def EventActivity(self) -> IEventActivity:
        """ Get: EventActivity(self: EventDrivenActivity) -> IEventActivity """
        ...



class EventHandlersActivity(CompositeActivity, IActivityEventListener): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    EventHandlersActivity()
    EventHandlersActivity(name: str)
    """
    def GetDynamicActivity(self, childActivityName:str) -> Activity:
        """ GetDynamicActivity(self: EventHandlersActivity, childActivityName: str) -> Activity """
        ...


class EventHandlingScopeActivity(CompositeActivity, IActivityEventListener): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    EventHandlingScopeActivity()
    EventHandlingScopeActivity(name: str)
    """
    pass

class EventQueueName(IComparable): # skipped bases: <type 'object'>
    """
    EventQueueName(interfaceType: Type, operation: str)
    EventQueueName(interfaceType: Type, operation: str, propertyValues: ICollection[CorrelationProperty])
    """
    @property
    def InterfaceType(self) -> Type:
        """ Get: InterfaceType(self: EventQueueName) -> Type """
        ...

    @property
    def MethodName(self) -> str:
        """ Get: MethodName(self: EventQueueName) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: EventQueueName, obj: object) -> bool """
        ...

    def GetCorrelationValues(self) -> Array:
        """ GetCorrelationValues(self: EventQueueName) -> Array[CorrelationProperty] """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: EventQueueName) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: EventQueueName) -> str """
        ...


class ExecutionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ExecutionType, values: Parallel (1), Sequence (0) """
    Parallel: ExecutionType = ...
    Sequence: ExecutionType = ...
    value__ = ...


class ExternalDataEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    ExternalDataEventArgs()
    ExternalDataEventArgs(instanceId: Guid)
    ExternalDataEventArgs(instanceId: Guid, workHandler: IPendingWork, workItem: object, waitForIdle: bool)
    ExternalDataEventArgs(instanceId: Guid, workHandler: IPendingWork, workItem: object)
    """
    @property
    def Identity(self) -> str:
        """
        Get: Identity(self: ExternalDataEventArgs) -> str
        Set: Identity(self: ExternalDataEventArgs) = value
        """
        ...

    @property
    def InstanceId(self) -> Guid:
        """
        Get: InstanceId(self: ExternalDataEventArgs) -> Guid
        Set: InstanceId(self: ExternalDataEventArgs) = value
        """
        ...

    @property
    def WaitForIdle(self) -> bool:
        """
        Get: WaitForIdle(self: ExternalDataEventArgs) -> bool
        Set: WaitForIdle(self: ExternalDataEventArgs) = value
        """
        ...

    @property
    def WorkHandler(self): # -> IPendingWork
        """
        Get: WorkHandler(self: ExternalDataEventArgs) -> IPendingWork
        Set: WorkHandler(self: ExternalDataEventArgs) = value
        """
        ...

    @property
    def WorkItem(self) -> object:
        """
        Get: WorkItem(self: ExternalDataEventArgs) -> object
        Set: WorkItem(self: ExternalDataEventArgs) = value
        """
        ...


    def __new__(cls, instanceId:Guid = ..., workHandler = ..., workItem:object = ..., waitForIdle:bool = ...) -> Self: # Not found arg types: {'workHandler': 'IPendingWork'}
        """
        __new__(cls: type)
        __new__(cls: type, instanceId: Guid)
        __new__(cls: type, instanceId: Guid, workHandler: IPendingWork, workItem: object, waitForIdle: bool)
        __new__(cls: type, instanceId: Guid, workHandler: IPendingWork, workItem: object)
        """
        ...


class ExternalDataExchangeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ExternalDataExchangeAttribute() """
    pass

class ExternalDataExchangeService(WorkflowRuntimeService): # skipped bases: <type 'object'>
    """
    ExternalDataExchangeService()
    ExternalDataExchangeService(configSectionName: str)
    ExternalDataExchangeService(parameters: NameValueCollection)
    ExternalDataExchangeService(settings: ExternalDataExchangeServiceSection)
    """
    def AddService(self, service:object): # -> 
        """ AddService(self: ExternalDataExchangeService, service: object) """
        ...

    def GetService(self, serviceType:Type) -> object:
        """ GetService(self: ExternalDataExchangeService, serviceType: Type) -> object """
        ...

    def RemoveService(self, service:object): # -> 
        """ RemoveService(self: ExternalDataExchangeService, service: object) """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, configSectionName: str)
        __new__(cls: type, parameters: NameValueCollection)
        __new__(cls: type, settings: ExternalDataExchangeServiceSection)
        """
        ...


class ExternalDataExchangeServiceSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ ExternalDataExchangeServiceSection() """
    @property
    def Services(self) -> WorkflowRuntimeServiceElementCollection:
        """ Get: Services(self: ExternalDataExchangeServiceSection) -> WorkflowRuntimeServiceElementCollection """
        ...



class HandleExternalEventActivity(IPropertyValueProvider, IEventActivity, IDynamicPropertyTypeProvider, IActivityEventListener, Activity): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    HandleExternalEventActivity()
    HandleExternalEventActivity(name: str)
    """
    @property
    def CorrelationToken(self): # -> CorrelationToken
        """
        Get: CorrelationToken(self: HandleExternalEventActivity) -> CorrelationToken
        Set: CorrelationToken(self: HandleExternalEventActivity) = value
        """
        ...

    @property
    def EventName(self) -> str:
        """
        Get: EventName(self: HandleExternalEventActivity) -> str
        Set: EventName(self: HandleExternalEventActivity) = value
        """
        ...

    @property
    def InterfaceType(self) -> Type:
        """
        Get: InterfaceType(self: HandleExternalEventActivity) -> Type
        Set: InterfaceType(self: HandleExternalEventActivity) = value
        """
        ...

    @property
    def ParameterBindings(self) -> WorkflowParameterBindingCollection:
        """ Get: ParameterBindings(self: HandleExternalEventActivity) -> WorkflowParameterBindingCollection """
        ...

    @property
    def Roles(self): # -> WorkflowRoleCollection
        """
        Get: Roles(self: HandleExternalEventActivity) -> WorkflowRoleCollection
        Set: Roles(self: HandleExternalEventActivity) = value
        """
        ...


    def OnInvoked(self, *args): #cannot find CLR method
        """ OnInvoked(self: HandleExternalEventActivity, e: EventArgs) """
        ...

    CorrelationTokenProperty: DependencyProperty = ...
    EventNameProperty: DependencyProperty = ...
    InterfaceTypeProperty: DependencyProperty = ...
    Invoked = ...
    InvokedEvent: DependencyProperty = ...
    ParameterBindingsProperty: DependencyProperty = ...
    RolesProperty: DependencyProperty = ...


class HandleExternalEventActivityValidator(ActivityValidator): # skipped bases: <type 'object'>
    """ HandleExternalEventActivityValidator() """
    pass

class IfElseActivity(CompositeActivity, IActivityEventListener): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    IfElseActivity()
    IfElseActivity(name: str)
    """
    def AddBranch(self, activities:ICollection, branchCondition:ActivityCondition = ...): # -> IfElseBranchActivity
        """
        AddBranch(self: IfElseActivity, activities: ICollection[Activity]) -> IfElseBranchActivity
        AddBranch(self: IfElseActivity, activities: ICollection[Activity], branchCondition: ActivityCondition) -> IfElseBranchActivity
        """
        ...


class IfElseBranchActivity(SequenceActivity): # skipped bases: <type 'IActivityEventListener[ActivityExecutionStatusChangedEventArgs]'>, <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    IfElseBranchActivity()
    IfElseBranchActivity(name: str)
    """
    @property
    def Condition(self) -> ActivityCondition:
        """
        Get: Condition(self: IfElseBranchActivity) -> ActivityCondition
        Set: Condition(self: IfElseBranchActivity) = value
        """
        ...


    ConditionProperty: DependencyProperty = ...


class InvokeWebServiceActivity(IPropertyValueProvider, IDynamicPropertyTypeProvider, Activity): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    InvokeWebServiceActivity()
    InvokeWebServiceActivity(name: str)
    """
    @property
    def MethodName(self) -> str:
        """
        Get: MethodName(self: InvokeWebServiceActivity) -> str
        Set: MethodName(self: InvokeWebServiceActivity) = value
        """
        ...

    @property
    def ParameterBindings(self) -> WorkflowParameterBindingCollection:
        """ Get: ParameterBindings(self: InvokeWebServiceActivity) -> WorkflowParameterBindingCollection """
        ...

    @property
    def ProxyClass(self) -> Type:
        """
        Get: ProxyClass(self: InvokeWebServiceActivity) -> Type
        Set: ProxyClass(self: InvokeWebServiceActivity) = value
        """
        ...

    @property
    def SessionId(self) -> str:
        """
        Get: SessionId(self: InvokeWebServiceActivity) -> str
        Set: SessionId(self: InvokeWebServiceActivity) = value
        """
        ...


    Invoked = ...
    InvokedEvent: DependencyProperty = ...
    Invoking = ...
    InvokingEvent: DependencyProperty = ...
    MethodNameProperty: DependencyProperty = ...
    ParameterBindingsProperty: DependencyProperty = ...
    ProxyClassProperty: DependencyProperty = ...
    SessionIdProperty: DependencyProperty = ...


class InvokeWebServiceEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ InvokeWebServiceEventArgs(proxyInstance: object) """
    @property
    def WebServiceProxy(self) -> object:
        """ Get: WebServiceProxy(self: InvokeWebServiceEventArgs) -> object """
        ...


    def __new__(cls, proxyInstance:object) -> Self:
        """ __new__(cls: type, proxyInstance: object) """
        ...


class InvokeWorkflowActivity(Activity, ITypeFilterProvider): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    InvokeWorkflowActivity()
    InvokeWorkflowActivity(name: str)
    """
    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: InvokeWorkflowActivity) -> Guid """
        ...

    @property
    def ParameterBindings(self) -> WorkflowParameterBindingCollection:
        """ Get: ParameterBindings(self: InvokeWorkflowActivity) -> WorkflowParameterBindingCollection """
        ...

    @property
    def TargetWorkflow(self) -> Type:
        """
        Get: TargetWorkflow(self: InvokeWorkflowActivity) -> Type
        Set: TargetWorkflow(self: InvokeWorkflowActivity) = value
        """
        ...


    InstanceIdProperty: DependencyProperty = ...
    Invoking = ...
    InvokingEvent: DependencyProperty = ...
    ParameterBindingsProperty: DependencyProperty = ...
    TargetWorkflowProperty: DependencyProperty = ...


class ListenActivity(CompositeActivity, IActivityEventListener): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    ListenActivity()
    ListenActivity(name: str)
    """
    pass

class MessageEventSubscription: # skipped bases: <type 'object'>, <type 'object'>
    """
    MessageEventSubscription(queueName: IComparable, instanceId: Guid)
    MessageEventSubscription(queueName: IComparable, instanceId: Guid, subscriptionId: Guid)
    MessageEventSubscription(queueName: IComparable, subscriptionId: Guid, interfaceType: Type, operation: str)
    MessageEventSubscription(queueName: IComparable, instanceId: Guid, interfaceType: Type, operation: str, subscriptionId: Guid)
    """
    @property
    def CorrelationProperties(self) -> ICollection:
        """ Get: CorrelationProperties(self: MessageEventSubscription) -> ICollection[CorrelationProperty] """
        ...

    @property
    def InterfaceType(self) -> Type:
        """
        Get: InterfaceType(self: MessageEventSubscription) -> Type
        Set: InterfaceType(self: MessageEventSubscription) = value
        """
        ...

    @property
    def MethodName(self) -> str:
        """
        Get: MethodName(self: MessageEventSubscription) -> str
        Set: MethodName(self: MessageEventSubscription) = value
        """
        ...

    @property
    def QueueName(self) -> IComparable:
        """ Get: QueueName(self: MessageEventSubscription) -> IComparable """
        ...

    @property
    def SubscriptionId(self) -> Guid:
        """ Get: SubscriptionId(self: MessageEventSubscription) -> Guid """
        ...

    @property
    def WorkflowInstanceId(self) -> Guid:
        """ Get: WorkflowInstanceId(self: MessageEventSubscription) -> Guid """
        ...



class OperationInfoBase(DependencyObject): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: OperationInfoBase) -> str
        Set: Name(self: OperationInfoBase) = value
        """
        ...

    @property
    def PrincipalPermissionName(self) -> str:
        """
        Get: PrincipalPermissionName(self: OperationInfoBase) -> str
        Set: PrincipalPermissionName(self: OperationInfoBase) = value
        """
        ...

    @property
    def PrincipalPermissionRole(self) -> str:
        """
        Get: PrincipalPermissionRole(self: OperationInfoBase) -> str
        Set: PrincipalPermissionRole(self: OperationInfoBase) = value
        """
        ...


    def Clone(self) -> OperationInfoBase:
        """ Clone(self: OperationInfoBase) -> OperationInfoBase """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: OperationInfoBase, obj: object) -> bool """
        ...

    def GetContractFullName(self, *args): #cannot find CLR method
        """ GetContractFullName(self: OperationInfoBase, provider: IServiceProvider) -> str """
        ...

    def GetContractType(self, *args): #cannot find CLR method
        """ GetContractType(self: OperationInfoBase, provider: IServiceProvider) -> Type """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: OperationInfoBase) -> int """
        ...

    def GetIsOneWay(self, *args): #cannot find CLR method
        """ GetIsOneWay(self: OperationInfoBase, provider: IServiceProvider) -> bool """
        ...

    def GetMethodInfo(self, *args): #cannot find CLR method
        """ GetMethodInfo(self: OperationInfoBase, provider: IServiceProvider) -> MethodInfo """
        ...

    def GetParameters(self, *args): #cannot find CLR method
        """ GetParameters(self: OperationInfoBase, provider: IServiceProvider) -> OperationParameterInfoCollection """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class OperationInfo(OperationInfoBase): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """ OperationInfo() """
    @property
    def ContractName(self) -> str:
        """
        Get: ContractName(self: OperationInfo) -> str
        Set: ContractName(self: OperationInfo) = value
        """
        ...

    @property
    def HasProtectionLevel(self) -> bool:
        """ Get: HasProtectionLevel(self: OperationInfo) -> bool """
        ...

    @property
    def IsOneWay(self) -> bool:
        """
        Get: IsOneWay(self: OperationInfo) -> bool
        Set: IsOneWay(self: OperationInfo) = value
        """
        ...

    @property
    def Parameters(self) -> OperationParameterInfoCollection:
        """ Get: Parameters(self: OperationInfo) -> OperationParameterInfoCollection """
        ...

    @property
    def ProtectionLevel(self) -> Nullable:
        """
        Get: ProtectionLevel(self: OperationInfo) -> Nullable[ProtectionLevel]
        Set: ProtectionLevel(self: OperationInfo) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: OperationInfo) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class OperationParameterInfo(DependencyObject): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    OperationParameterInfo()
    OperationParameterInfo(parameterName: str)
    """
    @property
    def Attributes(self) -> ParameterAttributes:
        """
        Get: Attributes(self: OperationParameterInfo) -> ParameterAttributes
        Set: Attributes(self: OperationParameterInfo) = value
        """
        ...

    @property
    def IsIn(self) -> bool:
        """ Get: IsIn(self: OperationParameterInfo) -> bool """
        ...

    @property
    def IsLcid(self) -> bool:
        """ Get: IsLcid(self: OperationParameterInfo) -> bool """
        ...

    @property
    def IsOptional(self) -> bool:
        """ Get: IsOptional(self: OperationParameterInfo) -> bool """
        ...

    @property
    def IsOut(self) -> bool:
        """ Get: IsOut(self: OperationParameterInfo) -> bool """
        ...

    @property
    def IsRetval(self) -> bool:
        """ Get: IsRetval(self: OperationParameterInfo) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: OperationParameterInfo) -> str
        Set: Name(self: OperationParameterInfo) = value
        """
        ...

    @property
    def ParameterType(self) -> Type:
        """
        Get: ParameterType(self: OperationParameterInfo) -> Type
        Set: ParameterType(self: OperationParameterInfo) = value
        """
        ...

    @property
    def Position(self) -> int:
        """
        Get: Position(self: OperationParameterInfo) -> int
        Set: Position(self: OperationParameterInfo) = value
        """
        ...


    def Clone(self) -> OperationParameterInfo:
        """ Clone(self: OperationParameterInfo) -> OperationParameterInfo """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: OperationParameterInfo, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: OperationParameterInfo) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, parameterName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parameterName: str)
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    AttributesProperty: DependencyProperty = ...
    NameProperty: DependencyProperty = ...
    ParameterTypeProperty: DependencyProperty = ...
    PositionProperty: DependencyProperty = ...


class OperationParameterInfoCollection(List): # skipped bases: <type 'ICollection[OperationParameterInfo]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyCollection[OperationParameterInfo]'>, <type 'IList[OperationParameterInfo]'>, <type 'IReadOnlyList[OperationParameterInfo]'>, <type 'IEnumerable[OperationParameterInfo]'>, <type 'ICollection'>, <type 'object'>
    """
    OperationParameterInfoCollection()
    OperationParameterInfoCollection(owner: OperationInfoBase)
    """
    pass

class OperationValidationEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ OperationValidationEventArgs(claimSets: ReadOnlyCollection[ClaimSet]) """
    @property
    def ClaimSets(self) -> ReadOnlyCollection:
        """ Get: ClaimSets(self: OperationValidationEventArgs) -> ReadOnlyCollection[ClaimSet] """
        ...

    @property
    def IsValid(self) -> bool:
        """
        Get: IsValid(self: OperationValidationEventArgs) -> bool
        Set: IsValid(self: OperationValidationEventArgs) = value
        """
        ...


    def __new__(cls, claimSets:ReadOnlyCollection) -> Self:
        """ __new__(cls: type, claimSets: ReadOnlyCollection[ClaimSet]) """
        ...


class ParallelActivity(CompositeActivity, IActivityEventListener): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    ParallelActivity()
    ParallelActivity(name: str)
    """
    pass

class PolicyActivity(Activity): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    PolicyActivity()
    PolicyActivity(name: str)
    """
    @property
    def RuleSetReference(self) -> RuleSetReference:
        """
        Get: RuleSetReference(self: PolicyActivity) -> RuleSetReference
        Set: RuleSetReference(self: PolicyActivity) = value
        """
        ...


    RuleSetReferenceProperty: DependencyProperty = ...


class ReceiveActivity(SequenceActivity, IEventActivity, IActivityEventListener, IServiceDescriptionBuilder): # skipped bases: <type 'IActivityEventListener[ActivityExecutionStatusChangedEventArgs]'>, <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    ReceiveActivity()
    ReceiveActivity(name: str)
    """
    @property
    def CanCreateInstance(self) -> bool:
        """
        Get: CanCreateInstance(self: ReceiveActivity) -> bool
        Set: CanCreateInstance(self: ReceiveActivity) = value
        """
        ...

    @property
    def Context(self) -> IDictionary:
        """ Get: Context(self: ReceiveActivity) -> IDictionary[str, str] """
        ...

    @property
    def ContextToken(self) -> ContextToken:
        """
        Get: ContextToken(self: ReceiveActivity) -> ContextToken
        Set: ContextToken(self: ReceiveActivity) = value
        """
        ...

    @property
    def FaultMessage(self) -> FaultException:
        """
        Get: FaultMessage(self: ReceiveActivity) -> FaultException
        Set: FaultMessage(self: ReceiveActivity) = value
        """
        ...

    @property
    def ParameterBindings(self) -> WorkflowParameterBindingCollection:
        """ Get: ParameterBindings(self: ReceiveActivity) -> WorkflowParameterBindingCollection """
        ...

    @property
    def ServiceOperationInfo(self) -> OperationInfoBase:
        """
        Get: ServiceOperationInfo(self: ReceiveActivity) -> OperationInfoBase
        Set: ServiceOperationInfo(self: ReceiveActivity) = value
        """
        ...


    @staticmethod
    def GetContext(activity:Activity, *__args:ContextToken) -> IDictionary:
        """
        GetContext(activity: Activity, contextToken: ContextToken) -> IDictionary[str, str]
        GetContext(activity: Activity, contextName: str, ownerActivityName: str) -> IDictionary[str, str]
        """
        ...

    @staticmethod
    def GetRootContext(activity:Activity) -> IDictionary:
        """ GetRootContext(activity: Activity) -> IDictionary[str, str] """
        ...

    @staticmethod
    def GetWorkflowServiceAttributes(dependencyObject:object) -> object:
        """ GetWorkflowServiceAttributes(dependencyObject: object) -> object """
        ...

    @staticmethod
    def SetWorkflowServiceAttributes(dependencyObject:object, value:object): # -> 
        """ SetWorkflowServiceAttributes(dependencyObject: object, value: object) """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    FaultMessageProperty: DependencyProperty = ...
    OperationValidation = ...
    OperationValidationEvent: DependencyProperty = ...
    WorkflowServiceAttributesProperty: DependencyProperty = ...


class ReplicatorActivity(CompositeActivity): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    ReplicatorActivity()
    ReplicatorActivity(name: str)
    """
    @property
    def AllChildrenComplete(self) -> bool:
        """ Get: AllChildrenComplete(self: ReplicatorActivity) -> bool """
        ...

    @property
    def CurrentChildData(self) -> IList:
        """ Get: CurrentChildData(self: ReplicatorActivity) -> IList """
        ...

    @property
    def CurrentIndex(self) -> int:
        """ Get: CurrentIndex(self: ReplicatorActivity) -> int """
        ...

    @property
    def DynamicActivities(self) -> ICollection:
        """ Get: DynamicActivities(self: ReplicatorActivity) -> ICollection[Activity] """
        ...

    @property
    def ExecutionType(self) -> ExecutionType:
        """
        Get: ExecutionType(self: ReplicatorActivity) -> ExecutionType
        Set: ExecutionType(self: ReplicatorActivity) = value
        """
        ...

    @property
    def InitialChildData(self) -> IList:
        """
        Get: InitialChildData(self: ReplicatorActivity) -> IList
        Set: InitialChildData(self: ReplicatorActivity) = value
        """
        ...

    @property
    def UntilCondition(self) -> ActivityCondition:
        """
        Get: UntilCondition(self: ReplicatorActivity) -> ActivityCondition
        Set: UntilCondition(self: ReplicatorActivity) = value
        """
        ...


    def IsExecuting(self, index:int) -> bool:
        """ IsExecuting(self: ReplicatorActivity, index: int) -> bool """
        ...

    ChildCompleted = ...
    ChildCompletedEvent: DependencyProperty = ...
    ChildInitialized = ...
    ChildInitializedEvent: DependencyProperty = ...
    Completed = ...
    CompletedEvent: DependencyProperty = ...
    ExecutionTypeProperty: DependencyProperty = ...
    InitialChildDataProperty: DependencyProperty = ...
    Initialized = ...
    InitializedEvent: DependencyProperty = ...
    UntilConditionProperty: DependencyProperty = ...


class ReplicatorChildEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ReplicatorChildEventArgs(instanceData: object, activity: Activity) """
    @property
    def Activity(self) -> Activity:
        """ Get: Activity(self: ReplicatorChildEventArgs) -> Activity """
        ...

    @property
    def InstanceData(self) -> object:
        """ Get: InstanceData(self: ReplicatorChildEventArgs) -> object """
        ...


    def __new__(cls, instanceData:object, activity:Activity) -> Self:
        """ __new__(cls: type, instanceData: object, activity: Activity) """
        ...


class SendActivity(Activity): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    SendActivity()
    SendActivity(name: str)
    """
    @property
    def ChannelToken(self) -> ChannelToken:
        """
        Get: ChannelToken(self: SendActivity) -> ChannelToken
        Set: ChannelToken(self: SendActivity) = value
        """
        ...

    @property
    def Context(self) -> IDictionary:
        """
        Get: Context(self: SendActivity) -> IDictionary[str, str]
        Set: Context(self: SendActivity) = value
        """
        ...

    @property
    def CustomAddress(self) -> str:
        """
        Get: CustomAddress(self: SendActivity) -> str
        Set: CustomAddress(self: SendActivity) = value
        """
        ...

    @property
    def ParameterBindings(self) -> WorkflowParameterBindingCollection:
        """ Get: ParameterBindings(self: SendActivity) -> WorkflowParameterBindingCollection """
        ...

    @property
    def ServiceOperationInfo(self) -> TypedOperationInfo:
        """
        Get: ServiceOperationInfo(self: SendActivity) -> TypedOperationInfo
        Set: ServiceOperationInfo(self: SendActivity) = value
        """
        ...


    @staticmethod
    def GetContext(activity, *__args) -> IDictionary:
        """
        GetContext(activity: Activity, endpoint: ChannelToken, contractType: Type) -> IDictionary[str, str]
        GetContext(activity: Activity, endpointName: str, ownerActivityName: str, contractType: Type) -> IDictionary[str, str]
        """
        ...

    @staticmethod
    def SetContext(activity, *__args): # -> 
        """ SetContext(activity: Activity, endpoint: ChannelToken, contractType: Type, context: IDictionary[str, str])SetContext(activity: Activity, endpointName: str, ownerActivityName: str, contractType: Type, context: IDictionary[str, str]) """
        ...

    AfterResponse = ...
    AfterResponseEvent: DependencyProperty = ...
    BeforeSend = ...
    BeforeSendEvent: DependencyProperty = ...
    CustomAddressProperty: DependencyProperty = ...
    ReturnValuePropertyName: str = ...


class SendActivityEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SendActivityEventArgs(sendActivity: SendActivity) """
    @property
    def SendActivity(self) -> SendActivity:
        """ Get: SendActivity(self: SendActivityEventArgs) -> SendActivity """
        ...


    def __new__(cls, sendActivity:SendActivity) -> Self:
        """ __new__(cls: type, sendActivity: SendActivity) """
        ...


class SequentialWorkflowActivity(SequenceActivity): # skipped bases: <type 'IActivityEventListener[ActivityExecutionStatusChangedEventArgs]'>, <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    SequentialWorkflowActivity()
    SequentialWorkflowActivity(name: str)
    """
    @property
    def DynamicUpdateCondition(self) -> ActivityCondition:
        """
        Get: DynamicUpdateCondition(self: SequentialWorkflowActivity) -> ActivityCondition
        Set: DynamicUpdateCondition(self: SequentialWorkflowActivity) = value
        """
        ...


    Completed = ...
    CompletedEvent: DependencyProperty = ...
    Initialized = ...
    InitializedEvent: DependencyProperty = ...


class SetStateActivity(Activity): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    SetStateActivity()
    SetStateActivity(name: str)
    """
    @property
    def TargetStateName(self) -> str:
        """
        Get: TargetStateName(self: SetStateActivity) -> str
        Set: TargetStateName(self: SetStateActivity) = value
        """
        ...


    TargetStateNameProperty: DependencyProperty = ...


class SetStateEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SetStateEventArgs(targetStateName: str) """
    @property
    def TargetStateName(self) -> str:
        """ Get: TargetStateName(self: SetStateEventArgs) -> str """
        ...


    def __new__(cls, targetStateName:str) -> Self:
        """ __new__(cls: type, targetStateName: str) """
        ...


class StateActivity(CompositeActivity): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    StateActivity()
    StateActivity(name: str)
    """
    def GetDynamicActivity(self, childActivityName:str) -> Activity:
        """ GetDynamicActivity(self: StateActivity, childActivityName: str) -> Activity """
        ...

    StateChangeTrackingDataKey: str = ...


class StateActivityValidator(CompositeActivityValidator): # skipped bases: <type 'object'>
    """ StateActivityValidator() """
    pass

class StateFinalizationActivity(SequenceActivity): # skipped bases: <type 'IActivityEventListener[ActivityExecutionStatusChangedEventArgs]'>, <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    StateFinalizationActivity()
    StateFinalizationActivity(name: str)
    """
    pass

class StateInitializationActivity(SequenceActivity): # skipped bases: <type 'IActivityEventListener[ActivityExecutionStatusChangedEventArgs]'>, <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    StateInitializationActivity()
    StateInitializationActivity(name: str)
    """
    pass

class StateMachineWorkflowActivity(StateActivity): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    StateMachineWorkflowActivity()
    StateMachineWorkflowActivity(name: str)
    """
    @property
    def CompletedStateName(self) -> str:
        """
        Get: CompletedStateName(self: StateMachineWorkflowActivity) -> str
        Set: CompletedStateName(self: StateMachineWorkflowActivity) = value
        """
        ...

    @property
    def CurrentStateName(self) -> str:
        """ Get: CurrentStateName(self: StateMachineWorkflowActivity) -> str """
        ...

    @property
    def DynamicUpdateCondition(self) -> ActivityCondition:
        """
        Get: DynamicUpdateCondition(self: StateMachineWorkflowActivity) -> ActivityCondition
        Set: DynamicUpdateCondition(self: StateMachineWorkflowActivity) = value
        """
        ...

    @property
    def InitialStateName(self) -> str:
        """
        Get: InitialStateName(self: StateMachineWorkflowActivity) -> str
        Set: InitialStateName(self: StateMachineWorkflowActivity) = value
        """
        ...

    @property
    def PreviousStateName(self) -> str:
        """ Get: PreviousStateName(self: StateMachineWorkflowActivity) -> str """
        ...


    CompletedStateNameProperty: DependencyProperty = ...
    InitialStateNameProperty: DependencyProperty = ...
    SetStateQueueName: str = ...


class StateMachineWorkflowInstance: # skipped bases: <type 'object'>, <type 'object'>
    """ StateMachineWorkflowInstance(runtime: WorkflowRuntime, instanceId: Guid) """
    @property
    def CurrentState(self) -> StateActivity:
        """ Get: CurrentState(self: StateMachineWorkflowInstance) -> StateActivity """
        ...

    @property
    def CurrentStateName(self) -> str:
        """ Get: CurrentStateName(self: StateMachineWorkflowInstance) -> str """
        ...

    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: StateMachineWorkflowInstance) -> Guid """
        ...

    @property
    def PossibleStateTransitions(self) -> ReadOnlyCollection:
        """ Get: PossibleStateTransitions(self: StateMachineWorkflowInstance) -> ReadOnlyCollection[str] """
        ...

    @property
    def StateHistory(self) -> ReadOnlyCollection:
        """ Get: StateHistory(self: StateMachineWorkflowInstance) -> ReadOnlyCollection[str] """
        ...

    @property
    def StateMachineWorkflow(self) -> StateMachineWorkflowActivity:
        """ Get: StateMachineWorkflow(self: StateMachineWorkflowInstance) -> StateMachineWorkflowActivity """
        ...

    @property
    def States(self) -> ReadOnlyCollection:
        """ Get: States(self: StateMachineWorkflowInstance) -> ReadOnlyCollection[StateActivity] """
        ...

    @property
    def WorkflowInstance(self) -> WorkflowInstance:
        """ Get: WorkflowInstance(self: StateMachineWorkflowInstance) -> WorkflowInstance """
        ...


    def EnqueueItem(self, queueName:IComparable, item:object, pendingWork = ..., workItem:object = ...): # ->  # Not found arg types: {'pendingWork': 'IPendingWork'}
        """ EnqueueItem(self: StateMachineWorkflowInstance, queueName: IComparable, item: object)EnqueueItem(self: StateMachineWorkflowInstance, queueName: IComparable, item: object, pendingWork: IPendingWork, workItem: object) """
        ...

    def SetState(self, *__args:StateActivity): # -> 
        """ SetState(self: StateMachineWorkflowInstance, targetState: StateActivity)SetState(self: StateMachineWorkflowInstance, targetStateName: str) """
        ...


class TypedOperationInfo(OperationInfoBase): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    TypedOperationInfo()
    TypedOperationInfo(contractType: Type, operationName: str)
    """
    @property
    def ContractType(self) -> Type:
        """
        Get: ContractType(self: TypedOperationInfo) -> Type
        Set: ContractType(self: TypedOperationInfo) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: TypedOperationInfo) -> str """
        ...

    def __new__(cls, contractType:Type = ..., operationName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, contractType: Type, operationName: str)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class WebServiceFaultActivity(IPropertyValueProvider, Activity): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    WebServiceFaultActivity()
    WebServiceFaultActivity(name: str)
    """
    @property
    def Fault(self) -> Exception:
        """
        Get: Fault(self: WebServiceFaultActivity) -> Exception
        Set: Fault(self: WebServiceFaultActivity) = value
        """
        ...

    @property
    def InputActivityName(self) -> str:
        """
        Get: InputActivityName(self: WebServiceFaultActivity) -> str
        Set: InputActivityName(self: WebServiceFaultActivity) = value
        """
        ...


    FaultProperty: DependencyProperty = ...
    InputActivityNameProperty: DependencyProperty = ...
    SendingFault = ...
    SendingFaultEvent: DependencyProperty = ...


class WebServiceInputActivity(IPropertyValueProvider, IEventActivity, IDynamicPropertyTypeProvider, IActivityEventListener, Activity): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    WebServiceInputActivity()
    WebServiceInputActivity(name: str)
    """
    @property
    def InterfaceType(self) -> Type:
        """
        Get: InterfaceType(self: WebServiceInputActivity) -> Type
        Set: InterfaceType(self: WebServiceInputActivity) = value
        """
        ...

    @property
    def IsActivating(self) -> bool:
        """
        Get: IsActivating(self: WebServiceInputActivity) -> bool
        Set: IsActivating(self: WebServiceInputActivity) = value
        """
        ...

    @property
    def MethodName(self) -> str:
        """
        Get: MethodName(self: WebServiceInputActivity) -> str
        Set: MethodName(self: WebServiceInputActivity) = value
        """
        ...

    @property
    def ParameterBindings(self) -> WorkflowParameterBindingCollection:
        """ Get: ParameterBindings(self: WebServiceInputActivity) -> WorkflowParameterBindingCollection """
        ...

    @property
    def Roles(self): # -> WorkflowRoleCollection
        """
        Get: Roles(self: WebServiceInputActivity) -> WorkflowRoleCollection
        Set: Roles(self: WebServiceInputActivity) = value
        """
        ...


    ActivitySubscribedProperty: DependencyProperty = ...
    InputReceived = ...
    InputReceivedEvent: DependencyProperty = ...
    InterfaceTypeProperty: DependencyProperty = ...
    IsActivatingProperty: DependencyProperty = ...
    MethodNameProperty: DependencyProperty = ...
    ParameterBindingsProperty: DependencyProperty = ...
    RolesProperty: DependencyProperty = ...


class WebServiceOutputActivity(IPropertyValueProvider, IDynamicPropertyTypeProvider, Activity): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    WebServiceOutputActivity()
    WebServiceOutputActivity(name: str)
    """
    @property
    def InputActivityName(self) -> str:
        """
        Get: InputActivityName(self: WebServiceOutputActivity) -> str
        Set: InputActivityName(self: WebServiceOutputActivity) = value
        """
        ...

    @property
    def ParameterBindings(self) -> WorkflowParameterBindingCollection:
        """ Get: ParameterBindings(self: WebServiceOutputActivity) -> WorkflowParameterBindingCollection """
        ...


    InputActivityNameProperty: DependencyProperty = ...
    ParameterBindingsProperty: DependencyProperty = ...
    SendingOutput = ...
    SendingOutputEvent: DependencyProperty = ...


class WebWorkflowRole(WorkflowRole): # skipped bases: <type 'object'>
    """
    WebWorkflowRole(roleName: str)
    WebWorkflowRole(roleName: str, provider: str)
    """
    @property
    def RoleProvider(self) -> str:
        """
        Get: RoleProvider(self: WebWorkflowRole) -> str
        Set: RoleProvider(self: WebWorkflowRole) = value
        """
        ...


    def __new__(cls, roleName:str, provider:str = ...) -> Self:
        """
        __new__(cls: type, roleName: str)
        __new__(cls: type, roleName: str, provider: str)
        """
        ...


class WhileActivity(CompositeActivity, IActivityEventListener): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    WhileActivity()
    WhileActivity(name: str)
    """
    @property
    def Condition(self) -> ActivityCondition:
        """
        Get: Condition(self: WhileActivity) -> ActivityCondition
        Set: Condition(self: WhileActivity) = value
        """
        ...

    @property
    def DynamicActivity(self) -> Activity:
        """ Get: DynamicActivity(self: WhileActivity) -> Activity """
        ...


    ConditionProperty: DependencyProperty = ...


class WorkflowAuthorizationException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WorkflowAuthorizationException()
    WorkflowAuthorizationException(activityName: str, principalName: str)
    WorkflowAuthorizationException(message: str)
    WorkflowAuthorizationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class WorkflowRoleCollection(List): # skipped bases: <type 'IEnumerable[WorkflowRole]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[WorkflowRole]'>, <type 'IReadOnlyCollection[WorkflowRole]'>, <type 'IList[WorkflowRole]'>, <type 'IReadOnlyList[WorkflowRole]'>, <type 'ICollection'>, <type 'object'>
    """ WorkflowRoleCollection() """
    def IncludesIdentity(self, identity:str) -> bool:
        """ IncludesIdentity(self: WorkflowRoleCollection, identity: str) -> bool """
        ...


class WorkflowServiceAttributes(DependencyObject, IServiceDescriptionBuilder): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """ WorkflowServiceAttributes() """
    @property
    def AddressFilterMode(self) -> AddressFilterMode:
        """
        Get: AddressFilterMode(self: WorkflowServiceAttributes) -> AddressFilterMode
        Set: AddressFilterMode(self: WorkflowServiceAttributes) = value
        """
        ...

    @property
    def ConfigurationName(self) -> str:
        """
        Get: ConfigurationName(self: WorkflowServiceAttributes) -> str
        Set: ConfigurationName(self: WorkflowServiceAttributes) = value
        """
        ...

    @property
    def IgnoreExtensionDataObject(self) -> bool:
        """
        Get: IgnoreExtensionDataObject(self: WorkflowServiceAttributes) -> bool
        Set: IgnoreExtensionDataObject(self: WorkflowServiceAttributes) = value
        """
        ...

    @property
    def IncludeExceptionDetailInFaults(self) -> bool:
        """
        Get: IncludeExceptionDetailInFaults(self: WorkflowServiceAttributes) -> bool
        Set: IncludeExceptionDetailInFaults(self: WorkflowServiceAttributes) = value
        """
        ...

    @property
    def MaxItemsInObjectGraph(self) -> int:
        """
        Get: MaxItemsInObjectGraph(self: WorkflowServiceAttributes) -> int
        Set: MaxItemsInObjectGraph(self: WorkflowServiceAttributes) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: WorkflowServiceAttributes) -> str
        Set: Name(self: WorkflowServiceAttributes) = value
        """
        ...

    @property
    def Namespace(self) -> str:
        """
        Get: Namespace(self: WorkflowServiceAttributes) -> str
        Set: Namespace(self: WorkflowServiceAttributes) = value
        """
        ...

    @property
    def UseSynchronizationContext(self) -> bool:
        """
        Get: UseSynchronizationContext(self: WorkflowServiceAttributes) -> bool
        Set: UseSynchronizationContext(self: WorkflowServiceAttributes) = value
        """
        ...

    @property
    def ValidateMustUnderstand(self) -> bool:
        """
        Get: ValidateMustUnderstand(self: WorkflowServiceAttributes) -> bool
        Set: ValidateMustUnderstand(self: WorkflowServiceAttributes) = value
        """
        ...



class WorkflowServiceAttributesDynamicPropertyValidator(Validator): # skipped bases: <type 'object'>
    """ WorkflowServiceAttributesDynamicPropertyValidator() """
    pass

class WorkflowSubscriptionService: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateSubscription(self, subscription:MessageEventSubscription): # -> 
        """ CreateSubscription(self: WorkflowSubscriptionService, subscription: MessageEventSubscription) """
        ...

    def DeleteSubscription(self, subscriptionId:Guid): # -> 
        """ DeleteSubscription(self: WorkflowSubscriptionService, subscriptionId: Guid) """
        ...


class WorkflowWebService(WebService): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IServiceProvider'>, <type 'object'>
    """ no doc """
    @property
    def WorkflowRuntime(self):
        ...


    def Invoke(self, *args): #cannot find CLR method
        """ Invoke(self: WorkflowWebService, interfaceType: Type, methodName: str, isActivation: bool, parameters: Array[object]) -> Array[object] """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, workflowType: Type) """
        ...


# variables with complex values

