# encoding: utf-8
# module Windows.UI calls itself UI
# from System.Runtime.WindowsRuntime.UI.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Runtime.WindowsRuntime, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Byte, IFormattable

from System.Drawing import Color


# no functions
# classes

class Color(IFormattable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def A(self) -> Byte:
        """
        Get: A(self: Color) -> Byte
        Set: A(self: Color) = value
        """
        ...

    @property
    def B(self) -> Byte:
        """
        Get: B(self: Color) -> Byte
        Set: B(self: Color) = value
        """
        ...

    @property
    def G(self) -> Byte:
        """
        Get: G(self: Color) -> Byte
        Set: G(self: Color) = value
        """
        ...

    @property
    def R(self) -> Byte:
        """
        Get: R(self: Color) -> Byte
        Set: R(self: Color) = value
        """
        ...


    def Equals(self, *__args:object) -> bool:
        """
        Equals(self: Color, o: object) -> bool
        Equals(self: Color, color: Color) -> bool
        """
        ...

    @staticmethod
    def FromArgb(a:Byte, r:Byte, g:Byte, b:Byte) -> Color:
        """ FromArgb(a: Byte, r: Byte, g: Byte, b: Byte) -> Color """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Color) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


# variables with complex values

