# encoding: utf-8
# module System.Web.Management calls itself Management
# from System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import DateTime, Enum, Guid, Int64, IntPtr, SystemException

from System.Collections import ICollection, ReadOnlyCollectionBase

from System.Collections.Specialized import NameValueCollection

from System.Configuration.Provider import ProviderBase

from System.Data.SqlClient import SqlException

from System.Net.Mail import MailMessage

from System.Security.Principal import IPrincipal

from System.Web.UI import ViewStateException

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    IInternalWebEventProvider, RuleFiringRecord, WebBaseEvent, 
    WebBaseEventCollection, WebEventBufferFlushInfo, WebEventFormatter, 
    WebProcessInformation, WebProcessStatistics, WebRequestInformation, 
    WebThreadInformation, field#)
"""

# no functions
# classes

class WebEventProvider(ProviderBase): # skipped bases: <type 'object'>
    """ no doc """
    def Flush(self): # -> 
        """ Flush(self: WebEventProvider) """
        ...

    def ProcessEvent(self, raisedEvent): # ->  # Not found arg types: {'raisedEvent': 'WebBaseEvent'}
        """ ProcessEvent(self: WebEventProvider, raisedEvent: WebBaseEvent) """
        ...

    def Shutdown(self): # -> 
        """ Shutdown(self: WebEventProvider) """
        ...


class BufferedWebEventProvider(WebEventProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BufferMode(self) -> str:
        """ Get: BufferMode(self: BufferedWebEventProvider) -> str """
        ...

    @property
    def UseBuffering(self) -> bool:
        """ Get: UseBuffering(self: BufferedWebEventProvider) -> bool """
        ...


    def Initialize(self, name:str, config:NameValueCollection): # -> 
        """ Initialize(self: BufferedWebEventProvider, name: str, config: NameValueCollection) """
        ...

    def ProcessEventFlush(self, flushInfo): # ->  # Not found arg types: {'flushInfo': 'WebEventBufferFlushInfo'}
        """ ProcessEventFlush(self: BufferedWebEventProvider, flushInfo: WebEventBufferFlushInfo) """
        ...


class EventLogWebEventProvider(WebEventProvider, IInternalWebEventProvider): # skipped bases: <type 'object'>
    """ no doc """
    def Initialize(self, name:str, config:NameValueCollection): # -> 
        """ Initialize(self: EventLogWebEventProvider, name: str, config: NameValueCollection) """
        ...


class EventNotificationType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum EventNotificationType, values: Flush (2), Regular (0), Unbuffered (3), Urgent (1) """
    Flush: EventNotificationType = ...
    Regular: EventNotificationType = ...
    Unbuffered: EventNotificationType = ...
    Urgent: EventNotificationType = ...
    value__ = ...


class IisTraceWebEventProvider(WebEventProvider): # skipped bases: <type 'object'>
    """ IisTraceWebEventProvider() """
    def Initialize(self, name:str, config:NameValueCollection): # -> 
        """ Initialize(self: IisTraceWebEventProvider, name: str, config: NameValueCollection) """
        ...


class IRegiisUtility: # skipped bases: <type 'object'>
    """ no doc """
    def ProtectedConfigAction(self, actionToPerform, firstArgument, secondArgument, providerName, appPath, site, cspOrLocation, keySize, exception) -> IntPtr:
        """ ProtectedConfigAction(self: IRegiisUtility, actionToPerform: Int64, firstArgument: str, secondArgument: str, providerName: str, appPath: str, site: str, cspOrLocation: str, keySize: int) -> IntPtr """
        ...

    def RegisterAsnetMmcAssembly(self, doReg, assemblyName, binaryDirectory, exception) -> IntPtr:
        """ RegisterAsnetMmcAssembly(self: IRegiisUtility, doReg: int, assemblyName: str, binaryDirectory: str) -> IntPtr """
        ...

    def RegisterSystemWebAssembly(self, doReg, exception) -> IntPtr:
        """ RegisterSystemWebAssembly(self: IRegiisUtility, doReg: int) -> IntPtr """
        ...

    def RemoveBrowserCaps(self, exception) -> IntPtr:
        """ RemoveBrowserCaps(self: IRegiisUtility) -> IntPtr """
        ...


class IWebEventCustomEvaluator: # skipped bases: <type 'object'>
    """ no doc """
    def CanFire(self, raisedEvent, record) -> bool: # Not found arg types: {'record': 'RuleFiringRecord', 'raisedEvent': 'WebBaseEvent'}
        """ CanFire(self: IWebEventCustomEvaluator, raisedEvent: WebBaseEvent, record: RuleFiringRecord) -> bool """
        ...


class MailEventNotificationInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Events(self): # -> WebBaseEventCollection
        """ Get: Events(self: MailEventNotificationInfo) -> WebBaseEventCollection """
        ...

    @property
    def EventsDiscardedByBuffer(self) -> int:
        """ Get: EventsDiscardedByBuffer(self: MailEventNotificationInfo) -> int """
        ...

    @property
    def EventsDiscardedDueToMessageLimit(self) -> int:
        """ Get: EventsDiscardedDueToMessageLimit(self: MailEventNotificationInfo) -> int """
        ...

    @property
    def EventsInBuffer(self) -> int:
        """ Get: EventsInBuffer(self: MailEventNotificationInfo) -> int """
        ...

    @property
    def EventsInNotification(self) -> int:
        """ Get: EventsInNotification(self: MailEventNotificationInfo) -> int """
        ...

    @property
    def EventsRemaining(self) -> int:
        """ Get: EventsRemaining(self: MailEventNotificationInfo) -> int """
        ...

    @property
    def LastNotificationUtc(self) -> DateTime:
        """ Get: LastNotificationUtc(self: MailEventNotificationInfo) -> DateTime """
        ...

    @property
    def Message(self) -> MailMessage:
        """ Get: Message(self: MailEventNotificationInfo) -> MailMessage """
        ...

    @property
    def MessageSequence(self) -> int:
        """ Get: MessageSequence(self: MailEventNotificationInfo) -> int """
        ...

    @property
    def MessagesInNotification(self) -> int:
        """ Get: MessagesInNotification(self: MailEventNotificationInfo) -> int """
        ...

    @property
    def NotificationSequence(self) -> int:
        """ Get: NotificationSequence(self: MailEventNotificationInfo) -> int """
        ...

    @property
    def NotificationType(self) -> EventNotificationType:
        """ Get: NotificationType(self: MailEventNotificationInfo) -> EventNotificationType """
        ...



class MailWebEventProvider(BufferedWebEventProvider): # skipped bases: <type 'object'>
    """ no doc """
    pass

class RegiisUtility(IRegiisUtility): # skipped bases: <type 'object'>
    """ RegiisUtility() """
    pass

class RuleFiringRecord: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def LastFired(self) -> DateTime:
        """ Get: LastFired(self: RuleFiringRecord) -> DateTime """
        ...

    @property
    def TimesRaised(self) -> int:
        """ Get: TimesRaised(self: RuleFiringRecord) -> int """
        ...



class SessionStateType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SessionStateType, values: Custom (2), Persisted (1), Temporary (0) """
    Custom: SessionStateType = ...
    Persisted: SessionStateType = ...
    Temporary: SessionStateType = ...
    value__ = ...


class SimpleMailWebEventProvider(MailWebEventProvider, IInternalWebEventProvider): # skipped bases: <type 'object'>
    """ no doc """
    pass

class SqlExecutionException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SqlExecutionException(message: str, server: str, database: str, sqlFile: str, commands: str, sqlException: SqlException)
    SqlExecutionException(message: str)
    SqlExecutionException(message: str, innerException: Exception)
    SqlExecutionException()
    """
    @property
    def Commands(self) -> str:
        """ Get: Commands(self: SqlExecutionException) -> str """
        ...

    @property
    def Database(self) -> str:
        """ Get: Database(self: SqlExecutionException) -> str """
        ...

    @property
    def Exception(self) -> SqlException:
        """ Get: Exception(self: SqlExecutionException) -> SqlException """
        ...

    @property
    def Server(self) -> str:
        """ Get: Server(self: SqlExecutionException) -> str """
        ...

    @property
    def SqlFile(self) -> str:
        """ Get: SqlFile(self: SqlExecutionException) -> str """
        ...


    SerializeObjectState = ...


class SqlFeatures(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SqlFeatures, values: All (1073741855), Membership (1), None (0), Personalization (8), Profile (2), RoleManager (4), SqlWebEventProvider (16) """
    All: SqlFeatures = ...
    Membership: SqlFeatures = ...
    Personalization: SqlFeatures = ...
    Profile: SqlFeatures = ...
    RoleManager: SqlFeatures = ...
    SqlWebEventProvider: SqlFeatures = ...
    value__ = ...


class SqlServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GenerateApplicationServicesScripts(install:bool, features:SqlFeatures, database:str) -> str:
        """ GenerateApplicationServicesScripts(install: bool, features: SqlFeatures, database: str) -> str """
        ...

    @staticmethod
    def GenerateSessionStateScripts(install:bool, type:SessionStateType, customDatabase:str) -> str:
        """ GenerateSessionStateScripts(install: bool, type: SessionStateType, customDatabase: str) -> str """
        ...

    @staticmethod
    def Install(*__args): # -> 
        """ Install(server: str, user: str, password: str, database: str, features: SqlFeatures)Install(server: str, database: str, features: SqlFeatures)Install(database: str, features: SqlFeatures, connectionString: str) """
        ...

    @staticmethod
    def InstallSessionState(*__args): # -> 
        """ InstallSessionState(server: str, user: str, password: str, customDatabase: str, type: SessionStateType)InstallSessionState(server: str, customDatabase: str, type: SessionStateType)InstallSessionState(customDatabase: str, type: SessionStateType, connectionString: str) """
        ...

    @staticmethod
    def Uninstall(*__args): # -> 
        """ Uninstall(server: str, user: str, password: str, database: str, features: SqlFeatures)Uninstall(server: str, database: str, features: SqlFeatures)Uninstall(database: str, features: SqlFeatures, connectionString: str) """
        ...

    @staticmethod
    def UninstallSessionState(*__args): # -> 
        """ UninstallSessionState(server: str, user: str, password: str, customDatabase: str, type: SessionStateType)UninstallSessionState(server: str, customDatabase: str, type: SessionStateType)UninstallSessionState(customDatabase: str, type: SessionStateType, connectionString: str) """
        ...

    __all__: list = ...


class SqlWebEventProvider(BufferedWebEventProvider, IInternalWebEventProvider): # skipped bases: <type 'object'>
    """ no doc """
    def EventProcessingComplete(self, *args): #cannot find CLR method
        """ EventProcessingComplete(self: SqlWebEventProvider, raisedEvents: WebBaseEventCollection) """
        ...


class TemplatedMailWebEventProvider(MailWebEventProvider, IInternalWebEventProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CurrentNotification(self) -> MailEventNotificationInfo:
        """ Get: CurrentNotification() -> MailEventNotificationInfo """
        ...



class TraceWebEventProvider(WebEventProvider, IInternalWebEventProvider): # skipped bases: <type 'object'>
    """ no doc """
    def Initialize(self, name:str, config:NameValueCollection): # -> 
        """ Initialize(self: TraceWebEventProvider, name: str, config: NameValueCollection) """
        ...


class WebApplicationInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ApplicationDomain(self) -> str:
        """ Get: ApplicationDomain(self: WebApplicationInformation) -> str """
        ...

    @property
    def ApplicationPath(self) -> str:
        """ Get: ApplicationPath(self: WebApplicationInformation) -> str """
        ...

    @property
    def ApplicationVirtualPath(self) -> str:
        """ Get: ApplicationVirtualPath(self: WebApplicationInformation) -> str """
        ...

    @property
    def MachineName(self) -> str:
        """ Get: MachineName(self: WebApplicationInformation) -> str """
        ...

    @property
    def TrustLevel(self) -> str:
        """ Get: TrustLevel(self: WebApplicationInformation) -> str """
        ...


    def FormatToString(self, formatter): # ->  # Not found arg types: {'formatter': 'WebEventFormatter'}
        """ FormatToString(self: WebApplicationInformation, formatter: WebEventFormatter) """
        ...

    def ToString(self) -> str:
        """ ToString(self: WebApplicationInformation) -> str """
        ...


class WebBaseEvent: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ApplicationInformation(self) -> WebApplicationInformation:
        """ Get: ApplicationInformation() -> WebApplicationInformation """
        ...

    @property
    def EventCode(self) -> int:
        """ Get: EventCode(self: WebBaseEvent) -> int """
        ...

    @property
    def EventDetailCode(self) -> int:
        """ Get: EventDetailCode(self: WebBaseEvent) -> int """
        ...

    @property
    def EventID(self) -> Guid:
        """ Get: EventID(self: WebBaseEvent) -> Guid """
        ...

    @property
    def EventOccurrence(self) -> Int64:
        """ Get: EventOccurrence(self: WebBaseEvent) -> Int64 """
        ...

    @property
    def EventSequence(self) -> Int64:
        """ Get: EventSequence(self: WebBaseEvent) -> Int64 """
        ...

    @property
    def EventSource(self) -> object:
        """ Get: EventSource(self: WebBaseEvent) -> object """
        ...

    @property
    def EventTime(self) -> DateTime:
        """ Get: EventTime(self: WebBaseEvent) -> DateTime """
        ...

    @property
    def EventTimeUtc(self) -> DateTime:
        """ Get: EventTimeUtc(self: WebBaseEvent) -> DateTime """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: WebBaseEvent) -> str """
        ...


    def FormatCustomEventDetails(self, formatter): # ->  # Not found arg types: {'formatter': 'WebEventFormatter'}
        """ FormatCustomEventDetails(self: WebBaseEvent, formatter: WebEventFormatter) """
        ...

    def IncrementPerfCounters(self, *args): #cannot find CLR method
        """ IncrementPerfCounters(self: WebBaseEvent) """
        ...

    def Raise(self, eventRaised=None): # -> 
        """ Raise(self: WebBaseEvent)Raise(eventRaised: WebBaseEvent) """
        ...

    def ToString(self, includeAppInfo:bool = ..., includeCustomEventDetails:bool = ...) -> str:
        """
        ToString(self: WebBaseEvent) -> str
        ToString(self: WebBaseEvent, includeAppInfo: bool, includeCustomEventDetails: bool) -> str
        """
        ...



class WebManagementEvent(WebBaseEvent): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ProcessInformation(self): # -> WebProcessInformation
        """ Get: ProcessInformation(self: WebManagementEvent) -> WebProcessInformation """
        ...



class WebApplicationLifetimeEvent(WebManagementEvent): # skipped bases: <type 'object'>
    """ no doc """
    pass

class WebAuditEvent(WebManagementEvent): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RequestInformation(self): # -> WebRequestInformation
        """ Get: RequestInformation(self: WebAuditEvent) -> WebRequestInformation """
        ...



class WebFailureAuditEvent(WebAuditEvent): # skipped bases: <type 'object'>
    """ no doc """
    pass

class WebAuthenticationFailureAuditEvent(WebFailureAuditEvent): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def NameToAuthenticate(self) -> str:
        """ Get: NameToAuthenticate(self: WebAuthenticationFailureAuditEvent) -> str """
        ...



class WebSuccessAuditEvent(WebAuditEvent): # skipped bases: <type 'object'>
    """ no doc """
    pass

class WebAuthenticationSuccessAuditEvent(WebSuccessAuditEvent): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def NameToAuthenticate(self) -> str:
        """ Get: NameToAuthenticate(self: WebAuthenticationSuccessAuditEvent) -> str """
        ...



class WebBaseErrorEvent(WebManagementEvent): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ErrorException(self) -> Exception:
        """ Get: ErrorException(self: WebBaseErrorEvent) -> Exception """
        ...



class WebBaseEventCollection(ReadOnlyCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ WebBaseEventCollection(events: ICollection) """
    def Contains(self, value:WebBaseEvent) -> bool:
        """ Contains(self: WebBaseEventCollection, value: WebBaseEvent) -> bool """
        ...

    def IndexOf(self, value:WebBaseEvent) -> int:
        """ IndexOf(self: WebBaseEventCollection, value: WebBaseEvent) -> int """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __new__(cls, events:ICollection) -> Self:
        """ __new__(cls: type, events: ICollection) """
        ...


class WebErrorEvent(WebBaseErrorEvent): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RequestInformation(self): # -> WebRequestInformation
        """ Get: RequestInformation(self: WebErrorEvent) -> WebRequestInformation """
        ...

    @property
    def ThreadInformation(self): # -> WebThreadInformation
        """ Get: ThreadInformation(self: WebErrorEvent) -> WebThreadInformation """
        ...



class WebEventBufferFlushInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Events(self) -> WebBaseEventCollection:
        """ Get: Events(self: WebEventBufferFlushInfo) -> WebBaseEventCollection """
        ...

    @property
    def EventsDiscardedSinceLastNotification(self) -> int:
        """ Get: EventsDiscardedSinceLastNotification(self: WebEventBufferFlushInfo) -> int """
        ...

    @property
    def EventsInBuffer(self) -> int:
        """ Get: EventsInBuffer(self: WebEventBufferFlushInfo) -> int """
        ...

    @property
    def LastNotificationUtc(self) -> DateTime:
        """ Get: LastNotificationUtc(self: WebEventBufferFlushInfo) -> DateTime """
        ...

    @property
    def NotificationSequence(self) -> int:
        """ Get: NotificationSequence(self: WebEventBufferFlushInfo) -> int """
        ...

    @property
    def NotificationType(self) -> EventNotificationType:
        """ Get: NotificationType(self: WebEventBufferFlushInfo) -> EventNotificationType """
        ...



class WebEventCodes: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    ApplicationCodeBase: int = ...
    ApplicationCompilationEnd: int = ...
    ApplicationCompilationStart: int = ...
    ApplicationDetailCodeBase: int = ...
    ApplicationHeartbeat: int = ...
    ApplicationShutdown: int = ...
    ApplicationShutdownBinDirChangeOrDirectoryRename: int = ...
    ApplicationShutdownBrowsersDirChangeOrDirectoryRename: int = ...
    ApplicationShutdownBuildManagerChange: int = ...
    ApplicationShutdownChangeInGlobalAsax: int = ...
    ApplicationShutdownChangeInSecurityPolicyFile: int = ...
    ApplicationShutdownCodeDirChangeOrDirectoryRename: int = ...
    ApplicationShutdownConfigurationChange: int = ...
    ApplicationShutdownHostingEnvironment: int = ...
    ApplicationShutdownHttpRuntimeClose: int = ...
    ApplicationShutdownIdleTimeout: int = ...
    ApplicationShutdownInitializationError: int = ...
    ApplicationShutdownMaxRecompilationsReached: int = ...
    ApplicationShutdownPhysicalApplicationPathChanged: int = ...
    ApplicationShutdownResourcesDirChangeOrDirectoryRename: int = ...
    ApplicationShutdownUnknown: int = ...
    ApplicationShutdownUnloadAppDomainCalled: int = ...
    ApplicationStart: int = ...
    AuditCodeBase: int = ...
    AuditDetailCodeBase: int = ...
    AuditFileAuthorizationFailure: int = ...
    AuditFileAuthorizationSuccess: int = ...
    AuditFormsAuthenticationFailure: int = ...
    AuditFormsAuthenticationSuccess: int = ...
    AuditInvalidViewStateFailure: int = ...
    AuditMembershipAuthenticationFailure: int = ...
    AuditMembershipAuthenticationSuccess: int = ...
    AuditUnhandledAccessException: int = ...
    AuditUnhandledSecurityException: int = ...
    AuditUrlAuthorizationFailure: int = ...
    AuditUrlAuthorizationSuccess: int = ...
    ErrorCodeBase: int = ...
    ExpiredTicketFailure: int = ...
    InvalidEventCode: int = ...
    InvalidTicketFailure: int = ...
    InvalidViewState: int = ...
    InvalidViewStateMac: int = ...
    MiscCodeBase: int = ...
    RequestCodeBase: int = ...
    RequestTransactionAbort: int = ...
    RequestTransactionComplete: int = ...
    RuntimeErrorPostTooLarge: int = ...
    RuntimeErrorRequestAbort: int = ...
    RuntimeErrorUnhandledException: int = ...
    RuntimeErrorValidationFailure: int = ...
    RuntimeErrorViewStateFailure: int = ...
    RuntimeErrorWebResourceFailure: int = ...
    SqlProviderEventsDropped: int = ...
    StateServerConnectionError: int = ...
    UndefinedEventCode: int = ...
    UndefinedEventDetailCode: int = ...
    WebErrorCompilationError: int = ...
    WebErrorConfigurationError: int = ...
    WebErrorObjectStateFormatterDeserializationError: int = ...
    WebErrorOtherError: int = ...
    WebErrorParserError: int = ...
    WebErrorPropertyDeserializationError: int = ...
    WebEventDetailCodeBase: int = ...
    WebEventProviderInformation: int = ...
    WebExtendedBase: int = ...


class WebEventFormatter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IndentationLevel(self) -> int:
        """
        Get: IndentationLevel(self: WebEventFormatter) -> int
        Set: IndentationLevel(self: WebEventFormatter) = value
        """
        ...

    @property
    def TabSize(self) -> int:
        """
        Get: TabSize(self: WebEventFormatter) -> int
        Set: TabSize(self: WebEventFormatter) = value
        """
        ...


    def AppendLine(self, s:str): # -> 
        """ AppendLine(self: WebEventFormatter, s: str) """
        ...

    def ToString(self) -> str:
        """ ToString(self: WebEventFormatter) -> str """
        ...


class WebEventManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Flush(providerName:str = ...): # -> 
        """ Flush(providerName: str)Flush() """
        ...

    __all__: list = ...


class WebHeartbeatEvent(WebManagementEvent): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ProcessStatistics(self): # -> WebProcessStatistics
        """ Get: ProcessStatistics(self: WebHeartbeatEvent) -> WebProcessStatistics """
        ...



class WebProcessInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AccountName(self) -> str:
        """ Get: AccountName(self: WebProcessInformation) -> str """
        ...

    @property
    def ProcessID(self) -> int:
        """ Get: ProcessID(self: WebProcessInformation) -> int """
        ...

    @property
    def ProcessName(self) -> str:
        """ Get: ProcessName(self: WebProcessInformation) -> str """
        ...


    def FormatToString(self, formatter:WebEventFormatter): # -> 
        """ FormatToString(self: WebProcessInformation, formatter: WebEventFormatter) """
        ...


class WebProcessStatistics: # skipped bases: <type 'object'>, <type 'object'>
    """ WebProcessStatistics() """
    @property
    def AppDomainCount(self) -> int:
        """ Get: AppDomainCount(self: WebProcessStatistics) -> int """
        ...

    @property
    def ManagedHeapSize(self) -> Int64:
        """ Get: ManagedHeapSize(self: WebProcessStatistics) -> Int64 """
        ...

    @property
    def PeakWorkingSet(self) -> Int64:
        """ Get: PeakWorkingSet(self: WebProcessStatistics) -> Int64 """
        ...

    @property
    def ProcessStartTime(self) -> DateTime:
        """ Get: ProcessStartTime(self: WebProcessStatistics) -> DateTime """
        ...

    @property
    def RequestsExecuting(self) -> int:
        """ Get: RequestsExecuting(self: WebProcessStatistics) -> int """
        ...

    @property
    def RequestsQueued(self) -> int:
        """ Get: RequestsQueued(self: WebProcessStatistics) -> int """
        ...

    @property
    def RequestsRejected(self) -> int:
        """ Get: RequestsRejected(self: WebProcessStatistics) -> int """
        ...

    @property
    def ThreadCount(self) -> int:
        """ Get: ThreadCount(self: WebProcessStatistics) -> int """
        ...

    @property
    def WorkingSet(self) -> Int64:
        """ Get: WorkingSet(self: WebProcessStatistics) -> Int64 """
        ...


    def FormatToString(self, formatter:WebEventFormatter): # -> 
        """ FormatToString(self: WebProcessStatistics, formatter: WebEventFormatter) """
        ...


class WebRequestErrorEvent(WebBaseErrorEvent): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RequestInformation(self): # -> WebRequestInformation
        """ Get: RequestInformation(self: WebRequestErrorEvent) -> WebRequestInformation """
        ...

    @property
    def ThreadInformation(self): # -> WebThreadInformation
        """ Get: ThreadInformation(self: WebRequestErrorEvent) -> WebThreadInformation """
        ...



class WebRequestEvent(WebManagementEvent): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RequestInformation(self): # -> WebRequestInformation
        """ Get: RequestInformation(self: WebRequestEvent) -> WebRequestInformation """
        ...



class WebRequestInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Principal(self) -> IPrincipal:
        """ Get: Principal(self: WebRequestInformation) -> IPrincipal """
        ...

    @property
    def RequestPath(self) -> str:
        """ Get: RequestPath(self: WebRequestInformation) -> str """
        ...

    @property
    def RequestUrl(self) -> str:
        """ Get: RequestUrl(self: WebRequestInformation) -> str """
        ...

    @property
    def ThreadAccountName(self) -> str:
        """ Get: ThreadAccountName(self: WebRequestInformation) -> str """
        ...

    @property
    def UserHostAddress(self) -> str:
        """ Get: UserHostAddress(self: WebRequestInformation) -> str """
        ...


    def FormatToString(self, formatter:WebEventFormatter): # -> 
        """ FormatToString(self: WebRequestInformation, formatter: WebEventFormatter) """
        ...


class WebServiceErrorEvent(WebRequestErrorEvent): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def WebServiceErrorEventCode(self) -> int:
        """ Get: WebServiceErrorEventCode() -> int """
        ...




class WebThreadInformation: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def IsImpersonating(self) -> bool:
        """ Get: IsImpersonating(self: WebThreadInformation) -> bool """
        ...

    @property
    def StackTrace(self) -> str:
        """ Get: StackTrace(self: WebThreadInformation) -> str """
        ...

    @property
    def ThreadAccountName(self) -> str:
        """ Get: ThreadAccountName(self: WebThreadInformation) -> str """
        ...

    @property
    def ThreadID(self) -> int:
        """ Get: ThreadID(self: WebThreadInformation) -> int """
        ...


    def FormatToString(self, formatter:WebEventFormatter): # -> 
        """ FormatToString(self: WebThreadInformation, formatter: WebEventFormatter) """
        ...


class WebViewStateFailureAuditEvent(WebFailureAuditEvent): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ViewStateException(self) -> ViewStateException:
        """ Get: ViewStateException(self: WebViewStateFailureAuditEvent) -> ViewStateException """
        ...



class WmiWebEventProvider(WebEventProvider): # skipped bases: <type 'object'>
    """ WmiWebEventProvider() """
    def Initialize(self, name:str, config:NameValueCollection): # -> 
        """ Initialize(self: WmiWebEventProvider, name: str, config: NameValueCollection) """
        ...


