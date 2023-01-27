# encoding: utf-8
# module System.Reflection calls itself Reflection
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (ApplicationException, Array, AsyncCallback, Attribute, 
    Delegate, Enum, FormatException, Guid, IAsyncResult, ICloneable, Int64, 
    MarshalByRefObject, ModuleHandle, MulticastDelegate, ResolveEventArgs, 
    RuntimeFieldHandle, RuntimeMethodHandle, RuntimeTypeHandle, 
    SystemException, Type, UInt32, Version, Void)

from System.Collections import IEnumerable, IList

from System.Configuration.Assemblies import (AssemblyHashAlgorithm, 
    AssemblyVersionCompatibility)

from System.Globalization import CultureInfo

from System.Runtime.InteropServices import (_Assembly, _AssemblyName, 
    _ConstructorInfo, _EventInfo, _FieldInfo, _MemberInfo, _MethodBase, 
    _MethodInfo, _Module, _ParameterInfo, _PropertyInfo)

from System.Runtime.Serialization import (IDeserializationCallback, 
    IObjectReference, ISerializable)

from System.Security import IEvidenceFactory, PermissionSet, SecurityRuleSet

from System.Security.Cryptography.X509Certificates import X509Certificate

from System.Security.Policy import Evidence

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class AmbiguousMatchException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    AmbiguousMatchException()
    AmbiguousMatchException(message: str)
    AmbiguousMatchException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class ICustomAttributeProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetCustomAttributes(self, *__args:bool) -> Array:
        """
        GetCustomAttributes(self: ICustomAttributeProvider, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: ICustomAttributeProvider, inherit: bool) -> Array[object]
        """
        ...

    def IsDefined(self, attributeType:Type, inherit:bool) -> bool:
        """ IsDefined(self: ICustomAttributeProvider, attributeType: Type, inherit: bool) -> bool """
        ...


class Assembly(ISerializable, _Assembly, IEvidenceFactory, ICustomAttributeProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CustomAttributes(self) -> IEnumerable:
        """ Get: CustomAttributes(self: Assembly) -> IEnumerable[CustomAttributeData] """
        ...

    @property
    def DefinedTypes(self) -> IEnumerable:
        """ Get: DefinedTypes(self: Assembly) -> IEnumerable[TypeInfo] """
        ...

    @property
    def ExportedTypes(self) -> IEnumerable:
        """ Get: ExportedTypes(self: Assembly) -> IEnumerable[Type] """
        ...

    @property
    def HostContext(self) -> Int64:
        """ Get: HostContext(self: Assembly) -> Int64 """
        ...

    @property
    def ImageRuntimeVersion(self) -> str:
        """ Get: ImageRuntimeVersion(self: Assembly) -> str """
        ...

    @property
    def IsDynamic(self) -> bool:
        """ Get: IsDynamic(self: Assembly) -> bool """
        ...

    @property
    def IsFullyTrusted(self) -> bool:
        """ Get: IsFullyTrusted(self: Assembly) -> bool """
        ...

    @property
    def ManifestModule(self) -> Module:
        """ Get: ManifestModule(self: Assembly) -> Module """
        ...

    @property
    def Modules(self) -> IEnumerable:
        """ Get: Modules(self: Assembly) -> IEnumerable[Module] """
        ...

    @property
    def PermissionSet(self) -> PermissionSet:
        """ Get: PermissionSet(self: Assembly) -> PermissionSet """
        ...

    @property
    def ReflectionOnly(self) -> bool:
        """ Get: ReflectionOnly(self: Assembly) -> bool """
        ...

    @property
    def SecurityRuleSet(self) -> SecurityRuleSet:
        """ Get: SecurityRuleSet(self: Assembly) -> SecurityRuleSet """
        ...


    @staticmethod
    def CreateQualifiedName(assemblyName:str, typeName:str) -> str:
        """ CreateQualifiedName(assemblyName: str, typeName: str) -> str """
        ...

    @staticmethod
    def GetAssembly(type:Type) -> Assembly:
        """ GetAssembly(type: Type) -> Assembly """
        ...

    @staticmethod
    def GetCallingAssembly() -> Assembly:
        """ GetCallingAssembly() -> Assembly """
        ...

    def GetCustomAttributesData(self) -> IList:
        """ GetCustomAttributesData(self: Assembly) -> IList[CustomAttributeData] """
        ...

    @staticmethod
    def GetEntryAssembly() -> Assembly:
        """ GetEntryAssembly() -> Assembly """
        ...

    @staticmethod
    def GetExecutingAssembly() -> Assembly:
        """ GetExecutingAssembly() -> Assembly """
        ...

    @staticmethod
    def Load(*__args:str) -> Assembly:
        """
        Load(assemblyString: str) -> Assembly
        Load(assemblyString: str, assemblySecurity: Evidence) -> Assembly
        Load(assemblyRef: AssemblyName) -> Assembly
        Load(assemblyRef: AssemblyName, assemblySecurity: Evidence) -> Assembly
        Load(rawAssembly: Array[Byte]) -> Assembly
        Load(rawAssembly: Array[Byte], rawSymbolStore: Array[Byte]) -> Assembly
        Load(rawAssembly: Array[Byte], rawSymbolStore: Array[Byte], securityContextSource: SecurityContextSource) -> Assembly
        Load(rawAssembly: Array[Byte], rawSymbolStore: Array[Byte], securityEvidence: Evidence) -> Assembly
        """
        ...

    @staticmethod
    def LoadFile(path:str, securityEvidence:Evidence = ...) -> Assembly:
        """
        LoadFile(path: str) -> Assembly
        LoadFile(path: str, securityEvidence: Evidence) -> Assembly
        """
        ...

    @staticmethod
    def LoadFrom(assemblyFile:str, *__args:Evidence) -> Assembly:
        """
        LoadFrom(assemblyFile: str) -> Assembly
        LoadFrom(assemblyFile: str, securityEvidence: Evidence) -> Assembly
        LoadFrom(assemblyFile: str, securityEvidence: Evidence, hashValue: Array[Byte], hashAlgorithm: AssemblyHashAlgorithm) -> Assembly
        LoadFrom(assemblyFile: str, hashValue: Array[Byte], hashAlgorithm: AssemblyHashAlgorithm) -> Assembly
        """
        ...

    @staticmethod
    def LoadWithPartialName(partialName:str, securityEvidence:Evidence = ...) -> Assembly:
        """
        LoadWithPartialName(partialName: str) -> Assembly
        LoadWithPartialName(partialName: str, securityEvidence: Evidence) -> Assembly
        """
        ...

    @staticmethod
    def ReflectionOnlyLoad(*__args:str) -> Assembly:
        """
        ReflectionOnlyLoad(assemblyString: str) -> Assembly
        ReflectionOnlyLoad(rawAssembly: Array[Byte]) -> Assembly
        """
        ...

    @staticmethod
    def ReflectionOnlyLoadFrom(assemblyFile:str) -> Assembly:
        """ ReflectionOnlyLoadFrom(assemblyFile: str) -> Assembly """
        ...

    @staticmethod
    def UnsafeLoadFrom(assemblyFile:str) -> Assembly:
        """ UnsafeLoadFrom(assemblyFile: str) -> Assembly """
        ...

    def __dir__(self, *args): #cannot find CLR method
        """ __dir__(self: Assembly) -> list """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    ModuleResolve = ...


class AssemblyAlgorithmIdAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    AssemblyAlgorithmIdAttribute(algorithmId: AssemblyHashAlgorithm)
    AssemblyAlgorithmIdAttribute(algorithmId: UInt32)
    """
    @property
    def AlgorithmId(self) -> UInt32:
        """ Get: AlgorithmId(self: AssemblyAlgorithmIdAttribute) -> UInt32 """
        ...


    def __new__(cls, algorithmId:AssemblyHashAlgorithm) -> Self:
        """
        __new__(cls: type, algorithmId: AssemblyHashAlgorithm)
        __new__(cls: type, algorithmId: UInt32)
        """
        ...


class AssemblyCompanyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyCompanyAttribute(company: str) """
    @property
    def Company(self) -> str:
        """ Get: Company(self: AssemblyCompanyAttribute) -> str """
        ...


    def __new__(cls, company:str) -> Self:
        """ __new__(cls: type, company: str) """
        ...


class AssemblyConfigurationAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyConfigurationAttribute(configuration: str) """
    @property
    def Configuration(self) -> str:
        """ Get: Configuration(self: AssemblyConfigurationAttribute) -> str """
        ...


    def __new__(cls, configuration:str) -> Self:
        """ __new__(cls: type, configuration: str) """
        ...


class AssemblyContentType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AssemblyContentType, values: Default (0), WindowsRuntime (1) """
    Default: AssemblyContentType = ...
    value__ = ...
    WindowsRuntime: AssemblyContentType = ...


class AssemblyCopyrightAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyCopyrightAttribute(copyright: str) """
    @property
    def Copyright(self) -> str:
        """ Get: Copyright(self: AssemblyCopyrightAttribute) -> str """
        ...


    def __new__(cls, copyright:str) -> Self:
        """ __new__(cls: type, copyright: str) """
        ...


class AssemblyCultureAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyCultureAttribute(culture: str) """
    @property
    def Culture(self) -> str:
        """ Get: Culture(self: AssemblyCultureAttribute) -> str """
        ...


    def __new__(cls, culture:str) -> Self:
        """ __new__(cls: type, culture: str) """
        ...


class AssemblyDefaultAliasAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyDefaultAliasAttribute(defaultAlias: str) """
    @property
    def DefaultAlias(self) -> str:
        """ Get: DefaultAlias(self: AssemblyDefaultAliasAttribute) -> str """
        ...


    def __new__(cls, defaultAlias:str) -> Self:
        """ __new__(cls: type, defaultAlias: str) """
        ...


class AssemblyDelaySignAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyDelaySignAttribute(delaySign: bool) """
    @property
    def DelaySign(self) -> bool:
        """ Get: DelaySign(self: AssemblyDelaySignAttribute) -> bool """
        ...


    def __new__(cls, delaySign:bool) -> Self:
        """ __new__(cls: type, delaySign: bool) """
        ...


class AssemblyDescriptionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyDescriptionAttribute(description: str) """
    @property
    def Description(self) -> str:
        """ Get: Description(self: AssemblyDescriptionAttribute) -> str """
        ...


    def __new__(cls, description:str) -> Self:
        """ __new__(cls: type, description: str) """
        ...


class AssemblyFileVersionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyFileVersionAttribute(version: str) """
    @property
    def Version(self) -> str:
        """ Get: Version(self: AssemblyFileVersionAttribute) -> str """
        ...


    def __new__(cls, version:str) -> Self:
        """ __new__(cls: type, version: str) """
        ...


class AssemblyFlagsAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    AssemblyFlagsAttribute(flags: UInt32)
    AssemblyFlagsAttribute(assemblyFlags: int)
    AssemblyFlagsAttribute(assemblyFlags: AssemblyNameFlags)
    """
    @property
    def AssemblyFlags(self) -> int:
        """ Get: AssemblyFlags(self: AssemblyFlagsAttribute) -> int """
        ...

    @property
    def Flags(self) -> UInt32:
        """ Get: Flags(self: AssemblyFlagsAttribute) -> UInt32 """
        ...


    def __new__(cls, *__args:UInt32) -> Self:
        """
        __new__(cls: type, flags: UInt32)
        __new__(cls: type, assemblyFlags: int)
        __new__(cls: type, assemblyFlags: AssemblyNameFlags)
        """
        ...


class AssemblyInformationalVersionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyInformationalVersionAttribute(informationalVersion: str) """
    @property
    def InformationalVersion(self) -> str:
        """ Get: InformationalVersion(self: AssemblyInformationalVersionAttribute) -> str """
        ...


    def __new__(cls, informationalVersion:str) -> Self:
        """ __new__(cls: type, informationalVersion: str) """
        ...


class AssemblyKeyFileAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyKeyFileAttribute(keyFile: str) """
    @property
    def KeyFile(self) -> str:
        """ Get: KeyFile(self: AssemblyKeyFileAttribute) -> str """
        ...


    def __new__(cls, keyFile:str) -> Self:
        """ __new__(cls: type, keyFile: str) """
        ...


class AssemblyKeyNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyKeyNameAttribute(keyName: str) """
    @property
    def KeyName(self) -> str:
        """ Get: KeyName(self: AssemblyKeyNameAttribute) -> str """
        ...


    def __new__(cls, keyName:str) -> Self:
        """ __new__(cls: type, keyName: str) """
        ...


class AssemblyMetadataAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyMetadataAttribute(key: str, value: str) """
    @property
    def Key(self) -> str:
        """ Get: Key(self: AssemblyMetadataAttribute) -> str """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: AssemblyMetadataAttribute) -> str """
        ...


    def __new__(cls, key:str, value:str) -> Self:
        """ __new__(cls: type, key: str, value: str) """
        ...


class AssemblyName(ICloneable, IDeserializationCallback, _AssemblyName, ISerializable): # skipped bases: <type 'object'>
    """
    AssemblyName()
    AssemblyName(assemblyName: str)
    """
    @property
    def CodeBase(self) -> str:
        """
        Get: CodeBase(self: AssemblyName) -> str
        Set: CodeBase(self: AssemblyName) = value
        """
        ...

    @property
    def ContentType(self) -> AssemblyContentType:
        """
        Get: ContentType(self: AssemblyName) -> AssemblyContentType
        Set: ContentType(self: AssemblyName) = value
        """
        ...

    @property
    def CultureInfo(self) -> CultureInfo:
        """
        Get: CultureInfo(self: AssemblyName) -> CultureInfo
        Set: CultureInfo(self: AssemblyName) = value
        """
        ...

    @property
    def CultureName(self) -> str:
        """
        Get: CultureName(self: AssemblyName) -> str
        Set: CultureName(self: AssemblyName) = value
        """
        ...

    @property
    def EscapedCodeBase(self) -> str:
        """ Get: EscapedCodeBase(self: AssemblyName) -> str """
        ...

    @property
    def Flags(self) -> AssemblyNameFlags:
        """
        Get: Flags(self: AssemblyName) -> AssemblyNameFlags
        Set: Flags(self: AssemblyName) = value
        """
        ...

    @property
    def FullName(self) -> str:
        """ Get: FullName(self: AssemblyName) -> str """
        ...

    @property
    def HashAlgorithm(self) -> AssemblyHashAlgorithm:
        """
        Get: HashAlgorithm(self: AssemblyName) -> AssemblyHashAlgorithm
        Set: HashAlgorithm(self: AssemblyName) = value
        """
        ...

    @property
    def KeyPair(self) -> StrongNameKeyPair:
        """
        Get: KeyPair(self: AssemblyName) -> StrongNameKeyPair
        Set: KeyPair(self: AssemblyName) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: AssemblyName) -> str
        Set: Name(self: AssemblyName) = value
        """
        ...

    @property
    def ProcessorArchitecture(self) -> ProcessorArchitecture:
        """
        Get: ProcessorArchitecture(self: AssemblyName) -> ProcessorArchitecture
        Set: ProcessorArchitecture(self: AssemblyName) = value
        """
        ...

    @property
    def Version(self) -> Version:
        """
        Get: Version(self: AssemblyName) -> Version
        Set: Version(self: AssemblyName) = value
        """
        ...

    @property
    def VersionCompatibility(self) -> AssemblyVersionCompatibility:
        """
        Get: VersionCompatibility(self: AssemblyName) -> AssemblyVersionCompatibility
        Set: VersionCompatibility(self: AssemblyName) = value
        """
        ...


    @staticmethod
    def GetAssemblyName(assemblyFile:str) -> AssemblyName:
        """ GetAssemblyName(assemblyFile: str) -> AssemblyName """
        ...

    def GetPublicKey(self) -> Array:
        """ GetPublicKey(self: AssemblyName) -> Array[Byte] """
        ...

    def GetPublicKeyToken(self) -> Array:
        """ GetPublicKeyToken(self: AssemblyName) -> Array[Byte] """
        ...

    @staticmethod
    def ReferenceMatchesDefinition(reference:AssemblyName, definition:AssemblyName) -> bool:
        """ ReferenceMatchesDefinition(reference: AssemblyName, definition: AssemblyName) -> bool """
        ...

    def SetPublicKey(self, publicKey:Array): # -> 
        """ SetPublicKey(self: AssemblyName, publicKey: Array[Byte]) """
        ...

    def SetPublicKeyToken(self, publicKeyToken:Array): # -> 
        """ SetPublicKeyToken(self: AssemblyName, publicKeyToken: Array[Byte]) """
        ...

    def ToString(self) -> str:
        """ ToString(self: AssemblyName) -> str """
        ...


class AssemblyNameFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) AssemblyNameFlags, values: EnableJITcompileOptimizer (16384), EnableJITcompileTracking (32768), None (0), PublicKey (1), Retargetable (256) """
    EnableJITcompileOptimizer: AssemblyNameFlags = ...
    EnableJITcompileTracking: AssemblyNameFlags = ...
    PublicKey: AssemblyNameFlags = ...
    Retargetable: AssemblyNameFlags = ...
    value__ = ...


class AssemblyNameProxy(MarshalByRefObject): # skipped bases: <type 'object'>
    """ AssemblyNameProxy() """
    def GetAssemblyName(self, assemblyFile:str) -> AssemblyName:
        """ GetAssemblyName(self: AssemblyNameProxy, assemblyFile: str) -> AssemblyName """
        ...


class AssemblyProductAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyProductAttribute(product: str) """
    @property
    def Product(self) -> str:
        """ Get: Product(self: AssemblyProductAttribute) -> str """
        ...


    def __new__(cls, product:str) -> Self:
        """ __new__(cls: type, product: str) """
        ...


class AssemblySignatureKeyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblySignatureKeyAttribute(publicKey: str, countersignature: str) """
    @property
    def Countersignature(self) -> str:
        """ Get: Countersignature(self: AssemblySignatureKeyAttribute) -> str """
        ...

    @property
    def PublicKey(self) -> str:
        """ Get: PublicKey(self: AssemblySignatureKeyAttribute) -> str """
        ...


    def __new__(cls, publicKey:str, countersignature:str) -> Self:
        """ __new__(cls: type, publicKey: str, countersignature: str) """
        ...


class AssemblyTitleAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyTitleAttribute(title: str) """
    @property
    def Title(self) -> str:
        """ Get: Title(self: AssemblyTitleAttribute) -> str """
        ...


    def __new__(cls, title:str) -> Self:
        """ __new__(cls: type, title: str) """
        ...


class AssemblyTrademarkAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyTrademarkAttribute(trademark: str) """
    @property
    def Trademark(self) -> str:
        """ Get: Trademark(self: AssemblyTrademarkAttribute) -> str """
        ...


    def __new__(cls, trademark:str) -> Self:
        """ __new__(cls: type, trademark: str) """
        ...


class AssemblyVersionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyVersionAttribute(version: str) """
    @property
    def Version(self) -> str:
        """ Get: Version(self: AssemblyVersionAttribute) -> str """
        ...


    def __new__(cls, version:str) -> Self:
        """ __new__(cls: type, version: str) """
        ...


class Binder: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def BindToField(self, bindingAttr:BindingFlags, match:Array, value:object, culture:CultureInfo) -> FieldInfo:
        """ BindToField(self: Binder, bindingAttr: BindingFlags, match: Array[FieldInfo], value: object, culture: CultureInfo) -> FieldInfo """
        ...

    def BindToMethod(self, bindingAttr, match, args, modifiers, culture, names, state) -> Tuple_[MethodBase, Array, object]:
        """ BindToMethod(self: Binder, bindingAttr: BindingFlags, match: Array[MethodBase], args: Array[object], modifiers: Array[ParameterModifier], culture: CultureInfo, names: Array[str]) -> (MethodBase, Array[object], object) """
        ...

    def ChangeType(self, value:object, type:Type, culture:CultureInfo) -> object:
        """ ChangeType(self: Binder, value: object, type: Type, culture: CultureInfo) -> object """
        ...

    def ReorderArgumentArray(self, args:Array, state:object) -> Array:
        """ ReorderArgumentArray(self: Binder, args: Array[object], state: object) -> Array[object] """
        ...

    def SelectMethod(self, bindingAttr:BindingFlags, match:Array, types:Array, modifiers:Array) -> MethodBase:
        """ SelectMethod(self: Binder, bindingAttr: BindingFlags, match: Array[MethodBase], types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodBase """
        ...

    def SelectProperty(self, bindingAttr:BindingFlags, match:Array, returnType:Type, indexes:Array, modifiers:Array) -> PropertyInfo:
        """ SelectProperty(self: Binder, bindingAttr: BindingFlags, match: Array[PropertyInfo], returnType: Type, indexes: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo """
        ...


class BindingFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) BindingFlags, values: CreateInstance (512), DeclaredOnly (2), Default (0), ExactBinding (65536), FlattenHierarchy (64), GetField (1024), GetProperty (4096), IgnoreCase (1), IgnoreReturn (16777216), Instance (4), InvokeMethod (256), NonPublic (32), OptionalParamBinding (262144), Public (16), PutDispProperty (16384), PutRefDispProperty (32768), SetField (2048), SetProperty (8192), Static (8), SuppressChangeType (131072) """
    CreateInstance: BindingFlags = ...
    DeclaredOnly: BindingFlags = ...
    Default: BindingFlags = ...
    ExactBinding: BindingFlags = ...
    FlattenHierarchy: BindingFlags = ...
    GetField: BindingFlags = ...
    GetProperty: BindingFlags = ...
    IgnoreCase: BindingFlags = ...
    IgnoreReturn: BindingFlags = ...
    Instance: BindingFlags = ...
    InvokeMethod: BindingFlags = ...
    NonPublic: BindingFlags = ...
    OptionalParamBinding: BindingFlags = ...
    Public: BindingFlags = ...
    PutDispProperty: BindingFlags = ...
    PutRefDispProperty: BindingFlags = ...
    SetField: BindingFlags = ...
    SetProperty: BindingFlags = ...
    Static: BindingFlags = ...
    SuppressChangeType: BindingFlags = ...
    value__ = ...


class CallingConventions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CallingConventions, values: Any (3), ExplicitThis (64), HasThis (32), Standard (1), VarArgs (2) """
    Any: CallingConventions = ...
    ExplicitThis: CallingConventions = ...
    HasThis: CallingConventions = ...
    Standard: CallingConventions = ...
    value__ = ...
    VarArgs: CallingConventions = ...


class MemberInfo(_MemberInfo, ICustomAttributeProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CustomAttributes(self) -> IEnumerable:
        """ Get: CustomAttributes(self: MemberInfo) -> IEnumerable[CustomAttributeData] """
        ...

    @property
    def MetadataToken(self) -> int:
        """ Get: MetadataToken(self: MemberInfo) -> int """
        ...

    @property
    def Module(self) -> Module:
        """ Get: Module(self: MemberInfo) -> Module """
        ...


    def GetCustomAttributesData(self) -> IList:
        """ GetCustomAttributesData(self: MemberInfo) -> IList[CustomAttributeData] """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MethodBase(_MethodBase, MemberInfo): # skipped bases: <type '_MemberInfo'>, <type 'ICustomAttributeProvider'>, <type 'object'>
    """ no doc """
    @property
    def ContainsGenericParameters(self) -> bool:
        """ Get: ContainsGenericParameters(self: MethodBase) -> bool """
        ...

    @property
    def IsGenericMethod(self) -> bool:
        """ Get: IsGenericMethod(self: MethodBase) -> bool """
        ...

    @property
    def IsGenericMethodDefinition(self) -> bool:
        """ Get: IsGenericMethodDefinition(self: MethodBase) -> bool """
        ...

    @property
    def IsSecurityCritical(self) -> bool:
        """ Get: IsSecurityCritical(self: MethodBase) -> bool """
        ...

    @property
    def IsSecuritySafeCritical(self) -> bool:
        """ Get: IsSecuritySafeCritical(self: MethodBase) -> bool """
        ...

    @property
    def IsSecurityTransparent(self) -> bool:
        """ Get: IsSecurityTransparent(self: MethodBase) -> bool """
        ...

    @property
    def MethodImplementationFlags(self) -> MethodImplAttributes:
        """ Get: MethodImplementationFlags(self: MethodBase) -> MethodImplAttributes """
        ...


    @staticmethod
    def GetCurrentMethod() -> MethodBase:
        """ GetCurrentMethod() -> MethodBase """
        ...

    def GetGenericArguments(self) -> Array:
        """ GetGenericArguments(self: MethodBase) -> Array[Type] """
        ...

    def GetMethodBody(self) -> MethodBody:
        """ GetMethodBody(self: MethodBase) -> MethodBody """
        ...

    @staticmethod
    def GetMethodFromHandle(handle:RuntimeMethodHandle, declaringType:RuntimeTypeHandle = ...) -> MethodBase:
        """
        GetMethodFromHandle(handle: RuntimeMethodHandle) -> MethodBase
        GetMethodFromHandle(handle: RuntimeMethodHandle, declaringType: RuntimeTypeHandle) -> MethodBase
        """
        ...


class ConstructorInfo(MethodBase, _ConstructorInfo): # skipped bases: <type '_MemberInfo'>, <type '_MethodBase'>, <type 'ICustomAttributeProvider'>, <type 'object'>
    """ no doc """
    ConstructorName: str = ...
    TypeConstructorName: str = ...


class CustomAttributeData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AttributeType(self) -> Type:
        """ Get: AttributeType(self: CustomAttributeData) -> Type """
        ...

    @property
    def Constructor(self) -> ConstructorInfo:
        """ Get: Constructor(self: CustomAttributeData) -> ConstructorInfo """
        ...

    @property
    def ConstructorArguments(self) -> IList:
        """ Get: ConstructorArguments(self: CustomAttributeData) -> IList[CustomAttributeTypedArgument] """
        ...

    @property
    def NamedArguments(self) -> IList:
        """ Get: NamedArguments(self: CustomAttributeData) -> IList[CustomAttributeNamedArgument] """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: CustomAttributeData, obj: object) -> bool """
        ...

    @staticmethod
    def GetCustomAttributes(target:MemberInfo) -> IList:
        """
        GetCustomAttributes(target: MemberInfo) -> IList[CustomAttributeData]
        GetCustomAttributes(target: Module) -> IList[CustomAttributeData]
        GetCustomAttributes(target: Assembly) -> IList[CustomAttributeData]
        GetCustomAttributes(target: ParameterInfo) -> IList[CustomAttributeData]
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CustomAttributeData) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: CustomAttributeData) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CustomAttributeExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetCustomAttribute(element, *__args):
        """ no doc """
        ...

    @staticmethod
    def GetCustomAttributes(element:ParameterInfo, *__args:Type) -> IEnumerable:
        """
        GetCustomAttributes(element: Assembly) -> IEnumerable[Attribute]
        GetCustomAttributes[T](element: ParameterInfo) -> IEnumerable[T]
        GetCustomAttributes[T](element: MemberInfo) -> IEnumerable[T]
        GetCustomAttributes[T](element: Module) -> IEnumerable[T]
        GetCustomAttributes[T](element: Assembly) -> IEnumerable[T]
        GetCustomAttributes(element: ParameterInfo, attributeType: Type, inherit: bool) -> IEnumerable[Attribute]
        GetCustomAttributes(element: MemberInfo, attributeType: Type, inherit: bool) -> IEnumerable[Attribute]
        GetCustomAttributes(element: ParameterInfo, attributeType: Type) -> IEnumerable[Attribute]
        GetCustomAttributes(element: MemberInfo, attributeType: Type) -> IEnumerable[Attribute]
        GetCustomAttributes(element: Module, attributeType: Type) -> IEnumerable[Attribute]
        GetCustomAttributes(element: Assembly, attributeType: Type) -> IEnumerable[Attribute]
        GetCustomAttributes(element: ParameterInfo, inherit: bool) -> IEnumerable[Attribute]
        GetCustomAttributes(element: MemberInfo, inherit: bool) -> IEnumerable[Attribute]
        GetCustomAttributes(element: ParameterInfo) -> IEnumerable[Attribute]
        GetCustomAttributes(element: MemberInfo) -> IEnumerable[Attribute]
        GetCustomAttributes(element: Module) -> IEnumerable[Attribute]
        GetCustomAttributes[T](element: MemberInfo, inherit: bool) -> IEnumerable[T]
        GetCustomAttributes[T](element: ParameterInfo, inherit: bool) -> IEnumerable[T]
        """
        ...

    @staticmethod
    def IsDefined(element:MemberInfo, attributeType:Type, inherit:bool = ...) -> bool:
        """
        IsDefined(element: Assembly, attributeType: Type) -> bool
        IsDefined(element: Module, attributeType: Type) -> bool
        IsDefined(element: MemberInfo, attributeType: Type) -> bool
        IsDefined(element: ParameterInfo, attributeType: Type) -> bool
        IsDefined(element: MemberInfo, attributeType: Type, inherit: bool) -> bool
        IsDefined(element: ParameterInfo, attributeType: Type, inherit: bool) -> bool
        """
        ...

    __all__: list = ...


class CustomAttributeFormatException(FormatException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CustomAttributeFormatException()
    CustomAttributeFormatException(message: str)
    CustomAttributeFormatException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class CustomAttributeNamedArgument: # skipped bases: <type 'object'>, <type 'object'>
    """
    CustomAttributeNamedArgument(memberInfo: MemberInfo, value: object)
    CustomAttributeNamedArgument(memberInfo: MemberInfo, typedArgument: CustomAttributeTypedArgument)
    """
    @property
    def IsField(self) -> bool:
        """ Get: IsField(self: CustomAttributeNamedArgument) -> bool """
        ...

    @property
    def MemberInfo(self) -> MemberInfo:
        """ Get: MemberInfo(self: CustomAttributeNamedArgument) -> MemberInfo """
        ...

    @property
    def MemberName(self) -> str:
        """ Get: MemberName(self: CustomAttributeNamedArgument) -> str """
        ...

    @property
    def TypedValue(self) -> CustomAttributeTypedArgument:
        """ Get: TypedValue(self: CustomAttributeNamedArgument) -> CustomAttributeTypedArgument """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: CustomAttributeNamedArgument, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CustomAttributeNamedArgument) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: CustomAttributeNamedArgument) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CustomAttributeTypedArgument: # skipped bases: <type 'object'>, <type 'object'>
    """
    CustomAttributeTypedArgument(argumentType: Type, value: object)
    CustomAttributeTypedArgument(value: object)
    """
    @property
    def ArgumentType(self) -> Type:
        """ Get: ArgumentType(self: CustomAttributeTypedArgument) -> Type """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: CustomAttributeTypedArgument) -> object """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: CustomAttributeTypedArgument, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CustomAttributeTypedArgument) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: CustomAttributeTypedArgument) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DefaultMemberAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DefaultMemberAttribute(memberName: str) """
    @property
    def MemberName(self) -> str:
        """ Get: MemberName(self: DefaultMemberAttribute) -> str """
        ...


    def __new__(cls, memberName:str) -> Self:
        """ __new__(cls: type, memberName: str) """
        ...


class EventAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EventAttributes, values: None (0), ReservedMask (1024), RTSpecialName (1024), SpecialName (512) """
    ReservedMask: EventAttributes = ...
    RTSpecialName: EventAttributes = ...
    SpecialName: EventAttributes = ...
    value__ = ...


class EventInfo(MemberInfo, _EventInfo): # skipped bases: <type '_MemberInfo'>, <type 'ICustomAttributeProvider'>, <type 'object'>
    """ no doc """
    @property
    def AddMethod(self) -> MethodInfo:
        """ Get: AddMethod(self: EventInfo) -> MethodInfo """
        ...

    @property
    def RaiseMethod(self) -> MethodInfo:
        """ Get: RaiseMethod(self: EventInfo) -> MethodInfo """
        ...

    @property
    def RemoveMethod(self) -> MethodInfo:
        """ Get: RemoveMethod(self: EventInfo) -> MethodInfo """
        ...


    def GetOtherMethods(self, nonPublic:bool = ...) -> Array:
        """
        GetOtherMethods(self: EventInfo, nonPublic: bool) -> Array[MethodInfo]
        GetOtherMethods(self: EventInfo) -> Array[MethodInfo]
        """
        ...


class ExceptionHandlingClause: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CatchType(self) -> Type:
        """ Get: CatchType(self: ExceptionHandlingClause) -> Type """
        ...

    @property
    def FilterOffset(self) -> int:
        """ Get: FilterOffset(self: ExceptionHandlingClause) -> int """
        ...

    @property
    def Flags(self) -> ExceptionHandlingClauseOptions:
        """ Get: Flags(self: ExceptionHandlingClause) -> ExceptionHandlingClauseOptions """
        ...

    @property
    def HandlerLength(self) -> int:
        """ Get: HandlerLength(self: ExceptionHandlingClause) -> int """
        ...

    @property
    def HandlerOffset(self) -> int:
        """ Get: HandlerOffset(self: ExceptionHandlingClause) -> int """
        ...

    @property
    def TryLength(self) -> int:
        """ Get: TryLength(self: ExceptionHandlingClause) -> int """
        ...

    @property
    def TryOffset(self) -> int:
        """ Get: TryOffset(self: ExceptionHandlingClause) -> int """
        ...


    def ToString(self) -> str:
        """ ToString(self: ExceptionHandlingClause) -> str """
        ...


class ExceptionHandlingClauseOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ExceptionHandlingClauseOptions, values: Clause (0), Fault (4), Filter (1), Finally (2) """
    Clause: ExceptionHandlingClauseOptions = ...
    Fault: ExceptionHandlingClauseOptions = ...
    Filter: ExceptionHandlingClauseOptions = ...
    Finally: ExceptionHandlingClauseOptions = ...
    value__ = ...


class FieldAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) FieldAttributes, values: Assembly (3), FamANDAssem (2), Family (4), FamORAssem (5), FieldAccessMask (7), HasDefault (32768), HasFieldMarshal (4096), HasFieldRVA (256), InitOnly (32), Literal (64), NotSerialized (128), PinvokeImpl (8192), Private (1), PrivateScope (0), Public (6), ReservedMask (38144), RTSpecialName (1024), SpecialName (512), Static (16) """
    Assembly: FieldAttributes = ...
    FamANDAssem: FieldAttributes = ...
    Family: FieldAttributes = ...
    FamORAssem: FieldAttributes = ...
    FieldAccessMask: FieldAttributes = ...
    HasDefault: FieldAttributes = ...
    HasFieldMarshal: FieldAttributes = ...
    HasFieldRVA: FieldAttributes = ...
    InitOnly: FieldAttributes = ...
    Literal: FieldAttributes = ...
    NotSerialized: FieldAttributes = ...
    PinvokeImpl: FieldAttributes = ...
    Private: FieldAttributes = ...
    PrivateScope: FieldAttributes = ...
    Public: FieldAttributes = ...
    ReservedMask: FieldAttributes = ...
    RTSpecialName: FieldAttributes = ...
    SpecialName: FieldAttributes = ...
    Static: FieldAttributes = ...
    value__ = ...


class FieldInfo(MemberInfo, _FieldInfo): # skipped bases: <type '_MemberInfo'>, <type 'ICustomAttributeProvider'>, <type 'object'>
    """ no doc """
    @property
    def IsSecurityCritical(self) -> bool:
        """ Get: IsSecurityCritical(self: FieldInfo) -> bool """
        ...

    @property
    def IsSecuritySafeCritical(self) -> bool:
        """ Get: IsSecuritySafeCritical(self: FieldInfo) -> bool """
        ...

    @property
    def IsSecurityTransparent(self) -> bool:
        """ Get: IsSecurityTransparent(self: FieldInfo) -> bool """
        ...


    @staticmethod
    def GetFieldFromHandle(handle:RuntimeFieldHandle, declaringType:RuntimeTypeHandle = ...) -> FieldInfo:
        """
        GetFieldFromHandle(handle: RuntimeFieldHandle) -> FieldInfo
        GetFieldFromHandle(handle: RuntimeFieldHandle, declaringType: RuntimeTypeHandle) -> FieldInfo
        """
        ...

    def GetOptionalCustomModifiers(self) -> Array:
        """ GetOptionalCustomModifiers(self: FieldInfo) -> Array[Type] """
        ...

    def GetRawConstantValue(self) -> object:
        """ GetRawConstantValue(self: FieldInfo) -> object """
        ...

    def GetRequiredCustomModifiers(self) -> Array:
        """ GetRequiredCustomModifiers(self: FieldInfo) -> Array[Type] """
        ...


class GenericParameterAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) GenericParameterAttributes, values: Contravariant (2), Covariant (1), DefaultConstructorConstraint (16), None (0), NotNullableValueTypeConstraint (8), ReferenceTypeConstraint (4), SpecialConstraintMask (28), VarianceMask (3) """
    Contravariant: GenericParameterAttributes = ...
    Covariant: GenericParameterAttributes = ...
    DefaultConstructorConstraint: GenericParameterAttributes = ...
    NotNullableValueTypeConstraint: GenericParameterAttributes = ...
    ReferenceTypeConstraint: GenericParameterAttributes = ...
    SpecialConstraintMask: GenericParameterAttributes = ...
    value__ = ...
    VarianceMask: GenericParameterAttributes = ...


class ICustomTypeProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetCustomType(self) -> Type:
        """ GetCustomType(self: ICustomTypeProvider) -> Type """
        ...


class ImageFileMachine(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ImageFileMachine, values: AMD64 (34404), ARM (452), I386 (332), IA64 (512) """
    AMD64: ImageFileMachine = ...
    ARM: ImageFileMachine = ...
    I386: ImageFileMachine = ...
    IA64: ImageFileMachine = ...
    value__ = ...


class InterfaceMapping: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    InterfaceMethods = ...
    InterfaceType = ...
    TargetMethods = ...
    TargetType = ...


class IntrospectionExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetTypeInfo(type:Type) -> TypeInfo:
        """ GetTypeInfo(type: Type) -> TypeInfo """
        ...

    __all__: list = ...


class InvalidFilterCriteriaException(ApplicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidFilterCriteriaException()
    InvalidFilterCriteriaException(message: str)
    InvalidFilterCriteriaException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class IReflect: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def UnderlyingSystemType(self) -> Type:
        """ Get: UnderlyingSystemType(self: IReflect) -> Type """
        ...


    def GetField(self, name:str, bindingAttr:BindingFlags) -> FieldInfo:
        """ GetField(self: IReflect, name: str, bindingAttr: BindingFlags) -> FieldInfo """
        ...

    def GetFields(self, bindingAttr:BindingFlags) -> Array:
        """ GetFields(self: IReflect, bindingAttr: BindingFlags) -> Array[FieldInfo] """
        ...

    def GetMember(self, name:str, bindingAttr:BindingFlags) -> Array:
        """ GetMember(self: IReflect, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo] """
        ...

    def GetMembers(self, bindingAttr:BindingFlags) -> Array:
        """ GetMembers(self: IReflect, bindingAttr: BindingFlags) -> Array[MemberInfo] """
        ...

    def GetMethod(self, name:str, bindingAttr:BindingFlags, binder:Binder = ..., types:Array = ..., modifiers:Array = ...) -> MethodInfo:
        """
        GetMethod(self: IReflect, name: str, bindingAttr: BindingFlags, binder: Binder, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo
        GetMethod(self: IReflect, name: str, bindingAttr: BindingFlags) -> MethodInfo
        """
        ...

    def GetMethods(self, bindingAttr:BindingFlags) -> Array:
        """ GetMethods(self: IReflect, bindingAttr: BindingFlags) -> Array[MethodInfo] """
        ...

    def GetProperties(self, bindingAttr:BindingFlags) -> Array:
        """ GetProperties(self: IReflect, bindingAttr: BindingFlags) -> Array[PropertyInfo] """
        ...

    def GetProperty(self, name:str, bindingAttr:BindingFlags, binder:Binder = ..., returnType:Type = ..., types:Array = ..., modifiers:Array = ...) -> PropertyInfo:
        """
        GetProperty(self: IReflect, name: str, bindingAttr: BindingFlags) -> PropertyInfo
        GetProperty(self: IReflect, name: str, bindingAttr: BindingFlags, binder: Binder, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo
        """
        ...

    def InvokeMember(self, name:str, invokeAttr:BindingFlags, binder:Binder, target:object, args:Array, modifiers:Array, culture:CultureInfo, namedParameters:Array) -> object:
        """ InvokeMember(self: IReflect, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: Array[object], modifiers: Array[ParameterModifier], culture: CultureInfo, namedParameters: Array[str]) -> object """
        ...


class IReflectableType: # skipped bases: <type 'object'>
    """ no doc """
    def GetTypeInfo(self) -> TypeInfo:
        """ GetTypeInfo(self: IReflectableType) -> TypeInfo """
        ...


class LocalVariableInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsPinned(self) -> bool:
        """ Get: IsPinned(self: LocalVariableInfo) -> bool """
        ...

    @property
    def LocalIndex(self) -> int:
        """ Get: LocalIndex(self: LocalVariableInfo) -> int """
        ...

    @property
    def LocalType(self) -> Type:
        """ Get: LocalType(self: LocalVariableInfo) -> Type """
        ...


    def ToString(self) -> str:
        """ ToString(self: LocalVariableInfo) -> str """
        ...


class ManifestResourceInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ ManifestResourceInfo(containingAssembly: Assembly, containingFileName: str, resourceLocation: ResourceLocation) """
    @property
    def FileName(self) -> str:
        """ Get: FileName(self: ManifestResourceInfo) -> str """
        ...

    @property
    def ReferencedAssembly(self) -> Assembly:
        """ Get: ReferencedAssembly(self: ManifestResourceInfo) -> Assembly """
        ...

    @property
    def ResourceLocation(self) -> ResourceLocation:
        """ Get: ResourceLocation(self: ManifestResourceInfo) -> ResourceLocation """
        ...



class MemberFilter(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ MemberFilter(object: object, method: IntPtr) """
    def BeginInvoke(self, m:MemberInfo, filterCriteria:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: MemberFilter, m: MemberInfo, filterCriteria: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: MemberFilter, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, m:MemberInfo, filterCriteria:object) -> bool:
        """ Invoke(self: MemberFilter, m: MemberInfo, filterCriteria: object) -> bool """
        ...


class MemberTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) MemberTypes, values: All (191), Constructor (1), Custom (64), Event (2), Field (4), Method (8), NestedType (128), Property (16), TypeInfo (32) """
    All: MemberTypes = ...
    Constructor: MemberTypes = ...
    Custom: MemberTypes = ...
    Event: MemberTypes = ...
    Field: MemberTypes = ...
    Method: MemberTypes = ...
    NestedType: MemberTypes = ...
    Property: MemberTypes = ...
    TypeInfo: MemberTypes = ...
    value__ = ...


class MethodAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) MethodAttributes, values: Abstract (1024), Assembly (3), CheckAccessOnOverride (512), FamANDAssem (2), Family (4), FamORAssem (5), Final (32), HasSecurity (16384), HideBySig (128), MemberAccessMask (7), NewSlot (256), PinvokeImpl (8192), Private (1), PrivateScope (0), Public (6), RequireSecObject (32768), ReservedMask (53248), ReuseSlot (0), RTSpecialName (4096), SpecialName (2048), Static (16), UnmanagedExport (8), Virtual (64), VtableLayoutMask (256) """
    Abstract: MethodAttributes = ...
    Assembly: MethodAttributes = ...
    CheckAccessOnOverride: MethodAttributes = ...
    FamANDAssem: MethodAttributes = ...
    Family: MethodAttributes = ...
    FamORAssem: MethodAttributes = ...
    Final: MethodAttributes = ...
    HasSecurity: MethodAttributes = ...
    HideBySig: MethodAttributes = ...
    MemberAccessMask: MethodAttributes = ...
    NewSlot: MethodAttributes = ...
    PinvokeImpl: MethodAttributes = ...
    Private: MethodAttributes = ...
    PrivateScope: MethodAttributes = ...
    Public: MethodAttributes = ...
    RequireSecObject: MethodAttributes = ...
    ReservedMask: MethodAttributes = ...
    ReuseSlot: MethodAttributes = ...
    RTSpecialName: MethodAttributes = ...
    SpecialName: MethodAttributes = ...
    Static: MethodAttributes = ...
    UnmanagedExport: MethodAttributes = ...
    value__ = ...
    Virtual: MethodAttributes = ...
    VtableLayoutMask: MethodAttributes = ...


class MethodBody: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ExceptionHandlingClauses(self) -> IList:
        """ Get: ExceptionHandlingClauses(self: MethodBody) -> IList[ExceptionHandlingClause] """
        ...

    @property
    def InitLocals(self) -> bool:
        """ Get: InitLocals(self: MethodBody) -> bool """
        ...

    @property
    def LocalSignatureMetadataToken(self) -> int:
        """ Get: LocalSignatureMetadataToken(self: MethodBody) -> int """
        ...

    @property
    def LocalVariables(self) -> IList:
        """ Get: LocalVariables(self: MethodBody) -> IList[LocalVariableInfo] """
        ...

    @property
    def MaxStackSize(self) -> int:
        """ Get: MaxStackSize(self: MethodBody) -> int """
        ...


    def GetILAsByteArray(self) -> Array:
        """ GetILAsByteArray(self: MethodBody) -> Array[Byte] """
        ...


class MethodImplAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MethodImplAttributes, values: AggressiveInlining (256), CodeTypeMask (3), ForwardRef (16), IL (0), InternalCall (4096), Managed (0), ManagedMask (4), MaxMethodImplVal (65535), Native (1), NoInlining (8), NoOptimization (64), OPTIL (2), PreserveSig (128), Runtime (3), SecurityMitigations (1024), Synchronized (32), Unmanaged (4) """
    AggressiveInlining: MethodImplAttributes = ...
    CodeTypeMask: MethodImplAttributes = ...
    ForwardRef: MethodImplAttributes = ...
    IL: MethodImplAttributes = ...
    InternalCall: MethodImplAttributes = ...
    Managed: MethodImplAttributes = ...
    ManagedMask: MethodImplAttributes = ...
    MaxMethodImplVal: MethodImplAttributes = ...
    Native: MethodImplAttributes = ...
    NoInlining: MethodImplAttributes = ...
    NoOptimization: MethodImplAttributes = ...
    OPTIL: MethodImplAttributes = ...
    PreserveSig: MethodImplAttributes = ...
    Runtime: MethodImplAttributes = ...
    SecurityMitigations: MethodImplAttributes = ...
    Synchronized: MethodImplAttributes = ...
    Unmanaged: MethodImplAttributes = ...
    value__ = ...


class MethodInfo(MethodBase, _MethodInfo): # skipped bases: <type '_MemberInfo'>, <type '_MethodBase'>, <type 'ICustomAttributeProvider'>, <type 'object'>
    """ no doc """
    @property
    def ReturnParameter(self) -> ParameterInfo:
        """ Get: ReturnParameter(self: MethodInfo) -> ParameterInfo """
        ...


    def CreateDelegate(self, delegateType:Type, target:object = ...) -> Delegate:
        """
        CreateDelegate(self: MethodInfo, delegateType: Type) -> Delegate
        CreateDelegate(self: MethodInfo, delegateType: Type, target: object) -> Delegate
        """
        ...

    def GetGenericMethodDefinition(self) -> MethodInfo:
        """ GetGenericMethodDefinition(self: MethodInfo) -> MethodInfo """
        ...

    def MakeGenericMethod(self, typeArguments:Array) -> MethodInfo:
        """ MakeGenericMethod(self: MethodInfo, *typeArguments: Array[Type]) -> MethodInfo """
        ...


class Missing(ISerializable): # skipped bases: <type 'object'>
    """ no doc """
    Value: Missing = ...


class Module(_Module, ISerializable, ICustomAttributeProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Assembly(self) -> Assembly:
        """ Get: Assembly(self: Module) -> Assembly """
        ...

    @property
    def CustomAttributes(self) -> IEnumerable:
        """ Get: CustomAttributes(self: Module) -> IEnumerable[CustomAttributeData] """
        ...

    @property
    def FullyQualifiedName(self) -> str:
        """ Get: FullyQualifiedName(self: Module) -> str """
        ...

    @property
    def MDStreamVersion(self) -> int:
        """ Get: MDStreamVersion(self: Module) -> int """
        ...

    @property
    def MetadataToken(self) -> int:
        """ Get: MetadataToken(self: Module) -> int """
        ...

    @property
    def ModuleHandle(self) -> ModuleHandle:
        """ Get: ModuleHandle(self: Module) -> ModuleHandle """
        ...

    @property
    def ModuleVersionId(self) -> Guid:
        """ Get: ModuleVersionId(self: Module) -> Guid """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Module) -> str """
        ...

    @property
    def ScopeName(self) -> str:
        """ Get: ScopeName(self: Module) -> str """
        ...


    def Equals(self, o:object) -> bool:
        """ Equals(self: Module, o: object) -> bool """
        ...

    def FindTypes(self, filter:TypeFilter, filterCriteria:object) -> Array:
        """ FindTypes(self: Module, filter: TypeFilter, filterCriteria: object) -> Array[Type] """
        ...

    def GetCustomAttributesData(self) -> IList:
        """ GetCustomAttributesData(self: Module) -> IList[CustomAttributeData] """
        ...

    def GetField(self, name:str, bindingAttr:BindingFlags = ...) -> FieldInfo:
        """
        GetField(self: Module, name: str) -> FieldInfo
        GetField(self: Module, name: str, bindingAttr: BindingFlags) -> FieldInfo
        """
        ...

    def GetFields(self, bindingFlags:BindingFlags = ...) -> Array:
        """
        GetFields(self: Module) -> Array[FieldInfo]
        GetFields(self: Module, bindingFlags: BindingFlags) -> Array[FieldInfo]
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Module) -> int """
        ...

    def GetMethod(self, name:str, *__args:Array) -> MethodInfo:
        """
        GetMethod(self: Module, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo
        GetMethod(self: Module, name: str, types: Array[Type]) -> MethodInfo
        GetMethod(self: Module, name: str) -> MethodInfo
        """
        ...

    def GetMethodImpl(self, *args): #cannot find CLR method
        """ GetMethodImpl(self: Module, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo """
        ...

    def GetMethods(self, bindingFlags:BindingFlags = ...) -> Array:
        """
        GetMethods(self: Module) -> Array[MethodInfo]
        GetMethods(self: Module, bindingFlags: BindingFlags) -> Array[MethodInfo]
        """
        ...

    def GetPEKind(self, peKind, machine) -> Tuple_[PortableExecutableKinds, ImageFileMachine]:
        """ GetPEKind(self: Module) -> (PortableExecutableKinds, ImageFileMachine) """
        ...

    def GetSignerCertificate(self) -> X509Certificate:
        """ GetSignerCertificate(self: Module) -> X509Certificate """
        ...

    def GetType(self, className:str = ..., *__args:bool) -> Type:
        """
        GetType(self: Module, className: str, ignoreCase: bool) -> Type
        GetType(self: Module, className: str) -> Type
        GetType(self: Module, className: str, throwOnError: bool, ignoreCase: bool) -> Type
        """
        ...

    def GetTypes(self) -> Array:
        """ GetTypes(self: Module) -> Array[Type] """
        ...

    def IsResource(self) -> bool:
        """ IsResource(self: Module) -> bool """
        ...

    def ResolveField(self, metadataToken:int, genericTypeArguments:Array = ..., genericMethodArguments:Array = ...) -> FieldInfo:
        """
        ResolveField(self: Module, metadataToken: int) -> FieldInfo
        ResolveField(self: Module, metadataToken: int, genericTypeArguments: Array[Type], genericMethodArguments: Array[Type]) -> FieldInfo
        """
        ...

    def ResolveMember(self, metadataToken:int, genericTypeArguments:Array = ..., genericMethodArguments:Array = ...) -> MemberInfo:
        """
        ResolveMember(self: Module, metadataToken: int) -> MemberInfo
        ResolveMember(self: Module, metadataToken: int, genericTypeArguments: Array[Type], genericMethodArguments: Array[Type]) -> MemberInfo
        """
        ...

    def ResolveMethod(self, metadataToken:int, genericTypeArguments:Array = ..., genericMethodArguments:Array = ...) -> MethodBase:
        """
        ResolveMethod(self: Module, metadataToken: int) -> MethodBase
        ResolveMethod(self: Module, metadataToken: int, genericTypeArguments: Array[Type], genericMethodArguments: Array[Type]) -> MethodBase
        """
        ...

    def ResolveSignature(self, metadataToken:int) -> Array:
        """ ResolveSignature(self: Module, metadataToken: int) -> Array[Byte] """
        ...

    def ResolveString(self, metadataToken:int) -> str:
        """ ResolveString(self: Module, metadataToken: int) -> str """
        ...

    def ResolveType(self, metadataToken:int, genericTypeArguments:Array = ..., genericMethodArguments:Array = ...) -> Type:
        """
        ResolveType(self: Module, metadataToken: int) -> Type
        ResolveType(self: Module, metadataToken: int, genericTypeArguments: Array[Type], genericMethodArguments: Array[Type]) -> Type
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: Module) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ModuleResolveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ModuleResolveEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ResolveEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ModuleResolveEventHandler, sender: object, e: ResolveEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> Module:
        """ EndInvoke(self: ModuleResolveEventHandler, result: IAsyncResult) -> Module """
        ...

    def Invoke(self, sender:object, e:ResolveEventArgs) -> Module:
        """ Invoke(self: ModuleResolveEventHandler, sender: object, e: ResolveEventArgs) -> Module """
        ...


class ObfuscateAssemblyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ObfuscateAssemblyAttribute(assemblyIsPrivate: bool) """
    @property
    def AssemblyIsPrivate(self) -> bool:
        """ Get: AssemblyIsPrivate(self: ObfuscateAssemblyAttribute) -> bool """
        ...

    @property
    def StripAfterObfuscation(self) -> bool:
        """
        Get: StripAfterObfuscation(self: ObfuscateAssemblyAttribute) -> bool
        Set: StripAfterObfuscation(self: ObfuscateAssemblyAttribute) = value
        """
        ...


    def __new__(cls, assemblyIsPrivate:bool) -> Self:
        """ __new__(cls: type, assemblyIsPrivate: bool) """
        ...


class ObfuscationAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ObfuscationAttribute() """
    @property
    def ApplyToMembers(self) -> bool:
        """
        Get: ApplyToMembers(self: ObfuscationAttribute) -> bool
        Set: ApplyToMembers(self: ObfuscationAttribute) = value
        """
        ...

    @property
    def Exclude(self) -> bool:
        """
        Get: Exclude(self: ObfuscationAttribute) -> bool
        Set: Exclude(self: ObfuscationAttribute) = value
        """
        ...

    @property
    def Feature(self) -> str:
        """
        Get: Feature(self: ObfuscationAttribute) -> str
        Set: Feature(self: ObfuscationAttribute) = value
        """
        ...

    @property
    def StripAfterObfuscation(self) -> bool:
        """
        Get: StripAfterObfuscation(self: ObfuscationAttribute) -> bool
        Set: StripAfterObfuscation(self: ObfuscationAttribute) = value
        """
        ...



class ParameterAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ParameterAttributes, values: HasDefault (4096), HasFieldMarshal (8192), In (1), Lcid (4), None (0), Optional (16), Out (2), Reserved3 (16384), Reserved4 (32768), ReservedMask (61440), Retval (8) """
    HasDefault: ParameterAttributes = ...
    HasFieldMarshal: ParameterAttributes = ...
    In: ParameterAttributes = ...
    Lcid: ParameterAttributes = ...
    Optional: ParameterAttributes = ...
    Out: ParameterAttributes = ...
    Reserved3: ParameterAttributes = ...
    Reserved4: ParameterAttributes = ...
    ReservedMask: ParameterAttributes = ...
    Retval: ParameterAttributes = ...
    value__ = ...


class ParameterInfo(IObjectReference, _ParameterInfo, ICustomAttributeProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> ParameterAttributes:
        """ Get: Attributes(self: ParameterInfo) -> ParameterAttributes """
        ...

    @property
    def CustomAttributes(self) -> IEnumerable:
        """ Get: CustomAttributes(self: ParameterInfo) -> IEnumerable[CustomAttributeData] """
        ...

    @property
    def DefaultValue(self) -> object:
        """ Get: DefaultValue(self: ParameterInfo) -> object """
        ...

    @property
    def HasDefaultValue(self) -> bool:
        """ Get: HasDefaultValue(self: ParameterInfo) -> bool """
        ...

    @property
    def IsIn(self) -> bool:
        """ Get: IsIn(self: ParameterInfo) -> bool """
        ...

    @property
    def IsLcid(self) -> bool:
        """ Get: IsLcid(self: ParameterInfo) -> bool """
        ...

    @property
    def IsOptional(self) -> bool:
        """ Get: IsOptional(self: ParameterInfo) -> bool """
        ...

    @property
    def IsOut(self) -> bool:
        """ Get: IsOut(self: ParameterInfo) -> bool """
        ...

    @property
    def IsRetval(self) -> bool:
        """ Get: IsRetval(self: ParameterInfo) -> bool """
        ...

    @property
    def Member(self) -> MemberInfo:
        """ Get: Member(self: ParameterInfo) -> MemberInfo """
        ...

    @property
    def MetadataToken(self) -> int:
        """ Get: MetadataToken(self: ParameterInfo) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ParameterInfo) -> str """
        ...

    @property
    def ParameterType(self) -> Type:
        """ Get: ParameterType(self: ParameterInfo) -> Type """
        ...

    @property
    def Position(self) -> int:
        """ Get: Position(self: ParameterInfo) -> int """
        ...

    @property
    def RawDefaultValue(self) -> object:
        """ Get: RawDefaultValue(self: ParameterInfo) -> object """
        ...


    def GetCustomAttributesData(self) -> IList:
        """ GetCustomAttributesData(self: ParameterInfo) -> IList[CustomAttributeData] """
        ...

    def GetOptionalCustomModifiers(self) -> Array:
        """ GetOptionalCustomModifiers(self: ParameterInfo) -> Array[Type] """
        ...

    def GetRequiredCustomModifiers(self) -> Array:
        """ GetRequiredCustomModifiers(self: ParameterInfo) -> Array[Type] """
        ...

    def ToString(self) -> str:
        """ ToString(self: ParameterInfo) -> str """
        ...

    AttrsImpl = ...
    ClassImpl = ...
    DefaultValueImpl = ...
    MemberImpl = ...
    NameImpl = ...
    PositionImpl = ...


class ParameterModifier: # skipped bases: <type 'object'>, <type 'object'>
    """ ParameterModifier(parameterCount: int) """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class Pointer(ISerializable): # skipped bases: <type 'object'>
    """ no doc """
    @staticmethod
    def Box(ptr:Void, type:Type) -> object:
        """ Box(ptr: Void*, type: Type) -> object """
        ...

    @staticmethod
    def Unbox(ptr:object) -> Void:
        """ Unbox(ptr: object) -> Void* """
        ...


class PortableExecutableKinds(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PortableExecutableKinds, values: ILOnly (1), NotAPortableExecutableImage (0), PE32Plus (4), Preferred32Bit (16), Required32Bit (2), Unmanaged32Bit (8) """
    ILOnly: PortableExecutableKinds = ...
    NotAPortableExecutableImage: PortableExecutableKinds = ...
    PE32Plus: PortableExecutableKinds = ...
    Preferred32Bit: PortableExecutableKinds = ...
    Required32Bit: PortableExecutableKinds = ...
    Unmanaged32Bit: PortableExecutableKinds = ...
    value__ = ...


class ProcessorArchitecture(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProcessorArchitecture, values: Amd64 (4), Arm (5), IA64 (3), MSIL (1), None (0), X86 (2) """
    Amd64: ProcessorArchitecture = ...
    Arm: ProcessorArchitecture = ...
    IA64: ProcessorArchitecture = ...
    MSIL: ProcessorArchitecture = ...
    value__ = ...
    X86: ProcessorArchitecture = ...


class PropertyAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PropertyAttributes, values: HasDefault (4096), None (0), Reserved2 (8192), Reserved3 (16384), Reserved4 (32768), ReservedMask (62464), RTSpecialName (1024), SpecialName (512) """
    HasDefault: PropertyAttributes = ...
    Reserved2: PropertyAttributes = ...
    Reserved3: PropertyAttributes = ...
    Reserved4: PropertyAttributes = ...
    ReservedMask: PropertyAttributes = ...
    RTSpecialName: PropertyAttributes = ...
    SpecialName: PropertyAttributes = ...
    value__ = ...


class PropertyInfo(MemberInfo, _PropertyInfo): # skipped bases: <type '_MemberInfo'>, <type 'ICustomAttributeProvider'>, <type 'object'>
    """ no doc """
    @property
    def GetMethod(self) -> MethodInfo:
        """ Get: GetMethod(self: PropertyInfo) -> MethodInfo """
        ...

    @property
    def SetMethod(self) -> MethodInfo:
        """ Get: SetMethod(self: PropertyInfo) -> MethodInfo """
        ...


    def GetConstantValue(self) -> object:
        """ GetConstantValue(self: PropertyInfo) -> object """
        ...

    def GetOptionalCustomModifiers(self) -> Array:
        """ GetOptionalCustomModifiers(self: PropertyInfo) -> Array[Type] """
        ...

    def GetRawConstantValue(self) -> object:
        """ GetRawConstantValue(self: PropertyInfo) -> object """
        ...

    def GetRequiredCustomModifiers(self) -> Array:
        """ GetRequiredCustomModifiers(self: PropertyInfo) -> Array[Type] """
        ...


class ReflectionContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetTypeForObject(self, value:object) -> TypeInfo:
        """ GetTypeForObject(self: ReflectionContext, value: object) -> TypeInfo """
        ...

    def MapAssembly(self, assembly:Assembly) -> Assembly:
        """ MapAssembly(self: ReflectionContext, assembly: Assembly) -> Assembly """
        ...

    def MapType(self, type:TypeInfo) -> TypeInfo:
        """ MapType(self: ReflectionContext, type: TypeInfo) -> TypeInfo """
        ...


class ReflectionTypeLoadException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ReflectionTypeLoadException(classes: Array[Type], exceptions: Array[Exception])
    ReflectionTypeLoadException(classes: Array[Type], exceptions: Array[Exception], message: str)
    """
    @property
    def LoaderExceptions(self) -> Array:
        """ Get: LoaderExceptions(self: ReflectionTypeLoadException) -> Array[Exception] """
        ...

    @property
    def Types(self) -> Array:
        """ Get: Types(self: ReflectionTypeLoadException) -> Array[Type] """
        ...


    SerializeObjectState = ...


class ResourceAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ResourceAttributes, values: Private (2), Public (1) """
    Private: ResourceAttributes = ...
    Public: ResourceAttributes = ...
    value__ = ...


class ResourceLocation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ResourceLocation, values: ContainedInAnotherAssembly (2), ContainedInManifestFile (4), Embedded (1) """
    ContainedInAnotherAssembly: ResourceLocation = ...
    ContainedInManifestFile: ResourceLocation = ...
    Embedded: ResourceLocation = ...
    value__ = ...


class RuntimeReflectionExtensions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetMethodInfo(del_:Delegate) -> MethodInfo:
        """ GetMethodInfo(del: Delegate) -> MethodInfo """
        ...

    @staticmethod
    def GetRuntimeBaseDefinition(method:MethodInfo) -> MethodInfo:
        """ GetRuntimeBaseDefinition(method: MethodInfo) -> MethodInfo """
        ...

    @staticmethod
    def GetRuntimeEvent(type:Type, name:str) -> EventInfo:
        """ GetRuntimeEvent(type: Type, name: str) -> EventInfo """
        ...

    @staticmethod
    def GetRuntimeEvents(type:Type) -> IEnumerable:
        """ GetRuntimeEvents(type: Type) -> IEnumerable[EventInfo] """
        ...

    @staticmethod
    def GetRuntimeField(type:Type, name:str) -> FieldInfo:
        """ GetRuntimeField(type: Type, name: str) -> FieldInfo """
        ...

    @staticmethod
    def GetRuntimeFields(type:Type) -> IEnumerable:
        """ GetRuntimeFields(type: Type) -> IEnumerable[FieldInfo] """
        ...

    @staticmethod
    def GetRuntimeInterfaceMap(typeInfo:TypeInfo, interfaceType:Type) -> InterfaceMapping:
        """ GetRuntimeInterfaceMap(typeInfo: TypeInfo, interfaceType: Type) -> InterfaceMapping """
        ...

    @staticmethod
    def GetRuntimeMethod(type:Type, name:str, parameters:Array) -> MethodInfo:
        """ GetRuntimeMethod(type: Type, name: str, parameters: Array[Type]) -> MethodInfo """
        ...

    @staticmethod
    def GetRuntimeMethods(type:Type) -> IEnumerable:
        """ GetRuntimeMethods(type: Type) -> IEnumerable[MethodInfo] """
        ...

    @staticmethod
    def GetRuntimeProperties(type:Type) -> IEnumerable:
        """ GetRuntimeProperties(type: Type) -> IEnumerable[PropertyInfo] """
        ...

    @staticmethod
    def GetRuntimeProperty(type:Type, name:str) -> PropertyInfo:
        """ GetRuntimeProperty(type: Type, name: str) -> PropertyInfo """
        ...

    __all__: list = ...


class StrongNameKeyPair(IDeserializationCallback, ISerializable): # skipped bases: <type 'object'>
    """
    StrongNameKeyPair(keyPairFile: FileStream)
    StrongNameKeyPair(keyPairArray: Array[Byte])
    StrongNameKeyPair(keyPairContainer: str)
    """
    @property
    def PublicKey(self) -> Array:
        """ Get: PublicKey(self: StrongNameKeyPair) -> Array[Byte] """
        ...



class TargetException(ApplicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TargetException()
    TargetException(message: str)
    TargetException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class TargetInvocationException(ApplicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TargetInvocationException(inner: Exception)
    TargetInvocationException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class TargetParameterCountException(ApplicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TargetParameterCountException()
    TargetParameterCountException(message: str)
    TargetParameterCountException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class TypeAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TypeAttributes, values: Abstract (128), AnsiClass (0), AutoClass (131072), AutoLayout (0), BeforeFieldInit (1048576), Class (0), ClassSemanticsMask (32), CustomFormatClass (196608), CustomFormatMask (12582912), ExplicitLayout (16), HasSecurity (262144), Import (4096), Interface (32), LayoutMask (24), NestedAssembly (5), NestedFamANDAssem (6), NestedFamily (4), NestedFamORAssem (7), NestedPrivate (3), NestedPublic (2), NotPublic (0), Public (1), ReservedMask (264192), RTSpecialName (2048), Sealed (256), SequentialLayout (8), Serializable (8192), SpecialName (1024), StringFormatMask (196608), UnicodeClass (65536), VisibilityMask (7), WindowsRuntime (16384) """
    Abstract: TypeAttributes = ...
    AnsiClass: TypeAttributes = ...
    AutoClass: TypeAttributes = ...
    AutoLayout: TypeAttributes = ...
    BeforeFieldInit: TypeAttributes = ...
    Class: TypeAttributes = ...
    ClassSemanticsMask: TypeAttributes = ...
    CustomFormatClass: TypeAttributes = ...
    CustomFormatMask: TypeAttributes = ...
    ExplicitLayout: TypeAttributes = ...
    HasSecurity: TypeAttributes = ...
    Import: TypeAttributes = ...
    Interface: TypeAttributes = ...
    LayoutMask: TypeAttributes = ...
    NestedAssembly: TypeAttributes = ...
    NestedFamANDAssem: TypeAttributes = ...
    NestedFamily: TypeAttributes = ...
    NestedFamORAssem: TypeAttributes = ...
    NestedPrivate: TypeAttributes = ...
    NestedPublic: TypeAttributes = ...
    NotPublic: TypeAttributes = ...
    Public: TypeAttributes = ...
    ReservedMask: TypeAttributes = ...
    RTSpecialName: TypeAttributes = ...
    Sealed: TypeAttributes = ...
    SequentialLayout: TypeAttributes = ...
    Serializable: TypeAttributes = ...
    SpecialName: TypeAttributes = ...
    StringFormatMask: TypeAttributes = ...
    UnicodeClass: TypeAttributes = ...
    value__ = ...
    VisibilityMask: TypeAttributes = ...
    WindowsRuntime: TypeAttributes = ...


class TypeInfo(Type, IReflectableType): # skipped bases: <type '_MemberInfo'>, <type 'ICustomAttributeProvider'>, <type 'IReflect'>, <type '_Type'>, <type 'object'>
    """ no doc """
    @property
    def DeclaredConstructors(self) -> IEnumerable:
        """ Get: DeclaredConstructors(self: TypeInfo) -> IEnumerable[ConstructorInfo] """
        ...

    @property
    def DeclaredEvents(self) -> IEnumerable:
        """ Get: DeclaredEvents(self: TypeInfo) -> IEnumerable[EventInfo] """
        ...

    @property
    def DeclaredFields(self) -> IEnumerable:
        """ Get: DeclaredFields(self: TypeInfo) -> IEnumerable[FieldInfo] """
        ...

    @property
    def DeclaredMembers(self) -> IEnumerable:
        """ Get: DeclaredMembers(self: TypeInfo) -> IEnumerable[MemberInfo] """
        ...

    @property
    def DeclaredMethods(self) -> IEnumerable:
        """ Get: DeclaredMethods(self: TypeInfo) -> IEnumerable[MethodInfo] """
        ...

    @property
    def DeclaredNestedTypes(self) -> IEnumerable:
        """ Get: DeclaredNestedTypes(self: TypeInfo) -> IEnumerable[TypeInfo] """
        ...

    @property
    def DeclaredProperties(self) -> IEnumerable:
        """ Get: DeclaredProperties(self: TypeInfo) -> IEnumerable[PropertyInfo] """
        ...

    @property
    def GenericTypeParameters(self) -> Array:
        """ Get: GenericTypeParameters(self: TypeInfo) -> Array[Type] """
        ...

    @property
    def ImplementedInterfaces(self) -> IEnumerable:
        """ Get: ImplementedInterfaces(self: TypeInfo) -> IEnumerable[Type] """
        ...


    def AsType(self) -> Type:
        """ AsType(self: TypeInfo) -> Type """
        ...

    def GetDeclaredEvent(self, name:str) -> EventInfo:
        """ GetDeclaredEvent(self: TypeInfo, name: str) -> EventInfo """
        ...

    def GetDeclaredField(self, name:str) -> FieldInfo:
        """ GetDeclaredField(self: TypeInfo, name: str) -> FieldInfo """
        ...

    def GetDeclaredMethod(self, name:str) -> MethodInfo:
        """ GetDeclaredMethod(self: TypeInfo, name: str) -> MethodInfo """
        ...

    def GetDeclaredMethods(self, name:str) -> IEnumerable:
        """ GetDeclaredMethods(self: TypeInfo, name: str) -> IEnumerable[MethodInfo] """
        ...

    def GetDeclaredNestedType(self, name:str) -> TypeInfo:
        """ GetDeclaredNestedType(self: TypeInfo, name: str) -> TypeInfo """
        ...

    def GetDeclaredProperty(self, name:str) -> PropertyInfo:
        """ GetDeclaredProperty(self: TypeInfo, name: str) -> PropertyInfo """
        ...


class TypeDelegator(TypeInfo): # skipped bases: <type '_MemberInfo'>, <type 'ICustomAttributeProvider'>, <type 'IReflect'>, <type 'IReflectableType'>, <type '_Type'>, <type 'object'>
    """ TypeDelegator(delegatingType: Type) """
    @property
    def IsConstructedGenericType(self) -> bool:
        """ Get: IsConstructedGenericType(self: TypeDelegator) -> bool """
        ...

    @property
    def MetadataToken(self) -> int:
        """ Get: MetadataToken(self: TypeDelegator) -> int """
        ...


    def __new__(cls, delegatingType:Type) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, delegatingType: Type)
        """
        ...

    typeImpl = ...


class TypeFilter(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TypeFilter(object: object, method: IntPtr) """
    def BeginInvoke(self, m:Type, filterCriteria:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: TypeFilter, m: Type, filterCriteria: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> bool:
        """ EndInvoke(self: TypeFilter, result: IAsyncResult) -> bool """
        ...

    def Invoke(self, m:Type, filterCriteria:object) -> bool:
        """ Invoke(self: TypeFilter, m: Type, filterCriteria: object) -> bool """
        ...


# variables with complex values

