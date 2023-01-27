# encoding: utf-8
# module Microsoft.Scripting.Actions.Calls calls itself Calls
# from Microsoft.Dynamic, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Scripting.Actions import (ActionBinder, CallSignature, 
    DefaultOverloadResolver, ErrorInfo)

from Microsoft.Scripting.Runtime import CallTypes

from System import Array, Enum, Type

from System.Collections import ICollection, IEnumerable, IList

from System.Collections.Generic import Dictionary

from System.Dynamic import BindingRestrictions, DynamicMetaObject

from System.Linq.Expressions import Expression

from System.Reflection import (CallingConventions, MethodAttributes, 
    MethodBase, ParameterInfo)

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ActualArguments: # skipped bases: <type 'object'>, <type 'object'>
    """ ActualArguments(args: IList[DynamicMetaObject], namedArgs: IList[DynamicMetaObject], argNames: IList[str], hiddenCount: int, collapsedCount: int, firstSplattedArg: int, splatIndex: int) """
    @property
    def ArgNames(self) -> IList:
        """ Get: ArgNames(self: ActualArguments) -> IList[str] """
        ...

    @property
    def Arguments(self) -> IList:
        """ Get: Arguments(self: ActualArguments) -> IList[DynamicMetaObject] """
        ...

    @property
    def CollapsedCount(self) -> int:
        """ Get: CollapsedCount(self: ActualArguments) -> int """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: ActualArguments) -> int """
        ...

    @property
    def FirstSplattedArg(self) -> int:
        """ Get: FirstSplattedArg(self: ActualArguments) -> int """
        ...

    @property
    def HiddenCount(self) -> int:
        """ Get: HiddenCount(self: ActualArguments) -> int """
        ...

    @property
    def NamedArguments(self) -> IList:
        """ Get: NamedArguments(self: ActualArguments) -> IList[DynamicMetaObject] """
        ...

    @property
    def SplatIndex(self) -> int:
        """ Get: SplatIndex(self: ActualArguments) -> int """
        ...

    @property
    def VisibleCount(self) -> int:
        """ Get: VisibleCount(self: ActualArguments) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ApplicableCandidate: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetParameter(self, argumentIndex:int) -> ParameterWrapper:
        """ GetParameter(self: ApplicableCandidate, argumentIndex: int) -> ParameterWrapper """
        ...

    def ToString(self) -> str:
        """ ToString(self: ApplicableCandidate) -> str """
        ...

    ArgumentBinding = ...
    Method = ...


class ArgBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ConsumedArgumentCount(self) -> int:
        """ Get: ConsumedArgumentCount(self: ArgBuilder) -> int """
        ...

    @property
    def ParameterInfo(self) -> ParameterInfo:
        """ Get: ParameterInfo(self: ArgBuilder) -> ParameterInfo """
        ...

    @property
    def Priority(self) -> int:
        """ Get: Priority(self: ArgBuilder) -> int """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: ArgBuilder) -> Type """
        ...


    def Clone(self, newType:ParameterInfo) -> ArgBuilder:
        """ Clone(self: ArgBuilder, newType: ParameterInfo) -> ArgBuilder """
        ...

    def ToExpression(self, *args): #cannot find CLR method
        """ ToExpression(self: ArgBuilder, resolver: OverloadResolver, args: RestrictedArguments, hasBeenUsed: Array[bool]) -> Expression """
        ...


class ArgumentBinding: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def PositionalArgCount(self) -> int:
        """ Get: PositionalArgCount(self: ArgumentBinding) -> int """
        ...


    def ArgumentToParameter(self, argumentIndex:int) -> int:
        """ ArgumentToParameter(self: ArgumentBinding, argumentIndex: int) -> int """
        ...


class BindingResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BindingResult, values: AmbiguousMatch (1), CallFailure (3), IncorrectArgumentCount (2), InvalidArguments (4), NoCallableMethod (5), Success (0) """
    AmbiguousMatch: BindingResult = ...
    CallFailure: BindingResult = ...
    IncorrectArgumentCount: BindingResult = ...
    InvalidArguments: BindingResult = ...
    NoCallableMethod: BindingResult = ...
    Success: BindingResult = ...
    value__ = ...


class BindingTarget: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ActualArgumentCount(self) -> int:
        """ Get: ActualArgumentCount(self: BindingTarget) -> int """
        ...

    @property
    def AmbiguousMatches(self) -> IEnumerable:
        """ Get: AmbiguousMatches(self: BindingTarget) -> IEnumerable[MethodCandidate] """
        ...

    @property
    def CallFailures(self) -> ICollection:
        """ Get: CallFailures(self: BindingTarget) -> ICollection[CallFailure] """
        ...

    @property
    def ExpectedArgumentCount(self) -> IList:
        """ Get: ExpectedArgumentCount(self: BindingTarget) -> IList[int] """
        ...

    @property
    def Method(self) -> MethodBase:
        """ Get: Method(self: BindingTarget) -> MethodBase """
        ...

    @property
    def MethodCandidate(self) -> MethodCandidate:
        """ Get: MethodCandidate(self: BindingTarget) -> MethodCandidate """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: BindingTarget) -> str """
        ...

    @property
    def NarrowingLevel(self) -> NarrowingLevel:
        """ Get: NarrowingLevel(self: BindingTarget) -> NarrowingLevel """
        ...

    @property
    def Overload(self) -> OverloadInfo:
        """ Get: Overload(self: BindingTarget) -> OverloadInfo """
        ...

    @property
    def RestrictedArguments(self) -> RestrictedArguments:
        """ Get: RestrictedArguments(self: BindingTarget) -> RestrictedArguments """
        ...

    @property
    def Result(self) -> BindingResult:
        """ Get: Result(self: BindingTarget) -> BindingResult """
        ...

    @property
    def ReturnType(self) -> Type:
        """ Get: ReturnType(self: BindingTarget) -> Type """
        ...

    @property
    def Success(self) -> bool:
        """ Get: Success(self: BindingTarget) -> bool """
        ...


    def MakeExpression(self) -> Expression:
        """ MakeExpression(self: BindingTarget) -> Expression """
        ...


class CallFailure: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Candidate(self) -> MethodCandidate:
        """ Get: Candidate(self: CallFailure) -> MethodCandidate """
        ...

    @property
    def ConversionResults(self) -> IList:
        """ Get: ConversionResults(self: CallFailure) -> IList[ConversionResult] """
        ...

    @property
    def KeywordArguments(self) -> IList:
        """ Get: KeywordArguments(self: CallFailure) -> IList[str] """
        ...

    @property
    def PositionalArguments(self) -> IList:
        """ Get: PositionalArguments(self: CallFailure) -> IList[int] """
        ...

    @property
    def Reason(self) -> CallFailureReason:
        """ Get: Reason(self: CallFailure) -> CallFailureReason """
        ...



class CallFailureReason(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CallFailureReason, values: ConversionFailure (1), DuplicateKeyword (3), None (0), TypeInference (4), UnassignableKeyword (2) """
    ConversionFailure: CallFailureReason = ...
    DuplicateKeyword: CallFailureReason = ...
    TypeInference: CallFailureReason = ...
    UnassignableKeyword: CallFailureReason = ...
    value__ = ...


class Candidate(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Candidate, values: Ambiguous (2), Equivalent (0), One (1), Two (-1) """
    Ambiguous: Candidate = ...
    Equivalent: Candidate = ...
    One: Candidate = ...
    Two: Candidate = ...
    value__ = ...


class ConversionResult: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Arg(self) -> object:
        """ Get: Arg(self: ConversionResult) -> object """
        ...

    @property
    def ArgType(self) -> Type:
        """ Get: ArgType(self: ConversionResult) -> Type """
        ...

    @property
    def Failed(self) -> bool:
        """ Get: Failed(self: ConversionResult) -> bool """
        ...

    @property
    def To(self) -> Type:
        """ Get: To(self: ConversionResult) -> Type """
        ...


    def GetArgumentTypeName(self, binder:ActionBinder) -> str:
        """ GetArgumentTypeName(self: ConversionResult, binder: ActionBinder) -> str """
        ...


class IInferableInvokable: # skipped bases: <type 'object'>
    """ no doc """
    def GetInferredType(self, delegateType:Type, parameterType:Type) -> InferenceResult:
        """ GetInferredType(self: IInferableInvokable, delegateType: Type, parameterType: Type) -> InferenceResult """
        ...


class InferenceResult: # skipped bases: <type 'object'>, <type 'object'>
    """ InferenceResult(type: Type, restrictions: BindingRestrictions) """
    @property
    def Restrictions(self) -> BindingRestrictions:
        """ Get: Restrictions(self: InferenceResult) -> BindingRestrictions """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: InferenceResult) -> Type """
        ...



class InstanceBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ InstanceBuilder(index: int) """
    @property
    def ConsumedArgumentCount(self) -> int:
        """ Get: ConsumedArgumentCount(self: InstanceBuilder) -> int """
        ...

    @property
    def HasValue(self) -> bool:
        """ Get: HasValue(self: InstanceBuilder) -> bool """
        ...


    def ToExpression(self, *args): #cannot find CLR method
        """ ToExpression(self: InstanceBuilder, method: MethodInfo, resolver: OverloadResolver, args: RestrictedArguments, hasBeenUsed: Array[bool]) -> (Expression, MethodInfo) """
        ...


class MethodCandidate: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Binder(self) -> ActionBinder:
        """ Get: Binder(self: MethodCandidate) -> ActionBinder """
        ...

    @property
    def HasParamsArray(self) -> bool:
        """ Get: HasParamsArray(self: MethodCandidate) -> bool """
        ...

    @property
    def HasParamsDictionary(self) -> bool:
        """ Get: HasParamsDictionary(self: MethodCandidate) -> bool """
        ...

    @property
    def Method(self) -> MethodBase:
        """ Get: Method(self: MethodCandidate) -> MethodBase """
        ...

    @property
    def Overload(self) -> OverloadInfo:
        """ Get: Overload(self: MethodCandidate) -> OverloadInfo """
        ...

    @property
    def ParamsArrayIndex(self) -> int:
        """ Get: ParamsArrayIndex(self: MethodCandidate) -> int """
        ...

    @property
    def Resolver(self) -> OverloadResolver:
        """ Get: Resolver(self: MethodCandidate) -> OverloadResolver """
        ...

    @property
    def ReturnType(self) -> Type:
        """ Get: ReturnType(self: MethodCandidate) -> Type """
        ...


    def GetParameters(self) -> IList:
        """ GetParameters(self: MethodCandidate) -> IList[ParameterWrapper] """
        ...

    def GetParameterTypes(self) -> Array:
        """ GetParameterTypes(self: MethodCandidate) -> Array[Type] """
        ...

    def GetVisibleParameterCount(self) -> int:
        """ GetVisibleParameterCount(self: MethodCandidate) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: MethodCandidate) -> str """
        ...


class NarrowingLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NarrowingLevel, values: All (4), None (0), One (1), Three (3), Two (2) """
    All: NarrowingLevel = ...
    One: NarrowingLevel = ...
    Three: NarrowingLevel = ...
    Two: NarrowingLevel = ...
    value__ = ...


class OverloadInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> MethodAttributes:
        """ Get: Attributes(self: OverloadInfo) -> MethodAttributes """
        ...

    @property
    def CallingConvention(self) -> CallingConventions:
        """ Get: CallingConvention(self: OverloadInfo) -> CallingConventions """
        ...

    @property
    def ContainsGenericParameters(self) -> bool:
        """ Get: ContainsGenericParameters(self: OverloadInfo) -> bool """
        ...

    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: OverloadInfo) -> Type """
        ...

    @property
    def GenericArguments(self) -> IList:
        """ Get: GenericArguments(self: OverloadInfo) -> IList[Type] """
        ...

    @property
    def IsAssembly(self) -> bool:
        """ Get: IsAssembly(self: OverloadInfo) -> bool """
        ...

    @property
    def IsConstructor(self) -> bool:
        """ Get: IsConstructor(self: OverloadInfo) -> bool """
        ...

    @property
    def IsExtension(self) -> bool:
        """ Get: IsExtension(self: OverloadInfo) -> bool """
        ...

    @property
    def IsFamily(self) -> bool:
        """ Get: IsFamily(self: OverloadInfo) -> bool """
        ...

    @property
    def IsFamilyAndAssembly(self) -> bool:
        """ Get: IsFamilyAndAssembly(self: OverloadInfo) -> bool """
        ...

    @property
    def IsFamilyOrAssembly(self) -> bool:
        """ Get: IsFamilyOrAssembly(self: OverloadInfo) -> bool """
        ...

    @property
    def IsFinal(self) -> bool:
        """ Get: IsFinal(self: OverloadInfo) -> bool """
        ...

    @property
    def IsGenericMethod(self) -> bool:
        """ Get: IsGenericMethod(self: OverloadInfo) -> bool """
        ...

    @property
    def IsGenericMethodDefinition(self) -> bool:
        """ Get: IsGenericMethodDefinition(self: OverloadInfo) -> bool """
        ...

    @property
    def IsInstanceFactory(self) -> bool:
        """ Get: IsInstanceFactory(self: OverloadInfo) -> bool """
        ...

    @property
    def IsPrivate(self) -> bool:
        """ Get: IsPrivate(self: OverloadInfo) -> bool """
        ...

    @property
    def IsProtected(self) -> bool:
        """ Get: IsProtected(self: OverloadInfo) -> bool """
        ...

    @property
    def IsPublic(self) -> bool:
        """ Get: IsPublic(self: OverloadInfo) -> bool """
        ...

    @property
    def IsSpecialName(self) -> bool:
        """ Get: IsSpecialName(self: OverloadInfo) -> bool """
        ...

    @property
    def IsStatic(self) -> bool:
        """ Get: IsStatic(self: OverloadInfo) -> bool """
        ...

    @property
    def IsVariadic(self) -> bool:
        """ Get: IsVariadic(self: OverloadInfo) -> bool """
        ...

    @property
    def IsVirtual(self) -> bool:
        """ Get: IsVirtual(self: OverloadInfo) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: OverloadInfo) -> str """
        ...

    @property
    def ParameterCount(self) -> int:
        """ Get: ParameterCount(self: OverloadInfo) -> int """
        ...

    @property
    def Parameters(self) -> IList:
        """ Get: Parameters(self: OverloadInfo) -> IList[ParameterInfo] """
        ...

    @property
    def ReflectionInfo(self) -> MethodBase:
        """ Get: ReflectionInfo(self: OverloadInfo) -> MethodBase """
        ...

    @property
    def ReturnParameter(self) -> ParameterInfo:
        """ Get: ReturnParameter(self: OverloadInfo) -> ParameterInfo """
        ...

    @property
    def ReturnType(self) -> Type:
        """ Get: ReturnType(self: OverloadInfo) -> Type """
        ...


    def IsParamArray(self, parameterIndex:int) -> bool:
        """ IsParamArray(self: OverloadInfo, parameterIndex: int) -> bool """
        ...

    def IsParamDictionary(self, parameterIndex:int) -> bool:
        """ IsParamDictionary(self: OverloadInfo, parameterIndex: int) -> bool """
        ...

    def MakeGenericMethod(self, genericArguments:Array) -> OverloadInfo:
        """ MakeGenericMethod(self: OverloadInfo, genericArguments: Array[Type]) -> OverloadInfo """
        ...

    def ProhibitsNull(self, parameterIndex:int) -> bool:
        """ ProhibitsNull(self: OverloadInfo, parameterIndex: int) -> bool """
        ...

    def ProhibitsNullItems(self, parameterIndex:int) -> bool:
        """ ProhibitsNullItems(self: OverloadInfo, parameterIndex: int) -> bool """
        ...


class OverloadResolver: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Binder(self) -> ActionBinder:
        """ Get: Binder(self: OverloadResolver) -> ActionBinder """
        ...

    @property
    def MaxAccessedCollapsedArg(self) -> int:
        """ Get: MaxAccessedCollapsedArg(self: OverloadResolver) -> int """
        ...


    def AllowByKeywordArgument(self, *args): #cannot find CLR method
        """ AllowByKeywordArgument(self: OverloadResolver, method: OverloadInfo, parameter: ParameterInfo) -> bool """
        ...

    def AllowKeywordArgumentSetting(self, *args): #cannot find CLR method
        """ AllowKeywordArgumentSetting(self: OverloadResolver, method: MethodBase) -> bool """
        ...

    def AllowMemberInitialization(self, *args): #cannot find CLR method
        """ AllowMemberInitialization(self: OverloadResolver, method: OverloadInfo) -> bool """
        ...

    def BindToUnexpandedParams(self, *args): #cannot find CLR method
        """ BindToUnexpandedParams(self: OverloadResolver, candidate: MethodCandidate) -> bool """
        ...

    def CanConvertFrom(self, *__args) -> bool:
        """
        CanConvertFrom(self: OverloadResolver, parameter1: ParameterWrapper, parameter2: ParameterWrapper) -> bool
        CanConvertFrom(self: OverloadResolver, fromType: Type, fromArgument: DynamicMetaObject, toParameter: ParameterWrapper, level: NarrowingLevel) -> bool
        """
        ...

    def CompareEquivalentCandidates(self, *args): #cannot find CLR method
        """ CompareEquivalentCandidates(self: OverloadResolver, one: ApplicableCandidate, two: ApplicableCandidate) -> Candidate """
        ...

    def Convert(self, metaObject:DynamicMetaObject, restrictedType:Type, info:ParameterInfo, toType:Type) -> Expression:
        """ Convert(self: OverloadResolver, metaObject: DynamicMetaObject, restrictedType: Type, info: ParameterInfo, toType: Type) -> Expression """
        ...

    def CreateActualArguments(self, *args): #cannot find CLR method
        """ CreateActualArguments(self: OverloadResolver, namedArgs: IList[DynamicMetaObject], argNames: IList[str], preSplatLimit: int, postSplatLimit: int) -> ActualArguments """
        ...

    def GetActualArguments(self) -> ActualArguments:
        """ GetActualArguments(self: OverloadResolver) -> ActualArguments """
        ...

    def GetByRefArrayExpression(self, *args): #cannot find CLR method
        """ GetByRefArrayExpression(self: OverloadResolver, argumentArrayExpression: Expression) -> Expression """
        ...

    def GetCollapsedArgsCondition(self) -> Expression:
        """ GetCollapsedArgsCondition(self: OverloadResolver) -> Expression """
        ...

    def GetDynamicConversion(self, value:Expression, type:Type) -> Expression:
        """ GetDynamicConversion(self: OverloadResolver, value: Expression, type: Type) -> Expression """
        ...

    def GetGenericInferenceType(self, dynamicObject:DynamicMetaObject) -> Type:
        """ GetGenericInferenceType(self: OverloadResolver, dynamicObject: DynamicMetaObject) -> Type """
        ...

    def GetNamedArguments(self, *args): #cannot find CLR method
        """ GetNamedArguments(self: OverloadResolver) -> (IList[DynamicMetaObject], IList[str]) """
        ...

    def GetSplattedExpression(self, *args): #cannot find CLR method
        """ GetSplattedExpression(self: OverloadResolver) -> Expression """
        ...

    def GetSplattedItem(self, *args): #cannot find CLR method
        """ GetSplattedItem(self: OverloadResolver, index: int) -> object """
        ...

    def MakeInvalidParametersError(self, target:BindingTarget) -> ErrorInfo:
        """ MakeInvalidParametersError(self: OverloadResolver, target: BindingTarget) -> ErrorInfo """
        ...

    def MapSpecialParameters(self, *args): #cannot find CLR method
        """ MapSpecialParameters(self: OverloadResolver, mapping: ParameterMapping) -> BitArray """
        ...

    def ParametersEquivalent(self, parameter1:ParameterWrapper, parameter2:ParameterWrapper) -> bool:
        """ ParametersEquivalent(self: OverloadResolver, parameter1: ParameterWrapper, parameter2: ParameterWrapper) -> bool """
        ...

    def PreferConvert(self, t1:Type, t2:Type) -> Candidate:
        """ PreferConvert(self: OverloadResolver, t1: Type, t2: Type) -> Candidate """
        ...

    def ResolveOverload(self, methodName:str, methods:IList, minLevel:NarrowingLevel, maxLevel:NarrowingLevel) -> BindingTarget:
        """
        ResolveOverload(self: OverloadResolver, methodName: str, methods: IList[MethodBase], minLevel: NarrowingLevel, maxLevel: NarrowingLevel) -> BindingTarget
        ResolveOverload(self: OverloadResolver, methodName: str, methods: IList[OverloadInfo], minLevel: NarrowingLevel, maxLevel: NarrowingLevel) -> BindingTarget
        """
        ...

    def SelectBestConversionFor(self, arg:DynamicMetaObject, candidateOne:ParameterWrapper, candidateTwo:ParameterWrapper, level:NarrowingLevel) -> Candidate:
        """ SelectBestConversionFor(self: OverloadResolver, arg: DynamicMetaObject, candidateOne: ParameterWrapper, candidateTwo: ParameterWrapper, level: NarrowingLevel) -> Candidate """
        ...

    def ToString(self) -> str:
        """ ToString(self: OverloadResolver) -> str """
        ...


class OverloadResolverFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateOverloadResolver(self, args:IList, signature:CallSignature, callType:CallTypes) -> DefaultOverloadResolver:
        """ CreateOverloadResolver(self: OverloadResolverFactory, args: IList[DynamicMetaObject], signature: CallSignature, callType: CallTypes) -> DefaultOverloadResolver """
        ...


class ParameterBindingFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ParameterBindingFlags, values: IsHidden (16), IsParamArray (4), IsParamDictionary (8), None (0), ProhibitNull (1), ProhibitNullItems (2) """
    IsHidden: ParameterBindingFlags = ...
    IsParamArray: ParameterBindingFlags = ...
    IsParamDictionary: ParameterBindingFlags = ...
    ProhibitNull: ParameterBindingFlags = ...
    ProhibitNullItems: ParameterBindingFlags = ...
    value__ = ...


class ParameterMapping: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ArgIndex(self) -> int:
        """ Get: ArgIndex(self: ParameterMapping) -> int """
        ...

    @property
    def Method(self) -> MethodBase:
        """ Get: Method(self: ParameterMapping) -> MethodBase """
        ...

    @property
    def Overload(self) -> OverloadInfo:
        """ Get: Overload(self: ParameterMapping) -> OverloadInfo """
        ...

    @property
    def ParameterInfos(self) -> Array:
        """ Get: ParameterInfos(self: ParameterMapping) -> Array[ParameterInfo] """
        ...


    def AddBuilder(self, builder:ArgBuilder): # -> 
        """ AddBuilder(self: ParameterMapping, builder: ArgBuilder) """
        ...

    def AddInstanceBuilder(self, builder:InstanceBuilder): # -> 
        """ AddInstanceBuilder(self: ParameterMapping, builder: InstanceBuilder) """
        ...

    def AddParameter(self, parameter:ParameterWrapper): # -> 
        """ AddParameter(self: ParameterMapping, parameter: ParameterWrapper) """
        ...

    def MapParameter(self, pi:ParameterInfo): # -> 
        """ MapParameter(self: ParameterMapping, pi: ParameterInfo) """
        ...


class ParameterWrapper: # skipped bases: <type 'object'>, <type 'object'>
    """
    ParameterWrapper(type: Type, name: str, prohibitNull: bool)
    ParameterWrapper(info: ParameterInfo, type: Type, name: str, prohibitNull: bool, isParams: bool, isParamsDict: bool, isHidden: bool)
    ParameterWrapper(info: ParameterInfo, type: Type, name: str, flags: ParameterBindingFlags)
    """
    @property
    def Flags(self) -> ParameterBindingFlags:
        """ Get: Flags(self: ParameterWrapper) -> ParameterBindingFlags """
        ...

    @property
    def IsByRef(self) -> bool:
        """ Get: IsByRef(self: ParameterWrapper) -> bool """
        ...

    @property
    def IsHidden(self) -> bool:
        """ Get: IsHidden(self: ParameterWrapper) -> bool """
        ...

    @property
    def IsParamsArray(self) -> bool:
        """ Get: IsParamsArray(self: ParameterWrapper) -> bool """
        ...

    @property
    def IsParamsDict(self) -> bool:
        """ Get: IsParamsDict(self: ParameterWrapper) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ParameterWrapper) -> str """
        ...

    @property
    def ParameterInfo(self) -> ParameterInfo:
        """ Get: ParameterInfo(self: ParameterWrapper) -> ParameterInfo """
        ...

    @property
    def ProhibitNull(self) -> bool:
        """ Get: ProhibitNull(self: ParameterWrapper) -> bool """
        ...

    @property
    def ProhibitNullItems(self) -> bool:
        """ Get: ProhibitNullItems(self: ParameterWrapper) -> bool """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: ParameterWrapper) -> Type """
        ...


    def Clone(self, name:str) -> ParameterWrapper:
        """ Clone(self: ParameterWrapper, name: str) -> ParameterWrapper """
        ...


class ReflectionOverloadInfo(OverloadInfo): # skipped bases: <type 'object'>
    """ ReflectionOverloadInfo(method: MethodBase) """
    @staticmethod
    def CreateArray(methods:Array) -> Array:
        """ CreateArray(methods: Array[MethodBase]) -> Array[OverloadInfo] """
        ...

    def __new__(cls, method:MethodBase) -> Self:
        """ __new__(cls: type, method: MethodBase) """
        ...


class RestrictedArguments: # skipped bases: <type 'object'>, <type 'object'>
    """ RestrictedArguments(objects: Array[DynamicMetaObject], types: Array[Type], hasUntypedRestrictions: bool) """
    @property
    def HasUntypedRestrictions(self) -> bool:
        """ Get: HasUntypedRestrictions(self: RestrictedArguments) -> bool """
        ...

    @property
    def Length(self) -> int:
        """ Get: Length(self: RestrictedArguments) -> int """
        ...


    def GetAllRestrictions(self) -> BindingRestrictions:
        """ GetAllRestrictions(self: RestrictedArguments) -> BindingRestrictions """
        ...

    def GetObject(self, i:int) -> DynamicMetaObject:
        """ GetObject(self: RestrictedArguments, i: int) -> DynamicMetaObject """
        ...

    def GetObjects(self) -> IList:
        """ GetObjects(self: RestrictedArguments) -> IList[DynamicMetaObject] """
        ...

    def GetType(self, i:int = ...) -> Type:
        """ GetType(self: RestrictedArguments, i: int) -> Type """
        ...

    def GetTypes(self) -> IList:
        """ GetTypes(self: RestrictedArguments) -> IList[Type] """
        ...


class SimpleArgBuilder(ArgBuilder): # skipped bases: <type 'object'>
    """
    SimpleArgBuilder(parameterType: Type, index: int, isParams: bool, isParamsDict: bool)
    SimpleArgBuilder(info: ParameterInfo, index: int)
    SimpleArgBuilder(info: ParameterInfo, parameterType: Type, index: int, isParams: bool, isParamsDict: bool)
    """
    @property
    def Index(self) -> int:
        """ Get: Index(self: SimpleArgBuilder) -> int """
        ...

    @property
    def IsParamsArray(self) -> bool:
        """ Get: IsParamsArray(self: SimpleArgBuilder) -> bool """
        ...

    @property
    def IsParamsDict(self) -> bool:
        """ Get: IsParamsDict(self: SimpleArgBuilder) -> bool """
        ...


    def Copy(self, *args): #cannot find CLR method
        """ Copy(self: SimpleArgBuilder, newIndex: int) -> SimpleArgBuilder """
        ...


class TypeInferer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetInferedType(genericParameter:Type, parameterType:Type, inputType:Type, argType:Type, binding:Dictionary) -> Type:
        """ GetInferedType(genericParameter: Type, parameterType: Type, inputType: Type, argType: Type, binding: Dictionary[Type, Type]) -> Type """
        ...

    __all__: list = ...


