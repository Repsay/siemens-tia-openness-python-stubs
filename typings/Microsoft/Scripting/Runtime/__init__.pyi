# encoding: utf-8
# module Microsoft.Scripting.Runtime calls itself Runtime
# from Microsoft.Dynamic, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1, Microsoft.Scripting, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1
# by generator 1.145
""" no doc """
from __future__ import annotations
from Babel import TokenInfo

from Microsoft.Scripting import (ArgumentTypeException, CompilerOptions, 
    ErrorSink, LanguageOptions, PlatformAdaptationLayer, ScriptCode, 
    SourceCodeKind, SourceCodeReader, SourceLocation, SourceSpan, SourceUnit, 
    TextContentProvider)

from Microsoft.Scripting.Actions import EventTracker, MethodGroup

from Microsoft.Scripting.Utils import ConsoleStreamType

from System import (Array, AsyncCallback, Attribute, Byte, Char, Decimal, 
    Delegate, Enum, EventArgs, Guid, IAsyncResult, IEquatable, Int16, Int64, 
    MulticastDelegate, Nullable, SByte, Single, Type, UInt16, UInt32, UInt64, 
    Version)

from System.CodeDom import CodeLinePragma, CodeMemberMethod, CodeObject

from System.Collections import ICollection, IDictionary, IEnumerable, IList

from System.Collections.Generic import Dictionary, IReadOnlyDictionary

from System.Dynamic import (BinaryOperationBinder, BindingRestrictions, 
    CallInfo, ConvertBinder, CreateInstanceBinder, DeleteMemberBinder, 
    DynamicMetaObject, GetMemberBinder, IDynamicMetaObjectProvider, 
    InvokeBinder, InvokeMemberBinder, SetMemberBinder, UnaryOperationBinder)

from System.IdentityModel import Scope

from System.IO import Stream, StringWriter, TextReader, TextWriter

from System.Linq.Expressions import Expression, ExpressionType

from System.Reflection import (Assembly, ConstructorInfo, EventInfo, 
    MethodBase, MethodInfo)

from System.Runtime.CompilerServices import (CallSite, CallSiteBinder, 
    IRuntimeVariables)

from System.Text import Encoding

from System.Xaml import XamlXmlReader

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (Array[ScopeExtension], 
    BoundEvent, Func, LanguageContext, OrdinalComparer, ParserSink, 
    RuntimeType, ScopeExtension, ScriptDomainManager, SharedIO, T, TOther, 
    TResult, TService, TTarget, field#, type-collision)
"""

# no functions
# classes

class ArgumentArray: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ArgumentArray) -> int """
        ...


    @staticmethod
    def GetArg(array:ArgumentArray, index:int) -> object:
        """ GetArg(array: ArgumentArray, index: int) -> object """
        ...

    def GetArgument(self, index:int) -> object:
        """ GetArgument(self: ArgumentArray, index: int) -> object """
        ...

    def GetMetaObject(self, parameter:Expression, index:int) -> DynamicMetaObject:
        """ GetMetaObject(self: ArgumentArray, parameter: Expression, index: int) -> DynamicMetaObject """
        ...


class BinderOps: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def BadArgumentsForOperation(op:ExpressionType, args:Array) -> ArgumentTypeException:
        """ BadArgumentsForOperation(op: ExpressionType, *args: Array[object]) -> ArgumentTypeException """
        ...

    @staticmethod
    def CheckDictionaryMembers(dict:IDictionary, names:Array, types:Array) -> bool:
        """ CheckDictionaryMembers(dict: IDictionary, names: Array[str], types: Array[Type]) -> bool """
        ...

    @staticmethod
    def GetCombinedParameters(initialArgs:Array, additionalArgs:object) -> Array:
        """ GetCombinedParameters(initialArgs: Array[object], additionalArgs: object) -> Array[object] """
        ...

    @staticmethod
    def GetEventHandlerType(eventInfo:EventInfo) -> Type:
        """ GetEventHandlerType(eventInfo: EventInfo) -> Type """
        ...

    @staticmethod
    def GetStringMembers(members:IList) -> IList:
        """ GetStringMembers(members: IList[object]) -> IList[str] """
        ...

    @staticmethod
    def InvalidSplatteeError(name:str, typeName:str) -> ArgumentTypeException:
        """ InvalidSplatteeError(name: str, typeName: str) -> ArgumentTypeException """
        ...

    @staticmethod
    def InvokeConstructor(ci:ConstructorInfo, args:Array) -> object:
        """ InvokeConstructor(ci: ConstructorInfo, args: Array[object]) -> object """
        ...

    @staticmethod
    def InvokeMethod(mb:MethodBase, obj:object, args:Array) -> object:
        """ InvokeMethod(mb: MethodBase, obj: object, args: Array[object]) -> object """
        ...

    @staticmethod
    def MakeDictionary(names:Array, values:Array) -> Dictionary:
        """ MakeDictionary[(TKey, TValue)](names: Array[str], values: Array[object]) -> Dictionary[TKey, TValue] """
        ...

    @staticmethod
    def MakeReadOnlyDictionary(names:Array, values:Array) -> IReadOnlyDictionary:
        """ MakeReadOnlyDictionary[(TKey, TValue)](names: Array[str], values: Array[object]) -> IReadOnlyDictionary[TKey, TValue] """
        ...

    @staticmethod
    def SetEvent(eventTracker:EventTracker, value:object): # -> 
        """ SetEvent(eventTracker: EventTracker, value: object) """
        ...

    @staticmethod
    def SimpleTypeError(message:str) -> ArgumentTypeException:
        """ SimpleTypeError(message: str) -> ArgumentTypeException """
        ...

    @staticmethod
    def TypeErrorForDuplicateArgument(name:str, position:int, argumentName:str) -> ArgumentTypeException:
        """ TypeErrorForDuplicateArgument(name: str, position: int, argumentName: str) -> ArgumentTypeException """
        ...

    @staticmethod
    def TypeErrorForDuplicateKeywordArgument(name:str, argumentName:str) -> ArgumentTypeException:
        """ TypeErrorForDuplicateKeywordArgument(name: str, argumentName: str) -> ArgumentTypeException """
        ...

    @staticmethod
    def TypeErrorForExtraKeywordArgument(name:str, argumentName:str) -> ArgumentTypeException:
        """ TypeErrorForExtraKeywordArgument(name: str, argumentName: str) -> ArgumentTypeException """
        ...

    @staticmethod
    def TypeErrorForIncorrectArgumentCount(*__args) -> ArgumentTypeException:
        """
        TypeErrorForIncorrectArgumentCount(methodName: str, formalNormalArgumentCount: int, defaultArgumentCount: int, providedArgumentCount: int, hasArgList: bool, keywordArgumentsProvided: bool) -> ArgumentTypeException
        TypeErrorForIncorrectArgumentCount(name: str, formalNormalArgumentCount: int, defaultArgumentCount: int, providedArgumentCount: int) -> ArgumentTypeException
        TypeErrorForIncorrectArgumentCount(name: str, expected: int, received: int) -> ArgumentTypeException
        TypeErrorForIncorrectArgumentCount(methodName: str, minFormalNormalArgumentCount: int, maxFormalNormalArgumentCount: int, defaultArgumentCount: int, providedArgumentCount: int, hasArgList: bool, keywordArgumentsProvided: bool) -> ArgumentTypeException
        """
        ...

    @staticmethod
    def TypeErrorForNonInferrableMethod(name:str) -> ArgumentTypeException:
        """ TypeErrorForNonInferrableMethod(name: str) -> ArgumentTypeException """
        ...

    __all__: list = ...


class BinderType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BinderType, values: BinaryOperator (1), ComparisonOperator (2), Constructor (3), Normal (0) """
    BinaryOperator: BinderType = ...
    ComparisonOperator: BinderType = ...
    Constructor: BinderType = ...
    Normal: BinderType = ...
    value__ = ...


class BindingRestrictionsHelpers: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetRuntimeTypeRestriction(*__args:DynamicMetaObject) -> BindingRestrictions:
        """
        GetRuntimeTypeRestriction(expr: Expression, type: Type) -> BindingRestrictions
        GetRuntimeTypeRestriction(obj: DynamicMetaObject) -> BindingRestrictions
        """
        ...

    __all__: list = ...


class CachedOptimizedCodeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    CachedOptimizedCodeAttribute()
    CachedOptimizedCodeAttribute(names: Array[str])
    """
    @property
    def Names(self) -> Array:
        """ Get: Names(self: CachedOptimizedCodeAttribute) -> Array[str] """
        ...


    def __new__(cls, names:Array = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, names: Array[str])
        """
        ...


class CallTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CallTypes, values: ImplicitInstance (1), None (0) """
    ImplicitInstance: CallTypes = ...
    value__ = ...


class Cast: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Explicit(o:object, to:Type = ...) -> object:
        """
        Explicit(o: object, to: Type) -> object
        Explicit[T](o: object) -> T
        """
        ...

    @staticmethod
    def ExplicitCastToBoolean(o:object) -> bool:
        """ ExplicitCastToBoolean(o: object) -> bool """
        ...

    @staticmethod
    def ExplicitCastToByte(o:object) -> Byte:
        """ ExplicitCastToByte(o: object) -> Byte """
        ...

    @staticmethod
    def ExplicitCastToChar(o:object) -> Char:
        """ ExplicitCastToChar(o: object) -> Char """
        ...

    @staticmethod
    def ExplicitCastToDecimal(o:object) -> Decimal:
        """ ExplicitCastToDecimal(o: object) -> Decimal """
        ...

    @staticmethod
    def ExplicitCastToDouble(o:object) -> float:
        """ ExplicitCastToDouble(o: object) -> float """
        ...

    @staticmethod
    def ExplicitCastToInt16(o:object) -> Int16:
        """ ExplicitCastToInt16(o: object) -> Int16 """
        ...

    @staticmethod
    def ExplicitCastToInt32(o:object) -> int:
        """ ExplicitCastToInt32(o: object) -> int """
        ...

    @staticmethod
    def ExplicitCastToInt64(o:object) -> Int64:
        """ ExplicitCastToInt64(o: object) -> Int64 """
        ...

    @staticmethod
    def ExplicitCastToNullableBoolean(o:object) -> Nullable:
        """ ExplicitCastToNullableBoolean(o: object) -> Nullable[bool] """
        ...

    @staticmethod
    def ExplicitCastToNullableByte(o:object) -> Nullable:
        """ ExplicitCastToNullableByte(o: object) -> Nullable[Byte] """
        ...

    @staticmethod
    def ExplicitCastToNullableChar(o:object) -> Nullable:
        """ ExplicitCastToNullableChar(o: object) -> Nullable[Char] """
        ...

    @staticmethod
    def ExplicitCastToNullableDecimal(o:object) -> Nullable:
        """ ExplicitCastToNullableDecimal(o: object) -> Nullable[Decimal] """
        ...

    @staticmethod
    def ExplicitCastToNullableDouble(o:object) -> Nullable:
        """ ExplicitCastToNullableDouble(o: object) -> Nullable[float] """
        ...

    @staticmethod
    def ExplicitCastToNullableInt16(o:object) -> Nullable:
        """ ExplicitCastToNullableInt16(o: object) -> Nullable[Int16] """
        ...

    @staticmethod
    def ExplicitCastToNullableInt32(o:object) -> Nullable:
        """ ExplicitCastToNullableInt32(o: object) -> Nullable[int] """
        ...

    @staticmethod
    def ExplicitCastToNullableInt64(o:object) -> Nullable:
        """ ExplicitCastToNullableInt64(o: object) -> Nullable[Int64] """
        ...

    @staticmethod
    def ExplicitCastToNullableSByte(o:object) -> Nullable:
        """ ExplicitCastToNullableSByte(o: object) -> Nullable[SByte] """
        ...

    @staticmethod
    def ExplicitCastToNullableSingle(o:object) -> Nullable:
        """ ExplicitCastToNullableSingle(o: object) -> Nullable[Single] """
        ...

    @staticmethod
    def ExplicitCastToNullableUInt16(o:object) -> Nullable:
        """ ExplicitCastToNullableUInt16(o: object) -> Nullable[UInt16] """
        ...

    @staticmethod
    def ExplicitCastToNullableUInt32(o:object) -> Nullable:
        """ ExplicitCastToNullableUInt32(o: object) -> Nullable[UInt32] """
        ...

    @staticmethod
    def ExplicitCastToNullableUInt64(o:object) -> Nullable:
        """ ExplicitCastToNullableUInt64(o: object) -> Nullable[UInt64] """
        ...

    @staticmethod
    def ExplicitCastToSByte(o:object) -> SByte:
        """ ExplicitCastToSByte(o: object) -> SByte """
        ...

    @staticmethod
    def ExplicitCastToSingle(o:object) -> Single:
        """ ExplicitCastToSingle(o: object) -> Single """
        ...

    @staticmethod
    def ExplicitCastToUInt16(o:object) -> UInt16:
        """ ExplicitCastToUInt16(o: object) -> UInt16 """
        ...

    @staticmethod
    def ExplicitCastToUInt32(o:object) -> UInt32:
        """ ExplicitCastToUInt32(o: object) -> UInt32 """
        ...

    @staticmethod
    def ExplicitCastToUInt64(o:object) -> UInt64:
        """ ExplicitCastToUInt64(o: object) -> UInt64 """
        ...

    @staticmethod
    def NewNullableInstance(type:Type) -> object:
        """ NewNullableInstance(type: Type) -> object """
        ...

    __all__: list = ...


class CodeDomCodeGen: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Writer(self):
        ...


    def GenerateCode(self, codeDom:CodeMemberMethod, context, path:str, kind:SourceCodeKind) -> SourceUnit: # Not found arg types: {'context': 'LanguageContext'}
        """ GenerateCode(self: CodeDomCodeGen, codeDom: CodeMemberMethod, context: LanguageContext, path: str, kind: SourceCodeKind) -> SourceUnit """
        ...

    def QuoteString(self, *args): #cannot find CLR method
        """ QuoteString(self: CodeDomCodeGen, val: str) -> str """
        ...

    def WriteArgumentReferenceExpression(self, *args): #cannot find CLR method
        """ WriteArgumentReferenceExpression(self: CodeDomCodeGen, e: CodeArgumentReferenceExpression) """
        ...

    def WriteCallExpression(self, *args): #cannot find CLR method
        """ WriteCallExpression(self: CodeDomCodeGen, m: CodeMethodInvokeExpression) """
        ...

    def WriteExpression(self, *args): #cannot find CLR method
        """ WriteExpression(self: CodeDomCodeGen, e: CodeExpression) """
        ...

    def WriteExpressionStatement(self, *args): #cannot find CLR method
        """ WriteExpressionStatement(self: CodeDomCodeGen, s: CodeExpressionStatement) """
        ...

    def WriteFunctionDefinition(self, *args): #cannot find CLR method
        """ WriteFunctionDefinition(self: CodeDomCodeGen, func: CodeMemberMethod) """
        ...

    def WritePrimitiveExpression(self, *args): #cannot find CLR method
        """ WritePrimitiveExpression(self: CodeDomCodeGen, e: CodePrimitiveExpression) """
        ...

    def WriteSnippetExpression(self, *args): #cannot find CLR method
        """ WriteSnippetExpression(self: CodeDomCodeGen, e: CodeSnippetExpression) """
        ...

    def WriteSnippetStatement(self, *args): #cannot find CLR method
        """ WriteSnippetStatement(self: CodeDomCodeGen, s: CodeSnippetStatement) """
        ...

    def WriteStatement(self, *args): #cannot find CLR method
        """ WriteStatement(self: CodeDomCodeGen, s: CodeStatement) """
        ...

    SourceSpanKey = ...


class CompilerContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    CompilerContext(sourceUnit: SourceUnit, options: CompilerOptions, errorSink: ErrorSink)
    CompilerContext(sourceUnit: SourceUnit, options: CompilerOptions, errorSink: ErrorSink, parserSink: ParserSink)
    """
    @property
    def Errors(self) -> ErrorSink:
        """ Get: Errors(self: CompilerContext) -> ErrorSink """
        ...

    @property
    def Options(self) -> CompilerOptions:
        """ Get: Options(self: CompilerContext) -> CompilerOptions """
        ...

    @property
    def ParserSink(self): # -> ParserSink
        """ Get: ParserSink(self: CompilerContext) -> ParserSink """
        ...

    @property
    def SourceUnit(self) -> SourceUnit:
        """ Get: SourceUnit(self: CompilerContext) -> SourceUnit """
        ...



class ContextId(IEquatable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Id(self) -> int:
        """ Get: Id(self: ContextId) -> int """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: ContextId) -> int """
        ...

    @staticmethod
    def LookupContext(identifier:object) -> ContextId:
        """ LookupContext(identifier: object) -> ContextId """
        ...

    @staticmethod
    def RegisterContext(identifier:object) -> ContextId:
        """ RegisterContext(identifier: object) -> ContextId """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Empty: ContextId = ...


class CustomStringDictionary(IDictionary, dict): # skipped bases: <type 'IEnumerable[KeyValuePair[object, object]]'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ICollection[KeyValuePair[object, object]]'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: CustomStringDictionary) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: CustomStringDictionary) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: CustomStringDictionary) -> object """
        ...


    def CopyTo(self, array:Array, *__args:int): # -> 
        """ CopyTo(self: CustomStringDictionary, array: Array[KeyValuePair[object, object]], arrayIndex: int)CopyTo(self: CustomStringDictionary, array: Array, index: int) """
        ...

    def GetExtraKeys(self) -> Array:
        """ GetExtraKeys(self: CustomStringDictionary) -> Array[str] """
        ...

    def GetValueHashCode(self) -> int:
        """ GetValueHashCode(self: CustomStringDictionary) -> int """
        ...

    @staticmethod
    def IsNullObject(o:object) -> bool:
        """ IsNullObject(o: object) -> bool """
        ...

    @staticmethod
    def NullToObj(o:object) -> object:
        """ NullToObj(o: object) -> object """
        ...

    @staticmethod
    def ObjToNull(o:object) -> object:
        """ ObjToNull(o: object) -> object """
        ...

    def TryGetExtraValue(self, *args): #cannot find CLR method
        """ TryGetExtraValue(self: CustomStringDictionary, key: str) -> (bool, object) """
        ...

    def TryGetValue(self, key, value) -> Tuple_[bool, object]:
        """ TryGetValue(self: CustomStringDictionary, key: object) -> (bool, object) """
        ...

    def TrySetExtraValue(self, *args): #cannot find CLR method
        """ TrySetExtraValue(self: CustomStringDictionary, key: str, value: object) -> bool """
        ...

    def ValueEquals(self, other:object) -> bool:
        """ ValueEquals(self: CustomStringDictionary, other: object) -> bool """
        ...


class CustomSymbolDictionary(CustomStringDictionary): # skipped bases: <type 'IEnumerable[KeyValuePair[object, object]]'>, <type 'dict'>, <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection[KeyValuePair[object, object]]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class DelegateInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ DelegateInfo(context: LanguageContext, returnType: Type, parameters: Array[Type]) """
    def CreateDelegate(self, delegateType:Type, dynamicObject:object) -> Delegate:
        """ CreateDelegate(self: DelegateInfo, delegateType: Type, dynamicObject: object) -> Delegate """
        ...


class DlrCachedCodeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DlrCachedCodeAttribute() """
    pass

class DlrConfiguration: # skipped bases: <type 'object'>, <type 'object'>
    """ DlrConfiguration(debugMode: bool, privateBinding: bool, options: IDictionary[str, object]) """
    @property
    def DebugMode(self) -> bool:
        """ Get: DebugMode(self: DlrConfiguration) -> bool """
        ...

    @property
    def PrivateBinding(self) -> bool:
        """ Get: PrivateBinding(self: DlrConfiguration) -> bool """
        ...


    def AddLanguage(self, languageTypeName:str, displayName:str, names:IList, fileExtensions:IList, options:IDictionary): # -> 
        """ AddLanguage(self: DlrConfiguration, languageTypeName: str, displayName: str, names: IList[str], fileExtensions: IList[str], options: IDictionary[str, object]) """
        ...

    def GetFileExtensions(self, context = ...) -> Array: # Not found arg types: {'context': 'LanguageContext'}
        """
        GetFileExtensions(self: DlrConfiguration, context: LanguageContext) -> Array[str]
        GetFileExtensions(self: DlrConfiguration) -> Array[str]
        """
        ...

    def GetLanguageNames(self, context = ...) -> Array: # Not found arg types: {'context': 'LanguageContext'}
        """
        GetLanguageNames(self: DlrConfiguration, context: LanguageContext) -> Array[str]
        GetLanguageNames(self: DlrConfiguration) -> Array[str]
        """
        ...

    FileExtensionComparer = ...
    LanguageNameComparer = ...
    OptionNameComparer = ...


class DlrMainCallTarget(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DlrMainCallTarget(object: object, method: IntPtr) """
    def BeginInvoke(self, scope:Scope, context, callback:AsyncCallback, object:object) -> IAsyncResult: # Not found arg types: {'context': 'LanguageContext'}
        """ BeginInvoke(self: DlrMainCallTarget, scope: Scope, context: LanguageContext, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> object:
        """ EndInvoke(self: DlrMainCallTarget, result: IAsyncResult) -> object """
        ...

    def Invoke(self, scope:Scope, context) -> object: # Not found arg types: {'context': 'LanguageContext'}
        """ Invoke(self: DlrMainCallTarget, scope: Scope, context: LanguageContext) -> object """
        ...


class DocumentationAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DocumentationAttribute(documentation: str) """
    @property
    def Documentation(self) -> str:
        """ Get: Documentation(self: DocumentationAttribute) -> str """
        ...


    def __new__(cls, documentation:str) -> Self:
        """ __new__(cls: type, documentation: str) """
        ...


class DocumentationProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetMembers(self, value:object) -> ICollection:
        """ GetMembers(self: DocumentationProvider, value: object) -> ICollection[MemberDoc] """
        ...

    def GetOverloads(self, value:object) -> ICollection:
        """ GetOverloads(self: DocumentationProvider, value: object) -> ICollection[OverloadDoc] """
        ...


class DynamicDelegateCreator: # skipped bases: <type 'object'>, <type 'object'>
    """ DynamicDelegateCreator(languageContext: LanguageContext) """
    def GetDelegate(self, callableObject:object, delegateType:Type) -> Delegate:
        """ GetDelegate(self: DynamicDelegateCreator, callableObject: object, delegateType: Type) -> Delegate """
        ...

    def GetOrCreateDelegateForDynamicObject(self, dynamicObject:object, delegateType:Type, invoke:MethodInfo) -> Delegate:
        """ GetOrCreateDelegateForDynamicObject(self: DynamicDelegateCreator, dynamicObject: object, delegateType: Type, invoke: MethodInfo) -> Delegate """
        ...


class DynamicNull: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class DynamicOperations: # skipped bases: <type 'object'>, <type 'object'>
    """ DynamicOperations(lc: LanguageContext) """
    def ContainsMember(self, obj:object, name:str, ignoreCase:bool = ...) -> bool:
        """
        ContainsMember(self: DynamicOperations, obj: object, name: str) -> bool
        ContainsMember(self: DynamicOperations, obj: object, name: str, ignoreCase: bool) -> bool
        """
        ...

    def ConvertTo(self, obj:object, type:Type = ...) -> object:
        """
        ConvertTo[T](self: DynamicOperations, obj: object) -> T
        ConvertTo(self: DynamicOperations, obj: object, type: Type) -> object
        """
        ...

    def CreateInstance(self, obj:object, parameters:Array) -> object:
        """ CreateInstance(self: DynamicOperations, obj: object, *parameters: Array[object]) -> object """
        ...

    def DoOperation(self, operation:ExpressionType, target, other = ...): # -> TResult # Not found arg types: {'other': 'TOther', 'target': 'TTarget'}
        """
        DoOperation[(TTarget, TResult)](self: DynamicOperations, operation: ExpressionType, target: TTarget) -> TResult
        DoOperation[(TTarget, TOther, TResult)](self: DynamicOperations, operation: ExpressionType, target: TTarget, other: TOther) -> TResult
        """
        ...

    def ExplicitConvertTo(self, obj:object, type:Type = ...) -> object:
        """
        ExplicitConvertTo[T](self: DynamicOperations, obj: object) -> T
        ExplicitConvertTo(self: DynamicOperations, obj: object, type: Type) -> object
        """
        ...

    def Format(self, obj:object) -> str:
        """ Format(self: DynamicOperations, obj: object) -> str """
        ...

    def GetCallSignatures(self, o:object) -> IList:
        """ GetCallSignatures(self: DynamicOperations, o: object) -> IList[str] """
        ...

    def GetDocumentation(self, o:object) -> str:
        """ GetDocumentation(self: DynamicOperations, o: object) -> str """
        ...

    def GetMember(self, obj:object, name:str, ignoreCase:bool = ...) -> object:
        """
        GetMember(self: DynamicOperations, obj: object, name: str) -> object
        GetMember(self: DynamicOperations, obj: object, name: str, ignoreCase: bool) -> object
        GetMember[T](self: DynamicOperations, obj: object, name: str) -> T
        GetMember[T](self: DynamicOperations, obj: object, name: str, ignoreCase: bool) -> T
        """
        ...

    def GetMemberNames(self, obj:object) -> IList:
        """ GetMemberNames(self: DynamicOperations, obj: object) -> IList[str] """
        ...

    def GetOrCreateActionSite(self, siteBinder:CallSiteBinder) -> CallSite:
        """ GetOrCreateActionSite[T1](self: DynamicOperations, siteBinder: CallSiteBinder) -> CallSite[Action[CallSite, T1]] """
        ...

    def GetOrCreateSite(self, siteBinder:CallSiteBinder) -> CallSite:
        """
        GetOrCreateSite[(T1, TResult)](self: DynamicOperations, siteBinder: CallSiteBinder) -> CallSite[Func[CallSite, T1, TResult]]
        GetOrCreateSite[(T1, T2, TResult)](self: DynamicOperations, siteBinder: CallSiteBinder) -> CallSite[Func[CallSite, T1, T2, TResult]]
        GetOrCreateSite[(T1, T2, T3, TResult)](self: DynamicOperations, siteBinder: CallSiteBinder) -> CallSite[Func[CallSite, T1, T2, T3, TResult]]
        GetOrCreateSite[TSiteFunc](self: DynamicOperations, siteBinder: CallSiteBinder) -> CallSite[TSiteFunc]
        """
        ...

    def ImplicitConvertTo(self, obj:object, type:Type = ...) -> object:
        """
        ImplicitConvertTo[T](self: DynamicOperations, obj: object) -> T
        ImplicitConvertTo(self: DynamicOperations, obj: object, type: Type) -> object
        """
        ...

    def Invoke(self, obj:object, parameters:Array) -> object:
        """ Invoke(self: DynamicOperations, obj: object, *parameters: Array[object]) -> object """
        ...

    def InvokeMember(self, obj:object, memberName:str, *__args:Array) -> object:
        """
        InvokeMember(self: DynamicOperations, obj: object, memberName: str, *parameters: Array[object]) -> object
        InvokeMember(self: DynamicOperations, obj: object, memberName: str, ignoreCase: bool, *parameters: Array[object]) -> object
        """
        ...

    def IsCallable(self, o:object) -> bool:
        """ IsCallable(self: DynamicOperations, o: object) -> bool """
        ...

    def RemoveMember(self, obj:object, name:str, ignoreCase:bool = ...): # -> 
        """ RemoveMember(self: DynamicOperations, obj: object, name: str)RemoveMember(self: DynamicOperations, obj: object, name: str, ignoreCase: bool) """
        ...

    def SetMember(self, obj:object, name:str, value:object, ignoreCase:bool = ...): # -> 
        """ SetMember(self: DynamicOperations, obj: object, name: str, value: object)SetMember(self: DynamicOperations, obj: object, name: str, value: object, ignoreCase: bool)SetMember[T](self: DynamicOperations, obj: object, name: str, value: T)SetMember[T](self: DynamicOperations, obj: object, name: str, value: T, ignoreCase: bool) """
        ...

    def TryConvertTo(self, obj:object, *__args:Type) -> Tuple_[bool, object]:
        """
        TryConvertTo(self: DynamicOperations, obj: object, type: Type) -> (bool, object)
        TryConvertTo[T](self: DynamicOperations, obj: object) -> (bool, T)
        """
        ...

    def TryExplicitConvertTo(self, obj:object, *__args:Type) -> Tuple_[bool, object]:
        """
        TryExplicitConvertTo(self: DynamicOperations, obj: object, type: Type) -> (bool, object)
        TryExplicitConvertTo[T](self: DynamicOperations, obj: object) -> (bool, T)
        """
        ...

    def TryGetMember(self, obj:object, name:str, *__args:bool) -> Tuple_[bool, object]:
        """
        TryGetMember(self: DynamicOperations, obj: object, name: str) -> (bool, object)
        TryGetMember(self: DynamicOperations, obj: object, name: str, ignoreCase: bool) -> (bool, object)
        """
        ...

    def TryImplicitConvertTo(self, obj:object, *__args:Type) -> Tuple_[bool, object]:
        """
        TryImplicitConvertTo(self: DynamicOperations, obj: object, type: Type) -> (bool, object)
        TryImplicitConvertTo[T](self: DynamicOperations, obj: object) -> (bool, T)
        """
        ...

    def __dir__(self, *args): #cannot find CLR method
        """ GetMemberNames(self: DynamicOperations, obj: object) -> IList[str] """
        ...


class DynamicRuntimeHostingProvider: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def PlatformAdaptationLayer(self) -> PlatformAdaptationLayer:
        """ Get: PlatformAdaptationLayer(self: DynamicRuntimeHostingProvider) -> PlatformAdaptationLayer """
        ...



class DynamicStackFrame: # skipped bases: <type 'object'>, <type 'object'>
    """ DynamicStackFrame(method: MethodBase, funcName: str, filename: str, line: int) """
    def GetFileLineNumber(self) -> int:
        """ GetFileLineNumber(self: DynamicStackFrame) -> int """
        ...

    def GetFileName(self) -> str:
        """ GetFileName(self: DynamicStackFrame) -> str """
        ...

    def GetMethod(self) -> MethodBase:
        """ GetMethod(self: DynamicStackFrame) -> MethodBase """
        ...

    def GetMethodName(self) -> str:
        """ GetMethodName(self: DynamicStackFrame) -> str """
        ...

    def ToString(self) -> str:
        """ ToString(self: DynamicStackFrame) -> str """
        ...


class DynamicXamlReader: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def LoadComponent(scope:object, operations:DynamicOperations, *__args:XamlXmlReader) -> object:
        """
        LoadComponent(scope: object, operations: DynamicOperations, stream: Stream, schemaContext: XamlSchemaContext) -> object
        LoadComponent(scope: object, operations: DynamicOperations, filename: str, schemaContext: XamlSchemaContext) -> object
        LoadComponent(scope: object, operations: DynamicOperations, reader: XmlReader, schemaContext: XamlSchemaContext) -> object
        LoadComponent(scope: object, operations: DynamicOperations, reader: TextReader, schemaContext: XamlSchemaContext) -> object
        LoadComponent(scope: object, operations: DynamicOperations, reader: XamlXmlReader) -> object
        """
        ...

    __all__: list = ...


class ExceptionHelpers: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetExceptionStackTraces(rethrow:Exception) -> IList:
        """ GetExceptionStackTraces(rethrow: Exception) -> IList[StackTrace] """
        ...

    @staticmethod
    def UpdateForRethrow(rethrow:Exception) -> Exception:
        """ UpdateForRethrow(rethrow: Exception) -> Exception """
        ...

    __all__: list = ...


class ExplicitConversionMethodAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ExplicitConversionMethodAttribute() """
    pass

class Extensible: # skipped bases: <type 'object'>, <type 'object'>
    """
    Extensible[T]()
    Extensible[T](value: T)
    """
    @property
    def Value(self): # -> T
        """ Get: Value(self: Extensible[T]) -> T """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: Extensible[T], obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Extensible[T]) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Extensible[T]) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ExtensionTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ExtensionTypeAttribute(extends: Type, extensionType: Type) """
    @property
    def Extends(self) -> Type:
        """ Get: Extends(self: ExtensionTypeAttribute) -> Type """
        ...

    @property
    def ExtensionType(self) -> Type:
        """ Get: ExtensionType(self: ExtensionTypeAttribute) -> Type """
        ...


    def __new__(cls, extends:Type, extensionType:Type) -> Self:
        """ __new__(cls: type, extends: Type, extensionType: Type) """
        ...


class GeneratorNext(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ GeneratorNext[T](object: object, method: IntPtr) """
    def BeginInvoke(self, state:int, current, callback:AsyncCallback, object:object): # -> Tuple_[IAsyncResult, int, T] # Not found arg types: {'current': 'T'}
        """ BeginInvoke(self: GeneratorNext[T], state: int, current: T, callback: AsyncCallback, object: object) -> (IAsyncResult, int, T) """
        ...

    def EndInvoke(self, state:int, current, result:IAsyncResult): # -> Tuple_[int, T] # Not found arg types: {'current': 'T'}
        """ EndInvoke(self: GeneratorNext[T], state: int, current: T, result: IAsyncResult) -> (int, T) """
        ...

    def Invoke(self, state:int, current): # -> Tuple_[int, T] # Not found arg types: {'current': 'T'}
        """ Invoke(self: GeneratorNext[T], state: int, current: T) -> (int, T) """
        ...


class IConvertibleMetaObject: # skipped bases: <type 'object'>
    """ no doc """
    def CanConvertTo(self, type:Type, isExplicit:bool) -> bool:
        """ CanConvertTo(self: IConvertibleMetaObject, type: Type, isExplicit: bool) -> bool """
        ...


class IdDispenser: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetId(o:object) -> Int64:
        """ GetId(o: object) -> Int64 """
        ...

    @staticmethod
    def GetObject(id:Int64) -> object:
        """ GetObject(id: Int64) -> object """
        ...

    __all__: list = ...


class IDebuggableGenerator: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def YieldMarkerLocation(self) -> int:
        """
        Get: YieldMarkerLocation(self: IDebuggableGenerator) -> int
        Set: YieldMarkerLocation(self: IDebuggableGenerator) = value
        """
        ...



class IExpressionSerializable: # skipped bases: <type 'object'>
    """ no doc """
    def CreateExpression(self) -> Expression:
        """ CreateExpression(self: IExpressionSerializable) -> Expression """
        ...


class IMembersList: # skipped bases: <type 'object'>
    """ no doc """
    def GetMemberNames(self) -> IList:
        """ GetMemberNames(self: IMembersList) -> IList[str] """
        ...

    def __dir__(self, *args): #cannot find CLR method
        """ GetMemberNames(self: IMembersList) -> IList[str] """
        ...


class ImplicitConversionMethodAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ImplicitConversionMethodAttribute() """
    pass

class IRestrictedMetaObject: # skipped bases: <type 'object'>
    """ no doc """
    def Restrict(self, type:Type) -> DynamicMetaObject:
        """ Restrict(self: IRestrictedMetaObject, type: Type) -> DynamicMetaObject """
        ...


class ISlice: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Start(self) -> object:
        """ Get: Start(self: ISlice) -> object """
        ...

    @property
    def Step(self) -> object:
        """ Get: Step(self: ISlice) -> object """
        ...

    @property
    def Stop(self) -> object:
        """ Get: Stop(self: ISlice) -> object """
        ...



class LanguageContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CanCreateSourceCode(self) -> bool:
        """ Get: CanCreateSourceCode(self: LanguageContext) -> bool """
        ...

    @property
    def ContextId(self) -> ContextId:
        """ Get: ContextId(self: LanguageContext) -> ContextId """
        ...

    @property
    def DefaultEncoding(self) -> Encoding:
        """ Get: DefaultEncoding(self: LanguageContext) -> Encoding """
        ...

    @property
    def DomainManager(self): # -> ScriptDomainManager
        """ Get: DomainManager(self: LanguageContext) -> ScriptDomainManager """
        ...

    @property
    def LanguageGuid(self) -> Guid:
        """ Get: LanguageGuid(self: LanguageContext) -> Guid """
        ...

    @property
    def LanguageVersion(self) -> Version:
        """ Get: LanguageVersion(self: LanguageContext) -> Version """
        ...

    @property
    def Operations(self) -> DynamicOperations:
        """ Get: Operations(self: LanguageContext) -> DynamicOperations """
        ...

    @property
    def Options(self) -> LanguageOptions:
        """ Get: Options(self: LanguageContext) -> LanguageOptions """
        ...

    @property
    def VendorGuid(self) -> Guid:
        """ Get: VendorGuid(self: LanguageContext) -> Guid """
        ...


    def CompileSourceCode(self, sourceUnit:SourceUnit, options:CompilerOptions, errorSink:ErrorSink) -> ScriptCode:
        """ CompileSourceCode(self: LanguageContext, sourceUnit: SourceUnit, options: CompilerOptions, errorSink: ErrorSink) -> ScriptCode """
        ...

    def CreateBinaryOperationBinder(self, operation:ExpressionType) -> BinaryOperationBinder:
        """ CreateBinaryOperationBinder(self: LanguageContext, operation: ExpressionType) -> BinaryOperationBinder """
        ...

    def CreateCallBinder(self, name:str, ignoreCase:bool, callInfo:CallInfo) -> InvokeMemberBinder:
        """ CreateCallBinder(self: LanguageContext, name: str, ignoreCase: bool, callInfo: CallInfo) -> InvokeMemberBinder """
        ...

    def CreateConvertBinder(self, toType:Type, explicitCast:Nullable) -> ConvertBinder:
        """ CreateConvertBinder(self: LanguageContext, toType: Type, explicitCast: Nullable[bool]) -> ConvertBinder """
        ...

    def CreateCreateBinder(self, callInfo:CallInfo) -> CreateInstanceBinder:
        """ CreateCreateBinder(self: LanguageContext, callInfo: CallInfo) -> CreateInstanceBinder """
        ...

    def CreateDeleteMemberBinder(self, name:str, ignoreCase:bool) -> DeleteMemberBinder:
        """ CreateDeleteMemberBinder(self: LanguageContext, name: str, ignoreCase: bool) -> DeleteMemberBinder """
        ...

    def CreateFileUnit(self, path:str, *__args:Encoding) -> SourceUnit:
        """
        CreateFileUnit(self: LanguageContext, path: str) -> SourceUnit
        CreateFileUnit(self: LanguageContext, path: str, encoding: Encoding) -> SourceUnit
        CreateFileUnit(self: LanguageContext, path: str, encoding: Encoding, kind: SourceCodeKind) -> SourceUnit
        CreateFileUnit(self: LanguageContext, path: str, content: str) -> SourceUnit
        """
        ...

    def CreateGetMemberBinder(self, name:str, ignoreCase:bool) -> GetMemberBinder:
        """ CreateGetMemberBinder(self: LanguageContext, name: str, ignoreCase: bool) -> GetMemberBinder """
        ...

    def CreateInvokeBinder(self, callInfo:CallInfo) -> InvokeBinder:
        """ CreateInvokeBinder(self: LanguageContext, callInfo: CallInfo) -> InvokeBinder """
        ...

    def CreateScope(self, *__args:IDictionary) -> Scope:
        """
        CreateScope(self: LanguageContext) -> Scope
        CreateScope(self: LanguageContext, dictionary: IDictionary[str, object]) -> Scope
        CreateScope(self: LanguageContext, storage: IDynamicMetaObjectProvider) -> Scope
        """
        ...

    def CreateScopeExtension(self, scope:Scope): # -> ScopeExtension
        """ CreateScopeExtension(self: LanguageContext, scope: Scope) -> ScopeExtension """
        ...

    def CreateSetMemberBinder(self, name:str, ignoreCase:bool) -> SetMemberBinder:
        """ CreateSetMemberBinder(self: LanguageContext, name: str, ignoreCase: bool) -> SetMemberBinder """
        ...

    def CreateSnippet(self, code:str, *__args:SourceCodeKind) -> SourceUnit:
        """
        CreateSnippet(self: LanguageContext, code: str, kind: SourceCodeKind) -> SourceUnit
        CreateSnippet(self: LanguageContext, code: str, id: str, kind: SourceCodeKind) -> SourceUnit
        """
        ...

    def CreateSourceUnit(self, contentProvider:TextContentProvider, path:str, *__args:SourceCodeKind) -> SourceUnit:
        """
        CreateSourceUnit(self: LanguageContext, contentProvider: StreamContentProvider, path: str, encoding: Encoding, kind: SourceCodeKind) -> SourceUnit
        CreateSourceUnit(self: LanguageContext, contentProvider: TextContentProvider, path: str, kind: SourceCodeKind) -> SourceUnit
        """
        ...

    def CreateUnaryOperationBinder(self, operation:ExpressionType) -> UnaryOperationBinder:
        """ CreateUnaryOperationBinder(self: LanguageContext, operation: ExpressionType) -> UnaryOperationBinder """
        ...

    def EnsureScopeExtension(self, scope:Scope): # -> ScopeExtension
        """ EnsureScopeExtension(self: LanguageContext, scope: Scope) -> ScopeExtension """
        ...

    def ExecuteProgram(self, program:SourceUnit) -> int:
        """ ExecuteProgram(self: LanguageContext, program: SourceUnit) -> int """
        ...

    def FormatException(self, exception:Exception) -> str:
        """ FormatException(self: LanguageContext, exception: Exception) -> str """
        ...

    def FormatObject(self, operations:DynamicOperations, obj:object) -> str:
        """ FormatObject(self: LanguageContext, operations: DynamicOperations, obj: object) -> str """
        ...

    def GenerateSourceCode(self, codeDom:CodeObject, path:str, kind:SourceCodeKind) -> SourceUnit:
        """ GenerateSourceCode(self: LanguageContext, codeDom: CodeObject, path: str, kind: SourceCodeKind) -> SourceUnit """
        ...

    def GetCallSignatures(self, obj:object) -> IList:
        """ GetCallSignatures(self: LanguageContext, obj: object) -> IList[str] """
        ...

    def GetCompilerErrorSink(self) -> ErrorSink:
        """ GetCompilerErrorSink(self: LanguageContext) -> ErrorSink """
        ...

    def GetCompilerOptions(self, scope:Scope = ...) -> CompilerOptions:
        """
        GetCompilerOptions(self: LanguageContext) -> CompilerOptions
        GetCompilerOptions(self: LanguageContext, scope: Scope) -> CompilerOptions
        """
        ...

    def GetDocumentation(self, obj:object) -> str:
        """ GetDocumentation(self: LanguageContext, obj: object) -> str """
        ...

    def GetExceptionMessage(self, exception, message, errorTypeName) -> Tuple_[str, str]:
        """ GetExceptionMessage(self: LanguageContext, exception: Exception) -> (str, str) """
        ...

    def GetMemberNames(self, obj:object) -> IList:
        """ GetMemberNames(self: LanguageContext, obj: object) -> IList[str] """
        ...

    def GetScope(self, path:str) -> Scope:
        """ GetScope(self: LanguageContext, path: str) -> Scope """
        ...

    def GetSearchPaths(self) -> ICollection:
        """ GetSearchPaths(self: LanguageContext) -> ICollection[str] """
        ...

    def GetService(self, args:Array): # -> TService
        """ GetService[TService](self: LanguageContext, *args: Array[object]) -> TService """
        ...

    def GetSourceReader(self, stream:Stream, defaultEncoding:Encoding, path:str) -> SourceCodeReader:
        """ GetSourceReader(self: LanguageContext, stream: Stream, defaultEncoding: Encoding, path: str) -> SourceCodeReader """
        ...

    def GetStackFrames(self, exception:Exception) -> IList:
        """ GetStackFrames(self: LanguageContext, exception: Exception) -> IList[DynamicStackFrame] """
        ...

    def IsCallable(self, obj:object) -> bool:
        """ IsCallable(self: LanguageContext, obj: object) -> bool """
        ...

    def LoadCompiledCode(self, method:Delegate, path:str, customData:str) -> ScriptCode:
        """ LoadCompiledCode(self: LanguageContext, method: Delegate, path: str, customData: str) -> ScriptCode """
        ...

    def ScopeGetVariable(self, scope:Scope, name:str) -> object:
        """
        ScopeGetVariable(self: LanguageContext, scope: Scope, name: str) -> object
        ScopeGetVariable[T](self: LanguageContext, scope: Scope, name: str) -> T
        """
        ...

    def ScopeSetVariable(self, scope:Scope, name:str, value:object): # -> 
        """ ScopeSetVariable(self: LanguageContext, scope: Scope, name: str, value: object) """
        ...

    def ScopeTryGetVariable(self, scope, name, value) -> Tuple_[bool, object]:
        """ ScopeTryGetVariable(self: LanguageContext, scope: Scope, name: str) -> (bool, object) """
        ...

    def SetSearchPaths(self, paths:ICollection): # -> 
        """ SetSearchPaths(self: LanguageContext, paths: ICollection[str]) """
        ...

    def Shutdown(self): # -> 
        """ Shutdown(self: LanguageContext) """
        ...

    def __dir__(self, *args): #cannot find CLR method
        """ GetMemberNames(self: LanguageContext, obj: object) -> IList[str] """
        ...


class LightExceptions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CheckAndThrow(*__args:object) -> object:
        """
        CheckAndThrow(value: object) -> object
        CheckAndThrow(expr: Expression) -> Expression
        """
        ...

    @staticmethod
    def GetLightException(exceptionValue:object) -> Exception:
        """ GetLightException(exceptionValue: object) -> Exception """
        ...

    @staticmethod
    def IsLightException(value:object) -> bool:
        """ IsLightException(value: object) -> bool """
        ...

    @staticmethod
    def Rewrite(expression:Expression) -> Expression:
        """ Rewrite(expression: Expression) -> Expression """
        ...

    @staticmethod
    def RewriteExternal(expression:Expression) -> Expression:
        """ RewriteExternal(expression: Expression) -> Expression """
        ...

    @staticmethod
    def RewriteLazy(expression:Expression) -> Expression:
        """ RewriteLazy(expression: Expression) -> Expression """
        ...

    @staticmethod
    def SupportsLightThrow(binder:CallSiteBinder) -> bool:
        """ SupportsLightThrow(binder: CallSiteBinder) -> bool """
        ...

    @staticmethod
    def Throw(*__args:Exception) -> object:
        """
        Throw(exceptionValue: Exception) -> object
        Throw(exceptionValue: Expression) -> Expression
        Throw(exceptionValue: Expression, retType: Type) -> Expression
        Throw(binder: DynamicMetaObjectBinder, exceptionValue: Expression) -> Expression
        Throw(binder: DynamicMetaObjectBinder, exceptionValue: Expression, retType: Type) -> Expression
        """
        ...

    __all__: list = ...


class LightThrowingAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ LightThrowingAttribute() """
    pass

class LocalsDictionary(CustomStringDictionary): # skipped bases: <type 'IEnumerable[KeyValuePair[object, object]]'>, <type 'dict'>, <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection[KeyValuePair[object, object]]'>, <type 'ICollection'>, <type 'object'>
    """ LocalsDictionary(locals: IRuntimeVariables, symbols: Array[str]) """
    def __new__(cls, locals:IRuntimeVariables, symbols:Array) -> Self:
        """ __new__(cls: type, locals: IRuntimeVariables, symbols: Array[str]) """
        ...


class MetaObjectExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Clone(self, *__args:Expression) -> DynamicMetaObject:
        """
        Clone(self: DynamicMetaObject, newExpression: Expression) -> DynamicMetaObject
        Clone(self: DynamicMetaObject, newRestrictions: BindingRestrictions) -> DynamicMetaObject
        Clone(self: DynamicMetaObject, newExpression: Expression, newRestrictions: BindingRestrictions) -> DynamicMetaObject
        """
        ...

    @staticmethod
    def GetLimitType(self) -> Type:
        """ GetLimitType(self: DynamicMetaObject) -> Type """
        ...

    @staticmethod
    def GetRuntimeType(self) -> Type:
        """ GetRuntimeType(self: DynamicMetaObject) -> Type """
        ...

    @staticmethod
    def NeedsDeferral(self) -> bool:
        """ NeedsDeferral(self: DynamicMetaObject) -> bool """
        ...

    @staticmethod
    def Restrict(self, type:Type) -> DynamicMetaObject:
        """ Restrict(self: DynamicMetaObject, type: Type) -> DynamicMetaObject """
        ...

    __all__: list = ...


class ModuleChangeEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    ModuleChangeEventArgs(name: str, changeType: ModuleChangeType)
    ModuleChangeEventArgs(name: str, changeType: ModuleChangeType, value: object)
    """
    @property
    def ChangeType(self) -> ModuleChangeType:
        """ Get: ChangeType(self: ModuleChangeEventArgs) -> ModuleChangeType """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ModuleChangeEventArgs) -> str """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: ModuleChangeEventArgs) -> object """
        ...


    def __new__(cls, name:str, changeType:ModuleChangeType, value:object = ...) -> Self:
        """
        __new__(cls: type, name: str, changeType: ModuleChangeType)
        __new__(cls: type, name: str, changeType: ModuleChangeType, value: object)
        """
        ...


class ModuleChangeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ModuleChangeType, values: Delete (1), Set (0) """
    Delete: ModuleChangeType = ...
    Set: ModuleChangeType = ...
    value__ = ...


class NotNullAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ NotNullAttribute() """
    pass

class NotNullItemsAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ NotNullItemsAttribute() """
    pass

class NullTextContentProvider(TextContentProvider): # skipped bases: <type 'object'>
    """ no doc """
    Null: NullTextContentProvider = ...


class ObjectDictionaryExpando(IDynamicMetaObjectProvider): # skipped bases: <type 'object'>
    """ ObjectDictionaryExpando(dictionary: dict) """
    @property
    def Dictionary(self) -> dict:
        """ Get: Dictionary(self: ObjectDictionaryExpando) -> dict """
        ...



class OperationFailed: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Value = ...


class OperatorSlotAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ OperatorSlotAttribute() """
    pass

class ParserSink: # skipped bases: <type 'object'>, <type 'object'>
    """ ParserSink() """
    def EndParameters(self, span:SourceSpan): # -> 
        """ EndParameters(self: ParserSink, span: SourceSpan) """
        ...

    def MatchPair(self, opening:SourceSpan, closing:SourceSpan, priority:int): # -> 
        """ MatchPair(self: ParserSink, opening: SourceSpan, closing: SourceSpan, priority: int) """
        ...

    def MatchTriple(self, opening:SourceSpan, middle:SourceSpan, closing:SourceSpan, priority:int): # -> 
        """ MatchTriple(self: ParserSink, opening: SourceSpan, middle: SourceSpan, closing: SourceSpan, priority: int) """
        ...

    def NextParameter(self, span:SourceSpan): # -> 
        """ NextParameter(self: ParserSink, span: SourceSpan) """
        ...

    def QualifyName(self, selector:SourceSpan, span:SourceSpan, name:str): # -> 
        """ QualifyName(self: ParserSink, selector: SourceSpan, span: SourceSpan, name: str) """
        ...

    def StartName(self, span:SourceSpan, name:str): # -> 
        """ StartName(self: ParserSink, span: SourceSpan, name: str) """
        ...

    def StartParameters(self, context:SourceSpan): # -> 
        """ StartParameters(self: ParserSink, context: SourceSpan) """
        ...

    Null: ParserSink = ...


class PositionTrackingWriter(StringWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ PositionTrackingWriter() """
    def GetFileMap(self) -> Array:
        """ GetFileMap(self: PositionTrackingWriter) -> Array[KeyValuePair[int, str]] """
        ...

    def GetLineMap(self) -> Array:
        """ GetLineMap(self: PositionTrackingWriter) -> Array[KeyValuePair[int, int]] """
        ...

    def MapLocation(self, linePragma:CodeLinePragma): # -> 
        """ MapLocation(self: PositionTrackingWriter, linePragma: CodeLinePragma) """
        ...

    CoreNewLine = ...


class PropertyMethodAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PropertyMethodAttribute() """
    pass

class ReflectionCache: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetMethodGroup(name:str, *__args:Array) -> MethodGroup:
        """
        GetMethodGroup(name: str, methods: Array[MethodBase]) -> MethodGroup
        GetMethodGroup(name: str, mems: MemberGroup) -> MethodGroup
        """
        ...

    @staticmethod
    def GetTypeTracker(type:Type): # -> type-collision
        """ GetTypeTracker(type: Type) -> type-collision """
        ...

    def MethodBaseCache(self, *args): #cannot find CLR method
        """ MethodBaseCache(name: str, members: Array[MethodBase]) """
        ...

    __all__: list = ...


class RestrictedMetaObject(DynamicMetaObject, IRestrictedMetaObject): # skipped bases: <type 'object'>
    """
    RestrictedMetaObject(expression: Expression, restriction: BindingRestrictions, value: object)
    RestrictedMetaObject(expression: Expression, restriction: BindingRestrictions)
    """
    pass

class Scope(IDynamicMetaObjectProvider): # skipped bases: <type 'object'>
    """
    Scope()
    Scope(dictionary: IDictionary[str, object])
    Scope(storage: IDynamicMetaObjectProvider)
    """
    @property
    def Storage(self) -> object:
        """ Get: Storage(self: Scope) -> object """
        ...


    def GetExtension(self, languageContextId:ContextId): # -> ScopeExtension
        """ GetExtension(self: Scope, languageContextId: ContextId) -> ScopeExtension """
        ...

    def SetExtension(self, languageContextId:ContextId, extension): # -> ScopeExtension # Not found arg types: {'extension': 'ScopeExtension'}
        """ SetExtension(self: Scope, languageContextId: ContextId, extension: ScopeExtension) -> ScopeExtension """
        ...


class ScopeExtension: # skipped bases: <type 'object'>, <type 'object'>
    """ ScopeExtension(scope: Scope) """
    @property
    def Scope(self) -> Scope:
        """ Get: Scope(self: ScopeExtension) -> Scope """
        ...


    EmptyArray = ...


class ScriptDomainManager: # skipped bases: <type 'object'>, <type 'object'>
    """ ScriptDomainManager(hostingProvider: DynamicRuntimeHostingProvider, configuration: DlrConfiguration) """
    @property
    def Configuration(self) -> DlrConfiguration:
        """ Get: Configuration(self: ScriptDomainManager) -> DlrConfiguration """
        ...

    @property
    def Globals(self) -> Scope:
        """
        Get: Globals(self: ScriptDomainManager) -> Scope
        Set: Globals(self: ScriptDomainManager) = value
        """
        ...

    @property
    def Host(self) -> DynamicRuntimeHostingProvider:
        """ Get: Host(self: ScriptDomainManager) -> DynamicRuntimeHostingProvider """
        ...

    @property
    def Platform(self) -> PlatformAdaptationLayer:
        """ Get: Platform(self: ScriptDomainManager) -> PlatformAdaptationLayer """
        ...

    @property
    def SharedIO(self): # -> SharedIO
        """ Get: SharedIO(self: ScriptDomainManager) -> SharedIO """
        ...


    def GetLanguage(self, providerType:Type) -> LanguageContext:
        """ GetLanguage(self: ScriptDomainManager, providerType: Type) -> LanguageContext """
        ...

    def GetLanguageByExtension(self, fileExtension:str) -> LanguageContext:
        """ GetLanguageByExtension(self: ScriptDomainManager, fileExtension: str) -> LanguageContext """
        ...

    def GetLanguageByName(self, languageName:str) -> LanguageContext:
        """ GetLanguageByName(self: ScriptDomainManager, languageName: str) -> LanguageContext """
        ...

    def GetLanguageByTypeName(self, providerAssemblyQualifiedTypeName:str) -> LanguageContext:
        """ GetLanguageByTypeName(self: ScriptDomainManager, providerAssemblyQualifiedTypeName: str) -> LanguageContext """
        ...

    def GetLoadedAssemblyList(self) -> IList:
        """ GetLoadedAssemblyList(self: ScriptDomainManager) -> IList[Assembly] """
        ...

    def LoadAssembly(self, assembly:Assembly) -> bool:
        """ LoadAssembly(self: ScriptDomainManager, assembly: Assembly) -> bool """
        ...

    def TryGetLanguage(self, languageName, language) -> Tuple_[bool, LanguageContext]:
        """ TryGetLanguage(self: ScriptDomainManager, languageName: str) -> (bool, LanguageContext) """
        ...

    def TryGetLanguageByFileExtension(self, fileExtension, language) -> Tuple_[bool, LanguageContext]:
        """ TryGetLanguageByFileExtension(self: ScriptDomainManager, fileExtension: str) -> (bool, LanguageContext) """
        ...

    AssemblyLoaded = ...


class ScriptingRuntimeHelpers: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def BooleanToObject(value:bool) -> object:
        """ BooleanToObject(value: bool) -> object """
        ...

    @staticmethod
    def CannotConvertError(toType:Type, value:object) -> Exception:
        """ CannotConvertError(toType: Type, value: object) -> Exception """
        ...

    @staticmethod
    def CharToString(ch:Char) -> str:
        """ CharToString(ch: Char) -> str """
        ...

    @staticmethod
    def CheckDictionaryMembers(dict:IDictionary, names:Array) -> bool:
        """ CheckDictionaryMembers(dict: IDictionary, names: Array[str]) -> bool """
        ...

    @staticmethod
    def CreateArray(args:int) -> Array:
        """ CreateArray[T](args: int) -> Array[T] """
        ...

    @staticmethod
    def CreateInstance(): # -> T
        """ CreateInstance[T]() -> T """
        ...

    @staticmethod
    def GetEventHandlerType(eventInfo:EventInfo) -> Type:
        """ GetEventHandlerType(eventInfo: EventInfo) -> Type """
        ...

    @staticmethod
    def GetStringMembers(members:IList) -> IList:
        """ GetStringMembers(members: IList[object]) -> IList[str] """
        ...

    @staticmethod
    def IncorrectBoxType(received:object): # -> T
        """ IncorrectBoxType[T](received: object) -> T """
        ...

    @staticmethod
    def Int32ToObject(value:int) -> object:
        """ Int32ToObject(value: int) -> object """
        ...

    @staticmethod
    def InterpretedCallSiteTest(restrictionResult:bool, bindingInfo:object) -> bool:
        """ InterpretedCallSiteTest(restrictionResult: bool, bindingInfo: object) -> bool """
        ...

    @staticmethod
    def MakeGenerator(next, yieldMarkers:Array = ...) -> IEnumerable: # Not found arg types: {'next': 'Func'}
        """
        MakeGenerator[T](next: Func[GeneratorNext[T]]) -> IEnumerable[T]
        MakeGenerator[T](next: GeneratorNext[T]) -> IEnumerator[T]
        MakeGenerator[T](next: Func[GeneratorNext[T]], yieldMarkers: Array[int]) -> IEnumerable[T]
        MakeGenerator[T](next: GeneratorNext[T], yieldMarkers: Array[int]) -> IEnumerator[T]
        """
        ...

    @staticmethod
    def MakeIncorrectBoxTypeError(type:Type, received:object) -> Exception:
        """ MakeIncorrectBoxTypeError(type: Type, received: object) -> Exception """
        ...

    @staticmethod
    def ReadOnlyAssignError(field:bool, fieldName:str) -> object:
        """ ReadOnlyAssignError(field: bool, fieldName: str) -> object """
        ...

    @staticmethod
    def SetEvent(eventTracker:EventTracker, value:object): # -> 
        """ SetEvent(eventTracker: EventTracker, value: object) """
        ...

    @staticmethod
    def ShiftParamsArray(array:Array, count:int) -> Array:
        """ ShiftParamsArray[T](array: Array[T], count: int) -> Array[T] """
        ...

    @staticmethod
    def SimpleAttributeError(message:str) -> Exception:
        """ SimpleAttributeError(message: str) -> Exception """
        ...

    @staticmethod
    def SimpleTypeError(message:str) -> ArgumentTypeException:
        """ SimpleTypeError(message: str) -> ArgumentTypeException """
        ...

    __all__: list = ...


class SharedIO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ErrorEncoding(self) -> Encoding:
        """ Get: ErrorEncoding(self: SharedIO) -> Encoding """
        ...

    @property
    def ErrorStream(self) -> Stream:
        """ Get: ErrorStream(self: SharedIO) -> Stream """
        ...

    @property
    def ErrorWriter(self) -> TextWriter:
        """ Get: ErrorWriter(self: SharedIO) -> TextWriter """
        ...

    @property
    def InputEncoding(self) -> Encoding:
        """ Get: InputEncoding(self: SharedIO) -> Encoding """
        ...

    @property
    def InputReader(self) -> TextReader:
        """ Get: InputReader(self: SharedIO) -> TextReader """
        ...

    @property
    def InputStream(self) -> Stream:
        """ Get: InputStream(self: SharedIO) -> Stream """
        ...

    @property
    def OutputEncoding(self) -> Encoding:
        """ Get: OutputEncoding(self: SharedIO) -> Encoding """
        ...

    @property
    def OutputStream(self) -> Stream:
        """ Get: OutputStream(self: SharedIO) -> Stream """
        ...

    @property
    def OutputWriter(self) -> TextWriter:
        """ Get: OutputWriter(self: SharedIO) -> TextWriter """
        ...


    def GetEncoding(self, type:ConsoleStreamType) -> Encoding:
        """ GetEncoding(self: SharedIO, type: ConsoleStreamType) -> Encoding """
        ...

    def GetReader(self, encoding) -> Tuple_[TextReader, Encoding]:
        """ GetReader(self: SharedIO) -> (TextReader, Encoding) """
        ...

    def GetStream(self, type:ConsoleStreamType) -> Stream:
        """ GetStream(self: SharedIO, type: ConsoleStreamType) -> Stream """
        ...

    def GetStreamProxy(self, type:ConsoleStreamType) -> Stream:
        """ GetStreamProxy(self: SharedIO, type: ConsoleStreamType) -> Stream """
        ...

    def GetWriter(self, type:ConsoleStreamType) -> TextWriter:
        """ GetWriter(self: SharedIO, type: ConsoleStreamType) -> TextWriter """
        ...

    def RedirectToConsole(self): # -> 
        """ RedirectToConsole(self: SharedIO) """
        ...

    def SetErrorOutput(self, stream:Stream, writer:TextWriter): # -> 
        """ SetErrorOutput(self: SharedIO, stream: Stream, writer: TextWriter) """
        ...

    def SetInput(self, stream:Stream, reader:TextReader, encoding:Encoding): # -> 
        """ SetInput(self: SharedIO, stream: Stream, reader: TextReader, encoding: Encoding) """
        ...

    def SetOutput(self, stream:Stream, writer:TextWriter): # -> 
        """ SetOutput(self: SharedIO, stream: Stream, writer: TextWriter) """
        ...


class StaticExtensionMethodAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ StaticExtensionMethodAttribute() """
    pass

class StringDictionaryExpando(IDynamicMetaObjectProvider): # skipped bases: <type 'object'>
    """ StringDictionaryExpando(data: IDictionary[str, object]) """
    @property
    def Dictionary(self) -> IDictionary:
        """ Get: Dictionary(self: StringDictionaryExpando) -> IDictionary[str, object] """
        ...



class TokenizerBuffer: # skipped bases: <type 'object'>, <type 'object'>
    """ TokenizerBuffer(reader: TextReader, initialLocation: SourceLocation, initialCapacity: int, multiEolns: bool) """
    @property
    def AtBeginning(self) -> bool:
        """ Get: AtBeginning(self: TokenizerBuffer) -> bool """
        ...

    @property
    def Position(self) -> int:
        """ Get: Position(self: TokenizerBuffer) -> int """
        ...

    @property
    def Reader(self) -> TextReader:
        """ Get: Reader(self: TokenizerBuffer) -> TextReader """
        ...

    @property
    def TokenEnd(self) -> SourceLocation:
        """ Get: TokenEnd(self: TokenizerBuffer) -> SourceLocation """
        ...

    @property
    def TokenLength(self) -> int:
        """ Get: TokenLength(self: TokenizerBuffer) -> int """
        ...

    @property
    def TokenRelativePosition(self) -> int:
        """ Get: TokenRelativePosition(self: TokenizerBuffer) -> int """
        ...

    @property
    def TokenSpan(self) -> SourceSpan:
        """ Get: TokenSpan(self: TokenizerBuffer) -> SourceSpan """
        ...

    @property
    def TokenStart(self) -> SourceLocation:
        """ Get: TokenStart(self: TokenizerBuffer) -> SourceLocation """
        ...


    def Back(self): # -> 
        """ Back(self: TokenizerBuffer) """
        ...

    def DiscardToken(self): # -> 
        """ DiscardToken(self: TokenizerBuffer) """
        ...

    def GetChar(self, offset:int) -> Char:
        """ GetChar(self: TokenizerBuffer, offset: int) -> Char """
        ...

    def GetCharRelative(self, disp:int) -> Char:
        """ GetCharRelative(self: TokenizerBuffer, disp: int) -> Char """
        ...

    def GetTokenString(self) -> str:
        """ GetTokenString(self: TokenizerBuffer) -> str """
        ...

    def GetTokenSubstring(self, offset:int, length:int = ...) -> str:
        """
        GetTokenSubstring(self: TokenizerBuffer, offset: int) -> str
        GetTokenSubstring(self: TokenizerBuffer, offset: int, length: int) -> str
        """
        ...

    def Initialize(self, reader:TextReader, initialLocation:SourceLocation, initialCapacity:int, multiEolns:bool): # -> 
        """ Initialize(self: TokenizerBuffer, reader: TextReader, initialLocation: SourceLocation, initialCapacity: int, multiEolns: bool) """
        ...

    def IsEoln(self, current:int) -> bool:
        """ IsEoln(self: TokenizerBuffer, current: int) -> bool """
        ...

    def MarkMultiLineTokenEnd(self, disp:int = ...): # -> 
        """ MarkMultiLineTokenEnd(self: TokenizerBuffer, disp: int)MarkMultiLineTokenEnd(self: TokenizerBuffer) """
        ...

    def MarkSingleLineTokenEnd(self, disp:int = ...): # -> 
        """ MarkSingleLineTokenEnd(self: TokenizerBuffer, disp: int)MarkSingleLineTokenEnd(self: TokenizerBuffer) """
        ...

    def MarkTokenEnd(self, isMultiLine:bool): # -> 
        """ MarkTokenEnd(self: TokenizerBuffer, isMultiLine: bool) """
        ...

    def Peek(self) -> int:
        """ Peek(self: TokenizerBuffer) -> int """
        ...

    def Read(self, *__args:int) -> bool:
        """
        Read(self: TokenizerBuffer) -> int
        Read(self: TokenizerBuffer, ch: int) -> bool
        Read(self: TokenizerBuffer, str: str) -> bool
        """
        ...

    def ReadEolnOpt(self, current:int) -> int:
        """ ReadEolnOpt(self: TokenizerBuffer, current: int) -> int """
        ...

    def ReadLine(self) -> int:
        """ ReadLine(self: TokenizerBuffer) -> int """
        ...

    def Seek(self, offset:int): # -> 
        """ Seek(self: TokenizerBuffer, offset: int) """
        ...

    def SeekRelative(self, disp:int): # -> 
        """ SeekRelative(self: TokenizerBuffer, disp: int) """
        ...

    EndOfFile: int = ...
    InvalidCharacter: int = ...


class TokenizerService: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CurrentPosition(self) -> SourceLocation:
        """ Get: CurrentPosition(self: TokenizerService) -> SourceLocation """
        ...

    @property
    def CurrentState(self) -> object:
        """ Get: CurrentState(self: TokenizerService) -> object """
        ...

    @property
    def ErrorSink(self) -> ErrorSink:
        """
        Get: ErrorSink(self: TokenizerService) -> ErrorSink
        Set: ErrorSink(self: TokenizerService) = value
        """
        ...

    @property
    def IsRestartable(self) -> bool:
        """ Get: IsRestartable(self: TokenizerService) -> bool """
        ...


    def Initialize(self, state:object, sourceReader:TextReader, sourceUnit:SourceUnit, initialLocation:SourceLocation): # -> 
        """ Initialize(self: TokenizerService, state: object, sourceReader: TextReader, sourceUnit: SourceUnit, initialLocation: SourceLocation) """
        ...

    def ReadToken(self) -> TokenInfo:
        """ ReadToken(self: TokenizerService) -> TokenInfo """
        ...

    def ReadTokens(self, characterCount:int) -> IEnumerable:
        """ ReadTokens(self: TokenizerService, characterCount: int) -> IEnumerable[TokenInfo] """
        ...

    def SkipToken(self) -> bool:
        """ SkipToken(self: TokenizerService) -> bool """
        ...

    def SkipTokens(self, countOfChars:int) -> bool:
        """ SkipTokens(self: TokenizerService, countOfChars: int) -> bool """
        ...


class Uninitialized: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Instance: Uninitialized = ...


