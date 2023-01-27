# encoding: utf-8
# module System.IO.Ports calls itself Ports
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Byte, Enum, EventArgs, IAsyncResult, 
    MulticastDelegate)

from System.ComponentModel import Component, IContainer

from System.IO import Stream

from System.Text import Encoding

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class Handshake(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Handshake, values: None (0), RequestToSend (2), RequestToSendXOnXOff (3), XOnXOff (1) """
    RequestToSend: Handshake = ...
    RequestToSendXOnXOff: Handshake = ...
    value__ = ...
    XOnXOff: Handshake = ...


class Parity(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Parity, values: Even (2), Mark (3), None (0), Odd (1), Space (4) """
    Even: Parity = ...
    Mark: Parity = ...
    Odd: Parity = ...
    Space: Parity = ...
    value__ = ...


class SerialData(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SerialData, values: Chars (1), Eof (2) """
    Chars: SerialData = ...
    Eof: SerialData = ...
    value__ = ...


class SerialDataReceivedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EventType(self) -> SerialData:
        """ Get: EventType(self: SerialDataReceivedEventArgs) -> SerialData """
        ...



class SerialDataReceivedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SerialDataReceivedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SerialDataReceivedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SerialDataReceivedEventHandler, sender: object, e: SerialDataReceivedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SerialDataReceivedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SerialDataReceivedEventArgs): # -> 
        """ Invoke(self: SerialDataReceivedEventHandler, sender: object, e: SerialDataReceivedEventArgs) """
        ...


class SerialError(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SerialError, values: Frame (8), Overrun (2), RXOver (1), RXParity (4), TXFull (256) """
    Frame: SerialError = ...
    Overrun: SerialError = ...
    RXOver: SerialError = ...
    RXParity: SerialError = ...
    TXFull: SerialError = ...
    value__ = ...


class SerialErrorReceivedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EventType(self) -> SerialError:
        """ Get: EventType(self: SerialErrorReceivedEventArgs) -> SerialError """
        ...



class SerialErrorReceivedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SerialErrorReceivedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SerialErrorReceivedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SerialErrorReceivedEventHandler, sender: object, e: SerialErrorReceivedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SerialErrorReceivedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SerialErrorReceivedEventArgs): # -> 
        """ Invoke(self: SerialErrorReceivedEventHandler, sender: object, e: SerialErrorReceivedEventArgs) """
        ...


class SerialPinChange(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SerialPinChange, values: Break (64), CDChanged (32), CtsChanged (8), DsrChanged (16), Ring (256) """
    Break: SerialPinChange = ...
    CDChanged: SerialPinChange = ...
    CtsChanged: SerialPinChange = ...
    DsrChanged: SerialPinChange = ...
    Ring: SerialPinChange = ...
    value__ = ...


class SerialPinChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def EventType(self) -> SerialPinChange:
        """ Get: EventType(self: SerialPinChangedEventArgs) -> SerialPinChange """
        ...



class SerialPinChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SerialPinChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SerialPinChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SerialPinChangedEventHandler, sender: object, e: SerialPinChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: SerialPinChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:SerialPinChangedEventArgs): # -> 
        """ Invoke(self: SerialPinChangedEventHandler, sender: object, e: SerialPinChangedEventArgs) """
        ...


class SerialPort(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    SerialPort(container: IContainer)
    SerialPort()
    SerialPort(portName: str)
    SerialPort(portName: str, baudRate: int)
    SerialPort(portName: str, baudRate: int, parity: Parity)
    SerialPort(portName: str, baudRate: int, parity: Parity, dataBits: int)
    SerialPort(portName: str, baudRate: int, parity: Parity, dataBits: int, stopBits: StopBits)
    """
    @property
    def BaseStream(self) -> Stream:
        """ Get: BaseStream(self: SerialPort) -> Stream """
        ...

    @property
    def BaudRate(self) -> int:
        """
        Get: BaudRate(self: SerialPort) -> int
        Set: BaudRate(self: SerialPort) = value
        """
        ...

    @property
    def BreakState(self) -> bool:
        """
        Get: BreakState(self: SerialPort) -> bool
        Set: BreakState(self: SerialPort) = value
        """
        ...

    @property
    def BytesToRead(self) -> int:
        """ Get: BytesToRead(self: SerialPort) -> int """
        ...

    @property
    def BytesToWrite(self) -> int:
        """ Get: BytesToWrite(self: SerialPort) -> int """
        ...

    @property
    def CDHolding(self) -> bool:
        """ Get: CDHolding(self: SerialPort) -> bool """
        ...

    @property
    def CtsHolding(self) -> bool:
        """ Get: CtsHolding(self: SerialPort) -> bool """
        ...

    @property
    def DataBits(self) -> int:
        """
        Get: DataBits(self: SerialPort) -> int
        Set: DataBits(self: SerialPort) = value
        """
        ...

    @property
    def DiscardNull(self) -> bool:
        """
        Get: DiscardNull(self: SerialPort) -> bool
        Set: DiscardNull(self: SerialPort) = value
        """
        ...

    @property
    def DsrHolding(self) -> bool:
        """ Get: DsrHolding(self: SerialPort) -> bool """
        ...

    @property
    def DtrEnable(self) -> bool:
        """
        Get: DtrEnable(self: SerialPort) -> bool
        Set: DtrEnable(self: SerialPort) = value
        """
        ...

    @property
    def Encoding(self) -> Encoding:
        """
        Get: Encoding(self: SerialPort) -> Encoding
        Set: Encoding(self: SerialPort) = value
        """
        ...

    @property
    def Handshake(self) -> Handshake:
        """
        Get: Handshake(self: SerialPort) -> Handshake
        Set: Handshake(self: SerialPort) = value
        """
        ...

    @property
    def IsOpen(self) -> bool:
        """ Get: IsOpen(self: SerialPort) -> bool """
        ...

    @property
    def NewLine(self) -> str:
        """
        Get: NewLine(self: SerialPort) -> str
        Set: NewLine(self: SerialPort) = value
        """
        ...

    @property
    def Parity(self) -> Parity:
        """
        Get: Parity(self: SerialPort) -> Parity
        Set: Parity(self: SerialPort) = value
        """
        ...

    @property
    def ParityReplace(self) -> Byte:
        """
        Get: ParityReplace(self: SerialPort) -> Byte
        Set: ParityReplace(self: SerialPort) = value
        """
        ...

    @property
    def PortName(self) -> str:
        """
        Get: PortName(self: SerialPort) -> str
        Set: PortName(self: SerialPort) = value
        """
        ...

    @property
    def ReadBufferSize(self) -> int:
        """
        Get: ReadBufferSize(self: SerialPort) -> int
        Set: ReadBufferSize(self: SerialPort) = value
        """
        ...

    @property
    def ReadTimeout(self) -> int:
        """
        Get: ReadTimeout(self: SerialPort) -> int
        Set: ReadTimeout(self: SerialPort) = value
        """
        ...

    @property
    def ReceivedBytesThreshold(self) -> int:
        """
        Get: ReceivedBytesThreshold(self: SerialPort) -> int
        Set: ReceivedBytesThreshold(self: SerialPort) = value
        """
        ...

    @property
    def RtsEnable(self) -> bool:
        """
        Get: RtsEnable(self: SerialPort) -> bool
        Set: RtsEnable(self: SerialPort) = value
        """
        ...

    @property
    def StopBits(self) -> StopBits:
        """
        Get: StopBits(self: SerialPort) -> StopBits
        Set: StopBits(self: SerialPort) = value
        """
        ...

    @property
    def WriteBufferSize(self) -> int:
        """
        Get: WriteBufferSize(self: SerialPort) -> int
        Set: WriteBufferSize(self: SerialPort) = value
        """
        ...

    @property
    def WriteTimeout(self) -> int:
        """
        Get: WriteTimeout(self: SerialPort) -> int
        Set: WriteTimeout(self: SerialPort) = value
        """
        ...


    def Close(self): # -> 
        """ Close(self: SerialPort) """
        ...

    def DiscardInBuffer(self): # -> 
        """ DiscardInBuffer(self: SerialPort) """
        ...

    def DiscardOutBuffer(self): # -> 
        """ DiscardOutBuffer(self: SerialPort) """
        ...

    @staticmethod
    def GetPortNames() -> Array:
        """ GetPortNames() -> Array[str] """
        ...

    def Open(self): # -> 
        """ Open(self: SerialPort) """
        ...

    def Read(self, buffer:Array, offset:int, count:int) -> int:
        """
        Read(self: SerialPort, buffer: Array[Byte], offset: int, count: int) -> int
        Read(self: SerialPort, buffer: Array[Char], offset: int, count: int) -> int
        """
        ...

    def ReadByte(self) -> int:
        """ ReadByte(self: SerialPort) -> int """
        ...

    def ReadChar(self) -> int:
        """ ReadChar(self: SerialPort) -> int """
        ...

    def ReadExisting(self) -> str:
        """ ReadExisting(self: SerialPort) -> str """
        ...

    def ReadLine(self) -> str:
        """ ReadLine(self: SerialPort) -> str """
        ...

    def ReadTo(self, value:str) -> str:
        """ ReadTo(self: SerialPort, value: str) -> str """
        ...

    def Write(self, *__args:str): # -> 
        """ Write(self: SerialPort, text: str)Write(self: SerialPort, buffer: Array[Char], offset: int, count: int)Write(self: SerialPort, buffer: Array[Byte], offset: int, count: int) """
        ...

    def WriteLine(self, text:str): # -> 
        """ WriteLine(self: SerialPort, text: str) """
        ...

    def __new__(cls, *__args:IContainer) -> Self:
        """
        __new__(cls: type, container: IContainer)
        __new__(cls: type)
        __new__(cls: type, portName: str)
        __new__(cls: type, portName: str, baudRate: int)
        __new__(cls: type, portName: str, baudRate: int, parity: Parity)
        __new__(cls: type, portName: str, baudRate: int, parity: Parity, dataBits: int)
        __new__(cls: type, portName: str, baudRate: int, parity: Parity, dataBits: int, stopBits: StopBits)
        """
        ...

    DataReceived = ...
    ErrorReceived = ...
    InfiniteTimeout: int = ...
    PinChanged = ...


class StopBits(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StopBits, values: None (0), One (1), OnePointFive (3), Two (2) """
    One: StopBits = ...
    OnePointFive: StopBits = ...
    Two: StopBits = ...
    value__ = ...


