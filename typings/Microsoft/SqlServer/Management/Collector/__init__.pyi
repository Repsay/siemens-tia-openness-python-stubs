# encoding: utf-8
# module Microsoft.SqlServer.Management.Collector calls itself Collector
# from Microsoft.SqlServer.Management.Collector, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Common import (IMarkForDrop, IRenamable, 
    SqlServerManagementException)

from Microsoft.SqlServer.Management.Sdk.Sfc import (ISfcAlterable, 
    ISfcCreatable, ISfcDomain, ISfcDroppable, ISfcRenamable, 
    SfcCollatedDictionaryCollection, SfcInstance, SfcObjectExtender, 
    SfcObjectFactory, SqlStoreConnection)

from System import DateTime, Guid, Int16, Int64, TimeSpan

from System.Collections.Specialized import StringCollection

from System.Data import DataTable

from System.Data.SqlClient import SqlConnection

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    CollectionModes, Key)
"""

# no functions
# classes

class CollectionItem(ISfcRenamable, SfcInstance, IRenamable, IMarkForDrop, ISfcAlterable): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'IAlterable'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ CollectionItem(set: CollectionSet, name: str) """
    @property
    def CollectionFrequency(self) -> TimeSpan:
        """
        Get: CollectionFrequency(self: CollectionItem) -> TimeSpan
        Set: CollectionFrequency(self: CollectionItem) = value
        """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: CollectionItem) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: CollectionItem) -> Key """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CollectionItem) -> str
        Set: Name(self: CollectionItem) = value
        """
        ...

    @property
    def Parameters(self) -> str:
        """
        Get: Parameters(self: CollectionItem) -> str
        Set: Parameters(self: CollectionItem) = value
        """
        ...

    @property
    def TypeName(self) -> str:
        """
        Get: TypeName(self: CollectionItem) -> str
        Set: TypeName(self: CollectionItem) = value
        """
        ...


    def Alter(self): # -> 
        """ Alter(self: CollectionItem) """
        ...

    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key(other: Key)
        Key(name: str)
        """
        ...

    def __new__(cls, set:CollectionSet, name:str) -> Self:
        """ __new__(cls: type, set: CollectionSet, name: str) """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class CollectionItemCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'IComparer[Key]'>, <type 'IEnumerable[CollectionItem]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection[CollectionItem]'>, <type 'ICollection'>, <type 'object'>
    """ CollectionItemCollection(parent: CollectionSet) """
    def AddCollectionItem(self, item:CollectionItem): # -> 
        """ AddCollectionItem(self: CollectionItemCollection, item: CollectionItem) """
        ...

    def RemoveCollectionItem(self, item:CollectionItem): # -> 
        """ RemoveCollectionItem(self: CollectionItemCollection, item: CollectionItem) """
        ...


class CollectionSet(ISfcDroppable, ISfcRenamable, SfcInstance, ISfcCreatable, ISfcAlterable): # skipped bases: <type 'ICreatable'>, <type 'IAlterable'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'INotifyPropertyChanged'>, <type 'ISfcDiscoverObject'>, <type 'IDroppable'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    CollectionSet()
    CollectionSet(store: CollectorConfigStore, name: str)
    """
    @property
    def CollectionItems(self) -> CollectionItemCollection:
        """ Get: CollectionItems(self: CollectionSet) -> CollectionItemCollection """
        ...

    @property
    def CollectionMode(self): # -> CollectionModes
        """
        Get: CollectionMode(self: CollectionSet) -> CollectionModes
        Set: CollectionMode(self: CollectionSet) = value
        """
        ...

    @property
    def DaysUntilExpiration(self) -> Int16:
        """
        Get: DaysUntilExpiration(self: CollectionSet) -> Int16
        Set: DaysUntilExpiration(self: CollectionSet) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: CollectionSet) -> str
        Set: Description(self: CollectionSet) = value
        """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: CollectionSet) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: CollectionSet) -> Key """
        ...

    @property
    def IsRunning(self) -> bool:
        """ Get: IsRunning(self: CollectionSet) -> bool """
        ...

    @property
    def IsSystem(self) -> bool:
        """ Get: IsSystem(self: CollectionSet) -> bool """
        ...

    @property
    def IsTransactionPerformance(self) -> bool:
        """ Get: IsTransactionPerformance(self: CollectionSet) -> bool """
        ...

    @property
    def LoggingLevel(self) -> Int16:
        """
        Get: LoggingLevel(self: CollectionSet) -> Int16
        Set: LoggingLevel(self: CollectionSet) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: CollectionSet) -> str
        Set: Name(self: CollectionSet) = value
        """
        ...

    @property
    def ProxyName(self) -> str:
        """
        Get: ProxyName(self: CollectionSet) -> str
        Set: ProxyName(self: CollectionSet) = value
        """
        ...

    @property
    def ScheduleName(self) -> str:
        """
        Get: ScheduleName(self: CollectionSet) -> str
        Set: ScheduleName(self: CollectionSet) = value
        """
        ...

    @property
    def TargetName(self) -> str:
        """
        Get: TargetName(self: CollectionSet) -> str
        Set: TargetName(self: CollectionSet) = value
        """
        ...

    @property
    def UId(self) -> Guid:
        """
        Get: UId(self: CollectionSet) -> Guid
        Set: UId(self: CollectionSet) = value
        """
        ...


    def Alter(self): # -> 
        """ Alter(self: CollectionSet) """
        ...

    def Cleanup(self): # -> 
        """ Cleanup(self: CollectionSet) """
        ...

    def CollectionModes(self, *args): #cannot find CLR method
        """ enum CollectionModes, values: Cached (0), NonCached (1) """
        ...

    def Create(self): # -> 
        """ Create(self: CollectionSet) """
        ...

    def Drop(self): # -> 
        """ Drop(self: CollectionSet) """
        ...

    def EnumCollectionSetExecutionHistory(self, parentLogId:Int64 = ...) -> DataTable:
        """
        EnumCollectionSetExecutionHistory(self: CollectionSet) -> DataTable
        EnumCollectionSetExecutionHistory(self: CollectionSet, parentLogId: Int64) -> DataTable
        """
        ...

    def EnumCollectionSetExecutionHistoryDetail(self, logId:Int64) -> DataTable:
        """ EnumCollectionSetExecutionHistoryDetail(self: CollectionSet, logId: Int64) -> DataTable """
        ...

    def ExecutionStatus(self, *args): #cannot find CLR method
        """ enum ExecutionStatus, values: Failed (2), Finished (1), Running (0), Warning (3) """
        ...

    def GetLastUploadTime(self) -> DateTime:
        """ GetLastUploadTime(self: CollectionSet) -> DateTime """
        ...

    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """
        Key(other: Key)
        Key(name: str)
        """
        ...

    def RunOnce(self): # -> 
        """ RunOnce(self: CollectionSet) """
        ...

    def RuntimeExecutionMode(self, *args): #cannot find CLR method
        """ enum RuntimeExecutionMode, values: Collection (0), Upload (1) """
        ...

    def Start(self): # -> 
        """ Start(self: CollectionSet) """
        ...

    def Stop(self): # -> 
        """ Stop(self: CollectionSet) """
        ...

    def Upload(self): # -> 
        """ Upload(self: CollectionSet) """
        ...

    def __new__(cls, store:CollectorConfigStore = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, store: CollectorConfigStore, name: str)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class CollectionSetCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'IComparer[Key]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'ICollection[CollectionSet]'>, <type 'IListSource'>, <type 'IEnumerable[CollectionSet]'>, <type 'ICollection'>, <type 'object'>
    """ CollectionSetCollection(parent: CollectorConfigStore) """
    pass

class CollectionSetExtender(SfcObjectExtender): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    CollectionSetExtender()
    CollectionSetExtender(collectionSet: CollectionSet)
    CollectionSetExtender(collectorConfigStore: CollectorConfigStore, name: str)
    """
    pass

class CollectorConfigStore(SfcInstance, ISfcDomain, ISfcAlterable): # skipped bases: <type 'ISfcDomainLite'>, <type 'IAlterable'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'INotifyPropertyChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'ISfcHasConnection'>, <type 'object'>
    """
    CollectorConfigStore()
    CollectorConfigStore(connection: SqlStoreConnection)
    """
    @property
    def CacheDirectory(self) -> str:
        """
        Get: CacheDirectory(self: CollectorConfigStore) -> str
        Set: CacheDirectory(self: CollectorConfigStore) = value
        """
        ...

    @property
    def CacheWindow(self) -> int:
        """
        Get: CacheWindow(self: CollectorConfigStore) -> int
        Set: CacheWindow(self: CollectorConfigStore) = value
        """
        ...

    @property
    def CollectionSets(self) -> CollectionSetCollection:
        """ Get: CollectionSets(self: CollectorConfigStore) -> CollectionSetCollection """
        ...

    @property
    def Enabled(self) -> bool:
        """ Get: Enabled(self: CollectorConfigStore) -> bool """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: CollectorConfigStore) -> Key """
        ...

    @property
    def MDWDatabase(self) -> str:
        """
        Get: MDWDatabase(self: CollectorConfigStore) -> str
        Set: MDWDatabase(self: CollectorConfigStore) = value
        """
        ...

    @property
    def MDWInstance(self) -> str:
        """
        Get: MDWInstance(self: CollectorConfigStore) -> str
        Set: MDWInstance(self: CollectorConfigStore) = value
        """
        ...


    def Alter(self): # -> 
        """ Alter(self: CollectorConfigStore) """
        ...

    def ConfigureTransactionPerformanceCollectors(self, warehouseConnection:SqlConnection): # -> 
        """ ConfigureTransactionPerformanceCollectors(self: CollectorConfigStore, warehouseConnection: SqlConnection) """
        ...

    def DisableCollector(self): # -> 
        """ DisableCollector(self: CollectorConfigStore) """
        ...

    def EnableCollector(self): # -> 
        """ EnableCollector(self: CollectorConfigStore) """
        ...

    def EnumTypes(self) -> StringCollection:
        """ EnumTypes(self: CollectorConfigStore) -> StringCollection """
        ...

    def Key(self, *args): #cannot find CLR method
        """ Key() """
        ...

    def __new__(cls, connection:SqlStoreConnection = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, connection: SqlStoreConnection)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class CollectorException(SqlServerManagementException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    CollectorException()
    CollectorException(message: str)
    CollectorException(message: str, innerException: Exception)
    CollectorException(info: SerializationInfo, context: StreamingContext)
    """
    @property
    def ProdVer(self):
        ...


    def SetHelpContext(self, *args): #cannot find CLR method
        """ SetHelpContext(self: CollectorException, resource: str) -> CollectorException """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    SerializeObjectState = ...


