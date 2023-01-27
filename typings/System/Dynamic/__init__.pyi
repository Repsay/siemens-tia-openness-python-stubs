# encoding: utf-8
# module System.Dynamic calls itself Dynamic
# from System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Type

from System.Collections import IDictionary, IEnumerable, IList

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel import INotifyPropertyChanged

from System.Linq.Expressions import Expression, ExpressionType

from System.Runtime.CompilerServices import CallSiteBinder

from typing import Tuple as Tuple_

"""The following names are not found in the module: (Array[DynamicMetaObject], 
    CustomRestriction)
"""

# no functions
# classes

class DynamicMetaObjectBinder(CallSiteBinder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ReturnType(self) -> Type:
        """ Get: ReturnType(self: DynamicMetaObjectBinder) -> Type """
        ...


    def Defer(self, *__args:Array) -> DynamicMetaObject:
        """
        Defer(self: DynamicMetaObjectBinder, *args: Array[DynamicMetaObject]) -> DynamicMetaObject
        Defer(self: DynamicMetaObjectBinder, target: DynamicMetaObject, *args: Array[DynamicMetaObject]) -> DynamicMetaObject
        """
        ...

    def GetUpdateExpression(self, type:Type) -> Expression:
        """ GetUpdateExpression(self: DynamicMetaObjectBinder, type: Type) -> Expression """
        ...


class BinaryOperationBinder(DynamicMetaObjectBinder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Operation(self) -> ExpressionType:
        """ Get: Operation(self: BinaryOperationBinder) -> ExpressionType """
        ...


    def FallbackBinaryOperation(self, target:DynamicMetaObject, arg:DynamicMetaObject, errorSuggestion:DynamicMetaObject = ...) -> DynamicMetaObject:
        """
        FallbackBinaryOperation(self: BinaryOperationBinder, target: DynamicMetaObject, arg: DynamicMetaObject) -> DynamicMetaObject
        FallbackBinaryOperation(self: BinaryOperationBinder, target: DynamicMetaObject, arg: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, operation: ExpressionType) """
        ...


class BindingRestrictions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Combine(contributingObjects:IList) -> BindingRestrictions:
        """ Combine(contributingObjects: IList[DynamicMetaObject]) -> BindingRestrictions """
        ...

    @staticmethod
    def GetExpressionRestriction(expression:Expression) -> BindingRestrictions:
        """ GetExpressionRestriction(expression: Expression) -> BindingRestrictions """
        ...

    @staticmethod
    def GetInstanceRestriction(expression:Expression, instance:object) -> BindingRestrictions:
        """ GetInstanceRestriction(expression: Expression, instance: object) -> BindingRestrictions """
        ...

    @staticmethod
    def GetTypeRestriction(expression:Expression, type:Type) -> BindingRestrictions:
        """ GetTypeRestriction(expression: Expression, type: Type) -> BindingRestrictions """
        ...

    def Merge(self, restrictions:BindingRestrictions) -> BindingRestrictions:
        """ Merge(self: BindingRestrictions, restrictions: BindingRestrictions) -> BindingRestrictions """
        ...

    def ToExpression(self) -> Expression:
        """ ToExpression(self: BindingRestrictions) -> Expression """
        ...

    Empty = ...


class CallInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    CallInfo(argCount: int, *argNames: Array[str])
    CallInfo(argCount: int, argNames: IEnumerable[str])
    """
    @property
    def ArgumentCount(self) -> int:
        """ Get: ArgumentCount(self: CallInfo) -> int """
        ...

    @property
    def ArgumentNames(self) -> ReadOnlyCollection:
        """ Get: ArgumentNames(self: CallInfo) -> ReadOnlyCollection[str] """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: CallInfo, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CallInfo) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConvertBinder(DynamicMetaObjectBinder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Explicit(self) -> bool:
        """ Get: Explicit(self: ConvertBinder) -> bool """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: ConvertBinder) -> Type """
        ...


    def FallbackConvert(self, target:DynamicMetaObject, errorSuggestion:DynamicMetaObject = ...) -> DynamicMetaObject:
        """
        FallbackConvert(self: ConvertBinder, target: DynamicMetaObject) -> DynamicMetaObject
        FallbackConvert(self: ConvertBinder, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, type: Type, explicit: bool) """
        ...


class CreateInstanceBinder(DynamicMetaObjectBinder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CallInfo(self) -> CallInfo:
        """ Get: CallInfo(self: CreateInstanceBinder) -> CallInfo """
        ...


    def FallbackCreateInstance(self, target:DynamicMetaObject, args:Array, errorSuggestion:DynamicMetaObject = ...) -> DynamicMetaObject:
        """
        FallbackCreateInstance(self: CreateInstanceBinder, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject
        FallbackCreateInstance(self: CreateInstanceBinder, target: DynamicMetaObject, args: Array[DynamicMetaObject], errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, callInfo: CallInfo) """
        ...


class DeleteIndexBinder(DynamicMetaObjectBinder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CallInfo(self) -> CallInfo:
        """ Get: CallInfo(self: DeleteIndexBinder) -> CallInfo """
        ...


    def FallbackDeleteIndex(self, target:DynamicMetaObject, indexes:Array, errorSuggestion:DynamicMetaObject = ...) -> DynamicMetaObject:
        """
        FallbackDeleteIndex(self: DeleteIndexBinder, target: DynamicMetaObject, indexes: Array[DynamicMetaObject]) -> DynamicMetaObject
        FallbackDeleteIndex(self: DeleteIndexBinder, target: DynamicMetaObject, indexes: Array[DynamicMetaObject], errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, callInfo: CallInfo) """
        ...


class DeleteMemberBinder(DynamicMetaObjectBinder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IgnoreCase(self) -> bool:
        """ Get: IgnoreCase(self: DeleteMemberBinder) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DeleteMemberBinder) -> str """
        ...


    def FallbackDeleteMember(self, target:DynamicMetaObject, errorSuggestion:DynamicMetaObject = ...) -> DynamicMetaObject:
        """
        FallbackDeleteMember(self: DeleteMemberBinder, target: DynamicMetaObject) -> DynamicMetaObject
        FallbackDeleteMember(self: DeleteMemberBinder, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, name: str, ignoreCase: bool) """
        ...


class DynamicMetaObject: # skipped bases: <type 'object'>, <type 'object'>
    """
    DynamicMetaObject(expression: Expression, restrictions: BindingRestrictions)
    DynamicMetaObject(expression: Expression, restrictions: BindingRestrictions, value: object)
    """
    @property
    def Expression(self) -> Expression:
        """ Get: Expression(self: DynamicMetaObject) -> Expression """
        ...

    @property
    def HasValue(self) -> bool:
        """ Get: HasValue(self: DynamicMetaObject) -> bool """
        ...

    @property
    def LimitType(self) -> Type:
        """ Get: LimitType(self: DynamicMetaObject) -> Type """
        ...

    @property
    def Restrictions(self) -> BindingRestrictions:
        """ Get: Restrictions(self: DynamicMetaObject) -> BindingRestrictions """
        ...

    @property
    def RuntimeType(self) -> Type:
        """ Get: RuntimeType(self: DynamicMetaObject) -> Type """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: DynamicMetaObject) -> object """
        ...


    def BindBinaryOperation(self, binder:BinaryOperationBinder, arg:DynamicMetaObject) -> DynamicMetaObject:
        """ BindBinaryOperation(self: DynamicMetaObject, binder: BinaryOperationBinder, arg: DynamicMetaObject) -> DynamicMetaObject """
        ...

    def BindConvert(self, binder:ConvertBinder) -> DynamicMetaObject:
        """ BindConvert(self: DynamicMetaObject, binder: ConvertBinder) -> DynamicMetaObject """
        ...

    def BindCreateInstance(self, binder:CreateInstanceBinder, args:Array) -> DynamicMetaObject:
        """ BindCreateInstance(self: DynamicMetaObject, binder: CreateInstanceBinder, args: Array[DynamicMetaObject]) -> DynamicMetaObject """
        ...

    def BindDeleteIndex(self, binder:DeleteIndexBinder, indexes:Array) -> DynamicMetaObject:
        """ BindDeleteIndex(self: DynamicMetaObject, binder: DeleteIndexBinder, indexes: Array[DynamicMetaObject]) -> DynamicMetaObject """
        ...

    def BindDeleteMember(self, binder:DeleteMemberBinder) -> DynamicMetaObject:
        """ BindDeleteMember(self: DynamicMetaObject, binder: DeleteMemberBinder) -> DynamicMetaObject """
        ...

    def BindGetIndex(self, binder:GetIndexBinder, indexes:Array) -> DynamicMetaObject:
        """ BindGetIndex(self: DynamicMetaObject, binder: GetIndexBinder, indexes: Array[DynamicMetaObject]) -> DynamicMetaObject """
        ...

    def BindGetMember(self, binder:GetMemberBinder) -> DynamicMetaObject:
        """ BindGetMember(self: DynamicMetaObject, binder: GetMemberBinder) -> DynamicMetaObject """
        ...

    def BindInvoke(self, binder:InvokeBinder, args:Array) -> DynamicMetaObject:
        """ BindInvoke(self: DynamicMetaObject, binder: InvokeBinder, args: Array[DynamicMetaObject]) -> DynamicMetaObject """
        ...

    def BindInvokeMember(self, binder:InvokeMemberBinder, args:Array) -> DynamicMetaObject:
        """ BindInvokeMember(self: DynamicMetaObject, binder: InvokeMemberBinder, args: Array[DynamicMetaObject]) -> DynamicMetaObject """
        ...

    def BindSetIndex(self, binder:SetIndexBinder, indexes:Array, value:DynamicMetaObject) -> DynamicMetaObject:
        """ BindSetIndex(self: DynamicMetaObject, binder: SetIndexBinder, indexes: Array[DynamicMetaObject], value: DynamicMetaObject) -> DynamicMetaObject """
        ...

    def BindSetMember(self, binder:SetMemberBinder, value:DynamicMetaObject) -> DynamicMetaObject:
        """ BindSetMember(self: DynamicMetaObject, binder: SetMemberBinder, value: DynamicMetaObject) -> DynamicMetaObject """
        ...

    def BindUnaryOperation(self, binder:UnaryOperationBinder) -> DynamicMetaObject:
        """ BindUnaryOperation(self: DynamicMetaObject, binder: UnaryOperationBinder) -> DynamicMetaObject """
        ...

    @staticmethod
    def Create(value:object, expression:Expression) -> DynamicMetaObject:
        """ Create(value: object, expression: Expression) -> DynamicMetaObject """
        ...

    def GetDynamicMemberNames(self) -> IEnumerable:
        """ GetDynamicMemberNames(self: DynamicMetaObject) -> IEnumerable[str] """
        ...

    EmptyMetaObjects = ...


class DynamicObject(IDynamicMetaObjectProvider): # skipped bases: <type 'object'>
    """ no doc """
    def GetDynamicMemberNames(self) -> IEnumerable:
        """ GetDynamicMemberNames(self: DynamicObject) -> IEnumerable[str] """
        ...

    def TryBinaryOperation(self, binder, arg, result) -> Tuple_[bool, object]:
        """ TryBinaryOperation(self: DynamicObject, binder: BinaryOperationBinder, arg: object) -> (bool, object) """
        ...

    def TryConvert(self, binder, result) -> Tuple_[bool, object]:
        """ TryConvert(self: DynamicObject, binder: ConvertBinder) -> (bool, object) """
        ...

    def TryCreateInstance(self, binder, args, result) -> Tuple_[bool, object]:
        """ TryCreateInstance(self: DynamicObject, binder: CreateInstanceBinder, args: Array[object]) -> (bool, object) """
        ...

    def TryDeleteIndex(self, binder:DeleteIndexBinder, indexes:Array) -> bool:
        """ TryDeleteIndex(self: DynamicObject, binder: DeleteIndexBinder, indexes: Array[object]) -> bool """
        ...

    def TryDeleteMember(self, binder:DeleteMemberBinder) -> bool:
        """ TryDeleteMember(self: DynamicObject, binder: DeleteMemberBinder) -> bool """
        ...

    def TryGetIndex(self, binder, indexes, result) -> Tuple_[bool, object]:
        """ TryGetIndex(self: DynamicObject, binder: GetIndexBinder, indexes: Array[object]) -> (bool, object) """
        ...

    def TryGetMember(self, binder, result) -> Tuple_[bool, object]:
        """ TryGetMember(self: DynamicObject, binder: GetMemberBinder) -> (bool, object) """
        ...

    def TryInvoke(self, binder, args, result) -> Tuple_[bool, object]:
        """ TryInvoke(self: DynamicObject, binder: InvokeBinder, args: Array[object]) -> (bool, object) """
        ...

    def TryInvokeMember(self, binder, args, result) -> Tuple_[bool, object]:
        """ TryInvokeMember(self: DynamicObject, binder: InvokeMemberBinder, args: Array[object]) -> (bool, object) """
        ...

    def TrySetIndex(self, binder:SetIndexBinder, indexes:Array, value:object) -> bool:
        """ TrySetIndex(self: DynamicObject, binder: SetIndexBinder, indexes: Array[object], value: object) -> bool """
        ...

    def TrySetMember(self, binder:SetMemberBinder, value:object) -> bool:
        """ TrySetMember(self: DynamicObject, binder: SetMemberBinder, value: object) -> bool """
        ...

    def TryUnaryOperation(self, binder, result) -> Tuple_[bool, object]:
        """ TryUnaryOperation(self: DynamicObject, binder: UnaryOperationBinder) -> (bool, object) """
        ...


class IDynamicMetaObjectProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetMetaObject(self, parameter:Expression) -> DynamicMetaObject:
        """ GetMetaObject(self: IDynamicMetaObjectProvider, parameter: Expression) -> DynamicMetaObject """
        ...

    def __dir__(self, *args): #cannot find CLR method
        """ __dir__(self: IDynamicMetaObjectProvider) -> list """
        ...


class ExpandoObject(IDictionary, IDynamicMetaObjectProvider, INotifyPropertyChanged): # skipped bases: <type 'IEnumerable[KeyValuePair[str, object]]'>, <type 'ICollection[KeyValuePair[str, object]]'>, <type 'IEnumerable'>, <type 'object'>
    """ ExpandoObject() """
    pass

class GetIndexBinder(DynamicMetaObjectBinder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CallInfo(self) -> CallInfo:
        """ Get: CallInfo(self: GetIndexBinder) -> CallInfo """
        ...


    def FallbackGetIndex(self, target:DynamicMetaObject, indexes:Array, errorSuggestion:DynamicMetaObject = ...) -> DynamicMetaObject:
        """
        FallbackGetIndex(self: GetIndexBinder, target: DynamicMetaObject, indexes: Array[DynamicMetaObject]) -> DynamicMetaObject
        FallbackGetIndex(self: GetIndexBinder, target: DynamicMetaObject, indexes: Array[DynamicMetaObject], errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, callInfo: CallInfo) """
        ...


class GetMemberBinder(DynamicMetaObjectBinder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IgnoreCase(self) -> bool:
        """ Get: IgnoreCase(self: GetMemberBinder) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: GetMemberBinder) -> str """
        ...


    def FallbackGetMember(self, target:DynamicMetaObject, errorSuggestion:DynamicMetaObject = ...) -> DynamicMetaObject:
        """
        FallbackGetMember(self: GetMemberBinder, target: DynamicMetaObject) -> DynamicMetaObject
        FallbackGetMember(self: GetMemberBinder, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, name: str, ignoreCase: bool) """
        ...


class IInvokeOnGetBinder: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def InvokeOnGet(self) -> bool:
        """ Get: InvokeOnGet(self: IInvokeOnGetBinder) -> bool """
        ...



class InvokeBinder(DynamicMetaObjectBinder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CallInfo(self) -> CallInfo:
        """ Get: CallInfo(self: InvokeBinder) -> CallInfo """
        ...


    def FallbackInvoke(self, target:DynamicMetaObject, args:Array, errorSuggestion:DynamicMetaObject = ...) -> DynamicMetaObject:
        """
        FallbackInvoke(self: InvokeBinder, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject
        FallbackInvoke(self: InvokeBinder, target: DynamicMetaObject, args: Array[DynamicMetaObject], errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, callInfo: CallInfo) """
        ...


class InvokeMemberBinder(DynamicMetaObjectBinder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CallInfo(self) -> CallInfo:
        """ Get: CallInfo(self: InvokeMemberBinder) -> CallInfo """
        ...

    @property
    def IgnoreCase(self) -> bool:
        """ Get: IgnoreCase(self: InvokeMemberBinder) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: InvokeMemberBinder) -> str """
        ...


    def FallbackInvoke(self, target:DynamicMetaObject, args:Array, errorSuggestion:DynamicMetaObject) -> DynamicMetaObject:
        """ FallbackInvoke(self: InvokeMemberBinder, target: DynamicMetaObject, args: Array[DynamicMetaObject], errorSuggestion: DynamicMetaObject) -> DynamicMetaObject """
        ...

    def FallbackInvokeMember(self, target:DynamicMetaObject, args:Array, errorSuggestion:DynamicMetaObject = ...) -> DynamicMetaObject:
        """
        FallbackInvokeMember(self: InvokeMemberBinder, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject
        FallbackInvokeMember(self: InvokeMemberBinder, target: DynamicMetaObject, args: Array[DynamicMetaObject], errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, name: str, ignoreCase: bool, callInfo: CallInfo) """
        ...


class SetIndexBinder(DynamicMetaObjectBinder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CallInfo(self) -> CallInfo:
        """ Get: CallInfo(self: SetIndexBinder) -> CallInfo """
        ...


    def FallbackSetIndex(self, target:DynamicMetaObject, indexes:Array, value:DynamicMetaObject, errorSuggestion:DynamicMetaObject = ...) -> DynamicMetaObject:
        """
        FallbackSetIndex(self: SetIndexBinder, target: DynamicMetaObject, indexes: Array[DynamicMetaObject], value: DynamicMetaObject) -> DynamicMetaObject
        FallbackSetIndex(self: SetIndexBinder, target: DynamicMetaObject, indexes: Array[DynamicMetaObject], value: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, callInfo: CallInfo) """
        ...


class SetMemberBinder(DynamicMetaObjectBinder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IgnoreCase(self) -> bool:
        """ Get: IgnoreCase(self: SetMemberBinder) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: SetMemberBinder) -> str """
        ...


    def FallbackSetMember(self, target:DynamicMetaObject, value:DynamicMetaObject, errorSuggestion:DynamicMetaObject = ...) -> DynamicMetaObject:
        """
        FallbackSetMember(self: SetMemberBinder, target: DynamicMetaObject, value: DynamicMetaObject) -> DynamicMetaObject
        FallbackSetMember(self: SetMemberBinder, target: DynamicMetaObject, value: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, name: str, ignoreCase: bool) """
        ...


class UnaryOperationBinder(DynamicMetaObjectBinder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Operation(self) -> ExpressionType:
        """ Get: Operation(self: UnaryOperationBinder) -> ExpressionType """
        ...


    def FallbackUnaryOperation(self, target:DynamicMetaObject, errorSuggestion:DynamicMetaObject = ...) -> DynamicMetaObject:
        """
        FallbackUnaryOperation(self: UnaryOperationBinder, target: DynamicMetaObject) -> DynamicMetaObject
        FallbackUnaryOperation(self: UnaryOperationBinder, target: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, operation: ExpressionType) """
        ...


