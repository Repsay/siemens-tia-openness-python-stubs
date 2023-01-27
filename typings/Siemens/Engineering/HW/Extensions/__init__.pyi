# encoding: utf-8
# module Siemens.Engineering.HW.Extensions calls itself Extensions
# from Siemens.Engineering, Version=16.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import IEngineeringObject

from System import IEquatable

"""The following names are not found in the module: IInternalObjectAccess
"""

from Siemens import IInternalObjectAccess

# no functions
# classes

class PlugLocation(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Information about a free slot. """
    @property
    def Label(self) -> str:
        """
        The label of the free slot.

        Get: Label(self: PlugLocation) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: PlugLocation) -> IEngineeringObject
        """
        ...

    @property
    def PositionNumber(self) -> int:
        """
        The position number of the free slot

        Get: PositionNumber(self: PlugLocation) -> int
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlugLocation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlugLocation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
