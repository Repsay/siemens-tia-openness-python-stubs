# encoding: utf-8
# module System.Diagnostics.Eventing calls itself Eventing
# from System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Byte, Guid, IDisposable, Int64

from System.Diagnostics import TraceListener

from typing import Tuple as Tuple_

"""The following names are not found in the module: WriteEventErrorCode
"""

# no functions
# classes

class EventDescriptor: # skipped bases: <type 'object'>, <type 'object'>
    """ EventDescriptor(id: int, version: Byte, channel: Byte, level: Byte, opcode: Byte, task: int, keywords: Int64) """
    @property
    def Channel(self) -> Byte:
        """ Get: Channel(self: EventDescriptor) -> Byte """
        ...

    @property
    def EventId(self) -> int:
        """ Get: EventId(self: EventDescriptor) -> int """
        ...

    @property
    def Keywords(self) -> Int64:
        """ Get: Keywords(self: EventDescriptor) -> Int64 """
        ...

    @property
    def Level(self) -> Byte:
        """ Get: Level(self: EventDescriptor) -> Byte """
        ...

    @property
    def Opcode(self) -> Byte:
        """ Get: Opcode(self: EventDescriptor) -> Byte """
        ...

    @property
    def Task(self) -> int:
        """ Get: Task(self: EventDescriptor) -> int """
        ...

    @property
    def Version(self) -> Byte:
        """ Get: Version(self: EventDescriptor) -> Byte """
        ...



class EventProvider(IDisposable): # skipped bases: <type 'object'>
    """ EventProvider(providerGuid: Guid) """
    def Close(self): # -> 
        """ Close(self: EventProvider) """
        ...

    @staticmethod
    def CreateActivityId() -> Guid:
        """ CreateActivityId() -> Guid """
        ...

    @staticmethod
    def GetLastWriteEventError(): # -> WriteEventErrorCode
        """ GetLastWriteEventError() -> WriteEventErrorCode """
        ...

    def IsEnabled(self, level:Byte = ..., keywords:Int64 = ...) -> bool:
        """
        IsEnabled(self: EventProvider) -> bool
        IsEnabled(self: EventProvider, level: Byte, keywords: Int64) -> bool
        """
        ...

    @staticmethod
    def SetActivityId(id:Guid) -> Guid:
        """ SetActivityId(id: Guid) -> Guid """
        ...

    def WriteEvent(self, eventDescriptor:EventDescriptor, *__args:Array) -> Tuple_[bool, EventDescriptor]:
        """
        WriteEvent(self: EventProvider, eventDescriptor: EventDescriptor, *eventPayload: Array[object]) -> (bool, EventDescriptor)
        WriteEvent(self: EventProvider, eventDescriptor: EventDescriptor, data: str) -> (bool, EventDescriptor)
        """
        ...

    def WriteEventErrorCode(self, *args): #cannot find CLR method
        """ enum WriteEventErrorCode, values: EventTooBig (2), NoError (0), NoFreeBuffers (1) """
        ...

    def WriteMessageEvent(self, eventMessage:str, eventLevel:Byte = ..., eventKeywords:Int64 = ...) -> bool:
        """
        WriteMessageEvent(self: EventProvider, eventMessage: str, eventLevel: Byte, eventKeywords: Int64) -> bool
        WriteMessageEvent(self: EventProvider, eventMessage: str) -> bool
        """
        ...

    def WriteTransferEvent(self, eventDescriptor:EventDescriptor, relatedActivityId:Guid, eventPayload:Array) -> Tuple_[bool, EventDescriptor]:
        """ WriteTransferEvent(self: EventProvider, eventDescriptor: EventDescriptor, relatedActivityId: Guid, *eventPayload: Array[object]) -> (bool, EventDescriptor) """
        ...



class EventProviderTraceListener(TraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    EventProviderTraceListener(providerId: str)
    EventProviderTraceListener(providerId: str, name: str)
    EventProviderTraceListener(providerId: str, name: str, delimiter: str)
    """
    @property
    def Delimiter(self) -> str:
        """
        Get: Delimiter(self: EventProviderTraceListener) -> str
        Set: Delimiter(self: EventProviderTraceListener) = value
        """
        ...



# variables with complex values

