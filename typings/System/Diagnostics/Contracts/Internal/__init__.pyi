# encoding: utf-8
# module System.Diagnostics.Contracts.Internal calls itself Internal
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from SqlContracts import ContractFailureKind


# no functions
# classes

class ContractHelper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def RaiseContractFailedEvent(failureKind:ContractFailureKind, userMessage:str, conditionText:str, innerException:Exception) -> str:
        """ RaiseContractFailedEvent(failureKind: ContractFailureKind, userMessage: str, conditionText: str, innerException: Exception) -> str """
        ...

    @staticmethod
    def TriggerFailure(kind:ContractFailureKind, displayMessage:str, userMessage:str, conditionText:str, innerException:Exception): # -> 
        """ TriggerFailure(kind: ContractFailureKind, displayMessage: str, userMessage: str, conditionText: str, innerException: Exception) """
        ...

    __all__: list = ...


