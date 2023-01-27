# encoding: utf-8
# module System.Runtime.InteropServices calls itself InteropServices
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Runtime.WindowsRuntime, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid

from System import (Array, AsyncCallback, Attribute, Byte, Decimal, Delegate, 
    Enum, Guid, IAsyncResult, IDisposable, IEquatable, Int16, Int64, IntPtr, 
    MarshalByRefObject, MulticastDelegate, RuntimeFieldHandle, 
    RuntimeMethodHandle, RuntimeTypeHandle, SystemException, Type, 
    TypedReference, UInt32, UInt64, Version)

from System.Globalization import CultureInfo

from System.IO import FileStream, Stream

from System.Reflection import (Assembly, AssemblyName, Binder, BindingFlags, 
    CallingConventions, ConstructorInfo, EventAttributes, EventInfo, 
    FieldAttributes, FieldInfo, ICustomAttributeProvider, InterfaceMapping, 
    ManifestResourceInfo, MemberFilter, MemberInfo, MemberTypes, 
    MethodAttributes, MethodBase, MethodImplAttributes, MethodInfo, Module, 
    PropertyAttributes, PropertyInfo, StrongNameKeyPair, TypeAttributes, 
    TypeFilter)

from System.Reflection.Emit import AssemblyBuilder

from System.Runtime.ConstrainedExecution import CriticalFinalizerObject

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from System.Security import SecureString

from System.Security.Policy import Evidence

from System.Threading import Thread

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, IMarshal, T, 
    field#)
"""

# no functions
# classes

class _Attribute: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _Attribute, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _Attribute, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _Attribute) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _Attribute, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class AllowReversePInvokeCallsAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AllowReversePInvokeCallsAttribute() """
    pass

class Architecture(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Architecture, values: Arm (2), Arm64 (3), X64 (1), X86 (0) """
    Arm: Architecture = ...
    Arm64: Architecture = ...
    value__ = ...
    X64: Architecture = ...
    X86: Architecture = ...


class ArrayWithOffset: # skipped bases: <type 'object'>, <type 'object'>
    """ ArrayWithOffset(array: object, offset: int) """
    def Equals(self, obj:object) -> bool:
        """
        Equals(self: ArrayWithOffset, obj: object) -> bool
        Equals(self: ArrayWithOffset, obj: ArrayWithOffset) -> bool
        """
        ...

    def GetArray(self) -> object:
        """ GetArray(self: ArrayWithOffset) -> object """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ArrayWithOffset) -> int """
        ...

    def GetOffset(self) -> int:
        """ GetOffset(self: ArrayWithOffset) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AssemblyRegistrationFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) AssemblyRegistrationFlags, values: None (0), SetCodeBase (1) """
    SetCodeBase: AssemblyRegistrationFlags = ...
    value__ = ...


class AutomationProxyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AutomationProxyAttribute(val: bool) """
    @property
    def Value(self) -> bool:
        """ Get: Value(self: AutomationProxyAttribute) -> bool """
        ...


    def __new__(cls, val:bool) -> Self:
        """ __new__(cls: type, val: bool) """
        ...


class BestFitMappingAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ BestFitMappingAttribute(BestFitMapping: bool) """
    @property
    def BestFitMapping(self) -> bool:
        """ Get: BestFitMapping(self: BestFitMappingAttribute) -> bool """
        ...


    def __new__(cls, BestFitMapping:bool) -> Self:
        """ __new__(cls: type, BestFitMapping: bool) """
        ...

    ThrowOnUnmappableChar = ...


class BINDPTR: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    lpfuncdesc = ...
    lptcomp = ...
    lpvardesc = ...


class BIND_OPTS: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    cbStruct = ...
    dwTickCountDeadline = ...
    grfFlags = ...
    grfMode = ...


class BStrWrapper: # skipped bases: <type 'object'>, <type 'object'>
    """
    BStrWrapper(value: str)
    BStrWrapper(value: object)
    """
    @property
    def WrappedObject(self) -> str:
        """ Get: WrappedObject(self: BStrWrapper) -> str """
        ...



class CALLCONV(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CALLCONV, values: CC_CDECL (1), CC_MACPASCAL (3), CC_MAX (9), CC_MPWCDECL (7), CC_MPWPASCAL (8), CC_MSCPASCAL (2), CC_PASCAL (2), CC_RESERVED (5), CC_STDCALL (4), CC_SYSCALL (6) """
    CC_CDECL: CALLCONV = ...
    CC_MACPASCAL: CALLCONV = ...
    CC_MAX: CALLCONV = ...
    CC_MPWCDECL: CALLCONV = ...
    CC_MPWPASCAL: CALLCONV = ...
    CC_MSCPASCAL: CALLCONV = ...
    CC_PASCAL: CALLCONV = ...
    CC_RESERVED: CALLCONV = ...
    CC_STDCALL: CALLCONV = ...
    CC_SYSCALL: CALLCONV = ...
    value__ = ...


class CallingConvention(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CallingConvention, values: Cdecl (2), FastCall (5), StdCall (3), ThisCall (4), Winapi (1) """
    Cdecl: CallingConvention = ...
    FastCall: CallingConvention = ...
    StdCall: CallingConvention = ...
    ThisCall: CallingConvention = ...
    value__ = ...
    Winapi: CallingConvention = ...


class CharSet(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CharSet, values: Ansi (2), Auto (4), None (1), Unicode (3) """
    Ansi: CharSet = ...
    Auto: CharSet = ...
    Unicode: CharSet = ...
    value__ = ...


class ClassInterfaceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ClassInterfaceAttribute(classInterfaceType: ClassInterfaceType)
    ClassInterfaceAttribute(classInterfaceType: Int16)
    """
    @property
    def Value(self) -> ClassInterfaceType:
        """ Get: Value(self: ClassInterfaceAttribute) -> ClassInterfaceType """
        ...


    def __new__(cls, classInterfaceType:ClassInterfaceType) -> Self:
        """
        __new__(cls: type, classInterfaceType: ClassInterfaceType)
        __new__(cls: type, classInterfaceType: Int16)
        """
        ...


class ClassInterfaceType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ClassInterfaceType, values: AutoDispatch (1), AutoDual (2), None (0) """
    AutoDispatch: ClassInterfaceType = ...
    AutoDual: ClassInterfaceType = ...
    value__ = ...


class CoClassAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CoClassAttribute(coClass: Type) """
    @property
    def CoClass(self) -> Type:
        """ Get: CoClass(self: CoClassAttribute) -> Type """
        ...


    def __new__(cls, coClass:Type) -> Self:
        """ __new__(cls: type, coClass: Type) """
        ...


class ComAliasNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ComAliasNameAttribute(alias: str) """
    @property
    def Value(self) -> str:
        """ Get: Value(self: ComAliasNameAttribute) -> str """
        ...


    def __new__(cls, alias:str) -> Self:
        """ __new__(cls: type, alias: str) """
        ...


class ComAwareEventInfo(EventInfo): # skipped bases: <type '_MemberInfo'>, <type 'ICustomAttributeProvider'>, <type '_EventInfo'>, <type 'object'>
    """ ComAwareEventInfo(type: Type, eventName: str) """
    def __new__(cls, type:Type, eventName:str) -> Self:
        """ __new__(cls: type, type: Type, eventName: str) """
        ...


class ComCompatibleVersionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ComCompatibleVersionAttribute(major: int, minor: int, build: int, revision: int) """
    @property
    def BuildNumber(self) -> int:
        """ Get: BuildNumber(self: ComCompatibleVersionAttribute) -> int """
        ...

    @property
    def MajorVersion(self) -> int:
        """ Get: MajorVersion(self: ComCompatibleVersionAttribute) -> int """
        ...

    @property
    def MinorVersion(self) -> int:
        """ Get: MinorVersion(self: ComCompatibleVersionAttribute) -> int """
        ...

    @property
    def RevisionNumber(self) -> int:
        """ Get: RevisionNumber(self: ComCompatibleVersionAttribute) -> int """
        ...


    def __new__(cls, major:int, minor:int, build:int, revision:int) -> Self:
        """ __new__(cls: type, major: int, minor: int, build: int, revision: int) """
        ...


class ComConversionLossAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ComConversionLossAttribute() """
    pass

class ComDefaultInterfaceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ComDefaultInterfaceAttribute(defaultInterface: Type) """
    @property
    def Value(self) -> Type:
        """ Get: Value(self: ComDefaultInterfaceAttribute) -> Type """
        ...


    def __new__(cls, defaultInterface:Type) -> Self:
        """ __new__(cls: type, defaultInterface: Type) """
        ...


class ComEventInterfaceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ComEventInterfaceAttribute(SourceInterface: Type, EventProvider: Type) """
    @property
    def EventProvider(self) -> Type:
        """ Get: EventProvider(self: ComEventInterfaceAttribute) -> Type """
        ...

    @property
    def SourceInterface(self) -> Type:
        """ Get: SourceInterface(self: ComEventInterfaceAttribute) -> Type """
        ...


    def __new__(cls, SourceInterface:Type, EventProvider:Type) -> Self:
        """ __new__(cls: type, SourceInterface: Type, EventProvider: Type) """
        ...


class ComEventsHelper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Combine(rcw:object, iid:Guid, dispid:int, d:Delegate): # -> 
        """ Combine(rcw: object, iid: Guid, dispid: int, d: Delegate) """
        ...

    @staticmethod
    def Remove(rcw:object, iid:Guid, dispid:int, d:Delegate) -> Delegate:
        """ Remove(rcw: object, iid: Guid, dispid: int, d: Delegate) -> Delegate """
        ...

    __all__: list = ...


class ExternalException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ExternalException()
    ExternalException(message: str)
    ExternalException(message: str, inner: Exception)
    ExternalException(message: str, errorCode: int)
    """
    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: ExternalException) -> int """
        ...


    SerializeObjectState = ...


class COMException(ExternalException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    COMException()
    COMException(message: str)
    COMException(message: str, inner: Exception)
    COMException(message: str, errorCode: int)
    """
    SerializeObjectState = ...


class ComImportAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ComImportAttribute() """
    pass

class ComInterfaceType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ComInterfaceType, values: InterfaceIsDual (0), InterfaceIsIDispatch (2), InterfaceIsIInspectable (3), InterfaceIsIUnknown (1) """
    InterfaceIsDual: ComInterfaceType = ...
    InterfaceIsIDispatch: ComInterfaceType = ...
    InterfaceIsIInspectable: ComInterfaceType = ...
    InterfaceIsIUnknown: ComInterfaceType = ...
    value__ = ...


class ComMemberType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ComMemberType, values: Method (0), PropGet (1), PropSet (2) """
    Method: ComMemberType = ...
    PropGet: ComMemberType = ...
    PropSet: ComMemberType = ...
    value__ = ...


class ComRegisterFunctionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ComRegisterFunctionAttribute() """
    pass

class ComSourceInterfacesAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ComSourceInterfacesAttribute(sourceInterfaces: str)
    ComSourceInterfacesAttribute(sourceInterface: Type)
    ComSourceInterfacesAttribute(sourceInterface1: Type, sourceInterface2: Type)
    ComSourceInterfacesAttribute(sourceInterface1: Type, sourceInterface2: Type, sourceInterface3: Type)
    ComSourceInterfacesAttribute(sourceInterface1: Type, sourceInterface2: Type, sourceInterface3: Type, sourceInterface4: Type)
    """
    @property
    def Value(self) -> str:
        """ Get: Value(self: ComSourceInterfacesAttribute) -> str """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, sourceInterfaces: str)
        __new__(cls: type, sourceInterface: Type)
        __new__(cls: type, sourceInterface1: Type, sourceInterface2: Type)
        __new__(cls: type, sourceInterface1: Type, sourceInterface2: Type, sourceInterface3: Type)
        __new__(cls: type, sourceInterface1: Type, sourceInterface2: Type, sourceInterface3: Type, sourceInterface4: Type)
        """
        ...


class ComUnregisterFunctionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ComUnregisterFunctionAttribute() """
    pass

class ComVisibleAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ComVisibleAttribute(visibility: bool) """
    @property
    def Value(self) -> bool:
        """ Get: Value(self: ComVisibleAttribute) -> bool """
        ...


    def __new__(cls, visibility:bool) -> Self:
        """ __new__(cls: type, visibility: bool) """
        ...


class CONNECTDATA: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwCookie = ...
    pUnk = ...


class CriticalHandle(IDisposable, CriticalFinalizerObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsClosed(self) -> bool:
        """ Get: IsClosed(self: CriticalHandle) -> bool """
        ...

    @property
    def IsInvalid(self) -> bool:
        """ Get: IsInvalid(self: CriticalHandle) -> bool """
        ...


    def Close(self): # -> 
        """ Close(self: CriticalHandle) """
        ...

    def ReleaseHandle(self, *args): #cannot find CLR method
        """ ReleaseHandle(self: CriticalHandle) -> bool """
        ...

    def SetHandle(self, *args): #cannot find CLR method
        """ SetHandle(self: CriticalHandle, handle: IntPtr) """
        ...

    def SetHandleAsInvalid(self): # -> 
        """ SetHandleAsInvalid(self: CriticalHandle) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, invalidHandleValue: IntPtr) """
        ...

    handle = ...


class CurrencyWrapper: # skipped bases: <type 'object'>, <type 'object'>
    """
    CurrencyWrapper(obj: Decimal)
    CurrencyWrapper(obj: object)
    """
    @property
    def WrappedObject(self) -> Decimal:
        """ Get: WrappedObject(self: CurrencyWrapper) -> Decimal """
        ...



class CustomQueryInterfaceMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CustomQueryInterfaceMode, values: Allow (1), Ignore (0) """
    Allow: CustomQueryInterfaceMode = ...
    Ignore: CustomQueryInterfaceMode = ...
    value__ = ...


class CustomQueryInterfaceResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CustomQueryInterfaceResult, values: Failed (2), Handled (0), NotHandled (1) """
    Failed: CustomQueryInterfaceResult = ...
    Handled: CustomQueryInterfaceResult = ...
    NotHandled: CustomQueryInterfaceResult = ...
    value__ = ...


class DefaultCharSetAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DefaultCharSetAttribute(charSet: CharSet) """
    @property
    def CharSet(self) -> CharSet:
        """ Get: CharSet(self: DefaultCharSetAttribute) -> CharSet """
        ...


    def __new__(cls, charSet:CharSet) -> Self:
        """ __new__(cls: type, charSet: CharSet) """
        ...


class DefaultDllImportSearchPathsAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DefaultDllImportSearchPathsAttribute(paths: DllImportSearchPath) """
    @property
    def Paths(self) -> DllImportSearchPath:
        """ Get: Paths(self: DefaultDllImportSearchPathsAttribute) -> DllImportSearchPath """
        ...


    def __new__(cls, paths:DllImportSearchPath) -> Self:
        """ __new__(cls: type, paths: DllImportSearchPath) """
        ...


class DefaultParameterValueAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DefaultParameterValueAttribute(value: object) """
    @property
    def Value(self) -> object:
        """ Get: Value(self: DefaultParameterValueAttribute) -> object """
        ...


    def __new__(cls, value:object) -> Self:
        """ __new__(cls: type, value: object) """
        ...


class DESCKIND(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DESCKIND, values: DESCKIND_FUNCDESC (1), DESCKIND_IMPLICITAPPOBJ (4), DESCKIND_MAX (5), DESCKIND_NONE (0), DESCKIND_TYPECOMP (3), DESCKIND_VARDESC (2) """
    DESCKIND_FUNCDESC: DESCKIND = ...
    DESCKIND_IMPLICITAPPOBJ: DESCKIND = ...
    DESCKIND_MAX: DESCKIND = ...
    DESCKIND_NONE: DESCKIND = ...
    DESCKIND_TYPECOMP: DESCKIND = ...
    DESCKIND_VARDESC: DESCKIND = ...
    value__ = ...


class DispatchWrapper: # skipped bases: <type 'object'>, <type 'object'>
    """ DispatchWrapper(obj: object) """
    @property
    def WrappedObject(self) -> object:
        """ Get: WrappedObject(self: DispatchWrapper) -> object """
        ...



class DispIdAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DispIdAttribute(dispId: int) """
    @property
    def Value(self) -> int:
        """ Get: Value(self: DispIdAttribute) -> int """
        ...


    def __new__(cls, dispId:int) -> Self:
        """ __new__(cls: type, dispId: int) """
        ...


class DISPPARAMS: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    cArgs = ...
    cNamedArgs = ...
    rgdispidNamedArgs = ...
    rgvarg = ...


class DllImportAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DllImportAttribute(dllName: str) """
    @property
    def Value(self) -> str:
        """ Get: Value(self: DllImportAttribute) -> str """
        ...


    def __new__(cls, dllName:str) -> Self:
        """ __new__(cls: type, dllName: str) """
        ...

    BestFitMapping = ...
    CallingConvention = ...
    CharSet = ...
    EntryPoint = ...
    ExactSpelling = ...
    PreserveSig = ...
    SetLastError = ...
    ThrowOnUnmappableChar = ...


class DllImportSearchPath(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DllImportSearchPath, values: ApplicationDirectory (512), AssemblyDirectory (2), LegacyBehavior (0), SafeDirectories (4096), System32 (2048), UseDllDirectoryForDependencies (256), UserDirectories (1024) """
    ApplicationDirectory: DllImportSearchPath = ...
    AssemblyDirectory: DllImportSearchPath = ...
    LegacyBehavior: DllImportSearchPath = ...
    SafeDirectories: DllImportSearchPath = ...
    System32: DllImportSearchPath = ...
    UseDllDirectoryForDependencies: DllImportSearchPath = ...
    UserDirectories: DllImportSearchPath = ...
    value__ = ...


class ELEMDESC: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def DESCUNION(self, *args): #cannot find CLR method
        """ no doc """
        ...

    desc = ...
    tdesc = ...


class ErrorWrapper: # skipped bases: <type 'object'>, <type 'object'>
    """
    ErrorWrapper(errorCode: int)
    ErrorWrapper(errorCode: object)
    ErrorWrapper(e: Exception)
    """
    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: ErrorWrapper) -> int """
        ...



class EXCEPINFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    bstrDescription = ...
    bstrHelpFile = ...
    bstrSource = ...
    dwHelpContext = ...
    pfnDeferredFillIn = ...
    pvReserved = ...
    wCode = ...
    wReserved = ...


class ExporterEventKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ExporterEventKind, values: ERROR_REFTOINVALIDASSEMBLY (2), NOTIF_CONVERTWARNING (1), NOTIF_TYPECONVERTED (0) """
    ERROR_REFTOINVALIDASSEMBLY: ExporterEventKind = ...
    NOTIF_CONVERTWARNING: ExporterEventKind = ...
    NOTIF_TYPECONVERTED: ExporterEventKind = ...
    value__ = ...


class ExtensibleClassFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def RegisterObjectCreationCallback(callback:ObjectCreationDelegate): # -> 
        """ RegisterObjectCreationCallback(callback: ObjectCreationDelegate) """
        ...


class FieldOffsetAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ FieldOffsetAttribute(offset: int) """
    @property
    def Value(self) -> int:
        """ Get: Value(self: FieldOffsetAttribute) -> int """
        ...


    def __new__(cls, offset:int) -> Self:
        """ __new__(cls: type, offset: int) """
        ...


class FILETIME: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwHighDateTime = ...
    dwLowDateTime = ...


class FUNCDESC: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    callconv = ...
    cParams = ...
    cParamsOpt = ...
    cScodes = ...
    elemdescFunc = ...
    funckind = ...
    invkind = ...
    lprgelemdescParam = ...
    lprgscode = ...
    memid = ...
    oVft = ...
    wFuncFlags = ...


class FUNCFLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) FUNCFLAGS, values: FUNCFLAG_FBINDABLE (4), FUNCFLAG_FDEFAULTBIND (32), FUNCFLAG_FDEFAULTCOLLELEM (256), FUNCFLAG_FDISPLAYBIND (16), FUNCFLAG_FHIDDEN (64), FUNCFLAG_FIMMEDIATEBIND (4096), FUNCFLAG_FNONBROWSABLE (1024), FUNCFLAG_FREPLACEABLE (2048), FUNCFLAG_FREQUESTEDIT (8), FUNCFLAG_FRESTRICTED (1), FUNCFLAG_FSOURCE (2), FUNCFLAG_FUIDEFAULT (512), FUNCFLAG_FUSESGETLASTERROR (128) """
    FUNCFLAG_FBINDABLE: FUNCFLAGS = ...
    FUNCFLAG_FDEFAULTBIND: FUNCFLAGS = ...
    FUNCFLAG_FDEFAULTCOLLELEM: FUNCFLAGS = ...
    FUNCFLAG_FDISPLAYBIND: FUNCFLAGS = ...
    FUNCFLAG_FHIDDEN: FUNCFLAGS = ...
    FUNCFLAG_FIMMEDIATEBIND: FUNCFLAGS = ...
    FUNCFLAG_FNONBROWSABLE: FUNCFLAGS = ...
    FUNCFLAG_FREPLACEABLE: FUNCFLAGS = ...
    FUNCFLAG_FREQUESTEDIT: FUNCFLAGS = ...
    FUNCFLAG_FRESTRICTED: FUNCFLAGS = ...
    FUNCFLAG_FSOURCE: FUNCFLAGS = ...
    FUNCFLAG_FUIDEFAULT: FUNCFLAGS = ...
    FUNCFLAG_FUSESGETLASTERROR: FUNCFLAGS = ...
    value__ = ...


class FUNCKIND(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FUNCKIND, values: FUNC_DISPATCH (4), FUNC_NONVIRTUAL (2), FUNC_PUREVIRTUAL (1), FUNC_STATIC (3), FUNC_VIRTUAL (0) """
    FUNC_DISPATCH: FUNCKIND = ...
    FUNC_NONVIRTUAL: FUNCKIND = ...
    FUNC_PUREVIRTUAL: FUNCKIND = ...
    FUNC_STATIC: FUNCKIND = ...
    FUNC_VIRTUAL: FUNCKIND = ...
    value__ = ...


class GCHandle: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsAllocated(self) -> bool:
        """ Get: IsAllocated(self: GCHandle) -> bool """
        ...

    @property
    def Target(self) -> object:
        """
        Get: Target(self: GCHandle) -> object
        Set: Target(self: GCHandle) = value
        """
        ...


    def AddrOfPinnedObject(self) -> IntPtr:
        """ AddrOfPinnedObject(self: GCHandle) -> IntPtr """
        ...

    @staticmethod
    def Alloc(value:object, type:GCHandleType = ...) -> GCHandle:
        """
        Alloc(value: object) -> GCHandle
        Alloc(value: object, type: GCHandleType) -> GCHandle
        """
        ...

    def Equals(self, o:object) -> bool:
        """ Equals(self: GCHandle, o: object) -> bool """
        ...

    def Free(self): # -> 
        """ Free(self: GCHandle) """
        ...

    @staticmethod
    def FromIntPtr(value:IntPtr) -> GCHandle:
        """ FromIntPtr(value: IntPtr) -> GCHandle """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: GCHandle) -> int """
        ...

    @staticmethod
    def ToIntPtr(value:GCHandle) -> IntPtr:
        """ ToIntPtr(value: GCHandle) -> IntPtr """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class GCHandleType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GCHandleType, values: Normal (2), Pinned (3), Weak (0), WeakTrackResurrection (1) """
    Normal: GCHandleType = ...
    Pinned: GCHandleType = ...
    value__ = ...
    Weak: GCHandleType = ...
    WeakTrackResurrection: GCHandleType = ...


class GuidAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ GuidAttribute(guid: str) """
    @property
    def Value(self) -> str:
        """ Get: Value(self: GuidAttribute) -> str """
        ...


    def __new__(cls, guid:str) -> Self:
        """ __new__(cls: type, guid: str) """
        ...


class HandleCollector: # skipped bases: <type 'object'>, <type 'object'>
    """
    HandleCollector(name: str, initialThreshold: int)
    HandleCollector(name: str, initialThreshold: int, maximumThreshold: int)
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: HandleCollector) -> int """
        ...

    @property
    def InitialThreshold(self) -> int:
        """ Get: InitialThreshold(self: HandleCollector) -> int """
        ...

    @property
    def MaximumThreshold(self) -> int:
        """ Get: MaximumThreshold(self: HandleCollector) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: HandleCollector) -> str """
        ...


    def Add(self): # -> 
        """ Add(self: HandleCollector) """
        ...

    def Remove(self): # -> 
        """ Remove(self: HandleCollector) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


class HandleRef: # skipped bases: <type 'object'>, <type 'object'>
    """ HandleRef(wrapper: object, handle: IntPtr) """
    @property
    def Handle(self) -> IntPtr:
        """ Get: Handle(self: HandleRef) -> IntPtr """
        ...

    @property
    def Wrapper(self) -> object:
        """ Get: Wrapper(self: HandleRef) -> object """
        ...


    @staticmethod
    def ToIntPtr(value:HandleRef) -> IntPtr:
        """ ToIntPtr(value: HandleRef) -> IntPtr """
        ...


class ICustomAdapter: # skipped bases: <type 'object'>
    """ no doc """
    def GetUnderlyingObject(self) -> object:
        """ GetUnderlyingObject(self: ICustomAdapter) -> object """
        ...


class ICustomFactory: # skipped bases: <type 'object'>
    """ no doc """
    def CreateInstance(self, serverType:Type) -> MarshalByRefObject:
        """ CreateInstance(self: ICustomFactory, serverType: Type) -> MarshalByRefObject """
        ...


class ICustomMarshaler: # skipped bases: <type 'object'>
    """ no doc """
    def CleanUpManagedData(self, ManagedObj:object): # -> 
        """ CleanUpManagedData(self: ICustomMarshaler, ManagedObj: object) """
        ...

    def CleanUpNativeData(self, pNativeData:IntPtr): # -> 
        """ CleanUpNativeData(self: ICustomMarshaler, pNativeData: IntPtr) """
        ...

    def GetNativeDataSize(self) -> int:
        """ GetNativeDataSize(self: ICustomMarshaler) -> int """
        ...

    def MarshalManagedToNative(self, ManagedObj:object) -> IntPtr:
        """ MarshalManagedToNative(self: ICustomMarshaler, ManagedObj: object) -> IntPtr """
        ...

    def MarshalNativeToManaged(self, pNativeData:IntPtr) -> object:
        """ MarshalNativeToManaged(self: ICustomMarshaler, pNativeData: IntPtr) -> object """
        ...


class ICustomQueryInterface: # skipped bases: <type 'object'>
    """ no doc """
    def GetInterface(self, iid, ppv) -> Tuple_[CustomQueryInterfaceResult, Guid, IntPtr]:
        """ GetInterface(self: ICustomQueryInterface, iid: Guid) -> (CustomQueryInterfaceResult, Guid, IntPtr) """
        ...


class IDispatchImplAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    IDispatchImplAttribute(implType: IDispatchImplType)
    IDispatchImplAttribute(implType: Int16)
    """
    @property
    def Value(self) -> IDispatchImplType:
        """ Get: Value(self: IDispatchImplAttribute) -> IDispatchImplType """
        ...


    def __new__(cls, implType:IDispatchImplType) -> Self:
        """
        __new__(cls: type, implType: IDispatchImplType)
        __new__(cls: type, implType: Int16)
        """
        ...


class IDispatchImplType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum IDispatchImplType, values: CompatibleImpl (2), InternalImpl (1), SystemDefinedImpl (0) """
    CompatibleImpl: IDispatchImplType = ...
    InternalImpl: IDispatchImplType = ...
    SystemDefinedImpl: IDispatchImplType = ...
    value__ = ...


class IDLDESC: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    dwReserved = ...
    wIDLFlags = ...


class IDLFLAG(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) IDLFLAG, values: IDLFLAG_FIN (1), IDLFLAG_FLCID (4), IDLFLAG_FOUT (2), IDLFLAG_FRETVAL (8), IDLFLAG_NONE (0) """
    IDLFLAG_FIN: IDLFLAG = ...
    IDLFLAG_FLCID: IDLFLAG = ...
    IDLFLAG_FOUT: IDLFLAG = ...
    IDLFLAG_FRETVAL: IDLFLAG = ...
    IDLFLAG_NONE: IDLFLAG = ...
    value__ = ...


class IMPLTYPEFLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) IMPLTYPEFLAGS, values: IMPLTYPEFLAG_FDEFAULT (1), IMPLTYPEFLAG_FDEFAULTVTABLE (8), IMPLTYPEFLAG_FRESTRICTED (4), IMPLTYPEFLAG_FSOURCE (2) """
    IMPLTYPEFLAG_FDEFAULT: IMPLTYPEFLAGS = ...
    IMPLTYPEFLAG_FDEFAULTVTABLE: IMPLTYPEFLAGS = ...
    IMPLTYPEFLAG_FRESTRICTED: IMPLTYPEFLAGS = ...
    IMPLTYPEFLAG_FSOURCE: IMPLTYPEFLAGS = ...
    value__ = ...


class ImportedFromTypeLibAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ImportedFromTypeLibAttribute(tlbFile: str) """
    @property
    def Value(self) -> str:
        """ Get: Value(self: ImportedFromTypeLibAttribute) -> str """
        ...


    def __new__(cls, tlbFile:str) -> Self:
        """ __new__(cls: type, tlbFile: str) """
        ...


class ImporterEventKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ImporterEventKind, values: ERROR_REFTOINVALIDTYPELIB (2), NOTIF_CONVERTWARNING (1), NOTIF_TYPECONVERTED (0) """
    ERROR_REFTOINVALIDTYPELIB: ImporterEventKind = ...
    NOTIF_CONVERTWARNING: ImporterEventKind = ...
    NOTIF_TYPECONVERTED: ImporterEventKind = ...
    value__ = ...


class InAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ InAttribute() """
    pass

class InterfaceTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    InterfaceTypeAttribute(interfaceType: ComInterfaceType)
    InterfaceTypeAttribute(interfaceType: Int16)
    """
    @property
    def Value(self) -> ComInterfaceType:
        """ Get: Value(self: InterfaceTypeAttribute) -> ComInterfaceType """
        ...


    def __new__(cls, interfaceType:ComInterfaceType) -> Self:
        """
        __new__(cls: type, interfaceType: ComInterfaceType)
        __new__(cls: type, interfaceType: Int16)
        """
        ...


class InvalidComObjectException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidComObjectException()
    InvalidComObjectException(message: str)
    InvalidComObjectException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class InvalidOleVariantTypeException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InvalidOleVariantTypeException()
    InvalidOleVariantTypeException(message: str)
    InvalidOleVariantTypeException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class INVOKEKIND(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum INVOKEKIND, values: INVOKE_FUNC (1), INVOKE_PROPERTYGET (2), INVOKE_PROPERTYPUT (4), INVOKE_PROPERTYPUTREF (8) """
    INVOKE_FUNC: INVOKEKIND = ...
    INVOKE_PROPERTYGET: INVOKEKIND = ...
    INVOKE_PROPERTYPUT: INVOKEKIND = ...
    INVOKE_PROPERTYPUTREF: INVOKEKIND = ...
    value__ = ...


class IRegistrationServices: # skipped bases: <type 'object'>
    """ no doc """
    def GetManagedCategoryGuid(self) -> Guid:
        """ GetManagedCategoryGuid(self: IRegistrationServices) -> Guid """
        ...

    def GetProgIdForType(self, type:Type) -> str:
        """ GetProgIdForType(self: IRegistrationServices, type: Type) -> str """
        ...

    def GetRegistrableTypesInAssembly(self, assembly:Assembly) -> Array:
        """ GetRegistrableTypesInAssembly(self: IRegistrationServices, assembly: Assembly) -> Array[Type] """
        ...

    def RegisterAssembly(self, assembly:Assembly, flags:AssemblyRegistrationFlags) -> bool:
        """ RegisterAssembly(self: IRegistrationServices, assembly: Assembly, flags: AssemblyRegistrationFlags) -> bool """
        ...

    def RegisterTypeForComClients(self, type:Type, g:Guid) -> Guid:
        """ RegisterTypeForComClients(self: IRegistrationServices, type: Type, g: Guid) -> Guid """
        ...

    def TypeRepresentsComType(self, type:Type) -> bool:
        """ TypeRepresentsComType(self: IRegistrationServices, type: Type) -> bool """
        ...

    def TypeRequiresRegistration(self, type:Type) -> bool:
        """ TypeRequiresRegistration(self: IRegistrationServices, type: Type) -> bool """
        ...

    def UnregisterAssembly(self, assembly:Assembly) -> bool:
        """ UnregisterAssembly(self: IRegistrationServices, assembly: Assembly) -> bool """
        ...


class ITypeLibConverter: # skipped bases: <type 'object'>
    """ no doc """
    def ConvertAssemblyToTypeLib(self, assembly:Assembly, typeLibName:str, flags:TypeLibExporterFlags, notifySink:ITypeLibExporterNotifySink) -> object:
        """ ConvertAssemblyToTypeLib(self: ITypeLibConverter, assembly: Assembly, typeLibName: str, flags: TypeLibExporterFlags, notifySink: ITypeLibExporterNotifySink) -> object """
        ...

    def ConvertTypeLibToAssembly(self, typeLib:object, asmFileName:str, flags:int, notifySink:ITypeLibImporterNotifySink, publicKey:Array, keyPair:StrongNameKeyPair, *__args:bool) -> AssemblyBuilder:
        """
        ConvertTypeLibToAssembly(self: ITypeLibConverter, typeLib: object, asmFileName: str, flags: TypeLibImporterFlags, notifySink: ITypeLibImporterNotifySink, publicKey: Array[Byte], keyPair: StrongNameKeyPair, asmNamespace: str, asmVersion: Version) -> AssemblyBuilder
        ConvertTypeLibToAssembly(self: ITypeLibConverter, typeLib: object, asmFileName: str, flags: int, notifySink: ITypeLibImporterNotifySink, publicKey: Array[Byte], keyPair: StrongNameKeyPair, unsafeInterfaces: bool) -> AssemblyBuilder
        """
        ...

    def GetPrimaryInteropAssembly(self, g, major, minor, lcid, asmName, asmCodeBase) -> Tuple_[bool, str, str]:
        """ GetPrimaryInteropAssembly(self: ITypeLibConverter, g: Guid, major: int, minor: int, lcid: int) -> (bool, str, str) """
        ...


class ITypeLibExporterNameProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetNames(self) -> Array:
        """ GetNames(self: ITypeLibExporterNameProvider) -> Array[str] """
        ...


class ITypeLibExporterNotifySink: # skipped bases: <type 'object'>
    """ no doc """
    def ReportEvent(self, eventKind:ExporterEventKind, eventCode:int, eventMsg:str): # -> 
        """ ReportEvent(self: ITypeLibExporterNotifySink, eventKind: ExporterEventKind, eventCode: int, eventMsg: str) """
        ...

    def ResolveRef(self, assembly:Assembly) -> object:
        """ ResolveRef(self: ITypeLibExporterNotifySink, assembly: Assembly) -> object """
        ...


class ITypeLibImporterNotifySink: # skipped bases: <type 'object'>
    """ no doc """
    def ReportEvent(self, eventKind:ImporterEventKind, eventCode:int, eventMsg:str): # -> 
        """ ReportEvent(self: ITypeLibImporterNotifySink, eventKind: ImporterEventKind, eventCode: int, eventMsg: str) """
        ...

    def ResolveRef(self, typeLib:object) -> Assembly:
        """ ResolveRef(self: ITypeLibImporterNotifySink, typeLib: object) -> Assembly """
        ...


class LayoutKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LayoutKind, values: Auto (3), Explicit (2), Sequential (0) """
    Auto: LayoutKind = ...
    Explicit: LayoutKind = ...
    Sequential: LayoutKind = ...
    value__ = ...


class LCIDConversionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ LCIDConversionAttribute(lcid: int) """
    @property
    def Value(self) -> int:
        """ Get: Value(self: LCIDConversionAttribute) -> int """
        ...


    def __new__(cls, lcid:int) -> Self:
        """ __new__(cls: type, lcid: int) """
        ...


class LIBFLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) LIBFLAGS, values: LIBFLAG_FCONTROL (2), LIBFLAG_FHASDISKIMAGE (8), LIBFLAG_FHIDDEN (4), LIBFLAG_FRESTRICTED (1) """
    LIBFLAG_FCONTROL: LIBFLAGS = ...
    LIBFLAG_FHASDISKIMAGE: LIBFLAGS = ...
    LIBFLAG_FHIDDEN: LIBFLAGS = ...
    LIBFLAG_FRESTRICTED: LIBFLAGS = ...
    value__ = ...


class ManagedToNativeComInteropStubAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ManagedToNativeComInteropStubAttribute(classType: Type, methodName: str) """
    @property
    def ClassType(self) -> Type:
        """ Get: ClassType(self: ManagedToNativeComInteropStubAttribute) -> Type """
        ...

    @property
    def MethodName(self) -> str:
        """ Get: MethodName(self: ManagedToNativeComInteropStubAttribute) -> str """
        ...


    def __new__(cls, classType:Type, methodName:str) -> Self:
        """ __new__(cls: type, classType: Type, methodName: str) """
        ...


class Marshal: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AddRef(pUnk:IntPtr) -> int:
        """ AddRef(pUnk: IntPtr) -> int """
        ...

    @staticmethod
    def AllocCoTaskMem(cb:int) -> IntPtr:
        """ AllocCoTaskMem(cb: int) -> IntPtr """
        ...

    @staticmethod
    def AllocHGlobal(cb:IntPtr) -> IntPtr:
        """
        AllocHGlobal(cb: IntPtr) -> IntPtr
        AllocHGlobal(cb: int) -> IntPtr
        """
        ...

    @staticmethod
    def AreComObjectsAvailableForCleanup() -> bool:
        """ AreComObjectsAvailableForCleanup() -> bool """
        ...

    @staticmethod
    def BindToMoniker(monikerName:str) -> object:
        """ BindToMoniker(monikerName: str) -> object """
        ...

    @staticmethod
    def ChangeWrapperHandleStrength(otp:object, fIsWeak:bool): # -> 
        """ ChangeWrapperHandleStrength(otp: object, fIsWeak: bool) """
        ...

    @staticmethod
    def CleanupUnusedObjectsInCurrentContext(): # -> 
        """ CleanupUnusedObjectsInCurrentContext() """
        ...

    @staticmethod
    def Copy(source, *__args): # -> 
        """ Copy(source: Array[int], startIndex: int, destination: IntPtr, length: int)Copy(source: Array[Char], startIndex: int, destination: IntPtr, length: int)Copy(source: Array[Int16], startIndex: int, destination: IntPtr, length: int)Copy(source: Array[Int64], startIndex: int, destination: IntPtr, length: int)Copy(source: Array[Single], startIndex: int, destination: IntPtr, length: int)Copy(source: Array[float], startIndex: int, destination: IntPtr, length: int)Copy(source: Array[Byte], startIndex: int, destination: IntPtr, length: int)Copy(source: Array[IntPtr], startIndex: int, destination: IntPtr, length: int)Copy(source: IntPtr, destination: Array[int], startIndex: int, length: int)Copy(source: IntPtr, destination: Array[Char], startIndex: int, length: int)Copy(source: IntPtr, destination: Array[Int16], startIndex: int, length: int)Copy(source: IntPtr, destination: Array[Int64], startIndex: int, length: int)Copy(source: IntPtr, destination: Array[Single], startIndex: int, length: int)Copy(source: IntPtr, destination: Array[float], startIndex: int, length: int)Copy(source: IntPtr, destination: Array[Byte], startIndex: int, length: int)Copy(source: IntPtr, destination: Array[IntPtr], startIndex: int, length: int) """
        ...

    @staticmethod
    def CreateAggregatedObject(pOuter:IntPtr, o:object) -> IntPtr:
        """
        CreateAggregatedObject(pOuter: IntPtr, o: object) -> IntPtr
        CreateAggregatedObject[T](pOuter: IntPtr, o: T) -> IntPtr
        """
        ...

    @staticmethod
    def CreateWrapperOfType(o:object, t:Type = ...) -> object:
        """
        CreateWrapperOfType(o: object, t: Type) -> object
        CreateWrapperOfType[(T, TWrapper)](o: T) -> TWrapper
        """
        ...

    @staticmethod
    def DestroyStructure(ptr:IntPtr, structuretype:Type = ...): # -> 
        """ DestroyStructure[T](ptr: IntPtr)DestroyStructure(ptr: IntPtr, structuretype: Type) """
        ...

    @staticmethod
    def FinalReleaseComObject(o:object) -> int:
        """ FinalReleaseComObject(o: object) -> int """
        ...

    @staticmethod
    def FreeBSTR(ptr:IntPtr): # -> 
        """ FreeBSTR(ptr: IntPtr) """
        ...

    @staticmethod
    def FreeCoTaskMem(ptr:IntPtr): # -> 
        """ FreeCoTaskMem(ptr: IntPtr) """
        ...

    @staticmethod
    def FreeHGlobal(hglobal:IntPtr): # -> 
        """ FreeHGlobal(hglobal: IntPtr) """
        ...

    @staticmethod
    def GenerateGuidForType(type:Type) -> Guid:
        """ GenerateGuidForType(type: Type) -> Guid """
        ...

    @staticmethod
    def GenerateProgIdForType(type:Type) -> str:
        """ GenerateProgIdForType(type: Type) -> str """
        ...

    @staticmethod
    def GetActiveObject(progID:str) -> object:
        """ GetActiveObject(progID: str) -> object """
        ...

    @staticmethod
    def GetComInterfaceForObject(o:object, T:Type = ..., mode:CustomQueryInterfaceMode = ...) -> IntPtr:
        """
        GetComInterfaceForObject(o: object, T: Type) -> IntPtr
        GetComInterfaceForObject(o: object, T: Type, mode: CustomQueryInterfaceMode) -> IntPtr
        GetComInterfaceForObject[(T, TInterface)](o: T) -> IntPtr
        """
        ...

    @staticmethod
    def GetComInterfaceForObjectInContext(o:object, t:Type) -> IntPtr:
        """ GetComInterfaceForObjectInContext(o: object, t: Type) -> IntPtr """
        ...

    @staticmethod
    def GetComObjectData(obj:object, key:object) -> object:
        """ GetComObjectData(obj: object, key: object) -> object """
        ...

    @staticmethod
    def GetComSlotForMethodInfo(m:MemberInfo) -> int:
        """ GetComSlotForMethodInfo(m: MemberInfo) -> int """
        ...

    @staticmethod
    def GetDelegateForFunctionPointer(ptr:IntPtr, t:Type = ...) -> Delegate:
        """
        GetDelegateForFunctionPointer(ptr: IntPtr, t: Type) -> Delegate
        GetDelegateForFunctionPointer[TDelegate](ptr: IntPtr) -> TDelegate
        """
        ...

    @staticmethod
    def GetEndComSlot(t:Type) -> int:
        """ GetEndComSlot(t: Type) -> int """
        ...

    @staticmethod
    def GetExceptionCode() -> int:
        """ GetExceptionCode() -> int """
        ...

    @staticmethod
    def GetExceptionForHR(errorCode:int, errorInfo:IntPtr = ...) -> Exception:
        """
        GetExceptionForHR(errorCode: int) -> Exception
        GetExceptionForHR(errorCode: int, errorInfo: IntPtr) -> Exception
        """
        ...

    @staticmethod
    def GetExceptionPointers() -> IntPtr:
        """ GetExceptionPointers() -> IntPtr """
        ...

    @staticmethod
    def GetFunctionPointerForDelegate(d:Delegate) -> IntPtr:
        """
        GetFunctionPointerForDelegate(d: Delegate) -> IntPtr
        GetFunctionPointerForDelegate[TDelegate](d: TDelegate) -> IntPtr
        """
        ...

    @staticmethod
    def GetHINSTANCE(m:Module) -> IntPtr:
        """ GetHINSTANCE(m: Module) -> IntPtr """
        ...

    @staticmethod
    def GetHRForException(e:Exception) -> int:
        """ GetHRForException(e: Exception) -> int """
        ...

    @staticmethod
    def GetHRForLastWin32Error() -> int:
        """ GetHRForLastWin32Error() -> int """
        ...

    @staticmethod
    def GetIDispatchForObject(o:object) -> IntPtr:
        """ GetIDispatchForObject(o: object) -> IntPtr """
        ...

    @staticmethod
    def GetIDispatchForObjectInContext(o:object) -> IntPtr:
        """ GetIDispatchForObjectInContext(o: object) -> IntPtr """
        ...

    @staticmethod
    def GetITypeInfoForType(t:Type) -> IntPtr:
        """ GetITypeInfoForType(t: Type) -> IntPtr """
        ...

    @staticmethod
    def GetIUnknownForObject(o:object) -> IntPtr:
        """ GetIUnknownForObject(o: object) -> IntPtr """
        ...

    @staticmethod
    def GetIUnknownForObjectInContext(o:object) -> IntPtr:
        """ GetIUnknownForObjectInContext(o: object) -> IntPtr """
        ...

    @staticmethod
    def GetLastWin32Error() -> int:
        """ GetLastWin32Error() -> int """
        ...

    @staticmethod
    def GetManagedThunkForUnmanagedMethodPtr(pfnMethodToWrap:IntPtr, pbSignature:IntPtr, cbSignature:int) -> IntPtr:
        """ GetManagedThunkForUnmanagedMethodPtr(pfnMethodToWrap: IntPtr, pbSignature: IntPtr, cbSignature: int) -> IntPtr """
        ...

    @staticmethod
    def GetMethodInfoForComSlot(t:Type, slot:int, memberType:ComMemberType) -> Tuple_[MemberInfo, ComMemberType]:
        """ GetMethodInfoForComSlot(t: Type, slot: int, memberType: ComMemberType) -> (MemberInfo, ComMemberType) """
        ...

    @staticmethod
    def GetNativeVariantForObject(obj:object, pDstNativeVariant:IntPtr): # -> 
        """ GetNativeVariantForObject(obj: object, pDstNativeVariant: IntPtr)GetNativeVariantForObject[T](obj: T, pDstNativeVariant: IntPtr) """
        ...

    @staticmethod
    def GetObjectForIUnknown(pUnk:IntPtr) -> object:
        """ GetObjectForIUnknown(pUnk: IntPtr) -> object """
        ...

    @staticmethod
    def GetObjectForNativeVariant(pSrcNativeVariant:IntPtr) -> object:
        """
        GetObjectForNativeVariant(pSrcNativeVariant: IntPtr) -> object
        GetObjectForNativeVariant[T](pSrcNativeVariant: IntPtr) -> T
        """
        ...

    @staticmethod
    def GetObjectsForNativeVariants(aSrcNativeVariant:IntPtr, cVars:int) -> Array:
        """
        GetObjectsForNativeVariants(aSrcNativeVariant: IntPtr, cVars: int) -> Array[object]
        GetObjectsForNativeVariants[T](aSrcNativeVariant: IntPtr, cVars: int) -> Array[T]
        """
        ...

    @staticmethod
    def GetStartComSlot(t:Type) -> int:
        """ GetStartComSlot(t: Type) -> int """
        ...

    @staticmethod
    def GetThreadFromFiberCookie(cookie:int) -> Thread:
        """ GetThreadFromFiberCookie(cookie: int) -> Thread """
        ...

    @staticmethod
    def GetTypedObjectForIUnknown(pUnk:IntPtr, t:Type) -> object:
        """ GetTypedObjectForIUnknown(pUnk: IntPtr, t: Type) -> object """
        ...

    @staticmethod
    def GetTypeForITypeInfo(piTypeInfo:IntPtr) -> Type:
        """ GetTypeForITypeInfo(piTypeInfo: IntPtr) -> Type """
        ...

    @staticmethod
    def GetTypeFromCLSID(clsid:Guid) -> Type:
        """ GetTypeFromCLSID(clsid: Guid) -> Type """
        ...

    @staticmethod
    def GetTypeInfoName(*__args:UCOMITypeInfo) -> str:
        """
        GetTypeInfoName(pTI: UCOMITypeInfo) -> str
        GetTypeInfoName(typeInfo: ITypeInfo) -> str
        """
        ...

    @staticmethod
    def GetTypeLibGuid(*__args:UCOMITypeLib) -> Guid:
        """
        GetTypeLibGuid(pTLB: UCOMITypeLib) -> Guid
        GetTypeLibGuid(typelib: ITypeLib) -> Guid
        """
        ...

    @staticmethod
    def GetTypeLibGuidForAssembly(asm:Assembly) -> Guid:
        """ GetTypeLibGuidForAssembly(asm: Assembly) -> Guid """
        ...

    @staticmethod
    def GetTypeLibLcid(*__args:UCOMITypeLib) -> int:
        """
        GetTypeLibLcid(pTLB: UCOMITypeLib) -> int
        GetTypeLibLcid(typelib: ITypeLib) -> int
        """
        ...

    @staticmethod
    def GetTypeLibName(*__args:UCOMITypeLib) -> str:
        """
        GetTypeLibName(pTLB: UCOMITypeLib) -> str
        GetTypeLibName(typelib: ITypeLib) -> str
        """
        ...

    @staticmethod
    def GetTypeLibVersionForAssembly(inputAssembly, majorVersion, minorVersion) -> Tuple_[int, int]:
        """ GetTypeLibVersionForAssembly(inputAssembly: Assembly) -> (int, int) """
        ...

    @staticmethod
    def GetUniqueObjectForIUnknown(unknown:IntPtr) -> object:
        """ GetUniqueObjectForIUnknown(unknown: IntPtr) -> object """
        ...

    @staticmethod
    def GetUnmanagedThunkForManagedMethodPtr(pfnMethodToWrap:IntPtr, pbSignature:IntPtr, cbSignature:int) -> IntPtr:
        """ GetUnmanagedThunkForManagedMethodPtr(pfnMethodToWrap: IntPtr, pbSignature: IntPtr, cbSignature: int) -> IntPtr """
        ...

    @staticmethod
    def IsComObject(o:object) -> bool:
        """ IsComObject(o: object) -> bool """
        ...

    @staticmethod
    def IsTypeVisibleFromCom(t:Type) -> bool:
        """ IsTypeVisibleFromCom(t: Type) -> bool """
        ...

    @staticmethod
    def NumParamBytes(m:MethodInfo) -> int:
        """ NumParamBytes(m: MethodInfo) -> int """
        ...

    @staticmethod
    def OffsetOf(*__args:str) -> IntPtr:
        """
        OffsetOf(t: Type, fieldName: str) -> IntPtr
        OffsetOf[T](fieldName: str) -> IntPtr
        """
        ...

    @staticmethod
    def Prelink(m:MethodInfo): # -> 
        """ Prelink(m: MethodInfo) """
        ...

    @staticmethod
    def PrelinkAll(c:Type): # -> 
        """ PrelinkAll(c: Type) """
        ...

    @staticmethod
    def PtrToStringAnsi(ptr:IntPtr, len:int = ...) -> str:
        """
        PtrToStringAnsi(ptr: IntPtr) -> str
        PtrToStringAnsi(ptr: IntPtr, len: int) -> str
        """
        ...

    @staticmethod
    def PtrToStringAuto(ptr:IntPtr, len:int = ...) -> str:
        """
        PtrToStringAuto(ptr: IntPtr, len: int) -> str
        PtrToStringAuto(ptr: IntPtr) -> str
        """
        ...

    @staticmethod
    def PtrToStringBSTR(ptr:IntPtr) -> str:
        """ PtrToStringBSTR(ptr: IntPtr) -> str """
        ...

    @staticmethod
    def PtrToStringUni(ptr:IntPtr, len:int = ...) -> str:
        """
        PtrToStringUni(ptr: IntPtr, len: int) -> str
        PtrToStringUni(ptr: IntPtr) -> str
        """
        ...

    @staticmethod
    def PtrToStructure(ptr:IntPtr, *__args:object): # -> 
        """
        PtrToStructure(ptr: IntPtr, structure: object)PtrToStructure(ptr: IntPtr, structureType: Type) -> object
        PtrToStructure[T](ptr: IntPtr, structure: T)PtrToStructure[T](ptr: IntPtr) -> T
        """
        ...

    @staticmethod
    def QueryInterface(pUnk, iid, ppv) -> Tuple_[int, Guid, IntPtr]:
        """ QueryInterface(pUnk: IntPtr, iid: Guid) -> (int, Guid, IntPtr) """
        ...

    @staticmethod
    def ReadByte(ptr:IntPtr, ofs:int = ...) -> Byte:
        """
        ReadByte(ptr: IntPtr, ofs: int) -> Byte
        ReadByte(ptr: IntPtr) -> Byte
        ReadByte(ptr: object, ofs: int) -> Byte
        """
        ...

    @staticmethod
    def ReadInt16(ptr:IntPtr, ofs:int = ...) -> Int16:
        """
        ReadInt16(ptr: IntPtr, ofs: int) -> Int16
        ReadInt16(ptr: IntPtr) -> Int16
        ReadInt16(ptr: object, ofs: int) -> Int16
        """
        ...

    @staticmethod
    def ReadInt32(ptr:IntPtr, ofs:int = ...) -> int:
        """
        ReadInt32(ptr: IntPtr, ofs: int) -> int
        ReadInt32(ptr: IntPtr) -> int
        ReadInt32(ptr: object, ofs: int) -> int
        """
        ...

    @staticmethod
    def ReadInt64(ptr:IntPtr, ofs:int = ...) -> Int64:
        """
        ReadInt64(ptr: IntPtr, ofs: int) -> Int64
        ReadInt64(ptr: IntPtr) -> Int64
        ReadInt64(ptr: object, ofs: int) -> Int64
        """
        ...

    @staticmethod
    def ReadIntPtr(ptr:object, ofs:int = ...) -> IntPtr:
        """
        ReadIntPtr(ptr: object, ofs: int) -> IntPtr
        ReadIntPtr(ptr: IntPtr, ofs: int) -> IntPtr
        ReadIntPtr(ptr: IntPtr) -> IntPtr
        """
        ...

    @staticmethod
    def ReAllocCoTaskMem(pv:IntPtr, cb:int) -> IntPtr:
        """ ReAllocCoTaskMem(pv: IntPtr, cb: int) -> IntPtr """
        ...

    @staticmethod
    def ReAllocHGlobal(pv:IntPtr, cb:IntPtr) -> IntPtr:
        """ ReAllocHGlobal(pv: IntPtr, cb: IntPtr) -> IntPtr """
        ...

    @staticmethod
    def Release(pUnk:IntPtr) -> int:
        """ Release(pUnk: IntPtr) -> int """
        ...

    @staticmethod
    def ReleaseComObject(o:object) -> int:
        """ ReleaseComObject(o: object) -> int """
        ...

    @staticmethod
    def ReleaseThreadCache(): # -> 
        """ ReleaseThreadCache() """
        ...

    @staticmethod
    def SecureStringToBSTR(s:SecureString) -> IntPtr:
        """ SecureStringToBSTR(s: SecureString) -> IntPtr """
        ...

    @staticmethod
    def SecureStringToCoTaskMemAnsi(s:SecureString) -> IntPtr:
        """ SecureStringToCoTaskMemAnsi(s: SecureString) -> IntPtr """
        ...

    @staticmethod
    def SecureStringToCoTaskMemUnicode(s:SecureString) -> IntPtr:
        """ SecureStringToCoTaskMemUnicode(s: SecureString) -> IntPtr """
        ...

    @staticmethod
    def SecureStringToGlobalAllocAnsi(s:SecureString) -> IntPtr:
        """ SecureStringToGlobalAllocAnsi(s: SecureString) -> IntPtr """
        ...

    @staticmethod
    def SecureStringToGlobalAllocUnicode(s:SecureString) -> IntPtr:
        """ SecureStringToGlobalAllocUnicode(s: SecureString) -> IntPtr """
        ...

    @staticmethod
    def SetComObjectData(obj:object, key:object, data:object) -> bool:
        """ SetComObjectData(obj: object, key: object, data: object) -> bool """
        ...

    @staticmethod
    def SizeOf(*__args:object) -> int:
        """
        SizeOf(structure: object) -> int
        SizeOf(t: Type) -> int
        SizeOf[T](structure: T) -> int
        SizeOf[T]() -> int
        """
        ...

    @staticmethod
    def StringToBSTR(s:str) -> IntPtr:
        """ StringToBSTR(s: str) -> IntPtr """
        ...

    @staticmethod
    def StringToCoTaskMemAnsi(s:str) -> IntPtr:
        """ StringToCoTaskMemAnsi(s: str) -> IntPtr """
        ...

    @staticmethod
    def StringToCoTaskMemAuto(s:str) -> IntPtr:
        """ StringToCoTaskMemAuto(s: str) -> IntPtr """
        ...

    @staticmethod
    def StringToCoTaskMemUni(s:str) -> IntPtr:
        """ StringToCoTaskMemUni(s: str) -> IntPtr """
        ...

    @staticmethod
    def StringToHGlobalAnsi(s:str) -> IntPtr:
        """ StringToHGlobalAnsi(s: str) -> IntPtr """
        ...

    @staticmethod
    def StringToHGlobalAuto(s:str) -> IntPtr:
        """ StringToHGlobalAuto(s: str) -> IntPtr """
        ...

    @staticmethod
    def StringToHGlobalUni(s:str) -> IntPtr:
        """ StringToHGlobalUni(s: str) -> IntPtr """
        ...

    @staticmethod
    def StructureToPtr(structure, ptr:IntPtr, fDeleteOld:bool): # ->  # Not found arg types: {'structure': 'T'}
        """ StructureToPtr[T](structure: T, ptr: IntPtr, fDeleteOld: bool)StructureToPtr(structure: object, ptr: IntPtr, fDeleteOld: bool) """
        ...

    @staticmethod
    def ThrowExceptionForHR(errorCode:int, errorInfo:IntPtr = ...): # -> 
        """ ThrowExceptionForHR(errorCode: int)ThrowExceptionForHR(errorCode: int, errorInfo: IntPtr) """
        ...

    @staticmethod
    def UnsafeAddrOfPinnedArrayElement(arr:Array, index:int) -> IntPtr:
        """
        UnsafeAddrOfPinnedArrayElement[T](arr: Array[T], index: int) -> IntPtr
        UnsafeAddrOfPinnedArrayElement(arr: Array, index: int) -> IntPtr
        """
        ...

    @staticmethod
    def WriteByte(ptr:IntPtr, *__args:Byte): # -> 
        """ WriteByte(ptr: IntPtr, ofs: int, val: Byte)WriteByte(ptr: IntPtr, val: Byte)WriteByte(ofs: int, val: Byte) -> object """
        ...

    @staticmethod
    def WriteInt16(ptr:IntPtr, *__args:Int16): # -> 
        """
        WriteInt16(ptr: IntPtr, ofs: int, val: Int16)WriteInt16(ptr: IntPtr, val: Int16)WriteInt16(ptr: IntPtr, ofs: int, val: Char)WriteInt16(ofs: int, val: Char) -> object
        WriteInt16(ptr: IntPtr, val: Char)WriteInt16(ofs: int, val: Int16) -> object
        """
        ...

    @staticmethod
    def WriteInt32(ptr:IntPtr, *__args:int): # -> 
        """ WriteInt32(ptr: IntPtr, ofs: int, val: int)WriteInt32(ptr: IntPtr, val: int)WriteInt32(ofs: int, val: int) -> object """
        ...

    @staticmethod
    def WriteInt64(ptr:IntPtr, *__args:Int64): # -> 
        """ WriteInt64(ptr: IntPtr, ofs: int, val: Int64)WriteInt64(ptr: IntPtr, val: Int64)WriteInt64(ofs: int, val: Int64) -> object """
        ...

    @staticmethod
    def WriteIntPtr(ptr:int, *__args:IntPtr) -> object:
        """
        WriteIntPtr(ptr: IntPtr, ofs: int, val: IntPtr)WriteIntPtr(ofs: int, val: IntPtr) -> object
        WriteIntPtr(ptr: IntPtr, val: IntPtr)
        """
        ...

    @staticmethod
    def ZeroFreeBSTR(s:IntPtr): # -> 
        """ ZeroFreeBSTR(s: IntPtr) """
        ...

    @staticmethod
    def ZeroFreeCoTaskMemAnsi(s:IntPtr): # -> 
        """ ZeroFreeCoTaskMemAnsi(s: IntPtr) """
        ...

    @staticmethod
    def ZeroFreeCoTaskMemUnicode(s:IntPtr): # -> 
        """ ZeroFreeCoTaskMemUnicode(s: IntPtr) """
        ...

    @staticmethod
    def ZeroFreeGlobalAllocAnsi(s:IntPtr): # -> 
        """ ZeroFreeGlobalAllocAnsi(s: IntPtr) """
        ...

    @staticmethod
    def ZeroFreeGlobalAllocUnicode(s:IntPtr): # -> 
        """ ZeroFreeGlobalAllocUnicode(s: IntPtr) """
        ...

    SystemDefaultCharSize: int = ...
    SystemMaxDBCSCharSize: int = ...
    __all__: list = ...


class MarshalAsAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    MarshalAsAttribute(unmanagedType: UnmanagedType)
    MarshalAsAttribute(unmanagedType: Int16)
    """
    @property
    def Value(self) -> UnmanagedType:
        """ Get: Value(self: MarshalAsAttribute) -> UnmanagedType """
        ...


    def __new__(cls, unmanagedType:UnmanagedType) -> Self:
        """
        __new__(cls: type, unmanagedType: UnmanagedType)
        __new__(cls: type, unmanagedType: Int16)
        """
        ...

    ArraySubType = ...
    IidParameterIndex = ...
    MarshalCookie = ...
    MarshalType = ...
    MarshalTypeRef = ...
    SafeArraySubType = ...
    SafeArrayUserDefinedSubType = ...
    SizeConst = ...
    SizeParamIndex = ...


class MarshalDirectiveException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    MarshalDirectiveException()
    MarshalDirectiveException(message: str)
    MarshalDirectiveException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class ObjectCreationDelegate(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ObjectCreationDelegate(object: object, method: IntPtr) """
    def BeginInvoke(self, aggregator:IntPtr, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ObjectCreationDelegate, aggregator: IntPtr, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> IntPtr:
        """ EndInvoke(self: ObjectCreationDelegate, result: IAsyncResult) -> IntPtr """
        ...

    def Invoke(self, aggregator:IntPtr) -> IntPtr:
        """ Invoke(self: ObjectCreationDelegate, aggregator: IntPtr) -> IntPtr """
        ...


class OptionalAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ OptionalAttribute() """
    pass

class OSPlatform(IEquatable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Linux(self) -> OSPlatform:
        """ Get: Linux() -> OSPlatform """
        ...

    @property
    def OSX(self) -> OSPlatform:
        """ Get: OSX() -> OSPlatform """
        ...

    @property
    def Windows(self) -> OSPlatform:
        """ Get: Windows() -> OSPlatform """
        ...


    @staticmethod
    def Create(osPlatform:str) -> OSPlatform:
        """ Create(osPlatform: str) -> OSPlatform """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: OSPlatform) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: OSPlatform) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class OutAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ OutAttribute() """
    pass

class PARAMDESC: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    lpVarValue = ...
    wParamFlags = ...


class PARAMFLAG(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PARAMFLAG, values: PARAMFLAG_FHASCUSTDATA (64), PARAMFLAG_FHASDEFAULT (32), PARAMFLAG_FIN (1), PARAMFLAG_FLCID (4), PARAMFLAG_FOPT (16), PARAMFLAG_FOUT (2), PARAMFLAG_FRETVAL (8), PARAMFLAG_NONE (0) """
    PARAMFLAG_FHASCUSTDATA: PARAMFLAG = ...
    PARAMFLAG_FHASDEFAULT: PARAMFLAG = ...
    PARAMFLAG_FIN: PARAMFLAG = ...
    PARAMFLAG_FLCID: PARAMFLAG = ...
    PARAMFLAG_FOPT: PARAMFLAG = ...
    PARAMFLAG_FOUT: PARAMFLAG = ...
    PARAMFLAG_FRETVAL: PARAMFLAG = ...
    PARAMFLAG_NONE: PARAMFLAG = ...
    value__ = ...


class PreserveSigAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PreserveSigAttribute() """
    pass

class PrimaryInteropAssemblyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PrimaryInteropAssemblyAttribute(major: int, minor: int) """
    @property
    def MajorVersion(self) -> int:
        """ Get: MajorVersion(self: PrimaryInteropAssemblyAttribute) -> int """
        ...

    @property
    def MinorVersion(self) -> int:
        """ Get: MinorVersion(self: PrimaryInteropAssemblyAttribute) -> int """
        ...


    def __new__(cls, major:int, minor:int) -> Self:
        """ __new__(cls: type, major: int, minor: int) """
        ...


class ProgIdAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ProgIdAttribute(progId: str) """
    @property
    def Value(self) -> str:
        """ Get: Value(self: ProgIdAttribute) -> str """
        ...


    def __new__(cls, progId:str) -> Self:
        """ __new__(cls: type, progId: str) """
        ...


class RegistrationClassContext(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) RegistrationClassContext, values: DisableActivateAsActivator (32768), EnableActivateAsActivator (65536), EnableCodeDownload (8192), FromDefaultContext (131072), InProcessHandler (2), InProcessHandler16 (32), InProcessServer (1), InProcessServer16 (8), LocalServer (4), NoCodeDownload (1024), NoCustomMarshal (4096), NoFailureLog (16384), RemoteServer (16), Reserved1 (64), Reserved2 (128), Reserved3 (256), Reserved4 (512), Reserved5 (2048) """
    DisableActivateAsActivator: RegistrationClassContext = ...
    EnableActivateAsActivator: RegistrationClassContext = ...
    EnableCodeDownload: RegistrationClassContext = ...
    FromDefaultContext: RegistrationClassContext = ...
    InProcessHandler: RegistrationClassContext = ...
    InProcessHandler16: RegistrationClassContext = ...
    InProcessServer: RegistrationClassContext = ...
    InProcessServer16: RegistrationClassContext = ...
    LocalServer: RegistrationClassContext = ...
    NoCodeDownload: RegistrationClassContext = ...
    NoCustomMarshal: RegistrationClassContext = ...
    NoFailureLog: RegistrationClassContext = ...
    RemoteServer: RegistrationClassContext = ...
    Reserved1: RegistrationClassContext = ...
    Reserved2: RegistrationClassContext = ...
    Reserved3: RegistrationClassContext = ...
    Reserved4: RegistrationClassContext = ...
    Reserved5: RegistrationClassContext = ...
    value__ = ...


class RegistrationConnectionType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) RegistrationConnectionType, values: MultipleUse (1), MultiSeparate (2), SingleUse (0), Surrogate (8), Suspended (4) """
    MultipleUse: RegistrationConnectionType = ...
    MultiSeparate: RegistrationConnectionType = ...
    SingleUse: RegistrationConnectionType = ...
    Surrogate: RegistrationConnectionType = ...
    Suspended: RegistrationConnectionType = ...
    value__ = ...


class RegistrationServices(IRegistrationServices): # skipped bases: <type 'object'>
    """ RegistrationServices() """
    def UnregisterTypeForComClients(self, cookie:int): # -> 
        """ UnregisterTypeForComClients(self: RegistrationServices, cookie: int) """
        ...


class RuntimeEnvironment: # skipped bases: <type 'object'>, <type 'object'>
    """ RuntimeEnvironment() """
    @property
    def SystemConfigurationFile(self) -> str:
        """ Get: SystemConfigurationFile() -> str """
        ...


    @staticmethod
    def FromGlobalAccessCache(a:Assembly) -> bool:
        """ FromGlobalAccessCache(a: Assembly) -> bool """
        ...

    @staticmethod
    def GetRuntimeDirectory() -> str:
        """ GetRuntimeDirectory() -> str """
        ...

    @staticmethod
    def GetRuntimeInterfaceAsIntPtr(clsid:Guid, riid:Guid) -> IntPtr:
        """ GetRuntimeInterfaceAsIntPtr(clsid: Guid, riid: Guid) -> IntPtr """
        ...

    @staticmethod
    def GetRuntimeInterfaceAsObject(clsid:Guid, riid:Guid) -> object:
        """ GetRuntimeInterfaceAsObject(clsid: Guid, riid: Guid) -> object """
        ...

    @staticmethod
    def GetSystemVersion() -> str:
        """ GetSystemVersion() -> str """
        ...



class RuntimeInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def FrameworkDescription(self) -> str:
        """ Get: FrameworkDescription() -> str """
        ...

    @property
    def OSArchitecture(self) -> Architecture:
        """ Get: OSArchitecture() -> Architecture """
        ...

    @property
    def OSDescription(self) -> str:
        """ Get: OSDescription() -> str """
        ...

    @property
    def ProcessArchitecture(self) -> Architecture:
        """ Get: ProcessArchitecture() -> Architecture """
        ...


    @staticmethod
    def IsOSPlatform(osPlatform:OSPlatform) -> bool:
        """ IsOSPlatform(osPlatform: OSPlatform) -> bool """
        ...

    __all__: list = ...


class SafeArrayRankMismatchException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SafeArrayRankMismatchException()
    SafeArrayRankMismatchException(message: str)
    SafeArrayRankMismatchException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class SafeArrayTypeMismatchException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SafeArrayTypeMismatchException()
    SafeArrayTypeMismatchException(message: str)
    SafeArrayTypeMismatchException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class SafeHandle(IDisposable, CriticalFinalizerObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsClosed(self) -> bool:
        """ Get: IsClosed(self: SafeHandle) -> bool """
        ...

    @property
    def IsInvalid(self) -> bool:
        """ Get: IsInvalid(self: SafeHandle) -> bool """
        ...


    def Close(self): # -> 
        """ Close(self: SafeHandle) """
        ...

    def DangerousAddRef(self, success:bool) -> bool:
        """ DangerousAddRef(self: SafeHandle, success: bool) -> bool """
        ...

    def DangerousGetHandle(self) -> IntPtr:
        """ DangerousGetHandle(self: SafeHandle) -> IntPtr """
        ...

    def DangerousRelease(self): # -> 
        """ DangerousRelease(self: SafeHandle) """
        ...

    def ReleaseHandle(self, *args): #cannot find CLR method
        """ ReleaseHandle(self: SafeHandle) -> bool """
        ...

    def SetHandle(self, *args): #cannot find CLR method
        """ SetHandle(self: SafeHandle, handle: IntPtr) """
        ...

    def SetHandleAsInvalid(self): # -> 
        """ SetHandleAsInvalid(self: SafeHandle) """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, invalidHandleValue: IntPtr, ownsHandle: bool) """
        ...

    handle = ...


class SafeBuffer(SafeHandleZeroOrMinusOneIsInvalid): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def ByteLength(self) -> UInt64:
        """ Get: ByteLength(self: SafeBuffer) -> UInt64 """
        ...


    def AcquirePointer(self, pointer:Byte) -> Byte:
        """ AcquirePointer(self: SafeBuffer, pointer: Byte*) -> Byte* """
        ...

    def Initialize(self, *__args:UInt64): # -> 
        """ Initialize(self: SafeBuffer, numBytes: UInt64)Initialize(self: SafeBuffer, numElements: UInt32, sizeOfEachElement: UInt32)Initialize[T](self: SafeBuffer, numElements: UInt32) """
        ...

    def Read(self, byteOffset:UInt64): # -> T
        """ Read[T](self: SafeBuffer, byteOffset: UInt64) -> T """
        ...

    def ReadArray(self, byteOffset:UInt64, array:Array, index:int, count:int): # -> 
        """ ReadArray[T](self: SafeBuffer, byteOffset: UInt64, array: Array[T], index: int, count: int) """
        ...

    def ReleasePointer(self): # -> 
        """ ReleasePointer(self: SafeBuffer) """
        ...

    def Write(self, byteOffset:UInt64, value): # ->  # Not found arg types: {'value': 'T'}
        """ Write[T](self: SafeBuffer, byteOffset: UInt64, value: T) """
        ...

    def WriteArray(self, byteOffset:UInt64, array:Array, index:int, count:int): # -> 
        """ WriteArray[T](self: SafeBuffer, byteOffset: UInt64, array: Array[T], index: int, count: int) """
        ...

    handle = ...


class SEHException(ExternalException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SEHException()
    SEHException(message: str)
    SEHException(message: str, inner: Exception)
    """
    def CanResume(self) -> bool:
        """ CanResume(self: SEHException) -> bool """
        ...

    SerializeObjectState = ...


class SetWin32ContextInIDispatchAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SetWin32ContextInIDispatchAttribute() """
    pass

class StandardOleMarshalObject(MarshalByRefObject, IMarshal): # skipped bases: <type 'object'>
    """ no doc """
    pass

class STATSTG: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    atime = ...
    cbSize = ...
    clsid = ...
    ctime = ...
    grfLocksSupported = ...
    grfMode = ...
    grfStateBits = ...
    mtime = ...
    pwcsName = ...
    reserved = ...
    type = ...


class StructLayoutAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    StructLayoutAttribute(layoutKind: LayoutKind)
    StructLayoutAttribute(layoutKind: Int16)
    """
    @property
    def Value(self) -> LayoutKind:
        """ Get: Value(self: StructLayoutAttribute) -> LayoutKind """
        ...


    def __new__(cls, layoutKind:LayoutKind) -> Self:
        """
        __new__(cls: type, layoutKind: LayoutKind)
        __new__(cls: type, layoutKind: Int16)
        """
        ...

    CharSet = ...
    Pack = ...
    Size = ...


class SYSKIND(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SYSKIND, values: SYS_MAC (2), SYS_WIN16 (0), SYS_WIN32 (1) """
    SYS_MAC: SYSKIND = ...
    SYS_WIN16: SYSKIND = ...
    SYS_WIN32: SYSKIND = ...
    value__ = ...


class TYPEATTR: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    cbAlignment = ...
    cbSizeInstance = ...
    cbSizeVft = ...
    cFuncs = ...
    cImplTypes = ...
    cVars = ...
    dwReserved = ...
    guid = ...
    idldescType = ...
    lcid = ...
    lpstrSchema = ...
    MEMBER_ID_NIL: int = ...
    memidConstructor = ...
    memidDestructor = ...
    tdescAlias = ...
    typekind = ...
    wMajorVerNum = ...
    wMinorVerNum = ...
    wTypeFlags = ...


class TYPEDESC: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    lpValue = ...
    vt = ...


class TYPEFLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TYPEFLAGS, values: TYPEFLAG_FAGGREGATABLE (1024), TYPEFLAG_FAPPOBJECT (1), TYPEFLAG_FCANCREATE (2), TYPEFLAG_FCONTROL (32), TYPEFLAG_FDISPATCHABLE (4096), TYPEFLAG_FDUAL (64), TYPEFLAG_FHIDDEN (16), TYPEFLAG_FLICENSED (4), TYPEFLAG_FNONEXTENSIBLE (128), TYPEFLAG_FOLEAUTOMATION (256), TYPEFLAG_FPREDECLID (8), TYPEFLAG_FPROXY (16384), TYPEFLAG_FREPLACEABLE (2048), TYPEFLAG_FRESTRICTED (512), TYPEFLAG_FREVERSEBIND (8192) """
    TYPEFLAG_FAGGREGATABLE: TYPEFLAGS = ...
    TYPEFLAG_FAPPOBJECT: TYPEFLAGS = ...
    TYPEFLAG_FCANCREATE: TYPEFLAGS = ...
    TYPEFLAG_FCONTROL: TYPEFLAGS = ...
    TYPEFLAG_FDISPATCHABLE: TYPEFLAGS = ...
    TYPEFLAG_FDUAL: TYPEFLAGS = ...
    TYPEFLAG_FHIDDEN: TYPEFLAGS = ...
    TYPEFLAG_FLICENSED: TYPEFLAGS = ...
    TYPEFLAG_FNONEXTENSIBLE: TYPEFLAGS = ...
    TYPEFLAG_FOLEAUTOMATION: TYPEFLAGS = ...
    TYPEFLAG_FPREDECLID: TYPEFLAGS = ...
    TYPEFLAG_FPROXY: TYPEFLAGS = ...
    TYPEFLAG_FREPLACEABLE: TYPEFLAGS = ...
    TYPEFLAG_FRESTRICTED: TYPEFLAGS = ...
    TYPEFLAG_FREVERSEBIND: TYPEFLAGS = ...
    value__ = ...


class TypeIdentifierAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    TypeIdentifierAttribute()
    TypeIdentifierAttribute(scope: str, identifier: str)
    """
    @property
    def Identifier(self) -> str:
        """ Get: Identifier(self: TypeIdentifierAttribute) -> str """
        ...

    @property
    def Scope(self) -> str:
        """ Get: Scope(self: TypeIdentifierAttribute) -> str """
        ...


    def __new__(cls, scope:str = ..., identifier:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, scope: str, identifier: str)
        """
        ...


class TYPEKIND(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TYPEKIND, values: TKIND_ALIAS (6), TKIND_COCLASS (5), TKIND_DISPATCH (4), TKIND_ENUM (0), TKIND_INTERFACE (3), TKIND_MAX (8), TKIND_MODULE (2), TKIND_RECORD (1), TKIND_UNION (7) """
    TKIND_ALIAS: TYPEKIND = ...
    TKIND_COCLASS: TYPEKIND = ...
    TKIND_DISPATCH: TYPEKIND = ...
    TKIND_ENUM: TYPEKIND = ...
    TKIND_INTERFACE: TYPEKIND = ...
    TKIND_MAX: TYPEKIND = ...
    TKIND_MODULE: TYPEKIND = ...
    TKIND_RECORD: TYPEKIND = ...
    TKIND_UNION: TYPEKIND = ...
    value__ = ...


class TYPELIBATTR: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    guid = ...
    lcid = ...
    syskind = ...
    wLibFlags = ...
    wMajorVerNum = ...
    wMinorVerNum = ...


class TypeLibConverter(ITypeLibConverter): # skipped bases: <type 'object'>
    """ TypeLibConverter() """
    pass

class TypeLibExporterFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TypeLibExporterFlags, values: CallerResolvedReferences (2), ExportAs32Bit (16), ExportAs64Bit (32), None (0), OldNames (4), OnlyReferenceRegistered (1) """
    CallerResolvedReferences: TypeLibExporterFlags = ...
    ExportAs32Bit: TypeLibExporterFlags = ...
    ExportAs64Bit: TypeLibExporterFlags = ...
    OldNames: TypeLibExporterFlags = ...
    OnlyReferenceRegistered: TypeLibExporterFlags = ...
    value__ = ...


class TypeLibFuncAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    TypeLibFuncAttribute(flags: TypeLibFuncFlags)
    TypeLibFuncAttribute(flags: Int16)
    """
    @property
    def Value(self) -> TypeLibFuncFlags:
        """ Get: Value(self: TypeLibFuncAttribute) -> TypeLibFuncFlags """
        ...


    def __new__(cls, flags:TypeLibFuncFlags) -> Self:
        """
        __new__(cls: type, flags: TypeLibFuncFlags)
        __new__(cls: type, flags: Int16)
        """
        ...


class TypeLibFuncFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TypeLibFuncFlags, values: FBindable (4), FDefaultBind (32), FDefaultCollelem (256), FDisplayBind (16), FHidden (64), FImmediateBind (4096), FNonBrowsable (1024), FReplaceable (2048), FRequestEdit (8), FRestricted (1), FSource (2), FUiDefault (512), FUsesGetLastError (128) """
    FBindable: TypeLibFuncFlags = ...
    FDefaultBind: TypeLibFuncFlags = ...
    FDefaultCollelem: TypeLibFuncFlags = ...
    FDisplayBind: TypeLibFuncFlags = ...
    FHidden: TypeLibFuncFlags = ...
    FImmediateBind: TypeLibFuncFlags = ...
    FNonBrowsable: TypeLibFuncFlags = ...
    FReplaceable: TypeLibFuncFlags = ...
    FRequestEdit: TypeLibFuncFlags = ...
    FRestricted: TypeLibFuncFlags = ...
    FSource: TypeLibFuncFlags = ...
    FUiDefault: TypeLibFuncFlags = ...
    FUsesGetLastError: TypeLibFuncFlags = ...
    value__ = ...


class TypeLibImportClassAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TypeLibImportClassAttribute(importClass: Type) """
    @property
    def Value(self) -> str:
        """ Get: Value(self: TypeLibImportClassAttribute) -> str """
        ...


    def __new__(cls, importClass:Type) -> Self:
        """ __new__(cls: type, importClass: Type) """
        ...


class TypeLibImporterFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TypeLibImporterFlags, values: ImportAsAgnostic (2048), ImportAsArm (16384), ImportAsItanium (1024), ImportAsX64 (512), ImportAsX86 (256), NoDefineVersionResource (8192), None (0), PreventClassMembers (16), PrimaryInteropAssembly (1), ReflectionOnlyLoading (4096), SafeArrayAsSystemArray (4), SerializableValueClasses (32), TransformDispRetVals (8), UnsafeInterfaces (2) """
    ImportAsAgnostic: TypeLibImporterFlags = ...
    ImportAsArm: TypeLibImporterFlags = ...
    ImportAsItanium: TypeLibImporterFlags = ...
    ImportAsX64: TypeLibImporterFlags = ...
    ImportAsX86: TypeLibImporterFlags = ...
    NoDefineVersionResource: TypeLibImporterFlags = ...
    PreventClassMembers: TypeLibImporterFlags = ...
    PrimaryInteropAssembly: TypeLibImporterFlags = ...
    ReflectionOnlyLoading: TypeLibImporterFlags = ...
    SafeArrayAsSystemArray: TypeLibImporterFlags = ...
    SerializableValueClasses: TypeLibImporterFlags = ...
    TransformDispRetVals: TypeLibImporterFlags = ...
    UnsafeInterfaces: TypeLibImporterFlags = ...
    value__ = ...


class TypeLibTypeAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    TypeLibTypeAttribute(flags: TypeLibTypeFlags)
    TypeLibTypeAttribute(flags: Int16)
    """
    @property
    def Value(self) -> TypeLibTypeFlags:
        """ Get: Value(self: TypeLibTypeAttribute) -> TypeLibTypeFlags """
        ...


    def __new__(cls, flags:TypeLibTypeFlags) -> Self:
        """
        __new__(cls: type, flags: TypeLibTypeFlags)
        __new__(cls: type, flags: Int16)
        """
        ...


class TypeLibTypeFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TypeLibTypeFlags, values: FAggregatable (1024), FAppObject (1), FCanCreate (2), FControl (32), FDispatchable (4096), FDual (64), FHidden (16), FLicensed (4), FNonExtensible (128), FOleAutomation (256), FPreDeclId (8), FReplaceable (2048), FRestricted (512), FReverseBind (8192) """
    FAggregatable: TypeLibTypeFlags = ...
    FAppObject: TypeLibTypeFlags = ...
    FCanCreate: TypeLibTypeFlags = ...
    FControl: TypeLibTypeFlags = ...
    FDispatchable: TypeLibTypeFlags = ...
    FDual: TypeLibTypeFlags = ...
    FHidden: TypeLibTypeFlags = ...
    FLicensed: TypeLibTypeFlags = ...
    FNonExtensible: TypeLibTypeFlags = ...
    FOleAutomation: TypeLibTypeFlags = ...
    FPreDeclId: TypeLibTypeFlags = ...
    FReplaceable: TypeLibTypeFlags = ...
    FRestricted: TypeLibTypeFlags = ...
    FReverseBind: TypeLibTypeFlags = ...
    value__ = ...


class TypeLibVarAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    TypeLibVarAttribute(flags: TypeLibVarFlags)
    TypeLibVarAttribute(flags: Int16)
    """
    @property
    def Value(self) -> TypeLibVarFlags:
        """ Get: Value(self: TypeLibVarAttribute) -> TypeLibVarFlags """
        ...


    def __new__(cls, flags:TypeLibVarFlags) -> Self:
        """
        __new__(cls: type, flags: TypeLibVarFlags)
        __new__(cls: type, flags: Int16)
        """
        ...


class TypeLibVarFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TypeLibVarFlags, values: FBindable (4), FDefaultBind (32), FDefaultCollelem (256), FDisplayBind (16), FHidden (64), FImmediateBind (4096), FNonBrowsable (1024), FReadOnly (1), FReplaceable (2048), FRequestEdit (8), FRestricted (128), FSource (2), FUiDefault (512) """
    FBindable: TypeLibVarFlags = ...
    FDefaultBind: TypeLibVarFlags = ...
    FDefaultCollelem: TypeLibVarFlags = ...
    FDisplayBind: TypeLibVarFlags = ...
    FHidden: TypeLibVarFlags = ...
    FImmediateBind: TypeLibVarFlags = ...
    FNonBrowsable: TypeLibVarFlags = ...
    FReadOnly: TypeLibVarFlags = ...
    FReplaceable: TypeLibVarFlags = ...
    FRequestEdit: TypeLibVarFlags = ...
    FRestricted: TypeLibVarFlags = ...
    FSource: TypeLibVarFlags = ...
    FUiDefault: TypeLibVarFlags = ...
    value__ = ...


class TypeLibVersionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TypeLibVersionAttribute(major: int, minor: int) """
    @property
    def MajorVersion(self) -> int:
        """ Get: MajorVersion(self: TypeLibVersionAttribute) -> int """
        ...

    @property
    def MinorVersion(self) -> int:
        """ Get: MinorVersion(self: TypeLibVersionAttribute) -> int """
        ...


    def __new__(cls, major:int, minor:int) -> Self:
        """ __new__(cls: type, major: int, minor: int) """
        ...


class UCOMIBindCtx: # skipped bases: <type 'object'>
    """ no doc """
    def EnumObjectParam(self, ppenum) -> UCOMIEnumString:
        """ EnumObjectParam(self: UCOMIBindCtx) -> UCOMIEnumString """
        ...

    def GetBindOptions(self, pbindopts:BIND_OPTS) -> BIND_OPTS:
        """ GetBindOptions(self: UCOMIBindCtx, pbindopts: BIND_OPTS) -> BIND_OPTS """
        ...

    def GetObjectParam(self, pszKey, ppunk) -> object:
        """ GetObjectParam(self: UCOMIBindCtx, pszKey: str) -> object """
        ...

    def GetRunningObjectTable(self, pprot) -> UCOMIRunningObjectTable:
        """ GetRunningObjectTable(self: UCOMIBindCtx) -> UCOMIRunningObjectTable """
        ...

    def RegisterObjectBound(self, punk:object): # -> 
        """ RegisterObjectBound(self: UCOMIBindCtx, punk: object) """
        ...

    def RegisterObjectParam(self, pszKey:str, punk:object): # -> 
        """ RegisterObjectParam(self: UCOMIBindCtx, pszKey: str, punk: object) """
        ...

    def ReleaseBoundObjects(self): # -> 
        """ ReleaseBoundObjects(self: UCOMIBindCtx) """
        ...

    def RevokeObjectBound(self, punk:object): # -> 
        """ RevokeObjectBound(self: UCOMIBindCtx, punk: object) """
        ...

    def RevokeObjectParam(self, pszKey:str): # -> 
        """ RevokeObjectParam(self: UCOMIBindCtx, pszKey: str) """
        ...

    def SetBindOptions(self, pbindopts:BIND_OPTS) -> BIND_OPTS:
        """ SetBindOptions(self: UCOMIBindCtx, pbindopts: BIND_OPTS) -> BIND_OPTS """
        ...


class UCOMIConnectionPoint: # skipped bases: <type 'object'>
    """ no doc """
    def Advise(self, pUnkSink, pdwCookie) -> int:
        """ Advise(self: UCOMIConnectionPoint, pUnkSink: object) -> int """
        ...

    def EnumConnections(self, ppEnum) -> UCOMIEnumConnections:
        """ EnumConnections(self: UCOMIConnectionPoint) -> UCOMIEnumConnections """
        ...

    def GetConnectionInterface(self, pIID) -> Guid:
        """ GetConnectionInterface(self: UCOMIConnectionPoint) -> Guid """
        ...

    def GetConnectionPointContainer(self, ppCPC) -> UCOMIConnectionPointContainer:
        """ GetConnectionPointContainer(self: UCOMIConnectionPoint) -> UCOMIConnectionPointContainer """
        ...

    def Unadvise(self, dwCookie:int): # -> 
        """ Unadvise(self: UCOMIConnectionPoint, dwCookie: int) """
        ...


class UCOMIConnectionPointContainer: # skipped bases: <type 'object'>
    """ no doc """
    def EnumConnectionPoints(self, ppEnum) -> UCOMIEnumConnectionPoints:
        """ EnumConnectionPoints(self: UCOMIConnectionPointContainer) -> UCOMIEnumConnectionPoints """
        ...

    def FindConnectionPoint(self, riid, ppCP) -> Tuple_[Guid, UCOMIConnectionPoint]:
        """ FindConnectionPoint(self: UCOMIConnectionPointContainer, riid: Guid) -> (Guid, UCOMIConnectionPoint) """
        ...


class UCOMIEnumConnectionPoints: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppenum) -> UCOMIEnumConnectionPoints:
        """ Clone(self: UCOMIEnumConnectionPoints) -> UCOMIEnumConnectionPoints """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, int]:
        """ Next(self: UCOMIEnumConnectionPoints, celt: int) -> (int, Array[UCOMIConnectionPoint], int) """
        ...

    def Reset(self) -> int:
        """ Reset(self: UCOMIEnumConnectionPoints) -> int """
        ...

    def Skip(self, celt:int) -> int:
        """ Skip(self: UCOMIEnumConnectionPoints, celt: int) -> int """
        ...


class UCOMIEnumConnections: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppenum) -> UCOMIEnumConnections:
        """ Clone(self: UCOMIEnumConnections) -> UCOMIEnumConnections """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, int]:
        """ Next(self: UCOMIEnumConnections, celt: int) -> (int, Array[CONNECTDATA], int) """
        ...

    def Reset(self): # -> 
        """ Reset(self: UCOMIEnumConnections) """
        ...

    def Skip(self, celt:int) -> int:
        """ Skip(self: UCOMIEnumConnections, celt: int) -> int """
        ...


class UCOMIEnumMoniker: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppenum) -> UCOMIEnumMoniker:
        """ Clone(self: UCOMIEnumMoniker) -> UCOMIEnumMoniker """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, int]:
        """ Next(self: UCOMIEnumMoniker, celt: int) -> (int, Array[UCOMIMoniker], int) """
        ...

    def Reset(self) -> int:
        """ Reset(self: UCOMIEnumMoniker) -> int """
        ...

    def Skip(self, celt:int) -> int:
        """ Skip(self: UCOMIEnumMoniker, celt: int) -> int """
        ...


class UCOMIEnumString: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppenum) -> UCOMIEnumString:
        """ Clone(self: UCOMIEnumString) -> UCOMIEnumString """
        ...

    def Next(self, celt, rgelt, pceltFetched) -> Tuple_[int, Array, int]:
        """ Next(self: UCOMIEnumString, celt: int) -> (int, Array[str], int) """
        ...

    def Reset(self) -> int:
        """ Reset(self: UCOMIEnumString) -> int """
        ...

    def Skip(self, celt:int) -> int:
        """ Skip(self: UCOMIEnumString, celt: int) -> int """
        ...


class UCOMIEnumVARIANT: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppenum:int): # -> 
        """ Clone(self: UCOMIEnumVARIANT, ppenum: int) """
        ...

    def Next(self, celt:int, rgvar:int, pceltFetched:int) -> int:
        """ Next(self: UCOMIEnumVARIANT, celt: int, rgvar: int, pceltFetched: int) -> int """
        ...

    def Reset(self) -> int:
        """ Reset(self: UCOMIEnumVARIANT) -> int """
        ...

    def Skip(self, celt:int) -> int:
        """ Skip(self: UCOMIEnumVARIANT, celt: int) -> int """
        ...


class UCOMIMoniker: # skipped bases: <type 'object'>
    """ no doc """
    def BindToObject(self, pbc, pmkToLeft, riidResult, ppvResult) -> Tuple_[Guid, object]:
        """ BindToObject(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, riidResult: Guid) -> (Guid, object) """
        ...

    def BindToStorage(self, pbc, pmkToLeft, riid, ppvObj) -> Tuple_[Guid, object]:
        """ BindToStorage(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, riid: Guid) -> (Guid, object) """
        ...

    def CommonPrefixWith(self, pmkOther, ppmkPrefix) -> UCOMIMoniker:
        """ CommonPrefixWith(self: UCOMIMoniker, pmkOther: UCOMIMoniker) -> UCOMIMoniker """
        ...

    def ComposeWith(self, pmkRight, fOnlyIfNotGeneric, ppmkComposite) -> UCOMIMoniker:
        """ ComposeWith(self: UCOMIMoniker, pmkRight: UCOMIMoniker, fOnlyIfNotGeneric: bool) -> UCOMIMoniker """
        ...

    def Enum(self, fForward, ppenumMoniker) -> UCOMIEnumMoniker:
        """ Enum(self: UCOMIMoniker, fForward: bool) -> UCOMIEnumMoniker """
        ...

    def GetClassID(self, pClassID) -> Guid:
        """ GetClassID(self: UCOMIMoniker) -> Guid """
        ...

    def GetDisplayName(self, pbc, pmkToLeft, ppszDisplayName) -> str:
        """ GetDisplayName(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker) -> str """
        ...

    def GetSizeMax(self, pcbSize) -> Int64:
        """ GetSizeMax(self: UCOMIMoniker) -> Int64 """
        ...

    def GetTimeOfLastChange(self, pbc, pmkToLeft, pFileTime) -> FILETIME:
        """ GetTimeOfLastChange(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker) -> FILETIME """
        ...

    def Hash(self, pdwHash) -> int:
        """ Hash(self: UCOMIMoniker) -> int """
        ...

    def Inverse(self, ppmk) -> UCOMIMoniker:
        """ Inverse(self: UCOMIMoniker) -> UCOMIMoniker """
        ...

    def IsDirty(self) -> int:
        """ IsDirty(self: UCOMIMoniker) -> int """
        ...

    def IsEqual(self, pmkOtherMoniker:UCOMIMoniker): # -> 
        """ IsEqual(self: UCOMIMoniker, pmkOtherMoniker: UCOMIMoniker) """
        ...

    def IsRunning(self, pbc:UCOMIBindCtx, pmkToLeft:UCOMIMoniker, pmkNewlyRunning:UCOMIMoniker): # -> 
        """ IsRunning(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, pmkNewlyRunning: UCOMIMoniker) """
        ...

    def IsSystemMoniker(self, pdwMksys) -> int:
        """ IsSystemMoniker(self: UCOMIMoniker) -> int """
        ...

    def Load(self, pStm:UCOMIStream): # -> 
        """ Load(self: UCOMIMoniker, pStm: UCOMIStream) """
        ...

    def ParseDisplayName(self, pbc, pmkToLeft, pszDisplayName, pchEaten, ppmkOut) -> Tuple_[int, UCOMIMoniker]:
        """ ParseDisplayName(self: UCOMIMoniker, pbc: UCOMIBindCtx, pmkToLeft: UCOMIMoniker, pszDisplayName: str) -> (int, UCOMIMoniker) """
        ...

    def Reduce(self, pbc, dwReduceHowFar, ppmkToLeft, ppmkReduced) -> Tuple_[UCOMIMoniker, UCOMIMoniker]:
        """ Reduce(self: UCOMIMoniker, pbc: UCOMIBindCtx, dwReduceHowFar: int, ppmkToLeft: UCOMIMoniker) -> (UCOMIMoniker, UCOMIMoniker) """
        ...

    def RelativePathTo(self, pmkOther, ppmkRelPath) -> UCOMIMoniker:
        """ RelativePathTo(self: UCOMIMoniker, pmkOther: UCOMIMoniker) -> UCOMIMoniker """
        ...

    def Save(self, pStm:UCOMIStream, fClearDirty:bool): # -> 
        """ Save(self: UCOMIMoniker, pStm: UCOMIStream, fClearDirty: bool) """
        ...


class UCOMIPersistFile: # skipped bases: <type 'object'>
    """ no doc """
    def GetClassID(self, pClassID) -> Guid:
        """ GetClassID(self: UCOMIPersistFile) -> Guid """
        ...

    def GetCurFile(self, ppszFileName) -> str:
        """ GetCurFile(self: UCOMIPersistFile) -> str """
        ...

    def IsDirty(self) -> int:
        """ IsDirty(self: UCOMIPersistFile) -> int """
        ...

    def Load(self, pszFileName:str, dwMode:int): # -> 
        """ Load(self: UCOMIPersistFile, pszFileName: str, dwMode: int) """
        ...

    def Save(self, pszFileName:str, fRemember:bool): # -> 
        """ Save(self: UCOMIPersistFile, pszFileName: str, fRemember: bool) """
        ...

    def SaveCompleted(self, pszFileName:str): # -> 
        """ SaveCompleted(self: UCOMIPersistFile, pszFileName: str) """
        ...


class UCOMIRunningObjectTable: # skipped bases: <type 'object'>
    """ no doc """
    def EnumRunning(self, ppenumMoniker) -> UCOMIEnumMoniker:
        """ EnumRunning(self: UCOMIRunningObjectTable) -> UCOMIEnumMoniker """
        ...

    def GetObject(self, pmkObjectName, ppunkObject) -> object:
        """ GetObject(self: UCOMIRunningObjectTable, pmkObjectName: UCOMIMoniker) -> object """
        ...

    def GetTimeOfLastChange(self, pmkObjectName, pfiletime) -> FILETIME:
        """ GetTimeOfLastChange(self: UCOMIRunningObjectTable, pmkObjectName: UCOMIMoniker) -> FILETIME """
        ...

    def IsRunning(self, pmkObjectName:UCOMIMoniker): # -> 
        """ IsRunning(self: UCOMIRunningObjectTable, pmkObjectName: UCOMIMoniker) """
        ...

    def NoteChangeTime(self, dwRegister:int, pfiletime:FILETIME) -> FILETIME:
        """ NoteChangeTime(self: UCOMIRunningObjectTable, dwRegister: int, pfiletime: FILETIME) -> FILETIME """
        ...

    def Register(self, grfFlags, punkObject, pmkObjectName, pdwRegister) -> int:
        """ Register(self: UCOMIRunningObjectTable, grfFlags: int, punkObject: object, pmkObjectName: UCOMIMoniker) -> int """
        ...

    def Revoke(self, dwRegister:int): # -> 
        """ Revoke(self: UCOMIRunningObjectTable, dwRegister: int) """
        ...


class UCOMIStream: # skipped bases: <type 'object'>
    """ no doc """
    def Clone(self, ppstm) -> UCOMIStream:
        """ Clone(self: UCOMIStream) -> UCOMIStream """
        ...

    def Commit(self, grfCommitFlags:int): # -> 
        """ Commit(self: UCOMIStream, grfCommitFlags: int) """
        ...

    def CopyTo(self, pstm:UCOMIStream, cb:Int64, pcbRead:IntPtr, pcbWritten:IntPtr): # -> 
        """ CopyTo(self: UCOMIStream, pstm: UCOMIStream, cb: Int64, pcbRead: IntPtr, pcbWritten: IntPtr) """
        ...

    def LockRegion(self, libOffset:Int64, cb:Int64, dwLockType:int): # -> 
        """ LockRegion(self: UCOMIStream, libOffset: Int64, cb: Int64, dwLockType: int) """
        ...

    def Read(self, pv, cb, pcbRead) -> Array:
        """ Read(self: UCOMIStream, cb: int, pcbRead: IntPtr) -> Array[Byte] """
        ...

    def Revert(self): # -> 
        """ Revert(self: UCOMIStream) """
        ...

    def Seek(self, dlibMove:Int64, dwOrigin:int, plibNewPosition:IntPtr): # -> 
        """ Seek(self: UCOMIStream, dlibMove: Int64, dwOrigin: int, plibNewPosition: IntPtr) """
        ...

    def SetSize(self, libNewSize:Int64): # -> 
        """ SetSize(self: UCOMIStream, libNewSize: Int64) """
        ...

    def Stat(self, pstatstg, grfStatFlag) -> STATSTG:
        """ Stat(self: UCOMIStream, grfStatFlag: int) -> STATSTG """
        ...

    def UnlockRegion(self, libOffset:Int64, cb:Int64, dwLockType:int): # -> 
        """ UnlockRegion(self: UCOMIStream, libOffset: Int64, cb: Int64, dwLockType: int) """
        ...

    def Write(self, pv:Array, cb:int, pcbWritten:IntPtr): # -> 
        """ Write(self: UCOMIStream, pv: Array[Byte], cb: int, pcbWritten: IntPtr) """
        ...


class UCOMITypeComp: # skipped bases: <type 'object'>
    """ no doc """
    def Bind(self, szName, lHashVal, wFlags, ppTInfo, pDescKind, pBindPtr) -> Tuple_[UCOMITypeInfo, DESCKIND, BINDPTR]:
        """ Bind(self: UCOMITypeComp, szName: str, lHashVal: int, wFlags: Int16) -> (UCOMITypeInfo, DESCKIND, BINDPTR) """
        ...

    def BindType(self, szName, lHashVal, ppTInfo, ppTComp) -> Tuple_[UCOMITypeInfo, UCOMITypeComp]:
        """ BindType(self: UCOMITypeComp, szName: str, lHashVal: int) -> (UCOMITypeInfo, UCOMITypeComp) """
        ...


class UCOMITypeInfo: # skipped bases: <type 'object'>
    """ no doc """
    def AddressOfMember(self, memid, invKind, ppv) -> IntPtr:
        """ AddressOfMember(self: UCOMITypeInfo, memid: int, invKind: INVOKEKIND) -> IntPtr """
        ...

    def CreateInstance(self, pUnkOuter, riid, ppvObj) -> Tuple_[Guid, object]:
        """ CreateInstance(self: UCOMITypeInfo, pUnkOuter: object, riid: Guid) -> (Guid, object) """
        ...

    def GetContainingTypeLib(self, ppTLB, pIndex) -> Tuple_[UCOMITypeLib, int]:
        """ GetContainingTypeLib(self: UCOMITypeInfo) -> (UCOMITypeLib, int) """
        ...

    def GetDllEntry(self, memid, invKind, pBstrDllName, pBstrName, pwOrdinal) -> Tuple_[str, str, Int16]:
        """ GetDllEntry(self: UCOMITypeInfo, memid: int, invKind: INVOKEKIND) -> (str, str, Int16) """
        ...

    def GetDocumentation(self, index, strName, strDocString, dwHelpContext, strHelpFile) -> Tuple_[str, str, int, str]:
        """ GetDocumentation(self: UCOMITypeInfo, index: int) -> (str, str, int, str) """
        ...

    def GetFuncDesc(self, index, ppFuncDesc) -> IntPtr:
        """ GetFuncDesc(self: UCOMITypeInfo, index: int) -> IntPtr """
        ...

    def GetIDsOfNames(self, rgszNames, cNames, pMemId) -> Array:
        """ GetIDsOfNames(self: UCOMITypeInfo, rgszNames: Array[str], cNames: int) -> Array[int] """
        ...

    def GetImplTypeFlags(self, index, pImplTypeFlags) -> int:
        """ GetImplTypeFlags(self: UCOMITypeInfo, index: int) -> int """
        ...

    def GetMops(self, memid, pBstrMops) -> str:
        """ GetMops(self: UCOMITypeInfo, memid: int) -> str """
        ...

    def GetNames(self, memid, rgBstrNames, cMaxNames, pcNames) -> Tuple_[Array, int]:
        """ GetNames(self: UCOMITypeInfo, memid: int, cMaxNames: int) -> (Array[str], int) """
        ...

    def GetRefTypeInfo(self, hRef, ppTI) -> UCOMITypeInfo:
        """ GetRefTypeInfo(self: UCOMITypeInfo, hRef: int) -> UCOMITypeInfo """
        ...

    def GetRefTypeOfImplType(self, index, href) -> int:
        """ GetRefTypeOfImplType(self: UCOMITypeInfo, index: int) -> int """
        ...

    def GetTypeAttr(self, ppTypeAttr) -> IntPtr:
        """ GetTypeAttr(self: UCOMITypeInfo) -> IntPtr """
        ...

    def GetTypeComp(self, ppTComp) -> UCOMITypeComp:
        """ GetTypeComp(self: UCOMITypeInfo) -> UCOMITypeComp """
        ...

    def GetVarDesc(self, index, ppVarDesc) -> IntPtr:
        """ GetVarDesc(self: UCOMITypeInfo, index: int) -> IntPtr """
        ...

    def Invoke(self, pvInstance, memid, wFlags, pDispParams, pVarResult, pExcepInfo, puArgErr) -> Tuple_[DISPPARAMS, object, EXCEPINFO, int]:
        """ Invoke(self: UCOMITypeInfo, pvInstance: object, memid: int, wFlags: Int16, pDispParams: DISPPARAMS) -> (DISPPARAMS, object, EXCEPINFO, int) """
        ...

    def ReleaseFuncDesc(self, pFuncDesc:IntPtr): # -> 
        """ ReleaseFuncDesc(self: UCOMITypeInfo, pFuncDesc: IntPtr) """
        ...

    def ReleaseTypeAttr(self, pTypeAttr:IntPtr): # -> 
        """ ReleaseTypeAttr(self: UCOMITypeInfo, pTypeAttr: IntPtr) """
        ...

    def ReleaseVarDesc(self, pVarDesc:IntPtr): # -> 
        """ ReleaseVarDesc(self: UCOMITypeInfo, pVarDesc: IntPtr) """
        ...


class UCOMITypeLib: # skipped bases: <type 'object'>
    """ no doc """
    def FindName(self, szNameBuf, lHashVal, ppTInfo, rgMemId, pcFound) -> Tuple_[Array, Array, Int16]:
        """ FindName(self: UCOMITypeLib, szNameBuf: str, lHashVal: int, pcFound: Int16) -> (Array[UCOMITypeInfo], Array[int], Int16) """
        ...

    def GetDocumentation(self, index, strName, strDocString, dwHelpContext, strHelpFile) -> Tuple_[str, str, int, str]:
        """ GetDocumentation(self: UCOMITypeLib, index: int) -> (str, str, int, str) """
        ...

    def GetLibAttr(self, ppTLibAttr) -> IntPtr:
        """ GetLibAttr(self: UCOMITypeLib) -> IntPtr """
        ...

    def GetTypeComp(self, ppTComp) -> UCOMITypeComp:
        """ GetTypeComp(self: UCOMITypeLib) -> UCOMITypeComp """
        ...

    def GetTypeInfo(self, index, ppTI) -> UCOMITypeInfo:
        """ GetTypeInfo(self: UCOMITypeLib, index: int) -> UCOMITypeInfo """
        ...

    def GetTypeInfoCount(self) -> int:
        """ GetTypeInfoCount(self: UCOMITypeLib) -> int """
        ...

    def GetTypeInfoOfGuid(self, guid, ppTInfo) -> Tuple_[Guid, UCOMITypeInfo]:
        """ GetTypeInfoOfGuid(self: UCOMITypeLib, guid: Guid) -> (Guid, UCOMITypeInfo) """
        ...

    def GetTypeInfoType(self, index, pTKind) -> TYPEKIND:
        """ GetTypeInfoType(self: UCOMITypeLib, index: int) -> TYPEKIND """
        ...

    def IsName(self, szNameBuf:str, lHashVal:int) -> bool:
        """ IsName(self: UCOMITypeLib, szNameBuf: str, lHashVal: int) -> bool """
        ...

    def ReleaseTLibAttr(self, pTLibAttr:IntPtr): # -> 
        """ ReleaseTLibAttr(self: UCOMITypeLib, pTLibAttr: IntPtr) """
        ...


class UnknownWrapper: # skipped bases: <type 'object'>, <type 'object'>
    """ UnknownWrapper(obj: object) """
    @property
    def WrappedObject(self) -> object:
        """ Get: WrappedObject(self: UnknownWrapper) -> object """
        ...



class UnmanagedFunctionPointerAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ UnmanagedFunctionPointerAttribute(callingConvention: CallingConvention) """
    @property
    def CallingConvention(self) -> CallingConvention:
        """ Get: CallingConvention(self: UnmanagedFunctionPointerAttribute) -> CallingConvention """
        ...


    def __new__(cls, callingConvention:CallingConvention) -> Self:
        """ __new__(cls: type, callingConvention: CallingConvention) """
        ...

    BestFitMapping = ...
    CharSet = ...
    SetLastError = ...
    ThrowOnUnmappableChar = ...


class UnmanagedType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UnmanagedType, values: AnsiBStr (35), AsAny (40), Bool (2), BStr (19), ByValArray (30), ByValTStr (23), Currency (15), CustomMarshaler (44), Error (45), FunctionPtr (38), HString (47), I1 (3), I2 (5), I4 (7), I8 (9), IDispatch (26), IInspectable (46), Interface (28), IUnknown (25), LPArray (42), LPStr (20), LPStruct (43), LPTStr (22), LPUTF8Str (48), LPWStr (21), R4 (11), R8 (12), SafeArray (29), Struct (27), SysInt (31), SysUInt (32), TBStr (36), U1 (4), U2 (6), U4 (8), U8 (10), VariantBool (37), VBByRefStr (34) """
    AnsiBStr: UnmanagedType = ...
    AsAny: UnmanagedType = ...
    Bool: UnmanagedType = ...
    BStr: UnmanagedType = ...
    ByValArray: UnmanagedType = ...
    ByValTStr: UnmanagedType = ...
    Currency: UnmanagedType = ...
    CustomMarshaler: UnmanagedType = ...
    Error: UnmanagedType = ...
    FunctionPtr: UnmanagedType = ...
    HString: UnmanagedType = ...
    I1: UnmanagedType = ...
    I2: UnmanagedType = ...
    I4: UnmanagedType = ...
    I8: UnmanagedType = ...
    IDispatch: UnmanagedType = ...
    IInspectable: UnmanagedType = ...
    Interface: UnmanagedType = ...
    IUnknown: UnmanagedType = ...
    LPArray: UnmanagedType = ...
    LPStr: UnmanagedType = ...
    LPStruct: UnmanagedType = ...
    LPTStr: UnmanagedType = ...
    LPUTF8Str: UnmanagedType = ...
    LPWStr: UnmanagedType = ...
    R4: UnmanagedType = ...
    R8: UnmanagedType = ...
    SafeArray: UnmanagedType = ...
    Struct: UnmanagedType = ...
    SysInt: UnmanagedType = ...
    SysUInt: UnmanagedType = ...
    TBStr: UnmanagedType = ...
    U1: UnmanagedType = ...
    U2: UnmanagedType = ...
    U4: UnmanagedType = ...
    U8: UnmanagedType = ...
    value__ = ...
    VariantBool: UnmanagedType = ...
    VBByRefStr: UnmanagedType = ...


class VARDESC: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def DESCUNION(self, *args): #cannot find CLR method
        """ no doc """
        ...

    elemdescVar = ...
    lpstrSchema = ...
    memid = ...
    varkind = ...
    wVarFlags = ...


class VarEnum(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum VarEnum, values: VT_ARRAY (8192), VT_BLOB (65), VT_BLOB_OBJECT (70), VT_BOOL (11), VT_BSTR (8), VT_BYREF (16384), VT_CARRAY (28), VT_CF (71), VT_CLSID (72), VT_CY (6), VT_DATE (7), VT_DECIMAL (14), VT_DISPATCH (9), VT_EMPTY (0), VT_ERROR (10), VT_FILETIME (64), VT_HRESULT (25), VT_I1 (16), VT_I2 (2), VT_I4 (3), VT_I8 (20), VT_INT (22), VT_LPSTR (30), VT_LPWSTR (31), VT_NULL (1), VT_PTR (26), VT_R4 (4), VT_R8 (5), VT_RECORD (36), VT_SAFEARRAY (27), VT_STORAGE (67), VT_STORED_OBJECT (69), VT_STREAM (66), VT_STREAMED_OBJECT (68), VT_UI1 (17), VT_UI2 (18), VT_UI4 (19), VT_UI8 (21), VT_UINT (23), VT_UNKNOWN (13), VT_USERDEFINED (29), VT_VARIANT (12), VT_VECTOR (4096), VT_VOID (24) """
    value__ = ...
    VT_ARRAY: VarEnum = ...
    VT_BLOB: VarEnum = ...
    VT_BLOB_OBJECT: VarEnum = ...
    VT_BOOL: VarEnum = ...
    VT_BSTR: VarEnum = ...
    VT_BYREF: VarEnum = ...
    VT_CARRAY: VarEnum = ...
    VT_CF: VarEnum = ...
    VT_CLSID: VarEnum = ...
    VT_CY: VarEnum = ...
    VT_DATE: VarEnum = ...
    VT_DECIMAL: VarEnum = ...
    VT_DISPATCH: VarEnum = ...
    VT_EMPTY: VarEnum = ...
    VT_ERROR: VarEnum = ...
    VT_FILETIME: VarEnum = ...
    VT_HRESULT: VarEnum = ...
    VT_I1: VarEnum = ...
    VT_I2: VarEnum = ...
    VT_I4: VarEnum = ...
    VT_I8: VarEnum = ...
    VT_INT: VarEnum = ...
    VT_LPSTR: VarEnum = ...
    VT_LPWSTR: VarEnum = ...
    VT_NULL: VarEnum = ...
    VT_PTR: VarEnum = ...
    VT_R4: VarEnum = ...
    VT_R8: VarEnum = ...
    VT_RECORD: VarEnum = ...
    VT_SAFEARRAY: VarEnum = ...
    VT_STORAGE: VarEnum = ...
    VT_STORED_OBJECT: VarEnum = ...
    VT_STREAM: VarEnum = ...
    VT_STREAMED_OBJECT: VarEnum = ...
    VT_UI1: VarEnum = ...
    VT_UI2: VarEnum = ...
    VT_UI4: VarEnum = ...
    VT_UI8: VarEnum = ...
    VT_UINT: VarEnum = ...
    VT_UNKNOWN: VarEnum = ...
    VT_USERDEFINED: VarEnum = ...
    VT_VARIANT: VarEnum = ...
    VT_VECTOR: VarEnum = ...
    VT_VOID: VarEnum = ...


class VARFLAGS(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) VARFLAGS, values: VARFLAG_FBINDABLE (4), VARFLAG_FDEFAULTBIND (32), VARFLAG_FDEFAULTCOLLELEM (256), VARFLAG_FDISPLAYBIND (16), VARFLAG_FHIDDEN (64), VARFLAG_FIMMEDIATEBIND (4096), VARFLAG_FNONBROWSABLE (1024), VARFLAG_FREADONLY (1), VARFLAG_FREPLACEABLE (2048), VARFLAG_FREQUESTEDIT (8), VARFLAG_FRESTRICTED (128), VARFLAG_FSOURCE (2), VARFLAG_FUIDEFAULT (512) """
    value__ = ...
    VARFLAG_FBINDABLE: VARFLAGS = ...
    VARFLAG_FDEFAULTBIND: VARFLAGS = ...
    VARFLAG_FDEFAULTCOLLELEM: VARFLAGS = ...
    VARFLAG_FDISPLAYBIND: VARFLAGS = ...
    VARFLAG_FHIDDEN: VARFLAGS = ...
    VARFLAG_FIMMEDIATEBIND: VARFLAGS = ...
    VARFLAG_FNONBROWSABLE: VARFLAGS = ...
    VARFLAG_FREADONLY: VARFLAGS = ...
    VARFLAG_FREPLACEABLE: VARFLAGS = ...
    VARFLAG_FREQUESTEDIT: VARFLAGS = ...
    VARFLAG_FRESTRICTED: VARFLAGS = ...
    VARFLAG_FSOURCE: VARFLAGS = ...
    VARFLAG_FUIDEFAULT: VARFLAGS = ...


class VariantWrapper: # skipped bases: <type 'object'>, <type 'object'>
    """ VariantWrapper(obj: object) """
    @property
    def WrappedObject(self) -> object:
        """ Get: WrappedObject(self: VariantWrapper) -> object """
        ...



class _Activator: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _Activator, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _Activator, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _Activator) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _Activator, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _Assembly: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CodeBase(self) -> str:
        """ Get: CodeBase(self: _Assembly) -> str """
        ...

    @property
    def EntryPoint(self) -> MethodInfo:
        """ Get: EntryPoint(self: _Assembly) -> MethodInfo """
        ...

    @property
    def EscapedCodeBase(self) -> str:
        """ Get: EscapedCodeBase(self: _Assembly) -> str """
        ...

    @property
    def Evidence(self) -> Evidence:
        """ Get: Evidence(self: _Assembly) -> Evidence """
        ...

    @property
    def FullName(self) -> str:
        """ Get: FullName(self: _Assembly) -> str """
        ...

    @property
    def GlobalAssemblyCache(self) -> bool:
        """ Get: GlobalAssemblyCache(self: _Assembly) -> bool """
        ...

    @property
    def Location(self) -> str:
        """ Get: Location(self: _Assembly) -> str """
        ...


    def CreateInstance(self, typeName:str, ignoreCase:bool = ..., bindingAttr:BindingFlags = ..., binder:Binder = ..., args:Array = ..., culture:CultureInfo = ..., activationAttributes:Array = ...) -> object:
        """
        CreateInstance(self: _Assembly, typeName: str) -> object
        CreateInstance(self: _Assembly, typeName: str, ignoreCase: bool) -> object
        CreateInstance(self: _Assembly, typeName: str, ignoreCase: bool, bindingAttr: BindingFlags, binder: Binder, args: Array[object], culture: CultureInfo, activationAttributes: Array[object]) -> object
        """
        ...

    def Equals(self, other:object) -> bool:
        """ Equals(self: _Assembly, other: object) -> bool """
        ...

    def GetCustomAttributes(self, *__args:bool) -> Array:
        """
        GetCustomAttributes(self: _Assembly, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _Assembly, inherit: bool) -> Array[object]
        """
        ...

    def GetExportedTypes(self) -> Array:
        """ GetExportedTypes(self: _Assembly) -> Array[Type] """
        ...

    def GetFile(self, name:str) -> FileStream:
        """ GetFile(self: _Assembly, name: str) -> FileStream """
        ...

    def GetFiles(self, getResourceModules:bool = ...) -> Array:
        """
        GetFiles(self: _Assembly) -> Array[FileStream]
        GetFiles(self: _Assembly, getResourceModules: bool) -> Array[FileStream]
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: _Assembly) -> int """
        ...

    def GetLoadedModules(self, getResourceModules:bool = ...) -> Array:
        """
        GetLoadedModules(self: _Assembly) -> Array[Module]
        GetLoadedModules(self: _Assembly, getResourceModules: bool) -> Array[Module]
        """
        ...

    def GetManifestResourceInfo(self, resourceName:str) -> ManifestResourceInfo:
        """ GetManifestResourceInfo(self: _Assembly, resourceName: str) -> ManifestResourceInfo """
        ...

    def GetManifestResourceNames(self) -> Array:
        """ GetManifestResourceNames(self: _Assembly) -> Array[str] """
        ...

    def GetManifestResourceStream(self, *__args:str) -> Stream:
        """
        GetManifestResourceStream(self: _Assembly, type: Type, name: str) -> Stream
        GetManifestResourceStream(self: _Assembly, name: str) -> Stream
        """
        ...

    def GetModule(self, name:str) -> Module:
        """ GetModule(self: _Assembly, name: str) -> Module """
        ...

    def GetModules(self, getResourceModules:bool = ...) -> Array:
        """
        GetModules(self: _Assembly) -> Array[Module]
        GetModules(self: _Assembly, getResourceModules: bool) -> Array[Module]
        """
        ...

    def GetName(self, copiedName:bool = ...) -> AssemblyName:
        """
        GetName(self: _Assembly) -> AssemblyName
        GetName(self: _Assembly, copiedName: bool) -> AssemblyName
        """
        ...

    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: _Assembly, info: SerializationInfo, context: StreamingContext) """
        ...

    def GetReferencedAssemblies(self) -> Array:
        """ GetReferencedAssemblies(self: _Assembly) -> Array[AssemblyName] """
        ...

    def GetSatelliteAssembly(self, culture:CultureInfo, version:Version = ...) -> Assembly:
        """
        GetSatelliteAssembly(self: _Assembly, culture: CultureInfo) -> Assembly
        GetSatelliteAssembly(self: _Assembly, culture: CultureInfo, version: Version) -> Assembly
        """
        ...

    def GetType(self, name:str = ..., throwOnError:bool = ..., ignoreCase:bool = ...) -> Type:
        """
        GetType(self: _Assembly) -> Type
        GetType(self: _Assembly, name: str) -> Type
        GetType(self: _Assembly, name: str, throwOnError: bool) -> Type
        GetType(self: _Assembly, name: str, throwOnError: bool, ignoreCase: bool) -> Type
        """
        ...

    def GetTypes(self) -> Array:
        """ GetTypes(self: _Assembly) -> Array[Type] """
        ...

    def IsDefined(self, attributeType:Type, inherit:bool) -> bool:
        """ IsDefined(self: _Assembly, attributeType: Type, inherit: bool) -> bool """
        ...

    def LoadModule(self, moduleName:str, rawModule:Array, rawSymbolStore:Array = ...) -> Module:
        """
        LoadModule(self: _Assembly, moduleName: str, rawModule: Array[Byte]) -> Module
        LoadModule(self: _Assembly, moduleName: str, rawModule: Array[Byte], rawSymbolStore: Array[Byte]) -> Module
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: _Assembly) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    ModuleResolve = ...


class _AssemblyBuilder: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _AssemblyBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _AssemblyBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _AssemblyBuilder) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _AssemblyBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _AssemblyName: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _AssemblyName, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _AssemblyName, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _AssemblyName) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _AssemblyName, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _ConstructorBuilder: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _ConstructorBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _ConstructorBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _ConstructorBuilder) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _ConstructorBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _ConstructorInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> MethodAttributes:
        """ Get: Attributes(self: _ConstructorInfo) -> MethodAttributes """
        ...

    @property
    def CallingConvention(self) -> CallingConventions:
        """ Get: CallingConvention(self: _ConstructorInfo) -> CallingConventions """
        ...

    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: _ConstructorInfo) -> Type """
        ...

    @property
    def IsAbstract(self) -> bool:
        """ Get: IsAbstract(self: _ConstructorInfo) -> bool """
        ...

    @property
    def IsAssembly(self) -> bool:
        """ Get: IsAssembly(self: _ConstructorInfo) -> bool """
        ...

    @property
    def IsConstructor(self) -> bool:
        """ Get: IsConstructor(self: _ConstructorInfo) -> bool """
        ...

    @property
    def IsFamily(self) -> bool:
        """ Get: IsFamily(self: _ConstructorInfo) -> bool """
        ...

    @property
    def IsFamilyAndAssembly(self) -> bool:
        """ Get: IsFamilyAndAssembly(self: _ConstructorInfo) -> bool """
        ...

    @property
    def IsFamilyOrAssembly(self) -> bool:
        """ Get: IsFamilyOrAssembly(self: _ConstructorInfo) -> bool """
        ...

    @property
    def IsFinal(self) -> bool:
        """ Get: IsFinal(self: _ConstructorInfo) -> bool """
        ...

    @property
    def IsHideBySig(self) -> bool:
        """ Get: IsHideBySig(self: _ConstructorInfo) -> bool """
        ...

    @property
    def IsPrivate(self) -> bool:
        """ Get: IsPrivate(self: _ConstructorInfo) -> bool """
        ...

    @property
    def IsPublic(self) -> bool:
        """ Get: IsPublic(self: _ConstructorInfo) -> bool """
        ...

    @property
    def IsSpecialName(self) -> bool:
        """ Get: IsSpecialName(self: _ConstructorInfo) -> bool """
        ...

    @property
    def IsStatic(self) -> bool:
        """ Get: IsStatic(self: _ConstructorInfo) -> bool """
        ...

    @property
    def IsVirtual(self) -> bool:
        """ Get: IsVirtual(self: _ConstructorInfo) -> bool """
        ...

    @property
    def MemberType(self) -> MemberTypes:
        """ Get: MemberType(self: _ConstructorInfo) -> MemberTypes """
        ...

    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """ Get: MethodHandle(self: _ConstructorInfo) -> RuntimeMethodHandle """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: _ConstructorInfo) -> str """
        ...

    @property
    def ReflectedType(self) -> Type:
        """ Get: ReflectedType(self: _ConstructorInfo) -> Type """
        ...


    def Equals(self, other:object) -> bool:
        """ Equals(self: _ConstructorInfo, other: object) -> bool """
        ...

    def GetCustomAttributes(self, *__args:bool) -> Array:
        """
        GetCustomAttributes(self: _ConstructorInfo, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _ConstructorInfo, inherit: bool) -> Array[object]
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: _ConstructorInfo) -> int """
        ...

    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _ConstructorInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """ GetMethodImplementationFlags(self: _ConstructorInfo) -> MethodImplAttributes """
        ...

    def GetParameters(self) -> Array:
        """ GetParameters(self: _ConstructorInfo) -> Array[ParameterInfo] """
        ...

    def GetType(self) -> Type:
        """ GetType(self: _ConstructorInfo) -> Type """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _ConstructorInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _ConstructorInfo) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _ConstructorInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...

    def Invoke_2(self, obj:object, invokeAttr:BindingFlags, binder:Binder, parameters:Array, culture:CultureInfo) -> object:
        """ Invoke_2(self: _ConstructorInfo, obj: object, invokeAttr: BindingFlags, binder: Binder, parameters: Array[object], culture: CultureInfo) -> object """
        ...

    def Invoke_3(self, obj:object, parameters:Array) -> object:
        """ Invoke_3(self: _ConstructorInfo, obj: object, parameters: Array[object]) -> object """
        ...

    def Invoke_4(self, invokeAttr:BindingFlags, binder:Binder, parameters:Array, culture:CultureInfo) -> object:
        """ Invoke_4(self: _ConstructorInfo, invokeAttr: BindingFlags, binder: Binder, parameters: Array[object], culture: CultureInfo) -> object """
        ...

    def Invoke_5(self, parameters:Array) -> object:
        """ Invoke_5(self: _ConstructorInfo, parameters: Array[object]) -> object """
        ...

    def IsDefined(self, attributeType:Type, inherit:bool) -> bool:
        """ IsDefined(self: _ConstructorInfo, attributeType: Type, inherit: bool) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: _ConstructorInfo) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class _CustomAttributeBuilder: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _CustomAttributeBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _CustomAttributeBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _CustomAttributeBuilder) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _CustomAttributeBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _EnumBuilder: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _EnumBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _EnumBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _EnumBuilder) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _EnumBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _EventBuilder: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _EventBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _EventBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _EventBuilder) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _EventBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _EventInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> EventAttributes:
        """ Get: Attributes(self: _EventInfo) -> EventAttributes """
        ...

    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: _EventInfo) -> Type """
        ...

    @property
    def EventHandlerType(self) -> Type:
        """ Get: EventHandlerType(self: _EventInfo) -> Type """
        ...

    @property
    def IsMulticast(self) -> bool:
        """ Get: IsMulticast(self: _EventInfo) -> bool """
        ...

    @property
    def IsSpecialName(self) -> bool:
        """ Get: IsSpecialName(self: _EventInfo) -> bool """
        ...

    @property
    def MemberType(self) -> MemberTypes:
        """ Get: MemberType(self: _EventInfo) -> MemberTypes """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: _EventInfo) -> str """
        ...

    @property
    def ReflectedType(self) -> Type:
        """ Get: ReflectedType(self: _EventInfo) -> Type """
        ...


    def AddEventHandler(self, target:object, handler:Delegate): # -> 
        """ AddEventHandler(self: _EventInfo, target: object, handler: Delegate) """
        ...

    def Equals(self, other:object) -> bool:
        """ Equals(self: _EventInfo, other: object) -> bool """
        ...

    def GetAddMethod(self, nonPublic:bool = ...) -> MethodInfo:
        """
        GetAddMethod(self: _EventInfo, nonPublic: bool) -> MethodInfo
        GetAddMethod(self: _EventInfo) -> MethodInfo
        """
        ...

    def GetCustomAttributes(self, *__args:bool) -> Array:
        """
        GetCustomAttributes(self: _EventInfo, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _EventInfo, inherit: bool) -> Array[object]
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: _EventInfo) -> int """
        ...

    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _EventInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetRaiseMethod(self, nonPublic:bool = ...) -> MethodInfo:
        """
        GetRaiseMethod(self: _EventInfo, nonPublic: bool) -> MethodInfo
        GetRaiseMethod(self: _EventInfo) -> MethodInfo
        """
        ...

    def GetRemoveMethod(self, nonPublic:bool = ...) -> MethodInfo:
        """
        GetRemoveMethod(self: _EventInfo, nonPublic: bool) -> MethodInfo
        GetRemoveMethod(self: _EventInfo) -> MethodInfo
        """
        ...

    def GetType(self) -> Type:
        """ GetType(self: _EventInfo) -> Type """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _EventInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _EventInfo) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _EventInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...

    def IsDefined(self, attributeType:Type, inherit:bool) -> bool:
        """ IsDefined(self: _EventInfo, attributeType: Type, inherit: bool) -> bool """
        ...

    def RemoveEventHandler(self, target:object, handler:Delegate): # -> 
        """ RemoveEventHandler(self: _EventInfo, target: object, handler: Delegate) """
        ...

    def ToString(self) -> str:
        """ ToString(self: _EventInfo) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class _Exception: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def HelpLink(self) -> str:
        """
        Get: HelpLink(self: _Exception) -> str
        Set: HelpLink(self: _Exception) = value
        """
        ...

    @property
    def InnerException(self) -> Exception:
        """ Get: InnerException(self: _Exception) -> Exception """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: _Exception) -> str """
        ...

    @property
    def Source(self) -> str:
        """
        Get: Source(self: _Exception) -> str
        Set: Source(self: _Exception) = value
        """
        ...

    @property
    def StackTrace(self) -> str:
        """ Get: StackTrace(self: _Exception) -> str """
        ...

    @property
    def TargetSite(self) -> MethodBase:
        """ Get: TargetSite(self: _Exception) -> MethodBase """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: _Exception, obj: object) -> bool """
        ...

    def GetBaseException(self) -> Exception:
        """ GetBaseException(self: _Exception) -> Exception """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: _Exception) -> int """
        ...

    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: _Exception, info: SerializationInfo, context: StreamingContext) """
        ...

    def GetType(self) -> Type:
        """ GetType(self: _Exception) -> Type """
        ...

    def ToString(self) -> str:
        """ ToString(self: _Exception) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class _FieldBuilder: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _FieldBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _FieldBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _FieldBuilder) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _FieldBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _FieldInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> FieldAttributes:
        """ Get: Attributes(self: _FieldInfo) -> FieldAttributes """
        ...

    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: _FieldInfo) -> Type """
        ...

    @property
    def FieldHandle(self) -> RuntimeFieldHandle:
        """ Get: FieldHandle(self: _FieldInfo) -> RuntimeFieldHandle """
        ...

    @property
    def FieldType(self) -> Type:
        """ Get: FieldType(self: _FieldInfo) -> Type """
        ...

    @property
    def IsAssembly(self) -> bool:
        """ Get: IsAssembly(self: _FieldInfo) -> bool """
        ...

    @property
    def IsFamily(self) -> bool:
        """ Get: IsFamily(self: _FieldInfo) -> bool """
        ...

    @property
    def IsFamilyAndAssembly(self) -> bool:
        """ Get: IsFamilyAndAssembly(self: _FieldInfo) -> bool """
        ...

    @property
    def IsFamilyOrAssembly(self) -> bool:
        """ Get: IsFamilyOrAssembly(self: _FieldInfo) -> bool """
        ...

    @property
    def IsInitOnly(self) -> bool:
        """ Get: IsInitOnly(self: _FieldInfo) -> bool """
        ...

    @property
    def IsLiteral(self) -> bool:
        """ Get: IsLiteral(self: _FieldInfo) -> bool """
        ...

    @property
    def IsNotSerialized(self) -> bool:
        """ Get: IsNotSerialized(self: _FieldInfo) -> bool """
        ...

    @property
    def IsPinvokeImpl(self) -> bool:
        """ Get: IsPinvokeImpl(self: _FieldInfo) -> bool """
        ...

    @property
    def IsPrivate(self) -> bool:
        """ Get: IsPrivate(self: _FieldInfo) -> bool """
        ...

    @property
    def IsPublic(self) -> bool:
        """ Get: IsPublic(self: _FieldInfo) -> bool """
        ...

    @property
    def IsSpecialName(self) -> bool:
        """ Get: IsSpecialName(self: _FieldInfo) -> bool """
        ...

    @property
    def IsStatic(self) -> bool:
        """ Get: IsStatic(self: _FieldInfo) -> bool """
        ...

    @property
    def MemberType(self) -> MemberTypes:
        """ Get: MemberType(self: _FieldInfo) -> MemberTypes """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: _FieldInfo) -> str """
        ...

    @property
    def ReflectedType(self) -> Type:
        """ Get: ReflectedType(self: _FieldInfo) -> Type """
        ...


    def Equals(self, other:object) -> bool:
        """ Equals(self: _FieldInfo, other: object) -> bool """
        ...

    def GetCustomAttributes(self, *__args:bool) -> Array:
        """
        GetCustomAttributes(self: _FieldInfo, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _FieldInfo, inherit: bool) -> Array[object]
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: _FieldInfo) -> int """
        ...

    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _FieldInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetType(self) -> Type:
        """ GetType(self: _FieldInfo) -> Type """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _FieldInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _FieldInfo) -> UInt32 """
        ...

    def GetValue(self, obj:object) -> object:
        """ GetValue(self: _FieldInfo, obj: object) -> object """
        ...

    def GetValueDirect(self, obj:TypedReference) -> object:
        """ GetValueDirect(self: _FieldInfo, obj: TypedReference) -> object """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _FieldInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...

    def IsDefined(self, attributeType:Type, inherit:bool) -> bool:
        """ IsDefined(self: _FieldInfo, attributeType: Type, inherit: bool) -> bool """
        ...

    def SetValue(self, obj:object, value:object, invokeAttr:BindingFlags = ..., binder:Binder = ..., culture:CultureInfo = ...): # -> 
        """ SetValue(self: _FieldInfo, obj: object, value: object, invokeAttr: BindingFlags, binder: Binder, culture: CultureInfo)SetValue(self: _FieldInfo, obj: object, value: object) """
        ...

    def SetValueDirect(self, obj:TypedReference, value:object): # -> 
        """ SetValueDirect(self: _FieldInfo, obj: TypedReference, value: object) """
        ...

    def ToString(self) -> str:
        """ ToString(self: _FieldInfo) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class _ILGenerator: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _ILGenerator, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _ILGenerator, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _ILGenerator) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _ILGenerator, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _LocalBuilder: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _LocalBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _LocalBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _LocalBuilder) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _LocalBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _MemberInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: _MemberInfo) -> Type """
        ...

    @property
    def MemberType(self) -> MemberTypes:
        """ Get: MemberType(self: _MemberInfo) -> MemberTypes """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: _MemberInfo) -> str """
        ...

    @property
    def ReflectedType(self) -> Type:
        """ Get: ReflectedType(self: _MemberInfo) -> Type """
        ...


    def Equals(self, other:object) -> bool:
        """ Equals(self: _MemberInfo, other: object) -> bool """
        ...

    def GetCustomAttributes(self, *__args:bool) -> Array:
        """
        GetCustomAttributes(self: _MemberInfo, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _MemberInfo, inherit: bool) -> Array[object]
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: _MemberInfo) -> int """
        ...

    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _MemberInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetType(self) -> Type:
        """ GetType(self: _MemberInfo) -> Type """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _MemberInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _MemberInfo) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _MemberInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...

    def IsDefined(self, attributeType:Type, inherit:bool) -> bool:
        """ IsDefined(self: _MemberInfo, attributeType: Type, inherit: bool) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: _MemberInfo) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class _MethodBase: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> MethodAttributes:
        """ Get: Attributes(self: _MethodBase) -> MethodAttributes """
        ...

    @property
    def CallingConvention(self) -> CallingConventions:
        """ Get: CallingConvention(self: _MethodBase) -> CallingConventions """
        ...

    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: _MethodBase) -> Type """
        ...

    @property
    def IsAbstract(self) -> bool:
        """ Get: IsAbstract(self: _MethodBase) -> bool """
        ...

    @property
    def IsAssembly(self) -> bool:
        """ Get: IsAssembly(self: _MethodBase) -> bool """
        ...

    @property
    def IsConstructor(self) -> bool:
        """ Get: IsConstructor(self: _MethodBase) -> bool """
        ...

    @property
    def IsFamily(self) -> bool:
        """ Get: IsFamily(self: _MethodBase) -> bool """
        ...

    @property
    def IsFamilyAndAssembly(self) -> bool:
        """ Get: IsFamilyAndAssembly(self: _MethodBase) -> bool """
        ...

    @property
    def IsFamilyOrAssembly(self) -> bool:
        """ Get: IsFamilyOrAssembly(self: _MethodBase) -> bool """
        ...

    @property
    def IsFinal(self) -> bool:
        """ Get: IsFinal(self: _MethodBase) -> bool """
        ...

    @property
    def IsHideBySig(self) -> bool:
        """ Get: IsHideBySig(self: _MethodBase) -> bool """
        ...

    @property
    def IsPrivate(self) -> bool:
        """ Get: IsPrivate(self: _MethodBase) -> bool """
        ...

    @property
    def IsPublic(self) -> bool:
        """ Get: IsPublic(self: _MethodBase) -> bool """
        ...

    @property
    def IsSpecialName(self) -> bool:
        """ Get: IsSpecialName(self: _MethodBase) -> bool """
        ...

    @property
    def IsStatic(self) -> bool:
        """ Get: IsStatic(self: _MethodBase) -> bool """
        ...

    @property
    def IsVirtual(self) -> bool:
        """ Get: IsVirtual(self: _MethodBase) -> bool """
        ...

    @property
    def MemberType(self) -> MemberTypes:
        """ Get: MemberType(self: _MethodBase) -> MemberTypes """
        ...

    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """ Get: MethodHandle(self: _MethodBase) -> RuntimeMethodHandle """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: _MethodBase) -> str """
        ...

    @property
    def ReflectedType(self) -> Type:
        """ Get: ReflectedType(self: _MethodBase) -> Type """
        ...


    def Equals(self, other:object) -> bool:
        """ Equals(self: _MethodBase, other: object) -> bool """
        ...

    def GetCustomAttributes(self, *__args:bool) -> Array:
        """
        GetCustomAttributes(self: _MethodBase, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _MethodBase, inherit: bool) -> Array[object]
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: _MethodBase) -> int """
        ...

    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _MethodBase, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """ GetMethodImplementationFlags(self: _MethodBase) -> MethodImplAttributes """
        ...

    def GetParameters(self) -> Array:
        """ GetParameters(self: _MethodBase) -> Array[ParameterInfo] """
        ...

    def GetType(self) -> Type:
        """ GetType(self: _MethodBase) -> Type """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _MethodBase, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _MethodBase) -> UInt32 """
        ...

    def Invoke(self, *__args) -> Guid:
        """
        Invoke(self: _MethodBase, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        Invoke(self: _MethodBase, obj: object, invokeAttr: BindingFlags, binder: Binder, parameters: Array[object], culture: CultureInfo) -> object
        Invoke(self: _MethodBase, obj: object, parameters: Array[object]) -> object
        """
        ...

    def IsDefined(self, attributeType:Type, inherit:bool) -> bool:
        """ IsDefined(self: _MethodBase, attributeType: Type, inherit: bool) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: _MethodBase) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class _MethodBuilder: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _MethodBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _MethodBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _MethodBuilder) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _MethodBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _MethodInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> MethodAttributes:
        """ Get: Attributes(self: _MethodInfo) -> MethodAttributes """
        ...

    @property
    def CallingConvention(self) -> CallingConventions:
        """ Get: CallingConvention(self: _MethodInfo) -> CallingConventions """
        ...

    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: _MethodInfo) -> Type """
        ...

    @property
    def IsAbstract(self) -> bool:
        """ Get: IsAbstract(self: _MethodInfo) -> bool """
        ...

    @property
    def IsAssembly(self) -> bool:
        """ Get: IsAssembly(self: _MethodInfo) -> bool """
        ...

    @property
    def IsConstructor(self) -> bool:
        """ Get: IsConstructor(self: _MethodInfo) -> bool """
        ...

    @property
    def IsFamily(self) -> bool:
        """ Get: IsFamily(self: _MethodInfo) -> bool """
        ...

    @property
    def IsFamilyAndAssembly(self) -> bool:
        """ Get: IsFamilyAndAssembly(self: _MethodInfo) -> bool """
        ...

    @property
    def IsFamilyOrAssembly(self) -> bool:
        """ Get: IsFamilyOrAssembly(self: _MethodInfo) -> bool """
        ...

    @property
    def IsFinal(self) -> bool:
        """ Get: IsFinal(self: _MethodInfo) -> bool """
        ...

    @property
    def IsHideBySig(self) -> bool:
        """ Get: IsHideBySig(self: _MethodInfo) -> bool """
        ...

    @property
    def IsPrivate(self) -> bool:
        """ Get: IsPrivate(self: _MethodInfo) -> bool """
        ...

    @property
    def IsPublic(self) -> bool:
        """ Get: IsPublic(self: _MethodInfo) -> bool """
        ...

    @property
    def IsSpecialName(self) -> bool:
        """ Get: IsSpecialName(self: _MethodInfo) -> bool """
        ...

    @property
    def IsStatic(self) -> bool:
        """ Get: IsStatic(self: _MethodInfo) -> bool """
        ...

    @property
    def IsVirtual(self) -> bool:
        """ Get: IsVirtual(self: _MethodInfo) -> bool """
        ...

    @property
    def MemberType(self) -> MemberTypes:
        """ Get: MemberType(self: _MethodInfo) -> MemberTypes """
        ...

    @property
    def MethodHandle(self) -> RuntimeMethodHandle:
        """ Get: MethodHandle(self: _MethodInfo) -> RuntimeMethodHandle """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: _MethodInfo) -> str """
        ...

    @property
    def ReflectedType(self) -> Type:
        """ Get: ReflectedType(self: _MethodInfo) -> Type """
        ...

    @property
    def ReturnType(self) -> Type:
        """ Get: ReturnType(self: _MethodInfo) -> Type """
        ...

    @property
    def ReturnTypeCustomAttributes(self) -> ICustomAttributeProvider:
        """ Get: ReturnTypeCustomAttributes(self: _MethodInfo) -> ICustomAttributeProvider """
        ...


    def Equals(self, other:object) -> bool:
        """ Equals(self: _MethodInfo, other: object) -> bool """
        ...

    def GetBaseDefinition(self) -> MethodInfo:
        """ GetBaseDefinition(self: _MethodInfo) -> MethodInfo """
        ...

    def GetCustomAttributes(self, *__args:bool) -> Array:
        """
        GetCustomAttributes(self: _MethodInfo, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _MethodInfo, inherit: bool) -> Array[object]
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: _MethodInfo) -> int """
        ...

    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _MethodInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetMethodImplementationFlags(self) -> MethodImplAttributes:
        """ GetMethodImplementationFlags(self: _MethodInfo) -> MethodImplAttributes """
        ...

    def GetParameters(self) -> Array:
        """ GetParameters(self: _MethodInfo) -> Array[ParameterInfo] """
        ...

    def GetType(self) -> Type:
        """ GetType(self: _MethodInfo) -> Type """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _MethodInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _MethodInfo) -> UInt32 """
        ...

    def Invoke(self, *__args) -> Guid:
        """
        Invoke(self: _MethodInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid
        Invoke(self: _MethodInfo, obj: object, invokeAttr: BindingFlags, binder: Binder, parameters: Array[object], culture: CultureInfo) -> object
        Invoke(self: _MethodInfo, obj: object, parameters: Array[object]) -> object
        """
        ...

    def IsDefined(self, attributeType:Type, inherit:bool) -> bool:
        """ IsDefined(self: _MethodInfo, attributeType: Type, inherit: bool) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: _MethodInfo) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class _MethodRental: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _MethodRental, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _MethodRental, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _MethodRental) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _MethodRental, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _Module: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _Module, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _Module, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _Module) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _Module, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _ModuleBuilder: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _ModuleBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _ModuleBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _ModuleBuilder) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _ModuleBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _ParameterBuilder: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _ParameterBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _ParameterBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _ParameterBuilder) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _ParameterBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _ParameterInfo: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _ParameterInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _ParameterInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _ParameterInfo) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _ParameterInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _PropertyBuilder: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _PropertyBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _PropertyBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _PropertyBuilder) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _PropertyBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _PropertyInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Attributes(self) -> PropertyAttributes:
        """ Get: Attributes(self: _PropertyInfo) -> PropertyAttributes """
        ...

    @property
    def CanRead(self) -> bool:
        """ Get: CanRead(self: _PropertyInfo) -> bool """
        ...

    @property
    def CanWrite(self) -> bool:
        """ Get: CanWrite(self: _PropertyInfo) -> bool """
        ...

    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: _PropertyInfo) -> Type """
        ...

    @property
    def IsSpecialName(self) -> bool:
        """ Get: IsSpecialName(self: _PropertyInfo) -> bool """
        ...

    @property
    def MemberType(self) -> MemberTypes:
        """ Get: MemberType(self: _PropertyInfo) -> MemberTypes """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: _PropertyInfo) -> str """
        ...

    @property
    def PropertyType(self) -> Type:
        """ Get: PropertyType(self: _PropertyInfo) -> Type """
        ...

    @property
    def ReflectedType(self) -> Type:
        """ Get: ReflectedType(self: _PropertyInfo) -> Type """
        ...


    def Equals(self, other:object) -> bool:
        """ Equals(self: _PropertyInfo, other: object) -> bool """
        ...

    def GetAccessors(self, nonPublic:bool = ...) -> Array:
        """
        GetAccessors(self: _PropertyInfo, nonPublic: bool) -> Array[MethodInfo]
        GetAccessors(self: _PropertyInfo) -> Array[MethodInfo]
        """
        ...

    def GetCustomAttributes(self, *__args:bool) -> Array:
        """
        GetCustomAttributes(self: _PropertyInfo, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _PropertyInfo, inherit: bool) -> Array[object]
        """
        ...

    def GetGetMethod(self, nonPublic:bool = ...) -> MethodInfo:
        """
        GetGetMethod(self: _PropertyInfo, nonPublic: bool) -> MethodInfo
        GetGetMethod(self: _PropertyInfo) -> MethodInfo
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: _PropertyInfo) -> int """
        ...

    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _PropertyInfo, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetIndexParameters(self) -> Array:
        """ GetIndexParameters(self: _PropertyInfo) -> Array[ParameterInfo] """
        ...

    def GetSetMethod(self, nonPublic:bool = ...) -> MethodInfo:
        """
        GetSetMethod(self: _PropertyInfo, nonPublic: bool) -> MethodInfo
        GetSetMethod(self: _PropertyInfo) -> MethodInfo
        """
        ...

    def GetType(self) -> Type:
        """ GetType(self: _PropertyInfo) -> Type """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _PropertyInfo, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _PropertyInfo) -> UInt32 """
        ...

    def GetValue(self, obj:object, *__args:Array) -> object:
        """
        GetValue(self: _PropertyInfo, obj: object, index: Array[object]) -> object
        GetValue(self: _PropertyInfo, obj: object, invokeAttr: BindingFlags, binder: Binder, index: Array[object], culture: CultureInfo) -> object
        """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _PropertyInfo, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...

    def IsDefined(self, attributeType:Type, inherit:bool) -> bool:
        """ IsDefined(self: _PropertyInfo, attributeType: Type, inherit: bool) -> bool """
        ...

    def SetValue(self, obj:object, value:object, *__args:Array): # -> 
        """ SetValue(self: _PropertyInfo, obj: object, value: object, index: Array[object])SetValue(self: _PropertyInfo, obj: object, value: object, invokeAttr: BindingFlags, binder: Binder, index: Array[object], culture: CultureInfo) """
        ...

    def ToString(self) -> str:
        """ ToString(self: _PropertyInfo) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class _SignatureHelper: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _SignatureHelper, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _SignatureHelper, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _SignatureHelper) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _SignatureHelper, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _Thread: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _Thread, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _Thread, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _Thread) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _Thread, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


class _Type: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Assembly(self) -> Assembly:
        """ Get: Assembly(self: _Type) -> Assembly """
        ...

    @property
    def AssemblyQualifiedName(self) -> str:
        """ Get: AssemblyQualifiedName(self: _Type) -> str """
        ...

    @property
    def Attributes(self) -> TypeAttributes:
        """ Get: Attributes(self: _Type) -> TypeAttributes """
        ...

    @property
    def BaseType(self) -> Type:
        """ Get: BaseType(self: _Type) -> Type """
        ...

    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: _Type) -> Type """
        ...

    @property
    def FullName(self) -> str:
        """ Get: FullName(self: _Type) -> str """
        ...

    @property
    def GUID(self) -> Guid:
        """ Get: GUID(self: _Type) -> Guid """
        ...

    @property
    def HasElementType(self) -> bool:
        """ Get: HasElementType(self: _Type) -> bool """
        ...

    @property
    def IsAbstract(self) -> bool:
        """ Get: IsAbstract(self: _Type) -> bool """
        ...

    @property
    def IsAnsiClass(self) -> bool:
        """ Get: IsAnsiClass(self: _Type) -> bool """
        ...

    @property
    def IsArray(self) -> bool:
        """ Get: IsArray(self: _Type) -> bool """
        ...

    @property
    def IsAutoClass(self) -> bool:
        """ Get: IsAutoClass(self: _Type) -> bool """
        ...

    @property
    def IsAutoLayout(self) -> bool:
        """ Get: IsAutoLayout(self: _Type) -> bool """
        ...

    @property
    def IsByRef(self) -> bool:
        """ Get: IsByRef(self: _Type) -> bool """
        ...

    @property
    def IsClass(self) -> bool:
        """ Get: IsClass(self: _Type) -> bool """
        ...

    @property
    def IsCOMObject(self) -> bool:
        """ Get: IsCOMObject(self: _Type) -> bool """
        ...

    @property
    def IsContextful(self) -> bool:
        """ Get: IsContextful(self: _Type) -> bool """
        ...

    @property
    def IsEnum(self) -> bool:
        """ Get: IsEnum(self: _Type) -> bool """
        ...

    @property
    def IsExplicitLayout(self) -> bool:
        """ Get: IsExplicitLayout(self: _Type) -> bool """
        ...

    @property
    def IsImport(self) -> bool:
        """ Get: IsImport(self: _Type) -> bool """
        ...

    @property
    def IsInterface(self) -> bool:
        """ Get: IsInterface(self: _Type) -> bool """
        ...

    @property
    def IsLayoutSequential(self) -> bool:
        """ Get: IsLayoutSequential(self: _Type) -> bool """
        ...

    @property
    def IsMarshalByRef(self) -> bool:
        """ Get: IsMarshalByRef(self: _Type) -> bool """
        ...

    @property
    def IsNestedAssembly(self) -> bool:
        """ Get: IsNestedAssembly(self: _Type) -> bool """
        ...

    @property
    def IsNestedFamANDAssem(self) -> bool:
        """ Get: IsNestedFamANDAssem(self: _Type) -> bool """
        ...

    @property
    def IsNestedFamily(self) -> bool:
        """ Get: IsNestedFamily(self: _Type) -> bool """
        ...

    @property
    def IsNestedFamORAssem(self) -> bool:
        """ Get: IsNestedFamORAssem(self: _Type) -> bool """
        ...

    @property
    def IsNestedPrivate(self) -> bool:
        """ Get: IsNestedPrivate(self: _Type) -> bool """
        ...

    @property
    def IsNestedPublic(self) -> bool:
        """ Get: IsNestedPublic(self: _Type) -> bool """
        ...

    @property
    def IsNotPublic(self) -> bool:
        """ Get: IsNotPublic(self: _Type) -> bool """
        ...

    @property
    def IsPointer(self) -> bool:
        """ Get: IsPointer(self: _Type) -> bool """
        ...

    @property
    def IsPrimitive(self) -> bool:
        """ Get: IsPrimitive(self: _Type) -> bool """
        ...

    @property
    def IsPublic(self) -> bool:
        """ Get: IsPublic(self: _Type) -> bool """
        ...

    @property
    def IsSealed(self) -> bool:
        """ Get: IsSealed(self: _Type) -> bool """
        ...

    @property
    def IsSerializable(self) -> bool:
        """ Get: IsSerializable(self: _Type) -> bool """
        ...

    @property
    def IsSpecialName(self) -> bool:
        """ Get: IsSpecialName(self: _Type) -> bool """
        ...

    @property
    def IsUnicodeClass(self) -> bool:
        """ Get: IsUnicodeClass(self: _Type) -> bool """
        ...

    @property
    def IsValueType(self) -> bool:
        """ Get: IsValueType(self: _Type) -> bool """
        ...

    @property
    def MemberType(self) -> MemberTypes:
        """ Get: MemberType(self: _Type) -> MemberTypes """
        ...

    @property
    def Module(self) -> Module:
        """ Get: Module(self: _Type) -> Module """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: _Type) -> str """
        ...

    @property
    def Namespace(self) -> str:
        """ Get: Namespace(self: _Type) -> str """
        ...

    @property
    def ReflectedType(self) -> Type:
        """ Get: ReflectedType(self: _Type) -> Type """
        ...

    @property
    def TypeHandle(self) -> RuntimeTypeHandle:
        """ Get: TypeHandle(self: _Type) -> RuntimeTypeHandle """
        ...

    @property
    def TypeInitializer(self) -> ConstructorInfo:
        """ Get: TypeInitializer(self: _Type) -> ConstructorInfo """
        ...

    @property
    def UnderlyingSystemType(self) -> Type:
        """ Get: UnderlyingSystemType(self: _Type) -> Type """
        ...


    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: _Type, other: object) -> bool
        Equals(self: _Type, o: Type) -> bool
        """
        ...

    def FindInterfaces(self, filter:TypeFilter, filterCriteria:object) -> Array:
        """ FindInterfaces(self: _Type, filter: TypeFilter, filterCriteria: object) -> Array[Type] """
        ...

    def FindMembers(self, memberType:MemberTypes, bindingAttr:BindingFlags, filter:MemberFilter, filterCriteria:object) -> Array:
        """ FindMembers(self: _Type, memberType: MemberTypes, bindingAttr: BindingFlags, filter: MemberFilter, filterCriteria: object) -> Array[MemberInfo] """
        ...

    def GetArrayRank(self) -> int:
        """ GetArrayRank(self: _Type) -> int """
        ...

    def GetConstructor(self, *__args:Array) -> ConstructorInfo:
        """
        GetConstructor(self: _Type, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> ConstructorInfo
        GetConstructor(self: _Type, bindingAttr: BindingFlags, binder: Binder, types: Array[Type], modifiers: Array[ParameterModifier]) -> ConstructorInfo
        GetConstructor(self: _Type, types: Array[Type]) -> ConstructorInfo
        """
        ...

    def GetConstructors(self, bindingAttr:BindingFlags = ...) -> Array:
        """
        GetConstructors(self: _Type, bindingAttr: BindingFlags) -> Array[ConstructorInfo]
        GetConstructors(self: _Type) -> Array[ConstructorInfo]
        """
        ...

    def GetCustomAttributes(self, *__args:bool) -> Array:
        """
        GetCustomAttributes(self: _Type, attributeType: Type, inherit: bool) -> Array[object]
        GetCustomAttributes(self: _Type, inherit: bool) -> Array[object]
        """
        ...

    def GetDefaultMembers(self) -> Array:
        """ GetDefaultMembers(self: _Type) -> Array[MemberInfo] """
        ...

    def GetElementType(self) -> Type:
        """ GetElementType(self: _Type) -> Type """
        ...

    def GetEvent(self, name:str, bindingAttr:BindingFlags = ...) -> EventInfo:
        """
        GetEvent(self: _Type, name: str, bindingAttr: BindingFlags) -> EventInfo
        GetEvent(self: _Type, name: str) -> EventInfo
        """
        ...

    def GetEvents(self, bindingAttr:BindingFlags = ...) -> Array:
        """
        GetEvents(self: _Type) -> Array[EventInfo]
        GetEvents(self: _Type, bindingAttr: BindingFlags) -> Array[EventInfo]
        """
        ...

    def GetField(self, name:str, bindingAttr:BindingFlags = ...) -> FieldInfo:
        """
        GetField(self: _Type, name: str, bindingAttr: BindingFlags) -> FieldInfo
        GetField(self: _Type, name: str) -> FieldInfo
        """
        ...

    def GetFields(self, bindingAttr:BindingFlags = ...) -> Array:
        """
        GetFields(self: _Type, bindingAttr: BindingFlags) -> Array[FieldInfo]
        GetFields(self: _Type) -> Array[FieldInfo]
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: _Type) -> int """
        ...

    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _Type, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetInterface(self, name:str, ignoreCase:bool = ...) -> Type:
        """
        GetInterface(self: _Type, name: str, ignoreCase: bool) -> Type
        GetInterface(self: _Type, name: str) -> Type
        """
        ...

    def GetInterfaceMap(self, interfaceType:Type) -> InterfaceMapping:
        """ GetInterfaceMap(self: _Type, interfaceType: Type) -> InterfaceMapping """
        ...

    def GetInterfaces(self) -> Array:
        """ GetInterfaces(self: _Type) -> Array[Type] """
        ...

    def GetMember(self, name:str, *__args:BindingFlags) -> Array:
        """
        GetMember(self: _Type, name: str, type: MemberTypes, bindingAttr: BindingFlags) -> Array[MemberInfo]
        GetMember(self: _Type, name: str, bindingAttr: BindingFlags) -> Array[MemberInfo]
        GetMember(self: _Type, name: str) -> Array[MemberInfo]
        """
        ...

    def GetMembers(self, bindingAttr:BindingFlags = ...) -> Array:
        """
        GetMembers(self: _Type, bindingAttr: BindingFlags) -> Array[MemberInfo]
        GetMembers(self: _Type) -> Array[MemberInfo]
        """
        ...

    def GetMethod(self, name:str, *__args:BindingFlags) -> MethodInfo:
        """
        GetMethod(self: _Type, name: str, bindingAttr: BindingFlags, binder: Binder, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo
        GetMethod(self: _Type, name: str, bindingAttr: BindingFlags) -> MethodInfo
        GetMethod(self: _Type, name: str, bindingAttr: BindingFlags, binder: Binder, callConvention: CallingConventions, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo
        GetMethod(self: _Type, name: str, types: Array[Type], modifiers: Array[ParameterModifier]) -> MethodInfo
        GetMethod(self: _Type, name: str, types: Array[Type]) -> MethodInfo
        GetMethod(self: _Type, name: str) -> MethodInfo
        """
        ...

    def GetMethods(self, bindingAttr:BindingFlags = ...) -> Array:
        """
        GetMethods(self: _Type, bindingAttr: BindingFlags) -> Array[MethodInfo]
        GetMethods(self: _Type) -> Array[MethodInfo]
        """
        ...

    def GetNestedType(self, name:str, bindingAttr:BindingFlags = ...) -> Type:
        """
        GetNestedType(self: _Type, name: str, bindingAttr: BindingFlags) -> Type
        GetNestedType(self: _Type, name: str) -> Type
        """
        ...

    def GetNestedTypes(self, bindingAttr:BindingFlags = ...) -> Array:
        """
        GetNestedTypes(self: _Type, bindingAttr: BindingFlags) -> Array[Type]
        GetNestedTypes(self: _Type) -> Array[Type]
        """
        ...

    def GetProperties(self, bindingAttr:BindingFlags = ...) -> Array:
        """
        GetProperties(self: _Type, bindingAttr: BindingFlags) -> Array[PropertyInfo]
        GetProperties(self: _Type) -> Array[PropertyInfo]
        """
        ...

    def GetProperty(self, name:str, *__args:BindingFlags) -> PropertyInfo:
        """
        GetProperty(self: _Type, name: str, bindingAttr: BindingFlags) -> PropertyInfo
        GetProperty(self: _Type, name: str, bindingAttr: BindingFlags, binder: Binder, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo
        GetProperty(self: _Type, name: str, returnType: Type, types: Array[Type], modifiers: Array[ParameterModifier]) -> PropertyInfo
        GetProperty(self: _Type, name: str, returnType: Type, types: Array[Type]) -> PropertyInfo
        GetProperty(self: _Type, name: str, types: Array[Type]) -> PropertyInfo
        GetProperty(self: _Type, name: str, returnType: Type) -> PropertyInfo
        GetProperty(self: _Type, name: str) -> PropertyInfo
        """
        ...

    def GetType(self) -> Type:
        """ GetType(self: _Type) -> Type """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _Type, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _Type) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _Type, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...

    def InvokeMember(self, name:str, invokeAttr:BindingFlags, binder:Binder, target:object, args:Array, *__args:CultureInfo) -> object:
        """
        InvokeMember(self: _Type, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: Array[object], modifiers: Array[ParameterModifier], culture: CultureInfo, namedParameters: Array[str]) -> object
        InvokeMember(self: _Type, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: Array[object], culture: CultureInfo) -> object
        InvokeMember(self: _Type, name: str, invokeAttr: BindingFlags, binder: Binder, target: object, args: Array[object]) -> object
        """
        ...

    def IsAssignableFrom(self, c:Type) -> bool:
        """ IsAssignableFrom(self: _Type, c: Type) -> bool """
        ...

    def IsDefined(self, attributeType:Type, inherit:bool) -> bool:
        """ IsDefined(self: _Type, attributeType: Type, inherit: bool) -> bool """
        ...

    def IsInstanceOfType(self, o:object) -> bool:
        """ IsInstanceOfType(self: _Type, o: object) -> bool """
        ...

    def IsSubclassOf(self, c:Type) -> bool:
        """ IsSubclassOf(self: _Type, c: Type) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: _Type) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class _TypeBuilder: # skipped bases: <type 'object'>
    """ no doc """
    def GetIDsOfNames(self, riid:Guid, rgszNames:IntPtr, cNames:UInt32, lcid:UInt32, rgDispId:IntPtr) -> Guid:
        """ GetIDsOfNames(self: _TypeBuilder, riid: Guid, rgszNames: IntPtr, cNames: UInt32, lcid: UInt32, rgDispId: IntPtr) -> Guid """
        ...

    def GetTypeInfo(self, iTInfo:UInt32, lcid:UInt32, ppTInfo:IntPtr): # -> 
        """ GetTypeInfo(self: _TypeBuilder, iTInfo: UInt32, lcid: UInt32, ppTInfo: IntPtr) """
        ...

    def GetTypeInfoCount(self, pcTInfo) -> UInt32:
        """ GetTypeInfoCount(self: _TypeBuilder) -> UInt32 """
        ...

    def Invoke(self, dispIdMember:UInt32, riid:Guid, lcid:UInt32, wFlags:Int16, pDispParams:IntPtr, pVarResult:IntPtr, pExcepInfo:IntPtr, puArgErr:IntPtr) -> Guid:
        """ Invoke(self: _TypeBuilder, dispIdMember: UInt32, riid: Guid, lcid: UInt32, wFlags: Int16, pDispParams: IntPtr, pVarResult: IntPtr, pExcepInfo: IntPtr, puArgErr: IntPtr) -> Guid """
        ...


# variables with complex values

