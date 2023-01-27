# encoding: utf-8
# module Windows.Foundation calls itself Foundation
# from System.Runtime.WindowsRuntime, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import IFormattable


# no functions
# classes

class Point(IFormattable): # skipped bases: <type 'object'>
    """ Point(x: float, y: float) """
    @property
    def X(self) -> float:
        """
        Get: X(self: Point) -> float
        Set: X(self: Point) = value
        """
        ...

    @property
    def Y(self) -> float:
        """
        Get: Y(self: Point) -> float
        Set: Y(self: Point) = value
        """
        ...


    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: Point, o: object) -> bool
        Equals(self: Point, value: Point) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Point) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Rect(IFormattable): # skipped bases: <type 'object'>
    """
    Rect(x: float, y: float, width: float, height: float)
    Rect(point1: Point, point2: Point)
    Rect(location: Point, size: Size)
    """
    @property
    def Bottom(self) -> float:
        """ Get: Bottom(self: Rect) -> float """
        ...

    @property
    def Empty(self) -> Rect:
        """ Get: Empty() -> Rect """
        ...

    @property
    def Height(self) -> float:
        """
        Get: Height(self: Rect) -> float
        Set: Height(self: Rect) = value
        """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: Rect) -> bool """
        ...

    @property
    def Left(self) -> float:
        """ Get: Left(self: Rect) -> float """
        ...

    @property
    def Right(self) -> float:
        """ Get: Right(self: Rect) -> float """
        ...

    @property
    def Top(self) -> float:
        """ Get: Top(self: Rect) -> float """
        ...

    @property
    def Width(self) -> float:
        """
        Get: Width(self: Rect) -> float
        Set: Width(self: Rect) = value
        """
        ...

    @property
    def X(self) -> float:
        """
        Get: X(self: Rect) -> float
        Set: X(self: Rect) = value
        """
        ...

    @property
    def Y(self) -> float:
        """
        Get: Y(self: Rect) -> float
        Set: Y(self: Rect) = value
        """
        ...


    def Contains(self, point:Point) -> bool:
        """ Contains(self: Rect, point: Point) -> bool """
        ...

    def Equals(self, *__args:Rect) -> bool:
        """
        Equals(self: Rect, value: Rect) -> bool
        Equals(self: Rect, o: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Rect) -> int """
        ...

    def Intersect(self, rect:Rect): # -> 
        """ Intersect(self: Rect, rect: Rect) """
        ...

    def Union(self, *__args:Rect): # -> 
        """ Union(self: Rect, rect: Rect)Union(self: Rect, point: Point) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class Size: # skipped bases: <type 'object'>, <type 'object'>
    """ Size(width: float, height: float) """
    @property
    def Empty(self) -> Size:
        """ Get: Empty() -> Size """
        ...

    @property
    def Height(self) -> float:
        """
        Get: Height(self: Size) -> float
        Set: Height(self: Size) = value
        """
        ...

    @property
    def IsEmpty(self) -> bool:
        """ Get: IsEmpty(self: Size) -> bool """
        ...

    @property
    def Width(self) -> float:
        """
        Get: Width(self: Size) -> float
        Set: Width(self: Size) = value
        """
        ...


    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: Size, o: object) -> bool
        Equals(self: Size, value: Size) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Size) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Size) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



