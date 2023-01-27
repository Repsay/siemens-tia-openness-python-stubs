# encoding: utf-8
# module System.Printing calls itself Printing
# from System.Printing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Byte, DateTime, Enum, EventArgs, IDisposable

from System.Collections import IEnumerable, IEnumerator

from System.Collections.Specialized import StringCollection

from System.ComponentModel.DataAnnotations import ValidationResult

from System.IO import MemoryStream, Stream

from System.Printing.IndexedProperties import PrintPropertyDictionary

from System.Threading import ThreadPriority

from System.Windows.Xps import XpsDocumentWriter

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (
    PackagingProgressEventArgs, PrintCapabilities, PrintTicket, 
    PrintTicketScope, field#)
"""

# no functions
# classes

class EnumeratedPrintQueueTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) EnumeratedPrintQueueTypes, values: Connections (16), DirectPrinting (2), EnableBidi (2048), EnableDevQuery (128), Fax (16384), KeepPrintedJobs (256), Local (64), PublishedInDirectoryServices (8192), PushedMachineConnection (262144), PushedUserConnection (131072), Queued (1), RawOnly (4096), Shared (8), TerminalServer (32768), WorkOffline (1024) """
    Connections: EnumeratedPrintQueueTypes = ...
    DirectPrinting: EnumeratedPrintQueueTypes = ...
    EnableBidi: EnumeratedPrintQueueTypes = ...
    EnableDevQuery: EnumeratedPrintQueueTypes = ...
    Fax: EnumeratedPrintQueueTypes = ...
    KeepPrintedJobs: EnumeratedPrintQueueTypes = ...
    Local: EnumeratedPrintQueueTypes = ...
    PublishedInDirectoryServices: EnumeratedPrintQueueTypes = ...
    PushedMachineConnection: EnumeratedPrintQueueTypes = ...
    PushedUserConnection: EnumeratedPrintQueueTypes = ...
    Queued: EnumeratedPrintQueueTypes = ...
    RawOnly: EnumeratedPrintQueueTypes = ...
    Shared: EnumeratedPrintQueueTypes = ...
    TerminalServer: EnumeratedPrintQueueTypes = ...
    value__ = ...
    WorkOffline: EnumeratedPrintQueueTypes = ...


class PrintSystemObject(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsDisposed(self):
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: PrintSystemObject) -> str """
        ...

    @property
    def Parent(self) -> PrintSystemObject:
        """ Get: Parent(self: PrintSystemObject) -> PrintSystemObject """
        ...

    @property
    def PropertiesCollection(self) -> PrintPropertyDictionary:
        """ Get: PropertiesCollection(self: PrintSystemObject) -> PrintPropertyDictionary """
        ...


    def BaseAttributeNames(self, *args): #cannot find CLR method
        """ BaseAttributeNames() -> Array[str] """
        ...

    def Commit(self): # -> 
        """ Commit(self: PrintSystemObject) """
        ...

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: PrintSystemObject) """
        ...

    def InternalDispose(self, *args): #cannot find CLR method
        """ InternalDispose(self: PrintSystemObject, disposing: bool) """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: PrintSystemObject) """
        ...


class PrintServer(PrintSystemObject): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    PrintServer(path: str, propertiesFilter: Array[str], desiredAccess: PrintSystemDesiredAccess)
    PrintServer(path: str, propertiesFilter: Array[PrintServerIndexedProperty], desiredAccess: PrintSystemDesiredAccess)
    PrintServer(path: str, desiredAccess: PrintSystemDesiredAccess)
    PrintServer(desiredAccess: PrintSystemDesiredAccess)
    PrintServer(path: str, propertiesFilter: Array[str])
    PrintServer(path: str, propertiesFilter: Array[PrintServerIndexedProperty])
    PrintServer(path: str)
    PrintServer()
    """
    @property
    def BeepEnabled(self) -> bool:
        """
        Get: BeepEnabled(self: PrintServer) -> bool
        Set: BeepEnabled(self: PrintServer) = value
        """
        ...

    @property
    def DefaultPortThreadPriority(self) -> ThreadPriority:
        """ Get: DefaultPortThreadPriority(self: PrintServer) -> ThreadPriority """
        ...

    @property
    def DefaultSchedulerPriority(self) -> ThreadPriority:
        """ Get: DefaultSchedulerPriority(self: PrintServer) -> ThreadPriority """
        ...

    @property
    def DefaultSpoolDirectory(self) -> str:
        """
        Get: DefaultSpoolDirectory(self: PrintServer) -> str
        Set: DefaultSpoolDirectory(self: PrintServer) = value
        """
        ...

    @property
    def EventLog(self) -> PrintServerEventLoggingTypes:
        """
        Get: EventLog(self: PrintServer) -> PrintServerEventLoggingTypes
        Set: EventLog(self: PrintServer) = value
        """
        ...

    @property
    def IsDelayInitialized(self):
        ...

    @property
    def MajorVersion(self) -> int:
        """ Get: MajorVersion(self: PrintServer) -> int """
        ...

    @property
    def MinorVersion(self) -> int:
        """ Get: MinorVersion(self: PrintServer) -> int """
        ...

    @property
    def NetPopup(self) -> bool:
        """
        Get: NetPopup(self: PrintServer) -> bool
        Set: NetPopup(self: PrintServer) = value
        """
        ...

    @property
    def PortThreadPriority(self) -> ThreadPriority:
        """
        Get: PortThreadPriority(self: PrintServer) -> ThreadPriority
        Set: PortThreadPriority(self: PrintServer) = value
        """
        ...

    @property
    def RestartJobOnPoolEnabled(self) -> bool:
        """
        Get: RestartJobOnPoolEnabled(self: PrintServer) -> bool
        Set: RestartJobOnPoolEnabled(self: PrintServer) = value
        """
        ...

    @property
    def RestartJobOnPoolTimeout(self) -> int:
        """
        Get: RestartJobOnPoolTimeout(self: PrintServer) -> int
        Set: RestartJobOnPoolTimeout(self: PrintServer) = value
        """
        ...

    @property
    def SchedulerPriority(self) -> ThreadPriority:
        """
        Get: SchedulerPriority(self: PrintServer) -> ThreadPriority
        Set: SchedulerPriority(self: PrintServer) = value
        """
        ...

    @property
    def SubSystemVersion(self) -> Byte:
        """ Get: SubSystemVersion(self: PrintServer) -> Byte """
        ...


    @staticmethod
    def DeletePrintQueue(*__args:PrintQueue) -> bool:
        """
        DeletePrintQueue(printQueue: PrintQueue) -> bool
        DeletePrintQueue(printQueueName: str) -> bool
        """
        ...

    def GetPrintQueue(self, printQueueName:str, propertiesFilter:Array = ...) -> PrintQueue:
        """
        GetPrintQueue(self: PrintServer, printQueueName: str, propertiesFilter: Array[str]) -> PrintQueue
        GetPrintQueue(self: PrintServer, printQueueName: str) -> PrintQueue
        """
        ...

    def GetPrintQueues(self, *__args:Array) -> PrintQueueCollection:
        """
        GetPrintQueues(self: PrintServer, propertiesFilter: Array[str], enumerationFlag: Array[EnumeratedPrintQueueTypes]) -> PrintQueueCollection
        GetPrintQueues(self: PrintServer, propertiesFilter: Array[PrintQueueIndexedProperty], enumerationFlag: Array[EnumeratedPrintQueueTypes]) -> PrintQueueCollection
        GetPrintQueues(self: PrintServer, enumerationFlag: Array[EnumeratedPrintQueueTypes]) -> PrintQueueCollection
        GetPrintQueues(self: PrintServer, propertiesFilter: Array[str]) -> PrintQueueCollection
        GetPrintQueues(self: PrintServer, propertiesFilter: Array[PrintQueueIndexedProperty]) -> PrintQueueCollection
        GetPrintQueues(self: PrintServer) -> PrintQueueCollection
        """
        ...

    def InstallPrintQueue(self, printQueueName:str, driverName:str, portNames:Array, printProcessorName:str, *__args:PrintPropertyDictionary) -> PrintQueue:
        """
        InstallPrintQueue(self: PrintServer, printQueueName: str, driverName: str, portNames: Array[str], printProcessorName: str, initialParameters: PrintPropertyDictionary) -> PrintQueue
        InstallPrintQueue(self: PrintServer, printQueueName: str, driverName: str, portNames: Array[str], printProcessorName: str, printQueueAttributes: PrintQueueAttributes, printQueueShareName: str, printQueueComment: str, printQueueLocation: str, printQueueSeparatorFile: str, printQueuePriority: int, printQueueDefaultPriority: int) -> PrintQueue
        InstallPrintQueue(self: PrintServer, printQueueName: str, driverName: str, portNames: Array[str], printProcessorName: str, printQueueAttributes: PrintQueueAttributes, printQueueProperty: PrintQueueStringProperty, printQueuePriority: int, printQueueDefaultPriority: int) -> PrintQueue
        InstallPrintQueue(self: PrintServer, printQueueName: str, driverName: str, portNames: Array[str], printProcessorName: str, printQueueAttributes: PrintQueueAttributes) -> PrintQueue
        """
        ...


class LocalPrintServer(PrintServer): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    LocalPrintServer(propertiesFilter: Array[str], desiredAccess: PrintSystemDesiredAccess)
    LocalPrintServer(propertiesFilter: Array[LocalPrintServerIndexedProperty], desiredAccess: PrintSystemDesiredAccess)
    LocalPrintServer(desiredAccess: PrintSystemDesiredAccess)
    LocalPrintServer(propertiesFilter: Array[str])
    LocalPrintServer(propertiesFilter: Array[LocalPrintServerIndexedProperty])
    LocalPrintServer()
    """
    @property
    def DefaultPrintQueue(self) -> PrintQueue:
        """
        Get: DefaultPrintQueue(self: LocalPrintServer) -> PrintQueue
        Set: DefaultPrintQueue(self: LocalPrintServer) = value
        """
        ...


    def ConnectToPrintQueue(self, *__args:str) -> bool:
        """
        ConnectToPrintQueue(self: LocalPrintServer, printQueuePath: str) -> bool
        ConnectToPrintQueue(self: LocalPrintServer, printer: PrintQueue) -> bool
        """
        ...

    def DisconnectFromPrintQueue(self, *__args:PrintQueue) -> bool:
        """
        DisconnectFromPrintQueue(self: LocalPrintServer, printer: PrintQueue) -> bool
        DisconnectFromPrintQueue(self: LocalPrintServer, printQueuePath: str) -> bool
        """
        ...

    @staticmethod
    def GetDefaultPrintQueue() -> PrintQueue:
        """ GetDefaultPrintQueue() -> PrintQueue """
        ...


class LocalPrintServerIndexedProperty(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LocalPrintServerIndexedProperty, values: BeepEnabled (5), DefaultPortThreadPriority (2), DefaultPrintQueue (12), DefaultSchedulerPriority (4), DefaultSpoolDirectory (0), EventLog (7), MajorVersion (8), MinorVersion (9), NetPopup (6), PortThreadPriority (1), RestartJobOnPoolEnabled (11), RestartJobOnPoolTimeout (10), SchedulerPriority (3) """
    BeepEnabled: LocalPrintServerIndexedProperty = ...
    DefaultPortThreadPriority: LocalPrintServerIndexedProperty = ...
    DefaultPrintQueue: LocalPrintServerIndexedProperty = ...
    DefaultSchedulerPriority: LocalPrintServerIndexedProperty = ...
    DefaultSpoolDirectory: LocalPrintServerIndexedProperty = ...
    EventLog: LocalPrintServerIndexedProperty = ...
    MajorVersion: LocalPrintServerIndexedProperty = ...
    MinorVersion: LocalPrintServerIndexedProperty = ...
    NetPopup: LocalPrintServerIndexedProperty = ...
    PortThreadPriority: LocalPrintServerIndexedProperty = ...
    RestartJobOnPoolEnabled: LocalPrintServerIndexedProperty = ...
    RestartJobOnPoolTimeout: LocalPrintServerIndexedProperty = ...
    SchedulerPriority: LocalPrintServerIndexedProperty = ...
    value__ = ...


class PrintDocumentImageableArea: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ExtentHeight(self) -> float:
        """ Get: ExtentHeight(self: PrintDocumentImageableArea) -> float """
        ...

    @property
    def ExtentWidth(self) -> float:
        """ Get: ExtentWidth(self: PrintDocumentImageableArea) -> float """
        ...

    @property
    def MediaSizeHeight(self) -> float:
        """ Get: MediaSizeHeight(self: PrintDocumentImageableArea) -> float """
        ...

    @property
    def MediaSizeWidth(self) -> float:
        """ Get: MediaSizeWidth(self: PrintDocumentImageableArea) -> float """
        ...

    @property
    def OriginHeight(self) -> float:
        """ Get: OriginHeight(self: PrintDocumentImageableArea) -> float """
        ...

    @property
    def OriginWidth(self) -> float:
        """ Get: OriginWidth(self: PrintDocumentImageableArea) -> float """
        ...



class PrintFilter(PrintSystemObject): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    pass

class PrintDriver(PrintFilter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    def Commit(self): # -> 
        """ Commit(self: PrintDriver) """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: PrintDriver) """
        ...


class PrintSystemObjects(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    pass

class PrintJobInfoCollection(PrintSystemObjects, IEnumerable): # skipped bases: <type 'IDisposable'>, <type 'IEnumerable'>, <type 'object'>
    """ PrintJobInfoCollection(printQueue: PrintQueue, propertyFilter: Array[str]) """
    def Add(self, printObject:PrintSystemJobInfo): # -> 
        """ Add(self: PrintJobInfoCollection, printObject: PrintSystemJobInfo) """
        ...

    def GetNonGenericEnumerator(self) -> IEnumerator:
        """ GetNonGenericEnumerator(self: PrintJobInfoCollection) -> IEnumerator """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PrintSystemJobInfo](enumerable: IEnumerable[PrintSystemJobInfo], value: PrintSystemJobInfo) -> bool """
        ...

    def __new__(cls, printQueue:PrintQueue, propertyFilter:Array) -> Self:
        """ __new__(cls: type, printQueue: PrintQueue, propertyFilter: Array[str]) """
        ...


class PrintJobPriority(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PrintJobPriority, values: Default (1), Maximum (99), Minimum (1), None (0) """
    Default: PrintJobPriority = ...
    Maximum: PrintJobPriority = ...
    Minimum: PrintJobPriority = ...
    value__ = ...


class PrintJobSettings: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CurrentPrintTicket(self): # -> PrintTicket
        """
        Get: CurrentPrintTicket(self: PrintJobSettings) -> PrintTicket
        Set: CurrentPrintTicket(self: PrintJobSettings) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: PrintJobSettings) -> str
        Set: Description(self: PrintJobSettings) = value
        """
        ...



class PrintJobStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PrintJobStatus, values: Blocked (512), Completed (4096), Deleted (256), Deleting (4), Error (2), None (0), Offline (32), PaperOut (64), Paused (1), Printed (128), Printing (16), Restarted (2048), Retained (8192), Spooling (8), UserIntervention (1024) """
    Blocked: PrintJobStatus = ...
    Completed: PrintJobStatus = ...
    Deleted: PrintJobStatus = ...
    Deleting: PrintJobStatus = ...
    Error: PrintJobStatus = ...
    Offline: PrintJobStatus = ...
    PaperOut: PrintJobStatus = ...
    Paused: PrintJobStatus = ...
    Printed: PrintJobStatus = ...
    Printing: PrintJobStatus = ...
    Restarted: PrintJobStatus = ...
    Retained: PrintJobStatus = ...
    Spooling: PrintJobStatus = ...
    UserIntervention: PrintJobStatus = ...
    value__ = ...


class PrintJobType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PrintJobType, values: Legacy (2), None (0), Xps (1) """
    Legacy: PrintJobType = ...
    value__ = ...
    Xps: PrintJobType = ...


class PrintPort(PrintSystemObject): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    pass

class PrintProcessor(PrintFilter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    def Commit(self): # -> 
        """ Commit(self: PrintProcessor) """
        ...

    def Refresh(self): # -> 
        """ Refresh(self: PrintProcessor) """
        ...


class PrintQueue(PrintSystemObject): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    PrintQueue(printServer: PrintServer, printQueueName: str, propertyFilter: Array[PrintQueueIndexedProperty], desiredAccess: PrintSystemDesiredAccess)
    PrintQueue(printServer: PrintServer, printQueueName: str, propertyFilter: Array[str], desiredAccess: PrintSystemDesiredAccess)
    PrintQueue(printServer: PrintServer, printQueueName: str, printSchemaVersion: int, desiredAccess: PrintSystemDesiredAccess)
    PrintQueue(printServer: PrintServer, printQueueName: str, desiredAccess: PrintSystemDesiredAccess)
    PrintQueue(printServer: PrintServer, printQueueName: str, propertyFilter: Array[PrintQueueIndexedProperty])
    PrintQueue(printServer: PrintServer, printQueueName: str, propertyFilter: Array[str])
    PrintQueue(printServer: PrintServer, printQueueName: str, printSchemaVersion: int)
    PrintQueue(printServer: PrintServer, printQueueName: str)
    """
    @property
    def AveragePagesPerMinute(self) -> int:
        """ Get: AveragePagesPerMinute(self: PrintQueue) -> int """
        ...

    @property
    def ClientPrintSchemaVersion(self) -> int:
        """ Get: ClientPrintSchemaVersion(self: PrintQueue) -> int """
        ...

    @property
    def Comment(self) -> str:
        """
        Get: Comment(self: PrintQueue) -> str
        Set: Comment(self: PrintQueue) = value
        """
        ...

    @property
    def CurrentJobSettings(self) -> PrintJobSettings:
        """ Get: CurrentJobSettings(self: PrintQueue) -> PrintJobSettings """
        ...

    @property
    def DefaultPrintTicket(self): # -> PrintTicket
        """
        Get: DefaultPrintTicket(self: PrintQueue) -> PrintTicket
        Set: DefaultPrintTicket(self: PrintQueue) = value
        """
        ...

    @property
    def DefaultPriority(self) -> int:
        """
        Get: DefaultPriority(self: PrintQueue) -> int
        Set: DefaultPriority(self: PrintQueue) = value
        """
        ...

    @property
    def Description(self) -> str:
        """ Get: Description(self: PrintQueue) -> str """
        ...

    @property
    def FullName(self) -> str:
        """ Get: FullName(self: PrintQueue) -> str """
        ...

    @property
    def HasPaperProblem(self) -> bool:
        """ Get: HasPaperProblem(self: PrintQueue) -> bool """
        ...

    @property
    def HasToner(self) -> bool:
        """ Get: HasToner(self: PrintQueue) -> bool """
        ...

    @property
    def HostingPrintServer(self) -> PrintServer:
        """ Get: HostingPrintServer(self: PrintQueue) -> PrintServer """
        ...

    @property
    def InPartialTrust(self) -> bool:
        """
        Get: InPartialTrust(self: PrintQueue) -> bool
        Set: InPartialTrust(self: PrintQueue) = value
        """
        ...

    @property
    def IsBidiEnabled(self) -> bool:
        """ Get: IsBidiEnabled(self: PrintQueue) -> bool """
        ...

    @property
    def IsBusy(self) -> bool:
        """ Get: IsBusy(self: PrintQueue) -> bool """
        ...

    @property
    def IsDevQueryEnabled(self) -> bool:
        """ Get: IsDevQueryEnabled(self: PrintQueue) -> bool """
        ...

    @property
    def IsDirect(self) -> bool:
        """ Get: IsDirect(self: PrintQueue) -> bool """
        ...

    @property
    def IsDoorOpened(self) -> bool:
        """ Get: IsDoorOpened(self: PrintQueue) -> bool """
        ...

    @property
    def IsHidden(self) -> bool:
        """ Get: IsHidden(self: PrintQueue) -> bool """
        ...

    @property
    def IsInError(self) -> bool:
        """ Get: IsInError(self: PrintQueue) -> bool """
        ...

    @property
    def IsInitializing(self) -> bool:
        """ Get: IsInitializing(self: PrintQueue) -> bool """
        ...

    @property
    def IsIOActive(self) -> bool:
        """ Get: IsIOActive(self: PrintQueue) -> bool """
        ...

    @property
    def IsManualFeedRequired(self) -> bool:
        """ Get: IsManualFeedRequired(self: PrintQueue) -> bool """
        ...

    @property
    def IsNotAvailable(self) -> bool:
        """ Get: IsNotAvailable(self: PrintQueue) -> bool """
        ...

    @property
    def IsOffline(self) -> bool:
        """ Get: IsOffline(self: PrintQueue) -> bool """
        ...

    @property
    def IsOutOfMemory(self) -> bool:
        """ Get: IsOutOfMemory(self: PrintQueue) -> bool """
        ...

    @property
    def IsOutOfPaper(self) -> bool:
        """ Get: IsOutOfPaper(self: PrintQueue) -> bool """
        ...

    @property
    def IsOutputBinFull(self) -> bool:
        """ Get: IsOutputBinFull(self: PrintQueue) -> bool """
        ...

    @property
    def IsPaperJammed(self) -> bool:
        """ Get: IsPaperJammed(self: PrintQueue) -> bool """
        ...

    @property
    def IsPaused(self) -> bool:
        """ Get: IsPaused(self: PrintQueue) -> bool """
        ...

    @property
    def IsPendingDeletion(self) -> bool:
        """ Get: IsPendingDeletion(self: PrintQueue) -> bool """
        ...

    @property
    def IsPowerSaveOn(self) -> bool:
        """ Get: IsPowerSaveOn(self: PrintQueue) -> bool """
        ...

    @property
    def IsPrinting(self) -> bool:
        """ Get: IsPrinting(self: PrintQueue) -> bool """
        ...

    @property
    def IsProcessing(self) -> bool:
        """ Get: IsProcessing(self: PrintQueue) -> bool """
        ...

    @property
    def IsPublished(self) -> bool:
        """ Get: IsPublished(self: PrintQueue) -> bool """
        ...

    @property
    def IsQueued(self) -> bool:
        """ Get: IsQueued(self: PrintQueue) -> bool """
        ...

    @property
    def IsRawOnlyEnabled(self) -> bool:
        """ Get: IsRawOnlyEnabled(self: PrintQueue) -> bool """
        ...

    @property
    def IsServerUnknown(self) -> bool:
        """ Get: IsServerUnknown(self: PrintQueue) -> bool """
        ...

    @property
    def IsShared(self) -> bool:
        """ Get: IsShared(self: PrintQueue) -> bool """
        ...

    @property
    def IsTonerLow(self) -> bool:
        """ Get: IsTonerLow(self: PrintQueue) -> bool """
        ...

    @property
    def IsWaiting(self) -> bool:
        """ Get: IsWaiting(self: PrintQueue) -> bool """
        ...

    @property
    def IsWarmingUp(self) -> bool:
        """ Get: IsWarmingUp(self: PrintQueue) -> bool """
        ...

    @property
    def IsXpsDevice(self) -> bool:
        """ Get: IsXpsDevice(self: PrintQueue) -> bool """
        ...

    @property
    def KeepPrintedJobs(self) -> bool:
        """ Get: KeepPrintedJobs(self: PrintQueue) -> bool """
        ...

    @property
    def Location(self) -> str:
        """
        Get: Location(self: PrintQueue) -> str
        Set: Location(self: PrintQueue) = value
        """
        ...

    @property
    def MaxPrintSchemaVersion(self) -> int:
        """ Get: MaxPrintSchemaVersion() -> int """
        ...

    @property
    def NeedUserIntervention(self) -> bool:
        """ Get: NeedUserIntervention(self: PrintQueue) -> bool """
        ...

    @property
    def NumberOfJobs(self) -> int:
        """ Get: NumberOfJobs(self: PrintQueue) -> int """
        ...

    @property
    def PagePunt(self) -> bool:
        """ Get: PagePunt(self: PrintQueue) -> bool """
        ...

    @property
    def PrintingIsCancelled(self) -> bool:
        """
        Get: PrintingIsCancelled(self: PrintQueue) -> bool
        Set: PrintingIsCancelled(self: PrintQueue) = value
        """
        ...

    @property
    def Priority(self) -> int:
        """
        Get: Priority(self: PrintQueue) -> int
        Set: Priority(self: PrintQueue) = value
        """
        ...

    @property
    def QueueAttributes(self) -> PrintQueueAttributes:
        """ Get: QueueAttributes(self: PrintQueue) -> PrintQueueAttributes """
        ...

    @property
    def QueueDriver(self) -> PrintDriver:
        """
        Get: QueueDriver(self: PrintQueue) -> PrintDriver
        Set: QueueDriver(self: PrintQueue) = value
        """
        ...

    @property
    def QueuePort(self) -> PrintPort:
        """
        Get: QueuePort(self: PrintQueue) -> PrintPort
        Set: QueuePort(self: PrintQueue) = value
        """
        ...

    @property
    def QueuePrintProcessor(self) -> PrintProcessor:
        """
        Get: QueuePrintProcessor(self: PrintQueue) -> PrintProcessor
        Set: QueuePrintProcessor(self: PrintQueue) = value
        """
        ...

    @property
    def QueueStatus(self) -> PrintQueueStatus:
        """ Get: QueueStatus(self: PrintQueue) -> PrintQueueStatus """
        ...

    @property
    def ScheduleCompletedJobsFirst(self) -> bool:
        """ Get: ScheduleCompletedJobsFirst(self: PrintQueue) -> bool """
        ...

    @property
    def SeparatorFile(self) -> str:
        """
        Get: SeparatorFile(self: PrintQueue) -> str
        Set: SeparatorFile(self: PrintQueue) = value
        """
        ...

    @property
    def ShareName(self) -> str:
        """
        Get: ShareName(self: PrintQueue) -> str
        Set: ShareName(self: PrintQueue) = value
        """
        ...

    @property
    def StartTimeOfDay(self) -> int:
        """
        Get: StartTimeOfDay(self: PrintQueue) -> int
        Set: StartTimeOfDay(self: PrintQueue) = value
        """
        ...

    @property
    def UntilTimeOfDay(self) -> int:
        """
        Get: UntilTimeOfDay(self: PrintQueue) -> int
        Set: UntilTimeOfDay(self: PrintQueue) = value
        """
        ...

    @property
    def UserPrintTicket(self): # -> PrintTicket
        """
        Get: UserPrintTicket(self: PrintQueue) -> PrintTicket
        Set: UserPrintTicket(self: PrintQueue) = value
        """
        ...


    def AddJob(self, jobName:str = ..., *__args) -> PrintSystemJobInfo: # Not found arg types: {'*__args': 'PrintTicket'}
        """
        AddJob(self: PrintQueue, jobName: str, documentPath: str, fastCopy: bool, printTicket: PrintTicket) -> PrintSystemJobInfo
        AddJob(self: PrintQueue, jobName: str, documentPath: str, fastCopy: bool) -> PrintSystemJobInfo
        AddJob(self: PrintQueue, jobName: str, printTicket: PrintTicket) -> PrintSystemJobInfo
        AddJob(self: PrintQueue, jobName: str) -> PrintSystemJobInfo
        AddJob(self: PrintQueue) -> PrintSystemJobInfo
        """
        ...

    @staticmethod
    def CreateXpsDocumentWriter(*__args:PrintDocumentImageableArea) -> Tuple_[XpsDocumentWriter, PrintDocumentImageableArea]:
        """
        CreateXpsDocumentWriter(jobDescription: str, documentImageableArea: PrintDocumentImageableArea, pageRangeSelection: PageRangeSelection, pageRange: PageRange) -> (XpsDocumentWriter, PrintDocumentImageableArea, PageRangeSelection, PageRange)
        CreateXpsDocumentWriter(jobDescription: str, documentImageableArea: PrintDocumentImageableArea) -> (XpsDocumentWriter, PrintDocumentImageableArea)
        CreateXpsDocumentWriter(documentImageableArea: PrintDocumentImageableArea, pageRangeSelection: PageRangeSelection, pageRange: PageRange) -> (XpsDocumentWriter, PrintDocumentImageableArea, PageRangeSelection, PageRange)
        CreateXpsDocumentWriter(documentImageableArea: PrintDocumentImageableArea) -> (XpsDocumentWriter, PrintDocumentImageableArea)
        CreateXpsDocumentWriter(width: float, height: float) -> (XpsDocumentWriter, float, float)
        CreateXpsDocumentWriter(printQueue: PrintQueue) -> XpsDocumentWriter
        """
        ...

    def GetJob(self, jobId:int) -> PrintSystemJobInfo:
        """ GetJob(self: PrintQueue, jobId: int) -> PrintSystemJobInfo """
        ...

    def GetPrintCapabilities(self, printTicket = ...): # -> PrintCapabilities # Not found arg types: {'printTicket': 'PrintTicket'}
        """
        GetPrintCapabilities(self: PrintQueue) -> PrintCapabilities
        GetPrintCapabilities(self: PrintQueue, printTicket: PrintTicket) -> PrintCapabilities
        """
        ...

    def GetPrintCapabilitiesAsXml(self, printTicket = ...) -> MemoryStream: # Not found arg types: {'printTicket': 'PrintTicket'}
        """
        GetPrintCapabilitiesAsXml(self: PrintQueue) -> MemoryStream
        GetPrintCapabilitiesAsXml(self: PrintQueue, printTicket: PrintTicket) -> MemoryStream
        """
        ...

    def GetPrintJobInfoCollection(self) -> PrintJobInfoCollection:
        """ GetPrintJobInfoCollection(self: PrintQueue) -> PrintJobInfoCollection """
        ...

    def MergeAndValidatePrintTicket(self, basePrintTicket, deltaPrintTicket, scope = ...) -> ValidationResult: # Not found arg types: {'basePrintTicket': 'PrintTicket', 'deltaPrintTicket': 'PrintTicket', 'scope': 'PrintTicketScope'}
        """
        MergeAndValidatePrintTicket(self: PrintQueue, basePrintTicket: PrintTicket, deltaPrintTicket: PrintTicket, scope: PrintTicketScope) -> ValidationResult
        MergeAndValidatePrintTicket(self: PrintQueue, basePrintTicket: PrintTicket, deltaPrintTicket: PrintTicket) -> ValidationResult
        """
        ...

    def Pause(self): # -> 
        """ Pause(self: PrintQueue) """
        ...

    def Purge(self): # -> 
        """ Purge(self: PrintQueue) """
        ...

    def Resume(self): # -> 
        """ Resume(self: PrintQueue) """
        ...



class PrintQueueAttributes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PrintQueueAttributes, values: Direct (2), EnableBidi (2048), EnableDevQuery (128), Hidden (32), KeepPrintedJobs (256), None (0), Published (8192), Queued (1), RawOnly (4096), ScheduleCompletedJobsFirst (512), Shared (8) """
    Direct: PrintQueueAttributes = ...
    EnableBidi: PrintQueueAttributes = ...
    EnableDevQuery: PrintQueueAttributes = ...
    Hidden: PrintQueueAttributes = ...
    KeepPrintedJobs: PrintQueueAttributes = ...
    Published: PrintQueueAttributes = ...
    Queued: PrintQueueAttributes = ...
    RawOnly: PrintQueueAttributes = ...
    ScheduleCompletedJobsFirst: PrintQueueAttributes = ...
    Shared: PrintQueueAttributes = ...
    value__ = ...


class PrintQueueCollection(PrintSystemObjects, IEnumerable): # skipped bases: <type 'IDisposable'>, <type 'IEnumerable'>, <type 'object'>
    """
    PrintQueueCollection(printServer: PrintServer, propertyFilter: Array[str])
    PrintQueueCollection(printServer: PrintServer, propertyFilter: Array[str], enumerationFlag: Array[EnumeratedPrintQueueTypes])
    PrintQueueCollection()
    """
    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot() -> object """
        ...


    def Add(self, printObject:PrintQueue): # -> 
        """ Add(self: PrintQueueCollection, printObject: PrintQueue) """
        ...

    def GetNonGenericEnumerator(self) -> IEnumerator:
        """ GetNonGenericEnumerator(self: PrintQueueCollection) -> IEnumerator """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PrintQueue](enumerable: IEnumerable[PrintQueue], value: PrintQueue) -> bool """
        ...

    def __new__(cls, printServer:PrintServer = ..., propertyFilter:Array = ..., enumerationFlag:Array = ...) -> Self:
        """
        __new__(cls: type, printServer: PrintServer, propertyFilter: Array[str])
        __new__(cls: type, printServer: PrintServer, propertyFilter: Array[str], enumerationFlag: Array[EnumeratedPrintQueueTypes])
        __new__(cls: type)
        """
        ...



class PrintQueueIndexedProperty(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PrintQueueIndexedProperty, values: AveragePagesPerMinute (9), Comment (2), DefaultPrintTicket (19), DefaultPriority (6), Description (4), HostingPrintServer (15), Location (3), Name (0), NumberOfJobs (10), Priority (5), QueueAttributes (11), QueueDriver (12), QueuePort (13), QueuePrintProcessor (14), QueueStatus (16), SeparatorFile (17), ShareName (1), StartTimeOfDay (7), UntilTimeOfDay (8), UserPrintTicket (18) """
    AveragePagesPerMinute: PrintQueueIndexedProperty = ...
    Comment: PrintQueueIndexedProperty = ...
    DefaultPrintTicket: PrintQueueIndexedProperty = ...
    DefaultPriority: PrintQueueIndexedProperty = ...
    Description: PrintQueueIndexedProperty = ...
    HostingPrintServer: PrintQueueIndexedProperty = ...
    Location: PrintQueueIndexedProperty = ...
    Name: PrintQueueIndexedProperty = ...
    NumberOfJobs: PrintQueueIndexedProperty = ...
    Priority: PrintQueueIndexedProperty = ...
    QueueAttributes: PrintQueueIndexedProperty = ...
    QueueDriver: PrintQueueIndexedProperty = ...
    QueuePort: PrintQueueIndexedProperty = ...
    QueuePrintProcessor: PrintQueueIndexedProperty = ...
    QueueStatus: PrintQueueIndexedProperty = ...
    SeparatorFile: PrintQueueIndexedProperty = ...
    ShareName: PrintQueueIndexedProperty = ...
    StartTimeOfDay: PrintQueueIndexedProperty = ...
    UntilTimeOfDay: PrintQueueIndexedProperty = ...
    UserPrintTicket: PrintQueueIndexedProperty = ...
    value__ = ...


class PrintQueueStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PrintQueueStatus, values: Busy (512), DoorOpen (4194304), Error (2), Initializing (32768), IOActive (256), ManualFeed (32), None (0), NotAvailable (4096), NoToner (262144), Offline (128), OutOfMemory (2097152), OutputBinFull (2048), PagePunt (524288), PaperJam (8), PaperOut (16), PaperProblem (64), Paused (1), PendingDeletion (4), PowerSave (16777216), Printing (1024), Processing (16384), ServerUnknown (8388608), TonerLow (131072), UserIntervention (1048576), Waiting (8192), WarmingUp (65536) """
    Busy: PrintQueueStatus = ...
    DoorOpen: PrintQueueStatus = ...
    Error: PrintQueueStatus = ...
    Initializing: PrintQueueStatus = ...
    IOActive: PrintQueueStatus = ...
    ManualFeed: PrintQueueStatus = ...
    NotAvailable: PrintQueueStatus = ...
    NoToner: PrintQueueStatus = ...
    Offline: PrintQueueStatus = ...
    OutOfMemory: PrintQueueStatus = ...
    OutputBinFull: PrintQueueStatus = ...
    PagePunt: PrintQueueStatus = ...
    PaperJam: PrintQueueStatus = ...
    PaperOut: PrintQueueStatus = ...
    PaperProblem: PrintQueueStatus = ...
    Paused: PrintQueueStatus = ...
    PendingDeletion: PrintQueueStatus = ...
    PowerSave: PrintQueueStatus = ...
    Printing: PrintQueueStatus = ...
    Processing: PrintQueueStatus = ...
    ServerUnknown: PrintQueueStatus = ...
    TonerLow: PrintQueueStatus = ...
    UserIntervention: PrintQueueStatus = ...
    value__ = ...
    Waiting: PrintQueueStatus = ...
    WarmingUp: PrintQueueStatus = ...


class PrintQueueStream(Stream): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    PrintQueueStream(printQueue: PrintQueue, printJobName: str)
    PrintQueueStream(printQueue: PrintQueue, printJobName: str, commitDataOnClose: bool)
    PrintQueueStream(printQueue: PrintQueue, printJobName: str, commitDataOnClose: bool, printTicket: PrintTicket)
    """
    @property
    def JobIdentifier(self) -> int:
        """ Get: JobIdentifier(self: PrintQueueStream) -> int """
        ...


    def HandlePackagingProgressEvent(self, sender:object, e): # ->  # Not found arg types: {'e': 'PackagingProgressEventArgs'}
        """ HandlePackagingProgressEvent(self: PrintQueueStream, sender: object, e: PackagingProgressEventArgs) """
        ...

    def __new__(cls, printQueue:PrintQueue, printJobName:str, commitDataOnClose:bool = ..., printTicket = ...) -> Self: # Not found arg types: {'printTicket': 'PrintTicket'}
        """
        __new__(cls: type, printQueue: PrintQueue, printJobName: str)
        __new__(cls: type, printQueue: PrintQueue, printJobName: str, commitDataOnClose: bool)
        __new__(cls: type, printQueue: PrintQueue, printJobName: str, commitDataOnClose: bool, printTicket: PrintTicket)
        """
        ...


class PrintQueueStringProperty: # skipped bases: <type 'object'>, <type 'object'>
    """ PrintQueueStringProperty() """
    @property
    def Name(self) -> str:
        """
        Get: Name(self: PrintQueueStringProperty) -> str
        Set: Name(self: PrintQueueStringProperty) = value
        """
        ...

    @property
    def Type(self) -> PrintQueueStringPropertyType:
        """
        Get: Type(self: PrintQueueStringProperty) -> PrintQueueStringPropertyType
        Set: Type(self: PrintQueueStringProperty) = value
        """
        ...



class PrintQueueStringPropertyType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PrintQueueStringPropertyType, values: Comment (1), Location (0), ShareName (2) """
    Comment: PrintQueueStringPropertyType = ...
    Location: PrintQueueStringPropertyType = ...
    ShareName: PrintQueueStringPropertyType = ...
    value__ = ...


class PrintServerEventLoggingTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) PrintServerEventLoggingTypes, values: LogAllPrintingEvents (5), LogPrintingErrorEvents (2), LogPrintingInformationEvents (4), LogPrintingSuccessEvents (1), LogPrintingWarningEvents (3), None (0) """
    LogAllPrintingEvents: PrintServerEventLoggingTypes = ...
    LogPrintingErrorEvents: PrintServerEventLoggingTypes = ...
    LogPrintingInformationEvents: PrintServerEventLoggingTypes = ...
    LogPrintingSuccessEvents: PrintServerEventLoggingTypes = ...
    LogPrintingWarningEvents: PrintServerEventLoggingTypes = ...
    value__ = ...


class PrintServerIndexedProperty(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PrintServerIndexedProperty, values: BeepEnabled (5), DefaultPortThreadPriority (2), DefaultSchedulerPriority (4), DefaultSpoolDirectory (0), EventLog (7), MajorVersion (8), MinorVersion (9), NetPopup (6), PortThreadPriority (1), RestartJobOnPoolEnabled (11), RestartJobOnPoolTimeout (10), SchedulerPriority (3) """
    BeepEnabled: PrintServerIndexedProperty = ...
    DefaultPortThreadPriority: PrintServerIndexedProperty = ...
    DefaultSchedulerPriority: PrintServerIndexedProperty = ...
    DefaultSpoolDirectory: PrintServerIndexedProperty = ...
    EventLog: PrintServerIndexedProperty = ...
    MajorVersion: PrintServerIndexedProperty = ...
    MinorVersion: PrintServerIndexedProperty = ...
    NetPopup: PrintServerIndexedProperty = ...
    PortThreadPriority: PrintServerIndexedProperty = ...
    RestartJobOnPoolEnabled: PrintServerIndexedProperty = ...
    RestartJobOnPoolTimeout: PrintServerIndexedProperty = ...
    SchedulerPriority: PrintServerIndexedProperty = ...
    value__ = ...


class PrintSystemDesiredAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PrintSystemDesiredAccess, values: AdministratePrinter (983052), AdministrateServer (983041), EnumerateServer (131074), None (0), UsePrinter (131080) """
    AdministratePrinter: PrintSystemDesiredAccess = ...
    AdministrateServer: PrintSystemDesiredAccess = ...
    EnumerateServer: PrintSystemDesiredAccess = ...
    UsePrinter: PrintSystemDesiredAccess = ...
    value__ = ...


class PrintSystemJobInfo(PrintSystemObject): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def HostingPrintQueue(self) -> PrintQueue:
        """ Get: HostingPrintQueue(self: PrintSystemJobInfo) -> PrintQueue """
        ...

    @property
    def HostingPrintServer(self) -> PrintServer:
        """ Get: HostingPrintServer(self: PrintSystemJobInfo) -> PrintServer """
        ...

    @property
    def IsBlocked(self) -> bool:
        """ Get: IsBlocked(self: PrintSystemJobInfo) -> bool """
        ...

    @property
    def IsCompleted(self) -> bool:
        """ Get: IsCompleted(self: PrintSystemJobInfo) -> bool """
        ...

    @property
    def IsDeleted(self) -> bool:
        """ Get: IsDeleted(self: PrintSystemJobInfo) -> bool """
        ...

    @property
    def IsDeleting(self) -> bool:
        """ Get: IsDeleting(self: PrintSystemJobInfo) -> bool """
        ...

    @property
    def IsInError(self) -> bool:
        """ Get: IsInError(self: PrintSystemJobInfo) -> bool """
        ...

    @property
    def IsOffline(self) -> bool:
        """ Get: IsOffline(self: PrintSystemJobInfo) -> bool """
        ...

    @property
    def IsPaperOut(self) -> bool:
        """ Get: IsPaperOut(self: PrintSystemJobInfo) -> bool """
        ...

    @property
    def IsPaused(self) -> bool:
        """ Get: IsPaused(self: PrintSystemJobInfo) -> bool """
        ...

    @property
    def IsPrinted(self) -> bool:
        """ Get: IsPrinted(self: PrintSystemJobInfo) -> bool """
        ...

    @property
    def IsPrinting(self) -> bool:
        """ Get: IsPrinting(self: PrintSystemJobInfo) -> bool """
        ...

    @property
    def IsRestarted(self) -> bool:
        """ Get: IsRestarted(self: PrintSystemJobInfo) -> bool """
        ...

    @property
    def IsRetained(self) -> bool:
        """ Get: IsRetained(self: PrintSystemJobInfo) -> bool """
        ...

    @property
    def IsSpooling(self) -> bool:
        """ Get: IsSpooling(self: PrintSystemJobInfo) -> bool """
        ...

    @property
    def IsUserInterventionRequired(self) -> bool:
        """ Get: IsUserInterventionRequired(self: PrintSystemJobInfo) -> bool """
        ...

    @property
    def JobIdentifier(self) -> int:
        """ Get: JobIdentifier(self: PrintSystemJobInfo) -> int """
        ...

    @property
    def JobName(self) -> str:
        """
        Get: JobName(self: PrintSystemJobInfo) -> str
        Set: JobName(self: PrintSystemJobInfo) = value
        """
        ...

    @property
    def JobSize(self) -> int:
        """ Get: JobSize(self: PrintSystemJobInfo) -> int """
        ...

    @property
    def JobStatus(self) -> PrintJobStatus:
        """ Get: JobStatus(self: PrintSystemJobInfo) -> PrintJobStatus """
        ...

    @property
    def JobStream(self) -> Stream:
        """ Get: JobStream(self: PrintSystemJobInfo) -> Stream """
        ...

    @property
    def NumberOfPages(self) -> int:
        """ Get: NumberOfPages(self: PrintSystemJobInfo) -> int """
        ...

    @property
    def NumberOfPagesPrinted(self) -> int:
        """ Get: NumberOfPagesPrinted(self: PrintSystemJobInfo) -> int """
        ...

    @property
    def PositionInPrintQueue(self) -> int:
        """ Get: PositionInPrintQueue(self: PrintSystemJobInfo) -> int """
        ...

    @property
    def Priority(self) -> PrintJobPriority:
        """ Get: Priority(self: PrintSystemJobInfo) -> PrintJobPriority """
        ...

    @property
    def StartTimeOfDay(self) -> int:
        """ Get: StartTimeOfDay(self: PrintSystemJobInfo) -> int """
        ...

    @property
    def Submitter(self) -> str:
        """ Get: Submitter(self: PrintSystemJobInfo) -> str """
        ...

    @property
    def TimeJobSubmitted(self) -> DateTime:
        """ Get: TimeJobSubmitted(self: PrintSystemJobInfo) -> DateTime """
        ...

    @property
    def TimeSinceStartedPrinting(self) -> int:
        """ Get: TimeSinceStartedPrinting(self: PrintSystemJobInfo) -> int """
        ...

    @property
    def UntilTimeOfDay(self) -> int:
        """ Get: UntilTimeOfDay(self: PrintSystemJobInfo) -> int """
        ...


    def Cancel(self): # -> 
        """ Cancel(self: PrintSystemJobInfo) """
        ...

    @staticmethod
    def Get(printQueue:PrintQueue, jobIdentifier:int) -> PrintSystemJobInfo:
        """ Get(printQueue: PrintQueue, jobIdentifier: int) -> PrintSystemJobInfo """
        ...

    def Pause(self): # -> 
        """ Pause(self: PrintSystemJobInfo) """
        ...

    def Restart(self): # -> 
        """ Restart(self: PrintSystemJobInfo) """
        ...

    def Resume(self): # -> 
        """ Resume(self: PrintSystemJobInfo) """
        ...


class PrintSystemObjectLoadMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum PrintSystemObjectLoadMode, values: LoadInitialized (2), LoadUninitialized (1), None (0) """
    LoadInitialized: PrintSystemObjectLoadMode = ...
    LoadUninitialized: PrintSystemObjectLoadMode = ...
    value__ = ...


class PrintSystemObjectPropertiesChangedEventArgs(IDisposable, EventArgs): # skipped bases: <type 'object'>
    """ PrintSystemObjectPropertiesChangedEventArgs(events: StringCollection) """
    @property
    def PropertiesNames(self) -> StringCollection:
        """ Get: PropertiesNames(self: PrintSystemObjectPropertiesChangedEventArgs) -> StringCollection """
        ...


    def __new__(cls, events:StringCollection) -> Self:
        """ __new__(cls: type, events: StringCollection) """
        ...


class PrintSystemObjectPropertyChangedEventArgs(IDisposable, EventArgs): # skipped bases: <type 'object'>
    """ PrintSystemObjectPropertyChangedEventArgs(eventName: str) """
    @property
    def PropertyName(self) -> str:
        """ Get: PropertyName(self: PrintSystemObjectPropertyChangedEventArgs) -> str """
        ...


    def __new__(cls, eventName:str) -> Self:
        """ __new__(cls: type, eventName: str) """
        ...


# variables with complex values

