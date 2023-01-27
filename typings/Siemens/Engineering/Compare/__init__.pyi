# encoding: utf-8
# module Siemens.Engineering.Compare calls itself Compare
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import IEngineeringComposition, IEngineeringObject

from System import Enum, IEquatable

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class CompareResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Summary object that contains the result of a comparison """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: CompareResult) -> IEngineeringObject
        """
        ...

    @property
    def RootElement(self) -> CompareResultElement:
        """
        Browse to the element containing the result of a given compare scenario

        Get: RootElement(self: CompareResult) -> CompareResultElement
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CompareResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CompareResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CompareResultElement(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Compare results on an element """
    @property
    def ComparisonResult(self) -> CompareResultState:
        """
        The result of a comparison

        Get: ComparisonResult(self: CompareResultElement) -> CompareResultState
        """
        ...

    @property
    def DetailedInformation(self) -> str:
        """
        Information on the result of a given compare scenario

        Get: DetailedInformation(self: CompareResultElement) -> str
        """
        ...

    @property
    def Elements(self) -> CompareResultElementComposition:
        """
        Browse to the collection of compare scenarios on a single element

        Get: Elements(self: CompareResultElement) -> CompareResultElementComposition
        """
        ...

    @property
    def LeftName(self) -> str:
        """
        Left side name of a compare scenario on a single element

        Get: LeftName(self: CompareResultElement) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: CompareResultElement) -> IEngineeringObject
        """
        ...

    @property
    def RightName(self) -> str:
        """
        Right side name of a compare scenario on a single element

        Get: RightName(self: CompareResultElement) -> str
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CompareResultElement) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CompareResultElement) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CompareResultElementComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of CompareResultElements """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: CompareResultElementComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CompareResultElementComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CompareResultElementComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CompareResultElement](enumerable: IEnumerable[CompareResultElement], value: CompareResultElement) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CompareResultState(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    The list of possible states of a compare result

    enum CompareResultState, values: CompareIrrelevant (8), FolderContainsDifferencesOwnStateDifferent (2), FolderContentEqualOwnStateDifferent (3), FolderContentsDifferent (0), FolderContentsIdentical (1), LeftMissing (5), ObjectsDifferent (4), ObjectsIdentical (7), RightMissing (6)
    """
    CompareIrrelevant: CompareResultState = ...
    FolderContainsDifferencesOwnStateDifferent: CompareResultState = ...
    FolderContentEqualOwnStateDifferent: CompareResultState = ...
    FolderContentsDifferent: CompareResultState = ...
    FolderContentsIdentical: CompareResultState = ...
    LeftMissing: CompareResultState = ...
    ObjectsDifferent: CompareResultState = ...
    ObjectsIdentical: CompareResultState = ...
    RightMissing: CompareResultState = ...
    value__ = ...
