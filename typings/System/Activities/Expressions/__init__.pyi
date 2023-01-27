# encoding: utf-8
# module System.Activities.Expressions calls itself Expressions
# from System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import Type

from System.Activities import (ActivityContext, AsyncCodeActivity, 
    CodeActivity, DelegateArgument, InArgument, InOutArgument, 
    LocationReference, Variable)

from System.Activities.XamlIntegration import (ICompiledExpressionRoot, 
    IValueSerializableExpression)

from System.Collections import IList

from System.EnterpriseServices import Activity

from System.Linq.Expressions import Expression

from System.Reflection import Assembly, AssemblyName

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    IExpressionContainer, ILocationReferenceExpression, T)
"""

# no functions
# classes

class Add(CodeActivity): # skipped bases: <type 'object'>
    """ Add[TLeft, TRight, TResult]() """
    @property
    def Checked(self) -> bool:
        """
        Get: Checked(self: Add[TLeft, TRight, TResult]) -> bool
        Set: Checked(self: Add[TLeft, TRight, TResult]) = value
        """
        ...

    @property
    def Left(self) -> InArgument:
        """
        Get: Left(self: Add[TLeft, TRight, TResult]) -> InArgument[TLeft]
        Set: Left(self: Add[TLeft, TRight, TResult]) = value
        """
        ...

    @property
    def Right(self) -> InArgument:
        """
        Get: Right(self: Add[TLeft, TRight, TResult]) -> InArgument[TRight]
        Set: Right(self: Add[TLeft, TRight, TResult]) = value
        """
        ...



class And(CodeActivity): # skipped bases: <type 'object'>
    """ And[TLeft, TRight, TResult]() """
    @property
    def Left(self) -> InArgument:
        """
        Get: Left(self: And[TLeft, TRight, TResult]) -> InArgument[TLeft]
        Set: Left(self: And[TLeft, TRight, TResult]) = value
        """
        ...

    @property
    def Right(self) -> InArgument:
        """
        Get: Right(self: And[TLeft, TRight, TResult]) -> InArgument[TRight]
        Set: Right(self: And[TLeft, TRight, TResult]) = value
        """
        ...



class AndAlso(Activity): # skipped bases: <type 'object'>
    """ AndAlso() """
    @property
    def Left(self) -> Activity:
        """
        Get: Left(self: AndAlso) -> Activity[bool]
        Set: Left(self: AndAlso) = value
        """
        ...

    @property
    def Right(self) -> Activity:
        """
        Get: Right(self: AndAlso) -> Activity[bool]
        Set: Right(self: AndAlso) = value
        """
        ...



class ArgumentReference(EnvironmentLocationReference): # skipped bases: <type 'IExpressionContainer'>, <type 'ILocationReferenceExpression'>, <type 'object'>
    """
    ArgumentReference[T]()
    ArgumentReference[T](argumentName: str)
    """
    @property
    def ArgumentName(self) -> str:
        """
        Get: ArgumentName(self: ArgumentReference[T]) -> str
        Set: ArgumentName(self: ArgumentReference[T]) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: ArgumentReference[T]) -> str """
        ...

    def __new__(cls, argumentName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, argumentName: str)
        """
        ...


class ArgumentValue(EnvironmentLocationValue): # skipped bases: <type 'IExpressionContainer'>, <type 'ILocationReferenceExpression'>, <type 'object'>
    """
    ArgumentValue[T]()
    ArgumentValue[T](argumentName: str)
    """
    @property
    def ArgumentName(self) -> str:
        """
        Get: ArgumentName(self: ArgumentValue[T]) -> str
        Set: ArgumentName(self: ArgumentValue[T]) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: ArgumentValue[T]) -> str """
        ...

    def __new__(cls, argumentName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, argumentName: str)
        """
        ...


class ArrayItemReference(CodeActivity): # skipped bases: <type 'object'>
    """ ArrayItemReference[TItem]() """
    @property
    def Array(self) -> InArgument:
        """
        Get: Array(self: ArrayItemReference[TItem]) -> InArgument[Array[TItem]]
        Set: Array(self: ArrayItemReference[TItem]) = value
        """
        ...

    @property
    def Index(self) -> InArgument:
        """
        Get: Index(self: ArrayItemReference[TItem]) -> InArgument[int]
        Set: Index(self: ArrayItemReference[TItem]) = value
        """
        ...



class ArrayItemValue(CodeActivity): # skipped bases: <type 'object'>
    """ ArrayItemValue[TItem]() """
    @property
    def Array(self) -> InArgument:
        """
        Get: Array(self: ArrayItemValue[TItem]) -> InArgument[Array[TItem]]
        Set: Array(self: ArrayItemValue[TItem]) = value
        """
        ...

    @property
    def Index(self) -> InArgument:
        """
        Get: Index(self: ArrayItemValue[TItem]) -> InArgument[int]
        Set: Index(self: ArrayItemValue[TItem]) = value
        """
        ...



class As(CodeActivity): # skipped bases: <type 'object'>
    """ As[TOperand, TResult]() """
    @property
    def Operand(self) -> InArgument:
        """
        Get: Operand(self: As[TOperand, TResult]) -> InArgument[TOperand]
        Set: Operand(self: As[TOperand, TResult]) = value
        """
        ...



class AssemblyReference: # skipped bases: <type 'object'>, <type 'object'>
    """ AssemblyReference() """
    @property
    def Assembly(self) -> Assembly:
        """
        Get: Assembly(self: AssemblyReference) -> Assembly
        Set: Assembly(self: AssemblyReference) = value
        """
        ...

    @property
    def AssemblyName(self) -> AssemblyName:
        """
        Get: AssemblyName(self: AssemblyReference) -> AssemblyName
        Set: AssemblyName(self: AssemblyReference) = value
        """
        ...


    def LoadAssembly(self): # -> 
        """ LoadAssembly(self: AssemblyReference) """
        ...


class Cast(CodeActivity): # skipped bases: <type 'object'>
    """ Cast[TOperand, TResult]() """
    @property
    def Checked(self) -> bool:
        """
        Get: Checked(self: Cast[TOperand, TResult]) -> bool
        Set: Checked(self: Cast[TOperand, TResult]) = value
        """
        ...

    @property
    def Operand(self) -> InArgument:
        """
        Get: Operand(self: Cast[TOperand, TResult]) -> InArgument[TOperand]
        Set: Operand(self: Cast[TOperand, TResult]) = value
        """
        ...



class CompiledExpressionInvoker: # skipped bases: <type 'object'>, <type 'object'>
    """ CompiledExpressionInvoker(expression: ITextExpression, isReference: bool, metadata: CodeActivityMetadata) """
    @property
    def IsStaticallyCompiled(self) -> bool:
        """ Get: IsStaticallyCompiled(self: CompiledExpressionInvoker) -> bool """
        ...


    @staticmethod
    def GetCompiledExpressionRoot(target:object) -> object:
        """ GetCompiledExpressionRoot(target: object) -> object """
        ...

    @staticmethod
    def GetCompiledExpressionRootForImplementation(target:object) -> object:
        """ GetCompiledExpressionRootForImplementation(target: object) -> object """
        ...

    def InvokeExpression(self, activityContext:ActivityContext) -> object:
        """ InvokeExpression(self: CompiledExpressionInvoker, activityContext: ActivityContext) -> object """
        ...

    @staticmethod
    def SetCompiledExpressionRoot(target:object, compiledExpressionRoot:ICompiledExpressionRoot): # -> 
        """ SetCompiledExpressionRoot(target: object, compiledExpressionRoot: ICompiledExpressionRoot) """
        ...

    @staticmethod
    def SetCompiledExpressionRootForImplementation(target:object, compiledExpressionRoot:ICompiledExpressionRoot): # -> 
        """ SetCompiledExpressionRootForImplementation(target: object, compiledExpressionRoot: ICompiledExpressionRoot) """
        ...


class DelegateArgumentReference(EnvironmentLocationReference): # skipped bases: <type 'IExpressionContainer'>, <type 'ILocationReferenceExpression'>, <type 'object'>
    """
    DelegateArgumentReference[T]()
    DelegateArgumentReference[T](delegateArgument: DelegateArgument)
    """
    @property
    def DelegateArgument(self) -> DelegateArgument:
        """
        Get: DelegateArgument(self: DelegateArgumentReference[T]) -> DelegateArgument
        Set: DelegateArgument(self: DelegateArgumentReference[T]) = value
        """
        ...


    def __new__(cls, delegateArgument:DelegateArgument = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, delegateArgument: DelegateArgument)
        """
        ...


class DelegateArgumentValue(EnvironmentLocationValue): # skipped bases: <type 'IExpressionContainer'>, <type 'ILocationReferenceExpression'>, <type 'object'>
    """
    DelegateArgumentValue[T]()
    DelegateArgumentValue[T](delegateArgument: DelegateArgument)
    """
    @property
    def DelegateArgument(self) -> DelegateArgument:
        """
        Get: DelegateArgument(self: DelegateArgumentValue[T]) -> DelegateArgument
        Set: DelegateArgument(self: DelegateArgumentValue[T]) = value
        """
        ...


    def __new__(cls, delegateArgument:DelegateArgument = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, delegateArgument: DelegateArgument)
        """
        ...


class Divide(CodeActivity): # skipped bases: <type 'object'>
    """ Divide[TLeft, TRight, TResult]() """
    @property
    def Left(self) -> InArgument:
        """
        Get: Left(self: Divide[TLeft, TRight, TResult]) -> InArgument[TLeft]
        Set: Left(self: Divide[TLeft, TRight, TResult]) = value
        """
        ...

    @property
    def Right(self) -> InArgument:
        """
        Get: Right(self: Divide[TLeft, TRight, TResult]) -> InArgument[TRight]
        Set: Right(self: Divide[TLeft, TRight, TResult]) = value
        """
        ...



class EnvironmentLocationReference(ILocationReferenceExpression, IExpressionContainer, CodeActivity): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LocationReference(self) -> LocationReference:
        """ Get: LocationReference(self: EnvironmentLocationReference[T]) -> LocationReference """
        ...



class EnvironmentLocationValue(ILocationReferenceExpression, IExpressionContainer, CodeActivity): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LocationReference(self) -> LocationReference:
        """ Get: LocationReference(self: EnvironmentLocationValue[T]) -> LocationReference """
        ...



class Equal(CodeActivity): # skipped bases: <type 'object'>
    """ Equal[TLeft, TRight, TResult]() """
    @property
    def Left(self) -> InArgument:
        """
        Get: Left(self: Equal[TLeft, TRight, TResult]) -> InArgument[TLeft]
        Set: Left(self: Equal[TLeft, TRight, TResult]) = value
        """
        ...

    @property
    def Right(self) -> InArgument:
        """
        Get: Right(self: Equal[TLeft, TRight, TResult]) -> InArgument[TRight]
        Set: Right(self: Equal[TLeft, TRight, TResult]) = value
        """
        ...



class ExpressionServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Convert(expression:Expression) -> Activity:
        """ Convert[TResult](expression: Expression[Func[ActivityContext, TResult]]) -> Activity[TResult] """
        ...

    @staticmethod
    def ConvertReference(expression:Expression) -> Activity:
        """ ConvertReference[TResult](expression: Expression[Func[ActivityContext, TResult]]) -> Activity[Location[TResult]] """
        ...

    @staticmethod
    def TryConvert(expression, result) -> Tuple_[bool, Activity]:
        """ TryConvert[TResult](expression: Expression[Func[ActivityContext, TResult]]) -> (bool, Activity[TResult]) """
        ...

    @staticmethod
    def TryConvertReference(expression, result) -> Tuple_[bool, Activity]:
        """ TryConvertReference[TResult](expression: Expression[Func[ActivityContext, TResult]]) -> (bool, Activity[Location[TResult]]) """
        ...

    __all__: list = ...


class FieldReference(CodeActivity): # skipped bases: <type 'object'>
    """ FieldReference[TOperand, TResult]() """
    @property
    def FieldName(self) -> str:
        """
        Get: FieldName(self: FieldReference[TOperand, TResult]) -> str
        Set: FieldName(self: FieldReference[TOperand, TResult]) = value
        """
        ...

    @property
    def Operand(self) -> InArgument:
        """
        Get: Operand(self: FieldReference[TOperand, TResult]) -> InArgument[TOperand]
        Set: Operand(self: FieldReference[TOperand, TResult]) = value
        """
        ...



class FieldValue(CodeActivity): # skipped bases: <type 'object'>
    """ FieldValue[TOperand, TResult]() """
    @property
    def FieldName(self) -> str:
        """
        Get: FieldName(self: FieldValue[TOperand, TResult]) -> str
        Set: FieldName(self: FieldValue[TOperand, TResult]) = value
        """
        ...

    @property
    def Operand(self) -> InArgument:
        """
        Get: Operand(self: FieldValue[TOperand, TResult]) -> InArgument[TOperand]
        Set: Operand(self: FieldValue[TOperand, TResult]) = value
        """
        ...



class GreaterThan(CodeActivity): # skipped bases: <type 'object'>
    """ GreaterThan[TLeft, TRight, TResult]() """
    @property
    def Left(self) -> InArgument:
        """
        Get: Left(self: GreaterThan[TLeft, TRight, TResult]) -> InArgument[TLeft]
        Set: Left(self: GreaterThan[TLeft, TRight, TResult]) = value
        """
        ...

    @property
    def Right(self) -> InArgument:
        """
        Get: Right(self: GreaterThan[TLeft, TRight, TResult]) -> InArgument[TRight]
        Set: Right(self: GreaterThan[TLeft, TRight, TResult]) = value
        """
        ...



class GreaterThanOrEqual(CodeActivity): # skipped bases: <type 'object'>
    """ GreaterThanOrEqual[TLeft, TRight, TResult]() """
    @property
    def Left(self) -> InArgument:
        """
        Get: Left(self: GreaterThanOrEqual[TLeft, TRight, TResult]) -> InArgument[TLeft]
        Set: Left(self: GreaterThanOrEqual[TLeft, TRight, TResult]) = value
        """
        ...

    @property
    def Right(self) -> InArgument:
        """
        Get: Right(self: GreaterThanOrEqual[TLeft, TRight, TResult]) -> InArgument[TRight]
        Set: Right(self: GreaterThanOrEqual[TLeft, TRight, TResult]) = value
        """
        ...



class IndexerReference(CodeActivity): # skipped bases: <type 'object'>
    """ IndexerReference[TOperand, TItem]() """
    @property
    def Indices(self) -> Collection:
        """ Get: Indices(self: IndexerReference[TOperand, TItem]) -> Collection[InArgument] """
        ...

    @property
    def Operand(self) -> InArgument:
        """
        Get: Operand(self: IndexerReference[TOperand, TItem]) -> InArgument[TOperand]
        Set: Operand(self: IndexerReference[TOperand, TItem]) = value
        """
        ...



class InvokeMethod(AsyncCodeActivity): # skipped bases: <type 'IAsyncCodeActivity'>, <type 'object'>
    """ InvokeMethod[TResult]() """
    @property
    def GenericTypeArguments(self) -> Collection:
        """ Get: GenericTypeArguments(self: InvokeMethod[TResult]) -> Collection[Type] """
        ...

    @property
    def MethodName(self) -> str:
        """
        Get: MethodName(self: InvokeMethod[TResult]) -> str
        Set: MethodName(self: InvokeMethod[TResult]) = value
        """
        ...

    @property
    def Parameters(self) -> Collection:
        """ Get: Parameters(self: InvokeMethod[TResult]) -> Collection[Argument] """
        ...

    @property
    def RunAsynchronously(self) -> bool:
        """
        Get: RunAsynchronously(self: InvokeMethod[TResult]) -> bool
        Set: RunAsynchronously(self: InvokeMethod[TResult]) = value
        """
        ...

    @property
    def TargetObject(self) -> InArgument:
        """
        Get: TargetObject(self: InvokeMethod[TResult]) -> InArgument
        Set: TargetObject(self: InvokeMethod[TResult]) = value
        """
        ...

    @property
    def TargetType(self) -> Type:
        """
        Get: TargetType(self: InvokeMethod[TResult]) -> Type
        Set: TargetType(self: InvokeMethod[TResult]) = value
        """
        ...



class ITextExpression: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ExpressionText(self) -> str:
        """ Get: ExpressionText(self: ITextExpression) -> str """
        ...

    @property
    def Language(self) -> str:
        """ Get: Language(self: ITextExpression) -> str """
        ...

    @property
    def RequiresCompilation(self) -> bool:
        """ Get: RequiresCompilation(self: ITextExpression) -> bool """
        ...


    def GetExpressionTree(self) -> Expression:
        """ GetExpressionTree(self: ITextExpression) -> Expression """
        ...


class LambdaReference(IExpressionContainer, IValueSerializableExpression, CodeActivity): # skipped bases: <type 'object'>
    """ LambdaReference[T](locationExpression: Expression[Func[ActivityContext, T]]) """
    def __new__(cls, locationExpression:Expression) -> Self:
        """ __new__(cls: type, locationExpression: Expression[Func[ActivityContext, T]]) """
        ...


class LambdaSerializationException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    LambdaSerializationException()
    LambdaSerializationException(message: str)
    LambdaSerializationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class LambdaValue(IExpressionContainer, IValueSerializableExpression, CodeActivity): # skipped bases: <type 'object'>
    """ LambdaValue[TResult](lambdaValue: Expression[Func[ActivityContext, TResult]]) """
    def __new__(cls, lambdaValue:Expression) -> Self:
        """ __new__(cls: type, lambdaValue: Expression[Func[ActivityContext, TResult]]) """
        ...


class LessThan(CodeActivity): # skipped bases: <type 'object'>
    """ LessThan[TLeft, TRight, TResult]() """
    @property
    def Left(self) -> InArgument:
        """
        Get: Left(self: LessThan[TLeft, TRight, TResult]) -> InArgument[TLeft]
        Set: Left(self: LessThan[TLeft, TRight, TResult]) = value
        """
        ...

    @property
    def Right(self) -> InArgument:
        """
        Get: Right(self: LessThan[TLeft, TRight, TResult]) -> InArgument[TRight]
        Set: Right(self: LessThan[TLeft, TRight, TResult]) = value
        """
        ...



class LessThanOrEqual(CodeActivity): # skipped bases: <type 'object'>
    """ LessThanOrEqual[TLeft, TRight, TResult]() """
    @property
    def Left(self) -> InArgument:
        """
        Get: Left(self: LessThanOrEqual[TLeft, TRight, TResult]) -> InArgument[TLeft]
        Set: Left(self: LessThanOrEqual[TLeft, TRight, TResult]) = value
        """
        ...

    @property
    def Right(self) -> InArgument:
        """
        Get: Right(self: LessThanOrEqual[TLeft, TRight, TResult]) -> InArgument[TRight]
        Set: Right(self: LessThanOrEqual[TLeft, TRight, TResult]) = value
        """
        ...



class Literal(IExpressionContainer, IValueSerializableExpression, CodeActivity): # skipped bases: <type 'object'>
    """
    Literal[T]()
    Literal[T](value: T)
    """
    @property
    def Value(self): # -> T
        """
        Get: Value(self: Literal[T]) -> T
        Set: Value(self: Literal[T]) = value
        """
        ...


    def ShouldSerializeValue(self) -> bool:
        """ ShouldSerializeValue(self: Literal[T]) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: Literal[T]) -> str """
        ...

    def __new__(cls, value = ...) -> Self: # Not found arg types: {'value': 'T'}
        """
        __new__(cls: type)
        __new__(cls: type, value: T)
        """
        ...


class MultidimensionalArrayItemReference(CodeActivity): # skipped bases: <type 'object'>
    """ MultidimensionalArrayItemReference[TItem]() """
    @property
    def Array(self) -> InArgument:
        """
        Get: Array(self: MultidimensionalArrayItemReference[TItem]) -> InArgument[Array]
        Set: Array(self: MultidimensionalArrayItemReference[TItem]) = value
        """
        ...

    @property
    def Indices(self) -> Collection:
        """ Get: Indices(self: MultidimensionalArrayItemReference[TItem]) -> Collection[InArgument[int]] """
        ...



class Multiply(CodeActivity): # skipped bases: <type 'object'>
    """ Multiply[TLeft, TRight, TResult]() """
    @property
    def Checked(self) -> bool:
        """
        Get: Checked(self: Multiply[TLeft, TRight, TResult]) -> bool
        Set: Checked(self: Multiply[TLeft, TRight, TResult]) = value
        """
        ...

    @property
    def Left(self) -> InArgument:
        """
        Get: Left(self: Multiply[TLeft, TRight, TResult]) -> InArgument[TLeft]
        Set: Left(self: Multiply[TLeft, TRight, TResult]) = value
        """
        ...

    @property
    def Right(self) -> InArgument:
        """
        Get: Right(self: Multiply[TLeft, TRight, TResult]) -> InArgument[TRight]
        Set: Right(self: Multiply[TLeft, TRight, TResult]) = value
        """
        ...



class New(CodeActivity): # skipped bases: <type 'object'>
    """ New[TResult]() """
    @property
    def Arguments(self) -> Collection:
        """ Get: Arguments(self: New[TResult]) -> Collection[Argument] """
        ...



class NewArray(CodeActivity): # skipped bases: <type 'object'>
    """ NewArray[TResult]() """
    @property
    def Bounds(self) -> Collection:
        """ Get: Bounds(self: NewArray[TResult]) -> Collection[Argument] """
        ...



class Not(CodeActivity): # skipped bases: <type 'object'>
    """ Not[TOperand, TResult]() """
    @property
    def Operand(self) -> InArgument:
        """
        Get: Operand(self: Not[TOperand, TResult]) -> InArgument[TOperand]
        Set: Operand(self: Not[TOperand, TResult]) = value
        """
        ...



class NotEqual(CodeActivity): # skipped bases: <type 'object'>
    """ NotEqual[TLeft, TRight, TResult]() """
    @property
    def Left(self) -> InArgument:
        """
        Get: Left(self: NotEqual[TLeft, TRight, TResult]) -> InArgument[TLeft]
        Set: Left(self: NotEqual[TLeft, TRight, TResult]) = value
        """
        ...

    @property
    def Right(self) -> InArgument:
        """
        Get: Right(self: NotEqual[TLeft, TRight, TResult]) -> InArgument[TRight]
        Set: Right(self: NotEqual[TLeft, TRight, TResult]) = value
        """
        ...



class Or(CodeActivity): # skipped bases: <type 'object'>
    """ Or[TLeft, TRight, TResult]() """
    @property
    def Left(self) -> InArgument:
        """
        Get: Left(self: Or[TLeft, TRight, TResult]) -> InArgument[TLeft]
        Set: Left(self: Or[TLeft, TRight, TResult]) = value
        """
        ...

    @property
    def Right(self) -> InArgument:
        """
        Get: Right(self: Or[TLeft, TRight, TResult]) -> InArgument[TRight]
        Set: Right(self: Or[TLeft, TRight, TResult]) = value
        """
        ...



class OrElse(Activity): # skipped bases: <type 'object'>
    """ OrElse() """
    @property
    def Left(self) -> Activity:
        """
        Get: Left(self: OrElse) -> Activity[bool]
        Set: Left(self: OrElse) = value
        """
        ...

    @property
    def Right(self) -> Activity:
        """
        Get: Right(self: OrElse) -> Activity[bool]
        Set: Right(self: OrElse) = value
        """
        ...



class PropertyReference(CodeActivity): # skipped bases: <type 'object'>
    """ PropertyReference[TOperand, TResult]() """
    @property
    def Operand(self) -> InArgument:
        """
        Get: Operand(self: PropertyReference[TOperand, TResult]) -> InArgument[TOperand]
        Set: Operand(self: PropertyReference[TOperand, TResult]) = value
        """
        ...

    @property
    def PropertyName(self) -> str:
        """
        Get: PropertyName(self: PropertyReference[TOperand, TResult]) -> str
        Set: PropertyName(self: PropertyReference[TOperand, TResult]) = value
        """
        ...



class PropertyValue(CodeActivity): # skipped bases: <type 'object'>
    """ PropertyValue[TOperand, TResult]() """
    @property
    def Operand(self) -> InArgument:
        """
        Get: Operand(self: PropertyValue[TOperand, TResult]) -> InArgument[TOperand]
        Set: Operand(self: PropertyValue[TOperand, TResult]) = value
        """
        ...

    @property
    def PropertyName(self) -> str:
        """
        Get: PropertyName(self: PropertyValue[TOperand, TResult]) -> str
        Set: PropertyName(self: PropertyValue[TOperand, TResult]) = value
        """
        ...



class Subtract(CodeActivity): # skipped bases: <type 'object'>
    """ Subtract[TLeft, TRight, TResult]() """
    @property
    def Checked(self) -> bool:
        """
        Get: Checked(self: Subtract[TLeft, TRight, TResult]) -> bool
        Set: Checked(self: Subtract[TLeft, TRight, TResult]) = value
        """
        ...

    @property
    def Left(self) -> InArgument:
        """
        Get: Left(self: Subtract[TLeft, TRight, TResult]) -> InArgument[TLeft]
        Set: Left(self: Subtract[TLeft, TRight, TResult]) = value
        """
        ...

    @property
    def Right(self) -> InArgument:
        """
        Get: Right(self: Subtract[TLeft, TRight, TResult]) -> InArgument[TRight]
        Set: Right(self: Subtract[TLeft, TRight, TResult]) = value
        """
        ...



class TextExpression: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DefaultNamespaces(self) -> IList:
        """ Get: DefaultNamespaces() -> IList[str] """
        ...

    @property
    def DefaultReferences(self) -> IList:
        """ Get: DefaultReferences() -> IList[AssemblyReference] """
        ...


    @staticmethod
    def GetNamespaces(target:object) -> IList:
        """ GetNamespaces(target: object) -> IList[str] """
        ...

    @staticmethod
    def GetNamespacesForImplementation(target:object) -> IList:
        """ GetNamespacesForImplementation(target: object) -> IList[str] """
        ...

    @staticmethod
    def GetNamespacesInScope(activity:Activity) -> IList:
        """ GetNamespacesInScope(activity: Activity) -> IList[str] """
        ...

    @staticmethod
    def GetReferences(target:object) -> IList:
        """ GetReferences(target: object) -> IList[AssemblyReference] """
        ...

    @staticmethod
    def GetReferencesForImplementation(target:object) -> IList:
        """ GetReferencesForImplementation(target: object) -> IList[AssemblyReference] """
        ...

    @staticmethod
    def GetReferencesInScope(activity:Activity) -> IList:
        """ GetReferencesInScope(activity: Activity) -> IList[AssemblyReference] """
        ...

    @staticmethod
    def SetNamespaces(target:object, namespaces:IList): # -> 
        """ SetNamespaces(target: object, namespaces: IList[str])SetNamespaces(target: object, *namespaces: Array[str]) """
        ...

    @staticmethod
    def SetNamespacesForImplementation(target:object, namespaces:IList): # -> 
        """ SetNamespacesForImplementation(target: object, namespaces: IList[str])SetNamespacesForImplementation(target: object, *namespaces: Array[str]) """
        ...

    @staticmethod
    def SetReferences(target:object, references:IList): # -> 
        """ SetReferences(target: object, references: IList[AssemblyReference])SetReferences(target: object, *references: Array[AssemblyReference]) """
        ...

    @staticmethod
    def SetReferencesForImplementation(target:object, references:IList): # -> 
        """ SetReferencesForImplementation(target: object, references: IList[AssemblyReference])SetReferencesForImplementation(target: object, *references: Array[AssemblyReference]) """
        ...

    @staticmethod
    def ShouldSerializeNamespaces(target:object) -> bool:
        """ ShouldSerializeNamespaces(target: object) -> bool """
        ...

    @staticmethod
    def ShouldSerializeNamespacesForImplementation(target:object) -> bool:
        """ ShouldSerializeNamespacesForImplementation(target: object) -> bool """
        ...

    @staticmethod
    def ShouldSerializeReferences(target:object) -> bool:
        """ ShouldSerializeReferences(target: object) -> bool """
        ...

    @staticmethod
    def ShouldSerializeReferencesForImplementation(target:object) -> bool:
        """ ShouldSerializeReferencesForImplementation(target: object) -> bool """
        ...

    __all__: list = ...


class ValueTypeFieldReference(CodeActivity): # skipped bases: <type 'object'>
    """ ValueTypeFieldReference[TOperand, TResult]() """
    @property
    def FieldName(self) -> str:
        """
        Get: FieldName(self: ValueTypeFieldReference[TOperand, TResult]) -> str
        Set: FieldName(self: ValueTypeFieldReference[TOperand, TResult]) = value
        """
        ...

    @property
    def OperandLocation(self) -> InOutArgument:
        """
        Get: OperandLocation(self: ValueTypeFieldReference[TOperand, TResult]) -> InOutArgument[TOperand]
        Set: OperandLocation(self: ValueTypeFieldReference[TOperand, TResult]) = value
        """
        ...



class ValueTypeIndexerReference(CodeActivity): # skipped bases: <type 'object'>
    """ ValueTypeIndexerReference[TOperand, TItem]() """
    @property
    def Indices(self) -> Collection:
        """ Get: Indices(self: ValueTypeIndexerReference[TOperand, TItem]) -> Collection[InArgument] """
        ...

    @property
    def OperandLocation(self) -> InOutArgument:
        """
        Get: OperandLocation(self: ValueTypeIndexerReference[TOperand, TItem]) -> InOutArgument[TOperand]
        Set: OperandLocation(self: ValueTypeIndexerReference[TOperand, TItem]) = value
        """
        ...



class ValueTypePropertyReference(CodeActivity): # skipped bases: <type 'object'>
    """ ValueTypePropertyReference[TOperand, TResult]() """
    @property
    def OperandLocation(self) -> InOutArgument:
        """
        Get: OperandLocation(self: ValueTypePropertyReference[TOperand, TResult]) -> InOutArgument[TOperand]
        Set: OperandLocation(self: ValueTypePropertyReference[TOperand, TResult]) = value
        """
        ...

    @property
    def PropertyName(self) -> str:
        """
        Get: PropertyName(self: ValueTypePropertyReference[TOperand, TResult]) -> str
        Set: PropertyName(self: ValueTypePropertyReference[TOperand, TResult]) = value
        """
        ...



class VariableReference(EnvironmentLocationReference): # skipped bases: <type 'IExpressionContainer'>, <type 'ILocationReferenceExpression'>, <type 'object'>
    """
    VariableReference[T]()
    VariableReference[T](variable: Variable)
    """
    @property
    def Variable(self) -> Variable:
        """
        Get: Variable(self: VariableReference[T]) -> Variable
        Set: Variable(self: VariableReference[T]) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: VariableReference[T]) -> str """
        ...

    def __new__(cls, variable:Variable = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, variable: Variable)
        """
        ...


class VariableValue(EnvironmentLocationValue): # skipped bases: <type 'IExpressionContainer'>, <type 'ILocationReferenceExpression'>, <type 'object'>
    """
    VariableValue[T]()
    VariableValue[T](variable: Variable)
    """
    @property
    def Variable(self) -> Variable:
        """
        Get: Variable(self: VariableValue[T]) -> Variable
        Set: Variable(self: VariableValue[T]) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: VariableValue[T]) -> str """
        ...

    def __new__(cls, variable:Variable = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, variable: Variable)
        """
        ...


