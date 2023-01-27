# encoding: utf-8
# module Microsoft.VisualBasic.Devices calls itself Devices
# from Microsoft.VisualBasic, Version=10.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic.MyServices import (ClipboardProxy, FileSystemProxy, 
    RegistryProxy)

from System import (AsyncCallback, DateTime, EventArgs, IAsyncResult, 
    MulticastDelegate, UInt64)

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Globalization import CultureInfo

from System.IO.Ports import Parity, SerialPort, StopBits

from System.Media import SystemSound

from System.Windows.Forms import Screen

from typing import Self

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class Audio: # skipped bases: <type 'object'>, <type 'object'>
    """ Audio() """
    def Play(self, *__args:str): # -> 
        """ Play(self: Audio, location: str)Play(self: Audio, location: str, playMode: AudioPlayMode)Play(self: Audio, data: Array[Byte], playMode: AudioPlayMode)Play(self: Audio, stream: Stream, playMode: AudioPlayMode) """
        ...

    def PlaySystemSound(self, systemSound:SystemSound): # -> 
        """ PlaySystemSound(self: Audio, systemSound: SystemSound) """
        ...

    def Stop(self): # -> 
        """ Stop(self: Audio) """
        ...


class Clock: # skipped bases: <type 'object'>, <type 'object'>
    """ Clock() """
    @property
    def GmtTime(self) -> DateTime:
        """ Get: GmtTime(self: Clock) -> DateTime """
        ...

    @property
    def LocalTime(self) -> DateTime:
        """ Get: LocalTime(self: Clock) -> DateTime """
        ...

    @property
    def TickCount(self) -> int:
        """ Get: TickCount(self: Clock) -> int """
        ...



class ServerComputer: # skipped bases: <type 'object'>, <type 'object'>
    """ ServerComputer() """
    @property
    def Clock(self) -> Clock:
        """ Get: Clock(self: ServerComputer) -> Clock """
        ...

    @property
    def FileSystem(self) -> FileSystemProxy:
        """ Get: FileSystem(self: ServerComputer) -> FileSystemProxy """
        ...

    @property
    def Info(self) -> ComputerInfo:
        """ Get: Info(self: ServerComputer) -> ComputerInfo """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ServerComputer) -> str """
        ...

    @property
    def Network(self) -> Network:
        """ Get: Network(self: ServerComputer) -> Network """
        ...

    @property
    def Registry(self) -> RegistryProxy:
        """ Get: Registry(self: ServerComputer) -> RegistryProxy """
        ...



class Computer(ServerComputer): # skipped bases: <type 'object'>
    """ Computer() """
    @property
    def Audio(self) -> Audio:
        """ Get: Audio(self: Computer) -> Audio """
        ...

    @property
    def Clipboard(self) -> ClipboardProxy:
        """ Get: Clipboard(self: Computer) -> ClipboardProxy """
        ...

    @property
    def Keyboard(self) -> Keyboard:
        """ Get: Keyboard(self: Computer) -> Keyboard """
        ...

    @property
    def Mouse(self) -> Mouse:
        """ Get: Mouse(self: Computer) -> Mouse """
        ...

    @property
    def Ports(self) -> Ports:
        """ Get: Ports(self: Computer) -> Ports """
        ...

    @property
    def Screen(self) -> Screen:
        """ Get: Screen(self: Computer) -> Screen """
        ...



class ComputerInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ ComputerInfo() """
    @property
    def AvailablePhysicalMemory(self) -> UInt64:
        """ Get: AvailablePhysicalMemory(self: ComputerInfo) -> UInt64 """
        ...

    @property
    def AvailableVirtualMemory(self) -> UInt64:
        """ Get: AvailableVirtualMemory(self: ComputerInfo) -> UInt64 """
        ...

    @property
    def InstalledUICulture(self) -> CultureInfo:
        """ Get: InstalledUICulture(self: ComputerInfo) -> CultureInfo """
        ...

    @property
    def OSFullName(self) -> str:
        """ Get: OSFullName(self: ComputerInfo) -> str """
        ...

    @property
    def OSPlatform(self) -> str:
        """ Get: OSPlatform(self: ComputerInfo) -> str """
        ...

    @property
    def OSVersion(self) -> str:
        """ Get: OSVersion(self: ComputerInfo) -> str """
        ...

    @property
    def TotalPhysicalMemory(self) -> UInt64:
        """ Get: TotalPhysicalMemory(self: ComputerInfo) -> UInt64 """
        ...

    @property
    def TotalVirtualMemory(self) -> UInt64:
        """ Get: TotalVirtualMemory(self: ComputerInfo) -> UInt64 """
        ...



class Keyboard: # skipped bases: <type 'object'>, <type 'object'>
    """ Keyboard() """
    @property
    def AltKeyDown(self) -> bool:
        """ Get: AltKeyDown(self: Keyboard) -> bool """
        ...

    @property
    def CapsLock(self) -> bool:
        """ Get: CapsLock(self: Keyboard) -> bool """
        ...

    @property
    def CtrlKeyDown(self) -> bool:
        """ Get: CtrlKeyDown(self: Keyboard) -> bool """
        ...

    @property
    def NumLock(self) -> bool:
        """ Get: NumLock(self: Keyboard) -> bool """
        ...

    @property
    def ScrollLock(self) -> bool:
        """ Get: ScrollLock(self: Keyboard) -> bool """
        ...

    @property
    def ShiftKeyDown(self) -> bool:
        """ Get: ShiftKeyDown(self: Keyboard) -> bool """
        ...


    def SendKeys(self, keys:str, wait:bool = ...): # -> 
        """ SendKeys(self: Keyboard, keys: str)SendKeys(self: Keyboard, keys: str, wait: bool) """
        ...


class Mouse: # skipped bases: <type 'object'>, <type 'object'>
    """ Mouse() """
    @property
    def ButtonsSwapped(self) -> bool:
        """ Get: ButtonsSwapped(self: Mouse) -> bool """
        ...

    @property
    def WheelExists(self) -> bool:
        """ Get: WheelExists(self: Mouse) -> bool """
        ...

    @property
    def WheelScrollLines(self) -> int:
        """ Get: WheelScrollLines(self: Mouse) -> int """
        ...



class Network: # skipped bases: <type 'object'>, <type 'object'>
    """ Network() """
    @property
    def IsAvailable(self) -> bool:
        """ Get: IsAvailable(self: Network) -> bool """
        ...


    def DownloadFile(self, address, destinationFileName, *__args): # -> 
        """ DownloadFile(self: Network, address: str, destinationFileName: str)DownloadFile(self: Network, address: Uri, destinationFileName: str)DownloadFile(self: Network, address: str, destinationFileName: str, userName: str, password: str)DownloadFile(self: Network, address: Uri, destinationFileName: str, userName: str, password: str)DownloadFile(self: Network, address: str, destinationFileName: str, userName: str, password: str, showUI: bool, connectionTimeout: int, overwrite: bool)DownloadFile(self: Network, address: str, destinationFileName: str, userName: str, password: str, showUI: bool, connectionTimeout: int, overwrite: bool, onUserCancel: UICancelOption)DownloadFile(self: Network, address: Uri, destinationFileName: str, userName: str, password: str, showUI: bool, connectionTimeout: int, overwrite: bool)DownloadFile(self: Network, address: Uri, destinationFileName: str, userName: str, password: str, showUI: bool, connectionTimeout: int, overwrite: bool, onUserCancel: UICancelOption)DownloadFile(self: Network, address: Uri, destinationFileName: str, networkCredentials: ICredentials, showUI: bool, connectionTimeout: int, overwrite: bool)DownloadFile(self: Network, address: Uri, destinationFileName: str, networkCredentials: ICredentials, showUI: bool, connectionTimeout: int, overwrite: bool, onUserCancel: UICancelOption) """
        ...

    def Ping(self, *__args:str) -> bool:
        """
        Ping(self: Network, hostNameOrAddress: str) -> bool
        Ping(self: Network, address: Uri) -> bool
        Ping(self: Network, address: Uri, timeout: int) -> bool
        Ping(self: Network, hostNameOrAddress: str, timeout: int) -> bool
        """
        ...

    def UploadFile(self, sourceFileName, address, *__args): # -> 
        """ UploadFile(self: Network, sourceFileName: str, address: str)UploadFile(self: Network, sourceFileName: str, address: Uri)UploadFile(self: Network, sourceFileName: str, address: str, userName: str, password: str)UploadFile(self: Network, sourceFileName: str, address: Uri, userName: str, password: str)UploadFile(self: Network, sourceFileName: str, address: str, userName: str, password: str, showUI: bool, connectionTimeout: int)UploadFile(self: Network, sourceFileName: str, address: Uri, userName: str, password: str, showUI: bool, connectionTimeout: int)UploadFile(self: Network, sourceFileName: str, address: Uri, userName: str, password: str, showUI: bool, connectionTimeout: int, onUserCancel: UICancelOption)UploadFile(self: Network, sourceFileName: str, address: Uri, networkCredentials: ICredentials, showUI: bool, connectionTimeout: int)UploadFile(self: Network, sourceFileName: str, address: str, userName: str, password: str, showUI: bool, connectionTimeout: int, onUserCancel: UICancelOption)UploadFile(self: Network, sourceFileName: str, address: Uri, networkCredentials: ICredentials, showUI: bool, connectionTimeout: int, onUserCancel: UICancelOption) """
        ...

    NetworkAvailabilityChanged = ...


class NetworkAvailableEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ NetworkAvailableEventArgs(networkAvailable: bool) """
    @property
    def IsNetworkAvailable(self) -> bool:
        """ Get: IsNetworkAvailable(self: NetworkAvailableEventArgs) -> bool """
        ...


    def __new__(cls, networkAvailable:bool) -> Self:
        """ __new__(cls: type, networkAvailable: bool) """
        ...


class NetworkAvailableEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ NetworkAvailableEventHandler(TargetObject: object, TargetMethod: IntPtr) """
    def BeginInvoke(self, sender:object, e:NetworkAvailableEventArgs, DelegateCallback:AsyncCallback, DelegateAsyncState:object) -> IAsyncResult:
        """ BeginInvoke(self: NetworkAvailableEventHandler, sender: object, e: NetworkAvailableEventArgs, DelegateCallback: AsyncCallback, DelegateAsyncState: object) -> IAsyncResult """
        ...

    def EndInvoke(self, DelegateAsyncResult:IAsyncResult): # -> 
        """ EndInvoke(self: NetworkAvailableEventHandler, DelegateAsyncResult: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:NetworkAvailableEventArgs): # -> 
        """ Invoke(self: NetworkAvailableEventHandler, sender: object, e: NetworkAvailableEventArgs) """
        ...


class Ports: # skipped bases: <type 'object'>, <type 'object'>
    """ Ports() """
    @property
    def SerialPortNames(self) -> ReadOnlyCollection:
        """ Get: SerialPortNames(self: Ports) -> ReadOnlyCollection[str] """
        ...


    def OpenSerialPort(self, portName:str, baudRate:int = ..., parity:Parity = ..., dataBits:int = ..., stopBits:StopBits = ...) -> SerialPort:
        """
        OpenSerialPort(self: Ports, portName: str) -> SerialPort
        OpenSerialPort(self: Ports, portName: str, baudRate: int) -> SerialPort
        OpenSerialPort(self: Ports, portName: str, baudRate: int, parity: Parity) -> SerialPort
        OpenSerialPort(self: Ports, portName: str, baudRate: int, parity: Parity, dataBits: int) -> SerialPort
        OpenSerialPort(self: Ports, portName: str, baudRate: int, parity: Parity, dataBits: int, stopBits: StopBits) -> SerialPort
        """
        ...


