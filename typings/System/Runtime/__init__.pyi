# encoding: utf-8
# module System.Runtime calls itself Runtime
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Runtime.Caching, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Runtime.Serialization.Formatters.Soap, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Runtime.Serialization, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Runtime.DurableInstancing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Runtime.Remoting, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Runtime.WindowsRuntime, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Enum, IDisposable

from System.Runtime.ConstrainedExecution import CriticalFinalizerObject

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class AssemblyTargetedPatchBandAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AssemblyTargetedPatchBandAttribute(targetedPatchBand: str) """
    @property
    def TargetedPatchBand(self) -> str:
        """ Get: TargetedPatchBand(self: AssemblyTargetedPatchBandAttribute) -> str """
        ...


    def __new__(cls, targetedPatchBand:str) -> Self:
        """ __new__(cls: type, targetedPatchBand: str) """
        ...


class GCLargeObjectHeapCompactionMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GCLargeObjectHeapCompactionMode, values: CompactOnce (2), Default (1) """
    CompactOnce: GCLargeObjectHeapCompactionMode = ...
    Default: GCLargeObjectHeapCompactionMode = ...
    value__ = ...


class GCLatencyMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum GCLatencyMode, values: Batch (0), Interactive (1), LowLatency (2), NoGCRegion (4), SustainedLowLatency (3) """
    Batch: GCLatencyMode = ...
    Interactive: GCLatencyMode = ...
    LowLatency: GCLatencyMode = ...
    NoGCRegion: GCLatencyMode = ...
    SustainedLowLatency: GCLatencyMode = ...
    value__ = ...


class GCSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsServerGC(self) -> bool:
        """ Get: IsServerGC() -> bool """
        ...

    @property
    def LargeObjectHeapCompactionMode(self) -> GCLargeObjectHeapCompactionMode:
        """
        Get: LargeObjectHeapCompactionMode() -> GCLargeObjectHeapCompactionMode
        Set: LargeObjectHeapCompactionMode() = value
        """
        ...

    @property
    def LatencyMode(self) -> GCLatencyMode:
        """
        Get: LatencyMode() -> GCLatencyMode
        Set: LatencyMode() = value
        """
        ...


    __all__: list = ...


class MemoryFailPoint(IDisposable, CriticalFinalizerObject): # skipped bases: <type 'object'>
    """ MemoryFailPoint(sizeInMegabytes: int) """
    def __new__(cls, sizeInMegabytes:int) -> Self:
        """ __new__(cls: type, sizeInMegabytes: int) """
        ...


class ProfileOptimization: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def SetProfileRoot(directoryPath:str): # -> 
        """ SetProfileRoot(directoryPath: str) """
        ...

    @staticmethod
    def StartProfile(profile:str): # -> 
        """ StartProfile(profile: str) """
        ...

    __all__: list = ...


class TargetedPatchingOptOutAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ TargetedPatchingOptOutAttribute(reason: str) """
    @property
    def Reason(self) -> str:
        """ Get: Reason(self: TargetedPatchingOptOutAttribute) -> str """
        ...


    def __new__(cls, reason:str) -> Self:
        """ __new__(cls: type, reason: str) """
        ...


# variables with complex values

