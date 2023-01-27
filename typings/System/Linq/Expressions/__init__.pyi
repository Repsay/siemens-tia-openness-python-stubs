# encoding: utf-8
# module System.Linq.Expressions calls itself Expressions
# from System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Delegate, Enum, Guid, Type

from System.Collections import IEnumerable

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Reflection import (ConstructorInfo, MemberInfo, MethodInfo, 
    PropertyInfo)

from System.Reflection.Emit import MethodBuilder

from System.Runtime.CompilerServices import (CallSiteBinder, 
    DebugInfoGenerator)

from typing import Tuple as Tuple_

"""The following names are not found in the module: T, field#
"""

# no functions
# classes

class BinaryExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Conversion(self) -> LambdaExpression:
        """ Get: Conversion(self: BinaryExpression) -> LambdaExpression """
        ...

    @property
    def IsLifted(self) -> bool:
        """ Get: IsLifted(self: BinaryExpression) -> bool """
        ...

    @property
    def IsLiftedToNull(self) -> bool:
        """ Get: IsLiftedToNull(self: BinaryExpression) -> bool """
        ...

    @property
    def Left(self) -> Expression:
        """ Get: Left(self: BinaryExpression) -> Expression """
        ...

    @property
    def Method(self) -> MethodInfo:
        """ Get: Method(self: BinaryExpression) -> MethodInfo """
        ...

    @property
    def Right(self) -> Expression:
        """ Get: Right(self: BinaryExpression) -> Expression """
        ...


    def Update(self, left:Expression, conversion:LambdaExpression, right:Expression) -> BinaryExpression:
        """ Update(self: BinaryExpression, left: Expression, conversion: LambdaExpression, right: Expression) -> BinaryExpression """
        ...


class BlockExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Expressions(self) -> ReadOnlyCollection:
        """ Get: Expressions(self: BlockExpression) -> ReadOnlyCollection[Expression] """
        ...

    @property
    def Result(self) -> Expression:
        """ Get: Result(self: BlockExpression) -> Expression """
        ...

    @property
    def Variables(self) -> ReadOnlyCollection:
        """ Get: Variables(self: BlockExpression) -> ReadOnlyCollection[ParameterExpression] """
        ...


    def Update(self, variables:IEnumerable, expressions:IEnumerable) -> BlockExpression:
        """ Update(self: BlockExpression, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]) -> BlockExpression """
        ...


class CatchBlock: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Body(self) -> Expression:
        """ Get: Body(self: CatchBlock) -> Expression """
        ...

    @property
    def Filter(self) -> Expression:
        """ Get: Filter(self: CatchBlock) -> Expression """
        ...

    @property
    def Test(self) -> Type:
        """ Get: Test(self: CatchBlock) -> Type """
        ...

    @property
    def Variable(self) -> ParameterExpression:
        """ Get: Variable(self: CatchBlock) -> ParameterExpression """
        ...


    def ToString(self) -> str:
        """ ToString(self: CatchBlock) -> str """
        ...

    def Update(self, variable:ParameterExpression, filter:Expression, body:Expression) -> CatchBlock:
        """ Update(self: CatchBlock, variable: ParameterExpression, filter: Expression, body: Expression) -> CatchBlock """
        ...


class ConditionalExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IfFalse(self) -> Expression:
        """ Get: IfFalse(self: ConditionalExpression) -> Expression """
        ...

    @property
    def IfTrue(self) -> Expression:
        """ Get: IfTrue(self: ConditionalExpression) -> Expression """
        ...

    @property
    def Test(self) -> Expression:
        """ Get: Test(self: ConditionalExpression) -> Expression """
        ...


    def Update(self, test:Expression, ifTrue:Expression, ifFalse:Expression) -> ConditionalExpression:
        """ Update(self: ConditionalExpression, test: Expression, ifTrue: Expression, ifFalse: Expression) -> ConditionalExpression """
        ...


class ConstantExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Value(self) -> object:
        """ Get: Value(self: ConstantExpression) -> object """
        ...



class DebugInfoExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Document(self) -> SymbolDocumentInfo:
        """ Get: Document(self: DebugInfoExpression) -> SymbolDocumentInfo """
        ...

    @property
    def EndColumn(self) -> int:
        """ Get: EndColumn(self: DebugInfoExpression) -> int """
        ...

    @property
    def EndLine(self) -> int:
        """ Get: EndLine(self: DebugInfoExpression) -> int """
        ...

    @property
    def IsClear(self) -> bool:
        """ Get: IsClear(self: DebugInfoExpression) -> bool """
        ...

    @property
    def StartColumn(self) -> int:
        """ Get: StartColumn(self: DebugInfoExpression) -> int """
        ...

    @property
    def StartLine(self) -> int:
        """ Get: StartLine(self: DebugInfoExpression) -> int """
        ...



class DefaultExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    pass

class IArgumentProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ArgumentCount(self) -> int:
        """ Get: ArgumentCount(self: IArgumentProvider) -> int """
        ...


    def GetArgument(self, index:int) -> Expression:
        """ GetArgument(self: IArgumentProvider, index: int) -> Expression """
        ...


class IDynamicExpression(IArgumentProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DelegateType(self) -> Type:
        """ Get: DelegateType(self: IDynamicExpression) -> Type """
        ...


    def CreateCallSite(self) -> object:
        """ CreateCallSite(self: IDynamicExpression) -> object """
        ...

    def Rewrite(self, args:Array) -> Expression:
        """ Rewrite(self: IDynamicExpression, args: Array[Expression]) -> Expression """
        ...


class DynamicExpression(Expression, IDynamicExpression): # skipped bases: <type 'IArgumentProvider'>, <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> ReadOnlyCollection:
        """ Get: Arguments(self: DynamicExpression) -> ReadOnlyCollection[Expression] """
        ...

    @property
    def Binder(self) -> CallSiteBinder:
        """ Get: Binder(self: DynamicExpression) -> CallSiteBinder """
        ...


    def Update(self, arguments:IEnumerable) -> DynamicExpression:
        """ Update(self: DynamicExpression, arguments: IEnumerable[Expression]) -> DynamicExpression """
        ...


class ExpressionVisitor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Visit(self, *__args:ReadOnlyCollection) -> ReadOnlyCollection:
        """
        Visit(self: ExpressionVisitor, nodes: ReadOnlyCollection[Expression]) -> ReadOnlyCollection[Expression]
        Visit(self: ExpressionVisitor, node: Expression) -> Expression
        Visit[T](nodes: ReadOnlyCollection[T], elementVisitor: Func[T, T]) -> ReadOnlyCollection[T]
        """
        ...

    def VisitAndConvert(self, *__args): # -> T
        """
        VisitAndConvert[T](self: ExpressionVisitor, node: T, callerName: str) -> T
        VisitAndConvert[T](self: ExpressionVisitor, nodes: ReadOnlyCollection[T], callerName: str) -> ReadOnlyCollection[T]
        """
        ...

    def VisitBinary(self, *args): #cannot find CLR method
        """ VisitBinary(self: ExpressionVisitor, node: BinaryExpression) -> Expression """
        ...

    def VisitBlock(self, *args): #cannot find CLR method
        """ VisitBlock(self: ExpressionVisitor, node: BlockExpression) -> Expression """
        ...

    def VisitCatchBlock(self, *args): #cannot find CLR method
        """ VisitCatchBlock(self: ExpressionVisitor, node: CatchBlock) -> CatchBlock """
        ...

    def VisitConditional(self, *args): #cannot find CLR method
        """ VisitConditional(self: ExpressionVisitor, node: ConditionalExpression) -> Expression """
        ...

    def VisitConstant(self, *args): #cannot find CLR method
        """ VisitConstant(self: ExpressionVisitor, node: ConstantExpression) -> Expression """
        ...

    def VisitDebugInfo(self, *args): #cannot find CLR method
        """ VisitDebugInfo(self: ExpressionVisitor, node: DebugInfoExpression) -> Expression """
        ...

    def VisitDefault(self, *args): #cannot find CLR method
        """ VisitDefault(self: ExpressionVisitor, node: DefaultExpression) -> Expression """
        ...

    def VisitDynamic(self, *args): #cannot find CLR method
        """ VisitDynamic(self: ExpressionVisitor, node: DynamicExpression) -> Expression """
        ...

    def VisitElementInit(self, *args): #cannot find CLR method
        """ VisitElementInit(self: ExpressionVisitor, node: ElementInit) -> ElementInit """
        ...

    def VisitExtension(self, *args): #cannot find CLR method
        """ VisitExtension(self: ExpressionVisitor, node: Expression) -> Expression """
        ...

    def VisitGoto(self, *args): #cannot find CLR method
        """ VisitGoto(self: ExpressionVisitor, node: GotoExpression) -> Expression """
        ...

    def VisitIndex(self, *args): #cannot find CLR method
        """ VisitIndex(self: ExpressionVisitor, node: IndexExpression) -> Expression """
        ...

    def VisitInvocation(self, *args): #cannot find CLR method
        """ VisitInvocation(self: ExpressionVisitor, node: InvocationExpression) -> Expression """
        ...

    def VisitLabel(self, *args): #cannot find CLR method
        """ VisitLabel(self: ExpressionVisitor, node: LabelExpression) -> Expression """
        ...

    def VisitLabelTarget(self, *args): #cannot find CLR method
        """ VisitLabelTarget(self: ExpressionVisitor, node: LabelTarget) -> LabelTarget """
        ...

    def VisitLambda(self, *args): #cannot find CLR method
        """ VisitLambda[T](self: ExpressionVisitor, node: Expression[T]) -> Expression """
        ...

    def VisitListInit(self, *args): #cannot find CLR method
        """ VisitListInit(self: ExpressionVisitor, node: ListInitExpression) -> Expression """
        ...

    def VisitLoop(self, *args): #cannot find CLR method
        """ VisitLoop(self: ExpressionVisitor, node: LoopExpression) -> Expression """
        ...

    def VisitMember(self, *args): #cannot find CLR method
        """ VisitMember(self: ExpressionVisitor, node: MemberExpression) -> Expression """
        ...

    def VisitMemberAssignment(self, *args): #cannot find CLR method
        """ VisitMemberAssignment(self: ExpressionVisitor, node: MemberAssignment) -> MemberAssignment """
        ...

    def VisitMemberBinding(self, *args): #cannot find CLR method
        """ VisitMemberBinding(self: ExpressionVisitor, node: MemberBinding) -> MemberBinding """
        ...

    def VisitMemberInit(self, *args): #cannot find CLR method
        """ VisitMemberInit(self: ExpressionVisitor, node: MemberInitExpression) -> Expression """
        ...

    def VisitMemberListBinding(self, *args): #cannot find CLR method
        """ VisitMemberListBinding(self: ExpressionVisitor, node: MemberListBinding) -> MemberListBinding """
        ...

    def VisitMemberMemberBinding(self, *args): #cannot find CLR method
        """ VisitMemberMemberBinding(self: ExpressionVisitor, node: MemberMemberBinding) -> MemberMemberBinding """
        ...

    def VisitMethodCall(self, *args): #cannot find CLR method
        """ VisitMethodCall(self: ExpressionVisitor, node: MethodCallExpression) -> Expression """
        ...

    def VisitNew(self, *args): #cannot find CLR method
        """ VisitNew(self: ExpressionVisitor, node: NewExpression) -> Expression """
        ...

    def VisitNewArray(self, *args): #cannot find CLR method
        """ VisitNewArray(self: ExpressionVisitor, node: NewArrayExpression) -> Expression """
        ...

    def VisitParameter(self, *args): #cannot find CLR method
        """ VisitParameter(self: ExpressionVisitor, node: ParameterExpression) -> Expression """
        ...

    def VisitRuntimeVariables(self, *args): #cannot find CLR method
        """ VisitRuntimeVariables(self: ExpressionVisitor, node: RuntimeVariablesExpression) -> Expression """
        ...

    def VisitSwitch(self, *args): #cannot find CLR method
        """ VisitSwitch(self: ExpressionVisitor, node: SwitchExpression) -> Expression """
        ...

    def VisitSwitchCase(self, *args): #cannot find CLR method
        """ VisitSwitchCase(self: ExpressionVisitor, node: SwitchCase) -> SwitchCase """
        ...

    def VisitTry(self, *args): #cannot find CLR method
        """ VisitTry(self: ExpressionVisitor, node: TryExpression) -> Expression """
        ...

    def VisitTypeBinary(self, *args): #cannot find CLR method
        """ VisitTypeBinary(self: ExpressionVisitor, node: TypeBinaryExpression) -> Expression """
        ...

    def VisitUnary(self, *args): #cannot find CLR method
        """ VisitUnary(self: ExpressionVisitor, node: UnaryExpression) -> Expression """
        ...


class DynamicExpressionVisitor(ExpressionVisitor): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ElementInit(IArgumentProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AddMethod(self) -> MethodInfo:
        """ Get: AddMethod(self: ElementInit) -> MethodInfo """
        ...

    @property
    def Arguments(self) -> ReadOnlyCollection:
        """ Get: Arguments(self: ElementInit) -> ReadOnlyCollection[Expression] """
        ...


    def ToString(self) -> str:
        """ ToString(self: ElementInit) -> str """
        ...

    def Update(self, arguments:IEnumerable) -> ElementInit:
        """ Update(self: ElementInit, arguments: IEnumerable[Expression]) -> ElementInit """
        ...


class Expression: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CanReduce(self) -> bool:
        """ Get: CanReduce(self: Expression) -> bool """
        ...

    @property
    def NodeType(self) -> ExpressionType:
        """ Get: NodeType(self: Expression) -> ExpressionType """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: Expression) -> Type """
        ...


    def Accept(self, *args): #cannot find CLR method
        """ Accept(self: Expression, visitor: ExpressionVisitor) -> Expression """
        ...

    @staticmethod
    def Add(left:Expression, right:Expression, method:MethodInfo = ...) -> BinaryExpression:
        """
        Add(left: Expression, right: Expression) -> BinaryExpression
        Add(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def AddAssign(left:Expression, right:Expression, method:MethodInfo = ..., conversion:LambdaExpression = ...) -> BinaryExpression:
        """
        AddAssign(left: Expression, right: Expression) -> BinaryExpression
        AddAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        AddAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression
        """
        ...

    @staticmethod
    def AddAssignChecked(left:Expression, right:Expression, method:MethodInfo = ..., conversion:LambdaExpression = ...) -> BinaryExpression:
        """
        AddAssignChecked(left: Expression, right: Expression) -> BinaryExpression
        AddAssignChecked(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        AddAssignChecked(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression
        """
        ...

    @staticmethod
    def AddChecked(left:Expression, right:Expression, method:MethodInfo = ...) -> BinaryExpression:
        """
        AddChecked(left: Expression, right: Expression) -> BinaryExpression
        AddChecked(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def And(left:Expression, right:Expression, method:MethodInfo = ...) -> BinaryExpression:
        """
        And(left: Expression, right: Expression) -> BinaryExpression
        And(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def AndAlso(left:Expression, right:Expression, method:MethodInfo = ...) -> BinaryExpression:
        """
        AndAlso(left: Expression, right: Expression) -> BinaryExpression
        AndAlso(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def AndAssign(left:Expression, right:Expression, method:MethodInfo = ..., conversion:LambdaExpression = ...) -> BinaryExpression:
        """
        AndAssign(left: Expression, right: Expression) -> BinaryExpression
        AndAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        AndAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression
        """
        ...

    @staticmethod
    def ArrayAccess(array:Expression, indexes:Array) -> IndexExpression:
        """
        ArrayAccess(array: Expression, *indexes: Array[Expression]) -> IndexExpression
        ArrayAccess(array: Expression, indexes: IEnumerable[Expression]) -> IndexExpression
        """
        ...

    @staticmethod
    def ArrayIndex(array:Expression, *__args:Array) -> MethodCallExpression:
        """
        ArrayIndex(array: Expression, *indexes: Array[Expression]) -> MethodCallExpression
        ArrayIndex(array: Expression, index: Expression) -> BinaryExpression
        ArrayIndex(array: Expression, indexes: IEnumerable[Expression]) -> MethodCallExpression
        """
        ...

    @staticmethod
    def ArrayLength(array:Expression) -> UnaryExpression:
        """ ArrayLength(array: Expression) -> UnaryExpression """
        ...

    @staticmethod
    def Assign(left:Expression, right:Expression) -> BinaryExpression:
        """ Assign(left: Expression, right: Expression) -> BinaryExpression """
        ...

    @staticmethod
    def Bind(*__args) -> MemberAssignment:
        """
        Bind(propertyAccessor: MethodInfo, expression: Expression) -> MemberAssignment
        Bind(member: MemberInfo, expression: Expression) -> MemberAssignment
        """
        ...

    @staticmethod
    def Block(*__args:IEnumerable) -> BlockExpression:
        """
        Block(expressions: IEnumerable[Expression]) -> BlockExpression
        Block(type: Type, *expressions: Array[Expression]) -> BlockExpression
        Block(type: Type, expressions: IEnumerable[Expression]) -> BlockExpression
        Block(variables: IEnumerable[ParameterExpression], *expressions: Array[Expression]) -> BlockExpression
        Block(type: Type, variables: IEnumerable[ParameterExpression], *expressions: Array[Expression]) -> BlockExpression
        Block(arg0: Expression, arg1: Expression) -> BlockExpression
        Block(arg0: Expression, arg1: Expression, arg2: Expression) -> BlockExpression
        Block(arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> BlockExpression
        Block(arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression, arg4: Expression) -> BlockExpression
        Block(*expressions: Array[Expression]) -> BlockExpression
        Block(variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]) -> BlockExpression
        Block(type: Type, variables: IEnumerable[ParameterExpression], expressions: IEnumerable[Expression]) -> BlockExpression
        """
        ...

    @staticmethod
    def Break(target:LabelTarget, *__args:Expression) -> GotoExpression:
        """
        Break(target: LabelTarget) -> GotoExpression
        Break(target: LabelTarget, value: Expression) -> GotoExpression
        Break(target: LabelTarget, type: Type) -> GotoExpression
        Break(target: LabelTarget, value: Expression, type: Type) -> GotoExpression
        """
        ...

    @staticmethod
    def Call(*__args) -> MethodCallExpression:
        """
        Call(method: MethodInfo, arg0: Expression) -> MethodCallExpression
        Call(method: MethodInfo, arg0: Expression, arg1: Expression) -> MethodCallExpression
        Call(method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression) -> MethodCallExpression
        Call(method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> MethodCallExpression
        Call(method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression, arg4: Expression) -> MethodCallExpression
        Call(method: MethodInfo, *arguments: Array[Expression]) -> MethodCallExpression
        Call(method: MethodInfo, arguments: IEnumerable[Expression]) -> MethodCallExpression
        Call(instance: Expression, method: MethodInfo) -> MethodCallExpression
        Call(instance: Expression, method: MethodInfo, *arguments: Array[Expression]) -> MethodCallExpression
        Call(instance: Expression, method: MethodInfo, arg0: Expression, arg1: Expression) -> MethodCallExpression
        Call(instance: Expression, method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression) -> MethodCallExpression
        Call(instance: Expression, method: MethodInfo, arguments: IEnumerable[Expression]) -> MethodCallExpression
        Call(instance: Expression, methodName: str, typeArguments: Array[Type], *arguments: Array[Expression]) -> MethodCallExpression
        Call(type: Type, methodName: str, typeArguments: Array[Type], *arguments: Array[Expression]) -> MethodCallExpression
        """
        ...

    @staticmethod
    def Catch(*__args) -> CatchBlock:
        """
        Catch(type: Type, body: Expression) -> CatchBlock
        Catch(variable: ParameterExpression, body: Expression) -> CatchBlock
        Catch(type: Type, body: Expression, filter: Expression) -> CatchBlock
        Catch(variable: ParameterExpression, body: Expression, filter: Expression) -> CatchBlock
        """
        ...

    @staticmethod
    def ClearDebugInfo(document:SymbolDocumentInfo) -> DebugInfoExpression:
        """ ClearDebugInfo(document: SymbolDocumentInfo) -> DebugInfoExpression """
        ...

    @staticmethod
    def Coalesce(left:Expression, right:Expression, conversion:LambdaExpression = ...) -> BinaryExpression:
        """
        Coalesce(left: Expression, right: Expression) -> BinaryExpression
        Coalesce(left: Expression, right: Expression, conversion: LambdaExpression) -> BinaryExpression
        """
        ...

    @staticmethod
    def Condition(test:Expression, ifTrue:Expression, ifFalse:Expression, type:Type = ...) -> ConditionalExpression:
        """
        Condition(test: Expression, ifTrue: Expression, ifFalse: Expression) -> ConditionalExpression
        Condition(test: Expression, ifTrue: Expression, ifFalse: Expression, type: Type) -> ConditionalExpression
        """
        ...

    @staticmethod
    def Constant(value:object, type:Type = ...) -> ConstantExpression:
        """
        Constant(value: object) -> ConstantExpression
        Constant(value: object, type: Type) -> ConstantExpression
        """
        ...

    @staticmethod
    def Continue(target:LabelTarget, type:Type = ...) -> GotoExpression:
        """
        Continue(target: LabelTarget) -> GotoExpression
        Continue(target: LabelTarget, type: Type) -> GotoExpression
        """
        ...

    @staticmethod
    def Convert(expression:Expression, type:Type, method:MethodInfo = ...) -> UnaryExpression:
        """
        Convert(expression: Expression, type: Type) -> UnaryExpression
        Convert(expression: Expression, type: Type, method: MethodInfo) -> UnaryExpression
        """
        ...

    @staticmethod
    def ConvertChecked(expression:Expression, type:Type, method:MethodInfo = ...) -> UnaryExpression:
        """
        ConvertChecked(expression: Expression, type: Type) -> UnaryExpression
        ConvertChecked(expression: Expression, type: Type, method: MethodInfo) -> UnaryExpression
        """
        ...

    @staticmethod
    def DebugInfo(document:SymbolDocumentInfo, startLine:int, startColumn:int, endLine:int, endColumn:int) -> DebugInfoExpression:
        """ DebugInfo(document: SymbolDocumentInfo, startLine: int, startColumn: int, endLine: int, endColumn: int) -> DebugInfoExpression """
        ...

    @staticmethod
    def Decrement(expression:Expression, method:MethodInfo = ...) -> UnaryExpression:
        """
        Decrement(expression: Expression) -> UnaryExpression
        Decrement(expression: Expression, method: MethodInfo) -> UnaryExpression
        """
        ...

    @staticmethod
    def Default(type:Type) -> DefaultExpression:
        """ Default(type: Type) -> DefaultExpression """
        ...

    @staticmethod
    def Divide(left:Expression, right:Expression, method:MethodInfo = ...) -> BinaryExpression:
        """
        Divide(left: Expression, right: Expression) -> BinaryExpression
        Divide(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def DivideAssign(left:Expression, right:Expression, method:MethodInfo = ..., conversion:LambdaExpression = ...) -> BinaryExpression:
        """
        DivideAssign(left: Expression, right: Expression) -> BinaryExpression
        DivideAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        DivideAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression
        """
        ...

    @staticmethod
    def Dynamic(binder:CallSiteBinder, returnType:Type, *__args:Array) -> DynamicExpression:
        """
        Dynamic(binder: CallSiteBinder, returnType: Type, *arguments: Array[Expression]) -> DynamicExpression
        Dynamic(binder: CallSiteBinder, returnType: Type, arg0: Expression) -> DynamicExpression
        Dynamic(binder: CallSiteBinder, returnType: Type, arg0: Expression, arg1: Expression) -> DynamicExpression
        Dynamic(binder: CallSiteBinder, returnType: Type, arg0: Expression, arg1: Expression, arg2: Expression) -> DynamicExpression
        Dynamic(binder: CallSiteBinder, returnType: Type, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> DynamicExpression
        Dynamic(binder: CallSiteBinder, returnType: Type, arguments: IEnumerable[Expression]) -> DynamicExpression
        """
        ...

    @staticmethod
    def ElementInit(addMethod:MethodInfo, arguments:Array) -> ElementInit:
        """
        ElementInit(addMethod: MethodInfo, *arguments: Array[Expression]) -> ElementInit
        ElementInit(addMethod: MethodInfo, arguments: IEnumerable[Expression]) -> ElementInit
        """
        ...

    @staticmethod
    def Empty() -> DefaultExpression:
        """ Empty() -> DefaultExpression """
        ...

    @staticmethod
    def Equal(left:Expression, right:Expression, liftToNull:bool = ..., method:MethodInfo = ...) -> BinaryExpression:
        """
        Equal(left: Expression, right: Expression) -> BinaryExpression
        Equal(left: Expression, right: Expression, liftToNull: bool, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def ExclusiveOr(left:Expression, right:Expression, method:MethodInfo = ...) -> BinaryExpression:
        """
        ExclusiveOr(left: Expression, right: Expression) -> BinaryExpression
        ExclusiveOr(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def ExclusiveOrAssign(left:Expression, right:Expression, method:MethodInfo = ..., conversion:LambdaExpression = ...) -> BinaryExpression:
        """
        ExclusiveOrAssign(left: Expression, right: Expression) -> BinaryExpression
        ExclusiveOrAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        ExclusiveOrAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression
        """
        ...

    @staticmethod
    def Field(expression:Expression, *__args:str) -> MemberExpression:
        """
        Field(expression: Expression, type: Type, fieldName: str) -> MemberExpression
        Field(expression: Expression, fieldName: str) -> MemberExpression
        Field(expression: Expression, field: FieldInfo) -> MemberExpression
        """
        ...

    @staticmethod
    def GetActionType(typeArgs:Array) -> Type:
        """ GetActionType(*typeArgs: Array[Type]) -> Type """
        ...

    @staticmethod
    def GetDelegateType(typeArgs:Array) -> Type:
        """ GetDelegateType(*typeArgs: Array[Type]) -> Type """
        ...

    @staticmethod
    def GetFuncType(typeArgs:Array) -> Type:
        """ GetFuncType(*typeArgs: Array[Type]) -> Type """
        ...

    @staticmethod
    def Goto(target:LabelTarget, *__args:Type) -> GotoExpression:
        """
        Goto(target: LabelTarget) -> GotoExpression
        Goto(target: LabelTarget, type: Type) -> GotoExpression
        Goto(target: LabelTarget, value: Expression) -> GotoExpression
        Goto(target: LabelTarget, value: Expression, type: Type) -> GotoExpression
        """
        ...

    @staticmethod
    def GreaterThan(left:Expression, right:Expression, liftToNull:bool = ..., method:MethodInfo = ...) -> BinaryExpression:
        """
        GreaterThan(left: Expression, right: Expression) -> BinaryExpression
        GreaterThan(left: Expression, right: Expression, liftToNull: bool, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def GreaterThanOrEqual(left:Expression, right:Expression, liftToNull:bool = ..., method:MethodInfo = ...) -> BinaryExpression:
        """
        GreaterThanOrEqual(left: Expression, right: Expression) -> BinaryExpression
        GreaterThanOrEqual(left: Expression, right: Expression, liftToNull: bool, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def IfThen(test:Expression, ifTrue:Expression) -> ConditionalExpression:
        """ IfThen(test: Expression, ifTrue: Expression) -> ConditionalExpression """
        ...

    @staticmethod
    def IfThenElse(test:Expression, ifTrue:Expression, ifFalse:Expression) -> ConditionalExpression:
        """ IfThenElse(test: Expression, ifTrue: Expression, ifFalse: Expression) -> ConditionalExpression """
        ...

    @staticmethod
    def Increment(expression:Expression, method:MethodInfo = ...) -> UnaryExpression:
        """
        Increment(expression: Expression) -> UnaryExpression
        Increment(expression: Expression, method: MethodInfo) -> UnaryExpression
        """
        ...

    @staticmethod
    def Invoke(expression:Expression, arguments:Array) -> InvocationExpression:
        """
        Invoke(expression: Expression, *arguments: Array[Expression]) -> InvocationExpression
        Invoke(expression: Expression, arguments: IEnumerable[Expression]) -> InvocationExpression
        """
        ...

    @staticmethod
    def IsFalse(expression:Expression, method:MethodInfo = ...) -> UnaryExpression:
        """
        IsFalse(expression: Expression) -> UnaryExpression
        IsFalse(expression: Expression, method: MethodInfo) -> UnaryExpression
        """
        ...

    @staticmethod
    def IsTrue(expression:Expression, method:MethodInfo = ...) -> UnaryExpression:
        """
        IsTrue(expression: Expression) -> UnaryExpression
        IsTrue(expression: Expression, method: MethodInfo) -> UnaryExpression
        """
        ...

    @staticmethod
    def Label(*__args:LabelTarget) -> LabelExpression:
        """
        Label(target: LabelTarget) -> LabelExpression
        Label() -> LabelTarget
        Label(name: str) -> LabelTarget
        Label(type: Type) -> LabelTarget
        Label(type: Type, name: str) -> LabelTarget
        Label(target: LabelTarget, defaultValue: Expression) -> LabelExpression
        """
        ...

    @staticmethod
    def Lambda(*__args) -> LambdaExpression:
        """
        Lambda(body: Expression, *parameters: Array[ParameterExpression]) -> LambdaExpression
        Lambda[TDelegate](body: Expression, name: str, parameters: IEnumerable[ParameterExpression]) -> Expression[TDelegate]
        Lambda[TDelegate](body: Expression, tailCall: bool, parameters: IEnumerable[ParameterExpression]) -> Expression[TDelegate]
        Lambda[TDelegate](body: Expression, parameters: IEnumerable[ParameterExpression]) -> Expression[TDelegate]
        Lambda[TDelegate](body: Expression, tailCall: bool, *parameters: Array[ParameterExpression]) -> Expression[TDelegate]
        Lambda[TDelegate](body: Expression, *parameters: Array[ParameterExpression]) -> Expression[TDelegate]
        Lambda(delegateType: Type, body: Expression, name: str, tailCall: bool, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression
        Lambda(delegateType: Type, body: Expression, name: str, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression
        Lambda(body: Expression, name: str, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression
        Lambda(delegateType: Type, body: Expression, tailCall: bool, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression
        Lambda(delegateType: Type, body: Expression, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression
        Lambda(delegateType: Type, body: Expression, tailCall: bool, *parameters: Array[ParameterExpression]) -> LambdaExpression
        Lambda(delegateType: Type, body: Expression, *parameters: Array[ParameterExpression]) -> LambdaExpression
        Lambda(body: Expression, tailCall: bool, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression
        Lambda(body: Expression, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression
        Lambda(body: Expression, tailCall: bool, *parameters: Array[ParameterExpression]) -> LambdaExpression
        Lambda[TDelegate](body: Expression, name: str, tailCall: bool, parameters: IEnumerable[ParameterExpression]) -> Expression[TDelegate]
        Lambda(body: Expression, name: str, tailCall: bool, parameters: IEnumerable[ParameterExpression]) -> LambdaExpression
        """
        ...

    @staticmethod
    def LeftShift(left:Expression, right:Expression, method:MethodInfo = ...) -> BinaryExpression:
        """
        LeftShift(left: Expression, right: Expression) -> BinaryExpression
        LeftShift(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def LeftShiftAssign(left:Expression, right:Expression, method:MethodInfo = ..., conversion:LambdaExpression = ...) -> BinaryExpression:
        """
        LeftShiftAssign(left: Expression, right: Expression) -> BinaryExpression
        LeftShiftAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        LeftShiftAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression
        """
        ...

    @staticmethod
    def LessThan(left:Expression, right:Expression, liftToNull:bool = ..., method:MethodInfo = ...) -> BinaryExpression:
        """
        LessThan(left: Expression, right: Expression) -> BinaryExpression
        LessThan(left: Expression, right: Expression, liftToNull: bool, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def LessThanOrEqual(left:Expression, right:Expression, liftToNull:bool = ..., method:MethodInfo = ...) -> BinaryExpression:
        """
        LessThanOrEqual(left: Expression, right: Expression) -> BinaryExpression
        LessThanOrEqual(left: Expression, right: Expression, liftToNull: bool, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def ListBind(*__args) -> MemberListBinding:
        """
        ListBind(member: MemberInfo, *initializers: Array[ElementInit]) -> MemberListBinding
        ListBind(member: MemberInfo, initializers: IEnumerable[ElementInit]) -> MemberListBinding
        ListBind(propertyAccessor: MethodInfo, *initializers: Array[ElementInit]) -> MemberListBinding
        ListBind(propertyAccessor: MethodInfo, initializers: IEnumerable[ElementInit]) -> MemberListBinding
        """
        ...

    @staticmethod
    def ListInit(newExpression:NewExpression, *__args:Array) -> ListInitExpression:
        """
        ListInit(newExpression: NewExpression, *initializers: Array[Expression]) -> ListInitExpression
        ListInit(newExpression: NewExpression, addMethod: MethodInfo, *initializers: Array[Expression]) -> ListInitExpression
        ListInit(newExpression: NewExpression, *initializers: Array[ElementInit]) -> ListInitExpression
        ListInit(newExpression: NewExpression, initializers: IEnumerable[ElementInit]) -> ListInitExpression
        ListInit(newExpression: NewExpression, initializers: IEnumerable[Expression]) -> ListInitExpression
        ListInit(newExpression: NewExpression, addMethod: MethodInfo, initializers: IEnumerable[Expression]) -> ListInitExpression
        """
        ...

    @staticmethod
    def Loop(body:Expression, break_:LabelTarget = ..., continue_:LabelTarget = ...) -> LoopExpression:
        """
        Loop(body: Expression) -> LoopExpression
        Loop(body: Expression, break: LabelTarget) -> LoopExpression
        Loop(body: Expression, break: LabelTarget, continue: LabelTarget) -> LoopExpression
        """
        ...

    @staticmethod
    def MakeBinary(binaryType:ExpressionType, left:Expression, right:Expression, liftToNull:bool = ..., method:MethodInfo = ..., conversion:LambdaExpression = ...) -> BinaryExpression:
        """
        MakeBinary(binaryType: ExpressionType, left: Expression, right: Expression) -> BinaryExpression
        MakeBinary(binaryType: ExpressionType, left: Expression, right: Expression, liftToNull: bool, method: MethodInfo) -> BinaryExpression
        MakeBinary(binaryType: ExpressionType, left: Expression, right: Expression, liftToNull: bool, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression
        """
        ...

    @staticmethod
    def MakeCatchBlock(type:Type, variable:ParameterExpression, body:Expression, filter:Expression) -> CatchBlock:
        """ MakeCatchBlock(type: Type, variable: ParameterExpression, body: Expression, filter: Expression) -> CatchBlock """
        ...

    @staticmethod
    def MakeDynamic(delegateType:Type, binder:CallSiteBinder, *__args:Array) -> DynamicExpression:
        """
        MakeDynamic(delegateType: Type, binder: CallSiteBinder, *arguments: Array[Expression]) -> DynamicExpression
        MakeDynamic(delegateType: Type, binder: CallSiteBinder, arguments: IEnumerable[Expression]) -> DynamicExpression
        MakeDynamic(delegateType: Type, binder: CallSiteBinder, arg0: Expression) -> DynamicExpression
        MakeDynamic(delegateType: Type, binder: CallSiteBinder, arg0: Expression, arg1: Expression) -> DynamicExpression
        MakeDynamic(delegateType: Type, binder: CallSiteBinder, arg0: Expression, arg1: Expression, arg2: Expression) -> DynamicExpression
        MakeDynamic(delegateType: Type, binder: CallSiteBinder, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> DynamicExpression
        """
        ...

    @staticmethod
    def MakeGoto(kind:GotoExpressionKind, target:LabelTarget, value:Expression, type:Type) -> GotoExpression:
        """ MakeGoto(kind: GotoExpressionKind, target: LabelTarget, value: Expression, type: Type) -> GotoExpression """
        ...

    @staticmethod
    def MakeIndex(instance:Expression, indexer:PropertyInfo, arguments:IEnumerable) -> IndexExpression:
        """ MakeIndex(instance: Expression, indexer: PropertyInfo, arguments: IEnumerable[Expression]) -> IndexExpression """
        ...

    @staticmethod
    def MakeMemberAccess(expression:Expression, member:MemberInfo) -> MemberExpression:
        """ MakeMemberAccess(expression: Expression, member: MemberInfo) -> MemberExpression """
        ...

    @staticmethod
    def MakeTry(type:Type, body:Expression, finally_:Expression, fault:Expression, handlers:IEnumerable) -> TryExpression:
        """ MakeTry(type: Type, body: Expression, finally: Expression, fault: Expression, handlers: IEnumerable[CatchBlock]) -> TryExpression """
        ...

    @staticmethod
    def MakeUnary(unaryType:ExpressionType, operand:Expression, type:Type, method:MethodInfo = ...) -> UnaryExpression:
        """
        MakeUnary(unaryType: ExpressionType, operand: Expression, type: Type) -> UnaryExpression
        MakeUnary(unaryType: ExpressionType, operand: Expression, type: Type, method: MethodInfo) -> UnaryExpression
        """
        ...

    @staticmethod
    def MemberBind(*__args) -> MemberMemberBinding:
        """
        MemberBind(member: MemberInfo, *bindings: Array[MemberBinding]) -> MemberMemberBinding
        MemberBind(member: MemberInfo, bindings: IEnumerable[MemberBinding]) -> MemberMemberBinding
        MemberBind(propertyAccessor: MethodInfo, *bindings: Array[MemberBinding]) -> MemberMemberBinding
        MemberBind(propertyAccessor: MethodInfo, bindings: IEnumerable[MemberBinding]) -> MemberMemberBinding
        """
        ...

    @staticmethod
    def MemberInit(newExpression:NewExpression, bindings:Array) -> MemberInitExpression:
        """
        MemberInit(newExpression: NewExpression, *bindings: Array[MemberBinding]) -> MemberInitExpression
        MemberInit(newExpression: NewExpression, bindings: IEnumerable[MemberBinding]) -> MemberInitExpression
        """
        ...

    @staticmethod
    def Modulo(left:Expression, right:Expression, method:MethodInfo = ...) -> BinaryExpression:
        """
        Modulo(left: Expression, right: Expression) -> BinaryExpression
        Modulo(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def ModuloAssign(left:Expression, right:Expression, method:MethodInfo = ..., conversion:LambdaExpression = ...) -> BinaryExpression:
        """
        ModuloAssign(left: Expression, right: Expression) -> BinaryExpression
        ModuloAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        ModuloAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression
        """
        ...

    @staticmethod
    def Multiply(left:Expression, right:Expression, method:MethodInfo = ...) -> BinaryExpression:
        """
        Multiply(left: Expression, right: Expression) -> BinaryExpression
        Multiply(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def MultiplyAssign(left:Expression, right:Expression, method:MethodInfo = ..., conversion:LambdaExpression = ...) -> BinaryExpression:
        """
        MultiplyAssign(left: Expression, right: Expression) -> BinaryExpression
        MultiplyAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        MultiplyAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression
        """
        ...

    @staticmethod
    def MultiplyAssignChecked(left:Expression, right:Expression, method:MethodInfo = ..., conversion:LambdaExpression = ...) -> BinaryExpression:
        """
        MultiplyAssignChecked(left: Expression, right: Expression) -> BinaryExpression
        MultiplyAssignChecked(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        MultiplyAssignChecked(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression
        """
        ...

    @staticmethod
    def MultiplyChecked(left:Expression, right:Expression, method:MethodInfo = ...) -> BinaryExpression:
        """
        MultiplyChecked(left: Expression, right: Expression) -> BinaryExpression
        MultiplyChecked(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def Negate(expression:Expression, method:MethodInfo = ...) -> UnaryExpression:
        """
        Negate(expression: Expression) -> UnaryExpression
        Negate(expression: Expression, method: MethodInfo) -> UnaryExpression
        """
        ...

    @staticmethod
    def NegateChecked(expression:Expression, method:MethodInfo = ...) -> UnaryExpression:
        """
        NegateChecked(expression: Expression) -> UnaryExpression
        NegateChecked(expression: Expression, method: MethodInfo) -> UnaryExpression
        """
        ...

    @staticmethod
    def New(*__args:ConstructorInfo) -> NewExpression:
        """
        New(constructor: ConstructorInfo) -> NewExpression
        New(constructor: ConstructorInfo, *arguments: Array[Expression]) -> NewExpression
        New(constructor: ConstructorInfo, arguments: IEnumerable[Expression]) -> NewExpression
        New(constructor: ConstructorInfo, arguments: IEnumerable[Expression], members: IEnumerable[MemberInfo]) -> NewExpression
        New(constructor: ConstructorInfo, arguments: IEnumerable[Expression], *members: Array[MemberInfo]) -> NewExpression
        New(type: Type) -> NewExpression
        """
        ...

    @staticmethod
    def NewArrayBounds(type:Type, bounds:Array) -> NewArrayExpression:
        """
        NewArrayBounds(type: Type, *bounds: Array[Expression]) -> NewArrayExpression
        NewArrayBounds(type: Type, bounds: IEnumerable[Expression]) -> NewArrayExpression
        """
        ...

    @staticmethod
    def NewArrayInit(type:Type, initializers:Array) -> NewArrayExpression:
        """
        NewArrayInit(type: Type, *initializers: Array[Expression]) -> NewArrayExpression
        NewArrayInit(type: Type, initializers: IEnumerable[Expression]) -> NewArrayExpression
        """
        ...

    @staticmethod
    def Not(expression:Expression, method:MethodInfo = ...) -> UnaryExpression:
        """
        Not(expression: Expression) -> UnaryExpression
        Not(expression: Expression, method: MethodInfo) -> UnaryExpression
        """
        ...

    @staticmethod
    def NotEqual(left:Expression, right:Expression, liftToNull:bool = ..., method:MethodInfo = ...) -> BinaryExpression:
        """
        NotEqual(left: Expression, right: Expression) -> BinaryExpression
        NotEqual(left: Expression, right: Expression, liftToNull: bool, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def OnesComplement(expression:Expression, method:MethodInfo = ...) -> UnaryExpression:
        """
        OnesComplement(expression: Expression) -> UnaryExpression
        OnesComplement(expression: Expression, method: MethodInfo) -> UnaryExpression
        """
        ...

    @staticmethod
    def Or(left:Expression, right:Expression, method:MethodInfo = ...) -> BinaryExpression:
        """
        Or(left: Expression, right: Expression) -> BinaryExpression
        Or(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def OrAssign(left:Expression, right:Expression, method:MethodInfo = ..., conversion:LambdaExpression = ...) -> BinaryExpression:
        """
        OrAssign(left: Expression, right: Expression) -> BinaryExpression
        OrAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        OrAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression
        """
        ...

    @staticmethod
    def OrElse(left:Expression, right:Expression, method:MethodInfo = ...) -> BinaryExpression:
        """
        OrElse(left: Expression, right: Expression) -> BinaryExpression
        OrElse(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def Parameter(type:Type, name:str = ...) -> ParameterExpression:
        """
        Parameter(type: Type) -> ParameterExpression
        Parameter(type: Type, name: str) -> ParameterExpression
        """
        ...

    @staticmethod
    def PostDecrementAssign(expression:Expression, method:MethodInfo = ...) -> UnaryExpression:
        """
        PostDecrementAssign(expression: Expression) -> UnaryExpression
        PostDecrementAssign(expression: Expression, method: MethodInfo) -> UnaryExpression
        """
        ...

    @staticmethod
    def PostIncrementAssign(expression:Expression, method:MethodInfo = ...) -> UnaryExpression:
        """
        PostIncrementAssign(expression: Expression) -> UnaryExpression
        PostIncrementAssign(expression: Expression, method: MethodInfo) -> UnaryExpression
        """
        ...

    @staticmethod
    def Power(left:Expression, right:Expression, method:MethodInfo = ...) -> BinaryExpression:
        """
        Power(left: Expression, right: Expression) -> BinaryExpression
        Power(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def PowerAssign(left:Expression, right:Expression, method:MethodInfo = ..., conversion:LambdaExpression = ...) -> BinaryExpression:
        """
        PowerAssign(left: Expression, right: Expression) -> BinaryExpression
        PowerAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        PowerAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression
        """
        ...

    @staticmethod
    def PreDecrementAssign(expression:Expression, method:MethodInfo = ...) -> UnaryExpression:
        """
        PreDecrementAssign(expression: Expression) -> UnaryExpression
        PreDecrementAssign(expression: Expression, method: MethodInfo) -> UnaryExpression
        """
        ...

    @staticmethod
    def PreIncrementAssign(expression:Expression, method:MethodInfo = ...) -> UnaryExpression:
        """
        PreIncrementAssign(expression: Expression) -> UnaryExpression
        PreIncrementAssign(expression: Expression, method: MethodInfo) -> UnaryExpression
        """
        ...

    @staticmethod
    def Property(*__args) -> IndexExpression:
        """
        Property(instance: Expression, indexer: PropertyInfo, *arguments: Array[Expression]) -> IndexExpression
        Property(instance: Expression, indexer: PropertyInfo, arguments: IEnumerable[Expression]) -> IndexExpression
        Property(expression: Expression, type: Type, propertyName: str) -> MemberExpression
        Property(expression: Expression, propertyAccessor: MethodInfo) -> MemberExpression
        Property(instance: Expression, propertyName: str, *arguments: Array[Expression]) -> IndexExpression
        Property(expression: Expression, propertyName: str) -> MemberExpression
        Property(expression: Expression, property: PropertyInfo) -> MemberExpression
        """
        ...

    @staticmethod
    def PropertyOrField(expression:Expression, propertyOrFieldName:str) -> MemberExpression:
        """ PropertyOrField(expression: Expression, propertyOrFieldName: str) -> MemberExpression """
        ...

    @staticmethod
    def Quote(expression:Expression) -> UnaryExpression:
        """ Quote(expression: Expression) -> UnaryExpression """
        ...

    def Reduce(self) -> Expression:
        """ Reduce(self: Expression) -> Expression """
        ...

    def ReduceAndCheck(self) -> Expression:
        """ ReduceAndCheck(self: Expression) -> Expression """
        ...

    def ReduceExtensions(self) -> Expression:
        """ ReduceExtensions(self: Expression) -> Expression """
        ...

    @staticmethod
    def ReferenceEqual(left:Expression, right:Expression) -> BinaryExpression:
        """ ReferenceEqual(left: Expression, right: Expression) -> BinaryExpression """
        ...

    @staticmethod
    def ReferenceNotEqual(left:Expression, right:Expression) -> BinaryExpression:
        """ ReferenceNotEqual(left: Expression, right: Expression) -> BinaryExpression """
        ...

    @staticmethod
    def Rethrow(type=None) -> UnaryExpression:
        """
        Rethrow() -> UnaryExpression
        Rethrow(type: Type) -> UnaryExpression
        """
        ...

    @staticmethod
    def Return(target:LabelTarget, *__args:Type) -> GotoExpression:
        """
        Return(target: LabelTarget) -> GotoExpression
        Return(target: LabelTarget, type: Type) -> GotoExpression
        Return(target: LabelTarget, value: Expression) -> GotoExpression
        Return(target: LabelTarget, value: Expression, type: Type) -> GotoExpression
        """
        ...

    @staticmethod
    def RightShift(left:Expression, right:Expression, method:MethodInfo = ...) -> BinaryExpression:
        """
        RightShift(left: Expression, right: Expression) -> BinaryExpression
        RightShift(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def RightShiftAssign(left:Expression, right:Expression, method:MethodInfo = ..., conversion:LambdaExpression = ...) -> BinaryExpression:
        """
        RightShiftAssign(left: Expression, right: Expression) -> BinaryExpression
        RightShiftAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        RightShiftAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression
        """
        ...

    @staticmethod
    def RuntimeVariables(variables:Array) -> RuntimeVariablesExpression:
        """
        RuntimeVariables(*variables: Array[ParameterExpression]) -> RuntimeVariablesExpression
        RuntimeVariables(variables: IEnumerable[ParameterExpression]) -> RuntimeVariablesExpression
        """
        ...

    @staticmethod
    def Subtract(left:Expression, right:Expression, method:MethodInfo = ...) -> BinaryExpression:
        """
        Subtract(left: Expression, right: Expression) -> BinaryExpression
        Subtract(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def SubtractAssign(left:Expression, right:Expression, method:MethodInfo = ..., conversion:LambdaExpression = ...) -> BinaryExpression:
        """
        SubtractAssign(left: Expression, right: Expression) -> BinaryExpression
        SubtractAssign(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        SubtractAssign(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression
        """
        ...

    @staticmethod
    def SubtractAssignChecked(left:Expression, right:Expression, method:MethodInfo = ..., conversion:LambdaExpression = ...) -> BinaryExpression:
        """
        SubtractAssignChecked(left: Expression, right: Expression) -> BinaryExpression
        SubtractAssignChecked(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        SubtractAssignChecked(left: Expression, right: Expression, method: MethodInfo, conversion: LambdaExpression) -> BinaryExpression
        """
        ...

    @staticmethod
    def SubtractChecked(left:Expression, right:Expression, method:MethodInfo = ...) -> BinaryExpression:
        """
        SubtractChecked(left: Expression, right: Expression) -> BinaryExpression
        SubtractChecked(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    @staticmethod
    def Switch(*__args) -> SwitchExpression:
        """
        Switch(switchValue: Expression, *cases: Array[SwitchCase]) -> SwitchExpression
        Switch(switchValue: Expression, defaultBody: Expression, *cases: Array[SwitchCase]) -> SwitchExpression
        Switch(switchValue: Expression, defaultBody: Expression, comparison: MethodInfo, *cases: Array[SwitchCase]) -> SwitchExpression
        Switch(type: Type, switchValue: Expression, defaultBody: Expression, comparison: MethodInfo, *cases: Array[SwitchCase]) -> SwitchExpression
        Switch(switchValue: Expression, defaultBody: Expression, comparison: MethodInfo, cases: IEnumerable[SwitchCase]) -> SwitchExpression
        Switch(type: Type, switchValue: Expression, defaultBody: Expression, comparison: MethodInfo, cases: IEnumerable[SwitchCase]) -> SwitchExpression
        """
        ...

    @staticmethod
    def SwitchCase(body:Expression, testValues:Array) -> SwitchCase:
        """
        SwitchCase(body: Expression, *testValues: Array[Expression]) -> SwitchCase
        SwitchCase(body: Expression, testValues: IEnumerable[Expression]) -> SwitchCase
        """
        ...

    @staticmethod
    def SymbolDocument(fileName:str, language:Guid = ..., languageVendor:Guid = ..., documentType:Guid = ...) -> SymbolDocumentInfo:
        """
        SymbolDocument(fileName: str) -> SymbolDocumentInfo
        SymbolDocument(fileName: str, language: Guid) -> SymbolDocumentInfo
        SymbolDocument(fileName: str, language: Guid, languageVendor: Guid) -> SymbolDocumentInfo
        SymbolDocument(fileName: str, language: Guid, languageVendor: Guid, documentType: Guid) -> SymbolDocumentInfo
        """
        ...

    @staticmethod
    def Throw(value:Expression, type:Type = ...) -> UnaryExpression:
        """
        Throw(value: Expression) -> UnaryExpression
        Throw(value: Expression, type: Type) -> UnaryExpression
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: Expression) -> str """
        ...

    @staticmethod
    def TryCatch(body:Expression, handlers:Array) -> TryExpression:
        """ TryCatch(body: Expression, *handlers: Array[CatchBlock]) -> TryExpression """
        ...

    @staticmethod
    def TryCatchFinally(body:Expression, finally_:Expression, handlers:Array) -> TryExpression:
        """ TryCatchFinally(body: Expression, finally: Expression, *handlers: Array[CatchBlock]) -> TryExpression """
        ...

    @staticmethod
    def TryFault(body:Expression, fault:Expression) -> TryExpression:
        """ TryFault(body: Expression, fault: Expression) -> TryExpression """
        ...

    @staticmethod
    def TryFinally(body:Expression, finally_:Expression) -> TryExpression:
        """ TryFinally(body: Expression, finally: Expression) -> TryExpression """
        ...

    @staticmethod
    def TryGetActionType(typeArgs, actionType) -> Tuple_[bool, Type]:
        """ TryGetActionType(typeArgs: Array[Type]) -> (bool, Type) """
        ...

    @staticmethod
    def TryGetFuncType(typeArgs, funcType) -> Tuple_[bool, Type]:
        """ TryGetFuncType(typeArgs: Array[Type]) -> (bool, Type) """
        ...

    @staticmethod
    def TypeAs(expression:Expression, type:Type) -> UnaryExpression:
        """ TypeAs(expression: Expression, type: Type) -> UnaryExpression """
        ...

    @staticmethod
    def TypeEqual(expression:Expression, type:Type) -> TypeBinaryExpression:
        """ TypeEqual(expression: Expression, type: Type) -> TypeBinaryExpression """
        ...

    @staticmethod
    def TypeIs(expression:Expression, type:Type) -> TypeBinaryExpression:
        """ TypeIs(expression: Expression, type: Type) -> TypeBinaryExpression """
        ...

    @staticmethod
    def UnaryPlus(expression:Expression, method:MethodInfo = ...) -> UnaryExpression:
        """
        UnaryPlus(expression: Expression) -> UnaryExpression
        UnaryPlus(expression: Expression, method: MethodInfo) -> UnaryExpression
        """
        ...

    @staticmethod
    def Unbox(expression:Expression, type:Type) -> UnaryExpression:
        """ Unbox(expression: Expression, type: Type) -> UnaryExpression """
        ...

    @staticmethod
    def Variable(type:Type, name:str = ...) -> ParameterExpression:
        """
        Variable(type: Type) -> ParameterExpression
        Variable(type: Type, name: str) -> ParameterExpression
        """
        ...

    def VisitChildren(self, *args): #cannot find CLR method
        """ VisitChildren(self: Expression, visitor: ExpressionVisitor) -> Expression """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __call__(self, *args): #cannot find CLR method
        """
        Call(method: MethodInfo, arg0: Expression) -> MethodCallExpression
        Call(method: MethodInfo, arg0: Expression, arg1: Expression) -> MethodCallExpression
        Call(method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression) -> MethodCallExpression
        Call(method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression) -> MethodCallExpression
        Call(method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression, arg3: Expression, arg4: Expression) -> MethodCallExpression
        Call(method: MethodInfo, *arguments: Array[Expression]) -> MethodCallExpression
        Call(method: MethodInfo, arguments: IEnumerable[Expression]) -> MethodCallExpression
        Call(instance: Expression, method: MethodInfo) -> MethodCallExpression
        Call(instance: Expression, method: MethodInfo, *arguments: Array[Expression]) -> MethodCallExpression
        Call(instance: Expression, method: MethodInfo, arg0: Expression, arg1: Expression) -> MethodCallExpression
        Call(instance: Expression, method: MethodInfo, arg0: Expression, arg1: Expression, arg2: Expression) -> MethodCallExpression
        Call(instance: Expression, method: MethodInfo, arguments: IEnumerable[Expression]) -> MethodCallExpression
        Call(instance: Expression, methodName: str, typeArguments: Array[Type], *arguments: Array[Expression]) -> MethodCallExpression
        Call(type: Type, methodName: str, typeArguments: Array[Type], *arguments: Array[Expression]) -> MethodCallExpression
        """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        ...

    def __ge__(self, *args): #cannot find CLR method
        ...

    def __gt__(self, *args): #cannot find CLR method
        ...

    def __invert__(self, *args): #cannot find CLR method
        """
        __invert__(expression: Expression) -> UnaryExpression
        __invert__(expression: Expression, method: MethodInfo) -> UnaryExpression
        """
        ...

    def __le__(self, *args): #cannot find CLR method
        ...

    def __lshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x<<yx.__rshift__(y) <==> x<<y """
        ...

    def __lt__(self, *args): #cannot find CLR method
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*yx.__mul__(y) <==> x*y """
        ...

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -xx.__neg__() <==> -x """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type, nodeType: ExpressionType, type: Type)
        __new__(cls: type)
        """
        ...

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """
        __radd__(left: Expression, right: Expression) -> BinaryExpression
        __radd__(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    def __rdiv__(self, *args): #cannot find CLR method
        """
        __rdiv__(left: Expression, right: Expression) -> BinaryExpression
        __rdiv__(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...

    def __rlshift__(self, *args): #cannot find CLR method
        """
        __rlshift__(left: Expression, right: Expression) -> BinaryExpression
        __rlshift__(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """
        __rmul__(left: Expression, right: Expression) -> BinaryExpression
        __rmul__(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    def __rpow__(self, *args): #cannot find CLR method
        """
        __rpow__(left: Expression, right: Expression) -> BinaryExpression
        __rpow__(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    def __rrshift__(self, *args): #cannot find CLR method
        """
        __rrshift__(left: Expression, right: Expression) -> BinaryExpression
        __rrshift__(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>yx.__rshift__(y) <==> x>>y """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """
        __rsub__(left: Expression, right: Expression) -> BinaryExpression
        __rsub__(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    def __rxor__(self, *args): #cannot find CLR method
        """
        __rxor__(left: Expression, right: Expression) -> BinaryExpression
        __rxor__(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """
        __xor__(left: Expression, right: Expression) -> BinaryExpression
        __xor__(left: Expression, right: Expression, method: MethodInfo) -> BinaryExpression
        """
        ...


class ExpressionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
    def Add(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def AddAssign(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def AddAssignChecked(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def AddChecked(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def And(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def AndAlso(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def AndAssign(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def ArrayIndex(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def ArrayLength(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Assign(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Block(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Call(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Coalesce(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Conditional(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Constant(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Convert(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def ConvertChecked(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def DebugInfo(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Decrement(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Default(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Divide(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def DivideAssign(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Dynamic(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Equal(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def ExclusiveOr(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def ExclusiveOrAssign(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Extension(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Goto(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def GreaterThan(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def GreaterThanOrEqual(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Increment(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Index(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Invoke(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def IsFalse(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def IsTrue(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Label(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Lambda(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def LeftShift(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def LeftShiftAssign(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def LessThan(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def LessThanOrEqual(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def ListInit(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Loop(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def MemberAccess(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def MemberInit(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Modulo(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def ModuloAssign(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Multiply(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def MultiplyAssign(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def MultiplyAssignChecked(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def MultiplyChecked(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Negate(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def NegateChecked(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def New(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def NewArrayBounds(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def NewArrayInit(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Not(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def NotEqual(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def OnesComplement(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Or(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def OrAssign(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def OrElse(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Parameter(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def PostDecrementAssign(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def PostIncrementAssign(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Power(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def PowerAssign(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def PreDecrementAssign(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def PreIncrementAssign(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Quote(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def RightShift(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def RightShiftAssign(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def RuntimeVariables(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Subtract(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def SubtractAssign(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def SubtractAssignChecked(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def SubtractChecked(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Switch(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Throw(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Try(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def TypeAs(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def TypeEqual(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def TypeIs(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def UnaryPlus(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def Unbox(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    def __call__(self, *args): #cannot find CLR method
        """ enum ExpressionType, values: Add (0), AddAssign (63), AddAssignChecked (74), AddChecked (1), And (2), AndAlso (3), AndAssign (64), ArrayIndex (5), ArrayLength (4), Assign (46), Block (47), Call (6), Coalesce (7), Conditional (8), Constant (9), Convert (10), ConvertChecked (11), DebugInfo (48), Decrement (49), Default (51), Divide (12), DivideAssign (65), Dynamic (50), Equal (13), ExclusiveOr (14), ExclusiveOrAssign (66), Extension (52), Goto (53), GreaterThan (15), GreaterThanOrEqual (16), Increment (54), Index (55), Invoke (17), IsFalse (84), IsTrue (83), Label (56), Lambda (18), LeftShift (19), LeftShiftAssign (67), LessThan (20), LessThanOrEqual (21), ListInit (22), Loop (58), MemberAccess (23), MemberInit (24), Modulo (25), ModuloAssign (68), Multiply (26), MultiplyAssign (69), MultiplyAssignChecked (75), MultiplyChecked (27), Negate (28), NegateChecked (30), New (31), NewArrayBounds (33), NewArrayInit (32), Not (34), NotEqual (35), OnesComplement (82), Or (36), OrAssign (70), OrElse (37), Parameter (38), PostDecrementAssign (80), PostIncrementAssign (79), Power (39), PowerAssign (71), PreDecrementAssign (78), PreIncrementAssign (77), Quote (40), RightShift (41), RightShiftAssign (72), RuntimeVariables (57), Subtract (42), SubtractAssign (73), SubtractAssignChecked (76), SubtractChecked (43), Switch (59), Throw (60), Try (61), TypeAs (44), TypeEqual (81), TypeIs (45), UnaryPlus (29), Unbox (62) """
        ...

    value__ = ...


class GotoExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Kind(self) -> GotoExpressionKind:
        """ Get: Kind(self: GotoExpression) -> GotoExpressionKind """
        ...

    @property
    def Target(self) -> LabelTarget:
        """ Get: Target(self: GotoExpression) -> LabelTarget """
        ...

    @property
    def Value(self) -> Expression:
        """ Get: Value(self: GotoExpression) -> Expression """
        ...


    def Update(self, target:LabelTarget, value:Expression) -> GotoExpression:
        """ Update(self: GotoExpression, target: LabelTarget, value: Expression) -> GotoExpression """
        ...


class GotoExpressionKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GotoExpressionKind, values: Break (2), Continue (3), Goto (0), Return (1) """
    Break: GotoExpressionKind = ...
    Continue: GotoExpressionKind = ...
    Goto: GotoExpressionKind = ...
    Return: GotoExpressionKind = ...
    value__ = ...


class IndexExpression(Expression, IArgumentProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> ReadOnlyCollection:
        """ Get: Arguments(self: IndexExpression) -> ReadOnlyCollection[Expression] """
        ...

    @property
    def Indexer(self) -> PropertyInfo:
        """ Get: Indexer(self: IndexExpression) -> PropertyInfo """
        ...

    @property
    def Object(self) -> Expression:
        """ Get: Object(self: IndexExpression) -> Expression """
        ...


    def Update(self, object:Expression, arguments:IEnumerable) -> IndexExpression:
        """ Update(self: IndexExpression, object: Expression, arguments: IEnumerable[Expression]) -> IndexExpression """
        ...


class InvocationExpression(Expression, IArgumentProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> ReadOnlyCollection:
        """ Get: Arguments(self: InvocationExpression) -> ReadOnlyCollection[Expression] """
        ...

    @property
    def Expression(self) -> Expression:
        """ Get: Expression(self: InvocationExpression) -> Expression """
        ...


    def Update(self, expression:Expression, arguments:IEnumerable) -> InvocationExpression:
        """ Update(self: InvocationExpression, expression: Expression, arguments: IEnumerable[Expression]) -> InvocationExpression """
        ...


class LabelExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DefaultValue(self) -> Expression:
        """ Get: DefaultValue(self: LabelExpression) -> Expression """
        ...

    @property
    def Target(self) -> LabelTarget:
        """ Get: Target(self: LabelExpression) -> LabelTarget """
        ...


    def Update(self, target:LabelTarget, defaultValue:Expression) -> LabelExpression:
        """ Update(self: LabelExpression, target: LabelTarget, defaultValue: Expression) -> LabelExpression """
        ...


class LabelTarget: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: LabelTarget) -> str """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: LabelTarget) -> Type """
        ...


    def ToString(self) -> str:
        """ ToString(self: LabelTarget) -> str """
        ...


class LambdaExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Body(self) -> Expression:
        """ Get: Body(self: LambdaExpression) -> Expression """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: LambdaExpression) -> str """
        ...

    @property
    def Parameters(self) -> ReadOnlyCollection:
        """ Get: Parameters(self: LambdaExpression) -> ReadOnlyCollection[ParameterExpression] """
        ...

    @property
    def ReturnType(self) -> Type:
        """ Get: ReturnType(self: LambdaExpression) -> Type """
        ...

    @property
    def TailCall(self) -> bool:
        """ Get: TailCall(self: LambdaExpression) -> bool """
        ...


    def Compile(self, *__args:DebugInfoGenerator) -> Delegate:
        """
        Compile(self: LambdaExpression) -> Delegate
        Compile(self: LambdaExpression, debugInfoGenerator: DebugInfoGenerator) -> Delegate
        Compile(self: LambdaExpression, preferInterpretation: bool) -> Delegate
        """
        ...

    def CompileToMethod(self, method:MethodBuilder, debugInfoGenerator:DebugInfoGenerator = ...): # -> 
        """ CompileToMethod(self: LambdaExpression, method: MethodBuilder)CompileToMethod(self: LambdaExpression, method: MethodBuilder, debugInfoGenerator: DebugInfoGenerator) """
        ...


class ListInitExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Initializers(self) -> ReadOnlyCollection:
        """ Get: Initializers(self: ListInitExpression) -> ReadOnlyCollection[ElementInit] """
        ...

    @property
    def NewExpression(self) -> NewExpression:
        """ Get: NewExpression(self: ListInitExpression) -> NewExpression """
        ...


    def Update(self, newExpression:NewExpression, initializers:IEnumerable) -> ListInitExpression:
        """ Update(self: ListInitExpression, newExpression: NewExpression, initializers: IEnumerable[ElementInit]) -> ListInitExpression """
        ...


class LoopExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Body(self) -> Expression:
        """ Get: Body(self: LoopExpression) -> Expression """
        ...

    @property
    def BreakLabel(self) -> LabelTarget:
        """ Get: BreakLabel(self: LoopExpression) -> LabelTarget """
        ...

    @property
    def ContinueLabel(self) -> LabelTarget:
        """ Get: ContinueLabel(self: LoopExpression) -> LabelTarget """
        ...


    def Update(self, breakLabel:LabelTarget, continueLabel:LabelTarget, body:Expression) -> LoopExpression:
        """ Update(self: LoopExpression, breakLabel: LabelTarget, continueLabel: LabelTarget, body: Expression) -> LoopExpression """
        ...


class MemberBinding: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BindingType(self) -> MemberBindingType:
        """ Get: BindingType(self: MemberBinding) -> MemberBindingType """
        ...

    @property
    def Member(self) -> MemberInfo:
        """ Get: Member(self: MemberBinding) -> MemberInfo """
        ...


    def ToString(self) -> str:
        """ ToString(self: MemberBinding) -> str """
        ...


class MemberAssignment(MemberBinding): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Expression(self) -> Expression:
        """ Get: Expression(self: MemberAssignment) -> Expression """
        ...


    def Update(self, expression:Expression) -> MemberAssignment:
        """ Update(self: MemberAssignment, expression: Expression) -> MemberAssignment """
        ...


class MemberBindingType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MemberBindingType, values: Assignment (0), ListBinding (2), MemberBinding (1) """
    Assignment: MemberBindingType = ...
    ListBinding: MemberBindingType = ...
    MemberBinding: MemberBindingType = ...
    value__ = ...


class MemberExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Expression(self) -> Expression:
        """ Get: Expression(self: MemberExpression) -> Expression """
        ...

    @property
    def Member(self) -> MemberInfo:
        """ Get: Member(self: MemberExpression) -> MemberInfo """
        ...


    def Update(self, expression:Expression) -> MemberExpression:
        """ Update(self: MemberExpression, expression: Expression) -> MemberExpression """
        ...


class MemberInitExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Bindings(self) -> ReadOnlyCollection:
        """ Get: Bindings(self: MemberInitExpression) -> ReadOnlyCollection[MemberBinding] """
        ...

    @property
    def NewExpression(self) -> NewExpression:
        """ Get: NewExpression(self: MemberInitExpression) -> NewExpression """
        ...


    def Update(self, newExpression:NewExpression, bindings:IEnumerable) -> MemberInitExpression:
        """ Update(self: MemberInitExpression, newExpression: NewExpression, bindings: IEnumerable[MemberBinding]) -> MemberInitExpression """
        ...


class MemberListBinding(MemberBinding): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Initializers(self) -> ReadOnlyCollection:
        """ Get: Initializers(self: MemberListBinding) -> ReadOnlyCollection[ElementInit] """
        ...


    def Update(self, initializers:IEnumerable) -> MemberListBinding:
        """ Update(self: MemberListBinding, initializers: IEnumerable[ElementInit]) -> MemberListBinding """
        ...


class MemberMemberBinding(MemberBinding): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Bindings(self) -> ReadOnlyCollection:
        """ Get: Bindings(self: MemberMemberBinding) -> ReadOnlyCollection[MemberBinding] """
        ...


    def Update(self, bindings:IEnumerable) -> MemberMemberBinding:
        """ Update(self: MemberMemberBinding, bindings: IEnumerable[MemberBinding]) -> MemberMemberBinding """
        ...


class MethodCallExpression(Expression, IArgumentProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> ReadOnlyCollection:
        """ Get: Arguments(self: MethodCallExpression) -> ReadOnlyCollection[Expression] """
        ...

    @property
    def Method(self) -> MethodInfo:
        """ Get: Method(self: MethodCallExpression) -> MethodInfo """
        ...

    @property
    def Object(self) -> Expression:
        """ Get: Object(self: MethodCallExpression) -> Expression """
        ...


    def Update(self, object:Expression, arguments:IEnumerable) -> MethodCallExpression:
        """ Update(self: MethodCallExpression, object: Expression, arguments: IEnumerable[Expression]) -> MethodCallExpression """
        ...


class NewArrayExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Expressions(self) -> ReadOnlyCollection:
        """ Get: Expressions(self: NewArrayExpression) -> ReadOnlyCollection[Expression] """
        ...


    def Update(self, expressions:IEnumerable) -> NewArrayExpression:
        """ Update(self: NewArrayExpression, expressions: IEnumerable[Expression]) -> NewArrayExpression """
        ...


class NewExpression(Expression, IArgumentProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Arguments(self) -> ReadOnlyCollection:
        """ Get: Arguments(self: NewExpression) -> ReadOnlyCollection[Expression] """
        ...

    @property
    def Constructor(self) -> ConstructorInfo:
        """ Get: Constructor(self: NewExpression) -> ConstructorInfo """
        ...

    @property
    def Members(self) -> ReadOnlyCollection:
        """ Get: Members(self: NewExpression) -> ReadOnlyCollection[MemberInfo] """
        ...


    def Update(self, arguments:IEnumerable) -> NewExpression:
        """ Update(self: NewExpression, arguments: IEnumerable[Expression]) -> NewExpression """
        ...


class ParameterExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsByRef(self) -> bool:
        """ Get: IsByRef(self: ParameterExpression) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ParameterExpression) -> str """
        ...



class RuntimeVariablesExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Variables(self) -> ReadOnlyCollection:
        """ Get: Variables(self: RuntimeVariablesExpression) -> ReadOnlyCollection[ParameterExpression] """
        ...


    def Update(self, variables:IEnumerable) -> RuntimeVariablesExpression:
        """ Update(self: RuntimeVariablesExpression, variables: IEnumerable[ParameterExpression]) -> RuntimeVariablesExpression """
        ...


class SwitchCase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Body(self) -> Expression:
        """ Get: Body(self: SwitchCase) -> Expression """
        ...

    @property
    def TestValues(self) -> ReadOnlyCollection:
        """ Get: TestValues(self: SwitchCase) -> ReadOnlyCollection[Expression] """
        ...


    def ToString(self) -> str:
        """ ToString(self: SwitchCase) -> str """
        ...

    def Update(self, testValues:IEnumerable, body:Expression) -> SwitchCase:
        """ Update(self: SwitchCase, testValues: IEnumerable[Expression], body: Expression) -> SwitchCase """
        ...


class SwitchExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Cases(self) -> ReadOnlyCollection:
        """ Get: Cases(self: SwitchExpression) -> ReadOnlyCollection[SwitchCase] """
        ...

    @property
    def Comparison(self) -> MethodInfo:
        """ Get: Comparison(self: SwitchExpression) -> MethodInfo """
        ...

    @property
    def DefaultBody(self) -> Expression:
        """ Get: DefaultBody(self: SwitchExpression) -> Expression """
        ...

    @property
    def SwitchValue(self) -> Expression:
        """ Get: SwitchValue(self: SwitchExpression) -> Expression """
        ...


    def Update(self, switchValue:Expression, cases:IEnumerable, defaultBody:Expression) -> SwitchExpression:
        """ Update(self: SwitchExpression, switchValue: Expression, cases: IEnumerable[SwitchCase], defaultBody: Expression) -> SwitchExpression """
        ...


class SymbolDocumentInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DocumentType(self) -> Guid:
        """ Get: DocumentType(self: SymbolDocumentInfo) -> Guid """
        ...

    @property
    def FileName(self) -> str:
        """ Get: FileName(self: SymbolDocumentInfo) -> str """
        ...

    @property
    def Language(self) -> Guid:
        """ Get: Language(self: SymbolDocumentInfo) -> Guid """
        ...

    @property
    def LanguageVendor(self) -> Guid:
        """ Get: LanguageVendor(self: SymbolDocumentInfo) -> Guid """
        ...



class TryExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Body(self) -> Expression:
        """ Get: Body(self: TryExpression) -> Expression """
        ...

    @property
    def Fault(self) -> Expression:
        """ Get: Fault(self: TryExpression) -> Expression """
        ...

    @property
    def Finally(self) -> Expression:
        """ Get: Finally(self: TryExpression) -> Expression """
        ...

    @property
    def Handlers(self) -> ReadOnlyCollection:
        """ Get: Handlers(self: TryExpression) -> ReadOnlyCollection[CatchBlock] """
        ...


    def Update(self, body:Expression, handlers:IEnumerable, finally_:Expression, fault:Expression) -> TryExpression:
        """ Update(self: TryExpression, body: Expression, handlers: IEnumerable[CatchBlock], finally: Expression, fault: Expression) -> TryExpression """
        ...


class TypeBinaryExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Expression(self) -> Expression:
        """ Get: Expression(self: TypeBinaryExpression) -> Expression """
        ...

    @property
    def TypeOperand(self) -> Type:
        """ Get: TypeOperand(self: TypeBinaryExpression) -> Type """
        ...


    def Update(self, expression:Expression) -> TypeBinaryExpression:
        """ Update(self: TypeBinaryExpression, expression: Expression) -> TypeBinaryExpression """
        ...


class UnaryExpression(Expression): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsLifted(self) -> bool:
        """ Get: IsLifted(self: UnaryExpression) -> bool """
        ...

    @property
    def IsLiftedToNull(self) -> bool:
        """ Get: IsLiftedToNull(self: UnaryExpression) -> bool """
        ...

    @property
    def Method(self) -> MethodInfo:
        """ Get: Method(self: UnaryExpression) -> MethodInfo """
        ...

    @property
    def Operand(self) -> Expression:
        """ Get: Operand(self: UnaryExpression) -> Expression """
        ...


    def Update(self, operand:Expression) -> UnaryExpression:
        """ Update(self: UnaryExpression, operand: Expression) -> UnaryExpression """
        ...


