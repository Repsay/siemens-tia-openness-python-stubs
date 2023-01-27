# encoding: utf-8
# module Microsoft.Scripting.Hosting.Shell.Remote calls itself Remote
# from Microsoft.Dynamic, Version=1.3.1.0, Culture=neutral, PublicKeyToken=7f709c5b713576e1
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Scripting.Hosting.Shell import (CommandLine, ConsoleHost, 
    ICommandDispatcher)

from System import IDisposable, MarshalByRefObject

from System.Collections import IList

from System.Diagnostics import Process, ProcessStartInfo

from System.Threading import AutoResetEvent, Thread

from typing import Self

"""The following names are not found in the module: BoundEvent, ScriptScope
"""

# no functions
# classes

class ConsoleRestartManager: # skipped bases: <type 'object'>, <type 'object'>
    """ ConsoleRestartManager(exitOnNormalExit: bool) """
    @property
    def AccessLock(self):
        ...

    @property
    def ConsoleThread(self) -> Thread:
        """ Get: ConsoleThread(self: ConsoleRestartManager) -> Thread """
        ...

    @property
    def CurrentConsoleHost(self):
        ...


    def BreakExecution(self): # -> 
        """ BreakExecution(self: ConsoleRestartManager) """
        ...

    def CreateRemoteConsoleHost(self) -> RemoteConsoleHost:
        """ CreateRemoteConsoleHost(self: ConsoleRestartManager) -> RemoteConsoleHost """
        ...

    def GetMemberNames(self, expression:str) -> IList:
        """ GetMemberNames(self: ConsoleRestartManager, expression: str) -> IList[str] """
        ...

    def RestartConsole(self): # -> 
        """ RestartConsole(self: ConsoleRestartManager) """
        ...

    def Start(self): # -> 
        """ Start(self: ConsoleRestartManager) """
        ...

    def Terminate(self): # -> 
        """ Terminate(self: ConsoleRestartManager) """
        ...

    def __dir__(self, *args): #cannot find CLR method
        """ GetMemberNames(self: ConsoleRestartManager, expression: str) -> IList[str] """
        ...


class RemoteCommandDispatcher(MarshalByRefObject, ICommandDispatcher): # skipped bases: <type 'object'>
    """ RemoteCommandDispatcher(scope: ScriptScope) """
    @property
    def ScriptScope(self): # -> ScriptScope
        """ Get: ScriptScope(self: RemoteCommandDispatcher) -> ScriptScope """
        ...


    def AbortCommand(self) -> bool:
        """ AbortCommand(self: RemoteCommandDispatcher) -> bool """
        ...

    def __new__(cls, scope) -> Self: # Not found arg types: {'scope': 'ScriptScope'}
        """ __new__(cls: type, scope: ScriptScope) """
        ...


class RemoteConsoleCommandLine(CommandLine): # skipped bases: <type 'object'>
    """ RemoteConsoleCommandLine(scope: ScriptScope, remoteCommandDispatcher: RemoteCommandDispatcher, remoteOutputReceived: AutoResetEvent) """
    def __new__(cls, scope, remoteCommandDispatcher:RemoteCommandDispatcher, remoteOutputReceived:AutoResetEvent) -> Self: # Not found arg types: {'scope': 'ScriptScope'}
        """ __new__(cls: type, scope: ScriptScope, remoteCommandDispatcher: RemoteCommandDispatcher, remoteOutputReceived: AutoResetEvent) """
        ...


class RemoteConsoleHost(IDisposable, ConsoleHost): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RemoteRuntimeProcess(self) -> Process:
        """ Get: RemoteRuntimeProcess(self: RemoteConsoleHost) -> Process """
        ...

    @property
    def ScriptScope(self): # -> ScriptScope
        """ Get: ScriptScope(self: RemoteConsoleHost) -> ScriptScope """
        ...


    def AbortCommand(self) -> bool:
        """ AbortCommand(self: RemoteConsoleHost) -> bool """
        ...

    def CustomizeRemoteRuntimeStartInfo(self, processInfo:ProcessStartInfo): # -> 
        """ CustomizeRemoteRuntimeStartInfo(self: RemoteConsoleHost, processInfo: ProcessStartInfo) """
        ...

    def OnOutputDataReceived(self, *args): #cannot find CLR method
        """ OnOutputDataReceived(self: RemoteConsoleHost, sender: object, eventArgs: DataReceivedEventArgs) """
        ...

    def OnRemoteRuntimeExited(self, *args): #cannot find CLR method
        """ OnRemoteRuntimeExited(self: RemoteConsoleHost, sender: object, args: EventArgs) """
        ...


class RemoteRuntimeServer: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    __all__: list = ...


class RemoteRuntimeStartupException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    RemoteRuntimeStartupException()
    RemoteRuntimeStartupException(message: str)
    RemoteRuntimeStartupException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


