# encoding: utf-8
# module Microsoft.Scripting.Hosting calls itself Hosting
# from Microsoft.Dynamic, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1, Microsoft.Scripting, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1
# by generator 1.145
""" no doc """
from __future__ import annotations
from Babel import TokenInfo

from Microsoft.Scripting import (CompilerOptions, ErrorSink, 
    PlatformAdaptationLayer, ScriptCodeParseResult, Severity, SourceCodeKind, 
    SourceCodeReader, SourceLocation, SourceSpan)

from System import AppDomain, Array, Enum, MarshalByRefObject, Type, Version

from System.CodeDom import CodeObject

from System.Collections import ICollection, IDictionary, IEnumerable, IList

from System.Dynamic import IDynamicMetaObjectProvider

from System.IO import Stream, TextReader, TextWriter

from System.Linq.Expressions import ExpressionType

from System.Reflection import Assembly

from System.Runtime.Remoting import ObjectHandle

from System.Text import Encoding

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (MemberKind, ParameterDoc, 
    ParameterFlags, ScriptEngine, ScriptRuntime, ScriptRuntimeSetup, 
    ScriptScope, ScriptSource, T, TService, field#)
"""

# no functions
# classes

class CompiledCode(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DefaultScope(self): # -> ScriptScope
        """ Get: DefaultScope(self: CompiledCode) -> ScriptScope """
        ...

    @property
    def Engine(self): # -> ScriptEngine
        """ Get: Engine(self: CompiledCode) -> ScriptEngine """
        ...


    def Execute(self, scope = ...) -> object: # Not found arg types: {'scope': 'ScriptScope'}
        """
        Execute(self: CompiledCode) -> object
        Execute(self: CompiledCode, scope: ScriptScope) -> object
        Execute[T](self: CompiledCode) -> T
        Execute[T](self: CompiledCode, scope: ScriptScope) -> T
        """
        ...

    def ExecuteAndWrap(self, *__args) -> ObjectHandle: # Not found arg types: {'*__args': 'ScriptScope'}
        """
        ExecuteAndWrap(self: CompiledCode) -> ObjectHandle
        ExecuteAndWrap(self: CompiledCode, scope: ScriptScope) -> ObjectHandle
        ExecuteAndWrap(self: CompiledCode) -> (ObjectHandle, ObjectHandle)
        ExecuteAndWrap(self: CompiledCode, scope: ScriptScope) -> (ObjectHandle, ObjectHandle)
        """
        ...


class DocumentationOperations(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    def GetMembers(self, value:object) -> ICollection:
        """
        GetMembers(self: DocumentationOperations, value: object) -> ICollection[MemberDoc]
        GetMembers(self: DocumentationOperations, value: ObjectHandle) -> ICollection[MemberDoc]
        """
        ...

    def GetOverloads(self, value:object) -> ICollection:
        """
        GetOverloads(self: DocumentationOperations, value: object) -> ICollection[OverloadDoc]
        GetOverloads(self: DocumentationOperations, value: ObjectHandle) -> ICollection[OverloadDoc]
        """
        ...


class ErrorListener(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    def ErrorReported(self, source, message:str, span:SourceSpan, errorCode:int, severity:Severity): # ->  # Not found arg types: {'source': 'ScriptSource'}
        """ ErrorReported(self: ErrorListener, source: ScriptSource, message: str, span: SourceSpan, errorCode: int, severity: Severity) """
        ...


class ErrorSinkProxyListener(ErrorListener): # skipped bases: <type 'object'>
    """ ErrorSinkProxyListener(errorSink: ErrorSink) """
    def __new__(cls, errorSink:ErrorSink) -> Self:
        """ __new__(cls: type, errorSink: ErrorSink) """
        ...


class ExceptionOperations(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    def FormatException(self, exception:Exception) -> str:
        """
        FormatException(self: ExceptionOperations, exception: Exception) -> str
        FormatException(self: ExceptionOperations, exception: ObjectHandle) -> str
        """
        ...

    def GetExceptionMessage(self, exception, message, errorTypeName) -> Tuple_[str, str]:
        """
        GetExceptionMessage(self: ExceptionOperations, exception: Exception) -> (str, str)
        GetExceptionMessage(self: ExceptionOperations, exception: ObjectHandle) -> (str, str)
        """
        ...

    def GetStackFrames(self, exception:Exception) -> IList:
        """
        GetStackFrames(self: ExceptionOperations, exception: Exception) -> IList[DynamicStackFrame]
        GetStackFrames(self: ExceptionOperations, exception: ObjectHandle) -> IList[DynamicStackFrame]
        """
        ...

    def HandleException(self, exception:Exception) -> bool:
        """
        HandleException(self: ExceptionOperations, exception: Exception) -> bool
        HandleException(self: ExceptionOperations, exception: ObjectHandle) -> bool
        """
        ...


class LanguageSetup: # skipped bases: <type 'object'>, <type 'object'>
    """
    LanguageSetup(typeName: str)
    LanguageSetup(typeName: str, displayName: str)
    LanguageSetup(typeName: str, displayName: str, names: IEnumerable[str], fileExtensions: IEnumerable[str])
    """
    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: LanguageSetup) -> str
        Set: DisplayName(self: LanguageSetup) = value
        """
        ...

    @property
    def ExceptionDetail(self) -> bool:
        """
        Get: ExceptionDetail(self: LanguageSetup) -> bool
        Set: ExceptionDetail(self: LanguageSetup) = value
        """
        ...

    @property
    def FileExtensions(self) -> IList:
        """ Get: FileExtensions(self: LanguageSetup) -> IList[str] """
        ...

    @property
    def InterpretedMode(self) -> bool:
        """
        Get: InterpretedMode(self: LanguageSetup) -> bool
        Set: InterpretedMode(self: LanguageSetup) = value
        """
        ...

    @property
    def Names(self) -> IList:
        """ Get: Names(self: LanguageSetup) -> IList[str] """
        ...

    @property
    def NoAdaptiveCompilation(self) -> bool:
        """
        Get: NoAdaptiveCompilation(self: LanguageSetup) -> bool
        Set: NoAdaptiveCompilation(self: LanguageSetup) = value
        """
        ...

    @property
    def Options(self) -> IDictionary:
        """ Get: Options(self: LanguageSetup) -> IDictionary[str, object] """
        ...

    @property
    def PerfStats(self) -> bool:
        """
        Get: PerfStats(self: LanguageSetup) -> bool
        Set: PerfStats(self: LanguageSetup) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: LanguageSetup) -> str
        Set: TypeName(self: LanguageSetup) = value
        """
        ...


    def GetOption(self, name:str, defaultValue): # -> T # Not found arg types: {'defaultValue': 'T'}
        """ GetOption[T](self: LanguageSetup, name: str, defaultValue: T) -> T """
        ...


class MemberDoc: # skipped bases: <type 'object'>, <type 'object'>
    """ MemberDoc(name: str, kind: MemberKind) """
    @property
    def Kind(self): # -> MemberKind
        """ Get: Kind(self: MemberDoc) -> MemberKind """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MemberDoc) -> str """
        ...



class MemberKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MemberKind, values: Class (1), Constant (9), Delegate (2), Enum (3), EnumMember (10), Event (4), Field (5), Function (6), Instance (11), Method (12), Module (7), Namespace (13), None (0), Property (8) """
    Class: MemberKind = ...
    Constant: MemberKind = ...
    Delegate: MemberKind = ...
    Enum: MemberKind = ...
    EnumMember: MemberKind = ...
    Event: MemberKind = ...
    Field: MemberKind = ...
    Function: MemberKind = ...
    Instance: MemberKind = ...
    Method: MemberKind = ...
    Module: MemberKind = ...
    Namespace: MemberKind = ...
    Property: MemberKind = ...
    value__ = ...


class ObjectOperations(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Engine(self): # -> ScriptEngine
        """ Get: Engine(self: ObjectOperations) -> ScriptEngine """
        ...


    def Add(self, self, other:object) -> object:
        """
        Add(self: ObjectOperations, self: object, other: object) -> object
        Add(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> ObjectHandle
        """
        ...

    def BitwiseAnd(self, self, other:object) -> object:
        """
        BitwiseAnd(self: ObjectOperations, self: object, other: object) -> object
        BitwiseAnd(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> ObjectHandle
        """
        ...

    def BitwiseOr(self, self, other:object) -> object:
        """
        BitwiseOr(self: ObjectOperations, self: object, other: object) -> object
        BitwiseOr(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> ObjectHandle
        """
        ...

    def ContainsMember(self, obj:object, name:str, ignoreCase:bool = ...) -> bool:
        """
        ContainsMember(self: ObjectOperations, obj: object, name: str) -> bool
        ContainsMember(self: ObjectOperations, obj: object, name: str, ignoreCase: bool) -> bool
        ContainsMember(self: ObjectOperations, obj: ObjectHandle, name: str) -> bool
        """
        ...

    def ConvertTo(self, obj:object, type:Type = ...) -> object:
        """
        ConvertTo[T](self: ObjectOperations, obj: object) -> T
        ConvertTo(self: ObjectOperations, obj: object, type: Type) -> object
        ConvertTo[T](self: ObjectOperations, obj: ObjectHandle) -> ObjectHandle
        ConvertTo(self: ObjectOperations, obj: ObjectHandle, type: Type) -> ObjectHandle
        """
        ...

    def CreateInstance(self, obj:object, parameters:Array) -> object:
        """
        CreateInstance(self: ObjectOperations, obj: object, *parameters: Array[object]) -> object
        CreateInstance(self: ObjectOperations, obj: ObjectHandle, *parameters: Array[ObjectHandle]) -> ObjectHandle
        CreateInstance(self: ObjectOperations, obj: ObjectHandle, *parameters: Array[object]) -> ObjectHandle
        """
        ...

    def Divide(self, self, other:object) -> object:
        """
        Divide(self: ObjectOperations, self: object, other: object) -> object
        Divide(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> ObjectHandle
        """
        ...

    def DoOperation(self, *__args) -> object:
        """
        DoOperation(self: ObjectOperations, operation: ExpressionType, target: object) -> object
        DoOperation[(TTarget, TResult)](self: ObjectOperations, operation: ExpressionType, target: TTarget) -> TResult
        DoOperation(self: ObjectOperations, operation: ExpressionType, target: object, other: object) -> object
        DoOperation[(TTarget, TOther, TResult)](self: ObjectOperations, operation: ExpressionType, target: TTarget, other: TOther) -> TResult
        DoOperation(self: ObjectOperations, op: ExpressionType, target: ObjectHandle) -> ObjectHandle
        DoOperation(self: ObjectOperations, op: ExpressionType, target: ObjectHandle, other: ObjectHandle) -> ObjectHandle
        """
        ...

    def Equal(self, self, other:object) -> bool:
        """
        Equal(self: ObjectOperations, self: object, other: object) -> bool
        Equal(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> bool
        """
        ...

    def ExclusiveOr(self, self, other:object) -> object:
        """
        ExclusiveOr(self: ObjectOperations, self: object, other: object) -> object
        ExclusiveOr(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> ObjectHandle
        """
        ...

    def ExplicitConvertTo(self, obj:object, type:Type = ...) -> object:
        """
        ExplicitConvertTo[T](self: ObjectOperations, obj: object) -> T
        ExplicitConvertTo(self: ObjectOperations, obj: object, type: Type) -> object
        ExplicitConvertTo[T](self: ObjectOperations, obj: ObjectHandle) -> ObjectHandle
        ExplicitConvertTo(self: ObjectOperations, obj: ObjectHandle, type: Type) -> ObjectHandle
        """
        ...

    def Format(self, obj:object) -> str:
        """
        Format(self: ObjectOperations, obj: object) -> str
        Format(self: ObjectOperations, obj: ObjectHandle) -> str
        """
        ...

    def GetCallSignatures(self, obj:object) -> IList:
        """
        GetCallSignatures(self: ObjectOperations, obj: object) -> IList[str]
        GetCallSignatures(self: ObjectOperations, obj: ObjectHandle) -> IList[str]
        """
        ...

    def GetCodeRepresentation(self, obj:object) -> str:
        """ GetCodeRepresentation(self: ObjectOperations, obj: object) -> str """
        ...

    def GetDocumentation(self, obj:object) -> str:
        """
        GetDocumentation(self: ObjectOperations, obj: object) -> str
        GetDocumentation(self: ObjectOperations, obj: ObjectHandle) -> str
        """
        ...

    def GetMember(self, obj:object, name:str, ignoreCase:bool = ...) -> object:
        """
        GetMember(self: ObjectOperations, obj: object, name: str) -> object
        GetMember[T](self: ObjectOperations, obj: object, name: str) -> T
        GetMember(self: ObjectOperations, obj: object, name: str, ignoreCase: bool) -> object
        GetMember[T](self: ObjectOperations, obj: object, name: str, ignoreCase: bool) -> T
        GetMember(self: ObjectOperations, obj: ObjectHandle, name: str) -> ObjectHandle
        GetMember[T](self: ObjectOperations, obj: ObjectHandle, name: str) -> T
        """
        ...

    def GetMemberNames(self, obj:object) -> IList:
        """
        GetMemberNames(self: ObjectOperations, obj: object) -> IList[str]
        GetMemberNames(self: ObjectOperations, obj: ObjectHandle) -> IList[str]
        """
        ...

    def GreaterThan(self, self, other:object) -> bool:
        """
        GreaterThan(self: ObjectOperations, self: object, other: object) -> bool
        GreaterThan(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> bool
        """
        ...

    def GreaterThanOrEqual(self, self, other:object) -> bool:
        """
        GreaterThanOrEqual(self: ObjectOperations, self: object, other: object) -> bool
        GreaterThanOrEqual(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> bool
        """
        ...

    def ImplicitConvertTo(self, obj:object, type:Type = ...) -> object:
        """
        ImplicitConvertTo[T](self: ObjectOperations, obj: object) -> T
        ImplicitConvertTo(self: ObjectOperations, obj: object, type: Type) -> object
        ImplicitConvertTo[T](self: ObjectOperations, obj: ObjectHandle) -> ObjectHandle
        ImplicitConvertTo(self: ObjectOperations, obj: ObjectHandle, type: Type) -> ObjectHandle
        """
        ...

    def Invoke(self, obj:object, parameters:Array) -> object:
        """
        Invoke(self: ObjectOperations, obj: object, *parameters: Array[object]) -> object
        Invoke(self: ObjectOperations, obj: ObjectHandle, *parameters: Array[ObjectHandle]) -> ObjectHandle
        Invoke(self: ObjectOperations, obj: ObjectHandle, *parameters: Array[object]) -> ObjectHandle
        """
        ...

    def InvokeMember(self, obj:object, memberName:str, parameters:Array) -> object:
        """ InvokeMember(self: ObjectOperations, obj: object, memberName: str, *parameters: Array[object]) -> object """
        ...

    def IsCallable(self, obj:object) -> bool:
        """
        IsCallable(self: ObjectOperations, obj: object) -> bool
        IsCallable(self: ObjectOperations, obj: ObjectHandle) -> bool
        """
        ...

    def LeftShift(self, self, other:object) -> object:
        """
        LeftShift(self: ObjectOperations, self: object, other: object) -> object
        LeftShift(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> ObjectHandle
        """
        ...

    def LessThan(self, self, other:object) -> bool:
        """
        LessThan(self: ObjectOperations, self: object, other: object) -> bool
        LessThan(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> bool
        """
        ...

    def LessThanOrEqual(self, self, other:object) -> bool:
        """
        LessThanOrEqual(self: ObjectOperations, self: object, other: object) -> bool
        LessThanOrEqual(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> bool
        """
        ...

    def Modulo(self, self, other:object) -> object:
        """
        Modulo(self: ObjectOperations, self: object, other: object) -> object
        Modulo(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> ObjectHandle
        """
        ...

    def Multiply(self, self, other:object) -> object:
        """
        Multiply(self: ObjectOperations, self: object, other: object) -> object
        Multiply(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> ObjectHandle
        """
        ...

    def NotEqual(self, self, other:object) -> bool:
        """
        NotEqual(self: ObjectOperations, self: object, other: object) -> bool
        NotEqual(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> bool
        """
        ...

    def Power(self, self, other:object) -> object:
        """
        Power(self: ObjectOperations, self: object, other: object) -> object
        Power(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> ObjectHandle
        """
        ...

    def RemoveMember(self, obj:object, name:str, ignoreCase:bool = ...): # -> 
        """ RemoveMember(self: ObjectOperations, obj: object, name: str)RemoveMember(self: ObjectOperations, obj: object, name: str, ignoreCase: bool)RemoveMember(self: ObjectOperations, obj: ObjectHandle, name: str) """
        ...

    def RightShift(self, self, other:object) -> object:
        """
        RightShift(self: ObjectOperations, self: object, other: object) -> object
        RightShift(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> ObjectHandle
        """
        ...

    def SetMember(self, obj:object, name:str, value:object, ignoreCase:bool = ...): # -> 
        """ SetMember(self: ObjectOperations, obj: object, name: str, value: object)SetMember[T](self: ObjectOperations, obj: object, name: str, value: T)SetMember(self: ObjectOperations, obj: object, name: str, value: object, ignoreCase: bool)SetMember[T](self: ObjectOperations, obj: object, name: str, value: T, ignoreCase: bool)SetMember(self: ObjectOperations, obj: ObjectHandle, name: str, value: ObjectHandle)SetMember[T](self: ObjectOperations, obj: ObjectHandle, name: str, value: T) """
        ...

    def Subtract(self, self, other:object) -> object:
        """
        Subtract(self: ObjectOperations, self: object, other: object) -> object
        Subtract(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> ObjectHandle
        """
        ...

    def TryConvertTo(self, obj:object, *__args:Type) -> Tuple_[bool, object]:
        """
        TryConvertTo[T](self: ObjectOperations, obj: object) -> (bool, T)
        TryConvertTo(self: ObjectOperations, obj: object, type: Type) -> (bool, object)
        TryConvertTo[T](self: ObjectOperations, obj: ObjectHandle) -> (bool, ObjectHandle)
        TryConvertTo(self: ObjectOperations, obj: ObjectHandle, type: Type) -> (bool, ObjectHandle)
        """
        ...

    def TryExplicitConvertTo(self, obj:object, *__args:Type) -> Tuple_[bool, object]:
        """
        TryExplicitConvertTo[T](self: ObjectOperations, obj: object) -> (bool, T)
        TryExplicitConvertTo(self: ObjectOperations, obj: object, type: Type) -> (bool, object)
        TryExplicitConvertTo[T](self: ObjectOperations, obj: ObjectHandle) -> (bool, ObjectHandle)
        TryExplicitConvertTo(self: ObjectOperations, obj: ObjectHandle, type: Type) -> (bool, ObjectHandle)
        """
        ...

    def TryGetMember(self, obj:object, name:str, *__args:bool) -> Tuple_[bool, object]:
        """
        TryGetMember(self: ObjectOperations, obj: object, name: str) -> (bool, object)
        TryGetMember(self: ObjectOperations, obj: object, name: str, ignoreCase: bool) -> (bool, object)
        TryGetMember(self: ObjectOperations, obj: ObjectHandle, name: str) -> (bool, ObjectHandle)
        """
        ...

    def TryImplicitConvertTo(self, obj:object, *__args:Type) -> Tuple_[bool, object]:
        """
        TryImplicitConvertTo[T](self: ObjectOperations, obj: object) -> (bool, T)
        TryImplicitConvertTo(self: ObjectOperations, obj: object, type: Type) -> (bool, object)
        TryImplicitConvertTo[T](self: ObjectOperations, obj: ObjectHandle) -> (bool, ObjectHandle)
        TryImplicitConvertTo(self: ObjectOperations, obj: ObjectHandle, type: Type) -> (bool, ObjectHandle)
        """
        ...

    def Unwrap(self, obj:ObjectHandle): # -> T
        """ Unwrap[T](self: ObjectOperations, obj: ObjectHandle) -> T """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __and__(self, *args): #cannot find CLR method
        """
        __and__(self: ObjectOperations, self: object, other: object) -> object
        __and__(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> ObjectHandle
        """
        ...

    def __dir__(self, *args): #cannot find CLR method
        """
        GetMemberNames(self: ObjectOperations, obj: object) -> IList[str]
        GetMemberNames(self: ObjectOperations, obj: ObjectHandle) -> IList[str]
        """
        ...

    def __div__(self, *args): #cannot find CLR method
        """ x.__div__(y) <==> x/yx.__div__(y) <==> x/y """
        ...

    def __ge__(self, *args): #cannot find CLR method
        ...

    def __gt__(self, *args): #cannot find CLR method
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

    def __or__(self, *args): #cannot find CLR method
        """
        __or__(self: ObjectOperations, self: object, other: object) -> object
        __or__(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> ObjectHandle
        """
        ...

    def __pow__(self, *args): #cannot find CLR method
        """ x.__pow__(y[, z]) <==> pow(x, y[, z])x.__pow__(y[, z]) <==> pow(x, y[, z]) """
        ...

    def __rshift__(self, *args): #cannot find CLR method
        """ x.__rshift__(y) <==> x>>yx.__rshift__(y) <==> x>>y """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        ...

    def __xor__(self, *args): #cannot find CLR method
        """
        __xor__(self: ObjectOperations, self: object, other: object) -> object
        __xor__(self: ObjectOperations, self: ObjectHandle, other: ObjectHandle) -> ObjectHandle
        """
        ...


class OverloadDoc: # skipped bases: <type 'object'>, <type 'object'>
    """
    OverloadDoc(name: str, documentation: str, parameters: ICollection[ParameterDoc])
    OverloadDoc(name: str, documentation: str, parameters: ICollection[ParameterDoc], returnParameter: ParameterDoc)
    """
    @property
    def Documentation(self) -> str:
        """ Get: Documentation(self: OverloadDoc) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: OverloadDoc) -> str """
        ...

    @property
    def Parameters(self) -> ICollection:
        """ Get: Parameters(self: OverloadDoc) -> ICollection[ParameterDoc] """
        ...

    @property
    def ReturnParameter(self): # -> ParameterDoc
        """ Get: ReturnParameter(self: OverloadDoc) -> ParameterDoc """
        ...



class ParameterDoc: # skipped bases: <type 'object'>, <type 'object'>
    """
    ParameterDoc(name: str)
    ParameterDoc(name: str, paramFlags: ParameterFlags)
    ParameterDoc(name: str, typeName: str)
    ParameterDoc(name: str, typeName: str, documentation: str)
    ParameterDoc(name: str, typeName: str, documentation: str, paramFlags: ParameterFlags)
    """
    @property
    def Documentation(self) -> str:
        """ Get: Documentation(self: ParameterDoc) -> str """
        ...

    @property
    def Flags(self): # -> ParameterFlags
        """ Get: Flags(self: ParameterDoc) -> ParameterFlags """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ParameterDoc) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: ParameterDoc) -> str """
        ...



class ParameterFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ParameterFlags, values: None (0), ParamsArray (1), ParamsDict (2) """
    ParamsArray: ParameterFlags = ...
    ParamsDict: ParameterFlags = ...
    value__ = ...


class ScriptEngine(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def LanguageVersion(self) -> Version:
        """ Get: LanguageVersion(self: ScriptEngine) -> Version """
        ...

    @property
    def Operations(self) -> ObjectOperations:
        """ Get: Operations(self: ScriptEngine) -> ObjectOperations """
        ...

    @property
    def Runtime(self): # -> ScriptRuntime
        """ Get: Runtime(self: ScriptEngine) -> ScriptRuntime """
        ...

    @property
    def Setup(self) -> LanguageSetup:
        """ Get: Setup(self: ScriptEngine) -> LanguageSetup """
        ...


    def CreateOperations(self, scope = ...) -> ObjectOperations: # Not found arg types: {'scope': 'ScriptScope'}
        """
        CreateOperations(self: ScriptEngine) -> ObjectOperations
        CreateOperations(self: ScriptEngine, scope: ScriptScope) -> ObjectOperations
        """
        ...

    def CreateScope(self, *__args:IDictionary): # -> ScriptScope
        """
        CreateScope(self: ScriptEngine) -> ScriptScope
        CreateScope(self: ScriptEngine, dictionary: IDictionary[str, object]) -> ScriptScope
        CreateScope(self: ScriptEngine, storage: IDynamicMetaObjectProvider) -> ScriptScope
        """
        ...

    def CreateScriptSource(self, *__args:CodeObject): # -> ScriptSource
        """
        CreateScriptSource(self: ScriptEngine, content: CodeObject) -> ScriptSource
        CreateScriptSource(self: ScriptEngine, content: CodeObject, path: str) -> ScriptSource
        CreateScriptSource(self: ScriptEngine, content: CodeObject, kind: SourceCodeKind) -> ScriptSource
        CreateScriptSource(self: ScriptEngine, content: CodeObject, path: str, kind: SourceCodeKind) -> ScriptSource
        CreateScriptSource(self: ScriptEngine, content: StreamContentProvider, path: str) -> ScriptSource
        CreateScriptSource(self: ScriptEngine, content: StreamContentProvider, path: str, encoding: Encoding) -> ScriptSource
        CreateScriptSource(self: ScriptEngine, content: StreamContentProvider, path: str, encoding: Encoding, kind: SourceCodeKind) -> ScriptSource
        CreateScriptSource(self: ScriptEngine, contentProvider: TextContentProvider, path: str, kind: SourceCodeKind) -> ScriptSource
        """
        ...

    def CreateScriptSourceFromFile(self, path:str, encoding:Encoding = ..., kind:SourceCodeKind = ...): # -> ScriptSource
        """
        CreateScriptSourceFromFile(self: ScriptEngine, path: str) -> ScriptSource
        CreateScriptSourceFromFile(self: ScriptEngine, path: str, encoding: Encoding) -> ScriptSource
        CreateScriptSourceFromFile(self: ScriptEngine, path: str, encoding: Encoding, kind: SourceCodeKind) -> ScriptSource
        """
        ...

    def CreateScriptSourceFromString(self, *__args:str): # -> ScriptSource
        """
        CreateScriptSourceFromString(self: ScriptEngine, expression: str) -> ScriptSource
        CreateScriptSourceFromString(self: ScriptEngine, code: str, kind: SourceCodeKind) -> ScriptSource
        CreateScriptSourceFromString(self: ScriptEngine, expression: str, path: str) -> ScriptSource
        CreateScriptSourceFromString(self: ScriptEngine, code: str, path: str, kind: SourceCodeKind) -> ScriptSource
        """
        ...

    def Execute(self, expression:str, scope = ...) -> object: # Not found arg types: {'scope': 'ScriptScope'}
        """
        Execute(self: ScriptEngine, expression: str) -> object
        Execute(self: ScriptEngine, expression: str, scope: ScriptScope) -> object
        Execute[T](self: ScriptEngine, expression: str) -> T
        Execute[T](self: ScriptEngine, expression: str, scope: ScriptScope) -> T
        """
        ...

    def ExecuteAndWrap(self, expression:str, *__args) -> ObjectHandle: # Not found arg types: {'*__args': 'ScriptScope'}
        """
        ExecuteAndWrap(self: ScriptEngine, expression: str, scope: ScriptScope) -> ObjectHandle
        ExecuteAndWrap(self: ScriptEngine, expression: str) -> ObjectHandle
        ExecuteAndWrap(self: ScriptEngine, expression: str, scope: ScriptScope) -> (ObjectHandle, ObjectHandle)
        ExecuteAndWrap(self: ScriptEngine, expression: str) -> (ObjectHandle, ObjectHandle)
        """
        ...

    def ExecuteFile(self, path:str, scope = ...): # -> ScriptScope # Not found arg types: {'scope': 'ScriptScope'}
        """
        ExecuteFile(self: ScriptEngine, path: str) -> ScriptScope
        ExecuteFile(self: ScriptEngine, path: str, scope: ScriptScope) -> ScriptScope
        """
        ...

    def GetCompilerOptions(self, scope = ...) -> CompilerOptions: # Not found arg types: {'scope': 'ScriptScope'}
        """
        GetCompilerOptions(self: ScriptEngine) -> CompilerOptions
        GetCompilerOptions(self: ScriptEngine, scope: ScriptScope) -> CompilerOptions
        """
        ...

    def GetScope(self, path:str): # -> ScriptScope
        """ GetScope(self: ScriptEngine, path: str) -> ScriptScope """
        ...

    def GetSearchPaths(self) -> ICollection:
        """ GetSearchPaths(self: ScriptEngine) -> ICollection[str] """
        ...

    def GetService(self, args:Array): # -> TService
        """ GetService[TService](self: ScriptEngine, *args: Array[object]) -> TService """
        ...

    def SetSearchPaths(self, paths:ICollection): # -> 
        """ SetSearchPaths(self: ScriptEngine, paths: ICollection[str]) """
        ...


class ScriptHost(MarshalByRefObject): # skipped bases: <type 'object'>
    """ ScriptHost() """
    @property
    def PlatformAdaptationLayer(self) -> PlatformAdaptationLayer:
        """ Get: PlatformAdaptationLayer(self: ScriptHost) -> PlatformAdaptationLayer """
        ...

    @property
    def Runtime(self): # -> ScriptRuntime
        """ Get: Runtime(self: ScriptHost) -> ScriptRuntime """
        ...


    def EngineCreated(self, *args): #cannot find CLR method
        """ EngineCreated(self: ScriptHost, engine: ScriptEngine) """
        ...

    def RuntimeAttached(self, *args): #cannot find CLR method
        """ RuntimeAttached(self: ScriptHost) """
        ...


class ScriptIO(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ErrorEncoding(self) -> Encoding:
        """ Get: ErrorEncoding(self: ScriptIO) -> Encoding """
        ...

    @property
    def ErrorStream(self) -> Stream:
        """ Get: ErrorStream(self: ScriptIO) -> Stream """
        ...

    @property
    def ErrorWriter(self) -> TextWriter:
        """ Get: ErrorWriter(self: ScriptIO) -> TextWriter """
        ...

    @property
    def InputEncoding(self) -> Encoding:
        """ Get: InputEncoding(self: ScriptIO) -> Encoding """
        ...

    @property
    def InputReader(self) -> TextReader:
        """ Get: InputReader(self: ScriptIO) -> TextReader """
        ...

    @property
    def InputStream(self) -> Stream:
        """ Get: InputStream(self: ScriptIO) -> Stream """
        ...

    @property
    def OutputEncoding(self) -> Encoding:
        """ Get: OutputEncoding(self: ScriptIO) -> Encoding """
        ...

    @property
    def OutputStream(self) -> Stream:
        """ Get: OutputStream(self: ScriptIO) -> Stream """
        ...

    @property
    def OutputWriter(self) -> TextWriter:
        """ Get: OutputWriter(self: ScriptIO) -> TextWriter """
        ...


    def RedirectToConsole(self): # -> 
        """ RedirectToConsole(self: ScriptIO) """
        ...

    def SetErrorOutput(self, stream:Stream, *__args:Encoding): # -> 
        """ SetErrorOutput(self: ScriptIO, stream: Stream, encoding: Encoding)SetErrorOutput(self: ScriptIO, stream: Stream, writer: TextWriter) """
        ...

    def SetInput(self, stream:Stream, *__args:Encoding): # -> 
        """ SetInput(self: ScriptIO, stream: Stream, encoding: Encoding)SetInput(self: ScriptIO, stream: Stream, reader: TextReader, encoding: Encoding) """
        ...

    def SetOutput(self, stream:Stream, *__args:Encoding): # -> 
        """ SetOutput(self: ScriptIO, stream: Stream, encoding: Encoding)SetOutput(self: ScriptIO, stream: Stream, writer: TextWriter) """
        ...


class ScriptRuntime(MarshalByRefObject): # skipped bases: <type 'object'>
    """ ScriptRuntime(setup: ScriptRuntimeSetup) """
    @property
    def Globals(self): # -> ScriptScope
        """
        Get: Globals(self: ScriptRuntime) -> ScriptScope
        Set: Globals(self: ScriptRuntime) = value
        """
        ...

    @property
    def Host(self) -> ScriptHost:
        """ Get: Host(self: ScriptRuntime) -> ScriptHost """
        ...

    @property
    def IO(self) -> ScriptIO:
        """ Get: IO(self: ScriptRuntime) -> ScriptIO """
        ...

    @property
    def Operations(self) -> ObjectOperations:
        """ Get: Operations(self: ScriptRuntime) -> ObjectOperations """
        ...

    @property
    def Setup(self): # -> ScriptRuntimeSetup
        """ Get: Setup(self: ScriptRuntime) -> ScriptRuntimeSetup """
        ...


    @staticmethod
    def CreateFromConfiguration() -> ScriptRuntime:
        """ CreateFromConfiguration() -> ScriptRuntime """
        ...

    def CreateOperations(self) -> ObjectOperations:
        """ CreateOperations(self: ScriptRuntime) -> ObjectOperations """
        ...

    @staticmethod
    def CreateRemote(domain:AppDomain, setup) -> ScriptRuntime: # Not found arg types: {'setup': 'ScriptRuntimeSetup'}
        """ CreateRemote(domain: AppDomain, setup: ScriptRuntimeSetup) -> ScriptRuntime """
        ...

    def CreateScope(self, *__args:str): # -> ScriptScope
        """
        CreateScope(self: ScriptRuntime) -> ScriptScope
        CreateScope(self: ScriptRuntime, languageId: str) -> ScriptScope
        CreateScope(self: ScriptRuntime, storage: IDynamicMetaObjectProvider) -> ScriptScope
        CreateScope(self: ScriptRuntime, languageId: str, storage: IDynamicMetaObjectProvider) -> ScriptScope
        CreateScope(self: ScriptRuntime, dictionary: IDictionary[str, object]) -> ScriptScope
        CreateScope(self: ScriptRuntime, languageId: str, storage: IDictionary[str, object]) -> ScriptScope
        """
        ...

    def ExecuteFile(self, path:str): # -> ScriptScope
        """ ExecuteFile(self: ScriptRuntime, path: str) -> ScriptScope """
        ...

    def GetEngine(self, languageName:str) -> ScriptEngine:
        """ GetEngine(self: ScriptRuntime, languageName: str) -> ScriptEngine """
        ...

    def GetEngineByFileExtension(self, fileExtension:str) -> ScriptEngine:
        """ GetEngineByFileExtension(self: ScriptRuntime, fileExtension: str) -> ScriptEngine """
        ...

    def GetEngineByTypeName(self, assemblyQualifiedTypeName:str) -> ScriptEngine:
        """ GetEngineByTypeName(self: ScriptRuntime, assemblyQualifiedTypeName: str) -> ScriptEngine """
        ...

    def LoadAssembly(self, assembly:Assembly): # -> 
        """ LoadAssembly(self: ScriptRuntime, assembly: Assembly) """
        ...

    def Shutdown(self): # -> 
        """ Shutdown(self: ScriptRuntime) """
        ...

    def TryGetEngine(self, languageName, engine) -> Tuple_[bool, ScriptEngine]:
        """ TryGetEngine(self: ScriptRuntime, languageName: str) -> (bool, ScriptEngine) """
        ...

    def TryGetEngineByFileExtension(self, fileExtension, engine) -> Tuple_[bool, ScriptEngine]:
        """ TryGetEngineByFileExtension(self: ScriptRuntime, fileExtension: str) -> (bool, ScriptEngine) """
        ...

    def UseFile(self, path:str): # -> ScriptScope
        """ UseFile(self: ScriptRuntime, path: str) -> ScriptScope """
        ...

    def __new__(cls, setup) -> Self: # Not found arg types: {'setup': 'ScriptRuntimeSetup'}
        """ __new__(cls: type, setup: ScriptRuntimeSetup) """
        ...


class ScriptRuntimeSetup: # skipped bases: <type 'object'>, <type 'object'>
    """ ScriptRuntimeSetup() """
    @property
    def DebugMode(self) -> bool:
        """
        Get: DebugMode(self: ScriptRuntimeSetup) -> bool
        Set: DebugMode(self: ScriptRuntimeSetup) = value
        """
        ...

    @property
    def HostArguments(self) -> IList:
        """
        Get: HostArguments(self: ScriptRuntimeSetup) -> IList[object]
        Set: HostArguments(self: ScriptRuntimeSetup) = value
        """
        ...

    @property
    def HostType(self) -> Type:
        """
        Get: HostType(self: ScriptRuntimeSetup) -> Type
        Set: HostType(self: ScriptRuntimeSetup) = value
        """
        ...

    @property
    def LanguageSetups(self) -> IList:
        """ Get: LanguageSetups(self: ScriptRuntimeSetup) -> IList[LanguageSetup] """
        ...

    @property
    def Options(self) -> IDictionary:
        """ Get: Options(self: ScriptRuntimeSetup) -> IDictionary[str, object] """
        ...

    @property
    def PrivateBinding(self) -> bool:
        """
        Get: PrivateBinding(self: ScriptRuntimeSetup) -> bool
        Set: PrivateBinding(self: ScriptRuntimeSetup) = value
        """
        ...


    @staticmethod
    def ReadConfiguration(*__args) -> ScriptRuntimeSetup:
        """
        ReadConfiguration() -> ScriptRuntimeSetup
        ReadConfiguration(configFileStream: Stream) -> ScriptRuntimeSetup
        ReadConfiguration(configFilePath: str) -> ScriptRuntimeSetup
        """
        ...


class ScriptScope(MarshalByRefObject, IDynamicMetaObjectProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Engine(self) -> ScriptEngine:
        """ Get: Engine(self: ScriptScope) -> ScriptEngine """
        ...


    def ContainsVariable(self, name:str) -> bool:
        """ ContainsVariable(self: ScriptScope, name: str) -> bool """
        ...

    def GetItems(self) -> IEnumerable:
        """ GetItems(self: ScriptScope) -> IEnumerable[KeyValuePair[str, object]] """
        ...

    def GetVariable(self, name:str) -> object:
        """
        GetVariable(self: ScriptScope, name: str) -> object
        GetVariable[T](self: ScriptScope, name: str) -> T
        """
        ...

    def GetVariableHandle(self, name:str) -> ObjectHandle:
        """ GetVariableHandle(self: ScriptScope, name: str) -> ObjectHandle """
        ...

    def GetVariableNames(self) -> IEnumerable:
        """ GetVariableNames(self: ScriptScope) -> IEnumerable[str] """
        ...

    def RemoveVariable(self, name:str) -> bool:
        """ RemoveVariable(self: ScriptScope, name: str) -> bool """
        ...

    def SetVariable(self, name:str, *__args:object): # -> 
        """ SetVariable(self: ScriptScope, name: str, value: object)SetVariable(self: ScriptScope, name: str, handle: ObjectHandle) """
        ...

    def TryGetVariable(self, name, value) -> Tuple_[bool, object]:
        """
        TryGetVariable(self: ScriptScope, name: str) -> (bool, object)
        TryGetVariable[T](self: ScriptScope, name: str) -> (bool, T)
        """
        ...

    def TryGetVariableHandle(self, name, handle) -> Tuple_[bool, ObjectHandle]:
        """ TryGetVariableHandle(self: ScriptScope, name: str) -> (bool, ObjectHandle) """
        ...


class ScriptSource(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Engine(self) -> ScriptEngine:
        """ Get: Engine(self: ScriptSource) -> ScriptEngine """
        ...

    @property
    def Kind(self) -> SourceCodeKind:
        """ Get: Kind(self: ScriptSource) -> SourceCodeKind """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: ScriptSource) -> str """
        ...


    def Compile(self, *__args:ErrorListener) -> CompiledCode:
        """
        Compile(self: ScriptSource) -> CompiledCode
        Compile(self: ScriptSource, errorListener: ErrorListener) -> CompiledCode
        Compile(self: ScriptSource, compilerOptions: CompilerOptions) -> CompiledCode
        Compile(self: ScriptSource, compilerOptions: CompilerOptions, errorListener: ErrorListener) -> CompiledCode
        """
        ...

    def DetectEncoding(self) -> Encoding:
        """ DetectEncoding(self: ScriptSource) -> Encoding """
        ...

    def Execute(self, scope:ScriptScope = ...) -> object:
        """
        Execute(self: ScriptSource, scope: ScriptScope) -> object
        Execute(self: ScriptSource) -> object
        Execute[T](self: ScriptSource, scope: ScriptScope) -> T
        Execute[T](self: ScriptSource) -> T
        """
        ...

    def ExecuteAndWrap(self, *__args:ScriptScope) -> ObjectHandle:
        """
        ExecuteAndWrap(self: ScriptSource) -> ObjectHandle
        ExecuteAndWrap(self: ScriptSource, scope: ScriptScope) -> ObjectHandle
        ExecuteAndWrap(self: ScriptSource) -> (ObjectHandle, ObjectHandle)
        ExecuteAndWrap(self: ScriptSource, scope: ScriptScope) -> (ObjectHandle, ObjectHandle)
        """
        ...

    def ExecuteProgram(self) -> int:
        """ ExecuteProgram(self: ScriptSource) -> int """
        ...

    def GetCode(self) -> str:
        """ GetCode(self: ScriptSource) -> str """
        ...

    def GetCodeLine(self, line:int) -> str:
        """ GetCodeLine(self: ScriptSource, line: int) -> str """
        ...

    def GetCodeLines(self, start:int, count:int) -> Array:
        """ GetCodeLines(self: ScriptSource, start: int, count: int) -> Array[str] """
        ...

    def GetCodeProperties(self, options:CompilerOptions = ...) -> ScriptCodeParseResult:
        """
        GetCodeProperties(self: ScriptSource) -> ScriptCodeParseResult
        GetCodeProperties(self: ScriptSource, options: CompilerOptions) -> ScriptCodeParseResult
        """
        ...

    def GetReader(self) -> SourceCodeReader:
        """ GetReader(self: ScriptSource) -> SourceCodeReader """
        ...

    def MapLine(self, *__args:int) -> int:
        """
        MapLine(self: ScriptSource, line: int) -> int
        MapLine(self: ScriptSource, span: SourceSpan) -> SourceSpan
        MapLine(self: ScriptSource, location: SourceLocation) -> SourceLocation
        """
        ...

    def MapLinetoFile(self, line:int) -> str:
        """ MapLinetoFile(self: ScriptSource, line: int) -> str """
        ...


class TokenCategorizer(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CurrentPosition(self) -> SourceLocation:
        """ Get: CurrentPosition(self: TokenCategorizer) -> SourceLocation """
        ...

    @property
    def CurrentState(self) -> object:
        """ Get: CurrentState(self: TokenCategorizer) -> object """
        ...

    @property
    def ErrorSink(self) -> ErrorSink:
        """
        Get: ErrorSink(self: TokenCategorizer) -> ErrorSink
        Set: ErrorSink(self: TokenCategorizer) = value
        """
        ...

    @property
    def IsRestartable(self) -> bool:
        """ Get: IsRestartable(self: TokenCategorizer) -> bool """
        ...


    def Initialize(self, state:object, scriptSource:ScriptSource, initialLocation:SourceLocation): # -> 
        """ Initialize(self: TokenCategorizer, state: object, scriptSource: ScriptSource, initialLocation: SourceLocation) """
        ...

    def ReadToken(self) -> TokenInfo:
        """ ReadToken(self: TokenCategorizer) -> TokenInfo """
        ...

    def ReadTokens(self, characterCount:int) -> IEnumerable:
        """ ReadTokens(self: TokenCategorizer, characterCount: int) -> IEnumerable[TokenInfo] """
        ...

    def SkipToken(self) -> bool:
        """ SkipToken(self: TokenCategorizer) -> bool """
        ...

    def SkipTokens(self, characterCount:int) -> bool:
        """ SkipTokens(self: TokenCategorizer, characterCount: int) -> bool """
        ...


# variables with complex values

