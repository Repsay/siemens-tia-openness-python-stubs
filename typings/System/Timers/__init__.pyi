# encoding: utf-8
# module System.Timers calls itself Timers
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (AsyncCallback, DateTime, EventArgs, IAsyncResult, 
    MulticastDelegate)

from System.ComponentModel import (Component, ISupportInitialize, 
    ISynchronizeInvoke)

from System.EnterpriseServices import DescriptionAttribute

from typing import Self

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class ElapsedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SignalTime(self) -> DateTime:
        """ Get: SignalTime(self: ElapsedEventArgs) -> DateTime """
        ...



class ElapsedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ ElapsedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:ElapsedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: ElapsedEventHandler, sender: object, e: ElapsedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: ElapsedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:ElapsedEventArgs): # -> 
        """ Invoke(self: ElapsedEventHandler, sender: object, e: ElapsedEventArgs) """
        ...


class Timer(ISupportInitialize, Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    Timer()
    Timer(interval: float)
    """
    @property
    def AutoReset(self) -> bool:
        """
        Get: AutoReset(self: Timer) -> bool
        Set: AutoReset(self: Timer) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: Timer) -> bool
        Set: Enabled(self: Timer) = value
        """
        ...

    @property
    def Interval(self) -> float:
        """
        Get: Interval(self: Timer) -> float
        Set: Interval(self: Timer) = value
        """
        ...

    @property
    def SynchronizingObject(self) -> ISynchronizeInvoke:
        """
        Get: SynchronizingObject(self: Timer) -> ISynchronizeInvoke
        Set: SynchronizingObject(self: Timer) = value
        """
        ...


    def Close(self): # -> 
        """ Close(self: Timer) """
        ...

    def Start(self): # -> 
        """ Start(self: Timer) """
        ...

    def Stop(self): # -> 
        """ Stop(self: Timer) """
        ...

    def __new__(cls, interval:float = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, interval: float)
        """
        ...

    Elapsed = ...


class TimersDescriptionAttribute(DescriptionAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TimersDescriptionAttribute(description: str) """
    pass

