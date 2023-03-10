# encoding: utf-8
# module System.Diagnostics.PerformanceData calls itself PerformanceData
# from System.Core, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, IDisposable, Int64

"""The following names are not found in the module: field#
"""

# no functions
# classes

class CounterData: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def RawValue(self) -> Int64:
        """
        Get: RawValue(self: CounterData) -> Int64
        Set: RawValue(self: CounterData) = value
        """
        ...

    @property
    def Value(self) -> Int64:
        """
        Get: Value(self: CounterData) -> Int64
        Set: Value(self: CounterData) = value
        """
        ...


    def Decrement(self): # -> 
        """ Decrement(self: CounterData) """
        ...

    def Increment(self): # -> 
        """ Increment(self: CounterData) """
        ...

    def IncrementBy(self, value:Int64): # -> 
        """ IncrementBy(self: CounterData, value: Int64) """
        ...


class CounterSet(IDisposable): # skipped bases: <type 'object'>
    """ CounterSet(providerGuid: Guid, counterSetGuid: Guid, instanceType: CounterSetInstanceType) """
    def AddCounter(self, counterId:int, counterType:CounterType, counterName:str = ...): # -> 
        """ AddCounter(self: CounterSet, counterId: int, counterType: CounterType)AddCounter(self: CounterSet, counterId: int, counterType: CounterType, counterName: str) """
        ...

    def CreateCounterSetInstance(self, instanceName:str) -> CounterSetInstance:
        """ CreateCounterSetInstance(self: CounterSet, instanceName: str) -> CounterSetInstance """
        ...


class CounterSetInstance(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Counters(self) -> CounterSetInstanceCounterDataSet:
        """ Get: Counters(self: CounterSetInstance) -> CounterSetInstanceCounterDataSet """
        ...



class CounterSetInstanceCounterDataSet(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class CounterSetInstanceType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CounterSetInstanceType, values: GlobalAggregate (4), GlobalAggregateWithHistory (11), InstanceAggregate (22), Multiple (2), MultipleAggregate (6), Single (0) """
    GlobalAggregate: CounterSetInstanceType = ...
    GlobalAggregateWithHistory: CounterSetInstanceType = ...
    InstanceAggregate: CounterSetInstanceType = ...
    Multiple: CounterSetInstanceType = ...
    MultipleAggregate: CounterSetInstanceType = ...
    Single: CounterSetInstanceType = ...
    value__ = ...


class CounterType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CounterType, values: AverageBase (1073939458), AverageCount64 (1073874176), AverageTimer32 (805438464), Delta32 (4195328), Delta64 (4195584), ElapsedTime (807666944), LargeQueueLength (4523264), MultiTimerBase (1107494144), MultiTimerPercentageActive (574686464), MultiTimerPercentageActive100Ns (575735040), MultiTimerPercentageNotActive (591463680), MultiTimerPercentageNotActive100Ns (592512256), ObjectSpecificTimer (543229184), PercentageActive (541132032), PercentageActive100Ns (542180608), PercentageNotActive (557909248), PercentageNotActive100Ns (558957824), PrecisionObjectSpecificTimer (543622400), PrecisionSystemTimer (541525248), PrecisionTimer100Ns (542573824), QueueLength (4523008), QueueLength100Ns (5571840), QueueLengthObjectTime (6620416), RateOfCountPerSecond32 (272696320), RateOfCountPerSecond64 (272696576), RawBase32 (1073939459), RawBase64 (1073939712), RawData32 (65536), RawData64 (65792), RawDataHex32 (0), RawDataHex64 (256), RawFraction32 (537003008), RawFraction64 (537003264), SampleBase (1073939457), SampleCounter (4260864), SampleFraction (549585920) """
    AverageBase: CounterType = ...
    AverageCount64: CounterType = ...
    AverageTimer32: CounterType = ...
    Delta32: CounterType = ...
    Delta64: CounterType = ...
    ElapsedTime: CounterType = ...
    LargeQueueLength: CounterType = ...
    MultiTimerBase: CounterType = ...
    MultiTimerPercentageActive: CounterType = ...
    MultiTimerPercentageActive100Ns: CounterType = ...
    MultiTimerPercentageNotActive: CounterType = ...
    MultiTimerPercentageNotActive100Ns: CounterType = ...
    ObjectSpecificTimer: CounterType = ...
    PercentageActive: CounterType = ...
    PercentageActive100Ns: CounterType = ...
    PercentageNotActive: CounterType = ...
    PercentageNotActive100Ns: CounterType = ...
    PrecisionObjectSpecificTimer: CounterType = ...
    PrecisionSystemTimer: CounterType = ...
    PrecisionTimer100Ns: CounterType = ...
    QueueLength: CounterType = ...
    QueueLength100Ns: CounterType = ...
    QueueLengthObjectTime: CounterType = ...
    RateOfCountPerSecond32: CounterType = ...
    RateOfCountPerSecond64: CounterType = ...
    RawBase32: CounterType = ...
    RawBase64: CounterType = ...
    RawData32: CounterType = ...
    RawData64: CounterType = ...
    RawDataHex32: CounterType = ...
    RawDataHex64: CounterType = ...
    RawFraction32: CounterType = ...
    RawFraction64: CounterType = ...
    SampleBase: CounterType = ...
    SampleCounter: CounterType = ...
    SampleFraction: CounterType = ...
    value__ = ...


