# encoding: utf-8
# module System.Activities.DurableInstancing calls itself DurableInstancing
# from System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Activities.DurableInstancing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, Guid, TimeSpan

from System.Collections import ICollection, IDictionary, IEnumerable

from System.Collections.Generic import List

from System.Runtime.DurableInstancing import (InstancePersistenceCommand, 
    InstancePersistenceEvent, InstanceStore, InstanceStoreQueryResult)

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ActivatableWorkflowsQueryResult(InstanceStoreQueryResult): # skipped bases: <type 'object'>
    """
    ActivatableWorkflowsQueryResult()
    ActivatableWorkflowsQueryResult(parameters: IDictionary[XName, object])
    ActivatableWorkflowsQueryResult(parameters: IEnumerable[IDictionary[XName, object]])
    """
    @property
    def ActivationParameters(self) -> List:
        """ Get: ActivationParameters(self: ActivatableWorkflowsQueryResult) -> List[IDictionary[XName, object]] """
        ...


    def __new__(cls, parameters:IDictionary = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parameters: IDictionary[XName, object])
        __new__(cls: type, parameters: IEnumerable[IDictionary[XName, object]])
        """
        ...


class CreateWorkflowOwnerCommand(InstancePersistenceCommand): # skipped bases: <type 'object'>
    """ CreateWorkflowOwnerCommand() """
    @property
    def InstanceOwnerMetadata(self) -> IDictionary:
        """ Get: InstanceOwnerMetadata(self: CreateWorkflowOwnerCommand) -> IDictionary[XName, InstanceValue] """
        ...



class CreateWorkflowOwnerWithIdentityCommand(InstancePersistenceCommand): # skipped bases: <type 'object'>
    """ CreateWorkflowOwnerWithIdentityCommand() """
    @property
    def InstanceOwnerMetadata(self) -> IDictionary:
        """ Get: InstanceOwnerMetadata(self: CreateWorkflowOwnerWithIdentityCommand) -> IDictionary[XName, InstanceValue] """
        ...



class DeleteWorkflowOwnerCommand(InstancePersistenceCommand): # skipped bases: <type 'object'>
    """ DeleteWorkflowOwnerCommand() """
    pass

class HasActivatableWorkflowEvent(InstancePersistenceEvent): # skipped bases: <type 'IEquatable[InstancePersistenceEvent]'>, <type 'object'>
    """ HasActivatableWorkflowEvent() """
    pass

class HasRunnableWorkflowEvent(InstancePersistenceEvent): # skipped bases: <type 'IEquatable[InstancePersistenceEvent]'>, <type 'object'>
    """ HasRunnableWorkflowEvent() """
    pass

class InstanceCompletionAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InstanceCompletionAction, values: DeleteAll (1), DeleteNothing (0) """
    DeleteAll: InstanceCompletionAction = ...
    DeleteNothing: InstanceCompletionAction = ...
    value__ = ...


class InstanceEncodingOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InstanceEncodingOption, values: GZip (1), None (0) """
    GZip: InstanceEncodingOption = ...
    value__ = ...


class InstanceLockedExceptionAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum InstanceLockedExceptionAction, values: AggressiveRetry (2), BasicRetry (1), NoRetry (0) """
    AggressiveRetry: InstanceLockedExceptionAction = ...
    BasicRetry: InstanceLockedExceptionAction = ...
    NoRetry: InstanceLockedExceptionAction = ...
    value__ = ...


class LoadWorkflowByInstanceKeyCommand(InstancePersistenceCommand): # skipped bases: <type 'object'>
    """ LoadWorkflowByInstanceKeyCommand() """
    @property
    def AcceptUninitializedInstance(self) -> bool:
        """
        Get: AcceptUninitializedInstance(self: LoadWorkflowByInstanceKeyCommand) -> bool
        Set: AcceptUninitializedInstance(self: LoadWorkflowByInstanceKeyCommand) = value
        """
        ...

    @property
    def AssociateInstanceKeyToInstanceId(self) -> Guid:
        """
        Get: AssociateInstanceKeyToInstanceId(self: LoadWorkflowByInstanceKeyCommand) -> Guid
        Set: AssociateInstanceKeyToInstanceId(self: LoadWorkflowByInstanceKeyCommand) = value
        """
        ...

    @property
    def InstanceKeysToAssociate(self) -> IDictionary:
        """ Get: InstanceKeysToAssociate(self: LoadWorkflowByInstanceKeyCommand) -> IDictionary[Guid, IDictionary[XName, InstanceValue]] """
        ...

    @property
    def LookupInstanceKey(self) -> Guid:
        """
        Get: LookupInstanceKey(self: LoadWorkflowByInstanceKeyCommand) -> Guid
        Set: LookupInstanceKey(self: LoadWorkflowByInstanceKeyCommand) = value
        """
        ...



class LoadWorkflowCommand(InstancePersistenceCommand): # skipped bases: <type 'object'>
    """ LoadWorkflowCommand() """
    @property
    def AcceptUninitializedInstance(self) -> bool:
        """
        Get: AcceptUninitializedInstance(self: LoadWorkflowCommand) -> bool
        Set: AcceptUninitializedInstance(self: LoadWorkflowCommand) = value
        """
        ...



class QueryActivatableWorkflowsCommand(InstancePersistenceCommand): # skipped bases: <type 'object'>
    """ QueryActivatableWorkflowsCommand() """
    pass

class SaveWorkflowCommand(InstancePersistenceCommand): # skipped bases: <type 'object'>
    """ SaveWorkflowCommand() """
    @property
    def CompleteInstance(self) -> bool:
        """
        Get: CompleteInstance(self: SaveWorkflowCommand) -> bool
        Set: CompleteInstance(self: SaveWorkflowCommand) = value
        """
        ...

    @property
    def InstanceData(self) -> IDictionary:
        """ Get: InstanceData(self: SaveWorkflowCommand) -> IDictionary[XName, InstanceValue] """
        ...

    @property
    def InstanceKeyMetadataChanges(self) -> IDictionary:
        """ Get: InstanceKeyMetadataChanges(self: SaveWorkflowCommand) -> IDictionary[Guid, IDictionary[XName, InstanceValue]] """
        ...

    @property
    def InstanceKeysToAssociate(self) -> IDictionary:
        """ Get: InstanceKeysToAssociate(self: SaveWorkflowCommand) -> IDictionary[Guid, IDictionary[XName, InstanceValue]] """
        ...

    @property
    def InstanceKeysToComplete(self) -> ICollection:
        """ Get: InstanceKeysToComplete(self: SaveWorkflowCommand) -> ICollection[Guid] """
        ...

    @property
    def InstanceKeysToFree(self) -> ICollection:
        """ Get: InstanceKeysToFree(self: SaveWorkflowCommand) -> ICollection[Guid] """
        ...

    @property
    def InstanceMetadataChanges(self) -> IDictionary:
        """ Get: InstanceMetadataChanges(self: SaveWorkflowCommand) -> IDictionary[XName, InstanceValue] """
        ...

    @property
    def UnlockInstance(self) -> bool:
        """
        Get: UnlockInstance(self: SaveWorkflowCommand) -> bool
        Set: UnlockInstance(self: SaveWorkflowCommand) = value
        """
        ...



class SqlWorkflowInstanceStore(InstanceStore): # skipped bases: <type 'object'>
    """
    SqlWorkflowInstanceStore()
    SqlWorkflowInstanceStore(connectionString: str)
    """
    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: SqlWorkflowInstanceStore) -> str
        Set: ConnectionString(self: SqlWorkflowInstanceStore) = value
        """
        ...

    @property
    def EnqueueRunCommands(self) -> bool:
        """
        Get: EnqueueRunCommands(self: SqlWorkflowInstanceStore) -> bool
        Set: EnqueueRunCommands(self: SqlWorkflowInstanceStore) = value
        """
        ...

    @property
    def HostLockRenewalPeriod(self) -> TimeSpan:
        """
        Get: HostLockRenewalPeriod(self: SqlWorkflowInstanceStore) -> TimeSpan
        Set: HostLockRenewalPeriod(self: SqlWorkflowInstanceStore) = value
        """
        ...

    @property
    def InstanceCompletionAction(self) -> InstanceCompletionAction:
        """
        Get: InstanceCompletionAction(self: SqlWorkflowInstanceStore) -> InstanceCompletionAction
        Set: InstanceCompletionAction(self: SqlWorkflowInstanceStore) = value
        """
        ...

    @property
    def InstanceEncodingOption(self) -> InstanceEncodingOption:
        """
        Get: InstanceEncodingOption(self: SqlWorkflowInstanceStore) -> InstanceEncodingOption
        Set: InstanceEncodingOption(self: SqlWorkflowInstanceStore) = value
        """
        ...

    @property
    def InstanceLockedExceptionAction(self) -> InstanceLockedExceptionAction:
        """
        Get: InstanceLockedExceptionAction(self: SqlWorkflowInstanceStore) -> InstanceLockedExceptionAction
        Set: InstanceLockedExceptionAction(self: SqlWorkflowInstanceStore) = value
        """
        ...

    @property
    def MaxConnectionRetries(self) -> int:
        """
        Get: MaxConnectionRetries(self: SqlWorkflowInstanceStore) -> int
        Set: MaxConnectionRetries(self: SqlWorkflowInstanceStore) = value
        """
        ...

    @property
    def RunnableInstancesDetectionPeriod(self) -> TimeSpan:
        """
        Get: RunnableInstancesDetectionPeriod(self: SqlWorkflowInstanceStore) -> TimeSpan
        Set: RunnableInstancesDetectionPeriod(self: SqlWorkflowInstanceStore) = value
        """
        ...


    def Promote(self, name:str, promoteAsVariant:IEnumerable, promoteAsBinary:IEnumerable): # -> 
        """ Promote(self: SqlWorkflowInstanceStore, name: str, promoteAsVariant: IEnumerable[XName], promoteAsBinary: IEnumerable[XName]) """
        ...

    def __new__(cls, connectionString:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, connectionString: str)
        """
        ...


class TryLoadRunnableWorkflowCommand(InstancePersistenceCommand): # skipped bases: <type 'object'>
    """ TryLoadRunnableWorkflowCommand() """
    pass

