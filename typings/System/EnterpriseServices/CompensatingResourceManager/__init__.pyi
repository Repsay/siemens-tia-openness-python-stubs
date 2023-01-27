# encoding: utf-8
# module System.EnterpriseServices.CompensatingResourceManager calls itself CompensatingResourceManager
# from System.EnterpriseServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Attribute, Enum

from System.Collections import IEnumerable

from System.EnterpriseServices import ServicedComponent

from typing import Self

"""The following names are not found in the module: (IConfigurationAttribute, 
    _ICompensator, _IFormatLogRecords, field#)
"""

# no functions
# classes

class ApplicationCrmEnabledAttribute(IConfigurationAttribute, Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    ApplicationCrmEnabledAttribute()
    ApplicationCrmEnabledAttribute(val: bool)
    """
    @property
    def Value(self) -> bool:
        """ Get: Value(self: ApplicationCrmEnabledAttribute) -> bool """
        ...


    def __new__(cls, val:bool = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, val: bool)
        """
        ...


class Clerk: # skipped bases: <type 'object'>, <type 'object'>
    """
    Clerk(compensator: Type, description: str, flags: CompensatorOptions)
    Clerk(compensator: str, description: str, flags: CompensatorOptions)
    """
    @property
    def LogRecordCount(self) -> int:
        """ Get: LogRecordCount(self: Clerk) -> int """
        ...

    @property
    def TransactionUOW(self) -> str:
        """ Get: TransactionUOW(self: Clerk) -> str """
        ...


    def ForceLog(self): # -> 
        """ ForceLog(self: Clerk) """
        ...

    def ForceTransactionToAbort(self): # -> 
        """ ForceTransactionToAbort(self: Clerk) """
        ...

    def ForgetLogRecord(self): # -> 
        """ ForgetLogRecord(self: Clerk) """
        ...

    def WriteLogRecord(self, record:object): # -> 
        """ WriteLogRecord(self: Clerk, record: object) """
        ...


class ClerkInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ActivityId(self) -> str:
        """ Get: ActivityId(self: ClerkInfo) -> str """
        ...

    @property
    def Clerk(self) -> Clerk:
        """ Get: Clerk(self: ClerkInfo) -> Clerk """
        ...

    @property
    def Compensator(self) -> str:
        """ Get: Compensator(self: ClerkInfo) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: ClerkInfo) -> str """
        ...

    @property
    def InstanceId(self) -> str:
        """ Get: InstanceId(self: ClerkInfo) -> str """
        ...

    @property
    def TransactionUOW(self) -> str:
        """ Get: TransactionUOW(self: ClerkInfo) -> str """
        ...



class ClerkMonitor(IEnumerable): # skipped bases: <type 'object'>
    """ ClerkMonitor() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: ClerkMonitor) -> int """
        ...


    def Populate(self): # -> 
        """ Populate(self: ClerkMonitor) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class Compensator(_ICompensator, _IFormatLogRecords, ServicedComponent): # skipped bases: <type 'IRemoteDispatch'>, <type 'IDisposable'>, <type 'IServicedComponentInfo'>, <type 'IManagedObject'>, <type 'object'>
    """ Compensator() """
    @property
    def Clerk(self) -> Clerk:
        """ Get: Clerk(self: Compensator) -> Clerk """
        ...


    def AbortRecord(self, rec:LogRecord) -> bool:
        """ AbortRecord(self: Compensator, rec: LogRecord) -> bool """
        ...

    def BeginAbort(self, fRecovery:bool): # -> 
        """ BeginAbort(self: Compensator, fRecovery: bool) """
        ...

    def BeginCommit(self, fRecovery:bool): # -> 
        """ BeginCommit(self: Compensator, fRecovery: bool) """
        ...

    def BeginPrepare(self): # -> 
        """ BeginPrepare(self: Compensator) """
        ...

    def CommitRecord(self, rec:LogRecord) -> bool:
        """ CommitRecord(self: Compensator, rec: LogRecord) -> bool """
        ...

    def EndAbort(self): # -> 
        """ EndAbort(self: Compensator) """
        ...

    def EndCommit(self): # -> 
        """ EndCommit(self: Compensator) """
        ...

    def EndPrepare(self) -> bool:
        """ EndPrepare(self: Compensator) -> bool """
        ...

    def PrepareRecord(self, rec:LogRecord) -> bool:
        """ PrepareRecord(self: Compensator, rec: LogRecord) -> bool """
        ...


class CompensatorOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) CompensatorOptions, values: AbortPhase (4), AllPhases (7), CommitPhase (2), FailIfInDoubtsRemain (16), PreparePhase (1) """
    AbortPhase: CompensatorOptions = ...
    AllPhases: CompensatorOptions = ...
    CommitPhase: CompensatorOptions = ...
    FailIfInDoubtsRemain: CompensatorOptions = ...
    PreparePhase: CompensatorOptions = ...
    value__ = ...


class LogRecord: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Flags(self) -> LogRecordFlags:
        """ Get: Flags(self: LogRecord) -> LogRecordFlags """
        ...

    @property
    def Record(self) -> object:
        """ Get: Record(self: LogRecord) -> object """
        ...

    @property
    def Sequence(self) -> int:
        """ Get: Sequence(self: LogRecord) -> int """
        ...



class LogRecordFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) LogRecordFlags, values: ForgetTarget (1), ReplayInProgress (64), WrittenDuringAbort (8), WrittenDuringCommit (4), WrittenDuringPrepare (2), WrittenDuringReplay (32), WrittenDurringRecovery (16) """
    ForgetTarget: LogRecordFlags = ...
    ReplayInProgress: LogRecordFlags = ...
    value__ = ...
    WrittenDuringAbort: LogRecordFlags = ...
    WrittenDuringCommit: LogRecordFlags = ...
    WrittenDuringPrepare: LogRecordFlags = ...
    WrittenDuringReplay: LogRecordFlags = ...
    WrittenDurringRecovery: LogRecordFlags = ...


class TransactionState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TransactionState, values: Aborted (2), Active (0), Committed (1), Indoubt (3) """
    Aborted: TransactionState = ...
    Active: TransactionState = ...
    Committed: TransactionState = ...
    Indoubt: TransactionState = ...
    value__ = ...


