# encoding: utf-8
# module System.Activities.DynamicUpdate calls itself DynamicUpdate
# from System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array

from System.Activities import (ActivityAction, ActivityBuilder, 
    ActivityDelegate, Argument, Bookmark, BookmarkScope, CompletionCallback, 
    DelegateCompletionCallback, FaultCallback, Location, 
    LocationReferenceEnvironment, Variable)

from System.Collections import IDictionary, IList

from System.Collections.Generic import ISet

from System.EnterpriseServices import Activity

"""The following names are not found in the module: (ActivityFunc, BoundEvent, 
    Func)
"""

# no functions
# classes

class ActivityBlockingUpdate: # skipped bases: <type 'object'>, <type 'object'>
    """
    ActivityBlockingUpdate(activity: Activity, originalActivityId: str, reason: str)
    ActivityBlockingUpdate(activity: Activity, originalActivityId: str, reason: str, activityInstanceId: str)
    ActivityBlockingUpdate(updatedActivityId: str, originalActivityId: str, reason: str)
    ActivityBlockingUpdate(updatedActivityId: str, originalActivityId: str, reason: str, activityInstanceId: str)
    """
    @property
    def Activity(self) -> Activity:
        """ Get: Activity(self: ActivityBlockingUpdate) -> Activity """
        ...

    @property
    def ActivityInstanceId(self) -> str:
        """ Get: ActivityInstanceId(self: ActivityBlockingUpdate) -> str """
        ...

    @property
    def OriginalActivityId(self) -> str:
        """ Get: OriginalActivityId(self: ActivityBlockingUpdate) -> str """
        ...

    @property
    def Reason(self) -> str:
        """ Get: Reason(self: ActivityBlockingUpdate) -> str """
        ...

    @property
    def UpdatedActivityId(self) -> str:
        """ Get: UpdatedActivityId(self: ActivityBlockingUpdate) -> str """
        ...



class DynamicUpdateInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetMapItem(instance:object) -> DynamicUpdateMapItem:
        """ GetMapItem(instance: object) -> DynamicUpdateMapItem """
        ...

    @staticmethod
    def GetOriginalActivityBuilder(instance:object) -> ActivityBuilder:
        """ GetOriginalActivityBuilder(instance: object) -> ActivityBuilder """
        ...

    @staticmethod
    def GetOriginalDefinition(instance:object) -> Activity:
        """ GetOriginalDefinition(instance: object) -> Activity """
        ...

    @staticmethod
    def SetMapItem(instance:object, mapItem:DynamicUpdateMapItem): # -> 
        """ SetMapItem(instance: object, mapItem: DynamicUpdateMapItem) """
        ...

    @staticmethod
    def SetOriginalActivityBuilder(instance:object, originalActivityBuilder:ActivityBuilder): # -> 
        """ SetOriginalActivityBuilder(instance: object, originalActivityBuilder: ActivityBuilder) """
        ...

    @staticmethod
    def SetOriginalDefinition(instance:object, originalDefinition:Activity): # -> 
        """ SetOriginalDefinition(instance: object, originalDefinition: Activity) """
        ...

    __all__: list = ...


class DynamicUpdateMap: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def NoChanges(self) -> DynamicUpdateMap:
        """ Get: NoChanges() -> DynamicUpdateMap """
        ...


    @staticmethod
    def CalculateImplementationMapItems(activityDefinitionToBeUpdated:Activity, environment:LocationReferenceEnvironment = ...) -> IDictionary:
        """
        CalculateImplementationMapItems(activityDefinitionToBeUpdated: Activity) -> IDictionary[object, DynamicUpdateMapItem]
        CalculateImplementationMapItems(activityDefinitionToBeUpdated: Activity, environment: LocationReferenceEnvironment) -> IDictionary[object, DynamicUpdateMapItem]
        """
        ...

    @staticmethod
    def CalculateMapItems(workflowDefinitionToBeUpdated:Activity, environment:LocationReferenceEnvironment = ...) -> IDictionary:
        """
        CalculateMapItems(workflowDefinitionToBeUpdated: Activity) -> IDictionary[object, DynamicUpdateMapItem]
        CalculateMapItems(workflowDefinitionToBeUpdated: Activity, environment: LocationReferenceEnvironment) -> IDictionary[object, DynamicUpdateMapItem]
        """
        ...

    @staticmethod
    def Merge(maps:Array) -> DynamicUpdateMap:
        """
        Merge(*maps: Array[DynamicUpdateMap]) -> DynamicUpdateMap
        Merge(maps: IEnumerable[DynamicUpdateMap]) -> DynamicUpdateMap
        """
        ...

    def Query(self, updatedWorkflowDefinition:Activity, originalWorkflowDefinition:Activity) -> DynamicUpdateMapQuery:
        """ Query(self: DynamicUpdateMap, updatedWorkflowDefinition: Activity, originalWorkflowDefinition: Activity) -> DynamicUpdateMapQuery """
        ...



class DynamicUpdateMapBuilder: # skipped bases: <type 'object'>, <type 'object'>
    """ DynamicUpdateMapBuilder() """
    @property
    def DisallowUpdateInside(self) -> ISet:
        """ Get: DisallowUpdateInside(self: DynamicUpdateMapBuilder) -> ISet[Activity] """
        ...

    @property
    def ForImplementation(self) -> bool:
        """
        Get: ForImplementation(self: DynamicUpdateMapBuilder) -> bool
        Set: ForImplementation(self: DynamicUpdateMapBuilder) = value
        """
        ...

    @property
    def LookupImplementationMap(self): # -> Func
        """
        Get: LookupImplementationMap(self: DynamicUpdateMapBuilder) -> Func[Activity, DynamicUpdateMap]
        Set: LookupImplementationMap(self: DynamicUpdateMapBuilder) = value
        """
        ...

    @property
    def LookupMapItem(self): # -> Func
        """
        Get: LookupMapItem(self: DynamicUpdateMapBuilder) -> Func[object, DynamicUpdateMapItem]
        Set: LookupMapItem(self: DynamicUpdateMapBuilder) = value
        """
        ...

    @property
    def OriginalEnvironment(self) -> LocationReferenceEnvironment:
        """
        Get: OriginalEnvironment(self: DynamicUpdateMapBuilder) -> LocationReferenceEnvironment
        Set: OriginalEnvironment(self: DynamicUpdateMapBuilder) = value
        """
        ...

    @property
    def OriginalWorkflowDefinition(self) -> Activity:
        """
        Get: OriginalWorkflowDefinition(self: DynamicUpdateMapBuilder) -> Activity
        Set: OriginalWorkflowDefinition(self: DynamicUpdateMapBuilder) = value
        """
        ...

    @property
    def UpdatedEnvironment(self) -> LocationReferenceEnvironment:
        """
        Get: UpdatedEnvironment(self: DynamicUpdateMapBuilder) -> LocationReferenceEnvironment
        Set: UpdatedEnvironment(self: DynamicUpdateMapBuilder) = value
        """
        ...

    @property
    def UpdatedWorkflowDefinition(self) -> Activity:
        """
        Get: UpdatedWorkflowDefinition(self: DynamicUpdateMapBuilder) -> Activity
        Set: UpdatedWorkflowDefinition(self: DynamicUpdateMapBuilder) = value
        """
        ...


    def CreateMap(self, activitiesBlockingUpdate=None) -> DynamicUpdateMap:
        """
        CreateMap(self: DynamicUpdateMapBuilder) -> DynamicUpdateMap
        CreateMap(self: DynamicUpdateMapBuilder) -> (DynamicUpdateMap, IList[ActivityBlockingUpdate])
        """
        ...


class DynamicUpdateMapItem: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class DynamicUpdateMapQuery: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CanApplyUpdateWhileRunning(self, activity:Activity) -> bool:
        """ CanApplyUpdateWhileRunning(self: DynamicUpdateMapQuery, activity: Activity) -> bool """
        ...

    def FindMatch(self, *__args:Activity) -> Activity:
        """
        FindMatch(self: DynamicUpdateMapQuery, activity: Activity) -> Activity
        FindMatch(self: DynamicUpdateMapQuery, variable: Variable) -> Variable
        """
        ...


class DynamicUpdateServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateUpdateMap(*__args:Activity) -> DynamicUpdateMap:
        """
        CreateUpdateMap(updatedWorkflowDefinition: Activity) -> DynamicUpdateMap
        CreateUpdateMap(updatedWorkflowDefinition: Activity, disallowUpdateInsideActivities: IEnumerable[Activity]) -> DynamicUpdateMap
        CreateUpdateMap(updatedActivityDefinition: ActivityBuilder) -> DynamicUpdateMap
        CreateUpdateMap(updatedActivityDefinition: ActivityBuilder, disallowUpdateInsideActivities: IEnumerable[Activity]) -> DynamicUpdateMap
        CreateUpdateMap(updatedWorkflowDefinition: Activity, disallowUpdateInsideActivities: IEnumerable[Activity]) -> (DynamicUpdateMap, IList[ActivityBlockingUpdate])
        CreateUpdateMap(updatedActivityDefinition: ActivityBuilder, disallowUpdateInsideActivities: IEnumerable[Activity]) -> (DynamicUpdateMap, IList[ActivityBlockingUpdate])
        """
        ...

    @staticmethod
    def GetImplementationMap(targetActivity:Activity) -> DynamicUpdateMap:
        """ GetImplementationMap(targetActivity: Activity) -> DynamicUpdateMap """
        ...

    @staticmethod
    def PrepareForUpdate(*__args:Activity): # -> 
        """ PrepareForUpdate(workflowDefinitionToBeUpdated: Activity)PrepareForUpdate(activityDefinitionToBeUpdated: ActivityBuilder) """
        ...

    @staticmethod
    def SetImplementationMap(targetActivity:Activity, implementationMap:DynamicUpdateMap): # -> 
        """ SetImplementationMap(targetActivity: Activity, implementationMap: DynamicUpdateMap) """
        ...

    __all__: list = ...


class InstanceUpdateException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    InstanceUpdateException()
    InstanceUpdateException(message: str)
    InstanceUpdateException(message: str, innerException: Exception)
    InstanceUpdateException(blockingActivities: IList[ActivityBlockingUpdate])
    InstanceUpdateException(message: str, blockingActivities: IList[ActivityBlockingUpdate])
    InstanceUpdateException(message: str, blockingActivities: IList[ActivityBlockingUpdate], innerException: Exception)
    """
    @property
    def BlockingActivities(self) -> IList:
        """ Get: BlockingActivities(self: InstanceUpdateException) -> IList[ActivityBlockingUpdate] """
        ...


    SerializeObjectState = ...


class NativeActivityUpdateContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ActivityInstanceId(self) -> str:
        """ Get: ActivityInstanceId(self: NativeActivityUpdateContext) -> str """
        ...

    @property
    def DefaultBookmarkScope(self) -> BookmarkScope:
        """ Get: DefaultBookmarkScope(self: NativeActivityUpdateContext) -> BookmarkScope """
        ...

    @property
    def IsCancellationRequested(self) -> bool:
        """ Get: IsCancellationRequested(self: NativeActivityUpdateContext) -> bool """
        ...


    def CreateBookmark(self, *__args:str) -> Bookmark:
        """
        CreateBookmark(self: NativeActivityUpdateContext, name: str) -> Bookmark
        CreateBookmark(self: NativeActivityUpdateContext, name: str, callback: BookmarkCallback) -> Bookmark
        CreateBookmark(self: NativeActivityUpdateContext, name: str, callback: BookmarkCallback, options: BookmarkOptions) -> Bookmark
        CreateBookmark(self: NativeActivityUpdateContext, name: str, callback: BookmarkCallback, scope: BookmarkScope) -> Bookmark
        CreateBookmark(self: NativeActivityUpdateContext, name: str, callback: BookmarkCallback, scope: BookmarkScope, options: BookmarkOptions) -> Bookmark
        CreateBookmark(self: NativeActivityUpdateContext) -> Bookmark
        CreateBookmark(self: NativeActivityUpdateContext, callback: BookmarkCallback) -> Bookmark
        CreateBookmark(self: NativeActivityUpdateContext, callback: BookmarkCallback, options: BookmarkOptions) -> Bookmark
        """
        ...

    def DisallowUpdate(self, reason:str): # -> 
        """ DisallowUpdate(self: NativeActivityUpdateContext, reason: str) """
        ...

    def FindExecutionProperty(self, name:str) -> object:
        """ FindExecutionProperty(self: NativeActivityUpdateContext, name: str) -> object """
        ...

    def GetLocation(self, variable:Variable) -> Location:
        """ GetLocation[T](self: NativeActivityUpdateContext, variable: Variable) -> Location[T] """
        ...

    def GetSavedOriginalValue(self, *__args:Activity) -> object:
        """
        GetSavedOriginalValue(self: NativeActivityUpdateContext, childActivity: Activity) -> object
        GetSavedOriginalValue(self: NativeActivityUpdateContext, propertyName: str) -> object
        """
        ...

    def GetValue(self, *__args:Argument) -> object:
        """
        GetValue(self: NativeActivityUpdateContext, argument: Argument) -> object
        GetValue(self: NativeActivityUpdateContext, runtimeArgument: RuntimeArgument) -> object
        GetValue(self: NativeActivityUpdateContext, variable: Variable) -> object
        GetValue[T](self: NativeActivityUpdateContext, variable: Variable[T]) -> T
        """
        ...

    def IsNewlyAdded(self, childActivity:Activity) -> bool:
        """ IsNewlyAdded(self: NativeActivityUpdateContext, childActivity: Activity) -> bool """
        ...

    def RemoveAllBookmarks(self): # -> 
        """ RemoveAllBookmarks(self: NativeActivityUpdateContext) """
        ...

    def RemoveBookmark(self, *__args:str) -> bool:
        """
        RemoveBookmark(self: NativeActivityUpdateContext, name: str) -> bool
        RemoveBookmark(self: NativeActivityUpdateContext, bookmark: Bookmark) -> bool
        RemoveBookmark(self: NativeActivityUpdateContext, name: str, scope: BookmarkScope) -> bool
        """
        ...

    def ScheduleAction(self, activityAction, *__args): # -> 
        """ ScheduleAction(self: NativeActivityUpdateContext, activityAction: ActivityAction, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14)](self: NativeActivityUpdateContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, argument13: T13, argument14: T14, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13)](self: NativeActivityUpdateContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, argument13: T13, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12)](self: NativeActivityUpdateContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11)](self: NativeActivityUpdateContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10)](self: NativeActivityUpdateContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8, T9)](self: NativeActivityUpdateContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8, T9], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15)](self: NativeActivityUpdateContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, argument13: T13, argument14: T14, argument15: T15, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8)](self: NativeActivityUpdateContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleAction[(T1, T2, T3, T4, T5, T6)](self: NativeActivityUpdateContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleAction[(T1, T2, T3, T4, T5)](self: NativeActivityUpdateContext, activityAction: ActivityAction[T1, T2, T3, T4, T5], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleAction[(T1, T2, T3, T4)](self: NativeActivityUpdateContext, activityAction: ActivityAction[T1, T2, T3, T4], argument1: T1, argument2: T2, argument3: T3, argument4: T4, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleAction[(T1, T2, T3)](self: NativeActivityUpdateContext, activityAction: ActivityAction[T1, T2, T3], argument1: T1, argument2: T2, argument3: T3, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleAction[(T1, T2)](self: NativeActivityUpdateContext, activityAction: ActivityAction[T1, T2], argument1: T1, argument2: T2, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleAction[T](self: NativeActivityUpdateContext, activityAction: ActivityAction[T], argument: T, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleAction[(T1, T2, T3, T4, T5, T6, T7)](self: NativeActivityUpdateContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleAction[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16)](self: NativeActivityUpdateContext, activityAction: ActivityAction[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, argument13: T13, argument14: T14, argument15: T15, argument16: T16, onCompleted: CompletionCallback, onFaulted: FaultCallback) """
        ...

    def ScheduleActivity(self, activity:Activity, *__args:CompletionCallback): # -> 
        """ ScheduleActivity(self: NativeActivityUpdateContext, activity: Activity)ScheduleActivity(self: NativeActivityUpdateContext, activity: Activity, onCompleted: CompletionCallback)ScheduleActivity(self: NativeActivityUpdateContext, activity: Activity, onFaulted: FaultCallback)ScheduleActivity(self: NativeActivityUpdateContext, activity: Activity, onCompleted: CompletionCallback, onFaulted: FaultCallback)ScheduleActivity[TResult](self: NativeActivityUpdateContext, activity: Activity[TResult], onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) """
        ...

    def ScheduleDelegate(self, activityDelegate:ActivityDelegate, inputParameters:IDictionary, onCompleted:DelegateCompletionCallback, onFaulted:FaultCallback): # -> 
        """ ScheduleDelegate(self: NativeActivityUpdateContext, activityDelegate: ActivityDelegate, inputParameters: IDictionary[str, object], onCompleted: DelegateCompletionCallback, onFaulted: FaultCallback) """
        ...

    def ScheduleFunc(self, activityFunc, *__args): # -> 
        """ ScheduleFunc[TResult](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[TResult], onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback)ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TResult)](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, argument13: T13, argument14: T14, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback)ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TResult)](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, argument13: T13, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback)ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TResult)](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback)ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TResult)](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback)ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TResult)](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback)ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, T9, TResult)](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, T9, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback)ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TResult)](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, argument13: T13, argument14: T14, argument15: T15, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback)ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, TResult)](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback)ScheduleFunc[(T1, T2, T3, T4, T5, T6, TResult)](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback)ScheduleFunc[(T1, T2, T3, T4, T5, TResult)](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback)ScheduleFunc[(T1, T2, T3, T4, TResult)](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[T1, T2, T3, T4, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback)ScheduleFunc[(T1, T2, T3, TResult)](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[T1, T2, T3, TResult], argument1: T1, argument2: T2, argument3: T3, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback)ScheduleFunc[(T1, T2, TResult)](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[T1, T2, TResult], argument1: T1, argument2: T2, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback)ScheduleFunc[(T, TResult)](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[T, TResult], argument: T, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback)ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, TResult)](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback)ScheduleFunc[(T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, TResult)](self: NativeActivityUpdateContext, activityFunc: ActivityFunc[T1, T2, T3, T4, T5, T6, T7, T8, T9, T10, T11, T12, T13, T14, T15, T16, TResult], argument1: T1, argument2: T2, argument3: T3, argument4: T4, argument5: T5, argument6: T6, argument7: T7, argument8: T8, argument9: T9, argument10: T10, argument11: T11, argument12: T12, argument13: T13, argument14: T14, argument15: T15, argument16: T16, onCompleted: CompletionCallback[TResult], onFaulted: FaultCallback) """
        ...

    def SetValue(self, *__args): # -> 
        """ SetValue(self: NativeActivityUpdateContext, argument: Argument, value: object)SetValue(self: NativeActivityUpdateContext, variable: Variable, value: object)SetValue[T](self: NativeActivityUpdateContext, variable: Variable[T], value: T) """
        ...


class UpdateMapMetadata: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def AddMatch(self, *__args): # -> 
        """ AddMatch(self: UpdateMapMetadata, updatedChild: Activity, originalChild: Activity)AddMatch(self: UpdateMapMetadata, updatedVariable: Variable, originalVariable: Variable) """
        ...

    def AllowUpdateInsideThisActivity(self): # -> 
        """ AllowUpdateInsideThisActivity(self: UpdateMapMetadata) """
        ...

    def DisallowUpdateInsideThisActivity(self, reason:str): # -> 
        """ DisallowUpdateInsideThisActivity(self: UpdateMapMetadata, reason: str) """
        ...

    def GetMatch(self, *__args:Activity) -> Activity:
        """
        GetMatch(self: UpdateMapMetadata, updatedChild: Activity) -> Activity
        GetMatch(self: UpdateMapMetadata, updatedVariable: Variable) -> Variable
        """
        ...

    def IsReferenceToImportedChild(self, childActivity:Activity) -> bool:
        """ IsReferenceToImportedChild(self: UpdateMapMetadata, childActivity: Activity) -> bool """
        ...


class NativeActivityUpdateMapMetadata(UpdateMapMetadata): # skipped bases: <type 'object'>
    """ no doc """
    def SaveOriginalValue(self, *__args): # -> 
        """ SaveOriginalValue(self: NativeActivityUpdateMapMetadata, updatedChildActivity: Activity, originalValue: object)SaveOriginalValue(self: NativeActivityUpdateMapMetadata, propertyName: str, originalValue: object) """
        ...


