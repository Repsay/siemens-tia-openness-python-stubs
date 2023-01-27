# encoding: utf-8
# module Microsoft.Scripting.Actions calls itself Actions
# from Microsoft.Dynamic, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Scripting.Actions.Calls import (Candidate, NarrowingLevel, 
    OverloadResolver, OverloadResolverFactory)

from Microsoft.Scripting.Runtime import (CallTypes, DynamicDelegateCreator, 
    IMembersList)

from System import Array, Attribute, Enum, IEquatable, Type

from System.Collections import IEnumerable, IEqualityComparer, IList

from System.Dynamic import (BinaryOperationBinder, BindingRestrictions, 
    DynamicMetaObject, DynamicMetaObjectBinder, UnaryOperationBinder)

from System.Linq.Expressions import (ConstantExpression, 
    DynamicExpressionVisitor, Expression)

from System.Reflection import (Assembly, ConstructorInfo, EventInfo, 
    FieldInfo, MemberInfo, MethodBase, MethodInfo, PropertyInfo)

from System.Runtime.CompilerServices import CallSiteBinder

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (Array[MemberTracker], 
    ScriptDomainManager, dictproxy, field#, member_descriptor, namespace#, 
    type-collision)
"""

# no functions
# classes

class ActionBinder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Manager(self): # -> ScriptDomainManager
        """ Get: Manager(self: ActionBinder) -> ScriptDomainManager """
        ...

    @property
    def PrivateBinding(self) -> bool:
        """ Get: PrivateBinding(self: ActionBinder) -> bool """
        ...


    def CanConvertFrom(self, fromType:Type, toType:Type, toNotNullable:bool, level:NarrowingLevel) -> bool:
        """ CanConvertFrom(self: ActionBinder, fromType: Type, toType: Type, toNotNullable: bool, level: NarrowingLevel) -> bool """
        ...

    def Convert(self, obj:object, toType:Type) -> object:
        """ Convert(self: ActionBinder, obj: object, toType: Type) -> object """
        ...

    def ConvertExpression(self, expr:Expression, toType:Type, kind:ConversionResultKind, resolverFactory:OverloadResolverFactory) -> Expression:
        """ ConvertExpression(self: ActionBinder, expr: Expression, toType: Type, kind: ConversionResultKind, resolverFactory: OverloadResolverFactory) -> Expression """
        ...

    def GetAllExtensionMembers(self, type:Type, name:str) -> MemberGroup:
        """ GetAllExtensionMembers(self: ActionBinder, type: Type, name: str) -> MemberGroup """
        ...

    def GetExtensionMembers(self, declaringType:Type, name:str) -> MemberGroup:
        """ GetExtensionMembers(self: ActionBinder, declaringType: Type, name: str) -> MemberGroup """
        ...

    def GetExtensionTypes(self, t:Type) -> IList:
        """ GetExtensionTypes(self: ActionBinder, t: Type) -> IList[Type] """
        ...

    def GetMember(self, action:MemberRequestKind, type:Type, name:str) -> MemberGroup:
        """ GetMember(self: ActionBinder, action: MemberRequestKind, type: Type, name: str) -> MemberGroup """
        ...

    def GetObjectTypeName(self, arg:object) -> str:
        """ GetObjectTypeName(self: ActionBinder, arg: object) -> str """
        ...

    def GetTypeName(self, t:Type) -> str:
        """ GetTypeName(self: ActionBinder, t: Type) -> str """
        ...

    def IncludeExtensionMember(self, member:MemberInfo) -> bool:
        """ IncludeExtensionMember(self: ActionBinder, member: MemberInfo) -> bool """
        ...

    def MakeCallExpression(self, resolverFactory:OverloadResolverFactory, method:MethodInfo, parameters:Array) -> DynamicMetaObject:
        """ MakeCallExpression(self: ActionBinder, resolverFactory: OverloadResolverFactory, method: MethodInfo, *parameters: Array[DynamicMetaObject]) -> DynamicMetaObject """
        ...

    def MakeContainsGenericParametersError(self, tracker:MemberTracker) -> ErrorInfo:
        """ MakeContainsGenericParametersError(self: ActionBinder, tracker: MemberTracker) -> ErrorInfo """
        ...

    def MakeConversionError(self, toType:Type, value:Expression) -> ErrorInfo:
        """ MakeConversionError(self: ActionBinder, toType: Type, value: Expression) -> ErrorInfo """
        ...

    def MakeGenericAccessError(self, info:MemberTracker) -> ErrorInfo:
        """ MakeGenericAccessError(self: ActionBinder, info: MemberTracker) -> ErrorInfo """
        ...

    def MakeMissingMemberError(self, type:Type, self, name:str) -> ErrorInfo:
        """ MakeMissingMemberError(self: ActionBinder, type: Type, self: DynamicMetaObject, name: str) -> ErrorInfo """
        ...

    def MakeMissingMemberErrorForAssign(self, type:Type, self, name:str) -> ErrorInfo:
        """ MakeMissingMemberErrorForAssign(self: ActionBinder, type: Type, self: DynamicMetaObject, name: str) -> ErrorInfo """
        ...

    def MakeMissingMemberErrorForAssignReadOnlyProperty(self, type:Type, self, name:str) -> ErrorInfo:
        """ MakeMissingMemberErrorForAssignReadOnlyProperty(self: ActionBinder, type: Type, self: DynamicMetaObject, name: str) -> ErrorInfo """
        ...

    def MakeMissingMemberErrorForDelete(self, type:Type, self, name:str) -> ErrorInfo:
        """ MakeMissingMemberErrorForDelete(self: ActionBinder, type: Type, self: DynamicMetaObject, name: str) -> ErrorInfo """
        ...

    def MakeMissingMemberErrorInfo(self, type:Type, name:str) -> ErrorInfo:
        """ MakeMissingMemberErrorInfo(self: ActionBinder, type: Type, name: str) -> ErrorInfo """
        ...

    def MakeSetValueTypeFieldError(self, field:FieldTracker, instance:DynamicMetaObject, value:DynamicMetaObject) -> ErrorInfo:
        """ MakeSetValueTypeFieldError(self: ActionBinder, field: FieldTracker, instance: DynamicMetaObject, value: DynamicMetaObject) -> ErrorInfo """
        ...

    def MakeStaticAssignFromDerivedTypeError(self, accessingType:Type, self, assigning:MemberTracker, assignedValue:DynamicMetaObject, context:OverloadResolverFactory) -> ErrorInfo:
        """ MakeStaticAssignFromDerivedTypeError(self: ActionBinder, accessingType: Type, self: DynamicMetaObject, assigning: MemberTracker, assignedValue: DynamicMetaObject, context: OverloadResolverFactory) -> ErrorInfo """
        ...

    def MakeStaticPropertyInstanceAccessError(self, tracker:PropertyTracker, isAssignment:bool, parameters:Array) -> ErrorInfo:
        """
        MakeStaticPropertyInstanceAccessError(self: ActionBinder, tracker: PropertyTracker, isAssignment: bool, *parameters: Array[DynamicMetaObject]) -> ErrorInfo
        MakeStaticPropertyInstanceAccessError(self: ActionBinder, tracker: PropertyTracker, isAssignment: bool, parameters: IList[DynamicMetaObject]) -> ErrorInfo
        """
        ...

    def PreferConvert(self, t1:Type, t2:Type) -> Candidate:
        """ PreferConvert(self: ActionBinder, t1: Type, t2: Type) -> Candidate """
        ...

    def ReturnMemberTracker(self, type:Type, memberTracker:MemberTracker) -> DynamicMetaObject:
        """ ReturnMemberTracker(self: ActionBinder, type: Type, memberTracker: MemberTracker) -> DynamicMetaObject """
        ...


class Argument(IEquatable): # skipped bases: <type 'object'>
    """
    Argument(name: str)
    Argument(kind: ArgumentType)
    Argument(kind: ArgumentType, name: str)
    """
    @property
    def IsSimple(self) -> bool:
        """ Get: IsSimple(self: Argument) -> bool """
        ...

    @property
    def Kind(self) -> ArgumentType:
        """ Get: Kind(self: Argument) -> ArgumentType """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Argument) -> str """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: Argument) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Argument) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Simple: Argument = ...


class ArgumentType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ArgumentType, values: Dictionary (3), Instance (4), List (2), Named (1), Simple (0) """
    Dictionary: ArgumentType = ...
    Instance: ArgumentType = ...
    List: ArgumentType = ...
    Named: ArgumentType = ...
    Simple: ArgumentType = ...
    value__ = ...


class BinderMappingInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    BinderMappingInfo(binder: DynamicMetaObjectBinder, mappingInfo: IList[ParameterMappingInfo])
    BinderMappingInfo(binder: DynamicMetaObjectBinder, *mappingInfos: Array[ParameterMappingInfo])
    """
    def ToString(self) -> str:
        """ ToString(self: BinderMappingInfo) -> str """
        ...

    Binder = ...
    MappingInfo = ...


class MemberTracker: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: MemberTracker) -> Type """
        ...

    @property
    def MemberType(self) -> TrackerTypes:
        """ Get: MemberType(self: MemberTracker) -> TrackerTypes """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MemberTracker) -> str """
        ...


    def BindToInstance(self, instance:DynamicMetaObject) -> MemberTracker:
        """ BindToInstance(self: MemberTracker, instance: DynamicMetaObject) -> MemberTracker """
        ...

    @staticmethod
    def FromMemberInfo(member:MemberInfo, extending:Type = ...) -> MemberTracker:
        """
        FromMemberInfo(member: MemberInfo) -> MemberTracker
        FromMemberInfo(member: MemberInfo, extending: Type) -> MemberTracker
        """
        ...

    def GetBoundError(self, binder:ActionBinder, instance:DynamicMetaObject, instanceType:Type) -> ErrorInfo:
        """ GetBoundError(self: MemberTracker, binder: ActionBinder, instance: DynamicMetaObject, instanceType: Type) -> ErrorInfo """
        ...

    def GetBoundValue(self, *args): #cannot find CLR method
        """ GetBoundValue(self: MemberTracker, resolverFactory: OverloadResolverFactory, binder: ActionBinder, instanceType: Type, instance: DynamicMetaObject) -> DynamicMetaObject """
        ...

    def GetError(self, binder:ActionBinder, instanceType:Type) -> ErrorInfo:
        """ GetError(self: MemberTracker, binder: ActionBinder, instanceType: Type) -> ErrorInfo """
        ...

    def GetValue(self, resolverFactory:OverloadResolverFactory, binder:ActionBinder, instanceType:Type) -> DynamicMetaObject:
        """ GetValue(self: MemberTracker, resolverFactory: OverloadResolverFactory, binder: ActionBinder, instanceType: Type) -> DynamicMetaObject """
        ...

    def SetBoundValue(self, *args): #cannot find CLR method
        """
        SetBoundValue(self: MemberTracker, resolverFactory: OverloadResolverFactory, binder: ActionBinder, instanceType: Type, value: DynamicMetaObject, instance: DynamicMetaObject) -> DynamicMetaObject
        SetBoundValue(self: MemberTracker, resolverFactory: OverloadResolverFactory, binder: ActionBinder, instanceType: Type, value: DynamicMetaObject, instance: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    def SetValue(self, resolverFactory:OverloadResolverFactory, binder:ActionBinder, instanceType:Type, value:DynamicMetaObject, errorSuggestion:DynamicMetaObject = ...) -> DynamicMetaObject:
        """
        SetValue(self: MemberTracker, resolverFactory: OverloadResolverFactory, binder: ActionBinder, instanceType: Type, value: DynamicMetaObject) -> DynamicMetaObject
        SetValue(self: MemberTracker, resolverFactory: OverloadResolverFactory, binder: ActionBinder, instanceType: Type, value: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    EmptyTrackers = ...


class BoundMemberTracker(MemberTracker): # skipped bases: <type 'object'>
    """
    BoundMemberTracker(tracker: MemberTracker, instance: DynamicMetaObject)
    BoundMemberTracker(tracker: MemberTracker, instance: object)
    """
    @property
    def BoundTo(self) -> MemberTracker:
        """ Get: BoundTo(self: BoundMemberTracker) -> MemberTracker """
        ...

    @property
    def Instance(self) -> DynamicMetaObject:
        """ Get: Instance(self: BoundMemberTracker) -> DynamicMetaObject """
        ...

    @property
    def ObjectInstance(self) -> object:
        """ Get: ObjectInstance(self: BoundMemberTracker) -> object """
        ...


    def __new__(cls, tracker:MemberTracker, instance:DynamicMetaObject) -> Self:
        """
        __new__(cls: type, tracker: MemberTracker, instance: DynamicMetaObject)
        __new__(cls: type, tracker: MemberTracker, instance: object)
        """
        ...


class CallSignature(IEquatable): # skipped bases: <type 'object'>
    """
    CallSignature(signature: CallSignature)
    CallSignature(argumentCount: int)
    CallSignature(*infos: Array[Argument])
    CallSignature(*kinds: Array[ArgumentType])
    """
    @property
    def ArgumentCount(self) -> int:
        """ Get: ArgumentCount(self: CallSignature) -> int """
        ...

    @property
    def IsSimple(self) -> bool:
        """ Get: IsSimple(self: CallSignature) -> bool """
        ...


    def CreateExpression(self) -> Expression:
        """ CreateExpression(self: CallSignature) -> Expression """
        ...

    def GetArgumentInfos(self) -> Array:
        """ GetArgumentInfos(self: CallSignature) -> Array[Argument] """
        ...

    def GetArgumentKind(self, index:int) -> ArgumentType:
        """ GetArgumentKind(self: CallSignature, index: int) -> ArgumentType """
        ...

    def GetArgumentName(self, index:int) -> str:
        """ GetArgumentName(self: CallSignature, index: int) -> str """
        ...

    def GetArgumentNames(self) -> Array:
        """ GetArgumentNames(self: CallSignature) -> Array[str] """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CallSignature) -> int """
        ...

    def GetProvidedPositionalArgumentCount(self) -> int:
        """ GetProvidedPositionalArgumentCount(self: CallSignature) -> int """
        ...

    def HasDictionaryArgument(self) -> bool:
        """ HasDictionaryArgument(self: CallSignature) -> bool """
        ...

    def HasInstanceArgument(self) -> bool:
        """ HasInstanceArgument(self: CallSignature) -> bool """
        ...

    def HasKeywordArgument(self) -> bool:
        """ HasKeywordArgument(self: CallSignature) -> bool """
        ...

    def HasListArgument(self) -> bool:
        """ HasListArgument(self: CallSignature) -> bool """
        ...

    def IndexOf(self, kind:ArgumentType) -> int:
        """ IndexOf(self: CallSignature, kind: ArgumentType) -> int """
        ...

    def InsertArgument(self, info:Argument) -> CallSignature:
        """ InsertArgument(self: CallSignature, info: Argument) -> CallSignature """
        ...

    def InsertArgumentAt(self, index:int, info:Argument) -> CallSignature:
        """ InsertArgumentAt(self: CallSignature, index: int, info: Argument) -> CallSignature """
        ...

    def RemoveArgumentAt(self, index:int) -> CallSignature:
        """ RemoveArgumentAt(self: CallSignature, index: int) -> CallSignature """
        ...

    def RemoveFirstArgument(self) -> CallSignature:
        """ RemoveFirstArgument(self: CallSignature) -> CallSignature """
        ...

    def ToString(self) -> str:
        """ ToString(self: CallSignature) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ComboActionRewriter(DynamicExpressionVisitor): # skipped bases: <type 'object'>
    """ ComboActionRewriter() """
    pass

class ComboBinder(DynamicMetaObjectBinder): # skipped bases: <type 'object'>
    """
    ComboBinder(*binders: Array[BinderMappingInfo])
    ComboBinder(binders: ICollection[BinderMappingInfo])
    """
    def Equals(self, obj:object) -> bool:
        """ Equals(self: ComboBinder, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ComboBinder) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, binders:Array) -> Self:
        """
        __new__(cls: type, *binders: Array[BinderMappingInfo])
        __new__(cls: type, binders: ICollection[BinderMappingInfo])
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConstructorTracker(MemberTracker): # skipped bases: <type 'object'>
    """ ConstructorTracker(ctor: ConstructorInfo) """
    @property
    def IsPublic(self) -> bool:
        """ Get: IsPublic(self: ConstructorTracker) -> bool """
        ...


    def ToString(self) -> str:
        """ ToString(self: ConstructorTracker) -> str """
        ...

    def __new__(cls, ctor:ConstructorInfo) -> Self:
        """ __new__(cls: type, ctor: ConstructorInfo) """
        ...


class ConversionResultKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ConversionResultKind, values: ExplicitCast (1), ExplicitTry (3), ImplicitCast (0), ImplicitTry (2) """
    ExplicitCast: ConversionResultKind = ...
    ExplicitTry: ConversionResultKind = ...
    ImplicitCast: ConversionResultKind = ...
    ImplicitTry: ConversionResultKind = ...
    value__ = ...


class CustomTracker(MemberTracker): # skipped bases: <type 'object'>
    """ no doc """
    pass

class DefaultBinder(ActionBinder): # skipped bases: <type 'object'>
    """ DefaultBinder() """
    def Call(self, signature, *__args) -> DynamicMetaObject:
        """
        Call(self: DefaultBinder, signature: CallSignature, target: DynamicMetaObject, *args: Array[DynamicMetaObject]) -> DynamicMetaObject
        Call(self: DefaultBinder, signature: CallSignature, resolverFactory: OverloadResolverFactory, target: DynamicMetaObject, *args: Array[DynamicMetaObject]) -> DynamicMetaObject
        Call(self: DefaultBinder, signature: CallSignature, errorSuggestion: DynamicMetaObject, resolverFactory: OverloadResolverFactory, target: DynamicMetaObject, *args: Array[DynamicMetaObject]) -> DynamicMetaObject
        """
        ...

    def CallMethod(self, resolver:DefaultOverloadResolver, targets:IList, *__args:BindingRestrictions) -> DynamicMetaObject:
        """
        CallMethod(self: DefaultBinder, resolver: DefaultOverloadResolver, targets: IList[MethodBase], restrictions: BindingRestrictions) -> DynamicMetaObject
        CallMethod(self: DefaultBinder, resolver: DefaultOverloadResolver, targets: IList[MethodBase], restrictions: BindingRestrictions, name: str) -> DynamicMetaObject
        CallMethod(self: DefaultBinder, resolver: DefaultOverloadResolver, targets: IList[MethodBase]) -> DynamicMetaObject
        CallMethod(self: DefaultBinder, resolver: DefaultOverloadResolver, targets: IList[MethodBase], name: str) -> DynamicMetaObject
        CallMethod(self: DefaultBinder, resolver: DefaultOverloadResolver, targets: IList[MethodBase], restrictions: BindingRestrictions, name: str, minLevel: NarrowingLevel, maxLevel: NarrowingLevel) -> (DynamicMetaObject, BindingTarget)
        """
        ...

    def ConvertTo(self, toType:Type, kind:ConversionResultKind, arg:DynamicMetaObject, resolverFactory:OverloadResolverFactory = ..., errorSuggestion:DynamicMetaObject = ...) -> DynamicMetaObject:
        """
        ConvertTo(self: DefaultBinder, toType: Type, kind: ConversionResultKind, arg: DynamicMetaObject) -> DynamicMetaObject
        ConvertTo(self: DefaultBinder, toType: Type, kind: ConversionResultKind, arg: DynamicMetaObject, resolverFactory: OverloadResolverFactory) -> DynamicMetaObject
        ConvertTo(self: DefaultBinder, toType: Type, kind: ConversionResultKind, arg: DynamicMetaObject, resolverFactory: OverloadResolverFactory, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    def DeleteMember(self, name:str, target:DynamicMetaObject, resolutionFactory:OverloadResolverFactory = ..., errorSuggestion:DynamicMetaObject = ...) -> DynamicMetaObject:
        """
        DeleteMember(self: DefaultBinder, name: str, target: DynamicMetaObject) -> DynamicMetaObject
        DeleteMember(self: DefaultBinder, name: str, target: DynamicMetaObject, resolutionFactory: OverloadResolverFactory) -> DynamicMetaObject
        DeleteMember(self: DefaultBinder, name: str, target: DynamicMetaObject, resolutionFactory: OverloadResolverFactory, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    def DoOperation(self, operation:str, *__args:Array) -> DynamicMetaObject:
        """
        DoOperation(self: DefaultBinder, operation: str, *args: Array[DynamicMetaObject]) -> DynamicMetaObject
        DoOperation(self: DefaultBinder, operation: ExpressionType, *args: Array[DynamicMetaObject]) -> DynamicMetaObject
        DoOperation(self: DefaultBinder, operation: str, resolverFactory: OverloadResolverFactory, *args: Array[DynamicMetaObject]) -> DynamicMetaObject
        DoOperation(self: DefaultBinder, operation: ExpressionType, resolverFactory: OverloadResolverFactory, *args: Array[DynamicMetaObject]) -> DynamicMetaObject
        """
        ...

    def GetCallSignatures(self, target:DynamicMetaObject) -> DynamicMetaObject:
        """ GetCallSignatures(self: DefaultBinder, target: DynamicMetaObject) -> DynamicMetaObject """
        ...

    def GetDocumentation(self, target:DynamicMetaObject) -> DynamicMetaObject:
        """ GetDocumentation(self: DefaultBinder, target: DynamicMetaObject) -> DynamicMetaObject """
        ...

    def GetIndex(self, *__args:Array) -> DynamicMetaObject:
        """
        GetIndex(self: DefaultBinder, args: Array[DynamicMetaObject]) -> DynamicMetaObject
        GetIndex(self: DefaultBinder, resolverFactory: OverloadResolverFactory, args: Array[DynamicMetaObject]) -> DynamicMetaObject
        """
        ...

    def GetIsCallable(self, target:DynamicMetaObject) -> DynamicMetaObject:
        """ GetIsCallable(self: DefaultBinder, target: DynamicMetaObject) -> DynamicMetaObject """
        ...

    def GetMemberNames(self, target:DynamicMetaObject) -> DynamicMetaObject:
        """ GetMemberNames(self: DefaultBinder, target: DynamicMetaObject) -> DynamicMetaObject """
        ...

    def GetMemberType(self, members, error) -> Tuple_[TrackerTypes, Expression]:
        """ GetMemberType(self: DefaultBinder, members: MemberGroup) -> (TrackerTypes, Expression) """
        ...

    def GetMethod(self, type:Type, name:str) -> MethodInfo:
        """ GetMethod(self: DefaultBinder, type: Type, name: str) -> MethodInfo """
        ...

    @staticmethod
    def GetTryConvertReturnValue(type:Type) -> Expression:
        """ GetTryConvertReturnValue(type: Type) -> Expression """
        ...

    @staticmethod
    def MakeError(error:ErrorInfo, *__args:Type) -> DynamicMetaObject:
        """
        MakeError(error: ErrorInfo, restrictions: BindingRestrictions, type: Type) -> DynamicMetaObject
        MakeError(error: ErrorInfo, type: Type) -> DynamicMetaObject
        """
        ...

    def MakeEventValidation(self, members:MemberGroup, eventObject:DynamicMetaObject, value:DynamicMetaObject, resolverFactory:OverloadResolverFactory) -> ErrorInfo:
        """ MakeEventValidation(self: DefaultBinder, members: MemberGroup, eventObject: DynamicMetaObject, value: DynamicMetaObject, resolverFactory: OverloadResolverFactory) -> ErrorInfo """
        ...

    def MakeNonPublicMemberGetError(self, resolverFactory:OverloadResolverFactory, member:MemberTracker, type:Type, instance:DynamicMetaObject) -> ErrorInfo:
        """ MakeNonPublicMemberGetError(self: DefaultBinder, resolverFactory: OverloadResolverFactory, member: MemberTracker, type: Type, instance: DynamicMetaObject) -> ErrorInfo """
        ...

    def MakeReadOnlyMemberError(self, type:Type, name:str) -> ErrorInfo:
        """ MakeReadOnlyMemberError(self: DefaultBinder, type: Type, name: str) -> ErrorInfo """
        ...

    def MakeUndeletableMemberError(self, type:Type, name:str) -> ErrorInfo:
        """ MakeUndeletableMemberError(self: DefaultBinder, type: Type, name: str) -> ErrorInfo """
        ...

    def SetIndex(self, *__args:Array) -> DynamicMetaObject:
        """
        SetIndex(self: DefaultBinder, args: Array[DynamicMetaObject]) -> DynamicMetaObject
        SetIndex(self: DefaultBinder, resolverFactory: OverloadResolverFactory, args: Array[DynamicMetaObject]) -> DynamicMetaObject
        """
        ...

    def SetMember(self, name:str, target:DynamicMetaObject, value:DynamicMetaObject, *__args:OverloadResolverFactory) -> DynamicMetaObject:
        """
        SetMember(self: DefaultBinder, name: str, target: DynamicMetaObject, value: DynamicMetaObject) -> DynamicMetaObject
        SetMember(self: DefaultBinder, name: str, target: DynamicMetaObject, value: DynamicMetaObject, resolverFactory: OverloadResolverFactory) -> DynamicMetaObject
        SetMember(self: DefaultBinder, name: str, target: DynamicMetaObject, value: DynamicMetaObject, errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        SetMember(self: DefaultBinder, name: str, target: DynamicMetaObject, value: DynamicMetaObject, errorSuggestion: DynamicMetaObject, resolverFactory: OverloadResolverFactory) -> DynamicMetaObject
        """
        ...

    def __call__(self, *args): #cannot find CLR method
        """
        Call(self: DefaultBinder, signature: CallSignature, target: DynamicMetaObject, *args: Array[DynamicMetaObject]) -> DynamicMetaObject
        Call(self: DefaultBinder, signature: CallSignature, resolverFactory: OverloadResolverFactory, target: DynamicMetaObject, *args: Array[DynamicMetaObject]) -> DynamicMetaObject
        Call(self: DefaultBinder, signature: CallSignature, errorSuggestion: DynamicMetaObject, resolverFactory: OverloadResolverFactory, target: DynamicMetaObject, *args: Array[DynamicMetaObject]) -> DynamicMetaObject
        """
        ...

    def __dir__(self, *args): #cannot find CLR method
        """ GetMemberNames(self: DefaultBinder, target: DynamicMetaObject) -> DynamicMetaObject """
        ...


class DefaultOverloadResolver(OverloadResolver): # skipped bases: <type 'object'>
    """
    DefaultOverloadResolver(binder: ActionBinder, instance: DynamicMetaObject, args: IList[DynamicMetaObject], signature: CallSignature)
    DefaultOverloadResolver(binder: ActionBinder, args: IList[DynamicMetaObject], signature: CallSignature)
    DefaultOverloadResolver(binder: ActionBinder, args: IList[DynamicMetaObject], signature: CallSignature, callType: CallTypes)
    """
    @property
    def Arguments(self) -> IList:
        """ Get: Arguments(self: DefaultOverloadResolver) -> IList[DynamicMetaObject] """
        ...

    @property
    def CallType(self) -> CallTypes:
        """ Get: CallType(self: DefaultOverloadResolver) -> CallTypes """
        ...

    @property
    def Factory(self) -> OverloadResolverFactory:
        """ Get: Factory() -> OverloadResolverFactory """
        ...

    @property
    def Signature(self) -> CallSignature:
        """ Get: Signature(self: DefaultOverloadResolver) -> CallSignature """
        ...




class DynamicSiteHelpers: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetStandardDelegateType(types:Array) -> Type:
        """ GetStandardDelegateType(types: Array[Type]) -> Type """
        ...

    @staticmethod
    def IsInvisibleDlrStackFrame(mb:MethodBase) -> bool:
        """ IsInvisibleDlrStackFrame(mb: MethodBase) -> bool """
        ...

    @staticmethod
    def MakeCallSiteDelegate(types:Array) -> Type:
        """ MakeCallSiteDelegate(*types: Array[Type]) -> Type """
        ...

    __all__: list = ...


class ErrorInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Expression(self) -> Expression:
        """ Get: Expression(self: ErrorInfo) -> Expression """
        ...

    @property
    def Kind(self) -> ErrorInfoKind:
        """ Get: Kind(self: ErrorInfo) -> ErrorInfoKind """
        ...


    @staticmethod
    def FromException(exceptionValue:Expression) -> ErrorInfo:
        """ FromException(exceptionValue: Expression) -> ErrorInfo """
        ...

    @staticmethod
    def FromValue(resultValue:Expression) -> ErrorInfo:
        """ FromValue(resultValue: Expression) -> ErrorInfo """
        ...

    @staticmethod
    def FromValueNoError(resultValue:Expression) -> ErrorInfo:
        """ FromValueNoError(resultValue: Expression) -> ErrorInfo """
        ...


class ErrorInfoKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ErrorInfoKind, values: Error (1), Exception (0), Success (2) """
    Error: ErrorInfoKind = ...
    Exception: ErrorInfoKind = ...
    Success: ErrorInfoKind = ...
    value__ = ...


class ErrorMetaObject(DynamicMetaObject): # skipped bases: <type 'object'>
    """ ErrorMetaObject(body: Expression, restrictions: BindingRestrictions) """
    pass

class EventTracker(MemberTracker): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Event(self) -> EventInfo:
        """ Get: Event(self: EventTracker) -> EventInfo """
        ...

    @property
    def IsStatic(self) -> bool:
        """ Get: IsStatic(self: EventTracker) -> bool """
        ...


    def AddHandler(self, target:object, handler:object, delegateCreator:DynamicDelegateCreator): # -> 
        """ AddHandler(self: EventTracker, target: object, handler: object, delegateCreator: DynamicDelegateCreator) """
        ...

    def GetCallableAddMethod(self) -> MethodInfo:
        """ GetCallableAddMethod(self: EventTracker) -> MethodInfo """
        ...

    def GetCallableRemoveMethod(self) -> MethodInfo:
        """ GetCallableRemoveMethod(self: EventTracker) -> MethodInfo """
        ...

    def RemoveHandler(self, target:object, handler:object, objectComparer:IEqualityComparer): # -> 
        """ RemoveHandler(self: EventTracker, target: object, handler: object, objectComparer: IEqualityComparer[object]) """
        ...

    def ToString(self) -> str:
        """ ToString(self: EventTracker) -> str """
        ...


class ExtensionBinaryOperationBinder(BinaryOperationBinder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ExtensionOperation(self) -> str:
        """ Get: ExtensionOperation(self: ExtensionBinaryOperationBinder) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: ExtensionBinaryOperationBinder, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ExtensionBinaryOperationBinder) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MethodTracker(MemberTracker): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsPublic(self) -> bool:
        """ Get: IsPublic(self: MethodTracker) -> bool """
        ...

    @property
    def IsStatic(self) -> bool:
        """ Get: IsStatic(self: MethodTracker) -> bool """
        ...

    @property
    def Method(self) -> MethodInfo:
        """ Get: Method(self: MethodTracker) -> MethodInfo """
        ...


    def ToString(self) -> str:
        """ ToString(self: MethodTracker) -> str """
        ...


class ExtensionMethodTracker(MethodTracker): # skipped bases: <type 'object'>
    """ no doc """
    pass

class PropertyTracker(MemberTracker): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsStatic(self) -> bool:
        """ Get: IsStatic(self: PropertyTracker) -> bool """
        ...

    @property
    def PropertyType(self) -> Type:
        """ Get: PropertyType(self: PropertyTracker) -> Type """
        ...


    def GetDeleteMethod(self, privateMembers:bool = ...) -> MethodInfo:
        """
        GetDeleteMethod(self: PropertyTracker) -> MethodInfo
        GetDeleteMethod(self: PropertyTracker, privateMembers: bool) -> MethodInfo
        """
        ...

    def GetGetMethod(self, privateMembers:bool = ...) -> MethodInfo:
        """
        GetGetMethod(self: PropertyTracker) -> MethodInfo
        GetGetMethod(self: PropertyTracker, privateMembers: bool) -> MethodInfo
        """
        ...

    def GetIndexParameters(self) -> Array:
        """ GetIndexParameters(self: PropertyTracker) -> Array[ParameterInfo] """
        ...

    def GetSetMethod(self, privateMembers:bool = ...) -> MethodInfo:
        """
        GetSetMethod(self: PropertyTracker) -> MethodInfo
        GetSetMethod(self: PropertyTracker, privateMembers: bool) -> MethodInfo
        """
        ...


class ExtensionPropertyTracker(PropertyTracker): # skipped bases: <type 'object'>
    """ ExtensionPropertyTracker(name: str, getter: MethodInfo, setter: MethodInfo, deleter: MethodInfo, declaringType: Type) """
    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: ExtensionPropertyTracker) -> Type """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ExtensionPropertyTracker) -> str """
        ...


    def __new__(cls, name:str, getter:MethodInfo, setter:MethodInfo, deleter:MethodInfo, declaringType:Type) -> Self:
        """ __new__(cls: type, name: str, getter: MethodInfo, setter: MethodInfo, deleter: MethodInfo, declaringType: Type) """
        ...


class ExtensionUnaryOperationBinder(UnaryOperationBinder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ExtensionOperation(self) -> str:
        """ Get: ExtensionOperation(self: ExtensionUnaryOperationBinder) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: ExtensionUnaryOperationBinder, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ExtensionUnaryOperationBinder) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class FieldTracker(MemberTracker): # skipped bases: <type 'object'>
    """ FieldTracker(field: FieldInfo) """
    @property
    def Field(self) -> FieldInfo:
        """ Get: Field(self: FieldTracker) -> FieldInfo """
        ...

    @property
    def FieldType(self) -> Type:
        """ Get: FieldType(self: FieldTracker) -> Type """
        ...

    @property
    def IsInitOnly(self) -> bool:
        """ Get: IsInitOnly(self: FieldTracker) -> bool """
        ...

    @property
    def IsLiteral(self) -> bool:
        """ Get: IsLiteral(self: FieldTracker) -> bool """
        ...

    @property
    def IsPublic(self) -> bool:
        """ Get: IsPublic(self: FieldTracker) -> bool """
        ...

    @property
    def IsStatic(self) -> bool:
        """ Get: IsStatic(self: FieldTracker) -> bool """
        ...


    def ToString(self) -> str:
        """ ToString(self: FieldTracker) -> str """
        ...

    def __new__(cls, field:FieldInfo) -> Self:
        """ __new__(cls: type, field: FieldInfo) """
        ...


class ILightExceptionBinder: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SupportsLightThrow(self) -> bool:
        """ Get: SupportsLightThrow(self: ILightExceptionBinder) -> bool """
        ...


    def GetLightExceptionBinder(self) -> CallSiteBinder:
        """ GetLightExceptionBinder(self: ILightExceptionBinder) -> CallSiteBinder """
        ...


class Interceptor: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Intercept(*__args:Expression) -> Expression:
        """
        Intercept(expression: Expression) -> Expression
        Intercept(lambda: LambdaExpression) -> LambdaExpression
        """
        ...

    __all__: list = ...


class MemberGroup(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """
    MemberGroup(*members: Array[MemberTracker])
    MemberGroup(*members: Array[MemberInfo])
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: MemberGroup) -> int """
        ...


    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MemberTracker](enumerable: IEnumerable[MemberTracker], value: MemberTracker) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    EmptyGroup: MemberGroup = ...


class MemberRequestKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MemberRequestKind, values: Convert (6), Delete (3), Get (1), Invoke (4), InvokeMember (5), None (0), Operation (7), Set (2) """
    Convert: MemberRequestKind = ...
    Delete: MemberRequestKind = ...
    Get: MemberRequestKind = ...
    Invoke: MemberRequestKind = ...
    InvokeMember: MemberRequestKind = ...
    Operation: MemberRequestKind = ...
    Set: MemberRequestKind = ...
    value__ = ...


class MethodGroup(MemberTracker): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ContainsInstance(self) -> bool:
        """ Get: ContainsInstance(self: MethodGroup) -> bool """
        ...

    @property
    def ContainsStatic(self) -> bool:
        """ Get: ContainsStatic(self: MethodGroup) -> bool """
        ...

    @property
    def Methods(self) -> IList:
        """ Get: Methods(self: MethodGroup) -> IList[MethodTracker] """
        ...


    def GetMethodBases(self) -> Array:
        """ GetMethodBases(self: MethodGroup) -> Array[MethodBase] """
        ...

    def MakeGenericMethod(self, types:Array) -> MethodGroup:
        """ MakeGenericMethod(self: MethodGroup, types: Array[Type]) -> MethodGroup """
        ...


class NamespaceTracker(MemberTracker): # skipped bases: <type 'object'>
    """ no doc """
    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[KeyValuePair[str, object]](enumerable: IEnumerable[KeyValuePair[str, object]], value: KeyValuePair[str, object]) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, name: str) """
        ...

    __dict__ = ...
    __file__ = ...
    __name__: str = ...


class TypeTracker(MemberTracker): # skipped bases: <type 'object'>
    """ no doc """
    __dict__ = ...


class NestedTypeTracker(type-collision, IMembersList): # skipped bases: <type 'object'>
    """ NestedTypeTracker(type: Type) """
    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: NestedTypeTracker) -> Type """
        ...

    @property
    def IsGenericType(self) -> bool:
        """ Get: IsGenericType(self: NestedTypeTracker) -> bool """
        ...

    @property
    def IsPublic(self) -> bool:
        """ Get: IsPublic(self: NestedTypeTracker) -> bool """
        ...

    @property
    def MemberType(self) -> TrackerTypes:
        """ Get: MemberType(self: NestedTypeTracker) -> TrackerTypes """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: NestedTypeTracker) -> str """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: NestedTypeTracker) -> Type """
        ...


    def ToString(self) -> str:
        """ ToString(self: NestedTypeTracker) -> str """
        ...

    def __new__(cls, type:Type) -> Self:
        """ __new__(cls: type, type: Type) """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class NoSideEffectsAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ NoSideEffectsAttribute() """
    pass

class OperationBinder(DynamicMetaObjectBinder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Operation(self) -> str:
        """ Get: Operation(self: OperationBinder) -> str """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: OperationBinder, obj: object) -> bool """
        ...

    def FallbackOperation(self, target:DynamicMetaObject, args:Array, errorSuggestion:DynamicMetaObject = ...) -> DynamicMetaObject:
        """
        FallbackOperation(self: OperationBinder, target: DynamicMetaObject, args: Array[DynamicMetaObject]) -> DynamicMetaObject
        FallbackOperation(self: OperationBinder, target: DynamicMetaObject, args: Array[DynamicMetaObject], errorSuggestion: DynamicMetaObject) -> DynamicMetaObject
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: OperationBinder) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, operation: str) """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class OperationMetaObject(DynamicMetaObject): # skipped bases: <type 'object'>
    """
    OperationMetaObject(expression: Expression, restrictions: BindingRestrictions)
    OperationMetaObject(expression: Expression, restrictions: BindingRestrictions, value: object)
    """
    def BindOperation(self, binder:OperationBinder, args:Array) -> DynamicMetaObject:
        """ BindOperation(self: OperationMetaObject, binder: OperationBinder, *args: Array[DynamicMetaObject]) -> DynamicMetaObject """
        ...


class ParameterMappingInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ActionIndex(self) -> int:
        """ Get: ActionIndex(self: ParameterMappingInfo) -> int """
        ...

    @property
    def Constant(self) -> ConstantExpression:
        """ Get: Constant(self: ParameterMappingInfo) -> ConstantExpression """
        ...

    @property
    def IsAction(self) -> bool:
        """ Get: IsAction(self: ParameterMappingInfo) -> bool """
        ...

    @property
    def IsConstant(self) -> bool:
        """ Get: IsConstant(self: ParameterMappingInfo) -> bool """
        ...

    @property
    def IsParameter(self) -> bool:
        """ Get: IsParameter(self: ParameterMappingInfo) -> bool """
        ...

    @property
    def ParameterIndex(self) -> int:
        """ Get: ParameterIndex(self: ParameterMappingInfo) -> int """
        ...


    @staticmethod
    def Action(index:int) -> ParameterMappingInfo:
        """ Action(index: int) -> ParameterMappingInfo """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: ParameterMappingInfo, obj: object) -> bool """
        ...

    @staticmethod
    def Fixed(e:ConstantExpression) -> ParameterMappingInfo:
        """ Fixed(e: ConstantExpression) -> ParameterMappingInfo """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ParameterMappingInfo) -> int """
        ...

    @staticmethod
    def Parameter(index:int) -> ParameterMappingInfo:
        """ Parameter(index: int) -> ParameterMappingInfo """
        ...

    def ToString(self) -> str:
        """ ToString(self: ParameterMappingInfo) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ReflectedPropertyTracker(PropertyTracker): # skipped bases: <type 'object'>
    """ ReflectedPropertyTracker(property: PropertyInfo) """
    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: ReflectedPropertyTracker) -> Type """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ReflectedPropertyTracker) -> str """
        ...

    @property
    def Property(self) -> PropertyInfo:
        """ Get: Property(self: ReflectedPropertyTracker) -> PropertyInfo """
        ...


    def ToString(self) -> str:
        """ ToString(self: ReflectedPropertyTracker) -> str """
        ...

    def __new__(cls, property:PropertyInfo) -> Self:
        """ __new__(cls: type, property: PropertyInfo) """
        ...


class TopNamespaceTracker(IEnumerable, IMembersList, namespace#): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ TopNamespaceTracker(manager: ScriptDomainManager) """
    @property
    def DomainManager(self): # -> ScriptDomainManager
        """ Get: DomainManager(self: TopNamespaceTracker) -> ScriptDomainManager """
        ...


    def LoadAssembly(self, assem:Assembly) -> bool:
        """ LoadAssembly(self: TopNamespaceTracker, assem: Assembly) -> bool """
        ...

    def LoadNamespaces(self, *args): #cannot find CLR method
        """ LoadNamespaces(self: TopNamespaceTracker) """
        ...

    @staticmethod
    def PublishComTypes(interopAssembly:Assembly): # -> 
        """ PublishComTypes(interopAssembly: Assembly) """
        ...

    def TryGetPackage(self, name:str): # -> namespace#
        """ TryGetPackage(self: TopNamespaceTracker, name: str) -> namespace# """
        ...

    def TryGetPackageAny(self, name:str) -> MemberTracker:
        """ TryGetPackageAny(self: TopNamespaceTracker, name: str) -> MemberTracker """
        ...

    def TryGetPackageLazy(self, name:str) -> MemberTracker:
        """ TryGetPackageLazy(self: TopNamespaceTracker, name: str) -> MemberTracker """
        ...


class TrackerTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TrackerTypes, values: All (1535), Bound (1024), Constructor (1), Custom (512), Event (2), Field (4), Method (8), MethodGroup (128), Namespace (64), None (0), Property (16), Type (32), TypeGroup (256) """
    All: TrackerTypes = ...
    Bound: TrackerTypes = ...
    Constructor: TrackerTypes = ...
    Custom: TrackerTypes = ...
    Event: TrackerTypes = ...
    Field: TrackerTypes = ...
    Method: TrackerTypes = ...
    MethodGroup: TrackerTypes = ...
    Namespace: TrackerTypes = ...
    Property: TrackerTypes = ...
    Type: TrackerTypes = ...
    TypeGroup: TrackerTypes = ...
    value__ = ...


class TypeGroup(type-collision): # skipped bases: <type 'object'>
    """ no doc """
    def __call__(self, *args): #cannot find CLR method
        """ x.__call__(...) <==> x(...)x.__call__(...) <==> x(...) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


# variables with complex values

