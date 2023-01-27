# encoding: utf-8
# module System.Workflow.ComponentModel calls itself ComponentModel
# from System.Workflow.ComponentModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Attribute, Enum, EventArgs, Guid, 
    IAsyncResult, IComparable, IDisposable, IServiceProvider, 
    MulticastDelegate, TimeSpan, Type)

from System.Collections import ICollection, IDictionary, IEnumerable, IList

from System.Collections.Generic import Dictionary, List

from System.Collections.ObjectModel import (KeyedCollection, 
    ReadOnlyCollection)

from System.ComponentModel import IComponent

from System.Data import IsolationLevel

from System.IO import Stream

from System.Runtime.Serialization import IFormatter, ISerializable

from System.Windows.Markup import MarkupExtension

from System.Workflow.ComponentModel.Compiler import (AccessTypes, 
    ValidationErrorCollection)

from System.Workflow.ComponentModel.Design import ITypeFilterProvider

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    IDependencyObjectAccessor, IPropertyValueProvider, ISupportAlternateFlow, 
    T, field#)
"""

# no functions
# classes

class DependencyObject(IDependencyObjectAccessor, IComponent): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def DesignMode(self):
        ...

    @property
    def ParentDependencyObject(self):
        ...

    @property
    def UserData(self) -> IDictionary:
        """ Get: UserData(self: DependencyObject) -> IDictionary """
        ...


    def AddHandler(self, dependencyEvent:DependencyProperty, value:object): # -> 
        """ AddHandler(self: DependencyObject, dependencyEvent: DependencyProperty, value: object) """
        ...

    def Dispose(self): # -> 
        """ Dispose(self: DependencyObject) """
        ...

    def GetBinding(self, dependencyProperty:DependencyProperty) -> ActivityBind:
        """ GetBinding(self: DependencyObject, dependencyProperty: DependencyProperty) -> ActivityBind """
        ...

    def GetBoundValue(self, *args): #cannot find CLR method
        """ GetBoundValue(self: DependencyObject, bind: ActivityBind, targetType: Type) -> object """
        ...

    def GetInvocationList(self, *args): #cannot find CLR method
        """ GetInvocationList[T](self: DependencyObject, dependencyEvent: DependencyProperty) -> Array[T] """
        ...

    def GetValue(self, dependencyProperty:DependencyProperty) -> object:
        """ GetValue(self: DependencyObject, dependencyProperty: DependencyProperty) -> object """
        ...

    def GetValueBase(self, dependencyProperty:DependencyProperty) -> object:
        """ GetValueBase(self: DependencyObject, dependencyProperty: DependencyProperty) -> object """
        ...

    def InitializeProperties(self, *args): #cannot find CLR method
        """ InitializeProperties(self: DependencyObject) """
        ...

    def IsBindingSet(self, dependencyProperty:DependencyProperty) -> bool:
        """ IsBindingSet(self: DependencyObject, dependencyProperty: DependencyProperty) -> bool """
        ...

    def MetaEquals(self, dependencyObject:DependencyObject) -> bool:
        """ MetaEquals(self: DependencyObject, dependencyObject: DependencyObject) -> bool """
        ...

    def RemoveHandler(self, dependencyEvent:DependencyProperty, value:object): # -> 
        """ RemoveHandler(self: DependencyObject, dependencyEvent: DependencyProperty, value: object) """
        ...

    def RemoveProperty(self, dependencyProperty:DependencyProperty) -> bool:
        """ RemoveProperty(self: DependencyObject, dependencyProperty: DependencyProperty) -> bool """
        ...

    def SetBinding(self, dependencyProperty:DependencyProperty, bind:ActivityBind): # -> 
        """ SetBinding(self: DependencyObject, dependencyProperty: DependencyProperty, bind: ActivityBind) """
        ...

    def SetBoundValue(self, *args): #cannot find CLR method
        """ SetBoundValue(self: DependencyObject, bind: ActivityBind, value: object) """
        ...

    def SetReadOnlyPropertyValue(self, *args): #cannot find CLR method
        """ SetReadOnlyPropertyValue(self: DependencyObject, dependencyProperty: DependencyProperty, value: object) """
        ...

    def SetValue(self, dependencyProperty:DependencyProperty, value:object): # -> 
        """ SetValue(self: DependencyObject, dependencyProperty: DependencyProperty, value: object) """
        ...

    def SetValueBase(self, dependencyProperty:DependencyProperty, value:object): # -> 
        """ SetValueBase(self: DependencyObject, dependencyProperty: DependencyProperty, value: object) """
        ...


class Activity(DependencyObject): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    Activity()
    Activity(name: str)
    """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: Activity) -> str
        Set: Description(self: Activity) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: Activity) -> bool
        Set: Enabled(self: Activity) = value
        """
        ...

    @property
    def ExecutionResult(self) -> ActivityExecutionResult:
        """ Get: ExecutionResult(self: Activity) -> ActivityExecutionResult """
        ...

    @property
    def ExecutionStatus(self) -> ActivityExecutionStatus:
        """ Get: ExecutionStatus(self: Activity) -> ActivityExecutionStatus """
        ...

    @property
    def IsDynamicActivity(self) -> bool:
        """ Get: IsDynamicActivity(self: Activity) -> bool """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Activity) -> str
        Set: Name(self: Activity) = value
        """
        ...

    @property
    def Parent(self) -> CompositeActivity:
        """ Get: Parent(self: Activity) -> CompositeActivity """
        ...

    @property
    def QualifiedName(self) -> str:
        """ Get: QualifiedName(self: Activity) -> str """
        ...

    @property
    def WorkflowInstanceId(self):
        ...


    def Cancel(self, *args): #cannot find CLR method
        """ Cancel(self: Activity, executionContext: ActivityExecutionContext) -> ActivityExecutionStatus """
        ...

    def Clone(self) -> Activity:
        """ Clone(self: Activity) -> Activity """
        ...

    def Execute(self, *args): #cannot find CLR method
        """ Execute(self: Activity, executionContext: ActivityExecutionContext) -> ActivityExecutionStatus """
        ...

    def GetActivityByName(self, activityQualifiedName:str, withinThisActivityOnly:bool = ...) -> Activity:
        """
        GetActivityByName(self: Activity, activityQualifiedName: str) -> Activity
        GetActivityByName(self: Activity, activityQualifiedName: str, withinThisActivityOnly: bool) -> Activity
        """
        ...

    def HandleFault(self, *args): #cannot find CLR method
        """ HandleFault(self: Activity, executionContext: ActivityExecutionContext, exception: Exception) -> ActivityExecutionStatus """
        ...

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: Activity, provider: IServiceProvider) """
        ...

    def Invoke(self, *args): #cannot find CLR method
        """ Invoke[T](self: Activity, handler: EventHandler[T], e: T)Invoke[T](self: Activity, eventListener: IActivityEventListener[T], e: T) """
        ...

    @staticmethod
    def Load(stream:Stream, outerActivity:Activity, formatter:IFormatter = ...) -> Activity:
        """
        Load(stream: Stream, outerActivity: Activity) -> Activity
        Load(stream: Stream, outerActivity: Activity, formatter: IFormatter) -> Activity
        """
        ...

    def OnActivityExecutionContextLoad(self, *args): #cannot find CLR method
        """ OnActivityExecutionContextLoad(self: Activity, provider: IServiceProvider) """
        ...

    def OnActivityExecutionContextUnload(self, *args): #cannot find CLR method
        """ OnActivityExecutionContextUnload(self: Activity, provider: IServiceProvider) """
        ...

    def OnClosed(self, *args): #cannot find CLR method
        """ OnClosed(self: Activity, provider: IServiceProvider) """
        ...

    def RaiseEvent(self, *args): #cannot find CLR method
        """ RaiseEvent(self: Activity, dependencyEvent: DependencyProperty, sender: object, e: EventArgs) """
        ...

    def RaiseGenericEvent(self, *args): #cannot find CLR method
        """ RaiseGenericEvent[T](self: Activity, dependencyEvent: DependencyProperty, sender: object, e: T) """
        ...

    def RegisterForStatusChange(self, dependencyProp:DependencyProperty, activityStatusChangeListener:IActivityEventListener): # -> 
        """ RegisterForStatusChange(self: Activity, dependencyProp: DependencyProperty, activityStatusChangeListener: IActivityEventListener[ActivityExecutionStatusChangedEventArgs]) """
        ...

    def Save(self, stream:Stream, formatter:IFormatter = ...): # -> 
        """ Save(self: Activity, stream: Stream)Save(self: Activity, stream: Stream, formatter: IFormatter) """
        ...

    def ToString(self) -> str:
        """ ToString(self: Activity) -> str """
        ...

    def TrackData(self, *args): #cannot find CLR method
        """ TrackData(self: Activity, userData: object)TrackData(self: Activity, userDataKey: str, userData: object) """
        ...

    def Uninitialize(self, *args): #cannot find CLR method
        """ Uninitialize(self: Activity, provider: IServiceProvider) """
        ...

    def UnregisterForStatusChange(self, dependencyProp:DependencyProperty, activityStatusChangeListener:IActivityEventListener): # -> 
        """ UnregisterForStatusChange(self: Activity, dependencyProp: DependencyProperty, activityStatusChangeListener: IActivityEventListener[ActivityExecutionStatusChangedEventArgs]) """
        ...

    def __new__(cls, name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    ActivityContextGuidProperty: DependencyProperty = ...
    Canceling = ...
    CancelingEvent: DependencyProperty = ...
    Closed = ...
    ClosedEvent: DependencyProperty = ...
    Compensating = ...
    CompensatingEvent: DependencyProperty = ...
    Executing = ...
    ExecutingEvent: DependencyProperty = ...
    Faulting = ...
    FaultingEvent: DependencyProperty = ...
    StatusChanged = ...
    StatusChangedEvent: DependencyProperty = ...


class ActivityBind(IPropertyValueProvider, MarkupExtension): # skipped bases: <type 'object'>
    """
    ActivityBind()
    ActivityBind(name: str)
    ActivityBind(name: str, path: str)
    """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: ActivityBind) -> str
        Set: Name(self: ActivityBind) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: ActivityBind) -> str
        Set: Path(self: ActivityBind) = value
        """
        ...

    @property
    def UserData(self) -> IDictionary:
        """ Get: UserData(self: ActivityBind) -> IDictionary """
        ...


    def GetRuntimeValue(self, activity:Activity, targetType:Type = ...) -> object:
        """
        GetRuntimeValue(self: ActivityBind, activity: Activity, targetType: Type) -> object
        GetRuntimeValue(self: ActivityBind, activity: Activity) -> object
        """
        ...

    def SetRuntimeValue(self, activity:Activity, value:object): # -> 
        """ SetRuntimeValue(self: ActivityBind, activity: Activity, value: object) """
        ...

    def ToString(self) -> str:
        """ ToString(self: ActivityBind) -> str """
        ...

    def __new__(cls, name:str = ..., path:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, path: str)
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class WorkflowChangeAction: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def ApplyTo(self, *args): #cannot find CLR method
        """ ApplyTo(self: WorkflowChangeAction, rootActivity: Activity) -> bool """
        ...

    def ValidateChanges(self, *args): #cannot find CLR method
        """ ValidateChanges(self: WorkflowChangeAction, activity: Activity) -> ValidationErrorCollection """
        ...


class ActivityChangeAction(WorkflowChangeAction): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def OwnerActivityDottedPath(self) -> str:
        """ Get: OwnerActivityDottedPath(self: ActivityChangeAction) -> str """
        ...


    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, compositeActivity: CompositeActivity)
        """
        ...


class ActivityCollection(List): # skipped bases: <type 'IEnumerable'>, <type 'IEnumerable[Activity]'>, <type 'IList'>, <type 'IList[Activity]'>, <type 'IReadOnlyCollection[Activity]'>, <type 'ICollection[Activity]'>, <type 'ICollection'>, <type 'IReadOnlyList[Activity]'>, <type 'object'>
    """ ActivityCollection(owner: Activity) """
    ListChanged = ...


class ActivityCollectionChangeAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ActivityCollectionChangeAction, values: Add (0), Remove (1), Replace (2) """
    Add: ActivityCollectionChangeAction = ...
    Remove: ActivityCollectionChangeAction = ...
    Replace: ActivityCollectionChangeAction = ...
    value__ = ...


class ActivityCollectionChangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    ActivityCollectionChangeEventArgs(index: int, removedItems: ICollection[Activity], addedItems: ICollection[Activity], owner: object, action: ActivityCollectionChangeAction)
    ActivityCollectionChangeEventArgs(index: int, removedActivity: Activity, addedActivity: Activity, owner: object, action: ActivityCollectionChangeAction)
    """
    @property
    def Action(self) -> ActivityCollectionChangeAction:
        """ Get: Action(self: ActivityCollectionChangeEventArgs) -> ActivityCollectionChangeAction """
        ...

    @property
    def AddedItems(self) -> IList:
        """ Get: AddedItems(self: ActivityCollectionChangeEventArgs) -> IList[Activity] """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: ActivityCollectionChangeEventArgs) -> int """
        ...

    @property
    def Owner(self) -> object:
        """ Get: Owner(self: ActivityCollectionChangeEventArgs) -> object """
        ...

    @property
    def RemovedItems(self) -> IList:
        """ Get: RemovedItems(self: ActivityCollectionChangeEventArgs) -> IList[Activity] """
        ...


    def __new__(cls, index, *__args) -> Self:
        """
        __new__(cls: type, index: int, removedItems: ICollection[Activity], addedItems: ICollection[Activity], owner: object, action: ActivityCollectionChangeAction)
        __new__(cls: type, index: int, removedActivity: Activity, addedActivity: Activity, owner: object, action: ActivityCollectionChangeAction)
        """
        ...


class ActivityCondition(DependencyObject): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """ no doc """
    def Evaluate(self, activity:Activity, provider:IServiceProvider) -> bool:
        """ Evaluate(self: ActivityCondition, activity: Activity, provider: IServiceProvider) -> bool """
        ...


class ActivityExecutionContext(IServiceProvider, IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Activity(self) -> Activity:
        """ Get: Activity(self: ActivityExecutionContext) -> Activity """
        ...

    @property
    def ContextGuid(self) -> Guid:
        """ Get: ContextGuid(self: ActivityExecutionContext) -> Guid """
        ...

    @property
    def ExecutionContextManager(self) -> ActivityExecutionContextManager:
        """ Get: ExecutionContextManager(self: ActivityExecutionContext) -> ActivityExecutionContextManager """
        ...


    def CancelActivity(self, activity:Activity): # -> 
        """ CancelActivity(self: ActivityExecutionContext, activity: Activity) """
        ...

    def CloseActivity(self): # -> 
        """ CloseActivity(self: ActivityExecutionContext) """
        ...

    def ExecuteActivity(self, activity:Activity): # -> 
        """ ExecuteActivity(self: ActivityExecutionContext, activity: Activity) """
        ...

    def TrackData(self, *__args:object): # -> 
        """ TrackData(self: ActivityExecutionContext, userData: object)TrackData(self: ActivityExecutionContext, userDataKey: str, userData: object) """
        ...

    CurrentExceptionProperty: DependencyProperty = ...


class ActivityExecutionContextManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ExecutionContexts(self) -> ReadOnlyCollection:
        """ Get: ExecutionContexts(self: ActivityExecutionContextManager) -> ReadOnlyCollection[ActivityExecutionContext] """
        ...

    @property
    def PersistedExecutionContexts(self) -> IEnumerable:
        """ Get: PersistedExecutionContexts(self: ActivityExecutionContextManager) -> IEnumerable[Guid] """
        ...


    def CompleteExecutionContext(self, childContext:ActivityExecutionContext, forcePersist:bool = ...): # -> 
        """ CompleteExecutionContext(self: ActivityExecutionContextManager, childContext: ActivityExecutionContext)CompleteExecutionContext(self: ActivityExecutionContextManager, childContext: ActivityExecutionContext, forcePersist: bool) """
        ...

    def CreateExecutionContext(self, activity:Activity) -> ActivityExecutionContext:
        """ CreateExecutionContext(self: ActivityExecutionContextManager, activity: Activity) -> ActivityExecutionContext """
        ...

    def GetExecutionContext(self, activity:Activity) -> ActivityExecutionContext:
        """ GetExecutionContext(self: ActivityExecutionContextManager, activity: Activity) -> ActivityExecutionContext """
        ...

    def GetPersistedExecutionContext(self, contextGuid:Guid) -> ActivityExecutionContext:
        """ GetPersistedExecutionContext(self: ActivityExecutionContextManager, contextGuid: Guid) -> ActivityExecutionContext """
        ...


class ActivityExecutionResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ActivityExecutionResult, values: Canceled (2), Compensated (3), Faulted (4), None (0), Succeeded (1), Uninitialized (5) """
    Canceled: ActivityExecutionResult = ...
    Compensated: ActivityExecutionResult = ...
    Faulted: ActivityExecutionResult = ...
    Succeeded: ActivityExecutionResult = ...
    Uninitialized: ActivityExecutionResult = ...
    value__ = ...


class ActivityExecutionStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ActivityExecutionStatus, values: Canceling (2), Closed (3), Compensating (4), Executing (1), Faulting (5), Initialized (0) """
    Canceling: ActivityExecutionStatus = ...
    Closed: ActivityExecutionStatus = ...
    Compensating: ActivityExecutionStatus = ...
    Executing: ActivityExecutionStatus = ...
    Faulting: ActivityExecutionStatus = ...
    Initialized: ActivityExecutionStatus = ...
    value__ = ...


class ActivityExecutionStatusChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Activity(self) -> Activity:
        """ Get: Activity(self: ActivityExecutionStatusChangedEventArgs) -> Activity """
        ...

    @property
    def ExecutionResult(self) -> ActivityExecutionResult:
        """ Get: ExecutionResult(self: ActivityExecutionStatusChangedEventArgs) -> ActivityExecutionResult """
        ...

    @property
    def ExecutionStatus(self) -> ActivityExecutionStatus:
        """ Get: ExecutionStatus(self: ActivityExecutionStatusChangedEventArgs) -> ActivityExecutionStatus """
        ...


    def ToString(self) -> str:
        """ ToString(self: ActivityExecutionStatusChangedEventArgs) -> str """
        ...


class AddedActivityAction(ActivityChangeAction): # skipped bases: <type 'object'>
    """
    AddedActivityAction()
    AddedActivityAction(compositeActivity: CompositeActivity, activityAdded: Activity)
    """
    @property
    def AddedActivity(self) -> Activity:
        """ Get: AddedActivity(self: AddedActivityAction) -> Activity """
        ...

    @property
    def Index(self) -> int:
        """ Get: Index(self: AddedActivityAction) -> int """
        ...



class AlternateFlowActivityAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AlternateFlowActivityAttribute() """
    pass

class CompositeActivity(Activity, ISupportAlternateFlow): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    CompositeActivity()
    CompositeActivity(children: IEnumerable[Activity])
    CompositeActivity(name: str)
    """
    @property
    def Activities(self) -> ActivityCollection:
        """ Get: Activities(self: CompositeActivity) -> ActivityCollection """
        ...

    @property
    def CanModifyActivities(self):
        ...

    @property
    def EnabledActivities(self) -> ReadOnlyCollection:
        """ Get: EnabledActivities(self: CompositeActivity) -> ReadOnlyCollection[Activity] """
        ...


    def ApplyWorkflowChanges(self, *args): #cannot find CLR method
        """ ApplyWorkflowChanges(self: CompositeActivity, workflowChanges: WorkflowChanges) """
        ...

    def GetDynamicActivities(self, *args): #cannot find CLR method
        """ GetDynamicActivities(self: CompositeActivity, activity: Activity) -> Array[Activity] """
        ...

    def OnActivityChangeAdd(self, *args): #cannot find CLR method
        """ OnActivityChangeAdd(self: CompositeActivity, executionContext: ActivityExecutionContext, addedActivity: Activity) """
        ...

    def OnActivityChangeRemove(self, *args): #cannot find CLR method
        """ OnActivityChangeRemove(self: CompositeActivity, executionContext: ActivityExecutionContext, removedActivity: Activity) """
        ...

    def OnListChanged(self, *args): #cannot find CLR method
        """ OnListChanged(self: CompositeActivity, e: ActivityCollectionChangeEventArgs) """
        ...

    def OnListChanging(self, *args): #cannot find CLR method
        """ OnListChanging(self: CompositeActivity, e: ActivityCollectionChangeEventArgs) """
        ...

    def OnWorkflowChangesCompleted(self, *args): #cannot find CLR method
        """ OnWorkflowChangesCompleted(self: CompositeActivity, rootContext: ActivityExecutionContext) """
        ...


class CancellationHandlerActivity(CompositeActivity, IActivityEventListener): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    CancellationHandlerActivity()
    CancellationHandlerActivity(name: str)
    """
    pass

class ICompensatableActivity: # skipped bases: <type 'object'>
    """ no doc """
    def Compensate(self, executionContext:ActivityExecutionContext) -> ActivityExecutionStatus:
        """ Compensate(self: ICompensatableActivity, executionContext: ActivityExecutionContext) -> ActivityExecutionStatus """
        ...


class CompensatableTransactionScopeActivity(ICompensatableActivity, CompositeActivity, IActivityEventListener): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    CompensatableTransactionScopeActivity()
    CompensatableTransactionScopeActivity(name: str)
    """
    @property
    def TransactionOptions(self) -> WorkflowTransactionOptions:
        """
        Get: TransactionOptions(self: CompensatableTransactionScopeActivity) -> WorkflowTransactionOptions
        Set: TransactionOptions(self: CompensatableTransactionScopeActivity) = value
        """
        ...



class CompensateActivity(IPropertyValueProvider, IActivityEventListener, Activity): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    CompensateActivity()
    CompensateActivity(name: str)
    """
    @property
    def TargetActivityName(self) -> str:
        """
        Get: TargetActivityName(self: CompensateActivity) -> str
        Set: TargetActivityName(self: CompensateActivity) = value
        """
        ...


    TargetActivityNameProperty: DependencyProperty = ...


class CompensationHandlerActivity(CompositeActivity, IActivityEventListener): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    CompensationHandlerActivity()
    CompensationHandlerActivity(name: str)
    """
    pass

class DependencyProperty(ISerializable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DefaultMetadata(self) -> PropertyMetadata:
        """ Get: DefaultMetadata(self: DependencyProperty) -> PropertyMetadata """
        ...

    @property
    def IsAttached(self) -> bool:
        """ Get: IsAttached(self: DependencyProperty) -> bool """
        ...

    @property
    def IsEvent(self) -> bool:
        """ Get: IsEvent(self: DependencyProperty) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DependencyProperty) -> str """
        ...

    @property
    def OwnerType(self) -> Type:
        """ Get: OwnerType(self: DependencyProperty) -> Type """
        ...

    @property
    def PropertyType(self) -> Type:
        """ Get: PropertyType(self: DependencyProperty) -> Type """
        ...

    @property
    def ValidatorType(self) -> Type:
        """ Get: ValidatorType(self: DependencyProperty) -> Type """
        ...


    @staticmethod
    def FromName(propertyName:str, ownerType:Type) -> DependencyProperty:
        """ FromName(propertyName: str, ownerType: Type) -> DependencyProperty """
        ...

    @staticmethod
    def FromType(ownerType:Type) -> IList:
        """ FromType(ownerType: Type) -> IList[DependencyProperty] """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: DependencyProperty) -> int """
        ...

    @staticmethod
    def Register(name:str, propertyType:Type, ownerType:Type, defaultMetadata:PropertyMetadata = ...) -> DependencyProperty:
        """
        Register(name: str, propertyType: Type, ownerType: Type) -> DependencyProperty
        Register(name: str, propertyType: Type, ownerType: Type, defaultMetadata: PropertyMetadata) -> DependencyProperty
        """
        ...

    @staticmethod
    def RegisterAttached(name:str, propertyType:Type, ownerType:Type, defaultMetadata:PropertyMetadata = ..., validatorType:Type = ...) -> DependencyProperty:
        """
        RegisterAttached(name: str, propertyType: Type, ownerType: Type) -> DependencyProperty
        RegisterAttached(name: str, propertyType: Type, ownerType: Type, defaultMetadata: PropertyMetadata) -> DependencyProperty
        RegisterAttached(name: str, propertyType: Type, ownerType: Type, defaultMetadata: PropertyMetadata, validatorType: Type) -> DependencyProperty
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: DependencyProperty) -> str """
        ...


class DependencyPropertyOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DependencyPropertyOptions, values: Default (1), DelegateProperty (32), Metadata (8), NonSerialized (16), Optional (4), ReadOnly (2) """
    Default: DependencyPropertyOptions = ...
    DelegateProperty: DependencyPropertyOptions = ...
    Metadata: DependencyPropertyOptions = ...
    NonSerialized: DependencyPropertyOptions = ...
    Optional: DependencyPropertyOptions = ...
    ReadOnly: DependencyPropertyOptions = ...
    value__ = ...


class IDynamicPropertyTypeProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetAccessType(self, serviceProvider:IServiceProvider, propertyName:str) -> AccessTypes:
        """ GetAccessType(self: IDynamicPropertyTypeProvider, serviceProvider: IServiceProvider, propertyName: str) -> AccessTypes """
        ...

    def GetPropertyType(self, serviceProvider:IServiceProvider, propertyName:str) -> Type:
        """ GetPropertyType(self: IDynamicPropertyTypeProvider, serviceProvider: IServiceProvider, propertyName: str) -> Type """
        ...


class FaultHandlerActivity(IDynamicPropertyTypeProvider, CompositeActivity, IActivityEventListener, ITypeFilterProvider): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    FaultHandlerActivity()
    FaultHandlerActivity(name: str)
    """
    @property
    def Fault(self) -> Exception:
        """ Get: Fault(self: FaultHandlerActivity) -> Exception """
        ...

    @property
    def FaultType(self) -> Type:
        """
        Get: FaultType(self: FaultHandlerActivity) -> Type
        Set: FaultType(self: FaultHandlerActivity) = value
        """
        ...


    FaultTypeProperty: DependencyProperty = ...


class FaultHandlersActivity(CompositeActivity, IActivityEventListener): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    FaultHandlersActivity()
    FaultHandlersActivity(name: str)
    """
    pass

class GetValueOverride(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ GetValueOverride(object: object, method: IntPtr) """
    def BeginInvoke(self, d:DependencyObject, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: GetValueOverride, d: DependencyObject, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> object:
        """ EndInvoke(self: GetValueOverride, result: IAsyncResult) -> object """
        ...

    def Invoke(self, d:DependencyObject) -> object:
        """ Invoke(self: GetValueOverride, d: DependencyObject) -> object """
        ...


class IActivityEventListener: # skipped bases: <type 'object'>
    """ no doc """
    def OnEvent(self, sender:object, e): # ->  # Not found arg types: {'e': 'T'}
        """ OnEvent(self: IActivityEventListener[T], sender: object, e: T) """
        ...


class IStartWorkflow: # skipped bases: <type 'object'>
    """ no doc """
    def StartWorkflow(self, workflowType:Type, namedArgumentValues:Dictionary) -> Guid:
        """ StartWorkflow(self: IStartWorkflow, workflowType: Type, namedArgumentValues: Dictionary[str, object]) -> Guid """
        ...


class IWorkflowChangeDiff: # skipped bases: <type 'object'>
    """ no doc """
    def Diff(self, originalDefinition:object, changedDefinition:object) -> IList:
        """ Diff(self: IWorkflowChangeDiff, originalDefinition: object, changedDefinition: object) -> IList[WorkflowChangeAction] """
        ...


class PersistOnCloseAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PersistOnCloseAttribute() """
    pass

class PropertyMetadata: # skipped bases: <type 'object'>, <type 'object'>
    """
    PropertyMetadata()
    PropertyMetadata(defaultValue: object)
    PropertyMetadata(options: DependencyPropertyOptions)
    PropertyMetadata(defaultValue: object, options: DependencyPropertyOptions)
    PropertyMetadata(defaultValue: object, *attributes: Array[Attribute])
    PropertyMetadata(defaultValue: object, options: DependencyPropertyOptions, *attributes: Array[Attribute])
    PropertyMetadata(options: DependencyPropertyOptions, *attributes: Array[Attribute])
    PropertyMetadata(*attributes: Array[Attribute])
    PropertyMetadata(defaultValue: object, options: DependencyPropertyOptions, getValueOverride: GetValueOverride, setValueOverride: SetValueOverride)
    PropertyMetadata(defaultValue: object, options: DependencyPropertyOptions, getValueOverride: GetValueOverride, setValueOverride: SetValueOverride, *attributes: Array[Attribute])
    """
    @property
    def DefaultValue(self) -> object:
        """
        Get: DefaultValue(self: PropertyMetadata) -> object
        Set: DefaultValue(self: PropertyMetadata) = value
        """
        ...

    @property
    def GetValueOverride(self) -> GetValueOverride:
        """
        Get: GetValueOverride(self: PropertyMetadata) -> GetValueOverride
        Set: GetValueOverride(self: PropertyMetadata) = value
        """
        ...

    @property
    def IsMetaProperty(self) -> bool:
        """ Get: IsMetaProperty(self: PropertyMetadata) -> bool """
        ...

    @property
    def IsNonSerialized(self) -> bool:
        """ Get: IsNonSerialized(self: PropertyMetadata) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: PropertyMetadata) -> bool """
        ...

    @property
    def IsSealed(self):
        ...

    @property
    def Options(self) -> DependencyPropertyOptions:
        """
        Get: Options(self: PropertyMetadata) -> DependencyPropertyOptions
        Set: Options(self: PropertyMetadata) = value
        """
        ...

    @property
    def SetValueOverride(self) -> SetValueOverride:
        """
        Get: SetValueOverride(self: PropertyMetadata) -> SetValueOverride
        Set: SetValueOverride(self: PropertyMetadata) = value
        """
        ...


    def GetAttributes(self, attributeType:Type = ...) -> Array:
        """
        GetAttributes(self: PropertyMetadata) -> Array[Attribute]
        GetAttributes(self: PropertyMetadata, attributeType: Type) -> Array[Attribute]
        """
        ...

    def OnApply(self, *args): #cannot find CLR method
        """ OnApply(self: PropertyMetadata, dependencyProperty: DependencyProperty, targetType: Type) """
        ...


class QueueEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def QueueName(self) -> IComparable:
        """ Get: QueueName(self: QueueEventArgs) -> IComparable """
        ...



class RemovedActivityAction(ActivityChangeAction): # skipped bases: <type 'object'>
    """
    RemovedActivityAction()
    RemovedActivityAction(removedActivityIndex: int, originalActivity: Activity, clonedParentActivity: CompositeActivity)
    """
    @property
    def OriginalRemovedActivity(self) -> Activity:
        """ Get: OriginalRemovedActivity(self: RemovedActivityAction) -> Activity """
        ...

    @property
    def RemovedActivityIndex(self) -> int:
        """ Get: RemovedActivityIndex(self: RemovedActivityAction) -> int """
        ...



class SetValueOverride(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SetValueOverride(object: object, method: IntPtr) """
    def BeginInvoke(self, d:DependencyObject, value:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SetValueOverride, d: DependencyObject, value: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SetValueOverride, result: IAsyncResult) """
        ...

    def Invoke(self, d:DependencyObject, value:object): # -> 
        """ Invoke(self: SetValueOverride, d: DependencyObject, value: object) """
        ...


class SuspendActivity(Activity): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    SuspendActivity()
    SuspendActivity(name: str)
    """
    @property
    def Error(self) -> str:
        """
        Get: Error(self: SuspendActivity) -> str
        Set: Error(self: SuspendActivity) = value
        """
        ...


    ErrorProperty: DependencyProperty = ...


class SynchronizationScopeActivity(CompositeActivity, IActivityEventListener): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    SynchronizationScopeActivity()
    SynchronizationScopeActivity(name: str)
    """
    @property
    def SynchronizationHandles(self) -> ICollection:
        """
        Get: SynchronizationHandles(self: SynchronizationScopeActivity) -> ICollection[str]
        Set: SynchronizationHandles(self: SynchronizationScopeActivity) = value
        """
        ...



class TerminateActivity(Activity): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    TerminateActivity()
    TerminateActivity(name: str)
    """
    @property
    def Error(self) -> str:
        """
        Get: Error(self: TerminateActivity) -> str
        Set: Error(self: TerminateActivity) = value
        """
        ...


    ErrorProperty: DependencyProperty = ...


class ThrowActivity(IDynamicPropertyTypeProvider, Activity, ITypeFilterProvider): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    ThrowActivity()
    ThrowActivity(name: str)
    """
    @property
    def Fault(self) -> Exception:
        """
        Get: Fault(self: ThrowActivity) -> Exception
        Set: Fault(self: ThrowActivity) = value
        """
        ...

    @property
    def FaultType(self) -> Type:
        """
        Get: FaultType(self: ThrowActivity) -> Type
        Set: FaultType(self: ThrowActivity) = value
        """
        ...


    FaultProperty: DependencyProperty = ...
    FaultTypeProperty: DependencyProperty = ...


class TransactionScopeActivity(CompositeActivity, IActivityEventListener): # skipped bases: <type 'IDisposable'>, <type 'ISupportAlternateFlow'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    TransactionScopeActivity()
    TransactionScopeActivity(name: str)
    """
    @property
    def TransactionOptions(self) -> WorkflowTransactionOptions:
        """
        Get: TransactionOptions(self: TransactionScopeActivity) -> WorkflowTransactionOptions
        Set: TransactionOptions(self: TransactionScopeActivity) = value
        """
        ...



class WorkflowChanges: # skipped bases: <type 'object'>, <type 'object'>
    """ WorkflowChanges(rootActivity: Activity) """
    @property
    def TransientWorkflow(self) -> CompositeActivity:
        """ Get: TransientWorkflow(self: WorkflowChanges) -> CompositeActivity """
        ...


    @staticmethod
    def GetCondition(dependencyObject:object) -> object:
        """ GetCondition(dependencyObject: object) -> object """
        ...

    @staticmethod
    def SetCondition(dependencyObject:object, value:object): # -> 
        """ SetCondition(dependencyObject: object, value: object) """
        ...

    def Validate(self) -> ValidationErrorCollection:
        """ Validate(self: WorkflowChanges) -> ValidationErrorCollection """
        ...

    ConditionProperty: DependencyProperty = ...


class WorkflowParameterBinding(DependencyObject): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """
    WorkflowParameterBinding()
    WorkflowParameterBinding(parameterName: str)
    """
    @property
    def ParameterName(self) -> str:
        """
        Get: ParameterName(self: WorkflowParameterBinding) -> str
        Set: ParameterName(self: WorkflowParameterBinding) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: WorkflowParameterBinding) -> object
        Set: Value(self: WorkflowParameterBinding) = value
        """
        ...


    def __new__(cls, parameterName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parameterName: str)
        """
        ...

    ParameterNameProperty: DependencyProperty = ...
    ValueProperty: DependencyProperty = ...


class WorkflowParameterBindingCollection(KeyedCollection): # skipped bases: <type 'ICollection[WorkflowParameterBinding]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IEnumerable[WorkflowParameterBinding]'>, <type 'IReadOnlyList[WorkflowParameterBinding]'>, <type 'IList[WorkflowParameterBinding]'>, <type 'IReadOnlyCollection[WorkflowParameterBinding]'>, <type 'ICollection'>, <type 'object'>
    """ WorkflowParameterBindingCollection(ownerActivity: Activity) """
    def GetItem(self, key:str) -> WorkflowParameterBinding:
        """ GetItem(self: WorkflowParameterBindingCollection, key: str) -> WorkflowParameterBinding """
        ...


class WorkflowTerminatedException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WorkflowTerminatedException()
    WorkflowTerminatedException(message: str)
    WorkflowTerminatedException(message: str, exception: Exception)
    """
    SerializeObjectState = ...


class WorkflowTransactionOptions(DependencyObject): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'IDependencyObjectAccessor'>, <type 'object'>
    """ WorkflowTransactionOptions() """
    @property
    def IsolationLevel(self) -> IsolationLevel:
        """
        Get: IsolationLevel(self: WorkflowTransactionOptions) -> IsolationLevel
        Set: IsolationLevel(self: WorkflowTransactionOptions) = value
        """
        ...

    @property
    def TimeoutDuration(self) -> TimeSpan:
        """
        Get: TimeoutDuration(self: WorkflowTransactionOptions) -> TimeSpan
        Set: TimeoutDuration(self: WorkflowTransactionOptions) = value
        """
        ...


    IsolationLevelProperty: DependencyProperty = ...
    TimeoutDurationProperty: DependencyProperty = ...


# variables with complex values

