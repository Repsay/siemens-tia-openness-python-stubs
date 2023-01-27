# encoding: utf-8
# module Windows.UI.Xaml.Media calls itself Media
# from System.Runtime.WindowsRuntime.UI.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import IFormattable

from Windows.Foundation import Point


# no functions
# classes

class Matrix(IFormattable): # skipped bases: <type 'object'>
    """ Matrix(m11: float, m12: float, m21: float, m22: float, offsetX: float, offsetY: float) """
    @property
    def Identity(self) -> Matrix:
        """ Get: Identity() -> Matrix """
        ...

    @property
    def IsIdentity(self) -> bool:
        """ Get: IsIdentity(self: Matrix) -> bool """
        ...

    @property
    def M11(self) -> float:
        """
        Get: M11(self: Matrix) -> float
        Set: M11(self: Matrix) = value
        """
        ...

    @property
    def M12(self) -> float:
        """
        Get: M12(self: Matrix) -> float
        Set: M12(self: Matrix) = value
        """
        ...

    @property
    def M21(self) -> float:
        """
        Get: M21(self: Matrix) -> float
        Set: M21(self: Matrix) = value
        """
        ...

    @property
    def M22(self) -> float:
        """
        Get: M22(self: Matrix) -> float
        Set: M22(self: Matrix) = value
        """
        ...

    @property
    def OffsetX(self) -> float:
        """
        Get: OffsetX(self: Matrix) -> float
        Set: OffsetX(self: Matrix) = value
        """
        ...

    @property
    def OffsetY(self) -> float:
        """
        Get: OffsetY(self: Matrix) -> float
        Set: OffsetY(self: Matrix) = value
        """
        ...


    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: Matrix, o: object) -> bool
        Equals(self: Matrix, value: Matrix) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Matrix) -> int """
        ...

    def Transform(self, point:Point) -> Point:
        """ Transform(self: Matrix, point: Point) -> Point """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



# variables with complex values

