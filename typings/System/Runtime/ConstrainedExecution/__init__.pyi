# encoding: utf-8
# module System.Runtime.ConstrainedExecution calls itself ConstrainedExecution
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Enum

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class Cer(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Cer, values: MayFail (1), None (0), Success (2) """
    MayFail: Cer = ...
    Success: Cer = ...
    value__ = ...


class Consistency(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum Consistency, values: MayCorruptAppDomain (1), MayCorruptInstance (2), MayCorruptProcess (0), WillNotCorruptState (3) """
    MayCorruptAppDomain: Consistency = ...
    MayCorruptInstance: Consistency = ...
    MayCorruptProcess: Consistency = ...
    value__ = ...
    WillNotCorruptState: Consistency = ...


class CriticalFinalizerObject: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class PrePrepareMethodAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PrePrepareMethodAttribute() """
    pass

class ReliabilityContractAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ReliabilityContractAttribute(consistencyGuarantee: Consistency, cer: Cer) """
    @property
    def Cer(self) -> Cer:
        """ Get: Cer(self: ReliabilityContractAttribute) -> Cer """
        ...

    @property
    def ConsistencyGuarantee(self) -> Consistency:
        """ Get: ConsistencyGuarantee(self: ReliabilityContractAttribute) -> Consistency """
        ...


    def __new__(cls, consistencyGuarantee:Consistency, cer:Cer) -> Self:
        """ __new__(cls: type, consistencyGuarantee: Consistency, cer: Cer) """
        ...


