# encoding: utf-8
# module System.ServiceProcess calls itself ServiceProcess
# from System.ServiceProcess, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, IntPtr, SystemException, TimeSpan

from System.Collections import CollectionBase, IDictionary

from System.ComponentModel import Component

from System.Configuration.Install import ComponentInstaller

from System.Diagnostics import EventLog

from System.EnterpriseServices import DescriptionAttribute

from System.Runtime.InteropServices import SafeHandle

from System.Security import IPermission

from System.Security.Permissions import (CodeAccessSecurityAttribute, 
    ResourcePermissionBase)

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class PowerBroadcastStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PowerBroadcastStatus, values: BatteryLow (9), OemEvent (11), PowerStatusChange (10), QuerySuspend (0), QuerySuspendFailed (2), ResumeAutomatic (18), ResumeCritical (6), ResumeSuspend (7), Suspend (4) """
    BatteryLow: PowerBroadcastStatus = ...
    OemEvent: PowerBroadcastStatus = ...
    PowerStatusChange: PowerBroadcastStatus = ...
    QuerySuspend: PowerBroadcastStatus = ...
    QuerySuspendFailed: PowerBroadcastStatus = ...
    ResumeAutomatic: PowerBroadcastStatus = ...
    ResumeCritical: PowerBroadcastStatus = ...
    ResumeSuspend: PowerBroadcastStatus = ...
    Suspend: PowerBroadcastStatus = ...
    value__ = ...


class ServiceAccount(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ServiceAccount, values: LocalService (0), LocalSystem (2), NetworkService (1), User (3) """
    LocalService: ServiceAccount = ...
    LocalSystem: ServiceAccount = ...
    NetworkService: ServiceAccount = ...
    User: ServiceAccount = ...
    value__ = ...


class ServiceBase(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ ServiceBase() """
    @property
    def AutoLog(self) -> bool:
        """
        Get: AutoLog(self: ServiceBase) -> bool
        Set: AutoLog(self: ServiceBase) = value
        """
        ...

    @property
    def CanHandlePowerEvent(self) -> bool:
        """
        Get: CanHandlePowerEvent(self: ServiceBase) -> bool
        Set: CanHandlePowerEvent(self: ServiceBase) = value
        """
        ...

    @property
    def CanHandleSessionChangeEvent(self) -> bool:
        """
        Get: CanHandleSessionChangeEvent(self: ServiceBase) -> bool
        Set: CanHandleSessionChangeEvent(self: ServiceBase) = value
        """
        ...

    @property
    def CanPauseAndContinue(self) -> bool:
        """
        Get: CanPauseAndContinue(self: ServiceBase) -> bool
        Set: CanPauseAndContinue(self: ServiceBase) = value
        """
        ...

    @property
    def CanShutdown(self) -> bool:
        """
        Get: CanShutdown(self: ServiceBase) -> bool
        Set: CanShutdown(self: ServiceBase) = value
        """
        ...

    @property
    def CanStop(self) -> bool:
        """
        Get: CanStop(self: ServiceBase) -> bool
        Set: CanStop(self: ServiceBase) = value
        """
        ...

    @property
    def EventLog(self) -> EventLog:
        """ Get: EventLog(self: ServiceBase) -> EventLog """
        ...

    @property
    def ExitCode(self) -> int:
        """
        Get: ExitCode(self: ServiceBase) -> int
        Set: ExitCode(self: ServiceBase) = value
        """
        ...

    @property
    def ServiceHandle(self):
        ...

    @property
    def ServiceName(self) -> str:
        """
        Get: ServiceName(self: ServiceBase) -> str
        Set: ServiceName(self: ServiceBase) = value
        """
        ...


    def OnContinue(self, *args): #cannot find CLR method
        """ OnContinue(self: ServiceBase) """
        ...

    def OnCustomCommand(self, *args): #cannot find CLR method
        """ OnCustomCommand(self: ServiceBase, command: int) """
        ...

    def OnPause(self, *args): #cannot find CLR method
        """ OnPause(self: ServiceBase) """
        ...

    def OnPowerEvent(self, *args): #cannot find CLR method
        """ OnPowerEvent(self: ServiceBase, powerStatus: PowerBroadcastStatus) -> bool """
        ...

    def OnSessionChange(self, *args): #cannot find CLR method
        """ OnSessionChange(self: ServiceBase, changeDescription: SessionChangeDescription) """
        ...

    def OnShutdown(self, *args): #cannot find CLR method
        """ OnShutdown(self: ServiceBase) """
        ...

    def OnStart(self, *args): #cannot find CLR method
        """ OnStart(self: ServiceBase, args: Array[str]) """
        ...

    def OnStop(self, *args): #cannot find CLR method
        """ OnStop(self: ServiceBase) """
        ...

    def RequestAdditionalTime(self, milliseconds:int): # -> 
        """ RequestAdditionalTime(self: ServiceBase, milliseconds: int) """
        ...

    @staticmethod
    def Run(*__args:Array): # -> 
        """ Run(services: Array[ServiceBase])Run(service: ServiceBase) """
        ...

    def ServiceMainCallback(self, argCount:int, argPointer:IntPtr): # -> 
        """ ServiceMainCallback(self: ServiceBase, argCount: int, argPointer: IntPtr) """
        ...

    def Stop(self): # -> 
        """ Stop(self: ServiceBase) """
        ...

    MaxNameLength: int = ...


class ServiceController(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    ServiceController()
    ServiceController(name: str)
    ServiceController(name: str, machineName: str)
    """
    @property
    def CanPauseAndContinue(self) -> bool:
        """ Get: CanPauseAndContinue(self: ServiceController) -> bool """
        ...

    @property
    def CanShutdown(self) -> bool:
        """ Get: CanShutdown(self: ServiceController) -> bool """
        ...

    @property
    def CanStop(self) -> bool:
        """ Get: CanStop(self: ServiceController) -> bool """
        ...

    @property
    def DependentServices(self) -> Array:
        """ Get: DependentServices(self: ServiceController) -> Array[ServiceController] """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: ServiceController) -> str
        Set: DisplayName(self: ServiceController) = value
        """
        ...

    @property
    def MachineName(self) -> str:
        """
        Get: MachineName(self: ServiceController) -> str
        Set: MachineName(self: ServiceController) = value
        """
        ...

    @property
    def ServiceHandle(self) -> SafeHandle:
        """ Get: ServiceHandle(self: ServiceController) -> SafeHandle """
        ...

    @property
    def ServiceName(self) -> str:
        """
        Get: ServiceName(self: ServiceController) -> str
        Set: ServiceName(self: ServiceController) = value
        """
        ...

    @property
    def ServicesDependedOn(self) -> Array:
        """ Get: ServicesDependedOn(self: ServiceController) -> Array[ServiceController] """
        ...

    @property
    def ServiceType(self) -> ServiceType:
        """ Get: ServiceType(self: ServiceController) -> ServiceType """
        ...

    @property
    def StartType(self) -> ServiceStartMode:
        """ Get: StartType(self: ServiceController) -> ServiceStartMode """
        ...

    @property
    def Status(self) -> ServiceControllerStatus:
        """ Get: Status(self: ServiceController) -> ServiceControllerStatus """
        ...


    def Close(self): # -> 
        """ Close(self: ServiceController) """
        ...

    def Continue(self): # -> 
        """ Continue(self: ServiceController) """
        ...

    def ExecuteCommand(self, command:int): # -> 
        """ ExecuteCommand(self: ServiceController, command: int) """
        ...

    @staticmethod
    def GetDevices(machineName:str = ...) -> Array:
        """
        GetDevices(machineName: str) -> Array[ServiceController]
        GetDevices() -> Array[ServiceController]
        """
        ...

    @staticmethod
    def GetServices(machineName:str = ...) -> Array:
        """
        GetServices(machineName: str) -> Array[ServiceController]
        GetServices() -> Array[ServiceController]
        """
        ...

    def Pause(self): # -> 
        """ Pause(self: ServiceController) """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: ServiceController) """
        ...

    def Start(self, args:Array = ...): # -> 
        """ Start(self: ServiceController)Start(self: ServiceController, args: Array[str]) """
        ...

    def Stop(self): # -> 
        """ Stop(self: ServiceController) """
        ...

    def WaitForStatus(self, desiredStatus:ServiceControllerStatus, timeout:TimeSpan = ...): # -> 
        """ WaitForStatus(self: ServiceController, desiredStatus: ServiceControllerStatus)WaitForStatus(self: ServiceController, desiredStatus: ServiceControllerStatus, timeout: TimeSpan) """
        ...

    def __new__(cls, name:str = ..., machineName:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        __new__(cls: type, name: str, machineName: str)
        """
        ...


class ServiceControllerPermission(ResourcePermissionBase): # skipped bases: <type 'IPermission'>, <type 'IUnrestrictedPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    ServiceControllerPermission()
    ServiceControllerPermission(state: PermissionState)
    ServiceControllerPermission(permissionAccess: ServiceControllerPermissionAccess, machineName: str, serviceName: str)
    ServiceControllerPermission(permissionAccessEntries: Array[ServiceControllerPermissionEntry])
    """
    @property
    def PermissionEntries(self) -> ServiceControllerPermissionEntryCollection:
        """ Get: PermissionEntries(self: ServiceControllerPermission) -> ServiceControllerPermissionEntryCollection """
        ...



class ServiceControllerPermissionAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ServiceControllerPermissionAccess, values: Browse (2), Control (6), None (0) """
    Browse: ServiceControllerPermissionAccess = ...
    Control: ServiceControllerPermissionAccess = ...
    value__ = ...


class ServiceControllerPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ServiceControllerPermissionAttribute(action: SecurityAction) """
    @property
    def MachineName(self) -> str:
        """
        Get: MachineName(self: ServiceControllerPermissionAttribute) -> str
        Set: MachineName(self: ServiceControllerPermissionAttribute) = value
        """
        ...

    @property
    def PermissionAccess(self) -> ServiceControllerPermissionAccess:
        """
        Get: PermissionAccess(self: ServiceControllerPermissionAttribute) -> ServiceControllerPermissionAccess
        Set: PermissionAccess(self: ServiceControllerPermissionAttribute) = value
        """
        ...

    @property
    def ServiceName(self) -> str:
        """
        Get: ServiceName(self: ServiceControllerPermissionAttribute) -> str
        Set: ServiceName(self: ServiceControllerPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: ServiceControllerPermissionAttribute) -> IPermission """
        ...


class ServiceControllerPermissionEntry: # skipped bases: <type 'object'>, <type 'object'>
    """
    ServiceControllerPermissionEntry()
    ServiceControllerPermissionEntry(permissionAccess: ServiceControllerPermissionAccess, machineName: str, serviceName: str)
    """
    @property
    def MachineName(self) -> str:
        """ Get: MachineName(self: ServiceControllerPermissionEntry) -> str """
        ...

    @property
    def PermissionAccess(self) -> ServiceControllerPermissionAccess:
        """ Get: PermissionAccess(self: ServiceControllerPermissionEntry) -> ServiceControllerPermissionAccess """
        ...

    @property
    def ServiceName(self) -> str:
        """ Get: ServiceName(self: ServiceControllerPermissionEntry) -> str """
        ...



class ServiceControllerPermissionEntryCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, value:ServiceControllerPermissionEntry) -> int:
        """ Add(self: ServiceControllerPermissionEntryCollection, value: ServiceControllerPermissionEntry) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: ServiceControllerPermissionEntryCollection, value: Array[ServiceControllerPermissionEntry])AddRange(self: ServiceControllerPermissionEntryCollection, value: ServiceControllerPermissionEntryCollection) """
        ...

    def Contains(self, value:ServiceControllerPermissionEntry) -> bool:
        """ Contains(self: ServiceControllerPermissionEntryCollection, value: ServiceControllerPermissionEntry) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ServiceControllerPermissionEntryCollection, array: Array[ServiceControllerPermissionEntry], index: int) """
        ...

    def IndexOf(self, value:ServiceControllerPermissionEntry) -> int:
        """ IndexOf(self: ServiceControllerPermissionEntryCollection, value: ServiceControllerPermissionEntry) -> int """
        ...

    def Insert(self, index:int, value:ServiceControllerPermissionEntry): # -> 
        """ Insert(self: ServiceControllerPermissionEntryCollection, index: int, value: ServiceControllerPermissionEntry) """
        ...

    def Remove(self, value:ServiceControllerPermissionEntry): # -> 
        """ Remove(self: ServiceControllerPermissionEntryCollection, value: ServiceControllerPermissionEntry) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ServiceControllerStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ServiceControllerStatus, values: ContinuePending (5), Paused (7), PausePending (6), Running (4), StartPending (2), Stopped (1), StopPending (3) """
    ContinuePending: ServiceControllerStatus = ...
    Paused: ServiceControllerStatus = ...
    PausePending: ServiceControllerStatus = ...
    Running: ServiceControllerStatus = ...
    StartPending: ServiceControllerStatus = ...
    Stopped: ServiceControllerStatus = ...
    StopPending: ServiceControllerStatus = ...
    value__ = ...


class ServiceInstaller(ComponentInstaller): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ ServiceInstaller() """
    @property
    def DelayedAutoStart(self) -> bool:
        """
        Get: DelayedAutoStart(self: ServiceInstaller) -> bool
        Set: DelayedAutoStart(self: ServiceInstaller) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: ServiceInstaller) -> str
        Set: Description(self: ServiceInstaller) = value
        """
        ...

    @property
    def DisplayName(self) -> str:
        """
        Get: DisplayName(self: ServiceInstaller) -> str
        Set: DisplayName(self: ServiceInstaller) = value
        """
        ...

    @property
    def ServiceName(self) -> str:
        """
        Get: ServiceName(self: ServiceInstaller) -> str
        Set: ServiceName(self: ServiceInstaller) = value
        """
        ...

    @property
    def ServicesDependedOn(self) -> Array:
        """
        Get: ServicesDependedOn(self: ServiceInstaller) -> Array[str]
        Set: ServicesDependedOn(self: ServiceInstaller) = value
        """
        ...

    @property
    def StartType(self) -> ServiceStartMode:
        """
        Get: StartType(self: ServiceInstaller) -> ServiceStartMode
        Set: StartType(self: ServiceInstaller) = value
        """
        ...


    def Install(self, stateSaver:IDictionary): # -> 
        """ Install(self: ServiceInstaller, stateSaver: IDictionary) """
        ...

    def Rollback(self, savedState:IDictionary): # -> 
        """ Rollback(self: ServiceInstaller, savedState: IDictionary) """
        ...

    def Uninstall(self, savedState:IDictionary): # -> 
        """ Uninstall(self: ServiceInstaller, savedState: IDictionary) """
        ...


class ServiceProcessDescriptionAttribute(DescriptionAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ServiceProcessDescriptionAttribute(description: str) """
    pass

class ServiceProcessInstaller(ComponentInstaller): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ ServiceProcessInstaller() """
    @property
    def Account(self) -> ServiceAccount:
        """
        Get: Account(self: ServiceProcessInstaller) -> ServiceAccount
        Set: Account(self: ServiceProcessInstaller) = value
        """
        ...

    @property
    def HelpText(self) -> str:
        """ Get: HelpText(self: ServiceProcessInstaller) -> str """
        ...

    @property
    def Password(self) -> str:
        """
        Get: Password(self: ServiceProcessInstaller) -> str
        Set: Password(self: ServiceProcessInstaller) = value
        """
        ...

    @property
    def Username(self) -> str:
        """
        Get: Username(self: ServiceProcessInstaller) -> str
        Set: Username(self: ServiceProcessInstaller) = value
        """
        ...


    def Install(self, stateSaver:IDictionary): # -> 
        """ Install(self: ServiceProcessInstaller, stateSaver: IDictionary) """
        ...

    def Rollback(self, savedState:IDictionary): # -> 
        """ Rollback(self: ServiceProcessInstaller, savedState: IDictionary) """
        ...


class ServiceStartMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ServiceStartMode, values: Automatic (2), Boot (0), Disabled (4), Manual (3), System (1) """
    Automatic: ServiceStartMode = ...
    Boot: ServiceStartMode = ...
    Disabled: ServiceStartMode = ...
    Manual: ServiceStartMode = ...
    System: ServiceStartMode = ...
    value__ = ...


class ServiceType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ServiceType, values: Adapter (4), FileSystemDriver (2), InteractiveProcess (256), KernelDriver (1), RecognizerDriver (8), Win32OwnProcess (16), Win32ShareProcess (32) """
    Adapter: ServiceType = ...
    FileSystemDriver: ServiceType = ...
    InteractiveProcess: ServiceType = ...
    KernelDriver: ServiceType = ...
    RecognizerDriver: ServiceType = ...
    value__ = ...
    Win32OwnProcess: ServiceType = ...
    Win32ShareProcess: ServiceType = ...


class SessionChangeDescription: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Reason(self) -> SessionChangeReason:
        """ Get: Reason(self: SessionChangeDescription) -> SessionChangeReason """
        ...

    @property
    def SessionId(self) -> int:
        """ Get: SessionId(self: SessionChangeDescription) -> int """
        ...


    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: SessionChangeDescription, obj: object) -> bool
        Equals(self: SessionChangeDescription, changeDescription: SessionChangeDescription) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SessionChangeDescription) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SessionChangeReason(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SessionChangeReason, values: ConsoleConnect (1), ConsoleDisconnect (2), RemoteConnect (3), RemoteDisconnect (4), SessionLock (7), SessionLogoff (6), SessionLogon (5), SessionRemoteControl (9), SessionUnlock (8) """
    ConsoleConnect: SessionChangeReason = ...
    ConsoleDisconnect: SessionChangeReason = ...
    RemoteConnect: SessionChangeReason = ...
    RemoteDisconnect: SessionChangeReason = ...
    SessionLock: SessionChangeReason = ...
    SessionLogoff: SessionChangeReason = ...
    SessionLogon: SessionChangeReason = ...
    SessionRemoteControl: SessionChangeReason = ...
    SessionUnlock: SessionChangeReason = ...
    value__ = ...


class TimeoutException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TimeoutException()
    TimeoutException(message: str)
    TimeoutException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


# variables with complex values

