# encoding: utf-8
# module System.Runtime.CompilerServices calls itself CompilerServices
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from SqlContracts import ContractFailureKind

from System import (Action, Array, Attribute, Byte, Decimal, Delegate, Enum, 
    FormattableString, Int64, ModuleHandle, RuntimeFieldHandle, 
    RuntimeMethodHandle, RuntimeTypeHandle, Type, UInt32)

from System.Collections import IEnumerator, IList

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Dynamic import ExpandoObject

from System.Linq.Expressions import (DebugInfoExpression, Expression, 
    LabelTarget, LambdaExpression)

from System.Reflection import MethodBase

from System.Threading.Tasks import Task

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, CleanupCode, 
    ConfiguredTaskAwaiter, CreateValueCallback, T, TKey, TValue, TryCode, 
    YieldAwaiter, field#)
"""

# no functions
# classes

class AccessedThroughPropertyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AccessedThroughPropertyAttribute(propertyName: str) """
    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: AccessedThroughPropertyAttribute) -> str """
        ...


    def __new__(cls, propertyName:str) -> Self:
        """ __new__(cls: type, propertyName: str) """
        ...


class StateMachineAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ StateMachineAttribute(stateMachineType: Type) """
    @property
    def StateMachineType(self) -> Type:
        """ Get: StateMachineType(self: StateMachineAttribute) -> Type """
        ...


    def __new__(cls, stateMachineType:Type) -> Self:
        """ __new__(cls: type, stateMachineType: Type) """
        ...


class AsyncStateMachineAttribute(StateMachineAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AsyncStateMachineAttribute(stateMachineType: Type) """
    pass

class AsyncTaskMethodBuilder: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Task(self) -> Task:
        """ Get: Task(self: AsyncTaskMethodBuilder) -> Task """
        ...


    def AwaitOnCompleted(self, awaiter, stateMachine):
        """ no doc """
        ...

    def AwaitUnsafeOnCompleted(self, awaiter, stateMachine):
        """ no doc """
        ...

    @staticmethod
    def Create() -> AsyncTaskMethodBuilder:
        """ Create() -> AsyncTaskMethodBuilder """
        ...

    def SetException(self, exception:Exception): # -> 
        """ SetException(self: AsyncTaskMethodBuilder, exception: Exception) """
        ...

    def SetResult(self): # -> 
        """ SetResult(self: AsyncTaskMethodBuilder) """
        ...

    def SetStateMachine(self, stateMachine:IAsyncStateMachine): # -> 
        """ SetStateMachine(self: AsyncTaskMethodBuilder, stateMachine: IAsyncStateMachine) """
        ...

    def Start(self, stateMachine):
        """ no doc """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class AsyncVoidMethodBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def AwaitOnCompleted(self, awaiter, stateMachine):
        """ no doc """
        ...

    def AwaitUnsafeOnCompleted(self, awaiter, stateMachine):
        """ no doc """
        ...

    @staticmethod
    def Create() -> AsyncVoidMethodBuilder:
        """ Create() -> AsyncVoidMethodBuilder """
        ...

    def SetException(self, exception:Exception): # -> 
        """ SetException(self: AsyncVoidMethodBuilder, exception: Exception) """
        ...

    def SetResult(self): # -> 
        """ SetResult(self: AsyncVoidMethodBuilder) """
        ...

    def SetStateMachine(self, stateMachine:IAsyncStateMachine): # -> 
        """ SetStateMachine(self: AsyncVoidMethodBuilder, stateMachine: IAsyncStateMachine) """
        ...

    def Start(self, stateMachine):
        """ no doc """
        ...


class CallConvCdecl: # skipped bases: <type 'object'>, <type 'object'>
    """ CallConvCdecl() """
    pass

class CallConvFastcall: # skipped bases: <type 'object'>, <type 'object'>
    """ CallConvFastcall() """
    pass

class CallConvStdcall: # skipped bases: <type 'object'>, <type 'object'>
    """ CallConvStdcall() """
    pass

class CallConvThiscall: # skipped bases: <type 'object'>, <type 'object'>
    """ CallConvThiscall() """
    pass

class CallerFilePathAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CallerFilePathAttribute() """
    pass

class CallerLineNumberAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CallerLineNumberAttribute() """
    pass

class CallerMemberNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CallerMemberNameAttribute() """
    pass

class CallSite: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Binder(self) -> CallSiteBinder:
        """ Get: Binder(self: CallSite) -> CallSiteBinder """
        ...


    @staticmethod
    def Create(delegateType:Type, binder:CallSiteBinder) -> CallSite:
        """ Create(delegateType: Type, binder: CallSiteBinder) -> CallSite """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class CallSiteBinder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def UpdateLabel(self) -> LabelTarget:
        """ Get: UpdateLabel() -> LabelTarget """
        ...


    def Bind(self, args:Array, parameters:ReadOnlyCollection, returnLabel:LabelTarget) -> Expression:
        """ Bind(self: CallSiteBinder, args: Array[object], parameters: ReadOnlyCollection[ParameterExpression], returnLabel: LabelTarget) -> Expression """
        ...

    def BindDelegate(self, site:CallSite, args:Array): # -> T
        """ BindDelegate[T](self: CallSiteBinder, site: CallSite[T], args: Array[object]) -> T """
        ...

    def CacheTarget(self, *args): #cannot find CLR method
        """ CacheTarget[T](self: CallSiteBinder, target: T) """
        ...



class CallSiteHelpers: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def IsInternalFrame(mb:MethodBase) -> bool:
        """ IsInternalFrame(mb: MethodBase) -> bool """
        ...

    __all__: list = ...


class CallSiteOps: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AddRule(site:CallSite, rule): # ->  # Not found arg types: {'rule': 'T'}
        """ AddRule[T](site: CallSite[T], rule: T) """
        ...

    @staticmethod
    def Bind(binder:CallSiteBinder, site:CallSite, args:Array): # -> T
        """ Bind[T](binder: CallSiteBinder, site: CallSite[T], args: Array[object]) -> T """
        ...

    @staticmethod
    def ClearMatch(site:CallSite): # -> 
        """ ClearMatch(site: CallSite) """
        ...

    @staticmethod
    def CreateMatchmaker(site:CallSite) -> CallSite:
        """ CreateMatchmaker[T](site: CallSite[T]) -> CallSite[T] """
        ...

    @staticmethod
    def GetCachedRules(cache:RuleCache) -> Array:
        """ GetCachedRules[T](cache: RuleCache[T]) -> Array[T] """
        ...

    @staticmethod
    def GetMatch(site:CallSite) -> bool:
        """ GetMatch(site: CallSite) -> bool """
        ...

    @staticmethod
    def GetRuleCache(site:CallSite) -> RuleCache:
        """ GetRuleCache[T](site: CallSite[T]) -> RuleCache[T] """
        ...

    @staticmethod
    def GetRules(site:CallSite) -> Array:
        """ GetRules[T](site: CallSite[T]) -> Array[T] """
        ...

    @staticmethod
    def MoveRule(cache:RuleCache, rule, i:int): # ->  # Not found arg types: {'rule': 'T'}
        """ MoveRule[T](cache: RuleCache[T], rule: T, i: int) """
        ...

    @staticmethod
    def SetNotMatched(site:CallSite) -> bool:
        """ SetNotMatched(site: CallSite) -> bool """
        ...

    @staticmethod
    def UpdateRules(this:CallSite, matched:int): # -> 
        """ UpdateRules[T](this: CallSite[T], matched: int) """
        ...

    __all__: list = ...


class Closure: # skipped bases: <type 'object'>, <type 'object'>
    """ Closure(constants: Array[object], locals: Array[object]) """
    Constants = ...
    Locals = ...


class CompilationRelaxations(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CompilationRelaxations, values: NoStringInterning (8) """
    NoStringInterning: CompilationRelaxations = ...
    value__ = ...


class CompilationRelaxationsAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    CompilationRelaxationsAttribute(relaxations: int)
    CompilationRelaxationsAttribute(relaxations: CompilationRelaxations)
    """
    @property
    def CompilationRelaxations(self) -> int:
        """ Get: CompilationRelaxations(self: CompilationRelaxationsAttribute) -> int """
        ...


    def __new__(cls, relaxations:int) -> Self:
        """
        __new__(cls: type, relaxations: int)
        __new__(cls: type, relaxations: CompilationRelaxations)
        """
        ...


class CompilerGeneratedAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CompilerGeneratedAttribute() """
    pass

class CompilerGlobalScopeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CompilerGlobalScopeAttribute() """
    pass

class CompilerMarshalOverride: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    __all__: list = ...


class ConditionalWeakTable: # skipped bases: <type 'object'>, <type 'object'>
    """ ConditionalWeakTable[TKey, TValue]() """
    def Add(self, key, value): # ->  # Not found arg types: {'value': 'TValue', 'key': 'TKey'}
        """ Add(self: ConditionalWeakTable[TKey, TValue], key: TKey, value: TValue) """
        ...

    def CreateValueCallback(self, *args): #cannot find CLR method
        """ CreateValueCallback(object: object, method: IntPtr) """
        ...

    def GetOrCreateValue(self, key): # -> TValue # Not found arg types: {'key': 'TKey'}
        """ GetOrCreateValue(self: ConditionalWeakTable[TKey, TValue], key: TKey) -> TValue """
        ...

    def GetValue(self, key, createValueCallback): # -> TValue # Not found arg types: {'key': 'TKey', 'createValueCallback': 'CreateValueCallback'}
        """ GetValue(self: ConditionalWeakTable[TKey, TValue], key: TKey, createValueCallback: CreateValueCallback) -> TValue """
        ...

    def Remove(self, key) -> bool: # Not found arg types: {'key': 'TKey'}
        """ Remove(self: ConditionalWeakTable[TKey, TValue], key: TKey) -> bool """
        ...

    def TryGetValue(self, key, value): # -> Tuple_[bool, TValue]
        """ TryGetValue(self: ConditionalWeakTable[TKey, TValue], key: TKey) -> (bool, TValue) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...



class ConfiguredTaskAwaitable: # skipped bases: <type 'object'>
    """ no doc """
    def ConfiguredTaskAwaiter(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def GetAwaiter(self): # -> ConfiguredTaskAwaiter
        """ GetAwaiter(self: ConfiguredTaskAwaitable) -> ConfiguredTaskAwaiter """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...



class ContractHelper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def RaiseContractFailedEvent(failureKind:ContractFailureKind, userMessage:str, conditionText:str, innerException:Exception) -> str:
        """ RaiseContractFailedEvent(failureKind: ContractFailureKind, userMessage: str, conditionText: str, innerException: Exception) -> str """
        ...

    @staticmethod
    def TriggerFailure(kind:ContractFailureKind, displayMessage:str, userMessage:str, conditionText:str, innerException:Exception): # -> 
        """ TriggerFailure(kind: ContractFailureKind, displayMessage: str, userMessage: str, conditionText: str, innerException: Exception) """
        ...

    __all__: list = ...


class CustomConstantAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    @property
    def Value(self) -> object:
        """ Get: Value(self: CustomConstantAttribute) -> object """
        ...



class DateTimeConstantAttribute(CustomConstantAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DateTimeConstantAttribute(ticks: Int64) """
    def __new__(cls, ticks:Int64) -> Self:
        """ __new__(cls: type, ticks: Int64) """
        ...


class DebugInfoGenerator: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreatePdbGenerator() -> DebugInfoGenerator:
        """ CreatePdbGenerator() -> DebugInfoGenerator """
        ...

    def MarkSequencePoint(self, method:LambdaExpression, ilOffset:int, sequencePoint:DebugInfoExpression): # -> 
        """ MarkSequencePoint(self: DebugInfoGenerator, method: LambdaExpression, ilOffset: int, sequencePoint: DebugInfoExpression) """
        ...


class DecimalConstantAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DecimalConstantAttribute(scale: Byte, sign: Byte, hi: UInt32, mid: UInt32, low: UInt32)
    DecimalConstantAttribute(scale: Byte, sign: Byte, hi: int, mid: int, low: int)
    """
    @property
    def Value(self) -> Decimal:
        """ Get: Value(self: DecimalConstantAttribute) -> Decimal """
        ...


    def __new__(cls, scale:Byte, sign:Byte, hi:UInt32, mid:UInt32, low:UInt32) -> Self:
        """
        __new__(cls: type, scale: Byte, sign: Byte, hi: UInt32, mid: UInt32, low: UInt32)
        __new__(cls: type, scale: Byte, sign: Byte, hi: int, mid: int, low: int)
        """
        ...


class DefaultDependencyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DefaultDependencyAttribute(loadHintArgument: LoadHint) """
    @property
    def LoadHint(self) -> LoadHint:
        """ Get: LoadHint(self: DefaultDependencyAttribute) -> LoadHint """
        ...


    def __new__(cls, loadHintArgument:LoadHint) -> Self:
        """ __new__(cls: type, loadHintArgument: LoadHint) """
        ...


class DependencyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DependencyAttribute(dependentAssemblyArgument: str, loadHintArgument: LoadHint) """
    @property
    def DependentAssembly(self) -> str:
        """ Get: DependentAssembly(self: DependencyAttribute) -> str """
        ...

    @property
    def LoadHint(self) -> LoadHint:
        """ Get: LoadHint(self: DependencyAttribute) -> LoadHint """
        ...


    def __new__(cls, dependentAssemblyArgument:str, loadHintArgument:LoadHint) -> Self:
        """ __new__(cls: type, dependentAssemblyArgument: str, loadHintArgument: LoadHint) """
        ...


class DisablePrivateReflectionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DisablePrivateReflectionAttribute() """
    pass

class DiscardableAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DiscardableAttribute() """
    pass

class DynamicAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    DynamicAttribute()
    DynamicAttribute(transformFlags: Array[bool])
    """
    @property
    def TransformFlags(self) -> IList:
        """ Get: TransformFlags(self: DynamicAttribute) -> IList[bool] """
        ...


    def __new__(cls, transformFlags:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, transformFlags: Array[bool])
        """
        ...


class ExecutionScope: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateDelegate(self, indexLambda:int, locals:Array) -> Delegate:
        """ CreateDelegate(self: ExecutionScope, indexLambda: int, locals: Array[object]) -> Delegate """
        ...

    def CreateHoistedLocals(self) -> Array:
        """ CreateHoistedLocals(self: ExecutionScope) -> Array[object] """
        ...

    def IsolateExpression(self, expression:Expression, locals:Array) -> Expression:
        """ IsolateExpression(self: ExecutionScope, expression: Expression, locals: Array[object]) -> Expression """
        ...

    Globals = ...
    Locals = ...
    Parent = ...


class ExtensionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ExtensionAttribute() """
    pass

class FixedAddressValueTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ FixedAddressValueTypeAttribute() """
    pass

class FixedBufferAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ FixedBufferAttribute(elementType: Type, length: int) """
    @property
    def ElementType(self) -> Type:
        """ Get: ElementType(self: FixedBufferAttribute) -> Type """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: FixedBufferAttribute) -> int """
        ...


    def __new__(cls, elementType:Type, length:int) -> Self:
        """ __new__(cls: type, elementType: Type, length: int) """
        ...


class FormattableStringFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Create(format:str, arguments:Array) -> FormattableString:
        """ Create(format: str, *arguments: Array[object]) -> FormattableString """
        ...

    __all__: list = ...


class HasCopySemanticsAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ HasCopySemanticsAttribute() """
    pass

class IAsyncStateMachine: # skipped bases: <type 'object'>
    """ no doc """
    def MoveNext(self): # -> 
        """ MoveNext(self: IAsyncStateMachine) """
        ...

    def SetStateMachine(self, stateMachine:IAsyncStateMachine): # -> 
        """ SetStateMachine(self: IAsyncStateMachine, stateMachine: IAsyncStateMachine) """
        ...


class INotifyCompletion: # skipped bases: <type 'object'>
    """ no doc """
    def OnCompleted(self, continuation:Action): # -> 
        """ OnCompleted(self: INotifyCompletion, continuation: Action) """
        ...


class ICriticalNotifyCompletion(INotifyCompletion): # skipped bases: <type 'object'>
    """ no doc """
    def UnsafeOnCompleted(self, continuation:Action): # -> 
        """ UnsafeOnCompleted(self: ICriticalNotifyCompletion, continuation: Action) """
        ...


class IDispatchConstantAttribute(CustomConstantAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ IDispatchConstantAttribute() """
    pass

class IndexerNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ IndexerNameAttribute(indexerName: str) """
    def __new__(cls, indexerName:str) -> Self:
        """ __new__(cls: type, indexerName: str) """
        ...


class InternalsVisibleToAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ InternalsVisibleToAttribute(assemblyName: str) """
    @property
    def AllInternalsVisible(self) -> bool:
        """
        Get: AllInternalsVisible(self: InternalsVisibleToAttribute) -> bool
        Set: AllInternalsVisible(self: InternalsVisibleToAttribute) = value
        """
        ...

    @property
    def AssemblyName(self) -> str:
        """ Get: AssemblyName(self: InternalsVisibleToAttribute) -> str """
        ...


    def __new__(cls, assemblyName:str) -> Self:
        """ __new__(cls: type, assemblyName: str) """
        ...


class IRuntimeVariables: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: IRuntimeVariables) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IsBoxed: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    __all__: list = ...


class IsByRefLikeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ IsByRefLikeAttribute() """
    pass

class IsByValue: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    __all__: list = ...


class IsConst: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    __all__: list = ...


class IsCopyConstructed: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    __all__: list = ...


class IsExplicitlyDereferenced: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    __all__: list = ...


class IsImplicitlyDereferenced: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    __all__: list = ...


class IsJitIntrinsic: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    __all__: list = ...


class IsLong: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    __all__: list = ...


class IsPinned: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    __all__: list = ...


class IsReadOnlyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ IsReadOnlyAttribute() """
    pass

class IsSignUnspecifiedByte: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    __all__: list = ...


class IStrongBox: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Value(self) -> object:
        """
        Get: Value(self: IStrongBox) -> object
        Set: Value(self: IStrongBox) = value
        """
        ...



class IsUdtReturn: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    __all__: list = ...


class IsVolatile: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    __all__: list = ...


class IteratorStateMachineAttribute(StateMachineAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ IteratorStateMachineAttribute(stateMachineType: Type) """
    pass

class ITuple: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Length(self) -> int:
        """ Get: Length(self: ITuple) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class IUnknownConstantAttribute(CustomConstantAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ IUnknownConstantAttribute() """
    pass

class LoadHint(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LoadHint, values: Always (1), Default (0), Sometimes (2) """
    Always: LoadHint = ...
    Default: LoadHint = ...
    Sometimes: LoadHint = ...
    value__ = ...


class MethodCodeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MethodCodeType, values: IL (0), Native (1), OPTIL (2), Runtime (3) """
    IL: MethodCodeType = ...
    Native: MethodCodeType = ...
    OPTIL: MethodCodeType = ...
    Runtime: MethodCodeType = ...
    value__ = ...


class MethodImplAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    MethodImplAttribute(methodImplOptions: MethodImplOptions)
    MethodImplAttribute(value: Int16)
    MethodImplAttribute()
    """
    @property
    def Value(self) -> MethodImplOptions:
        """ Get: Value(self: MethodImplAttribute) -> MethodImplOptions """
        ...


    def __new__(cls, *__args:MethodImplOptions) -> Self:
        """
        __new__(cls: type, methodImplOptions: MethodImplOptions)
        __new__(cls: type, value: Int16)
        __new__(cls: type)
        """
        ...

    MethodCodeType = ...


class MethodImplOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) MethodImplOptions, values: AggressiveInlining (256), ForwardRef (16), InternalCall (4096), NoInlining (8), NoOptimization (64), PreserveSig (128), SecurityMitigations (1024), Synchronized (32), Unmanaged (4) """
    AggressiveInlining: MethodImplOptions = ...
    ForwardRef: MethodImplOptions = ...
    InternalCall: MethodImplOptions = ...
    NoInlining: MethodImplOptions = ...
    NoOptimization: MethodImplOptions = ...
    PreserveSig: MethodImplOptions = ...
    SecurityMitigations: MethodImplOptions = ...
    Synchronized: MethodImplOptions = ...
    Unmanaged: MethodImplOptions = ...
    value__ = ...


class NativeCppClassAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ NativeCppClassAttribute() """
    pass

class ReadOnlyCollectionBuilder(IList): # skipped bases: <type 'ICollection'>, <type 'IEnumerable'>, <type 'ICollection[T]'>, <type 'IEnumerable[T]'>, <type 'object'>
    """
    ReadOnlyCollectionBuilder[T]()
    ReadOnlyCollectionBuilder[T](capacity: int)
    ReadOnlyCollectionBuilder[T](collection: IEnumerable[T])
    """
    @property
    def Capacity(self) -> int:
        """
        Get: Capacity(self: ReadOnlyCollectionBuilder[T]) -> int
        Set: Capacity(self: ReadOnlyCollectionBuilder[T]) = value
        """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ReadOnlyCollectionBuilder[T]) -> int """
        ...


    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: ReadOnlyCollectionBuilder[T], array: Array[T], arrayIndex: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ReadOnlyCollectionBuilder[T]) -> IEnumerator[T] """
        ...

    def Reverse(self, index:int = ..., count:int = ...): # -> 
        """ Reverse(self: ReadOnlyCollectionBuilder[T])Reverse(self: ReadOnlyCollectionBuilder[T], index: int, count: int) """
        ...

    def ToArray(self) -> Array:
        """ ToArray(self: ReadOnlyCollectionBuilder[T]) -> Array[T] """
        ...

    def ToReadOnlyCollection(self) -> ReadOnlyCollection:
        """ ToReadOnlyCollection(self: ReadOnlyCollectionBuilder[T]) -> ReadOnlyCollection[T] """
        ...


class ReferenceAssemblyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ReferenceAssemblyAttribute()
    ReferenceAssemblyAttribute(description: str)
    """
    @property
    def Description(self) -> str:
        """ Get: Description(self: ReferenceAssemblyAttribute) -> str """
        ...


    def __new__(cls, description:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, description: str)
        """
        ...


class RequiredAttributeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ RequiredAttributeAttribute(requiredContract: Type) """
    @property
    def RequiredContract(self) -> Type:
        """ Get: RequiredContract(self: RequiredAttributeAttribute) -> Type """
        ...


    def __new__(cls, requiredContract:Type) -> Self:
        """ __new__(cls: type, requiredContract: Type) """
        ...


class RuleCache: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class RuntimeCompatibilityAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ RuntimeCompatibilityAttribute() """
    @property
    def WrapNonExceptionThrows(self) -> bool:
        """
        Get: WrapNonExceptionThrows(self: RuntimeCompatibilityAttribute) -> bool
        Set: WrapNonExceptionThrows(self: RuntimeCompatibilityAttribute) = value
        """
        ...



class RuntimeFeature: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def IsSupported(feature:str) -> bool:
        """ IsSupported(feature: str) -> bool """
        ...

    PortablePdb: str = ...
    __all__: list = ...


class RuntimeHelpers: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def OffsetToStringData(self) -> int:
        """ Get: OffsetToStringData() -> int """
        ...


    def CleanupCode(self, *args): #cannot find CLR method
        """ CleanupCode(object: object, method: IntPtr) """
        ...

    @staticmethod
    def EnsureSufficientExecutionStack(): # -> 
        """ EnsureSufficientExecutionStack() """
        ...

    @staticmethod
    def Equals(*__args) -> bool:
        """ Equals(o1: object, o2: object) -> bool """
        ...

    @staticmethod
    def ExecuteCodeWithGuaranteedCleanup(code, backoutCode, userData:object): # ->  # Not found arg types: {'code': 'TryCode', 'backoutCode': 'CleanupCode'}
        """ ExecuteCodeWithGuaranteedCleanup(code: TryCode, backoutCode: CleanupCode, userData: object) """
        ...

    @staticmethod
    def GetHashCode(o:object = ...) -> int:
        """ GetHashCode(o: object) -> int """
        ...

    @staticmethod
    def GetObjectValue(obj:object) -> object:
        """ GetObjectValue(obj: object) -> object """
        ...

    @staticmethod
    def InitializeArray(array:Array, fldHandle:RuntimeFieldHandle): # -> 
        """ InitializeArray(array: Array, fldHandle: RuntimeFieldHandle) """
        ...

    @staticmethod
    def PrepareConstrainedRegions(): # -> 
        """ PrepareConstrainedRegions() """
        ...

    @staticmethod
    def PrepareConstrainedRegionsNoOP(): # -> 
        """ PrepareConstrainedRegionsNoOP() """
        ...

    @staticmethod
    def PrepareContractedDelegate(d:Delegate): # -> 
        """ PrepareContractedDelegate(d: Delegate) """
        ...

    @staticmethod
    def PrepareDelegate(d:Delegate): # -> 
        """ PrepareDelegate(d: Delegate) """
        ...

    @staticmethod
    def PrepareMethod(method:RuntimeMethodHandle, instantiation:Array = ...): # -> 
        """ PrepareMethod(method: RuntimeMethodHandle)PrepareMethod(method: RuntimeMethodHandle, instantiation: Array[RuntimeTypeHandle]) """
        ...

    @staticmethod
    def ProbeForSufficientStack(): # -> 
        """ ProbeForSufficientStack() """
        ...

    @staticmethod
    def RunClassConstructor(type:RuntimeTypeHandle): # -> 
        """ RunClassConstructor(type: RuntimeTypeHandle) """
        ...

    @staticmethod
    def RunModuleConstructor(module:ModuleHandle): # -> 
        """ RunModuleConstructor(module: ModuleHandle) """
        ...

    def TryCode(self, *args): #cannot find CLR method
        """ TryCode(object: object, method: IntPtr) """
        ...

    __all__: list = ...


class RuntimeOps: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateRuntimeVariables(data:Array = ..., indexes:Array = ...) -> IRuntimeVariables:
        """
        CreateRuntimeVariables(data: Array[object], indexes: Array[Int64]) -> IRuntimeVariables
        CreateRuntimeVariables() -> IRuntimeVariables
        """
        ...

    @staticmethod
    def ExpandoCheckVersion(expando:ExpandoObject, version:object) -> bool:
        """ ExpandoCheckVersion(expando: ExpandoObject, version: object) -> bool """
        ...

    @staticmethod
    def ExpandoPromoteClass(expando:ExpandoObject, oldClass:object, newClass:object): # -> 
        """ ExpandoPromoteClass(expando: ExpandoObject, oldClass: object, newClass: object) """
        ...

    @staticmethod
    def ExpandoTryDeleteValue(expando:ExpandoObject, indexClass:object, index:int, name:str, ignoreCase:bool) -> bool:
        """ ExpandoTryDeleteValue(expando: ExpandoObject, indexClass: object, index: int, name: str, ignoreCase: bool) -> bool """
        ...

    @staticmethod
    def ExpandoTryGetValue(expando, indexClass, index, name, ignoreCase, value) -> Tuple_[bool, object]:
        """ ExpandoTryGetValue(expando: ExpandoObject, indexClass: object, index: int, name: str, ignoreCase: bool) -> (bool, object) """
        ...

    @staticmethod
    def ExpandoTrySetValue(expando:ExpandoObject, indexClass:object, index:int, value:object, name:str, ignoreCase:bool) -> object:
        """ ExpandoTrySetValue(expando: ExpandoObject, indexClass: object, index: int, value: object, name: str, ignoreCase: bool) -> object """
        ...

    @staticmethod
    def MergeRuntimeVariables(first:IRuntimeVariables, second:IRuntimeVariables, indexes:Array) -> IRuntimeVariables:
        """ MergeRuntimeVariables(first: IRuntimeVariables, second: IRuntimeVariables, indexes: Array[int]) -> IRuntimeVariables """
        ...

    @staticmethod
    def Quote(expression:Expression, hoistedLocals:object, locals:Array) -> Expression:
        """ Quote(expression: Expression, hoistedLocals: object, locals: Array[object]) -> Expression """
        ...

    __all__: list = ...


class RuntimeWrappedException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def WrappedException(self) -> object:
        """ Get: WrappedException(self: RuntimeWrappedException) -> object """
        ...


    SerializeObjectState = ...


class ScopelessEnumAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ScopelessEnumAttribute() """
    pass

class SpecialNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SpecialNameAttribute() """
    pass

class StringFreezingAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ StringFreezingAttribute() """
    pass

class StrongBox(IStrongBox): # skipped bases: <type 'object'>
    """
    StrongBox[T]()
    StrongBox[T](value: T)
    """
    Value = ...


class SuppressIldasmAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SuppressIldasmAttribute() """
    pass

class TaskAwaiter: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsCompleted(self) -> bool:
        """ Get: IsCompleted(self: TaskAwaiter) -> bool """
        ...


    def GetResult(self): # -> 
        """ GetResult(self: TaskAwaiter) """
        ...

    def OnCompleted(self, continuation:Action): # -> 
        """ OnCompleted(self: TaskAwaiter, continuation: Action) """
        ...

    def UnsafeOnCompleted(self, continuation:Action): # -> 
        """ UnsafeOnCompleted(self: TaskAwaiter, continuation: Action) """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class TupleElementNamesAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TupleElementNamesAttribute(transformNames: Array[str]) """
    @property
    def TransformNames(self) -> IList:
        """ Get: TransformNames(self: TupleElementNamesAttribute) -> IList[str] """
        ...


    def __new__(cls, transformNames:Array) -> Self:
        """ __new__(cls: type, transformNames: Array[str]) """
        ...


class TypeForwardedFromAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TypeForwardedFromAttribute(assemblyFullName: str) """
    @property
    def AssemblyFullName(self) -> str:
        """ Get: AssemblyFullName(self: TypeForwardedFromAttribute) -> str """
        ...


    def __new__(cls, assemblyFullName:str) -> Self:
        """ __new__(cls: type, assemblyFullName: str) """
        ...


class TypeForwardedToAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TypeForwardedToAttribute(destination: Type) """
    @property
    def Destination(self) -> Type:
        """ Get: Destination(self: TypeForwardedToAttribute) -> Type """
        ...


    def __new__(cls, destination:Type) -> Self:
        """ __new__(cls: type, destination: Type) """
        ...


class UnsafeValueTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ UnsafeValueTypeAttribute() """
    pass

class YieldAwaitable: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetAwaiter(self): # -> YieldAwaiter
        """ GetAwaiter(self: YieldAwaitable) -> YieldAwaiter """
        ...

    def YieldAwaiter(self, *args): #cannot find CLR method
        """ no doc """
        ...



