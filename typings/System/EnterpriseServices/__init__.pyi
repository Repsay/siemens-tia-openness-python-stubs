# encoding: utf-8
# module System.EnterpriseServices calls itself EnterpriseServices
# from System.EnterpriseServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Attribute, ContextBoundObject, Enum, Guid, 
    IDisposable, MarshalByRefObject, SystemException, Type)

from System.Collections import Hashtable, IEnumerable

from System.Transactions import Transaction

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    IConfigurationAttribute, IManagedObject, IObjPool, IThunkInstallation, 
    field#)
"""

# no functions
# classes

class AccessChecksLevelOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AccessChecksLevelOption, values: Application (0), ApplicationComponent (1) """
    Application: AccessChecksLevelOption = ...
    ApplicationComponent: AccessChecksLevelOption = ...
    value__ = ...


class ActivationOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ActivationOption, values: Library (0), Server (1) """
    Library: ActivationOption = ...
    Server: ActivationOption = ...
    value__ = ...


class Activity: # skipped bases: <type 'object'>, <type 'object'>
    """ Activity(cfg: ServiceConfig) """
    def AsynchronousCall(self, serviceCall:IServiceCall): # -> 
        """ AsynchronousCall(self: Activity, serviceCall: IServiceCall) """
        ...

    def BindToCurrentThread(self): # -> 
        """ BindToCurrentThread(self: Activity) """
        ...

    def SynchronousCall(self, serviceCall:IServiceCall): # -> 
        """ SynchronousCall(self: Activity, serviceCall: IServiceCall) """
        ...

    def UnbindFromThread(self): # -> 
        """ UnbindFromThread(self: Activity) """
        ...


class ApplicationAccessControlAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ApplicationAccessControlAttribute()
    ApplicationAccessControlAttribute(val: bool)
    """
    @property
    def AccessChecksLevel(self) -> AccessChecksLevelOption:
        """
        Get: AccessChecksLevel(self: ApplicationAccessControlAttribute) -> AccessChecksLevelOption
        Set: AccessChecksLevel(self: ApplicationAccessControlAttribute) = value
        """
        ...

    @property
    def Authentication(self) -> AuthenticationOption:
        """
        Get: Authentication(self: ApplicationAccessControlAttribute) -> AuthenticationOption
        Set: Authentication(self: ApplicationAccessControlAttribute) = value
        """
        ...

    @property
    def ImpersonationLevel(self) -> ImpersonationLevelOption:
        """
        Get: ImpersonationLevel(self: ApplicationAccessControlAttribute) -> ImpersonationLevelOption
        Set: ImpersonationLevel(self: ApplicationAccessControlAttribute) = value
        """
        ...

    @property
    def Value(self) -> bool:
        """
        Get: Value(self: ApplicationAccessControlAttribute) -> bool
        Set: Value(self: ApplicationAccessControlAttribute) = value
        """
        ...


    def __new__(cls, val:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, val: bool)
        """
        ...


class ApplicationActivationAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ApplicationActivationAttribute(opt: ActivationOption) """
    @property
    def SoapMailbox(self) -> str:
        """
        Get: SoapMailbox(self: ApplicationActivationAttribute) -> str
        Set: SoapMailbox(self: ApplicationActivationAttribute) = value
        """
        ...

    @property
    def SoapVRoot(self) -> str:
        """
        Get: SoapVRoot(self: ApplicationActivationAttribute) -> str
        Set: SoapVRoot(self: ApplicationActivationAttribute) = value
        """
        ...

    @property
    def Value(self) -> ActivationOption:
        """ Get: Value(self: ApplicationActivationAttribute) -> ActivationOption """
        ...


    def __new__(cls, opt:ActivationOption) -> Self:
        """ __new__(cls: type, opt: ActivationOption) """
        ...


class ApplicationIDAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ApplicationIDAttribute(guid: str) """
    @property
    def Value(self) -> Guid:
        """ Get: Value(self: ApplicationIDAttribute) -> Guid """
        ...


    def __new__(cls, guid:str) -> Self:
        """ __new__(cls: type, guid: str) """
        ...


class ApplicationNameAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ApplicationNameAttribute(name: str) """
    @property
    def Value(self) -> str:
        """ Get: Value(self: ApplicationNameAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class ApplicationQueuingAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ApplicationQueuingAttribute() """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ApplicationQueuingAttribute) -> bool
        Set: Enabled(self: ApplicationQueuingAttribute) = value
        """
        ...

    @property
    def MaxListenerThreads(self) -> int:
        """
        Get: MaxListenerThreads(self: ApplicationQueuingAttribute) -> int
        Set: MaxListenerThreads(self: ApplicationQueuingAttribute) = value
        """
        ...

    @property
    def QueueListenerEnabled(self) -> bool:
        """
        Get: QueueListenerEnabled(self: ApplicationQueuingAttribute) -> bool
        Set: QueueListenerEnabled(self: ApplicationQueuingAttribute) = value
        """
        ...



class AuthenticationOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AuthenticationOption, values: Call (3), Connect (2), Default (0), Integrity (5), None (1), Packet (4), Privacy (6) """
    def Call(self, *args): #cannot find CLR method
        """ enum AuthenticationOption, values: Call (3), Connect (2), Default (0), Integrity (5), None (1), Packet (4), Privacy (6) """
        ...

    def Connect(self, *args): #cannot find CLR method
        """ enum AuthenticationOption, values: Call (3), Connect (2), Default (0), Integrity (5), None (1), Packet (4), Privacy (6) """
        ...

    def Default(self, *args): #cannot find CLR method
        """ enum AuthenticationOption, values: Call (3), Connect (2), Default (0), Integrity (5), None (1), Packet (4), Privacy (6) """
        ...

    def Integrity(self, *args): #cannot find CLR method
        """ enum AuthenticationOption, values: Call (3), Connect (2), Default (0), Integrity (5), None (1), Packet (4), Privacy (6) """
        ...

    def None(self, *args): #cannot find CLR method
        """ enum AuthenticationOption, values: Call (3), Connect (2), Default (0), Integrity (5), None (1), Packet (4), Privacy (6) """
        ...

    def Packet(self, *args): #cannot find CLR method
        """ enum AuthenticationOption, values: Call (3), Connect (2), Default (0), Integrity (5), None (1), Packet (4), Privacy (6) """
        ...

    def Privacy(self, *args): #cannot find CLR method
        """ enum AuthenticationOption, values: Call (3), Connect (2), Default (0), Integrity (5), None (1), Packet (4), Privacy (6) """
        ...

    def __call__(self, *args): #cannot find CLR method
        """ enum AuthenticationOption, values: Call (3), Connect (2), Default (0), Integrity (5), None (1), Packet (4), Privacy (6) """
        ...

    value__ = ...


class AutoCompleteAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    AutoCompleteAttribute()
    AutoCompleteAttribute(val: bool)
    """
    @property
    def Value(self) -> bool:
        """ Get: Value(self: AutoCompleteAttribute) -> bool """
        ...


    def __new__(cls, val:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, val: bool)
        """
        ...


class BindingOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BindingOption, values: BindingToPoolThread (1), NoBinding (0) """
    BindingToPoolThread: BindingOption = ...
    NoBinding: BindingOption = ...
    value__ = ...


class BOID: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    rgb = ...


class BYOT: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateWithTipTransaction(url:str, t:Type) -> object:
        """ CreateWithTipTransaction(url: str, t: Type) -> object """
        ...

    @staticmethod
    def CreateWithTransaction(transaction:object, t:Type) -> object:
        """ CreateWithTransaction(transaction: object, t: Type) -> object """
        ...


class ComponentAccessControlAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ComponentAccessControlAttribute()
    ComponentAccessControlAttribute(val: bool)
    """
    @property
    def Value(self) -> bool:
        """ Get: Value(self: ComponentAccessControlAttribute) -> bool """
        ...


    def __new__(cls, val:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, val: bool)
        """
        ...


class COMTIIntrinsicsAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    COMTIIntrinsicsAttribute()
    COMTIIntrinsicsAttribute(val: bool)
    """
    @property
    def Value(self) -> bool:
        """ Get: Value(self: COMTIIntrinsicsAttribute) -> bool """
        ...


    def __new__(cls, val:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, val: bool)
        """
        ...


class ConstructionEnabledAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ConstructionEnabledAttribute()
    ConstructionEnabledAttribute(val: bool)
    """
    @property
    def Default(self) -> str:
        """
        Get: Default(self: ConstructionEnabledAttribute) -> str
        Set: Default(self: ConstructionEnabledAttribute) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ConstructionEnabledAttribute) -> bool
        Set: Enabled(self: ConstructionEnabledAttribute) = value
        """
        ...


    def __new__(cls, val:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, val: bool)
        """
        ...


class ContextUtil: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ActivityId(self) -> Guid:
        """ Get: ActivityId() -> Guid """
        ...

    @property
    def ApplicationId(self) -> Guid:
        """ Get: ApplicationId() -> Guid """
        ...

    @property
    def ApplicationInstanceId(self) -> Guid:
        """ Get: ApplicationInstanceId() -> Guid """
        ...

    @property
    def ContextId(self) -> Guid:
        """ Get: ContextId() -> Guid """
        ...

    @property
    def DeactivateOnReturn(self) -> bool:
        """
        Get: DeactivateOnReturn() -> bool
        Set: DeactivateOnReturn() = value
        """
        ...

    @property
    def IsInTransaction(self) -> bool:
        """ Get: IsInTransaction() -> bool """
        ...

    @property
    def IsSecurityEnabled(self) -> bool:
        """ Get: IsSecurityEnabled() -> bool """
        ...

    @property
    def MyTransactionVote(self) -> TransactionVote:
        """
        Get: MyTransactionVote() -> TransactionVote
        Set: MyTransactionVote() = value
        """
        ...

    @property
    def PartitionId(self) -> Guid:
        """ Get: PartitionId() -> Guid """
        ...

    @property
    def SystemTransaction(self) -> Transaction:
        """ Get: SystemTransaction() -> Transaction """
        ...

    @property
    def Transaction(self) -> object:
        """ Get: Transaction() -> object """
        ...

    @property
    def TransactionId(self) -> Guid:
        """ Get: TransactionId() -> Guid """
        ...


    @staticmethod
    def DisableCommit(): # -> 
        """ DisableCommit() """
        ...

    @staticmethod
    def EnableCommit(): # -> 
        """ EnableCommit() """
        ...

    @staticmethod
    def GetNamedProperty(name:str) -> object:
        """ GetNamedProperty(name: str) -> object """
        ...

    @staticmethod
    def IsCallerInRole(role:str) -> bool:
        """ IsCallerInRole(role: str) -> bool """
        ...

    @staticmethod
    def IsDefaultContext() -> bool:
        """ IsDefaultContext() -> bool """
        ...

    @staticmethod
    def SetAbort(): # -> 
        """ SetAbort() """
        ...

    @staticmethod
    def SetComplete(): # -> 
        """ SetComplete() """
        ...

    @staticmethod
    def SetNamedProperty(name:str, value:object): # -> 
        """ SetNamedProperty(name: str, value: object) """
        ...



class DescriptionAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DescriptionAttribute(desc: str) """
    def __new__(cls, desc:str) -> Self:
        """ __new__(cls: type, desc: str) """
        ...


class EventClassAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ EventClassAttribute() """
    @property
    def AllowInprocSubscribers(self) -> bool:
        """
        Get: AllowInprocSubscribers(self: EventClassAttribute) -> bool
        Set: AllowInprocSubscribers(self: EventClassAttribute) = value
        """
        ...

    @property
    def FireInParallel(self) -> bool:
        """
        Get: FireInParallel(self: EventClassAttribute) -> bool
        Set: FireInParallel(self: EventClassAttribute) = value
        """
        ...

    @property
    def PublisherFilter(self) -> str:
        """
        Get: PublisherFilter(self: EventClassAttribute) -> str
        Set: PublisherFilter(self: EventClassAttribute) = value
        """
        ...



class EventTrackingEnabledAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    EventTrackingEnabledAttribute()
    EventTrackingEnabledAttribute(val: bool)
    """
    @property
    def Value(self) -> bool:
        """ Get: Value(self: EventTrackingEnabledAttribute) -> bool """
        ...


    def __new__(cls, val:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, val: bool)
        """
        ...


class ExceptionClassAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ExceptionClassAttribute(name: str) """
    @property
    def Value(self) -> str:
        """ Get: Value(self: ExceptionClassAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class IAsyncErrorNotify: # skipped bases: <type 'object'>
    """ no doc """
    def OnError(self, hresult:int): # -> 
        """ OnError(self: IAsyncErrorNotify, hresult: int) """
        ...


class IISIntrinsicsAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    IISIntrinsicsAttribute()
    IISIntrinsicsAttribute(val: bool)
    """
    @property
    def Value(self) -> bool:
        """ Get: Value(self: IISIntrinsicsAttribute) -> bool """
        ...


    def __new__(cls, val:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, val: bool)
        """
        ...


class ImpersonationLevelOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ImpersonationLevelOption, values: Anonymous (1), Default (0), Delegate (4), Identify (2), Impersonate (3) """
    Anonymous: ImpersonationLevelOption = ...
    Default: ImpersonationLevelOption = ...
    Delegate: ImpersonationLevelOption = ...
    Identify: ImpersonationLevelOption = ...
    Impersonate: ImpersonationLevelOption = ...
    value__ = ...


class InheritanceOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InheritanceOption, values: Ignore (1), Inherit (0) """
    Ignore: InheritanceOption = ...
    Inherit: InheritanceOption = ...
    value__ = ...


class InstallationFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) InstallationFlags, values: Configure (1024), ConfigureComponentsOnly (16), CreateTargetApplication (2), Default (0), ExpectExistingTypeLib (1), FindOrCreateTargetApplication (4), Install (512), ReconfigureExistingApplication (8), Register (256), ReportWarningsToConsole (32) """
    Configure: InstallationFlags = ...
    ConfigureComponentsOnly: InstallationFlags = ...
    CreateTargetApplication: InstallationFlags = ...
    Default: InstallationFlags = ...
    ExpectExistingTypeLib: InstallationFlags = ...
    FindOrCreateTargetApplication: InstallationFlags = ...
    Install: InstallationFlags = ...
    ReconfigureExistingApplication: InstallationFlags = ...
    Register: InstallationFlags = ...
    ReportWarningsToConsole: InstallationFlags = ...
    value__ = ...


class InterfaceQueuingAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    InterfaceQueuingAttribute()
    InterfaceQueuingAttribute(enabled: bool)
    """
    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: InterfaceQueuingAttribute) -> bool
        Set: Enabled(self: InterfaceQueuingAttribute) = value
        """
        ...

    @property
    def Interface(self) -> str:
        """
        Get: Interface(self: InterfaceQueuingAttribute) -> str
        Set: Interface(self: InterfaceQueuingAttribute) = value
        """
        ...


    def __new__(cls, enabled:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, enabled: bool)
        """
        ...


class IPlaybackControl: # skipped bases: <type 'object'>
    """ no doc """
    def FinalClientRetry(self): # -> 
        """ FinalClientRetry(self: IPlaybackControl) """
        ...

    def FinalServerRetry(self): # -> 
        """ FinalServerRetry(self: IPlaybackControl) """
        ...


class IProcessInitControl: # skipped bases: <type 'object'>
    """ no doc """
    def ResetInitializerTimeout(self, dwSecondsRemaining:int): # -> 
        """ ResetInitializerTimeout(self: IProcessInitControl, dwSecondsRemaining: int) """
        ...


class IProcessInitializer: # skipped bases: <type 'object'>
    """ no doc """
    def Shutdown(self): # -> 
        """ Shutdown(self: IProcessInitializer) """
        ...

    def Startup(self, punkProcessControl:object): # -> 
        """ Startup(self: IProcessInitializer, punkProcessControl: object) """
        ...


class IRegistrationHelper: # skipped bases: <type 'object'>
    """ no doc """
    def InstallAssembly(self, assembly, application, tlb, installFlags) -> Tuple_[str, str]:
        """ InstallAssembly(self: IRegistrationHelper, assembly: str, installFlags: InstallationFlags) -> (str, str) """
        ...

    def UninstallAssembly(self, assembly:str, application:str): # -> 
        """ UninstallAssembly(self: IRegistrationHelper, assembly: str, application: str) """
        ...


class IRemoteDispatch: # skipped bases: <type 'object'>
    """ no doc """
    def RemoteDispatchAutoDone(self, s:str) -> str:
        """ RemoteDispatchAutoDone(self: IRemoteDispatch, s: str) -> str """
        ...

    def RemoteDispatchNotAutoDone(self, s:str) -> str:
        """ RemoteDispatchNotAutoDone(self: IRemoteDispatch, s: str) -> str """
        ...


class IServiceCall: # skipped bases: <type 'object'>
    """ no doc """
    def OnCall(self): # -> 
        """ OnCall(self: IServiceCall) """
        ...


class IServicedComponentInfo: # skipped bases: <type 'object'>
    """ no doc """
    def GetComponentInfo(self, infoMask, infoArray) -> Tuple_[int, Array]:
        """ GetComponentInfo(self: IServicedComponentInfo, infoMask: int) -> (int, Array[str]) """
        ...


class ITransaction: # skipped bases: <type 'object'>
    """ no doc """
    def Abort(self, pboidReason:BOID, fRetaining:int, fAsync:int) -> BOID:
        """ Abort(self: ITransaction, pboidReason: BOID, fRetaining: int, fAsync: int) -> BOID """
        ...

    def Commit(self, fRetaining:int, grfTC:int, grfRM:int): # -> 
        """ Commit(self: ITransaction, fRetaining: int, grfTC: int, grfRM: int) """
        ...

    def GetTransactionInfo(self, pinfo) -> XACTTRANSINFO:
        """ GetTransactionInfo(self: ITransaction) -> XACTTRANSINFO """
        ...


class JustInTimeActivationAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    JustInTimeActivationAttribute()
    JustInTimeActivationAttribute(val: bool)
    """
    @property
    def Value(self) -> bool:
        """ Get: Value(self: JustInTimeActivationAttribute) -> bool """
        ...


    def __new__(cls, val:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, val: bool)
        """
        ...


class LoadBalancingSupportedAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    LoadBalancingSupportedAttribute()
    LoadBalancingSupportedAttribute(val: bool)
    """
    @property
    def Value(self) -> bool:
        """ Get: Value(self: LoadBalancingSupportedAttribute) -> bool """
        ...


    def __new__(cls, val:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, val: bool)
        """
        ...


class MustRunInClientContextAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    MustRunInClientContextAttribute()
    MustRunInClientContextAttribute(val: bool)
    """
    @property
    def Value(self) -> bool:
        """ Get: Value(self: MustRunInClientContextAttribute) -> bool """
        ...


    def __new__(cls, val:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, val: bool)
        """
        ...


class ObjectPoolingAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ObjectPoolingAttribute()
    ObjectPoolingAttribute(minPoolSize: int, maxPoolSize: int)
    ObjectPoolingAttribute(enable: bool)
    ObjectPoolingAttribute(enable: bool, minPoolSize: int, maxPoolSize: int)
    """
    @property
    def CreationTimeout(self) -> int:
        """
        Get: CreationTimeout(self: ObjectPoolingAttribute) -> int
        Set: CreationTimeout(self: ObjectPoolingAttribute) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: ObjectPoolingAttribute) -> bool
        Set: Enabled(self: ObjectPoolingAttribute) = value
        """
        ...

    @property
    def MaxPoolSize(self) -> int:
        """
        Get: MaxPoolSize(self: ObjectPoolingAttribute) -> int
        Set: MaxPoolSize(self: ObjectPoolingAttribute) = value
        """
        ...

    @property
    def MinPoolSize(self) -> int:
        """
        Get: MinPoolSize(self: ObjectPoolingAttribute) -> int
        Set: MinPoolSize(self: ObjectPoolingAttribute) = value
        """
        ...


    def AfterSaveChanges(self, info:Hashtable) -> bool:
        """ AfterSaveChanges(self: ObjectPoolingAttribute, info: Hashtable) -> bool """
        ...

    def Apply(self, info:Hashtable) -> bool:
        """ Apply(self: ObjectPoolingAttribute, info: Hashtable) -> bool """
        ...

    def IsValidTarget(self, s:str) -> bool:
        """ IsValidTarget(self: ObjectPoolingAttribute, s: str) -> bool """
        ...

    def __new__(cls, *__args:bool) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, minPoolSize: int, maxPoolSize: int)
        __new__(cls: type, enable: bool)
        __new__(cls: type, enable: bool, minPoolSize: int, maxPoolSize: int)
        """
        ...


class PartitionOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PartitionOption, values: Ignore (0), Inherit (1), New (2) """
    Ignore: PartitionOption = ...
    Inherit: PartitionOption = ...
    New: PartitionOption = ...
    value__ = ...


class PrivateComponentAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PrivateComponentAttribute() """
    pass

class PropertyLockMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PropertyLockMode, values: Method (1), SetGet (0) """
    Method: PropertyLockMode = ...
    SetGet: PropertyLockMode = ...
    value__ = ...


class PropertyReleaseMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PropertyReleaseMode, values: Process (1), Standard (0) """
    Process: PropertyReleaseMode = ...
    Standard: PropertyReleaseMode = ...
    value__ = ...


class RegistrationConfig: # skipped bases: <type 'object'>, <type 'object'>
    """ RegistrationConfig() """
    @property
    def Application(self) -> str:
        """
        Get: Application(self: RegistrationConfig) -> str
        Set: Application(self: RegistrationConfig) = value
        """
        ...

    @property
    def ApplicationRootDirectory(self) -> str:
        """
        Get: ApplicationRootDirectory(self: RegistrationConfig) -> str
        Set: ApplicationRootDirectory(self: RegistrationConfig) = value
        """
        ...

    @property
    def AssemblyFile(self) -> str:
        """
        Get: AssemblyFile(self: RegistrationConfig) -> str
        Set: AssemblyFile(self: RegistrationConfig) = value
        """
        ...

    @property
    def InstallationFlags(self) -> InstallationFlags:
        """
        Get: InstallationFlags(self: RegistrationConfig) -> InstallationFlags
        Set: InstallationFlags(self: RegistrationConfig) = value
        """
        ...

    @property
    def Partition(self) -> str:
        """
        Get: Partition(self: RegistrationConfig) -> str
        Set: Partition(self: RegistrationConfig) = value
        """
        ...

    @property
    def TypeLibrary(self) -> str:
        """
        Get: TypeLibrary(self: RegistrationConfig) -> str
        Set: TypeLibrary(self: RegistrationConfig) = value
        """
        ...



class RegistrationErrorInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: RegistrationErrorInfo) -> int """
        ...

    @property
    def ErrorString(self) -> str:
        """ Get: ErrorString(self: RegistrationErrorInfo) -> str """
        ...

    @property
    def MajorRef(self) -> str:
        """ Get: MajorRef(self: RegistrationErrorInfo) -> str """
        ...

    @property
    def MinorRef(self) -> str:
        """ Get: MinorRef(self: RegistrationErrorInfo) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: RegistrationErrorInfo) -> str """
        ...



class RegistrationException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RegistrationException()
    RegistrationException(msg: str)
    RegistrationException(msg: str, inner: Exception)
    """
    @property
    def ErrorInfo(self) -> Array:
        """ Get: ErrorInfo(self: RegistrationException) -> Array[RegistrationErrorInfo] """
        ...


    SerializeObjectState = ...


class RegistrationHelper(IThunkInstallation, MarshalByRefObject, IRegistrationHelper): # skipped bases: <type 'object'>
    """ RegistrationHelper() """
    def InstallAssemblyFromConfig(self, regConfig:RegistrationConfig) -> RegistrationConfig:
        """ InstallAssemblyFromConfig(self: RegistrationHelper, regConfig: RegistrationConfig) -> RegistrationConfig """
        ...

    def UninstallAssemblyFromConfig(self, regConfig:RegistrationConfig) -> RegistrationConfig:
        """ UninstallAssemblyFromConfig(self: RegistrationHelper, regConfig: RegistrationConfig) -> RegistrationConfig """
        ...


class ServicedComponent(IDisposable, ContextBoundObject, IRemoteDispatch, IManagedObject, IServicedComponentInfo): # skipped bases: <type 'object'>
    """ ServicedComponent() """
    def Activate(self, *args): #cannot find CLR method
        """ Activate(self: ServicedComponent) """
        ...

    def CanBePooled(self, *args): #cannot find CLR method
        """ CanBePooled(self: ServicedComponent) -> bool """
        ...

    def Construct(self, *args): #cannot find CLR method
        """ Construct(self: ServicedComponent, s: str) """
        ...

    def Deactivate(self, *args): #cannot find CLR method
        """ Deactivate(self: ServicedComponent) """
        ...

    @staticmethod
    def DisposeObject(sc:ServicedComponent): # -> 
        """ DisposeObject(sc: ServicedComponent) """
        ...


class RegistrationHelperTx(ServicedComponent): # skipped bases: <type 'IRemoteDispatch'>, <type 'IDisposable'>, <type 'IServicedComponentInfo'>, <type 'IManagedObject'>, <type 'object'>
    """ RegistrationHelperTx() """
    def InstallAssembly(self, assembly, application, *__args) -> Tuple_[str, str]:
        """
        InstallAssembly(self: RegistrationHelperTx, assembly: str, application: str, tlb: str, installFlags: InstallationFlags, sync: object) -> (str, str)
        InstallAssembly(self: RegistrationHelperTx, assembly: str, application: str, partition: str, tlb: str, installFlags: InstallationFlags, sync: object) -> (str, str)
        """
        ...

    def InstallAssemblyFromConfig(self, regConfig:RegistrationConfig, sync:object) -> RegistrationConfig:
        """ InstallAssemblyFromConfig(self: RegistrationHelperTx, regConfig: RegistrationConfig, sync: object) -> RegistrationConfig """
        ...

    def IsInTransaction(self) -> bool:
        """ IsInTransaction(self: RegistrationHelperTx) -> bool """
        ...

    def UninstallAssembly(self, assembly:str, application:str, *__args:object): # -> 
        """ UninstallAssembly(self: RegistrationHelperTx, assembly: str, application: str, sync: object)UninstallAssembly(self: RegistrationHelperTx, assembly: str, application: str, partition: str, sync: object) """
        ...

    def UninstallAssemblyFromConfig(self, regConfig:RegistrationConfig, sync:object) -> RegistrationConfig:
        """ UninstallAssemblyFromConfig(self: RegistrationHelperTx, regConfig: RegistrationConfig, sync: object) -> RegistrationConfig """
        ...


class ResourcePool(IObjPool): # skipped bases: <type 'object'>
    """ ResourcePool(cb: TransactionEndDelegate) """
    def GetResource(self) -> object:
        """ GetResource(self: ResourcePool) -> object """
        ...

    def PutResource(self, resource:object) -> bool:
        """ PutResource(self: ResourcePool, resource: object) -> bool """
        ...

    def TransactionEndDelegate(self, *args): #cannot find CLR method
        """ TransactionEndDelegate(object: object, method: IntPtr) """
        ...



class SecureMethodAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SecureMethodAttribute() """
    pass

class SecurityCallContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Callers(self) -> SecurityCallers:
        """ Get: Callers(self: SecurityCallContext) -> SecurityCallers """
        ...

    @property
    def CurrentCall(self) -> SecurityCallContext:
        """ Get: CurrentCall() -> SecurityCallContext """
        ...

    @property
    def DirectCaller(self) -> SecurityIdentity:
        """ Get: DirectCaller(self: SecurityCallContext) -> SecurityIdentity """
        ...

    @property
    def IsSecurityEnabled(self) -> bool:
        """ Get: IsSecurityEnabled(self: SecurityCallContext) -> bool """
        ...

    @property
    def MinAuthenticationLevel(self) -> int:
        """ Get: MinAuthenticationLevel(self: SecurityCallContext) -> int """
        ...

    @property
    def NumCallers(self) -> int:
        """ Get: NumCallers(self: SecurityCallContext) -> int """
        ...

    @property
    def OriginalCaller(self) -> SecurityIdentity:
        """ Get: OriginalCaller(self: SecurityCallContext) -> SecurityIdentity """
        ...


    def IsCallerInRole(self, role:str) -> bool:
        """ IsCallerInRole(self: SecurityCallContext, role: str) -> bool """
        ...

    def IsUserInRole(self, user:str, role:str) -> bool:
        """ IsUserInRole(self: SecurityCallContext, user: str, role: str) -> bool """
        ...


class SecurityCallers(IEnumerable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: SecurityCallers) -> int """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class SecurityIdentity: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AccountName(self) -> str:
        """ Get: AccountName(self: SecurityIdentity) -> str """
        ...

    @property
    def AuthenticationLevel(self) -> AuthenticationOption:
        """ Get: AuthenticationLevel(self: SecurityIdentity) -> AuthenticationOption """
        ...

    @property
    def AuthenticationService(self) -> int:
        """ Get: AuthenticationService(self: SecurityIdentity) -> int """
        ...

    @property
    def ImpersonationLevel(self) -> ImpersonationLevelOption:
        """ Get: ImpersonationLevel(self: SecurityIdentity) -> ImpersonationLevelOption """
        ...



class SecurityRoleAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SecurityRoleAttribute(role: str)
    SecurityRoleAttribute(role: str, everyone: bool)
    """
    @property
    def Description(self) -> str:
        """
        Get: Description(self: SecurityRoleAttribute) -> str
        Set: Description(self: SecurityRoleAttribute) = value
        """
        ...

    @property
    def Role(self) -> str:
        """
        Get: Role(self: SecurityRoleAttribute) -> str
        Set: Role(self: SecurityRoleAttribute) = value
        """
        ...

    @property
    def SetEveryoneAccess(self) -> bool:
        """
        Get: SetEveryoneAccess(self: SecurityRoleAttribute) -> bool
        Set: SetEveryoneAccess(self: SecurityRoleAttribute) = value
        """
        ...


    def __new__(cls, role:str, everyone:bool = ...) -> Self:
        """
        __new__(cls: type, role: str)
        __new__(cls: type, role: str, everyone: bool)
        """
        ...


class ServiceConfig: # skipped bases: <type 'object'>, <type 'object'>
    """ ServiceConfig() """
    @property
    def Binding(self) -> BindingOption:
        """
        Get: Binding(self: ServiceConfig) -> BindingOption
        Set: Binding(self: ServiceConfig) = value
        """
        ...

    @property
    def BringYourOwnSystemTransaction(self) -> Transaction:
        """
        Get: BringYourOwnSystemTransaction(self: ServiceConfig) -> Transaction
        Set: BringYourOwnSystemTransaction(self: ServiceConfig) = value
        """
        ...

    @property
    def BringYourOwnTransaction(self) -> ITransaction:
        """
        Get: BringYourOwnTransaction(self: ServiceConfig) -> ITransaction
        Set: BringYourOwnTransaction(self: ServiceConfig) = value
        """
        ...

    @property
    def COMTIIntrinsicsEnabled(self) -> bool:
        """
        Get: COMTIIntrinsicsEnabled(self: ServiceConfig) -> bool
        Set: COMTIIntrinsicsEnabled(self: ServiceConfig) = value
        """
        ...

    @property
    def IISIntrinsicsEnabled(self) -> bool:
        """
        Get: IISIntrinsicsEnabled(self: ServiceConfig) -> bool
        Set: IISIntrinsicsEnabled(self: ServiceConfig) = value
        """
        ...

    @property
    def Inheritance(self) -> InheritanceOption:
        """
        Get: Inheritance(self: ServiceConfig) -> InheritanceOption
        Set: Inheritance(self: ServiceConfig) = value
        """
        ...

    @property
    def IsolationLevel(self) -> TransactionIsolationLevel:
        """
        Get: IsolationLevel(self: ServiceConfig) -> TransactionIsolationLevel
        Set: IsolationLevel(self: ServiceConfig) = value
        """
        ...

    @property
    def PartitionId(self) -> Guid:
        """
        Get: PartitionId(self: ServiceConfig) -> Guid
        Set: PartitionId(self: ServiceConfig) = value
        """
        ...

    @property
    def PartitionOption(self) -> PartitionOption:
        """
        Get: PartitionOption(self: ServiceConfig) -> PartitionOption
        Set: PartitionOption(self: ServiceConfig) = value
        """
        ...

    @property
    def SxsDirectory(self) -> str:
        """
        Get: SxsDirectory(self: ServiceConfig) -> str
        Set: SxsDirectory(self: ServiceConfig) = value
        """
        ...

    @property
    def SxsName(self) -> str:
        """
        Get: SxsName(self: ServiceConfig) -> str
        Set: SxsName(self: ServiceConfig) = value
        """
        ...

    @property
    def SxsOption(self) -> SxsOption:
        """
        Get: SxsOption(self: ServiceConfig) -> SxsOption
        Set: SxsOption(self: ServiceConfig) = value
        """
        ...

    @property
    def Synchronization(self) -> SynchronizationOption:
        """
        Get: Synchronization(self: ServiceConfig) -> SynchronizationOption
        Set: Synchronization(self: ServiceConfig) = value
        """
        ...

    @property
    def ThreadPool(self) -> ThreadPoolOption:
        """
        Get: ThreadPool(self: ServiceConfig) -> ThreadPoolOption
        Set: ThreadPool(self: ServiceConfig) = value
        """
        ...

    @property
    def TipUrl(self) -> str:
        """
        Get: TipUrl(self: ServiceConfig) -> str
        Set: TipUrl(self: ServiceConfig) = value
        """
        ...

    @property
    def TrackingAppName(self) -> str:
        """
        Get: TrackingAppName(self: ServiceConfig) -> str
        Set: TrackingAppName(self: ServiceConfig) = value
        """
        ...

    @property
    def TrackingComponentName(self) -> str:
        """
        Get: TrackingComponentName(self: ServiceConfig) -> str
        Set: TrackingComponentName(self: ServiceConfig) = value
        """
        ...

    @property
    def TrackingEnabled(self) -> bool:
        """
        Get: TrackingEnabled(self: ServiceConfig) -> bool
        Set: TrackingEnabled(self: ServiceConfig) = value
        """
        ...

    @property
    def Transaction(self) -> TransactionOption:
        """
        Get: Transaction(self: ServiceConfig) -> TransactionOption
        Set: Transaction(self: ServiceConfig) = value
        """
        ...

    @property
    def TransactionDescription(self) -> str:
        """
        Get: TransactionDescription(self: ServiceConfig) -> str
        Set: TransactionDescription(self: ServiceConfig) = value
        """
        ...

    @property
    def TransactionTimeout(self) -> int:
        """
        Get: TransactionTimeout(self: ServiceConfig) -> int
        Set: TransactionTimeout(self: ServiceConfig) = value
        """
        ...



class ServicedComponentException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ServicedComponentException()
    ServicedComponentException(message: str)
    ServicedComponentException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ServiceDomain: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Enter(cfg:ServiceConfig): # -> 
        """ Enter(cfg: ServiceConfig) """
        ...

    @staticmethod
    def Leave() -> TransactionStatus:
        """ Leave() -> TransactionStatus """
        ...


class SharedProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Value(self) -> object:
        """
        Get: Value(self: SharedProperty) -> object
        Set: Value(self: SharedProperty) = value
        """
        ...



class SharedPropertyGroup: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateProperty(self, name, fExists) -> Tuple_[SharedProperty, bool]:
        """ CreateProperty(self: SharedPropertyGroup, name: str) -> (SharedProperty, bool) """
        ...

    def CreatePropertyByPosition(self, position, fExists) -> Tuple_[SharedProperty, bool]:
        """ CreatePropertyByPosition(self: SharedPropertyGroup, position: int) -> (SharedProperty, bool) """
        ...

    def Property(self, name:str) -> SharedProperty:
        """ Property(self: SharedPropertyGroup, name: str) -> SharedProperty """
        ...

    def PropertyByPosition(self, position:int) -> SharedProperty:
        """ PropertyByPosition(self: SharedPropertyGroup, position: int) -> SharedProperty """
        ...


class SharedPropertyGroupManager(IEnumerable): # skipped bases: <type 'object'>
    """ SharedPropertyGroupManager() """
    def CreatePropertyGroup(self, name, dwIsoMode, dwRelMode, fExist) -> Tuple_[SharedPropertyGroup, PropertyLockMode, PropertyReleaseMode, bool]:
        """ CreatePropertyGroup(self: SharedPropertyGroupManager, name: str, dwIsoMode: PropertyLockMode, dwRelMode: PropertyReleaseMode) -> (SharedPropertyGroup, PropertyLockMode, PropertyReleaseMode, bool) """
        ...

    def Group(self, name:str) -> SharedPropertyGroup:
        """ Group(self: SharedPropertyGroupManager, name: str) -> SharedPropertyGroup """
        ...


class SxsOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SxsOption, values: Ignore (0), Inherit (1), New (2) """
    Ignore: SxsOption = ...
    Inherit: SxsOption = ...
    New: SxsOption = ...
    value__ = ...


class SynchronizationAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SynchronizationAttribute()
    SynchronizationAttribute(val: SynchronizationOption)
    """
    @property
    def Value(self) -> SynchronizationOption:
        """ Get: Value(self: SynchronizationAttribute) -> SynchronizationOption """
        ...


    def __new__(cls, val:SynchronizationOption = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, val: SynchronizationOption)
        """
        ...


class SynchronizationOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SynchronizationOption, values: Disabled (0), NotSupported (1), Required (3), RequiresNew (4), Supported (2) """
    Disabled: SynchronizationOption = ...
    NotSupported: SynchronizationOption = ...
    Required: SynchronizationOption = ...
    RequiresNew: SynchronizationOption = ...
    Supported: SynchronizationOption = ...
    value__ = ...


class ThreadPoolOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ThreadPoolOption, values: Inherit (1), MTA (3), None (0), STA (2) """
    Inherit: ThreadPoolOption = ...
    MTA: ThreadPoolOption = ...
    STA: ThreadPoolOption = ...
    value__ = ...


class TransactionAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    TransactionAttribute()
    TransactionAttribute(val: TransactionOption)
    """
    @property
    def Isolation(self) -> TransactionIsolationLevel:
        """
        Get: Isolation(self: TransactionAttribute) -> TransactionIsolationLevel
        Set: Isolation(self: TransactionAttribute) = value
        """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: TransactionAttribute) -> int
        Set: Timeout(self: TransactionAttribute) = value
        """
        ...

    @property
    def Value(self) -> TransactionOption:
        """ Get: Value(self: TransactionAttribute) -> TransactionOption """
        ...


    def __new__(cls, val:TransactionOption = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, val: TransactionOption)
        """
        ...


class TransactionIsolationLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TransactionIsolationLevel, values: Any (0), ReadCommitted (2), ReadUncommitted (1), RepeatableRead (3), Serializable (4) """
    Any: TransactionIsolationLevel = ...
    ReadCommitted: TransactionIsolationLevel = ...
    ReadUncommitted: TransactionIsolationLevel = ...
    RepeatableRead: TransactionIsolationLevel = ...
    Serializable: TransactionIsolationLevel = ...
    value__ = ...


class TransactionOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TransactionOption, values: Disabled (0), NotSupported (1), Required (3), RequiresNew (4), Supported (2) """
    Disabled: TransactionOption = ...
    NotSupported: TransactionOption = ...
    Required: TransactionOption = ...
    RequiresNew: TransactionOption = ...
    Supported: TransactionOption = ...
    value__ = ...


class TransactionStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TransactionStatus, values: Aborted (4), Aborting (3), Commited (0), LocallyOk (1), NoTransaction (2) """
    Aborted: TransactionStatus = ...
    Aborting: TransactionStatus = ...
    Commited: TransactionStatus = ...
    LocallyOk: TransactionStatus = ...
    NoTransaction: TransactionStatus = ...
    value__ = ...


class TransactionVote(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TransactionVote, values: Abort (1), Commit (0) """
    Abort: TransactionVote = ...
    Commit: TransactionVote = ...
    value__ = ...


class XACTTRANSINFO: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    grfRMSupported = ...
    grfRMSupportedRetaining = ...
    grfTCSupported = ...
    grfTCSupportedRetaining = ...
    isoFlags = ...
    isoLevel = ...
    uow = ...


# variables with complex values

