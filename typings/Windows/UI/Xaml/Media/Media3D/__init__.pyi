# encoding: utf-8
# module Windows.UI.Xaml.Media.Media3D calls itself Media3D
# from System.Runtime.WindowsRuntime.UI.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import IFormattable


# no functions
# classes

class Matrix3D(IFormattable): # skipped bases: <type 'object'>
    """ Matrix3D(m11: float, m12: float, m13: float, m14: float, m21: float, m22: float, m23: float, m24: float, m31: float, m32: float, m33: float, m34: float, offsetX: float, offsetY: float, offsetZ: float, m44: float) """
    @property
    def HasInverse(self) -> bool:
        """ Get: HasInverse(self: Matrix3D) -> bool """
        ...

    @property
    def Identity(self) -> Matrix3D:
        """ Get: Identity() -> Matrix3D """
        ...

    @property
    def IsIdentity(self) -> bool:
        """ Get: IsIdentity(self: Matrix3D) -> bool """
        ...

    @property
    def M11(self) -> float:
        """
        Get: M11(self: Matrix3D) -> float
        Set: M11(self: Matrix3D) = value
        """
        ...

    @property
    def M12(self) -> float:
        """
        Get: M12(self: Matrix3D) -> float
        Set: M12(self: Matrix3D) = value
        """
        ...

    @property
    def M13(self) -> float:
        """
        Get: M13(self: Matrix3D) -> float
        Set: M13(self: Matrix3D) = value
        """
        ...

    @property
    def M14(self) -> float:
        """
        Get: M14(self: Matrix3D) -> float
        Set: M14(self: Matrix3D) = value
        """
        ...

    @property
    def M21(self) -> float:
        """
        Get: M21(self: Matrix3D) -> float
        Set: M21(self: Matrix3D) = value
        """
        ...

    @property
    def M22(self) -> float:
        """
        Get: M22(self: Matrix3D) -> float
        Set: M22(self: Matrix3D) = value
        """
        ...

    @property
    def M23(self) -> float:
        """
        Get: M23(self: Matrix3D) -> float
        Set: M23(self: Matrix3D) = value
        """
        ...

    @property
    def M24(self) -> float:
        """
        Get: M24(self: Matrix3D) -> float
        Set: M24(self: Matrix3D) = value
        """
        ...

    @property
    def M31(self) -> float:
        """
        Get: M31(self: Matrix3D) -> float
        Set: M31(self: Matrix3D) = value
        """
        ...

    @property
    def M32(self) -> float:
        """
        Get: M32(self: Matrix3D) -> float
        Set: M32(self: Matrix3D) = value
        """
        ...

    @property
    def M33(self) -> float:
        """
        Get: M33(self: Matrix3D) -> float
        Set: M33(self: Matrix3D) = value
        """
        ...

    @property
    def M34(self) -> float:
        """
        Get: M34(self: Matrix3D) -> float
        Set: M34(self: Matrix3D) = value
        """
        ...

    @property
    def M44(self) -> float:
        """
        Get: M44(self: Matrix3D) -> float
        Set: M44(self: Matrix3D) = value
        """
        ...

    @property
    def OffsetX(self) -> float:
        """
        Get: OffsetX(self: Matrix3D) -> float
        Set: OffsetX(self: Matrix3D) = value
        """
        ...

    @property
    def OffsetY(self) -> float:
        """
        Get: OffsetY(self: Matrix3D) -> float
        Set: OffsetY(self: Matrix3D) = value
        """
        ...

    @property
    def OffsetZ(self) -> float:
        """
        Get: OffsetZ(self: Matrix3D) -> float
        Set: OffsetZ(self: Matrix3D) = value
        """
        ...


    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: Matrix3D, o: object) -> bool
        Equals(self: Matrix3D, value: Matrix3D) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Matrix3D) -> int """
        ...

    def Invert(self): # -> 
        """ Invert(self: Matrix3D) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(matrix1: Matrix3D, matrix2: Matrix3D) -> Matrix3D """
        ...



