# encoding: utf-8
# module System.Diagnostics.Contracts calls itself Contracts
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Enum, EventArgs, Predicate, Type

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: BoundEvent, T, field#
"""

# no functions
# classes

class Contract: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Assert(condition:bool, userMessage:str = ...): # -> 
        """ Assert(condition: bool)Assert(condition: bool, userMessage: str) """
        ...

    @staticmethod
    def Assume(condition:bool, userMessage:str = ...): # -> 
        """ Assume(condition: bool)Assume(condition: bool, userMessage: str) """
        ...

    @staticmethod
    def EndContractBlock(): # -> 
        """ EndContractBlock() """
        ...

    @staticmethod
    def Ensures(condition:bool, userMessage:str = ...): # -> 
        """ Ensures(condition: bool)Ensures(condition: bool, userMessage: str) """
        ...

    @staticmethod
    def EnsuresOnThrow(condition:bool, userMessage:str = ...): # -> 
        """ EnsuresOnThrow[TException](condition: bool)EnsuresOnThrow[TException](condition: bool, userMessage: str) """
        ...

    @staticmethod
    def Exists(*__args) -> bool:
        """
        Exists(fromInclusive: int, toExclusive: int, predicate: Predicate[int]) -> bool
        Exists[T](collection: IEnumerable[T], predicate: Predicate[T]) -> bool
        """
        ...

    @staticmethod
    def ForAll(*__args) -> bool:
        """
        ForAll(fromInclusive: int, toExclusive: int, predicate: Predicate[int]) -> bool
        ForAll[T](collection: IEnumerable[T], predicate: Predicate[T]) -> bool
        """
        ...

    @staticmethod
    def Invariant(condition:bool, userMessage:str = ...): # -> 
        """ Invariant(condition: bool)Invariant(condition: bool, userMessage: str) """
        ...

    @staticmethod
    def OldValue(value): # -> T # Not found arg types: {'value': 'T'}
        """ OldValue[T](value: T) -> T """
        ...

    @staticmethod
    def Requires(condition:bool, userMessage:str = ...): # -> 
        """ Requires(condition: bool)Requires(condition: bool, userMessage: str)Requires[TException](condition: bool)Requires[TException](condition: bool, userMessage: str) """
        ...

    @staticmethod
    def Result(): # -> T
        """ Result[T]() -> T """
        ...

    @staticmethod
    def ValueAtReturn(value): # -> Tuple_[T, T]
        """ ValueAtReturn[T]() -> (T, T) """
        ...

    ContractFailed = ...
    __all__: list = ...


class ContractAbbreviatorAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ContractAbbreviatorAttribute() """
    pass

class ContractArgumentValidatorAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ContractArgumentValidatorAttribute() """
    pass

class ContractClassAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ContractClassAttribute(typeContainingContracts: Type) """
    @property
    def TypeContainingContracts(self) -> Type:
        """ Get: TypeContainingContracts(self: ContractClassAttribute) -> Type """
        ...


    def __new__(cls, typeContainingContracts:Type) -> Self:
        """ __new__(cls: type, typeContainingContracts: Type) """
        ...


class ContractClassForAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ContractClassForAttribute(typeContractsAreFor: Type) """
    @property
    def TypeContractsAreFor(self) -> Type:
        """ Get: TypeContractsAreFor(self: ContractClassForAttribute) -> Type """
        ...


    def __new__(cls, typeContractsAreFor:Type) -> Self:
        """ __new__(cls: type, typeContractsAreFor: Type) """
        ...


class ContractFailedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ ContractFailedEventArgs(failureKind: ContractFailureKind, message: str, condition: str, originalException: Exception) """
    @property
    def Condition(self) -> str:
        """ Get: Condition(self: ContractFailedEventArgs) -> str """
        ...

    @property
    def FailureKind(self) -> ContractFailureKind:
        """ Get: FailureKind(self: ContractFailedEventArgs) -> ContractFailureKind """
        ...

    @property
    def Handled(self) -> bool:
        """ Get: Handled(self: ContractFailedEventArgs) -> bool """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: ContractFailedEventArgs) -> str """
        ...

    @property
    def OriginalException(self) -> Exception:
        """ Get: OriginalException(self: ContractFailedEventArgs) -> Exception """
        ...

    @property
    def Unwind(self) -> bool:
        """ Get: Unwind(self: ContractFailedEventArgs) -> bool """
        ...


    def SetHandled(self): # -> 
        """ SetHandled(self: ContractFailedEventArgs) """
        ...

    def SetUnwind(self): # -> 
        """ SetUnwind(self: ContractFailedEventArgs) """
        ...

    def __new__(cls, failureKind:ContractFailureKind, message:str, condition:str, originalException:Exception) -> Self:
        """ __new__(cls: type, failureKind: ContractFailureKind, message: str, condition: str, originalException: Exception) """
        ...


class ContractFailureKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ContractFailureKind, values: Assert (4), Assume (5), Invariant (3), Postcondition (1), PostconditionOnException (2), Precondition (0) """
    Assert: ContractFailureKind = ...
    Assume: ContractFailureKind = ...
    Invariant: ContractFailureKind = ...
    Postcondition: ContractFailureKind = ...
    PostconditionOnException: ContractFailureKind = ...
    Precondition: ContractFailureKind = ...
    value__ = ...


class ContractInvariantMethodAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ContractInvariantMethodAttribute() """
    pass

class ContractOptionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ContractOptionAttribute(category: str, setting: str, enabled: bool)
    ContractOptionAttribute(category: str, setting: str, value: str)
    """
    @property
    def Category(self) -> str:
        """ Get: Category(self: ContractOptionAttribute) -> str """
        ...

    @property
    def Enabled(self) -> bool:
        """ Get: Enabled(self: ContractOptionAttribute) -> bool """
        ...

    @property
    def Setting(self) -> str:
        """ Get: Setting(self: ContractOptionAttribute) -> str """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: ContractOptionAttribute) -> str """
        ...


    def __new__(cls, category:str, setting:str, *__args:bool) -> Self:
        """
        __new__(cls: type, category: str, setting: str, enabled: bool)
        __new__(cls: type, category: str, setting: str, value: str)
        """
        ...


class ContractPublicPropertyNameAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ContractPublicPropertyNameAttribute(name: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: ContractPublicPropertyNameAttribute) -> str """
        ...


    def __new__(cls, name:str) -> Self:
        """ __new__(cls: type, name: str) """
        ...


class ContractReferenceAssemblyAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ContractReferenceAssemblyAttribute() """
    pass

class ContractRuntimeIgnoredAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ContractRuntimeIgnoredAttribute() """
    pass

class ContractVerificationAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ContractVerificationAttribute(value: bool) """
    @property
    def Value(self) -> bool:
        """ Get: Value(self: ContractVerificationAttribute) -> bool """
        ...


    def __new__(cls, value:bool) -> Self:
        """ __new__(cls: type, value: bool) """
        ...


class PureAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PureAttribute() """
    pass

# variables with complex values

