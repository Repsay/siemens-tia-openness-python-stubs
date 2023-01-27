# encoding: utf-8
# module Microsoft.PowerShell.Commands.GetCounter calls itself GetCounter
# from Microsoft.PowerShell.Commands.Diagnostics, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, DateTime, UInt32, UInt64

from System.Collections.Specialized import StringCollection

from System.Diagnostics import (PerformanceCounterCategoryType, 
    PerformanceCounterType)


# no functions
# classes

class CounterFileInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def NewestRecord(self) -> DateTime:
        """ Get: NewestRecord(self: CounterFileInfo) -> DateTime """
        ...

    @property
    def OldestRecord(self) -> DateTime:
        """ Get: OldestRecord(self: CounterFileInfo) -> DateTime """
        ...

    @property
    def SampleCount(self) -> UInt32:
        """ Get: SampleCount(self: CounterFileInfo) -> UInt32 """
        ...



class CounterSet: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CounterSetName(self) -> str:
        """ Get: CounterSetName(self: CounterSet) -> str """
        ...

    @property
    def CounterSetType(self) -> PerformanceCounterCategoryType:
        """ Get: CounterSetType(self: CounterSet) -> PerformanceCounterCategoryType """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: CounterSet) -> str """
        ...

    @property
    def MachineName(self) -> str:
        """ Get: MachineName(self: CounterSet) -> str """
        ...

    @property
    def Paths(self) -> StringCollection:
        """ Get: Paths(self: CounterSet) -> StringCollection """
        ...

    @property
    def PathsWithInstances(self) -> StringCollection:
        """ Get: PathsWithInstances(self: CounterSet) -> StringCollection """
        ...



class PerformanceCounterSample: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CookedValue(self) -> float:
        """
        Get: CookedValue(self: PerformanceCounterSample) -> float
        Set: CookedValue(self: PerformanceCounterSample) = value
        """
        ...

    @property
    def CounterType(self) -> PerformanceCounterType:
        """
        Get: CounterType(self: PerformanceCounterSample) -> PerformanceCounterType
        Set: CounterType(self: PerformanceCounterSample) = value
        """
        ...

    @property
    def DefaultScale(self) -> UInt32:
        """
        Get: DefaultScale(self: PerformanceCounterSample) -> UInt32
        Set: DefaultScale(self: PerformanceCounterSample) = value
        """
        ...

    @property
    def InstanceName(self) -> str:
        """
        Get: InstanceName(self: PerformanceCounterSample) -> str
        Set: InstanceName(self: PerformanceCounterSample) = value
        """
        ...

    @property
    def MultipleCount(self) -> UInt32:
        """
        Get: MultipleCount(self: PerformanceCounterSample) -> UInt32
        Set: MultipleCount(self: PerformanceCounterSample) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: PerformanceCounterSample) -> str
        Set: Path(self: PerformanceCounterSample) = value
        """
        ...

    @property
    def RawValue(self) -> UInt64:
        """
        Get: RawValue(self: PerformanceCounterSample) -> UInt64
        Set: RawValue(self: PerformanceCounterSample) = value
        """
        ...

    @property
    def SecondValue(self) -> UInt64:
        """
        Get: SecondValue(self: PerformanceCounterSample) -> UInt64
        Set: SecondValue(self: PerformanceCounterSample) = value
        """
        ...

    @property
    def Status(self) -> UInt32:
        """
        Get: Status(self: PerformanceCounterSample) -> UInt32
        Set: Status(self: PerformanceCounterSample) = value
        """
        ...

    @property
    def TimeBase(self) -> UInt64:
        """
        Get: TimeBase(self: PerformanceCounterSample) -> UInt64
        Set: TimeBase(self: PerformanceCounterSample) = value
        """
        ...

    @property
    def Timestamp(self) -> DateTime:
        """
        Get: Timestamp(self: PerformanceCounterSample) -> DateTime
        Set: Timestamp(self: PerformanceCounterSample) = value
        """
        ...

    @property
    def Timestamp100NSec(self) -> UInt64:
        """
        Get: Timestamp100NSec(self: PerformanceCounterSample) -> UInt64
        Set: Timestamp100NSec(self: PerformanceCounterSample) = value
        """
        ...



class PerformanceCounterSampleSet: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CounterSamples(self) -> Array:
        """
        Get: CounterSamples(self: PerformanceCounterSampleSet) -> Array[PerformanceCounterSample]
        Set: CounterSamples(self: PerformanceCounterSampleSet) = value
        """
        ...

    @property
    def Timestamp(self) -> DateTime:
        """
        Get: Timestamp(self: PerformanceCounterSampleSet) -> DateTime
        Set: Timestamp(self: PerformanceCounterSampleSet) = value
        """
        ...



