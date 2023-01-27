# encoding: utf-8
# module Windows.UI.Xaml.Media.Animation calls itself Animation
# from System.Runtime.WindowsRuntime.UI.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, IFormattable, TimeSpan

"""The following names are not found in the module: field#
"""

# no functions
# classes

class KeyTime: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def TimeSpan(self) -> TimeSpan:
        """ Get: TimeSpan(self: KeyTime) -> TimeSpan """
        ...


    @staticmethod
    def Equals(*__args) -> bool:
        """
        Equals(keyTime1: KeyTime, keyTime2: KeyTime) -> bool
        Equals(self: KeyTime, value: KeyTime) -> bool
        Equals(self: KeyTime, value: object) -> bool
        """
        ...

    @staticmethod
    def FromTimeSpan(timeSpan:TimeSpan) -> KeyTime:
        """ FromTimeSpan(timeSpan: TimeSpan) -> KeyTime """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: KeyTime) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: KeyTime) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class RepeatBehavior(IFormattable): # skipped bases: <type 'object'>
    """
    RepeatBehavior(count: float)
    RepeatBehavior(duration: TimeSpan)
    """
    @property
    def Count(self) -> float:
        """
        Get: Count(self: RepeatBehavior) -> float
        Set: Count(self: RepeatBehavior) = value
        """
        ...

    @property
    def Duration(self) -> TimeSpan:
        """
        Get: Duration(self: RepeatBehavior) -> TimeSpan
        Set: Duration(self: RepeatBehavior) = value
        """
        ...

    @property
    def Forever(self) -> RepeatBehavior:
        """ Get: Forever() -> RepeatBehavior """
        ...

    @property
    def HasCount(self) -> bool:
        """ Get: HasCount(self: RepeatBehavior) -> bool """
        ...

    @property
    def HasDuration(self) -> bool:
        """ Get: HasDuration(self: RepeatBehavior) -> bool """
        ...

    @property
    def Type(self) -> RepeatBehaviorType:
        """
        Get: Type(self: RepeatBehavior) -> RepeatBehaviorType
        Set: Type(self: RepeatBehavior) = value
        """
        ...


    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: RepeatBehavior, value: object) -> bool
        Equals(self: RepeatBehavior, repeatBehavior: RepeatBehavior) -> bool
        Equals(repeatBehavior1: RepeatBehavior, repeatBehavior2: RepeatBehavior) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: RepeatBehavior) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class RepeatBehaviorType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RepeatBehaviorType, values: Count (0), Duration (1), Forever (2) """
    Count: RepeatBehaviorType = ...
    Duration: RepeatBehaviorType = ...
    Forever: RepeatBehaviorType = ...
    value__ = ...


