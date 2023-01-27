# encoding: utf-8
# module System.Windows.Forms.Layout calls itself Layout
# from System.Windows.Forms, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array

from System.Collections import IEnumerator, IList

from System.ComponentModel import TypeConverter

from System.Windows.Forms import BoundsSpecified, LayoutEventArgs


# no functions
# classes

class ArrangedElementCollection(IList): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ArrangedElementCollection) -> int """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ArrangedElementCollection, array: Array, index: int) """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: ArrangedElementCollection, obj: object) -> bool """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ArrangedElementCollection) -> IEnumerator """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: ArrangedElementCollection) -> int """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LayoutEngine: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def InitLayout(self, child:object, specified:BoundsSpecified): # -> 
        """ InitLayout(self: LayoutEngine, child: object, specified: BoundsSpecified) """
        ...

    def Layout(self, container:object, layoutEventArgs:LayoutEventArgs) -> bool:
        """ Layout(self: LayoutEngine, container: object, layoutEventArgs: LayoutEventArgs) -> bool """
        ...


class TableLayoutSettingsTypeConverter(TypeConverter): # skipped bases: <type 'object'>
    """ TableLayoutSettingsTypeConverter() """
    pass

