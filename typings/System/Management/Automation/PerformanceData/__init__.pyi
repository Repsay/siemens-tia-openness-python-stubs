# encoding: utf-8
# module System.Management.Automation.PerformanceData calls itself PerformanceData
# from System.Management.Automation, Version=3.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Guid, IDisposable, Int64

from System.Diagnostics.PerformanceData import (CounterSetInstanceType, 
    CounterType)

from typing import Tuple as Tuple_

"""The following names are not found in the module: field#
"""

# no functions
# classes

class CounterInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    CounterInfo(id: int, type: CounterType, name: str)
    CounterInfo(id: int, type: CounterType)
    """
    @property
    def Id(self) -> int:
        """ Get: Id(self: CounterInfo) -> int """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: CounterInfo) -> str """
        ...

    @property
    def Type(self) -> CounterType:
        """ Get: Type(self: CounterInfo) -> CounterType """
        ...



class CounterSetInstanceBase(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def GetCounterValue(self, *__args) -> Tuple_[bool, Int64]:
        """
        GetCounterValue(self: CounterSetInstanceBase, counterId: int, isNumerator: bool) -> (bool, Int64)
        GetCounterValue(self: CounterSetInstanceBase, counterName: str, isNumerator: bool) -> (bool, Int64)
        """
        ...

    def RetrieveTargetCounterIdIfValid(self, *args): #cannot find CLR method
        """ RetrieveTargetCounterIdIfValid(self: CounterSetInstanceBase, counterId: int, isNumerator: bool) -> (bool, int) """
        ...

    def SetCounterValue(self, *__args) -> bool:
        """
        SetCounterValue(self: CounterSetInstanceBase, counterId: int, counterValue: Int64, isNumerator: bool) -> bool
        SetCounterValue(self: CounterSetInstanceBase, counterName: str, counterValue: Int64, isNumerator: bool) -> bool
        """
        ...

    def UpdateCounterByValue(self, *__args) -> bool:
        """
        UpdateCounterByValue(self: CounterSetInstanceBase, counterId: int, stepAmount: Int64, isNumerator: bool) -> bool
        UpdateCounterByValue(self: CounterSetInstanceBase, counterName: str, stepAmount: Int64, isNumerator: bool) -> bool
        """
        ...

    _counterIdToTypeMapping = ...
    _counterNameToIdMapping = ...
    _counterSetRegistrarBase = ...


class CounterSetRegistrarBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CounterInfoArray(self) -> Array:
        """ Get: CounterInfoArray(self: CounterSetRegistrarBase) -> Array[CounterInfo] """
        ...

    @property
    def CounterSetId(self) -> Guid:
        """ Get: CounterSetId(self: CounterSetRegistrarBase) -> Guid """
        ...

    @property
    def CounterSetInstance(self) -> CounterSetInstanceBase:
        """ Get: CounterSetInstance(self: CounterSetRegistrarBase) -> CounterSetInstanceBase """
        ...

    @property
    def CounterSetInstType(self) -> CounterSetInstanceType:
        """ Get: CounterSetInstType(self: CounterSetRegistrarBase) -> CounterSetInstanceType """
        ...

    @property
    def CounterSetName(self) -> str:
        """ Get: CounterSetName(self: CounterSetRegistrarBase) -> str """
        ...

    @property
    def ProviderId(self) -> Guid:
        """ Get: ProviderId(self: CounterSetRegistrarBase) -> Guid """
        ...


    def CreateCounterSetInstance(self, *args): #cannot find CLR method
        """ CreateCounterSetInstance(self: CounterSetRegistrarBase) -> CounterSetInstanceBase """
        ...

    def DisposeCounterSetInstance(self): # -> 
        """ DisposeCounterSetInstance(self: CounterSetRegistrarBase) """
        ...

    _counterSetInstanceBase = ...


class PSCounterSetInstance(CounterSetInstanceBase): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ PSCounterSetInstance(counterSetRegBaseObj: CounterSetRegistrarBase) """
    _counterIdToTypeMapping = ...
    _counterNameToIdMapping = ...
    _counterSetRegistrarBase = ...


class PSCounterSetRegistrar(CounterSetRegistrarBase): # skipped bases: <type 'object'>
    """
    PSCounterSetRegistrar(providerId: Guid, counterSetId: Guid, counterSetInstType: CounterSetInstanceType, counterInfoArray: Array[CounterInfo], counterSetName: str)
    PSCounterSetRegistrar(srcPSCounterSetRegistrar: PSCounterSetRegistrar)
    """
    _counterSetInstanceBase = ...


class PSPerfCountersMgr: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Instance(self) -> PSPerfCountersMgr:
        """ Get: Instance() -> PSPerfCountersMgr """
        ...


    def AddCounterSetInstance(self, counterSetRegistrarInstance:CounterSetRegistrarBase) -> bool:
        """ AddCounterSetInstance(self: PSPerfCountersMgr, counterSetRegistrarInstance: CounterSetRegistrarBase) -> bool """
        ...

    def GetCounterSetInstanceName(self) -> str:
        """ GetCounterSetInstanceName(self: PSPerfCountersMgr) -> str """
        ...

    def IsCounterSetRegistered(self, *__args:Guid) -> Tuple_[bool, CounterSetInstanceBase]:
        """
        IsCounterSetRegistered(self: PSPerfCountersMgr, counterSetId: Guid) -> (bool, CounterSetInstanceBase)
        IsCounterSetRegistered(self: PSPerfCountersMgr, counterSetName: str) -> (bool, Guid)
        """
        ...

    def SetCounterValue(self, *__args) -> bool:
        """
        SetCounterValue(self: PSPerfCountersMgr, counterSetId: Guid, counterId: int, counterValue: Int64, isNumerator: bool) -> bool
        SetCounterValue(self: PSPerfCountersMgr, counterSetId: Guid, counterName: str, counterValue: Int64, isNumerator: bool) -> bool
        SetCounterValue(self: PSPerfCountersMgr, counterSetName: str, counterId: int, counterValue: Int64, isNumerator: bool) -> bool
        SetCounterValue(self: PSPerfCountersMgr, counterSetName: str, counterName: str, counterValue: Int64, isNumerator: bool) -> bool
        """
        ...

    def UpdateCounterByValue(self, *__args) -> bool:
        """
        UpdateCounterByValue(self: PSPerfCountersMgr, counterSetId: Guid, counterId: int, stepAmount: Int64, isNumerator: bool) -> bool
        UpdateCounterByValue(self: PSPerfCountersMgr, counterSetId: Guid, counterName: str, stepAmount: Int64, isNumerator: bool) -> bool
        UpdateCounterByValue(self: PSPerfCountersMgr, counterSetName: str, counterId: int, stepAmount: Int64, isNumerator: bool) -> bool
        UpdateCounterByValue(self: PSPerfCountersMgr, counterSetName: str, counterName: str, stepAmount: Int64, isNumerator: bool) -> bool
        """
        ...



