# encoding: utf-8
# module System.Security.Authentication.ExtendedProtection calls itself ExtendedProtection
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.Win32.SafeHandles import SafeHandleZeroOrMinusOneIsInvalid

from System import Array, Enum

from System.Collections import ICollection, ReadOnlyCollectionBase

from System.ComponentModel import TypeConverter

from System.Runtime.Serialization import ISerializable

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ChannelBinding(SafeHandleZeroOrMinusOneIsInvalid): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def Size(self) -> int:
        """ Get: Size(self: ChannelBinding) -> int """
        ...


    handle = ...


class ChannelBindingKind(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ChannelBindingKind, values: Endpoint (26), Unique (25), Unknown (0) """
    Endpoint: ChannelBindingKind = ...
    Unique: ChannelBindingKind = ...
    Unknown: ChannelBindingKind = ...
    value__ = ...


class ExtendedProtectionPolicy(ISerializable): # skipped bases: <type 'object'>
    """
    ExtendedProtectionPolicy(policyEnforcement: PolicyEnforcement, protectionScenario: ProtectionScenario, customServiceNames: ServiceNameCollection)
    ExtendedProtectionPolicy(policyEnforcement: PolicyEnforcement, protectionScenario: ProtectionScenario, customServiceNames: ICollection)
    ExtendedProtectionPolicy(policyEnforcement: PolicyEnforcement, customChannelBinding: ChannelBinding)
    ExtendedProtectionPolicy(policyEnforcement: PolicyEnforcement)
    """
    @property
    def CustomChannelBinding(self) -> ChannelBinding:
        """ Get: CustomChannelBinding(self: ExtendedProtectionPolicy) -> ChannelBinding """
        ...

    @property
    def CustomServiceNames(self) -> ServiceNameCollection:
        """ Get: CustomServiceNames(self: ExtendedProtectionPolicy) -> ServiceNameCollection """
        ...

    @property
    def OSSupportsExtendedProtection(self) -> bool:
        """ Get: OSSupportsExtendedProtection() -> bool """
        ...

    @property
    def PolicyEnforcement(self) -> PolicyEnforcement:
        """ Get: PolicyEnforcement(self: ExtendedProtectionPolicy) -> PolicyEnforcement """
        ...

    @property
    def ProtectionScenario(self) -> ProtectionScenario:
        """ Get: ProtectionScenario(self: ExtendedProtectionPolicy) -> ProtectionScenario """
        ...


    def ToString(self) -> str:
        """ ToString(self: ExtendedProtectionPolicy) -> str """
        ...



class ExtendedProtectionPolicyTypeConverter(TypeConverter): # skipped bases: <type 'object'>
    """ ExtendedProtectionPolicyTypeConverter() """
    pass

class PolicyEnforcement(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PolicyEnforcement, values: Always (2), Never (0), WhenSupported (1) """
    Always: PolicyEnforcement = ...
    Never: PolicyEnforcement = ...
    value__ = ...
    WhenSupported: PolicyEnforcement = ...


class ProtectionScenario(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProtectionScenario, values: TransportSelected (0), TrustedProxy (1) """
    TransportSelected: ProtectionScenario = ...
    TrustedProxy: ProtectionScenario = ...
    value__ = ...


class ServiceNameCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ ServiceNameCollection(items: ICollection) """
    def Contains(self, searchServiceName:str) -> bool:
        """ Contains(self: ServiceNameCollection, searchServiceName: str) -> bool """
        ...

    def Merge(self, *__args:str) -> ServiceNameCollection:
        """
        Merge(self: ServiceNameCollection, serviceName: str) -> ServiceNameCollection
        Merge(self: ServiceNameCollection, serviceNames: IEnumerable) -> ServiceNameCollection
        """
        ...

    def __new__(cls, items:ICollection) -> Self:
        """ __new__(cls: type, items: ICollection) """
        ...


class TokenBinding: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BindingType(self) -> TokenBindingType:
        """ Get: BindingType(self: TokenBinding) -> TokenBindingType """
        ...


    def GetRawTokenBindingId(self) -> Array:
        """ GetRawTokenBindingId(self: TokenBinding) -> Array[Byte] """
        ...


class TokenBindingType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TokenBindingType, values: Provided (0), Referred (1) """
    Provided: TokenBindingType = ...
    Referred: TokenBindingType = ...
    value__ = ...


# variables with complex values

