# encoding: utf-8
# module System.Reflection.Emit calls itself Emit
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Byte, Enum, Guid, IEquatable, Int16, IntPtr, 
    RuntimeMethodHandle, Type)

from System.Collections import IEnumerable

from System.Diagnostics.SymbolStore import (ISymbolDocumentWriter, 
    ISymbolWriter)

from System.IO import Stream

from System.Reflection import (Assembly, AssemblyName, CallingConventions, 
    ConstructorInfo, EventAttributes, ExceptionHandlingClauseOptions, 
    FieldAttributes, FieldInfo, GenericParameterAttributes, ImageFileMachine, 
    LocalVariableInfo, MethodAttributes, MethodBase, MethodImplAttributes, 
    MethodInfo, Module, ParameterAttributes, PortableExecutableKinds, 
    PropertyAttributes, PropertyInfo, ResourceAttributes, TypeAttributes, 
    TypeInfo)

from System.Resources import IResourceWriter

from System.Runtime.InteropServices import (CallingConvention, CharSet, 
    UnmanagedType, _AssemblyBuilder, _ConstructorBuilder, 
    _CustomAttributeBuilder, _EnumBuilder, _EventBuilder, _FieldBuilder, 
    _ILGenerator, _LocalBuilder, _MethodBuilder, _MethodRental, 
    _ModuleBuilder, _ParameterBuilder, _PropertyBuilder, _SignatureHelper, 
    _TypeBuilder)

from System.Security import PermissionSet

from System.Security.Permissions import SecurityAction

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class AssemblyBuilder(_AssemblyBuilder, Assembly): # skipped bases: <type 'IEvidenceFactory'>, <type 'ICustomAttributeProvider'>, <type 'ISerializable'>, <type '_Assembly'>, <type 'object'>
    """ no doc """
    def AddResourceFile(self, name:str, fileName:str, attribute:ResourceAttributes = ...): # -> 
        """ AddResourceFile(self: AssemblyBuilder, name: str, fileName: str)AddResourceFile(self: AssemblyBuilder, name: str, fileName: str, attribute: ResourceAttributes) """
        ...

    @staticmethod
    def DefineDynamicAssembly(name:AssemblyName, access:AssemblyBuilderAccess, assemblyAttributes:IEnumerable = ...) -> AssemblyBuilder:
        """
        DefineDynamicAssembly(name: AssemblyName, access: AssemblyBuilderAccess) -> AssemblyBuilder
        DefineDynamicAssembly(name: AssemblyName, access: AssemblyBuilderAccess, assemblyAttributes: IEnumerable[CustomAttributeBuilder]) -> AssemblyBuilder
        """
        ...

    def DefineDynamicModule(self, name:str, *__args:bool) -> ModuleBuilder:
        """
        DefineDynamicModule(self: AssemblyBuilder, name: str) -> ModuleBuilder
        DefineDynamicModule(self: AssemblyBuilder, name: str, emitSymbolInfo: bool) -> ModuleBuilder
        DefineDynamicModule(self: AssemblyBuilder, name: str, fileName: str) -> ModuleBuilder
        DefineDynamicModule(self: AssemblyBuilder, name: str, fileName: str, emitSymbolInfo: bool) -> ModuleBuilder
        """
        ...

    def DefineResource(self, name:str, description:str, fileName:str, attribute:ResourceAttributes = ...) -> IResourceWriter:
        """
        DefineResource(self: AssemblyBuilder, name: str, description: str, fileName: str) -> IResourceWriter
        DefineResource(self: AssemblyBuilder, name: str, description: str, fileName: str, attribute: ResourceAttributes) -> IResourceWriter
        """
        ...

    def DefineUnmanagedResource(self, *__args:Array): # -> 
        """ DefineUnmanagedResource(self: AssemblyBuilder, resource: Array[Byte])DefineUnmanagedResource(self: AssemblyBuilder, resourceFileName: str) """
        ...

    def DefineVersionInfoResource(self, product:str = ..., productVersion:str = ..., company:str = ..., copyright:str = ..., trademark:str = ...): # -> 
        """ DefineVersionInfoResource(self: AssemblyBuilder, product: str, productVersion: str, company: str, copyright: str, trademark: str)DefineVersionInfoResource(self: AssemblyBuilder) """
        ...

    def GetDynamicModule(self, name:str) -> ModuleBuilder:
        """ GetDynamicModule(self: AssemblyBuilder, name: str) -> ModuleBuilder """
        ...

    def Save(self, assemblyFileName:str, portableExecutableKind:PortableExecutableKinds = ..., imageFileMachine:ImageFileMachine = ...): # -> 
        """ Save(self: AssemblyBuilder, assemblyFileName: str)Save(self: AssemblyBuilder, assemblyFileName: str, portableExecutableKind: PortableExecutableKinds, imageFileMachine: ImageFileMachine) """
        ...

    def SetCustomAttribute(self, *__args:CustomAttributeBuilder): # -> 
        """ SetCustomAttribute(self: AssemblyBuilder, customBuilder: CustomAttributeBuilder)SetCustomAttribute(self: AssemblyBuilder, con: ConstructorInfo, binaryAttribute: Array[Byte]) """
        ...

    def SetEntryPoint(self, entryMethod:MethodInfo, fileKind:PEFileKinds = ...): # -> 
        """ SetEntryPoint(self: AssemblyBuilder, entryMethod: MethodInfo)SetEntryPoint(self: AssemblyBuilder, entryMethod: MethodInfo, fileKind: PEFileKinds) """
        ...


class AssemblyBuilderAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) AssemblyBuilderAccess, values: ReflectionOnly (6), Run (1), RunAndCollect (9), RunAndSave (3), Save (2) """
    ReflectionOnly: AssemblyBuilderAccess = ...
    Run: AssemblyBuilderAccess = ...
    RunAndCollect: AssemblyBuilderAccess = ...
    RunAndSave: AssemblyBuilderAccess = ...
    Save: AssemblyBuilderAccess = ...
    value__ = ...


class ConstructorBuilder(_ConstructorBuilder, ConstructorInfo): # skipped bases: <type '_MemberInfo'>, <type '_MethodBase'>, <type 'ICustomAttributeProvider'>, <type '_ConstructorInfo'>, <type 'object'>
    """ no doc """
    @property
    def InitLocals(self) -> bool:
        """
        Get: InitLocals(self: ConstructorBuilder) -> bool
        Set: InitLocals(self: ConstructorBuilder) = value
        """
        ...

    @property
    def Module(self) -> Module:
        """ Get: Module(self: ConstructorBuilder) -> Module """
        ...

    @property
    def ReturnType(self) -> Type:
        """ Get: ReturnType(self: ConstructorBuilder) -> Type """
        ...

    @property
    def Signature(self) -> str:
        """ Get: Signature(self: ConstructorBuilder) -> str """
        ...


    def AddDeclarativeSecurity(self, action:SecurityAction, pset:PermissionSet): # -> 
        """ AddDeclarativeSecurity(self: ConstructorBuilder, action: SecurityAction, pset: PermissionSet) """
        ...

    def DefineParameter(self, iSequence:int, attributes:ParameterAttributes, strParamName:str) -> ParameterBuilder:
        """ DefineParameter(self: ConstructorBuilder, iSequence: int, attributes: ParameterAttributes, strParamName: str) -> ParameterBuilder """
        ...

    def GetILGenerator(self, streamSize:int = ...) -> ILGenerator:
        """
        GetILGenerator(self: ConstructorBuilder) -> ILGenerator
        GetILGenerator(self: ConstructorBuilder, streamSize: int) -> ILGenerator
        """
        ...

    def GetModule(self) -> Module:
        """ GetModule(self: ConstructorBuilder) -> Module """
        ...

    def GetToken(self) -> MethodToken:
        """ GetToken(self: ConstructorBuilder) -> MethodToken """
        ...

    def SetCustomAttribute(self, *__args:CustomAttributeBuilder): # -> 
        """ SetCustomAttribute(self: ConstructorBuilder, con: ConstructorInfo, binaryAttribute: Array[Byte])SetCustomAttribute(self: ConstructorBuilder, customBuilder: CustomAttributeBuilder) """
        ...

    def SetImplementationFlags(self, attributes:MethodImplAttributes): # -> 
        """ SetImplementationFlags(self: ConstructorBuilder, attributes: MethodImplAttributes) """
        ...

    def SetMethodBody(self, il:Array, maxStack:int, localSignature:Array, exceptionHandlers:IEnumerable, tokenFixups:IEnumerable): # -> 
        """ SetMethodBody(self: ConstructorBuilder, il: Array[Byte], maxStack: int, localSignature: Array[Byte], exceptionHandlers: IEnumerable[ExceptionHandler], tokenFixups: IEnumerable[int]) """
        ...

    def SetSymCustomAttribute(self, name:str, data:Array): # -> 
        """ SetSymCustomAttribute(self: ConstructorBuilder, name: str, data: Array[Byte]) """
        ...


class CustomAttributeBuilder(_CustomAttributeBuilder): # skipped bases: <type 'object'>
    """
    CustomAttributeBuilder(con: ConstructorInfo, constructorArgs: Array[object])
    CustomAttributeBuilder(con: ConstructorInfo, constructorArgs: Array[object], namedProperties: Array[PropertyInfo], propertyValues: Array[object])
    CustomAttributeBuilder(con: ConstructorInfo, constructorArgs: Array[object], namedFields: Array[FieldInfo], fieldValues: Array[object])
    CustomAttributeBuilder(con: ConstructorInfo, constructorArgs: Array[object], namedProperties: Array[PropertyInfo], propertyValues: Array[object], namedFields: Array[FieldInfo], fieldValues: Array[object])
    """
    pass

class DynamicILInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DynamicMethod(self) -> DynamicMethod:
        """ Get: DynamicMethod(self: DynamicILInfo) -> DynamicMethod """
        ...


    def GetTokenFor(self, *__args:RuntimeMethodHandle) -> int:
        """
        GetTokenFor(self: DynamicILInfo, method: RuntimeMethodHandle) -> int
        GetTokenFor(self: DynamicILInfo, method: DynamicMethod) -> int
        GetTokenFor(self: DynamicILInfo, method: RuntimeMethodHandle, contextType: RuntimeTypeHandle) -> int
        GetTokenFor(self: DynamicILInfo, field: RuntimeFieldHandle) -> int
        GetTokenFor(self: DynamicILInfo, field: RuntimeFieldHandle, contextType: RuntimeTypeHandle) -> int
        GetTokenFor(self: DynamicILInfo, type: RuntimeTypeHandle) -> int
        GetTokenFor(self: DynamicILInfo, literal: str) -> int
        GetTokenFor(self: DynamicILInfo, signature: Array[Byte]) -> int
        """
        ...

    def SetCode(self, code:Array, *__args:int): # -> 
        """ SetCode(self: DynamicILInfo, code: Array[Byte], maxStackSize: int)SetCode(self: DynamicILInfo, code: Byte*, codeSize: int, maxStackSize: int) """
        ...

    def SetExceptions(self, exceptions:Byte, exceptionsSize:int = ...): # -> 
        """ SetExceptions(self: DynamicILInfo, exceptions: Array[Byte])SetExceptions(self: DynamicILInfo, exceptions: Byte*, exceptionsSize: int) """
        ...

    def SetLocalSignature(self, localSignature:Byte, signatureSize:int = ...): # -> 
        """ SetLocalSignature(self: DynamicILInfo, localSignature: Array[Byte])SetLocalSignature(self: DynamicILInfo, localSignature: Byte*, signatureSize: int) """
        ...


class DynamicMethod(MethodInfo): # skipped bases: <type '_MemberInfo'>, <type '_MethodInfo'>, <type '_MethodBase'>, <type 'ICustomAttributeProvider'>, <type 'object'>
    """
    DynamicMethod(name: str, returnType: Type, parameterTypes: Array[Type])
    DynamicMethod(name: str, returnType: Type, parameterTypes: Array[Type], restrictedSkipVisibility: bool)
    DynamicMethod(name: str, returnType: Type, parameterTypes: Array[Type], m: Module)
    DynamicMethod(name: str, returnType: Type, parameterTypes: Array[Type], m: Module, skipVisibility: bool)
    DynamicMethod(name: str, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: Type, parameterTypes: Array[Type], m: Module, skipVisibility: bool)
    DynamicMethod(name: str, returnType: Type, parameterTypes: Array[Type], owner: Type)
    DynamicMethod(name: str, returnType: Type, parameterTypes: Array[Type], owner: Type, skipVisibility: bool)
    DynamicMethod(name: str, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: Type, parameterTypes: Array[Type], owner: Type, skipVisibility: bool)
    """
    @property
    def InitLocals(self) -> bool:
        """
        Get: InitLocals(self: DynamicMethod) -> bool
        Set: InitLocals(self: DynamicMethod) = value
        """
        ...

    @property
    def IsSecurityCritical(self) -> bool:
        """ Get: IsSecurityCritical(self: DynamicMethod) -> bool """
        ...

    @property
    def IsSecuritySafeCritical(self) -> bool:
        """ Get: IsSecuritySafeCritical(self: DynamicMethod) -> bool """
        ...

    @property
    def IsSecurityTransparent(self) -> bool:
        """ Get: IsSecurityTransparent(self: DynamicMethod) -> bool """
        ...

    @property
    def Module(self) -> Module:
        """ Get: Module(self: DynamicMethod) -> Module """
        ...


    def DefineParameter(self, position:int, attributes:ParameterAttributes, parameterName:str) -> ParameterBuilder:
        """ DefineParameter(self: DynamicMethod, position: int, attributes: ParameterAttributes, parameterName: str) -> ParameterBuilder """
        ...

    def GetDynamicILInfo(self) -> DynamicILInfo:
        """ GetDynamicILInfo(self: DynamicMethod) -> DynamicILInfo """
        ...

    def GetILGenerator(self, streamSize:int = ...) -> ILGenerator:
        """
        GetILGenerator(self: DynamicMethod) -> ILGenerator
        GetILGenerator(self: DynamicMethod, streamSize: int) -> ILGenerator
        """
        ...

    def __new__(cls, name, *__args) -> Self:
        """
        __new__(cls: type, name: str, returnType: Type, parameterTypes: Array[Type])
        __new__(cls: type, name: str, returnType: Type, parameterTypes: Array[Type], restrictedSkipVisibility: bool)
        __new__(cls: type, name: str, returnType: Type, parameterTypes: Array[Type], m: Module)
        __new__(cls: type, name: str, returnType: Type, parameterTypes: Array[Type], m: Module, skipVisibility: bool)
        __new__(cls: type, name: str, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: Type, parameterTypes: Array[Type], m: Module, skipVisibility: bool)
        __new__(cls: type, name: str, returnType: Type, parameterTypes: Array[Type], owner: Type)
        __new__(cls: type, name: str, returnType: Type, parameterTypes: Array[Type], owner: Type, skipVisibility: bool)
        __new__(cls: type, name: str, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: Type, parameterTypes: Array[Type], owner: Type, skipVisibility: bool)
        """
        ...


class EnumBuilder(_EnumBuilder, TypeInfo): # skipped bases: <type '_MemberInfo'>, <type 'ICustomAttributeProvider'>, <type 'IReflect'>, <type 'IReflectableType'>, <type '_Type'>, <type 'object'>
    """ no doc """
    @property
    def IsConstructedGenericType(self) -> bool:
        """ Get: IsConstructedGenericType(self: EnumBuilder) -> bool """
        ...

    @property
    def TypeToken(self) -> TypeToken:
        """ Get: TypeToken(self: EnumBuilder) -> TypeToken """
        ...

    @property
    def UnderlyingField(self) -> FieldBuilder:
        """ Get: UnderlyingField(self: EnumBuilder) -> FieldBuilder """
        ...


    def CreateType(self) -> Type:
        """ CreateType(self: EnumBuilder) -> Type """
        ...

    def CreateTypeInfo(self) -> TypeInfo:
        """ CreateTypeInfo(self: EnumBuilder) -> TypeInfo """
        ...

    def DefineLiteral(self, literalName:str, literalValue:object) -> FieldBuilder:
        """ DefineLiteral(self: EnumBuilder, literalName: str, literalValue: object) -> FieldBuilder """
        ...

    def GetEnumUnderlyingType(self) -> Type:
        """ GetEnumUnderlyingType(self: EnumBuilder) -> Type """
        ...

    def MakeArrayType(self, rank:int = ...) -> Type:
        """
        MakeArrayType(self: EnumBuilder) -> Type
        MakeArrayType(self: EnumBuilder, rank: int) -> Type
        """
        ...

    def MakeByRefType(self) -> Type:
        """ MakeByRefType(self: EnumBuilder) -> Type """
        ...

    def MakePointerType(self) -> Type:
        """ MakePointerType(self: EnumBuilder) -> Type """
        ...

    def SetCustomAttribute(self, *__args:CustomAttributeBuilder): # -> 
        """ SetCustomAttribute(self: EnumBuilder, con: ConstructorInfo, binaryAttribute: Array[Byte])SetCustomAttribute(self: EnumBuilder, customBuilder: CustomAttributeBuilder) """
        ...


class EventBuilder(_EventBuilder): # skipped bases: <type 'object'>
    """ no doc """
    def AddOtherMethod(self, mdBuilder:MethodBuilder): # -> 
        """ AddOtherMethod(self: EventBuilder, mdBuilder: MethodBuilder) """
        ...

    def GetEventToken(self) -> EventToken:
        """ GetEventToken(self: EventBuilder) -> EventToken """
        ...

    def SetAddOnMethod(self, mdBuilder:MethodBuilder): # -> 
        """ SetAddOnMethod(self: EventBuilder, mdBuilder: MethodBuilder) """
        ...

    def SetCustomAttribute(self, *__args:CustomAttributeBuilder): # -> 
        """ SetCustomAttribute(self: EventBuilder, con: ConstructorInfo, binaryAttribute: Array[Byte])SetCustomAttribute(self: EventBuilder, customBuilder: CustomAttributeBuilder) """
        ...

    def SetRaiseMethod(self, mdBuilder:MethodBuilder): # -> 
        """ SetRaiseMethod(self: EventBuilder, mdBuilder: MethodBuilder) """
        ...

    def SetRemoveOnMethod(self, mdBuilder:MethodBuilder): # -> 
        """ SetRemoveOnMethod(self: EventBuilder, mdBuilder: MethodBuilder) """
        ...


class EventToken: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Token(self) -> int:
        """ Get: Token(self: EventToken) -> int """
        ...


    def Equals(self, obj:object) -> bool:
        """
        Equals(self: EventToken, obj: object) -> bool
        Equals(self: EventToken, obj: EventToken) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: EventToken) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Empty: EventToken = ...


class ExceptionHandler(IEquatable): # skipped bases: <type 'object'>
    """ ExceptionHandler(tryOffset: int, tryLength: int, filterOffset: int, handlerOffset: int, handlerLength: int, kind: ExceptionHandlingClauseOptions, exceptionTypeToken: int) """
    @property
    def ExceptionTypeToken(self) -> int:
        """ Get: ExceptionTypeToken(self: ExceptionHandler) -> int """
        ...

    @property
    def FilterOffset(self) -> int:
        """ Get: FilterOffset(self: ExceptionHandler) -> int """
        ...

    @property
    def HandlerLength(self) -> int:
        """ Get: HandlerLength(self: ExceptionHandler) -> int """
        ...

    @property
    def HandlerOffset(self) -> int:
        """ Get: HandlerOffset(self: ExceptionHandler) -> int """
        ...

    @property
    def Kind(self) -> ExceptionHandlingClauseOptions:
        """ Get: Kind(self: ExceptionHandler) -> ExceptionHandlingClauseOptions """
        ...

    @property
    def TryLength(self) -> int:
        """ Get: TryLength(self: ExceptionHandler) -> int """
        ...

    @property
    def TryOffset(self) -> int:
        """ Get: TryOffset(self: ExceptionHandler) -> int """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: ExceptionHandler) -> int """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class FieldBuilder(_FieldBuilder, FieldInfo): # skipped bases: <type '_MemberInfo'>, <type '_FieldInfo'>, <type 'ICustomAttributeProvider'>, <type 'object'>
    """ no doc """
    @property
    def Module(self) -> Module:
        """ Get: Module(self: FieldBuilder) -> Module """
        ...


    def GetToken(self) -> FieldToken:
        """ GetToken(self: FieldBuilder) -> FieldToken """
        ...

    def SetConstant(self, defaultValue:object): # -> 
        """ SetConstant(self: FieldBuilder, defaultValue: object) """
        ...

    def SetCustomAttribute(self, *__args:CustomAttributeBuilder): # -> 
        """ SetCustomAttribute(self: FieldBuilder, con: ConstructorInfo, binaryAttribute: Array[Byte])SetCustomAttribute(self: FieldBuilder, customBuilder: CustomAttributeBuilder) """
        ...

    def SetMarshal(self, unmanagedMarshal:UnmanagedMarshal): # -> 
        """ SetMarshal(self: FieldBuilder, unmanagedMarshal: UnmanagedMarshal) """
        ...

    def SetOffset(self, iOffset:int): # -> 
        """ SetOffset(self: FieldBuilder, iOffset: int) """
        ...


class FieldToken: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Token(self) -> int:
        """ Get: Token(self: FieldToken) -> int """
        ...


    def Equals(self, obj:object) -> bool:
        """
        Equals(self: FieldToken, obj: object) -> bool
        Equals(self: FieldToken, obj: FieldToken) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: FieldToken) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Empty: FieldToken = ...


class FlowControl(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FlowControl, values: Branch (0), Break (1), Call (2), Cond_Branch (3), Meta (4), Next (5), Phi (6), Return (7), Throw (8) """
    def Branch(self, *args): #cannot find CLR method
        """ enum FlowControl, values: Branch (0), Break (1), Call (2), Cond_Branch (3), Meta (4), Next (5), Phi (6), Return (7), Throw (8) """
        ...

    def Break(self, *args): #cannot find CLR method
        """ enum FlowControl, values: Branch (0), Break (1), Call (2), Cond_Branch (3), Meta (4), Next (5), Phi (6), Return (7), Throw (8) """
        ...

    def Call(self, *args): #cannot find CLR method
        """ enum FlowControl, values: Branch (0), Break (1), Call (2), Cond_Branch (3), Meta (4), Next (5), Phi (6), Return (7), Throw (8) """
        ...

    def Cond_Branch(self, *args): #cannot find CLR method
        """ enum FlowControl, values: Branch (0), Break (1), Call (2), Cond_Branch (3), Meta (4), Next (5), Phi (6), Return (7), Throw (8) """
        ...

    def Meta(self, *args): #cannot find CLR method
        """ enum FlowControl, values: Branch (0), Break (1), Call (2), Cond_Branch (3), Meta (4), Next (5), Phi (6), Return (7), Throw (8) """
        ...

    def Next(self, *args): #cannot find CLR method
        """ enum FlowControl, values: Branch (0), Break (1), Call (2), Cond_Branch (3), Meta (4), Next (5), Phi (6), Return (7), Throw (8) """
        ...

    def Phi(self, *args): #cannot find CLR method
        """ enum FlowControl, values: Branch (0), Break (1), Call (2), Cond_Branch (3), Meta (4), Next (5), Phi (6), Return (7), Throw (8) """
        ...

    def Return(self, *args): #cannot find CLR method
        """ enum FlowControl, values: Branch (0), Break (1), Call (2), Cond_Branch (3), Meta (4), Next (5), Phi (6), Return (7), Throw (8) """
        ...

    def Throw(self, *args): #cannot find CLR method
        """ enum FlowControl, values: Branch (0), Break (1), Call (2), Cond_Branch (3), Meta (4), Next (5), Phi (6), Return (7), Throw (8) """
        ...

    def __call__(self, *args): #cannot find CLR method
        """ enum FlowControl, values: Branch (0), Break (1), Call (2), Cond_Branch (3), Meta (4), Next (5), Phi (6), Return (7), Throw (8) """
        ...

    value__ = ...


class GenericTypeParameterBuilder(TypeInfo): # skipped bases: <type '_MemberInfo'>, <type 'ICustomAttributeProvider'>, <type 'IReflect'>, <type 'IReflectableType'>, <type '_Type'>, <type 'object'>
    """ no doc """
    @property
    def ContainsGenericParameters(self) -> bool:
        """ Get: ContainsGenericParameters(self: GenericTypeParameterBuilder) -> bool """
        ...

    @property
    def DeclaringMethod(self) -> MethodBase:
        """ Get: DeclaringMethod(self: GenericTypeParameterBuilder) -> MethodBase """
        ...

    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """ Get: GenericParameterAttributes(self: GenericTypeParameterBuilder) -> GenericParameterAttributes """
        ...

    @property
    def GenericParameterPosition(self) -> int:
        """ Get: GenericParameterPosition(self: GenericTypeParameterBuilder) -> int """
        ...

    @property
    def IsConstructedGenericType(self) -> bool:
        """ Get: IsConstructedGenericType(self: GenericTypeParameterBuilder) -> bool """
        ...

    @property
    def IsGenericParameter(self) -> bool:
        """ Get: IsGenericParameter(self: GenericTypeParameterBuilder) -> bool """
        ...

    @property
    def IsGenericType(self) -> bool:
        """ Get: IsGenericType(self: GenericTypeParameterBuilder) -> bool """
        ...

    @property
    def IsGenericTypeDefinition(self) -> bool:
        """ Get: IsGenericTypeDefinition(self: GenericTypeParameterBuilder) -> bool """
        ...


    def GetGenericArguments(self) -> Array:
        """ GetGenericArguments(self: GenericTypeParameterBuilder) -> Array[Type] """
        ...

    def GetGenericTypeDefinition(self) -> Type:
        """ GetGenericTypeDefinition(self: GenericTypeParameterBuilder) -> Type """
        ...

    def MakeArrayType(self, rank:int = ...) -> Type:
        """
        MakeArrayType(self: GenericTypeParameterBuilder) -> Type
        MakeArrayType(self: GenericTypeParameterBuilder, rank: int) -> Type
        """
        ...

    def MakeByRefType(self) -> Type:
        """ MakeByRefType(self: GenericTypeParameterBuilder) -> Type """
        ...

    def MakeGenericType(self, typeArguments:Array) -> Type:
        """ MakeGenericType(self: GenericTypeParameterBuilder, *typeArguments: Array[Type]) -> Type """
        ...

    def MakePointerType(self) -> Type:
        """ MakePointerType(self: GenericTypeParameterBuilder) -> Type """
        ...

    def SetBaseTypeConstraint(self, baseTypeConstraint:Type): # -> 
        """ SetBaseTypeConstraint(self: GenericTypeParameterBuilder, baseTypeConstraint: Type) """
        ...

    def SetCustomAttribute(self, *__args:CustomAttributeBuilder): # -> 
        """ SetCustomAttribute(self: GenericTypeParameterBuilder, con: ConstructorInfo, binaryAttribute: Array[Byte])SetCustomAttribute(self: GenericTypeParameterBuilder, customBuilder: CustomAttributeBuilder) """
        ...

    def SetGenericParameterAttributes(self, genericParameterAttributes:GenericParameterAttributes): # -> 
        """ SetGenericParameterAttributes(self: GenericTypeParameterBuilder, genericParameterAttributes: GenericParameterAttributes) """
        ...

    def SetInterfaceConstraints(self, interfaceConstraints:Array): # -> 
        """ SetInterfaceConstraints(self: GenericTypeParameterBuilder, *interfaceConstraints: Array[Type]) """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ILGenerator(_ILGenerator): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ILOffset(self) -> int:
        """ Get: ILOffset(self: ILGenerator) -> int """
        ...


    def BeginCatchBlock(self, exceptionType:Type): # -> 
        """ BeginCatchBlock(self: ILGenerator, exceptionType: Type) """
        ...

    def BeginExceptFilterBlock(self): # -> 
        """ BeginExceptFilterBlock(self: ILGenerator) """
        ...

    def BeginExceptionBlock(self) -> Label:
        """ BeginExceptionBlock(self: ILGenerator) -> Label """
        ...

    def BeginFaultBlock(self): # -> 
        """ BeginFaultBlock(self: ILGenerator) """
        ...

    def BeginFinallyBlock(self): # -> 
        """ BeginFinallyBlock(self: ILGenerator) """
        ...

    def BeginScope(self): # -> 
        """ BeginScope(self: ILGenerator) """
        ...

    def DeclareLocal(self, localType:Type, pinned:bool = ...) -> LocalBuilder:
        """
        DeclareLocal(self: ILGenerator, localType: Type) -> LocalBuilder
        DeclareLocal(self: ILGenerator, localType: Type, pinned: bool) -> LocalBuilder
        """
        ...

    def DefineLabel(self) -> Label:
        """ DefineLabel(self: ILGenerator) -> Label """
        ...

    def Emit(self, opcode:OpCode, *__args:FieldInfo): # -> 
        """ Emit(self: ILGenerator, opcode: OpCode)Emit(self: ILGenerator, opcode: OpCode, field: FieldInfo)Emit(self: ILGenerator, opcode: OpCode, labels: Array[Label])Emit(self: ILGenerator, opcode: OpCode, label: Label)Emit(self: ILGenerator, opcode: OpCode, arg: float)Emit(self: ILGenerator, opcode: OpCode, arg: Single)Emit(self: ILGenerator, opcode: OpCode, arg: Int64)Emit(self: ILGenerator, opcode: OpCode, str: str)Emit(self: ILGenerator, opcode: OpCode, cls: Type)Emit(self: ILGenerator, opcode: OpCode, signature: SignatureHelper)Emit(self: ILGenerator, opcode: OpCode, meth: MethodInfo)Emit(self: ILGenerator, opcode: OpCode, arg: int)Emit(self: ILGenerator, opcode: OpCode, arg: Int16)Emit(self: ILGenerator, opcode: OpCode, arg: SByte)Emit(self: ILGenerator, opcode: OpCode, arg: Byte)Emit(self: ILGenerator, opcode: OpCode, con: ConstructorInfo)Emit(self: ILGenerator, opcode: OpCode, local: LocalBuilder) """
        ...

    def EmitCall(self, opcode:OpCode, methodInfo:MethodInfo, optionalParameterTypes:Array): # -> 
        """ EmitCall(self: ILGenerator, opcode: OpCode, methodInfo: MethodInfo, optionalParameterTypes: Array[Type]) """
        ...

    def EmitCalli(self, opcode, *__args): # -> 
        """ EmitCalli(self: ILGenerator, opcode: OpCode, callingConvention: CallingConventions, returnType: Type, parameterTypes: Array[Type], optionalParameterTypes: Array[Type])EmitCalli(self: ILGenerator, opcode: OpCode, unmanagedCallConv: CallingConvention, returnType: Type, parameterTypes: Array[Type]) """
        ...

    def EmitWriteLine(self, *__args:str): # -> 
        """ EmitWriteLine(self: ILGenerator, value: str)EmitWriteLine(self: ILGenerator, localBuilder: LocalBuilder)EmitWriteLine(self: ILGenerator, fld: FieldInfo) """
        ...

    def EndExceptionBlock(self): # -> 
        """ EndExceptionBlock(self: ILGenerator) """
        ...

    def EndScope(self): # -> 
        """ EndScope(self: ILGenerator) """
        ...

    def MarkLabel(self, loc:Label): # -> 
        """ MarkLabel(self: ILGenerator, loc: Label) """
        ...

    def MarkSequencePoint(self, document:ISymbolDocumentWriter, startLine:int, startColumn:int, endLine:int, endColumn:int): # -> 
        """ MarkSequencePoint(self: ILGenerator, document: ISymbolDocumentWriter, startLine: int, startColumn: int, endLine: int, endColumn: int) """
        ...

    def ThrowException(self, excType:Type): # -> 
        """ ThrowException(self: ILGenerator, excType: Type) """
        ...

    def UsingNamespace(self, usingNamespace:str): # -> 
        """ UsingNamespace(self: ILGenerator, usingNamespace: str) """
        ...


class Label: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Equals(self, obj:Label) -> bool:
        """
        Equals(self: Label, obj: Label) -> bool
        Equals(self: Label, obj: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Label) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LocalBuilder(LocalVariableInfo, _LocalBuilder): # skipped bases: <type 'object'>
    """ no doc """
    def SetLocalSymInfo(self, name:str, startOffset:int = ..., endOffset:int = ...): # -> 
        """ SetLocalSymInfo(self: LocalBuilder, name: str)SetLocalSymInfo(self: LocalBuilder, name: str, startOffset: int, endOffset: int) """
        ...


class MethodBuilder(MethodInfo, _MethodBuilder): # skipped bases: <type '_MemberInfo'>, <type '_MethodInfo'>, <type '_MethodBase'>, <type 'ICustomAttributeProvider'>, <type 'object'>
    """ no doc """
    @property
    def ContainsGenericParameters(self) -> bool:
        """ Get: ContainsGenericParameters(self: MethodBuilder) -> bool """
        ...

    @property
    def InitLocals(self) -> bool:
        """
        Get: InitLocals(self: MethodBuilder) -> bool
        Set: InitLocals(self: MethodBuilder) = value
        """
        ...

    @property
    def IsGenericMethod(self) -> bool:
        """ Get: IsGenericMethod(self: MethodBuilder) -> bool """
        ...

    @property
    def IsGenericMethodDefinition(self) -> bool:
        """ Get: IsGenericMethodDefinition(self: MethodBuilder) -> bool """
        ...

    @property
    def IsSecurityCritical(self) -> bool:
        """ Get: IsSecurityCritical(self: MethodBuilder) -> bool """
        ...

    @property
    def IsSecuritySafeCritical(self) -> bool:
        """ Get: IsSecuritySafeCritical(self: MethodBuilder) -> bool """
        ...

    @property
    def IsSecurityTransparent(self) -> bool:
        """ Get: IsSecurityTransparent(self: MethodBuilder) -> bool """
        ...

    @property
    def Module(self) -> Module:
        """ Get: Module(self: MethodBuilder) -> Module """
        ...

    @property
    def Signature(self) -> str:
        """ Get: Signature(self: MethodBuilder) -> str """
        ...


    def AddDeclarativeSecurity(self, action:SecurityAction, pset:PermissionSet): # -> 
        """ AddDeclarativeSecurity(self: MethodBuilder, action: SecurityAction, pset: PermissionSet) """
        ...

    def CreateMethodBody(self, il:Array, count:int): # -> 
        """ CreateMethodBody(self: MethodBuilder, il: Array[Byte], count: int) """
        ...

    def DefineGenericParameters(self, names:Array) -> Array:
        """ DefineGenericParameters(self: MethodBuilder, *names: Array[str]) -> Array[GenericTypeParameterBuilder] """
        ...

    def DefineParameter(self, position:int, attributes:ParameterAttributes, strParamName:str) -> ParameterBuilder:
        """ DefineParameter(self: MethodBuilder, position: int, attributes: ParameterAttributes, strParamName: str) -> ParameterBuilder """
        ...

    def GetILGenerator(self, size:int = ...) -> ILGenerator:
        """
        GetILGenerator(self: MethodBuilder) -> ILGenerator
        GetILGenerator(self: MethodBuilder, size: int) -> ILGenerator
        """
        ...

    def GetModule(self) -> Module:
        """ GetModule(self: MethodBuilder) -> Module """
        ...

    def GetToken(self) -> MethodToken:
        """ GetToken(self: MethodBuilder) -> MethodToken """
        ...

    def SetCustomAttribute(self, *__args:CustomAttributeBuilder): # -> 
        """ SetCustomAttribute(self: MethodBuilder, con: ConstructorInfo, binaryAttribute: Array[Byte])SetCustomAttribute(self: MethodBuilder, customBuilder: CustomAttributeBuilder) """
        ...

    def SetImplementationFlags(self, attributes:MethodImplAttributes): # -> 
        """ SetImplementationFlags(self: MethodBuilder, attributes: MethodImplAttributes) """
        ...

    def SetMarshal(self, unmanagedMarshal:UnmanagedMarshal): # -> 
        """ SetMarshal(self: MethodBuilder, unmanagedMarshal: UnmanagedMarshal) """
        ...

    def SetMethodBody(self, il:Array, maxStack:int, localSignature:Array, exceptionHandlers:IEnumerable, tokenFixups:IEnumerable): # -> 
        """ SetMethodBody(self: MethodBuilder, il: Array[Byte], maxStack: int, localSignature: Array[Byte], exceptionHandlers: IEnumerable[ExceptionHandler], tokenFixups: IEnumerable[int]) """
        ...

    def SetParameters(self, parameterTypes:Array): # -> 
        """ SetParameters(self: MethodBuilder, *parameterTypes: Array[Type]) """
        ...

    def SetReturnType(self, returnType:Type): # -> 
        """ SetReturnType(self: MethodBuilder, returnType: Type) """
        ...

    def SetSignature(self, returnType:Type, returnTypeRequiredCustomModifiers:Array, returnTypeOptionalCustomModifiers:Array, parameterTypes:Array, parameterTypeRequiredCustomModifiers:Array, parameterTypeOptionalCustomModifiers:Array): # -> 
        """ SetSignature(self: MethodBuilder, returnType: Type, returnTypeRequiredCustomModifiers: Array[Type], returnTypeOptionalCustomModifiers: Array[Type], parameterTypes: Array[Type], parameterTypeRequiredCustomModifiers: Array[Array[Type]], parameterTypeOptionalCustomModifiers: Array[Array[Type]]) """
        ...

    def SetSymCustomAttribute(self, name:str, data:Array): # -> 
        """ SetSymCustomAttribute(self: MethodBuilder, name: str, data: Array[Byte]) """
        ...


class MethodRental(_MethodRental): # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def SwapMethodBody(cls, methodtoken:int, rgIL:IntPtr, methodSize:int, flags:int): # -> 
        """ SwapMethodBody(cls: Type, methodtoken: int, rgIL: IntPtr, methodSize: int, flags: int) """
        ...

    JitImmediate: int = ...
    JitOnDemand: int = ...


class MethodToken: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Token(self) -> int:
        """ Get: Token(self: MethodToken) -> int """
        ...


    def Equals(self, obj:object) -> bool:
        """
        Equals(self: MethodToken, obj: object) -> bool
        Equals(self: MethodToken, obj: MethodToken) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: MethodToken) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Empty: MethodToken = ...


class ModuleBuilder(Module, _ModuleBuilder): # skipped bases: <type 'ICustomAttributeProvider'>, <type '_Module'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    def CreateGlobalFunctions(self): # -> 
        """ CreateGlobalFunctions(self: ModuleBuilder) """
        ...

    def DefineDocument(self, url:str, language:Guid, languageVendor:Guid, documentType:Guid) -> ISymbolDocumentWriter:
        """ DefineDocument(self: ModuleBuilder, url: str, language: Guid, languageVendor: Guid, documentType: Guid) -> ISymbolDocumentWriter """
        ...

    def DefineEnum(self, name:str, visibility:TypeAttributes, underlyingType:Type) -> EnumBuilder:
        """ DefineEnum(self: ModuleBuilder, name: str, visibility: TypeAttributes, underlyingType: Type) -> EnumBuilder """
        ...

    def DefineGlobalMethod(self, name, attributes, *__args) -> MethodBuilder:
        """
        DefineGlobalMethod(self: ModuleBuilder, name: str, attributes: MethodAttributes, returnType: Type, parameterTypes: Array[Type]) -> MethodBuilder
        DefineGlobalMethod(self: ModuleBuilder, name: str, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: Type, parameterTypes: Array[Type]) -> MethodBuilder
        DefineGlobalMethod(self: ModuleBuilder, name: str, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: Type, requiredReturnTypeCustomModifiers: Array[Type], optionalReturnTypeCustomModifiers: Array[Type], parameterTypes: Array[Type], requiredParameterTypeCustomModifiers: Array[Array[Type]], optionalParameterTypeCustomModifiers: Array[Array[Type]]) -> MethodBuilder
        """
        ...

    def DefineInitializedData(self, name:str, data:Array, attributes:FieldAttributes) -> FieldBuilder:
        """ DefineInitializedData(self: ModuleBuilder, name: str, data: Array[Byte], attributes: FieldAttributes) -> FieldBuilder """
        ...

    def DefineManifestResource(self, name:str, stream:Stream, attribute:ResourceAttributes): # -> 
        """ DefineManifestResource(self: ModuleBuilder, name: str, stream: Stream, attribute: ResourceAttributes) """
        ...

    def DefinePInvokeMethod(self, name, dllName, *__args) -> MethodBuilder:
        """
        DefinePInvokeMethod(self: ModuleBuilder, name: str, dllName: str, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: Type, parameterTypes: Array[Type], nativeCallConv: CallingConvention, nativeCharSet: CharSet) -> MethodBuilder
        DefinePInvokeMethod(self: ModuleBuilder, name: str, dllName: str, entryName: str, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: Type, parameterTypes: Array[Type], nativeCallConv: CallingConvention, nativeCharSet: CharSet) -> MethodBuilder
        """
        ...

    def DefineResource(self, name:str, description:str, attribute:ResourceAttributes = ...) -> IResourceWriter:
        """
        DefineResource(self: ModuleBuilder, name: str, description: str) -> IResourceWriter
        DefineResource(self: ModuleBuilder, name: str, description: str, attribute: ResourceAttributes) -> IResourceWriter
        """
        ...

    def DefineType(self, name:str, attr:TypeAttributes = ..., parent:Type = ..., *__args:Array) -> TypeBuilder:
        """
        DefineType(self: ModuleBuilder, name: str, attr: TypeAttributes, parent: Type, interfaces: Array[Type]) -> TypeBuilder
        DefineType(self: ModuleBuilder, name: str) -> TypeBuilder
        DefineType(self: ModuleBuilder, name: str, attr: TypeAttributes) -> TypeBuilder
        DefineType(self: ModuleBuilder, name: str, attr: TypeAttributes, parent: Type) -> TypeBuilder
        DefineType(self: ModuleBuilder, name: str, attr: TypeAttributes, parent: Type, typesize: int) -> TypeBuilder
        DefineType(self: ModuleBuilder, name: str, attr: TypeAttributes, parent: Type, packingSize: PackingSize, typesize: int) -> TypeBuilder
        DefineType(self: ModuleBuilder, name: str, attr: TypeAttributes, parent: Type, packsize: PackingSize) -> TypeBuilder
        """
        ...

    def DefineUninitializedData(self, name:str, size:int, attributes:FieldAttributes) -> FieldBuilder:
        """ DefineUninitializedData(self: ModuleBuilder, name: str, size: int, attributes: FieldAttributes) -> FieldBuilder """
        ...

    def DefineUnmanagedResource(self, *__args:Array): # -> 
        """ DefineUnmanagedResource(self: ModuleBuilder, resource: Array[Byte])DefineUnmanagedResource(self: ModuleBuilder, resourceFileName: str) """
        ...

    def GetArrayMethod(self, arrayClass:Type, methodName:str, callingConvention:CallingConventions, returnType:Type, parameterTypes:Array) -> MethodInfo:
        """ GetArrayMethod(self: ModuleBuilder, arrayClass: Type, methodName: str, callingConvention: CallingConventions, returnType: Type, parameterTypes: Array[Type]) -> MethodInfo """
        ...

    def GetArrayMethodToken(self, arrayClass:Type, methodName:str, callingConvention:CallingConventions, returnType:Type, parameterTypes:Array) -> MethodToken:
        """ GetArrayMethodToken(self: ModuleBuilder, arrayClass: Type, methodName: str, callingConvention: CallingConventions, returnType: Type, parameterTypes: Array[Type]) -> MethodToken """
        ...

    def GetConstructorToken(self, *__args:ConstructorInfo) -> MethodToken:
        """
        GetConstructorToken(self: ModuleBuilder, constructor: ConstructorInfo, optionalParameterTypes: IEnumerable[Type]) -> MethodToken
        GetConstructorToken(self: ModuleBuilder, con: ConstructorInfo) -> MethodToken
        """
        ...

    def GetFieldToken(self, field:FieldInfo) -> FieldToken:
        """ GetFieldToken(self: ModuleBuilder, field: FieldInfo) -> FieldToken """
        ...

    def GetMethodToken(self, method:MethodInfo, optionalParameterTypes:IEnumerable = ...) -> MethodToken:
        """
        GetMethodToken(self: ModuleBuilder, method: MethodInfo) -> MethodToken
        GetMethodToken(self: ModuleBuilder, method: MethodInfo, optionalParameterTypes: IEnumerable[Type]) -> MethodToken
        """
        ...

    def GetSignatureToken(self, *__args:SignatureHelper) -> SignatureToken:
        """
        GetSignatureToken(self: ModuleBuilder, sigHelper: SignatureHelper) -> SignatureToken
        GetSignatureToken(self: ModuleBuilder, sigBytes: Array[Byte], sigLength: int) -> SignatureToken
        """
        ...

    def GetStringConstant(self, str:str) -> StringToken:
        """ GetStringConstant(self: ModuleBuilder, str: str) -> StringToken """
        ...

    def GetSymWriter(self) -> ISymbolWriter:
        """ GetSymWriter(self: ModuleBuilder) -> ISymbolWriter """
        ...

    def GetTypeToken(self, *__args:Type) -> TypeToken:
        """
        GetTypeToken(self: ModuleBuilder, type: Type) -> TypeToken
        GetTypeToken(self: ModuleBuilder, name: str) -> TypeToken
        """
        ...

    def IsTransient(self) -> bool:
        """ IsTransient(self: ModuleBuilder) -> bool """
        ...

    def SetCustomAttribute(self, *__args:CustomAttributeBuilder): # -> 
        """ SetCustomAttribute(self: ModuleBuilder, con: ConstructorInfo, binaryAttribute: Array[Byte])SetCustomAttribute(self: ModuleBuilder, customBuilder: CustomAttributeBuilder) """
        ...

    def SetSymCustomAttribute(self, name:str, data:Array): # -> 
        """ SetSymCustomAttribute(self: ModuleBuilder, name: str, data: Array[Byte]) """
        ...

    def SetUserEntryPoint(self, entryPoint:MethodInfo): # -> 
        """ SetUserEntryPoint(self: ModuleBuilder, entryPoint: MethodInfo) """
        ...


class OpCode: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def FlowControl(self) -> FlowControl:
        """ Get: FlowControl(self: OpCode) -> FlowControl """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: OpCode) -> str """
        ...

    @property
    def OpCodeType(self) -> OpCodeType:
        """ Get: OpCodeType(self: OpCode) -> OpCodeType """
        ...

    @property
    def OperandType(self) -> OperandType:
        """ Get: OperandType(self: OpCode) -> OperandType """
        ...

    @property
    def Size(self) -> int:
        """ Get: Size(self: OpCode) -> int """
        ...

    @property
    def StackBehaviourPop(self) -> StackBehaviour:
        """ Get: StackBehaviourPop(self: OpCode) -> StackBehaviour """
        ...

    @property
    def StackBehaviourPush(self) -> StackBehaviour:
        """ Get: StackBehaviourPush(self: OpCode) -> StackBehaviour """
        ...

    @property
    def Value(self) -> Int16:
        """ Get: Value(self: OpCode) -> Int16 """
        ...


    def Equals(self, obj:OpCode) -> bool:
        """
        Equals(self: OpCode, obj: OpCode) -> bool
        Equals(self: OpCode, obj: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: OpCode) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: OpCode) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class OpCodes: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def TakesSingleByteArgument(inst:OpCode) -> bool:
        """ TakesSingleByteArgument(inst: OpCode) -> bool """
        ...

    Add: OpCode = ...
    Add_Ovf: OpCode = ...
    Add_Ovf_Un: OpCode = ...
    And: OpCode = ...
    Arglist: OpCode = ...
    Beq: OpCode = ...
    Beq_S: OpCode = ...
    Bge: OpCode = ...
    Bge_S: OpCode = ...
    Bge_Un: OpCode = ...
    Bge_Un_S: OpCode = ...
    Bgt: OpCode = ...
    Bgt_S: OpCode = ...
    Bgt_Un: OpCode = ...
    Bgt_Un_S: OpCode = ...
    Ble: OpCode = ...
    Ble_S: OpCode = ...
    Ble_Un: OpCode = ...
    Ble_Un_S: OpCode = ...
    Blt: OpCode = ...
    Blt_S: OpCode = ...
    Blt_Un: OpCode = ...
    Blt_Un_S: OpCode = ...
    Bne_Un: OpCode = ...
    Bne_Un_S: OpCode = ...
    Box: OpCode = ...
    Br: OpCode = ...
    Break: OpCode = ...
    Brfalse: OpCode = ...
    Brfalse_S: OpCode = ...
    Brtrue: OpCode = ...
    Brtrue_S: OpCode = ...
    Br_S: OpCode = ...
    Call: OpCode = ...
    Calli: OpCode = ...
    Callvirt: OpCode = ...
    Castclass: OpCode = ...
    Ceq: OpCode = ...
    Cgt: OpCode = ...
    Cgt_Un: OpCode = ...
    Ckfinite: OpCode = ...
    Clt: OpCode = ...
    Clt_Un: OpCode = ...
    Constrained: OpCode = ...
    Conv_I: OpCode = ...
    Conv_I1: OpCode = ...
    Conv_I2: OpCode = ...
    Conv_I4: OpCode = ...
    Conv_I8: OpCode = ...
    Conv_Ovf_I: OpCode = ...
    Conv_Ovf_I1: OpCode = ...
    Conv_Ovf_I1_Un: OpCode = ...
    Conv_Ovf_I2: OpCode = ...
    Conv_Ovf_I2_Un: OpCode = ...
    Conv_Ovf_I4: OpCode = ...
    Conv_Ovf_I4_Un: OpCode = ...
    Conv_Ovf_I8: OpCode = ...
    Conv_Ovf_I8_Un: OpCode = ...
    Conv_Ovf_I_Un: OpCode = ...
    Conv_Ovf_U: OpCode = ...
    Conv_Ovf_U1: OpCode = ...
    Conv_Ovf_U1_Un: OpCode = ...
    Conv_Ovf_U2: OpCode = ...
    Conv_Ovf_U2_Un: OpCode = ...
    Conv_Ovf_U4: OpCode = ...
    Conv_Ovf_U4_Un: OpCode = ...
    Conv_Ovf_U8: OpCode = ...
    Conv_Ovf_U8_Un: OpCode = ...
    Conv_Ovf_U_Un: OpCode = ...
    Conv_R4: OpCode = ...
    Conv_R8: OpCode = ...
    Conv_R_Un: OpCode = ...
    Conv_U: OpCode = ...
    Conv_U1: OpCode = ...
    Conv_U2: OpCode = ...
    Conv_U4: OpCode = ...
    Conv_U8: OpCode = ...
    Cpblk: OpCode = ...
    Cpobj: OpCode = ...
    Div: OpCode = ...
    Div_Un: OpCode = ...
    Dup: OpCode = ...
    Endfilter: OpCode = ...
    Endfinally: OpCode = ...
    Initblk: OpCode = ...
    Initobj: OpCode = ...
    Isinst: OpCode = ...
    Jmp: OpCode = ...
    Ldarg: OpCode = ...
    Ldarga: OpCode = ...
    Ldarga_S: OpCode = ...
    Ldarg_0: OpCode = ...
    Ldarg_1: OpCode = ...
    Ldarg_2: OpCode = ...
    Ldarg_3: OpCode = ...
    Ldarg_S: OpCode = ...
    Ldc_I4: OpCode = ...
    Ldc_I4_0: OpCode = ...
    Ldc_I4_1: OpCode = ...
    Ldc_I4_2: OpCode = ...
    Ldc_I4_3: OpCode = ...
    Ldc_I4_4: OpCode = ...
    Ldc_I4_5: OpCode = ...
    Ldc_I4_6: OpCode = ...
    Ldc_I4_7: OpCode = ...
    Ldc_I4_8: OpCode = ...
    Ldc_I4_M1: OpCode = ...
    Ldc_I4_S: OpCode = ...
    Ldc_I8: OpCode = ...
    Ldc_R4: OpCode = ...
    Ldc_R8: OpCode = ...
    Ldelem: OpCode = ...
    Ldelema: OpCode = ...
    Ldelem_I: OpCode = ...
    Ldelem_I1: OpCode = ...
    Ldelem_I2: OpCode = ...
    Ldelem_I4: OpCode = ...
    Ldelem_I8: OpCode = ...
    Ldelem_R4: OpCode = ...
    Ldelem_R8: OpCode = ...
    Ldelem_Ref: OpCode = ...
    Ldelem_U1: OpCode = ...
    Ldelem_U2: OpCode = ...
    Ldelem_U4: OpCode = ...
    Ldfld: OpCode = ...
    Ldflda: OpCode = ...
    Ldftn: OpCode = ...
    Ldind_I: OpCode = ...
    Ldind_I1: OpCode = ...
    Ldind_I2: OpCode = ...
    Ldind_I4: OpCode = ...
    Ldind_I8: OpCode = ...
    Ldind_R4: OpCode = ...
    Ldind_R8: OpCode = ...
    Ldind_Ref: OpCode = ...
    Ldind_U1: OpCode = ...
    Ldind_U2: OpCode = ...
    Ldind_U4: OpCode = ...
    Ldlen: OpCode = ...
    Ldloc: OpCode = ...
    Ldloca: OpCode = ...
    Ldloca_S: OpCode = ...
    Ldloc_0: OpCode = ...
    Ldloc_1: OpCode = ...
    Ldloc_2: OpCode = ...
    Ldloc_3: OpCode = ...
    Ldloc_S: OpCode = ...
    Ldnull: OpCode = ...
    Ldobj: OpCode = ...
    Ldsfld: OpCode = ...
    Ldsflda: OpCode = ...
    Ldstr: OpCode = ...
    Ldtoken: OpCode = ...
    Ldvirtftn: OpCode = ...
    Leave: OpCode = ...
    Leave_S: OpCode = ...
    Localloc: OpCode = ...
    Mkrefany: OpCode = ...
    Mul: OpCode = ...
    Mul_Ovf: OpCode = ...
    Mul_Ovf_Un: OpCode = ...
    Neg: OpCode = ...
    Newarr: OpCode = ...
    Newobj: OpCode = ...
    Nop: OpCode = ...
    Not: OpCode = ...
    Or: OpCode = ...
    Pop: OpCode = ...
    Prefix1: OpCode = ...
    Prefix2: OpCode = ...
    Prefix3: OpCode = ...
    Prefix4: OpCode = ...
    Prefix5: OpCode = ...
    Prefix6: OpCode = ...
    Prefix7: OpCode = ...
    Prefixref: OpCode = ...
    Readonly: OpCode = ...
    Refanytype: OpCode = ...
    Refanyval: OpCode = ...
    Rem: OpCode = ...
    Rem_Un: OpCode = ...
    Ret: OpCode = ...
    Rethrow: OpCode = ...
    Shl: OpCode = ...
    Shr: OpCode = ...
    Shr_Un: OpCode = ...
    Sizeof: OpCode = ...
    Starg: OpCode = ...
    Starg_S: OpCode = ...
    Stelem: OpCode = ...
    Stelem_I: OpCode = ...
    Stelem_I1: OpCode = ...
    Stelem_I2: OpCode = ...
    Stelem_I4: OpCode = ...
    Stelem_I8: OpCode = ...
    Stelem_R4: OpCode = ...
    Stelem_R8: OpCode = ...
    Stelem_Ref: OpCode = ...
    Stfld: OpCode = ...
    Stind_I: OpCode = ...
    Stind_I1: OpCode = ...
    Stind_I2: OpCode = ...
    Stind_I4: OpCode = ...
    Stind_I8: OpCode = ...
    Stind_R4: OpCode = ...
    Stind_R8: OpCode = ...
    Stind_Ref: OpCode = ...
    Stloc: OpCode = ...
    Stloc_0: OpCode = ...
    Stloc_1: OpCode = ...
    Stloc_2: OpCode = ...
    Stloc_3: OpCode = ...
    Stloc_S: OpCode = ...
    Stobj: OpCode = ...
    Stsfld: OpCode = ...
    Sub: OpCode = ...
    Sub_Ovf: OpCode = ...
    Sub_Ovf_Un: OpCode = ...
    Switch: OpCode = ...
    Tailcall: OpCode = ...
    Throw: OpCode = ...
    Unaligned: OpCode = ...
    Unbox: OpCode = ...
    Unbox_Any: OpCode = ...
    Volatile: OpCode = ...
    Xor: OpCode = ...
    __call__: OpCode = ...


class OpCodeType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OpCodeType, values: Annotation (0), Macro (1), Nternal (2), Objmodel (3), Prefix (4), Primitive (5) """
    Annotation: OpCodeType = ...
    Macro: OpCodeType = ...
    Nternal: OpCodeType = ...
    Objmodel: OpCodeType = ...
    Prefix: OpCodeType = ...
    Primitive: OpCodeType = ...
    value__ = ...


class OperandType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OperandType, values: InlineBrTarget (0), InlineField (1), InlineI (2), InlineI8 (3), InlineMethod (4), InlineNone (5), InlinePhi (6), InlineR (7), InlineSig (9), InlineString (10), InlineSwitch (11), InlineTok (12), InlineType (13), InlineVar (14), ShortInlineBrTarget (15), ShortInlineI (16), ShortInlineR (17), ShortInlineVar (18) """
    InlineBrTarget: OperandType = ...
    InlineField: OperandType = ...
    InlineI: OperandType = ...
    InlineI8: OperandType = ...
    InlineMethod: OperandType = ...
    InlineNone: OperandType = ...
    InlinePhi: OperandType = ...
    InlineR: OperandType = ...
    InlineSig: OperandType = ...
    InlineString: OperandType = ...
    InlineSwitch: OperandType = ...
    InlineTok: OperandType = ...
    InlineType: OperandType = ...
    InlineVar: OperandType = ...
    ShortInlineBrTarget: OperandType = ...
    ShortInlineI: OperandType = ...
    ShortInlineR: OperandType = ...
    ShortInlineVar: OperandType = ...
    value__ = ...


class PackingSize(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PackingSize, values: Size1 (1), Size128 (128), Size16 (16), Size2 (2), Size32 (32), Size4 (4), Size64 (64), Size8 (8), Unspecified (0) """
    Size1: PackingSize = ...
    Size128: PackingSize = ...
    Size16: PackingSize = ...
    Size2: PackingSize = ...
    Size32: PackingSize = ...
    Size4: PackingSize = ...
    Size64: PackingSize = ...
    Size8: PackingSize = ...
    Unspecified: PackingSize = ...
    value__ = ...


class ParameterBuilder(_ParameterBuilder): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> int:
        """ Get: Attributes(self: ParameterBuilder) -> int """
        ...

    @property
    def IsIn(self) -> bool:
        """ Get: IsIn(self: ParameterBuilder) -> bool """
        ...

    @property
    def IsOptional(self) -> bool:
        """ Get: IsOptional(self: ParameterBuilder) -> bool """
        ...

    @property
    def IsOut(self) -> bool:
        """ Get: IsOut(self: ParameterBuilder) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ParameterBuilder) -> str """
        ...

    @property
    def Position(self) -> int:
        """ Get: Position(self: ParameterBuilder) -> int """
        ...


    def GetToken(self) -> ParameterToken:
        """ GetToken(self: ParameterBuilder) -> ParameterToken """
        ...

    def SetConstant(self, defaultValue:object): # -> 
        """ SetConstant(self: ParameterBuilder, defaultValue: object) """
        ...

    def SetCustomAttribute(self, *__args:CustomAttributeBuilder): # -> 
        """ SetCustomAttribute(self: ParameterBuilder, con: ConstructorInfo, binaryAttribute: Array[Byte])SetCustomAttribute(self: ParameterBuilder, customBuilder: CustomAttributeBuilder) """
        ...

    def SetMarshal(self, unmanagedMarshal:UnmanagedMarshal): # -> 
        """ SetMarshal(self: ParameterBuilder, unmanagedMarshal: UnmanagedMarshal) """
        ...


class ParameterToken: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Token(self) -> int:
        """ Get: Token(self: ParameterToken) -> int """
        ...


    def Equals(self, obj:object) -> bool:
        """
        Equals(self: ParameterToken, obj: object) -> bool
        Equals(self: ParameterToken, obj: ParameterToken) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ParameterToken) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Empty: ParameterToken = ...


class PEFileKinds(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PEFileKinds, values: ConsoleApplication (2), Dll (1), WindowApplication (3) """
    ConsoleApplication: PEFileKinds = ...
    Dll: PEFileKinds = ...
    value__ = ...
    WindowApplication: PEFileKinds = ...


class PropertyBuilder(PropertyInfo, _PropertyBuilder): # skipped bases: <type '_MemberInfo'>, <type 'ICustomAttributeProvider'>, <type '_PropertyInfo'>, <type 'object'>
    """ no doc """
    @property
    def Module(self) -> Module:
        """ Get: Module(self: PropertyBuilder) -> Module """
        ...

    @property
    def PropertyToken(self) -> PropertyToken:
        """ Get: PropertyToken(self: PropertyBuilder) -> PropertyToken """
        ...


    def AddOtherMethod(self, mdBuilder:MethodBuilder): # -> 
        """ AddOtherMethod(self: PropertyBuilder, mdBuilder: MethodBuilder) """
        ...

    def SetConstant(self, defaultValue:object): # -> 
        """ SetConstant(self: PropertyBuilder, defaultValue: object) """
        ...

    def SetCustomAttribute(self, *__args:CustomAttributeBuilder): # -> 
        """ SetCustomAttribute(self: PropertyBuilder, con: ConstructorInfo, binaryAttribute: Array[Byte])SetCustomAttribute(self: PropertyBuilder, customBuilder: CustomAttributeBuilder) """
        ...

    def SetGetMethod(self, mdBuilder:MethodBuilder): # -> 
        """ SetGetMethod(self: PropertyBuilder, mdBuilder: MethodBuilder) """
        ...

    def SetSetMethod(self, mdBuilder:MethodBuilder): # -> 
        """ SetSetMethod(self: PropertyBuilder, mdBuilder: MethodBuilder) """
        ...


class PropertyToken: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Token(self) -> int:
        """ Get: Token(self: PropertyToken) -> int """
        ...


    def Equals(self, obj:object) -> bool:
        """
        Equals(self: PropertyToken, obj: object) -> bool
        Equals(self: PropertyToken, obj: PropertyToken) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: PropertyToken) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Empty: PropertyToken = ...


class SignatureHelper(_SignatureHelper): # skipped bases: <type 'object'>
    """ no doc """
    def AddArgument(self, *__args:Type): # -> 
        """ AddArgument(self: SignatureHelper, clsArgument: Type)AddArgument(self: SignatureHelper, argument: Type, pinned: bool)AddArgument(self: SignatureHelper, argument: Type, requiredCustomModifiers: Array[Type], optionalCustomModifiers: Array[Type]) """
        ...

    def AddArguments(self, arguments:Array, requiredCustomModifiers:Array, optionalCustomModifiers:Array): # -> 
        """ AddArguments(self: SignatureHelper, arguments: Array[Type], requiredCustomModifiers: Array[Array[Type]], optionalCustomModifiers: Array[Array[Type]]) """
        ...

    def AddSentinel(self): # -> 
        """ AddSentinel(self: SignatureHelper) """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: SignatureHelper, obj: object) -> bool """
        ...

    @staticmethod
    def GetFieldSigHelper(mod:Module) -> SignatureHelper:
        """ GetFieldSigHelper(mod: Module) -> SignatureHelper """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SignatureHelper) -> int """
        ...

    @staticmethod
    def GetLocalVarSigHelper(mod=None) -> SignatureHelper:
        """
        GetLocalVarSigHelper() -> SignatureHelper
        GetLocalVarSigHelper(mod: Module) -> SignatureHelper
        """
        ...

    @staticmethod
    def GetMethodSigHelper(*__args) -> SignatureHelper:
        """
        GetMethodSigHelper(mod: Module, returnType: Type, parameterTypes: Array[Type]) -> SignatureHelper
        GetMethodSigHelper(mod: Module, callingConvention: CallingConventions, returnType: Type) -> SignatureHelper
        GetMethodSigHelper(mod: Module, unmanagedCallConv: CallingConvention, returnType: Type) -> SignatureHelper
        GetMethodSigHelper(callingConvention: CallingConventions, returnType: Type) -> SignatureHelper
        GetMethodSigHelper(unmanagedCallingConvention: CallingConvention, returnType: Type) -> SignatureHelper
        """
        ...

    @staticmethod
    def GetPropertySigHelper(mod, *__args) -> SignatureHelper:
        """
        GetPropertySigHelper(mod: Module, returnType: Type, parameterTypes: Array[Type]) -> SignatureHelper
        GetPropertySigHelper(mod: Module, returnType: Type, requiredReturnTypeCustomModifiers: Array[Type], optionalReturnTypeCustomModifiers: Array[Type], parameterTypes: Array[Type], requiredParameterTypeCustomModifiers: Array[Array[Type]], optionalParameterTypeCustomModifiers: Array[Array[Type]]) -> SignatureHelper
        GetPropertySigHelper(mod: Module, callingConvention: CallingConventions, returnType: Type, requiredReturnTypeCustomModifiers: Array[Type], optionalReturnTypeCustomModifiers: Array[Type], parameterTypes: Array[Type], requiredParameterTypeCustomModifiers: Array[Array[Type]], optionalParameterTypeCustomModifiers: Array[Array[Type]]) -> SignatureHelper
        """
        ...

    def GetSignature(self) -> Array:
        """ GetSignature(self: SignatureHelper) -> Array[Byte] """
        ...

    def ToString(self) -> str:
        """ ToString(self: SignatureHelper) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SignatureToken: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Token(self) -> int:
        """ Get: Token(self: SignatureToken) -> int """
        ...


    def Equals(self, obj:object) -> bool:
        """
        Equals(self: SignatureToken, obj: object) -> bool
        Equals(self: SignatureToken, obj: SignatureToken) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SignatureToken) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Empty: SignatureToken = ...


class StackBehaviour(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StackBehaviour, values: Pop0 (0), Pop1 (1), Pop1_pop1 (2), Popi (3), Popi_pop1 (4), Popi_popi (5), Popi_popi_popi (7), Popi_popi8 (6), Popi_popr4 (8), Popi_popr8 (9), Popref (10), Popref_pop1 (11), Popref_popi (12), Popref_popi_pop1 (28), Popref_popi_popi (13), Popref_popi_popi8 (14), Popref_popi_popr4 (15), Popref_popi_popr8 (16), Popref_popi_popref (17), Push0 (18), Push1 (19), Push1_push1 (20), Pushi (21), Pushi8 (22), Pushr4 (23), Pushr8 (24), Pushref (25), Varpop (26), Varpush (27) """
    Pop0: StackBehaviour = ...
    Pop1: StackBehaviour = ...
    Pop1_pop1: StackBehaviour = ...
    Popi: StackBehaviour = ...
    Popi_pop1: StackBehaviour = ...
    Popi_popi: StackBehaviour = ...
    Popi_popi8: StackBehaviour = ...
    Popi_popi_popi: StackBehaviour = ...
    Popi_popr4: StackBehaviour = ...
    Popi_popr8: StackBehaviour = ...
    Popref: StackBehaviour = ...
    Popref_pop1: StackBehaviour = ...
    Popref_popi: StackBehaviour = ...
    Popref_popi_pop1: StackBehaviour = ...
    Popref_popi_popi: StackBehaviour = ...
    Popref_popi_popi8: StackBehaviour = ...
    Popref_popi_popr4: StackBehaviour = ...
    Popref_popi_popr8: StackBehaviour = ...
    Popref_popi_popref: StackBehaviour = ...
    Push0: StackBehaviour = ...
    Push1: StackBehaviour = ...
    Push1_push1: StackBehaviour = ...
    Pushi: StackBehaviour = ...
    Pushi8: StackBehaviour = ...
    Pushr4: StackBehaviour = ...
    Pushr8: StackBehaviour = ...
    Pushref: StackBehaviour = ...
    value__ = ...
    Varpop: StackBehaviour = ...
    Varpush: StackBehaviour = ...


class StringToken: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Token(self) -> int:
        """ Get: Token(self: StringToken) -> int """
        ...


    def Equals(self, obj:object) -> bool:
        """
        Equals(self: StringToken, obj: object) -> bool
        Equals(self: StringToken, obj: StringToken) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: StringToken) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TypeBuilder(TypeInfo, _TypeBuilder): # skipped bases: <type '_MemberInfo'>, <type 'ICustomAttributeProvider'>, <type 'IReflect'>, <type 'IReflectableType'>, <type '_Type'>, <type 'object'>
    """ no doc """
    @property
    def DeclaringMethod(self) -> MethodBase:
        """ Get: DeclaringMethod(self: TypeBuilder) -> MethodBase """
        ...

    @property
    def GenericParameterAttributes(self) -> GenericParameterAttributes:
        """ Get: GenericParameterAttributes(self: TypeBuilder) -> GenericParameterAttributes """
        ...

    @property
    def GenericParameterPosition(self) -> int:
        """ Get: GenericParameterPosition(self: TypeBuilder) -> int """
        ...

    @property
    def IsConstructedGenericType(self) -> bool:
        """ Get: IsConstructedGenericType(self: TypeBuilder) -> bool """
        ...

    @property
    def IsGenericParameter(self) -> bool:
        """ Get: IsGenericParameter(self: TypeBuilder) -> bool """
        ...

    @property
    def IsGenericType(self) -> bool:
        """ Get: IsGenericType(self: TypeBuilder) -> bool """
        ...

    @property
    def IsGenericTypeDefinition(self) -> bool:
        """ Get: IsGenericTypeDefinition(self: TypeBuilder) -> bool """
        ...

    @property
    def IsSecurityCritical(self) -> bool:
        """ Get: IsSecurityCritical(self: TypeBuilder) -> bool """
        ...

    @property
    def IsSecuritySafeCritical(self) -> bool:
        """ Get: IsSecuritySafeCritical(self: TypeBuilder) -> bool """
        ...

    @property
    def IsSecurityTransparent(self) -> bool:
        """ Get: IsSecurityTransparent(self: TypeBuilder) -> bool """
        ...

    @property
    def PackingSize(self) -> PackingSize:
        """ Get: PackingSize(self: TypeBuilder) -> PackingSize """
        ...

    @property
    def Size(self) -> int:
        """ Get: Size(self: TypeBuilder) -> int """
        ...

    @property
    def TypeToken(self) -> TypeToken:
        """ Get: TypeToken(self: TypeBuilder) -> TypeToken """
        ...


    def AddDeclarativeSecurity(self, action:SecurityAction, pset:PermissionSet): # -> 
        """ AddDeclarativeSecurity(self: TypeBuilder, action: SecurityAction, pset: PermissionSet) """
        ...

    def AddInterfaceImplementation(self, interfaceType:Type): # -> 
        """ AddInterfaceImplementation(self: TypeBuilder, interfaceType: Type) """
        ...

    def CreateType(self) -> Type:
        """ CreateType(self: TypeBuilder) -> Type """
        ...

    def CreateTypeInfo(self) -> TypeInfo:
        """ CreateTypeInfo(self: TypeBuilder) -> TypeInfo """
        ...

    def DefineConstructor(self, attributes:MethodAttributes, callingConvention:CallingConventions, parameterTypes:Array, requiredCustomModifiers:Array = ..., optionalCustomModifiers:Array = ...) -> ConstructorBuilder:
        """
        DefineConstructor(self: TypeBuilder, attributes: MethodAttributes, callingConvention: CallingConventions, parameterTypes: Array[Type]) -> ConstructorBuilder
        DefineConstructor(self: TypeBuilder, attributes: MethodAttributes, callingConvention: CallingConventions, parameterTypes: Array[Type], requiredCustomModifiers: Array[Array[Type]], optionalCustomModifiers: Array[Array[Type]]) -> ConstructorBuilder
        """
        ...

    def DefineDefaultConstructor(self, attributes:MethodAttributes) -> ConstructorBuilder:
        """ DefineDefaultConstructor(self: TypeBuilder, attributes: MethodAttributes) -> ConstructorBuilder """
        ...

    def DefineEvent(self, name:str, attributes:EventAttributes, eventtype:Type) -> EventBuilder:
        """ DefineEvent(self: TypeBuilder, name: str, attributes: EventAttributes, eventtype: Type) -> EventBuilder """
        ...

    def DefineField(self, fieldName:str, type:Type, *__args:FieldAttributes) -> FieldBuilder:
        """
        DefineField(self: TypeBuilder, fieldName: str, type: Type, requiredCustomModifiers: Array[Type], optionalCustomModifiers: Array[Type], attributes: FieldAttributes) -> FieldBuilder
        DefineField(self: TypeBuilder, fieldName: str, type: Type, attributes: FieldAttributes) -> FieldBuilder
        """
        ...

    def DefineGenericParameters(self, names:Array) -> Array:
        """ DefineGenericParameters(self: TypeBuilder, *names: Array[str]) -> Array[GenericTypeParameterBuilder] """
        ...

    def DefineInitializedData(self, name:str, data:Array, attributes:FieldAttributes) -> FieldBuilder:
        """ DefineInitializedData(self: TypeBuilder, name: str, data: Array[Byte], attributes: FieldAttributes) -> FieldBuilder """
        ...

    def DefineMethod(self, name:str, attributes:MethodAttributes, *__args:CallingConventions) -> MethodBuilder:
        """
        DefineMethod(self: TypeBuilder, name: str, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: Type, returnTypeRequiredCustomModifiers: Array[Type], returnTypeOptionalCustomModifiers: Array[Type], parameterTypes: Array[Type], parameterTypeRequiredCustomModifiers: Array[Array[Type]], parameterTypeOptionalCustomModifiers: Array[Array[Type]]) -> MethodBuilder
        DefineMethod(self: TypeBuilder, name: str, attributes: MethodAttributes, returnType: Type, parameterTypes: Array[Type]) -> MethodBuilder
        DefineMethod(self: TypeBuilder, name: str, attributes: MethodAttributes) -> MethodBuilder
        DefineMethod(self: TypeBuilder, name: str, attributes: MethodAttributes, callingConvention: CallingConventions) -> MethodBuilder
        DefineMethod(self: TypeBuilder, name: str, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: Type, parameterTypes: Array[Type]) -> MethodBuilder
        """
        ...

    def DefineMethodOverride(self, methodInfoBody:MethodInfo, methodInfoDeclaration:MethodInfo): # -> 
        """ DefineMethodOverride(self: TypeBuilder, methodInfoBody: MethodInfo, methodInfoDeclaration: MethodInfo) """
        ...

    def DefineNestedType(self, name:str, attr:TypeAttributes = ..., parent:Type = ..., *__args:Array) -> TypeBuilder:
        """
        DefineNestedType(self: TypeBuilder, name: str) -> TypeBuilder
        DefineNestedType(self: TypeBuilder, name: str, attr: TypeAttributes, parent: Type, interfaces: Array[Type]) -> TypeBuilder
        DefineNestedType(self: TypeBuilder, name: str, attr: TypeAttributes, parent: Type) -> TypeBuilder
        DefineNestedType(self: TypeBuilder, name: str, attr: TypeAttributes) -> TypeBuilder
        DefineNestedType(self: TypeBuilder, name: str, attr: TypeAttributes, parent: Type, typeSize: int) -> TypeBuilder
        DefineNestedType(self: TypeBuilder, name: str, attr: TypeAttributes, parent: Type, packSize: PackingSize) -> TypeBuilder
        DefineNestedType(self: TypeBuilder, name: str, attr: TypeAttributes, parent: Type, packSize: PackingSize, typeSize: int) -> TypeBuilder
        """
        ...

    def DefinePInvokeMethod(self, name, dllName, *__args) -> MethodBuilder:
        """
        DefinePInvokeMethod(self: TypeBuilder, name: str, dllName: str, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: Type, parameterTypes: Array[Type], nativeCallConv: CallingConvention, nativeCharSet: CharSet) -> MethodBuilder
        DefinePInvokeMethod(self: TypeBuilder, name: str, dllName: str, entryName: str, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: Type, parameterTypes: Array[Type], nativeCallConv: CallingConvention, nativeCharSet: CharSet) -> MethodBuilder
        DefinePInvokeMethod(self: TypeBuilder, name: str, dllName: str, entryName: str, attributes: MethodAttributes, callingConvention: CallingConventions, returnType: Type, returnTypeRequiredCustomModifiers: Array[Type], returnTypeOptionalCustomModifiers: Array[Type], parameterTypes: Array[Type], parameterTypeRequiredCustomModifiers: Array[Array[Type]], parameterTypeOptionalCustomModifiers: Array[Array[Type]], nativeCallConv: CallingConvention, nativeCharSet: CharSet) -> MethodBuilder
        """
        ...

    def DefineProperty(self, name, attributes, *__args) -> PropertyBuilder:
        """
        DefineProperty(self: TypeBuilder, name: str, attributes: PropertyAttributes, callingConvention: CallingConventions, returnType: Type, returnTypeRequiredCustomModifiers: Array[Type], returnTypeOptionalCustomModifiers: Array[Type], parameterTypes: Array[Type], parameterTypeRequiredCustomModifiers: Array[Array[Type]], parameterTypeOptionalCustomModifiers: Array[Array[Type]]) -> PropertyBuilder
        DefineProperty(self: TypeBuilder, name: str, attributes: PropertyAttributes, returnType: Type, parameterTypes: Array[Type]) -> PropertyBuilder
        DefineProperty(self: TypeBuilder, name: str, attributes: PropertyAttributes, callingConvention: CallingConventions, returnType: Type, parameterTypes: Array[Type]) -> PropertyBuilder
        DefineProperty(self: TypeBuilder, name: str, attributes: PropertyAttributes, returnType: Type, returnTypeRequiredCustomModifiers: Array[Type], returnTypeOptionalCustomModifiers: Array[Type], parameterTypes: Array[Type], parameterTypeRequiredCustomModifiers: Array[Array[Type]], parameterTypeOptionalCustomModifiers: Array[Array[Type]]) -> PropertyBuilder
        """
        ...

    def DefineTypeInitializer(self) -> ConstructorBuilder:
        """ DefineTypeInitializer(self: TypeBuilder) -> ConstructorBuilder """
        ...

    def DefineUninitializedData(self, name:str, size:int, attributes:FieldAttributes) -> FieldBuilder:
        """ DefineUninitializedData(self: TypeBuilder, name: str, size: int, attributes: FieldAttributes) -> FieldBuilder """
        ...

    def GetGenericArguments(self) -> Array:
        """ GetGenericArguments(self: TypeBuilder) -> Array[Type] """
        ...

    def GetGenericTypeDefinition(self) -> Type:
        """ GetGenericTypeDefinition(self: TypeBuilder) -> Type """
        ...

    def IsCreated(self) -> bool:
        """ IsCreated(self: TypeBuilder) -> bool """
        ...

    def MakeArrayType(self, rank:int = ...) -> Type:
        """
        MakeArrayType(self: TypeBuilder) -> Type
        MakeArrayType(self: TypeBuilder, rank: int) -> Type
        """
        ...

    def MakeByRefType(self) -> Type:
        """ MakeByRefType(self: TypeBuilder) -> Type """
        ...

    def MakeGenericType(self, typeArguments:Array) -> Type:
        """ MakeGenericType(self: TypeBuilder, *typeArguments: Array[Type]) -> Type """
        ...

    def MakePointerType(self) -> Type:
        """ MakePointerType(self: TypeBuilder) -> Type """
        ...

    def SetCustomAttribute(self, *__args:CustomAttributeBuilder): # -> 
        """ SetCustomAttribute(self: TypeBuilder, con: ConstructorInfo, binaryAttribute: Array[Byte])SetCustomAttribute(self: TypeBuilder, customBuilder: CustomAttributeBuilder) """
        ...

    def SetParent(self, parent:Type): # -> 
        """ SetParent(self: TypeBuilder, parent: Type) """
        ...

    UnspecifiedTypeSize: int = ...


class TypeToken: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Token(self) -> int:
        """ Get: Token(self: TypeToken) -> int """
        ...


    def Equals(self, obj:object) -> bool:
        """
        Equals(self: TypeToken, obj: object) -> bool
        Equals(self: TypeToken, obj: TypeToken) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: TypeToken) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Empty: TypeToken = ...


class UnmanagedMarshal: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BaseType(self) -> UnmanagedType:
        """ Get: BaseType(self: UnmanagedMarshal) -> UnmanagedType """
        ...

    @property
    def ElementCount(self) -> int:
        """ Get: ElementCount(self: UnmanagedMarshal) -> int """
        ...

    @property
    def GetUnmanagedType(self) -> UnmanagedType:
        """ Get: GetUnmanagedType(self: UnmanagedMarshal) -> UnmanagedType """
        ...

    @property
    def IIDGuid(self) -> Guid:
        """ Get: IIDGuid(self: UnmanagedMarshal) -> Guid """
        ...


    @staticmethod
    def DefineByValArray(elemCount:int) -> UnmanagedMarshal:
        """ DefineByValArray(elemCount: int) -> UnmanagedMarshal """
        ...

    @staticmethod
    def DefineByValTStr(elemCount:int) -> UnmanagedMarshal:
        """ DefineByValTStr(elemCount: int) -> UnmanagedMarshal """
        ...

    @staticmethod
    def DefineLPArray(elemType:UnmanagedType) -> UnmanagedMarshal:
        """ DefineLPArray(elemType: UnmanagedType) -> UnmanagedMarshal """
        ...

    @staticmethod
    def DefineSafeArray(elemType:UnmanagedType) -> UnmanagedMarshal:
        """ DefineSafeArray(elemType: UnmanagedType) -> UnmanagedMarshal """
        ...

    @staticmethod
    def DefineUnmanagedMarshal(unmanagedType:UnmanagedType) -> UnmanagedMarshal:
        """ DefineUnmanagedMarshal(unmanagedType: UnmanagedType) -> UnmanagedMarshal """
        ...


