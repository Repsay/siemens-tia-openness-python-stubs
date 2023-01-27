# encoding: utf-8
# module System.Media calls itself Media
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.ComponentModel import Component

from System.IO import Stream

from System.Runtime.Serialization import ISerializable

from typing import Self

"""The following names are not found in the module: BoundEvent
"""

# no functions
# classes

class SoundPlayer(ISerializable, Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """
    SoundPlayer()
    SoundPlayer(soundLocation: str)
    SoundPlayer(stream: Stream)
    """
    @property
    def IsLoadCompleted(self) -> bool:
        """ Get: IsLoadCompleted(self: SoundPlayer) -> bool """
        ...

    @property
    def LoadTimeout(self) -> int:
        """
        Get: LoadTimeout(self: SoundPlayer) -> int
        Set: LoadTimeout(self: SoundPlayer) = value
        """
        ...

    @property
    def SoundLocation(self) -> str:
        """
        Get: SoundLocation(self: SoundPlayer) -> str
        Set: SoundLocation(self: SoundPlayer) = value
        """
        ...

    @property
    def Stream(self) -> Stream:
        """
        Get: Stream(self: SoundPlayer) -> Stream
        Set: Stream(self: SoundPlayer) = value
        """
        ...

    @property
    def Tag(self) -> object:
        """
        Get: Tag(self: SoundPlayer) -> object
        Set: Tag(self: SoundPlayer) = value
        """
        ...


    def Load(self): # -> 
        """ Load(self: SoundPlayer) """
        ...

    def LoadAsync(self): # -> 
        """ LoadAsync(self: SoundPlayer) """
        ...

    def OnLoadCompleted(self, *args): #cannot find CLR method
        """ OnLoadCompleted(self: SoundPlayer, e: AsyncCompletedEventArgs) """
        ...

    def OnSoundLocationChanged(self, *args): #cannot find CLR method
        """ OnSoundLocationChanged(self: SoundPlayer, e: EventArgs) """
        ...

    def OnStreamChanged(self, *args): #cannot find CLR method
        """ OnStreamChanged(self: SoundPlayer, e: EventArgs) """
        ...

    def Play(self): # -> 
        """ Play(self: SoundPlayer) """
        ...

    def PlayLooping(self): # -> 
        """ PlayLooping(self: SoundPlayer) """
        ...

    def PlaySync(self): # -> 
        """ PlaySync(self: SoundPlayer) """
        ...

    def Stop(self): # -> 
        """ Stop(self: SoundPlayer) """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, soundLocation: str)
        __new__(cls: type, stream: Stream)
        __new__(cls: type, serializationInfo: SerializationInfo, context: StreamingContext)
        """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    LoadCompleted = ...
    SoundLocationChanged = ...
    StreamChanged = ...


class SystemSound: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Play(self): # -> 
        """ Play(self: SystemSound) """
        ...


class SystemSounds: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Asterisk(self) -> SystemSound:
        """ Get: Asterisk() -> SystemSound """
        ...

    @property
    def Beep(self) -> SystemSound:
        """ Get: Beep() -> SystemSound """
        ...

    @property
    def Exclamation(self) -> SystemSound:
        """ Get: Exclamation() -> SystemSound """
        ...

    @property
    def Hand(self) -> SystemSound:
        """ Get: Hand() -> SystemSound """
        ...

    @property
    def Question(self) -> SystemSound:
        """ Get: Question() -> SystemSound """
        ...




