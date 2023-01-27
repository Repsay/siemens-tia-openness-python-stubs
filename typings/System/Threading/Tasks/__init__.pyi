# encoding: utf-8
# module System.Threading.Tasks calls itself Tasks
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Action, AggregateException, Array, Enum, EventArgs, 
    IAsyncResult, Nullable, OperationCanceledException, TimeSpan)

from System.Collections import IEnumerable

from System.Collections.Concurrent import OrderablePartitioner

from System.Runtime.CompilerServices import (ConfiguredTaskAwaitable, 
    TaskAwaiter, YieldAwaitable)

from System.Threading import CancellationToken

from typing import Self

"""The following names are not found in the module: (BoundEvent, TResult, 
    field#)
"""

# no functions
# classes

class ConcurrentExclusiveSchedulerPair: # skipped bases: <type 'object'>, <type 'object'>
    """
    ConcurrentExclusiveSchedulerPair()
    ConcurrentExclusiveSchedulerPair(taskScheduler: TaskScheduler)
    ConcurrentExclusiveSchedulerPair(taskScheduler: TaskScheduler, maxConcurrencyLevel: int)
    ConcurrentExclusiveSchedulerPair(taskScheduler: TaskScheduler, maxConcurrencyLevel: int, maxItemsPerTask: int)
    """
    @property
    def Completion(self) -> Task:
        """ Get: Completion(self: ConcurrentExclusiveSchedulerPair) -> Task """
        ...

    @property
    def ConcurrentScheduler(self) -> TaskScheduler:
        """ Get: ConcurrentScheduler(self: ConcurrentExclusiveSchedulerPair) -> TaskScheduler """
        ...

    @property
    def ExclusiveScheduler(self) -> TaskScheduler:
        """ Get: ExclusiveScheduler(self: ConcurrentExclusiveSchedulerPair) -> TaskScheduler """
        ...


    def Complete(self): # -> 
        """ Complete(self: ConcurrentExclusiveSchedulerPair) """
        ...


class Parallel: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def For(fromInclusive:int, toExclusive:int, *__args:Action) -> ParallelLoopResult:
        """
        For(fromInclusive: int, toExclusive: int, body: Action[int]) -> ParallelLoopResult
        For(fromInclusive: Int64, toExclusive: Int64, body: Action[Int64]) -> ParallelLoopResult
        For(fromInclusive: int, toExclusive: int, parallelOptions: ParallelOptions, body: Action[int]) -> ParallelLoopResult
        For(fromInclusive: Int64, toExclusive: Int64, parallelOptions: ParallelOptions, body: Action[Int64]) -> ParallelLoopResult
        For(fromInclusive: int, toExclusive: int, body: Action[int, ParallelLoopState]) -> ParallelLoopResult
        For(fromInclusive: Int64, toExclusive: Int64, body: Action[Int64, ParallelLoopState]) -> ParallelLoopResult
        For(fromInclusive: int, toExclusive: int, parallelOptions: ParallelOptions, body: Action[int, ParallelLoopState]) -> ParallelLoopResult
        For(fromInclusive: Int64, toExclusive: Int64, parallelOptions: ParallelOptions, body: Action[Int64, ParallelLoopState]) -> ParallelLoopResult
        For[TLocal](fromInclusive: int, toExclusive: int, localInit: Func[TLocal], body: Func[int, ParallelLoopState, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult
        For[TLocal](fromInclusive: Int64, toExclusive: Int64, localInit: Func[TLocal], body: Func[Int64, ParallelLoopState, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult
        For[TLocal](fromInclusive: int, toExclusive: int, parallelOptions: ParallelOptions, localInit: Func[TLocal], body: Func[int, ParallelLoopState, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult
        For[TLocal](fromInclusive: Int64, toExclusive: Int64, parallelOptions: ParallelOptions, localInit: Func[TLocal], body: Func[Int64, ParallelLoopState, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult
        """
        ...

    @staticmethod
    def ForEach(source:OrderablePartitioner, *__args:Action) -> ParallelLoopResult:
        """
        ForEach[TSource](source: IEnumerable[TSource], parallelOptions: ParallelOptions, body: Action[TSource]) -> ParallelLoopResult
        ForEach[TSource](source: OrderablePartitioner[TSource], parallelOptions: ParallelOptions, body: Action[TSource, ParallelLoopState, Int64]) -> ParallelLoopResult
        ForEach[TSource](source: Partitioner[TSource], parallelOptions: ParallelOptions, body: Action[TSource, ParallelLoopState]) -> ParallelLoopResult
        ForEach[TSource](source: Partitioner[TSource], parallelOptions: ParallelOptions, body: Action[TSource]) -> ParallelLoopResult
        ForEach[(TSource, TLocal)](source: OrderablePartitioner[TSource], localInit: Func[TLocal], body: Func[TSource, ParallelLoopState, Int64, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult
        ForEach[(TSource, TLocal)](source: Partitioner[TSource], localInit: Func[TLocal], body: Func[TSource, ParallelLoopState, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult
        ForEach[TSource](source: OrderablePartitioner[TSource], body: Action[TSource, ParallelLoopState, Int64]) -> ParallelLoopResult
        ForEach[TSource](source: Partitioner[TSource], body: Action[TSource, ParallelLoopState]) -> ParallelLoopResult
        ForEach[TSource](source: Partitioner[TSource], body: Action[TSource]) -> ParallelLoopResult
        ForEach[(TSource, TLocal)](source: IEnumerable[TSource], parallelOptions: ParallelOptions, localInit: Func[TLocal], body: Func[TSource, ParallelLoopState, Int64, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult
        ForEach[(TSource, TLocal)](source: IEnumerable[TSource], localInit: Func[TLocal], body: Func[TSource, ParallelLoopState, Int64, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult
        ForEach[(TSource, TLocal)](source: IEnumerable[TSource], parallelOptions: ParallelOptions, localInit: Func[TLocal], body: Func[TSource, ParallelLoopState, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult
        ForEach[(TSource, TLocal)](source: IEnumerable[TSource], localInit: Func[TLocal], body: Func[TSource, ParallelLoopState, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult
        ForEach[TSource](source: IEnumerable[TSource], parallelOptions: ParallelOptions, body: Action[TSource, ParallelLoopState, Int64]) -> ParallelLoopResult
        ForEach[TSource](source: IEnumerable[TSource], body: Action[TSource, ParallelLoopState, Int64]) -> ParallelLoopResult
        ForEach[TSource](source: IEnumerable[TSource], parallelOptions: ParallelOptions, body: Action[TSource, ParallelLoopState]) -> ParallelLoopResult
        ForEach[TSource](source: IEnumerable[TSource], body: Action[TSource, ParallelLoopState]) -> ParallelLoopResult
        ForEach[TSource](source: IEnumerable[TSource], body: Action[TSource]) -> ParallelLoopResult
        ForEach[(TSource, TLocal)](source: Partitioner[TSource], parallelOptions: ParallelOptions, localInit: Func[TLocal], body: Func[TSource, ParallelLoopState, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult
        ForEach[(TSource, TLocal)](source: OrderablePartitioner[TSource], parallelOptions: ParallelOptions, localInit: Func[TLocal], body: Func[TSource, ParallelLoopState, Int64, TLocal, TLocal], localFinally: Action[TLocal]) -> ParallelLoopResult
        """
        ...

    @staticmethod
    def Invoke(*__args:Array): # -> 
        """ Invoke(*actions: Array[Action])Invoke(parallelOptions: ParallelOptions, *actions: Array[Action]) """
        ...

    __all__: list = ...


class ParallelLoopResult: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsCompleted(self) -> bool:
        """ Get: IsCompleted(self: ParallelLoopResult) -> bool """
        ...

    @property
    def LowestBreakIteration(self) -> Nullable:
        """ Get: LowestBreakIteration(self: ParallelLoopResult) -> Nullable[Int64] """
        ...



class ParallelLoopState: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsExceptional(self) -> bool:
        """ Get: IsExceptional(self: ParallelLoopState) -> bool """
        ...

    @property
    def IsStopped(self) -> bool:
        """ Get: IsStopped(self: ParallelLoopState) -> bool """
        ...

    @property
    def LowestBreakIteration(self) -> Nullable:
        """ Get: LowestBreakIteration(self: ParallelLoopState) -> Nullable[Int64] """
        ...

    @property
    def ShouldExitCurrentIteration(self) -> bool:
        """ Get: ShouldExitCurrentIteration(self: ParallelLoopState) -> bool """
        ...


    def Break(self): # -> 
        """ Break(self: ParallelLoopState) """
        ...

    def Stop(self): # -> 
        """ Stop(self: ParallelLoopState) """
        ...


class ParallelOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ ParallelOptions() """
    @property
    def CancellationToken(self) -> CancellationToken:
        """
        Get: CancellationToken(self: ParallelOptions) -> CancellationToken
        Set: CancellationToken(self: ParallelOptions) = value
        """
        ...

    @property
    def MaxDegreeOfParallelism(self) -> int:
        """
        Get: MaxDegreeOfParallelism(self: ParallelOptions) -> int
        Set: MaxDegreeOfParallelism(self: ParallelOptions) = value
        """
        ...

    @property
    def TaskScheduler(self) -> TaskScheduler:
        """
        Get: TaskScheduler(self: ParallelOptions) -> TaskScheduler
        Set: TaskScheduler(self: ParallelOptions) = value
        """
        ...



class Task: # skipped bases: <type 'object'>
    """
    Task(action: Action)
    Task(action: Action, cancellationToken: CancellationToken)
    Task(action: Action, creationOptions: TaskCreationOptions)
    Task(action: Action, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions)
    Task(action: Action[object], state: object)
    Task(action: Action[object], state: object, cancellationToken: CancellationToken)
    Task(action: Action[object], state: object, creationOptions: TaskCreationOptions)
    Task(action: Action[object], state: object, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions)
    """
    @property
    def AsyncState(self) -> object:
        """ Get: AsyncState(self: Task) -> object """
        ...

    @property
    def CompletedTask(self) -> Task:
        """ Get: CompletedTask() -> Task """
        ...

    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """ Get: CreationOptions(self: Task) -> TaskCreationOptions """
        ...

    @property
    def CurrentId(self) -> Nullable:
        """ Get: CurrentId() -> Nullable[int] """
        ...

    @property
    def Exception(self) -> AggregateException:
        """ Get: Exception(self: Task) -> AggregateException """
        ...

    @property
    def Factory(self) -> TaskFactory:
        """ Get: Factory() -> TaskFactory """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: Task) -> int """
        ...

    @property
    def IsCanceled(self) -> bool:
        """ Get: IsCanceled(self: Task) -> bool """
        ...

    @property
    def IsCompleted(self) -> bool:
        """ Get: IsCompleted(self: Task) -> bool """
        ...

    @property
    def IsFaulted(self) -> bool:
        """ Get: IsFaulted(self: Task) -> bool """
        ...

    @property
    def Status(self) -> TaskStatus:
        """ Get: Status(self: Task) -> TaskStatus """
        ...


    def ConfigureAwait(self, continueOnCapturedContext:bool) -> ConfiguredTaskAwaitable:
        """ ConfigureAwait(self: Task, continueOnCapturedContext: bool) -> ConfiguredTaskAwaitable """
        ...

    def ContinueWith(self, *__args:Action) -> Task:
        """
        ContinueWith(self: Task, continuationAction: Action[Task]) -> Task
        ContinueWith[TResult](self: Task, continuationFunction: Func[Task, object, TResult], state: object, scheduler: TaskScheduler) -> Task[TResult]
        ContinueWith[TResult](self: Task, continuationFunction: Func[Task, object, TResult], state: object, cancellationToken: CancellationToken) -> Task[TResult]
        ContinueWith[TResult](self: Task, continuationFunction: Func[Task, object, TResult], state: object) -> Task[TResult]
        ContinueWith[TResult](self: Task, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TResult]
        ContinueWith[TResult](self: Task, continuationFunction: Func[Task, TResult], continuationOptions: TaskContinuationOptions) -> Task[TResult]
        ContinueWith[TResult](self: Task, continuationFunction: Func[Task, TResult], scheduler: TaskScheduler) -> Task[TResult]
        ContinueWith[TResult](self: Task, continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken) -> Task[TResult]
        ContinueWith[TResult](self: Task, continuationFunction: Func[Task, TResult]) -> Task[TResult]
        ContinueWith(self: Task, continuationAction: Action[Task, object], state: object, cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task
        ContinueWith(self: Task, continuationAction: Action[Task, object], state: object, continuationOptions: TaskContinuationOptions) -> Task
        ContinueWith(self: Task, continuationAction: Action[Task, object], state: object, scheduler: TaskScheduler) -> Task
        ContinueWith(self: Task, continuationAction: Action[Task, object], state: object, cancellationToken: CancellationToken) -> Task
        ContinueWith(self: Task, continuationAction: Action[Task, object], state: object) -> Task
        ContinueWith(self: Task, continuationAction: Action[Task], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task
        ContinueWith(self: Task, continuationAction: Action[Task], continuationOptions: TaskContinuationOptions) -> Task
        ContinueWith(self: Task, continuationAction: Action[Task], scheduler: TaskScheduler) -> Task
        ContinueWith(self: Task, continuationAction: Action[Task], cancellationToken: CancellationToken) -> Task
        ContinueWith[TResult](self: Task, continuationFunction: Func[Task, object, TResult], state: object, continuationOptions: TaskContinuationOptions) -> Task[TResult]
        ContinueWith[TResult](self: Task, continuationFunction: Func[Task, object, TResult], state: object, cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TResult]
        """
        ...

    @staticmethod
    def Delay(*__args:TimeSpan) -> Task:
        """
        Delay(delay: TimeSpan) -> Task
        Delay(delay: TimeSpan, cancellationToken: CancellationToken) -> Task
        Delay(millisecondsDelay: int) -> Task
        Delay(millisecondsDelay: int, cancellationToken: CancellationToken) -> Task
        """
        ...

    def Dispose(self): # -> 
        """ Dispose(self: Task) """
        ...

    @staticmethod
    def FromCanceled(cancellationToken:CancellationToken) -> Task:
        """
        FromCanceled(cancellationToken: CancellationToken) -> Task
        FromCanceled[TResult](cancellationToken: CancellationToken) -> Task[TResult]
        """
        ...

    @staticmethod
    def FromException(exception:Exception) -> Task:
        """
        FromException(exception: Exception) -> Task
        FromException[TResult](exception: Exception) -> Task[TResult]
        """
        ...

    @staticmethod
    def FromResult(result) -> Task: # Not found arg types: {'result': 'TResult'}
        """ FromResult[TResult](result: TResult) -> Task[TResult] """
        ...

    def GetAwaiter(self) -> TaskAwaiter:
        """ GetAwaiter(self: Task) -> TaskAwaiter """
        ...

    @staticmethod
    def Run(*__args:Action) -> Task:
        """
        Run(action: Action) -> Task
        Run(action: Action, cancellationToken: CancellationToken) -> Task
        Run(function: Func[Task]) -> Task
        Run(function: Func[Task], cancellationToken: CancellationToken) -> Task
        Run[TResult](function: Func[TResult]) -> Task[TResult]
        Run[TResult](function: Func[TResult], cancellationToken: CancellationToken) -> Task[TResult]
        Run[TResult](function: Func[Task[TResult]]) -> Task[TResult]
        Run[TResult](function: Func[Task[TResult]], cancellationToken: CancellationToken) -> Task[TResult]
        """
        ...

    def RunSynchronously(self, scheduler:TaskScheduler = ...): # -> 
        """ RunSynchronously(self: Task)RunSynchronously(self: Task, scheduler: TaskScheduler) """
        ...

    def Start(self, scheduler:TaskScheduler = ...): # -> 
        """ Start(self: Task)Start(self: Task, scheduler: TaskScheduler) """
        ...

    def Wait(self, *__args:TimeSpan) -> bool:
        """
        Wait(self: Task)Wait(self: Task, timeout: TimeSpan) -> bool
        Wait(self: Task, cancellationToken: CancellationToken)Wait(self: Task, millisecondsTimeout: int) -> bool
        Wait(self: Task, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool
        """
        ...

    @staticmethod
    def WaitAll(tasks:Array, *__args:TimeSpan) -> bool:
        """
        WaitAll(*tasks: Array[Task])WaitAll(tasks: Array[Task], timeout: TimeSpan) -> bool
        WaitAll(tasks: Array[Task], millisecondsTimeout: int) -> bool
        WaitAll(tasks: Array[Task], cancellationToken: CancellationToken)WaitAll(tasks: Array[Task], millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool
        """
        ...

    @staticmethod
    def WaitAny(tasks:Array, *__args:TimeSpan) -> int:
        """
        WaitAny(*tasks: Array[Task]) -> int
        WaitAny(tasks: Array[Task], timeout: TimeSpan) -> int
        WaitAny(tasks: Array[Task], cancellationToken: CancellationToken) -> int
        WaitAny(tasks: Array[Task], millisecondsTimeout: int) -> int
        WaitAny(tasks: Array[Task], millisecondsTimeout: int, cancellationToken: CancellationToken) -> int
        """
        ...

    @staticmethod
    def WhenAll(tasks:IEnumerable) -> Task:
        """
        WhenAll(tasks: IEnumerable[Task]) -> Task
        WhenAll(*tasks: Array[Task]) -> Task
        WhenAll[TResult](tasks: IEnumerable[Task[TResult]]) -> Task[Array[TResult]]
        WhenAll[TResult](*tasks: Array[Task[TResult]]) -> Task[Array[TResult]]
        """
        ...

    @staticmethod
    def WhenAny(tasks:Array) -> Task:
        """
        WhenAny(*tasks: Array[Task]) -> Task[Task]
        WhenAny(tasks: IEnumerable[Task]) -> Task[Task]
        WhenAny[TResult](*tasks: Array[Task[TResult]]) -> Task[Task[TResult]]
        WhenAny[TResult](tasks: IEnumerable[Task[TResult]]) -> Task[Task[TResult]]
        """
        ...

    @staticmethod
    def Yield() -> YieldAwaitable:
        """ Yield() -> YieldAwaitable """
        ...

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        ...

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        ...

    def __new__(cls, action:Action, *__args:CancellationToken) -> Self:
        """
        __new__(cls: type, action: Action)
        __new__(cls: type, action: Action, cancellationToken: CancellationToken)
        __new__(cls: type, action: Action, creationOptions: TaskCreationOptions)
        __new__(cls: type, action: Action, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions)
        __new__(cls: type, action: Action[object], state: object)
        __new__(cls: type, action: Action[object], state: object, cancellationToken: CancellationToken)
        __new__(cls: type, action: Action[object], state: object, creationOptions: TaskCreationOptions)
        __new__(cls: type, action: Action[object], state: object, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions)
        """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...



class TaskCanceledException(OperationCanceledException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TaskCanceledException()
    TaskCanceledException(message: str)
    TaskCanceledException(message: str, innerException: Exception)
    TaskCanceledException(task: Task)
    """
    @property
    def Task(self) -> Task:
        """ Get: Task(self: TaskCanceledException) -> Task """
        ...


    SerializeObjectState = ...


class TaskCompletionSource: # skipped bases: <type 'object'>, <type 'object'>
    """
    TaskCompletionSource[TResult]()
    TaskCompletionSource[TResult](creationOptions: TaskCreationOptions)
    TaskCompletionSource[TResult](state: object)
    TaskCompletionSource[TResult](state: object, creationOptions: TaskCreationOptions)
    """
    @property
    def Task(self) -> Task:
        """ Get: Task(self: TaskCompletionSource[TResult]) -> Task[TResult] """
        ...


    def SetCanceled(self): # -> 
        """ SetCanceled(self: TaskCompletionSource[TResult]) """
        ...

    def SetException(self, *__args:Exception): # -> 
        """ SetException(self: TaskCompletionSource[TResult], exception: Exception)SetException(self: TaskCompletionSource[TResult], exceptions: IEnumerable[Exception]) """
        ...

    def SetResult(self, result): # ->  # Not found arg types: {'result': 'TResult'}
        """ SetResult(self: TaskCompletionSource[TResult], result: TResult) """
        ...

    def TrySetCanceled(self, cancellationToken:CancellationToken = ...) -> bool:
        """
        TrySetCanceled(self: TaskCompletionSource[TResult]) -> bool
        TrySetCanceled(self: TaskCompletionSource[TResult], cancellationToken: CancellationToken) -> bool
        """
        ...

    def TrySetException(self, *__args:Exception) -> bool:
        """
        TrySetException(self: TaskCompletionSource[TResult], exception: Exception) -> bool
        TrySetException(self: TaskCompletionSource[TResult], exceptions: IEnumerable[Exception]) -> bool
        """
        ...

    def TrySetResult(self, result) -> bool: # Not found arg types: {'result': 'TResult'}
        """ TrySetResult(self: TaskCompletionSource[TResult], result: TResult) -> bool """
        ...


class TaskContinuationOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TaskContinuationOptions, values: AttachedToParent (4), DenyChildAttach (8), ExecuteSynchronously (524288), HideScheduler (16), LazyCancellation (32), LongRunning (2), None (0), NotOnCanceled (262144), NotOnFaulted (131072), NotOnRanToCompletion (65536), OnlyOnCanceled (196608), OnlyOnFaulted (327680), OnlyOnRanToCompletion (393216), PreferFairness (1), RunContinuationsAsynchronously (64) """
    AttachedToParent: TaskContinuationOptions = ...
    DenyChildAttach: TaskContinuationOptions = ...
    ExecuteSynchronously: TaskContinuationOptions = ...
    HideScheduler: TaskContinuationOptions = ...
    LazyCancellation: TaskContinuationOptions = ...
    LongRunning: TaskContinuationOptions = ...
    NotOnCanceled: TaskContinuationOptions = ...
    NotOnFaulted: TaskContinuationOptions = ...
    NotOnRanToCompletion: TaskContinuationOptions = ...
    OnlyOnCanceled: TaskContinuationOptions = ...
    OnlyOnFaulted: TaskContinuationOptions = ...
    OnlyOnRanToCompletion: TaskContinuationOptions = ...
    PreferFairness: TaskContinuationOptions = ...
    RunContinuationsAsynchronously: TaskContinuationOptions = ...
    value__ = ...


class TaskCreationOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TaskCreationOptions, values: AttachedToParent (4), DenyChildAttach (8), HideScheduler (16), LongRunning (2), None (0), PreferFairness (1), RunContinuationsAsynchronously (64) """
    AttachedToParent: TaskCreationOptions = ...
    DenyChildAttach: TaskCreationOptions = ...
    HideScheduler: TaskCreationOptions = ...
    LongRunning: TaskCreationOptions = ...
    PreferFairness: TaskCreationOptions = ...
    RunContinuationsAsynchronously: TaskCreationOptions = ...
    value__ = ...


class TaskExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Unwrap(task:Task) -> Task:
        """
        Unwrap(task: Task[Task]) -> Task
        Unwrap[TResult](task: Task[Task[TResult]]) -> Task[TResult]
        """
        ...

    __all__: list = ...


class TaskFactory: # skipped bases: <type 'object'>
    """
    TaskFactory()
    TaskFactory(cancellationToken: CancellationToken)
    TaskFactory(scheduler: TaskScheduler)
    TaskFactory(creationOptions: TaskCreationOptions, continuationOptions: TaskContinuationOptions)
    TaskFactory(cancellationToken: CancellationToken, creationOptions: TaskCreationOptions, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler)
    """
    @property
    def CancellationToken(self) -> CancellationToken:
        """ Get: CancellationToken(self: TaskFactory) -> CancellationToken """
        ...

    @property
    def ContinuationOptions(self) -> TaskContinuationOptions:
        """ Get: ContinuationOptions(self: TaskFactory) -> TaskContinuationOptions """
        ...

    @property
    def CreationOptions(self) -> TaskCreationOptions:
        """ Get: CreationOptions(self: TaskFactory) -> TaskCreationOptions """
        ...

    @property
    def Scheduler(self) -> TaskScheduler:
        """ Get: Scheduler(self: TaskFactory) -> TaskScheduler """
        ...


    def ContinueWhenAll(self, tasks:Array, *__args:Action) -> Task:
        """
        ContinueWhenAll(self: TaskFactory, tasks: Array[Task], continuationAction: Action[Array[Task]]) -> Task
        ContinueWhenAll(self: TaskFactory, tasks: Array[Task], continuationAction: Action[Array[Task]], cancellationToken: CancellationToken) -> Task
        ContinueWhenAll(self: TaskFactory, tasks: Array[Task], continuationAction: Action[Array[Task]], continuationOptions: TaskContinuationOptions) -> Task
        ContinueWhenAll(self: TaskFactory, tasks: Array[Task], continuationAction: Action[Array[Task]], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task
        ContinueWhenAll[TAntecedentResult](self: TaskFactory, tasks: Array[Task[TAntecedentResult]], continuationAction: Action[Array[Task[TAntecedentResult]]]) -> Task
        ContinueWhenAll[TAntecedentResult](self: TaskFactory, tasks: Array[Task[TAntecedentResult]], continuationAction: Action[Array[Task[TAntecedentResult]]], cancellationToken: CancellationToken) -> Task
        ContinueWhenAll[TAntecedentResult](self: TaskFactory, tasks: Array[Task[TAntecedentResult]], continuationAction: Action[Array[Task[TAntecedentResult]]], continuationOptions: TaskContinuationOptions) -> Task
        ContinueWhenAll[TAntecedentResult](self: TaskFactory, tasks: Array[Task[TAntecedentResult]], continuationAction: Action[Array[Task[TAntecedentResult]]], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task
        ContinueWhenAll[TResult](self: TaskFactory, tasks: Array[Task], continuationFunction: Func[Array[Task], TResult]) -> Task[TResult]
        ContinueWhenAll[TResult](self: TaskFactory, tasks: Array[Task], continuationFunction: Func[Array[Task], TResult], cancellationToken: CancellationToken) -> Task[TResult]
        ContinueWhenAll[TResult](self: TaskFactory, tasks: Array[Task], continuationFunction: Func[Array[Task], TResult], continuationOptions: TaskContinuationOptions) -> Task[TResult]
        ContinueWhenAll[TResult](self: TaskFactory, tasks: Array[Task], continuationFunction: Func[Array[Task], TResult], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TResult]
        ContinueWhenAll[(TAntecedentResult, TResult)](self: TaskFactory, tasks: Array[Task[TAntecedentResult]], continuationFunction: Func[Array[Task[TAntecedentResult]], TResult]) -> Task[TResult]
        ContinueWhenAll[(TAntecedentResult, TResult)](self: TaskFactory, tasks: Array[Task[TAntecedentResult]], continuationFunction: Func[Array[Task[TAntecedentResult]], TResult], cancellationToken: CancellationToken) -> Task[TResult]
        ContinueWhenAll[(TAntecedentResult, TResult)](self: TaskFactory, tasks: Array[Task[TAntecedentResult]], continuationFunction: Func[Array[Task[TAntecedentResult]], TResult], continuationOptions: TaskContinuationOptions) -> Task[TResult]
        ContinueWhenAll[(TAntecedentResult, TResult)](self: TaskFactory, tasks: Array[Task[TAntecedentResult]], continuationFunction: Func[Array[Task[TAntecedentResult]], TResult], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TResult]
        """
        ...

    def ContinueWhenAny(self, tasks:Array, *__args:Action) -> Task:
        """
        ContinueWhenAny(self: TaskFactory, tasks: Array[Task], continuationAction: Action[Task]) -> Task
        ContinueWhenAny(self: TaskFactory, tasks: Array[Task], continuationAction: Action[Task], cancellationToken: CancellationToken) -> Task
        ContinueWhenAny(self: TaskFactory, tasks: Array[Task], continuationAction: Action[Task], continuationOptions: TaskContinuationOptions) -> Task
        ContinueWhenAny(self: TaskFactory, tasks: Array[Task], continuationAction: Action[Task], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task
        ContinueWhenAny[TResult](self: TaskFactory, tasks: Array[Task], continuationFunction: Func[Task, TResult]) -> Task[TResult]
        ContinueWhenAny[TResult](self: TaskFactory, tasks: Array[Task], continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken) -> Task[TResult]
        ContinueWhenAny[TResult](self: TaskFactory, tasks: Array[Task], continuationFunction: Func[Task, TResult], continuationOptions: TaskContinuationOptions) -> Task[TResult]
        ContinueWhenAny[TResult](self: TaskFactory, tasks: Array[Task], continuationFunction: Func[Task, TResult], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TResult]
        ContinueWhenAny[(TAntecedentResult, TResult)](self: TaskFactory, tasks: Array[Task[TAntecedentResult]], continuationFunction: Func[Task[TAntecedentResult], TResult]) -> Task[TResult]
        ContinueWhenAny[(TAntecedentResult, TResult)](self: TaskFactory, tasks: Array[Task[TAntecedentResult]], continuationFunction: Func[Task[TAntecedentResult], TResult], cancellationToken: CancellationToken) -> Task[TResult]
        ContinueWhenAny[(TAntecedentResult, TResult)](self: TaskFactory, tasks: Array[Task[TAntecedentResult]], continuationFunction: Func[Task[TAntecedentResult], TResult], continuationOptions: TaskContinuationOptions) -> Task[TResult]
        ContinueWhenAny[(TAntecedentResult, TResult)](self: TaskFactory, tasks: Array[Task[TAntecedentResult]], continuationFunction: Func[Task[TAntecedentResult], TResult], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task[TResult]
        ContinueWhenAny[TAntecedentResult](self: TaskFactory, tasks: Array[Task[TAntecedentResult]], continuationAction: Action[Task[TAntecedentResult]]) -> Task
        ContinueWhenAny[TAntecedentResult](self: TaskFactory, tasks: Array[Task[TAntecedentResult]], continuationAction: Action[Task[TAntecedentResult]], cancellationToken: CancellationToken) -> Task
        ContinueWhenAny[TAntecedentResult](self: TaskFactory, tasks: Array[Task[TAntecedentResult]], continuationAction: Action[Task[TAntecedentResult]], continuationOptions: TaskContinuationOptions) -> Task
        ContinueWhenAny[TAntecedentResult](self: TaskFactory, tasks: Array[Task[TAntecedentResult]], continuationAction: Action[Task[TAntecedentResult]], cancellationToken: CancellationToken, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler) -> Task
        """
        ...

    def FromAsync(self, *__args) -> Task:
        """
        FromAsync(self: TaskFactory, asyncResult: IAsyncResult, endMethod: Action[IAsyncResult]) -> Task
        FromAsync[(TArg1, TArg2, TResult)](self: TaskFactory, beginMethod: Func[TArg1, TArg2, AsyncCallback, object, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, state: object, creationOptions: TaskCreationOptions) -> Task[TResult]
        FromAsync[(TArg1, TArg2, TResult)](self: TaskFactory, beginMethod: Func[TArg1, TArg2, AsyncCallback, object, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, state: object) -> Task[TResult]
        FromAsync[(TArg1, TResult)](self: TaskFactory, beginMethod: Func[TArg1, AsyncCallback, object, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, state: object, creationOptions: TaskCreationOptions) -> Task[TResult]
        FromAsync[(TArg1, TResult)](self: TaskFactory, beginMethod: Func[TArg1, AsyncCallback, object, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, state: object) -> Task[TResult]
        FromAsync[TResult](self: TaskFactory, beginMethod: Func[AsyncCallback, object, IAsyncResult], endMethod: Func[IAsyncResult, TResult], state: object, creationOptions: TaskCreationOptions) -> Task[TResult]
        FromAsync[TResult](self: TaskFactory, beginMethod: Func[AsyncCallback, object, IAsyncResult], endMethod: Func[IAsyncResult, TResult], state: object) -> Task[TResult]
        FromAsync[TResult](self: TaskFactory, asyncResult: IAsyncResult, endMethod: Func[IAsyncResult, TResult], creationOptions: TaskCreationOptions, scheduler: TaskScheduler) -> Task[TResult]
        FromAsync[TResult](self: TaskFactory, asyncResult: IAsyncResult, endMethod: Func[IAsyncResult, TResult], creationOptions: TaskCreationOptions) -> Task[TResult]
        FromAsync[TResult](self: TaskFactory, asyncResult: IAsyncResult, endMethod: Func[IAsyncResult, TResult]) -> Task[TResult]
        FromAsync[(TArg1, TArg2, TArg3)](self: TaskFactory, beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, object, IAsyncResult], endMethod: Action[IAsyncResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: object, creationOptions: TaskCreationOptions) -> Task
        FromAsync[(TArg1, TArg2, TArg3)](self: TaskFactory, beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, object, IAsyncResult], endMethod: Action[IAsyncResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: object) -> Task
        FromAsync[(TArg1, TArg2)](self: TaskFactory, beginMethod: Func[TArg1, TArg2, AsyncCallback, object, IAsyncResult], endMethod: Action[IAsyncResult], arg1: TArg1, arg2: TArg2, state: object, creationOptions: TaskCreationOptions) -> Task
        FromAsync[(TArg1, TArg2)](self: TaskFactory, beginMethod: Func[TArg1, TArg2, AsyncCallback, object, IAsyncResult], endMethod: Action[IAsyncResult], arg1: TArg1, arg2: TArg2, state: object) -> Task
        FromAsync[TArg1](self: TaskFactory, beginMethod: Func[TArg1, AsyncCallback, object, IAsyncResult], endMethod: Action[IAsyncResult], arg1: TArg1, state: object, creationOptions: TaskCreationOptions) -> Task
        FromAsync[TArg1](self: TaskFactory, beginMethod: Func[TArg1, AsyncCallback, object, IAsyncResult], endMethod: Action[IAsyncResult], arg1: TArg1, state: object) -> Task
        FromAsync(self: TaskFactory, beginMethod: Func[AsyncCallback, object, IAsyncResult], endMethod: Action[IAsyncResult], state: object, creationOptions: TaskCreationOptions) -> Task
        FromAsync(self: TaskFactory, beginMethod: Func[AsyncCallback, object, IAsyncResult], endMethod: Action[IAsyncResult], state: object) -> Task
        FromAsync(self: TaskFactory, asyncResult: IAsyncResult, endMethod: Action[IAsyncResult], creationOptions: TaskCreationOptions, scheduler: TaskScheduler) -> Task
        FromAsync(self: TaskFactory, asyncResult: IAsyncResult, endMethod: Action[IAsyncResult], creationOptions: TaskCreationOptions) -> Task
        FromAsync[(TArg1, TArg2, TArg3, TResult)](self: TaskFactory, beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, object, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: object) -> Task[TResult]
        FromAsync[(TArg1, TArg2, TArg3, TResult)](self: TaskFactory, beginMethod: Func[TArg1, TArg2, TArg3, AsyncCallback, object, IAsyncResult], endMethod: Func[IAsyncResult, TResult], arg1: TArg1, arg2: TArg2, arg3: TArg3, state: object, creationOptions: TaskCreationOptions) -> Task[TResult]
        """
        ...

    def StartNew(self, *__args:Action) -> Task:
        """
        StartNew(self: TaskFactory, action: Action[object], state: object) -> Task
        StartNew(self: TaskFactory, action: Action) -> Task
        StartNew(self: TaskFactory, action: Action, cancellationToken: CancellationToken) -> Task
        StartNew(self: TaskFactory, action: Action, creationOptions: TaskCreationOptions) -> Task
        StartNew(self: TaskFactory, action: Action, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions, scheduler: TaskScheduler) -> Task
        StartNew(self: TaskFactory, action: Action[object], state: object, cancellationToken: CancellationToken) -> Task
        StartNew(self: TaskFactory, action: Action[object], state: object, creationOptions: TaskCreationOptions) -> Task
        StartNew(self: TaskFactory, action: Action[object], state: object, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions, scheduler: TaskScheduler) -> Task
        StartNew[TResult](self: TaskFactory, function: Func[TResult]) -> Task[TResult]
        StartNew[TResult](self: TaskFactory, function: Func[TResult], cancellationToken: CancellationToken) -> Task[TResult]
        StartNew[TResult](self: TaskFactory, function: Func[TResult], creationOptions: TaskCreationOptions) -> Task[TResult]
        StartNew[TResult](self: TaskFactory, function: Func[TResult], cancellationToken: CancellationToken, creationOptions: TaskCreationOptions, scheduler: TaskScheduler) -> Task[TResult]
        StartNew[TResult](self: TaskFactory, function: Func[object, TResult], state: object) -> Task[TResult]
        StartNew[TResult](self: TaskFactory, function: Func[object, TResult], state: object, cancellationToken: CancellationToken) -> Task[TResult]
        StartNew[TResult](self: TaskFactory, function: Func[object, TResult], state: object, creationOptions: TaskCreationOptions) -> Task[TResult]
        StartNew[TResult](self: TaskFactory, function: Func[object, TResult], state: object, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions, scheduler: TaskScheduler) -> Task[TResult]
        """
        ...

    def __new__(cls, *__args:CancellationToken) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, cancellationToken: CancellationToken)
        __new__(cls: type, scheduler: TaskScheduler)
        __new__(cls: type, creationOptions: TaskCreationOptions, continuationOptions: TaskContinuationOptions)
        __new__(cls: type, cancellationToken: CancellationToken, creationOptions: TaskCreationOptions, continuationOptions: TaskContinuationOptions, scheduler: TaskScheduler)
        """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class TaskScheduler: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> TaskScheduler:
        """ Get: Current() -> TaskScheduler """
        ...

    @property
    def Default(self) -> TaskScheduler:
        """ Get: Default() -> TaskScheduler """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: TaskScheduler) -> int """
        ...

    @property
    def MaximumConcurrencyLevel(self) -> int:
        """ Get: MaximumConcurrencyLevel(self: TaskScheduler) -> int """
        ...


    @staticmethod
    def FromCurrentSynchronizationContext() -> TaskScheduler:
        """ FromCurrentSynchronizationContext() -> TaskScheduler """
        ...

    def GetScheduledTasks(self, *args): #cannot find CLR method
        """ GetScheduledTasks(self: TaskScheduler) -> IEnumerable[Task] """
        ...

    def QueueTask(self, *args): #cannot find CLR method
        """ QueueTask(self: TaskScheduler, task: Task) """
        ...

    def TryDequeue(self, *args): #cannot find CLR method
        """ TryDequeue(self: TaskScheduler, task: Task) -> bool """
        ...

    def TryExecuteTask(self, *args): #cannot find CLR method
        """ TryExecuteTask(self: TaskScheduler, task: Task) -> bool """
        ...

    def TryExecuteTaskInline(self, *args): #cannot find CLR method
        """ TryExecuteTaskInline(self: TaskScheduler, task: Task, taskWasPreviouslyQueued: bool) -> bool """
        ...

    UnobservedTaskException = ...


class TaskSchedulerException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TaskSchedulerException()
    TaskSchedulerException(message: str)
    TaskSchedulerException(innerException: Exception)
    TaskSchedulerException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class TaskStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TaskStatus, values: Canceled (6), Created (0), Faulted (7), RanToCompletion (5), Running (3), WaitingForActivation (1), WaitingForChildrenToComplete (4), WaitingToRun (2) """
    Canceled: TaskStatus = ...
    Created: TaskStatus = ...
    Faulted: TaskStatus = ...
    RanToCompletion: TaskStatus = ...
    Running: TaskStatus = ...
    value__ = ...
    WaitingForActivation: TaskStatus = ...
    WaitingForChildrenToComplete: TaskStatus = ...
    WaitingToRun: TaskStatus = ...


class UnobservedTaskExceptionEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ UnobservedTaskExceptionEventArgs(exception: AggregateException) """
    @property
    def Exception(self) -> AggregateException:
        """ Get: Exception(self: UnobservedTaskExceptionEventArgs) -> AggregateException """
        ...

    @property
    def Observed(self) -> bool:
        """ Get: Observed(self: UnobservedTaskExceptionEventArgs) -> bool """
        ...


    def SetObserved(self): # -> 
        """ SetObserved(self: UnobservedTaskExceptionEventArgs) """
        ...

    def __new__(cls, exception:AggregateException) -> Self:
        """ __new__(cls: type, exception: AggregateException) """
        ...


