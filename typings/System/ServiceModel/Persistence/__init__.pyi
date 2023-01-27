# encoding: utf-8
# module System.ServiceModel.Persistence calls itself Persistence
# from System.WorkflowServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import AsyncCallback, Guid, IAsyncResult, TimeSpan

from System.ServiceModel import CommunicationException

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    CommunicationObject)
"""

# no functions
# classes

class PersistenceException(CommunicationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PersistenceException()
    PersistenceException(message: str)
    PersistenceException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class InstanceLockException(PersistenceException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstanceLockException()
    InstanceLockException(message: str)
    InstanceLockException(message: str, innerException: Exception)
    InstanceLockException(id: Guid)
    InstanceLockException(id: Guid, message: str)
    InstanceLockException(id: Guid, message: str, innerException: Exception)
    InstanceLockException(id: Guid, innerException: Exception)
    """
    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: InstanceLockException) -> Guid """
        ...


    SerializeObjectState = ...


class InstanceNotFoundException(PersistenceException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstanceNotFoundException()
    InstanceNotFoundException(message: str)
    InstanceNotFoundException(message: str, innerException: Exception)
    InstanceNotFoundException(id: Guid)
    InstanceNotFoundException(id: Guid, message: str)
    InstanceNotFoundException(id: Guid, message: str, innerException: Exception)
    InstanceNotFoundException(id: Guid, innerException: Exception)
    """
    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: InstanceNotFoundException) -> Guid """
        ...


    SerializeObjectState = ...


class PersistenceProvider(CommunicationObject): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    @property
    def Id(self) -> Guid:
        """ Get: Id(self: PersistenceProvider) -> Guid """
        ...


    def BeginCreate(self, instance:object, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginCreate(self: PersistenceProvider, instance: object, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginDelete(self, instance:object, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginDelete(self: PersistenceProvider, instance: object, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginLoad(self, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginLoad(self: PersistenceProvider, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginLoadIfChanged(self, timeout:TimeSpan, instanceToken:object, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginLoadIfChanged(self: PersistenceProvider, timeout: TimeSpan, instanceToken: object, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginUpdate(self, instance:object, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginUpdate(self: PersistenceProvider, instance: object, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def Create(self, instance:object, timeout:TimeSpan) -> object:
        """ Create(self: PersistenceProvider, instance: object, timeout: TimeSpan) -> object """
        ...

    def Delete(self, instance:object, timeout:TimeSpan): # -> 
        """ Delete(self: PersistenceProvider, instance: object, timeout: TimeSpan) """
        ...

    def EndCreate(self, result:IAsyncResult) -> object:
        """ EndCreate(self: PersistenceProvider, result: IAsyncResult) -> object """
        ...

    def EndDelete(self, result:IAsyncResult): # -> 
        """ EndDelete(self: PersistenceProvider, result: IAsyncResult) """
        ...

    def EndLoad(self, result:IAsyncResult) -> object:
        """ EndLoad(self: PersistenceProvider, result: IAsyncResult) -> object """
        ...

    def EndLoadIfChanged(self, result, instance) -> Tuple_[bool, object]:
        """ EndLoadIfChanged(self: PersistenceProvider, result: IAsyncResult) -> (bool, object) """
        ...

    def EndUpdate(self, result:IAsyncResult) -> object:
        """ EndUpdate(self: PersistenceProvider, result: IAsyncResult) -> object """
        ...

    def Load(self, timeout:TimeSpan) -> object:
        """ Load(self: PersistenceProvider, timeout: TimeSpan) -> object """
        ...

    def LoadIfChanged(self, timeout, instanceToken, instance) -> Tuple_[bool, object]:
        """ LoadIfChanged(self: PersistenceProvider, timeout: TimeSpan, instanceToken: object) -> (bool, object) """
        ...

    def Update(self, instance:object, timeout:TimeSpan) -> object:
        """ Update(self: PersistenceProvider, instance: object, timeout: TimeSpan) -> object """
        ...


class LockingPersistenceProvider(PersistenceProvider): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    def BeginUnlock(self, timeout:TimeSpan, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginUnlock(self: LockingPersistenceProvider, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndUnlock(self, result:IAsyncResult): # -> 
        """ EndUnlock(self: LockingPersistenceProvider, result: IAsyncResult) """
        ...

    def Unlock(self, timeout:TimeSpan): # -> 
        """ Unlock(self: LockingPersistenceProvider, timeout: TimeSpan) """
        ...


class PersistenceProviderFactory(CommunicationObject): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """ no doc """
    def CreateProvider(self, id:Guid) -> PersistenceProvider:
        """ CreateProvider(self: PersistenceProviderFactory, id: Guid) -> PersistenceProvider """
        ...


class SqlPersistenceProviderFactory(PersistenceProviderFactory): # skipped bases: <type 'ICommunicationObject'>, <type 'object'>
    """
    SqlPersistenceProviderFactory(connectionString: str)
    SqlPersistenceProviderFactory(connectionString: str, serializeAsText: bool)
    SqlPersistenceProviderFactory(connectionString: str, serializeAsText: bool, lockTimeout: TimeSpan)
    SqlPersistenceProviderFactory(parameters: NameValueCollection)
    """
    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: SqlPersistenceProviderFactory) -> str
        Set: ConnectionString(self: SqlPersistenceProviderFactory) = value
        """
        ...

    @property
    def LockTimeout(self) -> TimeSpan:
        """
        Get: LockTimeout(self: SqlPersistenceProviderFactory) -> TimeSpan
        Set: LockTimeout(self: SqlPersistenceProviderFactory) = value
        """
        ...

    @property
    def SerializeAsText(self) -> bool:
        """
        Get: SerializeAsText(self: SqlPersistenceProviderFactory) -> bool
        Set: SerializeAsText(self: SqlPersistenceProviderFactory) = value
        """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, connectionString: str)
        __new__(cls: type, connectionString: str, serializeAsText: bool)
        __new__(cls: type, connectionString: str, serializeAsText: bool, lockTimeout: TimeSpan)
        __new__(cls: type, parameters: NameValueCollection)
        """
        ...


