# encoding: utf-8
# module Microsoft.Scripting.Ast calls itself Ast
# from Microsoft.Dynamic, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Scripting import SourceLocation

from Microsoft.Scripting.Interpreter import IInstructionProvider

from System import Array, Delegate, Enum, Type

from System.Collections import IEnumerable, IList

from System.Collections.Generic import List

from System.Linq.Expressions import (BinaryExpression, ConstantExpression, 
    DefaultExpression, Expression, ExpressionType, LabelTarget, 
    LambdaExpression, LoopExpression, MemberExpression, MethodCallExpression, 
    NewArrayExpression, NewExpression, ParameterExpression, 
    SymbolDocumentInfo)

from System.Reflection import ConstructorInfo, MethodInfo

from System.Runtime.CompilerServices import CallSiteBinder

from typing import Tuple as Tuple_

"""The following names are not found in the module: field#
"""

# no functions
# classes

class BlockBuilder(ExpressionCollectionBuilder): # skipped bases: <type 'IEnumerable[Expression]'>, <type 'ICollection[Expression]'>, <type 'IEnumerable'>, <type 'object'>
    """ BlockBuilder() """
    def ToExpression(self) -> Expression:
        """ ToExpression(self: BlockBuilder) -> Expression """
        ...


class ExpressionAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ExpressionAccess, values: None (0), Read (1), ReadWrite (3), Write (2) """
    Read: ExpressionAccess = ...
    ReadWrite: ExpressionAccess = ...
    value__ = ...
    Write: ExpressionAccess = ...


class ExpressionCollectionBuilder: # skipped bases: <type 'object'>
    """ ExpressionCollectionBuilder() """
    def ToMethodCall(self, instance:Expression, method:MethodInfo) -> Expression:
        """ ToMethodCall(self: ExpressionCollectionBuilder, instance: Expression, method: MethodInfo) -> Expression """
        ...

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        ...


class FinallyFlowControlExpression(Expression, IInstructionProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Body(self) -> Expression:
        """ Get: Body(self: FinallyFlowControlExpression) -> Expression """
        ...



class GeneratorExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Body(self) -> Expression:
        """ Get: Body(self: GeneratorExpression) -> Expression """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: GeneratorExpression) -> str """
        ...

    @property
    def RewriteAssignments(self) -> bool:
        """ Get: RewriteAssignments(self: GeneratorExpression) -> bool """
        ...

    @property
    def Target(self) -> LabelTarget:
        """ Get: Target(self: GeneratorExpression) -> LabelTarget """
        ...



class IfStatementBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Else(self, body:Expression) -> Expression:
        """
        Else(self: IfStatementBuilder, body: Expression) -> Expression
        Else(self: IfStatementBuilder, *body: Array[Expression]) -> Expression
        """
        ...

    def ElseIf(self, test:Expression, body:Expression) -> IfStatementBuilder:
        """
        ElseIf(self: IfStatementBuilder, test: Expression, body: Expression) -> IfStatementBuilder
        ElseIf(self: IfStatementBuilder, test: Expression, *body: Array[Expression]) -> IfStatementBuilder
        """
        ...

    def ToStatement(self) -> Expression:
        """ ToStatement(self: IfStatementBuilder) -> Expression """
        ...


class IfStatementTest: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Body(self) -> Expression:
        """ Get: Body(self: IfStatementTest) -> Expression """
        ...

    @property
    def Test(self) -> Expression:
        """ Get: Test(self: IfStatementTest) -> Expression """
        ...



class ILightExceptionAwareExpression: # skipped bases: <type 'object'>
    """ no doc """
    def ReduceForLightExceptions(self) -> Expression:
        """ ReduceForLightExceptions(self: ILightExceptionAwareExpression) -> Expression """
        ...


class LambdaBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Body(self) -> Expression:
        """
        Get: Body(self: LambdaBuilder) -> Expression
        Set: Body(self: LambdaBuilder) = value
        """
        ...

    @property
    def Dictionary(self) -> bool:
        """
        Get: Dictionary(self: LambdaBuilder) -> bool
        Set: Dictionary(self: LambdaBuilder) = value
        """
        ...

    @property
    def Locals(self) -> List:
        """ Get: Locals(self: LambdaBuilder) -> List[ParameterExpression] """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: LambdaBuilder) -> str
        Set: Name(self: LambdaBuilder) = value
        """
        ...

    @property
    def Parameters(self) -> List:
        """ Get: Parameters(self: LambdaBuilder) -> List[ParameterExpression] """
        ...

    @property
    def ParamsArray(self) -> ParameterExpression:
        """ Get: ParamsArray(self: LambdaBuilder) -> ParameterExpression """
        ...

    @property
    def ReturnType(self) -> Type:
        """
        Get: ReturnType(self: LambdaBuilder) -> Type
        Set: ReturnType(self: LambdaBuilder) = value
        """
        ...

    @property
    def Visible(self) -> bool:
        """
        Get: Visible(self: LambdaBuilder) -> bool
        Set: Visible(self: LambdaBuilder) = value
        """
        ...


    def AddHiddenVariable(self, temp:ParameterExpression): # -> 
        """ AddHiddenVariable(self: LambdaBuilder, temp: ParameterExpression) """
        ...

    def AddParameters(self, parameters:Array): # -> 
        """ AddParameters(self: LambdaBuilder, *parameters: Array[ParameterExpression]) """
        ...

    def ClosedOverParameter(self, type:Type, name:str) -> ParameterExpression:
        """ ClosedOverParameter(self: LambdaBuilder, type: Type, name: str) -> ParameterExpression """
        ...

    def ClosedOverVariable(self, type:Type, name:str) -> Expression:
        """ ClosedOverVariable(self: LambdaBuilder, type: Type, name: str) -> Expression """
        ...

    def CreateHiddenParameter(self, name:str, type:Type) -> ParameterExpression:
        """ CreateHiddenParameter(self: LambdaBuilder, name: str, type: Type) -> ParameterExpression """
        ...

    def CreateParamsArray(self, type:Type, name:str) -> ParameterExpression:
        """ CreateParamsArray(self: LambdaBuilder, type: Type, name: str) -> ParameterExpression """
        ...

    def GetVisibleVariables(self) -> List:
        """ GetVisibleVariables(self: LambdaBuilder) -> List[ParameterExpression] """
        ...

    def HiddenVariable(self, type:Type, name:str) -> ParameterExpression:
        """ HiddenVariable(self: LambdaBuilder, type: Type, name: str) -> ParameterExpression """
        ...

    def MakeGenerator(self, label:LabelTarget, lambdaType:Type) -> LambdaExpression:
        """ MakeGenerator(self: LambdaBuilder, label: LabelTarget, lambdaType: Type) -> LambdaExpression """
        ...

    def MakeLambda(self, lambdaType:Type = ...) -> LambdaExpression:
        """
        MakeLambda(self: LambdaBuilder, lambdaType: Type) -> LambdaExpression
        MakeLambda(self: LambdaBuilder) -> LambdaExpression
        """
        ...

    def Parameter(self, type:Type, name:str) -> ParameterExpression:
        """ Parameter(self: LambdaBuilder, type: Type, name: str) -> ParameterExpression """
        ...

    def Variable(self, type:Type, name:str) -> Expression:
        """ Variable(self: LambdaBuilder, type: Type, name: str) -> Expression """
        ...


class LightDynamicExpression(Expression, IInstructionProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ArgumentCount(self):
        ...

    @property
    def Binder(self) -> CallSiteBinder:
        """ Get: Binder(self: LightDynamicExpression) -> CallSiteBinder """
        ...


    def GetArgument(self, *args): #cannot find CLR method
        """ GetArgument(self: LightDynamicExpression, index: int) -> Expression """
        ...

    def GetLightBinder(self, *args): #cannot find CLR method
        """ GetLightBinder(self: LightDynamicExpression) -> CallSiteBinder """
        ...


class LightDynamicExpression1(ILightExceptionAwareExpression, LightDynamicExpression): # skipped bases: <type 'IInstructionProvider'>, <type 'object'>
    """ no doc """
    @property
    def Argument0(self) -> Expression:
        """ Get: Argument0(self: LightDynamicExpression1) -> Expression """
        ...


    def Rewrite(self, *args): #cannot find CLR method
        """ Rewrite(self: LightDynamicExpression1, binder: CallSiteBinder, arg0: Expression) -> Expression """
        ...


class LightDynamicExpression2(ILightExceptionAwareExpression, LightDynamicExpression): # skipped bases: <type 'IInstructionProvider'>, <type 'object'>
    """ no doc """
    @property
    def Argument0(self) -> Expression:
        """ Get: Argument0(self: LightDynamicExpression2) -> Expression """
        ...

    @property
    def Argument1(self) -> Expression:
        """ Get: Argument1(self: LightDynamicExpression2) -> Expression """
        ...


    def Rewrite(self, *args): #cannot find CLR method
        """ Rewrite(self: LightDynamicExpression2, binder: CallSiteBinder, arg0: Expression, arg1: Expression) -> Expression """
        ...


class LightDynamicExpression3(ILightExceptionAwareExpression, LightDynamicExpression): # skipped bases: <type 'IInstructionProvider'>, <type 'object'>
    """ no doc """
    @property
    def Argument0(self) -> Expression:
        """ Get: Argument0(self: LightDynamicExpression3) -> Expression """
        ...

    @property
    def Argument1(self) -> Expression:
        """ Get: Argument1(self: LightDynamicExpression3) -> Expression """
        ...

    @property
    def Argument2(self) -> Expression:
        """ Get: Argument2(self: LightDynamicExpression3) -> Expression """
        ...


    def Rewrite(self, *args): #cannot find CLR method
        """ Rewrite(self: LightDynamicExpression3, binder: CallSiteBinder, arg0: Expression, arg1: Expression, arg2: Expression) -> Expression """
        ...


class LightDynamicExpression4(ILightExceptionAwareExpression, LightDynamicExpression): # skipped bases: <type 'IInstructionProvider'>, <type 'object'>
    """ no doc """
    @property
    def Argument0(self) -> Expression:
        """ Get: Argument0(self: LightDynamicExpression4) -> Expression """
        ...

    @property
    def Argument1(self) -> Expression:
        """ Get: Argument1(self: LightDynamicExpression4) -> Expression """
        ...

    @property
    def Argument2(self) -> Expression:
        """ Get: Argument2(self: LightDynamicExpression4) -> Expression """
        ...

    @property
    def Argument3(self) -> Expression:
        """ Get: Argument3(self: LightDynamicExpression4) -> Expression """
        ...


    def Rewrite(self, *args): #cannot find CLR method
        """ Rewrite(self: LightDynamicExpression4, binder: CallSiteBinder, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> Expression """
        ...


class LightLambdaExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Body(self) -> Expression:
        """ Get: Body(self: LightLambdaExpression) -> Expression """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: LightLambdaExpression) -> str """
        ...

    @property
    def Parameters(self) -> IList:
        """ Get: Parameters(self: LightLambdaExpression) -> IList[ParameterExpression] """
        ...

    @property
    def ReturnType(self) -> Type:
        """ Get: ReturnType(self: LightLambdaExpression) -> Type """
        ...


    def Compile(self, compilationThreshold:int = ...) -> Delegate:
        """
        Compile(self: LightLambdaExpression) -> Delegate
        Compile(self: LightLambdaExpression, compilationThreshold: int) -> Delegate
        """
        ...


class LightExpression(LightLambdaExpression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Type(self) -> Type:
        """ Get: Type(self: LightExpression[T]) -> Type """
        ...


    def ReduceToLambda(self) -> Expression:
        """ ReduceToLambda(self: LightExpression[T]) -> Expression[T] """
        ...


class LightTypedDynamicExpression1(LightDynamicExpression1): # skipped bases: <type 'ILightExceptionAwareExpression'>, <type 'IInstructionProvider'>, <type 'object'>
    """ no doc """
    @property
    def Type(self) -> Type:
        """ Get: Type(self: LightTypedDynamicExpression1) -> Type """
        ...



class LightTypedDynamicExpression2(LightDynamicExpression2): # skipped bases: <type 'ILightExceptionAwareExpression'>, <type 'IInstructionProvider'>, <type 'object'>
    """ no doc """
    @property
    def Type(self) -> Type:
        """ Get: Type(self: LightTypedDynamicExpression2) -> Type """
        ...



class LightTypedDynamicExpression4(LightDynamicExpression4): # skipped bases: <type 'ILightExceptionAwareExpression'>, <type 'IInstructionProvider'>, <type 'object'>
    """ no doc """
    @property
    def Type(self) -> Type:
        """ Get: Type(self: LightTypedDynamicExpression4) -> Type """
        ...



class LightTypedDynamicExpressionN(ILightExceptionAwareExpression, LightDynamicExpression): # skipped bases: <type 'IInstructionProvider'>, <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> IList:
        """ Get: Arguments(self: LightTypedDynamicExpressionN) -> IList[Expression] """
        ...


    def Rewrite(self, *args): #cannot find CLR method
        """ Rewrite(self: LightTypedDynamicExpressionN, binder: CallSiteBinder, args: IList[Expression]) -> Expression """
        ...


class TryStatementBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Catch(self, *__args) -> TryStatementBuilder:
        """
        Catch(self: TryStatementBuilder, type: Type, body: Expression) -> TryStatementBuilder
        Catch(self: TryStatementBuilder, type: Type, expr0: Expression, expr1: Expression) -> TryStatementBuilder
        Catch(self: TryStatementBuilder, type: Type, expr0: Expression, expr1: Expression, expr2: Expression) -> TryStatementBuilder
        Catch(self: TryStatementBuilder, type: Type, expr0: Expression, expr1: Expression, expr2: Expression, expr3: Expression) -> TryStatementBuilder
        Catch(self: TryStatementBuilder, type: Type, *body: Array[Expression]) -> TryStatementBuilder
        Catch(self: TryStatementBuilder, holder: ParameterExpression, expr0: Expression, expr1: Expression) -> TryStatementBuilder
        Catch(self: TryStatementBuilder, holder: ParameterExpression, expr0: Expression, expr1: Expression, expr2: Expression) -> TryStatementBuilder
        Catch(self: TryStatementBuilder, holder: ParameterExpression, expr0: Expression, expr1: Expression, expr2: Expression, expr3: Expression) -> TryStatementBuilder
        Catch(self: TryStatementBuilder, holder: ParameterExpression, *body: Array[Expression]) -> TryStatementBuilder
        Catch(self: TryStatementBuilder, holder: ParameterExpression, body: Expression) -> TryStatementBuilder
        """
        ...

    def Fault(self, body:Array) -> TryStatementBuilder:
        """ Fault(self: TryStatementBuilder, *body: Array[Expression]) -> TryStatementBuilder """
        ...

    def Filter(self, *__args) -> TryStatementBuilder:
        """
        Filter(self: TryStatementBuilder, type: Type, condition: Expression, *body: Array[Expression]) -> TryStatementBuilder
        Filter(self: TryStatementBuilder, type: Type, condition: Expression, body: Expression) -> TryStatementBuilder
        Filter(self: TryStatementBuilder, holder: ParameterExpression, condition: Expression, *body: Array[Expression]) -> TryStatementBuilder
        Filter(self: TryStatementBuilder, holder: ParameterExpression, condition: Expression, body: Expression) -> TryStatementBuilder
        """
        ...

    def Finally(self, body:Array) -> TryStatementBuilder:
        """
        Finally(self: TryStatementBuilder, *body: Array[Expression]) -> TryStatementBuilder
        Finally(self: TryStatementBuilder, body: Expression) -> TryStatementBuilder
        """
        ...

    def FinallyWithJumps(self, body:Array) -> TryStatementBuilder:
        """
        FinallyWithJumps(self: TryStatementBuilder, *body: Array[Expression]) -> TryStatementBuilder
        FinallyWithJumps(self: TryStatementBuilder, body: Expression) -> TryStatementBuilder
        """
        ...

    def ToExpression(self) -> Expression:
        """ ToExpression(self: TryStatementBuilder) -> Expression """
        ...


class Utils: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AddDebugInfo(expression, document, *__args) -> Expression:
        """
        AddDebugInfo(expression: Expression, document: SymbolDocumentInfo, start: SourceLocation, end: SourceLocation) -> Expression
        AddDebugInfo(expression: Expression, document: SymbolDocumentInfo, startLine: int, startColumn: int, endLine: int, endColumn: int) -> Expression
        """
        ...

    @staticmethod
    def Box(expression:Expression) -> Expression:
        """ Box(expression: Expression) -> Expression """
        ...

    @staticmethod
    def Coalesce(*__args) -> Tuple_[Expression, ParameterExpression]:
        """
        Coalesce(left: Expression, right: Expression) -> (Expression, ParameterExpression)
        Coalesce(builder: LambdaBuilder, left: Expression, right: Expression) -> Expression
        """
        ...

    @staticmethod
    def CoalesceFalse(*__args) -> Tuple_[Expression, ParameterExpression]:
        """
        CoalesceFalse(left: Expression, right: Expression, isTrue: MethodInfo) -> (Expression, ParameterExpression)
        CoalesceFalse(builder: LambdaBuilder, left: Expression, right: Expression, isTrue: MethodInfo) -> Expression
        """
        ...

    @staticmethod
    def CoalesceTrue(*__args) -> Tuple_[Expression, ParameterExpression]:
        """
        CoalesceTrue(left: Expression, right: Expression, isTrue: MethodInfo) -> (Expression, ParameterExpression)
        CoalesceTrue(builder: LambdaBuilder, left: Expression, right: Expression, isTrue: MethodInfo) -> Expression
        """
        ...

    @staticmethod
    def ComplexCallHelper(*__args) -> Expression:
        """
        ComplexCallHelper(method: MethodInfo, *arguments: Array[Expression]) -> Expression
        ComplexCallHelper(instance: Expression, method: MethodInfo, *arguments: Array[Expression]) -> Expression
        """
        ...

    @staticmethod
    def Constant(value:object, type:Type = ...) -> ConstantExpression:
        """
        Constant(value: object, type: Type) -> ConstantExpression
        Constant(value: object) -> Expression
        """
        ...

    @staticmethod
    def Convert(expression:Expression, type:Type) -> Expression:
        """ Convert(expression: Expression, type: Type) -> Expression """
        ...

    @staticmethod
    def DebugMark(expression:Expression, marker:str) -> Expression:
        """ DebugMark(expression: Expression, marker: str) -> Expression """
        ...

    @staticmethod
    def DebugMarker(marker:str) -> Expression:
        """ DebugMarker(marker: str) -> Expression """
        ...

    @staticmethod
    def Default(type:Type) -> DefaultExpression:
        """ Default(type: Type) -> DefaultExpression """
        ...

    @staticmethod
    def Empty() -> DefaultExpression:
        """ Empty() -> DefaultExpression """
        ...

    @staticmethod
    def FinallyFlowControl(body:Expression) -> Expression:
        """ FinallyFlowControl(body: Expression) -> Expression """
        ...

    @staticmethod
    def Generator(*__args) -> GeneratorExpression:
        """
        Generator(name: str, label: LabelTarget, body: Expression, type: Type) -> GeneratorExpression
        Generator(name: str, label: LabelTarget, body: Expression, type: Type, rewriteAssignments: bool) -> GeneratorExpression
        Generator(label: LabelTarget, body: Expression) -> GeneratorExpression
        Generator(label: LabelTarget, body: Expression, type: Type) -> GeneratorExpression
        """
        ...

    @staticmethod
    def GeneratorLambda(*__args) -> LambdaExpression:
        """
        GeneratorLambda(delegateType: Type, label: LabelTarget, body: Expression, *parameters: Array[ParameterExpression]) -> LambdaExpression
        GeneratorLambda(delegateType: Type, label: LabelTarget, body: Expression, name: str, *parameters: Array[ParameterExpression]) -> LambdaExpression
        GeneratorLambda(delegateType: Type, label: LabelTarget, body: Expression, name: str, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression
        GeneratorLambda[T](label: LabelTarget, body: Expression, *parameters: Array[ParameterExpression]) -> Expression[T]
        GeneratorLambda[T](label: LabelTarget, body: Expression, name: str, *parameters: Array[ParameterExpression]) -> Expression[T]
        GeneratorLambda[T](label: LabelTarget, body: Expression, name: str, parameters: IEnumerable[ParameterExpression]) -> Expression[T]
        GeneratorLambda(delegateType: Type, label: LabelTarget, body: Expression, name: str, rewriteAssignments: bool, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression
        """
        ...

    @staticmethod
    def GetLValueAccess(type:ExpressionType) -> ExpressionAccess:
        """ GetLValueAccess(type: ExpressionType) -> ExpressionAccess """
        ...

    @staticmethod
    def If(*__args) -> IfStatementBuilder:
        """
        If() -> IfStatementBuilder
        If(test: Expression, *body: Array[Expression]) -> IfStatementBuilder
        If(test: Expression, body: Expression) -> IfStatementBuilder
        If(tests: Array[IfStatementTest], else: Expression) -> Expression
        """
        ...

    @staticmethod
    def IfCondition(test:Expression, body:Expression) -> IfStatementTest:
        """ IfCondition(test: Expression, body: Expression) -> IfStatementTest """
        ...

    @staticmethod
    def IfThen(test:Expression, body:Expression) -> Expression:
        """
        IfThen(test: Expression, body: Expression) -> Expression
        IfThen(test: Expression, *body: Array[Expression]) -> Expression
        """
        ...

    @staticmethod
    def IfThenElse(test:Expression, body:Expression, else_:Expression) -> Expression:
        """ IfThenElse(test: Expression, body: Expression, else: Expression) -> Expression """
        ...

    @staticmethod
    def Infinite(body:Expression, break_:LabelTarget = ..., continue_:LabelTarget = ...) -> LoopExpression:
        """
        Infinite(body: Expression) -> LoopExpression
        Infinite(body: Expression, break: LabelTarget, continue: LabelTarget) -> LoopExpression
        """
        ...

    @staticmethod
    def IsAssignment(type:ExpressionType) -> bool:
        """ IsAssignment(type: ExpressionType) -> bool """
        ...

    @staticmethod
    def IsLValue(type:ExpressionType) -> bool:
        """ IsLValue(type: ExpressionType) -> bool """
        ...

    @staticmethod
    def IsReadWriteAssignment(type:ExpressionType) -> bool:
        """ IsReadWriteAssignment(type: ExpressionType) -> bool """
        ...

    @staticmethod
    def IsWriteOnlyAssignment(type:ExpressionType) -> bool:
        """ IsWriteOnlyAssignment(type: ExpressionType) -> bool """
        ...

    @staticmethod
    def Lambda(returnType:Type, name:str) -> LambdaBuilder:
        """ Lambda(returnType: Type, name: str) -> LambdaBuilder """
        ...

    @staticmethod
    def LightDynamic(binder:CallSiteBinder, *__args:Expression) -> LightDynamicExpression:
        """
        LightDynamic(binder: CallSiteBinder, arg0: Expression) -> LightDynamicExpression
        LightDynamic(binder: CallSiteBinder, returnType: Type, arg0: Expression) -> LightDynamicExpression
        LightDynamic(binder: CallSiteBinder, arg0: Expression, arg1: Expression) -> LightDynamicExpression
        LightDynamic(binder: CallSiteBinder, returnType: Type, arg0: Expression, arg1: Expression) -> LightDynamicExpression
        LightDynamic(binder: CallSiteBinder, arg0: Expression, arg1: Expression, arg2: Expression) -> LightDynamicExpression
        LightDynamic(binder: CallSiteBinder, returnType: Type, arg0: Expression, arg1: Expression, arg2: Expression) -> LightDynamicExpression
        LightDynamic(binder: CallSiteBinder, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> LightDynamicExpression
        LightDynamic(binder: CallSiteBinder, returnType: Type, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> LightDynamicExpression
        LightDynamic(binder: CallSiteBinder, arguments: IList[Expression]) -> LightDynamicExpression
        LightDynamic(binder: CallSiteBinder, returnType: Type, arguments: IList[Expression]) -> LightDynamicExpression
        LightDynamic(binder: CallSiteBinder, arguments: ExpressionCollectionBuilder[Expression]) -> LightDynamicExpression
        LightDynamic(binder: CallSiteBinder, returnType: Type, arguments: ExpressionCollectionBuilder[Expression]) -> LightDynamicExpression
        """
        ...

    @staticmethod
    def LightLambda(retType, *__args) -> LightLambdaExpression:
        """
        LightLambda(retType: Type, delegateType: Type, body: Expression, name: str, args: IList[ParameterExpression]) -> LightLambdaExpression
        LightLambda[T](retType: Type, body: Expression, name: str, args: IList[ParameterExpression]) -> LightExpression[T]
        """
        ...

    @staticmethod
    def Loop(test:Expression, increment:Expression, body:Expression, else_:Expression, break_:LabelTarget = ..., continue_:LabelTarget = ...) -> LoopExpression:
        """
        Loop(test: Expression, increment: Expression, body: Expression, else: Expression) -> LoopExpression
        Loop(test: Expression, increment: Expression, body: Expression, else: Expression, break: LabelTarget, continue: LabelTarget) -> LoopExpression
        """
        ...

    @staticmethod
    def MakeYield(target:LabelTarget, value:Expression, yieldMarker:int) -> YieldExpression:
        """ MakeYield(target: LabelTarget, value: Expression, yieldMarker: int) -> YieldExpression """
        ...

    @staticmethod
    def NewArrayHelper(type:Type, initializers:IEnumerable) -> NewArrayExpression:
        """ NewArrayHelper(type: Type, initializers: IEnumerable[Expression]) -> NewArrayExpression """
        ...

    @staticmethod
    def SimpleCallHelper(*__args) -> MethodCallExpression:
        """
        SimpleCallHelper(method: MethodInfo, *arguments: Array[Expression]) -> MethodCallExpression
        SimpleCallHelper(instance: Expression, method: MethodInfo, *arguments: Array[Expression]) -> MethodCallExpression
        """
        ...

    @staticmethod
    def SimpleNewHelper(constructor:ConstructorInfo, arguments:Array) -> NewExpression:
        """ SimpleNewHelper(constructor: ConstructorInfo, *arguments: Array[Expression]) -> NewExpression """
        ...

    @staticmethod
    def Try(*__args:Expression) -> TryStatementBuilder:
        """
        Try(body: Expression) -> TryStatementBuilder
        Try(expr0: Expression, expr1: Expression) -> TryStatementBuilder
        Try(expr0: Expression, expr1: Expression, expr2: Expression) -> TryStatementBuilder
        Try(expr0: Expression, expr1: Expression, expr2: Expression, expr3: Expression) -> TryStatementBuilder
        Try(*body: Array[Expression]) -> TryStatementBuilder
        """
        ...

    @staticmethod
    def Unless(test:Expression, body:Expression) -> Expression:
        """ Unless(test: Expression, body: Expression) -> Expression """
        ...

    @staticmethod
    def Update(expression:BinaryExpression, left:Expression, right:Expression) -> BinaryExpression:
        """ Update(expression: BinaryExpression, left: Expression, right: Expression) -> BinaryExpression """
        ...

    @staticmethod
    def Void(expression:Expression) -> Expression:
        """ Void(expression: Expression) -> Expression """
        ...

    @staticmethod
    def WeakConstant(value:object) -> MemberExpression:
        """ WeakConstant(value: object) -> MemberExpression """
        ...

    @staticmethod
    def While(test:Expression, body:Expression, else_:Expression, break_:LabelTarget = ..., continue_:LabelTarget = ...) -> LoopExpression:
        """
        While(test: Expression, body: Expression, else: Expression) -> LoopExpression
        While(test: Expression, body: Expression, else: Expression, break: LabelTarget, continue: LabelTarget) -> LoopExpression
        """
        ...

    @staticmethod
    def YieldBreak(target:LabelTarget) -> YieldExpression:
        """ YieldBreak(target: LabelTarget) -> YieldExpression """
        ...

    @staticmethod
    def YieldReturn(target:LabelTarget, value:Expression, yieldMarker:int = ...) -> YieldExpression:
        """
        YieldReturn(target: LabelTarget, value: Expression) -> YieldExpression
        YieldReturn(target: LabelTarget, value: Expression, yieldMarker: int) -> YieldExpression
        """
        ...

    __all__: list = ...


class YieldExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Target(self) -> LabelTarget:
        """ Get: Target(self: YieldExpression) -> LabelTarget """
        ...

    @property
    def Value(self) -> Expression:
        """ Get: Value(self: YieldExpression) -> Expression """
        ...

    @property
    def YieldMarker(self) -> int:
        """ Get: YieldMarker(self: YieldExpression) -> int """
        ...



