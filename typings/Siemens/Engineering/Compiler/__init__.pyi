# encoding: utf-8
# module Siemens.Engineering.Compiler calls itself Compiler
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringComposition, IEngineeringObject,
    IEngineeringService)

from System import DateTime, Enum, IEquatable

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class CompilerResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ The results of a compilation """
    @property
    def ErrorCount(self) -> int:
        """
        Number of errors in a given compile scenario

        Get: ErrorCount(self: CompilerResult) -> int
        """
        ...

    @property
    def Messages(self) -> CompilerResultMessageComposition:
        """
        Collection of output messages for the result of a given compile scenario

        Get: Messages(self: CompilerResult) -> CompilerResultMessageComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: CompilerResult) -> IEngineeringObject
        """
        ...

    @property
    def State(self) -> CompilerResultState:
        """
        Final state of a given compile scenario

        Get: State(self: CompilerResult) -> CompilerResultState
        """
        ...

    @property
    def WarningCount(self) -> int:
        """
        Number of warnings in a given compile scenario

        Get: WarningCount(self: CompilerResult) -> int
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CompilerResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CompilerResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CompilerResultMessage(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Compilation results message """
    @property
    def DateTime(self) -> DateTime:
        """
        Date and time in a compiler message

        Get: DateTime(self: CompilerResultMessage) -> DateTime
        """
        ...

    @property
    def Description(self) -> str:
        """
        Description or content of a compiler message

        Get: Description(self: CompilerResultMessage) -> str
        """
        ...

    @property
    def ErrorCount(self) -> int:
        """
        Number of errors in a compiler message

        Get: ErrorCount(self: CompilerResultMessage) -> int
        """
        ...

    @property
    def Messages(self) -> CompilerResultMessageComposition:
        """
        Access to the compiler messages for a given compile scenario

        Get: Messages(self: CompilerResultMessage) -> CompilerResultMessageComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: CompilerResultMessage) -> IEngineeringObject
        """
        ...

    @property
    def Path(self) -> str:
        """
        Path to a compiler message

        Get: Path(self: CompilerResultMessage) -> str
        """
        ...

    @property
    def State(self) -> CompilerResultState:
        """
        Final state in a compiler message

        Get: State(self: CompilerResultMessage) -> CompilerResultState
        """
        ...

    @property
    def WarningCount(self) -> int:
        """
        Number of warnings in a compiler message

        Get: WarningCount(self: CompilerResultMessage) -> int
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CompilerResultMessage) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CompilerResultMessage) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CompilerResultMessageComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of CompareResultMessages """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: CompilerResultMessageComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CompilerResultMessageComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CompilerResultMessageComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CompilerResultMessage](enumerable: IEnumerable[CompilerResultMessage], value: CompilerResultMessage) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CompilerResultState(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    The list of possible compiler result options

    enum CompilerResultState, values: Error (3), Information (1), Success (0), Warning (2)
    """
    Error: CompilerResultState = ...
    Information: CompilerResultState = ...
    Success: CompilerResultState = ...
    value__ = ...
    Warning: CompilerResultState = ...


class ICompilable(IEngineeringService): # skipped bases: <type 'object'>
    """ An interface indication that the item supports compilation """
    def Compile(self) -> CompilerResult:
        """
        Compile(self: ICompilable) -> CompilerResult

            Compiles the item

            Returns: Siemens.Engineering.Compiler.CompilerResult
        """
        ...
