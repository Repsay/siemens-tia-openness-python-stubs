# encoding: utf-8
# module System.Activities.Statements calls itself Statements
# from System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Workflow.Runtime, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import IDisposable, TimeSpan, Type

from System.Activities import (ActivityAction, ActivityDelegate, 
    AsyncCodeActivity, Bookmark, CodeActivity, InArgument, NativeActivity, 
    OutArgument)

from System.Activities.Hosting import IWorkflowInstanceExtension

from System.Activities.Persistence import PersistenceParticipant

from System.Collections import IDictionary

from System.ComponentModel import ICustomTypeDescriptor

from System.Data import IsolationLevel

from System.EnterpriseServices import Activity

from System.Linq.Expressions import Expression

from typing import Self

"""The following names are not found in the module: (BoundEvent, ICancelable, 
    IFlowSwitch)
"""

# no functions
# classes

class AddToCollection(CodeActivity): # skipped bases: <type 'object'>
    """ AddToCollection[T]() """
    @property
    def Collection(self) -> InArgument:
        """
        Get: Collection(self: AddToCollection[T]) -> InArgument[ICollection[T]]
        Set: Collection(self: AddToCollection[T]) = value
        """
        ...

    @property
    def Item(self) -> InArgument:
        """
        Get: Item(self: AddToCollection[T]) -> InArgument[T]
        Set: Item(self: AddToCollection[T]) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class Assign: # skipped bases: <type 'object'>
    """ Assign() """
    @property
    def CacheId(self):
        ...

    @property
    def Constraints(self):
        ...

    @property
    def Implementation(self):
        ...

    @property
    def ImplementationVersion(self):
        ...

    @property
    def To(self) -> OutArgument:
        """
        Get: To(self: Assign) -> OutArgument
        Set: To(self: Assign) = value
        """
        ...

    @property
    def Value(self) -> InArgument:
        """
        Get: Value(self: Assign) -> InArgument
        Set: Value(self: Assign) = value
        """
        ...


    def CacheMetadata(self, *args): #cannot find CLR method
        """ CacheMetadata(self: Assign, metadata: CodeActivityMetadata)CacheMetadata(self: CodeActivity, metadata: ActivityMetadata) """
        ...

    def Execute(self, *args): #cannot find CLR method
        """ Execute(self: Assign, context: CodeActivityContext) """
        ...

    def OnCreateDynamicUpdateMap(self, *args): #cannot find CLR method
        """ OnCreateDynamicUpdateMap(self: CodeActivity, metadata: UpdateMapMetadata, originalActivity: Activity) """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class CancellationScope(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ CancellationScope() """
    @property
    def Body(self) -> Activity:
        """
        Get: Body(self: CancellationScope) -> Activity
        Set: Body(self: CancellationScope) = value
        """
        ...

    @property
    def CancellationHandler(self) -> Activity:
        """
        Get: CancellationHandler(self: CancellationScope) -> Activity
        Set: CancellationHandler(self: CancellationScope) = value
        """
        ...

    @property
    def Variables(self) -> Collection:
        """ Get: Variables(self: CancellationScope) -> Collection[Variable] """
        ...



class Catch: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ExceptionType(self) -> Type:
        """ Get: ExceptionType(self: Catch) -> Type """
        ...


    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class ClearCollection(CodeActivity): # skipped bases: <type 'object'>
    """ ClearCollection[T]() """
    @property
    def Collection(self) -> InArgument:
        """
        Get: Collection(self: ClearCollection[T]) -> InArgument[ICollection[T]]
        Set: Collection(self: ClearCollection[T]) = value
        """
        ...



class CompensableActivity(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ CompensableActivity() """
    @property
    def Body(self) -> Activity:
        """
        Get: Body(self: CompensableActivity) -> Activity
        Set: Body(self: CompensableActivity) = value
        """
        ...

    @property
    def CancellationHandler(self) -> Activity:
        """
        Get: CancellationHandler(self: CompensableActivity) -> Activity
        Set: CancellationHandler(self: CompensableActivity) = value
        """
        ...

    @property
    def CompensationHandler(self) -> Activity:
        """
        Get: CompensationHandler(self: CompensableActivity) -> Activity
        Set: CompensationHandler(self: CompensableActivity) = value
        """
        ...

    @property
    def ConfirmationHandler(self) -> Activity:
        """
        Get: ConfirmationHandler(self: CompensableActivity) -> Activity
        Set: ConfirmationHandler(self: CompensableActivity) = value
        """
        ...

    @property
    def Variables(self) -> Collection:
        """ Get: Variables(self: CompensableActivity) -> Collection[Variable] """
        ...



class Compensate(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ Compensate() """
    @property
    def Target(self) -> InArgument:
        """
        Get: Target(self: Compensate) -> InArgument[CompensationToken]
        Set: Target(self: Compensate) = value
        """
        ...



class CompensationExtension(IWorkflowInstanceExtension, PersistenceParticipant): # skipped bases: <type 'IPersistencePipelineModule'>, <type 'object'>
    """ CompensationExtension() """
    pass

class CompensationToken: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class Confirm(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ Confirm() """
    @property
    def Target(self) -> InArgument:
        """
        Get: Target(self: Confirm) -> InArgument[CompensationToken]
        Set: Target(self: Confirm) = value
        """
        ...



class CreateBookmarkScope(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ CreateBookmarkScope() """
    pass

class Delay(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ Delay() """
    @property
    def Duration(self) -> InArgument:
        """
        Get: Duration(self: Delay) -> InArgument[TimeSpan]
        Set: Duration(self: Delay) = value
        """
        ...



class DeleteBookmarkScope(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ DeleteBookmarkScope() """
    @property
    def Scope(self) -> InArgument:
        """
        Get: Scope(self: DeleteBookmarkScope) -> InArgument[BookmarkScope]
        Set: Scope(self: DeleteBookmarkScope) = value
        """
        ...



class DoWhile(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """
    DoWhile()
    DoWhile(condition: Expression[Func[ActivityContext, bool]])
    DoWhile(condition: Activity[bool])
    """
    @property
    def Body(self) -> Activity:
        """
        Get: Body(self: DoWhile) -> Activity
        Set: Body(self: DoWhile) = value
        """
        ...

    @property
    def Condition(self) -> Activity:
        """
        Get: Condition(self: DoWhile) -> Activity[bool]
        Set: Condition(self: DoWhile) = value
        """
        ...

    @property
    def Variables(self) -> Collection:
        """ Get: Variables(self: DoWhile) -> Collection[Variable] """
        ...


    def __new__(cls, condition:Expression = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, condition: Expression[Func[ActivityContext, bool]])
        __new__(cls: type, condition: Activity[bool])
        """
        ...


class TimerExtension: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CancelTimer(self, bookmark:Bookmark): # -> 
        """ CancelTimer(self: TimerExtension, bookmark: Bookmark) """
        ...

    def OnCancelTimer(self, *args): #cannot find CLR method
        """ OnCancelTimer(self: TimerExtension, bookmark: Bookmark) """
        ...

    def OnRegisterTimer(self, *args): #cannot find CLR method
        """ OnRegisterTimer(self: TimerExtension, timeout: TimeSpan, bookmark: Bookmark) """
        ...

    def RegisterTimer(self, timeout:TimeSpan, bookmark:Bookmark): # -> 
        """ RegisterTimer(self: TimerExtension, timeout: TimeSpan, bookmark: Bookmark) """
        ...


class DurableTimerExtension(IWorkflowInstanceExtension, IDisposable, TimerExtension, ICancelable): # skipped bases: <type 'object'>
    """ DurableTimerExtension() """
    pass

class ExistsInCollection(CodeActivity): # skipped bases: <type 'object'>
    """ ExistsInCollection[T]() """
    @property
    def Collection(self) -> InArgument:
        """
        Get: Collection(self: ExistsInCollection[T]) -> InArgument[ICollection[T]]
        Set: Collection(self: ExistsInCollection[T]) = value
        """
        ...

    @property
    def Item(self) -> InArgument:
        """
        Get: Item(self: ExistsInCollection[T]) -> InArgument[T]
        Set: Item(self: ExistsInCollection[T]) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class Flowchart(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ Flowchart() """
    @property
    def Nodes(self) -> Collection:
        """ Get: Nodes(self: Flowchart) -> Collection[FlowNode] """
        ...

    @property
    def StartNode(self) -> FlowNode:
        """
        Get: StartNode(self: Flowchart) -> FlowNode
        Set: StartNode(self: Flowchart) = value
        """
        ...

    @property
    def ValidateUnconnectedNodes(self) -> bool:
        """
        Get: ValidateUnconnectedNodes(self: Flowchart) -> bool
        Set: ValidateUnconnectedNodes(self: Flowchart) = value
        """
        ...

    @property
    def Variables(self) -> Collection:
        """ Get: Variables(self: Flowchart) -> Collection[Variable] """
        ...



class FlowNode: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class FlowDecision(FlowNode): # skipped bases: <type 'object'>
    """
    FlowDecision()
    FlowDecision(condition: Expression[Func[ActivityContext, bool]])
    FlowDecision(condition: Activity[bool])
    """
    @property
    def Condition(self) -> Activity:
        """
        Get: Condition(self: FlowDecision) -> Activity[bool]
        Set: Condition(self: FlowDecision) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: FlowDecision) -> str
        Set: DisplayName(self: FlowDecision) = value
        """
        ...

    @property
    def False(self) -> FlowNode:
        """
        Get: False(self: FlowDecision) -> FlowNode
        Set: False(self: FlowDecision) = value
        """
        ...

    @property
    def True(self) -> FlowNode:
        """
        Get: True(self: FlowDecision) -> FlowNode
        Set: True(self: FlowDecision) = value
        """
        ...


    def __new__(cls, condition:Expression = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, condition: Expression[Func[ActivityContext, bool]])
        __new__(cls: type, condition: Activity[bool])
        """
        ...


class FlowStep(FlowNode): # skipped bases: <type 'object'>
    """ FlowStep() """
    @property
    def Action(self) -> Activity:
        """
        Get: Action(self: FlowStep) -> Activity
        Set: Action(self: FlowStep) = value
        """
        ...

    @property
    def Next(self) -> FlowNode:
        """
        Get: Next(self: FlowStep) -> FlowNode
        Set: Next(self: FlowStep) = value
        """
        ...



class FlowSwitch(FlowNode, IFlowSwitch): # skipped bases: <type 'object'>
    """ FlowSwitch[T]() """
    @property
    def Cases(self) -> IDictionary:
        """ Get: Cases(self: FlowSwitch[T]) -> IDictionary[T, FlowNode] """
        ...

    @property
    def Default(self) -> FlowNode:
        """
        Get: Default(self: FlowSwitch[T]) -> FlowNode
        Set: Default(self: FlowSwitch[T]) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: FlowSwitch[T]) -> str
        Set: DisplayName(self: FlowSwitch[T]) = value
        """
        ...

    @property
    def Expression(self) -> Activity:
        """
        Get: Expression(self: FlowSwitch[T]) -> Activity[T]
        Set: Expression(self: FlowSwitch[T]) = value
        """
        ...



class ForEach(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ ForEach[T]() """
    @property
    def Body(self) -> ActivityAction:
        """
        Get: Body(self: ForEach[T]) -> ActivityAction[T]
        Set: Body(self: ForEach[T]) = value
        """
        ...

    @property
    def Values(self) -> InArgument:
        """
        Get: Values(self: ForEach[T]) -> InArgument[IEnumerable[T]]
        Set: Values(self: ForEach[T]) = value
        """
        ...



class HandleScope(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ HandleScope[THandle]() """
    @property
    def Body(self) -> Activity:
        """
        Get: Body(self: HandleScope[THandle]) -> Activity
        Set: Body(self: HandleScope[THandle]) = value
        """
        ...

    @property
    def Handle(self) -> InArgument:
        """
        Get: Handle(self: HandleScope[THandle]) -> InArgument[THandle]
        Set: Handle(self: HandleScope[THandle]) = value
        """
        ...



class If(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """
    If()
    If(condition: Expression[Func[ActivityContext, bool]])
    If(condition: Activity[bool])
    If(condition: InArgument[bool])
    """
    @property
    def Condition(self) -> InArgument:
        """
        Get: Condition(self: If) -> InArgument[bool]
        Set: Condition(self: If) = value
        """
        ...

    @property
    def Else(self) -> Activity:
        """
        Get: Else(self: If) -> Activity
        Set: Else(self: If) = value
        """
        ...

    @property
    def Then(self) -> Activity:
        """
        Get: Then(self: If) -> Activity
        Set: Then(self: If) = value
        """
        ...


    def __new__(cls, condition:Expression = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, condition: Expression[Func[ActivityContext, bool]])
        __new__(cls: type, condition: Activity[bool])
        __new__(cls: type, condition: InArgument[bool])
        """
        ...


class Interop(NativeActivity, ICustomTypeDescriptor): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ Interop() """
    @property
    def ActivityMetaProperties(self) -> IDictionary:
        """ Get: ActivityMetaProperties(self: Interop) -> IDictionary[str, object] """
        ...

    @property
    def ActivityProperties(self) -> IDictionary:
        """ Get: ActivityProperties(self: Interop) -> IDictionary[str, Argument] """
        ...

    @property
    def ActivityType(self) -> Type:
        """
        Get: ActivityType(self: Interop) -> Type
        Set: ActivityType(self: Interop) = value
        """
        ...



class InvokeAction: # skipped bases: <type 'object'>
    """ InvokeAction() """
    @property
    def Action(self) -> ActivityAction:
        """
        Get: Action(self: InvokeAction) -> ActivityAction
        Set: Action(self: InvokeAction) = value
        """
        ...

    @property
    def CacheId(self):
        ...

    @property
    def CanInduceIdle(self):
        ...

    @property
    def Constraints(self):
        ...

    @property
    def Implementation(self):
        ...

    @property
    def ImplementationVersion(self):
        ...


    def Abort(self, *args): #cannot find CLR method
        """ Abort(self: NativeActivity, context: NativeActivityAbortContext) """
        ...

    def CacheMetadata(self, *args): #cannot find CLR method
        """ CacheMetadata(self: InvokeAction, metadata: NativeActivityMetadata)CacheMetadata(self: NativeActivity, metadata: ActivityMetadata) """
        ...

    def Cancel(self, *args): #cannot find CLR method
        """ Cancel(self: NativeActivity, context: NativeActivityContext) """
        ...

    def Execute(self, *args): #cannot find CLR method
        """ Execute(self: InvokeAction, context: NativeActivityContext) """
        ...

    def OnCreateDynamicUpdateMap(self, *args): #cannot find CLR method
        """ OnCreateDynamicUpdateMap(self: NativeActivity, metadata: UpdateMapMetadata, originalActivity: Activity)OnCreateDynamicUpdateMap(self: NativeActivity, metadata: NativeActivityUpdateMapMetadata, originalActivity: Activity) """
        ...

    def UpdateInstance(self, *args): #cannot find CLR method
        """ UpdateInstance(self: NativeActivity, updateContext: NativeActivityUpdateContext) """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class InvokeDelegate(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ InvokeDelegate() """
    @property
    def Default(self) -> Activity:
        """
        Get: Default(self: InvokeDelegate) -> Activity
        Set: Default(self: InvokeDelegate) = value
        """
        ...

    @property
    def Delegate(self) -> ActivityDelegate:
        """
        Get: Delegate(self: InvokeDelegate) -> ActivityDelegate
        Set: Delegate(self: InvokeDelegate) = value
        """
        ...

    @property
    def DelegateArguments(self) -> IDictionary:
        """ Get: DelegateArguments(self: InvokeDelegate) -> IDictionary[str, Argument] """
        ...



class InvokeMethod(AsyncCodeActivity): # skipped bases: <type 'IAsyncCodeActivity'>, <type 'object'>
    """ InvokeMethod() """
    @property
    def GenericTypeArguments(self) -> Collection:
        """ Get: GenericTypeArguments(self: InvokeMethod) -> Collection[Type] """
        ...

    @property
    def MethodName(self) -> str:
        """
        Get: MethodName(self: InvokeMethod) -> str
        Set: MethodName(self: InvokeMethod) = value
        """
        ...

    @property
    def Parameters(self) -> Collection:
        """ Get: Parameters(self: InvokeMethod) -> Collection[Argument] """
        ...

    @property
    def Result(self) -> OutArgument:
        """
        Get: Result(self: InvokeMethod) -> OutArgument
        Set: Result(self: InvokeMethod) = value
        """
        ...

    @property
    def RunAsynchronously(self) -> bool:
        """
        Get: RunAsynchronously(self: InvokeMethod) -> bool
        Set: RunAsynchronously(self: InvokeMethod) = value
        """
        ...

    @property
    def TargetObject(self) -> InArgument:
        """
        Get: TargetObject(self: InvokeMethod) -> InArgument
        Set: TargetObject(self: InvokeMethod) = value
        """
        ...

    @property
    def TargetType(self) -> Type:
        """
        Get: TargetType(self: InvokeMethod) -> Type
        Set: TargetType(self: InvokeMethod) = value
        """
        ...



class NoPersistScope(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ NoPersistScope() """
    @property
    def Body(self) -> Activity:
        """
        Get: Body(self: NoPersistScope) -> Activity
        Set: Body(self: NoPersistScope) = value
        """
        ...



class Parallel(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ Parallel() """
    @property
    def Branches(self) -> Collection:
        """ Get: Branches(self: Parallel) -> Collection[Activity] """
        ...

    @property
    def CompletionCondition(self) -> Activity:
        """
        Get: CompletionCondition(self: Parallel) -> Activity[bool]
        Set: CompletionCondition(self: Parallel) = value
        """
        ...

    @property
    def Variables(self) -> Collection:
        """ Get: Variables(self: Parallel) -> Collection[Variable] """
        ...



class ParallelForEach(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ ParallelForEach[T]() """
    @property
    def Body(self) -> ActivityAction:
        """
        Get: Body(self: ParallelForEach[T]) -> ActivityAction[T]
        Set: Body(self: ParallelForEach[T]) = value
        """
        ...

    @property
    def CompletionCondition(self) -> Activity:
        """
        Get: CompletionCondition(self: ParallelForEach[T]) -> Activity[bool]
        Set: CompletionCondition(self: ParallelForEach[T]) = value
        """
        ...

    @property
    def Values(self) -> InArgument:
        """
        Get: Values(self: ParallelForEach[T]) -> InArgument[IEnumerable[T]]
        Set: Values(self: ParallelForEach[T]) = value
        """
        ...



class Persist(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ Persist() """
    pass

class Pick(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ Pick() """
    @property
    def Branches(self) -> Collection:
        """ Get: Branches(self: Pick) -> Collection[PickBranch] """
        ...



class PickBranch: # skipped bases: <type 'object'>, <type 'object'>
    """ PickBranch() """
    @property
    def Action(self) -> Activity:
        """
        Get: Action(self: PickBranch) -> Activity
        Set: Action(self: PickBranch) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: PickBranch) -> str
        Set: DisplayName(self: PickBranch) = value
        """
        ...

    @property
    def Trigger(self) -> Activity:
        """
        Get: Trigger(self: PickBranch) -> Activity
        Set: Trigger(self: PickBranch) = value
        """
        ...

    @property
    def Variables(self) -> Collection:
        """ Get: Variables(self: PickBranch) -> Collection[Variable] """
        ...



class RemoveFromCollection(CodeActivity): # skipped bases: <type 'object'>
    """ RemoveFromCollection[T]() """
    @property
    def Collection(self) -> InArgument:
        """
        Get: Collection(self: RemoveFromCollection[T]) -> InArgument[ICollection[T]]
        Set: Collection(self: RemoveFromCollection[T]) = value
        """
        ...

    @property
    def Item(self) -> InArgument:
        """
        Get: Item(self: RemoveFromCollection[T]) -> InArgument[T]
        Set: Item(self: RemoveFromCollection[T]) = value
        """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class Rethrow(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ Rethrow() """
    pass

class Sequence(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ Sequence() """
    @property
    def Activities(self) -> Collection:
        """ Get: Activities(self: Sequence) -> Collection[Activity] """
        ...

    @property
    def Variables(self) -> Collection:
        """ Get: Variables(self: Sequence) -> Collection[Variable] """
        ...



class State: # skipped bases: <type 'object'>, <type 'object'>
    """ State() """
    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: State) -> str
        Set: DisplayName(self: State) = value
        """
        ...

    @property
    def Entry(self) -> Activity:
        """
        Get: Entry(self: State) -> Activity
        Set: Entry(self: State) = value
        """
        ...

    @property
    def Exit(self) -> Activity:
        """
        Get: Exit(self: State) -> Activity
        Set: Exit(self: State) = value
        """
        ...

    @property
    def IsFinal(self) -> bool:
        """
        Get: IsFinal(self: State) -> bool
        Set: IsFinal(self: State) = value
        """
        ...

    @property
    def Transitions(self) -> Collection:
        """ Get: Transitions(self: State) -> Collection[Transition] """
        ...

    @property
    def Variables(self) -> Collection:
        """ Get: Variables(self: State) -> Collection[Variable] """
        ...



class StateMachine(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ StateMachine() """
    @property
    def InitialState(self) -> State:
        """
        Get: InitialState(self: StateMachine) -> State
        Set: InitialState(self: StateMachine) = value
        """
        ...

    @property
    def States(self) -> Collection:
        """ Get: States(self: StateMachine) -> Collection[State] """
        ...

    @property
    def Variables(self) -> Collection:
        """ Get: Variables(self: StateMachine) -> Collection[Variable] """
        ...



class Switch(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """
    Switch[T]()
    Switch[T](expression: Expression[Func[ActivityContext, T]])
    Switch[T](expression: Activity[T])
    Switch[T](expression: InArgument[T])
    """
    @property
    def Cases(self) -> IDictionary:
        """ Get: Cases(self: Switch[T]) -> IDictionary[T, Activity] """
        ...

    @property
    def Default(self) -> Activity:
        """
        Get: Default(self: Switch[T]) -> Activity
        Set: Default(self: Switch[T]) = value
        """
        ...

    @property
    def Expression(self) -> InArgument:
        """
        Get: Expression(self: Switch[T]) -> InArgument[T]
        Set: Expression(self: Switch[T]) = value
        """
        ...


    def __new__(cls, expression:Expression = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, expression: Expression[Func[ActivityContext, T]])
        __new__(cls: type, expression: Activity[T])
        __new__(cls: type, expression: InArgument[T])
        """
        ...


class TerminateWorkflow(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ TerminateWorkflow() """
    @property
    def Exception(self) -> InArgument:
        """
        Get: Exception(self: TerminateWorkflow) -> InArgument[Exception]
        Set: Exception(self: TerminateWorkflow) = value
        """
        ...

    @property
    def Reason(self) -> InArgument:
        """
        Get: Reason(self: TerminateWorkflow) -> InArgument[str]
        Set: Reason(self: TerminateWorkflow) = value
        """
        ...



class Throw(CodeActivity): # skipped bases: <type 'object'>
    """ Throw() """
    @property
    def Exception(self) -> InArgument:
        """
        Get: Exception(self: Throw) -> InArgument[Exception]
        Set: Exception(self: Throw) = value
        """
        ...



class TransactionScope(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ TransactionScope() """
    @property
    def AbortInstanceOnTransactionFailure(self) -> bool:
        """
        Get: AbortInstanceOnTransactionFailure(self: TransactionScope) -> bool
        Set: AbortInstanceOnTransactionFailure(self: TransactionScope) = value
        """
        ...

    @property
    def Body(self) -> Activity:
        """
        Get: Body(self: TransactionScope) -> Activity
        Set: Body(self: TransactionScope) = value
        """
        ...

    @property
    def IsolationLevel(self) -> IsolationLevel:
        """
        Get: IsolationLevel(self: TransactionScope) -> IsolationLevel
        Set: IsolationLevel(self: TransactionScope) = value
        """
        ...

    @property
    def Timeout(self) -> InArgument:
        """
        Get: Timeout(self: TransactionScope) -> InArgument[TimeSpan]
        Set: Timeout(self: TransactionScope) = value
        """
        ...


    def ShouldSerializeIsolationLevel(self) -> bool:
        """ ShouldSerializeIsolationLevel(self: TransactionScope) -> bool """
        ...

    def ShouldSerializeTimeout(self) -> bool:
        """ ShouldSerializeTimeout(self: TransactionScope) -> bool """
        ...


class Transition: # skipped bases: <type 'object'>, <type 'object'>
    """ Transition() """
    @property
    def Action(self) -> Activity:
        """
        Get: Action(self: Transition) -> Activity
        Set: Action(self: Transition) = value
        """
        ...

    @property
    def Condition(self) -> Activity:
        """
        Get: Condition(self: Transition) -> Activity[bool]
        Set: Condition(self: Transition) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: Transition) -> str
        Set: DisplayName(self: Transition) = value
        """
        ...

    @property
    def To(self) -> State:
        """
        Get: To(self: Transition) -> State
        Set: To(self: Transition) = value
        """
        ...

    @property
    def Trigger(self) -> Activity:
        """
        Get: Trigger(self: Transition) -> Activity
        Set: Trigger(self: Transition) = value
        """
        ...



class TryCatch(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """ TryCatch() """
    @property
    def Catches(self) -> Collection:
        """ Get: Catches(self: TryCatch) -> Collection[Catch] """
        ...

    @property
    def Finally(self) -> Activity:
        """
        Get: Finally(self: TryCatch) -> Activity
        Set: Finally(self: TryCatch) = value
        """
        ...

    @property
    def Try(self) -> Activity:
        """
        Get: Try(self: TryCatch) -> Activity
        Set: Try(self: TryCatch) = value
        """
        ...

    @property
    def Variables(self) -> Collection:
        """ Get: Variables(self: TryCatch) -> Collection[Variable] """
        ...



class While(NativeActivity): # skipped bases: <type 'IInstanceUpdatable'>, <type 'object'>
    """
    While()
    While(condition: Expression[Func[ActivityContext, bool]])
    While(condition: Activity[bool])
    """
    @property
    def Body(self) -> Activity:
        """
        Get: Body(self: While) -> Activity
        Set: Body(self: While) = value
        """
        ...

    @property
    def Condition(self) -> Activity:
        """
        Get: Condition(self: While) -> Activity[bool]
        Set: Condition(self: While) = value
        """
        ...

    @property
    def Variables(self) -> Collection:
        """ Get: Variables(self: While) -> Collection[Variable] """
        ...


    def __new__(cls, condition:Expression = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, condition: Expression[Func[ActivityContext, bool]])
        __new__(cls: type, condition: Activity[bool])
        """
        ...


class WorkflowTerminatedException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WorkflowTerminatedException()
    WorkflowTerminatedException(message: str)
    WorkflowTerminatedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class WriteLine(CodeActivity): # skipped bases: <type 'object'>
    """ WriteLine() """
    @property
    def Text(self) -> InArgument:
        """
        Get: Text(self: WriteLine) -> InArgument[str]
        Set: Text(self: WriteLine) = value
        """
        ...

    @property
    def TextWriter(self) -> InArgument:
        """
        Get: TextWriter(self: WriteLine) -> InArgument[TextWriter]
        Set: TextWriter(self: WriteLine) = value
        """
        ...



# variables with complex values

