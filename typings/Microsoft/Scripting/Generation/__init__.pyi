# encoding: utf-8
# module Microsoft.Scripting.Generation calls itself Generation
# from Microsoft.Dynamic, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Byte, Char, Decimal, Delegate, 
    IAsyncResult, Int16, Int64, MulticastDelegate, SByte, Single, Type, 
    UInt16, UInt32, UInt64)

from System.Collections import IEnumerable, IList

from System.ComponentModel import TypeConverter

from System.Diagnostics.SymbolStore import ISymbolDocumentWriter

from System.Linq.Expressions import (DynamicExpression, Expression, 
    ExpressionType, LambdaExpression)

from System.Reflection import (Assembly, ConstructorInfo, FieldInfo, 
    MemberInfo, MethodAttributes, MethodBase, MethodInfo, PropertyInfo)

from System.Reflection.Emit import (AssemblyBuilder, FieldBuilder, Label, 
    LocalBuilder, MethodBuilder, ModuleBuilder, OpCode, SignatureHelper, 
    TypeBuilder)

from System.Runtime.InteropServices import CallingConvention

from typing import Tuple as Tuple_

"""The following names are not found in the module: T, T0, T1, long
"""

# no functions
# classes

class ActionRef(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ActionRef[T0, T1](object: object, method: IntPtr) """
    def BeginInvoke(self, arg0, arg1, callback:AsyncCallback, object:object): # -> Tuple_[IAsyncResult, T0, T1] # Not found arg types: {'arg1': 'T1', 'arg0': 'T0'}
        """ BeginInvoke(self: ActionRef[T0, T1], arg0: T0, arg1: T1, callback: AsyncCallback, object: object) -> (IAsyncResult, T0, T1) """
        ...

    def EndInvoke(self, arg0, arg1, result:IAsyncResult): # -> Tuple_[T0, T1] # Not found arg types: {'arg1': 'T1', 'arg0': 'T0'}
        """ EndInvoke(self: ActionRef[T0, T1], arg0: T0, arg1: T1, result: IAsyncResult) -> (T0, T1) """
        ...

    def Invoke(self, arg0, arg1): # -> Tuple_[T0, T1] # Not found arg types: {'arg1': 'T1', 'arg0': 'T0'}
        """ Invoke(self: ActionRef[T0, T1], arg0: T0, arg1: T1) -> (T0, T1) """
        ...


class AssemblyGen: # skipped bases: <type 'object'>, <type 'object'>
    """ AssemblyGen(name: AssemblyName, outDir: str, outFileExtension: str, isDebuggable: bool, attrs: IDictionary[str, object]) """
    @property
    def AssemblyBuilder(self) -> AssemblyBuilder:
        """ Get: AssemblyBuilder(self: AssemblyGen) -> AssemblyBuilder """
        ...

    @property
    def ModuleBuilder(self) -> ModuleBuilder:
        """ Get: ModuleBuilder(self: AssemblyGen) -> ModuleBuilder """
        ...


    def DefinePublicType(self, name:str, parent:Type, preserveName:bool) -> TypeBuilder:
        """ DefinePublicType(self: AssemblyGen, name: str, parent: Type, preserveName: bool) -> TypeBuilder """
        ...

    def MakeDelegateType(self, name:str, parameters:Array, returnType:Type) -> Type:
        """ MakeDelegateType(self: AssemblyGen, name: str, parameters: Array[Type], returnType: Type) -> Type """
        ...

    def SaveAssembly(self) -> str:
        """ SaveAssembly(self: AssemblyGen) -> str """
        ...


class CompilerHelpers: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CanEmitConstant(value:object, type:Type) -> bool:
        """ CanEmitConstant(value: object, type: Type) -> bool """
        ...

    @staticmethod
    def CanOptimizeMethod(method:MethodBase) -> bool:
        """ CanOptimizeMethod(method: MethodBase) -> bool """
        ...

    @staticmethod
    def Compile(lambda_:Expression, emitDebugSymbols:bool): # -> T
        """ Compile[T](lambda: Expression[T], emitDebugSymbols: bool) -> T """
        ...

    @staticmethod
    def CompileToMethod(lambda_, *__args): # -> 
        """
        CompileToMethod(lambda: LambdaExpression, method: MethodBuilder, emitDebugSymbols: bool)CompileToMethod(lambda: LambdaExpression, debugInfoGenerator: DebugInfoGenerator, emitDebugSymbols: bool) -> Delegate
        CompileToMethod[T](lambda: Expression[T], debugInfoGenerator: DebugInfoGenerator, emitDebugSymbols: bool) -> T
        """
        ...

    @staticmethod
    def CreateBigInt(*__args:int): # -> long
        """
        CreateBigInt(value: int) -> long
        CreateBigInt(value: Int64) -> long
        CreateBigInt(isNegative: bool, data: Array[Byte]) -> long
        """
        ...

    @staticmethod
    def CreateBigInteger(*__args:int): # -> long
        """
        CreateBigInteger(value: int) -> long
        CreateBigInteger(value: Int64) -> long
        CreateBigInteger(isNegative: bool, data: Array[Byte]) -> long
        """
        ...

    @staticmethod
    def FilterConstructorsToPublicAndProtected(ctors:IEnumerable) -> IEnumerable:
        """ FilterConstructorsToPublicAndProtected(ctors: IEnumerable[ConstructorInfo]) -> IEnumerable[ConstructorInfo] """
        ...

    @staticmethod
    def FilterNonVisibleMembers(targetType:Type, members:IEnumerable) -> IEnumerable:
        """ FilterNonVisibleMembers(targetType: Type, members: IEnumerable[MemberInfo]) -> IEnumerable[MemberInfo] """
        ...

    @staticmethod
    def FilterNonVisibleMembersIterator(targetType:Type, members:IEnumerable) -> IEnumerable:
        """ FilterNonVisibleMembersIterator(targetType: Type, members: IEnumerable[MemberInfo]) -> IEnumerable[MemberInfo] """
        ...

    @staticmethod
    def GetConstructors(t:Type, privateBinding:bool, includeProtected:bool = ...) -> Array:
        """
        GetConstructors(t: Type, privateBinding: bool) -> Array[MethodBase]
        GetConstructors(t: Type, privateBinding: bool, includeProtected: bool) -> Array[MethodBase]
        """
        ...

    @staticmethod
    def GetExplicitConverter(fromType:Type, toType:Type) -> MethodInfo:
        """ GetExplicitConverter(fromType: Type, toType: Type) -> MethodInfo """
        ...

    @staticmethod
    def GetExpressionTypes(expressions:Array) -> Array:
        """ GetExpressionTypes(expressions: Array[Expression]) -> Array[Type] """
        ...

    @staticmethod
    def GetImplicitConverter(fromType:Type, toType:Type) -> MethodInfo:
        """ GetImplicitConverter(fromType: Type, toType: Type) -> MethodInfo """
        ...

    @staticmethod
    def GetMethodTargets(obj:object) -> Array:
        """ GetMethodTargets(obj: object) -> Array[MethodBase] """
        ...

    @staticmethod
    def GetMissingValue(type:Type) -> object:
        """ GetMissingValue(type: Type) -> object """
        ...

    @staticmethod
    def GetSiteTypes(arguments:IList, returnType:Type) -> Array:
        """ GetSiteTypes(arguments: IList[Expression], returnType: Type) -> Array[Type] """
        ...

    @staticmethod
    def GetTryConvertReturnValue(type:Type) -> Expression:
        """ GetTryConvertReturnValue(type: Type) -> Expression """
        ...

    @staticmethod
    def GetType(obj:object = ...) -> Type:
        """ GetType(obj: object) -> Type """
        ...

    @staticmethod
    def GetTypes(args:Array) -> Array:
        """ GetTypes(args: Array[object]) -> Array[Type] """
        ...

    @staticmethod
    def GetUniqueMethodName() -> str:
        """ GetUniqueMethodName() -> str """
        ...

    @staticmethod
    def GetVisibleType(*__args:object) -> Type:
        """
        GetVisibleType(value: object) -> Type
        GetVisibleType(t: Type) -> Type
        """
        ...

    @staticmethod
    def HasTypeConverter(fromType:Type, toType:Type) -> bool:
        """ HasTypeConverter(fromType: Type, toType: Type) -> bool """
        ...

    @staticmethod
    def IsComparisonOperator(op:ExpressionType) -> bool:
        """ IsComparisonOperator(op: ExpressionType) -> bool """
        ...

    @staticmethod
    def IsConstructor(mb:MethodBase) -> bool:
        """ IsConstructor(mb: MethodBase) -> bool """
        ...

    @staticmethod
    def IsProtected(*__args:MethodBase) -> bool:
        """
        IsProtected(info: MethodBase) -> bool
        IsProtected(info: FieldInfo) -> bool
        IsProtected(type: Type) -> bool
        """
        ...

    @staticmethod
    def IsStatic(mi:MethodBase) -> bool:
        """ IsStatic(mi: MethodBase) -> bool """
        ...

    @staticmethod
    def IsStrongBox(*__args:object) -> bool:
        """
        IsStrongBox(target: object) -> bool
        IsStrongBox(t: Type) -> bool
        """
        ...

    @staticmethod
    def IsVisible(info:MethodBase) -> bool:
        """
        IsVisible(info: MethodBase) -> bool
        IsVisible(info: FieldInfo) -> bool
        """
        ...

    @staticmethod
    def LightCompile(lambda_:LambdaExpression, compilationThreshold:int = ...) -> Delegate:
        """
        LightCompile(lambda: LambdaExpression) -> Delegate
        LightCompile(lambda: LambdaExpression, compilationThreshold: int) -> Delegate
        LightCompile[T](lambda: Expression[T]) -> T
        LightCompile[T](lambda: Expression[T], compilationThreshold: int) -> T
        """
        ...

    @staticmethod
    def MakeCallSiteDelegateType(types:Array) -> Type:
        """ MakeCallSiteDelegateType(types: Array[Type]) -> Type """
        ...

    @staticmethod
    def MakeCallSiteType(types:Array) -> Type:
        """ MakeCallSiteType(*types: Array[Type]) -> Type """
        ...

    @staticmethod
    def MakeRepeatedArray(item, count:int) -> Array: # Not found arg types: {'item': 'T'}
        """ MakeRepeatedArray[T](item: T, count: int) -> Array[T] """
        ...

    @staticmethod
    def MemberEquals(self, other:MemberInfo) -> bool:
        """ MemberEquals(self: MemberInfo, other: MemberInfo) -> bool """
        ...

    @staticmethod
    def Reduce(node:DynamicExpression) -> Expression:
        """ Reduce(node: DynamicExpression) -> Expression """
        ...

    @staticmethod
    def TryApplyTypeConverter(value, toType, result) -> Tuple_[bool, object]:
        """ TryApplyTypeConverter(value: object, toType: Type) -> (bool, object) """
        ...

    @staticmethod
    def TryGetCallableMethod(targetType:Type, method:MethodInfo) -> MethodInfo:
        """ TryGetCallableMethod(targetType: Type, method: MethodInfo) -> MethodInfo """
        ...

    @staticmethod
    def TryGetTypeConverter(fromType, toType, converter) -> Tuple_[bool, TypeConverter]:
        """ TryGetTypeConverter(fromType: Type, toType: Type) -> (bool, TypeConverter) """
        ...

    @staticmethod
    def TryGetVisibleMember(targetType:Type, member:MemberInfo) -> MemberInfo:
        """ TryGetVisibleMember(targetType: Type, member: MemberInfo) -> MemberInfo """
        ...

    @staticmethod
    def TryImplicitConversion(value, to, result) -> Tuple_[bool, object]:
        """ TryImplicitConversion(value: object, to: Type) -> (bool, object) """
        ...

    @staticmethod
    def TypesEqual(args:IList, start:int, types:Array) -> bool:
        """ TypesEqual(args: IList, start: int, types: Array[Type]) -> bool """
        ...

    PublicStatic: MethodAttributes = ...
    __all__: list = ...


class ConstantCheck: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Check(expression:Expression, value:object) -> bool:
        """ Check(expression: Expression, value: object) -> bool """
        ...

    __all__: list = ...


class ILGen: # skipped bases: <type 'object'>, <type 'object'>
    """ ILGen(ilg: ILGenerator) """
    def BeginCatchBlock(self, exceptionType:Type): # -> 
        """ BeginCatchBlock(self: ILGen, exceptionType: Type) """
        ...

    def BeginExceptFilterBlock(self): # -> 
        """ BeginExceptFilterBlock(self: ILGen) """
        ...

    def BeginExceptionBlock(self) -> Label:
        """ BeginExceptionBlock(self: ILGen) -> Label """
        ...

    def BeginFaultBlock(self): # -> 
        """ BeginFaultBlock(self: ILGen) """
        ...

    def BeginFinallyBlock(self): # -> 
        """ BeginFinallyBlock(self: ILGen) """
        ...

    def BeginScope(self): # -> 
        """ BeginScope(self: ILGen) """
        ...

    def DeclareLocal(self, localType:Type, pinned:bool = ...) -> LocalBuilder:
        """
        DeclareLocal(self: ILGen, localType: Type) -> LocalBuilder
        DeclareLocal(self: ILGen, localType: Type, pinned: bool) -> LocalBuilder
        """
        ...

    def DefineLabel(self) -> Label:
        """ DefineLabel(self: ILGen) -> Label """
        ...

    def Emit(self, opcode:OpCode, *__args:SignatureHelper): # -> 
        """ Emit(self: ILGen, opcode: OpCode)Emit(self: ILGen, opcode: OpCode, signature: SignatureHelper)Emit(self: ILGen, opcode: OpCode, arg: Int16)Emit(self: ILGen, opcode: OpCode, arg: SByte)Emit(self: ILGen, opcode: OpCode, meth: MethodInfo)Emit(self: ILGen, opcode: OpCode, arg: Int64)Emit(self: ILGen, opcode: OpCode, local: LocalBuilder)Emit(self: ILGen, opcode: OpCode, str: str)Emit(self: ILGen, opcode: OpCode, labels: Array[Label])Emit(self: ILGen, opcode: OpCode, arg: int)Emit(self: ILGen, opcode: OpCode, arg: Single)Emit(self: ILGen, opcode: OpCode, field: FieldInfo)Emit(self: ILGen, opcode: OpCode, arg: float)Emit(self: ILGen, opcode: OpCode, con: ConstructorInfo)Emit(self: ILGen, opcode: OpCode, arg: Byte)Emit(self: ILGen, opcode: OpCode, label: Label)Emit(self: ILGen, opcode: OpCode, cls: Type) """
        ...

    def EmitArray(self, *__args:IList): # -> 
        """ EmitArray(self: ILGen, elementType: Type, count: int, emit: EmitArrayHelper)EmitArray[T](self: ILGen, items: IList[T])EmitArray(self: ILGen, arrayType: Type) """
        ...

    def EmitBoolean(self, value:bool): # -> 
        """ EmitBoolean(self: ILGen, value: bool) """
        ...

    def EmitBoxing(self, type:Type): # -> 
        """ EmitBoxing(self: ILGen, type: Type) """
        ...

    def EmitByte(self, value:Byte): # -> 
        """ EmitByte(self: ILGen, value: Byte) """
        ...

    def EmitCall(self, *__args:MethodInfo): # -> 
        """ EmitCall(self: ILGen, opcode: OpCode, methodInfo: MethodInfo, optionalParameterTypes: Array[Type])EmitCall(self: ILGen, mi: MethodInfo)EmitCall(self: ILGen, type: Type, name: str)EmitCall(self: ILGen, type: Type, name: str, paramTypes: Array[Type]) """
        ...

    def EmitCalli(self, opcode, *__args): # -> 
        """ EmitCalli(self: ILGen, opcode: OpCode, unmanagedCallConv: CallingConvention, returnType: Type, parameterTypes: Array[Type])EmitCalli(self: ILGen, opcode: OpCode, callingConvention: CallingConventions, returnType: Type, parameterTypes: Array[Type], optionalParameterTypes: Array[Type]) """
        ...

    def EmitChar(self, value:Char): # -> 
        """ EmitChar(self: ILGen, value: Char) """
        ...

    def EmitDecimal(self, value:Decimal): # -> 
        """ EmitDecimal(self: ILGen, value: Decimal) """
        ...

    def EmitDouble(self, value:float): # -> 
        """ EmitDouble(self: ILGen, value: float) """
        ...

    def EmitExplicitCast(self, from_:Type, to:Type): # -> 
        """ EmitExplicitCast(self: ILGen, from: Type, to: Type) """
        ...

    def EmitFieldAddress(self, fi:FieldInfo): # -> 
        """ EmitFieldAddress(self: ILGen, fi: FieldInfo) """
        ...

    def EmitFieldGet(self, fi:FieldInfo): # -> 
        """ EmitFieldGet(self: ILGen, fi: FieldInfo) """
        ...

    def EmitFieldSet(self, fi:FieldInfo): # -> 
        """ EmitFieldSet(self: ILGen, fi: FieldInfo) """
        ...

    def EmitImplicitCast(self, from_:Type, to:Type): # -> 
        """ EmitImplicitCast(self: ILGen, from: Type, to: Type) """
        ...

    def EmitInt(self, value:int): # -> 
        """ EmitInt(self: ILGen, value: int) """
        ...

    def EmitLoadArg(self, index:int): # -> 
        """ EmitLoadArg(self: ILGen, index: int) """
        ...

    def EmitLoadArgAddress(self, index:int): # -> 
        """ EmitLoadArgAddress(self: ILGen, index: int) """
        ...

    def EmitLoadElement(self, type:Type): # -> 
        """ EmitLoadElement(self: ILGen, type: Type) """
        ...

    def EmitLoadValueIndirect(self, type:Type): # -> 
        """ EmitLoadValueIndirect(self: ILGen, type: Type) """
        ...

    def EmitLong(self, value:Int64): # -> 
        """ EmitLong(self: ILGen, value: Int64) """
        ...

    def EmitMissingValue(self, type:Type): # -> 
        """ EmitMissingValue(self: ILGen, type: Type) """
        ...

    def EmitNew(self, *__args:ConstructorInfo): # -> 
        """ EmitNew(self: ILGen, ci: ConstructorInfo)EmitNew(self: ILGen, type: Type, paramTypes: Array[Type]) """
        ...

    def EmitNull(self): # -> 
        """ EmitNull(self: ILGen) """
        ...

    def EmitNumericCast(self, from_:Type, to:Type, implicitOnly:bool) -> bool:
        """ EmitNumericCast(self: ILGen, from: Type, to: Type, implicitOnly: bool) -> bool """
        ...

    def EmitPropertyGet(self, pi:PropertyInfo): # -> 
        """ EmitPropertyGet(self: ILGen, pi: PropertyInfo) """
        ...

    def EmitPropertySet(self, pi:PropertyInfo): # -> 
        """ EmitPropertySet(self: ILGen, pi: PropertyInfo) """
        ...

    def EmitSByte(self, value:SByte): # -> 
        """ EmitSByte(self: ILGen, value: SByte) """
        ...

    def EmitShort(self, value:Int16): # -> 
        """ EmitShort(self: ILGen, value: Int16) """
        ...

    def EmitSingle(self, value:Single): # -> 
        """ EmitSingle(self: ILGen, value: Single) """
        ...

    def EmitStoreArg(self, index:int): # -> 
        """ EmitStoreArg(self: ILGen, index: int) """
        ...

    def EmitStoreElement(self, type:Type): # -> 
        """ EmitStoreElement(self: ILGen, type: Type) """
        ...

    def EmitStoreValueIndirect(self, type:Type): # -> 
        """ EmitStoreValueIndirect(self: ILGen, type: Type) """
        ...

    def EmitString(self, value:str): # -> 
        """ EmitString(self: ILGen, value: str) """
        ...

    def EmitType(self, type:Type): # -> 
        """ EmitType(self: ILGen, type: Type) """
        ...

    def EmitUInt(self, value:UInt32): # -> 
        """ EmitUInt(self: ILGen, value: UInt32) """
        ...

    def EmitULong(self, value:UInt64): # -> 
        """ EmitULong(self: ILGen, value: UInt64) """
        ...

    def EmitUnbox(self, type:Type): # -> 
        """ EmitUnbox(self: ILGen, type: Type) """
        ...

    def EmitUShort(self, value:UInt16): # -> 
        """ EmitUShort(self: ILGen, value: UInt16) """
        ...

    def EndExceptionBlock(self): # -> 
        """ EndExceptionBlock(self: ILGen) """
        ...

    def EndScope(self): # -> 
        """ EndScope(self: ILGen) """
        ...

    def MarkLabel(self, loc:Label): # -> 
        """ MarkLabel(self: ILGen, loc: Label) """
        ...

    def MarkSequencePoint(self, document:ISymbolDocumentWriter, startLine:int, startColumn:int, endLine:int, endColumn:int): # -> 
        """ MarkSequencePoint(self: ILGen, document: ISymbolDocumentWriter, startLine: int, startColumn: int, endLine: int, endColumn: int) """
        ...

    @staticmethod
    def ShouldLdtoken(*__args:Type) -> bool:
        """
        ShouldLdtoken(t: Type) -> bool
        ShouldLdtoken(mb: MethodBase) -> bool
        """
        ...

    def TryEmitExplicitCast(self, from_:Type, to:Type) -> bool:
        """ TryEmitExplicitCast(self: ILGen, from: Type, to: Type) -> bool """
        ...

    def TryEmitImplicitCast(self, from_:Type, to:Type) -> bool:
        """ TryEmitImplicitCast(self: ILGen, from: Type, to: Type) -> bool """
        ...

    def UsingNamespace(self, usingNamespace:str): # -> 
        """ UsingNamespace(self: ILGen, usingNamespace: str) """
        ...


class DynamicILGen(ILGen): # skipped bases: <type 'object'>
    """ no doc """
    def CreateDelegate(self, mi=None): # -> T
        """
        CreateDelegate[T](self: DynamicILGen) -> T
        CreateDelegate[T](self: DynamicILGen) -> (T, MethodInfo)
        """
        ...

    def Finish(self) -> MethodInfo:
        """ Finish(self: DynamicILGen) -> MethodInfo """
        ...


class EmitArrayHelper(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EmitArrayHelper(object: object, method: IntPtr) """
    def BeginInvoke(self, index:int, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: EmitArrayHelper, index: int, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: EmitArrayHelper, result: IAsyncResult) """
        ...

    def Invoke(self, index:int): # -> 
        """ Invoke(self: EmitArrayHelper, index: int) """
        ...


class FieldBuilderExpression(Expression): # skipped bases: <type 'object'>
    """ FieldBuilderExpression(builder: FieldBuilder) """
    pass

class GeneratorOps: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def BoxGeneric(value) -> object: # Not found arg types: {'value': 'T'}
        """ BoxGeneric[T](value: T) -> object """
        ...

    __all__: list = ...


class MethodSignatureInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    MethodSignatureInfo(info: MethodInfo)
    MethodSignatureInfo(isStatic: bool, pis: Array[ParameterInfo], genericArity: int)
    """
    def Equals(self, obj:object) -> bool:
        """ Equals(self: MethodSignatureInfo, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MethodSignatureInfo) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Snippets: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def SaveSnippets(self) -> bool:
        """ Get: SaveSnippets(self: Snippets) -> bool """
        ...

    @property
    def SnippetsDirectory(self) -> str:
        """ Get: SnippetsDirectory(self: Snippets) -> str """
        ...


    def CreateDynamicMethod(self, methodName:str, returnType:Type, parameterTypes:Array, isDebuggable:bool) -> DynamicILGen:
        """ CreateDynamicMethod(self: Snippets, methodName: str, returnType: Type, parameterTypes: Array[Type], isDebuggable: bool) -> DynamicILGen """
        ...

    def DefineDelegate(self, name:str, returnType:Type, argTypes:Array) -> Type:
        """ DefineDelegate(self: Snippets, name: str, returnType: Type, *argTypes: Array[Type]) -> Type """
        ...

    def DefineDelegateType(self, name:str) -> TypeBuilder:
        """ DefineDelegateType(self: Snippets, name: str) -> TypeBuilder """
        ...

    def DefinePublicType(self, name:str, parent:Type) -> TypeBuilder:
        """ DefinePublicType(self: Snippets, name: str, parent: Type) -> TypeBuilder """
        ...

    def DefineType(self, name:str, parent:Type, preserveName:bool, emitDebugSymbols:bool) -> TypeGen:
        """ DefineType(self: Snippets, name: str, parent: Type, preserveName: bool, emitDebugSymbols: bool) -> TypeGen """
        ...

    def IsSnippetsAssembly(self, asm:Assembly) -> bool:
        """ IsSnippetsAssembly(self: Snippets, asm: Assembly) -> bool """
        ...

    @staticmethod
    def SaveAndVerifyAssemblies(): # -> 
        """ SaveAndVerifyAssemblies() """
        ...

    @staticmethod
    def SetSaveAssemblies(enable:bool, directory:str): # -> 
        """ SetSaveAssemblies(enable: bool, directory: str) """
        ...

    Shared: Snippets = ...


class TypeGen: # skipped bases: <type 'object'>, <type 'object'>
    """ TypeGen(myAssembly: AssemblyGen, myType: TypeBuilder) """
    @property
    def TypeBuilder(self) -> TypeBuilder:
        """ Get: TypeBuilder(self: TypeGen) -> TypeBuilder """
        ...

    @property
    def TypeInitializer(self) -> ILGen:
        """ Get: TypeInitializer(self: TypeGen) -> ILGen """
        ...


    def AddStaticField(self, fieldType:Type, *__args:str) -> FieldBuilder:
        """
        AddStaticField(self: TypeGen, fieldType: Type, name: str) -> FieldBuilder
        AddStaticField(self: TypeGen, fieldType: Type, attributes: FieldAttributes, name: str) -> FieldBuilder
        """
        ...

    def DefineExplicitInterfaceImplementation(self, baseMethod:MethodInfo) -> ILGen:
        """ DefineExplicitInterfaceImplementation(self: TypeGen, baseMethod: MethodInfo) -> ILGen """
        ...

    def DefineMethodOverride(self, baseMethod:MethodInfo) -> ILGen:
        """ DefineMethodOverride(self: TypeGen, baseMethod: MethodInfo) -> ILGen """
        ...

    def FinishType(self) -> Type:
        """ FinishType(self: TypeGen) -> Type """
        ...

    def ToString(self) -> str:
        """ ToString(self: TypeGen) -> str """
        ...


