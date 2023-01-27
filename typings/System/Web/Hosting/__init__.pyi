# encoding: utf-8
# module System.Web.Hosting calls itself Hosting
# from System.Web.ApplicationServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Action, AppDomain, Array, Attribute, DateTime, Enum, 
    IDisposable, IObservable, IObserver, Int64, IntPtr, MarshalByRefObject, 
    Type)

from System.Collections import IEnumerable

from System.IO import Stream, TextWriter

from System.Security.Policy import Evidence

from System.Web import ApplicationShutdownReason, HttpWorkerRequest

from System.Web.Caching import Cache, CacheDependency

from System.Web.Configuration import IConfigMapPathFactory

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, Func, 
    HostSecurityPolicyResults, IAppDomainFactory, IAppDomainInfo, 
    IAppDomainInfoEnum, IAppManagerAppDomainFactory, IApplicationHost, 
    IApplicationMonitor, IApplicationPreloadUtil, ICustomRuntimeManager, 
    IISAPIRuntime2, IListenerChannelCallback, IProcessHostLite, 
    IProcessHostSupportFunctions, IProcessPingCallback, 
    IProcessSuspendListener, IRegisteredObject, 
    RecycleLimitNotificationFrequency, VirtualPathProvider, field#)
"""

# no functions
# classes

class AppDomainFactory(IAppDomainFactory): # skipped bases: <type 'object'>
    """ AppDomainFactory() """
    pass

class AppDomainInfo(IAppDomainInfo): # skipped bases: <type 'object'>
    """ no doc """
    pass

class AppDomainInfoEnum(IAppDomainInfoEnum): # skipped bases: <type 'object'>
    """ no doc """
    pass

class AppDomainProtocolHandler(IRegisteredObject, MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    def StartListenerChannel(self, listenerChannelCallback): # ->  # Not found arg types: {'listenerChannelCallback': 'IListenerChannelCallback'}
        """ StartListenerChannel(self: AppDomainProtocolHandler, listenerChannelCallback: IListenerChannelCallback) """
        ...

    def StopListenerChannel(self, listenerChannelId:int, immediate:bool): # -> 
        """ StopListenerChannel(self: AppDomainProtocolHandler, listenerChannelId: int, immediate: bool) """
        ...

    def StopProtocol(self, immediate:bool): # -> 
        """ StopProtocol(self: AppDomainProtocolHandler, immediate: bool) """
        ...


class ApplicationHost: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateApplicationHost(hostType:Type, virtualDir:str, physicalDir:str) -> object:
        """ CreateApplicationHost(hostType: Type, virtualDir: str, physicalDir: str) -> object """
        ...


class ApplicationInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ID(self) -> str:
        """ Get: ID(self: ApplicationInfo) -> str """
        ...

    @property
    def PhysicalPath(self) -> str:
        """ Get: PhysicalPath(self: ApplicationInfo) -> str """
        ...

    @property
    def VirtualPath(self) -> str:
        """ Get: VirtualPath(self: ApplicationInfo) -> str """
        ...



class ApplicationManager(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    def Close(self): # -> 
        """ Close(self: ApplicationManager) """
        ...

    def CreateObject(self, *__args): # -> IRegisteredObject
        """
        CreateObject(self: ApplicationManager, appHost: IApplicationHost, type: Type) -> IRegisteredObject
        CreateObject(self: ApplicationManager, appId: str, type: Type, virtualPath: str, physicalPath: str, failIfExists: bool) -> IRegisteredObject
        CreateObject(self: ApplicationManager, appId: str, type: Type, virtualPath: str, physicalPath: str, failIfExists: bool, throwOnError: bool) -> IRegisteredObject
        """
        ...

    def GetAppDomain(self, *__args:str) -> AppDomain:
        """
        GetAppDomain(self: ApplicationManager, appId: str) -> AppDomain
        GetAppDomain(self: ApplicationManager, appHost: IApplicationHost) -> AppDomain
        """
        ...

    @staticmethod
    def GetApplicationManager() -> ApplicationManager:
        """ GetApplicationManager() -> ApplicationManager """
        ...

    def GetObject(self, appId:str, type:Type): # -> IRegisteredObject
        """ GetObject(self: ApplicationManager, appId: str, type: Type) -> IRegisteredObject """
        ...

    def GetRunningApplications(self) -> Array:
        """ GetRunningApplications(self: ApplicationManager) -> Array[ApplicationInfo] """
        ...

    def IsIdle(self) -> bool:
        """ IsIdle(self: ApplicationManager) -> bool """
        ...

    def Open(self): # -> 
        """ Open(self: ApplicationManager) """
        ...

    def ShutdownAll(self): # -> 
        """ ShutdownAll(self: ApplicationManager) """
        ...

    def ShutdownApplication(self, appId:str): # -> 
        """ ShutdownApplication(self: ApplicationManager, appId: str) """
        ...

    def StopObject(self, appId:str, type:Type): # -> 
        """ StopObject(self: ApplicationManager, appId: str, type: Type) """
        ...


class ApplicationMonitors: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def MemoryMonitor(self): # -> IApplicationMonitor
        """
        Get: MemoryMonitor(self: ApplicationMonitors) -> IApplicationMonitor
        Set: MemoryMonitor(self: ApplicationMonitors) = value
        """
        ...



class AppManagerAppDomainFactory(IAppManagerAppDomainFactory): # skipped bases: <type 'object'>
    """ AppManagerAppDomainFactory() """
    pass

class AspNetMemoryMonitor(IObservable, IApplicationMonitor): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def DefaultLowPhysicalMemoryObserver(self) -> IObserver:
        """
        Get: DefaultLowPhysicalMemoryObserver(self: AspNetMemoryMonitor) -> IObserver[LowPhysicalMemoryInfo]
        Set: DefaultLowPhysicalMemoryObserver(self: AspNetMemoryMonitor) = value
        """
        ...

    @property
    def DefaultRecycleLimitObserver(self) -> IObserver:
        """
        Get: DefaultRecycleLimitObserver(self: AspNetMemoryMonitor) -> IObserver[RecycleLimitInfo]
        Set: DefaultRecycleLimitObserver(self: AspNetMemoryMonitor) = value
        """
        ...


    def Dispose(self): # -> 
        """ Dispose(self: AspNetMemoryMonitor) """
        ...


class CustomLoaderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ CustomLoaderAttribute(customLoaderType: Type) """
    @property
    def CustomLoaderType(self) -> Type:
        """ Get: CustomLoaderType(self: CustomLoaderAttribute) -> Type """
        ...


    def __new__(cls, customLoaderType:Type) -> Self:
        """ __new__(cls: type, customLoaderType: Type) """
        ...


class HostingEnvironment(MarshalByRefObject): # skipped bases: <type 'object'>
    """ HostingEnvironment() """
    @property
    def ApplicationHost(self): # -> IApplicationHost
        """ Get: ApplicationHost() -> IApplicationHost """
        ...

    @property
    def ApplicationID(self) -> str:
        """ Get: ApplicationID() -> str """
        ...

    @property
    def ApplicationMonitors(self) -> ApplicationMonitors:
        """ Get: ApplicationMonitors() -> ApplicationMonitors """
        ...

    @property
    def ApplicationPhysicalPath(self) -> str:
        """ Get: ApplicationPhysicalPath() -> str """
        ...

    @property
    def ApplicationVirtualPath(self) -> str:
        """ Get: ApplicationVirtualPath() -> str """
        ...

    @property
    def Cache(self) -> Cache:
        """ Get: Cache() -> Cache """
        ...

    @property
    def InClientBuildManager(self) -> bool:
        """ Get: InClientBuildManager() -> bool """
        ...

    @property
    def InitializationException(self) -> Exception:
        """ Get: InitializationException() -> Exception """
        ...

    @property
    def IsDevelopmentEnvironment(self) -> bool:
        """ Get: IsDevelopmentEnvironment() -> bool """
        ...

    @property
    def IsHosted(self) -> bool:
        """ Get: IsHosted() -> bool """
        ...

    @property
    def MaxConcurrentRequestsPerCPU(self) -> int:
        """
        Get: MaxConcurrentRequestsPerCPU() -> int
        Set: MaxConcurrentRequestsPerCPU() = value
        """
        ...

    @property
    def MaxConcurrentThreadsPerCPU(self) -> int:
        """
        Get: MaxConcurrentThreadsPerCPU() -> int
        Set: MaxConcurrentThreadsPerCPU() = value
        """
        ...

    @property
    def ShutdownReason(self) -> ApplicationShutdownReason:
        """ Get: ShutdownReason() -> ApplicationShutdownReason """
        ...

    @property
    def SiteName(self) -> str:
        """ Get: SiteName() -> str """
        ...

    @property
    def VirtualPathProvider(self): # -> VirtualPathProvider
        """ Get: VirtualPathProvider() -> VirtualPathProvider """
        ...


    @staticmethod
    def DecrementBusyCount(): # -> 
        """ DecrementBusyCount() """
        ...

    @staticmethod
    def Impersonate(*__args) -> IDisposable:
        """
        Impersonate() -> IDisposable
        Impersonate(token: IntPtr) -> IDisposable
        Impersonate(userToken: IntPtr, virtualPath: str) -> IDisposable
        """
        ...

    @staticmethod
    def IncrementBusyCount(): # -> 
        """ IncrementBusyCount() """
        ...

    @staticmethod
    def InitiateShutdown(): # -> 
        """ InitiateShutdown() """
        ...

    @staticmethod
    def MapPath(virtualPath:str) -> str:
        """ MapPath(virtualPath: str) -> str """
        ...

    @staticmethod
    def MessageReceived(): # -> 
        """ MessageReceived() """
        ...

    @staticmethod
    def QueueBackgroundWorkItem(workItem): # ->  # Not found arg types: {'workItem': 'Func'}
        """ QueueBackgroundWorkItem(workItem: Func[CancellationToken, Task])QueueBackgroundWorkItem(workItem: Action[CancellationToken]) """
        ...

    @staticmethod
    def RegisterObject(obj): # ->  # Not found arg types: {'obj': 'IRegisteredObject'}
        """ RegisterObject(obj: IRegisteredObject) """
        ...

    @staticmethod
    def RegisterVirtualPathProvider(virtualPathProvider): # ->  # Not found arg types: {'virtualPathProvider': 'VirtualPathProvider'}
        """ RegisterVirtualPathProvider(virtualPathProvider: VirtualPathProvider) """
        ...

    @staticmethod
    def SetCultures(virtualPath=None) -> IDisposable:
        """
        SetCultures() -> IDisposable
        SetCultures(virtualPath: str) -> IDisposable
        """
        ...

    @staticmethod
    def UnregisterObject(obj): # ->  # Not found arg types: {'obj': 'IRegisteredObject'}
        """ UnregisterObject(obj: IRegisteredObject) """
        ...

    StopListening = ...


class HostSecurityPolicyResolver: # skipped bases: <type 'object'>, <type 'object'>
    """ HostSecurityPolicyResolver() """
    def ResolvePolicy(self, evidence:Evidence): # -> HostSecurityPolicyResults
        """ ResolvePolicy(self: HostSecurityPolicyResolver, evidence: Evidence) -> HostSecurityPolicyResults """
        ...


class HostSecurityPolicyResults(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HostSecurityPolicyResults, values: AppDomainTrust (2), DefaultPolicy (0), FullTrust (1), Nothing (3) """
    AppDomainTrust: HostSecurityPolicyResults = ...
    DefaultPolicy: HostSecurityPolicyResults = ...
    FullTrust: HostSecurityPolicyResults = ...
    Nothing: HostSecurityPolicyResults = ...
    value__ = ...


class IAdphManager: # skipped bases: <type 'object'>
    """ no doc """
    def StartAppDomainProtocolListenerChannel(self, appId:str, protocolId:str, listenerChannelCallback): # ->  # Not found arg types: {'listenerChannelCallback': 'IListenerChannelCallback'}
        """ StartAppDomainProtocolListenerChannel(self: IAdphManager, appId: str, protocolId: str, listenerChannelCallback: IListenerChannelCallback) """
        ...

    def StopAppDomainProtocol(self, appId:str, protocolId:str, immediate:bool): # -> 
        """ StopAppDomainProtocol(self: IAdphManager, appId: str, protocolId: str, immediate: bool) """
        ...

    def StopAppDomainProtocolListenerChannel(self, appId:str, protocolId:str, listenerChannelId:int, immediate:bool): # -> 
        """ StopAppDomainProtocolListenerChannel(self: IAdphManager, appId: str, protocolId: str, listenerChannelId: int, immediate: bool) """
        ...


class IAppDomainFactory: # skipped bases: <type 'object'>
    """ no doc """
    def Create(self, module:str, typeName:str, appId:str, appPath:str, strUrlOfAppOrigin:str, iZone:int) -> object:
        """ Create(self: IAppDomainFactory, module: str, typeName: str, appId: str, appPath: str, strUrlOfAppOrigin: str, iZone: int) -> object """
        ...


class IAppDomainInfo: # skipped bases: <type 'object'>
    """ no doc """
    def GetId(self) -> str:
        """ GetId(self: IAppDomainInfo) -> str """
        ...

    def GetPhysicalPath(self) -> str:
        """ GetPhysicalPath(self: IAppDomainInfo) -> str """
        ...

    def GetSiteId(self) -> int:
        """ GetSiteId(self: IAppDomainInfo) -> int """
        ...

    def GetVirtualPath(self) -> str:
        """ GetVirtualPath(self: IAppDomainInfo) -> str """
        ...

    def IsIdle(self) -> bool:
        """ IsIdle(self: IAppDomainInfo) -> bool """
        ...


class IAppDomainInfoEnum: # skipped bases: <type 'object'>
    """ no doc """
    def Count(self) -> int:
        """ Count(self: IAppDomainInfoEnum) -> int """
        ...

    def GetData(self) -> IAppDomainInfo:
        """ GetData(self: IAppDomainInfoEnum) -> IAppDomainInfo """
        ...

    def MoveNext(self) -> bool:
        """ MoveNext(self: IAppDomainInfoEnum) -> bool """
        ...

    def Reset(self): # -> 
        """ Reset(self: IAppDomainInfoEnum) """
        ...


class IApplicationHost: # skipped bases: <type 'object'>
    """ no doc """
    def GetConfigMapPathFactory(self) -> IConfigMapPathFactory:
        """ GetConfigMapPathFactory(self: IApplicationHost) -> IConfigMapPathFactory """
        ...

    def GetConfigToken(self) -> IntPtr:
        """ GetConfigToken(self: IApplicationHost) -> IntPtr """
        ...

    def GetPhysicalPath(self) -> str:
        """ GetPhysicalPath(self: IApplicationHost) -> str """
        ...

    def GetSiteID(self) -> str:
        """ GetSiteID(self: IApplicationHost) -> str """
        ...

    def GetSiteName(self) -> str:
        """ GetSiteName(self: IApplicationHost) -> str """
        ...

    def GetVirtualPath(self) -> str:
        """ GetVirtualPath(self: IApplicationHost) -> str """
        ...

    def MessageReceived(self): # -> 
        """ MessageReceived(self: IApplicationHost) """
        ...


class IApplicationMonitor(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def Start(self): # -> 
        """ Start(self: IApplicationMonitor) """
        ...

    def Stop(self): # -> 
        """ Stop(self: IApplicationMonitor) """
        ...


class IApplicationPreloadManager: # skipped bases: <type 'object'>
    """ no doc """
    def SetApplicationPreloadState(self, context:str, appId:str, enabled:bool): # -> 
        """ SetApplicationPreloadState(self: IApplicationPreloadManager, context: str, appId: str, enabled: bool) """
        ...

    def SetApplicationPreloadUtil(self, preloadUtil): # ->  # Not found arg types: {'preloadUtil': 'IApplicationPreloadUtil'}
        """ SetApplicationPreloadUtil(self: IApplicationPreloadManager, preloadUtil: IApplicationPreloadUtil) """
        ...


class IApplicationPreloadUtil: # skipped bases: <type 'object'>
    """ no doc """
    def GetApplicationPreloadInfo(self, context, enabled, startupObjType, parametersForStartupObj) -> Tuple_[bool, str, Array]:
        """ GetApplicationPreloadInfo(self: IApplicationPreloadUtil, context: str) -> (bool, str, Array[str]) """
        ...

    def ReportApplicationPreloadFailure(self, context:str, errorCode:int, errorMessage:str): # -> 
        """ ReportApplicationPreloadFailure(self: IApplicationPreloadUtil, context: str, errorCode: int, errorMessage: str) """
        ...


class IAppManagerAppDomainFactory: # skipped bases: <type 'object'>
    """ no doc """
    def Create(self, appId:str, appPath:str) -> object:
        """ Create(self: IAppManagerAppDomainFactory, appId: str, appPath: str) -> object """
        ...

    def Stop(self): # -> 
        """ Stop(self: IAppManagerAppDomainFactory) """
        ...


class IISAPIRuntime: # skipped bases: <type 'object'>
    """ no doc """
    def DoGCCollect(self): # -> 
        """ DoGCCollect(self: IISAPIRuntime) """
        ...

    def ProcessRequest(self, ecb:IntPtr, useProcessModel:int) -> int:
        """ ProcessRequest(self: IISAPIRuntime, ecb: IntPtr, useProcessModel: int) -> int """
        ...

    def StartProcessing(self): # -> 
        """ StartProcessing(self: IISAPIRuntime) """
        ...

    def StopProcessing(self): # -> 
        """ StopProcessing(self: IISAPIRuntime) """
        ...


class IListenerChannelCallback: # skipped bases: <type 'object'>
    """ no doc """
    def GetBlob(self, buffer, bufferSize) -> Tuple_[Array, int]:
        """ GetBlob(self: IListenerChannelCallback, bufferSize: int) -> (Array[Byte], int) """
        ...

    def GetBlobLength(self) -> int:
        """ GetBlobLength(self: IListenerChannelCallback) -> int """
        ...

    def GetId(self) -> int:
        """ GetId(self: IListenerChannelCallback) -> int """
        ...

    def ReportMessageReceived(self): # -> 
        """ ReportMessageReceived(self: IListenerChannelCallback) """
        ...

    def ReportStarted(self): # -> 
        """ ReportStarted(self: IListenerChannelCallback) """
        ...

    def ReportStopped(self, hr:int): # -> 
        """ ReportStopped(self: IListenerChannelCallback, hr: int) """
        ...


class IPphManager: # skipped bases: <type 'object'>
    """ no doc """
    def StartProcessProtocolListenerChannel(self, protocolId:str, listenerChannelCallback:IListenerChannelCallback): # -> 
        """ StartProcessProtocolListenerChannel(self: IPphManager, protocolId: str, listenerChannelCallback: IListenerChannelCallback) """
        ...

    def StopProcessProtocol(self, protocolId:str, immediate:bool): # -> 
        """ StopProcessProtocol(self: IPphManager, protocolId: str, immediate: bool) """
        ...

    def StopProcessProtocolListenerChannel(self, protocolId:str, listenerChannelId:int, immediate:bool): # -> 
        """ StopProcessProtocolListenerChannel(self: IPphManager, protocolId: str, listenerChannelId: int, immediate: bool) """
        ...


class IProcessHost: # skipped bases: <type 'object'>
    """ no doc """
    def EnumerateAppDomains(self, appDomainInfoEnum) -> IAppDomainInfoEnum:
        """ EnumerateAppDomains(self: IProcessHost) -> IAppDomainInfoEnum """
        ...

    def Shutdown(self): # -> 
        """ Shutdown(self: IProcessHost) """
        ...

    def ShutdownApplication(self, appId:str): # -> 
        """ ShutdownApplication(self: IProcessHost, appId: str) """
        ...

    def StartApplication(self, appId, appPath, runtimeInterface) -> object:
        """ StartApplication(self: IProcessHost, appId: str, appPath: str) -> object """
        ...


class IProcessHostFactoryHelper: # skipped bases: <type 'object'>
    """ no doc """
    def GetProcessHost(self, functions) -> object: # Not found arg types: {'functions': 'IProcessHostSupportFunctions'}
        """ GetProcessHost(self: IProcessHostFactoryHelper, functions: IProcessHostSupportFunctions) -> object """
        ...


class IProcessHostIdleAndHealthCheck: # skipped bases: <type 'object'>
    """ no doc """
    def IsIdle(self) -> bool:
        """ IsIdle(self: IProcessHostIdleAndHealthCheck) -> bool """
        ...

    def Ping(self, callback): # ->  # Not found arg types: {'callback': 'IProcessPingCallback'}
        """ Ping(self: IProcessHostIdleAndHealthCheck, callback: IProcessPingCallback) """
        ...


class IProcessHostPreloadClient: # skipped bases: <type 'object'>
    """ no doc """
    def Preload(self, parameters:Array): # -> 
        """ Preload(self: IProcessHostPreloadClient, parameters: Array[str]) """
        ...


class IProcessHostSupportFunctions: # skipped bases: <type 'object'>
    """ no doc """
    def GetAppHostConfigFilename(self) -> str:
        """ GetAppHostConfigFilename(self: IProcessHostSupportFunctions) -> str """
        ...

    def GetApplicationProperties(self, appId, virtualPath, physicalPath, siteName, siteId) -> Tuple_[str, str, str, str]:
        """ GetApplicationProperties(self: IProcessHostSupportFunctions, appId: str) -> (str, str, str, str) """
        ...

    def GetConfigToken(self, appId:str) -> IntPtr:
        """ GetConfigToken(self: IProcessHostSupportFunctions, appId: str) -> IntPtr """
        ...

    def GetNativeConfigurationSystem(self) -> IntPtr:
        """ GetNativeConfigurationSystem(self: IProcessHostSupportFunctions) -> IntPtr """
        ...

    def GetRootWebConfigFilename(self) -> str:
        """ GetRootWebConfigFilename(self: IProcessHostSupportFunctions) -> str """
        ...

    def MapPath(self, appId, virtualPath, physicalPath) -> str:
        """ MapPath(self: IProcessHostSupportFunctions, appId: str, virtualPath: str) -> str """
        ...


class IProcessPingCallback: # skipped bases: <type 'object'>
    """ no doc """
    def Respond(self): # -> 
        """ Respond(self: IProcessPingCallback) """
        ...


class IRegisteredObject: # skipped bases: <type 'object'>
    """ no doc """
    def Stop(self, immediate:bool): # -> 
        """ Stop(self: IRegisteredObject, immediate: bool) """
        ...


class ISAPIRuntime(IISAPIRuntime2, IRegisteredObject, MarshalByRefObject, IISAPIRuntime): # skipped bases: <type 'object'>
    """ ISAPIRuntime() """
    pass

class IStopListeningRegisteredObject(IRegisteredObject): # skipped bases: <type 'object'>
    """ no doc """
    def StopListening(self): # -> 
        """ StopListening(self: IStopListeningRegisteredObject) """
        ...


class ISuspendibleRegisteredObject(IRegisteredObject): # skipped bases: <type 'object'>
    """ no doc """
    def Suspend(self) -> Action:
        """ Suspend(self: ISuspendibleRegisteredObject) -> Action """
        ...


class LowPhysicalMemoryInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ LowPhysicalMemoryInfo(currentPercentUsed: int, percentLimit: int) """
    @property
    def CurrentPercentUsed(self) -> int:
        """ Get: CurrentPercentUsed(self: LowPhysicalMemoryInfo) -> int """
        ...

    @property
    def PercentLimit(self) -> int:
        """ Get: PercentLimit(self: LowPhysicalMemoryInfo) -> int """
        ...

    @property
    def RequestGC(self) -> bool:
        """
        Get: RequestGC(self: LowPhysicalMemoryInfo) -> bool
        Set: RequestGC(self: LowPhysicalMemoryInfo) = value
        """
        ...



class LowPhysicalMemoryObserver(IObserver): # skipped bases: <type 'object'>
    """ LowPhysicalMemoryObserver() """
    pass

class ProcessHost(IPphManager, MarshalByRefObject, IProcessHostLite, ICustomRuntimeManager, IProcessSuspendListener, IProcessHostIdleAndHealthCheck, IProcessHost, IApplicationPreloadManager, IAdphManager): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ProcessHostFactoryHelper(MarshalByRefObject, IProcessHostFactoryHelper): # skipped bases: <type 'object'>
    """ ProcessHostFactoryHelper() """
    pass

class ProcessProtocolHandler(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    def StartListenerChannel(self, listenerChannelCallback:IListenerChannelCallback, AdphManager:IAdphManager): # -> 
        """ StartListenerChannel(self: ProcessProtocolHandler, listenerChannelCallback: IListenerChannelCallback, AdphManager: IAdphManager) """
        ...

    def StopListenerChannel(self, listenerChannelId:int, immediate:bool): # -> 
        """ StopListenerChannel(self: ProcessProtocolHandler, listenerChannelId: int, immediate: bool) """
        ...

    def StopProtocol(self, immediate:bool): # -> 
        """ StopProtocol(self: ProcessProtocolHandler, immediate: bool) """
        ...


class RecycleLimitInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ RecycleLimitInfo(currentPrivateBytes: Int64, recycleLimit: Int64, recycleLimitNearFrequency: RecycleLimitNotificationFrequency) """
    @property
    def CurrentPrivateBytes(self) -> Int64:
        """ Get: CurrentPrivateBytes(self: RecycleLimitInfo) -> Int64 """
        ...

    @property
    def RecycleLimit(self) -> Int64:
        """ Get: RecycleLimit(self: RecycleLimitInfo) -> Int64 """
        ...

    @property
    def RequestGC(self) -> bool:
        """
        Get: RequestGC(self: RecycleLimitInfo) -> bool
        Set: RequestGC(self: RecycleLimitInfo) = value
        """
        ...

    @property
    def TrimFrequency(self): # -> RecycleLimitNotificationFrequency
        """ Get: TrimFrequency(self: RecycleLimitInfo) -> RecycleLimitNotificationFrequency """
        ...



class RecycleLimitMonitor(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    def Dispose(self): # -> 
        """ Dispose(self: RecycleLimitMonitor) """
        ...

    def RecycleLimitMonitorSingleton(self, *args): #cannot find CLR method
        """ no doc """
        ...



class RecycleLimitNotificationFrequency(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RecycleLimitNotificationFrequency, values: High (0), Low (2), Medium (1) """
    High: RecycleLimitNotificationFrequency = ...
    Low: RecycleLimitNotificationFrequency = ...
    Medium: RecycleLimitNotificationFrequency = ...
    value__ = ...


class RecycleLimitObserver(IObserver): # skipped bases: <type 'object'>
    """ RecycleLimitObserver() """
    pass

class SimpleWorkerRequest(HttpWorkerRequest): # skipped bases: <type 'object'>
    """
    SimpleWorkerRequest(page: str, query: str, output: TextWriter)
    SimpleWorkerRequest(appVirtualDir: str, appPhysicalDir: str, page: str, query: str, output: TextWriter)
    """
    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type, page: str, query: str, output: TextWriter)
        __new__(cls: type, appVirtualDir: str, appPhysicalDir: str, page: str, query: str, output: TextWriter)
        """
        ...


class VirtualFileBase(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsDirectory(self) -> bool:
        """ Get: IsDirectory(self: VirtualFileBase) -> bool """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: VirtualFileBase) -> str """
        ...

    @property
    def VirtualPath(self) -> str:
        """ Get: VirtualPath(self: VirtualFileBase) -> str """
        ...



class VirtualDirectory(VirtualFileBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Children(self) -> IEnumerable:
        """ Get: Children(self: VirtualDirectory) -> IEnumerable """
        ...

    @property
    def Directories(self) -> IEnumerable:
        """ Get: Directories(self: VirtualDirectory) -> IEnumerable """
        ...

    @property
    def Files(self) -> IEnumerable:
        """ Get: Files(self: VirtualDirectory) -> IEnumerable """
        ...


    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, virtualPath: str) """
        ...


class VirtualFile(VirtualFileBase): # skipped bases: <type 'object'>
    """ no doc """
    def Open(self) -> Stream:
        """ Open(self: VirtualFile) -> Stream """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """ __new__(cls: type, virtualPath: str) """
        ...


class VirtualPathProvider(MarshalByRefObject): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Previous(self):
        ...


    def CombineVirtualPaths(self, basePath:str, relativePath:str) -> str:
        """ CombineVirtualPaths(self: VirtualPathProvider, basePath: str, relativePath: str) -> str """
        ...

    def DirectoryExists(self, virtualDir:str) -> bool:
        """ DirectoryExists(self: VirtualPathProvider, virtualDir: str) -> bool """
        ...

    def FileExists(self, virtualPath:str) -> bool:
        """ FileExists(self: VirtualPathProvider, virtualPath: str) -> bool """
        ...

    def GetCacheDependency(self, virtualPath:str, virtualPathDependencies:IEnumerable, utcStart:DateTime) -> CacheDependency:
        """ GetCacheDependency(self: VirtualPathProvider, virtualPath: str, virtualPathDependencies: IEnumerable, utcStart: DateTime) -> CacheDependency """
        ...

    def GetCacheKey(self, virtualPath:str) -> str:
        """ GetCacheKey(self: VirtualPathProvider, virtualPath: str) -> str """
        ...

    def GetDirectory(self, virtualDir:str) -> VirtualDirectory:
        """ GetDirectory(self: VirtualPathProvider, virtualDir: str) -> VirtualDirectory """
        ...

    def GetFile(self, virtualPath:str) -> VirtualFile:
        """ GetFile(self: VirtualPathProvider, virtualPath: str) -> VirtualFile """
        ...

    def GetFileHash(self, virtualPath:str, virtualPathDependencies:IEnumerable) -> str:
        """ GetFileHash(self: VirtualPathProvider, virtualPath: str, virtualPathDependencies: IEnumerable) -> str """
        ...

    def Initialize(self, *args): #cannot find CLR method
        """ Initialize(self: VirtualPathProvider) """
        ...

    @staticmethod
    def OpenFile(virtualPath:str) -> Stream:
        """ OpenFile(virtualPath: str) -> Stream """
        ...


