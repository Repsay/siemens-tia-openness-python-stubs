# encoding: utf-8
# module System.Transactions calls itself Transactions
# from System.Transactions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, DateTime, Enum, EventArgs, Guid, 
    IAsyncResult, IDisposable, IntPtr, MulticastDelegate, SystemException, 
    TimeSpan)

from System.Runtime.Serialization import ISerializable

from System.Security import CodeAccessPermission, IPermission

from System.Security.Permissions import (CodeAccessSecurityAttribute, 
    IUnrestrictedPermission, PermissionState)

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class Transaction(IDisposable, ISerializable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Current(self) -> Transaction:
        """
        Get: Current() -> Transaction
        Set: Current() = value
        """
        ...

    @property
    def IsolationLevel(self) -> IsolationLevel:
        """ Get: IsolationLevel(self: Transaction) -> IsolationLevel """
        ...

    @property
    def PromoterType(self) -> Guid:
        """ Get: PromoterType(self: Transaction) -> Guid """
        ...

    @property
    def TransactionInformation(self) -> TransactionInformation:
        """ Get: TransactionInformation(self: Transaction) -> TransactionInformation """
        ...


    def Clone(self) -> Transaction:
        """ Clone(self: Transaction) -> Transaction """
        ...

    def DependentClone(self, cloneOption:DependentCloneOption) -> DependentTransaction:
        """ DependentClone(self: Transaction, cloneOption: DependentCloneOption) -> DependentTransaction """
        ...

    def EnlistDurable(self, resourceManagerIdentifier, *__args) -> Enlistment:
        """
        EnlistDurable(self: Transaction, resourceManagerIdentifier: Guid, enlistmentNotification: IEnlistmentNotification, enlistmentOptions: EnlistmentOptions) -> Enlistment
        EnlistDurable(self: Transaction, resourceManagerIdentifier: Guid, singlePhaseNotification: ISinglePhaseNotification, enlistmentOptions: EnlistmentOptions) -> Enlistment
        """
        ...

    def EnlistPromotableSinglePhase(self, promotableSinglePhaseNotification:IPromotableSinglePhaseNotification, promoterType:Guid = ...) -> bool:
        """
        EnlistPromotableSinglePhase(self: Transaction, promotableSinglePhaseNotification: IPromotableSinglePhaseNotification) -> bool
        EnlistPromotableSinglePhase(self: Transaction, promotableSinglePhaseNotification: IPromotableSinglePhaseNotification, promoterType: Guid) -> bool
        """
        ...

    def EnlistVolatile(self, *__args) -> Enlistment:
        """
        EnlistVolatile(self: Transaction, enlistmentNotification: IEnlistmentNotification, enlistmentOptions: EnlistmentOptions) -> Enlistment
        EnlistVolatile(self: Transaction, singlePhaseNotification: ISinglePhaseNotification, enlistmentOptions: EnlistmentOptions) -> Enlistment
        """
        ...

    def Equals(self, obj:object) -> bool:
        """ Equals(self: Transaction, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Transaction) -> int """
        ...

    def GetPromotedToken(self) -> Array:
        """ GetPromotedToken(self: Transaction) -> Array[Byte] """
        ...

    def PromoteAndEnlistDurable(self, resourceManagerIdentifier:Guid, promotableNotification:IPromotableSinglePhaseNotification, enlistmentNotification:ISinglePhaseNotification, enlistmentOptions:EnlistmentOptions) -> Enlistment:
        """ PromoteAndEnlistDurable(self: Transaction, resourceManagerIdentifier: Guid, promotableNotification: IPromotableSinglePhaseNotification, enlistmentNotification: ISinglePhaseNotification, enlistmentOptions: EnlistmentOptions) -> Enlistment """
        ...

    def Rollback(self, e:Exception = ...): # -> 
        """ Rollback(self: Transaction)Rollback(self: Transaction, e: Exception) """
        ...

    def SetDistributedTransactionIdentifier(self, promotableNotification:IPromotableSinglePhaseNotification, distributedTransactionIdentifier:Guid): # -> 
        """ SetDistributedTransactionIdentifier(self: Transaction, promotableNotification: IPromotableSinglePhaseNotification, distributedTransactionIdentifier: Guid) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    TransactionCompleted = ...


class CommittableTransaction(Transaction, IAsyncResult): # skipped bases: <type 'IDisposable'>, <type 'ISerializable'>, <type 'object'>
    """
    CommittableTransaction()
    CommittableTransaction(timeout: TimeSpan)
    CommittableTransaction(options: TransactionOptions)
    """
    def BeginCommit(self, asyncCallback:AsyncCallback, asyncState:object) -> IAsyncResult:
        """ BeginCommit(self: CommittableTransaction, asyncCallback: AsyncCallback, asyncState: object) -> IAsyncResult """
        ...

    def Commit(self): # -> 
        """ Commit(self: CommittableTransaction) """
        ...

    def EndCommit(self, asyncResult:IAsyncResult): # -> 
        """ EndCommit(self: CommittableTransaction, asyncResult: IAsyncResult) """
        ...

    def __new__(cls, *__args:TimeSpan) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, timeout: TimeSpan)
        __new__(cls: type, options: TransactionOptions)
        """
        ...


class DependentCloneOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DependentCloneOption, values: BlockCommitUntilComplete (0), RollbackIfNotComplete (1) """
    BlockCommitUntilComplete: DependentCloneOption = ...
    RollbackIfNotComplete: DependentCloneOption = ...
    value__ = ...


class DependentTransaction(Transaction): # skipped bases: <type 'IDisposable'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    def Complete(self): # -> 
        """ Complete(self: DependentTransaction) """
        ...


class DistributedTransactionPermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """ DistributedTransactionPermission(state: PermissionState) """
    def __new__(cls, state:PermissionState) -> Self:
        """ __new__(cls: type, state: PermissionState) """
        ...


class DistributedTransactionPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DistributedTransactionPermissionAttribute(action: SecurityAction) """
    @property
    def Unrestricted(self) -> bool:
        """
        Get: Unrestricted(self: DistributedTransactionPermissionAttribute) -> bool
        Set: Unrestricted(self: DistributedTransactionPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: DistributedTransactionPermissionAttribute) -> IPermission """
        ...


class Enlistment: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def Done(self): # -> 
        """ Done(self: Enlistment) """
        ...


class EnlistmentOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EnlistmentOptions, values: EnlistDuringPrepareRequired (1), None (0) """
    EnlistDuringPrepareRequired: EnlistmentOptions = ...
    value__ = ...


class EnterpriseServicesInteropOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EnterpriseServicesInteropOption, values: Automatic (1), Full (2), None (0) """
    Automatic: EnterpriseServicesInteropOption = ...
    Full: EnterpriseServicesInteropOption = ...
    value__ = ...


class HostCurrentTransactionCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ HostCurrentTransactionCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: HostCurrentTransactionCallback, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> Transaction:
        """ EndInvoke(self: HostCurrentTransactionCallback, result: IAsyncResult) -> Transaction """
        ...

    def Invoke(self) -> Transaction:
        """ Invoke(self: HostCurrentTransactionCallback) -> Transaction """
        ...


class IDtcTransaction: # skipped bases: <type 'object'>
    """ no doc """
    def Abort(self, reason:IntPtr, retaining:int, async:int): # -> 
        """ Abort(self: IDtcTransaction, reason: IntPtr, retaining: int, async: int) """
        ...

    def Commit(self, retaining:int, commitType:int, reserved:int): # -> 
        """ Commit(self: IDtcTransaction, retaining: int, commitType: int, reserved: int) """
        ...

    def GetTransactionInfo(self, transactionInformation:IntPtr): # -> 
        """ GetTransactionInfo(self: IDtcTransaction, transactionInformation: IntPtr) """
        ...


class IEnlistmentNotification: # skipped bases: <type 'object'>
    """ no doc """
    def Commit(self, enlistment:Enlistment): # -> 
        """ Commit(self: IEnlistmentNotification, enlistment: Enlistment) """
        ...

    def InDoubt(self, enlistment:Enlistment): # -> 
        """ InDoubt(self: IEnlistmentNotification, enlistment: Enlistment) """
        ...

    def Prepare(self, preparingEnlistment:PreparingEnlistment): # -> 
        """ Prepare(self: IEnlistmentNotification, preparingEnlistment: PreparingEnlistment) """
        ...

    def Rollback(self, enlistment:Enlistment): # -> 
        """ Rollback(self: IEnlistmentNotification, enlistment: Enlistment) """
        ...


class ITransactionPromoter: # skipped bases: <type 'object'>
    """ no doc """
    def Promote(self) -> Array:
        """ Promote(self: ITransactionPromoter) -> Array[Byte] """
        ...


class IPromotableSinglePhaseNotification(ITransactionPromoter): # skipped bases: <type 'object'>
    """ no doc """
    def Initialize(self): # -> 
        """ Initialize(self: IPromotableSinglePhaseNotification) """
        ...

    def Rollback(self, singlePhaseEnlistment:SinglePhaseEnlistment): # -> 
        """ Rollback(self: IPromotableSinglePhaseNotification, singlePhaseEnlistment: SinglePhaseEnlistment) """
        ...

    def SinglePhaseCommit(self, singlePhaseEnlistment:SinglePhaseEnlistment): # -> 
        """ SinglePhaseCommit(self: IPromotableSinglePhaseNotification, singlePhaseEnlistment: SinglePhaseEnlistment) """
        ...


class ISimpleTransactionSuperior(ITransactionPromoter): # skipped bases: <type 'object'>
    """ no doc """
    def Rollback(self): # -> 
        """ Rollback(self: ISimpleTransactionSuperior) """
        ...


class ISinglePhaseNotification(IEnlistmentNotification): # skipped bases: <type 'object'>
    """ no doc """
    def SinglePhaseCommit(self, singlePhaseEnlistment:SinglePhaseEnlistment): # -> 
        """ SinglePhaseCommit(self: ISinglePhaseNotification, singlePhaseEnlistment: SinglePhaseEnlistment) """
        ...


class IsolationLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum IsolationLevel, values: Chaos (5), ReadCommitted (2), ReadUncommitted (3), RepeatableRead (1), Serializable (0), Snapshot (4), Unspecified (6) """
    Chaos: IsolationLevel = ...
    ReadCommitted: IsolationLevel = ...
    ReadUncommitted: IsolationLevel = ...
    RepeatableRead: IsolationLevel = ...
    Serializable: IsolationLevel = ...
    Snapshot: IsolationLevel = ...
    Unspecified: IsolationLevel = ...
    value__ = ...


class PreparingEnlistment(Enlistment): # skipped bases: <type 'object'>
    """ no doc """
    def ForceRollback(self, e:Exception = ...): # -> 
        """ ForceRollback(self: PreparingEnlistment)ForceRollback(self: PreparingEnlistment, e: Exception) """
        ...

    def Prepared(self): # -> 
        """ Prepared(self: PreparingEnlistment) """
        ...

    def RecoveryInformation(self) -> Array:
        """ RecoveryInformation(self: PreparingEnlistment) -> Array[Byte] """
        ...


class SinglePhaseEnlistment(Enlistment): # skipped bases: <type 'object'>
    """ no doc """
    def Aborted(self, e:Exception = ...): # -> 
        """ Aborted(self: SinglePhaseEnlistment)Aborted(self: SinglePhaseEnlistment, e: Exception) """
        ...

    def Committed(self): # -> 
        """ Committed(self: SinglePhaseEnlistment) """
        ...

    def InDoubt(self, e:Exception = ...): # -> 
        """ InDoubt(self: SinglePhaseEnlistment)InDoubt(self: SinglePhaseEnlistment, e: Exception) """
        ...


class SubordinateTransaction(Transaction): # skipped bases: <type 'IDisposable'>, <type 'ISerializable'>, <type 'object'>
    """ SubordinateTransaction(isoLevel: IsolationLevel, superior: ISimpleTransactionSuperior) """
    def __new__(cls, isoLevel:IsolationLevel, superior:ISimpleTransactionSuperior) -> Self:
        """ __new__(cls: type, isoLevel: IsolationLevel, superior: ISimpleTransactionSuperior) """
        ...


class TransactionException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TransactionException()
    TransactionException(message: str)
    TransactionException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class TransactionAbortedException(TransactionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TransactionAbortedException()
    TransactionAbortedException(message: str)
    TransactionAbortedException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class TransactionCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TransactionCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:TransactionEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: TransactionCompletedEventHandler, sender: object, e: TransactionEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: TransactionCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:TransactionEventArgs): # -> 
        """ Invoke(self: TransactionCompletedEventHandler, sender: object, e: TransactionEventArgs) """
        ...


class TransactionEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ TransactionEventArgs() """
    @property
    def Transaction(self) -> Transaction:
        """ Get: Transaction(self: TransactionEventArgs) -> Transaction """
        ...



class TransactionInDoubtException(TransactionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TransactionInDoubtException()
    TransactionInDoubtException(message: str)
    TransactionInDoubtException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class TransactionInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CreationTime(self) -> DateTime:
        """ Get: CreationTime(self: TransactionInformation) -> DateTime """
        ...

    @property
    def DistributedIdentifier(self) -> Guid:
        """ Get: DistributedIdentifier(self: TransactionInformation) -> Guid """
        ...

    @property
    def LocalIdentifier(self) -> str:
        """ Get: LocalIdentifier(self: TransactionInformation) -> str """
        ...

    @property
    def Status(self) -> TransactionStatus:
        """ Get: Status(self: TransactionInformation) -> TransactionStatus """
        ...



class TransactionInterop: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetDtcTransaction(transaction:Transaction) -> IDtcTransaction:
        """ GetDtcTransaction(transaction: Transaction) -> IDtcTransaction """
        ...

    @staticmethod
    def GetExportCookie(transaction:Transaction, whereabouts:Array) -> Array:
        """ GetExportCookie(transaction: Transaction, whereabouts: Array[Byte]) -> Array[Byte] """
        ...

    @staticmethod
    def GetTransactionFromDtcTransaction(transactionNative:IDtcTransaction) -> Transaction:
        """ GetTransactionFromDtcTransaction(transactionNative: IDtcTransaction) -> Transaction """
        ...

    @staticmethod
    def GetTransactionFromExportCookie(cookie:Array) -> Transaction:
        """ GetTransactionFromExportCookie(cookie: Array[Byte]) -> Transaction """
        ...

    @staticmethod
    def GetTransactionFromTransmitterPropagationToken(propagationToken:Array) -> Transaction:
        """ GetTransactionFromTransmitterPropagationToken(propagationToken: Array[Byte]) -> Transaction """
        ...

    @staticmethod
    def GetTransmitterPropagationToken(transaction:Transaction) -> Array:
        """ GetTransmitterPropagationToken(transaction: Transaction) -> Array[Byte] """
        ...

    @staticmethod
    def GetWhereabouts() -> Array:
        """ GetWhereabouts() -> Array[Byte] """
        ...

    PromoterTypeDtc: Guid = ...
    __all__: list = ...


class TransactionManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DefaultTimeout(self) -> TimeSpan:
        """ Get: DefaultTimeout() -> TimeSpan """
        ...

    @property
    def HostCurrentCallback(self) -> HostCurrentTransactionCallback:
        """
        Get: HostCurrentCallback() -> HostCurrentTransactionCallback
        Set: HostCurrentCallback() = value
        """
        ...

    @property
    def MaximumTimeout(self) -> TimeSpan:
        """ Get: MaximumTimeout() -> TimeSpan """
        ...


    @staticmethod
    def RecoveryComplete(resourceManagerIdentifier:Guid): # -> 
        """ RecoveryComplete(resourceManagerIdentifier: Guid) """
        ...

    @staticmethod
    def Reenlist(resourceManagerIdentifier:Guid, recoveryInformation:Array, enlistmentNotification:IEnlistmentNotification) -> Enlistment:
        """ Reenlist(resourceManagerIdentifier: Guid, recoveryInformation: Array[Byte], enlistmentNotification: IEnlistmentNotification) -> Enlistment """
        ...

    DistributedTransactionStarted = ...
    __all__: list = ...


class TransactionManagerCommunicationException(TransactionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TransactionManagerCommunicationException()
    TransactionManagerCommunicationException(message: str)
    TransactionManagerCommunicationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class TransactionOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsolationLevel(self) -> IsolationLevel:
        """
        Get: IsolationLevel(self: TransactionOptions) -> IsolationLevel
        Set: IsolationLevel(self: TransactionOptions) = value
        """
        ...

    @property
    def Timeout(self) -> TimeSpan:
        """
        Get: Timeout(self: TransactionOptions) -> TimeSpan
        Set: Timeout(self: TransactionOptions) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: TransactionOptions, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: TransactionOptions) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TransactionPromotionException(TransactionException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TransactionPromotionException()
    TransactionPromotionException(message: str)
    TransactionPromotionException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class TransactionScope(IDisposable): # skipped bases: <type 'object'>
    """
    TransactionScope()
    TransactionScope(scopeOption: TransactionScopeOption)
    TransactionScope(asyncFlowOption: TransactionScopeAsyncFlowOption)
    TransactionScope(scopeOption: TransactionScopeOption, asyncFlowOption: TransactionScopeAsyncFlowOption)
    TransactionScope(scopeOption: TransactionScopeOption, scopeTimeout: TimeSpan)
    TransactionScope(scopeOption: TransactionScopeOption, scopeTimeout: TimeSpan, asyncFlowOption: TransactionScopeAsyncFlowOption)
    TransactionScope(scopeOption: TransactionScopeOption, transactionOptions: TransactionOptions)
    TransactionScope(scopeOption: TransactionScopeOption, transactionOptions: TransactionOptions, asyncFlowOption: TransactionScopeAsyncFlowOption)
    TransactionScope(scopeOption: TransactionScopeOption, transactionOptions: TransactionOptions, interopOption: EnterpriseServicesInteropOption)
    TransactionScope(transactionToUse: Transaction)
    TransactionScope(transactionToUse: Transaction, asyncFlowOption: TransactionScopeAsyncFlowOption)
    TransactionScope(transactionToUse: Transaction, scopeTimeout: TimeSpan)
    TransactionScope(transactionToUse: Transaction, scopeTimeout: TimeSpan, asyncFlowOption: TransactionScopeAsyncFlowOption)
    TransactionScope(transactionToUse: Transaction, scopeTimeout: TimeSpan, interopOption: EnterpriseServicesInteropOption)
    """
    def Complete(self): # -> 
        """ Complete(self: TransactionScope) """
        ...


class TransactionScopeAsyncFlowOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TransactionScopeAsyncFlowOption, values: Enabled (1), Suppress (0) """
    Enabled: TransactionScopeAsyncFlowOption = ...
    Suppress: TransactionScopeAsyncFlowOption = ...
    value__ = ...


class TransactionScopeOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TransactionScopeOption, values: Required (0), RequiresNew (1), Suppress (2) """
    Required: TransactionScopeOption = ...
    RequiresNew: TransactionScopeOption = ...
    Suppress: TransactionScopeOption = ...
    value__ = ...


class TransactionStartedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TransactionStartedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:TransactionEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: TransactionStartedEventHandler, sender: object, e: TransactionEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: TransactionStartedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:TransactionEventArgs): # -> 
        """ Invoke(self: TransactionStartedEventHandler, sender: object, e: TransactionEventArgs) """
        ...


class TransactionStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TransactionStatus, values: Aborted (2), Active (0), Committed (1), InDoubt (3) """
    Aborted: TransactionStatus = ...
    Active: TransactionStatus = ...
    Committed: TransactionStatus = ...
    InDoubt: TransactionStatus = ...
    value__ = ...


# variables with complex values

