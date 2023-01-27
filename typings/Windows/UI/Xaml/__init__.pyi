# encoding: utf-8
# module Windows.UI.Xaml calls itself Xaml
# from System.Runtime.WindowsRuntime.UI.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, TimeSpan

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class CornerRadius: # skipped bases: <type 'object'>, <type 'object'>
    """
    CornerRadius(uniformRadius: float)
    CornerRadius(topLeft: float, topRight: float, bottomRight: float, bottomLeft: float)
    """
    @property
    def BottomLeft(self) -> float:
        """
        Get: BottomLeft(self: CornerRadius) -> float
        Set: BottomLeft(self: CornerRadius) = value
        """
        ...

    @property
    def BottomRight(self) -> float:
        """
        Get: BottomRight(self: CornerRadius) -> float
        Set: BottomRight(self: CornerRadius) = value
        """
        ...

    @property
    def TopLeft(self) -> float:
        """
        Get: TopLeft(self: CornerRadius) -> float
        Set: TopLeft(self: CornerRadius) = value
        """
        ...

    @property
    def TopRight(self) -> float:
        """
        Get: TopRight(self: CornerRadius) -> float
        Set: TopRight(self: CornerRadius) = value
        """
        ...


    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: CornerRadius, obj: object) -> bool
        Equals(self: CornerRadius, cornerRadius: CornerRadius) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: CornerRadius) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: CornerRadius) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Duration: # skipped bases: <type 'object'>, <type 'object'>
    """ Duration(timeSpan: TimeSpan) """
    @property
    def Automatic(self) -> Duration:
        """ Get: Automatic() -> Duration """
        ...

    @property
    def Forever(self) -> Duration:
        """ Get: Forever() -> Duration """
        ...

    @property
    def HasTimeSpan(self) -> bool:
        """ Get: HasTimeSpan(self: Duration) -> bool """
        ...

    @property
    def TimeSpan(self) -> TimeSpan:
        """ Get: TimeSpan(self: Duration) -> TimeSpan """
        ...


    def Add(self, duration:Duration) -> Duration:
        """ Add(self: Duration, duration: Duration) -> Duration """
        ...

    @staticmethod
    def Compare(t1:Duration, t2:Duration) -> int:
        """ Compare(t1: Duration, t2: Duration) -> int """
        ...

    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: Duration, value: object) -> bool
        Equals(self: Duration, duration: Duration) -> bool
        Equals(t1: Duration, t2: Duration) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Duration) -> int """
        ...

    def Subtract(self, duration:Duration) -> Duration:
        """ Subtract(self: Duration, duration: Duration) -> Duration """
        ...

    def ToString(self) -> str:
        """ ToString(self: Duration) -> str """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __cmp__(self, *args): #cannot find CLR method
        """ x.__cmp__(y) <==> cmp(x,y) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ge__(self, *args): #cannot find CLR method
        ...

    def __gt__(self, *args): #cannot find CLR method
        ...

    def __le__(self, *args): #cannot find CLR method
        ...

    def __lt__(self, *args): #cannot find CLR method
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __pos__(self, *args): #cannot find CLR method
        """ __pos__(duration: Duration) -> Duration """
        ...

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(t1: Duration, t2: Duration) -> Duration """
        ...

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(t1: Duration, t2: Duration) -> Duration """
        ...

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-y """
        ...



class DurationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DurationType, values: Automatic (0), Forever (2), TimeSpan (1) """
    Automatic: DurationType = ...
    Forever: DurationType = ...
    TimeSpan: DurationType = ...
    value__ = ...


class GridLength: # skipped bases: <type 'object'>, <type 'object'>
    """
    GridLength(pixels: float)
    GridLength(value: float, type: GridUnitType)
    """
    @property
    def Auto(self) -> GridLength:
        """ Get: Auto() -> GridLength """
        ...

    @property
    def GridUnitType(self) -> GridUnitType:
        """ Get: GridUnitType(self: GridLength) -> GridUnitType """
        ...

    @property
    def IsAbsolute(self) -> bool:
        """ Get: IsAbsolute(self: GridLength) -> bool """
        ...

    @property
    def IsAuto(self) -> bool:
        """ Get: IsAuto(self: GridLength) -> bool """
        ...

    @property
    def IsStar(self) -> bool:
        """ Get: IsStar(self: GridLength) -> bool """
        ...

    @property
    def Value(self) -> float:
        """ Get: Value(self: GridLength) -> float """
        ...


    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: GridLength, oCompare: object) -> bool
        Equals(self: GridLength, gridLength: GridLength) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: GridLength) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: GridLength) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class GridUnitType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GridUnitType, values: Auto (0), Pixel (1), Star (2) """
    Auto: GridUnitType = ...
    Pixel: GridUnitType = ...
    Star: GridUnitType = ...
    value__ = ...


class LayoutCycleException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    LayoutCycleException()
    LayoutCycleException(message: str)
    LayoutCycleException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class Thickness: # skipped bases: <type 'object'>, <type 'object'>
    """
    Thickness(uniformLength: float)
    Thickness(left: float, top: float, right: float, bottom: float)
    """
    @property
    def Bottom(self) -> float:
        """
        Get: Bottom(self: Thickness) -> float
        Set: Bottom(self: Thickness) = value
        """
        ...

    @property
    def Left(self) -> float:
        """
        Get: Left(self: Thickness) -> float
        Set: Left(self: Thickness) = value
        """
        ...

    @property
    def Right(self) -> float:
        """
        Get: Right(self: Thickness) -> float
        Set: Right(self: Thickness) = value
        """
        ...

    @property
    def Top(self) -> float:
        """
        Get: Top(self: Thickness) -> float
        Set: Top(self: Thickness) = value
        """
        ...


    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: Thickness, obj: object) -> bool
        Equals(self: Thickness, thickness: Thickness) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Thickness) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Thickness) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


# variables with complex values

