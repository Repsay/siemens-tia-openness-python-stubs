# encoding: utf-8
# module System.Activities.Hosting calls itself Hosting
# from System.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, AsyncCallback, Enum, Guid, IAsyncResult

from System.Activities import (Bookmark, BookmarkResumptionResult, 
    LocationReferenceEnvironment, WorkflowIdentity)

from System.Collections import IDictionary, IEnumerable, IEnumerator

from System.Collections.Generic import KeyValuePair

from System.EnterpriseServices import Activity

from System.Threading import SynchronizationContext

"""The following names are not found in the module: field#
"""

# no functions
# classes

class BookmarkInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BookmarkName(self) -> str:
        """ Get: BookmarkName(self: BookmarkInfo) -> str """
        ...

    @property
    def OwnerDisplayName(self) -> str:
        """ Get: OwnerDisplayName(self: BookmarkInfo) -> str """
        ...

    @property
    def ScopeInfo(self) -> BookmarkScopeInfo:
        """ Get: ScopeInfo(self: BookmarkInfo) -> BookmarkScopeInfo """
        ...



class BookmarkScopeInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Id(self) -> Guid:
        """ Get: Id(self: BookmarkScopeInfo) -> Guid """
        ...

    @property
    def IsInitialized(self) -> bool:
        """ Get: IsInitialized(self: BookmarkScopeInfo) -> bool """
        ...

    @property
    def TemporaryId(self) -> str:
        """ Get: TemporaryId(self: BookmarkScopeInfo) -> str """
        ...



class IWorkflowInstanceExtension: # skipped bases: <type 'object'>
    """ no doc """
    def GetAdditionalExtensions(self) -> IEnumerable:
        """ GetAdditionalExtensions(self: IWorkflowInstanceExtension) -> IEnumerable[object] """
        ...

    def SetInstance(self, instance:WorkflowInstanceProxy): # -> 
        """ SetInstance(self: IWorkflowInstanceExtension, instance: WorkflowInstanceProxy) """
        ...


class LocationInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Name(self) -> str:
        """ Get: Name(self: LocationInfo) -> str """
        ...

    @property
    def OwnerDisplayName(self) -> str:
        """ Get: OwnerDisplayName(self: LocationInfo) -> str """
        ...

    @property
    def Value(self) -> object:
        """ Get: Value(self: LocationInfo) -> object """
        ...



class SymbolResolver(IDictionary): # skipped bases: <type 'IEnumerable[KeyValuePair[str, object]]'>, <type 'ICollection[KeyValuePair[str, object]]'>, <type 'IEnumerable'>, <type 'object'>
    """ SymbolResolver() """
    @property
    def Count(self) -> int:
        """ Get: Count(self: SymbolResolver) -> int """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: SymbolResolver) -> bool """
        ...


    def AsLocationReferenceEnvironment(self) -> LocationReferenceEnvironment:
        """ AsLocationReferenceEnvironment(self: SymbolResolver) -> LocationReferenceEnvironment """
        ...

    def Clear(self): # -> 
        """ Clear(self: SymbolResolver) """
        ...

    def Contains(self, item:KeyValuePair) -> bool:
        """ Contains(self: SymbolResolver, item: KeyValuePair[str, object]) -> bool """
        ...

    def CopyTo(self, array:Array, arrayIndex:int): # -> 
        """ CopyTo(self: SymbolResolver, array: Array[KeyValuePair[str, object]], arrayIndex: int) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SymbolResolver) -> IEnumerator[KeyValuePair[str, object]] """
        ...


class WorkflowInstance: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Controller(self):
        ...

    @property
    def DefinitionIdentity(self) -> WorkflowIdentity:
        """ Get: DefinitionIdentity(self: WorkflowInstance) -> WorkflowIdentity """
        ...

    @property
    def HostEnvironment(self) -> LocationReferenceEnvironment:
        """
        Get: HostEnvironment(self: WorkflowInstance) -> LocationReferenceEnvironment
        Set: HostEnvironment(self: WorkflowInstance) = value
        """
        ...

    @property
    def Id(self) -> Guid:
        """ Get: Id(self: WorkflowInstance) -> Guid """
        ...

    @property
    def IsReadOnly(self):
        ...

    @property
    def SupportsInstanceKeys(self):
        ...

    @property
    def SynchronizationContext(self) -> SynchronizationContext:
        """
        Get: SynchronizationContext(self: WorkflowInstance) -> SynchronizationContext
        Set: SynchronizationContext(self: WorkflowInstance) = value
        """
        ...

    @property
    def WorkflowDefinition(self) -> Activity:
        """ Get: WorkflowDefinition(self: WorkflowInstance) -> Activity """
        ...


    def BeginFlushTrackingRecords(self, *args): #cannot find CLR method
        """ BeginFlushTrackingRecords(self: WorkflowInstance, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def DisposeExtensions(self, *args): #cannot find CLR method
        """ DisposeExtensions(self: WorkflowInstance) """
        ...

    def EndFlushTrackingRecords(self, *args): #cannot find CLR method
        """ EndFlushTrackingRecords(self: WorkflowInstance, result: IAsyncResult) """
        ...

    def FlushTrackingRecords(self, *args): #cannot find CLR method
        """ FlushTrackingRecords(self: WorkflowInstance, timeout: TimeSpan) """
        ...

    def GetActivitiesBlockingUpdate(self, *args): #cannot find CLR method
        """ GetActivitiesBlockingUpdate(deserializedRuntimeState: object, updateMap: DynamicUpdateMap) -> IList[ActivityBlockingUpdate] """
        ...

    def GetExtension(self, *args): #cannot find CLR method
        """ GetExtension[T](self: WorkflowInstance) -> T """
        ...

    def GetExtensions(self, *args): #cannot find CLR method
        """ GetExtensions[T](self: WorkflowInstance) -> IEnumerable[T] """
        ...

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: WorkflowInstance, deserializedRuntimeState: object)Initialize(self: WorkflowInstance, deserializedRuntimeState: object, updateMap: DynamicUpdateMap)Initialize(self: WorkflowInstance, workflowArgumentValues: IDictionary[str, object], workflowExecutionProperties: IList[Handle]) """
        ...

    def OnBeginAssociateKeys(self, *args): #cannot find CLR method
        """ OnBeginAssociateKeys(self: WorkflowInstance, keys: ICollection[InstanceKey], callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnBeginFlushTrackingRecords(self, *args): #cannot find CLR method
        """ OnBeginFlushTrackingRecords(self: WorkflowInstance, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnBeginPersist(self, *args): #cannot find CLR method
        """ OnBeginPersist(self: WorkflowInstance, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnBeginResumeBookmark(self, *args): #cannot find CLR method
        """ OnBeginResumeBookmark(self: WorkflowInstance, bookmark: Bookmark, value: object, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def OnDisassociateKeys(self, *args): #cannot find CLR method
        """ OnDisassociateKeys(self: WorkflowInstance, keys: ICollection[InstanceKey]) """
        ...

    def OnEndAssociateKeys(self, *args): #cannot find CLR method
        """ OnEndAssociateKeys(self: WorkflowInstance, result: IAsyncResult) """
        ...

    def OnEndFlushTrackingRecords(self, *args): #cannot find CLR method
        """ OnEndFlushTrackingRecords(self: WorkflowInstance, result: IAsyncResult) """
        ...

    def OnEndPersist(self, *args): #cannot find CLR method
        """ OnEndPersist(self: WorkflowInstance, result: IAsyncResult) """
        ...

    def OnEndResumeBookmark(self, *args): #cannot find CLR method
        """ OnEndResumeBookmark(self: WorkflowInstance, result: IAsyncResult) -> BookmarkResumptionResult """
        ...

    def OnNotifyPaused(self, *args): #cannot find CLR method
        """ OnNotifyPaused(self: WorkflowInstance) """
        ...

    def OnNotifyUnhandledException(self, *args): #cannot find CLR method
        """ OnNotifyUnhandledException(self: WorkflowInstance, exception: Exception, source: Activity, sourceInstanceId: str) """
        ...

    def OnRequestAbort(self, *args): #cannot find CLR method
        """ OnRequestAbort(self: WorkflowInstance, reason: Exception) """
        ...

    def RegisterExtensionManager(self, *args): #cannot find CLR method
        """ RegisterExtensionManager(self: WorkflowInstance, extensionManager: WorkflowInstanceExtensionManager) """
        ...

    def ThrowIfReadOnly(self, *args): #cannot find CLR method
        """ ThrowIfReadOnly(self: WorkflowInstance) """
        ...

    def WorkflowInstanceControl(self, *args): #cannot find CLR method
        """ no doc """
        ...



class WorkflowInstanceExtensionManager: # skipped bases: <type 'object'>, <type 'object'>
    """ WorkflowInstanceExtensionManager() """
    def Add(self, *__args:object): # -> 
        """ Add(self: WorkflowInstanceExtensionManager, singletonExtension: object)Add[T](self: WorkflowInstanceExtensionManager, extensionCreationFunction: Func[T]) """
        ...

    def MakeReadOnly(self): # -> 
        """ MakeReadOnly(self: WorkflowInstanceExtensionManager) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...


class WorkflowInstanceProxy: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Id(self) -> Guid:
        """ Get: Id(self: WorkflowInstanceProxy) -> Guid """
        ...

    @property
    def WorkflowDefinition(self) -> Activity:
        """ Get: WorkflowDefinition(self: WorkflowInstanceProxy) -> Activity """
        ...


    def BeginResumeBookmark(self, bookmark, value, *__args) -> IAsyncResult:
        """
        BeginResumeBookmark(self: WorkflowInstanceProxy, bookmark: Bookmark, value: object, callback: AsyncCallback, state: object) -> IAsyncResult
        BeginResumeBookmark(self: WorkflowInstanceProxy, bookmark: Bookmark, value: object, timeout: TimeSpan, callback: AsyncCallback, state: object) -> IAsyncResult
        """
        ...

    def EndResumeBookmark(self, result:IAsyncResult) -> BookmarkResumptionResult:
        """ EndResumeBookmark(self: WorkflowInstanceProxy, result: IAsyncResult) -> BookmarkResumptionResult """
        ...


class WorkflowInstanceState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WorkflowInstanceState, values: Aborted (3), Complete (2), Idle (0), Runnable (1) """
    Aborted: WorkflowInstanceState = ...
    Complete: WorkflowInstanceState = ...
    Idle: WorkflowInstanceState = ...
    Runnable: WorkflowInstanceState = ...
    value__ = ...


