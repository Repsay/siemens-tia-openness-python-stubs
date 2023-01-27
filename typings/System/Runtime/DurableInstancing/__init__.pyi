# encoding: utf-8
# module System.Runtime.DurableInstancing calls itself DurableInstancing
# from System.Runtime.DurableInstancing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Action, AsyncCallback, Enum, Guid, IAsyncResult, Int64, 
    TimeSpan)

from System.Collections import IDictionary

from System.Collections.Generic import List

from System.Collections.ObjectModel import ReadOnlyCollection

from System.Xml.Linq import XName

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class InstancePersistenceException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstancePersistenceException()
    InstancePersistenceException(message: str)
    InstancePersistenceException(message: str, innerException: Exception)
    InstancePersistenceException(commandName: XName)
    InstancePersistenceException(commandName: XName, innerException: Exception)
    InstancePersistenceException(commandName: XName, message: str)
    InstancePersistenceException(commandName: XName, message: str, innerException: Exception)
    """
    @property
    def CommandName(self) -> XName:
        """ Get: CommandName(self: InstancePersistenceException) -> XName """
        ...


    SerializeObjectState = ...


class InstancePersistenceCommandException(InstancePersistenceException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstancePersistenceCommandException()
    InstancePersistenceCommandException(message: str)
    InstancePersistenceCommandException(message: str, innerException: Exception)
    InstancePersistenceCommandException(commandName: XName)
    InstancePersistenceCommandException(commandName: XName, instanceId: Guid)
    InstancePersistenceCommandException(commandName: XName, innerException: Exception)
    InstancePersistenceCommandException(commandName: XName, message: str, innerException: Exception)
    InstancePersistenceCommandException(commandName: XName, instanceId: Guid, innerException: Exception)
    InstancePersistenceCommandException(commandName: XName, instanceId: Guid, message: str, innerException: Exception)
    """
    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: InstancePersistenceCommandException) -> Guid """
        ...


    SerializeObjectState = ...


class InstanceCollisionException(InstancePersistenceCommandException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstanceCollisionException()
    InstanceCollisionException(message: str)
    InstanceCollisionException(message: str, innerException: Exception)
    InstanceCollisionException(commandName: XName, instanceId: Guid)
    InstanceCollisionException(commandName: XName, instanceId: Guid, innerException: Exception)
    InstanceCollisionException(commandName: XName, instanceId: Guid, message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InstanceCompleteException(InstancePersistenceCommandException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstanceCompleteException()
    InstanceCompleteException(message: str)
    InstanceCompleteException(message: str, innerException: Exception)
    InstanceCompleteException(commandName: XName, instanceId: Guid)
    InstanceCompleteException(commandName: XName, instanceId: Guid, innerException: Exception)
    InstanceCompleteException(commandName: XName, instanceId: Guid, message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InstanceHandle: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsValid(self) -> bool:
        """ Get: IsValid(self: InstanceHandle) -> bool """
        ...


    def Free(self): # -> 
        """ Free(self: InstanceHandle) """
        ...


class InstanceHandleConflictException(InstancePersistenceCommandException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstanceHandleConflictException()
    InstanceHandleConflictException(message: str)
    InstanceHandleConflictException(message: str, innerException: Exception)
    InstanceHandleConflictException(commandName: XName, instanceId: Guid)
    InstanceHandleConflictException(commandName: XName, instanceId: Guid, innerException: Exception)
    InstanceHandleConflictException(commandName: XName, instanceId: Guid, message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InstanceKey: # skipped bases: <type 'object'>, <type 'object'>
    """
    InstanceKey(value: Guid)
    InstanceKey(value: Guid, metadata: IDictionary[XName, InstanceValue])
    """
    @property
    def InvalidKey(self) -> InstanceKey:
        """ Get: InvalidKey() -> InstanceKey """
        ...

    @property
    def IsValid(self) -> bool:
        """ Get: IsValid(self: InstanceKey) -> bool """
        ...

    @property
    def Metadata(self) -> IDictionary:
        """ Get: Metadata(self: InstanceKey) -> IDictionary[XName, InstanceValue] """
        ...

    @property
    def Value(self) -> Guid:
        """ Get: Value(self: InstanceKey) -> Guid """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: InstanceKey, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: InstanceKey) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class InstanceKeyCollisionException(InstancePersistenceCommandException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstanceKeyCollisionException()
    InstanceKeyCollisionException(message: str)
    InstanceKeyCollisionException(message: str, innerException: Exception)
    InstanceKeyCollisionException(commandName: XName, instanceId: Guid, instanceKey: InstanceKey, conflictingInstanceId: Guid)
    InstanceKeyCollisionException(commandName: XName, instanceId: Guid, instanceKey: InstanceKey, conflictingInstanceId: Guid, innerException: Exception)
    InstanceKeyCollisionException(commandName: XName, instanceId: Guid, instanceKey: InstanceKey, conflictingInstanceId: Guid, message: str, innerException: Exception)
    """
    @property
    def ConflictingInstanceId(self) -> Guid:
        """ Get: ConflictingInstanceId(self: InstanceKeyCollisionException) -> Guid """
        ...

    @property
    def InstanceKey(self) -> InstanceKey:
        """ Get: InstanceKey(self: InstanceKeyCollisionException) -> InstanceKey """
        ...


    SerializeObjectState = ...


class InstanceKeyCompleteException(InstancePersistenceCommandException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstanceKeyCompleteException()
    InstanceKeyCompleteException(message: str)
    InstanceKeyCompleteException(message: str, innerException: Exception)
    InstanceKeyCompleteException(commandName: XName, instanceKey: InstanceKey)
    InstanceKeyCompleteException(commandName: XName, instanceKey: InstanceKey, innerException: Exception)
    InstanceKeyCompleteException(commandName: XName, instanceId: Guid, instanceKey: InstanceKey, message: str, innerException: Exception)
    """
    @property
    def InstanceKey(self) -> InstanceKey:
        """ Get: InstanceKey(self: InstanceKeyCompleteException) -> InstanceKey """
        ...


    SerializeObjectState = ...


class InstanceKeyNotReadyException(InstancePersistenceCommandException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstanceKeyNotReadyException()
    InstanceKeyNotReadyException(message: str)
    InstanceKeyNotReadyException(message: str, innerException: Exception)
    InstanceKeyNotReadyException(commandName: XName, instanceKey: InstanceKey)
    InstanceKeyNotReadyException(commandName: XName, instanceKey: InstanceKey, innerException: Exception)
    InstanceKeyNotReadyException(commandName: XName, instanceId: Guid, instanceKey: InstanceKey, message: str, innerException: Exception)
    """
    @property
    def InstanceKey(self) -> InstanceKey:
        """ Get: InstanceKey(self: InstanceKeyNotReadyException) -> InstanceKey """
        ...


    SerializeObjectState = ...


class InstanceKeyState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InstanceKeyState, values: Associated (1), Completed (2), Unknown (0) """
    Associated: InstanceKeyState = ...
    Completed: InstanceKeyState = ...
    Unknown: InstanceKeyState = ...
    value__ = ...


class InstanceKeyView: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def InstanceKey(self) -> Guid:
        """ Get: InstanceKey(self: InstanceKeyView) -> Guid """
        ...

    @property
    def InstanceKeyMetadata(self) -> IDictionary:
        """ Get: InstanceKeyMetadata(self: InstanceKeyView) -> IDictionary[XName, InstanceValue] """
        ...

    @property
    def InstanceKeyMetadataConsistency(self) -> InstanceValueConsistency:
        """ Get: InstanceKeyMetadataConsistency(self: InstanceKeyView) -> InstanceValueConsistency """
        ...

    @property
    def InstanceKeyState(self) -> InstanceKeyState:
        """ Get: InstanceKeyState(self: InstanceKeyView) -> InstanceKeyState """
        ...



class InstanceLockedException(InstancePersistenceCommandException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstanceLockedException()
    InstanceLockedException(message: str)
    InstanceLockedException(message: str, innerException: Exception)
    InstanceLockedException(commandName: XName, instanceId: Guid)
    InstanceLockedException(commandName: XName, instanceId: Guid, innerException: Exception)
    InstanceLockedException(commandName: XName, instanceId: Guid, message: str, innerException: Exception)
    InstanceLockedException(commandName: XName, instanceId: Guid, instanceOwnerId: Guid, serializableInstanceOwnerMetadata: IDictionary[XName, object])
    InstanceLockedException(commandName: XName, instanceId: Guid, instanceOwnerId: Guid, serializableInstanceOwnerMetadata: IDictionary[XName, object], innerException: Exception)
    InstanceLockedException(commandName: XName, instanceId: Guid, instanceOwnerId: Guid, serializableInstanceOwnerMetadata: IDictionary[XName, object], message: str, innerException: Exception)
    """
    @property
    def InstanceOwnerId(self) -> Guid:
        """ Get: InstanceOwnerId(self: InstanceLockedException) -> Guid """
        ...

    @property
    def SerializableInstanceOwnerMetadata(self) -> IDictionary:
        """ Get: SerializableInstanceOwnerMetadata(self: InstanceLockedException) -> IDictionary[XName, object] """
        ...


    SerializeObjectState = ...


class InstanceLockLostException(InstancePersistenceCommandException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstanceLockLostException()
    InstanceLockLostException(message: str)
    InstanceLockLostException(message: str, innerException: Exception)
    InstanceLockLostException(commandName: XName, instanceId: Guid)
    InstanceLockLostException(commandName: XName, instanceId: Guid, innerException: Exception)
    InstanceLockLostException(commandName: XName, instanceId: Guid, message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InstanceStoreQueryResult: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class InstanceLockQueryResult(InstanceStoreQueryResult): # skipped bases: <type 'object'>
    """
    InstanceLockQueryResult()
    InstanceLockQueryResult(instanceId: Guid, instanceOwnerId: Guid)
    InstanceLockQueryResult(instanceOwnerIds: IDictionary[Guid, Guid])
    """
    @property
    def InstanceOwnerIds(self) -> IDictionary:
        """ Get: InstanceOwnerIds(self: InstanceLockQueryResult) -> IDictionary[Guid, Guid] """
        ...


    def __new__(cls, *__args:IDictionary) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, instanceId: Guid, instanceOwnerId: Guid)
        __new__(cls: type, instanceOwnerIds: IDictionary[Guid, Guid])
        """
        ...


class InstanceNotReadyException(InstancePersistenceCommandException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstanceNotReadyException()
    InstanceNotReadyException(message: str)
    InstanceNotReadyException(message: str, innerException: Exception)
    InstanceNotReadyException(commandName: XName, instanceId: Guid)
    InstanceNotReadyException(commandName: XName, instanceId: Guid, innerException: Exception)
    InstanceNotReadyException(commandName: XName, instanceId: Guid, message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InstanceOwner: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def InstanceOwnerId(self) -> Guid:
        """ Get: InstanceOwnerId(self: InstanceOwner) -> Guid """
        ...



class InstanceOwnerException(InstancePersistenceException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstanceOwnerException()
    InstanceOwnerException(message: str)
    InstanceOwnerException(message: str, innerException: Exception)
    InstanceOwnerException(commandName: XName, instanceOwnerId: Guid)
    InstanceOwnerException(commandName: XName, instanceOwnerId: Guid, innerException: Exception)
    InstanceOwnerException(commandName: XName, instanceOwnerId: Guid, message: str, innerException: Exception)
    """
    @property
    def InstanceOwnerId(self) -> Guid:
        """ Get: InstanceOwnerId(self: InstanceOwnerException) -> Guid """
        ...


    SerializeObjectState = ...


class InstanceOwnerQueryResult(InstanceStoreQueryResult): # skipped bases: <type 'object'>
    """
    InstanceOwnerQueryResult()
    InstanceOwnerQueryResult(instanceOwnerId: Guid, metadata: IDictionary[XName, InstanceValue])
    InstanceOwnerQueryResult(instanceOwners: IDictionary[Guid, IDictionary[XName, InstanceValue]])
    """
    @property
    def InstanceOwners(self) -> IDictionary:
        """ Get: InstanceOwners(self: InstanceOwnerQueryResult) -> IDictionary[Guid, IDictionary[XName, InstanceValue]] """
        ...


    def __new__(cls, *__args:IDictionary) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, instanceOwnerId: Guid, metadata: IDictionary[XName, InstanceValue])
        __new__(cls: type, instanceOwners: IDictionary[Guid, IDictionary[XName, InstanceValue]])
        """
        ...


class InstancePersistenceCommand: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AutomaticallyAcquiringLock(self):
        ...

    @property
    def IsTransactionEnlistmentOptional(self):
        ...

    @property
    def Name(self) -> XName:
        """ Get: Name(self: InstancePersistenceCommand) -> XName """
        ...


    def Validate(self, *args): #cannot find CLR method
        """ Validate(self: InstancePersistenceCommand, view: InstanceView) """
        ...


class InstancePersistenceContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def InstanceHandle(self) -> InstanceHandle:
        """ Get: InstanceHandle(self: InstancePersistenceContext) -> InstanceHandle """
        ...

    @property
    def InstanceVersion(self) -> Int64:
        """ Get: InstanceVersion(self: InstancePersistenceContext) -> Int64 """
        ...

    @property
    def InstanceView(self) -> InstanceView:
        """ Get: InstanceView(self: InstancePersistenceContext) -> InstanceView """
        ...

    @property
    def LockToken(self) -> Guid:
        """ Get: LockToken(self: InstancePersistenceContext) -> Guid """
        ...

    @property
    def UserContext(self) -> object:
        """ Get: UserContext(self: InstancePersistenceContext) -> object """
        ...


    def AssociatedInstanceKey(self, key:Guid): # -> 
        """ AssociatedInstanceKey(self: InstancePersistenceContext, key: Guid) """
        ...

    def BeginBindReclaimedLock(self, instanceVersion:Int64, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginBindReclaimedLock(self: InstancePersistenceContext, instanceVersion: Int64, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginExecute(self, command:InstancePersistenceCommand, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginExecute(self: InstancePersistenceContext, command: InstancePersistenceCommand, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BindAcquiredLock(self, instanceVersion:Int64): # -> 
        """ BindAcquiredLock(self: InstancePersistenceContext, instanceVersion: Int64) """
        ...

    def BindEvent(self, persistenceEvent:InstancePersistenceEvent): # -> 
        """ BindEvent(self: InstancePersistenceContext, persistenceEvent: InstancePersistenceEvent) """
        ...

    def BindInstance(self, instanceId:Guid): # -> 
        """ BindInstance(self: InstancePersistenceContext, instanceId: Guid) """
        ...

    def BindInstanceOwner(self, instanceOwnerId:Guid, lockToken:Guid): # -> 
        """ BindInstanceOwner(self: InstancePersistenceContext, instanceOwnerId: Guid, lockToken: Guid) """
        ...

    def BindReclaimedLock(self, instanceVersion:Int64, timeout:TimeSpan): # -> 
        """ BindReclaimedLock(self: InstancePersistenceContext, instanceVersion: Int64, timeout: TimeSpan) """
        ...

    def CompletedInstance(self): # -> 
        """ CompletedInstance(self: InstancePersistenceContext) """
        ...

    def CompletedInstanceKey(self, key:Guid): # -> 
        """ CompletedInstanceKey(self: InstancePersistenceContext, key: Guid) """
        ...

    def CreateBindReclaimedLockException(self, instanceVersion:Int64) -> Exception:
        """ CreateBindReclaimedLockException(self: InstancePersistenceContext, instanceVersion: Int64) -> Exception """
        ...

    def EndBindReclaimedLock(self, result:IAsyncResult): # -> 
        """ EndBindReclaimedLock(self: InstancePersistenceContext, result: IAsyncResult) """
        ...

    def EndExecute(self, result:IAsyncResult): # -> 
        """ EndExecute(self: InstancePersistenceContext, result: IAsyncResult) """
        ...

    def Execute(self, command:InstancePersistenceCommand, timeout:TimeSpan): # -> 
        """ Execute(self: InstancePersistenceContext, command: InstancePersistenceCommand, timeout: TimeSpan) """
        ...

    def LoadedInstance(self, state:InstanceState, instanceData:IDictionary, instanceMetadata:IDictionary, associatedInstanceKeyMetadata:IDictionary, completedInstanceKeyMetadata:IDictionary): # -> 
        """ LoadedInstance(self: InstancePersistenceContext, state: InstanceState, instanceData: IDictionary[XName, InstanceValue], instanceMetadata: IDictionary[XName, InstanceValue], associatedInstanceKeyMetadata: IDictionary[Guid, IDictionary[XName, InstanceValue]], completedInstanceKeyMetadata: IDictionary[Guid, IDictionary[XName, InstanceValue]]) """
        ...

    def PersistedInstance(self, data:IDictionary): # -> 
        """ PersistedInstance(self: InstancePersistenceContext, data: IDictionary[XName, InstanceValue]) """
        ...

    def QueriedInstanceStore(self, queryResult:InstanceStoreQueryResult): # -> 
        """ QueriedInstanceStore(self: InstancePersistenceContext, queryResult: InstanceStoreQueryResult) """
        ...

    def ReadInstanceKeyMetadata(self, key:Guid, metadata:IDictionary, complete:bool): # -> 
        """ ReadInstanceKeyMetadata(self: InstancePersistenceContext, key: Guid, metadata: IDictionary[XName, InstanceValue], complete: bool) """
        ...

    def ReadInstanceMetadata(self, metadata:IDictionary, complete:bool): # -> 
        """ ReadInstanceMetadata(self: InstancePersistenceContext, metadata: IDictionary[XName, InstanceValue], complete: bool) """
        ...

    def ReadInstanceOwnerMetadata(self, metadata:IDictionary, complete:bool): # -> 
        """ ReadInstanceOwnerMetadata(self: InstancePersistenceContext, metadata: IDictionary[XName, InstanceValue], complete: bool) """
        ...

    def SetCancellationHandler(self, cancellationHandler:Action): # -> 
        """ SetCancellationHandler(self: InstancePersistenceContext, cancellationHandler: Action[InstancePersistenceContext]) """
        ...

    def UnassociatedInstanceKey(self, key:Guid): # -> 
        """ UnassociatedInstanceKey(self: InstancePersistenceContext, key: Guid) """
        ...

    def WroteInstanceKeyMetadataValue(self, key:Guid, name:XName, value:InstanceValue): # -> 
        """ WroteInstanceKeyMetadataValue(self: InstancePersistenceContext, key: Guid, name: XName, value: InstanceValue) """
        ...

    def WroteInstanceMetadataValue(self, name:XName, value:InstanceValue): # -> 
        """ WroteInstanceMetadataValue(self: InstancePersistenceContext, name: XName, value: InstanceValue) """
        ...

    def WroteInstanceOwnerMetadataValue(self, name:XName, value:InstanceValue): # -> 
        """ WroteInstanceOwnerMetadataValue(self: InstancePersistenceContext, name: XName, value: InstanceValue) """
        ...


class InstancePersistenceEvent: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Name(self) -> XName:
        """ Get: Name(self: InstancePersistenceEvent) -> XName """
        ...


    def Equals(self, *__args:InstancePersistenceEvent) -> bool:
        """
        Equals(self: InstancePersistenceEvent, persistenceEvent: InstancePersistenceEvent) -> bool
        Equals(self: InstancePersistenceEvent, obj: object) -> bool
        """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: InstancePersistenceEvent) -> int """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        ...


class InstanceState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InstanceState, values: Completed (3), Initialized (2), Uninitialized (1), Unknown (0) """
    Completed: InstanceState = ...
    Initialized: InstanceState = ...
    Uninitialized: InstanceState = ...
    Unknown: InstanceState = ...
    value__ = ...


class InstanceStore: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DefaultInstanceOwner(self) -> InstanceOwner:
        """
        Get: DefaultInstanceOwner(self: InstanceStore) -> InstanceOwner
        Set: DefaultInstanceOwner(self: InstanceStore) = value
        """
        ...


    def BeginExecute(self, handle:InstanceHandle, command:InstancePersistenceCommand, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginExecute(self: InstanceStore, handle: InstanceHandle, command: InstancePersistenceCommand, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginTryCommand(self, *args): #cannot find CLR method
        """ BeginTryCommand(self: InstanceStore, context: InstancePersistenceContext, command: InstancePersistenceCommand, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginWaitForEvents(self, handle:InstanceHandle, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginWaitForEvents(self: InstanceStore, handle: InstanceHandle, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def CreateInstanceHandle(self, *__args:InstanceOwner) -> InstanceHandle:
        """
        CreateInstanceHandle(self: InstanceStore) -> InstanceHandle
        CreateInstanceHandle(self: InstanceStore, owner: InstanceOwner, instanceId: Guid) -> InstanceHandle
        CreateInstanceHandle(self: InstanceStore, owner: InstanceOwner) -> InstanceHandle
        CreateInstanceHandle(self: InstanceStore, instanceId: Guid) -> InstanceHandle
        """
        ...

    def EndExecute(self, result:IAsyncResult) -> InstanceView:
        """ EndExecute(self: InstanceStore, result: IAsyncResult) -> InstanceView """
        ...

    def EndTryCommand(self, *args): #cannot find CLR method
        """ EndTryCommand(self: InstanceStore, result: IAsyncResult) -> bool """
        ...

    def EndWaitForEvents(self, result:IAsyncResult) -> List:
        """ EndWaitForEvents(self: InstanceStore, result: IAsyncResult) -> List[InstancePersistenceEvent] """
        ...

    def Execute(self, handle:InstanceHandle, command:InstancePersistenceCommand, timeout:TimeSpan) -> InstanceView:
        """ Execute(self: InstanceStore, handle: InstanceHandle, command: InstancePersistenceCommand, timeout: TimeSpan) -> InstanceView """
        ...

    def GetEvents(self, *args): #cannot find CLR method
        """ GetEvents(self: InstanceStore, owner: InstanceOwner) -> Array[InstancePersistenceEvent] """
        ...

    def GetInstanceOwners(self, *args): #cannot find CLR method
        """ GetInstanceOwners(self: InstanceStore) -> Array[InstanceOwner] """
        ...

    def OnFreeInstanceHandle(self, *args): #cannot find CLR method
        """ OnFreeInstanceHandle(self: InstanceStore, instanceHandle: InstanceHandle, userContext: object) """
        ...

    def OnNewInstanceHandle(self, *args): #cannot find CLR method
        """ OnNewInstanceHandle(self: InstanceStore, instanceHandle: InstanceHandle) -> object """
        ...

    def ResetEvent(self, *args): #cannot find CLR method
        """ ResetEvent(self: InstanceStore, persistenceEvent: InstancePersistenceEvent, owner: InstanceOwner) """
        ...

    def SignalEvent(self, *args): #cannot find CLR method
        """ SignalEvent(self: InstanceStore, persistenceEvent: InstancePersistenceEvent, owner: InstanceOwner) """
        ...

    def TryCommand(self, *args): #cannot find CLR method
        """ TryCommand(self: InstanceStore, context: InstancePersistenceContext, command: InstancePersistenceCommand, timeout: TimeSpan) -> bool """
        ...

    def WaitForEvents(self, handle:InstanceHandle, timeout:TimeSpan) -> List:
        """ WaitForEvents(self: InstanceStore, handle: InstanceHandle, timeout: TimeSpan) -> List[InstancePersistenceEvent] """
        ...


class InstanceValue: # skipped bases: <type 'object'>, <type 'object'>
    """
    InstanceValue(value: object)
    InstanceValue(value: object, options: InstanceValueOptions)
    """
    @property
    def DeletedValue(self) -> InstanceValue:
        """ Get: DeletedValue() -> InstanceValue """
        ...

    @property
    def IsDeletedValue(self) -> bool:
        """ Get: IsDeletedValue(self: InstanceValue) -> bool """
        ...

    @property
    def Options(self) -> InstanceValueOptions:
        """ Get: Options(self: InstanceValue) -> InstanceValueOptions """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: InstanceValue) -> object """
        ...




class InstanceValueConsistency(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) InstanceValueConsistency, values: InDoubt (1), None (0), Partial (2) """
    InDoubt: InstanceValueConsistency = ...
    Partial: InstanceValueConsistency = ...
    value__ = ...


class InstanceValueOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) InstanceValueOptions, values: None (0), Optional (1), WriteOnly (2) """
    Optional: InstanceValueOptions = ...
    value__ = ...
    WriteOnly: InstanceValueOptions = ...


class InstanceView: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def InstanceData(self) -> IDictionary:
        """ Get: InstanceData(self: InstanceView) -> IDictionary[XName, InstanceValue] """
        ...

    @property
    def InstanceDataConsistency(self) -> InstanceValueConsistency:
        """ Get: InstanceDataConsistency(self: InstanceView) -> InstanceValueConsistency """
        ...

    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: InstanceView) -> Guid """
        ...

    @property
    def InstanceKeys(self) -> IDictionary:
        """ Get: InstanceKeys(self: InstanceView) -> IDictionary[Guid, InstanceKeyView] """
        ...

    @property
    def InstanceKeysConsistency(self) -> InstanceValueConsistency:
        """ Get: InstanceKeysConsistency(self: InstanceView) -> InstanceValueConsistency """
        ...

    @property
    def InstanceMetadata(self) -> IDictionary:
        """ Get: InstanceMetadata(self: InstanceView) -> IDictionary[XName, InstanceValue] """
        ...

    @property
    def InstanceMetadataConsistency(self) -> InstanceValueConsistency:
        """ Get: InstanceMetadataConsistency(self: InstanceView) -> InstanceValueConsistency """
        ...

    @property
    def InstanceOwner(self) -> InstanceOwner:
        """ Get: InstanceOwner(self: InstanceView) -> InstanceOwner """
        ...

    @property
    def InstanceOwnerMetadata(self) -> IDictionary:
        """ Get: InstanceOwnerMetadata(self: InstanceView) -> IDictionary[XName, InstanceValue] """
        ...

    @property
    def InstanceOwnerMetadataConsistency(self) -> InstanceValueConsistency:
        """ Get: InstanceOwnerMetadataConsistency(self: InstanceView) -> InstanceValueConsistency """
        ...

    @property
    def InstanceState(self) -> InstanceState:
        """ Get: InstanceState(self: InstanceView) -> InstanceState """
        ...

    @property
    def InstanceStoreQueryResults(self) -> ReadOnlyCollection:
        """ Get: InstanceStoreQueryResults(self: InstanceView) -> ReadOnlyCollection[InstanceStoreQueryResult] """
        ...

    @property
    def IsBoundToInstance(self) -> bool:
        """ Get: IsBoundToInstance(self: InstanceView) -> bool """
        ...

    @property
    def IsBoundToInstanceOwner(self) -> bool:
        """ Get: IsBoundToInstanceOwner(self: InstanceView) -> bool """
        ...

    @property
    def IsBoundToLock(self) -> bool:
        """ Get: IsBoundToLock(self: InstanceView) -> bool """
        ...



