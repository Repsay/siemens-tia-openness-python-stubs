# encoding: utf-8
# module Microsoft.SqlServer.Management.Utility calls itself Utility
# from Microsoft.SqlServer.Management.Utility, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Common import SqlSecureString

from Microsoft.SqlServer.Management.Common import (
    SqlServerManagementException)

from Microsoft.SqlServer.Management.Dmf import PolicyStore

from Microsoft.SqlServer.Management.Sdk.Sfc import (IDmfFacet, ISfcAlterable, 
    ISfcCreatable, ISfcDomain2, ISfcDroppable, 
    SfcCollatedDictionaryCollection, SfcInstance, SfcKey, SfcObjectFactory, 
    SqlStoreConnection)

from System import DateTime, DateTimeOffset, Enum, Single

from typing import Self

"""The following names are not found in the module: (BoundEvent, IDmfAdapter, 
    IManagedInstanceContext, IProcessorUtilizationProvider, 
    IStorageUtilizationProvider, Key, field#)
"""

# no functions
# classes

class Computer(SfcInstance, IProcessorUtilizationProvider): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    Computer()
    Computer(parent: Utility, name: str)
    """
    @property
    def CpuMaxClockSpeed(self) -> int:
        """ Get: CpuMaxClockSpeed(self: Computer) -> int """
        ...

    @property
    def CpuName(self) -> str:
        """ Get: CpuName(self: Computer) -> str """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: Computer) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: Computer) -> Key """
        ...

    @property
    def IsClustered(self) -> bool:
        """ Get: IsClustered(self: Computer) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Computer) -> str """
        ...

    @property
    def ProcessorUtilization(self) -> Single:
        """ Get: ProcessorUtilization(self: Computer) -> Single """
        ...

    @property
    def Volumes(self) -> VolumeCollection:
        """ Get: Volumes(self: Computer) -> VolumeCollection """
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
        """
        ...

    def __new__(cls, parent:Utility = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: Utility, name: str)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class ComputerCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'IComparer[Key]'>, <type 'IEnumerable'>, <type 'IEnumerable[Computer]'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'ICollection[Computer]'>, <type 'ICollection'>, <type 'object'>
    """
    ComputerCollection(parent: Utility)
    ComputerCollection(parent: Utility, customComparer: IComparer[str])
    """
    pass

class DatabaseState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum DatabaseState, values: Available (0), Unavailable (1), Unknown (-1) """
    Available: DatabaseState = ...
    Unavailable: DatabaseState = ...
    Unknown: DatabaseState = ...
    value__ = ...


class DataFileAdapter(IDataFilePerformanceFacet, IDmfAdapter): # skipped bases: <type 'IDmfFacet'>, <type 'object'>
    """ DataFileAdapter(file: DataFile) """
    pass

class DeployedDac(IManagedInstanceContext, SfcInstance, IProcessorUtilizationProvider): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ DeployedDac() """
    @property
    def Collation(self) -> str:
        """ Get: Collation(self: DeployedDac) -> str """
        ...

    @property
    def CompatibilityLevel(self) -> int:
        """ Get: CompatibilityLevel(self: DeployedDac) -> int """
        ...

    @property
    def ComputerName(self) -> str:
        """ Get: ComputerName(self: DeployedDac) -> str """
        ...

    @property
    def ComputerProcessorHealthState(self) -> HealthState:
        """ Get: ComputerProcessorHealthState(self: DeployedDac) -> HealthState """
        ...

    @property
    def ContainsOverUtilizedFileGroups(self) -> bool:
        """ Get: ContainsOverUtilizedFileGroups(self: DeployedDac) -> bool """
        ...

    @property
    def ContainsOverUtilizedVolumes(self) -> bool:
        """ Get: ContainsOverUtilizedVolumes(self: DeployedDac) -> bool """
        ...

    @property
    def ContainsUnderUtilizedFileGroups(self) -> bool:
        """ Get: ContainsUnderUtilizedFileGroups(self: DeployedDac) -> bool """
        ...

    @property
    def ContainsUnderUtilizedVolumes(self) -> bool:
        """ Get: ContainsUnderUtilizedVolumes(self: DeployedDac) -> bool """
        ...

    @property
    def DacProcessorHealthState(self) -> HealthState:
        """ Get: DacProcessorHealthState(self: DeployedDac) -> HealthState """
        ...

    @property
    def DatabaseName(self) -> str:
        """ Get: DatabaseName(self: DeployedDac) -> str """
        ...

    @property
    def DatabaseState(self) -> DatabaseState:
        """ Get: DatabaseState(self: DeployedDac) -> DatabaseState """
        ...

    @property
    def DeployedDate(self) -> DateTime:
        """ Get: DeployedDate(self: DeployedDac) -> DateTime """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: DeployedDac) -> str """
        ...

    @property
    def EncryptionEnabled(self) -> bool:
        """ Get: EncryptionEnabled(self: DeployedDac) -> bool """
        ...

    @property
    def FileSpaceHealthState(self) -> HealthState:
        """ Get: FileSpaceHealthState(self: DeployedDac) -> HealthState """
        ...

    @property
    def Id(self) -> int:
        """ Get: Id(self: DeployedDac) -> int """
        ...

    @property
    def IsPolicyOverridden(self) -> bool:
        """ Get: IsPolicyOverridden(self: DeployedDac) -> bool """
        ...

    @property
    def LastReportedTime(self) -> DateTimeOffset:
        """ Get: LastReportedTime(self: DeployedDac) -> DateTimeOffset """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: DeployedDac) -> str """
        ...

    @property
    def ProcessorUtilization(self) -> Single:
        """ Get: ProcessorUtilization(self: DeployedDac) -> Single """
        ...

    @property
    def RecoveryModel(self) -> int:
        """ Get: RecoveryModel(self: DeployedDac) -> int """
        ...

    @property
    def ServerInstanceName(self) -> str:
        """ Get: ServerInstanceName(self: DeployedDac) -> str """
        ...

    @property
    def Trustworthy(self) -> bool:
        """ Get: Trustworthy(self: DeployedDac) -> bool """
        ...

    @property
    def VolumeSpaceHealthState(self) -> HealthState:
        """ Get: VolumeSpaceHealthState(self: DeployedDac) -> HealthState """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """ Key(keyName: str, keyServerInstanceName: str) """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class DeployedDacCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'ICollection[DeployedDac]'>, <type 'IEnumerable'>, <type 'IComparer[Key]'>, <type 'ISfcCollection'>, <type 'IEnumerable[DeployedDac]'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """
    DeployedDacCollection(parent: Utility)
    DeployedDacCollection(parent: Utility, customComparer: IComparer[str])
    """
    pass

class HealthState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HealthState, values: Critical (3), None (0), Steady (1), Warning (2) """
    Critical: HealthState = ...
    Steady: HealthState = ...
    value__ = ...
    Warning: HealthState = ...


class IDataFilePerformanceFacet(IDmfFacet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SpaceUtilization(self) -> float:
        """ Get: SpaceUtilization(self: IDataFilePerformanceFacet) -> float """
        ...



class ILogFilePerformanceFacet(IDmfFacet): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def SpaceUtilization(self) -> float:
        """ Get: SpaceUtilization(self: ILogFilePerformanceFacet) -> float """
        ...



class LogFileAdapter(IDmfAdapter, ILogFilePerformanceFacet): # skipped bases: <type 'IDmfFacet'>, <type 'object'>
    """ LogFileAdapter(file: LogFile) """
    pass

class ManagedInstance(ISfcDroppable, IManagedInstanceContext, SfcInstance, IProcessorUtilizationProvider, ISfcCreatable): # skipped bases: <type 'ICreatable'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'INotifyPropertyChanged'>, <type 'ISfcDiscoverObject'>, <type 'IDroppable'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """ ManagedInstance() """
    @property
    def AgentProxyAccount(self) -> str:
        """ Get: AgentProxyAccount(self: ManagedInstance) -> str """
        ...

    @property
    def BackupDirectory(self) -> str:
        """ Get: BackupDirectory(self: ManagedInstance) -> str """
        ...

    @property
    def CacheDirectory(self) -> str:
        """ Get: CacheDirectory(self: ManagedInstance) -> str """
        ...

    @property
    def Collation(self) -> str:
        """ Get: Collation(self: ManagedInstance) -> str """
        ...

    @property
    def ComputerNamePhysicalNetBIOS(self) -> str:
        """ Get: ComputerNamePhysicalNetBIOS(self: ManagedInstance) -> str """
        ...

    @property
    def ComputerProcessorHealthState(self) -> HealthState:
        """ Get: ComputerProcessorHealthState(self: ManagedInstance) -> HealthState """
        ...

    @property
    def ContainsOverUtilizedDatabases(self) -> bool:
        """ Get: ContainsOverUtilizedDatabases(self: ManagedInstance) -> bool """
        ...

    @property
    def ContainsOverUtilizedVolumes(self) -> bool:
        """ Get: ContainsOverUtilizedVolumes(self: ManagedInstance) -> bool """
        ...

    @property
    def ContainsUnderUtilizedDatabases(self) -> bool:
        """ Get: ContainsUnderUtilizedDatabases(self: ManagedInstance) -> bool """
        ...

    @property
    def ContainsUnderUtilizedVolumes(self) -> bool:
        """ Get: ContainsUnderUtilizedVolumes(self: ManagedInstance) -> bool """
        ...

    @property
    def CpuMaxClockSpeed(self) -> int:
        """ Get: CpuMaxClockSpeed(self: ManagedInstance) -> int """
        ...

    @property
    def CpuName(self) -> str:
        """ Get: CpuName(self: ManagedInstance) -> str """
        ...

    @property
    def DateCreated(self) -> DateTimeOffset:
        """ Get: DateCreated(self: ManagedInstance) -> DateTimeOffset """
        ...

    @property
    def Edition(self) -> str:
        """ Get: Edition(self: ManagedInstance) -> str """
        ...

    @property
    def EngineEdition(self) -> int:
        """ Get: EngineEdition(self: ManagedInstance) -> int """
        ...

    @property
    def FileSpaceHealthState(self) -> HealthState:
        """ Get: FileSpaceHealthState(self: ManagedInstance) -> HealthState """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: ManagedInstance) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: ManagedInstance) -> Key """
        ...

    @property
    def InstanceName(self) -> str:
        """ Get: InstanceName(self: ManagedInstance) -> str """
        ...

    @property
    def IsCaseSensitive(self) -> bool:
        """ Get: IsCaseSensitive(self: ManagedInstance) -> bool """
        ...

    @property
    def IsClustered(self) -> bool:
        """ Get: IsClustered(self: ManagedInstance) -> bool """
        ...

    @property
    def IsPolicyOverridden(self) -> bool:
        """ Get: IsPolicyOverridden(self: ManagedInstance) -> bool """
        ...

    @property
    def Language(self) -> str:
        """ Get: Language(self: ManagedInstance) -> str """
        ...

    @property
    def LastReportedTime(self) -> DateTimeOffset:
        """ Get: LastReportedTime(self: ManagedInstance) -> DateTimeOffset """
        ...

    @property
    def ManagementState(self) -> ManagementState:
        """ Get: ManagementState(self: ManagedInstance) -> ManagementState """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: ManagedInstance) -> str """
        ...

    @property
    def NetName(self) -> str:
        """ Get: NetName(self: ManagedInstance) -> str """
        ...

    @property
    def OSVersion(self) -> str:
        """ Get: OSVersion(self: ManagedInstance) -> str """
        ...

    @property
    def PhysicalMemory(self) -> int:
        """ Get: PhysicalMemory(self: ManagedInstance) -> int """
        ...

    @property
    def Processors(self) -> int:
        """ Get: Processors(self: ManagedInstance) -> int """
        ...

    @property
    def ProductLevel(self) -> str:
        """ Get: ProductLevel(self: ManagedInstance) -> str """
        ...

    @property
    def ServerProcessorHealthState(self) -> HealthState:
        """ Get: ServerProcessorHealthState(self: ManagedInstance) -> HealthState """
        ...

    @property
    def ServerType(self) -> int:
        """ Get: ServerType(self: ManagedInstance) -> int """
        ...

    @property
    def ServerUrn(self) -> str:
        """ Get: ServerUrn(self: ManagedInstance) -> str """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: ManagedInstance) -> str """
        ...

    @property
    def VolumeSpaceHealthState(self) -> HealthState:
        """ Get: VolumeSpaceHealthState(self: ManagedInstance) -> HealthState """
        ...


    @staticmethod
    def GetObjectFactory() -> SfcObjectFactory:
        """ GetObjectFactory() -> SfcObjectFactory """
        ...

    def Key(self, *args): #cannot find CLR method
        """ Key(managedInstanceName: str) """
        ...

    def Remove(self, sqlStoreConnection:SqlStoreConnection): # -> 
        """ Remove(self: ManagedInstance, sqlStoreConnection: SqlStoreConnection) """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class ManagedInstanceCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'IEnumerable'>, <type 'IComparer[Key]'>, <type 'ISfcCollection'>, <type 'IEnumerable[ManagedInstance]'>, <type 'ICollection[ManagedInstance]'>, <type 'IListSource'>, <type 'ICollection'>, <type 'object'>
    """
    ManagedInstanceCollection(parent: Utility)
    ManagedInstanceCollection(parent: Utility, customComparer: IComparer[str])
    """
    pass

class ManagementState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ManagementState, values: Discovered (1), Manageable (2), Managed (4), ManagementPending (3), Unknown (0) """
    Discovered: ManagementState = ...
    Manageable: ManagementState = ...
    Managed: ManagementState = ...
    ManagementPending: ManagementState = ...
    Unknown: ManagementState = ...
    value__ = ...


class NameKey(SfcKey): # skipped bases: <type 'IEquatable[SfcKey]'>, <type 'object'>
    """ NameKey(keyName: str) """
    @property
    def Name(self) -> str:
        """ Get: Name(self: NameKey) -> str """
        ...


    def __new__(cls, keyName:str) -> Self:
        """ __new__(cls: type, keyName: str) """
        ...


class Utility(IStorageUtilizationProvider, ISfcDomain2, SfcInstance, ISfcAlterable): # skipped bases: <type 'ISfcDomainLite'>, <type 'IAlterable'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'INotifyPropertyChanged'>, <type 'ISfcDomain'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'ISfcHasConnection'>, <type 'object'>
    """
    Utility()
    Utility(connection: SqlStoreConnection)
    """
    @property
    def Computers(self) -> ComputerCollection:
        """ Get: Computers(self: Utility) -> ComputerCollection """
        ...

    @property
    def CreatedBy(self) -> str:
        """ Get: CreatedBy(self: Utility) -> str """
        ...

    @property
    def DateCreated(self) -> DateTimeOffset:
        """ Get: DateCreated(self: Utility) -> DateTimeOffset """
        ...

    @property
    def DeployedDacCount(self) -> int:
        """ Get: DeployedDacCount(self: Utility) -> int """
        ...

    @property
    def DeployedDacHealthyCount(self) -> int:
        """ Get: DeployedDacHealthyCount(self: Utility) -> int """
        ...

    @property
    def DeployedDacManagementPendingCount(self) -> int:
        """ Get: DeployedDacManagementPendingCount(self: Utility) -> int """
        ...

    @property
    def DeployedDacOnOverutilizedComputerCount(self) -> int:
        """ Get: DeployedDacOnOverutilizedComputerCount(self: Utility) -> int """
        ...

    @property
    def DeployedDacOnUnderutilizedComputerCount(self) -> int:
        """ Get: DeployedDacOnUnderutilizedComputerCount(self: Utility) -> int """
        ...

    @property
    def DeployedDacOverutilizedCount(self) -> int:
        """ Get: DeployedDacOverutilizedCount(self: Utility) -> int """
        ...

    @property
    def DeployedDacs(self) -> DeployedDacCollection:
        """ Get: DeployedDacs(self: Utility) -> DeployedDacCollection """
        ...

    @property
    def DeployedDacUnderutilizedCount(self) -> int:
        """ Get: DeployedDacUnderutilizedCount(self: Utility) -> int """
        ...

    @property
    def DeployedDacUnhealthyCount(self) -> int:
        """ Get: DeployedDacUnhealthyCount(self: Utility) -> int """
        ...

    @property
    def DeployedDacWithFilesOnOverutilizedVolumeCount(self) -> int:
        """ Get: DeployedDacWithFilesOnOverutilizedVolumeCount(self: Utility) -> int """
        ...

    @property
    def DeployedDacWithFilesOnUnderutilizedVolumeCount(self) -> int:
        """ Get: DeployedDacWithFilesOnUnderutilizedVolumeCount(self: Utility) -> int """
        ...

    @property
    def DeployedDacWithOverutilizedFileCount(self) -> int:
        """ Get: DeployedDacWithOverutilizedFileCount(self: Utility) -> int """
        ...

    @property
    def DeployedDacWithOverutilizedProcessorCount(self) -> int:
        """ Get: DeployedDacWithOverutilizedProcessorCount(self: Utility) -> int """
        ...

    @property
    def DeployedDacWithUnderutilizedFileCount(self) -> int:
        """ Get: DeployedDacWithUnderutilizedFileCount(self: Utility) -> int """
        ...

    @property
    def DeployedDacWithUnderutilizedProcessorCount(self) -> int:
        """ Get: DeployedDacWithUnderutilizedProcessorCount(self: Utility) -> int """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: Utility) -> str
        Set: Description(self: Utility) = value
        """
        ...

    @property
    def ManagedInstanceCount(self) -> int:
        """ Get: ManagedInstanceCount(self: Utility) -> int """
        ...

    @property
    def ManagedInstanceHealthyCount(self) -> int:
        """ Get: ManagedInstanceHealthyCount(self: Utility) -> int """
        ...

    @property
    def ManagedInstanceManagementPendingCount(self) -> int:
        """ Get: ManagedInstanceManagementPendingCount(self: Utility) -> int """
        ...

    @property
    def ManagedInstanceOnOverutilizedComputerCount(self) -> int:
        """ Get: ManagedInstanceOnOverutilizedComputerCount(self: Utility) -> int """
        ...

    @property
    def ManagedInstanceOnUnderutilizedComputerCount(self) -> int:
        """ Get: ManagedInstanceOnUnderutilizedComputerCount(self: Utility) -> int """
        ...

    @property
    def ManagedInstanceOverutilizedCount(self) -> int:
        """ Get: ManagedInstanceOverutilizedCount(self: Utility) -> int """
        ...

    @property
    def ManagedInstances(self) -> ManagedInstanceCollection:
        """ Get: ManagedInstances(self: Utility) -> ManagedInstanceCollection """
        ...

    @property
    def ManagedInstanceUnderutilizedCount(self) -> int:
        """ Get: ManagedInstanceUnderutilizedCount(self: Utility) -> int """
        ...

    @property
    def ManagedInstanceUnhealthyCount(self) -> int:
        """ Get: ManagedInstanceUnhealthyCount(self: Utility) -> int """
        ...

    @property
    def ManagedInstanceWithFilesOnOverutilizedVolumeCount(self) -> int:
        """ Get: ManagedInstanceWithFilesOnOverutilizedVolumeCount(self: Utility) -> int """
        ...

    @property
    def ManagedInstanceWithFilesOnUnderutilizedVolumeCount(self) -> int:
        """ Get: ManagedInstanceWithFilesOnUnderutilizedVolumeCount(self: Utility) -> int """
        ...

    @property
    def ManagedInstanceWithOverutilizedFileCount(self) -> int:
        """ Get: ManagedInstanceWithOverutilizedFileCount(self: Utility) -> int """
        ...

    @property
    def ManagedInstanceWithOverutilizedProcessorCount(self) -> int:
        """ Get: ManagedInstanceWithOverutilizedProcessorCount(self: Utility) -> int """
        ...

    @property
    def ManagedInstanceWithUnderutilizedFileCount(self) -> int:
        """ Get: ManagedInstanceWithUnderutilizedFileCount(self: Utility) -> int """
        ...

    @property
    def ManagedInstanceWithUnderutilizedProcessorCount(self) -> int:
        """ Get: ManagedInstanceWithUnderutilizedProcessorCount(self: Utility) -> int """
        ...

    @property
    def MdwDatabaseName(self) -> str:
        """ Get: MdwDatabaseName(self: Utility) -> str """
        ...

    @property
    def MdwRetentionLengthInDaysForDaysHistory(self) -> int:
        """
        Get: MdwRetentionLengthInDaysForDaysHistory(self: Utility) -> int
        Set: MdwRetentionLengthInDaysForDaysHistory(self: Utility) = value
        """
        ...

    @property
    def MdwRetentionLengthInDaysForHoursHistory(self) -> int:
        """
        Get: MdwRetentionLengthInDaysForHoursHistory(self: Utility) -> int
        Set: MdwRetentionLengthInDaysForHoursHistory(self: Utility) = value
        """
        ...

    @property
    def MdwRetentionLengthInDaysForMinutesHistory(self) -> int:
        """
        Get: MdwRetentionLengthInDaysForMinutesHistory(self: Utility) -> int
        Set: MdwRetentionLengthInDaysForMinutesHistory(self: Utility) = value
        """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Utility) -> str """
        ...

    @property
    def OverUtilizationOccurenceFrequency(self) -> int:
        """
        Get: OverUtilizationOccurenceFrequency(self: Utility) -> int
        Set: OverUtilizationOccurenceFrequency(self: Utility) = value
        """
        ...

    @property
    def OverUtilizationTrailingWindow(self) -> int:
        """
        Get: OverUtilizationTrailingWindow(self: Utility) -> int
        Set: OverUtilizationTrailingWindow(self: Utility) = value
        """
        ...

    @property
    def PolicyStore(self) -> PolicyStore:
        """ Get: PolicyStore(self: Utility) -> PolicyStore """
        ...

    @property
    def SqlStoreConnection(self) -> SqlStoreConnection:
        """
        Get: SqlStoreConnection(self: Utility) -> SqlStoreConnection
        Set: SqlStoreConnection(self: Utility) = value
        """
        ...

    @property
    def TotalStorageCapacity(self) -> float:
        """ Get: TotalStorageCapacity(self: Utility) -> float """
        ...

    @property
    def TotalStorageUtilization(self) -> float:
        """ Get: TotalStorageUtilization(self: Utility) -> float """
        ...

    @property
    def UnderUtilizationOccurenceFrequency(self) -> int:
        """
        Get: UnderUtilizationOccurenceFrequency(self: Utility) -> int
        Set: UnderUtilizationOccurenceFrequency(self: Utility) = value
        """
        ...

    @property
    def UnderUtilizationTrailingWindow(self) -> int:
        """
        Get: UnderUtilizationTrailingWindow(self: Utility) -> int
        Set: UnderUtilizationTrailingWindow(self: Utility) = value
        """
        ...

    @property
    def UtilityName(self) -> str:
        """
        Get: UtilityName(self: Utility) -> str
        Set: UtilityName(self: Utility) = value
        """
        ...


    def Alter(self): # -> 
        """ Alter(self: Utility) """
        ...

    @staticmethod
    def Connect(connection:SqlStoreConnection) -> Utility:
        """ Connect(connection: SqlStoreConnection) -> Utility """
        ...

    @staticmethod
    def CreateUtility(utilityName:str, sqlStoreConnection:SqlStoreConnection, agentProxyAccount:str = ..., agentProxyPassword:SqlSecureString = ...) -> Utility:
        """
        CreateUtility(utilityName: str, sqlStoreConnection: SqlStoreConnection) -> Utility
        CreateUtility(utilityName: str, sqlStoreConnection: SqlStoreConnection, agentProxyAccount: str, agentProxyPassword: SqlSecureString) -> Utility
        """
        ...

    def EnrollInstance(self, sqlStoreConnection:SqlStoreConnection, agentProxyAccount:str = ..., agentProxyPassword:SqlSecureString = ...) -> ManagedInstance:
        """
        EnrollInstance(self: Utility, sqlStoreConnection: SqlStoreConnection) -> ManagedInstance
        EnrollInstance(self: Utility, sqlStoreConnection: SqlStoreConnection, agentProxyAccount: str, agentProxyPassword: SqlSecureString) -> ManagedInstance
        """
        ...

    @staticmethod
    def IsLoginUtilityReader(storeConnection:SqlStoreConnection) -> bool:
        """ IsLoginUtilityReader(storeConnection: SqlStoreConnection) -> bool """
        ...

    @staticmethod
    def IsUtilityControlPoint(storeConnection:SqlStoreConnection) -> bool:
        """ IsUtilityControlPoint(storeConnection: SqlStoreConnection) -> bool """
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


class UtilityException(SqlServerManagementException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    UtilityException()
    UtilityException(message: str)
    UtilityException(message: str, innerException: Exception)
    """
    @property
    def ProdVer(self):
        ...


    def Init(self, *args): #cannot find CLR method
        """ Init(self: UtilityException) """
        ...

    def SetHelpContext(self, *args): #cannot find CLR method
        """ SetHelpContext(self: UtilityException, resource: str) -> UtilityException """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    SerializeObjectState = ...


class Volume(SfcInstance): # skipped bases: <type 'INotifyPropertyChanged'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcDiscoverObject'>, <type 'ISfcPropertyProvider'>, <type 'object'>
    """
    Volume()
    Volume(parent: Computer, name: str)
    """
    @property
    def DeviceId(self) -> str:
        """ Get: DeviceId(self: Volume) -> str """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: Volume) -> int """
        ...

    @property
    def IdentityKey(self): # -> Key
        """ Get: IdentityKey(self: Volume) -> Key """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: Volume) -> str """
        ...

    @property
    def TotalSpace(self) -> Single:
        """ Get: TotalSpace(self: Volume) -> Single """
        ...

    @property
    def TotalSpaceUsed(self) -> Single:
        """ Get: TotalSpaceUsed(self: Volume) -> Single """
        ...

    @property
    def TotalSpaceUtilization(self) -> Single:
        """ Get: TotalSpaceUtilization(self: Volume) -> Single """
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
        """
        ...

    def __new__(cls, parent:Computer = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: Computer, name: str)
        """
        ...

    propertyChanged = ...
    propertyMetadataChanged = ...


class VolumeCollection(SfcCollatedDictionaryCollection): # skipped bases: <type 'ICollection[Volume]'>, <type 'IEnumerable[Volume]'>, <type 'IEnumerable'>, <type 'ISfcCollection'>, <type 'IListSource'>, <type 'IComparer[Key]'>, <type 'ICollection'>, <type 'object'>
    """
    VolumeCollection(parent: Computer)
    VolumeCollection(parent: Computer, customComparer: IComparer[str])
    """
    pass

