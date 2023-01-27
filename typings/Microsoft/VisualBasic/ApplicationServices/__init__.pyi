# encoding: utf-8
# module Microsoft.VisualBasic.ApplicationServices calls itself ApplicationServices
# from Microsoft.VisualBasic, Version=10.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic.Logging import Log

from System import (Array, AsyncCallback, Enum, EventArgs, IAsyncResult, 
    Int64, MulticastDelegate, Version)

from System.Collections.ObjectModel import ReadOnlyCollection

from System.ComponentModel import CancelEventArgs, TypeConverter

from System.Deployment.Application import ApplicationDeployment

from System.Globalization import CultureInfo

from System.Security.Principal import IPrincipal

from System.Threading import ThreadExceptionEventArgs

from System.Windows.Forms import ApplicationContext, Form, FormCollection

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class ApplicationBase: # skipped bases: <type 'object'>, <type 'object'>
    """ ApplicationBase() """
    @property
    def Culture(self) -> CultureInfo:
        """ Get: Culture(self: ApplicationBase) -> CultureInfo """
        ...

    @property
    def Info(self) -> AssemblyInfo:
        """ Get: Info(self: ApplicationBase) -> AssemblyInfo """
        ...

    @property
    def Log(self) -> Log:
        """ Get: Log(self: ApplicationBase) -> Log """
        ...

    @property
    def UICulture(self) -> CultureInfo:
        """ Get: UICulture(self: ApplicationBase) -> CultureInfo """
        ...


    def ChangeCulture(self, cultureName:str): # -> 
        """ ChangeCulture(self: ApplicationBase, cultureName: str) """
        ...

    def ChangeUICulture(self, cultureName:str): # -> 
        """ ChangeUICulture(self: ApplicationBase, cultureName: str) """
        ...

    def GetEnvironmentVariable(self, name:str) -> str:
        """ GetEnvironmentVariable(self: ApplicationBase, name: str) -> str """
        ...


class AssemblyInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ AssemblyInfo(currentAssembly: Assembly) """
    @property
    def AssemblyName(self) -> str:
        """ Get: AssemblyName(self: AssemblyInfo) -> str """
        ...

    @property
    def CompanyName(self) -> str:
        """ Get: CompanyName(self: AssemblyInfo) -> str """
        ...

    @property
    def Copyright(self) -> str:
        """ Get: Copyright(self: AssemblyInfo) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: AssemblyInfo) -> str """
        ...

    @property
    def DirectoryPath(self) -> str:
        """ Get: DirectoryPath(self: AssemblyInfo) -> str """
        ...

    @property
    def LoadedAssemblies(self) -> ReadOnlyCollection:
        """ Get: LoadedAssemblies(self: AssemblyInfo) -> ReadOnlyCollection[Assembly] """
        ...

    @property
    def ProductName(self) -> str:
        """ Get: ProductName(self: AssemblyInfo) -> str """
        ...

    @property
    def StackTrace(self) -> str:
        """ Get: StackTrace(self: AssemblyInfo) -> str """
        ...

    @property
    def Title(self) -> str:
        """ Get: Title(self: AssemblyInfo) -> str """
        ...

    @property
    def Trademark(self) -> str:
        """ Get: Trademark(self: AssemblyInfo) -> str """
        ...

    @property
    def Version(self) -> Version:
        """ Get: Version(self: AssemblyInfo) -> Version """
        ...

    @property
    def WorkingSet(self) -> Int64:
        """ Get: WorkingSet(self: AssemblyInfo) -> Int64 """
        ...



class AuthenticationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AuthenticationMode, values: ApplicationDefined (1), Windows (0) """
    ApplicationDefined: AuthenticationMode = ...
    value__ = ...
    Windows: AuthenticationMode = ...


class BuiltInRole(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum BuiltInRole, values: AccountOperator (548), Administrator (544), BackupOperator (551), Guest (546), PowerUser (547), PrintOperator (550), Replicator (552), SystemOperator (549), User (545) """
    AccountOperator: BuiltInRole = ...
    Administrator: BuiltInRole = ...
    BackupOperator: BuiltInRole = ...
    Guest: BuiltInRole = ...
    PowerUser: BuiltInRole = ...
    PrintOperator: BuiltInRole = ...
    Replicator: BuiltInRole = ...
    SystemOperator: BuiltInRole = ...
    User: BuiltInRole = ...
    value__ = ...


class BuiltInRoleConverter(TypeConverter): # skipped bases: <type 'object'>
    """ BuiltInRoleConverter() """
    pass

class CantStartSingleInstanceException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CantStartSingleInstanceException()
    CantStartSingleInstanceException(message: str)
    CantStartSingleInstanceException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class ConsoleApplicationBase(ApplicationBase): # skipped bases: <type 'object'>
    """ ConsoleApplicationBase() """
    @property
    def CommandLineArgs(self) -> ReadOnlyCollection:
        """ Get: CommandLineArgs(self: ConsoleApplicationBase) -> ReadOnlyCollection[str] """
        ...

    @property
    def Deployment(self) -> ApplicationDeployment:
        """ Get: Deployment(self: ConsoleApplicationBase) -> ApplicationDeployment """
        ...

    @property
    def IsNetworkDeployed(self) -> bool:
        """ Get: IsNetworkDeployed(self: ConsoleApplicationBase) -> bool """
        ...



class NoStartupFormException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    NoStartupFormException()
    NoStartupFormException(message: str)
    NoStartupFormException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class ShutdownEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ShutdownEventHandler(TargetObject: object, TargetMethod: IntPtr) """
    def BeginInvoke(self, sender:object, e:EventArgs, DelegateCallback:AsyncCallback, DelegateAsyncState:object) -> IAsyncResult:
        """ BeginInvoke(self: ShutdownEventHandler, sender: object, e: EventArgs, DelegateCallback: AsyncCallback, DelegateAsyncState: object) -> IAsyncResult """
        ...

    def EndInvoke(self, DelegateAsyncResult:IAsyncResult): # -> 
        """ EndInvoke(self: ShutdownEventHandler, DelegateAsyncResult: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:EventArgs): # -> 
        """ Invoke(self: ShutdownEventHandler, sender: object, e: EventArgs) """
        ...


class ShutdownMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ShutdownMode, values: AfterAllFormsClose (1), AfterMainFormCloses (0) """
    AfterAllFormsClose: ShutdownMode = ...
    AfterMainFormCloses: ShutdownMode = ...
    value__ = ...


class StartupEventArgs(CancelEventArgs): # skipped bases: <type 'object'>
    """ StartupEventArgs(args: ReadOnlyCollection[str]) """
    @property
    def CommandLine(self) -> ReadOnlyCollection:
        """ Get: CommandLine(self: StartupEventArgs) -> ReadOnlyCollection[str] """
        ...



class StartupEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ StartupEventHandler(TargetObject: object, TargetMethod: IntPtr) """
    def BeginInvoke(self, sender:object, e:StartupEventArgs, DelegateCallback:AsyncCallback, DelegateAsyncState:object) -> IAsyncResult:
        """ BeginInvoke(self: StartupEventHandler, sender: object, e: StartupEventArgs, DelegateCallback: AsyncCallback, DelegateAsyncState: object) -> IAsyncResult """
        ...

    def EndInvoke(self, DelegateAsyncResult:IAsyncResult): # -> 
        """ EndInvoke(self: StartupEventHandler, DelegateAsyncResult: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:StartupEventArgs): # -> 
        """ Invoke(self: StartupEventHandler, sender: object, e: StartupEventArgs) """
        ...


class StartupNextInstanceEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ StartupNextInstanceEventArgs(args: ReadOnlyCollection[str], bringToForegroundFlag: bool) """
    @property
    def BringToForeground(self) -> bool:
        """
        Get: BringToForeground(self: StartupNextInstanceEventArgs) -> bool
        Set: BringToForeground(self: StartupNextInstanceEventArgs) = value
        """
        ...

    @property
    def CommandLine(self) -> ReadOnlyCollection:
        """ Get: CommandLine(self: StartupNextInstanceEventArgs) -> ReadOnlyCollection[str] """
        ...


    def __new__(cls, args:ReadOnlyCollection, bringToForegroundFlag:bool) -> Self:
        """ __new__(cls: type, args: ReadOnlyCollection[str], bringToForegroundFlag: bool) """
        ...


class StartupNextInstanceEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ StartupNextInstanceEventHandler(TargetObject: object, TargetMethod: IntPtr) """
    def BeginInvoke(self, sender:object, e:StartupNextInstanceEventArgs, DelegateCallback:AsyncCallback, DelegateAsyncState:object) -> IAsyncResult:
        """ BeginInvoke(self: StartupNextInstanceEventHandler, sender: object, e: StartupNextInstanceEventArgs, DelegateCallback: AsyncCallback, DelegateAsyncState: object) -> IAsyncResult """
        ...

    def EndInvoke(self, DelegateAsyncResult:IAsyncResult): # -> 
        """ EndInvoke(self: StartupNextInstanceEventHandler, DelegateAsyncResult: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:StartupNextInstanceEventArgs): # -> 
        """ Invoke(self: StartupNextInstanceEventHandler, sender: object, e: StartupNextInstanceEventArgs) """
        ...


class UnhandledExceptionEventArgs(ThreadExceptionEventArgs): # skipped bases: <type 'object'>
    """ UnhandledExceptionEventArgs(exitApplication: bool, exception: Exception) """
    @property
    def ExitApplication(self) -> bool:
        """
        Get: ExitApplication(self: UnhandledExceptionEventArgs) -> bool
        Set: ExitApplication(self: UnhandledExceptionEventArgs) = value
        """
        ...



class UnhandledExceptionEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ UnhandledExceptionEventHandler(TargetObject: object, TargetMethod: IntPtr) """
    def BeginInvoke(self, sender:object, e:UnhandledExceptionEventArgs, DelegateCallback:AsyncCallback, DelegateAsyncState:object) -> IAsyncResult:
        """ BeginInvoke(self: UnhandledExceptionEventHandler, sender: object, e: UnhandledExceptionEventArgs, DelegateCallback: AsyncCallback, DelegateAsyncState: object) -> IAsyncResult """
        ...

    def EndInvoke(self, DelegateAsyncResult:IAsyncResult): # -> 
        """ EndInvoke(self: UnhandledExceptionEventHandler, DelegateAsyncResult: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:UnhandledExceptionEventArgs): # -> 
        """ Invoke(self: UnhandledExceptionEventHandler, sender: object, e: UnhandledExceptionEventArgs) """
        ...


class User: # skipped bases: <type 'object'>, <type 'object'>
    """ User() """
    @property
    def CurrentPrincipal(self) -> IPrincipal:
        """
        Get: CurrentPrincipal(self: User) -> IPrincipal
        Set: CurrentPrincipal(self: User) = value
        """
        ...

    @property
    def InternalPrincipal(self):
        ...

    @property
    def IsAuthenticated(self) -> bool:
        """ Get: IsAuthenticated(self: User) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: User) -> str """
        ...


    def InitializeWithWindowsUser(self): # -> 
        """ InitializeWithWindowsUser(self: User) """
        ...

    def IsInRole(self, role:str) -> bool:
        """
        IsInRole(self: User, role: str) -> bool
        IsInRole(self: User, role: BuiltInRole) -> bool
        """
        ...


class WebUser(User): # skipped bases: <type 'object'>
    """ WebUser() """
    pass

class WindowsFormsApplicationBase(ConsoleApplicationBase): # skipped bases: <type 'object'>
    """
    WindowsFormsApplicationBase()
    WindowsFormsApplicationBase(authenticationMode: AuthenticationMode)
    """
    @property
    def ApplicationContext(self) -> ApplicationContext:
        """ Get: ApplicationContext(self: WindowsFormsApplicationBase) -> ApplicationContext """
        ...

    @property
    def EnableVisualStyles(self):
        ...

    @property
    def IsSingleInstance(self):
        ...

    @property
    def MainForm(self):
        ...

    @property
    def MinimumSplashScreenDisplayTime(self) -> int:
        """
        Get: MinimumSplashScreenDisplayTime(self: WindowsFormsApplicationBase) -> int
        Set: MinimumSplashScreenDisplayTime(self: WindowsFormsApplicationBase) = value
        """
        ...

    @property
    def OpenForms(self) -> FormCollection:
        """ Get: OpenForms(self: WindowsFormsApplicationBase) -> FormCollection """
        ...

    @property
    def SaveMySettingsOnExit(self) -> bool:
        """
        Get: SaveMySettingsOnExit(self: WindowsFormsApplicationBase) -> bool
        Set: SaveMySettingsOnExit(self: WindowsFormsApplicationBase) = value
        """
        ...

    @property
    def ShutdownStyle(self):
        ...

    @property
    def SplashScreen(self) -> Form:
        """
        Get: SplashScreen(self: WindowsFormsApplicationBase) -> Form
        Set: SplashScreen(self: WindowsFormsApplicationBase) = value
        """
        ...

    @property
    def UseCompatibleTextRendering(self):
        ...


    def DoEvents(self): # -> 
        """ DoEvents(self: WindowsFormsApplicationBase) """
        ...

    def HideSplashScreen(self, *args): #cannot find CLR method
        """ HideSplashScreen(self: WindowsFormsApplicationBase) """
        ...

    def OnCreateMainForm(self, *args): #cannot find CLR method
        """ OnCreateMainForm(self: WindowsFormsApplicationBase) """
        ...

    def OnCreateSplashScreen(self, *args): #cannot find CLR method
        """ OnCreateSplashScreen(self: WindowsFormsApplicationBase) """
        ...

    def OnInitialize(self, *args): #cannot find CLR method
        """ OnInitialize(self: WindowsFormsApplicationBase, commandLineArgs: ReadOnlyCollection[str]) -> bool """
        ...

    def OnRun(self, *args): #cannot find CLR method
        """ OnRun(self: WindowsFormsApplicationBase) """
        ...

    def OnShutdown(self, *args): #cannot find CLR method
        """ OnShutdown(self: WindowsFormsApplicationBase) """
        ...

    def OnStartup(self, *args): #cannot find CLR method
        """ OnStartup(self: WindowsFormsApplicationBase, eventArgs: StartupEventArgs) -> bool """
        ...

    def OnStartupNextInstance(self, *args): #cannot find CLR method
        """ OnStartupNextInstance(self: WindowsFormsApplicationBase, eventArgs: StartupNextInstanceEventArgs) """
        ...

    def OnUnhandledException(self, *args): #cannot find CLR method
        """ OnUnhandledException(self: WindowsFormsApplicationBase, e: UnhandledExceptionEventArgs) -> bool """
        ...

    def Run(self, commandLine:Array): # -> 
        """ Run(self: WindowsFormsApplicationBase, commandLine: Array[str]) """
        ...

    def ShowSplashScreen(self, *args): #cannot find CLR method
        """ ShowSplashScreen(self: WindowsFormsApplicationBase) """
        ...

    def __new__(cls, authenticationMode:AuthenticationMode = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, authenticationMode: AuthenticationMode)
        """
        ...

    NetworkAvailabilityChanged = ...
    Shutdown = ...
    Startup = ...
    StartupNextInstance = ...
    UnhandledException = ...


