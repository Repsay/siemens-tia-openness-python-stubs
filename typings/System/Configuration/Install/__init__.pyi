# encoding: utf-8
# module System.Configuration.Install calls itself Install
# from System.Configuration.Install, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Enum, EventArgs, IAsyncResult, 
    MulticastDelegate, SystemException)

from System.Collections import CollectionBase, IDictionary

from System.Collections.Specialized import StringDictionary

from System.ComponentModel import Component, IComponent

from System.Reflection import Assembly

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class Installer(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ Installer() """
    @property
    def Context(self) -> InstallContext:
        """
        Get: Context(self: Installer) -> InstallContext
        Set: Context(self: Installer) = value
        """
        ...

    @property
    def HelpText(self) -> str:
        """ Get: HelpText(self: Installer) -> str """
        ...

    @property
    def Installers(self) -> InstallerCollection:
        """ Get: Installers(self: Installer) -> InstallerCollection """
        ...

    @property
    def Parent(self) -> Installer:
        """
        Get: Parent(self: Installer) -> Installer
        Set: Parent(self: Installer) = value
        """
        ...


    def Commit(self, savedState:IDictionary): # -> 
        """ Commit(self: Installer, savedState: IDictionary) """
        ...

    def Install(self, stateSaver:IDictionary): # -> 
        """ Install(self: Installer, stateSaver: IDictionary) """
        ...

    def OnAfterInstall(self, *args): #cannot find CLR method
        """ OnAfterInstall(self: Installer, savedState: IDictionary) """
        ...

    def OnAfterRollback(self, *args): #cannot find CLR method
        """ OnAfterRollback(self: Installer, savedState: IDictionary) """
        ...

    def OnAfterUninstall(self, *args): #cannot find CLR method
        """ OnAfterUninstall(self: Installer, savedState: IDictionary) """
        ...

    def OnBeforeInstall(self, *args): #cannot find CLR method
        """ OnBeforeInstall(self: Installer, savedState: IDictionary) """
        ...

    def OnBeforeRollback(self, *args): #cannot find CLR method
        """ OnBeforeRollback(self: Installer, savedState: IDictionary) """
        ...

    def OnBeforeUninstall(self, *args): #cannot find CLR method
        """ OnBeforeUninstall(self: Installer, savedState: IDictionary) """
        ...

    def OnCommitted(self, *args): #cannot find CLR method
        """ OnCommitted(self: Installer, savedState: IDictionary) """
        ...

    def OnCommitting(self, *args): #cannot find CLR method
        """ OnCommitting(self: Installer, savedState: IDictionary) """
        ...

    def Rollback(self, savedState:IDictionary): # -> 
        """ Rollback(self: Installer, savedState: IDictionary) """
        ...

    def Uninstall(self, savedState:IDictionary): # -> 
        """ Uninstall(self: Installer, savedState: IDictionary) """
        ...

    AfterInstall = ...
    AfterRollback = ...
    AfterUninstall = ...
    BeforeInstall = ...
    BeforeRollback = ...
    BeforeUninstall = ...
    Committed = ...
    Committing = ...


class AssemblyInstaller(Installer): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    AssemblyInstaller()
    AssemblyInstaller(fileName: str, commandLine: Array[str])
    AssemblyInstaller(assembly: Assembly, commandLine: Array[str])
    """
    @property
    def Assembly(self) -> Assembly:
        """
        Get: Assembly(self: AssemblyInstaller) -> Assembly
        Set: Assembly(self: AssemblyInstaller) = value
        """
        ...

    @property
    def CommandLine(self) -> Array:
        """
        Get: CommandLine(self: AssemblyInstaller) -> Array[str]
        Set: CommandLine(self: AssemblyInstaller) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: AssemblyInstaller) -> str
        Set: Path(self: AssemblyInstaller) = value
        """
        ...

    @property
    def UseNewContext(self) -> bool:
        """
        Get: UseNewContext(self: AssemblyInstaller) -> bool
        Set: UseNewContext(self: AssemblyInstaller) = value
        """
        ...


    @staticmethod
    def CheckIfInstallable(assemblyName:str): # -> 
        """ CheckIfInstallable(assemblyName: str) """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, fileName: str, commandLine: Array[str])
        __new__(cls: type, assembly: Assembly, commandLine: Array[str])
        """
        ...


class ComponentInstaller(Installer): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    def CopyFromComponent(self, component:IComponent): # -> 
        """ CopyFromComponent(self: ComponentInstaller, component: IComponent) """
        ...

    def IsEquivalentInstaller(self, otherInstaller:ComponentInstaller) -> bool:
        """ IsEquivalentInstaller(self: ComponentInstaller, otherInstaller: ComponentInstaller) -> bool """
        ...


class IManagedInstaller: # skipped bases: <type 'object'>
    """ no doc """
    def ManagedInstall(self, commandLine:str, hInstall:int) -> int:
        """ ManagedInstall(self: IManagedInstaller, commandLine: str, hInstall: int) -> int """
        ...


class InstallContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    InstallContext()
    InstallContext(logFilePath: str, commandLine: Array[str])
    """
    @property
    def Parameters(self) -> StringDictionary:
        """ Get: Parameters(self: InstallContext) -> StringDictionary """
        ...


    def IsParameterTrue(self, paramName:str) -> bool:
        """ IsParameterTrue(self: InstallContext, paramName: str) -> bool """
        ...

    def LogMessage(self, message:str): # -> 
        """ LogMessage(self: InstallContext, message: str) """
        ...

    def ParseCommandLine(self, *args): #cannot find CLR method
        """ ParseCommandLine(args: Array[str]) -> StringDictionary """
        ...


class InstallerCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ no doc """
    def Add(self, value:Installer) -> int:
        """ Add(self: InstallerCollection, value: Installer) -> int """
        ...

    def AddRange(self, value:InstallerCollection): # -> 
        """ AddRange(self: InstallerCollection, value: InstallerCollection)AddRange(self: InstallerCollection, value: Array[Installer]) """
        ...

    def Contains(self, value:Installer) -> bool:
        """ Contains(self: InstallerCollection, value: Installer) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: InstallerCollection, array: Array[Installer], index: int) """
        ...

    def IndexOf(self, value:Installer) -> int:
        """ IndexOf(self: InstallerCollection, value: Installer) -> int """
        ...

    def Insert(self, index:int, value:Installer): # -> 
        """ Insert(self: InstallerCollection, index: int, value: Installer) """
        ...

    def Remove(self, value:Installer): # -> 
        """ Remove(self: InstallerCollection, value: Installer) """
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


class InstallEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    InstallEventArgs()
    InstallEventArgs(savedState: IDictionary)
    """
    @property
    def SavedState(self) -> IDictionary:
        """ Get: SavedState(self: InstallEventArgs) -> IDictionary """
        ...


    def __new__(cls, savedState:IDictionary = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, savedState: IDictionary)
        """
        ...


class InstallEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InstallEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InstallEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InstallEventHandler, sender: object, e: InstallEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InstallEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InstallEventArgs): # -> 
        """ Invoke(self: InstallEventHandler, sender: object, e: InstallEventArgs) """
        ...


class InstallException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstallException()
    InstallException(message: str)
    InstallException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class ManagedInstallerClass(IManagedInstaller): # skipped bases: <type 'object'>
    """ ManagedInstallerClass() """
    @staticmethod
    def InstallHelper(args:Array): # -> 
        """ InstallHelper(args: Array[str]) """
        ...


class TransactedInstaller(Installer): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ TransactedInstaller() """
    pass

class UninstallAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum UninstallAction, values: NoAction (1), Remove (0) """
    NoAction: UninstallAction = ...
    Remove: UninstallAction = ...
    value__ = ...


