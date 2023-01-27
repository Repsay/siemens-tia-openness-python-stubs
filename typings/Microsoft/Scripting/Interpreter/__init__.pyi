# encoding: utf-8
# module Microsoft.Scripting.Interpreter calls itself Interpreter
# from Microsoft.Dynamic, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Action, Array, Delegate, Enum, EventArgs, IEquatable, 
    Type, TypeCode)

from System.Collections import IEnumerable, IList

from System.Collections.Generic import Dictionary

from System.Linq.Expressions import (Expression, LabelTarget, 
    ParameterExpression)

from System.Reflection import (ConstructorInfo, FieldInfo, MethodBase, 
    MethodInfo)

from System.Runtime.CompilerServices import CallSiteBinder

from typing import Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, Func, 
    ThreadLocal[InterpretedFrame], field#)
"""

# no functions
# classes

class BranchLabel: # skipped bases: <type 'object'>, <type 'object'>
    """ BranchLabel() """
    pass

class Instruction: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ConsumedContinuations(self) -> int:
        """ Get: ConsumedContinuations(self: Instruction) -> int """
        ...

    @property
    def ConsumedStack(self) -> int:
        """ Get: ConsumedStack(self: Instruction) -> int """
        ...

    @property
    def ContinuationsBalance(self) -> int:
        """ Get: ContinuationsBalance(self: Instruction) -> int """
        ...

    @property
    def InstructionName(self) -> str:
        """ Get: InstructionName(self: Instruction) -> str """
        ...

    @property
    def ProducedContinuations(self) -> int:
        """ Get: ProducedContinuations(self: Instruction) -> int """
        ...

    @property
    def ProducedStack(self) -> int:
        """ Get: ProducedStack(self: Instruction) -> int """
        ...

    @property
    def StackBalance(self) -> int:
        """ Get: StackBalance(self: Instruction) -> int """
        ...


    def GetDebugCookie(self, compiler:LightCompiler) -> object:
        """ GetDebugCookie(self: Instruction, compiler: LightCompiler) -> object """
        ...

    def Run(self, frame:InterpretedFrame) -> int:
        """ Run(self: Instruction, frame: InterpretedFrame) -> int """
        ...

    def ToDebugString(self, instructionIndex:int, cookie:object, labelIndexer, objects:IList) -> str: # Not found arg types: {'labelIndexer': 'Func'}
        """ ToDebugString(self: Instruction, instructionIndex: int, cookie: object, labelIndexer: Func[int, int], objects: IList[object]) -> str """
        ...

    def ToString(self) -> str:
        """ ToString(self: Instruction) -> str """
        ...


class CallInstruction(Instruction): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ArgumentCount(self) -> int:
        """ Get: ArgumentCount(self: CallInstruction) -> int """
        ...

    @property
    def Info(self) -> MethodInfo:
        """ Get: Info(self: CallInstruction) -> MethodInfo """
        ...


    @staticmethod
    def ArrayItemSetter1(array:Array, index0:int, value:object): # -> 
        """ ArrayItemSetter1(array: Array, index0: int, value: object) """
        ...

    @staticmethod
    def ArrayItemSetter2(array:Array, index0:int, index1:int, value:object): # -> 
        """ ArrayItemSetter2(array: Array, index0: int, index1: int, value: object) """
        ...

    @staticmethod
    def ArrayItemSetter3(array:Array, index0:int, index1:int, index2:int, value:object): # -> 
        """ ArrayItemSetter3(array: Array, index0: int, index1: int, index2: int, value: object) """
        ...

    @staticmethod
    def CacheAction(method:Action) -> MethodInfo:
        """
        CacheAction(method: Action) -> MethodInfo
        CacheAction[T0](method: Action[T0]) -> MethodInfo
        CacheAction[(T0, T1)](method: Action[T0, T1]) -> MethodInfo
        CacheAction[(T0, T1, T2)](method: Action[T0, T1, T2]) -> MethodInfo
        CacheAction[(T0, T1, T2, T3)](method: Action[T0, T1, T2, T3]) -> MethodInfo
        CacheAction[(T0, T1, T2, T3, T4)](method: Action[T0, T1, T2, T3, T4]) -> MethodInfo
        CacheAction[(T0, T1, T2, T3, T4, T5)](method: Action[T0, T1, T2, T3, T4, T5]) -> MethodInfo
        CacheAction[(T0, T1, T2, T3, T4, T5, T6)](method: Action[T0, T1, T2, T3, T4, T5, T6]) -> MethodInfo
        CacheAction[(T0, T1, T2, T3, T4, T5, T6, T7)](method: Action[T0, T1, T2, T3, T4, T5, T6, T7]) -> MethodInfo
        CacheAction[(T0, T1, T2, T3, T4, T5, T6, T7, T8)](method: Action[T0, T1, T2, T3, T4, T5, T6, T7, T8]) -> MethodInfo
        """
        ...

    @staticmethod
    def CacheFunc(method) -> MethodInfo: # Not found arg types: {'method': 'Func'}
        """
        CacheFunc[TRet](method: Func[TRet]) -> MethodInfo
        CacheFunc[(T0, TRet)](method: Func[T0, TRet]) -> MethodInfo
        CacheFunc[(T0, T1, TRet)](method: Func[T0, T1, TRet]) -> MethodInfo
        CacheFunc[(T0, T1, T2, TRet)](method: Func[T0, T1, T2, TRet]) -> MethodInfo
        CacheFunc[(T0, T1, T2, T3, TRet)](method: Func[T0, T1, T2, T3, TRet]) -> MethodInfo
        CacheFunc[(T0, T1, T2, T3, T4, TRet)](method: Func[T0, T1, T2, T3, T4, TRet]) -> MethodInfo
        CacheFunc[(T0, T1, T2, T3, T4, T5, TRet)](method: Func[T0, T1, T2, T3, T4, T5, TRet]) -> MethodInfo
        CacheFunc[(T0, T1, T2, T3, T4, T5, T6, TRet)](method: Func[T0, T1, T2, T3, T4, T5, T6, TRet]) -> MethodInfo
        CacheFunc[(T0, T1, T2, T3, T4, T5, T6, T7, TRet)](method: Func[T0, T1, T2, T3, T4, T5, T6, T7, TRet]) -> MethodInfo
        CacheFunc[(T0, T1, T2, T3, T4, T5, T6, T7, T8, TRet)](method: Func[T0, T1, T2, T3, T4, T5, T6, T7, T8, TRet]) -> MethodInfo
        """
        ...

    @staticmethod
    def Create(info:MethodInfo, parameters:Array = ...) -> CallInstruction:
        """
        Create(info: MethodInfo) -> CallInstruction
        Create(info: MethodInfo, parameters: Array[ParameterInfo]) -> CallInstruction
        """
        ...

    def Invoke(self, *__args:Array) -> object:
        """
        Invoke(self: CallInstruction, *args: Array[object]) -> object
        Invoke(self: CallInstruction) -> object
        Invoke(self: CallInstruction, arg0: object) -> object
        Invoke(self: CallInstruction, arg0: object, arg1: object) -> object
        Invoke(self: CallInstruction, arg0: object, arg1: object, arg2: object) -> object
        Invoke(self: CallInstruction, arg0: object, arg1: object, arg2: object, arg3: object) -> object
        Invoke(self: CallInstruction, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object) -> object
        Invoke(self: CallInstruction, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object) -> object
        Invoke(self: CallInstruction, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object) -> object
        Invoke(self: CallInstruction, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object, arg7: object) -> object
        Invoke(self: CallInstruction, arg0: object, arg1: object, arg2: object, arg3: object, arg4: object, arg5: object, arg6: object, arg7: object, arg8: object) -> object
        """
        ...

    def InvokeInstance(self, instance:object, args:Array) -> object:
        """ InvokeInstance(self: CallInstruction, instance: object, *args: Array[object]) -> object """
        ...


class DebugInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ DebugInfo() """
    @staticmethod
    def GetMatchingDebugInfo(debugInfos:Array, index:int) -> DebugInfo:
        """ GetMatchingDebugInfo(debugInfos: Array[DebugInfo], index: int) -> DebugInfo """
        ...

    def ToString(self) -> str:
        """ ToString(self: DebugInfo) -> str """
        ...

    EndLine = ...
    FileName = ...
    Index = ...
    IsClear = ...
    StartLine = ...


class ExceptionHandler: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsFault(self) -> bool:
        """ Get: IsFault(self: ExceptionHandler) -> bool """
        ...


    def IsBetterThan(self, other:ExceptionHandler) -> bool:
        """ IsBetterThan(self: ExceptionHandler, other: ExceptionHandler) -> bool """
        ...

    def Matches(self, exceptionType:Type, index:int) -> bool:
        """ Matches(self: ExceptionHandler, exceptionType: Type, index: int) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: ExceptionHandler) -> str """
        ...

    EndIndex = ...
    ExceptionType = ...
    HandlerStartIndex = ...
    LabelIndex = ...
    StartIndex = ...


class GetArrayItemInstruction(Instruction): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IInstructionProvider: # skipped bases: <type 'object'>
    """ no doc """
    def AddInstructions(self, compiler:LightCompiler): # -> 
        """ AddInstructions(self: IInstructionProvider, compiler: LightCompiler) """
        ...


class ILightCallSiteBinder: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AcceptsArgumentArray(self) -> bool:
        """ Get: AcceptsArgumentArray(self: ILightCallSiteBinder) -> bool """
        ...



class InstructionArray: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class InstructionFactory: # skipped bases: <type 'object'>
    """ no doc """
    def DefaultValue(self, *args): #cannot find CLR method
        """ DefaultValue(self: InstructionFactory) -> Instruction """
        ...

    def GetArrayItem(self, *args): #cannot find CLR method
        """ GetArrayItem(self: InstructionFactory) -> Instruction """
        ...

    def NewArray(self, *args): #cannot find CLR method
        """ NewArray(self: InstructionFactory) -> Instruction """
        ...

    def NewArrayInit(self, *args): #cannot find CLR method
        """ NewArrayInit(self: InstructionFactory, elementCount: int) -> Instruction """
        ...

    def SetArrayItem(self, *args): #cannot find CLR method
        """ SetArrayItem(self: InstructionFactory) -> Instruction """
        ...

    def TypeAs(self, *args): #cannot find CLR method
        """ TypeAs(self: InstructionFactory) -> Instruction """
        ...

    def TypeIs(self, *args): #cannot find CLR method
        """ TypeIs(self: InstructionFactory) -> Instruction """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class InstructionList: # skipped bases: <type 'object'>, <type 'object'>
    """ InstructionList() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: InstructionList) -> int """
        ...

    @property
    def CurrentContinuationsDepth(self) -> int:
        """ Get: CurrentContinuationsDepth(self: InstructionList) -> int """
        ...

    @property
    def CurrentStackDepth(self) -> int:
        """ Get: CurrentStackDepth(self: InstructionList) -> int """
        ...

    @property
    def MaxStackDepth(self) -> int:
        """ Get: MaxStackDepth(self: InstructionList) -> int """
        ...


    def Emit(self, instruction:Instruction): # -> 
        """ Emit(self: InstructionList, instruction: Instruction) """
        ...

    def EmitAdd(self, type:Type, checked:bool): # -> 
        """ EmitAdd(self: InstructionList, type: Type, checked: bool) """
        ...

    def EmitAssignLocal(self, index:int): # -> 
        """ EmitAssignLocal(self: InstructionList, index: int) """
        ...

    def EmitAssignLocalBoxed(self, index:int): # -> 
        """ EmitAssignLocalBoxed(self: InstructionList, index: int) """
        ...

    def EmitAssignLocalToClosure(self, index:int): # -> 
        """ EmitAssignLocalToClosure(self: InstructionList, index: int) """
        ...

    def EmitBranch(self, label:BranchLabel, hasResult:bool = ..., hasValue:bool = ...): # -> 
        """ EmitBranch(self: InstructionList, label: BranchLabel)EmitBranch(self: InstructionList, label: BranchLabel, hasResult: bool, hasValue: bool) """
        ...

    def EmitBranchFalse(self, elseLabel:BranchLabel): # -> 
        """ EmitBranchFalse(self: InstructionList, elseLabel: BranchLabel) """
        ...

    def EmitBranchTrue(self, elseLabel:BranchLabel): # -> 
        """ EmitBranchTrue(self: InstructionList, elseLabel: BranchLabel) """
        ...

    def EmitCoalescingBranch(self, leftNotNull:BranchLabel): # -> 
        """ EmitCoalescingBranch(self: InstructionList, leftNotNull: BranchLabel) """
        ...

    def EmitDefaultValue(self, type:Type): # -> 
        """ EmitDefaultValue(self: InstructionList, type: Type) """
        ...

    def EmitDiv(self, type:Type): # -> 
        """ EmitDiv(self: InstructionList, type: Type) """
        ...

    def EmitDup(self): # -> 
        """ EmitDup(self: InstructionList) """
        ...

    def EmitDynamic(self, *__args:CallSiteBinder): # -> 
        """ EmitDynamic(self: InstructionList, type: Type, binder: CallSiteBinder)EmitDynamic[(T0, TRet)](self: InstructionList, binder: CallSiteBinder)EmitDynamic[(T0, T1, TRet)](self: InstructionList, binder: CallSiteBinder)EmitDynamic[(T0, T1, T2, TRet)](self: InstructionList, binder: CallSiteBinder)EmitDynamic[(T0, T1, T2, T3, TRet)](self: InstructionList, binder: CallSiteBinder)EmitDynamic[(T0, T1, T2, T3, T4, TRet)](self: InstructionList, binder: CallSiteBinder)EmitDynamic[(T0, T1, T2, T3, T4, T5, TRet)](self: InstructionList, binder: CallSiteBinder)EmitDynamic[(T0, T1, T2, T3, T4, T5, T6, TRet)](self: InstructionList, binder: CallSiteBinder)EmitDynamic[(T0, T1, T2, T3, T4, T5, T6, T7, TRet)](self: InstructionList, binder: CallSiteBinder)EmitDynamic[(T0, T1, T2, T3, T4, T5, T6, T7, T8, TRet)](self: InstructionList, binder: CallSiteBinder)EmitDynamic[(T0, T1, T2, T3, T4, T5, T6, T7, T8, T9, TRet)](self: InstructionList, binder: CallSiteBinder)EmitDynamic[(T0, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TRet)](self: InstructionList, binder: CallSiteBinder)EmitDynamic[(T0, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TRet)](self: InstructionList, binder: CallSiteBinder)EmitDynamic[(T0, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TRet)](self: InstructionList, binder: CallSiteBinder)EmitDynamic[(T0, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TRet)](self: InstructionList, binder: CallSiteBinder)EmitDynamic[(T0, T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TRet)](self: InstructionList, binder: CallSiteBinder) """
        ...

    def EmitEnterExceptionHandlerNonVoid(self): # -> 
        """ EmitEnterExceptionHandlerNonVoid(self: InstructionList) """
        ...

    def EmitEnterExceptionHandlerVoid(self): # -> 
        """ EmitEnterExceptionHandlerVoid(self: InstructionList) """
        ...

    def EmitEnterFinally(self): # -> 
        """ EmitEnterFinally(self: InstructionList) """
        ...

    def EmitEnterTryFinally(self, finallyStartLabel:BranchLabel): # -> 
        """ EmitEnterTryFinally(self: InstructionList, finallyStartLabel: BranchLabel) """
        ...

    def EmitEqual(self, type:Type): # -> 
        """ EmitEqual(self: InstructionList, type: Type) """
        ...

    def EmitGetArrayItem(self, arrayType:Type): # -> 
        """ EmitGetArrayItem(self: InstructionList, arrayType: Type) """
        ...

    def EmitGoto(self, label:BranchLabel, hasResult:bool, hasValue:bool): # -> 
        """ EmitGoto(self: InstructionList, label: BranchLabel, hasResult: bool, hasValue: bool) """
        ...

    def EmitGreaterThan(self, type:Type): # -> 
        """ EmitGreaterThan(self: InstructionList, type: Type) """
        ...

    def EmitGreaterThanOrEqual(self, type:Type): # -> 
        """ EmitGreaterThanOrEqual(self: InstructionList, type: Type) """
        ...

    def EmitInitializeLocal(self, index:int, type:Type): # -> 
        """ EmitInitializeLocal(self: InstructionList, index: int, type: Type) """
        ...

    def EmitLeaveExceptionHandler(self, hasValue:bool, tryExpressionEndLabel:BranchLabel): # -> 
        """ EmitLeaveExceptionHandler(self: InstructionList, hasValue: bool, tryExpressionEndLabel: BranchLabel) """
        ...

    def EmitLeaveFault(self, hasValue:bool): # -> 
        """ EmitLeaveFault(self: InstructionList, hasValue: bool) """
        ...

    def EmitLeaveFinally(self): # -> 
        """ EmitLeaveFinally(self: InstructionList) """
        ...

    def EmitLessThan(self, type:Type): # -> 
        """ EmitLessThan(self: InstructionList, type: Type) """
        ...

    def EmitLessThanOrEqual(self, type:Type): # -> 
        """ EmitLessThanOrEqual(self: InstructionList, type: Type) """
        ...

    def EmitLoad(self, value:object, type:Type = ...): # -> 
        """ EmitLoad(self: InstructionList, value: object)EmitLoad(self: InstructionList, value: bool)EmitLoad(self: InstructionList, value: object, type: Type) """
        ...

    def EmitLoadField(self, field:FieldInfo): # -> 
        """ EmitLoadField(self: InstructionList, field: FieldInfo) """
        ...

    def EmitLoadLocal(self, index:int): # -> 
        """ EmitLoadLocal(self: InstructionList, index: int) """
        ...

    def EmitLoadLocalBoxed(self, index:int): # -> 
        """ EmitLoadLocalBoxed(self: InstructionList, index: int) """
        ...

    def EmitLoadLocalFromClosure(self, index:int): # -> 
        """ EmitLoadLocalFromClosure(self: InstructionList, index: int) """
        ...

    def EmitLoadLocalFromClosureBoxed(self, index:int): # -> 
        """ EmitLoadLocalFromClosureBoxed(self: InstructionList, index: int) """
        ...

    def EmitMul(self, type:Type, checked:bool): # -> 
        """ EmitMul(self: InstructionList, type: Type, checked: bool) """
        ...

    def EmitNew(self, constructorInfo:ConstructorInfo): # -> 
        """ EmitNew(self: InstructionList, constructorInfo: ConstructorInfo) """
        ...

    def EmitNewArray(self, elementType:Type): # -> 
        """ EmitNewArray(self: InstructionList, elementType: Type) """
        ...

    def EmitNewArrayBounds(self, elementType:Type, rank:int): # -> 
        """ EmitNewArrayBounds(self: InstructionList, elementType: Type, rank: int) """
        ...

    def EmitNewArrayInit(self, elementType:Type, elementCount:int): # -> 
        """ EmitNewArrayInit(self: InstructionList, elementType: Type, elementCount: int) """
        ...

    def EmitNewRuntimeVariables(self, count:int): # -> 
        """ EmitNewRuntimeVariables(self: InstructionList, count: int) """
        ...

    def EmitNot(self): # -> 
        """ EmitNot(self: InstructionList) """
        ...

    def EmitNotEqual(self, type:Type): # -> 
        """ EmitNotEqual(self: InstructionList, type: Type) """
        ...

    def EmitNumericConvertChecked(self, from_:TypeCode, to:TypeCode): # -> 
        """ EmitNumericConvertChecked(self: InstructionList, from: TypeCode, to: TypeCode) """
        ...

    def EmitNumericConvertUnchecked(self, from_:TypeCode, to:TypeCode): # -> 
        """ EmitNumericConvertUnchecked(self: InstructionList, from: TypeCode, to: TypeCode) """
        ...

    def EmitPop(self): # -> 
        """ EmitPop(self: InstructionList) """
        ...

    def EmitRethrow(self): # -> 
        """ EmitRethrow(self: InstructionList) """
        ...

    def EmitRethrowVoid(self): # -> 
        """ EmitRethrowVoid(self: InstructionList) """
        ...

    def EmitSetArrayItem(self, arrayType:Type): # -> 
        """ EmitSetArrayItem(self: InstructionList, arrayType: Type) """
        ...

    def EmitStoreField(self, field:FieldInfo): # -> 
        """ EmitStoreField(self: InstructionList, field: FieldInfo) """
        ...

    def EmitStoreLocal(self, index:int): # -> 
        """ EmitStoreLocal(self: InstructionList, index: int) """
        ...

    def EmitStoreLocalBoxed(self, index:int): # -> 
        """ EmitStoreLocalBoxed(self: InstructionList, index: int) """
        ...

    def EmitStoreLocalToClosure(self, index:int): # -> 
        """ EmitStoreLocalToClosure(self: InstructionList, index: int) """
        ...

    def EmitSub(self, type:Type, checked:bool): # -> 
        """ EmitSub(self: InstructionList, type: Type, checked: bool) """
        ...

    def EmitSwitch(self, cases:Dictionary): # -> 
        """ EmitSwitch(self: InstructionList, cases: Dictionary[int, int]) """
        ...

    def EmitThrow(self): # -> 
        """ EmitThrow(self: InstructionList) """
        ...

    def EmitThrowVoid(self): # -> 
        """ EmitThrowVoid(self: InstructionList) """
        ...

    def EmitTypeAs(self, type:Type): # -> 
        """ EmitTypeAs(self: InstructionList, type: Type) """
        ...

    def EmitTypeEquals(self): # -> 
        """ EmitTypeEquals(self: InstructionList) """
        ...

    def EmitTypeIs(self, type:Type): # -> 
        """ EmitTypeIs(self: InstructionList, type: Type) """
        ...

    def MakeLabel(self) -> BranchLabel:
        """ MakeLabel(self: InstructionList) -> BranchLabel """
        ...

    def MarkLabel(self, label:BranchLabel): # -> 
        """ MarkLabel(self: InstructionList, label: BranchLabel) """
        ...

    def MarkRuntimeLabel(self) -> int:
        """ MarkRuntimeLabel(self: InstructionList) -> int """
        ...

    def SetDebugCookie(self, cookie:object): # -> 
        """ SetDebugCookie(self: InstructionList, cookie: object) """
        ...

    def ToArray(self) -> InstructionArray:
        """ ToArray(self: InstructionList) -> InstructionArray """
        ...


class InterpretedFrame: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: InterpretedFrame) -> str """
        ...

    @property
    def Parent(self) -> InterpretedFrame:
        """ Get: Parent(self: InterpretedFrame) -> InterpretedFrame """
        ...


    def Dup(self): # -> 
        """ Dup(self: InterpretedFrame) """
        ...

    def GetDebugInfo(self, instructionIndex:int) -> DebugInfo:
        """ GetDebugInfo(self: InterpretedFrame, instructionIndex: int) -> DebugInfo """
        ...

    @staticmethod
    def GetExceptionStackTrace(exception:Exception) -> Array:
        """ GetExceptionStackTrace(exception: Exception) -> Array[InterpretedFrameInfo] """
        ...

    def GetStackTraceDebugInfo(self) -> IEnumerable:
        """ GetStackTraceDebugInfo(self: InterpretedFrame) -> IEnumerable[InterpretedFrameInfo] """
        ...

    def Goto(self, labelIndex:int, value:object) -> int:
        """ Goto(self: InterpretedFrame, labelIndex: int, value: object) -> int """
        ...

    @staticmethod
    def GroupStackFrames(stackTrace:IEnumerable) -> IEnumerable:
        """ GroupStackFrames(stackTrace: IEnumerable[StackFrame]) -> IEnumerable[StackFrame] """
        ...

    @staticmethod
    def IsInterpretedFrame(method:MethodBase) -> bool:
        """ IsInterpretedFrame(method: MethodBase) -> bool """
        ...

    def Peek(self) -> object:
        """ Peek(self: InterpretedFrame) -> object """
        ...

    def Pop(self, n:int = ...) -> object:
        """
        Pop(self: InterpretedFrame) -> object
        Pop(self: InterpretedFrame, n: int) -> object
        """
        ...

    def Push(self, value:object): # -> 
        """ Push(self: InterpretedFrame, value: object)Push(self: InterpretedFrame, value: bool)Push(self: InterpretedFrame, value: int) """
        ...

    def PushContinuation(self, continuation:int): # -> 
        """ PushContinuation(self: InterpretedFrame, continuation: int) """
        ...

    def RemoveContinuation(self): # -> 
        """ RemoveContinuation(self: InterpretedFrame) """
        ...

    def VoidGoto(self, labelIndex:int) -> int:
        """ VoidGoto(self: InterpretedFrame, labelIndex: int) -> int """
        ...

    def YieldToCurrentContinuation(self) -> int:
        """ YieldToCurrentContinuation(self: InterpretedFrame) -> int """
        ...

    def YieldToPendingContinuation(self) -> int:
        """ YieldToPendingContinuation(self: InterpretedFrame) -> int """
        ...

    Closure = ...
    CurrentAbortHandler = ...
    CurrentFrame = ...
    Data = ...
    InstructionIndex = ...
    StackIndex = ...


class InterpretedFrameInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ InterpretedFrameInfo(methodName: str, info: DebugInfo) """
    def ToString(self) -> str:
        """ ToString(self: InterpretedFrameInfo) -> str """
        ...

    DebugInfo = ...
    MethodName = ...


class LabelScopeKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LabelScopeKind, values: Block (1), Catch (5), Expression (8), Filter (7), Finally (6), Lambda (3), Statement (0), Switch (2), Try (4) """
    Block: LabelScopeKind = ...
    Catch: LabelScopeKind = ...
    Expression: LabelScopeKind = ...
    Filter: LabelScopeKind = ...
    Finally: LabelScopeKind = ...
    Lambda: LabelScopeKind = ...
    Statement: LabelScopeKind = ...
    Switch: LabelScopeKind = ...
    Try: LabelScopeKind = ...
    value__ = ...


class LightCompiler: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Instructions(self) -> InstructionList:
        """ Get: Instructions(self: LightCompiler) -> InstructionList """
        ...

    @property
    def Locals(self) -> LocalVariables:
        """ Get: Locals(self: LightCompiler) -> LocalVariables """
        ...


    def Compile(self, expr:Expression): # -> 
        """ Compile(self: LightCompiler, expr: Expression) """
        ...

    def CompileGetBoxedVariable(self, variable:ParameterExpression): # -> 
        """ CompileGetBoxedVariable(self: LightCompiler, variable: ParameterExpression) """
        ...

    def CompileGetVariable(self, variable:ParameterExpression): # -> 
        """ CompileGetVariable(self: LightCompiler, variable: ParameterExpression) """
        ...

    def CompileParameterExpression(self, expr:Expression): # -> 
        """ CompileParameterExpression(self: LightCompiler, expr: Expression) """
        ...

    def CompileSetVariable(self, variable:ParameterExpression, isVoid:bool): # -> 
        """ CompileSetVariable(self: LightCompiler, variable: ParameterExpression, isVoid: bool) """
        ...

    def EmitCall(self, method:MethodInfo, parameters:Array = ...): # -> 
        """ EmitCall(self: LightCompiler, method: MethodInfo)EmitCall(self: LightCompiler, method: MethodInfo, parameters: Array[ParameterInfo]) """
        ...

    def GetBranchLabel(self, target:LabelTarget) -> BranchLabel:
        """ GetBranchLabel(self: LightCompiler, target: LabelTarget) -> BranchLabel """
        ...

    def PopLabelBlock(self, kind:LabelScopeKind): # -> 
        """ PopLabelBlock(self: LightCompiler, kind: LabelScopeKind) """
        ...

    def PushLabelBlock(self, type:LabelScopeKind): # -> 
        """ PushLabelBlock(self: LightCompiler, type: LabelScopeKind) """
        ...


class LightLambda: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Run(self, arguments:Array) -> object:
        """ Run(self: LightLambda, *arguments: Array[object]) -> object """
        ...

    Compile = ...


class LightLambdaCompileEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Compiled(self) -> Delegate:
        """ Get: Compiled(self: LightLambdaCompileEventArgs) -> Delegate """
        ...



class LocalDefinition(IEquatable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Index(self) -> int:
        """ Get: Index(self: LocalDefinition) -> int """
        ...

    @property
    def Parameter(self) -> ParameterExpression:
        """ Get: Parameter(self: LocalDefinition) -> ParameterExpression """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: LocalDefinition) -> int """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LocalVariable: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def InClosure(self) -> bool:
        """ Get: InClosure(self: LocalVariable) -> bool """
        ...

    @property
    def InClosureOrBoxed(self) -> bool:
        """ Get: InClosureOrBoxed(self: LocalVariable) -> bool """
        ...

    @property
    def IsBoxed(self) -> bool:
        """
        Get: IsBoxed(self: LocalVariable) -> bool
        Set: IsBoxed(self: LocalVariable) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: LocalVariable) -> str """
        ...

    Index = ...


class LocalVariables: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def LocalCount(self) -> int:
        """ Get: LocalCount(self: LocalVariables) -> int """
        ...


    def DefineLocal(self, variable:ParameterExpression, start:int) -> LocalDefinition:
        """ DefineLocal(self: LocalVariables, variable: ParameterExpression, start: int) -> LocalDefinition """
        ...

    def GetLocalIndex(self, var:ParameterExpression) -> int:
        """ GetLocalIndex(self: LocalVariables, var: ParameterExpression) -> int """
        ...

    def GetOrDefineLocal(self, var:ParameterExpression) -> int:
        """ GetOrDefineLocal(self: LocalVariables, var: ParameterExpression) -> int """
        ...

    def TryGetLocalOrClosure(self, var, local) -> Tuple_[bool, LocalVariable]:
        """ TryGetLocalOrClosure(self: LocalVariables, var: ParameterExpression) -> (bool, LocalVariable) """
        ...

    def UndefineLocal(self, definition:LocalDefinition, end:int): # -> 
        """ UndefineLocal(self: LocalVariables, definition: LocalDefinition, end: int) """
        ...


class NewArrayBoundsInstruction(Instruction): # skipped bases: <type 'object'>
    """ no doc """
    pass

class NewArrayInitInstruction(Instruction): # skipped bases: <type 'object'>
    """ no doc """
    pass

class NewArrayInstruction(Instruction): # skipped bases: <type 'object'>
    """ no doc """
    pass

class SetArrayItemInstruction(Instruction): # skipped bases: <type 'object'>
    """ no doc """
    pass

