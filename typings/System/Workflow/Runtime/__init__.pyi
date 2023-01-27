# encoding: utf-8
# module System.Workflow.Runtime calls itself Runtime
# from System.WorkflowServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Workflow.Runtime, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (DateTime, Enum, EventArgs, Guid, IComparable, IDisposable, 
    IServiceProvider, Type)

from System.Activities.Hosting import WorkflowInstance

from System.Collections import ICollection, IEnumerator

from System.Collections.Generic import Dictionary

from System.Collections.ObjectModel import (KeyedCollection, 
    ReadOnlyCollection)

from System.EnterpriseServices import Activity

from System.Transactions import Transaction

from System.Workflow.ComponentModel import (DependencyObject, 
    DependencyProperty, IActivityEventListener, WorkflowChanges)

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    IPropertyValueProvider, WorkflowQueuingService, WorkflowRuntime, field#)
"""

# no functions
# classes

class CorrelationProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ CorrelationProperty(name: str, value: object) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: CorrelationProperty) -> str """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: CorrelationProperty) -> object """
        ...



class CorrelationToken(DependencyObject, IPropertyValueProvider): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    CorrelationToken()
    CorrelationToken(name: str)
    """
    @property
    def Initialized(self) -> bool:
        """ Get: Initialized(self: CorrelationToken) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CorrelationToken) -> str
        Set: Name(self: CorrelationToken) = value
        """
        ...

    @property
    def OwnerActivityName(self) -> str:
        """
        Get: OwnerActivityName(self: CorrelationToken) -> str
        Set: OwnerActivityName(self: CorrelationToken) = value
        """
        ...

    @property
    def Properties(self) -> ICollection:
        """ Get: Properties(self: CorrelationToken) -> ICollection[CorrelationProperty] """
        ...


    def Initialize(self, activity:Activity, propertyValues:ICollection): # -> 
        """ Initialize(self: CorrelationToken, activity: Activity, propertyValues: ICollection[CorrelationProperty]) """
        ...

    def SubscribeForCorrelationTokenInitializedEvent(self, activity:Activity, dataChangeListener:IActivityEventListener): # -> 
        """ SubscribeForCorrelationTokenInitializedEvent(self: CorrelationToken, activity: Activity, dataChangeListener: IActivityEventListener[CorrelationTokenEventArgs]) """
        ...

    def UnsubscribeFromCorrelationTokenInitializedEvent(self, activity:Activity, dataChangeListener:IActivityEventListener): # -> 
        """ UnsubscribeFromCorrelationTokenInitializedEvent(self: CorrelationToken, activity: Activity, dataChangeListener: IActivityEventListener[CorrelationTokenEventArgs]) """
        ...

    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...


class CorrelationTokenCollection(KeyedCollection): # skipped bases: <type 'IList[CorrelationToken]'>, <type 'ICollection[CorrelationToken]'>, <type 'IList'>, <type 'IReadOnlyList[CorrelationToken]'>, <type 'IEnumerable[CorrelationToken]'>, <type 'IEnumerable'>, <type 'IReadOnlyCollection[CorrelationToken]'>, <type 'ICollection'>, <type 'object'>
    """ CorrelationTokenCollection() """
    @staticmethod
    def GetCorrelationToken(activity:Activity, correlationTokenName:str, ownerActivityName:str) -> CorrelationToken:
        """ GetCorrelationToken(activity: Activity, correlationTokenName: str, ownerActivityName: str) -> CorrelationToken """
        ...

    def GetItem(self, key:str) -> CorrelationToken:
        """ GetItem(self: CorrelationTokenCollection, key: str) -> CorrelationToken """
        ...

    CorrelationTokenCollectionProperty: DependencyProperty = ...


class CorrelationTokenEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CorrelationToken(self) -> CorrelationToken:
        """ Get: CorrelationToken(self: CorrelationTokenEventArgs) -> CorrelationToken """
        ...

    @property
    def IsInitializing(self) -> bool:
        """ Get: IsInitializing(self: CorrelationTokenEventArgs) -> bool """
        ...



class IPendingWork: # skipped bases: <type 'object'>
    """ no doc """
    def Commit(self, transaction:Transaction, items:ICollection): # -> 
        """ Commit(self: IPendingWork, transaction: Transaction, items: ICollection) """
        ...

    def Complete(self, succeeded:bool, items:ICollection): # -> 
        """ Complete(self: IPendingWork, succeeded: bool, items: ICollection) """
        ...

    def MustCommit(self, items:ICollection) -> bool:
        """ MustCommit(self: IPendingWork, items: ICollection) -> bool """
        ...


class IWorkBatch: # skipped bases: <type 'object'>
    """ no doc """
    def Add(self, work:IPendingWork, workItem:object): # -> 
        """ Add(self: IWorkBatch, work: IPendingWork, workItem: object) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class ServicesExceptionNotHandledEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: ServicesExceptionNotHandledEventArgs) -> Exception """
        ...

    @property
    def WorkflowInstanceId(self) -> Guid:
        """ Get: WorkflowInstanceId(self: ServicesExceptionNotHandledEventArgs) -> Guid """
        ...



class TimerEventSubscription: # skipped bases: <type 'object'>, <type 'object'>
    """
    TimerEventSubscription(workflowInstanceId: Guid, expiresAt: DateTime)
    TimerEventSubscription(timerId: Guid, workflowInstanceId: Guid, expiresAt: DateTime)
    """
    @property
    def ExpiresAt(self) -> DateTime:
        """ Get: ExpiresAt(self: TimerEventSubscription) -> DateTime """
        ...

    @property
    def QueueName(self) -> IComparable:
        """ Get: QueueName(self: TimerEventSubscription) -> IComparable """
        ...

    @property
    def SubscriptionId(self) -> Guid:
        """ Get: SubscriptionId(self: TimerEventSubscription) -> Guid """
        ...

    @property
    def WorkflowInstanceId(self) -> Guid:
        """ Get: WorkflowInstanceId(self: TimerEventSubscription) -> Guid """
        ...



class TimerEventSubscriptionCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Add(self, item:TimerEventSubscription): # -> 
        """ Add(self: TimerEventSubscriptionCollection, item: TimerEventSubscription) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: TimerEventSubscriptionCollection) -> IEnumerator """
        ...

    def Peek(self) -> TimerEventSubscription:
        """ Peek(self: TimerEventSubscriptionCollection) -> TimerEventSubscription """
        ...

    def Remove(self, *__args:Guid): # -> 
        """ Remove(self: TimerEventSubscriptionCollection, timerSubscriptionId: Guid)Remove(self: TimerEventSubscriptionCollection, item: TimerEventSubscription) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    TimerCollectionProperty: DependencyProperty = ...


class WorkflowEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def WorkflowInstance(self) -> WorkflowInstance:
        """ Get: WorkflowInstance(self: WorkflowEventArgs) -> WorkflowInstance """
        ...



class WorkflowCompletedEventArgs(WorkflowEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def OutputParameters(self) -> Dictionary:
        """ Get: OutputParameters(self: WorkflowCompletedEventArgs) -> Dictionary[str, object] """
        ...

    @property
    def WorkflowDefinition(self) -> Activity:
        """ Get: WorkflowDefinition(self: WorkflowCompletedEventArgs) -> Activity """
        ...



class WorkflowEnvironment: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def WorkBatch(self) -> IWorkBatch:
        """ Get: WorkBatch() -> IWorkBatch """
        ...

    @property
    def WorkflowInstanceId(self) -> Guid:
        """ Get: WorkflowInstanceId() -> Guid """
        ...


    __all__: list = ...


class WorkflowInstance: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: WorkflowInstance) -> Guid """
        ...

    @property
    def WorkflowRuntime(self): # -> WorkflowRuntime
        """ Get: WorkflowRuntime(self: WorkflowInstance) -> WorkflowRuntime """
        ...


    def Abort(self): # -> 
        """ Abort(self: WorkflowInstance) """
        ...

    def ApplyWorkflowChanges(self, workflowChanges:WorkflowChanges): # -> 
        """ ApplyWorkflowChanges(self: WorkflowInstance, workflowChanges: WorkflowChanges) """
        ...

    def EnqueueItem(self, queueName:IComparable, item:object, pendingWork:IPendingWork, workItem:object): # -> 
        """ EnqueueItem(self: WorkflowInstance, queueName: IComparable, item: object, pendingWork: IPendingWork, workItem: object) """
        ...

    def EnqueueItemOnIdle(self, queueName:IComparable, item:object, pendingWork:IPendingWork, workItem:object): # -> 
        """ EnqueueItemOnIdle(self: WorkflowInstance, queueName: IComparable, item: object, pendingWork: IPendingWork, workItem: object) """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: WorkflowInstance, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: WorkflowInstance) -> int """
        ...

    def GetWorkflowDefinition(self) -> Activity:
        """ GetWorkflowDefinition(self: WorkflowInstance) -> Activity """
        ...

    def GetWorkflowNextTimerExpiration(self) -> DateTime:
        """ GetWorkflowNextTimerExpiration(self: WorkflowInstance) -> DateTime """
        ...

    def GetWorkflowQueueData(self) -> ReadOnlyCollection:
        """ GetWorkflowQueueData(self: WorkflowInstance) -> ReadOnlyCollection[WorkflowQueueInfo] """
        ...

    def Load(self): # -> 
        """ Load(self: WorkflowInstance) """
        ...

    def ReloadTrackingProfiles(self): # -> 
        """ ReloadTrackingProfiles(self: WorkflowInstance) """
        ...

    def Resume(self): # -> 
        """ Resume(self: WorkflowInstance) """
        ...

    def Start(self): # -> 
        """ Start(self: WorkflowInstance) """
        ...

    def Suspend(self, error:str): # -> 
        """ Suspend(self: WorkflowInstance, error: str) """
        ...

    def Terminate(self, error:str): # -> 
        """ Terminate(self: WorkflowInstance, error: str) """
        ...

    def TryUnload(self) -> bool:
        """ TryUnload(self: WorkflowInstance) -> bool """
        ...

    def Unload(self): # -> 
        """ Unload(self: WorkflowInstance) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class WorkflowOwnershipException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WorkflowOwnershipException()
    WorkflowOwnershipException(message: str)
    WorkflowOwnershipException(message: str, innerException: Exception)
    WorkflowOwnershipException(instanceId: Guid)
    WorkflowOwnershipException(instanceId: Guid, message: str)
    WorkflowOwnershipException(instanceId: Guid, message: str, innerException: Exception)
    """
    @property
    def InstanceId(self) -> Guid:
        """
        Get: InstanceId(self: WorkflowOwnershipException) -> Guid
        Set: InstanceId(self: WorkflowOwnershipException) = value
        """
        ...


    SerializeObjectState = ...


class WorkflowQueue: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: WorkflowQueue) -> int """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: WorkflowQueue) -> bool
        Set: Enabled(self: WorkflowQueue) = value
        """
        ...

    @property
    def QueueName(self) -> IComparable:
        """ Get: QueueName(self: WorkflowQueue) -> IComparable """
        ...

    @property
    def QueuingService(self): # -> WorkflowQueuingService
        """ Get: QueuingService(self: WorkflowQueue) -> WorkflowQueuingService """
        ...


    def Dequeue(self) -> object:
        """ Dequeue(self: WorkflowQueue) -> object """
        ...

    def Enqueue(self, item:object): # -> 
        """ Enqueue(self: WorkflowQueue, item: object) """
        ...

    def Peek(self) -> object:
        """ Peek(self: WorkflowQueue) -> object """
        ...

    def RegisterForQueueItemArrived(self, eventListener:IActivityEventListener): # -> 
        """ RegisterForQueueItemArrived(self: WorkflowQueue, eventListener: IActivityEventListener[QueueEventArgs]) """
        ...

    def RegisterForQueueItemAvailable(self, eventListener:IActivityEventListener, subscriberQualifiedName:str = ...): # -> 
        """ RegisterForQueueItemAvailable(self: WorkflowQueue, eventListener: IActivityEventListener[QueueEventArgs])RegisterForQueueItemAvailable(self: WorkflowQueue, eventListener: IActivityEventListener[QueueEventArgs], subscriberQualifiedName: str) """
        ...

    def UnregisterForQueueItemArrived(self, eventListener:IActivityEventListener): # -> 
        """ UnregisterForQueueItemArrived(self: WorkflowQueue, eventListener: IActivityEventListener[QueueEventArgs]) """
        ...

    def UnregisterForQueueItemAvailable(self, eventListener:IActivityEventListener): # -> 
        """ UnregisterForQueueItemAvailable(self: WorkflowQueue, eventListener: IActivityEventListener[QueueEventArgs]) """
        ...

    QueueItemArrived = ...
    QueueItemAvailable = ...


class WorkflowQueueInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Items(self) -> ICollection:
        """ Get: Items(self: WorkflowQueueInfo) -> ICollection """
        ...

    @property
    def QueueName(self) -> IComparable:
        """ Get: QueueName(self: WorkflowQueueInfo) -> IComparable """
        ...

    @property
    def SubscribedActivityNames(self) -> ReadOnlyCollection:
        """ Get: SubscribedActivityNames(self: WorkflowQueueInfo) -> ReadOnlyCollection[str] """
        ...



class WorkflowQueuingService: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateWorkflowQueue(self, queueName:IComparable, transactional:bool) -> WorkflowQueue:
        """ CreateWorkflowQueue(self: WorkflowQueuingService, queueName: IComparable, transactional: bool) -> WorkflowQueue """
        ...

    def DeleteWorkflowQueue(self, queueName:IComparable): # -> 
        """ DeleteWorkflowQueue(self: WorkflowQueuingService, queueName: IComparable) """
        ...

    def Exists(self, queueName:IComparable) -> bool:
        """ Exists(self: WorkflowQueuingService, queueName: IComparable) -> bool """
        ...

    def GetWorkflowQueue(self, queueName:IComparable) -> WorkflowQueue:
        """ GetWorkflowQueue(self: WorkflowQueuingService, queueName: IComparable) -> WorkflowQueue """
        ...

    PendingMessagesProperty: DependencyProperty = ...


class WorkflowRuntime(IServiceProvider, IDisposable): # skipped bases: <type 'object'>
    """
    WorkflowRuntime()
    WorkflowRuntime(configSectionName: str)
    WorkflowRuntime(settings: WorkflowRuntimeSection)
    """
    @property
    def IsStarted(self) -> bool:
        """ Get: IsStarted(self: WorkflowRuntime) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: WorkflowRuntime) -> str
        Set: Name(self: WorkflowRuntime) = value
        """
        ...


    def AddService(self, service:object): # -> 
        """ AddService(self: WorkflowRuntime, service: object) """
        ...

    def CreateWorkflow(self, *__args:Type) -> WorkflowInstance:
        """
        CreateWorkflow(self: WorkflowRuntime, workflowType: Type) -> WorkflowInstance
        CreateWorkflow(self: WorkflowRuntime, workflowType: Type, namedArgumentValues: Dictionary[str, object]) -> WorkflowInstance
        CreateWorkflow(self: WorkflowRuntime, workflowDefinitionReader: XmlReader) -> WorkflowInstance
        CreateWorkflow(self: WorkflowRuntime, workflowDefinitionReader: XmlReader, rulesReader: XmlReader, namedArgumentValues: Dictionary[str, object]) -> WorkflowInstance
        CreateWorkflow(self: WorkflowRuntime, workflowType: Type, namedArgumentValues: Dictionary[str, object], instanceId: Guid) -> WorkflowInstance
        CreateWorkflow(self: WorkflowRuntime, workflowDefinitionReader: XmlReader, rulesReader: XmlReader, namedArgumentValues: Dictionary[str, object], instanceId: Guid) -> WorkflowInstance
        """
        ...

    def GetAllServices(self, serviceType:Type = ...) -> ReadOnlyCollection:
        """
        GetAllServices(self: WorkflowRuntime, serviceType: Type) -> ReadOnlyCollection[object]
        GetAllServices[T](self: WorkflowRuntime) -> ReadOnlyCollection[T]
        """
        ...

    def GetLoadedWorkflows(self) -> ReadOnlyCollection:
        """ GetLoadedWorkflows(self: WorkflowRuntime) -> ReadOnlyCollection[WorkflowInstance] """
        ...

    def GetWorkflow(self, instanceId:Guid) -> WorkflowInstance:
        """ GetWorkflow(self: WorkflowRuntime, instanceId: Guid) -> WorkflowInstance """
        ...

    def RemoveService(self, service:object): # -> 
        """ RemoveService(self: WorkflowRuntime, service: object) """
        ...

    def StartRuntime(self): # -> 
        """ StartRuntime(self: WorkflowRuntime) """
        ...

    def StopRuntime(self): # -> 
        """ StopRuntime(self: WorkflowRuntime) """
        ...

    ServicesExceptionNotHandled = ...
    Started = ...
    Stopped = ...
    WorkflowAborted = ...
    WorkflowCompleted = ...
    WorkflowCreated = ...
    WorkflowIdled = ...
    WorkflowLoaded = ...
    WorkflowPersisted = ...
    WorkflowResumed = ...
    WorkflowStarted = ...
    WorkflowSuspended = ...
    WorkflowTerminated = ...
    WorkflowUnloaded = ...


class WorkflowRuntimeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsStarted(self) -> bool:
        """ Get: IsStarted(self: WorkflowRuntimeEventArgs) -> bool """
        ...



class WorkflowStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WorkflowStatus, values: Completed (1), Created (4), Running (0), Suspended (2), Terminated (3) """
    Completed: WorkflowStatus = ...
    Created: WorkflowStatus = ...
    Running: WorkflowStatus = ...
    Suspended: WorkflowStatus = ...
    Terminated: WorkflowStatus = ...
    value__ = ...


class WorkflowSuspendedEventArgs(WorkflowEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Error(self) -> str:
        """ Get: Error(self: WorkflowSuspendedEventArgs) -> str """
        ...



class WorkflowTerminatedEventArgs(WorkflowEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: WorkflowTerminatedEventArgs) -> Exception """
        ...



# variables with complex values

