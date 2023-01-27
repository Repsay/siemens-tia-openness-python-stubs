# encoding: utf-8
# module System.Threading calls itself Threading
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Runtime.WindowsRuntime, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.JScript import Context

from Microsoft.Win32.SafeHandles import SafeWaitHandle

from System import (Action, AppDomain, ApplicationException, Array, 
    AsyncCallback, Byte, Enum, EventArgs, IAsyncResult, IDisposable, 
    IEquatable, Int64, IntPtr, LocalDataStoreSlot, MarshalByRefObject, 
    MulticastDelegate, SystemException, TimeSpan, UInt32)

from System.Collections import IList

from System.Globalization import CultureInfo

from System.Runtime.ConstrainedExecution import CriticalFinalizerObject

from System.Runtime.InteropServices import SafeHandle, _Thread

from System.Runtime.Serialization import ISerializable

from System.Security.AccessControl import (EventWaitHandleRights, 
    EventWaitHandleSecurity, MutexRights, MutexSecurity, SemaphoreRights, 
    SemaphoreSecurity)

from System.Security.Principal import IPrincipal

from System.Threading.Tasks import Task

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, Func, 
    IAsyncLocal, IDeferredDisposable, Self -> bool, T, field#)
"""

# no functions
# classes

class AbandonedMutexException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    AbandonedMutexException()
    AbandonedMutexException(message: str)
    AbandonedMutexException(message: str, inner: Exception)
    AbandonedMutexException(location: int, handle: WaitHandle)
    AbandonedMutexException(message: str, location: int, handle: WaitHandle)
    AbandonedMutexException(message: str, inner: Exception, location: int, handle: WaitHandle)
    """
    @property
    def Mutex(self) -> Mutex:
        """ Get: Mutex(self: AbandonedMutexException) -> Mutex """
        ...

    @property
    def MutexIndex(self) -> int:
        """ Get: MutexIndex(self: AbandonedMutexException) -> int """
        ...


    SerializeObjectState = ...


class ApartmentState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ApartmentState, values: MTA (1), STA (0), Unknown (2) """
    MTA: ApartmentState = ...
    STA: ApartmentState = ...
    Unknown: ApartmentState = ...
    value__ = ...


class AsyncFlowControl(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def Equals(self, obj:object) -> bool:
        """
        Equals(self: AsyncFlowControl, obj: object) -> bool
        Equals(self: AsyncFlowControl, obj: AsyncFlowControl) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: AsyncFlowControl) -> int """
        ...

    def Undo(self): # -> 
        """ Undo(self: AsyncFlowControl) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AsyncLocal(IAsyncLocal): # skipped bases: <type 'object'>
    """
    AsyncLocal[T]()
    AsyncLocal[T](valueChangedHandler: Action[AsyncLocalValueChangedArgs[T]])
    """
    @property
    def Value(self): # -> T
        """
        Get: Value(self: AsyncLocal[T]) -> T
        Set: Value(self: AsyncLocal[T]) = value
        """
        ...



class AsyncLocalValueChangedArgs: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CurrentValue(self): # -> T
        """ Get: CurrentValue(self: AsyncLocalValueChangedArgs[T]) -> T """
        ...

    @property
    def PreviousValue(self): # -> T
        """ Get: PreviousValue(self: AsyncLocalValueChangedArgs[T]) -> T """
        ...

    @property
    def ThreadContextChanged(self) -> bool:
        """ Get: ThreadContextChanged(self: AsyncLocalValueChangedArgs[T]) -> bool """
        ...



class WaitHandle(IDisposable, MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Handle(self) -> IntPtr:
        """
        Get: Handle(self: WaitHandle) -> IntPtr
        Set: Handle(self: WaitHandle) = value
        """
        ...

    @property
    def SafeWaitHandle(self) -> SafeWaitHandle:
        """
        Get: SafeWaitHandle(self: WaitHandle) -> SafeWaitHandle
        Set: SafeWaitHandle(self: WaitHandle) = value
        """
        ...


    def Close(self): # -> 
        """ Close(self: WaitHandle) """
        ...

    @staticmethod
    def SignalAndWait(toSignal, toWaitOn, *__args) -> bool:
        """
        SignalAndWait(toSignal: WaitHandle, toWaitOn: WaitHandle) -> bool
        SignalAndWait(toSignal: WaitHandle, toWaitOn: WaitHandle, timeout: TimeSpan, exitContext: bool) -> bool
        SignalAndWait(toSignal: WaitHandle, toWaitOn: WaitHandle, millisecondsTimeout: int, exitContext: bool) -> bool
        """
        ...

    @staticmethod
    def WaitAll(waitHandles:Array, *__args:int) -> bool:
        """
        WaitAll(waitHandles: Array[WaitHandle], millisecondsTimeout: int, exitContext: bool) -> bool
        WaitAll(waitHandles: Array[WaitHandle], timeout: TimeSpan, exitContext: bool) -> bool
        WaitAll(waitHandles: Array[WaitHandle]) -> bool
        WaitAll(waitHandles: Array[WaitHandle], millisecondsTimeout: int) -> bool
        WaitAll(waitHandles: Array[WaitHandle], timeout: TimeSpan) -> bool
        """
        ...

    @staticmethod
    def WaitAny(waitHandles:Array, *__args:TimeSpan) -> int:
        """
        WaitAny(waitHandles: Array[WaitHandle], millisecondsTimeout: int, exitContext: bool) -> int
        WaitAny(waitHandles: Array[WaitHandle], timeout: TimeSpan, exitContext: bool) -> int
        WaitAny(waitHandles: Array[WaitHandle], timeout: TimeSpan) -> int
        WaitAny(waitHandles: Array[WaitHandle]) -> int
        WaitAny(waitHandles: Array[WaitHandle], millisecondsTimeout: int) -> int
        """
        ...

    def WaitOne(self, *__args:int) -> bool:
        """
        WaitOne(self: WaitHandle, millisecondsTimeout: int, exitContext: bool) -> bool
        WaitOne(self: WaitHandle, timeout: TimeSpan, exitContext: bool) -> bool
        WaitOne(self: WaitHandle) -> bool
        WaitOne(self: WaitHandle, millisecondsTimeout: int) -> bool
        WaitOne(self: WaitHandle, timeout: TimeSpan) -> bool
        """
        ...

    InvalidHandle: IntPtr = ...
    WaitTimeout: int = ...


class EventWaitHandle(WaitHandle): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    EventWaitHandle(initialState: bool, mode: EventResetMode)
    EventWaitHandle(initialState: bool, mode: EventResetMode, name: str)
    EventWaitHandle(initialState: bool, mode: EventResetMode, name: str) -> bool
    EventWaitHandle(initialState: bool, mode: EventResetMode, name: str, eventSecurity: EventWaitHandleSecurity) -> bool
    """
    def GetAccessControl(self) -> EventWaitHandleSecurity:
        """ GetAccessControl(self: EventWaitHandle) -> EventWaitHandleSecurity """
        ...

    @staticmethod
    def OpenExisting(name:str, rights:EventWaitHandleRights = ...) -> EventWaitHandle:
        """
        OpenExisting(name: str) -> EventWaitHandle
        OpenExisting(name: str, rights: EventWaitHandleRights) -> EventWaitHandle
        """
        ...

    def Reset(self) -> bool:
        """ Reset(self: EventWaitHandle) -> bool """
        ...

    def Set(self) -> bool:
        """ Set(self: EventWaitHandle) -> bool """
        ...

    def SetAccessControl(self, eventSecurity:EventWaitHandleSecurity): # -> 
        """ SetAccessControl(self: EventWaitHandle, eventSecurity: EventWaitHandleSecurity) """
        ...

    @staticmethod
    def TryOpenExisting(name:str, *__args:EventWaitHandleRights) -> Tuple_[bool, EventWaitHandle]:
        """
        TryOpenExisting(name: str) -> (bool, EventWaitHandle)
        TryOpenExisting(name: str, rights: EventWaitHandleRights) -> (bool, EventWaitHandle)
        """
        ...

    def __new__(cls, initialState, mode, name=None, createdNew=None, eventSecurity=None) -> Self:
        """
        __new__(cls: type, initialState: bool, mode: EventResetMode)
        __new__(cls: type, initialState: bool, mode: EventResetMode, name: str)
        __new__(cls: type, initialState: bool, mode: EventResetMode, name: str) -> bool
        __new__(cls: type, initialState: bool, mode: EventResetMode, name: str, eventSecurity: EventWaitHandleSecurity) -> bool
        """
        ...


class AutoResetEvent(EventWaitHandle): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ AutoResetEvent(initialState: bool) """
    pass

class Barrier(IDisposable): # skipped bases: <type 'object'>
    """
    Barrier(participantCount: int)
    Barrier(participantCount: int, postPhaseAction: Action[Barrier])
    """
    @property
    def CurrentPhaseNumber(self) -> Int64:
        """ Get: CurrentPhaseNumber(self: Barrier) -> Int64 """
        ...

    @property
    def ParticipantCount(self) -> int:
        """ Get: ParticipantCount(self: Barrier) -> int """
        ...

    @property
    def ParticipantsRemaining(self) -> int:
        """ Get: ParticipantsRemaining(self: Barrier) -> int """
        ...


    def AddParticipant(self) -> Int64:
        """ AddParticipant(self: Barrier) -> Int64 """
        ...

    def AddParticipants(self, participantCount:int) -> Int64:
        """ AddParticipants(self: Barrier, participantCount: int) -> Int64 """
        ...

    def RemoveParticipant(self): # -> 
        """ RemoveParticipant(self: Barrier) """
        ...

    def RemoveParticipants(self, participantCount:int): # -> 
        """ RemoveParticipants(self: Barrier, participantCount: int) """
        ...

    def SignalAndWait(self, *__args:CancellationToken): # -> 
        """
        SignalAndWait(self: Barrier)SignalAndWait(self: Barrier, cancellationToken: CancellationToken)SignalAndWait(self: Barrier, timeout: TimeSpan) -> bool
        SignalAndWait(self: Barrier, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool
        SignalAndWait(self: Barrier, millisecondsTimeout: int) -> bool
        SignalAndWait(self: Barrier, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool
        """
        ...


class BarrierPostPhaseException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    BarrierPostPhaseException()
    BarrierPostPhaseException(innerException: Exception)
    BarrierPostPhaseException(message: str)
    BarrierPostPhaseException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class CancellationToken: # skipped bases: <type 'object'>, <type 'object'>
    """ CancellationToken(canceled: bool) """
    @property
    def CanBeCanceled(self) -> bool:
        """ Get: CanBeCanceled(self: CancellationToken) -> bool """
        ...

    @property
    def IsCancellationRequested(self) -> bool:
        """ Get: IsCancellationRequested(self: CancellationToken) -> bool """
        ...

    @property
    def WaitHandle(self) -> WaitHandle:
        """ Get: WaitHandle(self: CancellationToken) -> WaitHandle """
        ...


    def Equals(self, other:CancellationToken) -> bool:
        """
        Equals(self: CancellationToken, other: CancellationToken) -> bool
        Equals(self: CancellationToken, other: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CancellationToken) -> int """
        ...

    def Register(self, callback:Action, *__args:bool) -> CancellationTokenRegistration:
        """
        Register(self: CancellationToken, callback: Action) -> CancellationTokenRegistration
        Register(self: CancellationToken, callback: Action, useSynchronizationContext: bool) -> CancellationTokenRegistration
        Register(self: CancellationToken, callback: Action[object], state: object) -> CancellationTokenRegistration
        Register(self: CancellationToken, callback: Action[object], state: object, useSynchronizationContext: bool) -> CancellationTokenRegistration
        """
        ...

    def ThrowIfCancellationRequested(self): # -> 
        """ ThrowIfCancellationRequested(self: CancellationToken) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CancellationTokenRegistration(IDisposable, IEquatable): # skipped bases: <type 'object'>
    """ no doc """
    def GetHashCode(self) -> int:
        """ GetHashCode(self: CancellationTokenRegistration) -> int """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CancellationTokenSource(IDisposable): # skipped bases: <type 'object'>
    """
    CancellationTokenSource()
    CancellationTokenSource(delay: TimeSpan)
    CancellationTokenSource(millisecondsDelay: int)
    """
    @property
    def IsCancellationRequested(self) -> bool:
        """ Get: IsCancellationRequested(self: CancellationTokenSource) -> bool """
        ...

    @property
    def Token(self) -> CancellationToken:
        """ Get: Token(self: CancellationTokenSource) -> CancellationToken """
        ...


    def Cancel(self, throwOnFirstException:bool = ...): # -> 
        """ Cancel(self: CancellationTokenSource, throwOnFirstException: bool)Cancel(self: CancellationTokenSource) """
        ...

    def CancelAfter(self, *__args:TimeSpan): # -> 
        """ CancelAfter(self: CancellationTokenSource, delay: TimeSpan)CancelAfter(self: CancellationTokenSource, millisecondsDelay: int) """
        ...

    @staticmethod
    def CreateLinkedTokenSource(*__args:Array) -> CancellationTokenSource:
        """
        CreateLinkedTokenSource(token1: CancellationToken, token2: CancellationToken) -> CancellationTokenSource
        CreateLinkedTokenSource(*tokens: Array[CancellationToken]) -> CancellationTokenSource
        """
        ...


class CompressedStack(ISerializable): # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def Capture() -> CompressedStack:
        """ Capture() -> CompressedStack """
        ...

    def CreateCopy(self) -> CompressedStack:
        """ CreateCopy(self: CompressedStack) -> CompressedStack """
        ...

    @staticmethod
    def GetCompressedStack() -> CompressedStack:
        """ GetCompressedStack() -> CompressedStack """
        ...

    @staticmethod
    def Run(compressedStack:CompressedStack, callback:ContextCallback, state:object): # -> 
        """ Run(compressedStack: CompressedStack, callback: ContextCallback, state: object) """
        ...


class ContextCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ContextCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, state:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ContextCallback, state: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ContextCallback, result: IAsyncResult) """
        ...

    def Invoke(self, state:object): # -> 
        """ Invoke(self: ContextCallback, state: object) """
        ...


class CountdownEvent(IDisposable): # skipped bases: <type 'object'>
    """ CountdownEvent(initialCount: int) """
    @property
    def CurrentCount(self) -> int:
        """ Get: CurrentCount(self: CountdownEvent) -> int """
        ...

    @property
    def InitialCount(self) -> int:
        """ Get: InitialCount(self: CountdownEvent) -> int """
        ...

    @property
    def IsSet(self) -> bool:
        """ Get: IsSet(self: CountdownEvent) -> bool """
        ...

    @property
    def WaitHandle(self) -> WaitHandle:
        """ Get: WaitHandle(self: CountdownEvent) -> WaitHandle """
        ...


    def AddCount(self, signalCount:int = ...): # -> 
        """ AddCount(self: CountdownEvent)AddCount(self: CountdownEvent, signalCount: int) """
        ...

    def Reset(self, count:int = ...): # -> 
        """ Reset(self: CountdownEvent)Reset(self: CountdownEvent, count: int) """
        ...

    def Signal(self, signalCount:int = ...) -> bool:
        """
        Signal(self: CountdownEvent) -> bool
        Signal(self: CountdownEvent, signalCount: int) -> bool
        """
        ...

    def TryAddCount(self, signalCount:int = ...) -> bool:
        """
        TryAddCount(self: CountdownEvent) -> bool
        TryAddCount(self: CountdownEvent, signalCount: int) -> bool
        """
        ...

    def Wait(self, *__args:CancellationToken): # -> 
        """
        Wait(self: CountdownEvent)Wait(self: CountdownEvent, cancellationToken: CancellationToken)Wait(self: CountdownEvent, timeout: TimeSpan) -> bool
        Wait(self: CountdownEvent, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool
        Wait(self: CountdownEvent, millisecondsTimeout: int) -> bool
        Wait(self: CountdownEvent, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool
        """
        ...


class DispatcherQueueHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DispatcherQueueHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DispatcherQueueHandler, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DispatcherQueueHandler, result: IAsyncResult) """
        ...

    def Invoke(self): # -> 
        """ Invoke(self: DispatcherQueueHandler) """
        ...


class DispatcherQueuePriority(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DispatcherQueuePriority, values: High (10), Low (-10), Normal (0) """
    High: DispatcherQueuePriority = ...
    Low: DispatcherQueuePriority = ...
    Normal: DispatcherQueuePriority = ...
    value__ = ...


class EventResetMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EventResetMode, values: AutoReset (0), ManualReset (1) """
    AutoReset: EventResetMode = ...
    ManualReset: EventResetMode = ...
    value__ = ...


class ExecutionContext(IDisposable, ISerializable): # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def Capture() -> ExecutionContext:
        """ Capture() -> ExecutionContext """
        ...

    def CreateCopy(self) -> ExecutionContext:
        """ CreateCopy(self: ExecutionContext) -> ExecutionContext """
        ...

    @staticmethod
    def IsFlowSuppressed() -> bool:
        """ IsFlowSuppressed() -> bool """
        ...

    @staticmethod
    def RestoreFlow(): # -> 
        """ RestoreFlow() """
        ...

    @staticmethod
    def Run(executionContext:ExecutionContext, callback:ContextCallback, state:object): # -> 
        """ Run(executionContext: ExecutionContext, callback: ContextCallback, state: object) """
        ...

    @staticmethod
    def SuppressFlow() -> AsyncFlowControl:
        """ SuppressFlow() -> AsyncFlowControl """
        ...


class HostExecutionContext(IDisposable): # skipped bases: <type 'object'>
    """
    HostExecutionContext()
    HostExecutionContext(state: object)
    """
    @property
    def State(self):
        ...


    def CreateCopy(self) -> HostExecutionContext:
        """ CreateCopy(self: HostExecutionContext) -> HostExecutionContext """
        ...


class HostExecutionContextManager: # skipped bases: <type 'object'>, <type 'object'>
    """ HostExecutionContextManager() """
    def Capture(self) -> HostExecutionContext:
        """ Capture(self: HostExecutionContextManager) -> HostExecutionContext """
        ...

    def Revert(self, previousState:object): # -> 
        """ Revert(self: HostExecutionContextManager, previousState: object) """
        ...

    def SetHostExecutionContext(self, hostExecutionContext:HostExecutionContext) -> object:
        """ SetHostExecutionContext(self: HostExecutionContextManager, hostExecutionContext: HostExecutionContext) -> object """
        ...


class Interlocked: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Add(location1:int, value:int) -> Tuple_[int, int]:
        """
        Add(location1: int, value: int) -> (int, int)
        Add(location1: Int64, value: Int64) -> (Int64, Int64)
        """
        ...

    @staticmethod
    def CompareExchange(location1:Int64, value:Int64, comparand:Int64) -> Tuple_[Int64, Int64]:
        """
        CompareExchange(location1: Int64, value: Int64, comparand: Int64) -> (Int64, Int64)
        CompareExchange(location1: Single, value: Single, comparand: Single) -> (Single, Single)
        CompareExchange(location1: float, value: float, comparand: float) -> (float, float)
        CompareExchange[T](location1: T, value: T, comparand: T) -> (T, T)
        CompareExchange(location1: int, value: int, comparand: int) -> (int, int)
        CompareExchange(location1: object, value: object, comparand: object) -> (object, object)
        CompareExchange(location1: IntPtr, value: IntPtr, comparand: IntPtr) -> (IntPtr, IntPtr)
        """
        ...

    @staticmethod
    def Decrement(location:int) -> Tuple_[int, int]:
        """
        Decrement(location: int) -> (int, int)
        Decrement(location: Int64) -> (Int64, Int64)
        """
        ...

    @staticmethod
    def Exchange(location1:Int64, value:Int64) -> Tuple_[Int64, Int64]:
        """
        Exchange(location1: Int64, value: Int64) -> (Int64, Int64)
        Exchange(location1: Single, value: Single) -> (Single, Single)
        Exchange(location1: float, value: float) -> (float, float)
        Exchange[T](location1: T, value: T) -> (T, T)
        Exchange(location1: int, value: int) -> (int, int)
        Exchange(location1: object, value: object) -> (object, object)
        Exchange(location1: IntPtr, value: IntPtr) -> (IntPtr, IntPtr)
        """
        ...

    @staticmethod
    def Increment(location:int) -> Tuple_[int, int]:
        """
        Increment(location: int) -> (int, int)
        Increment(location: Int64) -> (Int64, Int64)
        """
        ...

    @staticmethod
    def MemoryBarrier(): # -> 
        """ MemoryBarrier() """
        ...

    @staticmethod
    def Read(location:Int64) -> Tuple_[Int64, Int64]:
        """ Read(location: Int64) -> (Int64, Int64) """
        ...

    @staticmethod
    def SpeculationBarrier(): # -> 
        """ SpeculationBarrier() """
        ...

    __all__: list = ...


class IOCompletionCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ IOCompletionCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, errorCode:UInt32, numBytes:UInt32, pOVERLAP:NativeOverlapped, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: IOCompletionCallback, errorCode: UInt32, numBytes: UInt32, pOVERLAP: NativeOverlapped*, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: IOCompletionCallback, result: IAsyncResult) """
        ...

    def Invoke(self, errorCode:UInt32, numBytes:UInt32, pOVERLAP:NativeOverlapped): # -> 
        """ Invoke(self: IOCompletionCallback, errorCode: UInt32, numBytes: UInt32, pOVERLAP: NativeOverlapped*) """
        ...


class LazyInitializer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def EnsureInitialized(target, *__args): # -> Tuple_[T, T] # Not found arg types: {'*__args': 'Func', 'target': 'T'}
        """
        EnsureInitialized[T](target: T, valueFactory: Func[T]) -> (T, T)
        EnsureInitialized[T](target: T) -> (T, T)
        EnsureInitialized[T](target: T, initialized: bool, syncLock: object) -> (T, T, bool, object)
        EnsureInitialized[T](target: T, initialized: bool, syncLock: object, valueFactory: Func[T]) -> (T, T, bool, object)
        """
        ...

    __all__: list = ...


class LazyThreadSafetyMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LazyThreadSafetyMode, values: ExecutionAndPublication (2), None (0), PublicationOnly (1) """
    ExecutionAndPublication: LazyThreadSafetyMode = ...
    PublicationOnly: LazyThreadSafetyMode = ...
    value__ = ...


class LockCookie: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Equals(self, obj:object) -> bool:
        """
        Equals(self: LockCookie, obj: object) -> bool
        Equals(self: LockCookie, obj: LockCookie) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: LockCookie) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LockRecursionException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    LockRecursionException()
    LockRecursionException(message: str)
    LockRecursionException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class LockRecursionPolicy(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LockRecursionPolicy, values: NoRecursion (0), SupportsRecursion (1) """
    NoRecursion: LockRecursionPolicy = ...
    SupportsRecursion: LockRecursionPolicy = ...
    value__ = ...


class ManualResetEvent(EventWaitHandle): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ ManualResetEvent(initialState: bool) """
    pass

class ManualResetEventSlim(IDisposable): # skipped bases: <type 'object'>
    """
    ManualResetEventSlim()
    ManualResetEventSlim(initialState: bool)
    ManualResetEventSlim(initialState: bool, spinCount: int)
    """
    @property
    def IsSet(self) -> bool:
        """ Get: IsSet(self: ManualResetEventSlim) -> bool """
        ...

    @property
    def SpinCount(self) -> int:
        """ Get: SpinCount(self: ManualResetEventSlim) -> int """
        ...

    @property
    def WaitHandle(self) -> WaitHandle:
        """ Get: WaitHandle(self: ManualResetEventSlim) -> WaitHandle """
        ...


    def Reset(self): # -> 
        """ Reset(self: ManualResetEventSlim) """
        ...

    def Set(self): # -> 
        """ Set(self: ManualResetEventSlim) """
        ...

    def Wait(self, *__args:CancellationToken): # -> 
        """
        Wait(self: ManualResetEventSlim)Wait(self: ManualResetEventSlim, cancellationToken: CancellationToken)Wait(self: ManualResetEventSlim, timeout: TimeSpan) -> bool
        Wait(self: ManualResetEventSlim, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool
        Wait(self: ManualResetEventSlim, millisecondsTimeout: int) -> bool
        Wait(self: ManualResetEventSlim, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool
        """
        ...


class Monitor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Enter(obj:object, lockTaken:bool = ...) -> bool:
        """
        Enter(obj: object, lockTaken: bool) -> bool
        Enter(obj: object)
        """
        ...

    @staticmethod
    def Exit(obj:object): # -> 
        """ Exit(obj: object) """
        ...

    @staticmethod
    def IsEntered(obj:object) -> bool:
        """ IsEntered(obj: object) -> bool """
        ...

    @staticmethod
    def Pulse(obj:object): # -> 
        """ Pulse(obj: object) """
        ...

    @staticmethod
    def PulseAll(obj:object): # -> 
        """ PulseAll(obj: object) """
        ...

    @staticmethod
    def TryEnter(obj:object, *__args:bool) -> bool:
        """
        TryEnter(obj: object) -> bool
        TryEnter(obj: object, lockTaken: bool) -> bool
        TryEnter(obj: object, millisecondsTimeout: int) -> bool
        TryEnter(obj: object, timeout: TimeSpan) -> bool
        TryEnter(obj: object, millisecondsTimeout: int, lockTaken: bool) -> bool
        TryEnter(obj: object, timeout: TimeSpan, lockTaken: bool) -> bool
        """
        ...

    @staticmethod
    def Wait(obj:object, *__args:int) -> bool:
        """
        Wait(obj: object, millisecondsTimeout: int, exitContext: bool) -> bool
        Wait(obj: object, timeout: TimeSpan, exitContext: bool) -> bool
        Wait(obj: object, millisecondsTimeout: int) -> bool
        Wait(obj: object, timeout: TimeSpan) -> bool
        Wait(obj: object) -> bool
        """
        ...

    __all__: list = ...


class Mutex(WaitHandle): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    Mutex(initiallyOwned: bool, name: str) -> bool
    Mutex(initiallyOwned: bool, name: str, mutexSecurity: MutexSecurity) -> bool
    Mutex(initiallyOwned: bool, name: str)
    Mutex(initiallyOwned: bool)
    Mutex()
    """
    def GetAccessControl(self) -> MutexSecurity:
        """ GetAccessControl(self: Mutex) -> MutexSecurity """
        ...

    @staticmethod
    def OpenExisting(name:str, rights:MutexRights = ...) -> Mutex:
        """
        OpenExisting(name: str) -> Mutex
        OpenExisting(name: str, rights: MutexRights) -> Mutex
        """
        ...

    def ReleaseMutex(self): # -> 
        """ ReleaseMutex(self: Mutex) """
        ...

    def SetAccessControl(self, mutexSecurity:MutexSecurity): # -> 
        """ SetAccessControl(self: Mutex, mutexSecurity: MutexSecurity) """
        ...

    @staticmethod
    def TryOpenExisting(name:str, *__args:MutexRights) -> Tuple_[bool, Mutex]:
        """
        TryOpenExisting(name: str) -> (bool, Mutex)
        TryOpenExisting(name: str, rights: MutexRights) -> (bool, Mutex)
        """
        ...

    def __new__(cls, initiallyOwned=None, name=None, createdNew=None, mutexSecurity=None): # -> Self -> bool
        """
        __new__(cls: type, initiallyOwned: bool, name: str) -> bool
        __new__(cls: type, initiallyOwned: bool, name: str, mutexSecurity: MutexSecurity) -> bool
        __new__(cls: type, initiallyOwned: bool, name: str)
        __new__(cls: type, initiallyOwned: bool)
        __new__(cls: type)
        """
        ...


class NativeOverlapped: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    EventHandle = ...
    InternalHigh = ...
    InternalLow = ...
    OffsetHigh = ...
    OffsetLow = ...


class Overlapped: # skipped bases: <type 'object'>, <type 'object'>
    """
    Overlapped()
    Overlapped(offsetLo: int, offsetHi: int, hEvent: IntPtr, ar: IAsyncResult)
    Overlapped(offsetLo: int, offsetHi: int, hEvent: int, ar: IAsyncResult)
    """
    @property
    def AsyncResult(self) -> IAsyncResult:
        """
        Get: AsyncResult(self: Overlapped) -> IAsyncResult
        Set: AsyncResult(self: Overlapped) = value
        """
        ...

    @property
    def EventHandle(self) -> int:
        """
        Get: EventHandle(self: Overlapped) -> int
        Set: EventHandle(self: Overlapped) = value
        """
        ...

    @property
    def EventHandleIntPtr(self) -> IntPtr:
        """
        Get: EventHandleIntPtr(self: Overlapped) -> IntPtr
        Set: EventHandleIntPtr(self: Overlapped) = value
        """
        ...

    @property
    def OffsetHigh(self) -> int:
        """
        Get: OffsetHigh(self: Overlapped) -> int
        Set: OffsetHigh(self: Overlapped) = value
        """
        ...

    @property
    def OffsetLow(self) -> int:
        """
        Get: OffsetLow(self: Overlapped) -> int
        Set: OffsetLow(self: Overlapped) = value
        """
        ...


    @staticmethod
    def Free(nativeOverlappedPtr:NativeOverlapped): # -> 
        """ Free(nativeOverlappedPtr: NativeOverlapped*) """
        ...

    def Pack(self, iocb:IOCompletionCallback, userData:object = ...) -> NativeOverlapped:
        """
        Pack(self: Overlapped, iocb: IOCompletionCallback, userData: object) -> NativeOverlapped*
        Pack(self: Overlapped, iocb: IOCompletionCallback) -> NativeOverlapped*
        """
        ...

    @staticmethod
    def Unpack(nativeOverlappedPtr:NativeOverlapped) -> Overlapped:
        """ Unpack(nativeOverlappedPtr: NativeOverlapped*) -> Overlapped """
        ...

    def UnsafePack(self, iocb:IOCompletionCallback, userData:object = ...) -> NativeOverlapped:
        """
        UnsafePack(self: Overlapped, iocb: IOCompletionCallback, userData: object) -> NativeOverlapped*
        UnsafePack(self: Overlapped, iocb: IOCompletionCallback) -> NativeOverlapped*
        """
        ...


class ParameterizedThreadStart(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ParameterizedThreadStart(object: object, method: IntPtr) """
    def BeginInvoke(self, obj:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ParameterizedThreadStart, obj: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ParameterizedThreadStart, result: IAsyncResult) """
        ...

    def Invoke(self, obj:object): # -> 
        """ Invoke(self: ParameterizedThreadStart, obj: object) """
        ...


class PreAllocatedOverlapped(IDeferredDisposable, IDisposable): # skipped bases: <type 'object'>
    """ PreAllocatedOverlapped(callback: IOCompletionCallback, state: object, pinData: object) """
    pass

class ReaderWriterLock(CriticalFinalizerObject): # skipped bases: <type 'object'>
    """ ReaderWriterLock() """
    @property
    def IsReaderLockHeld(self) -> bool:
        """ Get: IsReaderLockHeld(self: ReaderWriterLock) -> bool """
        ...

    @property
    def IsWriterLockHeld(self) -> bool:
        """ Get: IsWriterLockHeld(self: ReaderWriterLock) -> bool """
        ...

    @property
    def WriterSeqNum(self) -> int:
        """ Get: WriterSeqNum(self: ReaderWriterLock) -> int """
        ...


    def AcquireReaderLock(self, *__args:int): # -> 
        """ AcquireReaderLock(self: ReaderWriterLock, millisecondsTimeout: int)AcquireReaderLock(self: ReaderWriterLock, timeout: TimeSpan) """
        ...

    def AcquireWriterLock(self, *__args:int): # -> 
        """ AcquireWriterLock(self: ReaderWriterLock, millisecondsTimeout: int)AcquireWriterLock(self: ReaderWriterLock, timeout: TimeSpan) """
        ...

    def AnyWritersSince(self, seqNum:int) -> bool:
        """ AnyWritersSince(self: ReaderWriterLock, seqNum: int) -> bool """
        ...

    def DowngradeFromWriterLock(self, lockCookie:LockCookie) -> LockCookie:
        """ DowngradeFromWriterLock(self: ReaderWriterLock, lockCookie: LockCookie) -> LockCookie """
        ...

    def ReleaseLock(self) -> LockCookie:
        """ ReleaseLock(self: ReaderWriterLock) -> LockCookie """
        ...

    def ReleaseReaderLock(self): # -> 
        """ ReleaseReaderLock(self: ReaderWriterLock) """
        ...

    def ReleaseWriterLock(self): # -> 
        """ ReleaseWriterLock(self: ReaderWriterLock) """
        ...

    def RestoreLock(self, lockCookie:LockCookie) -> LockCookie:
        """ RestoreLock(self: ReaderWriterLock, lockCookie: LockCookie) -> LockCookie """
        ...

    def UpgradeToWriterLock(self, *__args:int) -> LockCookie:
        """
        UpgradeToWriterLock(self: ReaderWriterLock, millisecondsTimeout: int) -> LockCookie
        UpgradeToWriterLock(self: ReaderWriterLock, timeout: TimeSpan) -> LockCookie
        """
        ...


class ReaderWriterLockSlim(IDisposable): # skipped bases: <type 'object'>
    """
    ReaderWriterLockSlim()
    ReaderWriterLockSlim(recursionPolicy: LockRecursionPolicy)
    """
    @property
    def CurrentReadCount(self) -> int:
        """ Get: CurrentReadCount(self: ReaderWriterLockSlim) -> int """
        ...

    @property
    def IsReadLockHeld(self) -> bool:
        """ Get: IsReadLockHeld(self: ReaderWriterLockSlim) -> bool """
        ...

    @property
    def IsUpgradeableReadLockHeld(self) -> bool:
        """ Get: IsUpgradeableReadLockHeld(self: ReaderWriterLockSlim) -> bool """
        ...

    @property
    def IsWriteLockHeld(self) -> bool:
        """ Get: IsWriteLockHeld(self: ReaderWriterLockSlim) -> bool """
        ...

    @property
    def RecursionPolicy(self) -> LockRecursionPolicy:
        """ Get: RecursionPolicy(self: ReaderWriterLockSlim) -> LockRecursionPolicy """
        ...

    @property
    def RecursiveReadCount(self) -> int:
        """ Get: RecursiveReadCount(self: ReaderWriterLockSlim) -> int """
        ...

    @property
    def RecursiveUpgradeCount(self) -> int:
        """ Get: RecursiveUpgradeCount(self: ReaderWriterLockSlim) -> int """
        ...

    @property
    def RecursiveWriteCount(self) -> int:
        """ Get: RecursiveWriteCount(self: ReaderWriterLockSlim) -> int """
        ...

    @property
    def WaitingReadCount(self) -> int:
        """ Get: WaitingReadCount(self: ReaderWriterLockSlim) -> int """
        ...

    @property
    def WaitingUpgradeCount(self) -> int:
        """ Get: WaitingUpgradeCount(self: ReaderWriterLockSlim) -> int """
        ...

    @property
    def WaitingWriteCount(self) -> int:
        """ Get: WaitingWriteCount(self: ReaderWriterLockSlim) -> int """
        ...


    def EnterReadLock(self): # -> 
        """ EnterReadLock(self: ReaderWriterLockSlim) """
        ...

    def EnterUpgradeableReadLock(self): # -> 
        """ EnterUpgradeableReadLock(self: ReaderWriterLockSlim) """
        ...

    def EnterWriteLock(self): # -> 
        """ EnterWriteLock(self: ReaderWriterLockSlim) """
        ...

    def ExitReadLock(self): # -> 
        """ ExitReadLock(self: ReaderWriterLockSlim) """
        ...

    def ExitUpgradeableReadLock(self): # -> 
        """ ExitUpgradeableReadLock(self: ReaderWriterLockSlim) """
        ...

    def ExitWriteLock(self): # -> 
        """ ExitWriteLock(self: ReaderWriterLockSlim) """
        ...

    def TryEnterReadLock(self, *__args:TimeSpan) -> bool:
        """
        TryEnterReadLock(self: ReaderWriterLockSlim, timeout: TimeSpan) -> bool
        TryEnterReadLock(self: ReaderWriterLockSlim, millisecondsTimeout: int) -> bool
        """
        ...

    def TryEnterUpgradeableReadLock(self, *__args:TimeSpan) -> bool:
        """
        TryEnterUpgradeableReadLock(self: ReaderWriterLockSlim, timeout: TimeSpan) -> bool
        TryEnterUpgradeableReadLock(self: ReaderWriterLockSlim, millisecondsTimeout: int) -> bool
        """
        ...

    def TryEnterWriteLock(self, *__args:TimeSpan) -> bool:
        """
        TryEnterWriteLock(self: ReaderWriterLockSlim, timeout: TimeSpan) -> bool
        TryEnterWriteLock(self: ReaderWriterLockSlim, millisecondsTimeout: int) -> bool
        """
        ...


class RegisteredWaitHandle(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    def Unregister(self, waitObject:WaitHandle) -> bool:
        """ Unregister(self: RegisteredWaitHandle, waitObject: WaitHandle) -> bool """
        ...


class Semaphore(WaitHandle): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    Semaphore(initialCount: int, maximumCount: int)
    Semaphore(initialCount: int, maximumCount: int, name: str)
    Semaphore(initialCount: int, maximumCount: int, name: str) -> bool
    Semaphore(initialCount: int, maximumCount: int, name: str, semaphoreSecurity: SemaphoreSecurity) -> bool
    """
    def GetAccessControl(self) -> SemaphoreSecurity:
        """ GetAccessControl(self: Semaphore) -> SemaphoreSecurity """
        ...

    @staticmethod
    def OpenExisting(name:str, rights:SemaphoreRights = ...) -> Semaphore:
        """
        OpenExisting(name: str) -> Semaphore
        OpenExisting(name: str, rights: SemaphoreRights) -> Semaphore
        """
        ...

    def Release(self, releaseCount:int = ...) -> int:
        """
        Release(self: Semaphore) -> int
        Release(self: Semaphore, releaseCount: int) -> int
        """
        ...

    def SetAccessControl(self, semaphoreSecurity:SemaphoreSecurity): # -> 
        """ SetAccessControl(self: Semaphore, semaphoreSecurity: SemaphoreSecurity) """
        ...

    @staticmethod
    def TryOpenExisting(name:str, *__args:SemaphoreRights) -> Tuple_[bool, Semaphore]:
        """
        TryOpenExisting(name: str) -> (bool, Semaphore)
        TryOpenExisting(name: str, rights: SemaphoreRights) -> (bool, Semaphore)
        """
        ...

    def __new__(cls, initialCount, maximumCount, name=None, createdNew=None, semaphoreSecurity=None) -> Self:
        """
        __new__(cls: type, initialCount: int, maximumCount: int)
        __new__(cls: type, initialCount: int, maximumCount: int, name: str)
        __new__(cls: type, initialCount: int, maximumCount: int, name: str) -> bool
        __new__(cls: type, initialCount: int, maximumCount: int, name: str, semaphoreSecurity: SemaphoreSecurity) -> bool
        """
        ...


class SemaphoreFullException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SemaphoreFullException()
    SemaphoreFullException(message: str)
    SemaphoreFullException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SemaphoreSlim(IDisposable): # skipped bases: <type 'object'>
    """
    SemaphoreSlim(initialCount: int)
    SemaphoreSlim(initialCount: int, maxCount: int)
    """
    @property
    def AvailableWaitHandle(self) -> WaitHandle:
        """ Get: AvailableWaitHandle(self: SemaphoreSlim) -> WaitHandle """
        ...

    @property
    def CurrentCount(self) -> int:
        """ Get: CurrentCount(self: SemaphoreSlim) -> int """
        ...


    def Release(self, releaseCount:int = ...) -> int:
        """
        Release(self: SemaphoreSlim) -> int
        Release(self: SemaphoreSlim, releaseCount: int) -> int
        """
        ...

    def Wait(self, *__args:CancellationToken): # -> 
        """
        Wait(self: SemaphoreSlim)Wait(self: SemaphoreSlim, cancellationToken: CancellationToken)Wait(self: SemaphoreSlim, timeout: TimeSpan) -> bool
        Wait(self: SemaphoreSlim, timeout: TimeSpan, cancellationToken: CancellationToken) -> bool
        Wait(self: SemaphoreSlim, millisecondsTimeout: int) -> bool
        Wait(self: SemaphoreSlim, millisecondsTimeout: int, cancellationToken: CancellationToken) -> bool
        """
        ...

    def WaitAsync(self, *__args:CancellationToken) -> Task:
        """
        WaitAsync(self: SemaphoreSlim) -> Task
        WaitAsync(self: SemaphoreSlim, cancellationToken: CancellationToken) -> Task
        WaitAsync(self: SemaphoreSlim, millisecondsTimeout: int) -> Task[bool]
        WaitAsync(self: SemaphoreSlim, timeout: TimeSpan) -> Task[bool]
        WaitAsync(self: SemaphoreSlim, timeout: TimeSpan, cancellationToken: CancellationToken) -> Task[bool]
        WaitAsync(self: SemaphoreSlim, millisecondsTimeout: int, cancellationToken: CancellationToken) -> Task[bool]
        """
        ...


class SendOrPostCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SendOrPostCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, state:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SendOrPostCallback, state: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SendOrPostCallback, result: IAsyncResult) """
        ...

    def Invoke(self, state:object): # -> 
        """ Invoke(self: SendOrPostCallback, state: object) """
        ...


class SpinLock: # skipped bases: <type 'object'>, <type 'object'>
    """ SpinLock(enableThreadOwnerTracking: bool) """
    @property
    def IsHeld(self) -> bool:
        """ Get: IsHeld(self: SpinLock) -> bool """
        ...

    @property
    def IsHeldByCurrentThread(self) -> bool:
        """ Get: IsHeldByCurrentThread(self: SpinLock) -> bool """
        ...

    @property
    def IsThreadOwnerTrackingEnabled(self) -> bool:
        """ Get: IsThreadOwnerTrackingEnabled(self: SpinLock) -> bool """
        ...


    def Enter(self, lockTaken:bool) -> bool:
        """ Enter(self: SpinLock, lockTaken: bool) -> bool """
        ...

    def Exit(self, useMemoryBarrier:bool = ...): # -> 
        """ Exit(self: SpinLock)Exit(self: SpinLock, useMemoryBarrier: bool) """
        ...

    def TryEnter(self, *__args:bool) -> bool:
        """
        TryEnter(self: SpinLock, lockTaken: bool) -> bool
        TryEnter(self: SpinLock, timeout: TimeSpan, lockTaken: bool) -> bool
        TryEnter(self: SpinLock, millisecondsTimeout: int, lockTaken: bool) -> bool
        """
        ...


class SpinWait: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: SpinWait) -> int """
        ...

    @property
    def NextSpinWillYield(self) -> bool:
        """ Get: NextSpinWillYield(self: SpinWait) -> bool """
        ...


    def Reset(self): # -> 
        """ Reset(self: SpinWait) """
        ...

    def SpinOnce(self): # -> 
        """ SpinOnce(self: SpinWait) """
        ...

    @staticmethod
    def SpinUntil(condition, *__args:TimeSpan) -> bool: # Not found arg types: {'condition': 'Func'}
        """
        SpinUntil(condition: Func[bool])SpinUntil(condition: Func[bool], timeout: TimeSpan) -> bool
        SpinUntil(condition: Func[bool], millisecondsTimeout: int) -> bool
        """
        ...


class SynchronizationContext: # skipped bases: <type 'object'>, <type 'object'>
    """ SynchronizationContext() """
    @property
    def Current(self) -> SynchronizationContext:
        """ Get: Current() -> SynchronizationContext """
        ...


    def CreateCopy(self) -> SynchronizationContext:
        """ CreateCopy(self: SynchronizationContext) -> SynchronizationContext """
        ...

    def IsWaitNotificationRequired(self) -> bool:
        """ IsWaitNotificationRequired(self: SynchronizationContext) -> bool """
        ...

    def OperationCompleted(self): # -> 
        """ OperationCompleted(self: SynchronizationContext) """
        ...

    def OperationStarted(self): # -> 
        """ OperationStarted(self: SynchronizationContext) """
        ...

    def Post(self, d:SendOrPostCallback, state:object): # -> 
        """ Post(self: SynchronizationContext, d: SendOrPostCallback, state: object) """
        ...

    def Send(self, d:SendOrPostCallback, state:object): # -> 
        """ Send(self: SynchronizationContext, d: SendOrPostCallback, state: object) """
        ...

    @staticmethod
    def SetSynchronizationContext(syncContext:SynchronizationContext): # -> 
        """ SetSynchronizationContext(syncContext: SynchronizationContext) """
        ...

    def SetWaitNotificationRequired(self, *args): #cannot find CLR method
        """ SetWaitNotificationRequired(self: SynchronizationContext) """
        ...

    def Wait(self, waitHandles:Array, waitAll:bool, millisecondsTimeout:int) -> int:
        """ Wait(self: SynchronizationContext, waitHandles: Array[IntPtr], waitAll: bool, millisecondsTimeout: int) -> int """
        ...

    def WaitHelper(self, *args): #cannot find CLR method
        """ WaitHelper(waitHandles: Array[IntPtr], waitAll: bool, millisecondsTimeout: int) -> int """
        ...



class SynchronizationLockException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SynchronizationLockException()
    SynchronizationLockException(message: str)
    SynchronizationLockException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class Thread(_Thread, CriticalFinalizerObject): # skipped bases: <type 'object'>
    """
    Thread(start: ThreadStart)
    Thread(start: ThreadStart, maxStackSize: int)
    Thread(start: ParameterizedThreadStart)
    Thread(start: ParameterizedThreadStart, maxStackSize: int)
    """
    @property
    def ApartmentState(self) -> ApartmentState:
        """
        Get: ApartmentState(self: Thread) -> ApartmentState
        Set: ApartmentState(self: Thread) = value
        """
        ...

    @property
    def CurrentContext(self) -> Context:
        """ Get: CurrentContext() -> Context """
        ...

    @property
    def CurrentCulture(self) -> CultureInfo:
        """
        Get: CurrentCulture(self: Thread) -> CultureInfo
        Set: CurrentCulture(self: Thread) = value
        """
        ...

    @property
    def CurrentPrincipal(self) -> IPrincipal:
        """
        Get: CurrentPrincipal() -> IPrincipal
        Set: CurrentPrincipal() = value
        """
        ...

    @property
    def CurrentThread(self) -> Thread:
        """ Get: CurrentThread() -> Thread """
        ...

    @property
    def CurrentUICulture(self) -> CultureInfo:
        """
        Get: CurrentUICulture(self: Thread) -> CultureInfo
        Set: CurrentUICulture(self: Thread) = value
        """
        ...

    @property
    def ExecutionContext(self) -> ExecutionContext:
        """ Get: ExecutionContext(self: Thread) -> ExecutionContext """
        ...

    @property
    def IsAlive(self) -> bool:
        """ Get: IsAlive(self: Thread) -> bool """
        ...

    @property
    def IsBackground(self) -> bool:
        """
        Get: IsBackground(self: Thread) -> bool
        Set: IsBackground(self: Thread) = value
        """
        ...

    @property
    def IsThreadPoolThread(self) -> bool:
        """ Get: IsThreadPoolThread(self: Thread) -> bool """
        ...

    @property
    def ManagedThreadId(self) -> int:
        """ Get: ManagedThreadId(self: Thread) -> int """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Thread) -> str
        Set: Name(self: Thread) = value
        """
        ...

    @property
    def Priority(self) -> ThreadPriority:
        """
        Get: Priority(self: Thread) -> ThreadPriority
        Set: Priority(self: Thread) = value
        """
        ...

    @property
    def ThreadState(self) -> ThreadState:
        """ Get: ThreadState(self: Thread) -> ThreadState """
        ...


    def Abort(self, stateInfo:object = ...): # -> 
        """ Abort(self: Thread, stateInfo: object)Abort(self: Thread) """
        ...

    @staticmethod
    def AllocateDataSlot() -> LocalDataStoreSlot:
        """ AllocateDataSlot() -> LocalDataStoreSlot """
        ...

    @staticmethod
    def AllocateNamedDataSlot(name:str) -> LocalDataStoreSlot:
        """ AllocateNamedDataSlot(name: str) -> LocalDataStoreSlot """
        ...

    @staticmethod
    def BeginCriticalRegion(): # -> 
        """ BeginCriticalRegion() """
        ...

    @staticmethod
    def BeginThreadAffinity(): # -> 
        """ BeginThreadAffinity() """
        ...

    def DisableComObjectEagerCleanup(self): # -> 
        """ DisableComObjectEagerCleanup(self: Thread) """
        ...

    @staticmethod
    def EndCriticalRegion(): # -> 
        """ EndCriticalRegion() """
        ...

    @staticmethod
    def EndThreadAffinity(): # -> 
        """ EndThreadAffinity() """
        ...

    @staticmethod
    def FreeNamedDataSlot(name:str): # -> 
        """ FreeNamedDataSlot(name: str) """
        ...

    def GetApartmentState(self) -> ApartmentState:
        """ GetApartmentState(self: Thread) -> ApartmentState """
        ...

    def GetCompressedStack(self) -> CompressedStack:
        """ GetCompressedStack(self: Thread) -> CompressedStack """
        ...

    @staticmethod
    def GetData(slot:LocalDataStoreSlot) -> object:
        """ GetData(slot: LocalDataStoreSlot) -> object """
        ...

    @staticmethod
    def GetDomain() -> AppDomain:
        """ GetDomain() -> AppDomain """
        ...

    @staticmethod
    def GetDomainID() -> int:
        """ GetDomainID() -> int """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Thread) -> int """
        ...

    @staticmethod
    def GetNamedDataSlot(name:str) -> LocalDataStoreSlot:
        """ GetNamedDataSlot(name: str) -> LocalDataStoreSlot """
        ...

    def Interrupt(self): # -> 
        """ Interrupt(self: Thread) """
        ...

    def Join(self, *__args:int) -> bool:
        """
        Join(self: Thread)Join(self: Thread, millisecondsTimeout: int) -> bool
        Join(self: Thread, timeout: TimeSpan) -> bool
        """
        ...

    @staticmethod
    def MemoryBarrier(): # -> 
        """ MemoryBarrier() """
        ...

    @staticmethod
    def ResetAbort(): # -> 
        """ ResetAbort() """
        ...

    def Resume(self): # -> 
        """ Resume(self: Thread) """
        ...

    def SetApartmentState(self, state:ApartmentState): # -> 
        """ SetApartmentState(self: Thread, state: ApartmentState) """
        ...

    def SetCompressedStack(self, stack:CompressedStack): # -> 
        """ SetCompressedStack(self: Thread, stack: CompressedStack) """
        ...

    @staticmethod
    def SetData(slot:LocalDataStoreSlot, data:object): # -> 
        """ SetData(slot: LocalDataStoreSlot, data: object) """
        ...

    @staticmethod
    def Sleep(*__args:int): # -> 
        """ Sleep(millisecondsTimeout: int)Sleep(timeout: TimeSpan) """
        ...

    @staticmethod
    def SpinWait(iterations:int): # -> 
        """ SpinWait(iterations: int) """
        ...

    def Start(self, parameter:object = ...): # -> 
        """ Start(self: Thread)Start(self: Thread, parameter: object) """
        ...

    def Suspend(self): # -> 
        """ Suspend(self: Thread) """
        ...

    def TrySetApartmentState(self, state:ApartmentState) -> bool:
        """ TrySetApartmentState(self: Thread, state: ApartmentState) -> bool """
        ...

    @staticmethod
    def VolatileRead(address:Byte) -> Tuple_[Byte, Byte]:
        """
        VolatileRead(address: Byte) -> (Byte, Byte)
        VolatileRead(address: Int16) -> (Int16, Int16)
        VolatileRead(address: int) -> (int, int)
        VolatileRead(address: Int64) -> (Int64, Int64)
        VolatileRead(address: SByte) -> (SByte, SByte)
        VolatileRead(address: UInt16) -> (UInt16, UInt16)
        VolatileRead(address: UInt32) -> (UInt32, UInt32)
        VolatileRead(address: IntPtr) -> (IntPtr, IntPtr)
        VolatileRead(address: UIntPtr) -> (UIntPtr, UIntPtr)
        VolatileRead(address: UInt64) -> (UInt64, UInt64)
        VolatileRead(address: Single) -> (Single, Single)
        VolatileRead(address: float) -> (float, float)
        VolatileRead(address: object) -> (object, object)
        """
        ...

    @staticmethod
    def VolatileWrite(address:Byte, value:Byte) -> Byte:
        """
        VolatileWrite(address: Byte, value: Byte) -> Byte
        VolatileWrite(address: Int16, value: Int16) -> Int16
        VolatileWrite(address: int, value: int) -> int
        VolatileWrite(address: Int64, value: Int64) -> Int64
        VolatileWrite(address: SByte, value: SByte) -> SByte
        VolatileWrite(address: UInt16, value: UInt16) -> UInt16
        VolatileWrite(address: UInt32, value: UInt32) -> UInt32
        VolatileWrite(address: IntPtr, value: IntPtr) -> IntPtr
        VolatileWrite(address: UIntPtr, value: UIntPtr) -> UIntPtr
        VolatileWrite(address: UInt64, value: UInt64) -> UInt64
        VolatileWrite(address: Single, value: Single) -> Single
        VolatileWrite(address: float, value: float) -> float
        VolatileWrite(address: object, value: object) -> object
        """
        ...

    @staticmethod
    def Yield() -> bool:
        """ Yield() -> bool """
        ...

    def __new__(cls, start:ThreadStart, maxStackSize:int = ...) -> Self:
        """
        __new__(cls: type, start: ThreadStart)
        __new__(cls: type, start: ThreadStart, maxStackSize: int)
        __new__(cls: type, start: ParameterizedThreadStart)
        __new__(cls: type, start: ParameterizedThreadStart, maxStackSize: int)
        """
        ...



class ThreadAbortException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def ExceptionState(self) -> object:
        """ Get: ExceptionState(self: ThreadAbortException) -> object """
        ...


    SerializeObjectState = ...


class ThreadExceptionEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ThreadExceptionEventArgs(t: Exception) """
    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: ThreadExceptionEventArgs) -> Exception """
        ...


    def __new__(cls, t:Exception) -> Self:
        """ __new__(cls: type, t: Exception) """
        ...


class ThreadExceptionEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ThreadExceptionEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ThreadExceptionEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ThreadExceptionEventHandler, sender: object, e: ThreadExceptionEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ThreadExceptionEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ThreadExceptionEventArgs): # -> 
        """ Invoke(self: ThreadExceptionEventHandler, sender: object, e: ThreadExceptionEventArgs) """
        ...


class ThreadInterruptedException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ThreadInterruptedException()
    ThreadInterruptedException(message: str)
    ThreadInterruptedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ThreadLocal(IDisposable): # skipped bases: <type 'object'>
    """
    ThreadLocal[T]()
    ThreadLocal[T](trackAllValues: bool)
    ThreadLocal[T](valueFactory: Func[T])
    ThreadLocal[T](valueFactory: Func[T], trackAllValues: bool)
    """
    @property
    def IsValueCreated(self) -> bool:
        """ Get: IsValueCreated(self: ThreadLocal[T]) -> bool """
        ...

    @property
    def Value(self): # -> T
        """
        Get: Value(self: ThreadLocal[T]) -> T
        Set: Value(self: ThreadLocal[T]) = value
        """
        ...

    @property
    def Values(self) -> IList:
        """ Get: Values(self: ThreadLocal[T]) -> IList[T] """
        ...


    def ToString(self) -> str:
        """ ToString(self: ThreadLocal[T]) -> str """
        ...


class ThreadPool: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def BindHandle(osHandle:IntPtr) -> bool:
        """
        BindHandle(osHandle: IntPtr) -> bool
        BindHandle(osHandle: SafeHandle) -> bool
        """
        ...

    @staticmethod
    def GetAvailableThreads(workerThreads, completionPortThreads) -> Tuple_[int, int]:
        """ GetAvailableThreads() -> (int, int) """
        ...

    @staticmethod
    def GetMaxThreads(workerThreads, completionPortThreads) -> Tuple_[int, int]:
        """ GetMaxThreads() -> (int, int) """
        ...

    @staticmethod
    def GetMinThreads(workerThreads, completionPortThreads) -> Tuple_[int, int]:
        """ GetMinThreads() -> (int, int) """
        ...

    @staticmethod
    def QueueUserWorkItem(callBack:WaitCallback, state:object = ...) -> bool:
        """
        QueueUserWorkItem(callBack: WaitCallback, state: object) -> bool
        QueueUserWorkItem(callBack: WaitCallback) -> bool
        """
        ...

    @staticmethod
    def RegisterWaitForSingleObject(waitObject, callBack, state, *__args) -> RegisteredWaitHandle:
        """
        RegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: object, millisecondsTimeOutInterval: UInt32, executeOnlyOnce: bool) -> RegisteredWaitHandle
        RegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: object, millisecondsTimeOutInterval: int, executeOnlyOnce: bool) -> RegisteredWaitHandle
        RegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: object, millisecondsTimeOutInterval: Int64, executeOnlyOnce: bool) -> RegisteredWaitHandle
        RegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: object, timeout: TimeSpan, executeOnlyOnce: bool) -> RegisteredWaitHandle
        """
        ...

    @staticmethod
    def SetMaxThreads(workerThreads:int, completionPortThreads:int) -> bool:
        """ SetMaxThreads(workerThreads: int, completionPortThreads: int) -> bool """
        ...

    @staticmethod
    def SetMinThreads(workerThreads:int, completionPortThreads:int) -> bool:
        """ SetMinThreads(workerThreads: int, completionPortThreads: int) -> bool """
        ...

    @staticmethod
    def UnsafeQueueNativeOverlapped(overlapped:NativeOverlapped) -> bool:
        """ UnsafeQueueNativeOverlapped(overlapped: NativeOverlapped*) -> bool """
        ...

    @staticmethod
    def UnsafeQueueUserWorkItem(callBack:WaitCallback, state:object) -> bool:
        """ UnsafeQueueUserWorkItem(callBack: WaitCallback, state: object) -> bool """
        ...

    @staticmethod
    def UnsafeRegisterWaitForSingleObject(waitObject, callBack, state, *__args) -> RegisteredWaitHandle:
        """
        UnsafeRegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: object, millisecondsTimeOutInterval: UInt32, executeOnlyOnce: bool) -> RegisteredWaitHandle
        UnsafeRegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: object, millisecondsTimeOutInterval: int, executeOnlyOnce: bool) -> RegisteredWaitHandle
        UnsafeRegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: object, millisecondsTimeOutInterval: Int64, executeOnlyOnce: bool) -> RegisteredWaitHandle
        UnsafeRegisterWaitForSingleObject(waitObject: WaitHandle, callBack: WaitOrTimerCallback, state: object, timeout: TimeSpan, executeOnlyOnce: bool) -> RegisteredWaitHandle
        """
        ...

    __all__: list = ...


class ThreadPoolBoundHandle(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Handle(self) -> SafeHandle:
        """ Get: Handle(self: ThreadPoolBoundHandle) -> SafeHandle """
        ...


    def AllocateNativeOverlapped(self, *__args:PreAllocatedOverlapped) -> NativeOverlapped:
        """
        AllocateNativeOverlapped(self: ThreadPoolBoundHandle, callback: IOCompletionCallback, state: object, pinData: object) -> NativeOverlapped*
        AllocateNativeOverlapped(self: ThreadPoolBoundHandle, preAllocated: PreAllocatedOverlapped) -> NativeOverlapped*
        """
        ...

    @staticmethod
    def BindHandle(handle:SafeHandle) -> ThreadPoolBoundHandle:
        """ BindHandle(handle: SafeHandle) -> ThreadPoolBoundHandle """
        ...

    def FreeNativeOverlapped(self, overlapped:NativeOverlapped): # -> 
        """ FreeNativeOverlapped(self: ThreadPoolBoundHandle, overlapped: NativeOverlapped*) """
        ...

    @staticmethod
    def GetNativeOverlappedState(overlapped:NativeOverlapped) -> object:
        """ GetNativeOverlappedState(overlapped: NativeOverlapped*) -> object """
        ...


class ThreadPriority(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ThreadPriority, values: AboveNormal (3), BelowNormal (1), Highest (4), Lowest (0), Normal (2) """
    AboveNormal: ThreadPriority = ...
    BelowNormal: ThreadPriority = ...
    Highest: ThreadPriority = ...
    Lowest: ThreadPriority = ...
    Normal: ThreadPriority = ...
    value__ = ...


class ThreadStart(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ThreadStart(object: object, method: IntPtr) """
    def BeginInvoke(self, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ThreadStart, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ThreadStart, result: IAsyncResult) """
        ...

    def Invoke(self): # -> 
        """ Invoke(self: ThreadStart) """
        ...


class ThreadStartException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    SerializeObjectState = ...


class ThreadState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ThreadState, values: Aborted (256), AbortRequested (128), Background (4), Running (0), Stopped (16), StopRequested (1), Suspended (64), SuspendRequested (2), Unstarted (8), WaitSleepJoin (32) """
    Aborted: ThreadState = ...
    AbortRequested: ThreadState = ...
    Background: ThreadState = ...
    Running: ThreadState = ...
    Stopped: ThreadState = ...
    StopRequested: ThreadState = ...
    Suspended: ThreadState = ...
    SuspendRequested: ThreadState = ...
    Unstarted: ThreadState = ...
    value__ = ...
    WaitSleepJoin: ThreadState = ...


class ThreadStateException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ThreadStateException()
    ThreadStateException(message: str)
    ThreadStateException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class Timeout: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Infinite: int = ...
    InfiniteTimeSpan: TimeSpan = ...
    __all__: list = ...


class Timer(IDisposable, MarshalByRefObject): # skipped bases: <type 'object'>
    """
    Timer(callback: TimerCallback, state: object, dueTime: int, period: int)
    Timer(callback: TimerCallback, state: object, dueTime: TimeSpan, period: TimeSpan)
    Timer(callback: TimerCallback, state: object, dueTime: UInt32, period: UInt32)
    Timer(callback: TimerCallback, state: object, dueTime: Int64, period: Int64)
    Timer(callback: TimerCallback)
    """
    def Change(self, dueTime:int, period:int) -> bool:
        """
        Change(self: Timer, dueTime: int, period: int) -> bool
        Change(self: Timer, dueTime: TimeSpan, period: TimeSpan) -> bool
        Change(self: Timer, dueTime: UInt32, period: UInt32) -> bool
        Change(self: Timer, dueTime: Int64, period: Int64) -> bool
        """
        ...

    def __new__(cls, callback:TimerCallback, state:object = ..., dueTime:int = ..., period:int = ...) -> Self:
        """
        __new__(cls: type, callback: TimerCallback, state: object, dueTime: int, period: int)
        __new__(cls: type, callback: TimerCallback, state: object, dueTime: TimeSpan, period: TimeSpan)
        __new__(cls: type, callback: TimerCallback, state: object, dueTime: UInt32, period: UInt32)
        __new__(cls: type, callback: TimerCallback, state: object, dueTime: Int64, period: Int64)
        __new__(cls: type, callback: TimerCallback)
        """
        ...


class TimerCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TimerCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, state:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: TimerCallback, state: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: TimerCallback, result: IAsyncResult) """
        ...

    def Invoke(self, state:object): # -> 
        """ Invoke(self: TimerCallback, state: object) """
        ...


class Volatile: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Read(location:Int64) -> Tuple_[Int64, Int64]:
        """
        Read(location: Int64) -> (Int64, Int64)
        Read[T](location: T) -> (T, T)
        Read(location: bool) -> (bool, bool)
        Read(location: SByte) -> (SByte, SByte)
        Read(location: Byte) -> (Byte, Byte)
        Read(location: Int16) -> (Int16, Int16)
        Read(location: UInt16) -> (UInt16, UInt16)
        Read(location: int) -> (int, int)
        Read(location: UInt32) -> (UInt32, UInt32)
        Read(location: UInt64) -> (UInt64, UInt64)
        Read(location: IntPtr) -> (IntPtr, IntPtr)
        Read(location: UIntPtr) -> (UIntPtr, UIntPtr)
        Read(location: Single) -> (Single, Single)
        Read(location: float) -> (float, float)
        """
        ...

    @staticmethod
    def Write(location:Int64, value:Int64) -> Int64:
        """
        Write(location: Int64, value: Int64) -> Int64
        Write[T](location: T, value: T) -> T
        Write(location: bool, value: bool) -> bool
        Write(location: SByte, value: SByte) -> SByte
        Write(location: Byte, value: Byte) -> Byte
        Write(location: Int16, value: Int16) -> Int16
        Write(location: UInt16, value: UInt16) -> UInt16
        Write(location: int, value: int) -> int
        Write(location: UInt32, value: UInt32) -> UInt32
        Write(location: UInt64, value: UInt64) -> UInt64
        Write(location: IntPtr, value: IntPtr) -> IntPtr
        Write(location: UIntPtr, value: UIntPtr) -> UIntPtr
        Write(location: Single, value: Single) -> Single
        Write(location: float, value: float) -> float
        """
        ...

    __all__: list = ...


class WaitCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WaitCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, state:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WaitCallback, state: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WaitCallback, result: IAsyncResult) """
        ...

    def Invoke(self, state:object): # -> 
        """ Invoke(self: WaitCallback, state: object) """
        ...


class WaitHandleCannotBeOpenedException(ApplicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WaitHandleCannotBeOpenedException()
    WaitHandleCannotBeOpenedException(message: str)
    WaitHandleCannotBeOpenedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class WaitHandleExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetSafeWaitHandle(waitHandle:WaitHandle) -> SafeWaitHandle:
        """ GetSafeWaitHandle(waitHandle: WaitHandle) -> SafeWaitHandle """
        ...

    @staticmethod
    def SetSafeWaitHandle(waitHandle:WaitHandle, value:SafeWaitHandle): # -> 
        """ SetSafeWaitHandle(waitHandle: WaitHandle, value: SafeWaitHandle) """
        ...

    __all__: list = ...


class WaitOrTimerCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WaitOrTimerCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, state:object, timedOut:bool, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WaitOrTimerCallback, state: object, timedOut: bool, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WaitOrTimerCallback, result: IAsyncResult) """
        ...

    def Invoke(self, state:object, timedOut:bool): # -> 
        """ Invoke(self: WaitOrTimerCallback, state: object, timedOut: bool) """
        ...


# variables with complex values

