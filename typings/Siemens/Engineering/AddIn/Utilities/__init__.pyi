# encoding: utf-8
# module Siemens.Engineering.AddIn.Utilities calls itself Utilities
# from Siemens.Engineering.AddIn.Utilities, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, DateTime, IntPtr

from System.Collections.Specialized import StringDictionary

from System.Diagnostics import ProcessWindowStyle

from System.IO import StreamReader, StreamWriter

from System.Security import SecureString

from System.Text import Encoding

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class Process: # skipped bases: <type 'object'>, <type 'object'>
    """ Process() """
    @property
    def EnableRaisingEvents(self) -> bool:
        """
        Get: EnableRaisingEvents(self: Process) -> bool
        Set: EnableRaisingEvents(self: Process) = value
        """
        ...

    @property
    def ExitCode(self) -> int:
        """ Get: ExitCode(self: Process) -> int """
        ...

    @property
    def ExitTime(self) -> DateTime:
        """ Get: ExitTime(self: Process) -> DateTime """
        ...

    @property
    def HasExited(self) -> bool:
        """ Get: HasExited(self: Process) -> bool """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: Process) -> int """
        ...

    @property
    def ProcessName(self) -> str:
        """ Get: ProcessName(self: Process) -> str """
        ...

    @property
    def Responding(self) -> bool:
        """ Get: Responding(self: Process) -> bool """
        ...

    @property
    def StandardError(self) -> StreamReader:
        """ Get: StandardError(self: Process) -> StreamReader """
        ...

    @property
    def StandardInput(self) -> StreamWriter:
        """ Get: StandardInput(self: Process) -> StreamWriter """
        ...

    @property
    def StandardOutput(self) -> StreamReader:
        """ Get: StandardOutput(self: Process) -> StreamReader """
        ...

    @property
    def StartInfo(self) -> ProcessStartInfo:
        """
        Get: StartInfo(self: Process) -> ProcessStartInfo
        Set: StartInfo(self: Process) = value
        """
        ...

    @property
    def StartTime(self) -> DateTime:
        """ Get: StartTime(self: Process) -> DateTime """
        ...


    def BeginErrorReadLine(self): # -> 
        """ BeginErrorReadLine(self: Process) """
        ...

    def BeginOutputReadLine(self): # -> 
        """ BeginOutputReadLine(self: Process) """
        ...

    def CancelErrorRead(self): # -> 
        """ CancelErrorRead(self: Process) """
        ...

    def CancelOutputRead(self): # -> 
        """ CancelOutputRead(self: Process) """
        ...

    def Close(self): # -> 
        """ Close(self: Process) """
        ...

    def Kill(self): # -> 
        """ Kill(self: Process) """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: Process) """
        ...

    def Start(self, fileName=None, *__args) -> bool:
        """
        Start(self: Process) -> bool
        Start(fileName: str) -> Process
        Start(fileName: str, arguments: str) -> Process
        Start(fileName: str, userName: str, password: SecureString, domain: str) -> Process
        Start(fileName: str, arguments: str, userName: str, password: SecureString, domain: str) -> Process
        """
        ...

    def WaitForExit(self, milliseconds:int = ...) -> bool:
        """
        WaitForExit(self: Process, milliseconds: int) -> bool
        WaitForExit(self: Process) -> bool
        """
        ...

    ErrorDataReceived = ...
    Exited = ...
    OutputDataReceived = ...


class ProcessStartInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ ProcessStartInfo() """
    @property
    def Arguments(self) -> str:
        """
        Get: Arguments(self: ProcessStartInfo) -> str
        Set: Arguments(self: ProcessStartInfo) = value
        """
        ...

    @property
    def CreateNoWindow(self) -> bool:
        """
        Get: CreateNoWindow(self: ProcessStartInfo) -> bool
        Set: CreateNoWindow(self: ProcessStartInfo) = value
        """
        ...

    @property
    def Domain(self) -> str:
        """
        Get: Domain(self: ProcessStartInfo) -> str
        Set: Domain(self: ProcessStartInfo) = value
        """
        ...

    @property
    def EnvironmentVariables(self) -> StringDictionary:
        """ Get: EnvironmentVariables(self: ProcessStartInfo) -> StringDictionary """
        ...

    @property
    def ErrorDialog(self) -> bool:
        """
        Get: ErrorDialog(self: ProcessStartInfo) -> bool
        Set: ErrorDialog(self: ProcessStartInfo) = value
        """
        ...

    @property
    def ErrorDialogParentHandle(self) -> IntPtr:
        """
        Get: ErrorDialogParentHandle(self: ProcessStartInfo) -> IntPtr
        Set: ErrorDialogParentHandle(self: ProcessStartInfo) = value
        """
        ...

    @property
    def FileName(self) -> str:
        """
        Get: FileName(self: ProcessStartInfo) -> str
        Set: FileName(self: ProcessStartInfo) = value
        """
        ...

    @property
    def LoadUserProfile(self) -> bool:
        """
        Get: LoadUserProfile(self: ProcessStartInfo) -> bool
        Set: LoadUserProfile(self: ProcessStartInfo) = value
        """
        ...

    @property
    def Password(self) -> SecureString:
        """
        Get: Password(self: ProcessStartInfo) -> SecureString
        Set: Password(self: ProcessStartInfo) = value
        """
        ...

    @property
    def PasswordInClearText(self) -> str:
        """
        Get: PasswordInClearText(self: ProcessStartInfo) -> str
        Set: PasswordInClearText(self: ProcessStartInfo) = value
        """
        ...

    @property
    def RedirectStandardError(self) -> bool:
        """
        Get: RedirectStandardError(self: ProcessStartInfo) -> bool
        Set: RedirectStandardError(self: ProcessStartInfo) = value
        """
        ...

    @property
    def RedirectStandardInput(self) -> bool:
        """
        Get: RedirectStandardInput(self: ProcessStartInfo) -> bool
        Set: RedirectStandardInput(self: ProcessStartInfo) = value
        """
        ...

    @property
    def RedirectStandardOutput(self) -> bool:
        """
        Get: RedirectStandardOutput(self: ProcessStartInfo) -> bool
        Set: RedirectStandardOutput(self: ProcessStartInfo) = value
        """
        ...

    @property
    def StandardErrorEncoding(self) -> Encoding:
        """
        Get: StandardErrorEncoding(self: ProcessStartInfo) -> Encoding
        Set: StandardErrorEncoding(self: ProcessStartInfo) = value
        """
        ...

    @property
    def StandardOutputEncoding(self) -> Encoding:
        """
        Get: StandardOutputEncoding(self: ProcessStartInfo) -> Encoding
        Set: StandardOutputEncoding(self: ProcessStartInfo) = value
        """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: ProcessStartInfo) -> str
        Set: UserName(self: ProcessStartInfo) = value
        """
        ...

    @property
    def UseShellExecute(self) -> bool:
        """
        Get: UseShellExecute(self: ProcessStartInfo) -> bool
        Set: UseShellExecute(self: ProcessStartInfo) = value
        """
        ...

    @property
    def Verb(self) -> str:
        """
        Get: Verb(self: ProcessStartInfo) -> str
        Set: Verb(self: ProcessStartInfo) = value
        """
        ...

    @property
    def Verbs(self) -> Array:
        """ Get: Verbs(self: ProcessStartInfo) -> Array[str] """
        ...

    @property
    def WindowStyle(self) -> ProcessWindowStyle:
        """
        Get: WindowStyle(self: ProcessStartInfo) -> ProcessWindowStyle
        Set: WindowStyle(self: ProcessStartInfo) = value
        """
        ...

    @property
    def WorkingDirectory(self) -> str:
        """
        Get: WorkingDirectory(self: ProcessStartInfo) -> str
        Set: WorkingDirectory(self: ProcessStartInfo) = value
        """
        ...



