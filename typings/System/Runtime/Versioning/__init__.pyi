# encoding: utf-8
# module System.Runtime.Versioning calls itself Versioning
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Enum, IEquatable, Type, Version

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class CompatibilitySwitch: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetValue(compatibilitySwitchName:str) -> str:
        """ GetValue(compatibilitySwitchName: str) -> str """
        ...

    @staticmethod
    def IsEnabled(compatibilitySwitchName:str) -> bool:
        """ IsEnabled(compatibilitySwitchName: str) -> bool """
        ...

    __all__: list = ...


class ComponentGuaranteesAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ComponentGuaranteesAttribute(guarantees: ComponentGuaranteesOptions) """
    @property
    def Guarantees(self) -> ComponentGuaranteesOptions:
        """ Get: Guarantees(self: ComponentGuaranteesAttribute) -> ComponentGuaranteesOptions """
        ...


    def __new__(cls, guarantees:ComponentGuaranteesOptions) -> Self:
        """ __new__(cls: type, guarantees: ComponentGuaranteesOptions) """
        ...


class ComponentGuaranteesOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ComponentGuaranteesOptions, values: Exchange (1), None (0), SideBySide (4), Stable (2) """
    Exchange: ComponentGuaranteesOptions = ...
    SideBySide: ComponentGuaranteesOptions = ...
    Stable: ComponentGuaranteesOptions = ...
    value__ = ...


class FrameworkName(IEquatable): # skipped bases: <type 'object'>
    """
    FrameworkName(identifier: str, version: Version)
    FrameworkName(identifier: str, version: Version, profile: str)
    FrameworkName(frameworkName: str)
    """
    @property
    def FullName(self) -> str:
        """ Get: FullName(self: FrameworkName) -> str """
        ...

    @property
    def Identifier(self) -> str:
        """ Get: Identifier(self: FrameworkName) -> str """
        ...

    @property
    def Profile(self) -> str:
        """ Get: Profile(self: FrameworkName) -> str """
        ...

    @property
    def Version(self) -> Version:
        """ Get: Version(self: FrameworkName) -> Version """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: FrameworkName) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: FrameworkName) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ResourceConsumptionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ResourceConsumptionAttribute(resourceScope: ResourceScope)
    ResourceConsumptionAttribute(resourceScope: ResourceScope, consumptionScope: ResourceScope)
    """
    @property
    def ConsumptionScope(self) -> ResourceScope:
        """ Get: ConsumptionScope(self: ResourceConsumptionAttribute) -> ResourceScope """
        ...

    @property
    def ResourceScope(self) -> ResourceScope:
        """ Get: ResourceScope(self: ResourceConsumptionAttribute) -> ResourceScope """
        ...


    def __new__(cls, resourceScope:ResourceScope, consumptionScope:ResourceScope = ...) -> Self:
        """
        __new__(cls: type, resourceScope: ResourceScope)
        __new__(cls: type, resourceScope: ResourceScope, consumptionScope: ResourceScope)
        """
        ...


class ResourceExposureAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ ResourceExposureAttribute(exposureLevel: ResourceScope) """
    @property
    def ResourceExposureLevel(self) -> ResourceScope:
        """ Get: ResourceExposureLevel(self: ResourceExposureAttribute) -> ResourceScope """
        ...


    def __new__(cls, exposureLevel:ResourceScope) -> Self:
        """ __new__(cls: type, exposureLevel: ResourceScope) """
        ...


class ResourceScope(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) ResourceScope, values: AppDomain (4), Assembly (32), Library (8), Machine (1), None (0), Private (16), Process (2) """
    AppDomain: ResourceScope = ...
    Assembly: ResourceScope = ...
    Library: ResourceScope = ...
    Machine: ResourceScope = ...
    Private: ResourceScope = ...
    Process: ResourceScope = ...
    value__ = ...


class TargetFrameworkAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TargetFrameworkAttribute(frameworkName: str) """
    @property
    def FrameworkDisplayName(self) -> str:
        """
        Get: FrameworkDisplayName(self: TargetFrameworkAttribute) -> str
        Set: FrameworkDisplayName(self: TargetFrameworkAttribute) = value
        """
        ...

    @property
    def FrameworkName(self) -> str:
        """ Get: FrameworkName(self: TargetFrameworkAttribute) -> str """
        ...


    def __new__(cls, frameworkName:str) -> Self:
        """ __new__(cls: type, frameworkName: str) """
        ...


class VersioningHelper: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def MakeVersionSafeName(name:str, from_:ResourceScope, to:ResourceScope, type:Type = ...) -> str:
        """
        MakeVersionSafeName(name: str, from: ResourceScope, to: ResourceScope, type: Type) -> str
        MakeVersionSafeName(name: str, from: ResourceScope, to: ResourceScope) -> str
        """
        ...

    __all__: list = ...


