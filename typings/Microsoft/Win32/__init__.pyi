# encoding: utf-8
# module Microsoft.Win32 calls itself Win32
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Win32.SafeHandles import SafeRegistryHandle

from System import (Array, AsyncCallback, Delegate, Enum, EventArgs, 
    IAsyncResult, IDisposable, IntPtr, MarshalByRefObject, MulticastDelegate)

from System.Net import ICredentialPolicy

from System.Security.AccessControl import (AccessControlSections, 
    RegistrySecurity)

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class IntranetZoneCredentialPolicy(ICredentialPolicy): # skipped bases: <type 'object'>
    """ IntranetZoneCredentialPolicy() """
    pass

class PowerModeChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ PowerModeChangedEventArgs(mode: PowerModes) """
    @property
    def Mode(self) -> PowerModes:
        """ Get: Mode(self: PowerModeChangedEventArgs) -> PowerModes """
        ...


    def __new__(cls, mode:PowerModes) -> Self:
        """ __new__(cls: type, mode: PowerModes) """
        ...


class PowerModeChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ PowerModeChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:PowerModeChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: PowerModeChangedEventHandler, sender: object, e: PowerModeChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: PowerModeChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:PowerModeChangedEventArgs): # -> 
        """ Invoke(self: PowerModeChangedEventHandler, sender: object, e: PowerModeChangedEventArgs) """
        ...


class PowerModes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PowerModes, values: Resume (1), StatusChange (2), Suspend (3) """
    Resume: PowerModes = ...
    StatusChange: PowerModes = ...
    Suspend: PowerModes = ...
    value__ = ...


class Registry: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetValue(keyName:str, valueName:str, defaultValue:object) -> object:
        """ GetValue(keyName: str, valueName: str, defaultValue: object) -> object """
        ...

    @staticmethod
    def SetValue(keyName:str, valueName:str, value:object, valueKind:RegistryValueKind = ...): # -> 
        """ SetValue(keyName: str, valueName: str, value: object, valueKind: RegistryValueKind)SetValue(keyName: str, valueName: str, value: object) """
        ...

    ClassesRoot: RegistryKey = ...
    CurrentConfig: RegistryKey = ...
    CurrentUser: RegistryKey = ...
    DynData: RegistryKey = ...
    LocalMachine: RegistryKey = ...
    PerformanceData: RegistryKey = ...
    Users: RegistryKey = ...
    __all__: list = ...


class RegistryHive(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RegistryHive, values: ClassesRoot (-2147483648), CurrentConfig (-2147483643), CurrentUser (-2147483647), DynData (-2147483642), LocalMachine (-2147483646), PerformanceData (-2147483644), Users (-2147483645) """
    ClassesRoot: RegistryHive = ...
    CurrentConfig: RegistryHive = ...
    CurrentUser: RegistryHive = ...
    DynData: RegistryHive = ...
    LocalMachine: RegistryHive = ...
    PerformanceData: RegistryHive = ...
    Users: RegistryHive = ...
    value__ = ...


class RegistryKey(IDisposable, MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Handle(self) -> SafeRegistryHandle:
        """ Get: Handle(self: RegistryKey) -> SafeRegistryHandle """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: RegistryKey) -> str """
        ...

    @property
    def SubKeyCount(self) -> int:
        """ Get: SubKeyCount(self: RegistryKey) -> int """
        ...

    @property
    def ValueCount(self) -> int:
        """ Get: ValueCount(self: RegistryKey) -> int """
        ...

    @property
    def View(self) -> RegistryView:
        """ Get: View(self: RegistryKey) -> RegistryView """
        ...


    def Close(self): # -> 
        """ Close(self: RegistryKey) """
        ...

    def CreateSubKey(self, subkey:str, *__args:RegistryKeyPermissionCheck) -> RegistryKey:
        """
        CreateSubKey(self: RegistryKey, subkey: str) -> RegistryKey
        CreateSubKey(self: RegistryKey, subkey: str, permissionCheck: RegistryKeyPermissionCheck) -> RegistryKey
        CreateSubKey(self: RegistryKey, subkey: str, permissionCheck: RegistryKeyPermissionCheck, options: RegistryOptions) -> RegistryKey
        CreateSubKey(self: RegistryKey, subkey: str, writable: bool) -> RegistryKey
        CreateSubKey(self: RegistryKey, subkey: str, writable: bool, options: RegistryOptions) -> RegistryKey
        CreateSubKey(self: RegistryKey, subkey: str, permissionCheck: RegistryKeyPermissionCheck, registrySecurity: RegistrySecurity) -> RegistryKey
        CreateSubKey(self: RegistryKey, subkey: str, permissionCheck: RegistryKeyPermissionCheck, registryOptions: RegistryOptions, registrySecurity: RegistrySecurity) -> RegistryKey
        """
        ...

    def DeleteSubKey(self, subkey:str, throwOnMissingSubKey:bool = ...): # -> 
        """ DeleteSubKey(self: RegistryKey, subkey: str)DeleteSubKey(self: RegistryKey, subkey: str, throwOnMissingSubKey: bool) """
        ...

    def DeleteSubKeyTree(self, subkey:str, throwOnMissingSubKey:bool = ...): # -> 
        """ DeleteSubKeyTree(self: RegistryKey, subkey: str)DeleteSubKeyTree(self: RegistryKey, subkey: str, throwOnMissingSubKey: bool) """
        ...

    def DeleteValue(self, name:str, throwOnMissingValue:bool = ...): # -> 
        """ DeleteValue(self: RegistryKey, name: str)DeleteValue(self: RegistryKey, name: str, throwOnMissingValue: bool) """
        ...

    def Flush(self): # -> 
        """ Flush(self: RegistryKey) """
        ...

    @staticmethod
    def FromHandle(handle:SafeRegistryHandle, view:RegistryView = ...) -> RegistryKey:
        """
        FromHandle(handle: SafeRegistryHandle) -> RegistryKey
        FromHandle(handle: SafeRegistryHandle, view: RegistryView) -> RegistryKey
        """
        ...

    def GetAccessControl(self, includeSections:AccessControlSections = ...) -> RegistrySecurity:
        """
        GetAccessControl(self: RegistryKey) -> RegistrySecurity
        GetAccessControl(self: RegistryKey, includeSections: AccessControlSections) -> RegistrySecurity
        """
        ...

    def GetSubKeyNames(self) -> Array:
        """ GetSubKeyNames(self: RegistryKey) -> Array[str] """
        ...

    def GetValue(self, name:str, defaultValue:object = ..., options:RegistryValueOptions = ...) -> object:
        """
        GetValue(self: RegistryKey, name: str) -> object
        GetValue(self: RegistryKey, name: str, defaultValue: object) -> object
        GetValue(self: RegistryKey, name: str, defaultValue: object, options: RegistryValueOptions) -> object
        """
        ...

    def GetValueKind(self, name:str) -> RegistryValueKind:
        """ GetValueKind(self: RegistryKey, name: str) -> RegistryValueKind """
        ...

    def GetValueNames(self) -> Array:
        """ GetValueNames(self: RegistryKey) -> Array[str] """
        ...

    @staticmethod
    def OpenBaseKey(hKey:RegistryHive, view:RegistryView) -> RegistryKey:
        """ OpenBaseKey(hKey: RegistryHive, view: RegistryView) -> RegistryKey """
        ...

    @staticmethod
    def OpenRemoteBaseKey(hKey:RegistryHive, machineName:str, view:RegistryView = ...) -> RegistryKey:
        """
        OpenRemoteBaseKey(hKey: RegistryHive, machineName: str) -> RegistryKey
        OpenRemoteBaseKey(hKey: RegistryHive, machineName: str, view: RegistryView) -> RegistryKey
        """
        ...

    def OpenSubKey(self, name:str, *__args:bool) -> RegistryKey:
        """
        OpenSubKey(self: RegistryKey, name: str, writable: bool) -> RegistryKey
        OpenSubKey(self: RegistryKey, name: str, permissionCheck: RegistryKeyPermissionCheck) -> RegistryKey
        OpenSubKey(self: RegistryKey, name: str, rights: RegistryRights) -> RegistryKey
        OpenSubKey(self: RegistryKey, name: str, permissionCheck: RegistryKeyPermissionCheck, rights: RegistryRights) -> RegistryKey
        OpenSubKey(self: RegistryKey, name: str) -> RegistryKey
        """
        ...

    def SetAccessControl(self, registrySecurity:RegistrySecurity): # -> 
        """ SetAccessControl(self: RegistryKey, registrySecurity: RegistrySecurity) """
        ...

    def SetValue(self, name:str, value:object, valueKind:RegistryValueKind = ...): # -> 
        """ SetValue(self: RegistryKey, name: str, value: object)SetValue(self: RegistryKey, name: str, value: object, valueKind: RegistryValueKind) """
        ...

    def ToString(self) -> str:
        """ ToString(self: RegistryKey) -> str """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class RegistryKeyPermissionCheck(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RegistryKeyPermissionCheck, values: Default (0), ReadSubTree (1), ReadWriteSubTree (2) """
    Default: RegistryKeyPermissionCheck = ...
    ReadSubTree: RegistryKeyPermissionCheck = ...
    ReadWriteSubTree: RegistryKeyPermissionCheck = ...
    value__ = ...


class RegistryOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) RegistryOptions, values: None (0), Volatile (1) """
    value__ = ...
    Volatile: RegistryOptions = ...


class RegistryValueKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RegistryValueKind, values: Binary (3), DWord (4), ExpandString (2), MultiString (7), None (-1), QWord (11), String (1), Unknown (0) """
    Binary: RegistryValueKind = ...
    DWord: RegistryValueKind = ...
    ExpandString: RegistryValueKind = ...
    MultiString: RegistryValueKind = ...
    QWord: RegistryValueKind = ...
    String: RegistryValueKind = ...
    Unknown: RegistryValueKind = ...
    value__ = ...


class RegistryValueOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) RegistryValueOptions, values: DoNotExpandEnvironmentNames (1), None (0) """
    DoNotExpandEnvironmentNames: RegistryValueOptions = ...
    value__ = ...


class RegistryView(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RegistryView, values: Default (0), Registry32 (512), Registry64 (256) """
    Default: RegistryView = ...
    Registry32: RegistryView = ...
    Registry64: RegistryView = ...
    value__ = ...


class SessionEndedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SessionEndedEventArgs(reason: SessionEndReasons) """
    @property
    def Reason(self) -> SessionEndReasons:
        """ Get: Reason(self: SessionEndedEventArgs) -> SessionEndReasons """
        ...


    def __new__(cls, reason:SessionEndReasons) -> Self:
        """ __new__(cls: type, reason: SessionEndReasons) """
        ...


class SessionEndedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SessionEndedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SessionEndedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SessionEndedEventHandler, sender: object, e: SessionEndedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SessionEndedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SessionEndedEventArgs): # -> 
        """ Invoke(self: SessionEndedEventHandler, sender: object, e: SessionEndedEventArgs) """
        ...


class SessionEndingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SessionEndingEventArgs(reason: SessionEndReasons) """
    @property
    def Cancel(self) -> bool:
        """
        Get: Cancel(self: SessionEndingEventArgs) -> bool
        Set: Cancel(self: SessionEndingEventArgs) = value
        """
        ...

    @property
    def Reason(self) -> SessionEndReasons:
        """ Get: Reason(self: SessionEndingEventArgs) -> SessionEndReasons """
        ...


    def __new__(cls, reason:SessionEndReasons) -> Self:
        """ __new__(cls: type, reason: SessionEndReasons) """
        ...


class SessionEndingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SessionEndingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SessionEndingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SessionEndingEventHandler, sender: object, e: SessionEndingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SessionEndingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SessionEndingEventArgs): # -> 
        """ Invoke(self: SessionEndingEventHandler, sender: object, e: SessionEndingEventArgs) """
        ...


class SessionEndReasons(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SessionEndReasons, values: Logoff (1), SystemShutdown (2) """
    Logoff: SessionEndReasons = ...
    SystemShutdown: SessionEndReasons = ...
    value__ = ...


class SessionSwitchEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SessionSwitchEventArgs(reason: SessionSwitchReason) """
    @property
    def Reason(self) -> SessionSwitchReason:
        """ Get: Reason(self: SessionSwitchEventArgs) -> SessionSwitchReason """
        ...


    def __new__(cls, reason:SessionSwitchReason) -> Self:
        """ __new__(cls: type, reason: SessionSwitchReason) """
        ...


class SessionSwitchEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SessionSwitchEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SessionSwitchEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SessionSwitchEventHandler, sender: object, e: SessionSwitchEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SessionSwitchEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SessionSwitchEventArgs): # -> 
        """ Invoke(self: SessionSwitchEventHandler, sender: object, e: SessionSwitchEventArgs) """
        ...


class SessionSwitchReason(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SessionSwitchReason, values: ConsoleConnect (1), ConsoleDisconnect (2), RemoteConnect (3), RemoteDisconnect (4), SessionLock (7), SessionLogoff (6), SessionLogon (5), SessionRemoteControl (9), SessionUnlock (8) """
    ConsoleConnect: SessionSwitchReason = ...
    ConsoleDisconnect: SessionSwitchReason = ...
    RemoteConnect: SessionSwitchReason = ...
    RemoteDisconnect: SessionSwitchReason = ...
    SessionLock: SessionSwitchReason = ...
    SessionLogoff: SessionSwitchReason = ...
    SessionLogon: SessionSwitchReason = ...
    SessionRemoteControl: SessionSwitchReason = ...
    SessionUnlock: SessionSwitchReason = ...
    value__ = ...


class SystemEvents: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateTimer(interval:int) -> IntPtr:
        """ CreateTimer(interval: int) -> IntPtr """
        ...

    @staticmethod
    def InvokeOnEventsThread(method:Delegate): # -> 
        """ InvokeOnEventsThread(method: Delegate) """
        ...

    @staticmethod
    def KillTimer(timerId:IntPtr): # -> 
        """ KillTimer(timerId: IntPtr) """
        ...

    DisplaySettingsChanged = ...
    DisplaySettingsChanging = ...
    EventsThreadShutdown = ...
    InstalledFontsChanged = ...
    LowMemory = ...
    PaletteChanged = ...
    PowerModeChanged = ...
    SessionEnded = ...
    SessionEnding = ...
    SessionSwitch = ...
    TimeChanged = ...
    TimerElapsed = ...
    UserPreferenceChanged = ...
    UserPreferenceChanging = ...


class TimerElapsedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ TimerElapsedEventArgs(timerId: IntPtr) """
    @property
    def TimerId(self) -> IntPtr:
        """ Get: TimerId(self: TimerElapsedEventArgs) -> IntPtr """
        ...


    def __new__(cls, timerId:IntPtr) -> Self:
        """ __new__(cls: type, timerId: IntPtr) """
        ...


class TimerElapsedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TimerElapsedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:TimerElapsedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: TimerElapsedEventHandler, sender: object, e: TimerElapsedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: TimerElapsedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:TimerElapsedEventArgs): # -> 
        """ Invoke(self: TimerElapsedEventHandler, sender: object, e: TimerElapsedEventArgs) """
        ...


class UserPreferenceCategory(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UserPreferenceCategory, values: Accessibility (1), Color (2), Desktop (3), General (4), Icon (5), Keyboard (6), Locale (13), Menu (7), Mouse (8), Policy (9), Power (10), Screensaver (11), VisualStyle (14), Window (12) """
    Accessibility: UserPreferenceCategory = ...
    Color: UserPreferenceCategory = ...
    Desktop: UserPreferenceCategory = ...
    General: UserPreferenceCategory = ...
    Icon: UserPreferenceCategory = ...
    Keyboard: UserPreferenceCategory = ...
    Locale: UserPreferenceCategory = ...
    Menu: UserPreferenceCategory = ...
    Mouse: UserPreferenceCategory = ...
    Policy: UserPreferenceCategory = ...
    Power: UserPreferenceCategory = ...
    Screensaver: UserPreferenceCategory = ...
    value__ = ...
    VisualStyle: UserPreferenceCategory = ...
    Window: UserPreferenceCategory = ...


class UserPreferenceChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ UserPreferenceChangedEventArgs(category: UserPreferenceCategory) """
    @property
    def Category(self) -> UserPreferenceCategory:
        """ Get: Category(self: UserPreferenceChangedEventArgs) -> UserPreferenceCategory """
        ...


    def __new__(cls, category:UserPreferenceCategory) -> Self:
        """ __new__(cls: type, category: UserPreferenceCategory) """
        ...


class UserPreferenceChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ UserPreferenceChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:UserPreferenceChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: UserPreferenceChangedEventHandler, sender: object, e: UserPreferenceChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: UserPreferenceChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:UserPreferenceChangedEventArgs): # -> 
        """ Invoke(self: UserPreferenceChangedEventHandler, sender: object, e: UserPreferenceChangedEventArgs) """
        ...


class UserPreferenceChangingEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ UserPreferenceChangingEventArgs(category: UserPreferenceCategory) """
    @property
    def Category(self) -> UserPreferenceCategory:
        """ Get: Category(self: UserPreferenceChangingEventArgs) -> UserPreferenceCategory """
        ...


    def __new__(cls, category:UserPreferenceCategory) -> Self:
        """ __new__(cls: type, category: UserPreferenceCategory) """
        ...


class UserPreferenceChangingEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ UserPreferenceChangingEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:UserPreferenceChangingEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: UserPreferenceChangingEventHandler, sender: object, e: UserPreferenceChangingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: UserPreferenceChangingEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:UserPreferenceChangingEventArgs): # -> 
        """ Invoke(self: UserPreferenceChangingEventHandler, sender: object, e: UserPreferenceChangingEventArgs) """
        ...


# variables with complex values

