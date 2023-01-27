# encoding: utf-8
# module System.Workflow.Runtime.Hosting calls itself Hosting
# from System.WorkflowServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Workflow.Runtime, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Enum, Guid, SystemException, TimeSpan

from System.Collections import IEnumerable, IList

from System.Collections.Specialized import NameValueCollection

from System.Data.SqlTypes import SqlDateTime

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    ChannelPoolSettings, IHttpModule, IPendingWork, WorkflowStatus, field#)
"""

# no functions
# classes

class WorkflowRuntimeService: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Runtime(self):
        ...

    @property
    def State(self):
        ...


    def OnStarted(self, *args): #cannot find CLR method
        """ OnStarted(self: WorkflowRuntimeService) """
        ...

    def OnStopped(self, *args): #cannot find CLR method
        """ OnStopped(self: WorkflowRuntimeService) """
        ...

    def RaiseServicesExceptionNotHandledEvent(self, *args): #cannot find CLR method
        """ RaiseServicesExceptionNotHandledEvent(self: WorkflowRuntimeService, exception: Exception, instanceId: Guid) """
        ...

    def Start(self, *args): #cannot find CLR method
        """ Start(self: WorkflowRuntimeService) """
        ...

    def Stop(self, *args): #cannot find CLR method
        """ Stop(self: WorkflowRuntimeService) """
        ...


class ChannelManagerService(WorkflowRuntimeService): # skipped bases: <type 'object'>
    """
    ChannelManagerService()
    ChannelManagerService(settings: ChannelPoolSettings)
    ChannelManagerService(endpoints: IList[ServiceEndpoint])
    ChannelManagerService(settings: ChannelPoolSettings, endpoints: IList[ServiceEndpoint])
    ChannelManagerService(parameters: NameValueCollection)
    """
    def __new__(cls, *__args) -> Self: # Not found arg types: {'*__args': 'ChannelPoolSettings'}
        """
        __new__(cls: type)
        __new__(cls: type, settings: ChannelPoolSettings)
        __new__(cls: type, endpoints: IList[ServiceEndpoint])
        __new__(cls: type, settings: ChannelPoolSettings, endpoints: IList[ServiceEndpoint])
        __new__(cls: type, parameters: NameValueCollection)
        """
        ...


class WorkflowCommitWorkBatchService(WorkflowRuntimeService): # skipped bases: <type 'object'>
    """ no doc """
    def CommitWorkBatch(self, *args): #cannot find CLR method
        """ CommitWorkBatch(self: WorkflowCommitWorkBatchService, commitWorkBatchCallback: CommitWorkBatchCallback) """
        ...

    def CommitWorkBatchCallback(self, *args): #cannot find CLR method
        """ CommitWorkBatchCallback(object: object, method: IntPtr) """
        ...



class DefaultWorkflowCommitWorkBatchService(WorkflowCommitWorkBatchService): # skipped bases: <type 'object'>
    """
    DefaultWorkflowCommitWorkBatchService()
    DefaultWorkflowCommitWorkBatchService(parameters: NameValueCollection)
    """
    @property
    def EnableRetries(self) -> bool:
        """
        Get: EnableRetries(self: DefaultWorkflowCommitWorkBatchService) -> bool
        Set: EnableRetries(self: DefaultWorkflowCommitWorkBatchService) = value
        """
        ...


    def __new__(cls, parameters:NameValueCollection = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parameters: NameValueCollection)
        """
        ...


class WorkflowLoaderService(WorkflowRuntimeService): # skipped bases: <type 'object'>
    """ no doc """
    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: WorkflowLoaderService, workflowType: Type) -> Activity
        CreateInstance(self: WorkflowLoaderService, workflowDefinitionReader: XmlReader, rulesReader: XmlReader) -> Activity
        """
        ...


class DefaultWorkflowLoaderService(WorkflowLoaderService): # skipped bases: <type 'object'>
    """ DefaultWorkflowLoaderService() """
    pass

class WorkflowSchedulerService(WorkflowRuntimeService): # skipped bases: <type 'object'>
    """ no doc """
    def Cancel(self, *args): #cannot find CLR method
        """ Cancel(self: WorkflowSchedulerService, timerId: Guid) """
        ...

    def Schedule(self, *args): #cannot find CLR method
        """ Schedule(self: WorkflowSchedulerService, callback: WaitCallback, workflowInstanceId: Guid)Schedule(self: WorkflowSchedulerService, callback: WaitCallback, workflowInstanceId: Guid, whenUtc: DateTime, timerId: Guid) """
        ...


class DefaultWorkflowSchedulerService(WorkflowSchedulerService): # skipped bases: <type 'object'>
    """
    DefaultWorkflowSchedulerService()
    DefaultWorkflowSchedulerService(maxSimultaneousWorkflows: int)
    DefaultWorkflowSchedulerService(parameters: NameValueCollection)
    """
    @property
    def MaxSimultaneousWorkflows(self) -> int:
        """ Get: MaxSimultaneousWorkflows(self: DefaultWorkflowSchedulerService) -> int """
        ...


    def __new__(cls, *__args:int) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, maxSimultaneousWorkflows: int)
        __new__(cls: type, parameters: NameValueCollection)
        """
        ...


class ManualWorkflowSchedulerService(WorkflowSchedulerService): # skipped bases: <type 'object'>
    """
    ManualWorkflowSchedulerService()
    ManualWorkflowSchedulerService(useActiveTimers: bool)
    ManualWorkflowSchedulerService(parameters: NameValueCollection)
    """
    def RunWorkflow(self, workflowInstanceId:Guid) -> bool:
        """ RunWorkflow(self: ManualWorkflowSchedulerService, workflowInstanceId: Guid) -> bool """
        ...

    def __new__(cls, *__args:bool) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, useActiveTimers: bool)
        __new__(cls: type, parameters: NameValueCollection)
        """
        ...


class PersistenceException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    PersistenceException()
    PersistenceException(message: str)
    PersistenceException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class SharedConnectionWorkflowCommitWorkBatchService(WorkflowCommitWorkBatchService): # skipped bases: <type 'object'>
    """
    SharedConnectionWorkflowCommitWorkBatchService(connectionString: str)
    SharedConnectionWorkflowCommitWorkBatchService(parameters: NameValueCollection)
    """
    @property
    def EnableRetries(self) -> bool:
        """
        Get: EnableRetries(self: SharedConnectionWorkflowCommitWorkBatchService) -> bool
        Set: EnableRetries(self: SharedConnectionWorkflowCommitWorkBatchService) = value
        """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, connectionString: str)
        __new__(cls: type, parameters: NameValueCollection)
        """
        ...


class SqlPersistenceWorkflowInstanceDescription: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsBlocked(self) -> bool:
        """ Get: IsBlocked(self: SqlPersistenceWorkflowInstanceDescription) -> bool """
        ...

    @property
    def NextTimerExpiration(self) -> SqlDateTime:
        """ Get: NextTimerExpiration(self: SqlPersistenceWorkflowInstanceDescription) -> SqlDateTime """
        ...

    @property
    def Status(self): # -> WorkflowStatus
        """ Get: Status(self: SqlPersistenceWorkflowInstanceDescription) -> WorkflowStatus """
        ...

    @property
    def SuspendOrTerminateDescription(self) -> str:
        """ Get: SuspendOrTerminateDescription(self: SqlPersistenceWorkflowInstanceDescription) -> str """
        ...

    @property
    def WorkflowInstanceId(self) -> Guid:
        """ Get: WorkflowInstanceId(self: SqlPersistenceWorkflowInstanceDescription) -> Guid """
        ...



class WorkflowPersistenceService(WorkflowRuntimeService): # skipped bases: <type 'object'>
    """ no doc """
    def GetDefaultSerializedForm(self, *args): #cannot find CLR method
        """ GetDefaultSerializedForm(activity: Activity) -> Array[Byte] """
        ...

    def GetIsBlocked(self, *args): #cannot find CLR method
        """ GetIsBlocked(rootActivity: Activity) -> bool """
        ...

    def GetSuspendOrTerminateInfo(self, *args): #cannot find CLR method
        """ GetSuspendOrTerminateInfo(rootActivity: Activity) -> str """
        ...

    def GetWorkflowStatus(self, *args): #cannot find CLR method
        """ GetWorkflowStatus(rootActivity: Activity) -> WorkflowStatus """
        ...

    def LoadCompletedContextActivity(self, *args): #cannot find CLR method
        """ LoadCompletedContextActivity(self: WorkflowPersistenceService, scopeId: Guid, outerActivity: Activity) -> Activity """
        ...

    def LoadWorkflowInstanceState(self, *args): #cannot find CLR method
        """ LoadWorkflowInstanceState(self: WorkflowPersistenceService, instanceId: Guid) -> Activity """
        ...

    def RestoreFromDefaultSerializedForm(self, *args): #cannot find CLR method
        """ RestoreFromDefaultSerializedForm(activityBytes: Array[Byte], outerActivity: Activity) -> Activity """
        ...

    def SaveCompletedContextActivity(self, *args): #cannot find CLR method
        """ SaveCompletedContextActivity(self: WorkflowPersistenceService, activity: Activity) """
        ...

    def SaveWorkflowInstanceState(self, *args): #cannot find CLR method
        """ SaveWorkflowInstanceState(self: WorkflowPersistenceService, rootActivity: Activity, unlock: bool) """
        ...

    def UnloadOnIdle(self, *args): #cannot find CLR method
        """ UnloadOnIdle(self: WorkflowPersistenceService, activity: Activity) -> bool """
        ...

    def UnlockWorkflowInstanceState(self, *args): #cannot find CLR method
        """ UnlockWorkflowInstanceState(self: WorkflowPersistenceService, rootActivity: Activity) """
        ...


class SqlWorkflowPersistenceService(WorkflowPersistenceService, IPendingWork): # skipped bases: <type 'object'>
    """
    SqlWorkflowPersistenceService(connectionString: str)
    SqlWorkflowPersistenceService(parameters: NameValueCollection)
    SqlWorkflowPersistenceService(connectionString: str, unloadOnIdle: bool, instanceOwnershipDuration: TimeSpan, loadingInterval: TimeSpan)
    """
    @property
    def EnableRetries(self) -> bool:
        """
        Get: EnableRetries(self: SqlWorkflowPersistenceService) -> bool
        Set: EnableRetries(self: SqlWorkflowPersistenceService) = value
        """
        ...

    @property
    def LoadingInterval(self) -> TimeSpan:
        """ Get: LoadingInterval(self: SqlWorkflowPersistenceService) -> TimeSpan """
        ...

    @property
    def ServiceInstanceId(self) -> Guid:
        """ Get: ServiceInstanceId(self: SqlWorkflowPersistenceService) -> Guid """
        ...


    def GetAllWorkflows(self) -> IEnumerable:
        """ GetAllWorkflows(self: SqlWorkflowPersistenceService) -> IEnumerable[SqlPersistenceWorkflowInstanceDescription] """
        ...

    def LoadExpiredTimerWorkflowIds(self) -> IList:
        """ LoadExpiredTimerWorkflowIds(self: SqlWorkflowPersistenceService) -> IList[Guid] """
        ...

    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, connectionString: str)
        __new__(cls: type, parameters: NameValueCollection)
        __new__(cls: type, connectionString: str, unloadOnIdle: bool, instanceOwnershipDuration: TimeSpan, loadingInterval: TimeSpan)
        """
        ...


class WorkflowRuntimeServiceState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WorkflowRuntimeServiceState, values: Started (2), Starting (1), Stopped (0), Stopping (3) """
    Started: WorkflowRuntimeServiceState = ...
    Starting: WorkflowRuntimeServiceState = ...
    Stopped: WorkflowRuntimeServiceState = ...
    Stopping: WorkflowRuntimeServiceState = ...
    value__ = ...


class WorkflowWebHostingModule(IHttpModule): # skipped bases: <type 'object'>
    """ WorkflowWebHostingModule() """
    pass

