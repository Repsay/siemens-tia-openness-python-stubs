# encoding: utf-8
# module System.Management calls itself Management
# from System.Management, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Management.Instrumentation, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, DateTime, Enum, EventArgs, 
    IAsyncResult, ICloneable, IDisposable, MulticastDelegate, SystemException, 
    TimeSpan)

from System.CodeDom import CodeTypeDeclaration

from System.Collections import ICollection

from System.Collections.Specialized import (NameObjectCollectionBase, 
    StringCollection)

from System.ComponentModel import Component

from System.Runtime.Serialization import ISerializable

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    ManagementObjectEnumerator, MethodDataEnumerator, PropertyDataEnumerator, 
    QualifierDataEnumerator, field#)
"""

# no functions
# classes

class AuthenticationLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AuthenticationLevel, values: Call (3), Connect (2), Default (0), None (1), Packet (4), PacketIntegrity (5), PacketPrivacy (6), Unchanged (-1) """
    def Call(self, *args): #cannot find CLR method
        """ enum AuthenticationLevel, values: Call (3), Connect (2), Default (0), None (1), Packet (4), PacketIntegrity (5), PacketPrivacy (6), Unchanged (-1) """
        ...

    def Connect(self, *args): #cannot find CLR method
        """ enum AuthenticationLevel, values: Call (3), Connect (2), Default (0), None (1), Packet (4), PacketIntegrity (5), PacketPrivacy (6), Unchanged (-1) """
        ...

    def Default(self, *args): #cannot find CLR method
        """ enum AuthenticationLevel, values: Call (3), Connect (2), Default (0), None (1), Packet (4), PacketIntegrity (5), PacketPrivacy (6), Unchanged (-1) """
        ...

    def None(self, *args): #cannot find CLR method
        """ enum AuthenticationLevel, values: Call (3), Connect (2), Default (0), None (1), Packet (4), PacketIntegrity (5), PacketPrivacy (6), Unchanged (-1) """
        ...

    def Packet(self, *args): #cannot find CLR method
        """ enum AuthenticationLevel, values: Call (3), Connect (2), Default (0), None (1), Packet (4), PacketIntegrity (5), PacketPrivacy (6), Unchanged (-1) """
        ...

    def PacketIntegrity(self, *args): #cannot find CLR method
        """ enum AuthenticationLevel, values: Call (3), Connect (2), Default (0), None (1), Packet (4), PacketIntegrity (5), PacketPrivacy (6), Unchanged (-1) """
        ...

    def PacketPrivacy(self, *args): #cannot find CLR method
        """ enum AuthenticationLevel, values: Call (3), Connect (2), Default (0), None (1), Packet (4), PacketIntegrity (5), PacketPrivacy (6), Unchanged (-1) """
        ...

    def Unchanged(self, *args): #cannot find CLR method
        """ enum AuthenticationLevel, values: Call (3), Connect (2), Default (0), None (1), Packet (4), PacketIntegrity (5), PacketPrivacy (6), Unchanged (-1) """
        ...

    def __call__(self, *args): #cannot find CLR method
        """ enum AuthenticationLevel, values: Call (3), Connect (2), Default (0), None (1), Packet (4), PacketIntegrity (5), PacketPrivacy (6), Unchanged (-1) """
        ...

    value__ = ...


class CimType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CimType, values: Boolean (11), Char16 (103), DateTime (101), None (0), Object (13), Real32 (4), Real64 (5), Reference (102), SInt16 (2), SInt32 (3), SInt64 (20), SInt8 (16), String (8), UInt16 (18), UInt32 (19), UInt64 (21), UInt8 (17) """
    Boolean: CimType = ...
    Char16: CimType = ...
    DateTime: CimType = ...
    Object: CimType = ...
    Real32: CimType = ...
    Real64: CimType = ...
    Reference: CimType = ...
    SInt16: CimType = ...
    SInt32: CimType = ...
    SInt64: CimType = ...
    SInt8: CimType = ...
    String: CimType = ...
    UInt16: CimType = ...
    UInt32: CimType = ...
    UInt64: CimType = ...
    UInt8: CimType = ...
    value__ = ...


class CodeLanguage(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CodeLanguage, values: CSharp (0), JScript (1), Mcpp (4), VB (2), VJSharp (3) """
    CSharp: CodeLanguage = ...
    JScript: CodeLanguage = ...
    Mcpp: CodeLanguage = ...
    value__ = ...
    VB: CodeLanguage = ...
    VJSharp: CodeLanguage = ...


class ComparisonSettings(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ComparisonSettings, values: IgnoreCase (16), IgnoreClass (8), IgnoreDefaultValues (4), IgnoreFlavor (32), IgnoreObjectSource (2), IgnoreQualifiers (1), IncludeAll (0) """
    IgnoreCase: ComparisonSettings = ...
    IgnoreClass: ComparisonSettings = ...
    IgnoreDefaultValues: ComparisonSettings = ...
    IgnoreFlavor: ComparisonSettings = ...
    IgnoreObjectSource: ComparisonSettings = ...
    IgnoreQualifiers: ComparisonSettings = ...
    IncludeAll: ComparisonSettings = ...
    value__ = ...


class ManagementEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Context(self) -> object:
        """ Get: Context(self: ManagementEventArgs) -> object """
        ...



class CompletedEventArgs(ManagementEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Status(self) -> ManagementStatus:
        """ Get: Status(self: CompletedEventArgs) -> ManagementStatus """
        ...

    @property
    def StatusObject(self) -> ManagementBaseObject:
        """ Get: StatusObject(self: CompletedEventArgs) -> ManagementBaseObject """
        ...



class CompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ CompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:CompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: CompletedEventHandler, sender: object, e: CompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: CompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:CompletedEventArgs): # -> 
        """ Invoke(self: CompletedEventHandler, sender: object, e: CompletedEventArgs) """
        ...


class ManagementOptions(ICloneable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Context(self) -> ManagementNamedValueCollection:
        """
        Get: Context(self: ManagementOptions) -> ManagementNamedValueCollection
        Set: Context(self: ManagementOptions) = value
        """
        ...

    @property
    def Timeout(self) -> TimeSpan:
        """
        Get: Timeout(self: ManagementOptions) -> TimeSpan
        Set: Timeout(self: ManagementOptions) = value
        """
        ...


    InfiniteTimeout: TimeSpan = ...


class ConnectionOptions(ManagementOptions): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    ConnectionOptions()
    ConnectionOptions(locale: str, username: str, password: str, authority: str, impersonation: ImpersonationLevel, authentication: AuthenticationLevel, enablePrivileges: bool, context: ManagementNamedValueCollection, timeout: TimeSpan)
    ConnectionOptions(locale: str, username: str, password: SecureString, authority: str, impersonation: ImpersonationLevel, authentication: AuthenticationLevel, enablePrivileges: bool, context: ManagementNamedValueCollection, timeout: TimeSpan)
    """
    @property
    def Authentication(self) -> AuthenticationLevel:
        """
        Get: Authentication(self: ConnectionOptions) -> AuthenticationLevel
        Set: Authentication(self: ConnectionOptions) = value
        """
        ...

    @property
    def Authority(self) -> str:
        """
        Get: Authority(self: ConnectionOptions) -> str
        Set: Authority(self: ConnectionOptions) = value
        """
        ...

    @property
    def EnablePrivileges(self) -> bool:
        """
        Get: EnablePrivileges(self: ConnectionOptions) -> bool
        Set: EnablePrivileges(self: ConnectionOptions) = value
        """
        ...

    @property
    def Impersonation(self) -> ImpersonationLevel:
        """
        Get: Impersonation(self: ConnectionOptions) -> ImpersonationLevel
        Set: Impersonation(self: ConnectionOptions) = value
        """
        ...

    @property
    def Locale(self) -> str:
        """
        Get: Locale(self: ConnectionOptions) -> str
        Set: Locale(self: ConnectionOptions) = value
        """
        ...

    @property
    def Password(self): # -> 
        """ Set: Password(self: ConnectionOptions) = value """
        ...

    @property
    def SecurePassword(self): # -> 
        """ Set: SecurePassword(self: ConnectionOptions) = value """
        ...

    @property
    def Username(self) -> str:
        """
        Get: Username(self: ConnectionOptions) -> str
        Set: Username(self: ConnectionOptions) = value
        """
        ...


    def __new__(cls, locale:str = ..., username:str = ..., password:str = ..., authority:str = ..., impersonation:ImpersonationLevel = ..., authentication:AuthenticationLevel = ..., enablePrivileges:bool = ..., context:ManagementNamedValueCollection = ..., timeout:TimeSpan = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, locale: str, username: str, password: str, authority: str, impersonation: ImpersonationLevel, authentication: AuthenticationLevel, enablePrivileges: bool, context: ManagementNamedValueCollection, timeout: TimeSpan)
        __new__(cls: type, locale: str, username: str, password: SecureString, authority: str, impersonation: ImpersonationLevel, authentication: AuthenticationLevel, enablePrivileges: bool, context: ManagementNamedValueCollection, timeout: TimeSpan)
        """
        ...


class DeleteOptions(ManagementOptions): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    DeleteOptions()
    DeleteOptions(context: ManagementNamedValueCollection, timeout: TimeSpan)
    """
    def __new__(cls, context:ManagementNamedValueCollection = ..., timeout:TimeSpan = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, context: ManagementNamedValueCollection, timeout: TimeSpan)
        """
        ...


class EnumerationOptions(ManagementOptions): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    EnumerationOptions()
    EnumerationOptions(context: ManagementNamedValueCollection, timeout: TimeSpan, blockSize: int, rewindable: bool, returnImmediatley: bool, useAmendedQualifiers: bool, ensureLocatable: bool, prototypeOnly: bool, directRead: bool, enumerateDeep: bool)
    """
    @property
    def BlockSize(self) -> int:
        """
        Get: BlockSize(self: EnumerationOptions) -> int
        Set: BlockSize(self: EnumerationOptions) = value
        """
        ...

    @property
    def DirectRead(self) -> bool:
        """
        Get: DirectRead(self: EnumerationOptions) -> bool
        Set: DirectRead(self: EnumerationOptions) = value
        """
        ...

    @property
    def EnsureLocatable(self) -> bool:
        """
        Get: EnsureLocatable(self: EnumerationOptions) -> bool
        Set: EnsureLocatable(self: EnumerationOptions) = value
        """
        ...

    @property
    def EnumerateDeep(self) -> bool:
        """
        Get: EnumerateDeep(self: EnumerationOptions) -> bool
        Set: EnumerateDeep(self: EnumerationOptions) = value
        """
        ...

    @property
    def PrototypeOnly(self) -> bool:
        """
        Get: PrototypeOnly(self: EnumerationOptions) -> bool
        Set: PrototypeOnly(self: EnumerationOptions) = value
        """
        ...

    @property
    def ReturnImmediately(self) -> bool:
        """
        Get: ReturnImmediately(self: EnumerationOptions) -> bool
        Set: ReturnImmediately(self: EnumerationOptions) = value
        """
        ...

    @property
    def Rewindable(self) -> bool:
        """
        Get: Rewindable(self: EnumerationOptions) -> bool
        Set: Rewindable(self: EnumerationOptions) = value
        """
        ...

    @property
    def UseAmendedQualifiers(self) -> bool:
        """
        Get: UseAmendedQualifiers(self: EnumerationOptions) -> bool
        Set: UseAmendedQualifiers(self: EnumerationOptions) = value
        """
        ...


    def __new__(cls, context:ManagementNamedValueCollection = ..., timeout:TimeSpan = ..., blockSize:int = ..., rewindable:bool = ..., returnImmediatley:bool = ..., useAmendedQualifiers:bool = ..., ensureLocatable:bool = ..., prototypeOnly:bool = ..., directRead:bool = ..., enumerateDeep:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, context: ManagementNamedValueCollection, timeout: TimeSpan, blockSize: int, rewindable: bool, returnImmediatley: bool, useAmendedQualifiers: bool, ensureLocatable: bool, prototypeOnly: bool, directRead: bool, enumerateDeep: bool)
        """
        ...


class EventArrivedEventArgs(ManagementEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def NewEvent(self) -> ManagementBaseObject:
        """ Get: NewEvent(self: EventArrivedEventArgs) -> ManagementBaseObject """
        ...



class EventArrivedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EventArrivedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:EventArrivedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: EventArrivedEventHandler, sender: object, e: EventArrivedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: EventArrivedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:EventArrivedEventArgs): # -> 
        """ Invoke(self: EventArrivedEventHandler, sender: object, e: EventArrivedEventArgs) """
        ...


class ManagementQuery(ICloneable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def QueryLanguage(self) -> str:
        """
        Get: QueryLanguage(self: ManagementQuery) -> str
        Set: QueryLanguage(self: ManagementQuery) = value
        """
        ...

    @property
    def QueryString(self) -> str:
        """
        Get: QueryString(self: ManagementQuery) -> str
        Set: QueryString(self: ManagementQuery) = value
        """
        ...


    def ParseQuery(self, *args): #cannot find CLR method
        """ ParseQuery(self: ManagementQuery, query: str) """
        ...


class EventQuery(ManagementQuery): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    EventQuery()
    EventQuery(query: str)
    EventQuery(language: str, query: str)
    """
    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, query: str)
        __new__(cls: type, language: str, query: str)
        """
        ...


class EventWatcherOptions(ManagementOptions): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    EventWatcherOptions()
    EventWatcherOptions(context: ManagementNamedValueCollection, timeout: TimeSpan, blockSize: int)
    """
    @property
    def BlockSize(self) -> int:
        """
        Get: BlockSize(self: EventWatcherOptions) -> int
        Set: BlockSize(self: EventWatcherOptions) = value
        """
        ...


    def __new__(cls, context:ManagementNamedValueCollection = ..., timeout:TimeSpan = ..., blockSize:int = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, context: ManagementNamedValueCollection, timeout: TimeSpan, blockSize: int)
        """
        ...


class ImpersonationLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ImpersonationLevel, values: Anonymous (1), Default (0), Delegate (4), Identify (2), Impersonate (3) """
    Anonymous: ImpersonationLevel = ...
    Default: ImpersonationLevel = ...
    Delegate: ImpersonationLevel = ...
    Identify: ImpersonationLevel = ...
    Impersonate: ImpersonationLevel = ...
    value__ = ...


class InvokeMethodOptions(ManagementOptions): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    InvokeMethodOptions()
    InvokeMethodOptions(context: ManagementNamedValueCollection, timeout: TimeSpan)
    """
    def __new__(cls, context:ManagementNamedValueCollection = ..., timeout:TimeSpan = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, context: ManagementNamedValueCollection, timeout: TimeSpan)
        """
        ...


class ManagementBaseObject(ICloneable, ISerializable, Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def ClassPath(self) -> ManagementPath:
        """ Get: ClassPath(self: ManagementBaseObject) -> ManagementPath """
        ...

    @property
    def Properties(self) -> PropertyDataCollection:
        """ Get: Properties(self: ManagementBaseObject) -> PropertyDataCollection """
        ...

    @property
    def Qualifiers(self) -> QualifierDataCollection:
        """ Get: Qualifiers(self: ManagementBaseObject) -> QualifierDataCollection """
        ...

    @property
    def SystemProperties(self) -> PropertyDataCollection:
        """ Get: SystemProperties(self: ManagementBaseObject) -> PropertyDataCollection """
        ...


    def CompareTo(self, otherObject:ManagementBaseObject, settings:ComparisonSettings) -> bool:
        """ CompareTo(self: ManagementBaseObject, otherObject: ManagementBaseObject, settings: ComparisonSettings) -> bool """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: ManagementBaseObject, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ManagementBaseObject) -> int """
        ...

    def GetPropertyQualifierValue(self, propertyName:str, qualifierName:str) -> object:
        """ GetPropertyQualifierValue(self: ManagementBaseObject, propertyName: str, qualifierName: str) -> object """
        ...

    def GetPropertyValue(self, propertyName:str) -> object:
        """ GetPropertyValue(self: ManagementBaseObject, propertyName: str) -> object """
        ...

    def GetQualifierValue(self, qualifierName:str) -> object:
        """ GetQualifierValue(self: ManagementBaseObject, qualifierName: str) -> object """
        ...

    def GetText(self, format:TextFormat) -> str:
        """ GetText(self: ManagementBaseObject, format: TextFormat) -> str """
        ...

    def SetPropertyQualifierValue(self, propertyName:str, qualifierName:str, qualifierValue:object): # -> 
        """ SetPropertyQualifierValue(self: ManagementBaseObject, propertyName: str, qualifierName: str, qualifierValue: object) """
        ...

    def SetPropertyValue(self, propertyName:str, propertyValue:object): # -> 
        """ SetPropertyValue(self: ManagementBaseObject, propertyName: str, propertyValue: object) """
        ...

    def SetQualifierValue(self, qualifierName:str, qualifierValue:object): # -> 
        """ SetQualifierValue(self: ManagementBaseObject, qualifierName: str, qualifierValue: object) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, info: SerializationInfo, context: StreamingContext) """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ManagementObject(ManagementBaseObject): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """
    ManagementObject()
    ManagementObject(path: ManagementPath)
    ManagementObject(path: str)
    ManagementObject(path: ManagementPath, options: ObjectGetOptions)
    ManagementObject(path: str, options: ObjectGetOptions)
    ManagementObject(scope: ManagementScope, path: ManagementPath, options: ObjectGetOptions)
    ManagementObject(scopeString: str, pathString: str, options: ObjectGetOptions)
    """
    @property
    def Options(self) -> ObjectGetOptions:
        """
        Get: Options(self: ManagementObject) -> ObjectGetOptions
        Set: Options(self: ManagementObject) = value
        """
        ...

    @property
    def Path(self) -> ManagementPath:
        """
        Get: Path(self: ManagementObject) -> ManagementPath
        Set: Path(self: ManagementObject) = value
        """
        ...

    @property
    def Scope(self) -> ManagementScope:
        """
        Get: Scope(self: ManagementObject) -> ManagementScope
        Set: Scope(self: ManagementObject) = value
        """
        ...


    def CopyTo(self, *__args:ManagementPath) -> ManagementPath:
        """
        CopyTo(self: ManagementObject, path: ManagementPath) -> ManagementPath
        CopyTo(self: ManagementObject, path: str) -> ManagementPath
        CopyTo(self: ManagementObject, path: str, options: PutOptions) -> ManagementPath
        CopyTo(self: ManagementObject, path: ManagementPath, options: PutOptions) -> ManagementPath
        CopyTo(self: ManagementObject, watcher: ManagementOperationObserver, path: ManagementPath)CopyTo(self: ManagementObject, watcher: ManagementOperationObserver, path: str)CopyTo(self: ManagementObject, watcher: ManagementOperationObserver, path: str, options: PutOptions)CopyTo(self: ManagementObject, watcher: ManagementOperationObserver, path: ManagementPath, options: PutOptions)
        """
        ...

    def Delete(self, *__args:DeleteOptions): # -> 
        """ Delete(self: ManagementObject)Delete(self: ManagementObject, options: DeleteOptions)Delete(self: ManagementObject, watcher: ManagementOperationObserver)Delete(self: ManagementObject, watcher: ManagementOperationObserver, options: DeleteOptions) """
        ...

    def Get(self, watcher:ManagementOperationObserver = ...): # -> 
        """ Get(self: ManagementObject)Get(self: ManagementObject, watcher: ManagementOperationObserver) """
        ...

    def GetMethodParameters(self, methodName:str) -> ManagementBaseObject:
        """ GetMethodParameters(self: ManagementObject, methodName: str) -> ManagementBaseObject """
        ...

    def GetRelated(self, *__args:str) -> ManagementObjectCollection:
        """
        GetRelated(self: ManagementObject) -> ManagementObjectCollection
        GetRelated(self: ManagementObject, relatedClass: str) -> ManagementObjectCollection
        GetRelated(self: ManagementObject, relatedClass: str, relationshipClass: str, relationshipQualifier: str, relatedQualifier: str, relatedRole: str, thisRole: str, classDefinitionsOnly: bool, options: EnumerationOptions) -> ManagementObjectCollection
        GetRelated(self: ManagementObject, watcher: ManagementOperationObserver)GetRelated(self: ManagementObject, watcher: ManagementOperationObserver, relatedClass: str)GetRelated(self: ManagementObject, watcher: ManagementOperationObserver, relatedClass: str, relationshipClass: str, relationshipQualifier: str, relatedQualifier: str, relatedRole: str, thisRole: str, classDefinitionsOnly: bool, options: EnumerationOptions)
        """
        ...

    def GetRelationships(self, *__args:str) -> ManagementObjectCollection:
        """
        GetRelationships(self: ManagementObject) -> ManagementObjectCollection
        GetRelationships(self: ManagementObject, relationshipClass: str) -> ManagementObjectCollection
        GetRelationships(self: ManagementObject, relationshipClass: str, relationshipQualifier: str, thisRole: str, classDefinitionsOnly: bool, options: EnumerationOptions) -> ManagementObjectCollection
        GetRelationships(self: ManagementObject, watcher: ManagementOperationObserver)GetRelationships(self: ManagementObject, watcher: ManagementOperationObserver, relationshipClass: str)GetRelationships(self: ManagementObject, watcher: ManagementOperationObserver, relationshipClass: str, relationshipQualifier: str, thisRole: str, classDefinitionsOnly: bool, options: EnumerationOptions)
        """
        ...

    def InvokeMethod(self, *__args) -> object:
        """
        InvokeMethod(self: ManagementObject, methodName: str, args: Array[object]) -> object
        InvokeMethod(self: ManagementObject, watcher: ManagementOperationObserver, methodName: str, args: Array[object])InvokeMethod(self: ManagementObject, methodName: str, inParameters: ManagementBaseObject, options: InvokeMethodOptions) -> ManagementBaseObject
        InvokeMethod(self: ManagementObject, watcher: ManagementOperationObserver, methodName: str, inParameters: ManagementBaseObject, options: InvokeMethodOptions)
        """
        ...

    def Put(self, *__args:PutOptions) -> ManagementPath:
        """
        Put(self: ManagementObject) -> ManagementPath
        Put(self: ManagementObject, options: PutOptions) -> ManagementPath
        Put(self: ManagementObject, watcher: ManagementOperationObserver)Put(self: ManagementObject, watcher: ManagementOperationObserver, options: PutOptions)
        """
        ...

    def ToString(self) -> str:
        """ ToString(self: ManagementObject) -> str """
        ...


class ManagementClass(ManagementObject): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """
    ManagementClass()
    ManagementClass(path: ManagementPath)
    ManagementClass(path: str)
    ManagementClass(path: ManagementPath, options: ObjectGetOptions)
    ManagementClass(path: str, options: ObjectGetOptions)
    ManagementClass(scope: ManagementScope, path: ManagementPath, options: ObjectGetOptions)
    ManagementClass(scope: str, path: str, options: ObjectGetOptions)
    """
    @property
    def Derivation(self) -> StringCollection:
        """ Get: Derivation(self: ManagementClass) -> StringCollection """
        ...

    @property
    def Methods(self) -> MethodDataCollection:
        """ Get: Methods(self: ManagementClass) -> MethodDataCollection """
        ...


    def CreateInstance(self) -> ManagementObject:
        """ CreateInstance(self: ManagementClass) -> ManagementObject """
        ...

    def Derive(self, newClassName:str) -> ManagementClass:
        """ Derive(self: ManagementClass, newClassName: str) -> ManagementClass """
        ...

    def GetInstances(self, *__args:EnumerationOptions) -> ManagementObjectCollection:
        """
        GetInstances(self: ManagementClass) -> ManagementObjectCollection
        GetInstances(self: ManagementClass, options: EnumerationOptions) -> ManagementObjectCollection
        GetInstances(self: ManagementClass, watcher: ManagementOperationObserver)GetInstances(self: ManagementClass, watcher: ManagementOperationObserver, options: EnumerationOptions)
        """
        ...

    def GetRelatedClasses(self, *__args:str) -> ManagementObjectCollection:
        """
        GetRelatedClasses(self: ManagementClass) -> ManagementObjectCollection
        GetRelatedClasses(self: ManagementClass, relatedClass: str) -> ManagementObjectCollection
        GetRelatedClasses(self: ManagementClass, relatedClass: str, relationshipClass: str, relationshipQualifier: str, relatedQualifier: str, relatedRole: str, thisRole: str, options: EnumerationOptions) -> ManagementObjectCollection
        GetRelatedClasses(self: ManagementClass, watcher: ManagementOperationObserver)GetRelatedClasses(self: ManagementClass, watcher: ManagementOperationObserver, relatedClass: str)GetRelatedClasses(self: ManagementClass, watcher: ManagementOperationObserver, relatedClass: str, relationshipClass: str, relationshipQualifier: str, relatedQualifier: str, relatedRole: str, thisRole: str, options: EnumerationOptions)
        """
        ...

    def GetRelationshipClasses(self, *__args:str) -> ManagementObjectCollection:
        """
        GetRelationshipClasses(self: ManagementClass) -> ManagementObjectCollection
        GetRelationshipClasses(self: ManagementClass, relationshipClass: str) -> ManagementObjectCollection
        GetRelationshipClasses(self: ManagementClass, relationshipClass: str, relationshipQualifier: str, thisRole: str, options: EnumerationOptions) -> ManagementObjectCollection
        GetRelationshipClasses(self: ManagementClass, watcher: ManagementOperationObserver)GetRelationshipClasses(self: ManagementClass, watcher: ManagementOperationObserver, relationshipClass: str)GetRelationshipClasses(self: ManagementClass, watcher: ManagementOperationObserver, relationshipClass: str, relationshipQualifier: str, thisRole: str, options: EnumerationOptions)
        """
        ...

    def GetStronglyTypedClassCode(self, *__args) -> CodeTypeDeclaration:
        """
        GetStronglyTypedClassCode(self: ManagementClass, includeSystemClassInClassDef: bool, systemPropertyClass: bool) -> CodeTypeDeclaration
        GetStronglyTypedClassCode(self: ManagementClass, lang: CodeLanguage, filePath: str, classNamespace: str) -> bool
        """
        ...

    def GetSubclasses(self, *__args:EnumerationOptions) -> ManagementObjectCollection:
        """
        GetSubclasses(self: ManagementClass) -> ManagementObjectCollection
        GetSubclasses(self: ManagementClass, options: EnumerationOptions) -> ManagementObjectCollection
        GetSubclasses(self: ManagementClass, watcher: ManagementOperationObserver)GetSubclasses(self: ManagementClass, watcher: ManagementOperationObserver, options: EnumerationOptions)
        """
        ...


class ManagementDateTimeConverter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def ToDateTime(dmtfDate:str) -> DateTime:
        """ ToDateTime(dmtfDate: str) -> DateTime """
        ...

    @staticmethod
    def ToDmtfDateTime(date:DateTime) -> str:
        """ ToDmtfDateTime(date: DateTime) -> str """
        ...

    @staticmethod
    def ToDmtfTimeInterval(timespan:TimeSpan) -> str:
        """ ToDmtfTimeInterval(timespan: TimeSpan) -> str """
        ...

    @staticmethod
    def ToTimeSpan(dmtfTimespan:str) -> TimeSpan:
        """ ToTimeSpan(dmtfTimespan: str) -> TimeSpan """
        ...


class ManagementEventWatcher(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    ManagementEventWatcher()
    ManagementEventWatcher(query: EventQuery)
    ManagementEventWatcher(query: str)
    ManagementEventWatcher(scope: ManagementScope, query: EventQuery)
    ManagementEventWatcher(scope: str, query: str)
    ManagementEventWatcher(scope: str, query: str, options: EventWatcherOptions)
    ManagementEventWatcher(scope: ManagementScope, query: EventQuery, options: EventWatcherOptions)
    """
    @property
    def Options(self) -> EventWatcherOptions:
        """
        Get: Options(self: ManagementEventWatcher) -> EventWatcherOptions
        Set: Options(self: ManagementEventWatcher) = value
        """
        ...

    @property
    def Query(self) -> EventQuery:
        """
        Get: Query(self: ManagementEventWatcher) -> EventQuery
        Set: Query(self: ManagementEventWatcher) = value
        """
        ...

    @property
    def Scope(self) -> ManagementScope:
        """
        Get: Scope(self: ManagementEventWatcher) -> ManagementScope
        Set: Scope(self: ManagementEventWatcher) = value
        """
        ...


    def Start(self): # -> 
        """ Start(self: ManagementEventWatcher) """
        ...

    def Stop(self): # -> 
        """ Stop(self: ManagementEventWatcher) """
        ...

    def WaitForNextEvent(self) -> ManagementBaseObject:
        """ WaitForNextEvent(self: ManagementEventWatcher) -> ManagementBaseObject """
        ...

    def __new__(cls, *__args:EventQuery) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, query: EventQuery)
        __new__(cls: type, query: str)
        __new__(cls: type, scope: ManagementScope, query: EventQuery)
        __new__(cls: type, scope: str, query: str)
        __new__(cls: type, scope: str, query: str, options: EventWatcherOptions)
        __new__(cls: type, scope: ManagementScope, query: EventQuery, options: EventWatcherOptions)
        """
        ...

    EventArrived = ...
    Stopped = ...


class ManagementException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ManagementException()
    ManagementException(message: str)
    ManagementException(message: str, innerException: Exception)
    """
    @property
    def ErrorCode(self) -> ManagementStatus:
        """ Get: ErrorCode(self: ManagementException) -> ManagementStatus """
        ...

    @property
    def ErrorInformation(self) -> ManagementBaseObject:
        """ Get: ErrorInformation(self: ManagementException) -> ManagementBaseObject """
        ...


    SerializeObjectState = ...


class ManagementNamedValueCollection(NameObjectCollectionBase): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ ManagementNamedValueCollection() """
    def Add(self, name:str, value:object): # -> 
        """ Add(self: ManagementNamedValueCollection, name: str, value: object) """
        ...

    def Clone(self) -> ManagementNamedValueCollection:
        """ Clone(self: ManagementNamedValueCollection) -> ManagementNamedValueCollection """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: ManagementNamedValueCollection, name: str) """
        ...

    def RemoveAll(self): # -> 
        """ RemoveAll(self: ManagementNamedValueCollection) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class ManagementObjectCollection(IDisposable, ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def GetEnumerator(self): # -> ManagementObjectEnumerator
        """ GetEnumerator(self: ManagementObjectCollection) -> ManagementObjectEnumerator """
        ...

    def ManagementObjectEnumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class ManagementObjectSearcher(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    ManagementObjectSearcher()
    ManagementObjectSearcher(queryString: str)
    ManagementObjectSearcher(query: ObjectQuery)
    ManagementObjectSearcher(scope: str, queryString: str)
    ManagementObjectSearcher(scope: ManagementScope, query: ObjectQuery)
    ManagementObjectSearcher(scope: str, queryString: str, options: EnumerationOptions)
    ManagementObjectSearcher(scope: ManagementScope, query: ObjectQuery, options: EnumerationOptions)
    """
    @property
    def Options(self) -> EnumerationOptions:
        """
        Get: Options(self: ManagementObjectSearcher) -> EnumerationOptions
        Set: Options(self: ManagementObjectSearcher) = value
        """
        ...

    @property
    def Query(self) -> ObjectQuery:
        """
        Get: Query(self: ManagementObjectSearcher) -> ObjectQuery
        Set: Query(self: ManagementObjectSearcher) = value
        """
        ...

    @property
    def Scope(self) -> ManagementScope:
        """
        Get: Scope(self: ManagementObjectSearcher) -> ManagementScope
        Set: Scope(self: ManagementObjectSearcher) = value
        """
        ...


    def Get(self, watcher:ManagementOperationObserver = ...): # -> 
        """
        Get(self: ManagementObjectSearcher) -> ManagementObjectCollection
        Get(self: ManagementObjectSearcher, watcher: ManagementOperationObserver)
        """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, queryString: str)
        __new__(cls: type, query: ObjectQuery)
        __new__(cls: type, scope: str, queryString: str)
        __new__(cls: type, scope: ManagementScope, query: ObjectQuery)
        __new__(cls: type, scope: str, queryString: str, options: EnumerationOptions)
        __new__(cls: type, scope: ManagementScope, query: ObjectQuery, options: EnumerationOptions)
        """
        ...


class ManagementOperationObserver: # skipped bases: <type 'object'>, <type 'object'>
    """ ManagementOperationObserver() """
    def Cancel(self): # -> 
        """ Cancel(self: ManagementOperationObserver) """
        ...

    Completed = ...
    ObjectPut = ...
    ObjectReady = ...
    Progress = ...


class ManagementPath(ICloneable): # skipped bases: <type 'object'>
    """
    ManagementPath()
    ManagementPath(path: str)
    """
    @property
    def ClassName(self) -> str:
        """
        Get: ClassName(self: ManagementPath) -> str
        Set: ClassName(self: ManagementPath) = value
        """
        ...

    @property
    def DefaultPath(self) -> ManagementPath:
        """
        Get: DefaultPath() -> ManagementPath
        Set: DefaultPath() = value
        """
        ...

    @property
    def IsClass(self) -> bool:
        """ Get: IsClass(self: ManagementPath) -> bool """
        ...

    @property
    def IsInstance(self) -> bool:
        """ Get: IsInstance(self: ManagementPath) -> bool """
        ...

    @property
    def IsSingleton(self) -> bool:
        """ Get: IsSingleton(self: ManagementPath) -> bool """
        ...

    @property
    def NamespacePath(self) -> str:
        """
        Get: NamespacePath(self: ManagementPath) -> str
        Set: NamespacePath(self: ManagementPath) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: ManagementPath) -> str
        Set: Path(self: ManagementPath) = value
        """
        ...

    @property
    def RelativePath(self) -> str:
        """
        Get: RelativePath(self: ManagementPath) -> str
        Set: RelativePath(self: ManagementPath) = value
        """
        ...

    @property
    def Server(self) -> str:
        """
        Get: Server(self: ManagementPath) -> str
        Set: Server(self: ManagementPath) = value
        """
        ...


    def SetAsClass(self): # -> 
        """ SetAsClass(self: ManagementPath) """
        ...

    def SetAsSingleton(self): # -> 
        """ SetAsSingleton(self: ManagementPath) """
        ...

    def ToString(self) -> str:
        """ ToString(self: ManagementPath) -> str """
        ...



class ManagementScope(ICloneable): # skipped bases: <type 'object'>
    """
    ManagementScope()
    ManagementScope(path: ManagementPath)
    ManagementScope(path: str)
    ManagementScope(path: str, options: ConnectionOptions)
    ManagementScope(path: ManagementPath, options: ConnectionOptions)
    """
    @property
    def IsConnected(self) -> bool:
        """ Get: IsConnected(self: ManagementScope) -> bool """
        ...

    @property
    def Options(self) -> ConnectionOptions:
        """
        Get: Options(self: ManagementScope) -> ConnectionOptions
        Set: Options(self: ManagementScope) = value
        """
        ...

    @property
    def Path(self) -> ManagementPath:
        """
        Get: Path(self: ManagementScope) -> ManagementPath
        Set: Path(self: ManagementScope) = value
        """
        ...


    def Connect(self): # -> 
        """ Connect(self: ManagementScope) """
        ...


class ManagementStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ManagementStatus, values: AccessDenied (-2147217405), AggregatingByObject (-2147217315), AlreadyExists (-2147217383), AmendedObject (-2147217306), BackupRestoreWinmgmtRunning (-2147217312), BufferTooSmall (-2147217348), CallCanceled (-2147217358), CannotBeAbstract (-2147217307), CannotBeKey (-2147217377), CannotBeSingleton (-2147217364), CannotChangeIndexInheritance (-2147217328), CannotChangeKeyInheritance (-2147217335), CircularReference (-2147217337), ClassHasChildren (-2147217371), ClassHasInstances (-2147217370), ClientTooSlow (-2147217305), CriticalError (-2147217398), Different (262147), DuplicateObjects (262152), Failed (-2147217407), False (1), IllegalNull (-2147217368), IllegalOperation (-2147217378), IncompleteClass (-2147217376), InitializationFailure (-2147217388), InvalidCimType (-2147217363), InvalidClass (-2147217392), InvalidContext (-2147217401), InvalidDuplicateParameter (-2147217341), InvalidFlavor (-2147217338), InvalidMethod (-2147217362), InvalidMethodParameters (-2147217361), InvalidNamespace (-2147217394), InvalidObject (-2147217393), InvalidObjectPath (-2147217350), InvalidOperation (-2147217386), InvalidOperator (-2147217309), InvalidParameter (-2147217400), InvalidParameterID (-2147217353), InvalidProperty (-2147217359), InvalidPropertyType (-2147217366), InvalidProviderRegistration (-2147217390), InvalidQualifier (-2147217342), InvalidQualifierType (-2147217367), InvalidQuery (-2147217385), InvalidQueryType (-2147217384), InvalidStream (-2147217397), InvalidSuperclass (-2147217395), InvalidSyntax (-2147217375), LocalCredentials (-2147217308), MarshalInvalidSignature (-2147217343), MarshalVersionMismatch (-2147217344), MethodDisabled (-2147217322), MethodNotImplemented (-2147217323), MissingAggregationList (-2147217317), MissingGroupWithin (-2147217318), MissingParameterID (-2147217354), NoError (0), NoMoreData (262149), NonconsecutiveParameterIDs (-2147217352), NondecoratedObject (-2147217374), NotAvailable (-2147217399), NotEventClass (-2147217319), NotFound (-2147217406), NotSupported (-2147217396), OperationCanceled (262150), OutOfDiskSpace (-2147217349), OutOfMemory (-2147217402), OverrideNotAllowed (-2147217382), ParameterIDOnRetval (-2147217351), PartialResults (262160), Pending (262151), PrivilegeNotHeld (-2147217310), PropagatedMethod (-2147217356), PropagatedProperty (-2147217380), PropagatedQualifier (-2147217381), PropertyNotAnObject (-2147217316), ProviderFailure (-2147217404), ProviderLoadFailure (-2147217389), ProviderNotCapable (-2147217372), ProviderNotFound (-2147217391), QueryNotImplemented (-2147217369), QueueOverflow (-2147217311), ReadOnly (-2147217373), RefresherBusy (-2147217321), RegistrationTooBroad (-2147213311), RegistrationTooPrecise (-2147213310), ResetToDefault (262146), ServerTooBusy (-2147217339), ShuttingDown (-2147217357), SystemProperty (-2147217360), Timedout (262148), TooManyProperties (-2147217327), TooMuchData (-2147217340), TransportFailure (-2147217387), TypeMismatch (-2147217403), Unexpected (-2147217379), UninterpretableProviderQuery (-2147217313), UnknownObjectType (-2147217346), UnknownPacketType (-2147217345), UnparsableQuery (-2147217320), UnsupportedClassUpdate (-2147217336), UnsupportedParameter (-2147217355), UnsupportedPutExtension (-2147217347), UpdateOverrideNotAllowed (-2147217325), UpdatePropagatedMethod (-2147217324), UpdateTypeMismatch (-2147217326), ValueOutOfRange (-2147217365) """
    AccessDenied: ManagementStatus = ...
    AggregatingByObject: ManagementStatus = ...
    AlreadyExists: ManagementStatus = ...
    AmendedObject: ManagementStatus = ...
    BackupRestoreWinmgmtRunning: ManagementStatus = ...
    BufferTooSmall: ManagementStatus = ...
    CallCanceled: ManagementStatus = ...
    CannotBeAbstract: ManagementStatus = ...
    CannotBeKey: ManagementStatus = ...
    CannotBeSingleton: ManagementStatus = ...
    CannotChangeIndexInheritance: ManagementStatus = ...
    CannotChangeKeyInheritance: ManagementStatus = ...
    CircularReference: ManagementStatus = ...
    ClassHasChildren: ManagementStatus = ...
    ClassHasInstances: ManagementStatus = ...
    ClientTooSlow: ManagementStatus = ...
    CriticalError: ManagementStatus = ...
    Different: ManagementStatus = ...
    DuplicateObjects: ManagementStatus = ...
    Failed: ManagementStatus = ...
    IllegalNull: ManagementStatus = ...
    IllegalOperation: ManagementStatus = ...
    IncompleteClass: ManagementStatus = ...
    InitializationFailure: ManagementStatus = ...
    InvalidCimType: ManagementStatus = ...
    InvalidClass: ManagementStatus = ...
    InvalidContext: ManagementStatus = ...
    InvalidDuplicateParameter: ManagementStatus = ...
    InvalidFlavor: ManagementStatus = ...
    InvalidMethod: ManagementStatus = ...
    InvalidMethodParameters: ManagementStatus = ...
    InvalidNamespace: ManagementStatus = ...
    InvalidObject: ManagementStatus = ...
    InvalidObjectPath: ManagementStatus = ...
    InvalidOperation: ManagementStatus = ...
    InvalidOperator: ManagementStatus = ...
    InvalidParameter: ManagementStatus = ...
    InvalidParameterID: ManagementStatus = ...
    InvalidProperty: ManagementStatus = ...
    InvalidPropertyType: ManagementStatus = ...
    InvalidProviderRegistration: ManagementStatus = ...
    InvalidQualifier: ManagementStatus = ...
    InvalidQualifierType: ManagementStatus = ...
    InvalidQuery: ManagementStatus = ...
    InvalidQueryType: ManagementStatus = ...
    InvalidStream: ManagementStatus = ...
    InvalidSuperclass: ManagementStatus = ...
    InvalidSyntax: ManagementStatus = ...
    LocalCredentials: ManagementStatus = ...
    MarshalInvalidSignature: ManagementStatus = ...
    MarshalVersionMismatch: ManagementStatus = ...
    MethodDisabled: ManagementStatus = ...
    MethodNotImplemented: ManagementStatus = ...
    MissingAggregationList: ManagementStatus = ...
    MissingGroupWithin: ManagementStatus = ...
    MissingParameterID: ManagementStatus = ...
    NoError: ManagementStatus = ...
    NoMoreData: ManagementStatus = ...
    NonconsecutiveParameterIDs: ManagementStatus = ...
    NondecoratedObject: ManagementStatus = ...
    NotAvailable: ManagementStatus = ...
    NotEventClass: ManagementStatus = ...
    NotFound: ManagementStatus = ...
    NotSupported: ManagementStatus = ...
    OperationCanceled: ManagementStatus = ...
    OutOfDiskSpace: ManagementStatus = ...
    OutOfMemory: ManagementStatus = ...
    OverrideNotAllowed: ManagementStatus = ...
    ParameterIDOnRetval: ManagementStatus = ...
    PartialResults: ManagementStatus = ...
    Pending: ManagementStatus = ...
    PrivilegeNotHeld: ManagementStatus = ...
    PropagatedMethod: ManagementStatus = ...
    PropagatedProperty: ManagementStatus = ...
    PropagatedQualifier: ManagementStatus = ...
    PropertyNotAnObject: ManagementStatus = ...
    ProviderFailure: ManagementStatus = ...
    ProviderLoadFailure: ManagementStatus = ...
    ProviderNotCapable: ManagementStatus = ...
    ProviderNotFound: ManagementStatus = ...
    QueryNotImplemented: ManagementStatus = ...
    QueueOverflow: ManagementStatus = ...
    ReadOnly: ManagementStatus = ...
    RefresherBusy: ManagementStatus = ...
    RegistrationTooBroad: ManagementStatus = ...
    RegistrationTooPrecise: ManagementStatus = ...
    ResetToDefault: ManagementStatus = ...
    ServerTooBusy: ManagementStatus = ...
    ShuttingDown: ManagementStatus = ...
    SystemProperty: ManagementStatus = ...
    Timedout: ManagementStatus = ...
    TooManyProperties: ManagementStatus = ...
    TooMuchData: ManagementStatus = ...
    TransportFailure: ManagementStatus = ...
    TypeMismatch: ManagementStatus = ...
    Unexpected: ManagementStatus = ...
    UninterpretableProviderQuery: ManagementStatus = ...
    UnknownObjectType: ManagementStatus = ...
    UnknownPacketType: ManagementStatus = ...
    UnparsableQuery: ManagementStatus = ...
    UnsupportedClassUpdate: ManagementStatus = ...
    UnsupportedParameter: ManagementStatus = ...
    UnsupportedPutExtension: ManagementStatus = ...
    UpdateOverrideNotAllowed: ManagementStatus = ...
    UpdatePropagatedMethod: ManagementStatus = ...
    UpdateTypeMismatch: ManagementStatus = ...
    ValueOutOfRange: ManagementStatus = ...
    value__ = ...


class MethodData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def InParameters(self) -> ManagementBaseObject:
        """ Get: InParameters(self: MethodData) -> ManagementBaseObject """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MethodData) -> str """
        ...

    @property
    def Origin(self) -> str:
        """ Get: Origin(self: MethodData) -> str """
        ...

    @property
    def OutParameters(self) -> ManagementBaseObject:
        """ Get: OutParameters(self: MethodData) -> ManagementBaseObject """
        ...

    @property
    def Qualifiers(self) -> QualifierDataCollection:
        """ Get: Qualifiers(self: MethodData) -> QualifierDataCollection """
        ...



class MethodDataCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Add(self, methodName:str, inParameters:ManagementBaseObject = ..., outParameters:ManagementBaseObject = ...): # -> 
        """ Add(self: MethodDataCollection, methodName: str)Add(self: MethodDataCollection, methodName: str, inParameters: ManagementBaseObject, outParameters: ManagementBaseObject) """
        ...

    def GetEnumerator(self): # -> MethodDataEnumerator
        """ GetEnumerator(self: MethodDataCollection) -> MethodDataEnumerator """
        ...

    def MethodDataEnumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Remove(self, methodName:str): # -> 
        """ Remove(self: MethodDataCollection, methodName: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class ObjectGetOptions(ManagementOptions): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    ObjectGetOptions()
    ObjectGetOptions(context: ManagementNamedValueCollection)
    ObjectGetOptions(context: ManagementNamedValueCollection, timeout: TimeSpan, useAmendedQualifiers: bool)
    """
    @property
    def UseAmendedQualifiers(self) -> bool:
        """
        Get: UseAmendedQualifiers(self: ObjectGetOptions) -> bool
        Set: UseAmendedQualifiers(self: ObjectGetOptions) = value
        """
        ...


    def __new__(cls, context:ManagementNamedValueCollection = ..., timeout:TimeSpan = ..., useAmendedQualifiers:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, context: ManagementNamedValueCollection)
        __new__(cls: type, context: ManagementNamedValueCollection, timeout: TimeSpan, useAmendedQualifiers: bool)
        """
        ...


class ObjectPutEventArgs(ManagementEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Path(self) -> ManagementPath:
        """ Get: Path(self: ObjectPutEventArgs) -> ManagementPath """
        ...



class ObjectPutEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ObjectPutEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ObjectPutEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ObjectPutEventHandler, sender: object, e: ObjectPutEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ObjectPutEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ObjectPutEventArgs): # -> 
        """ Invoke(self: ObjectPutEventHandler, sender: object, e: ObjectPutEventArgs) """
        ...


class ObjectQuery(ManagementQuery): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    ObjectQuery()
    ObjectQuery(query: str)
    ObjectQuery(language: str, query: str)
    """
    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, query: str)
        __new__(cls: type, language: str, query: str)
        """
        ...


class ObjectReadyEventArgs(ManagementEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def NewObject(self) -> ManagementBaseObject:
        """ Get: NewObject(self: ObjectReadyEventArgs) -> ManagementBaseObject """
        ...



class ObjectReadyEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ObjectReadyEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ObjectReadyEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ObjectReadyEventHandler, sender: object, e: ObjectReadyEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ObjectReadyEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ObjectReadyEventArgs): # -> 
        """ Invoke(self: ObjectReadyEventHandler, sender: object, e: ObjectReadyEventArgs) """
        ...


class ProgressEventArgs(ManagementEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Current(self) -> int:
        """ Get: Current(self: ProgressEventArgs) -> int """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: ProgressEventArgs) -> str """
        ...

    @property
    def UpperBound(self) -> int:
        """ Get: UpperBound(self: ProgressEventArgs) -> int """
        ...



class ProgressEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ProgressEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ProgressEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ProgressEventHandler, sender: object, e: ProgressEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ProgressEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ProgressEventArgs): # -> 
        """ Invoke(self: ProgressEventHandler, sender: object, e: ProgressEventArgs) """
        ...


class PropertyData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsArray(self) -> bool:
        """ Get: IsArray(self: PropertyData) -> bool """
        ...

    @property
    def IsLocal(self) -> bool:
        """ Get: IsLocal(self: PropertyData) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PropertyData) -> str """
        ...

    @property
    def Origin(self) -> str:
        """ Get: Origin(self: PropertyData) -> str """
        ...

    @property
    def Qualifiers(self) -> QualifierDataCollection:
        """ Get: Qualifiers(self: PropertyData) -> QualifierDataCollection """
        ...

    @property
    def Type(self) -> CimType:
        """ Get: Type(self: PropertyData) -> CimType """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: PropertyData) -> object
        Set: Value(self: PropertyData) = value
        """
        ...



class PropertyDataCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Add(self, propertyName:str, *__args:object): # -> 
        """ Add(self: PropertyDataCollection, propertyName: str, propertyValue: object)Add(self: PropertyDataCollection, propertyName: str, propertyValue: object, propertyType: CimType)Add(self: PropertyDataCollection, propertyName: str, propertyType: CimType, isArray: bool) """
        ...

    def GetEnumerator(self): # -> PropertyDataEnumerator
        """ GetEnumerator(self: PropertyDataCollection) -> PropertyDataEnumerator """
        ...

    def PropertyDataEnumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Remove(self, propertyName:str): # -> 
        """ Remove(self: PropertyDataCollection, propertyName: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class PutOptions(ManagementOptions): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    PutOptions()
    PutOptions(context: ManagementNamedValueCollection)
    PutOptions(context: ManagementNamedValueCollection, timeout: TimeSpan, useAmendedQualifiers: bool, putType: PutType)
    """
    @property
    def Type(self) -> PutType:
        """
        Get: Type(self: PutOptions) -> PutType
        Set: Type(self: PutOptions) = value
        """
        ...

    @property
    def UseAmendedQualifiers(self) -> bool:
        """
        Get: UseAmendedQualifiers(self: PutOptions) -> bool
        Set: UseAmendedQualifiers(self: PutOptions) = value
        """
        ...


    def __new__(cls, context:ManagementNamedValueCollection = ..., timeout:TimeSpan = ..., useAmendedQualifiers:bool = ..., putType:PutType = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, context: ManagementNamedValueCollection)
        __new__(cls: type, context: ManagementNamedValueCollection, timeout: TimeSpan, useAmendedQualifiers: bool, putType: PutType)
        """
        ...


class PutType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PutType, values: CreateOnly (2), None (0), UpdateOnly (1), UpdateOrCreate (3) """
    CreateOnly: PutType = ...
    UpdateOnly: PutType = ...
    UpdateOrCreate: PutType = ...
    value__ = ...


class QualifierData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsAmended(self) -> bool:
        """
        Get: IsAmended(self: QualifierData) -> bool
        Set: IsAmended(self: QualifierData) = value
        """
        ...

    @property
    def IsLocal(self) -> bool:
        """ Get: IsLocal(self: QualifierData) -> bool """
        ...

    @property
    def IsOverridable(self) -> bool:
        """
        Get: IsOverridable(self: QualifierData) -> bool
        Set: IsOverridable(self: QualifierData) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: QualifierData) -> str """
        ...

    @property
    def PropagatesToInstance(self) -> bool:
        """
        Get: PropagatesToInstance(self: QualifierData) -> bool
        Set: PropagatesToInstance(self: QualifierData) = value
        """
        ...

    @property
    def PropagatesToSubclass(self) -> bool:
        """
        Get: PropagatesToSubclass(self: QualifierData) -> bool
        Set: PropagatesToSubclass(self: QualifierData) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: QualifierData) -> object
        Set: Value(self: QualifierData) = value
        """
        ...



class QualifierDataCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    def Add(self, qualifierName:str, qualifierValue:object, isAmended:bool = ..., propagatesToInstance:bool = ..., propagatesToSubclass:bool = ..., isOverridable:bool = ...): # -> 
        """ Add(self: QualifierDataCollection, qualifierName: str, qualifierValue: object)Add(self: QualifierDataCollection, qualifierName: str, qualifierValue: object, isAmended: bool, propagatesToInstance: bool, propagatesToSubclass: bool, isOverridable: bool) """
        ...

    def GetEnumerator(self): # -> QualifierDataEnumerator
        """ GetEnumerator(self: QualifierDataCollection) -> QualifierDataEnumerator """
        ...

    def QualifierDataEnumerator(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Remove(self, qualifierName:str): # -> 
        """ Remove(self: QualifierDataCollection, qualifierName: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...



class WqlObjectQuery(ObjectQuery): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    WqlObjectQuery()
    WqlObjectQuery(query: str)
    """
    @property
    def QueryLanguage(self) -> str:
        """ Get: QueryLanguage(self: WqlObjectQuery) -> str """
        ...



class RelatedObjectQuery(WqlObjectQuery): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    RelatedObjectQuery()
    RelatedObjectQuery(queryOrSourceObject: str)
    RelatedObjectQuery(sourceObject: str, relatedClass: str)
    RelatedObjectQuery(sourceObject: str, relatedClass: str, relationshipClass: str, relatedQualifier: str, relationshipQualifier: str, relatedRole: str, thisRole: str, classDefinitionsOnly: bool)
    RelatedObjectQuery(isSchemaQuery: bool, sourceObject: str, relatedClass: str, relationshipClass: str, relatedQualifier: str, relationshipQualifier: str, relatedRole: str, thisRole: str)
    """
    @property
    def ClassDefinitionsOnly(self) -> bool:
        """
        Get: ClassDefinitionsOnly(self: RelatedObjectQuery) -> bool
        Set: ClassDefinitionsOnly(self: RelatedObjectQuery) = value
        """
        ...

    @property
    def IsSchemaQuery(self) -> bool:
        """
        Get: IsSchemaQuery(self: RelatedObjectQuery) -> bool
        Set: IsSchemaQuery(self: RelatedObjectQuery) = value
        """
        ...

    @property
    def RelatedClass(self) -> str:
        """
        Get: RelatedClass(self: RelatedObjectQuery) -> str
        Set: RelatedClass(self: RelatedObjectQuery) = value
        """
        ...

    @property
    def RelatedQualifier(self) -> str:
        """
        Get: RelatedQualifier(self: RelatedObjectQuery) -> str
        Set: RelatedQualifier(self: RelatedObjectQuery) = value
        """
        ...

    @property
    def RelatedRole(self) -> str:
        """
        Get: RelatedRole(self: RelatedObjectQuery) -> str
        Set: RelatedRole(self: RelatedObjectQuery) = value
        """
        ...

    @property
    def RelationshipClass(self) -> str:
        """
        Get: RelationshipClass(self: RelatedObjectQuery) -> str
        Set: RelationshipClass(self: RelatedObjectQuery) = value
        """
        ...

    @property
    def RelationshipQualifier(self) -> str:
        """
        Get: RelationshipQualifier(self: RelatedObjectQuery) -> str
        Set: RelationshipQualifier(self: RelatedObjectQuery) = value
        """
        ...

    @property
    def SourceObject(self) -> str:
        """
        Get: SourceObject(self: RelatedObjectQuery) -> str
        Set: SourceObject(self: RelatedObjectQuery) = value
        """
        ...

    @property
    def ThisRole(self) -> str:
        """
        Get: ThisRole(self: RelatedObjectQuery) -> str
        Set: ThisRole(self: RelatedObjectQuery) = value
        """
        ...


    def BuildQuery(self, *args): #cannot find CLR method
        """ BuildQuery(self: RelatedObjectQuery) """
        ...


class RelationshipQuery(WqlObjectQuery): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    RelationshipQuery()
    RelationshipQuery(queryOrSourceObject: str)
    RelationshipQuery(sourceObject: str, relationshipClass: str)
    RelationshipQuery(sourceObject: str, relationshipClass: str, relationshipQualifier: str, thisRole: str, classDefinitionsOnly: bool)
    RelationshipQuery(isSchemaQuery: bool, sourceObject: str, relationshipClass: str, relationshipQualifier: str, thisRole: str)
    """
    @property
    def ClassDefinitionsOnly(self) -> bool:
        """
        Get: ClassDefinitionsOnly(self: RelationshipQuery) -> bool
        Set: ClassDefinitionsOnly(self: RelationshipQuery) = value
        """
        ...

    @property
    def IsSchemaQuery(self) -> bool:
        """
        Get: IsSchemaQuery(self: RelationshipQuery) -> bool
        Set: IsSchemaQuery(self: RelationshipQuery) = value
        """
        ...

    @property
    def RelationshipClass(self) -> str:
        """
        Get: RelationshipClass(self: RelationshipQuery) -> str
        Set: RelationshipClass(self: RelationshipQuery) = value
        """
        ...

    @property
    def RelationshipQualifier(self) -> str:
        """
        Get: RelationshipQualifier(self: RelationshipQuery) -> str
        Set: RelationshipQualifier(self: RelationshipQuery) = value
        """
        ...

    @property
    def SourceObject(self) -> str:
        """
        Get: SourceObject(self: RelationshipQuery) -> str
        Set: SourceObject(self: RelationshipQuery) = value
        """
        ...

    @property
    def ThisRole(self) -> str:
        """
        Get: ThisRole(self: RelationshipQuery) -> str
        Set: ThisRole(self: RelationshipQuery) = value
        """
        ...


    def BuildQuery(self, *args): #cannot find CLR method
        """ BuildQuery(self: RelationshipQuery) """
        ...


class SelectQuery(WqlObjectQuery): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    SelectQuery()
    SelectQuery(queryOrClassName: str)
    SelectQuery(className: str, condition: str)
    SelectQuery(className: str, condition: str, selectedProperties: Array[str])
    SelectQuery(isSchemaQuery: bool, condition: str)
    """
    @property
    def ClassName(self) -> str:
        """
        Get: ClassName(self: SelectQuery) -> str
        Set: ClassName(self: SelectQuery) = value
        """
        ...

    @property
    def Condition(self) -> str:
        """
        Get: Condition(self: SelectQuery) -> str
        Set: Condition(self: SelectQuery) = value
        """
        ...

    @property
    def IsSchemaQuery(self) -> bool:
        """
        Get: IsSchemaQuery(self: SelectQuery) -> bool
        Set: IsSchemaQuery(self: SelectQuery) = value
        """
        ...

    @property
    def QueryString(self) -> str:
        """
        Get: QueryString(self: SelectQuery) -> str
        Set: QueryString(self: SelectQuery) = value
        """
        ...

    @property
    def SelectedProperties(self) -> StringCollection:
        """
        Get: SelectedProperties(self: SelectQuery) -> StringCollection
        Set: SelectedProperties(self: SelectQuery) = value
        """
        ...


    def BuildQuery(self, *args): #cannot find CLR method
        """ BuildQuery(self: SelectQuery) """
        ...


class StoppedEventArgs(ManagementEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Status(self) -> ManagementStatus:
        """ Get: Status(self: StoppedEventArgs) -> ManagementStatus """
        ...



class StoppedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ StoppedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:StoppedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: StoppedEventHandler, sender: object, e: StoppedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: StoppedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:StoppedEventArgs): # -> 
        """ Invoke(self: StoppedEventHandler, sender: object, e: StoppedEventArgs) """
        ...


class TextFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TextFormat, values: CimDtd20 (1), Mof (0), WmiDtd20 (2) """
    CimDtd20: TextFormat = ...
    Mof: TextFormat = ...
    value__ = ...
    WmiDtd20: TextFormat = ...


class WqlEventQuery(EventQuery): # skipped bases: <type 'ICloneable'>, <type 'object'>
    """
    WqlEventQuery()
    WqlEventQuery(queryOrEventClassName: str)
    WqlEventQuery(eventClassName: str, condition: str)
    WqlEventQuery(eventClassName: str, withinInterval: TimeSpan)
    WqlEventQuery(eventClassName: str, withinInterval: TimeSpan, condition: str)
    WqlEventQuery(eventClassName: str, condition: str, groupWithinInterval: TimeSpan)
    WqlEventQuery(eventClassName: str, condition: str, groupWithinInterval: TimeSpan, groupByPropertyList: Array[str])
    WqlEventQuery(eventClassName: str, withinInterval: TimeSpan, condition: str, groupWithinInterval: TimeSpan, groupByPropertyList: Array[str], havingCondition: str)
    """
    @property
    def Condition(self) -> str:
        """
        Get: Condition(self: WqlEventQuery) -> str
        Set: Condition(self: WqlEventQuery) = value
        """
        ...

    @property
    def EventClassName(self) -> str:
        """
        Get: EventClassName(self: WqlEventQuery) -> str
        Set: EventClassName(self: WqlEventQuery) = value
        """
        ...

    @property
    def GroupByPropertyList(self) -> StringCollection:
        """
        Get: GroupByPropertyList(self: WqlEventQuery) -> StringCollection
        Set: GroupByPropertyList(self: WqlEventQuery) = value
        """
        ...

    @property
    def GroupWithinInterval(self) -> TimeSpan:
        """
        Get: GroupWithinInterval(self: WqlEventQuery) -> TimeSpan
        Set: GroupWithinInterval(self: WqlEventQuery) = value
        """
        ...

    @property
    def HavingCondition(self) -> str:
        """
        Get: HavingCondition(self: WqlEventQuery) -> str
        Set: HavingCondition(self: WqlEventQuery) = value
        """
        ...

    @property
    def QueryLanguage(self) -> str:
        """ Get: QueryLanguage(self: WqlEventQuery) -> str """
        ...

    @property
    def QueryString(self) -> str:
        """
        Get: QueryString(self: WqlEventQuery) -> str
        Set: QueryString(self: WqlEventQuery) = value
        """
        ...

    @property
    def WithinInterval(self) -> TimeSpan:
        """
        Get: WithinInterval(self: WqlEventQuery) -> TimeSpan
        Set: WithinInterval(self: WqlEventQuery) = value
        """
        ...


    def BuildQuery(self, *args): #cannot find CLR method
        """ BuildQuery(self: WqlEventQuery) """
        ...


# variables with complex values

