# encoding: utf-8
# module SqlContracts
# from Microsoft.SqlServer.Diagnostics.STrace, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Attribute, Enum, EventArgs, InvalidOperationException, 
    Predicate, Type)

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    ObjectInvariantCheck, T, field#)
"""

# no functions
# classes

class Contract: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Assert(condition:bool, message:str = ...): # -> 
        """ Assert(condition: bool, message: str)Assert(condition: bool) """
        ...

    @staticmethod
    def Assume(condition:bool, message:str = ...): # -> 
        """ Assume(condition: bool, message: str)Assume(condition: bool) """
        ...

    @staticmethod
    def CheckObjectInvariant(check): # ->  # Not found arg types: {'check': 'ObjectInvariantCheck'}
        """ CheckObjectInvariant(check: ObjectInvariantCheck) """
        ...

    @staticmethod
    def EndContractBlock(): # -> 
        """ EndContractBlock() """
        ...

    @staticmethod
    def Ensures(condition:bool, message:str = ...): # -> 
        """ Ensures(condition: bool, message: str)Ensures(condition: bool) """
        ...

    @staticmethod
    def Ensures2(condition:bool, message:str = ...): # -> 
        """ Ensures2(condition: bool, message: str)Ensures2(condition: bool) """
        ...

    @staticmethod
    def EnsuresOnThrow(condition:bool, message:str = ...): # -> 
        """ EnsuresOnThrow[TException](condition: bool, message: str)EnsuresOnThrow[TException](condition: bool) """
        ...

    @staticmethod
    def Exists(*__args) -> bool:
        """
        Exists(inclusiveLowerBound: int, exclusiveUpperBound: int, predicate: Predicate[int]) -> bool
        Exists[T](collection: IEnumerable[T], predicate: Predicate[T]) -> bool
        """
        ...

    @staticmethod
    def ForAll(*__args) -> bool:
        """
        ForAll(inclusiveLowerBound: int, exclusiveUpperBound: int, predicate: Predicate[int]) -> bool
        ForAll[T](collection: IEnumerable[T], predicate: Predicate[T]) -> bool
        """
        ...

    @staticmethod
    def Invariant(condition:bool, message:str = ...): # -> 
        """ Invariant(condition: bool, message: str)Invariant(condition: bool) """
        ...

    def ObjectInvariantCheck(self, *args): #cannot find CLR method
        """ ObjectInvariantCheck(object: object, method: IntPtr) """
        ...

    @staticmethod
    def OldValue(value): # -> T # Not found arg types: {'value': 'T'}
        """ OldValue[T](value: T) -> T """
        ...

    @staticmethod
    def Requires(condition:bool, message:str = ...): # -> 
        """ Requires(condition: bool, message: str)Requires(condition: bool) """
        ...

    @staticmethod
    def RequiresAlways(condition:bool, message:str = ...): # -> 
        """ RequiresAlways(condition: bool, message: str)RequiresAlways(condition: bool) """
        ...

    @staticmethod
    def Result(): # -> T
        """ Result[T]() -> T """
        ...

    ContractFailed = ...
    __all__: list = ...


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
    """ ContractFailedEventArgs(debugMessage: str, failureKind: ContractFailureKind) """
    @property
    def Condition(self) -> str:
        """ Get: Condition(self: ContractFailedEventArgs) -> str """
        ...

    @property
    def DebugMessage(self) -> str:
        """ Get: DebugMessage(self: ContractFailedEventArgs) -> str """
        ...

    @property
    def FailureKind(self) -> ContractFailureKind:
        """ Get: FailureKind(self: ContractFailedEventArgs) -> ContractFailureKind """
        ...

    @property
    def Handled(self) -> bool:
        """
        Get: Handled(self: ContractFailedEventArgs) -> bool
        Set: Handled(self: ContractFailedEventArgs) = value
        """
        ...


    def __new__(cls, debugMessage:str, failureKind:ContractFailureKind) -> Self:
        """ __new__(cls: type, debugMessage: str, failureKind: ContractFailureKind) """
        ...


class ContractFailureException(InvalidOperationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ContractFailureException(failureKind: ContractFailureKind, debugMessage: str)
    ContractFailureException(info: SerializationInfo, context: StreamingContext)
    """
    @property
    def DebugMessage(self) -> str:
        """ Get: DebugMessage(self: ContractFailureException) -> str """
        ...

    @property
    def FailureKind(self) -> ContractFailureKind:
        """ Get: FailureKind(self: ContractFailureException) -> ContractFailureKind """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: ContractFailureException) -> str """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: ContractFailureException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class ContractFailureKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ContractFailureKind, values: Assert (0), Assume (1), Invariant (2), Postcondition (3), Precondition (4) """
    Assert: ContractFailureKind = ...
    Assume: ContractFailureKind = ...
    Invariant: ContractFailureKind = ...
    Postcondition: ContractFailureKind = ...
    Precondition: ContractFailureKind = ...
    value__ = ...


class ContractInvariantMethodAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ContractInvariantMethodAttribute() """
    pass

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

class RuntimeContractsAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ RuntimeContractsAttribute() """
    pass

