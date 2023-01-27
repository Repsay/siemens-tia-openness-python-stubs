# encoding: utf-8
# module Microsoft.SqlServer.Management.XEvent calls itself XEvent
# from Microsoft.SqlServer.Management.XEvent, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Common import (ISfcConnection, 
    SqlServerManagementException)

from Microsoft.SqlServer.Management.Sdk.Sfc import (ISfcAlterable, 
    ISfcCreatable, ISfcDomain, ISfcDroppable, ISfcExecutionEngine, ISfcScript, 
    ISfcValidate, SfcCollatedDictionaryCollection, SfcInstance, SfcKey, 
    SfcObjectFactory, SfcObjectQueryMode, SfcObjectState, SfcTypeMetadata)

from System import Array, DateTime, Guid

from System.Collections import IComparer

from System.Text import StringBuilder

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    ComparatorType, EventRetentionModeEnum, IXEObjectInfoCollection, Key, 
    LogicalOperatorType, MemoryPartitionModeEnum, ObjectMetadata)
"""

# no functions
# classes

class Action(SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    Action()
    Action(parent: Event, name: str)
    Action(parent: Event, actionInfo: ActionInfo)
    """
    @property
    def Description(self) -> str:
        """ Get: Description(self: Action) -> str """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: Action) -> Key """
        ...

    @property
    def ModuleID(self) -> Guid:
        """ Get: ModuleID(self: Action) -> Guid """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Action) -> str
        Set: Name(self: Action) = value
        """
        ...

    @property
    def PackageName(self) -> str:
        """ Get: PackageName(self: Action) -> str """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def GetScriptCreate(self) -> str:
        """ GetScriptCreate(self: Action) -> str """
        ...

    @staticmethod
    def GetTypeMetadata() -> SfcTypeMetadata:
        """ GetTypeMetadata() -> SfcTypeMetadata """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    def SetActionInfo(self, actionInfo:ActionInfo): # -> 
        """ SetActionInfo(self: Action, actionInfo: ActionInfo) """
        ...

    def __new__(cls, parent:Event = ..., *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: Event, name: str)
        __new__(cls: type, parent: Event, actionInfo: ActionInfo)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class ActionCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'ICollection[Action]'>, <type 'IComparer[Key]'>, <type 'IEnumerable[Action]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class ActionInfo(SfcInstance, IXEObjectInfo): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ no doc """
    @property
    def Capabilities(self) -> int:
        """ Get: Capabilities(self: ActionInfo) -> int """
        ...

    @property
    def CapabilitiesDesc(self) -> str:
        """ Get: CapabilitiesDesc(self: ActionInfo) -> str """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: ActionInfo) -> Key """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: ActionInfo) -> str """
        ...

    @property
    def TypePackageID(self) -> Guid:
        """ Get: TypePackageID(self: ActionInfo) -> Guid """
        ...

    @property
    def TypePackageName(self) -> str:
        """ Get: TypePackageName(self: ActionInfo) -> str """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class ActionInfoCollection(SfcCollatedDictionaryCollection, IXEObjectInfoCollection): # skipped bases: <type 'IEnumerable[ActionInfo]'>, <type 'IComparer[Key]'>, <type 'IEnumerable'>, <type 'ICollection[ActionInfo]'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class BaseXEStore(SfcInstance, ISfcDomain): # skipped bases: <type 'ISfcDomainLite'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'INotifyPropertyChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'ISfcHasConnection'>, <type 'object'>
    """ BaseXEStore(connection: ISfcConnection) """
    @property
    def EtwClassicSyncTargetInfo(self) -> TargetInfo:
        """ Get: EtwClassicSyncTargetInfo(self: BaseXEStore) -> TargetInfo """
        ...

    @property
    def EventCounterTargetInfo(self) -> TargetInfo:
        """ Get: EventCounterTargetInfo(self: BaseXEStore) -> TargetInfo """
        ...

    @property
    def EventFileTargetInfo(self) -> TargetInfo:
        """ Get: EventFileTargetInfo(self: BaseXEStore) -> TargetInfo """
        ...

    @property
    def ExecutionEngine(self):
        ...

    @property
    def HistogramTargetInfo(self) -> TargetInfo:
        """ Get: HistogramTargetInfo(self: BaseXEStore) -> TargetInfo """
        ...

    @property
    def IdentityKey(self) -> SfcKey:
        """ Get: IdentityKey(self: BaseXEStore) -> SfcKey """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: BaseXEStore) -> str """
        ...

    @property
    def ObjectInfoSet(self): # -> ObjectMetadata
        """ Get: ObjectInfoSet(self: BaseXEStore) -> ObjectMetadata """
        ...

    @property
    def OriginalConnection(self) -> ISfcConnection:
        """ Get: OriginalConnection(self: BaseXEStore) -> ISfcConnection """
        ...

    @property
    def Package0Package(self) -> Package:
        """ Get: Package0Package(self: BaseXEStore) -> Package """
        ...

    @property
    def Packages(self) -> PackageCollection:
        """ Get: Packages(self: BaseXEStore) -> PackageCollection """
        ...

    @property
    def PairMatchingTargetInfo(self) -> TargetInfo:
        """ Get: PairMatchingTargetInfo(self: BaseXEStore) -> TargetInfo """
        ...

    @property
    def RingBufferTargetInfo(self) -> TargetInfo:
        """ Get: RingBufferTargetInfo(self: BaseXEStore) -> TargetInfo """
        ...

    @property
    def RunningSessionCount(self) -> int:
        """ Get: RunningSessionCount(self: BaseXEStore) -> int """
        ...

    @property
    def ServerName(self) -> str:
        """ Get: ServerName(self: BaseXEStore) -> str """
        ...

    @property
    def Sessions(self) -> SessionCollection:
        """ Get: Sessions(self: BaseXEStore) -> SessionCollection """
        ...

    @property
    def SfcConnection(self) -> ISfcConnection:
        """ Get: SfcConnection(self: BaseXEStore) -> ISfcConnection """
        ...

    @property
    def StoreProvider(self):
        ...


    def CreateSession(self, sessionName:str) -> Session:
        """ CreateSession(self: BaseXEStore, sessionName: str) -> Session """
        ...

    def CreateSessionFromTemplate(self, sessionName:str, fileName:str) -> Session:
        """ CreateSessionFromTemplate(self: BaseXEStore, sessionName: str, fileName: str) -> Session """
        ...

    def FormatFieldValue(self, fieldValue:str, typePackageID:Guid, typeName:str) -> str:
        """ FormatFieldValue(self: BaseXEStore, fieldValue: str, typePackageID: Guid, typeName: str) -> str """
        ...

    def FormatPredicateExpression(self, predExpr:PredExpr) -> str:
        """ FormatPredicateExpression(self: BaseXEStore, predExpr: PredExpr) -> str """
        ...

    def GetComparer(self) -> IComparer:
        """ GetComparer(self: BaseXEStore) -> IComparer[str] """
        ...

    def GetEventProvider(self, *args): #cannot find CLR method
        """ GetEventProvider(self: BaseXEStore, xevent: Event) -> IEventProvider """
        ...

    def GetSessionProivder(self, *args): #cannot find CLR method
        """ GetSessionProivder(self: BaseXEStore, session: Session) -> ISessionProvider """
        ...

    def GetStoreProvider(self, *args): #cannot find CLR method
        """ GetStoreProvider(self: BaseXEStore) -> IXEStoreProvider """
        ...

    def GetTargetProvider(self, *args): #cannot find CLR method
        """ GetTargetProvider(self: BaseXEStore, target: Target) -> ITargetProvider """
        ...

    def InitConnection(self, *args): #cannot find CLR method
        """ InitConnection(self: BaseXEStore) """
        ...

    def Key(self, *args): #cannot find CLR method
        """ Key() """
        ...

    def ObjectMetadata(self, *args): #cannot find CLR method
        """ ObjectMetadata(store: BaseXEStore) """
        ...

    @staticmethod
    def SaveSessionToTemplate(session:Session, fileName:str, overwrite:bool): # -> 
        """ SaveSessionToTemplate(session: Session, fileName: str, overwrite: bool) """
        ...

    def SetConnection(self, *args): #cannot find CLR method
        """ SetConnection(self: BaseXEStore, connection: ISfcConnection) """
        ...

    def __new__(cls, connection:ISfcConnection) -> Self:
        """
        __new__(cls: type, connection: ISfcConnection)
        __new__(cls: type)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class DataEventColumnInfo(SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ no doc """
    @property
    def Capabilities(self) -> int:
        """ Get: Capabilities(self: DataEventColumnInfo) -> int """
        ...

    @property
    def CapabilitiesDesc(self) -> str:
        """ Get: CapabilitiesDesc(self: DataEventColumnInfo) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: DataEventColumnInfo) -> str """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: DataEventColumnInfo) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: DataEventColumnInfo) -> Key """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DataEventColumnInfo) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: DataEventColumnInfo) -> str """
        ...

    @property
    def TypePackageID(self) -> Guid:
        """ Get: TypePackageID(self: DataEventColumnInfo) -> Guid """
        ...

    @property
    def TypePackageName(self) -> str:
        """ Get: TypePackageName(self: DataEventColumnInfo) -> str """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class DataEventColumnInfoCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'ICollection[DataEventColumnInfo]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IComparer[Key]'>, <type 'IListSource'>, <type 'IEnumerable[DataEventColumnInfo]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class ISessionObject: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def State(self) -> SfcObjectState:
        """ Get: State(self: ISessionObject) -> SfcObjectState """
        ...


    def GetCreateScript(self) -> str:
        """ GetCreateScript(self: ISessionObject) -> str """
        ...

    def GetDropScript(self) -> str:
        """ GetDropScript(self: ISessionObject) -> str """
        ...

    def IsDirty(self) -> bool:
        """ IsDirty(self: ISessionObject) -> bool """
        ...


class Event(ISessionObject, SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    Event()
    Event(parent: Session, name: str)
    Event(parent: Session, eventInfo: EventInfo)
    """
    @property
    def Actions(self) -> ActionCollection:
        """ Get: Actions(self: Event) -> ActionCollection """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: Event) -> str """
        ...

    @property
    def EventFields(self) -> EventFieldCollection:
        """ Get: EventFields(self: Event) -> EventFieldCollection """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: Event) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: Event) -> Key """
        ...

    @property
    def ModuleID(self) -> Guid:
        """ Get: ModuleID(self: Event) -> Guid """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Event) -> str
        Set: Name(self: Event) = value
        """
        ...

    @property
    def PackageName(self) -> str:
        """ Get: PackageName(self: Event) -> str """
        ...

    @property
    def Predicate(self) -> PredExpr:
        """
        Get: Predicate(self: Event) -> PredExpr
        Set: Predicate(self: Event) = value
        """
        ...

    @property
    def PredicateExpression(self) -> str:
        """
        Get: PredicateExpression(self: Event) -> str
        Set: PredicateExpression(self: Event) = value
        """
        ...

    @property
    def ScriptName(self) -> str:
        """ Get: ScriptName(self: Event) -> str """
        ...


    def AddAction(self, *__args:ActionInfo) -> Action:
        """
        AddAction(self: Event, actionInfo: ActionInfo) -> Action
        AddAction(self: Event, actionName: str) -> Action
        """
        ...

    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    @staticmethod
    def GetTypeMetadata() -> SfcTypeMetadata:
        """ GetTypeMetadata() -> SfcTypeMetadata """
        ...

    def HasCustomizableField(self) -> bool:
        """ HasCustomizableField(self: Event) -> bool """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    def RemoveAction(self, action:Action) -> bool:
        """ RemoveAction(self: Event, action: Action) -> bool """
        ...

    def SetEventInfo(self, eventInfo:EventInfo): # -> 
        """ SetEventInfo(self: Event, eventInfo: EventInfo) """
        ...

    def __new__(cls, parent:Session = ..., *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: Session, name: str)
        __new__(cls: type, parent: Session, eventInfo: EventInfo)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class EventCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IComparer[Key]'>, <type 'ICollection[Event]'>, <type 'IEnumerable[Event]'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def AppendAlterScripts(self, addScript:StringBuilder, dropScript:StringBuilder): # -> 
        """ AppendAlterScripts(self: EventCollection, addScript: StringBuilder, dropScript: StringBuilder) """
        ...


class EventColumnInfo(SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ no doc """
    @property
    def Capabilities(self) -> int:
        """ Get: Capabilities(self: EventColumnInfo) -> int """
        ...

    @property
    def CapabilitiesDesc(self) -> str:
        """ Get: CapabilitiesDesc(self: EventColumnInfo) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: EventColumnInfo) -> str """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: EventColumnInfo) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: EventColumnInfo) -> Key """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: EventColumnInfo) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: EventColumnInfo) -> str """
        ...

    @property
    def TypePackageID(self) -> Guid:
        """ Get: TypePackageID(self: EventColumnInfo) -> Guid """
        ...

    @property
    def TypePackageName(self) -> str:
        """ Get: TypePackageName(self: EventColumnInfo) -> str """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: EventColumnInfo) -> str """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class EventColumnInfoCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'IComparer[Key]'>, <type 'IEnumerable[EventColumnInfo]'>, <type 'IEnumerable'>, <type 'ICollection[EventColumnInfo]'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class EventField(SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    EventField()
    EventField(parent: Event, eventColumnInfo: EventColumnInfo)
    """
    @property
    def Description(self) -> str:
        """ Get: Description(self: EventField) -> str """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: EventField) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: EventField) -> Key """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: EventField) -> str
        Set: Name(self: EventField) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: EventField) -> object
        Set: Value(self: EventField) = value
        """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    @staticmethod
    def GetTypeMetadata() -> SfcTypeMetadata:
        """ GetTypeMetadata() -> SfcTypeMetadata """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    def __new__(cls, parent:Event = ..., eventColumnInfo:EventColumnInfo = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: Event, eventColumnInfo: EventColumnInfo)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class EventFieldCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'IComparer[Key]'>, <type 'IEnumerable[EventField]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection[EventField]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class EventInfo(SfcInstance, IXEObjectInfo): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ no doc """
    @property
    def Capabilities(self) -> int:
        """ Get: Capabilities(self: EventInfo) -> int """
        ...

    @property
    def CapabilitiesDesc(self) -> str:
        """ Get: CapabilitiesDesc(self: EventInfo) -> str """
        ...

    @property
    def DataEventColumnInfoSet(self) -> DataEventColumnInfoCollection:
        """ Get: DataEventColumnInfoSet(self: EventInfo) -> DataEventColumnInfoCollection """
        ...

    @property
    def EventColumnInfoSet(self) -> EventColumnInfoCollection:
        """ Get: EventColumnInfoSet(self: EventInfo) -> EventColumnInfoCollection """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: EventInfo) -> Key """
        ...

    @property
    def ReadOnlyEventColumnInfoSet(self) -> ReadOnlyEventColumnInfoCollection:
        """ Get: ReadOnlyEventColumnInfoSet(self: EventInfo) -> ReadOnlyEventColumnInfoCollection """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class EventInfoCollection(SfcCollatedDictionaryCollection, IXEObjectInfoCollection): # skipped bases: <type 'IEnumerable'>, <type 'IComparer[Key]'>, <type 'IEnumerable[EventInfo]'>, <type 'ISfcCollection'>, <type 'ICollection[EventInfo]'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class IEventProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetCreateScript(self) -> str:
        """ GetCreateScript(self: IEventProvider) -> str """
        ...

    def GetDropScript(self) -> str:
        """ GetDropScript(self: IEventProvider) -> str """
        ...


class ISessionProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetAlterScript(self) -> ISfcScript:
        """ GetAlterScript(self: ISessionProvider) -> ISfcScript """
        ...

    def GetCreateScript(self) -> ISfcScript:
        """ GetCreateScript(self: ISessionProvider) -> ISfcScript """
        ...

    def GetDropScript(self) -> ISfcScript:
        """ GetDropScript(self: ISessionProvider) -> ISfcScript """
        ...

    def Start(self): # -> 
        """ Start(self: ISessionProvider) """
        ...

    def Stop(self): # -> 
        """ Stop(self: ISessionProvider) """
        ...

    def ValidateAlter(self): # -> 
        """ ValidateAlter(self: ISessionProvider) """
        ...


class ITargetProvider: # skipped bases: <type 'object'>
    """ no doc """
    def GetCreateScript(self) -> str:
        """ GetCreateScript(self: ITargetProvider) -> str """
        ...

    def GetDropScript(self) -> str:
        """ GetDropScript(self: ITargetProvider) -> str """
        ...

    def GetTargetData(self) -> str:
        """ GetTargetData(self: ITargetProvider) -> str """
        ...


class IXEObjectInfo: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Description(self) -> str:
        """ Get: Description(self: IXEObjectInfo) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: IXEObjectInfo) -> str """
        ...



class IXEStoreProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def DomainInstanceName(self) -> str:
        """ Get: DomainInstanceName(self: IXEStoreProvider) -> str """
        ...


    def GetComparer(self) -> IComparer:
        """ GetComparer(self: IXEStoreProvider) -> IComparer[str] """
        ...

    def GetConnection(self, mode:SfcObjectQueryMode) -> ISfcConnection:
        """ GetConnection(self: IXEStoreProvider, mode: SfcObjectQueryMode) -> ISfcConnection """
        ...

    def GetExecutionEngine(self) -> ISfcExecutionEngine:
        """ GetExecutionEngine(self: IXEStoreProvider) -> ISfcExecutionEngine """
        ...


class MapInfo(SfcInstance, IXEObjectInfo): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ no doc """
    @property
    def Capabilities(self) -> int:
        """ Get: Capabilities(self: MapInfo) -> int """
        ...

    @property
    def CapabilitiesDesc(self) -> str:
        """ Get: CapabilitiesDesc(self: MapInfo) -> str """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: MapInfo) -> Key """
        ...

    @property
    def MapValueInfoSet(self) -> MapValueInfoCollection:
        """ Get: MapValueInfoSet(self: MapInfo) -> MapValueInfoCollection """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class MapInfoCollection(SfcCollatedDictionaryCollection, IXEObjectInfoCollection): # skipped bases: <type 'IComparer[Key]'>, <type 'IEnumerable[MapInfo]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'ICollection[MapInfo]'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class MapValueInfo(SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ no doc """
    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: MapValueInfo) -> Key """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: MapValueInfo) -> str """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: MapValueInfo) -> str """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class MapValueInfoCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'IEnumerable[MapValueInfo]'>, <type 'IEnumerable'>, <type 'IComparer[Key]'>, <type 'ISfcCollection'>, <type 'ICollection[MapValueInfo]'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class Package(SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ no doc """
    @property
    def ActionInfoSet(self) -> ActionInfoCollection:
        """ Get: ActionInfoSet(self: Package) -> ActionInfoCollection """
        ...

    @property
    def Capabilities(self) -> int:
        """ Get: Capabilities(self: Package) -> int """
        ...

    @property
    def CapabilitiesDesc(self) -> str:
        """ Get: CapabilitiesDesc(self: Package) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: Package) -> str """
        ...

    @property
    def EventInfoSet(self) -> EventInfoCollection:
        """ Get: EventInfoSet(self: Package) -> EventInfoCollection """
        ...

    @property
    def ID(self) -> Guid:
        """ Get: ID(self: Package) -> Guid """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: Package) -> Key """
        ...

    @property
    def MapInfoSet(self) -> MapInfoCollection:
        """ Get: MapInfoSet(self: Package) -> MapInfoCollection """
        ...

    @property
    def ModuleAddress(self) -> Array:
        """ Get: ModuleAddress(self: Package) -> Array[Byte] """
        ...

    @property
    def ModuleID(self) -> Guid:
        """ Get: ModuleID(self: Package) -> Guid """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Package) -> str """
        ...

    @property
    def PredCompareInfoSet(self) -> PredCompareInfoCollection:
        """ Get: PredCompareInfoSet(self: Package) -> PredCompareInfoCollection """
        ...

    @property
    def PredSourceInfoSet(self) -> PredSourceInfoCollection:
        """ Get: PredSourceInfoSet(self: Package) -> PredSourceInfoCollection """
        ...

    @property
    def TargetInfoSet(self) -> TargetInfoCollection:
        """ Get: TargetInfoSet(self: Package) -> TargetInfoCollection """
        ...

    @property
    def TypeInfoSet(self) -> TypeInfoCollection:
        """ Get: TypeInfoSet(self: Package) -> TypeInfoCollection """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(guid: str, name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class PackageCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'IEnumerable[Package]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'ICollection[Package]'>, <type 'IComparer[Key]'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class Predicate: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    pass

class PredExpr(Predicate): # skipped bases: <type 'object'>
    """ no doc """
    pass

class PredCompareExpr(PredExpr): # skipped bases: <type 'object'>
    """ PredCompareExpr(type: ComparatorType, operand: PredOperand, value: PredValue) """
    @property
    def Operand(self) -> PredOperand:
        """ Get: Operand(self: PredCompareExpr) -> PredOperand """
        ...

    @property
    def Operator(self): # -> ComparatorType
        """ Get: Operator(self: PredCompareExpr) -> ComparatorType """
        ...

    @property
    def Value(self) -> PredValue:
        """ Get: Value(self: PredCompareExpr) -> PredValue """
        ...


    def ComparatorType(self, *args): #cannot find CLR method
        """ enum ComparatorType, values: EQ (0), GE (3), GT (2), LE (5), LT (4), NE (1) """
        ...

    def __new__(cls, type, operand:PredOperand, value:PredValue) -> Self: # Not found arg types: {'type': 'ComparatorType'}
        """ __new__(cls: type, type: ComparatorType, operand: PredOperand, value: PredValue) """
        ...



class PredCompareInfo(SfcInstance, IXEObjectInfo): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ no doc """
    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: PredCompareInfo) -> Key """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: PredCompareInfo) -> str """
        ...

    @property
    def TypePackageID(self) -> Guid:
        """ Get: TypePackageID(self: PredCompareInfo) -> Guid """
        ...

    @property
    def TypePackageName(self) -> str:
        """ Get: TypePackageName(self: PredCompareInfo) -> str """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class PredCompareInfoCollection(SfcCollatedDictionaryCollection, IXEObjectInfoCollection): # skipped bases: <type 'IEnumerable[PredCompareInfo]'>, <type 'IEnumerable'>, <type 'IComparer[Key]'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection[PredCompareInfo]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class PredFunctionExpr(PredExpr): # skipped bases: <type 'object'>
    """ PredFunctionExpr(func: PredCompareInfo, operand: PredOperand, value: PredValue) """
    @property
    def Operand(self) -> PredOperand:
        """ Get: Operand(self: PredFunctionExpr) -> PredOperand """
        ...

    @property
    def Operator(self) -> PredCompareInfo:
        """ Get: Operator(self: PredFunctionExpr) -> PredCompareInfo """
        ...

    @property
    def Value(self) -> PredValue:
        """ Get: Value(self: PredFunctionExpr) -> PredValue """
        ...


    def __new__(cls, func:PredCompareInfo, operand:PredOperand, value:PredValue) -> Self:
        """ __new__(cls: type, func: PredCompareInfo, operand: PredOperand, value: PredValue) """
        ...


class PredLogicalExpr(PredExpr): # skipped bases: <type 'object'>
    """ PredLogicalExpr(type: LogicalOperatorType, predExpr1: PredExpr, predExpr2: PredExpr) """
    @property
    def LeftExpr(self) -> PredExpr:
        """ Get: LeftExpr(self: PredLogicalExpr) -> PredExpr """
        ...

    @property
    def Operator(self): # -> LogicalOperatorType
        """ Get: Operator(self: PredLogicalExpr) -> LogicalOperatorType """
        ...

    @property
    def RightExpr(self) -> PredExpr:
        """ Get: RightExpr(self: PredLogicalExpr) -> PredExpr """
        ...


    def LogicalOperatorType(self, *args): #cannot find CLR method
        """ enum LogicalOperatorType, values: And (1), Not (0), Or (2) """
        ...

    def __new__(cls, type, predExpr1:PredExpr, predExpr2:PredExpr) -> Self: # Not found arg types: {'type': 'LogicalOperatorType'}
        """ __new__(cls: type, type: LogicalOperatorType, predExpr1: PredExpr, predExpr2: PredExpr) """
        ...



class PredOperand(Predicate): # skipped bases: <type 'object'>
    """
    PredOperand(eventColumn: DataEventColumnInfo)
    PredOperand(sourceInfo: PredSourceInfo)
    """
    @property
    def OperandObject(self) -> object:
        """ Get: OperandObject(self: PredOperand) -> object """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: PredOperand) -> str """
        ...

    @property
    def TypePackageId(self) -> Guid:
        """ Get: TypePackageId(self: PredOperand) -> Guid """
        ...


    def ToString(self) -> str:
        """ ToString(self: PredOperand) -> str """
        ...

    def __new__(cls, *__args:DataEventColumnInfo) -> Self:
        """
        __new__(cls: type, eventColumn: DataEventColumnInfo)
        __new__(cls: type, sourceInfo: PredSourceInfo)
        """
        ...


class PredSourceInfo(SfcInstance, IXEObjectInfo): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ no doc """
    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: PredSourceInfo) -> Key """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: PredSourceInfo) -> str """
        ...

    @property
    def TypePackageID(self) -> Guid:
        """ Get: TypePackageID(self: PredSourceInfo) -> Guid """
        ...

    @property
    def TypePackageName(self) -> str:
        """ Get: TypePackageName(self: PredSourceInfo) -> str """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class PredSourceInfoCollection(SfcCollatedDictionaryCollection, IXEObjectInfoCollection): # skipped bases: <type 'IComparer[Key]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IEnumerable[PredSourceInfo]'>, <type 'ICollection[PredSourceInfo]'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class PredValue(Predicate): # skipped bases: <type 'object'>
    """ PredValue(value: object) """
    def ToString(self) -> str:
        """ ToString(self: PredValue) -> str """
        ...

    def __new__(cls, value:object) -> Self:
        """ __new__(cls: type, value: object) """
        ...


class ReadOnlyEventColumnInfo(SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ no doc """
    @property
    def Capabilities(self) -> int:
        """ Get: Capabilities(self: ReadOnlyEventColumnInfo) -> int """
        ...

    @property
    def CapabilitiesDesc(self) -> str:
        """ Get: CapabilitiesDesc(self: ReadOnlyEventColumnInfo) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: ReadOnlyEventColumnInfo) -> str """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: ReadOnlyEventColumnInfo) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: ReadOnlyEventColumnInfo) -> Key """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ReadOnlyEventColumnInfo) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: ReadOnlyEventColumnInfo) -> str """
        ...

    @property
    def TypePackageID(self) -> Guid:
        """ Get: TypePackageID(self: ReadOnlyEventColumnInfo) -> Guid """
        ...

    @property
    def TypePackageName(self) -> str:
        """ Get: TypePackageName(self: ReadOnlyEventColumnInfo) -> str """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: ReadOnlyEventColumnInfo) -> str """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class ReadOnlyEventColumnInfoCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IComparer[Key]'>, <type 'IEnumerable[ReadOnlyEventColumnInfo]'>, <type 'IListSource'>, <type 'ICollection[ReadOnlyEventColumnInfo]'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class Session(ISfcDroppable, SfcInstance, ISfcValidate, ISfcCreatable, ISfcAlterable): # skipped bases: <type 'ICreatable'>, <type 'IAlterable'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'INotifyPropertyChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'IDroppable'>, <type 'object'>
    """
    Session()
    Session(parent: BaseXEStore, name: str)
    """
    @property
    def AutoStart(self) -> bool:
        """
        Get: AutoStart(self: Session) -> bool
        Set: AutoStart(self: Session) = value
        """
        ...

    @property
    def EventRetentionMode(self): # -> EventRetentionModeEnum
        """
        Get: EventRetentionMode(self: Session) -> EventRetentionModeEnum
        Set: EventRetentionMode(self: Session) = value
        """
        ...

    @property
    def Events(self) -> EventCollection:
        """ Get: Events(self: Session) -> EventCollection """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: Session) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: Session) -> Key """
        ...

    @property
    def IsRunning(self) -> bool:
        """ Get: IsRunning(self: Session) -> bool """
        ...

    @property
    def MaxDispatchLatency(self) -> int:
        """
        Get: MaxDispatchLatency(self: Session) -> int
        Set: MaxDispatchLatency(self: Session) = value
        """
        ...

    @property
    def MaxEventSize(self) -> int:
        """
        Get: MaxEventSize(self: Session) -> int
        Set: MaxEventSize(self: Session) = value
        """
        ...

    @property
    def MaxMemory(self) -> int:
        """
        Get: MaxMemory(self: Session) -> int
        Set: MaxMemory(self: Session) = value
        """
        ...

    @property
    def MemoryPartitionMode(self): # -> MemoryPartitionModeEnum
        """
        Get: MemoryPartitionMode(self: Session) -> MemoryPartitionModeEnum
        Set: MemoryPartitionMode(self: Session) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Session) -> str
        Set: Name(self: Session) = value
        """
        ...

    @property
    def StartTime(self) -> DateTime:
        """ Get: StartTime(self: Session) -> DateTime """
        ...

    @property
    def Targets(self) -> TargetCollection:
        """ Get: Targets(self: Session) -> TargetCollection """
        ...

    @property
    def TrackCausality(self) -> bool:
        """
        Get: TrackCausality(self: Session) -> bool
        Set: TrackCausality(self: Session) = value
        """
        ...


    def AddEvent(self, *__args:EventInfo) -> Event:
        """
        AddEvent(self: Session, eventInfo: EventInfo) -> Event
        AddEvent(self: Session, eventName: str) -> Event
        """
        ...

    def AddTarget(self, *__args:TargetInfo) -> Target:
        """
        AddTarget(self: Session, targetInfo: TargetInfo) -> Target
        AddTarget(self: Session, targetName: str) -> Target
        """
        ...

    def Alter(self): # -> 
        """ Alter(self: Session) """
        ...

    def Create(self): # -> 
        """ Create(self: Session) """
        ...

    def Drop(self): # -> 
        """ Drop(self: Session) """
        ...

    def EventRetentionModeEnum(self, *args): #cannot find CLR method
        """ enum EventRetentionModeEnum, values: AllowMultipleEventLoss (1), AllowSingleEventLoss (0), NoEventLoss (2) """
        ...

    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    def MemoryPartitionModeEnum(self, *args): #cannot find CLR method
        """ enum MemoryPartitionModeEnum, values: None (0), PerCpu (2), PerNode (1) """
        ...

    def RemoveEvent(self, evt:Event) -> bool:
        """ RemoveEvent(self: Session, evt: Event) -> bool """
        ...

    def RemoveTarget(self, target:Target) -> bool:
        """ RemoveTarget(self: Session, target: Target) -> bool """
        ...

    def Start(self): # -> 
        """ Start(self: Session) """
        ...

    def Stop(self): # -> 
        """ Stop(self: Session) """
        ...

    def __new__(cls, parent:BaseXEStore = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: BaseXEStore, name: str)
        """
        ...

    AutoStartProperty: str = ...
    DefaultDispatchLatency: int = ...
    DefaultMaxMemory: int = ...
    EventRetentionModeProperty: str = ...
    InfiniteDispatchLatency: int = ...
    MaxDispatchLatencyProperty: str = ...
    MaxEventSizeProperty: str = ...
    MaxMemoryProperty: str = ...
    MemoryPartitionModeProperty: str = ...
    NotStarted: DateTime = ...
    propertyChanged = ...
    propertyMetadataChanged = ...
    TrackCausalityProperty: str = ...
    TypeTypeName: str = ...


class SessionCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'IEnumerable'>, <type 'IComparer[Key]'>, <type 'IEnumerable[Session]'>, <type 'ICollection[Session]'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class SessionProviderBase(ISessionProvider): # skipped bases: <type 'object'>
    """ no doc """
    pass

class Target(ISessionObject, SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    Target()
    Target(parent: Session, name: str)
    Target(parent: Session, targetInfo: TargetInfo)
    """
    @property
    def Description(self) -> str:
        """ Get: Description(self: Target) -> str """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: Target) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: Target) -> Key """
        ...

    @property
    def ModuleID(self) -> Guid:
        """ Get: ModuleID(self: Target) -> Guid """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Target) -> str
        Set: Name(self: Target) = value
        """
        ...

    @property
    def PackageName(self) -> str:
        """ Get: PackageName(self: Target) -> str """
        ...

    @property
    def ScriptName(self) -> str:
        """ Get: ScriptName(self: Target) -> str """
        ...

    @property
    def TargetFields(self) -> TargetFieldCollection:
        """ Get: TargetFields(self: Target) -> TargetFieldCollection """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def GetTargetData(self) -> str:
        """ GetTargetData(self: Target) -> str """
        ...

    @staticmethod
    def GetTypeMetadata() -> SfcTypeMetadata:
        """ GetTypeMetadata() -> SfcTypeMetadata """
        ...

    def HasCustomizableField(self) -> bool:
        """ HasCustomizableField(self: Target) -> bool """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    def SetTargetInfo(self, targetInfo:TargetInfo): # -> 
        """ SetTargetInfo(self: Target, targetInfo: TargetInfo) """
        ...

    def __new__(cls, parent:Session = ..., *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: Session, name: str)
        __new__(cls: type, parent: Session, targetInfo: TargetInfo)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class TargetCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'ICollection[Target]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IEnumerable[Target]'>, <type 'IComparer[Key]'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    def AppendAlterScripts(self, addScript:StringBuilder, dropScript:StringBuilder): # -> 
        """ AppendAlterScripts(self: TargetCollection, addScript: StringBuilder, dropScript: StringBuilder) """
        ...


class TargetColumnInfo(SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ no doc """
    @property
    def Capabilities(self) -> int:
        """ Get: Capabilities(self: TargetColumnInfo) -> int """
        ...

    @property
    def CapabilitiesDesc(self) -> str:
        """ Get: CapabilitiesDesc(self: TargetColumnInfo) -> str """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: TargetColumnInfo) -> str """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: TargetColumnInfo) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: TargetColumnInfo) -> Key """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: TargetColumnInfo) -> str """
        ...

    @property
    def TypeName(self) -> str:
        """ Get: TypeName(self: TargetColumnInfo) -> str """
        ...

    @property
    def TypePackageID(self) -> Guid:
        """ Get: TypePackageID(self: TargetColumnInfo) -> Guid """
        ...

    @property
    def TypePackageName(self) -> str:
        """ Get: TypePackageName(self: TargetColumnInfo) -> str """
        ...

    @property
    def Value(self) -> str:
        """ Get: Value(self: TargetColumnInfo) -> str """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class TargetColumnInfoCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'ICollection[TargetColumnInfo]'>, <type 'IComparer[Key]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IEnumerable[TargetColumnInfo]'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class TargetField(SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    TargetField()
    TargetField(parent: Target, targetColumnInfo: TargetColumnInfo)
    """
    @property
    def Description(self) -> str:
        """ Get: Description(self: TargetField) -> str """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: TargetField) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: TargetField) -> Key """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: TargetField) -> str
        Set: Name(self: TargetField) = value
        """
        ...

    @property
    def Value(self) -> object:
        """
        Get: Value(self: TargetField) -> object
        Set: Value(self: TargetField) = value
        """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    @staticmethod
    def GetTypeMetadata() -> SfcTypeMetadata:
        """ GetTypeMetadata() -> SfcTypeMetadata """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    def __new__(cls, parent:Target = ..., targetColumnInfo:TargetColumnInfo = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: Target, targetColumnInfo: TargetColumnInfo)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class TargetFieldCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'ICollection[TargetField]'>, <type 'IEnumerable[TargetField]'>, <type 'IEnumerable'>, <type 'IComparer[Key]'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class TargetInfo(SfcInstance, IXEObjectInfo): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ no doc """
    @property
    def Capabilities(self) -> int:
        """ Get: Capabilities(self: TargetInfo) -> int """
        ...

    @property
    def CapabilitiesDesc(self) -> str:
        """ Get: CapabilitiesDesc(self: TargetInfo) -> str """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: TargetInfo) -> Key """
        ...

    @property
    def TargetColumnInfoSet(self) -> TargetColumnInfoCollection:
        """ Get: TargetColumnInfoSet(self: TargetInfo) -> TargetColumnInfoCollection """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class TargetInfoCollection(SfcCollatedDictionaryCollection, IXEObjectInfoCollection): # skipped bases: <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'ICollection[TargetInfo]'>, <type 'IListSource'>, <type 'IComparer[Key]'>, <type 'ICollection'>, <type 'IEnumerable[TargetInfo]'>, <type 'object'>
    """ no doc """
    pass

class TypeInfo(SfcInstance, IXEObjectInfo): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ no doc """
    @property
    def Capabilities(self) -> int:
        """ Get: Capabilities(self: TypeInfo) -> int """
        ...

    @property
    def CapabilitiesDesc(self) -> str:
        """ Get: CapabilitiesDesc(self: TypeInfo) -> str """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: TypeInfo) -> Key """
        ...

    @property
    def Size(self) -> int:
        """ Get: Size(self: TypeInfo) -> int """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key()
        Key(other: Key)
        Key(name: str)
        Key(filedDict: Dictionary[str, object])
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class TypeInfoCollection(SfcCollatedDictionaryCollection, IXEObjectInfoCollection): # skipped bases: <type 'IComparer[Key]'>, <type 'IEnumerable'>, <type 'ICollection[TypeInfo]'>, <type 'IEnumerable[TypeInfo]'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class XEStore(BaseXEStore): # skipped bases: <type 'ISfcDomainLite'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'INotifyPropertyChanged'>, <type 'ISfcDomain'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'ISfcHasConnection'>, <type 'object'>
    """ XEStore(connection: SqlStoreConnection) """
    def ServerKey(self, *args): #cannot find CLR method
        """ ServerKey() """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...
    TypeTypeName: str = ...


class XEUtils: # skipped bases: <type 'object'>, <type 'object'>
    """ XEUtils() """
    @staticmethod
    def ConvertToXsdEnumerationValue(*__args) -> str: # Not found arg types: {'*__args': 'EventRetentionModeEnum'}
        """
        ConvertToXsdEnumerationValue(retentionMode: EventRetentionModeEnum) -> str
        ConvertToXsdEnumerationValue(partitionMode: MemoryPartitionModeEnum) -> str
        """
        ...

    @staticmethod
    def ToBeCreated(state:SfcObjectState) -> bool:
        """ ToBeCreated(state: SfcObjectState) -> bool """
        ...


class XEventException(SqlServerManagementException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    XEventException()
    XEventException(message: str)
    XEventException(message: str, innerException: Exception)
    """
    @property
    def ProdVer(self):
        ...


    def Init(self, *args): #cannot find CLR method
        """ Init(self: XEventException) """
        ...

    def SetHelpContext(self, *args): #cannot find CLR method
        """ SetHelpContext(self: XEventException, resource: str) -> XEventException """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    SerializeObjectState = ...


