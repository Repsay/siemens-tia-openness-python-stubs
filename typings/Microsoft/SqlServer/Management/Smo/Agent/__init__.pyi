# encoding: utf-8
# module Microsoft.SqlServer.Management.Smo.Agent calls itself Agent
# from Microsoft.SqlServer.SqlEnum, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91, Microsoft.SqlServer.Smo, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Common import (IAlterable, ICreatable, 
    IDropIfExists, IDroppable, IRenamable)

from Microsoft.SqlServer.Management.Smo import (ArrayListCollectionBase, 
    IScriptable, JobScheduleCollectionBase, NamedSmoObject, 
    ParameterCollectionBase, ScriptingOptions, Server, 
    SimpleObjectCollectionBase, SqlSmoObject)

from System import Array, Byte, DateTime, Enum, Guid, TimeSpan

from System.Collections.Specialized import StringCollection

from System.Data import DataTable

from System.Management.Automation import Job

from System.ServiceProcess import ServiceStartMode

from typing import Self

"""The following names are not found in the module: (JobHistoryFilter, 
    JobScheduleCollection, JobServer, JobStepCollection, 
    OperatorCategoryCollection, OperatorCollection, ProxyAccountCollection, 
    TargetServerCollection, TargetServerGroupCollection, field#)
"""

# no functions
# classes

class ActivationOrder(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ActivationOrder, values: First (0), Last (2), None (1) """
    First: ActivationOrder = ...
    Last: ActivationOrder = ...
    value__ = ...


class AgentLogLevels(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) AgentLogLevels, values: All (7), Errors (1), Informational (4), Warnings (2) """
    All: AgentLogLevels = ...
    Errors: AgentLogLevels = ...
    Informational: AgentLogLevels = ...
    value__ = ...
    Warnings: AgentLogLevels = ...


class AgentMailType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AgentMailType, values: DatabaseMail (1), SqlAgentMail (0) """
    DatabaseMail: AgentMailType = ...
    SqlAgentMail: AgentMailType = ...
    value__ = ...


class AgentObjectBase(NamedSmoObject): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """ no doc """
    m_ExtendedProperties = ...
    singletonParent = ...


class AgentSubSystem(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AgentSubSystem, values: ActiveScripting (2), AnalysisCommand (10), AnalysisQuery (9), CmdExec (3), Distribution (6), LogReader (5), Merge (7), PowerShell (12), QueueReader (8), Snapshot (4), Ssis (11), TransactSql (1) """
    ActiveScripting: AgentSubSystem = ...
    AnalysisCommand: AgentSubSystem = ...
    AnalysisQuery: AgentSubSystem = ...
    CmdExec: AgentSubSystem = ...
    Distribution: AgentSubSystem = ...
    LogReader: AgentSubSystem = ...
    Merge: AgentSubSystem = ...
    PowerShell: AgentSubSystem = ...
    QueueReader: AgentSubSystem = ...
    Snapshot: AgentSubSystem = ...
    Ssis: AgentSubSystem = ...
    TransactSql: AgentSubSystem = ...
    value__ = ...


class Alert(IDroppable, IAlterable, ICreatable, IScriptable, IRenamable, AgentObjectBase, IDropIfExists): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    Alert()
    Alert(jobServer: JobServer, name: str)
    """
    @property
    def AlertType(self) -> AlertType:
        """ Get: AlertType(self: Alert) -> AlertType """
        ...

    @property
    def CategoryName(self) -> str:
        """
        Get: CategoryName(self: Alert) -> str
        Set: CategoryName(self: Alert) = value
        """
        ...

    @property
    def CountResetDate(self) -> DateTime:
        """ Get: CountResetDate(self: Alert) -> DateTime """
        ...

    @property
    def DatabaseName(self) -> str:
        """
        Get: DatabaseName(self: Alert) -> str
        Set: DatabaseName(self: Alert) = value
        """
        ...

    @property
    def DelayBetweenResponses(self) -> int:
        """
        Get: DelayBetweenResponses(self: Alert) -> int
        Set: DelayBetweenResponses(self: Alert) = value
        """
        ...

    @property
    def EventDescriptionKeyword(self) -> str:
        """
        Get: EventDescriptionKeyword(self: Alert) -> str
        Set: EventDescriptionKeyword(self: Alert) = value
        """
        ...

    @property
    def EventSource(self) -> str:
        """ Get: EventSource(self: Alert) -> str """
        ...

    @property
    def HasNotification(self) -> int:
        """ Get: HasNotification(self: Alert) -> int """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: Alert) -> int """
        ...

    @property
    def IncludeEventDescription(self) -> NotifyMethods:
        """
        Get: IncludeEventDescription(self: Alert) -> NotifyMethods
        Set: IncludeEventDescription(self: Alert) = value
        """
        ...

    @property
    def IsEnabled(self) -> bool:
        """
        Get: IsEnabled(self: Alert) -> bool
        Set: IsEnabled(self: Alert) = value
        """
        ...

    @property
    def JobID(self) -> Guid:
        """
        Get: JobID(self: Alert) -> Guid
        Set: JobID(self: Alert) = value
        """
        ...

    @property
    def JobName(self) -> str:
        """ Get: JobName(self: Alert) -> str """
        ...

    @property
    def LastOccurrenceDate(self) -> DateTime:
        """
        Get: LastOccurrenceDate(self: Alert) -> DateTime
        Set: LastOccurrenceDate(self: Alert) = value
        """
        ...

    @property
    def LastResponseDate(self) -> DateTime:
        """
        Get: LastResponseDate(self: Alert) -> DateTime
        Set: LastResponseDate(self: Alert) = value
        """
        ...

    @property
    def MessageID(self) -> int:
        """
        Get: MessageID(self: Alert) -> int
        Set: MessageID(self: Alert) = value
        """
        ...

    @property
    def NotificationMessage(self) -> str:
        """
        Get: NotificationMessage(self: Alert) -> str
        Set: NotificationMessage(self: Alert) = value
        """
        ...

    @property
    def OccurrenceCount(self) -> int:
        """ Get: OccurrenceCount(self: Alert) -> int """
        ...

    @property
    def Parent(self): # -> JobServer
        """
        Get: Parent(self: Alert) -> JobServer
        Set: Parent(self: Alert) = value
        """
        ...

    @property
    def PerformanceCondition(self) -> str:
        """
        Get: PerformanceCondition(self: Alert) -> str
        Set: PerformanceCondition(self: Alert) = value
        """
        ...

    @property
    def Severity(self) -> int:
        """
        Get: Severity(self: Alert) -> int
        Set: Severity(self: Alert) = value
        """
        ...

    @property
    def WmiEventNamespace(self) -> str:
        """
        Get: WmiEventNamespace(self: Alert) -> str
        Set: WmiEventNamespace(self: Alert) = value
        """
        ...

    @property
    def WmiEventQuery(self) -> str:
        """
        Get: WmiEventQuery(self: Alert) -> str
        Set: WmiEventQuery(self: Alert) = value
        """
        ...


    def AddNotification(self, operatorName:str, notifymethod:NotifyMethods): # -> 
        """ AddNotification(self: Alert, operatorName: str, notifymethod: NotifyMethods) """
        ...

    def EnumNotifications(self, *__args:NotifyMethods) -> DataTable:
        """
        EnumNotifications(self: Alert) -> DataTable
        EnumNotifications(self: Alert, notifyMethod: NotifyMethods) -> DataTable
        EnumNotifications(self: Alert, operatorName: str) -> DataTable
        EnumNotifications(self: Alert, notifyMethod: NotifyMethods, operatorName: str) -> DataTable
        """
        ...

    def RemoveNotification(self, operatorName:str): # -> 
        """ RemoveNotification(self: Alert, operatorName: str) """
        ...

    def ResetOccurrenceCount(self): # -> 
        """ ResetOccurrenceCount(self: Alert) """
        ...

    def UpdateNotification(self, operatorName:str, notifymethod:NotifyMethods): # -> 
        """ UpdateNotification(self: Alert, operatorName: str, notifymethod: NotifyMethods) """
        ...

    def __new__(cls, jobServer = ..., name:str = ...) -> Self: # Not found arg types: {'jobServer': 'JobServer'}
        """
        __new__(cls: type)
        __new__(cls: type, jobServer: JobServer, name: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class CategoryBase(IDroppable, ICreatable, IScriptable, IRenamable, AgentObjectBase, IDropIfExists): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """ no doc """
    def GetCatTypeName(self, *args): #cannot find CLR method
        """ GetCatTypeName(self: CategoryBase, ct: CategoryType) -> str """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class AlertCategory(CategoryBase): # skipped bases: <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'IScriptable'>, <type 'ISqlSmoObjectInitialize'>, <type 'IDroppable'>, <type 'ICreatable'>, <type 'IAlienObject'>, <type 'IDropIfExists'>, <type 'IRenamable'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'object'>
    """
    AlertCategory()
    AlertCategory(jobServer: JobServer, name: str)
    """
    @property
    def ID(self) -> int:
        """ Get: ID(self: AlertCategory) -> int """
        ...

    @property
    def Parent(self): # -> JobServer
        """
        Get: Parent(self: AlertCategory) -> JobServer
        Set: Parent(self: AlertCategory) = value
        """
        ...


    def __new__(cls, jobServer = ..., name:str = ...) -> Self: # Not found arg types: {'jobServer': 'JobServer'}
        """
        __new__(cls: type)
        __new__(cls: type, jobServer: JobServer, name: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class AlertCategoryCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self): # -> JobServer
        """ Get: Parent(self: AlertCategoryCollection) -> JobServer """
        ...


    def Add(self, alertCategory:AlertCategory): # -> 
        """ Add(self: AlertCategoryCollection, alertCategory: AlertCategory) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: AlertCategoryCollection, array: Array[AlertCategory], index: int) """
        ...

    def ItemById(self, id:int) -> AlertCategory:
        """ ItemById(self: AlertCategoryCollection, id: int) -> AlertCategory """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: AlertCategoryCollection, name: str)Remove(self: AlertCategoryCollection, alertCategory: AlertCategory) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class AlertCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self): # -> JobServer
        """ Get: Parent(self: AlertCollection) -> JobServer """
        ...


    def Add(self, alert:Alert): # -> 
        """ Add(self: AlertCollection, alert: Alert) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: AlertCollection, array: Array[Alert], index: int) """
        ...

    def ItemById(self, id:int) -> Alert:
        """ ItemById(self: AlertCollection, id: int) -> Alert """
        ...

    def Script(self, scriptingOptions:ScriptingOptions = ...) -> StringCollection:
        """
        Script(self: AlertCollection) -> StringCollection
        Script(self: AlertCollection, scriptingOptions: ScriptingOptions) -> StringCollection
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class AlertSystem(AgentObjectBase, IAlterable, IScriptable): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """ no doc """
    @property
    def FailSafeEmailAddress(self) -> str:
        """
        Get: FailSafeEmailAddress(self: AlertSystem) -> str
        Set: FailSafeEmailAddress(self: AlertSystem) = value
        """
        ...

    @property
    def FailSafeNetSendAddress(self) -> str:
        """
        Get: FailSafeNetSendAddress(self: AlertSystem) -> str
        Set: FailSafeNetSendAddress(self: AlertSystem) = value
        """
        ...

    @property
    def FailSafeOperator(self) -> str:
        """
        Get: FailSafeOperator(self: AlertSystem) -> str
        Set: FailSafeOperator(self: AlertSystem) = value
        """
        ...

    @property
    def FailSafePagerAddress(self) -> str:
        """
        Get: FailSafePagerAddress(self: AlertSystem) -> str
        Set: FailSafePagerAddress(self: AlertSystem) = value
        """
        ...

    @property
    def ForwardingServer(self) -> str:
        """
        Get: ForwardingServer(self: AlertSystem) -> str
        Set: ForwardingServer(self: AlertSystem) = value
        """
        ...

    @property
    def ForwardingSeverity(self) -> int:
        """
        Get: ForwardingSeverity(self: AlertSystem) -> int
        Set: ForwardingSeverity(self: AlertSystem) = value
        """
        ...

    @property
    def IsForwardedAlways(self) -> bool:
        """
        Get: IsForwardedAlways(self: AlertSystem) -> bool
        Set: IsForwardedAlways(self: AlertSystem) = value
        """
        ...

    @property
    def NotificationMethod(self) -> NotifyMethods:
        """
        Get: NotificationMethod(self: AlertSystem) -> NotifyMethods
        Set: NotificationMethod(self: AlertSystem) = value
        """
        ...

    @property
    def PagerCCTemplate(self) -> str:
        """
        Get: PagerCCTemplate(self: AlertSystem) -> str
        Set: PagerCCTemplate(self: AlertSystem) = value
        """
        ...

    @property
    def PagerSendSubjectOnly(self) -> bool:
        """
        Get: PagerSendSubjectOnly(self: AlertSystem) -> bool
        Set: PagerSendSubjectOnly(self: AlertSystem) = value
        """
        ...

    @property
    def PagerSubjectTemplate(self) -> str:
        """
        Get: PagerSubjectTemplate(self: AlertSystem) -> str
        Set: PagerSubjectTemplate(self: AlertSystem) = value
        """
        ...

    @property
    def PagerToTemplate(self) -> str:
        """
        Get: PagerToTemplate(self: AlertSystem) -> str
        Set: PagerToTemplate(self: AlertSystem) = value
        """
        ...

    @property
    def Parent(self): # -> JobServer
        """ Get: Parent(self: AlertSystem) -> JobServer """
        ...


    m_ExtendedProperties = ...
    singletonParent = ...


class AlertType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AlertType, values: NonSqlServerEvent (3), SqlServerEvent (1), SqlServerPerformanceCondition (2), WmiEvent (4) """
    NonSqlServerEvent: AlertType = ...
    SqlServerEvent: AlertType = ...
    SqlServerPerformanceCondition: AlertType = ...
    value__ = ...
    WmiEvent: AlertType = ...


class CategoryType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CategoryType, values: LocalJob (1), MultiServerJob (2), None (3) """
    LocalJob: CategoryType = ...
    MultiServerJob: CategoryType = ...
    value__ = ...


class CompletionAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CompletionAction, values: Always (3), Never (0), OnFailure (2), OnSuccess (1) """
    Always: CompletionAction = ...
    Never: CompletionAction = ...
    OnFailure: CompletionAction = ...
    OnSuccess: CompletionAction = ...
    value__ = ...


class CompletionResult(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum CompletionResult, values: Cancelled (3), Failed (0), InProgress (4), Retry (2), Succeeded (1), Unknown (5) """
    Cancelled: CompletionResult = ...
    Failed: CompletionResult = ...
    InProgress: CompletionResult = ...
    Retry: CompletionResult = ...
    Succeeded: CompletionResult = ...
    Unknown: CompletionResult = ...
    value__ = ...


class FindOperand(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FindOperand, values: EqualTo (1), GreaterThan (2), LessThan (3) """
    EqualTo: FindOperand = ...
    GreaterThan: FindOperand = ...
    LessThan: FindOperand = ...
    value__ = ...


class FrequencyRelativeIntervals(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) FrequencyRelativeIntervals, values: First (1), Fourth (8), Last (16), Second (2), Third (4) """
    First: FrequencyRelativeIntervals = ...
    Fourth: FrequencyRelativeIntervals = ...
    Last: FrequencyRelativeIntervals = ...
    Second: FrequencyRelativeIntervals = ...
    Third: FrequencyRelativeIntervals = ...
    value__ = ...


class FrequencySubDayTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) FrequencySubDayTypes, values: Hour (8), Minute (4), Once (1), Second (2), Unknown (0) """
    Hour: FrequencySubDayTypes = ...
    Minute: FrequencySubDayTypes = ...
    Once: FrequencySubDayTypes = ...
    Second: FrequencySubDayTypes = ...
    Unknown: FrequencySubDayTypes = ...
    value__ = ...


class FrequencyTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) FrequencyTypes, values: AutoStart (64), Daily (4), Monthly (16), MonthlyRelative (32), OneTime (1), OnIdle (128), Unknown (0), Weekly (8) """
    AutoStart: FrequencyTypes = ...
    Daily: FrequencyTypes = ...
    Monthly: FrequencyTypes = ...
    MonthlyRelative: FrequencyTypes = ...
    OneTime: FrequencyTypes = ...
    OnIdle: FrequencyTypes = ...
    Unknown: FrequencyTypes = ...
    value__ = ...
    Weekly: FrequencyTypes = ...


class Job(IDroppable, IAlterable, ICreatable, IScriptable, IRenamable, AgentObjectBase, IDropIfExists): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    Job()
    Job(jobServer: JobServer, name: str)
    Job(jobServer: JobServer, name: str, categoryID: int)
    """
    @property
    def Category(self) -> str:
        """
        Get: Category(self: Job) -> str
        Set: Category(self: Job) = value
        """
        ...

    @property
    def CategoryID(self) -> int:
        """ Get: CategoryID(self: Job) -> int """
        ...

    @property
    def CategoryType(self) -> Byte:
        """
        Get: CategoryType(self: Job) -> Byte
        Set: CategoryType(self: Job) = value
        """
        ...

    @property
    def CurrentRunRetryAttempt(self) -> int:
        """ Get: CurrentRunRetryAttempt(self: Job) -> int """
        ...

    @property
    def CurrentRunStatus(self) -> JobExecutionStatus:
        """ Get: CurrentRunStatus(self: Job) -> JobExecutionStatus """
        ...

    @property
    def CurrentRunStep(self) -> str:
        """ Get: CurrentRunStep(self: Job) -> str """
        ...

    @property
    def DateCreated(self) -> DateTime:
        """ Get: DateCreated(self: Job) -> DateTime """
        ...

    @property
    def DateLastModified(self) -> DateTime:
        """ Get: DateLastModified(self: Job) -> DateTime """
        ...

    @property
    def DeleteLevel(self) -> CompletionAction:
        """
        Get: DeleteLevel(self: Job) -> CompletionAction
        Set: DeleteLevel(self: Job) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: Job) -> str
        Set: Description(self: Job) = value
        """
        ...

    @property
    def EmailLevel(self) -> CompletionAction:
        """
        Get: EmailLevel(self: Job) -> CompletionAction
        Set: EmailLevel(self: Job) = value
        """
        ...

    @property
    def EventLogLevel(self) -> CompletionAction:
        """
        Get: EventLogLevel(self: Job) -> CompletionAction
        Set: EventLogLevel(self: Job) = value
        """
        ...

    @property
    def HasSchedule(self) -> bool:
        """ Get: HasSchedule(self: Job) -> bool """
        ...

    @property
    def HasServer(self) -> bool:
        """ Get: HasServer(self: Job) -> bool """
        ...

    @property
    def HasStep(self) -> bool:
        """ Get: HasStep(self: Job) -> bool """
        ...

    @property
    def IsEnabled(self) -> bool:
        """
        Get: IsEnabled(self: Job) -> bool
        Set: IsEnabled(self: Job) = value
        """
        ...

    @property
    def JobID(self) -> Guid:
        """ Get: JobID(self: Job) -> Guid """
        ...

    @property
    def JobSchedules(self): # -> JobScheduleCollection
        """ Get: JobSchedules(self: Job) -> JobScheduleCollection """
        ...

    @property
    def JobSteps(self): # -> JobStepCollection
        """ Get: JobSteps(self: Job) -> JobStepCollection """
        ...

    @property
    def JobType(self) -> JobType:
        """ Get: JobType(self: Job) -> JobType """
        ...

    @property
    def LastRunDate(self) -> DateTime:
        """ Get: LastRunDate(self: Job) -> DateTime """
        ...

    @property
    def LastRunOutcome(self) -> CompletionResult:
        """ Get: LastRunOutcome(self: Job) -> CompletionResult """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Job) -> str
        Set: Name(self: Job) = value
        """
        ...

    @property
    def NetSendLevel(self) -> CompletionAction:
        """
        Get: NetSendLevel(self: Job) -> CompletionAction
        Set: NetSendLevel(self: Job) = value
        """
        ...

    @property
    def NextRunDate(self) -> DateTime:
        """ Get: NextRunDate(self: Job) -> DateTime """
        ...

    @property
    def NextRunScheduleID(self) -> int:
        """ Get: NextRunScheduleID(self: Job) -> int """
        ...

    @property
    def OperatorToEmail(self) -> str:
        """
        Get: OperatorToEmail(self: Job) -> str
        Set: OperatorToEmail(self: Job) = value
        """
        ...

    @property
    def OperatorToNetSend(self) -> str:
        """
        Get: OperatorToNetSend(self: Job) -> str
        Set: OperatorToNetSend(self: Job) = value
        """
        ...

    @property
    def OperatorToPage(self) -> str:
        """
        Get: OperatorToPage(self: Job) -> str
        Set: OperatorToPage(self: Job) = value
        """
        ...

    @property
    def OriginatingServer(self) -> str:
        """ Get: OriginatingServer(self: Job) -> str """
        ...

    @property
    def OwnerLoginName(self) -> str:
        """
        Get: OwnerLoginName(self: Job) -> str
        Set: OwnerLoginName(self: Job) = value
        """
        ...

    @property
    def PageLevel(self) -> CompletionAction:
        """
        Get: PageLevel(self: Job) -> CompletionAction
        Set: PageLevel(self: Job) = value
        """
        ...

    @property
    def Parent(self): # -> JobServer
        """
        Get: Parent(self: Job) -> JobServer
        Set: Parent(self: Job) = value
        """
        ...

    @property
    def StartStepID(self) -> int:
        """
        Get: StartStepID(self: Job) -> int
        Set: StartStepID(self: Job) = value
        """
        ...

    @property
    def VersionNumber(self) -> int:
        """ Get: VersionNumber(self: Job) -> int """
        ...


    def AddSharedSchedule(self, scheduleId:int): # -> 
        """ AddSharedSchedule(self: Job, scheduleId: int) """
        ...

    def ApplyToTargetServer(self, serverName:str): # -> 
        """ ApplyToTargetServer(self: Job, serverName: str) """
        ...

    def ApplyToTargetServerGroup(self, groupName:str): # -> 
        """ ApplyToTargetServerGroup(self: Job, groupName: str) """
        ...

    def DeleteJobStepLogs(self, *__args:DateTime): # -> 
        """ DeleteJobStepLogs(self: Job, olderThan: DateTime)DeleteJobStepLogs(self: Job, largerThan: int) """
        ...

    def EnumAlerts(self) -> DataTable:
        """ EnumAlerts(self: Job) -> DataTable """
        ...

    def EnumHistory(self, filter = ...) -> DataTable: # Not found arg types: {'filter': 'JobHistoryFilter'}
        """
        EnumHistory(self: Job, filter: JobHistoryFilter) -> DataTable
        EnumHistory(self: Job) -> DataTable
        """
        ...

    def EnumJobStepLogs(self, *__args:int) -> DataTable:
        """
        EnumJobStepLogs(self: Job) -> DataTable
        EnumJobStepLogs(self: Job, stepId: int) -> DataTable
        EnumJobStepLogs(self: Job, stepName: str) -> DataTable
        """
        ...

    def EnumJobStepsByID(self) -> Array:
        """ EnumJobStepsByID(self: Job) -> Array[JobStep] """
        ...

    def EnumTargetServers(self) -> DataTable:
        """ EnumTargetServers(self: Job) -> DataTable """
        ...

    def Invoke(self): # -> 
        """ Invoke(self: Job) """
        ...

    def PurgeHistory(self): # -> 
        """ PurgeHistory(self: Job) """
        ...

    def RemoveAllJobSchedules(self, keepUnusedSchedules:bool = ...): # -> 
        """ RemoveAllJobSchedules(self: Job)RemoveAllJobSchedules(self: Job, keepUnusedSchedules: bool) """
        ...

    def RemoveAllJobSteps(self): # -> 
        """ RemoveAllJobSteps(self: Job) """
        ...

    def RemoveFromTargetServer(self, serverName:str): # -> 
        """ RemoveFromTargetServer(self: Job, serverName: str) """
        ...

    def RemoveFromTargetServerGroup(self, groupName:str): # -> 
        """ RemoveFromTargetServerGroup(self: Job, groupName: str) """
        ...

    def RemoveSharedSchedule(self, scheduleId:int, keepUnusedSchedules:bool = ...): # -> 
        """ RemoveSharedSchedule(self: Job, scheduleId: int)RemoveSharedSchedule(self: Job, scheduleId: int, keepUnusedSchedules: bool) """
        ...

    def Start(self, jobStepName:str = ...): # -> 
        """ Start(self: Job, jobStepName: str)Start(self: Job) """
        ...

    def Stop(self): # -> 
        """ Stop(self: Job) """
        ...

    def __new__(cls, jobServer = ..., name:str = ..., categoryID:int = ...) -> Self: # Not found arg types: {'jobServer': 'JobServer'}
        """
        __new__(cls: type)
        __new__(cls: type, jobServer: JobServer, name: str)
        __new__(cls: type, jobServer: JobServer, name: str, categoryID: int)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class JobCategory(CategoryBase): # skipped bases: <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'IScriptable'>, <type 'ISqlSmoObjectInitialize'>, <type 'IDroppable'>, <type 'ICreatable'>, <type 'IAlienObject'>, <type 'IDropIfExists'>, <type 'IRenamable'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'object'>
    """
    JobCategory()
    JobCategory(jobServer: JobServer, name: str)
    """
    @property
    def CategoryType(self) -> CategoryType:
        """
        Get: CategoryType(self: JobCategory) -> CategoryType
        Set: CategoryType(self: JobCategory) = value
        """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: JobCategory) -> int """
        ...

    @property
    def Parent(self): # -> JobServer
        """
        Get: Parent(self: JobCategory) -> JobServer
        Set: Parent(self: JobCategory) = value
        """
        ...


    def __new__(cls, jobServer = ..., name:str = ...) -> Self: # Not found arg types: {'jobServer': 'JobServer'}
        """
        __new__(cls: type)
        __new__(cls: type, jobServer: JobServer, name: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class JobCategoryCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self): # -> JobServer
        """ Get: Parent(self: JobCategoryCollection) -> JobServer """
        ...


    def Add(self, jobCategory:JobCategory): # -> 
        """ Add(self: JobCategoryCollection, jobCategory: JobCategory) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: JobCategoryCollection, array: Array[JobCategory], index: int) """
        ...

    def ItemById(self, id:int) -> JobCategory:
        """ ItemById(self: JobCategoryCollection, id: int) -> JobCategory """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: JobCategoryCollection, name: str)Remove(self: JobCategoryCollection, jobCategory: JobCategory) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class JobCollection(ArrayListCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self): # -> JobServer
        """ Get: Parent(self: JobCollection) -> JobServer """
        ...


    def Add(self, job:Job): # -> 
        """ Add(self: JobCollection, job: Job) """
        ...

    def Contains(self, name:str, categoryID:int = ...) -> bool:
        """
        Contains(self: JobCollection, name: str) -> bool
        Contains(self: JobCollection, name: str, categoryID: int) -> bool
        """
        ...

    def ItemById(self, id:Guid) -> Job:
        """ ItemById(self: JobCollection, id: Guid) -> Job """
        ...

    def Script(self, scriptingOptions:ScriptingOptions = ...) -> StringCollection:
        """
        Script(self: JobCollection) -> StringCollection
        Script(self: JobCollection, scriptingOptions: ScriptingOptions) -> StringCollection
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class JobExecutionStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum JobExecutionStatus, values: BetweenRetries (3), Executing (1), Idle (4), PerformingCompletionAction (7), Suspended (5), WaitingForStepToFinish (6), WaitingForWorkerThread (2) """
    BetweenRetries: JobExecutionStatus = ...
    Executing: JobExecutionStatus = ...
    Idle: JobExecutionStatus = ...
    PerformingCompletionAction: JobExecutionStatus = ...
    Suspended: JobExecutionStatus = ...
    value__ = ...
    WaitingForStepToFinish: JobExecutionStatus = ...
    WaitingForWorkerThread: JobExecutionStatus = ...


class JobFilter: # skipped bases: <type 'object'>, <type 'object'>
    """ JobFilter() """
    @property
    def Category(self) -> str:
        """
        Get: Category(self: JobFilter) -> str
        Set: Category(self: JobFilter) = value
        """
        ...

    @property
    def CurrentExecutionStatus(self) -> JobExecutionStatus:
        """
        Get: CurrentExecutionStatus(self: JobFilter) -> JobExecutionStatus
        Set: CurrentExecutionStatus(self: JobFilter) = value
        """
        ...

    @property
    def DateFindOperand(self) -> FindOperand:
        """
        Get: DateFindOperand(self: JobFilter) -> FindOperand
        Set: DateFindOperand(self: JobFilter) = value
        """
        ...

    @property
    def DateJobCreated(self) -> DateTime:
        """
        Get: DateJobCreated(self: JobFilter) -> DateTime
        Set: DateJobCreated(self: JobFilter) = value
        """
        ...

    @property
    def DateJobLastModified(self) -> DateTime:
        """
        Get: DateJobLastModified(self: JobFilter) -> DateTime
        Set: DateJobLastModified(self: JobFilter) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: JobFilter) -> bool
        Set: Enabled(self: JobFilter) = value
        """
        ...

    @property
    def JobType(self) -> JobType:
        """
        Get: JobType(self: JobFilter) -> JobType
        Set: JobType(self: JobFilter) = value
        """
        ...

    @property
    def Owner(self) -> str:
        """
        Get: Owner(self: JobFilter) -> str
        Set: Owner(self: JobFilter) = value
        """
        ...

    @property
    def StepSubsystem(self) -> AgentSubSystem:
        """
        Get: StepSubsystem(self: JobFilter) -> AgentSubSystem
        Set: StepSubsystem(self: JobFilter) = value
        """
        ...



class JobHistoryFilter: # skipped bases: <type 'object'>, <type 'object'>
    """ JobHistoryFilter() """
    @property
    def EndRunDate(self) -> DateTime:
        """
        Get: EndRunDate(self: JobHistoryFilter) -> DateTime
        Set: EndRunDate(self: JobHistoryFilter) = value
        """
        ...

    @property
    def JobID(self) -> Guid:
        """
        Get: JobID(self: JobHistoryFilter) -> Guid
        Set: JobID(self: JobHistoryFilter) = value
        """
        ...

    @property
    def JobName(self) -> str:
        """
        Get: JobName(self: JobHistoryFilter) -> str
        Set: JobName(self: JobHistoryFilter) = value
        """
        ...

    @property
    def MinimumRetries(self) -> int:
        """
        Get: MinimumRetries(self: JobHistoryFilter) -> int
        Set: MinimumRetries(self: JobHistoryFilter) = value
        """
        ...

    @property
    def MinimumRunDuration(self) -> int:
        """
        Get: MinimumRunDuration(self: JobHistoryFilter) -> int
        Set: MinimumRunDuration(self: JobHistoryFilter) = value
        """
        ...

    @property
    def OldestFirst(self) -> bool:
        """
        Get: OldestFirst(self: JobHistoryFilter) -> bool
        Set: OldestFirst(self: JobHistoryFilter) = value
        """
        ...

    @property
    def OutcomeTypes(self) -> CompletionResult:
        """
        Get: OutcomeTypes(self: JobHistoryFilter) -> CompletionResult
        Set: OutcomeTypes(self: JobHistoryFilter) = value
        """
        ...

    @property
    def SqlMessageID(self) -> int:
        """
        Get: SqlMessageID(self: JobHistoryFilter) -> int
        Set: SqlMessageID(self: JobHistoryFilter) = value
        """
        ...

    @property
    def SqlSeverity(self) -> int:
        """
        Get: SqlSeverity(self: JobHistoryFilter) -> int
        Set: SqlSeverity(self: JobHistoryFilter) = value
        """
        ...

    @property
    def StartRunDate(self) -> DateTime:
        """
        Get: StartRunDate(self: JobHistoryFilter) -> DateTime
        Set: StartRunDate(self: JobHistoryFilter) = value
        """
        ...



class JobOutcome(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum JobOutcome, values: Cancelled (3), Failed (0), InProgress (4), Succeeded (1), Unknown (5) """
    Cancelled: JobOutcome = ...
    Failed: JobOutcome = ...
    InProgress: JobOutcome = ...
    Succeeded: JobOutcome = ...
    Unknown: JobOutcome = ...
    value__ = ...


class ScheduleBase(AgentObjectBase): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """ no doc """
    @property
    def ID(self) -> int:
        """ Get: ID(self: ScheduleBase) -> int """
        ...


    def SetId(self, *args): #cannot find CLR method
        """ SetId(self: ScheduleBase, id: int) """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class JobSchedule(IDroppable, IAlterable, ICreatable, IScriptable, IRenamable, ScheduleBase, IDropIfExists): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    JobSchedule()
    JobSchedule(parent: SqlSmoObject, name: str)
    """
    @property
    def ActiveEndDate(self) -> DateTime:
        """
        Get: ActiveEndDate(self: JobSchedule) -> DateTime
        Set: ActiveEndDate(self: JobSchedule) = value
        """
        ...

    @property
    def ActiveEndTimeOfDay(self) -> TimeSpan:
        """
        Get: ActiveEndTimeOfDay(self: JobSchedule) -> TimeSpan
        Set: ActiveEndTimeOfDay(self: JobSchedule) = value
        """
        ...

    @property
    def ActiveStartDate(self) -> DateTime:
        """
        Get: ActiveStartDate(self: JobSchedule) -> DateTime
        Set: ActiveStartDate(self: JobSchedule) = value
        """
        ...

    @property
    def ActiveStartTimeOfDay(self) -> TimeSpan:
        """
        Get: ActiveStartTimeOfDay(self: JobSchedule) -> TimeSpan
        Set: ActiveStartTimeOfDay(self: JobSchedule) = value
        """
        ...

    @property
    def DateCreated(self) -> DateTime:
        """ Get: DateCreated(self: JobSchedule) -> DateTime """
        ...

    @property
    def FrequencyInterval(self) -> int:
        """
        Get: FrequencyInterval(self: JobSchedule) -> int
        Set: FrequencyInterval(self: JobSchedule) = value
        """
        ...

    @property
    def FrequencyRecurrenceFactor(self) -> int:
        """
        Get: FrequencyRecurrenceFactor(self: JobSchedule) -> int
        Set: FrequencyRecurrenceFactor(self: JobSchedule) = value
        """
        ...

    @property
    def FrequencyRelativeIntervals(self) -> FrequencyRelativeIntervals:
        """
        Get: FrequencyRelativeIntervals(self: JobSchedule) -> FrequencyRelativeIntervals
        Set: FrequencyRelativeIntervals(self: JobSchedule) = value
        """
        ...

    @property
    def FrequencySubDayInterval(self) -> int:
        """
        Get: FrequencySubDayInterval(self: JobSchedule) -> int
        Set: FrequencySubDayInterval(self: JobSchedule) = value
        """
        ...

    @property
    def FrequencySubDayTypes(self) -> FrequencySubDayTypes:
        """
        Get: FrequencySubDayTypes(self: JobSchedule) -> FrequencySubDayTypes
        Set: FrequencySubDayTypes(self: JobSchedule) = value
        """
        ...

    @property
    def FrequencyTypes(self) -> FrequencyTypes:
        """
        Get: FrequencyTypes(self: JobSchedule) -> FrequencyTypes
        Set: FrequencyTypes(self: JobSchedule) = value
        """
        ...

    @property
    def IsEnabled(self) -> bool:
        """
        Get: IsEnabled(self: JobSchedule) -> bool
        Set: IsEnabled(self: JobSchedule) = value
        """
        ...

    @property
    def JobCount(self) -> int:
        """ Get: JobCount(self: JobSchedule) -> int """
        ...

    @property
    def Parent(self) -> SqlSmoObject:
        """
        Get: Parent(self: JobSchedule) -> SqlSmoObject
        Set: Parent(self: JobSchedule) = value
        """
        ...

    @property
    def ScheduleUid(self) -> Guid:
        """
        Get: ScheduleUid(self: JobSchedule) -> Guid
        Set: ScheduleUid(self: JobSchedule) = value
        """
        ...


    def EnumJobReferences(self) -> Array:
        """ EnumJobReferences(self: JobSchedule) -> Array[Guid] """
        ...

    def __new__(cls, parent:SqlSmoObject = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, parent: SqlSmoObject, name: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class JobScheduleCollection(JobScheduleCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> SqlSmoObject:
        """ Get: Parent(self: JobScheduleCollection) -> SqlSmoObject """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: JobScheduleCollection, array: Array[JobSchedule], index: int) """
        ...

    def ItemById(self, id:int) -> JobSchedule:
        """ ItemById(self: JobScheduleCollection, id: int) -> JobSchedule """
        ...

    initialized = ...


class JobServer(SqlSmoObject, IAlterable, IScriptable): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """ no doc """
    @property
    def AgentDomainGroup(self) -> str:
        """ Get: AgentDomainGroup(self: JobServer) -> str """
        ...

    @property
    def AgentLogLevel(self) -> AgentLogLevels:
        """
        Get: AgentLogLevel(self: JobServer) -> AgentLogLevels
        Set: AgentLogLevel(self: JobServer) = value
        """
        ...

    @property
    def AgentMailType(self) -> AgentMailType:
        """
        Get: AgentMailType(self: JobServer) -> AgentMailType
        Set: AgentMailType(self: JobServer) = value
        """
        ...

    @property
    def AgentShutdownWaitTime(self) -> int:
        """
        Get: AgentShutdownWaitTime(self: JobServer) -> int
        Set: AgentShutdownWaitTime(self: JobServer) = value
        """
        ...

    @property
    def AlertCategories(self) -> AlertCategoryCollection:
        """ Get: AlertCategories(self: JobServer) -> AlertCategoryCollection """
        ...

    @property
    def Alerts(self) -> AlertCollection:
        """ Get: Alerts(self: JobServer) -> AlertCollection """
        ...

    @property
    def AlertSystem(self) -> AlertSystem:
        """ Get: AlertSystem(self: JobServer) -> AlertSystem """
        ...

    @property
    def DatabaseMailProfile(self) -> str:
        """
        Get: DatabaseMailProfile(self: JobServer) -> str
        Set: DatabaseMailProfile(self: JobServer) = value
        """
        ...

    @property
    def ErrorLogFile(self) -> str:
        """
        Get: ErrorLogFile(self: JobServer) -> str
        Set: ErrorLogFile(self: JobServer) = value
        """
        ...

    @property
    def HostLoginName(self) -> str:
        """ Get: HostLoginName(self: JobServer) -> str """
        ...

    @property
    def IdleCpuDuration(self) -> int:
        """
        Get: IdleCpuDuration(self: JobServer) -> int
        Set: IdleCpuDuration(self: JobServer) = value
        """
        ...

    @property
    def IdleCpuPercentage(self) -> int:
        """
        Get: IdleCpuPercentage(self: JobServer) -> int
        Set: IdleCpuPercentage(self: JobServer) = value
        """
        ...

    @property
    def IsCpuPollingEnabled(self) -> bool:
        """
        Get: IsCpuPollingEnabled(self: JobServer) -> bool
        Set: IsCpuPollingEnabled(self: JobServer) = value
        """
        ...

    @property
    def JobCategories(self) -> JobCategoryCollection:
        """ Get: JobCategories(self: JobServer) -> JobCategoryCollection """
        ...

    @property
    def Jobs(self) -> JobCollection:
        """ Get: Jobs(self: JobServer) -> JobCollection """
        ...

    @property
    def JobServerType(self) -> JobServerType:
        """ Get: JobServerType(self: JobServer) -> JobServerType """
        ...

    @property
    def LocalHostAlias(self) -> str:
        """
        Get: LocalHostAlias(self: JobServer) -> str
        Set: LocalHostAlias(self: JobServer) = value
        """
        ...

    @property
    def LoginTimeout(self) -> int:
        """
        Get: LoginTimeout(self: JobServer) -> int
        Set: LoginTimeout(self: JobServer) = value
        """
        ...

    @property
    def MaximumHistoryRows(self) -> int:
        """
        Get: MaximumHistoryRows(self: JobServer) -> int
        Set: MaximumHistoryRows(self: JobServer) = value
        """
        ...

    @property
    def MaximumJobHistoryRows(self) -> int:
        """
        Get: MaximumJobHistoryRows(self: JobServer) -> int
        Set: MaximumJobHistoryRows(self: JobServer) = value
        """
        ...

    @property
    def MsxAccountCredentialName(self) -> str:
        """ Get: MsxAccountCredentialName(self: JobServer) -> str """
        ...

    @property
    def MsxAccountName(self) -> str:
        """ Get: MsxAccountName(self: JobServer) -> str """
        ...

    @property
    def MsxServerName(self) -> str:
        """ Get: MsxServerName(self: JobServer) -> str """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: JobServer) -> str """
        ...

    @property
    def NetSendRecipient(self) -> str:
        """
        Get: NetSendRecipient(self: JobServer) -> str
        Set: NetSendRecipient(self: JobServer) = value
        """
        ...

    @property
    def OperatorCategories(self): # -> OperatorCategoryCollection
        """ Get: OperatorCategories(self: JobServer) -> OperatorCategoryCollection """
        ...

    @property
    def Operators(self): # -> OperatorCollection
        """ Get: Operators(self: JobServer) -> OperatorCollection """
        ...

    @property
    def Parent(self) -> Server:
        """ Get: Parent(self: JobServer) -> Server """
        ...

    @property
    def ProxyAccounts(self): # -> ProxyAccountCollection
        """ Get: ProxyAccounts(self: JobServer) -> ProxyAccountCollection """
        ...

    @property
    def ReplaceAlertTokensEnabled(self) -> bool:
        """
        Get: ReplaceAlertTokensEnabled(self: JobServer) -> bool
        Set: ReplaceAlertTokensEnabled(self: JobServer) = value
        """
        ...

    @property
    def SaveInSentFolder(self) -> bool:
        """
        Get: SaveInSentFolder(self: JobServer) -> bool
        Set: SaveInSentFolder(self: JobServer) = value
        """
        ...

    @property
    def ServiceAccount(self) -> str:
        """ Get: ServiceAccount(self: JobServer) -> str """
        ...

    @property
    def ServiceStartMode(self) -> ServiceStartMode:
        """ Get: ServiceStartMode(self: JobServer) -> ServiceStartMode """
        ...

    @property
    def SharedSchedules(self) -> JobScheduleCollection:
        """ Get: SharedSchedules(self: JobServer) -> JobScheduleCollection """
        ...

    @property
    def SqlAgentAutoStart(self) -> bool:
        """
        Get: SqlAgentAutoStart(self: JobServer) -> bool
        Set: SqlAgentAutoStart(self: JobServer) = value
        """
        ...

    @property
    def SqlAgentMailProfile(self) -> str:
        """
        Get: SqlAgentMailProfile(self: JobServer) -> str
        Set: SqlAgentMailProfile(self: JobServer) = value
        """
        ...

    @property
    def SqlAgentRestart(self) -> bool:
        """
        Get: SqlAgentRestart(self: JobServer) -> bool
        Set: SqlAgentRestart(self: JobServer) = value
        """
        ...

    @property
    def SqlServerRestart(self) -> bool:
        """
        Get: SqlServerRestart(self: JobServer) -> bool
        Set: SqlServerRestart(self: JobServer) = value
        """
        ...

    @property
    def SysAdminOnly(self) -> bool:
        """ Get: SysAdminOnly(self: JobServer) -> bool """
        ...

    @property
    def TargetServerGroups(self): # -> TargetServerGroupCollection
        """ Get: TargetServerGroups(self: JobServer) -> TargetServerGroupCollection """
        ...

    @property
    def TargetServers(self): # -> TargetServerCollection
        """ Get: TargetServers(self: JobServer) -> TargetServerCollection """
        ...

    @property
    def WriteOemErrorLog(self) -> bool:
        """
        Get: WriteOemErrorLog(self: JobServer) -> bool
        Set: WriteOemErrorLog(self: JobServer) = value
        """
        ...


    def ClearHostLoginAccount(self): # -> 
        """ ClearHostLoginAccount(self: JobServer) """
        ...

    def ClearMsxAccount(self): # -> 
        """ ClearMsxAccount(self: JobServer) """
        ...

    def CycleErrorLog(self): # -> 
        """ CycleErrorLog(self: JobServer) """
        ...

    def DropJobByID(self, jobid:Guid): # -> 
        """ DropJobByID(self: JobServer, jobid: Guid) """
        ...

    def DropJobsByLogin(self, login:str): # -> 
        """ DropJobsByLogin(self: JobServer, login: str) """
        ...

    def DropJobsByServer(self, serverName:str): # -> 
        """ DropJobsByServer(self: JobServer, serverName: str) """
        ...

    def EnumErrorLogs(self) -> DataTable:
        """ EnumErrorLogs(self: JobServer) -> DataTable """
        ...

    def EnumJobHistory(self, filter:JobHistoryFilter = ...) -> DataTable:
        """
        EnumJobHistory(self: JobServer, filter: JobHistoryFilter) -> DataTable
        EnumJobHistory(self: JobServer) -> DataTable
        """
        ...

    def EnumJobs(self, filter:JobFilter = ...) -> DataTable:
        """
        EnumJobs(self: JobServer, filter: JobFilter) -> DataTable
        EnumJobs(self: JobServer) -> DataTable
        """
        ...

    def EnumPerformanceCounters(self, objectName:str = ..., counterName:str = ..., instanceName:str = ...) -> DataTable:
        """
        EnumPerformanceCounters(self: JobServer) -> DataTable
        EnumPerformanceCounters(self: JobServer, objectName: str) -> DataTable
        EnumPerformanceCounters(self: JobServer, objectName: str, counterName: str) -> DataTable
        EnumPerformanceCounters(self: JobServer, objectName: str, counterName: str, instanceName: str) -> DataTable
        """
        ...

    def EnumSubSystems(self) -> DataTable:
        """ EnumSubSystems(self: JobServer) -> DataTable """
        ...

    def GetJobByID(self, jobId:Guid) -> Job:
        """ GetJobByID(self: JobServer, jobId: Guid) -> Job """
        ...

    def MsxDefect(self, forceDefection:bool = ...): # -> 
        """ MsxDefect(self: JobServer)MsxDefect(self: JobServer, forceDefection: bool) """
        ...

    def MsxEnlist(self, masterServer:str, location:str): # -> 
        """ MsxEnlist(self: JobServer, masterServer: str, location: str) """
        ...

    def PurgeJobHistory(self, filter:JobHistoryFilter = ...): # -> 
        """ PurgeJobHistory(self: JobServer)PurgeJobHistory(self: JobServer, filter: JobHistoryFilter) """
        ...

    def ReadErrorLog(self, logNumber:int = ...) -> DataTable:
        """
        ReadErrorLog(self: JobServer) -> DataTable
        ReadErrorLog(self: JobServer, logNumber: int) -> DataTable
        """
        ...

    def ReassignJobsByLogin(self, oldLogin:str, newLogin:str): # -> 
        """ ReassignJobsByLogin(self: JobServer, oldLogin: str, newLogin: str) """
        ...

    def RemoveJobByID(self, jobId:Guid): # -> 
        """ RemoveJobByID(self: JobServer, jobId: Guid) """
        ...

    def RemoveJobsByLogin(self, login:str): # -> 
        """ RemoveJobsByLogin(self: JobServer, login: str) """
        ...

    def SetHostLoginAccount(self, loginName:str, password:str): # -> 
        """ SetHostLoginAccount(self: JobServer, loginName: str, password: str) """
        ...

    def SetMsxAccount(self, *__args:str): # -> 
        """ SetMsxAccount(self: JobServer, account: str, password: str)SetMsxAccount(self: JobServer, credentialName: str) """
        ...

    def StartMonitor(self, netSendAddress:str, restartAttempts:int): # -> 
        """ StartMonitor(self: JobServer, netSendAddress: str, restartAttempts: int) """
        ...

    def StopMonitor(self): # -> 
        """ StopMonitor(self: JobServer) """
        ...

    def TestMailProfile(self, profileName:str): # -> 
        """ TestMailProfile(self: JobServer, profileName: str) """
        ...

    def TestNetSend(self): # -> 
        """ TestNetSend(self: JobServer) """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class JobServerType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum JobServerType, values: Msx (3), Standalone (1), Tsx (2) """
    Msx: JobServerType = ...
    Standalone: JobServerType = ...
    Tsx: JobServerType = ...
    value__ = ...


class JobStep(IDroppable, IAlterable, ICreatable, IScriptable, IRenamable, AgentObjectBase, IDropIfExists): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    JobStep()
    JobStep(job: Job, name: str)
    """
    @property
    def Command(self) -> str:
        """
        Get: Command(self: JobStep) -> str
        Set: Command(self: JobStep) = value
        """
        ...

    @property
    def CommandExecutionSuccessCode(self) -> int:
        """
        Get: CommandExecutionSuccessCode(self: JobStep) -> int
        Set: CommandExecutionSuccessCode(self: JobStep) = value
        """
        ...

    @property
    def DatabaseName(self) -> str:
        """
        Get: DatabaseName(self: JobStep) -> str
        Set: DatabaseName(self: JobStep) = value
        """
        ...

    @property
    def DatabaseUserName(self) -> str:
        """
        Get: DatabaseUserName(self: JobStep) -> str
        Set: DatabaseUserName(self: JobStep) = value
        """
        ...

    @property
    def ID(self) -> int:
        """
        Get: ID(self: JobStep) -> int
        Set: ID(self: JobStep) = value
        """
        ...

    @property
    def JobStepFlags(self) -> JobStepFlags:
        """
        Get: JobStepFlags(self: JobStep) -> JobStepFlags
        Set: JobStepFlags(self: JobStep) = value
        """
        ...

    @property
    def LastRunDate(self) -> DateTime:
        """ Get: LastRunDate(self: JobStep) -> DateTime """
        ...

    @property
    def LastRunDuration(self) -> int:
        """ Get: LastRunDuration(self: JobStep) -> int """
        ...

    @property
    def LastRunOutcome(self) -> CompletionResult:
        """ Get: LastRunOutcome(self: JobStep) -> CompletionResult """
        ...

    @property
    def LastRunRetries(self) -> int:
        """ Get: LastRunRetries(self: JobStep) -> int """
        ...

    @property
    def OnFailAction(self) -> StepCompletionAction:
        """
        Get: OnFailAction(self: JobStep) -> StepCompletionAction
        Set: OnFailAction(self: JobStep) = value
        """
        ...

    @property
    def OnFailStep(self) -> int:
        """
        Get: OnFailStep(self: JobStep) -> int
        Set: OnFailStep(self: JobStep) = value
        """
        ...

    @property
    def OnSuccessAction(self) -> StepCompletionAction:
        """
        Get: OnSuccessAction(self: JobStep) -> StepCompletionAction
        Set: OnSuccessAction(self: JobStep) = value
        """
        ...

    @property
    def OnSuccessStep(self) -> int:
        """
        Get: OnSuccessStep(self: JobStep) -> int
        Set: OnSuccessStep(self: JobStep) = value
        """
        ...

    @property
    def OSRunPriority(self) -> OSRunPriority:
        """
        Get: OSRunPriority(self: JobStep) -> OSRunPriority
        Set: OSRunPriority(self: JobStep) = value
        """
        ...

    @property
    def OutputFileName(self) -> str:
        """
        Get: OutputFileName(self: JobStep) -> str
        Set: OutputFileName(self: JobStep) = value
        """
        ...

    @property
    def Parent(self) -> Job:
        """
        Get: Parent(self: JobStep) -> Job
        Set: Parent(self: JobStep) = value
        """
        ...

    @property
    def ProxyName(self) -> str:
        """
        Get: ProxyName(self: JobStep) -> str
        Set: ProxyName(self: JobStep) = value
        """
        ...

    @property
    def RetryAttempts(self) -> int:
        """
        Get: RetryAttempts(self: JobStep) -> int
        Set: RetryAttempts(self: JobStep) = value
        """
        ...

    @property
    def RetryInterval(self) -> int:
        """
        Get: RetryInterval(self: JobStep) -> int
        Set: RetryInterval(self: JobStep) = value
        """
        ...

    @property
    def Server(self) -> str:
        """
        Get: Server(self: JobStep) -> str
        Set: Server(self: JobStep) = value
        """
        ...

    @property
    def SubSystem(self) -> AgentSubSystem:
        """
        Get: SubSystem(self: JobStep) -> AgentSubSystem
        Set: SubSystem(self: JobStep) = value
        """
        ...


    def DeleteLogs(self, *__args:DateTime): # -> 
        """ DeleteLogs(self: JobStep, olderThan: DateTime)DeleteLogs(self: JobStep, largerThan: int) """
        ...

    def EnumLogs(self) -> DataTable:
        """ EnumLogs(self: JobStep) -> DataTable """
        ...

    def __new__(cls, job:Job = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, job: Job, name: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class JobStepCollection(ParameterCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> Job:
        """ Get: Parent(self: JobStepCollection) -> Job """
        ...


    def Add(self, jobStep:JobStep, *__args:str): # -> 
        """ Add(self: JobStepCollection, jobStep: JobStep)Add(self: JobStepCollection, jobStep: JobStep, insertAtColumnName: str)Add(self: JobStepCollection, jobStep: JobStep, insertAtPosition: int) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: JobStepCollection, array: Array[JobStep], index: int) """
        ...

    def ItemById(self, id:int) -> JobStep:
        """ ItemById(self: JobStepCollection, id: int) -> JobStep """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class JobStepFlags(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) JobStepFlags, values: AppendAllCmdExecOutputToJobHistory (32), AppendToJobHistory (4), AppendToLogFile (2), AppendToTableLog (16), LogToTableWithOverwrite (8), None (0), ProvideStopProcessEvent (64) """
    AppendAllCmdExecOutputToJobHistory: JobStepFlags = ...
    AppendToJobHistory: JobStepFlags = ...
    AppendToLogFile: JobStepFlags = ...
    AppendToTableLog: JobStepFlags = ...
    LogToTableWithOverwrite: JobStepFlags = ...
    ProvideStopProcessEvent: JobStepFlags = ...
    value__ = ...


class JobType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum JobType, values: Local (1), MultiServer (2) """
    Local: JobType = ...
    MultiServer: JobType = ...
    value__ = ...


class MonthlyRelativeWeekDays(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum MonthlyRelativeWeekDays, values: EveryDay (8), Friday (6), Monday (2), Saturday (7), Sunday (1), Thursday (5), Tuesday (3), Wednesday (4), WeekDays (9), WeekEnds (10) """
    EveryDay: MonthlyRelativeWeekDays = ...
    Friday: MonthlyRelativeWeekDays = ...
    Monday: MonthlyRelativeWeekDays = ...
    Saturday: MonthlyRelativeWeekDays = ...
    Sunday: MonthlyRelativeWeekDays = ...
    Thursday: MonthlyRelativeWeekDays = ...
    Tuesday: MonthlyRelativeWeekDays = ...
    value__ = ...
    Wednesday: MonthlyRelativeWeekDays = ...
    WeekDays: MonthlyRelativeWeekDays = ...
    WeekEnds: MonthlyRelativeWeekDays = ...


class NotifyMethods(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) NotifyMethods, values: NetSend (4), None (0), NotifyAll (7), NotifyEmail (1), Pager (2) """
    NetSend: NotifyMethods = ...
    NotifyAll: NotifyMethods = ...
    NotifyEmail: NotifyMethods = ...
    Pager: NotifyMethods = ...
    value__ = ...


class NotifyType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum NotifyType, values: Actual (2), All (1), Target (3) """
    Actual: NotifyType = ...
    All: NotifyType = ...
    Target: NotifyType = ...
    value__ = ...


class Operator(IDroppable, IAlterable, ICreatable, IScriptable, IRenamable, AgentObjectBase, IDropIfExists): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    Operator()
    Operator(jobServer: JobServer, name: str)
    """
    @property
    def CategoryName(self) -> str:
        """
        Get: CategoryName(self: Operator) -> str
        Set: CategoryName(self: Operator) = value
        """
        ...

    @property
    def EmailAddress(self) -> str:
        """
        Get: EmailAddress(self: Operator) -> str
        Set: EmailAddress(self: Operator) = value
        """
        ...

    @property
    def Enabled(self) -> bool:
        """
        Get: Enabled(self: Operator) -> bool
        Set: Enabled(self: Operator) = value
        """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: Operator) -> int """
        ...

    @property
    def LastEmailDate(self) -> DateTime:
        """ Get: LastEmailDate(self: Operator) -> DateTime """
        ...

    @property
    def LastNetSendDate(self) -> DateTime:
        """ Get: LastNetSendDate(self: Operator) -> DateTime """
        ...

    @property
    def LastPagerDate(self) -> DateTime:
        """ Get: LastPagerDate(self: Operator) -> DateTime """
        ...

    @property
    def NetSendAddress(self) -> str:
        """
        Get: NetSendAddress(self: Operator) -> str
        Set: NetSendAddress(self: Operator) = value
        """
        ...

    @property
    def PagerAddress(self) -> str:
        """
        Get: PagerAddress(self: Operator) -> str
        Set: PagerAddress(self: Operator) = value
        """
        ...

    @property
    def PagerDays(self) -> WeekDays:
        """
        Get: PagerDays(self: Operator) -> WeekDays
        Set: PagerDays(self: Operator) = value
        """
        ...

    @property
    def Parent(self) -> JobServer:
        """
        Get: Parent(self: Operator) -> JobServer
        Set: Parent(self: Operator) = value
        """
        ...

    @property
    def SaturdayPagerEndTime(self) -> TimeSpan:
        """
        Get: SaturdayPagerEndTime(self: Operator) -> TimeSpan
        Set: SaturdayPagerEndTime(self: Operator) = value
        """
        ...

    @property
    def SaturdayPagerStartTime(self) -> TimeSpan:
        """
        Get: SaturdayPagerStartTime(self: Operator) -> TimeSpan
        Set: SaturdayPagerStartTime(self: Operator) = value
        """
        ...

    @property
    def SundayPagerEndTime(self) -> TimeSpan:
        """
        Get: SundayPagerEndTime(self: Operator) -> TimeSpan
        Set: SundayPagerEndTime(self: Operator) = value
        """
        ...

    @property
    def SundayPagerStartTime(self) -> TimeSpan:
        """
        Get: SundayPagerStartTime(self: Operator) -> TimeSpan
        Set: SundayPagerStartTime(self: Operator) = value
        """
        ...

    @property
    def WeekdayPagerEndTime(self) -> TimeSpan:
        """
        Get: WeekdayPagerEndTime(self: Operator) -> TimeSpan
        Set: WeekdayPagerEndTime(self: Operator) = value
        """
        ...

    @property
    def WeekdayPagerStartTime(self) -> TimeSpan:
        """
        Get: WeekdayPagerStartTime(self: Operator) -> TimeSpan
        Set: WeekdayPagerStartTime(self: Operator) = value
        """
        ...


    def AddNotification(self, alertName:str, notifymethod:NotifyMethods): # -> 
        """ AddNotification(self: Operator, alertName: str, notifymethod: NotifyMethods) """
        ...

    def EnumJobNotifications(self) -> DataTable:
        """ EnumJobNotifications(self: Operator) -> DataTable """
        ...

    def EnumNotifications(self, *__args:NotifyMethods) -> DataTable:
        """
        EnumNotifications(self: Operator) -> DataTable
        EnumNotifications(self: Operator, notifyMethod: NotifyMethods) -> DataTable
        EnumNotifications(self: Operator, alertName: str) -> DataTable
        EnumNotifications(self: Operator, notifyMethod: NotifyMethods, alertName: str) -> DataTable
        """
        ...

    def RemoveNotification(self, alertName:str): # -> 
        """ RemoveNotification(self: Operator, alertName: str) """
        ...

    def UpdateNotification(self, alertName:str, notifymethod:NotifyMethods): # -> 
        """ UpdateNotification(self: Operator, alertName: str, notifymethod: NotifyMethods) """
        ...

    def __new__(cls, jobServer:JobServer = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, jobServer: JobServer, name: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class OperatorCategory(CategoryBase): # skipped bases: <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'IScriptable'>, <type 'ISqlSmoObjectInitialize'>, <type 'IDroppable'>, <type 'ICreatable'>, <type 'IAlienObject'>, <type 'IDropIfExists'>, <type 'IRenamable'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'object'>
    """
    OperatorCategory()
    OperatorCategory(jobServer: JobServer, name: str)
    """
    @property
    def ID(self) -> int:
        """ Get: ID(self: OperatorCategory) -> int """
        ...

    @property
    def Parent(self) -> JobServer:
        """
        Get: Parent(self: OperatorCategory) -> JobServer
        Set: Parent(self: OperatorCategory) = value
        """
        ...


    def __new__(cls, jobServer:JobServer = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, jobServer: JobServer, name: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class OperatorCategoryCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> JobServer:
        """ Get: Parent(self: OperatorCategoryCollection) -> JobServer """
        ...


    def Add(self, operatorCategory:OperatorCategory): # -> 
        """ Add(self: OperatorCategoryCollection, operatorCategory: OperatorCategory) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: OperatorCategoryCollection, array: Array[OperatorCategory], index: int) """
        ...

    def ItemById(self, id:int) -> OperatorCategory:
        """ ItemById(self: OperatorCategoryCollection, id: int) -> OperatorCategory """
        ...

    def Remove(self, *__args:str): # -> 
        """ Remove(self: OperatorCategoryCollection, name: str)Remove(self: OperatorCategoryCollection, operatorCategory: OperatorCategory) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class OperatorCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> JobServer:
        """ Get: Parent(self: OperatorCollection) -> JobServer """
        ...


    def Add(self, serverOperator:Operator): # -> 
        """ Add(self: OperatorCollection, serverOperator: Operator) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: OperatorCollection, array: Array[Operator], index: int) """
        ...

    def ItemById(self, id:int) -> Operator:
        """ ItemById(self: OperatorCollection, id: int) -> Operator """
        ...

    def Script(self, scriptingOptions:ScriptingOptions = ...) -> StringCollection:
        """
        Script(self: OperatorCollection) -> StringCollection
        Script(self: OperatorCollection, scriptingOptions: ScriptingOptions) -> StringCollection
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class OSRunPriority(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum OSRunPriority, values: AboveNormal (1), BelowNormal (-1), Idle (-15), Normal (0), TimeCritical (15) """
    AboveNormal: OSRunPriority = ...
    BelowNormal: OSRunPriority = ...
    Idle: OSRunPriority = ...
    Normal: OSRunPriority = ...
    TimeCritical: OSRunPriority = ...
    value__ = ...


class ProxyAccount(IDroppable, IAlterable, ICreatable, IScriptable, IRenamable, AgentObjectBase, IDropIfExists): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    ProxyAccount()
    ProxyAccount(jobServer: JobServer, name: str)
    ProxyAccount(jobServer: JobServer, proxyName: str, credentialName: str, enabled: bool, description: str)
    ProxyAccount(jobServer: JobServer, proxyName: str, credentialName: str, enabled: bool)
    ProxyAccount(jobServer: JobServer, proxyName: str, credentialName: str)
    """
    @property
    def CredentialID(self) -> int:
        """ Get: CredentialID(self: ProxyAccount) -> int """
        ...

    @property
    def CredentialIdentity(self) -> str:
        """ Get: CredentialIdentity(self: ProxyAccount) -> str """
        ...

    @property
    def CredentialName(self) -> str:
        """
        Get: CredentialName(self: ProxyAccount) -> str
        Set: CredentialName(self: ProxyAccount) = value
        """
        ...

    @property
    def Description(self) -> str:
        """
        Get: Description(self: ProxyAccount) -> str
        Set: Description(self: ProxyAccount) = value
        """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: ProxyAccount) -> int """
        ...

    @property
    def IsEnabled(self) -> bool:
        """
        Get: IsEnabled(self: ProxyAccount) -> bool
        Set: IsEnabled(self: ProxyAccount) = value
        """
        ...

    @property
    def Parent(self) -> JobServer:
        """
        Get: Parent(self: ProxyAccount) -> JobServer
        Set: Parent(self: ProxyAccount) = value
        """
        ...


    def AddLogin(self, loginName:str): # -> 
        """ AddLogin(self: ProxyAccount, loginName: str) """
        ...

    def AddMsdbRole(self, msdbRoleName:str): # -> 
        """ AddMsdbRole(self: ProxyAccount, msdbRoleName: str) """
        ...

    def AddServerRole(self, serverRoleName:str): # -> 
        """ AddServerRole(self: ProxyAccount, serverRoleName: str) """
        ...

    def AddSubSystem(self, subSystem:AgentSubSystem): # -> 
        """ AddSubSystem(self: ProxyAccount, subSystem: AgentSubSystem) """
        ...

    def EnumLogins(self) -> DataTable:
        """ EnumLogins(self: ProxyAccount) -> DataTable """
        ...

    def EnumMsdbRoles(self) -> DataTable:
        """ EnumMsdbRoles(self: ProxyAccount) -> DataTable """
        ...

    def EnumServerRoles(self) -> DataTable:
        """ EnumServerRoles(self: ProxyAccount) -> DataTable """
        ...

    def EnumSubSystems(self) -> DataTable:
        """ EnumSubSystems(self: ProxyAccount) -> DataTable """
        ...

    def Reassign(self, targetProxyAccountName:str): # -> 
        """ Reassign(self: ProxyAccount, targetProxyAccountName: str) """
        ...

    def RemoveLogin(self, loginName:str): # -> 
        """ RemoveLogin(self: ProxyAccount, loginName: str) """
        ...

    def RemoveMsdbRole(self, msdbRoleName:str): # -> 
        """ RemoveMsdbRole(self: ProxyAccount, msdbRoleName: str) """
        ...

    def RemoveServerRole(self, serverRoleName:str): # -> 
        """ RemoveServerRole(self: ProxyAccount, serverRoleName: str) """
        ...

    def RemoveSubSystem(self, subSystem:AgentSubSystem): # -> 
        """ RemoveSubSystem(self: ProxyAccount, subSystem: AgentSubSystem) """
        ...

    def __new__(cls, jobServer:JobServer = ..., *__args:str) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, jobServer: JobServer, name: str)
        __new__(cls: type, jobServer: JobServer, proxyName: str, credentialName: str, enabled: bool, description: str)
        __new__(cls: type, jobServer: JobServer, proxyName: str, credentialName: str, enabled: bool)
        __new__(cls: type, jobServer: JobServer, proxyName: str, credentialName: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class ProxyAccountCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> JobServer:
        """ Get: Parent(self: ProxyAccountCollection) -> JobServer """
        ...


    def Add(self, proxyAccount:ProxyAccount): # -> 
        """ Add(self: ProxyAccountCollection, proxyAccount: ProxyAccount) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ProxyAccountCollection, array: Array[ProxyAccount], index: int) """
        ...

    def ItemById(self, id:int) -> ProxyAccount:
        """ ItemById(self: ProxyAccountCollection, id: int) -> ProxyAccount """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class StepCompletionAction(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum StepCompletionAction, values: GoToNextStep (3), GoToStep (4), QuitWithFailure (2), QuitWithSuccess (1) """
    GoToNextStep: StepCompletionAction = ...
    GoToStep: StepCompletionAction = ...
    QuitWithFailure: StepCompletionAction = ...
    QuitWithSuccess: StepCompletionAction = ...
    value__ = ...


class TargetServer(AgentObjectBase): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """ no doc """
    @property
    def EnlistDate(self) -> DateTime:
        """ Get: EnlistDate(self: TargetServer) -> DateTime """
        ...

    @property
    def ID(self) -> int:
        """ Get: ID(self: TargetServer) -> int """
        ...

    @property
    def LastPollDate(self) -> DateTime:
        """ Get: LastPollDate(self: TargetServer) -> DateTime """
        ...

    @property
    def LocalTime(self) -> DateTime:
        """ Get: LocalTime(self: TargetServer) -> DateTime """
        ...

    @property
    def Location(self) -> str:
        """ Get: Location(self: TargetServer) -> str """
        ...

    @property
    def Parent(self) -> JobServer:
        """ Get: Parent(self: TargetServer) -> JobServer """
        ...

    @property
    def PendingInstructions(self) -> int:
        """ Get: PendingInstructions(self: TargetServer) -> int """
        ...

    @property
    def PollingInterval(self) -> int:
        """ Get: PollingInterval(self: TargetServer) -> int """
        ...

    @property
    def Status(self) -> TargetServerStatus:
        """ Get: Status(self: TargetServer) -> TargetServerStatus """
        ...

    @property
    def TimeZoneAdjustment(self) -> int:
        """ Get: TimeZoneAdjustment(self: TargetServer) -> int """
        ...


    m_ExtendedProperties = ...
    singletonParent = ...


class TargetServerCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> JobServer:
        """ Get: Parent(self: TargetServerCollection) -> JobServer """
        ...


    def Add(self, server:TargetServer): # -> 
        """ Add(self: TargetServerCollection, server: TargetServer) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: TargetServerCollection, array: Array[TargetServer], index: int) """
        ...

    def ItemById(self, id:int) -> TargetServer:
        """ ItemById(self: TargetServerCollection, id: int) -> TargetServer """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class TargetServerGroup(IDroppable, AgentObjectBase, ICreatable, IDropIfExists, IRenamable): # skipped bases: <type 'IAlienObject'>, <type 'ISfcNotifyPropertyMetadataChanged'>, <type 'ISfcValidate'>, <type 'INotifyPropertyChanged'>, <type 'ISfcPropertyProvider'>, <type 'IRefreshable'>, <type 'ISqlSmoObjectInitialize'>, <type 'object'>
    """
    TargetServerGroup()
    TargetServerGroup(jobServer: JobServer, name: str)
    """
    @property
    def ID(self) -> int:
        """ Get: ID(self: TargetServerGroup) -> int """
        ...

    @property
    def Parent(self) -> JobServer:
        """
        Get: Parent(self: TargetServerGroup) -> JobServer
        Set: Parent(self: TargetServerGroup) = value
        """
        ...


    def AddMemberServer(self, srvname:str): # -> 
        """ AddMemberServer(self: TargetServerGroup, srvname: str) """
        ...

    def EnumMemberServers(self) -> Array:
        """ EnumMemberServers(self: TargetServerGroup) -> Array[TargetServer] """
        ...

    def RemoveMemberServer(self, srvname:str): # -> 
        """ RemoveMemberServer(self: TargetServerGroup, srvname: str) """
        ...

    def Script(self, scriptingOptions:ScriptingOptions = ...) -> StringCollection:
        """
        Script(self: TargetServerGroup) -> StringCollection
        Script(self: TargetServerGroup, scriptingOptions: ScriptingOptions) -> StringCollection
        """
        ...

    def __new__(cls, jobServer:JobServer = ..., name:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, jobServer: JobServer, name: str)
        """
        ...

    m_ExtendedProperties = ...
    singletonParent = ...


class TargetServerGroupCollection(SimpleObjectCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Parent(self) -> JobServer:
        """ Get: Parent(self: TargetServerGroupCollection) -> JobServer """
        ...


    def Add(self, targetServerGroup:TargetServerGroup): # -> 
        """ Add(self: TargetServerGroupCollection, targetServerGroup: TargetServerGroup) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: TargetServerGroupCollection, array: Array[TargetServerGroup], index: int) """
        ...

    def ItemById(self, id:int) -> TargetServerGroup:
        """ ItemById(self: TargetServerGroupCollection, id: int) -> TargetServerGroup """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    initialized = ...


class TargetServerStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) TargetServerStatus, values: Blocked (4), Normal (1), SuspectedOffline (2) """
    Blocked: TargetServerStatus = ...
    Normal: TargetServerStatus = ...
    SuspectedOffline: TargetServerStatus = ...
    value__ = ...


class WeekDays(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) WeekDays, values: EveryDay (127), Friday (32), Monday (2), Saturday (64), Sunday (1), Thursday (16), Tuesday (4), Wednesday (8), WeekDays (62), WeekEnds (65) """
    EveryDay: WeekDays = ...
    Friday: WeekDays = ...
    Monday: WeekDays = ...
    Saturday: WeekDays = ...
    Sunday: WeekDays = ...
    Thursday: WeekDays = ...
    Tuesday: WeekDays = ...
    value__ = ...
    Wednesday: WeekDays = ...
    WeekDays: WeekDays = ...
    WeekEnds: WeekDays = ...


