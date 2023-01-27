# encoding: utf-8
# module System.Activities.Tracking calls itself Tracking
# from System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Workflow.Runtime, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import DateTime, Enum, Guid, Int64

from System.Activities import WorkflowIdentity

from System.Collections import IDictionary, IList

from System.Diagnostics import TraceLevel

"""The following names are not found in the module: field#
"""

# no functions
# classes

class ActivityInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ ActivityInfo(name: str, id: str, instanceId: str, typeName: str) """
    @property
    def Id(self) -> str:
        """ Get: Id(self: ActivityInfo) -> str """
        ...

    @property
    def InstanceId(self) -> str:
        """ Get: InstanceId(self: ActivityInfo) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ActivityInfo) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: ActivityInfo) -> str """
        ...


    def ToString(self) -> str:
        """ ToString(self: ActivityInfo) -> str """
        ...


class TrackingQuery: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def QueryAnnotations(self) -> IDictionary:
        """ Get: QueryAnnotations(self: TrackingQuery) -> IDictionary[str, str] """
        ...



class ActivityScheduledQuery(TrackingQuery): # skipped bases: <type 'object'>
    """ ActivityScheduledQuery() """
    @property
    def ActivityName(self) -> str:
        """
        Get: ActivityName(self: ActivityScheduledQuery) -> str
        Set: ActivityName(self: ActivityScheduledQuery) = value
        """
        ...

    @property
    def ChildActivityName(self) -> str:
        """
        Get: ChildActivityName(self: ActivityScheduledQuery) -> str
        Set: ChildActivityName(self: ActivityScheduledQuery) = value
        """
        ...



class TrackingRecord: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Annotations(self) -> IDictionary:
        """ Get: Annotations(self: TrackingRecord) -> IDictionary[str, str] """
        ...

    @property
    def EventTime(self) -> DateTime:
        """ Get: EventTime(self: TrackingRecord) -> DateTime """
        ...

    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: TrackingRecord) -> Guid """
        ...

    @property
    def Level(self) -> TraceLevel:
        """ Get: Level(self: TrackingRecord) -> TraceLevel """
        ...

    @property
    def RecordNumber(self) -> Int64:
        """ Get: RecordNumber(self: TrackingRecord) -> Int64 """
        ...


    def Clone(self, *args): #cannot find CLR method
        """ Clone(self: TrackingRecord) -> TrackingRecord """
        ...

    def ToString(self) -> str:
        """ ToString(self: TrackingRecord) -> str """
        ...


class ActivityScheduledRecord(TrackingRecord): # skipped bases: <type 'object'>
    """ ActivityScheduledRecord(instanceId: Guid, recordNumber: Int64, activity: ActivityInfo, child: ActivityInfo) """
    @property
    def Activity(self) -> ActivityInfo:
        """ Get: Activity(self: ActivityScheduledRecord) -> ActivityInfo """
        ...

    @property
    def Child(self) -> ActivityInfo:
        """ Get: Child(self: ActivityScheduledRecord) -> ActivityInfo """
        ...



class ActivityStateQuery(TrackingQuery): # skipped bases: <type 'object'>
    """ ActivityStateQuery() """
    @property
    def ActivityName(self) -> str:
        """
        Get: ActivityName(self: ActivityStateQuery) -> str
        Set: ActivityName(self: ActivityStateQuery) = value
        """
        ...

    @property
    def Arguments(self) -> Collection:
        """ Get: Arguments(self: ActivityStateQuery) -> Collection[str] """
        ...

    @property
    def States(self) -> Collection:
        """ Get: States(self: ActivityStateQuery) -> Collection[str] """
        ...

    @property
    def Variables(self) -> Collection:
        """ Get: Variables(self: ActivityStateQuery) -> Collection[str] """
        ...



class ActivityStateRecord(TrackingRecord): # skipped bases: <type 'object'>
    """ ActivityStateRecord(instanceId: Guid, recordNumber: Int64, activity: ActivityInfo, state: str) """
    @property
    def Activity(self) -> ActivityInfo:
        """ Get: Activity(self: ActivityStateRecord) -> ActivityInfo """
        ...

    @property
    def Arguments(self) -> IDictionary:
        """ Get: Arguments(self: ActivityStateRecord) -> IDictionary[str, object] """
        ...

    @property
    def State(self) -> str:
        """ Get: State(self: ActivityStateRecord) -> str """
        ...

    @property
    def Variables(self) -> IDictionary:
        """ Get: Variables(self: ActivityStateRecord) -> IDictionary[str, object] """
        ...



class ActivityStates: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Canceled: str = ...
    Closed: str = ...
    Executing: str = ...
    Faulted: str = ...
    __all__: list = ...


class BookmarkResumptionQuery(TrackingQuery): # skipped bases: <type 'object'>
    """ BookmarkResumptionQuery() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: BookmarkResumptionQuery) -> str
        Set: Name(self: BookmarkResumptionQuery) = value
        """
        ...



class BookmarkResumptionRecord(TrackingRecord): # skipped bases: <type 'object'>
    """ BookmarkResumptionRecord(instanceId: Guid, recordNumber: Int64, bookmarkScope: Guid, bookmarkName: str, owner: ActivityInfo) """
    @property
    def BookmarkName(self) -> str:
        """ Get: BookmarkName(self: BookmarkResumptionRecord) -> str """
        ...

    @property
    def BookmarkScope(self) -> Guid:
        """ Get: BookmarkScope(self: BookmarkResumptionRecord) -> Guid """
        ...

    @property
    def Owner(self) -> ActivityInfo:
        """ Get: Owner(self: BookmarkResumptionRecord) -> ActivityInfo """
        ...

    @property
    def Payload(self) -> object:
        """ Get: Payload(self: BookmarkResumptionRecord) -> object """
        ...



class CancelRequestedQuery(TrackingQuery): # skipped bases: <type 'object'>
    """ CancelRequestedQuery() """
    @property
    def ActivityName(self) -> str:
        """
        Get: ActivityName(self: CancelRequestedQuery) -> str
        Set: ActivityName(self: CancelRequestedQuery) = value
        """
        ...

    @property
    def ChildActivityName(self) -> str:
        """
        Get: ChildActivityName(self: CancelRequestedQuery) -> str
        Set: ChildActivityName(self: CancelRequestedQuery) = value
        """
        ...



class CancelRequestedRecord(TrackingRecord): # skipped bases: <type 'object'>
    """ CancelRequestedRecord(instanceId: Guid, recordNumber: Int64, activity: ActivityInfo, child: ActivityInfo) """
    @property
    def Activity(self) -> ActivityInfo:
        """ Get: Activity(self: CancelRequestedRecord) -> ActivityInfo """
        ...

    @property
    def Child(self) -> ActivityInfo:
        """ Get: Child(self: CancelRequestedRecord) -> ActivityInfo """
        ...



class CustomTrackingQuery(TrackingQuery): # skipped bases: <type 'object'>
    """ CustomTrackingQuery() """
    @property
    def ActivityName(self) -> str:
        """
        Get: ActivityName(self: CustomTrackingQuery) -> str
        Set: ActivityName(self: CustomTrackingQuery) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CustomTrackingQuery) -> str
        Set: Name(self: CustomTrackingQuery) = value
        """
        ...



class CustomTrackingRecord(TrackingRecord): # skipped bases: <type 'object'>
    """
    CustomTrackingRecord(name: str)
    CustomTrackingRecord(name: str, level: TraceLevel)
    CustomTrackingRecord(instanceId: Guid, name: str, level: TraceLevel)
    """
    @property
    def Activity(self) -> ActivityInfo:
        """ Get: Activity(self: CustomTrackingRecord) -> ActivityInfo """
        ...

    @property
    def Data(self) -> IDictionary:
        """ Get: Data(self: CustomTrackingRecord) -> IDictionary[str, object] """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: CustomTrackingRecord) -> str """
        ...



class TrackingParticipant: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def TrackingProfile(self) -> TrackingProfile:
        """
        Get: TrackingProfile(self: TrackingParticipant) -> TrackingProfile
        Set: TrackingProfile(self: TrackingParticipant) = value
        """
        ...


    def BeginTrack(self, *args): #cannot find CLR method
        """ BeginTrack(self: TrackingParticipant, record: TrackingRecord, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndTrack(self, *args): #cannot find CLR method
        """ EndTrack(self: TrackingParticipant, result: IAsyncResult) """
        ...

    def Track(self, *args): #cannot find CLR method
        """ Track(self: TrackingParticipant, record: TrackingRecord, timeout: TimeSpan) """
        ...


class EtwTrackingParticipant(TrackingParticipant): # skipped bases: <type 'object'>
    """ EtwTrackingParticipant() """
    @property
    def ApplicationReference(self) -> str:
        """
        Get: ApplicationReference(self: EtwTrackingParticipant) -> str
        Set: ApplicationReference(self: EtwTrackingParticipant) = value
        """
        ...

    @property
    def EtwProviderId(self) -> Guid:
        """
        Get: EtwProviderId(self: EtwTrackingParticipant) -> Guid
        Set: EtwProviderId(self: EtwTrackingParticipant) = value
        """
        ...



class FaultPropagationQuery(TrackingQuery): # skipped bases: <type 'object'>
    """ FaultPropagationQuery() """
    @property
    def FaultHandlerActivityName(self) -> str:
        """
        Get: FaultHandlerActivityName(self: FaultPropagationQuery) -> str
        Set: FaultHandlerActivityName(self: FaultPropagationQuery) = value
        """
        ...

    @property
    def FaultSourceActivityName(self) -> str:
        """
        Get: FaultSourceActivityName(self: FaultPropagationQuery) -> str
        Set: FaultSourceActivityName(self: FaultPropagationQuery) = value
        """
        ...



class FaultPropagationRecord(TrackingRecord): # skipped bases: <type 'object'>
    """ FaultPropagationRecord(instanceId: Guid, recordNumber: Int64, faultSource: ActivityInfo, faultHandler: ActivityInfo, isFaultSource: bool, fault: Exception) """
    @property
    def Fault(self) -> Exception:
        """ Get: Fault(self: FaultPropagationRecord) -> Exception """
        ...

    @property
    def FaultHandler(self) -> ActivityInfo:
        """ Get: FaultHandler(self: FaultPropagationRecord) -> ActivityInfo """
        ...

    @property
    def FaultSource(self) -> ActivityInfo:
        """ Get: FaultSource(self: FaultPropagationRecord) -> ActivityInfo """
        ...

    @property
    def IsFaultSource(self) -> bool:
        """ Get: IsFaultSource(self: FaultPropagationRecord) -> bool """
        ...



class ImplementationVisibility(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ImplementationVisibility, values: All (1), RootScope (0) """
    All: ImplementationVisibility = ...
    RootScope: ImplementationVisibility = ...
    value__ = ...


class InteropTrackingRecord(CustomTrackingRecord): # skipped bases: <type 'object'>
    """ InteropTrackingRecord(activityDisplayName: str, v1TrackingRecord: TrackingRecord) """
    @property
    def TrackingRecord(self) -> TrackingRecord:
        """ Get: TrackingRecord(self: InteropTrackingRecord) -> TrackingRecord """
        ...



class TrackingProfile: # skipped bases: <type 'object'>, <type 'object'>
    """ TrackingProfile() """
    @property
    def ActivityDefinitionId(self) -> str:
        """
        Get: ActivityDefinitionId(self: TrackingProfile) -> str
        Set: ActivityDefinitionId(self: TrackingProfile) = value
        """
        ...

    @property
    def ImplementationVisibility(self) -> ImplementationVisibility:
        """
        Get: ImplementationVisibility(self: TrackingProfile) -> ImplementationVisibility
        Set: ImplementationVisibility(self: TrackingProfile) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: TrackingProfile) -> str
        Set: Name(self: TrackingProfile) = value
        """
        ...

    @property
    def Queries(self) -> Collection:
        """ Get: Queries(self: TrackingProfile) -> Collection[TrackingQuery] """
        ...



class WorkflowInstanceRecord(TrackingRecord): # skipped bases: <type 'object'>
    """
    WorkflowInstanceRecord(instanceId: Guid, activityDefinitionId: str, state: str)
    WorkflowInstanceRecord(instanceId: Guid, recordNumber: Int64, activityDefinitionId: str, state: str)
    WorkflowInstanceRecord(instanceId: Guid, activityDefinitionId: str, state: str, workflowDefinitionIdentity: WorkflowIdentity)
    WorkflowInstanceRecord(instanceId: Guid, recordNumber: Int64, activityDefinitionId: str, state: str, workflowDefinitionIdentity: WorkflowIdentity)
    """
    @property
    def ActivityDefinitionId(self) -> str:
        """ Get: ActivityDefinitionId(self: WorkflowInstanceRecord) -> str """
        ...

    @property
    def State(self) -> str:
        """ Get: State(self: WorkflowInstanceRecord) -> str """
        ...

    @property
    def WorkflowDefinitionIdentity(self) -> WorkflowIdentity:
        """ Get: WorkflowDefinitionIdentity(self: WorkflowInstanceRecord) -> WorkflowIdentity """
        ...



class WorkflowInstanceAbortedRecord(WorkflowInstanceRecord): # skipped bases: <type 'object'>
    """
    WorkflowInstanceAbortedRecord(instanceId: Guid, activityDefinitionId: str, reason: str)
    WorkflowInstanceAbortedRecord(instanceId: Guid, recordNumber: Int64, activityDefinitionId: str, reason: str)
    WorkflowInstanceAbortedRecord(instanceId: Guid, activityDefinitionId: str, reason: str, workflowDefinitionIdentity: WorkflowIdentity)
    WorkflowInstanceAbortedRecord(instanceId: Guid, recordNumber: Int64, activityDefinitionId: str, reason: str, workflowDefinitionIdentity: WorkflowIdentity)
    """
    @property
    def Reason(self) -> str:
        """ Get: Reason(self: WorkflowInstanceAbortedRecord) -> str """
        ...



class WorkflowInstanceQuery(TrackingQuery): # skipped bases: <type 'object'>
    """ WorkflowInstanceQuery() """
    @property
    def States(self) -> Collection:
        """ Get: States(self: WorkflowInstanceQuery) -> Collection[str] """
        ...



class WorkflowInstanceStates: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    Aborted: str = ...
    Canceled: str = ...
    Completed: str = ...
    Deleted: str = ...
    Idle: str = ...
    Persisted: str = ...
    Resumed: str = ...
    Started: str = ...
    Suspended: str = ...
    Terminated: str = ...
    UnhandledException: str = ...
    Unloaded: str = ...
    Unsuspended: str = ...
    Updated: str = ...
    UpdateFailed: str = ...
    __all__: list = ...


class WorkflowInstanceSuspendedRecord(WorkflowInstanceRecord): # skipped bases: <type 'object'>
    """
    WorkflowInstanceSuspendedRecord(instanceId: Guid, activityDefinitionId: str, reason: str)
    WorkflowInstanceSuspendedRecord(instanceId: Guid, recordNumber: Int64, activityDefinitionId: str, reason: str)
    WorkflowInstanceSuspendedRecord(instanceId: Guid, activityDefinitionId: str, reason: str, workflowDefinitionIdentity: WorkflowIdentity)
    WorkflowInstanceSuspendedRecord(instanceId: Guid, recordNumber: Int64, activityDefinitionId: str, reason: str, workflowDefinitionIdentity: WorkflowIdentity)
    """
    @property
    def Reason(self) -> str:
        """ Get: Reason(self: WorkflowInstanceSuspendedRecord) -> str """
        ...



class WorkflowInstanceTerminatedRecord(WorkflowInstanceRecord): # skipped bases: <type 'object'>
    """
    WorkflowInstanceTerminatedRecord(instanceId: Guid, activityDefinitionId: str, reason: str)
    WorkflowInstanceTerminatedRecord(instanceId: Guid, recordNumber: Int64, activityDefinitionId: str, reason: str)
    WorkflowInstanceTerminatedRecord(instanceId: Guid, activityDefinitionId: str, reason: str, workflowDefinitionIdentity: WorkflowIdentity)
    WorkflowInstanceTerminatedRecord(instanceId: Guid, recordNumber: Int64, activityDefinitionId: str, reason: str, workflowDefinitionIdentity: WorkflowIdentity)
    """
    @property
    def Reason(self) -> str:
        """ Get: Reason(self: WorkflowInstanceTerminatedRecord) -> str """
        ...



class WorkflowInstanceUnhandledExceptionRecord(WorkflowInstanceRecord): # skipped bases: <type 'object'>
    """
    WorkflowInstanceUnhandledExceptionRecord(instanceId: Guid, activityDefinitionId: str, faultSource: ActivityInfo, exception: Exception)
    WorkflowInstanceUnhandledExceptionRecord(instanceId: Guid, recordNumber: Int64, activityDefinitionId: str, faultSource: ActivityInfo, exception: Exception)
    WorkflowInstanceUnhandledExceptionRecord(instanceId: Guid, activityDefinitionId: str, faultSource: ActivityInfo, exception: Exception, workflowDefinitionIdentity: WorkflowIdentity)
    WorkflowInstanceUnhandledExceptionRecord(instanceId: Guid, recordNumber: Int64, activityDefinitionId: str, faultSource: ActivityInfo, exception: Exception, workflowDefinitionIdentity: WorkflowIdentity)
    """
    @property
    def FaultSource(self) -> ActivityInfo:
        """ Get: FaultSource(self: WorkflowInstanceUnhandledExceptionRecord) -> ActivityInfo """
        ...

    @property
    def UnhandledException(self) -> Exception:
        """ Get: UnhandledException(self: WorkflowInstanceUnhandledExceptionRecord) -> Exception """
        ...



class WorkflowInstanceUpdatedRecord(WorkflowInstanceRecord): # skipped bases: <type 'object'>
    """
    WorkflowInstanceUpdatedRecord(instanceId: Guid, activityDefinitionId: str, originalDefinitionIdentity: WorkflowIdentity, updatedDefinitionIdentity: WorkflowIdentity)
    WorkflowInstanceUpdatedRecord(instanceId: Guid, activityDefinitionId: str, originalDefinitionIdentity: WorkflowIdentity, updatedDefinitionIdentity: WorkflowIdentity, blockingActivities: IList[ActivityBlockingUpdate])
    WorkflowInstanceUpdatedRecord(instanceId: Guid, recordNumber: Int64, activityDefinitionId: str, originalDefinitionIdentity: WorkflowIdentity, updatedDefinitionIdentity: WorkflowIdentity)
    WorkflowInstanceUpdatedRecord(instanceId: Guid, recordNumber: Int64, activityDefinitionId: str, originalDefinitionIdentity: WorkflowIdentity, updatedDefinitionIdentity: WorkflowIdentity, blockingActivities: IList[ActivityBlockingUpdate])
    """
    @property
    def BlockingActivities(self) -> IList:
        """ Get: BlockingActivities(self: WorkflowInstanceUpdatedRecord) -> IList[ActivityBlockingUpdate] """
        ...

    @property
    def IsSuccessful(self) -> bool:
        """ Get: IsSuccessful(self: WorkflowInstanceUpdatedRecord) -> bool """
        ...

    @property
    def OriginalDefinitionIdentity(self) -> WorkflowIdentity:
        """ Get: OriginalDefinitionIdentity(self: WorkflowInstanceUpdatedRecord) -> WorkflowIdentity """
        ...



