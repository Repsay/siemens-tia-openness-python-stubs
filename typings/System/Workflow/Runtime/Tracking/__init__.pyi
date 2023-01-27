# encoding: utf-8
# module System.Workflow.Runtime.Tracking calls itself Tracking
# from System.Workflow.Runtime, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Attribute, DateTime, Enum, EventArgs, Guid, Int64, 
    Nullable, SystemException, Type, Version)

from System.Collections import IList

from System.Collections.Generic import List

from System.EnterpriseServices import Activity

from System.IO import TextReader, TextWriter

from System.Workflow.ComponentModel import ActivityExecutionStatus

from System.Workflow.Runtime import WorkflowStatus

from System.Workflow.Runtime.Hosting import WorkflowRuntimeService

from System.Xml.Schema import XmlSchema

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class TrackingExtract: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Annotations(self) -> TrackingAnnotationCollection:
        """ Get: Annotations(self: TrackingExtract) -> TrackingAnnotationCollection """
        ...

    @property
    def Member(self) -> str:
        """
        Get: Member(self: TrackingExtract) -> str
        Set: Member(self: TrackingExtract) = value
        """
        ...



class ActivityDataTrackingExtract(TrackingExtract): # skipped bases: <type 'object'>
    """
    ActivityDataTrackingExtract()
    ActivityDataTrackingExtract(member: str)
    """
    def __new__(cls, member:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, member: str)
        """
        ...


class TrackingCondition: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Member(self) -> str:
        """
        Get: Member(self: TrackingCondition) -> str
        Set: Member(self: TrackingCondition) = value
        """
        ...

    @property
    def Operator(self) -> ComparisonOperator:
        """
        Get: Operator(self: TrackingCondition) -> ComparisonOperator
        Set: Operator(self: TrackingCondition) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: TrackingCondition) -> str
        Set: Value(self: TrackingCondition) = value
        """
        ...



class ActivityTrackingCondition(TrackingCondition): # skipped bases: <type 'object'>
    """
    ActivityTrackingCondition()
    ActivityTrackingCondition(member: str, value: str)
    """
    def __new__(cls, member:str = ..., value:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, member: str, value: str)
        """
        ...


class ActivityTrackingLocation: # skipped bases: <type 'object'>, <type 'object'>
    """
    ActivityTrackingLocation()
    ActivityTrackingLocation(activityTypeName: str)
    ActivityTrackingLocation(activityType: Type)
    ActivityTrackingLocation(activityTypeName: str, executionStatusEvents: IEnumerable[ActivityExecutionStatus])
    ActivityTrackingLocation(activityType: Type, executionStatusEvents: IEnumerable[ActivityExecutionStatus])
    ActivityTrackingLocation(activityTypeName: str, matchDerivedTypes: bool, executionStatusEvents: IEnumerable[ActivityExecutionStatus])
    ActivityTrackingLocation(activityType: Type, matchDerivedTypes: bool, executionStatusEvents: IEnumerable[ActivityExecutionStatus])
    """
    @property
    def ActivityType(self) -> Type:
        """
        Get: ActivityType(self: ActivityTrackingLocation) -> Type
        Set: ActivityType(self: ActivityTrackingLocation) = value
        """
        ...

    @property
    def ActivityTypeName(self) -> str:
        """
        Get: ActivityTypeName(self: ActivityTrackingLocation) -> str
        Set: ActivityTypeName(self: ActivityTrackingLocation) = value
        """
        ...

    @property
    def Conditions(self) -> TrackingConditionCollection:
        """ Get: Conditions(self: ActivityTrackingLocation) -> TrackingConditionCollection """
        ...

    @property
    def ExecutionStatusEvents(self) -> IList:
        """ Get: ExecutionStatusEvents(self: ActivityTrackingLocation) -> IList[ActivityExecutionStatus] """
        ...

    @property
    def MatchDerivedTypes(self) -> bool:
        """
        Get: MatchDerivedTypes(self: ActivityTrackingLocation) -> bool
        Set: MatchDerivedTypes(self: ActivityTrackingLocation) = value
        """
        ...



class ActivityTrackingLocationCollection(List): # skipped bases: <type 'IEnumerable[ActivityTrackingLocation]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyList[ActivityTrackingLocation]'>, <type 'ICollection[ActivityTrackingLocation]'>, <type 'IReadOnlyCollection[ActivityTrackingLocation]'>, <type 'IList[ActivityTrackingLocation]'>, <type 'ICollection'>, <type 'object'>
    """
    ActivityTrackingLocationCollection()
    ActivityTrackingLocationCollection(locations: IEnumerable[ActivityTrackingLocation])
    """
    pass

class TrackingRecord: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Annotations(self) -> TrackingAnnotationCollection:
        """ Get: Annotations(self: TrackingRecord) -> TrackingAnnotationCollection """
        ...

    @property
    def EventArgs(self) -> EventArgs:
        """
        Get: EventArgs(self: TrackingRecord) -> EventArgs
        Set: EventArgs(self: TrackingRecord) = value
        """
        ...

    @property
    def EventDateTime(self) -> DateTime:
        """
        Get: EventDateTime(self: TrackingRecord) -> DateTime
        Set: EventDateTime(self: TrackingRecord) = value
        """
        ...

    @property
    def EventOrder(self) -> int:
        """
        Get: EventOrder(self: TrackingRecord) -> int
        Set: EventOrder(self: TrackingRecord) = value
        """
        ...



class ActivityTrackingRecord(TrackingRecord): # skipped bases: <type 'object'>
    """
    ActivityTrackingRecord()
    ActivityTrackingRecord(activityType: Type, qualifiedName: str, contextGuid: Guid, parentContextGuid: Guid, executionStatus: ActivityExecutionStatus, eventDateTime: DateTime, eventOrder: int, eventArgs: EventArgs)
    """
    @property
    def ActivityType(self) -> Type:
        """
        Get: ActivityType(self: ActivityTrackingRecord) -> Type
        Set: ActivityType(self: ActivityTrackingRecord) = value
        """
        ...

    @property
    def Body(self) -> IList:
        """ Get: Body(self: ActivityTrackingRecord) -> IList[TrackingDataItem] """
        ...

    @property
    def ContextGuid(self) -> Guid:
        """
        Get: ContextGuid(self: ActivityTrackingRecord) -> Guid
        Set: ContextGuid(self: ActivityTrackingRecord) = value
        """
        ...

    @property
    def ExecutionStatus(self) -> ActivityExecutionStatus:
        """
        Get: ExecutionStatus(self: ActivityTrackingRecord) -> ActivityExecutionStatus
        Set: ExecutionStatus(self: ActivityTrackingRecord) = value
        """
        ...

    @property
    def ParentContextGuid(self) -> Guid:
        """
        Get: ParentContextGuid(self: ActivityTrackingRecord) -> Guid
        Set: ParentContextGuid(self: ActivityTrackingRecord) = value
        """
        ...

    @property
    def QualifiedName(self) -> str:
        """
        Get: QualifiedName(self: ActivityTrackingRecord) -> str
        Set: QualifiedName(self: ActivityTrackingRecord) = value
        """
        ...


    def __new__(cls, activityType:Type = ..., qualifiedName:str = ..., contextGuid:Guid = ..., parentContextGuid:Guid = ..., executionStatus:ActivityExecutionStatus = ..., eventDateTime:DateTime = ..., eventOrder:int = ..., eventArgs:EventArgs = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, activityType: Type, qualifiedName: str, contextGuid: Guid, parentContextGuid: Guid, executionStatus: ActivityExecutionStatus, eventDateTime: DateTime, eventOrder: int, eventArgs: EventArgs)
        """
        ...


class ActivityTrackPoint: # skipped bases: <type 'object'>, <type 'object'>
    """ ActivityTrackPoint() """
    @property
    def Annotations(self) -> TrackingAnnotationCollection:
        """ Get: Annotations(self: ActivityTrackPoint) -> TrackingAnnotationCollection """
        ...

    @property
    def ExcludedLocations(self) -> ActivityTrackingLocationCollection:
        """ Get: ExcludedLocations(self: ActivityTrackPoint) -> ActivityTrackingLocationCollection """
        ...

    @property
    def Extracts(self) -> ExtractCollection:
        """ Get: Extracts(self: ActivityTrackPoint) -> ExtractCollection """
        ...

    @property
    def MatchingLocations(self) -> ActivityTrackingLocationCollection:
        """ Get: MatchingLocations(self: ActivityTrackPoint) -> ActivityTrackingLocationCollection """
        ...



class ActivityTrackPointCollection(List): # skipped bases: <type 'IEnumerable'>, <type 'IList'>, <type 'IEnumerable[ActivityTrackPoint]'>, <type 'IList[ActivityTrackPoint]'>, <type 'IReadOnlyList[ActivityTrackPoint]'>, <type 'ICollection[ActivityTrackPoint]'>, <type 'ICollection'>, <type 'IReadOnlyCollection[ActivityTrackPoint]'>, <type 'object'>
    """
    ActivityTrackPointCollection()
    ActivityTrackPointCollection(points: IEnumerable[ActivityTrackPoint])
    """
    pass

class ComparisonOperator(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ComparisonOperator, values: Equals (0), NotEquals (1) """
    Equals: ComparisonOperator = ...
    NotEquals: ComparisonOperator = ...
    value__ = ...


class ExtractCollection(List): # skipped bases: <type 'IList[TrackingExtract]'>, <type 'IEnumerable'>, <type 'ICollection[TrackingExtract]'>, <type 'IList'>, <type 'IEnumerable[TrackingExtract]'>, <type 'IReadOnlyList[TrackingExtract]'>, <type 'ICollection'>, <type 'IReadOnlyCollection[TrackingExtract]'>, <type 'object'>
    """
    ExtractCollection()
    ExtractCollection(extracts: IEnumerable[TrackingExtract])
    """
    pass

class IProfileNotification: # skipped bases: <type 'object'>
    """ no doc """
    ProfileRemoved = ...
    ProfileUpdated = ...


class PreviousTrackingServiceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PreviousTrackingServiceAttribute(assemblyQualifiedName: str) """
    @property
    def AssemblyQualifiedName(self) -> str:
        """ Get: AssemblyQualifiedName(self: PreviousTrackingServiceAttribute) -> str """
        ...


    def __new__(cls, assemblyQualifiedName:str) -> Self:
        """ __new__(cls: type, assemblyQualifiedName: str) """
        ...


class ProfileRemovedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    ProfileRemovedEventArgs()
    ProfileRemovedEventArgs(workflowType: Type)
    """
    @property
    def WorkflowType(self) -> Type:
        """
        Get: WorkflowType(self: ProfileRemovedEventArgs) -> Type
        Set: WorkflowType(self: ProfileRemovedEventArgs) = value
        """
        ...


    def __new__(cls, workflowType:Type = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, workflowType: Type)
        """
        ...


class ProfileUpdatedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """
    ProfileUpdatedEventArgs()
    ProfileUpdatedEventArgs(workflowType: Type, profile: TrackingProfile)
    """
    @property
    def TrackingProfile(self) -> TrackingProfile:
        """
        Get: TrackingProfile(self: ProfileUpdatedEventArgs) -> TrackingProfile
        Set: TrackingProfile(self: ProfileUpdatedEventArgs) = value
        """
        ...

    @property
    def WorkflowType(self) -> Type:
        """
        Get: WorkflowType(self: ProfileUpdatedEventArgs) -> Type
        Set: WorkflowType(self: ProfileUpdatedEventArgs) = value
        """
        ...


    def __new__(cls, workflowType:Type = ..., profile:TrackingProfile = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, workflowType: Type, profile: TrackingProfile)
        """
        ...


class SqlTrackingQuery: # skipped bases: <type 'object'>, <type 'object'>
    """
    SqlTrackingQuery()
    SqlTrackingQuery(connectionString: str)
    """
    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: SqlTrackingQuery) -> str
        Set: ConnectionString(self: SqlTrackingQuery) = value
        """
        ...


    def GetWorkflows(self, options:SqlTrackingQueryOptions) -> IList:
        """ GetWorkflows(self: SqlTrackingQuery, options: SqlTrackingQueryOptions) -> IList[SqlTrackingWorkflowInstance] """
        ...

    def TryGetWorkflow(self, workflowInstanceId, workflowInstance) -> Tuple_[bool, SqlTrackingWorkflowInstance]:
        """ TryGetWorkflow(self: SqlTrackingQuery, workflowInstanceId: Guid) -> (bool, SqlTrackingWorkflowInstance) """
        ...


class SqlTrackingQueryOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ SqlTrackingQueryOptions() """
    @property
    def StatusMaxDateTime(self) -> DateTime:
        """
        Get: StatusMaxDateTime(self: SqlTrackingQueryOptions) -> DateTime
        Set: StatusMaxDateTime(self: SqlTrackingQueryOptions) = value
        """
        ...

    @property
    def StatusMinDateTime(self) -> DateTime:
        """
        Get: StatusMinDateTime(self: SqlTrackingQueryOptions) -> DateTime
        Set: StatusMinDateTime(self: SqlTrackingQueryOptions) = value
        """
        ...

    @property
    def TrackingDataItems(self) -> IList:
        """ Get: TrackingDataItems(self: SqlTrackingQueryOptions) -> IList[TrackingDataItemValue] """
        ...

    @property
    def WorkflowStatus(self) -> Nullable:
        """
        Get: WorkflowStatus(self: SqlTrackingQueryOptions) -> Nullable[WorkflowStatus]
        Set: WorkflowStatus(self: SqlTrackingQueryOptions) = value
        """
        ...

    @property
    def WorkflowType(self) -> Type:
        """
        Get: WorkflowType(self: SqlTrackingQueryOptions) -> Type
        Set: WorkflowType(self: SqlTrackingQueryOptions) = value
        """
        ...


    def Clear(self): # -> 
        """ Clear(self: SqlTrackingQueryOptions) """
        ...


class TrackingService(WorkflowRuntimeService): # skipped bases: <type 'object'>
    """ no doc """
    def GetProfile(self, *args): #cannot find CLR method
        """
        GetProfile(self: TrackingService, workflowType: Type, profileVersionId: Version) -> TrackingProfile
        GetProfile(self: TrackingService, workflowInstanceId: Guid) -> TrackingProfile
        """
        ...

    def GetTrackingChannel(self, *args): #cannot find CLR method
        """ GetTrackingChannel(self: TrackingService, parameters: TrackingParameters) -> TrackingChannel """
        ...

    def TryGetProfile(self, *args): #cannot find CLR method
        """ TryGetProfile(self: TrackingService, workflowType: Type) -> (bool, TrackingProfile) """
        ...

    def TryReloadProfile(self, *args): #cannot find CLR method
        """ TryReloadProfile(self: TrackingService, workflowType: Type, workflowInstanceId: Guid) -> (bool, TrackingProfile) """
        ...


class SqlTrackingService(TrackingService, IProfileNotification): # skipped bases: <type 'object'>
    """
    SqlTrackingService(connectionString: str)
    SqlTrackingService(parameters: NameValueCollection)
    """
    @property
    def ConnectionString(self) -> str:
        """ Get: ConnectionString(self: SqlTrackingService) -> str """
        ...

    @property
    def EnableRetries(self) -> bool:
        """
        Get: EnableRetries(self: SqlTrackingService) -> bool
        Set: EnableRetries(self: SqlTrackingService) = value
        """
        ...

    @property
    def IsTransactional(self) -> bool:
        """
        Get: IsTransactional(self: SqlTrackingService) -> bool
        Set: IsTransactional(self: SqlTrackingService) = value
        """
        ...

    @property
    def PartitionOnCompletion(self) -> bool:
        """
        Get: PartitionOnCompletion(self: SqlTrackingService) -> bool
        Set: PartitionOnCompletion(self: SqlTrackingService) = value
        """
        ...

    @property
    def ProfileChangeCheckInterval(self) -> float:
        """
        Get: ProfileChangeCheckInterval(self: SqlTrackingService) -> float
        Set: ProfileChangeCheckInterval(self: SqlTrackingService) = value
        """
        ...

    @property
    def UseDefaultProfile(self) -> bool:
        """
        Get: UseDefaultProfile(self: SqlTrackingService) -> bool
        Set: UseDefaultProfile(self: SqlTrackingService) = value
        """
        ...


    def __new__(cls, *__args:str) -> Self:
        """
        __new__(cls: type, connectionString: str)
        __new__(cls: type, parameters: NameValueCollection)
        """
        ...

    ProfileRemoved = ...
    ProfileUpdated = ...


class SqlTrackingWorkflowInstance: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ActivityEvents(self) -> IList:
        """ Get: ActivityEvents(self: SqlTrackingWorkflowInstance) -> IList[ActivityTrackingRecord] """
        ...

    @property
    def AutoRefresh(self) -> bool:
        """
        Get: AutoRefresh(self: SqlTrackingWorkflowInstance) -> bool
        Set: AutoRefresh(self: SqlTrackingWorkflowInstance) = value
        """
        ...

    @property
    def Initialized(self) -> DateTime:
        """
        Get: Initialized(self: SqlTrackingWorkflowInstance) -> DateTime
        Set: Initialized(self: SqlTrackingWorkflowInstance) = value
        """
        ...

    @property
    def InvokedWorkflows(self) -> IList:
        """ Get: InvokedWorkflows(self: SqlTrackingWorkflowInstance) -> IList[SqlTrackingWorkflowInstance] """
        ...

    @property
    def InvokingWorkflowInstanceId(self) -> Guid:
        """
        Get: InvokingWorkflowInstanceId(self: SqlTrackingWorkflowInstance) -> Guid
        Set: InvokingWorkflowInstanceId(self: SqlTrackingWorkflowInstance) = value
        """
        ...

    @property
    def Status(self) -> WorkflowStatus:
        """
        Get: Status(self: SqlTrackingWorkflowInstance) -> WorkflowStatus
        Set: Status(self: SqlTrackingWorkflowInstance) = value
        """
        ...

    @property
    def UserEvents(self) -> IList:
        """ Get: UserEvents(self: SqlTrackingWorkflowInstance) -> IList[UserTrackingRecord] """
        ...

    @property
    def WorkflowDefinition(self) -> Activity:
        """ Get: WorkflowDefinition(self: SqlTrackingWorkflowInstance) -> Activity """
        ...

    @property
    def WorkflowDefinitionUpdated(self) -> bool:
        """ Get: WorkflowDefinitionUpdated(self: SqlTrackingWorkflowInstance) -> bool """
        ...

    @property
    def WorkflowEvents(self) -> IList:
        """ Get: WorkflowEvents(self: SqlTrackingWorkflowInstance) -> IList[WorkflowTrackingRecord] """
        ...

    @property
    def WorkflowInstanceId(self) -> Guid:
        """
        Get: WorkflowInstanceId(self: SqlTrackingWorkflowInstance) -> Guid
        Set: WorkflowInstanceId(self: SqlTrackingWorkflowInstance) = value
        """
        ...

    @property
    def WorkflowInstanceInternalId(self) -> Int64:
        """
        Get: WorkflowInstanceInternalId(self: SqlTrackingWorkflowInstance) -> Int64
        Set: WorkflowInstanceInternalId(self: SqlTrackingWorkflowInstance) = value
        """
        ...

    @property
    def WorkflowType(self) -> Type:
        """
        Get: WorkflowType(self: SqlTrackingWorkflowInstance) -> Type
        Set: WorkflowType(self: SqlTrackingWorkflowInstance) = value
        """
        ...


    def Refresh(self): # -> 
        """ Refresh(self: SqlTrackingWorkflowInstance) """
        ...


class TrackingAnnotationCollection(List): # skipped bases: <type 'IReadOnlyCollection[str]'>, <type 'IList[str]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IEnumerable[str]'>, <type 'ICollection[str]'>, <type 'IReadOnlyList[str]'>, <type 'ICollection'>, <type 'object'>
    """
    TrackingAnnotationCollection()
    TrackingAnnotationCollection(annotations: IEnumerable[str])
    """
    pass

class TrackingChannel: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def InstanceCompletedOrTerminated(self, *args): #cannot find CLR method
        """ InstanceCompletedOrTerminated(self: TrackingChannel) """
        ...

    def Send(self, *args): #cannot find CLR method
        """ Send(self: TrackingChannel, record: TrackingRecord) """
        ...


class TrackingConditionCollection(List): # skipped bases: <type 'IReadOnlyList[TrackingCondition]'>, <type 'IReadOnlyCollection[TrackingCondition]'>, <type 'IList[TrackingCondition]'>, <type 'IEnumerable[TrackingCondition]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'ICollection[TrackingCondition]'>, <type 'ICollection'>, <type 'object'>
    """
    TrackingConditionCollection()
    TrackingConditionCollection(conditions: IEnumerable[TrackingCondition])
    """
    pass

class TrackingDataItem: # skipped bases: <type 'object'>, <type 'object'>
    """ TrackingDataItem() """
    @property
    def Annotations(self) -> TrackingAnnotationCollection:
        """ Get: Annotations(self: TrackingDataItem) -> TrackingAnnotationCollection """
        ...

    @property
    def Data(self) -> object:
        """
        Get: Data(self: TrackingDataItem) -> object
        Set: Data(self: TrackingDataItem) = value
        """
        ...

    @property
    def FieldName(self) -> str:
        """
        Get: FieldName(self: TrackingDataItem) -> str
        Set: FieldName(self: TrackingDataItem) = value
        """
        ...



class TrackingDataItemValue: # skipped bases: <type 'object'>, <type 'object'>
    """
    TrackingDataItemValue()
    TrackingDataItemValue(qualifiedName: str, fieldName: str, dataValue: str)
    """
    @property
    def DataValue(self) -> str:
        """
        Get: DataValue(self: TrackingDataItemValue) -> str
        Set: DataValue(self: TrackingDataItemValue) = value
        """
        ...

    @property
    def FieldName(self) -> str:
        """
        Get: FieldName(self: TrackingDataItemValue) -> str
        Set: FieldName(self: TrackingDataItemValue) = value
        """
        ...

    @property
    def QualifiedName(self) -> str:
        """
        Get: QualifiedName(self: TrackingDataItemValue) -> str
        Set: QualifiedName(self: TrackingDataItemValue) = value
        """
        ...



class TrackingParameters: # skipped bases: <type 'object'>, <type 'object'>
    """ TrackingParameters(instanceId: Guid, workflowType: Type, rootActivity: Activity, callPath: IList[str], callerInstanceId: Guid, contextGuid: Guid, callerContextGuid: Guid, callerParentContextGuid: Guid) """
    @property
    def CallerContextGuid(self) -> Guid:
        """ Get: CallerContextGuid(self: TrackingParameters) -> Guid """
        ...

    @property
    def CallerInstanceId(self) -> Guid:
        """ Get: CallerInstanceId(self: TrackingParameters) -> Guid """
        ...

    @property
    def CallerParentContextGuid(self) -> Guid:
        """ Get: CallerParentContextGuid(self: TrackingParameters) -> Guid """
        ...

    @property
    def CallPath(self) -> IList:
        """ Get: CallPath(self: TrackingParameters) -> IList[str] """
        ...

    @property
    def ContextGuid(self) -> Guid:
        """ Get: ContextGuid(self: TrackingParameters) -> Guid """
        ...

    @property
    def InstanceId(self) -> Guid:
        """ Get: InstanceId(self: TrackingParameters) -> Guid """
        ...

    @property
    def RootActivity(self) -> Activity:
        """ Get: RootActivity(self: TrackingParameters) -> Activity """
        ...

    @property
    def WorkflowType(self) -> Type:
        """ Get: WorkflowType(self: TrackingParameters) -> Type """
        ...



class TrackingProfile: # skipped bases: <type 'object'>, <type 'object'>
    """ TrackingProfile() """
    @property
    def ActivityTrackPoints(self) -> ActivityTrackPointCollection:
        """ Get: ActivityTrackPoints(self: TrackingProfile) -> ActivityTrackPointCollection """
        ...

    @property
    def UserTrackPoints(self) -> UserTrackPointCollection:
        """ Get: UserTrackPoints(self: TrackingProfile) -> UserTrackPointCollection """
        ...

    @property
    def Version(self) -> Version:
        """
        Get: Version(self: TrackingProfile) -> Version
        Set: Version(self: TrackingProfile) = value
        """
        ...

    @property
    def WorkflowTrackPoints(self) -> WorkflowTrackPointCollection:
        """ Get: WorkflowTrackPoints(self: TrackingProfile) -> WorkflowTrackPointCollection """
        ...



class TrackingProfileCache: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Clear(): # -> 
        """ Clear() """
        ...

    __all__: list = ...


class TrackingProfileDeserializationException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    TrackingProfileDeserializationException()
    TrackingProfileDeserializationException(message: str)
    TrackingProfileDeserializationException(message: str, innerException: Exception)
    """
    @property
    def ValidationEventArgs(self) -> IList:
        """ Get: ValidationEventArgs(self: TrackingProfileDeserializationException) -> IList[ValidationEventArgs] """
        ...


    SerializeObjectState = ...


class TrackingProfileSerializer: # skipped bases: <type 'object'>, <type 'object'>
    """ TrackingProfileSerializer() """
    @property
    def Schema(self) -> XmlSchema:
        """ Get: Schema(self: TrackingProfileSerializer) -> XmlSchema """
        ...


    def Deserialize(self, reader:TextReader) -> TrackingProfile:
        """ Deserialize(self: TrackingProfileSerializer, reader: TextReader) -> TrackingProfile """
        ...

    def Serialize(self, writer:TextWriter, profile:TrackingProfile): # -> 
        """ Serialize(self: TrackingProfileSerializer, writer: TextWriter, profile: TrackingProfile) """
        ...


class TrackingWorkflowChangedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Changes(self) -> IList:
        """ Get: Changes(self: TrackingWorkflowChangedEventArgs) -> IList[WorkflowChangeAction] """
        ...

    @property
    def Definition(self) -> Activity:
        """ Get: Definition(self: TrackingWorkflowChangedEventArgs) -> Activity """
        ...



class TrackingWorkflowEvent(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TrackingWorkflowEvent, values: Aborted (10), Changed (11), Completed (1), Created (0), Exception (8), Idle (2), Loaded (7), Persisted (5), Resumed (4), Started (12), Suspended (3), Terminated (9), Unloaded (6) """
    Aborted: TrackingWorkflowEvent = ...
    Changed: TrackingWorkflowEvent = ...
    Completed: TrackingWorkflowEvent = ...
    Created: TrackingWorkflowEvent = ...
    Exception: TrackingWorkflowEvent = ...
    Idle: TrackingWorkflowEvent = ...
    Loaded: TrackingWorkflowEvent = ...
    Persisted: TrackingWorkflowEvent = ...
    Resumed: TrackingWorkflowEvent = ...
    Started: TrackingWorkflowEvent = ...
    Suspended: TrackingWorkflowEvent = ...
    Terminated: TrackingWorkflowEvent = ...
    Unloaded: TrackingWorkflowEvent = ...
    value__ = ...


class TrackingWorkflowExceptionEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ContextGuid(self) -> Guid:
        """ Get: ContextGuid(self: TrackingWorkflowExceptionEventArgs) -> Guid """
        ...

    @property
    def CurrentActivityPath(self) -> str:
        """ Get: CurrentActivityPath(self: TrackingWorkflowExceptionEventArgs) -> str """
        ...

    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: TrackingWorkflowExceptionEventArgs) -> Exception """
        ...

    @property
    def OriginalActivityPath(self) -> str:
        """ Get: OriginalActivityPath(self: TrackingWorkflowExceptionEventArgs) -> str """
        ...

    @property
    def ParentContextGuid(self) -> Guid:
        """ Get: ParentContextGuid(self: TrackingWorkflowExceptionEventArgs) -> Guid """
        ...



class TrackingWorkflowSuspendedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Error(self) -> str:
        """ Get: Error(self: TrackingWorkflowSuspendedEventArgs) -> str """
        ...



class TrackingWorkflowTerminatedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Exception(self) -> Exception:
        """ Get: Exception(self: TrackingWorkflowTerminatedEventArgs) -> Exception """
        ...



class UserTrackingLocation: # skipped bases: <type 'object'>, <type 'object'>
    """
    UserTrackingLocation()
    UserTrackingLocation(argumentType: Type)
    UserTrackingLocation(argumentType: Type, activityType: Type)
    UserTrackingLocation(argumentType: Type, activityTypeName: str)
    UserTrackingLocation(argumentTypeName: str)
    UserTrackingLocation(argumentTypeName: str, activityTypeName: str)
    UserTrackingLocation(argumentTypeName: str, activityType: Type)
    """
    @property
    def ActivityType(self) -> Type:
        """
        Get: ActivityType(self: UserTrackingLocation) -> Type
        Set: ActivityType(self: UserTrackingLocation) = value
        """
        ...

    @property
    def ActivityTypeName(self) -> str:
        """
        Get: ActivityTypeName(self: UserTrackingLocation) -> str
        Set: ActivityTypeName(self: UserTrackingLocation) = value
        """
        ...

    @property
    def ArgumentType(self) -> Type:
        """
        Get: ArgumentType(self: UserTrackingLocation) -> Type
        Set: ArgumentType(self: UserTrackingLocation) = value
        """
        ...

    @property
    def ArgumentTypeName(self) -> str:
        """
        Get: ArgumentTypeName(self: UserTrackingLocation) -> str
        Set: ArgumentTypeName(self: UserTrackingLocation) = value
        """
        ...

    @property
    def Conditions(self) -> TrackingConditionCollection:
        """ Get: Conditions(self: UserTrackingLocation) -> TrackingConditionCollection """
        ...

    @property
    def KeyName(self) -> str:
        """
        Get: KeyName(self: UserTrackingLocation) -> str
        Set: KeyName(self: UserTrackingLocation) = value
        """
        ...

    @property
    def MatchDerivedActivityTypes(self) -> bool:
        """
        Get: MatchDerivedActivityTypes(self: UserTrackingLocation) -> bool
        Set: MatchDerivedActivityTypes(self: UserTrackingLocation) = value
        """
        ...

    @property
    def MatchDerivedArgumentTypes(self) -> bool:
        """
        Get: MatchDerivedArgumentTypes(self: UserTrackingLocation) -> bool
        Set: MatchDerivedArgumentTypes(self: UserTrackingLocation) = value
        """
        ...



class UserTrackingLocationCollection(List): # skipped bases: <type 'IEnumerable[UserTrackingLocation]'>, <type 'IReadOnlyCollection[UserTrackingLocation]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IList[UserTrackingLocation]'>, <type 'ICollection[UserTrackingLocation]'>, <type 'ICollection'>, <type 'IReadOnlyList[UserTrackingLocation]'>, <type 'object'>
    """
    UserTrackingLocationCollection()
    UserTrackingLocationCollection(locations: IEnumerable[UserTrackingLocation])
    """
    pass

class UserTrackingRecord(TrackingRecord): # skipped bases: <type 'object'>
    """
    UserTrackingRecord()
    UserTrackingRecord(activityType: Type, qualifiedName: str, contextGuid: Guid, parentContextGuid: Guid, eventDateTime: DateTime, eventOrder: int, userDataKey: str, userData: object)
    """
    @property
    def ActivityType(self) -> Type:
        """
        Get: ActivityType(self: UserTrackingRecord) -> Type
        Set: ActivityType(self: UserTrackingRecord) = value
        """
        ...

    @property
    def Body(self) -> IList:
        """ Get: Body(self: UserTrackingRecord) -> IList[TrackingDataItem] """
        ...

    @property
    def ContextGuid(self) -> Guid:
        """
        Get: ContextGuid(self: UserTrackingRecord) -> Guid
        Set: ContextGuid(self: UserTrackingRecord) = value
        """
        ...

    @property
    def ParentContextGuid(self) -> Guid:
        """
        Get: ParentContextGuid(self: UserTrackingRecord) -> Guid
        Set: ParentContextGuid(self: UserTrackingRecord) = value
        """
        ...

    @property
    def QualifiedName(self) -> str:
        """
        Get: QualifiedName(self: UserTrackingRecord) -> str
        Set: QualifiedName(self: UserTrackingRecord) = value
        """
        ...

    @property
    def UserData(self) -> object:
        """
        Get: UserData(self: UserTrackingRecord) -> object
        Set: UserData(self: UserTrackingRecord) = value
        """
        ...

    @property
    def UserDataKey(self) -> str:
        """
        Get: UserDataKey(self: UserTrackingRecord) -> str
        Set: UserDataKey(self: UserTrackingRecord) = value
        """
        ...


    def __new__(cls, activityType:Type = ..., qualifiedName:str = ..., contextGuid:Guid = ..., parentContextGuid:Guid = ..., eventDateTime:DateTime = ..., eventOrder:int = ..., userDataKey:str = ..., userData:object = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, activityType: Type, qualifiedName: str, contextGuid: Guid, parentContextGuid: Guid, eventDateTime: DateTime, eventOrder: int, userDataKey: str, userData: object)
        """
        ...


class UserTrackPoint: # skipped bases: <type 'object'>, <type 'object'>
    """ UserTrackPoint() """
    @property
    def Annotations(self) -> TrackingAnnotationCollection:
        """ Get: Annotations(self: UserTrackPoint) -> TrackingAnnotationCollection """
        ...

    @property
    def ExcludedLocations(self) -> UserTrackingLocationCollection:
        """ Get: ExcludedLocations(self: UserTrackPoint) -> UserTrackingLocationCollection """
        ...

    @property
    def Extracts(self) -> ExtractCollection:
        """ Get: Extracts(self: UserTrackPoint) -> ExtractCollection """
        ...

    @property
    def MatchingLocations(self) -> UserTrackingLocationCollection:
        """ Get: MatchingLocations(self: UserTrackPoint) -> UserTrackingLocationCollection """
        ...



class UserTrackPointCollection(List): # skipped bases: <type 'IEnumerable[UserTrackPoint]'>, <type 'IReadOnlyCollection[UserTrackPoint]'>, <type 'IReadOnlyList[UserTrackPoint]'>, <type 'IEnumerable'>, <type 'ICollection[UserTrackPoint]'>, <type 'IList[UserTrackPoint]'>, <type 'IList'>, <type 'ICollection'>, <type 'object'>
    """
    UserTrackPointCollection()
    UserTrackPointCollection(points: IEnumerable[UserTrackPoint])
    """
    pass

class WorkflowDataTrackingExtract(TrackingExtract): # skipped bases: <type 'object'>
    """
    WorkflowDataTrackingExtract()
    WorkflowDataTrackingExtract(member: str)
    """
    def __new__(cls, member:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, member: str)
        """
        ...


class WorkflowTrackingLocation: # skipped bases: <type 'object'>, <type 'object'>
    """
    WorkflowTrackingLocation()
    WorkflowTrackingLocation(events: IList[TrackingWorkflowEvent])
    """
    @property
    def Events(self) -> IList:
        """ Get: Events(self: WorkflowTrackingLocation) -> IList[TrackingWorkflowEvent] """
        ...



class WorkflowTrackingRecord(TrackingRecord): # skipped bases: <type 'object'>
    """
    WorkflowTrackingRecord()
    WorkflowTrackingRecord(trackingWorkflowEvent: TrackingWorkflowEvent, eventDateTime: DateTime, eventOrder: int, eventArgs: EventArgs)
    """
    @property
    def TrackingWorkflowEvent(self) -> TrackingWorkflowEvent:
        """
        Get: TrackingWorkflowEvent(self: WorkflowTrackingRecord) -> TrackingWorkflowEvent
        Set: TrackingWorkflowEvent(self: WorkflowTrackingRecord) = value
        """
        ...


    def __new__(cls, trackingWorkflowEvent:TrackingWorkflowEvent = ..., eventDateTime:DateTime = ..., eventOrder:int = ..., eventArgs:EventArgs = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, trackingWorkflowEvent: TrackingWorkflowEvent, eventDateTime: DateTime, eventOrder: int, eventArgs: EventArgs)
        """
        ...


class WorkflowTrackPoint: # skipped bases: <type 'object'>, <type 'object'>
    """ WorkflowTrackPoint() """
    @property
    def Annotations(self) -> TrackingAnnotationCollection:
        """ Get: Annotations(self: WorkflowTrackPoint) -> TrackingAnnotationCollection """
        ...

    @property
    def MatchingLocation(self) -> WorkflowTrackingLocation:
        """
        Get: MatchingLocation(self: WorkflowTrackPoint) -> WorkflowTrackingLocation
        Set: MatchingLocation(self: WorkflowTrackPoint) = value
        """
        ...



class WorkflowTrackPointCollection(List): # skipped bases: <type 'IReadOnlyCollection[WorkflowTrackPoint]'>, <type 'IEnumerable[WorkflowTrackPoint]'>, <type 'IList[WorkflowTrackPoint]'>, <type 'IEnumerable'>, <type 'ICollection[WorkflowTrackPoint]'>, <type 'IList'>, <type 'IReadOnlyList[WorkflowTrackPoint]'>, <type 'ICollection'>, <type 'object'>
    """
    WorkflowTrackPointCollection()
    WorkflowTrackPointCollection(points: IEnumerable[WorkflowTrackPoint])
    """
    pass

