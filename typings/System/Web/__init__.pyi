# encoding: utf-8
# module System.Web calls itself Web
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Web.Extensions.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Web.DynamicData.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Web.Extensions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Web.Entity.Design, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Web.Services, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Web.Mobile, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Web.DynamicData, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Web.RegularExpressions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Web.Entity, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Web.ApplicationServices, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Diagnostics.STrace import TraceContext

from System import (Action, Array, AsyncCallback, Attribute, Char, DateTime, 
    Enum, EventArgs, Guid, IAsyncResult, ICloneable, IDisposable, 
    IServiceProvider, Int64, IntPtr, MulticastDelegate, TimeSpan, Type, Uri, 
    Version)

from System.CodeDom.Compiler import CompilerResults

from System.Collections import (ArrayList, CollectionBase, ICollection, 
    IDictionary, IEnumerator, IList)

from System.Collections.Specialized import (NameObjectCollectionBase, 
    NameValueCollection)

from System.ComponentModel import IComponent

from System.Configuration.Provider import ProviderBase, ProviderCollection

from System.Diagnostics import TraceListener

from System.Globalization import CultureInfo

from System.IO import BinaryReader, BinaryWriter, Stream, TextWriter

from System.Runtime.InteropServices import ExternalException

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from System.Security import (CodeAccessPermission, IPermission, 
    NamedPermissionSet)

from System.Security.Authentication.ExtendedProtection import ChannelBinding

from System.Security.Permissions import (CodeAccessSecurityAttribute, 
    IUnrestrictedPermission, PermissionState)

from System.Security.Principal import IPrincipal, WindowsIdentity

from System.Text import Encoding

from System.Threading import CancellationToken

from System.Threading.Tasks import Task

from System.Web.Caching import Cache

from System.Web.Instrumentation import PageInstrumentationService

from System.Web.Profile import ProfileBase

from System.Web.Routing import RequestContext

from System.Web.SessionState import (HttpSessionState, SessionStateBehavior, 
    SessionStateMode)

from System.Web.UI import (HtmlTextWriter, IFilterResolutionService, 
    IHierarchicalEnumerable, IHierarchyData, INavigateUIData)

from System.Web.WebSockets import AspNetWebSocketOptions

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (AsyncPreloadModeFlags, 
    BoundEvent, EndOfSendNotification, Func, HttpApplicationState, 
    HttpCacheRevalidation, HttpCacheValidateHandler, 
    HttpCacheVaryByContentEncodings, HttpCacheVaryByHeaders, 
    HttpCacheVaryByParams, HttpCapabilitiesBase, HttpContext, 
    HttpModuleCollection, HttpPostedFile, HttpPostedFileBase, HttpRequest, 
    HttpRequestBase, HttpResponse, HttpResponseBase, 
    HttpResponseSubstitutionCallback, HttpServerUtility, 
    HttpServerUtilityBase, HttpSessionStateBase, HttpStaticObjectsCollection, 
    HttpStaticObjectsCollectionBase, HttpValidationStatus, HttpWorkerRequest, 
    IHtmlString, IHttpAsyncHandler, IHttpModule, IPrincipalContainer, 
    IRequestCompletedNotifier, ISubscriptionToken, ISyncContext, 
    ITlsTokenBindingInfo, KeysCollection, ParserErrorCollection, 
    ProcessShutdownReason, ProcessStatus, ReadEntityBodyMode, 
    RequestNotification, SameSiteMode, SiteMapDataSource, 
    SiteMapDataSourceView, SiteMapHierarchicalDataSourceView, SiteMapNode, 
    SiteMapNodeCollection, SiteMapProvider, SiteMapProviderCollection, 
    TraceMode, UnvalidatedRequestValues, UnvalidatedRequestValuesBase, field#)
"""

# no functions
# classes

class ApplicationShutdownReason(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ApplicationShutdownReason, values: BinDirChangeOrDirectoryRename (6), BrowsersDirChangeOrDirectoryRename (7), BuildManagerChange (15), ChangeInGlobalAsax (2), ChangeInSecurityPolicyFile (5), CodeDirChangeOrDirectoryRename (8), ConfigurationChange (3), HostingEnvironment (1), HttpRuntimeClose (12), IdleTimeout (10), InitializationError (13), MaxRecompilationsReached (14), None (0), PhysicalApplicationPathChanged (11), ResourcesDirChangeOrDirectoryRename (9), UnloadAppDomainCalled (4) """
    BinDirChangeOrDirectoryRename: ApplicationShutdownReason = ...
    BrowsersDirChangeOrDirectoryRename: ApplicationShutdownReason = ...
    BuildManagerChange: ApplicationShutdownReason = ...
    ChangeInGlobalAsax: ApplicationShutdownReason = ...
    ChangeInSecurityPolicyFile: ApplicationShutdownReason = ...
    CodeDirChangeOrDirectoryRename: ApplicationShutdownReason = ...
    ConfigurationChange: ApplicationShutdownReason = ...
    HostingEnvironment: ApplicationShutdownReason = ...
    HttpRuntimeClose: ApplicationShutdownReason = ...
    IdleTimeout: ApplicationShutdownReason = ...
    InitializationError: ApplicationShutdownReason = ...
    MaxRecompilationsReached: ApplicationShutdownReason = ...
    PhysicalApplicationPathChanged: ApplicationShutdownReason = ...
    ResourcesDirChangeOrDirectoryRename: ApplicationShutdownReason = ...
    UnloadAppDomainCalled: ApplicationShutdownReason = ...
    value__ = ...


class AspNetHostingPermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    AspNetHostingPermission(state: PermissionState)
    AspNetHostingPermission(level: AspNetHostingPermissionLevel)
    """
    @property
    def Level(self) -> AspNetHostingPermissionLevel:
        """
        Get: Level(self: AspNetHostingPermission) -> AspNetHostingPermissionLevel
        Set: Level(self: AspNetHostingPermission) = value
        """
        ...


    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, level: AspNetHostingPermissionLevel)
        """
        ...


class AspNetHostingPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AspNetHostingPermissionAttribute(action: SecurityAction) """
    @property
    def Level(self) -> AspNetHostingPermissionLevel:
        """
        Get: Level(self: AspNetHostingPermissionAttribute) -> AspNetHostingPermissionLevel
        Set: Level(self: AspNetHostingPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: AspNetHostingPermissionAttribute) -> IPermission """
        ...


class AspNetHostingPermissionLevel(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum AspNetHostingPermissionLevel, values: High (500), Low (300), Medium (400), Minimal (200), None (100), Unrestricted (600) """
    High: AspNetHostingPermissionLevel = ...
    Low: AspNetHostingPermissionLevel = ...
    Medium: AspNetHostingPermissionLevel = ...
    Minimal: AspNetHostingPermissionLevel = ...
    Unrestricted: AspNetHostingPermissionLevel = ...
    value__ = ...


class BeginEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ BeginEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:EventArgs, cb:AsyncCallback, extraData:object, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: BeginEventHandler, sender: object, e: EventArgs, cb: AsyncCallback, extraData: object, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> IAsyncResult:
        """ EndInvoke(self: BeginEventHandler, result: IAsyncResult) -> IAsyncResult """
        ...

    def Invoke(self, sender:object, e:EventArgs, cb:AsyncCallback, extraData:object) -> IAsyncResult:
        """ Invoke(self: BeginEventHandler, sender: object, e: EventArgs, cb: AsyncCallback, extraData: object) -> IAsyncResult """
        ...


class DefaultHttpHandler(IHttpAsyncHandler): # skipped bases: <type 'IHttpHandler'>, <type 'object'>
    """ DefaultHttpHandler() """
    @property
    def Context(self):
        ...

    @property
    def ExecuteUrlHeaders(self):
        ...

    @property
    def IsReusable(self) -> bool:
        """ Get: IsReusable(self: DefaultHttpHandler) -> bool """
        ...


    def OnExecuteUrlPreconditionFailure(self): # -> 
        """ OnExecuteUrlPreconditionFailure(self: DefaultHttpHandler) """
        ...

    def OverrideExecuteUrlPath(self) -> str:
        """ OverrideExecuteUrlPath(self: DefaultHttpHandler) -> str """
        ...

    def ProcessRequest(self, context): # ->  # Not found arg types: {'context': 'HttpContext'}
        """ ProcessRequest(self: DefaultHttpHandler, context: HttpContext) """
        ...


class EndEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ EndEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, ar:IAsyncResult, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: EndEventHandler, ar: IAsyncResult, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: EndEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, ar:IAsyncResult): # -> 
        """ Invoke(self: EndEventHandler, ar: IAsyncResult) """
        ...


class EventHandlerTaskAsyncHelper: # skipped bases: <type 'object'>, <type 'object'>
    """ EventHandlerTaskAsyncHelper(handler: TaskEventHandler) """
    @property
    def BeginEventHandler(self) -> BeginEventHandler:
        """ Get: BeginEventHandler(self: EventHandlerTaskAsyncHelper) -> BeginEventHandler """
        ...

    @property
    def EndEventHandler(self) -> EndEventHandler:
        """ Get: EndEventHandler(self: EventHandlerTaskAsyncHelper) -> EndEventHandler """
        ...



class HtmlString(IHtmlString): # skipped bases: <type 'object'>
    """ HtmlString(value: str) """
    def ToString(self) -> str:
        """ ToString(self: HtmlString) -> str """
        ...


class IHttpHandler: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsReusable(self) -> bool:
        """ Get: IsReusable(self: IHttpHandler) -> bool """
        ...


    def ProcessRequest(self, context): # ->  # Not found arg types: {'context': 'HttpContext'}
        """ ProcessRequest(self: IHttpHandler, context: HttpContext) """
        ...


class IHttpAsyncHandler(IHttpHandler): # skipped bases: <type 'object'>
    """ no doc """
    def BeginProcessRequest(self, context, cb:AsyncCallback, extraData:object) -> IAsyncResult: # Not found arg types: {'context': 'HttpContext'}
        """ BeginProcessRequest(self: IHttpAsyncHandler, context: HttpContext, cb: AsyncCallback, extraData: object) -> IAsyncResult """
        ...

    def EndProcessRequest(self, result:IAsyncResult): # -> 
        """ EndProcessRequest(self: IHttpAsyncHandler, result: IAsyncResult) """
        ...


class HttpApplication(ISyncContext, IComponent, IRequestCompletedNotifier, IHttpAsyncHandler): # skipped bases: <type 'IDisposable'>, <type 'IHttpHandler'>, <type 'object'>
    """ HttpApplication() """
    @property
    def Application(self): # -> HttpApplicationState
        """ Get: Application(self: HttpApplication) -> HttpApplicationState """
        ...

    @property
    def Context(self): # -> HttpContext
        """ Get: Context(self: HttpApplication) -> HttpContext """
        ...

    @property
    def Events(self):
        ...

    @property
    def Modules(self): # -> HttpModuleCollection
        """ Get: Modules(self: HttpApplication) -> HttpModuleCollection """
        ...

    @property
    def Request(self): # -> HttpRequest
        """ Get: Request(self: HttpApplication) -> HttpRequest """
        ...

    @property
    def Response(self): # -> HttpResponse
        """ Get: Response(self: HttpApplication) -> HttpResponse """
        ...

    @property
    def Server(self): # -> HttpServerUtility
        """ Get: Server(self: HttpApplication) -> HttpServerUtility """
        ...

    @property
    def Session(self) -> HttpSessionState:
        """ Get: Session(self: HttpApplication) -> HttpSessionState """
        ...

    @property
    def User(self) -> IPrincipal:
        """ Get: User(self: HttpApplication) -> IPrincipal """
        ...


    def AddOnAcquireRequestStateAsync(self, *__args): # -> 
        """ AddOnAcquireRequestStateAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnAcquireRequestStateAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnAuthenticateRequestAsync(self, *__args): # -> 
        """ AddOnAuthenticateRequestAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnAuthenticateRequestAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnAuthorizeRequestAsync(self, *__args): # -> 
        """ AddOnAuthorizeRequestAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnAuthorizeRequestAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnBeginRequestAsync(self, *__args): # -> 
        """ AddOnBeginRequestAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnBeginRequestAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnEndRequestAsync(self, *__args): # -> 
        """ AddOnEndRequestAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnEndRequestAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnLogRequestAsync(self, *__args): # -> 
        """ AddOnLogRequestAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnLogRequestAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnMapRequestHandlerAsync(self, *__args): # -> 
        """ AddOnMapRequestHandlerAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnMapRequestHandlerAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnPostAcquireRequestStateAsync(self, *__args): # -> 
        """ AddOnPostAcquireRequestStateAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnPostAcquireRequestStateAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnPostAuthenticateRequestAsync(self, *__args): # -> 
        """ AddOnPostAuthenticateRequestAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnPostAuthenticateRequestAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnPostAuthorizeRequestAsync(self, *__args): # -> 
        """ AddOnPostAuthorizeRequestAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnPostAuthorizeRequestAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnPostLogRequestAsync(self, *__args): # -> 
        """ AddOnPostLogRequestAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnPostLogRequestAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnPostMapRequestHandlerAsync(self, *__args): # -> 
        """ AddOnPostMapRequestHandlerAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnPostMapRequestHandlerAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnPostReleaseRequestStateAsync(self, *__args): # -> 
        """ AddOnPostReleaseRequestStateAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnPostReleaseRequestStateAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnPostRequestHandlerExecuteAsync(self, *__args): # -> 
        """ AddOnPostRequestHandlerExecuteAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnPostRequestHandlerExecuteAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnPostResolveRequestCacheAsync(self, *__args): # -> 
        """ AddOnPostResolveRequestCacheAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnPostResolveRequestCacheAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnPostUpdateRequestCacheAsync(self, *__args): # -> 
        """ AddOnPostUpdateRequestCacheAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnPostUpdateRequestCacheAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnPreRequestHandlerExecuteAsync(self, *__args): # -> 
        """ AddOnPreRequestHandlerExecuteAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnPreRequestHandlerExecuteAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnReleaseRequestStateAsync(self, *__args): # -> 
        """ AddOnReleaseRequestStateAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnReleaseRequestStateAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnResolveRequestCacheAsync(self, *__args): # -> 
        """ AddOnResolveRequestCacheAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnResolveRequestCacheAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def AddOnUpdateRequestCacheAsync(self, *__args): # -> 
        """ AddOnUpdateRequestCacheAsync(self: HttpApplication, bh: BeginEventHandler, eh: EndEventHandler)AddOnUpdateRequestCacheAsync(self: HttpApplication, beginHandler: BeginEventHandler, endHandler: EndEventHandler, state: object) """
        ...

    def CompleteRequest(self): # -> 
        """ CompleteRequest(self: HttpApplication) """
        ...

    def Dispose(self): # -> 
        """ Dispose(self: HttpApplication) """
        ...

    def GetOutputCacheProviderName(self, context) -> str: # Not found arg types: {'context': 'HttpContext'}
        """ GetOutputCacheProviderName(self: HttpApplication, context: HttpContext) -> str """
        ...

    def GetVaryByCustomString(self, context, custom:str) -> str: # Not found arg types: {'context': 'HttpContext'}
        """ GetVaryByCustomString(self: HttpApplication, context: HttpContext, custom: str) -> str """
        ...

    def Init(self): # -> 
        """ Init(self: HttpApplication) """
        ...

    def OnExecuteRequestStep(self, callback:Action): # -> 
        """ OnExecuteRequestStep(self: HttpApplication, callback: Action[HttpContextBase, Action]) """
        ...

    @staticmethod
    def RegisterModule(moduleType:Type): # -> 
        """ RegisterModule(moduleType: Type) """
        ...

    AcquireRequestState = ...
    AuthenticateRequest = ...
    AuthorizeRequest = ...
    BeginRequest = ...
    Disposed = ...
    EndRequest = ...
    Error = ...
    LogRequest = ...
    MapRequestHandler = ...
    PostAcquireRequestState = ...
    PostAuthenticateRequest = ...
    PostAuthorizeRequest = ...
    PostLogRequest = ...
    PostMapRequestHandler = ...
    PostReleaseRequestState = ...
    PostRequestHandlerExecute = ...
    PostResolveRequestCache = ...
    PostUpdateRequestCache = ...
    PreRequestHandlerExecute = ...
    PreSendRequestContent = ...
    PreSendRequestHeaders = ...
    ReleaseRequestState = ...
    RequestCompleted = ...
    ResolveRequestCache = ...
    UpdateRequestCache = ...


class HttpApplicationState(NameObjectCollectionBase): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: HttpApplicationState) -> Array[str] """
        ...

    @property
    def Contents(self) -> HttpApplicationState:
        """ Get: Contents(self: HttpApplicationState) -> HttpApplicationState """
        ...

    @property
    def StaticObjects(self): # -> HttpStaticObjectsCollection
        """ Get: StaticObjects(self: HttpApplicationState) -> HttpStaticObjectsCollection """
        ...


    def Add(self, name:str, value:object): # -> 
        """ Add(self: HttpApplicationState, name: str, value: object) """
        ...

    def Clear(self): # -> 
        """ Clear(self: HttpApplicationState) """
        ...

    def Get(self, *__args:str) -> object:
        """
        Get(self: HttpApplicationState, name: str) -> object
        Get(self: HttpApplicationState, index: int) -> object
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: HttpApplicationState, index: int) -> str """
        ...

    def Lock(self): # -> 
        """ Lock(self: HttpApplicationState) """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: HttpApplicationState, name: str) """
        ...

    def RemoveAll(self): # -> 
        """ RemoveAll(self: HttpApplicationState) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: HttpApplicationState, index: int) """
        ...

    def Set(self, name:str, value:object): # -> 
        """ Set(self: HttpApplicationState, name: str, value: object) """
        ...

    def UnLock(self): # -> 
        """ UnLock(self: HttpApplicationState) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class HttpApplicationStateBase(NameObjectCollectionBase): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: HttpApplicationStateBase) -> Array[str] """
        ...

    @property
    def Contents(self) -> HttpApplicationStateBase:
        """ Get: Contents(self: HttpApplicationStateBase) -> HttpApplicationStateBase """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: HttpApplicationStateBase) -> bool """
        ...

    @property
    def StaticObjects(self): # -> HttpStaticObjectsCollectionBase
        """ Get: StaticObjects(self: HttpApplicationStateBase) -> HttpStaticObjectsCollectionBase """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: HttpApplicationStateBase) -> object """
        ...


    def Add(self, name:str, value:object): # -> 
        """ Add(self: HttpApplicationStateBase, name: str, value: object) """
        ...

    def Clear(self): # -> 
        """ Clear(self: HttpApplicationStateBase) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: HttpApplicationStateBase, array: Array, index: int) """
        ...

    def Get(self, *__args:int) -> object:
        """
        Get(self: HttpApplicationStateBase, index: int) -> object
        Get(self: HttpApplicationStateBase, name: str) -> object
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: HttpApplicationStateBase, index: int) -> str """
        ...

    def Lock(self): # -> 
        """ Lock(self: HttpApplicationStateBase) """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: HttpApplicationStateBase, name: str) """
        ...

    def RemoveAll(self): # -> 
        """ RemoveAll(self: HttpApplicationStateBase) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: HttpApplicationStateBase, index: int) """
        ...

    def Set(self, name:str, value:object): # -> 
        """ Set(self: HttpApplicationStateBase, name: str, value: object) """
        ...

    def UnLock(self): # -> 
        """ UnLock(self: HttpApplicationStateBase) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class HttpApplicationStateWrapper(HttpApplicationStateBase): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ HttpApplicationStateWrapper(httpApplicationState: HttpApplicationState) """
    @property
    def Keys(self): # -> KeysCollection
        """ Get: Keys(self: HttpApplicationStateWrapper) -> KeysCollection """
        ...


    def __new__(cls, httpApplicationState:HttpApplicationState) -> Self:
        """ __new__(cls: type, httpApplicationState: HttpApplicationState) """
        ...


class HttpBrowserCapabilities(HttpCapabilitiesBase): # skipped bases: <type 'IFilterResolutionService'>, <type 'object'>
    """ HttpBrowserCapabilities() """
    pass

class HttpBrowserCapabilitiesBase(IFilterResolutionService): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ActiveXControls(self) -> bool:
        """ Get: ActiveXControls(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def Adapters(self) -> IDictionary:
        """ Get: Adapters(self: HttpBrowserCapabilitiesBase) -> IDictionary """
        ...

    @property
    def AOL(self) -> bool:
        """ Get: AOL(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def BackgroundSounds(self) -> bool:
        """ Get: BackgroundSounds(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def Beta(self) -> bool:
        """ Get: Beta(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def Browser(self) -> str:
        """ Get: Browser(self: HttpBrowserCapabilitiesBase) -> str """
        ...

    @property
    def Browsers(self) -> ArrayList:
        """ Get: Browsers(self: HttpBrowserCapabilitiesBase) -> ArrayList """
        ...

    @property
    def CanCombineFormsInDeck(self) -> bool:
        """ Get: CanCombineFormsInDeck(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def CanInitiateVoiceCall(self) -> bool:
        """ Get: CanInitiateVoiceCall(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def CanRenderAfterInputOrSelectElement(self) -> bool:
        """ Get: CanRenderAfterInputOrSelectElement(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def CanRenderEmptySelects(self) -> bool:
        """ Get: CanRenderEmptySelects(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def CanRenderInputAndSelectElementsTogether(self) -> bool:
        """ Get: CanRenderInputAndSelectElementsTogether(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def CanRenderMixedSelects(self) -> bool:
        """ Get: CanRenderMixedSelects(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def CanRenderOneventAndPrevElementsTogether(self) -> bool:
        """ Get: CanRenderOneventAndPrevElementsTogether(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def CanRenderPostBackCards(self) -> bool:
        """ Get: CanRenderPostBackCards(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def CanRenderSetvarZeroWithMultiSelectionList(self) -> bool:
        """ Get: CanRenderSetvarZeroWithMultiSelectionList(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def CanSendMail(self) -> bool:
        """ Get: CanSendMail(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def Capabilities(self) -> IDictionary:
        """
        Get: Capabilities(self: HttpBrowserCapabilitiesBase) -> IDictionary
        Set: Capabilities(self: HttpBrowserCapabilitiesBase) = value
        """
        ...

    @property
    def CDF(self) -> bool:
        """ Get: CDF(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def ClrVersion(self) -> Version:
        """ Get: ClrVersion(self: HttpBrowserCapabilitiesBase) -> Version """
        ...

    @property
    def Cookies(self) -> bool:
        """ Get: Cookies(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def Crawler(self) -> bool:
        """ Get: Crawler(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def DefaultSubmitButtonLimit(self) -> int:
        """ Get: DefaultSubmitButtonLimit(self: HttpBrowserCapabilitiesBase) -> int """
        ...

    @property
    def EcmaScriptVersion(self) -> Version:
        """ Get: EcmaScriptVersion(self: HttpBrowserCapabilitiesBase) -> Version """
        ...

    @property
    def Frames(self) -> bool:
        """ Get: Frames(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def GatewayMajorVersion(self) -> int:
        """ Get: GatewayMajorVersion(self: HttpBrowserCapabilitiesBase) -> int """
        ...

    @property
    def GatewayMinorVersion(self) -> float:
        """ Get: GatewayMinorVersion(self: HttpBrowserCapabilitiesBase) -> float """
        ...

    @property
    def GatewayVersion(self) -> str:
        """ Get: GatewayVersion(self: HttpBrowserCapabilitiesBase) -> str """
        ...

    @property
    def HasBackButton(self) -> bool:
        """ Get: HasBackButton(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def HidesRightAlignedMultiselectScrollbars(self) -> bool:
        """ Get: HidesRightAlignedMultiselectScrollbars(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def HtmlTextWriter(self) -> str:
        """
        Get: HtmlTextWriter(self: HttpBrowserCapabilitiesBase) -> str
        Set: HtmlTextWriter(self: HttpBrowserCapabilitiesBase) = value
        """
        ...

    @property
    def Id(self) -> str:
        """ Get: Id(self: HttpBrowserCapabilitiesBase) -> str """
        ...

    @property
    def InputType(self) -> str:
        """ Get: InputType(self: HttpBrowserCapabilitiesBase) -> str """
        ...

    @property
    def IsColor(self) -> bool:
        """ Get: IsColor(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def IsMobileDevice(self) -> bool:
        """ Get: IsMobileDevice(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def JavaApplets(self) -> bool:
        """ Get: JavaApplets(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def JScriptVersion(self) -> Version:
        """ Get: JScriptVersion(self: HttpBrowserCapabilitiesBase) -> Version """
        ...

    @property
    def MajorVersion(self) -> int:
        """ Get: MajorVersion(self: HttpBrowserCapabilitiesBase) -> int """
        ...

    @property
    def MaximumHrefLength(self) -> int:
        """ Get: MaximumHrefLength(self: HttpBrowserCapabilitiesBase) -> int """
        ...

    @property
    def MaximumRenderedPageSize(self) -> int:
        """ Get: MaximumRenderedPageSize(self: HttpBrowserCapabilitiesBase) -> int """
        ...

    @property
    def MaximumSoftkeyLabelLength(self) -> int:
        """ Get: MaximumSoftkeyLabelLength(self: HttpBrowserCapabilitiesBase) -> int """
        ...

    @property
    def MinorVersion(self) -> float:
        """ Get: MinorVersion(self: HttpBrowserCapabilitiesBase) -> float """
        ...

    @property
    def MinorVersionString(self) -> str:
        """ Get: MinorVersionString(self: HttpBrowserCapabilitiesBase) -> str """
        ...

    @property
    def MobileDeviceManufacturer(self) -> str:
        """ Get: MobileDeviceManufacturer(self: HttpBrowserCapabilitiesBase) -> str """
        ...

    @property
    def MobileDeviceModel(self) -> str:
        """ Get: MobileDeviceModel(self: HttpBrowserCapabilitiesBase) -> str """
        ...

    @property
    def MSDomVersion(self) -> Version:
        """ Get: MSDomVersion(self: HttpBrowserCapabilitiesBase) -> Version """
        ...

    @property
    def NumberOfSoftkeys(self) -> int:
        """ Get: NumberOfSoftkeys(self: HttpBrowserCapabilitiesBase) -> int """
        ...

    @property
    def Platform(self) -> str:
        """ Get: Platform(self: HttpBrowserCapabilitiesBase) -> str """
        ...

    @property
    def PreferredImageMime(self) -> str:
        """ Get: PreferredImageMime(self: HttpBrowserCapabilitiesBase) -> str """
        ...

    @property
    def PreferredRenderingMime(self) -> str:
        """ Get: PreferredRenderingMime(self: HttpBrowserCapabilitiesBase) -> str """
        ...

    @property
    def PreferredRenderingType(self) -> str:
        """ Get: PreferredRenderingType(self: HttpBrowserCapabilitiesBase) -> str """
        ...

    @property
    def PreferredRequestEncoding(self) -> str:
        """ Get: PreferredRequestEncoding(self: HttpBrowserCapabilitiesBase) -> str """
        ...

    @property
    def PreferredResponseEncoding(self) -> str:
        """ Get: PreferredResponseEncoding(self: HttpBrowserCapabilitiesBase) -> str """
        ...

    @property
    def RendersBreakBeforeWmlSelectAndInput(self) -> bool:
        """ Get: RendersBreakBeforeWmlSelectAndInput(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RendersBreaksAfterHtmlLists(self) -> bool:
        """ Get: RendersBreaksAfterHtmlLists(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RendersBreaksAfterWmlAnchor(self) -> bool:
        """ Get: RendersBreaksAfterWmlAnchor(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RendersBreaksAfterWmlInput(self) -> bool:
        """ Get: RendersBreaksAfterWmlInput(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RendersWmlDoAcceptsInline(self) -> bool:
        """ Get: RendersWmlDoAcceptsInline(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RendersWmlSelectsAsMenuCards(self) -> bool:
        """ Get: RendersWmlSelectsAsMenuCards(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RequiredMetaTagNameValue(self) -> str:
        """ Get: RequiredMetaTagNameValue(self: HttpBrowserCapabilitiesBase) -> str """
        ...

    @property
    def RequiresAttributeColonSubstitution(self) -> bool:
        """ Get: RequiresAttributeColonSubstitution(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresContentTypeMetaTag(self) -> bool:
        """ Get: RequiresContentTypeMetaTag(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresControlStateInSession(self) -> bool:
        """ Get: RequiresControlStateInSession(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresDBCSCharacter(self) -> bool:
        """ Get: RequiresDBCSCharacter(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresHtmlAdaptiveErrorReporting(self) -> bool:
        """ Get: RequiresHtmlAdaptiveErrorReporting(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresLeadingPageBreak(self) -> bool:
        """ Get: RequiresLeadingPageBreak(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresNoBreakInFormatting(self) -> bool:
        """ Get: RequiresNoBreakInFormatting(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresOutputOptimization(self) -> bool:
        """ Get: RequiresOutputOptimization(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresPhoneNumbersAsPlainText(self) -> bool:
        """ Get: RequiresPhoneNumbersAsPlainText(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresSpecialViewStateEncoding(self) -> bool:
        """ Get: RequiresSpecialViewStateEncoding(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresUniqueFilePathSuffix(self) -> bool:
        """ Get: RequiresUniqueFilePathSuffix(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresUniqueHtmlCheckboxNames(self) -> bool:
        """ Get: RequiresUniqueHtmlCheckboxNames(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresUniqueHtmlInputNames(self) -> bool:
        """ Get: RequiresUniqueHtmlInputNames(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def RequiresUrlEncodedPostfieldValues(self) -> bool:
        """ Get: RequiresUrlEncodedPostfieldValues(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def ScreenBitDepth(self) -> int:
        """ Get: ScreenBitDepth(self: HttpBrowserCapabilitiesBase) -> int """
        ...

    @property
    def ScreenCharactersHeight(self) -> int:
        """ Get: ScreenCharactersHeight(self: HttpBrowserCapabilitiesBase) -> int """
        ...

    @property
    def ScreenCharactersWidth(self) -> int:
        """ Get: ScreenCharactersWidth(self: HttpBrowserCapabilitiesBase) -> int """
        ...

    @property
    def ScreenPixelsHeight(self) -> int:
        """ Get: ScreenPixelsHeight(self: HttpBrowserCapabilitiesBase) -> int """
        ...

    @property
    def ScreenPixelsWidth(self) -> int:
        """ Get: ScreenPixelsWidth(self: HttpBrowserCapabilitiesBase) -> int """
        ...

    @property
    def SupportsAccesskeyAttribute(self) -> bool:
        """ Get: SupportsAccesskeyAttribute(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsBodyColor(self) -> bool:
        """ Get: SupportsBodyColor(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsBold(self) -> bool:
        """ Get: SupportsBold(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsCacheControlMetaTag(self) -> bool:
        """ Get: SupportsCacheControlMetaTag(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsCallback(self) -> bool:
        """ Get: SupportsCallback(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsCss(self) -> bool:
        """ Get: SupportsCss(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsDivAlign(self) -> bool:
        """ Get: SupportsDivAlign(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsDivNoWrap(self) -> bool:
        """ Get: SupportsDivNoWrap(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsEmptyStringInCookieValue(self) -> bool:
        """ Get: SupportsEmptyStringInCookieValue(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsFontColor(self) -> bool:
        """ Get: SupportsFontColor(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsFontName(self) -> bool:
        """ Get: SupportsFontName(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsFontSize(self) -> bool:
        """ Get: SupportsFontSize(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsImageSubmit(self) -> bool:
        """ Get: SupportsImageSubmit(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsIModeSymbols(self) -> bool:
        """ Get: SupportsIModeSymbols(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsInputIStyle(self) -> bool:
        """ Get: SupportsInputIStyle(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsInputMode(self) -> bool:
        """ Get: SupportsInputMode(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsItalic(self) -> bool:
        """ Get: SupportsItalic(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsJPhoneMultiMediaAttributes(self) -> bool:
        """ Get: SupportsJPhoneMultiMediaAttributes(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsJPhoneSymbols(self) -> bool:
        """ Get: SupportsJPhoneSymbols(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsQueryStringInFormAction(self) -> bool:
        """ Get: SupportsQueryStringInFormAction(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsRedirectWithCookie(self) -> bool:
        """ Get: SupportsRedirectWithCookie(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsSelectMultiple(self) -> bool:
        """ Get: SupportsSelectMultiple(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsUncheck(self) -> bool:
        """ Get: SupportsUncheck(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def SupportsXmlHttp(self) -> bool:
        """ Get: SupportsXmlHttp(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def Tables(self) -> bool:
        """ Get: Tables(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def TagWriter(self) -> Type:
        """ Get: TagWriter(self: HttpBrowserCapabilitiesBase) -> Type """
        ...

    @property
    def Type(self) -> str:
        """ Get: Type(self: HttpBrowserCapabilitiesBase) -> str """
        ...

    @property
    def UseOptimizedCacheKey(self) -> bool:
        """ Get: UseOptimizedCacheKey(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def VBScript(self) -> bool:
        """ Get: VBScript(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def Version(self) -> str:
        """ Get: Version(self: HttpBrowserCapabilitiesBase) -> str """
        ...

    @property
    def W3CDomVersion(self) -> Version:
        """ Get: W3CDomVersion(self: HttpBrowserCapabilitiesBase) -> Version """
        ...

    @property
    def Win16(self) -> bool:
        """ Get: Win16(self: HttpBrowserCapabilitiesBase) -> bool """
        ...

    @property
    def Win32(self) -> bool:
        """ Get: Win32(self: HttpBrowserCapabilitiesBase) -> bool """
        ...


    def AddBrowser(self, browserName:str): # -> 
        """ AddBrowser(self: HttpBrowserCapabilitiesBase, browserName: str) """
        ...

    def CreateHtmlTextWriter(self, w:TextWriter) -> HtmlTextWriter:
        """ CreateHtmlTextWriter(self: HttpBrowserCapabilitiesBase, w: TextWriter) -> HtmlTextWriter """
        ...

    def DisableOptimizedCacheKey(self): # -> 
        """ DisableOptimizedCacheKey(self: HttpBrowserCapabilitiesBase) """
        ...

    def GetClrVersions(self) -> Array:
        """ GetClrVersions(self: HttpBrowserCapabilitiesBase) -> Array[Version] """
        ...

    def IsBrowser(self, browserName:str) -> bool:
        """ IsBrowser(self: HttpBrowserCapabilitiesBase, browserName: str) -> bool """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class HttpBrowserCapabilitiesWrapper(HttpBrowserCapabilitiesBase): # skipped bases: <type 'IFilterResolutionService'>, <type 'object'>
    """ HttpBrowserCapabilitiesWrapper(httpBrowserCapabilities: HttpBrowserCapabilities) """
    def __new__(cls, httpBrowserCapabilities:HttpBrowserCapabilities) -> Self:
        """ __new__(cls: type, httpBrowserCapabilities: HttpBrowserCapabilities) """
        ...


class HttpCacheability(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HttpCacheability, values: NoCache (1), Private (2), Public (4), Server (3), ServerAndNoCache (3), ServerAndPrivate (5) """
    NoCache: HttpCacheability = ...
    Private: HttpCacheability = ...
    Public: HttpCacheability = ...
    Server: HttpCacheability = ...
    ServerAndNoCache: HttpCacheability = ...
    ServerAndPrivate: HttpCacheability = ...
    value__ = ...


class HttpCachePolicy: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def UtcTimestampCreated(self) -> DateTime:
        """
        Get: UtcTimestampCreated(self: HttpCachePolicy) -> DateTime
        Set: UtcTimestampCreated(self: HttpCachePolicy) = value
        """
        ...

    @property
    def VaryByContentEncodings(self): # -> HttpCacheVaryByContentEncodings
        """ Get: VaryByContentEncodings(self: HttpCachePolicy) -> HttpCacheVaryByContentEncodings """
        ...

    @property
    def VaryByHeaders(self): # -> HttpCacheVaryByHeaders
        """ Get: VaryByHeaders(self: HttpCachePolicy) -> HttpCacheVaryByHeaders """
        ...

    @property
    def VaryByParams(self): # -> HttpCacheVaryByParams
        """ Get: VaryByParams(self: HttpCachePolicy) -> HttpCacheVaryByParams """
        ...


    def AddValidationCallback(self, handler, data:object): # ->  # Not found arg types: {'handler': 'HttpCacheValidateHandler'}
        """ AddValidationCallback(self: HttpCachePolicy, handler: HttpCacheValidateHandler, data: object) """
        ...

    def AppendCacheExtension(self, extension:str): # -> 
        """ AppendCacheExtension(self: HttpCachePolicy, extension: str) """
        ...

    def GetCacheability(self) -> HttpCacheability:
        """ GetCacheability(self: HttpCachePolicy) -> HttpCacheability """
        ...

    def GetCacheExtensions(self) -> str:
        """ GetCacheExtensions(self: HttpCachePolicy) -> str """
        ...

    def GetETag(self) -> str:
        """ GetETag(self: HttpCachePolicy) -> str """
        ...

    def GetETagFromFileDependencies(self) -> bool:
        """ GetETagFromFileDependencies(self: HttpCachePolicy) -> bool """
        ...

    def GetExpires(self) -> DateTime:
        """ GetExpires(self: HttpCachePolicy) -> DateTime """
        ...

    def GetIgnoreRangeRequests(self) -> bool:
        """ GetIgnoreRangeRequests(self: HttpCachePolicy) -> bool """
        ...

    def GetLastModifiedFromFileDependencies(self) -> bool:
        """ GetLastModifiedFromFileDependencies(self: HttpCachePolicy) -> bool """
        ...

    def GetMaxAge(self) -> TimeSpan:
        """ GetMaxAge(self: HttpCachePolicy) -> TimeSpan """
        ...

    def GetNoServerCaching(self) -> bool:
        """ GetNoServerCaching(self: HttpCachePolicy) -> bool """
        ...

    def GetNoStore(self) -> bool:
        """ GetNoStore(self: HttpCachePolicy) -> bool """
        ...

    def GetNoTransforms(self) -> bool:
        """ GetNoTransforms(self: HttpCachePolicy) -> bool """
        ...

    def GetOmitVaryStar(self) -> int:
        """ GetOmitVaryStar(self: HttpCachePolicy) -> int """
        ...

    def GetProxyMaxAge(self) -> TimeSpan:
        """ GetProxyMaxAge(self: HttpCachePolicy) -> TimeSpan """
        ...

    def GetRevalidation(self): # -> HttpCacheRevalidation
        """ GetRevalidation(self: HttpCachePolicy) -> HttpCacheRevalidation """
        ...

    def GetUtcLastModified(self) -> DateTime:
        """ GetUtcLastModified(self: HttpCachePolicy) -> DateTime """
        ...

    def GetVaryByCustom(self) -> str:
        """ GetVaryByCustom(self: HttpCachePolicy) -> str """
        ...

    def HasSlidingExpiration(self) -> bool:
        """ HasSlidingExpiration(self: HttpCachePolicy) -> bool """
        ...

    def IsModified(self) -> bool:
        """ IsModified(self: HttpCachePolicy) -> bool """
        ...

    def IsValidUntilExpires(self) -> bool:
        """ IsValidUntilExpires(self: HttpCachePolicy) -> bool """
        ...

    def SetAllowResponseInBrowserHistory(self, allow:bool): # -> 
        """ SetAllowResponseInBrowserHistory(self: HttpCachePolicy, allow: bool) """
        ...

    def SetCacheability(self, cacheability:HttpCacheability, field:str = ...): # -> 
        """ SetCacheability(self: HttpCachePolicy, cacheability: HttpCacheability)SetCacheability(self: HttpCachePolicy, cacheability: HttpCacheability, field: str) """
        ...

    def SetETag(self, etag:str): # -> 
        """ SetETag(self: HttpCachePolicy, etag: str) """
        ...

    def SetETagFromFileDependencies(self): # -> 
        """ SetETagFromFileDependencies(self: HttpCachePolicy) """
        ...

    def SetExpires(self, date:DateTime): # -> 
        """ SetExpires(self: HttpCachePolicy, date: DateTime) """
        ...

    def SetLastModified(self, date:DateTime): # -> 
        """ SetLastModified(self: HttpCachePolicy, date: DateTime) """
        ...

    def SetLastModifiedFromFileDependencies(self): # -> 
        """ SetLastModifiedFromFileDependencies(self: HttpCachePolicy) """
        ...

    def SetMaxAge(self, delta:TimeSpan): # -> 
        """ SetMaxAge(self: HttpCachePolicy, delta: TimeSpan) """
        ...

    def SetNoServerCaching(self): # -> 
        """ SetNoServerCaching(self: HttpCachePolicy) """
        ...

    def SetNoStore(self): # -> 
        """ SetNoStore(self: HttpCachePolicy) """
        ...

    def SetNoTransforms(self): # -> 
        """ SetNoTransforms(self: HttpCachePolicy) """
        ...

    def SetOmitVaryStar(self, omit:bool): # -> 
        """ SetOmitVaryStar(self: HttpCachePolicy, omit: bool) """
        ...

    def SetProxyMaxAge(self, delta:TimeSpan): # -> 
        """ SetProxyMaxAge(self: HttpCachePolicy, delta: TimeSpan) """
        ...

    def SetRevalidation(self, revalidation): # ->  # Not found arg types: {'revalidation': 'HttpCacheRevalidation'}
        """ SetRevalidation(self: HttpCachePolicy, revalidation: HttpCacheRevalidation) """
        ...

    def SetSlidingExpiration(self, slide:bool): # -> 
        """ SetSlidingExpiration(self: HttpCachePolicy, slide: bool) """
        ...

    def SetValidUntilExpires(self, validUntilExpires:bool): # -> 
        """ SetValidUntilExpires(self: HttpCachePolicy, validUntilExpires: bool) """
        ...

    def SetVaryByCustom(self, custom:str): # -> 
        """ SetVaryByCustom(self: HttpCachePolicy, custom: str) """
        ...


class HttpCachePolicyBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def VaryByContentEncodings(self): # -> HttpCacheVaryByContentEncodings
        """ Get: VaryByContentEncodings(self: HttpCachePolicyBase) -> HttpCacheVaryByContentEncodings """
        ...

    @property
    def VaryByHeaders(self): # -> HttpCacheVaryByHeaders
        """ Get: VaryByHeaders(self: HttpCachePolicyBase) -> HttpCacheVaryByHeaders """
        ...

    @property
    def VaryByParams(self): # -> HttpCacheVaryByParams
        """ Get: VaryByParams(self: HttpCachePolicyBase) -> HttpCacheVaryByParams """
        ...


    def AddValidationCallback(self, handler, data:object): # ->  # Not found arg types: {'handler': 'HttpCacheValidateHandler'}
        """ AddValidationCallback(self: HttpCachePolicyBase, handler: HttpCacheValidateHandler, data: object) """
        ...

    def AppendCacheExtension(self, extension:str): # -> 
        """ AppendCacheExtension(self: HttpCachePolicyBase, extension: str) """
        ...

    def SetAllowResponseInBrowserHistory(self, allow:bool): # -> 
        """ SetAllowResponseInBrowserHistory(self: HttpCachePolicyBase, allow: bool) """
        ...

    def SetCacheability(self, cacheability:HttpCacheability, field:str = ...): # -> 
        """ SetCacheability(self: HttpCachePolicyBase, cacheability: HttpCacheability)SetCacheability(self: HttpCachePolicyBase, cacheability: HttpCacheability, field: str) """
        ...

    def SetETag(self, etag:str): # -> 
        """ SetETag(self: HttpCachePolicyBase, etag: str) """
        ...

    def SetETagFromFileDependencies(self): # -> 
        """ SetETagFromFileDependencies(self: HttpCachePolicyBase) """
        ...

    def SetExpires(self, date:DateTime): # -> 
        """ SetExpires(self: HttpCachePolicyBase, date: DateTime) """
        ...

    def SetLastModified(self, date:DateTime): # -> 
        """ SetLastModified(self: HttpCachePolicyBase, date: DateTime) """
        ...

    def SetLastModifiedFromFileDependencies(self): # -> 
        """ SetLastModifiedFromFileDependencies(self: HttpCachePolicyBase) """
        ...

    def SetMaxAge(self, delta:TimeSpan): # -> 
        """ SetMaxAge(self: HttpCachePolicyBase, delta: TimeSpan) """
        ...

    def SetNoServerCaching(self): # -> 
        """ SetNoServerCaching(self: HttpCachePolicyBase) """
        ...

    def SetNoStore(self): # -> 
        """ SetNoStore(self: HttpCachePolicyBase) """
        ...

    def SetNoTransforms(self): # -> 
        """ SetNoTransforms(self: HttpCachePolicyBase) """
        ...

    def SetOmitVaryStar(self, omit:bool): # -> 
        """ SetOmitVaryStar(self: HttpCachePolicyBase, omit: bool) """
        ...

    def SetProxyMaxAge(self, delta:TimeSpan): # -> 
        """ SetProxyMaxAge(self: HttpCachePolicyBase, delta: TimeSpan) """
        ...

    def SetRevalidation(self, revalidation): # ->  # Not found arg types: {'revalidation': 'HttpCacheRevalidation'}
        """ SetRevalidation(self: HttpCachePolicyBase, revalidation: HttpCacheRevalidation) """
        ...

    def SetSlidingExpiration(self, slide:bool): # -> 
        """ SetSlidingExpiration(self: HttpCachePolicyBase, slide: bool) """
        ...

    def SetValidUntilExpires(self, validUntilExpires:bool): # -> 
        """ SetValidUntilExpires(self: HttpCachePolicyBase, validUntilExpires: bool) """
        ...

    def SetVaryByCustom(self, custom:str): # -> 
        """ SetVaryByCustom(self: HttpCachePolicyBase, custom: str) """
        ...


class HttpCachePolicyWrapper(HttpCachePolicyBase): # skipped bases: <type 'object'>
    """ HttpCachePolicyWrapper(httpCachePolicy: HttpCachePolicy) """
    def __new__(cls, httpCachePolicy:HttpCachePolicy) -> Self:
        """ __new__(cls: type, httpCachePolicy: HttpCachePolicy) """
        ...


class HttpCacheRevalidation(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HttpCacheRevalidation, values: AllCaches (1), None (3), ProxyCaches (2) """
    AllCaches: HttpCacheRevalidation = ...
    ProxyCaches: HttpCacheRevalidation = ...
    value__ = ...


class HttpCacheValidateHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ HttpCacheValidateHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, context, data:object, validationStatus, callback:AsyncCallback, object:object): # -> Tuple_[IAsyncResult, HttpValidationStatus] # Not found arg types: {'validationStatus': 'HttpValidationStatus', 'context': 'HttpContext'}
        """ BeginInvoke(self: HttpCacheValidateHandler, context: HttpContext, data: object, validationStatus: HttpValidationStatus, callback: AsyncCallback, object: object) -> (IAsyncResult, HttpValidationStatus) """
        ...

    def EndInvoke(self, validationStatus, result:IAsyncResult): # -> HttpValidationStatus # Not found arg types: {'validationStatus': 'HttpValidationStatus'}
        """ EndInvoke(self: HttpCacheValidateHandler, validationStatus: HttpValidationStatus, result: IAsyncResult) -> HttpValidationStatus """
        ...

    def Invoke(self, context, data:object, validationStatus): # -> HttpValidationStatus # Not found arg types: {'validationStatus': 'HttpValidationStatus', 'context': 'HttpContext'}
        """ Invoke(self: HttpCacheValidateHandler, context: HttpContext, data: object, validationStatus: HttpValidationStatus) -> HttpValidationStatus """
        ...


class HttpCacheVaryByContentEncodings: # skipped bases: <type 'object'>, <type 'object'>
    """ HttpCacheVaryByContentEncodings() """
    def GetContentEncodings(self) -> Array:
        """ GetContentEncodings(self: HttpCacheVaryByContentEncodings) -> Array[str] """
        ...

    def SetContentEncodings(self, contentEncodings:Array): # -> 
        """ SetContentEncodings(self: HttpCacheVaryByContentEncodings, contentEncodings: Array[str]) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class HttpCacheVaryByHeaders: # skipped bases: <type 'object'>, <type 'object'>
    """ HttpCacheVaryByHeaders() """
    @property
    def AcceptTypes(self) -> bool:
        """
        Get: AcceptTypes(self: HttpCacheVaryByHeaders) -> bool
        Set: AcceptTypes(self: HttpCacheVaryByHeaders) = value
        """
        ...

    @property
    def UserAgent(self) -> bool:
        """
        Get: UserAgent(self: HttpCacheVaryByHeaders) -> bool
        Set: UserAgent(self: HttpCacheVaryByHeaders) = value
        """
        ...

    @property
    def UserCharSet(self) -> bool:
        """
        Get: UserCharSet(self: HttpCacheVaryByHeaders) -> bool
        Set: UserCharSet(self: HttpCacheVaryByHeaders) = value
        """
        ...

    @property
    def UserLanguage(self) -> bool:
        """
        Get: UserLanguage(self: HttpCacheVaryByHeaders) -> bool
        Set: UserLanguage(self: HttpCacheVaryByHeaders) = value
        """
        ...


    def GetHeaders(self) -> Array:
        """ GetHeaders(self: HttpCacheVaryByHeaders) -> Array[str] """
        ...

    def SetHeaders(self, headers:Array): # -> 
        """ SetHeaders(self: HttpCacheVaryByHeaders, headers: Array[str]) """
        ...

    def VaryByUnspecifiedParameters(self): # -> 
        """ VaryByUnspecifiedParameters(self: HttpCacheVaryByHeaders) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class HttpCacheVaryByParams: # skipped bases: <type 'object'>, <type 'object'>
    """ HttpCacheVaryByParams() """
    @property
    def IgnoreParams(self) -> bool:
        """
        Get: IgnoreParams(self: HttpCacheVaryByParams) -> bool
        Set: IgnoreParams(self: HttpCacheVaryByParams) = value
        """
        ...


    def GetParams(self) -> Array:
        """ GetParams(self: HttpCacheVaryByParams) -> Array[str] """
        ...

    def SetParams(self, parameters:Array): # -> 
        """ SetParams(self: HttpCacheVaryByParams, parameters: Array[str]) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class HttpClientCertificate(NameValueCollection): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def BinaryIssuer(self) -> Array:
        """ Get: BinaryIssuer(self: HttpClientCertificate) -> Array[Byte] """
        ...

    @property
    def CertEncoding(self) -> int:
        """ Get: CertEncoding(self: HttpClientCertificate) -> int """
        ...

    @property
    def Certificate(self) -> Array:
        """ Get: Certificate(self: HttpClientCertificate) -> Array[Byte] """
        ...

    @property
    def Cookie(self) -> str:
        """ Get: Cookie(self: HttpClientCertificate) -> str """
        ...

    @property
    def Flags(self) -> int:
        """ Get: Flags(self: HttpClientCertificate) -> int """
        ...

    @property
    def IsPresent(self) -> bool:
        """ Get: IsPresent(self: HttpClientCertificate) -> bool """
        ...

    @property
    def Issuer(self) -> str:
        """ Get: Issuer(self: HttpClientCertificate) -> str """
        ...

    @property
    def IsValid(self) -> bool:
        """ Get: IsValid(self: HttpClientCertificate) -> bool """
        ...

    @property
    def KeySize(self) -> int:
        """ Get: KeySize(self: HttpClientCertificate) -> int """
        ...

    @property
    def PublicKey(self) -> Array:
        """ Get: PublicKey(self: HttpClientCertificate) -> Array[Byte] """
        ...

    @property
    def SecretKeySize(self) -> int:
        """ Get: SecretKeySize(self: HttpClientCertificate) -> int """
        ...

    @property
    def SerialNumber(self) -> str:
        """ Get: SerialNumber(self: HttpClientCertificate) -> str """
        ...

    @property
    def ServerIssuer(self) -> str:
        """ Get: ServerIssuer(self: HttpClientCertificate) -> str """
        ...

    @property
    def ServerSubject(self) -> str:
        """ Get: ServerSubject(self: HttpClientCertificate) -> str """
        ...

    @property
    def Subject(self) -> str:
        """ Get: Subject(self: HttpClientCertificate) -> str """
        ...

    @property
    def ValidFrom(self) -> DateTime:
        """ Get: ValidFrom(self: HttpClientCertificate) -> DateTime """
        ...

    @property
    def ValidUntil(self) -> DateTime:
        """ Get: ValidUntil(self: HttpClientCertificate) -> DateTime """
        ...



class HttpException(ExternalException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    HttpException()
    HttpException(message: str)
    HttpException(message: str, hr: int)
    HttpException(message: str, innerException: Exception)
    HttpException(httpCode: int, message: str, innerException: Exception)
    HttpException(httpCode: int, message: str)
    HttpException(httpCode: int, message: str, hr: int)
    """
    @property
    def WebEventCode(self) -> int:
        """ Get: WebEventCode(self: HttpException) -> int """
        ...


    @staticmethod
    def CreateFromLastError(message:str) -> HttpException:
        """ CreateFromLastError(message: str) -> HttpException """
        ...

    def GetHtmlErrorMessage(self) -> str:
        """ GetHtmlErrorMessage(self: HttpException) -> str """
        ...

    def GetHttpCode(self) -> int:
        """ GetHttpCode(self: HttpException) -> int """
        ...

    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: HttpException, info: SerializationInfo, context: StreamingContext) """
        ...

    SerializeObjectState = ...


class HttpCompileException(HttpException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    HttpCompileException()
    HttpCompileException(message: str)
    HttpCompileException(message: str, innerException: Exception)
    HttpCompileException(results: CompilerResults, sourceCode: str)
    """
    @property
    def Results(self) -> CompilerResults:
        """ Get: Results(self: HttpCompileException) -> CompilerResults """
        ...

    @property
    def SourceCode(self) -> str:
        """ Get: SourceCode(self: HttpCompileException) -> str """
        ...


    SerializeObjectState = ...


class HttpContext(IServiceProvider, IPrincipalContainer): # skipped bases: <type 'object'>
    """
    HttpContext(request: HttpRequest, response: HttpResponse)
    HttpContext(wr: HttpWorkerRequest)
    """
    @property
    def AllErrors(self) -> Array:
        """ Get: AllErrors(self: HttpContext) -> Array[Exception] """
        ...

    @property
    def AllowAsyncDuringSyncStages(self) -> bool:
        """
        Get: AllowAsyncDuringSyncStages(self: HttpContext) -> bool
        Set: AllowAsyncDuringSyncStages(self: HttpContext) = value
        """
        ...

    @property
    def Application(self) -> HttpApplicationState:
        """ Get: Application(self: HttpContext) -> HttpApplicationState """
        ...

    @property
    def ApplicationInstance(self) -> HttpApplication:
        """
        Get: ApplicationInstance(self: HttpContext) -> HttpApplication
        Set: ApplicationInstance(self: HttpContext) = value
        """
        ...

    @property
    def AsyncPreloadMode(self): # -> AsyncPreloadModeFlags
        """
        Get: AsyncPreloadMode(self: HttpContext) -> AsyncPreloadModeFlags
        Set: AsyncPreloadMode(self: HttpContext) = value
        """
        ...

    @property
    def Cache(self) -> Cache:
        """ Get: Cache(self: HttpContext) -> Cache """
        ...

    @property
    def Current(self) -> HttpContext:
        """
        Get: Current() -> HttpContext
        Set: Current() = value
        """
        ...

    @property
    def CurrentHandler(self) -> IHttpHandler:
        """ Get: CurrentHandler(self: HttpContext) -> IHttpHandler """
        ...

    @property
    def CurrentNotification(self): # -> RequestNotification
        """ Get: CurrentNotification(self: HttpContext) -> RequestNotification """
        ...

    @property
    def Error(self) -> Exception:
        """ Get: Error(self: HttpContext) -> Exception """
        ...

    @property
    def Handler(self) -> IHttpHandler:
        """
        Get: Handler(self: HttpContext) -> IHttpHandler
        Set: Handler(self: HttpContext) = value
        """
        ...

    @property
    def IsCustomErrorEnabled(self) -> bool:
        """ Get: IsCustomErrorEnabled(self: HttpContext) -> bool """
        ...

    @property
    def IsDebuggingEnabled(self) -> bool:
        """ Get: IsDebuggingEnabled(self: HttpContext) -> bool """
        ...

    @property
    def IsPostNotification(self) -> bool:
        """ Get: IsPostNotification(self: HttpContext) -> bool """
        ...

    @property
    def IsWebSocketRequest(self) -> bool:
        """ Get: IsWebSocketRequest(self: HttpContext) -> bool """
        ...

    @property
    def IsWebSocketRequestUpgrading(self) -> bool:
        """ Get: IsWebSocketRequestUpgrading(self: HttpContext) -> bool """
        ...

    @property
    def Items(self) -> IDictionary:
        """ Get: Items(self: HttpContext) -> IDictionary """
        ...

    @property
    def PageInstrumentation(self) -> PageInstrumentationService:
        """ Get: PageInstrumentation(self: HttpContext) -> PageInstrumentationService """
        ...

    @property
    def PreviousHandler(self) -> IHttpHandler:
        """ Get: PreviousHandler(self: HttpContext) -> IHttpHandler """
        ...

    @property
    def Profile(self) -> ProfileBase:
        """ Get: Profile(self: HttpContext) -> ProfileBase """
        ...

    @property
    def Request(self): # -> HttpRequest
        """ Get: Request(self: HttpContext) -> HttpRequest """
        ...

    @property
    def Response(self): # -> HttpResponse
        """ Get: Response(self: HttpContext) -> HttpResponse """
        ...

    @property
    def Server(self): # -> HttpServerUtility
        """ Get: Server(self: HttpContext) -> HttpServerUtility """
        ...

    @property
    def Session(self) -> HttpSessionState:
        """ Get: Session(self: HttpContext) -> HttpSessionState """
        ...

    @property
    def SkipAuthorization(self) -> bool:
        """
        Get: SkipAuthorization(self: HttpContext) -> bool
        Set: SkipAuthorization(self: HttpContext) = value
        """
        ...

    @property
    def ThreadAbortOnTimeout(self) -> bool:
        """
        Get: ThreadAbortOnTimeout(self: HttpContext) -> bool
        Set: ThreadAbortOnTimeout(self: HttpContext) = value
        """
        ...

    @property
    def Timestamp(self) -> DateTime:
        """ Get: Timestamp(self: HttpContext) -> DateTime """
        ...

    @property
    def Trace(self) -> TraceContext:
        """ Get: Trace(self: HttpContext) -> TraceContext """
        ...

    @property
    def User(self) -> IPrincipal:
        """
        Get: User(self: HttpContext) -> IPrincipal
        Set: User(self: HttpContext) = value
        """
        ...

    @property
    def WebSocketNegotiatedProtocol(self) -> str:
        """ Get: WebSocketNegotiatedProtocol(self: HttpContext) -> str """
        ...

    @property
    def WebSocketRequestedProtocols(self) -> IList:
        """ Get: WebSocketRequestedProtocols(self: HttpContext) -> IList[str] """
        ...


    def AcceptWebSocketRequest(self, userFunc, options:AspNetWebSocketOptions = ...): # ->  # Not found arg types: {'userFunc': 'Func'}
        """ AcceptWebSocketRequest(self: HttpContext, userFunc: Func[AspNetWebSocketContext, Task])AcceptWebSocketRequest(self: HttpContext, userFunc: Func[AspNetWebSocketContext, Task], options: AspNetWebSocketOptions) """
        ...

    def AddError(self, errorInfo:Exception): # -> 
        """ AddError(self: HttpContext, errorInfo: Exception) """
        ...

    def AddOnRequestCompleted(self, callback:Action): # -> ISubscriptionToken
        """ AddOnRequestCompleted(self: HttpContext, callback: Action[HttpContext]) -> ISubscriptionToken """
        ...

    def ClearError(self): # -> 
        """ ClearError(self: HttpContext) """
        ...

    def DisposeOnPipelineCompleted(self, target:IDisposable): # -> ISubscriptionToken
        """ DisposeOnPipelineCompleted(self: HttpContext, target: IDisposable) -> ISubscriptionToken """
        ...

    @staticmethod
    def GetAppConfig(name:str) -> object:
        """ GetAppConfig(name: str) -> object """
        ...

    def GetConfig(self, name:str) -> object:
        """ GetConfig(self: HttpContext, name: str) -> object """
        ...

    @staticmethod
    def GetGlobalResourceObject(classKey:str, resourceKey:str, culture:CultureInfo = ...) -> object:
        """
        GetGlobalResourceObject(classKey: str, resourceKey: str) -> object
        GetGlobalResourceObject(classKey: str, resourceKey: str, culture: CultureInfo) -> object
        """
        ...

    @staticmethod
    def GetLocalResourceObject(virtualPath:str, resourceKey:str, culture:CultureInfo = ...) -> object:
        """
        GetLocalResourceObject(virtualPath: str, resourceKey: str) -> object
        GetLocalResourceObject(virtualPath: str, resourceKey: str, culture: CultureInfo) -> object
        """
        ...

    def GetSection(self, sectionName:str) -> object:
        """ GetSection(self: HttpContext, sectionName: str) -> object """
        ...

    def RemapHandler(self, handler:IHttpHandler): # -> 
        """ RemapHandler(self: HttpContext, handler: IHttpHandler) """
        ...

    def RewritePath(self, *__args:str): # -> 
        """ RewritePath(self: HttpContext, path: str)RewritePath(self: HttpContext, path: str, rebaseClientPath: bool)RewritePath(self: HttpContext, filePath: str, pathInfo: str, queryString: str)RewritePath(self: HttpContext, filePath: str, pathInfo: str, queryString: str, setClientFilePath: bool) """
        ...

    def SetSessionStateBehavior(self, sessionStateBehavior:SessionStateBehavior): # -> 
        """ SetSessionStateBehavior(self: HttpContext, sessionStateBehavior: SessionStateBehavior) """
        ...


class HttpContextBase(IServiceProvider): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AllErrors(self) -> Array:
        """ Get: AllErrors(self: HttpContextBase) -> Array[Exception] """
        ...

    @property
    def AllowAsyncDuringSyncStages(self) -> bool:
        """
        Get: AllowAsyncDuringSyncStages(self: HttpContextBase) -> bool
        Set: AllowAsyncDuringSyncStages(self: HttpContextBase) = value
        """
        ...

    @property
    def Application(self) -> HttpApplicationStateBase:
        """ Get: Application(self: HttpContextBase) -> HttpApplicationStateBase """
        ...

    @property
    def ApplicationInstance(self) -> HttpApplication:
        """
        Get: ApplicationInstance(self: HttpContextBase) -> HttpApplication
        Set: ApplicationInstance(self: HttpContextBase) = value
        """
        ...

    @property
    def AsyncPreloadMode(self): # -> AsyncPreloadModeFlags
        """
        Get: AsyncPreloadMode(self: HttpContextBase) -> AsyncPreloadModeFlags
        Set: AsyncPreloadMode(self: HttpContextBase) = value
        """
        ...

    @property
    def Cache(self) -> Cache:
        """ Get: Cache(self: HttpContextBase) -> Cache """
        ...

    @property
    def CurrentHandler(self) -> IHttpHandler:
        """ Get: CurrentHandler(self: HttpContextBase) -> IHttpHandler """
        ...

    @property
    def CurrentNotification(self): # -> RequestNotification
        """ Get: CurrentNotification(self: HttpContextBase) -> RequestNotification """
        ...

    @property
    def Error(self) -> Exception:
        """ Get: Error(self: HttpContextBase) -> Exception """
        ...

    @property
    def Handler(self) -> IHttpHandler:
        """
        Get: Handler(self: HttpContextBase) -> IHttpHandler
        Set: Handler(self: HttpContextBase) = value
        """
        ...

    @property
    def IsCustomErrorEnabled(self) -> bool:
        """ Get: IsCustomErrorEnabled(self: HttpContextBase) -> bool """
        ...

    @property
    def IsDebuggingEnabled(self) -> bool:
        """ Get: IsDebuggingEnabled(self: HttpContextBase) -> bool """
        ...

    @property
    def IsPostNotification(self) -> bool:
        """ Get: IsPostNotification(self: HttpContextBase) -> bool """
        ...

    @property
    def IsWebSocketRequest(self) -> bool:
        """ Get: IsWebSocketRequest(self: HttpContextBase) -> bool """
        ...

    @property
    def IsWebSocketRequestUpgrading(self) -> bool:
        """ Get: IsWebSocketRequestUpgrading(self: HttpContextBase) -> bool """
        ...

    @property
    def Items(self) -> IDictionary:
        """ Get: Items(self: HttpContextBase) -> IDictionary """
        ...

    @property
    def PageInstrumentation(self) -> PageInstrumentationService:
        """ Get: PageInstrumentation(self: HttpContextBase) -> PageInstrumentationService """
        ...

    @property
    def PreviousHandler(self) -> IHttpHandler:
        """ Get: PreviousHandler(self: HttpContextBase) -> IHttpHandler """
        ...

    @property
    def Profile(self) -> ProfileBase:
        """ Get: Profile(self: HttpContextBase) -> ProfileBase """
        ...

    @property
    def Request(self): # -> HttpRequestBase
        """ Get: Request(self: HttpContextBase) -> HttpRequestBase """
        ...

    @property
    def Response(self): # -> HttpResponseBase
        """ Get: Response(self: HttpContextBase) -> HttpResponseBase """
        ...

    @property
    def Server(self): # -> HttpServerUtilityBase
        """ Get: Server(self: HttpContextBase) -> HttpServerUtilityBase """
        ...

    @property
    def Session(self): # -> HttpSessionStateBase
        """ Get: Session(self: HttpContextBase) -> HttpSessionStateBase """
        ...

    @property
    def SkipAuthorization(self) -> bool:
        """
        Get: SkipAuthorization(self: HttpContextBase) -> bool
        Set: SkipAuthorization(self: HttpContextBase) = value
        """
        ...

    @property
    def ThreadAbortOnTimeout(self) -> bool:
        """
        Get: ThreadAbortOnTimeout(self: HttpContextBase) -> bool
        Set: ThreadAbortOnTimeout(self: HttpContextBase) = value
        """
        ...

    @property
    def Timestamp(self) -> DateTime:
        """ Get: Timestamp(self: HttpContextBase) -> DateTime """
        ...

    @property
    def Trace(self) -> TraceContext:
        """ Get: Trace(self: HttpContextBase) -> TraceContext """
        ...

    @property
    def User(self) -> IPrincipal:
        """
        Get: User(self: HttpContextBase) -> IPrincipal
        Set: User(self: HttpContextBase) = value
        """
        ...

    @property
    def WebSocketNegotiatedProtocol(self) -> str:
        """ Get: WebSocketNegotiatedProtocol(self: HttpContextBase) -> str """
        ...

    @property
    def WebSocketRequestedProtocols(self) -> IList:
        """ Get: WebSocketRequestedProtocols(self: HttpContextBase) -> IList[str] """
        ...


    def AcceptWebSocketRequest(self, userFunc, options:AspNetWebSocketOptions = ...): # ->  # Not found arg types: {'userFunc': 'Func'}
        """ AcceptWebSocketRequest(self: HttpContextBase, userFunc: Func[AspNetWebSocketContext, Task])AcceptWebSocketRequest(self: HttpContextBase, userFunc: Func[AspNetWebSocketContext, Task], options: AspNetWebSocketOptions) """
        ...

    def AddError(self, errorInfo:Exception): # -> 
        """ AddError(self: HttpContextBase, errorInfo: Exception) """
        ...

    def AddOnRequestCompleted(self, callback:Action): # -> ISubscriptionToken
        """ AddOnRequestCompleted(self: HttpContextBase, callback: Action[HttpContextBase]) -> ISubscriptionToken """
        ...

    def ClearError(self): # -> 
        """ ClearError(self: HttpContextBase) """
        ...

    def DisposeOnPipelineCompleted(self, target:IDisposable): # -> ISubscriptionToken
        """ DisposeOnPipelineCompleted(self: HttpContextBase, target: IDisposable) -> ISubscriptionToken """
        ...

    def GetGlobalResourceObject(self, classKey:str, resourceKey:str, culture:CultureInfo = ...) -> object:
        """
        GetGlobalResourceObject(self: HttpContextBase, classKey: str, resourceKey: str) -> object
        GetGlobalResourceObject(self: HttpContextBase, classKey: str, resourceKey: str, culture: CultureInfo) -> object
        """
        ...

    def GetLocalResourceObject(self, virtualPath:str, resourceKey:str, culture:CultureInfo = ...) -> object:
        """
        GetLocalResourceObject(self: HttpContextBase, virtualPath: str, resourceKey: str) -> object
        GetLocalResourceObject(self: HttpContextBase, virtualPath: str, resourceKey: str, culture: CultureInfo) -> object
        """
        ...

    def GetSection(self, sectionName:str) -> object:
        """ GetSection(self: HttpContextBase, sectionName: str) -> object """
        ...

    def RemapHandler(self, handler:IHttpHandler): # -> 
        """ RemapHandler(self: HttpContextBase, handler: IHttpHandler) """
        ...

    def RewritePath(self, *__args:str): # -> 
        """ RewritePath(self: HttpContextBase, path: str)RewritePath(self: HttpContextBase, path: str, rebaseClientPath: bool)RewritePath(self: HttpContextBase, filePath: str, pathInfo: str, queryString: str)RewritePath(self: HttpContextBase, filePath: str, pathInfo: str, queryString: str, setClientFilePath: bool) """
        ...

    def SetSessionStateBehavior(self, sessionStateBehavior:SessionStateBehavior): # -> 
        """ SetSessionStateBehavior(self: HttpContextBase, sessionStateBehavior: SessionStateBehavior) """
        ...


class HttpContextWrapper(HttpContextBase): # skipped bases: <type 'IServiceProvider'>, <type 'object'>
    """ HttpContextWrapper(httpContext: HttpContext) """
    def __new__(cls, httpContext:HttpContext) -> Self:
        """ __new__(cls: type, httpContext: HttpContext) """
        ...


class HttpCookie: # skipped bases: <type 'object'>, <type 'object'>
    """
    HttpCookie(name: str)
    HttpCookie(name: str, value: str)
    """
    @property
    def Domain(self) -> str:
        """
        Get: Domain(self: HttpCookie) -> str
        Set: Domain(self: HttpCookie) = value
        """
        ...

    @property
    def Expires(self) -> DateTime:
        """
        Get: Expires(self: HttpCookie) -> DateTime
        Set: Expires(self: HttpCookie) = value
        """
        ...

    @property
    def HasKeys(self) -> bool:
        """ Get: HasKeys(self: HttpCookie) -> bool """
        ...

    @property
    def HttpOnly(self) -> bool:
        """
        Get: HttpOnly(self: HttpCookie) -> bool
        Set: HttpOnly(self: HttpCookie) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: HttpCookie) -> str
        Set: Name(self: HttpCookie) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: HttpCookie) -> str
        Set: Path(self: HttpCookie) = value
        """
        ...

    @property
    def SameSite(self): # -> SameSiteMode
        """
        Get: SameSite(self: HttpCookie) -> SameSiteMode
        Set: SameSite(self: HttpCookie) = value
        """
        ...

    @property
    def Secure(self) -> bool:
        """
        Get: Secure(self: HttpCookie) -> bool
        Set: Secure(self: HttpCookie) = value
        """
        ...

    @property
    def Shareable(self) -> bool:
        """
        Get: Shareable(self: HttpCookie) -> bool
        Set: Shareable(self: HttpCookie) = value
        """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: HttpCookie) -> str
        Set: Value(self: HttpCookie) = value
        """
        ...

    @property
    def Values(self) -> NameValueCollection:
        """ Get: Values(self: HttpCookie) -> NameValueCollection """
        ...


    @staticmethod
    def TryParse(input, result) -> Tuple_[bool, HttpCookie]:
        """ TryParse(input: str) -> (bool, HttpCookie) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class HttpCookieCollection(NameObjectCollectionBase): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ HttpCookieCollection() """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: HttpCookieCollection) -> Array[str] """
        ...


    def Add(self, cookie:HttpCookie): # -> 
        """ Add(self: HttpCookieCollection, cookie: HttpCookie) """
        ...

    def Clear(self): # -> 
        """ Clear(self: HttpCookieCollection) """
        ...

    def CopyTo(self, dest:Array, index:int): # -> 
        """ CopyTo(self: HttpCookieCollection, dest: Array, index: int) """
        ...

    def Get(self, *__args:str) -> HttpCookie:
        """
        Get(self: HttpCookieCollection, name: str) -> HttpCookie
        Get(self: HttpCookieCollection, index: int) -> HttpCookie
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: HttpCookieCollection, index: int) -> str """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: HttpCookieCollection, name: str) """
        ...

    def Set(self, cookie:HttpCookie): # -> 
        """ Set(self: HttpCookieCollection, cookie: HttpCookie) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class HttpCookieMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HttpCookieMode, values: AutoDetect (2), UseCookies (1), UseDeviceProfile (3), UseUri (0) """
    AutoDetect: HttpCookieMode = ...
    UseCookies: HttpCookieMode = ...
    UseDeviceProfile: HttpCookieMode = ...
    UseUri: HttpCookieMode = ...
    value__ = ...


class HttpFileCollection(NameObjectCollectionBase): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: HttpFileCollection) -> Array[str] """
        ...


    def CopyTo(self, dest:Array, index:int): # -> 
        """ CopyTo(self: HttpFileCollection, dest: Array, index: int) """
        ...

    def Get(self, *__args:str): # -> HttpPostedFile
        """
        Get(self: HttpFileCollection, name: str) -> HttpPostedFile
        Get(self: HttpFileCollection, index: int) -> HttpPostedFile
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: HttpFileCollection, index: int) -> str """
        ...

    def GetMultiple(self, name:str) -> IList:
        """ GetMultiple(self: HttpFileCollection, name: str) -> IList[HttpPostedFile] """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class HttpFileCollectionBase(NameObjectCollectionBase): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: HttpFileCollectionBase) -> Array[str] """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: HttpFileCollectionBase) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: HttpFileCollectionBase) -> object """
        ...


    def CopyTo(self, dest:Array, index:int): # -> 
        """ CopyTo(self: HttpFileCollectionBase, dest: Array, index: int) """
        ...

    def Get(self, *__args:int): # -> HttpPostedFileBase
        """
        Get(self: HttpFileCollectionBase, index: int) -> HttpPostedFileBase
        Get(self: HttpFileCollectionBase, name: str) -> HttpPostedFileBase
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: HttpFileCollectionBase, index: int) -> str """
        ...

    def GetMultiple(self, name:str) -> IList:
        """ GetMultiple(self: HttpFileCollectionBase, name: str) -> IList[HttpPostedFileBase] """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class HttpFileCollectionWrapper(HttpFileCollectionBase): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ HttpFileCollectionWrapper(httpFileCollection: HttpFileCollection) """
    @property
    def Keys(self): # -> KeysCollection
        """ Get: Keys(self: HttpFileCollectionWrapper) -> KeysCollection """
        ...


    def __new__(cls, httpFileCollection:HttpFileCollection) -> Self:
        """ __new__(cls: type, httpFileCollection: HttpFileCollection) """
        ...


class HttpModuleCollection(NameObjectCollectionBase): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def AllKeys(self) -> Array:
        """ Get: AllKeys(self: HttpModuleCollection) -> Array[str] """
        ...


    def CopyTo(self, dest:Array, index:int): # -> 
        """ CopyTo(self: HttpModuleCollection, dest: Array, index: int) """
        ...

    def Get(self, *__args:str): # -> IHttpModule
        """
        Get(self: HttpModuleCollection, name: str) -> IHttpModule
        Get(self: HttpModuleCollection, index: int) -> IHttpModule
        """
        ...

    def GetKey(self, index:int) -> str:
        """ GetKey(self: HttpModuleCollection, index: int) -> str """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...


class HttpParseException(HttpException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    HttpParseException()
    HttpParseException(message: str)
    HttpParseException(message: str, innerException: Exception)
    HttpParseException(message: str, innerException: Exception, virtualPath: str, sourceCode: str, line: int)
    """
    @property
    def FileName(self) -> str:
        """ Get: FileName(self: HttpParseException) -> str """
        ...

    @property
    def Line(self) -> int:
        """ Get: Line(self: HttpParseException) -> int """
        ...

    @property
    def ParserErrors(self): # -> ParserErrorCollection
        """ Get: ParserErrors(self: HttpParseException) -> ParserErrorCollection """
        ...

    @property
    def VirtualPath(self) -> str:
        """ Get: VirtualPath(self: HttpParseException) -> str """
        ...


    SerializeObjectState = ...


class HttpPostedFile: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ContentLength(self) -> int:
        """ Get: ContentLength(self: HttpPostedFile) -> int """
        ...

    @property
    def ContentType(self) -> str:
        """ Get: ContentType(self: HttpPostedFile) -> str """
        ...

    @property
    def FileName(self) -> str:
        """ Get: FileName(self: HttpPostedFile) -> str """
        ...

    @property
    def InputStream(self) -> Stream:
        """ Get: InputStream(self: HttpPostedFile) -> Stream """
        ...


    def SaveAs(self, filename:str): # -> 
        """ SaveAs(self: HttpPostedFile, filename: str) """
        ...


class HttpPostedFileBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ContentLength(self) -> int:
        """ Get: ContentLength(self: HttpPostedFileBase) -> int """
        ...

    @property
    def ContentType(self) -> str:
        """ Get: ContentType(self: HttpPostedFileBase) -> str """
        ...

    @property
    def FileName(self) -> str:
        """ Get: FileName(self: HttpPostedFileBase) -> str """
        ...

    @property
    def InputStream(self) -> Stream:
        """ Get: InputStream(self: HttpPostedFileBase) -> Stream """
        ...


    def SaveAs(self, filename:str): # -> 
        """ SaveAs(self: HttpPostedFileBase, filename: str) """
        ...


class HttpPostedFileWrapper(HttpPostedFileBase): # skipped bases: <type 'object'>
    """ HttpPostedFileWrapper(httpPostedFile: HttpPostedFile) """
    def __new__(cls, httpPostedFile:HttpPostedFile) -> Self:
        """ __new__(cls: type, httpPostedFile: HttpPostedFile) """
        ...


class HttpRequest: # skipped bases: <type 'object'>, <type 'object'>
    """ HttpRequest(filename: str, url: str, queryString: str) """
    @property
    def AcceptTypes(self) -> Array:
        """ Get: AcceptTypes(self: HttpRequest) -> Array[str] """
        ...

    @property
    def AnonymousID(self) -> str:
        """ Get: AnonymousID(self: HttpRequest) -> str """
        ...

    @property
    def ApplicationPath(self) -> str:
        """ Get: ApplicationPath(self: HttpRequest) -> str """
        ...

    @property
    def AppRelativeCurrentExecutionFilePath(self) -> str:
        """ Get: AppRelativeCurrentExecutionFilePath(self: HttpRequest) -> str """
        ...

    @property
    def Browser(self) -> HttpBrowserCapabilities:
        """
        Get: Browser(self: HttpRequest) -> HttpBrowserCapabilities
        Set: Browser(self: HttpRequest) = value
        """
        ...

    @property
    def ClientCertificate(self) -> HttpClientCertificate:
        """ Get: ClientCertificate(self: HttpRequest) -> HttpClientCertificate """
        ...

    @property
    def ContentEncoding(self) -> Encoding:
        """
        Get: ContentEncoding(self: HttpRequest) -> Encoding
        Set: ContentEncoding(self: HttpRequest) = value
        """
        ...

    @property
    def ContentLength(self) -> int:
        """ Get: ContentLength(self: HttpRequest) -> int """
        ...

    @property
    def ContentType(self) -> str:
        """
        Get: ContentType(self: HttpRequest) -> str
        Set: ContentType(self: HttpRequest) = value
        """
        ...

    @property
    def Cookies(self) -> HttpCookieCollection:
        """ Get: Cookies(self: HttpRequest) -> HttpCookieCollection """
        ...

    @property
    def CurrentExecutionFilePath(self) -> str:
        """ Get: CurrentExecutionFilePath(self: HttpRequest) -> str """
        ...

    @property
    def CurrentExecutionFilePathExtension(self) -> str:
        """ Get: CurrentExecutionFilePathExtension(self: HttpRequest) -> str """
        ...

    @property
    def FilePath(self) -> str:
        """ Get: FilePath(self: HttpRequest) -> str """
        ...

    @property
    def Files(self) -> HttpFileCollection:
        """ Get: Files(self: HttpRequest) -> HttpFileCollection """
        ...

    @property
    def Filter(self) -> Stream:
        """
        Get: Filter(self: HttpRequest) -> Stream
        Set: Filter(self: HttpRequest) = value
        """
        ...

    @property
    def Form(self) -> NameValueCollection:
        """ Get: Form(self: HttpRequest) -> NameValueCollection """
        ...

    @property
    def Headers(self) -> NameValueCollection:
        """ Get: Headers(self: HttpRequest) -> NameValueCollection """
        ...

    @property
    def HttpChannelBinding(self) -> ChannelBinding:
        """ Get: HttpChannelBinding(self: HttpRequest) -> ChannelBinding """
        ...

    @property
    def HttpMethod(self) -> str:
        """ Get: HttpMethod(self: HttpRequest) -> str """
        ...

    @property
    def InputStream(self) -> Stream:
        """ Get: InputStream(self: HttpRequest) -> Stream """
        ...

    @property
    def IsAuthenticated(self) -> bool:
        """ Get: IsAuthenticated(self: HttpRequest) -> bool """
        ...

    @property
    def IsLocal(self) -> bool:
        """ Get: IsLocal(self: HttpRequest) -> bool """
        ...

    @property
    def IsSecureConnection(self) -> bool:
        """ Get: IsSecureConnection(self: HttpRequest) -> bool """
        ...

    @property
    def LogonUserIdentity(self) -> WindowsIdentity:
        """ Get: LogonUserIdentity(self: HttpRequest) -> WindowsIdentity """
        ...

    @property
    def Params(self) -> NameValueCollection:
        """ Get: Params(self: HttpRequest) -> NameValueCollection """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: HttpRequest) -> str """
        ...

    @property
    def PathInfo(self) -> str:
        """ Get: PathInfo(self: HttpRequest) -> str """
        ...

    @property
    def PhysicalApplicationPath(self) -> str:
        """ Get: PhysicalApplicationPath(self: HttpRequest) -> str """
        ...

    @property
    def PhysicalPath(self) -> str:
        """ Get: PhysicalPath(self: HttpRequest) -> str """
        ...

    @property
    def QueryString(self) -> NameValueCollection:
        """ Get: QueryString(self: HttpRequest) -> NameValueCollection """
        ...

    @property
    def RawUrl(self) -> str:
        """ Get: RawUrl(self: HttpRequest) -> str """
        ...

    @property
    def ReadEntityBodyMode(self): # -> ReadEntityBodyMode
        """ Get: ReadEntityBodyMode(self: HttpRequest) -> ReadEntityBodyMode """
        ...

    @property
    def RequestContext(self) -> RequestContext:
        """
        Get: RequestContext(self: HttpRequest) -> RequestContext
        Set: RequestContext(self: HttpRequest) = value
        """
        ...

    @property
    def RequestType(self) -> str:
        """
        Get: RequestType(self: HttpRequest) -> str
        Set: RequestType(self: HttpRequest) = value
        """
        ...

    @property
    def ServerVariables(self) -> NameValueCollection:
        """ Get: ServerVariables(self: HttpRequest) -> NameValueCollection """
        ...

    @property
    def TimedOutToken(self) -> CancellationToken:
        """ Get: TimedOutToken(self: HttpRequest) -> CancellationToken """
        ...

    @property
    def TlsTokenBindingInfo(self): # -> ITlsTokenBindingInfo
        """ Get: TlsTokenBindingInfo(self: HttpRequest) -> ITlsTokenBindingInfo """
        ...

    @property
    def TotalBytes(self) -> int:
        """ Get: TotalBytes(self: HttpRequest) -> int """
        ...

    @property
    def Unvalidated(self): # -> UnvalidatedRequestValues
        """ Get: Unvalidated(self: HttpRequest) -> UnvalidatedRequestValues """
        ...

    @property
    def Url(self) -> Uri:
        """ Get: Url(self: HttpRequest) -> Uri """
        ...

    @property
    def UrlReferrer(self) -> Uri:
        """ Get: UrlReferrer(self: HttpRequest) -> Uri """
        ...

    @property
    def UserAgent(self) -> str:
        """ Get: UserAgent(self: HttpRequest) -> str """
        ...

    @property
    def UserHostAddress(self) -> str:
        """ Get: UserHostAddress(self: HttpRequest) -> str """
        ...

    @property
    def UserHostName(self) -> str:
        """ Get: UserHostName(self: HttpRequest) -> str """
        ...

    @property
    def UserLanguages(self) -> Array:
        """ Get: UserLanguages(self: HttpRequest) -> Array[str] """
        ...


    def Abort(self): # -> 
        """ Abort(self: HttpRequest) """
        ...

    def BinaryRead(self, count:int) -> Array:
        """ BinaryRead(self: HttpRequest, count: int) -> Array[Byte] """
        ...

    def GetBufferedInputStream(self) -> Stream:
        """ GetBufferedInputStream(self: HttpRequest) -> Stream """
        ...

    def GetBufferlessInputStream(self, disableMaxRequestLength:bool = ...) -> Stream:
        """
        GetBufferlessInputStream(self: HttpRequest) -> Stream
        GetBufferlessInputStream(self: HttpRequest, disableMaxRequestLength: bool) -> Stream
        """
        ...

    def InsertEntityBody(self, buffer:Array = ..., offset:int = ..., count:int = ...): # -> 
        """ InsertEntityBody(self: HttpRequest)InsertEntityBody(self: HttpRequest, buffer: Array[Byte], offset: int, count: int) """
        ...

    def MapImageCoordinates(self, imageFieldName:str) -> Array:
        """ MapImageCoordinates(self: HttpRequest, imageFieldName: str) -> Array[int] """
        ...

    def MapPath(self, virtualPath:str, baseVirtualDir:str = ..., allowCrossAppMapping:bool = ...) -> str:
        """
        MapPath(self: HttpRequest, virtualPath: str) -> str
        MapPath(self: HttpRequest, virtualPath: str, baseVirtualDir: str, allowCrossAppMapping: bool) -> str
        """
        ...

    def MapRawImageCoordinates(self, imageFieldName:str) -> Array:
        """ MapRawImageCoordinates(self: HttpRequest, imageFieldName: str) -> Array[float] """
        ...

    def SaveAs(self, filename:str, includeHeaders:bool): # -> 
        """ SaveAs(self: HttpRequest, filename: str, includeHeaders: bool) """
        ...

    def ValidateInput(self): # -> 
        """ ValidateInput(self: HttpRequest) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class HttpRequestBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AcceptTypes(self) -> Array:
        """ Get: AcceptTypes(self: HttpRequestBase) -> Array[str] """
        ...

    @property
    def AnonymousID(self) -> str:
        """ Get: AnonymousID(self: HttpRequestBase) -> str """
        ...

    @property
    def ApplicationPath(self) -> str:
        """ Get: ApplicationPath(self: HttpRequestBase) -> str """
        ...

    @property
    def AppRelativeCurrentExecutionFilePath(self) -> str:
        """ Get: AppRelativeCurrentExecutionFilePath(self: HttpRequestBase) -> str """
        ...

    @property
    def Browser(self) -> HttpBrowserCapabilitiesBase:
        """ Get: Browser(self: HttpRequestBase) -> HttpBrowserCapabilitiesBase """
        ...

    @property
    def ClientCertificate(self) -> HttpClientCertificate:
        """ Get: ClientCertificate(self: HttpRequestBase) -> HttpClientCertificate """
        ...

    @property
    def ContentEncoding(self) -> Encoding:
        """
        Get: ContentEncoding(self: HttpRequestBase) -> Encoding
        Set: ContentEncoding(self: HttpRequestBase) = value
        """
        ...

    @property
    def ContentLength(self) -> int:
        """ Get: ContentLength(self: HttpRequestBase) -> int """
        ...

    @property
    def ContentType(self) -> str:
        """
        Get: ContentType(self: HttpRequestBase) -> str
        Set: ContentType(self: HttpRequestBase) = value
        """
        ...

    @property
    def Cookies(self) -> HttpCookieCollection:
        """ Get: Cookies(self: HttpRequestBase) -> HttpCookieCollection """
        ...

    @property
    def CurrentExecutionFilePath(self) -> str:
        """ Get: CurrentExecutionFilePath(self: HttpRequestBase) -> str """
        ...

    @property
    def CurrentExecutionFilePathExtension(self) -> str:
        """ Get: CurrentExecutionFilePathExtension(self: HttpRequestBase) -> str """
        ...

    @property
    def FilePath(self) -> str:
        """ Get: FilePath(self: HttpRequestBase) -> str """
        ...

    @property
    def Files(self) -> HttpFileCollectionBase:
        """ Get: Files(self: HttpRequestBase) -> HttpFileCollectionBase """
        ...

    @property
    def Filter(self) -> Stream:
        """
        Get: Filter(self: HttpRequestBase) -> Stream
        Set: Filter(self: HttpRequestBase) = value
        """
        ...

    @property
    def Form(self) -> NameValueCollection:
        """ Get: Form(self: HttpRequestBase) -> NameValueCollection """
        ...

    @property
    def Headers(self) -> NameValueCollection:
        """ Get: Headers(self: HttpRequestBase) -> NameValueCollection """
        ...

    @property
    def HttpChannelBinding(self) -> ChannelBinding:
        """ Get: HttpChannelBinding(self: HttpRequestBase) -> ChannelBinding """
        ...

    @property
    def HttpMethod(self) -> str:
        """ Get: HttpMethod(self: HttpRequestBase) -> str """
        ...

    @property
    def InputStream(self) -> Stream:
        """ Get: InputStream(self: HttpRequestBase) -> Stream """
        ...

    @property
    def IsAuthenticated(self) -> bool:
        """ Get: IsAuthenticated(self: HttpRequestBase) -> bool """
        ...

    @property
    def IsLocal(self) -> bool:
        """ Get: IsLocal(self: HttpRequestBase) -> bool """
        ...

    @property
    def IsSecureConnection(self) -> bool:
        """ Get: IsSecureConnection(self: HttpRequestBase) -> bool """
        ...

    @property
    def LogonUserIdentity(self) -> WindowsIdentity:
        """ Get: LogonUserIdentity(self: HttpRequestBase) -> WindowsIdentity """
        ...

    @property
    def Params(self) -> NameValueCollection:
        """ Get: Params(self: HttpRequestBase) -> NameValueCollection """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: HttpRequestBase) -> str """
        ...

    @property
    def PathInfo(self) -> str:
        """ Get: PathInfo(self: HttpRequestBase) -> str """
        ...

    @property
    def PhysicalApplicationPath(self) -> str:
        """ Get: PhysicalApplicationPath(self: HttpRequestBase) -> str """
        ...

    @property
    def PhysicalPath(self) -> str:
        """ Get: PhysicalPath(self: HttpRequestBase) -> str """
        ...

    @property
    def QueryString(self) -> NameValueCollection:
        """ Get: QueryString(self: HttpRequestBase) -> NameValueCollection """
        ...

    @property
    def RawUrl(self) -> str:
        """ Get: RawUrl(self: HttpRequestBase) -> str """
        ...

    @property
    def ReadEntityBodyMode(self): # -> ReadEntityBodyMode
        """ Get: ReadEntityBodyMode(self: HttpRequestBase) -> ReadEntityBodyMode """
        ...

    @property
    def RequestContext(self) -> RequestContext:
        """
        Get: RequestContext(self: HttpRequestBase) -> RequestContext
        Set: RequestContext(self: HttpRequestBase) = value
        """
        ...

    @property
    def RequestType(self) -> str:
        """
        Get: RequestType(self: HttpRequestBase) -> str
        Set: RequestType(self: HttpRequestBase) = value
        """
        ...

    @property
    def ServerVariables(self) -> NameValueCollection:
        """ Get: ServerVariables(self: HttpRequestBase) -> NameValueCollection """
        ...

    @property
    def TimedOutToken(self) -> CancellationToken:
        """ Get: TimedOutToken(self: HttpRequestBase) -> CancellationToken """
        ...

    @property
    def TlsTokenBindingInfo(self): # -> ITlsTokenBindingInfo
        """ Get: TlsTokenBindingInfo(self: HttpRequestBase) -> ITlsTokenBindingInfo """
        ...

    @property
    def TotalBytes(self) -> int:
        """ Get: TotalBytes(self: HttpRequestBase) -> int """
        ...

    @property
    def Unvalidated(self): # -> UnvalidatedRequestValuesBase
        """ Get: Unvalidated(self: HttpRequestBase) -> UnvalidatedRequestValuesBase """
        ...

    @property
    def Url(self) -> Uri:
        """ Get: Url(self: HttpRequestBase) -> Uri """
        ...

    @property
    def UrlReferrer(self) -> Uri:
        """ Get: UrlReferrer(self: HttpRequestBase) -> Uri """
        ...

    @property
    def UserAgent(self) -> str:
        """ Get: UserAgent(self: HttpRequestBase) -> str """
        ...

    @property
    def UserHostAddress(self) -> str:
        """ Get: UserHostAddress(self: HttpRequestBase) -> str """
        ...

    @property
    def UserHostName(self) -> str:
        """ Get: UserHostName(self: HttpRequestBase) -> str """
        ...

    @property
    def UserLanguages(self) -> Array:
        """ Get: UserLanguages(self: HttpRequestBase) -> Array[str] """
        ...


    def Abort(self): # -> 
        """ Abort(self: HttpRequestBase) """
        ...

    def BinaryRead(self, count:int) -> Array:
        """ BinaryRead(self: HttpRequestBase, count: int) -> Array[Byte] """
        ...

    def GetBufferedInputStream(self) -> Stream:
        """ GetBufferedInputStream(self: HttpRequestBase) -> Stream """
        ...

    def GetBufferlessInputStream(self, disableMaxRequestLength:bool = ...) -> Stream:
        """
        GetBufferlessInputStream(self: HttpRequestBase) -> Stream
        GetBufferlessInputStream(self: HttpRequestBase, disableMaxRequestLength: bool) -> Stream
        """
        ...

    def InsertEntityBody(self, buffer:Array = ..., offset:int = ..., count:int = ...): # -> 
        """ InsertEntityBody(self: HttpRequestBase)InsertEntityBody(self: HttpRequestBase, buffer: Array[Byte], offset: int, count: int) """
        ...

    def MapImageCoordinates(self, imageFieldName:str) -> Array:
        """ MapImageCoordinates(self: HttpRequestBase, imageFieldName: str) -> Array[int] """
        ...

    def MapPath(self, virtualPath:str, baseVirtualDir:str = ..., allowCrossAppMapping:bool = ...) -> str:
        """
        MapPath(self: HttpRequestBase, virtualPath: str) -> str
        MapPath(self: HttpRequestBase, virtualPath: str, baseVirtualDir: str, allowCrossAppMapping: bool) -> str
        """
        ...

    def MapRawImageCoordinates(self, imageFieldName:str) -> Array:
        """ MapRawImageCoordinates(self: HttpRequestBase, imageFieldName: str) -> Array[float] """
        ...

    def SaveAs(self, filename:str, includeHeaders:bool): # -> 
        """ SaveAs(self: HttpRequestBase, filename: str, includeHeaders: bool) """
        ...

    def ValidateInput(self): # -> 
        """ ValidateInput(self: HttpRequestBase) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class HttpRequestValidationException(HttpException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    HttpRequestValidationException()
    HttpRequestValidationException(message: str)
    HttpRequestValidationException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class HttpRequestWrapper(HttpRequestBase): # skipped bases: <type 'object'>
    """ HttpRequestWrapper(httpRequest: HttpRequest) """
    def __new__(cls, httpRequest:HttpRequest) -> Self:
        """ __new__(cls: type, httpRequest: HttpRequest) """
        ...


class HttpResponse: # skipped bases: <type 'object'>, <type 'object'>
    """ HttpResponse(writer: TextWriter) """
    @property
    def Buffer(self) -> bool:
        """
        Get: Buffer(self: HttpResponse) -> bool
        Set: Buffer(self: HttpResponse) = value
        """
        ...

    @property
    def BufferOutput(self) -> bool:
        """
        Get: BufferOutput(self: HttpResponse) -> bool
        Set: BufferOutput(self: HttpResponse) = value
        """
        ...

    @property
    def Cache(self) -> HttpCachePolicy:
        """ Get: Cache(self: HttpResponse) -> HttpCachePolicy """
        ...

    @property
    def CacheControl(self) -> str:
        """
        Get: CacheControl(self: HttpResponse) -> str
        Set: CacheControl(self: HttpResponse) = value
        """
        ...

    @property
    def Charset(self) -> str:
        """
        Get: Charset(self: HttpResponse) -> str
        Set: Charset(self: HttpResponse) = value
        """
        ...

    @property
    def ClientDisconnectedToken(self) -> CancellationToken:
        """ Get: ClientDisconnectedToken(self: HttpResponse) -> CancellationToken """
        ...

    @property
    def ContentEncoding(self) -> Encoding:
        """
        Get: ContentEncoding(self: HttpResponse) -> Encoding
        Set: ContentEncoding(self: HttpResponse) = value
        """
        ...

    @property
    def ContentType(self) -> str:
        """
        Get: ContentType(self: HttpResponse) -> str
        Set: ContentType(self: HttpResponse) = value
        """
        ...

    @property
    def Cookies(self) -> HttpCookieCollection:
        """ Get: Cookies(self: HttpResponse) -> HttpCookieCollection """
        ...

    @property
    def Expires(self) -> int:
        """
        Get: Expires(self: HttpResponse) -> int
        Set: Expires(self: HttpResponse) = value
        """
        ...

    @property
    def ExpiresAbsolute(self) -> DateTime:
        """
        Get: ExpiresAbsolute(self: HttpResponse) -> DateTime
        Set: ExpiresAbsolute(self: HttpResponse) = value
        """
        ...

    @property
    def Filter(self) -> Stream:
        """
        Get: Filter(self: HttpResponse) -> Stream
        Set: Filter(self: HttpResponse) = value
        """
        ...

    @property
    def HeaderEncoding(self) -> Encoding:
        """
        Get: HeaderEncoding(self: HttpResponse) -> Encoding
        Set: HeaderEncoding(self: HttpResponse) = value
        """
        ...

    @property
    def Headers(self) -> NameValueCollection:
        """ Get: Headers(self: HttpResponse) -> NameValueCollection """
        ...

    @property
    def HeadersWritten(self) -> bool:
        """ Get: HeadersWritten(self: HttpResponse) -> bool """
        ...

    @property
    def IsClientConnected(self) -> bool:
        """ Get: IsClientConnected(self: HttpResponse) -> bool """
        ...

    @property
    def IsRequestBeingRedirected(self) -> bool:
        """ Get: IsRequestBeingRedirected(self: HttpResponse) -> bool """
        ...

    @property
    def Output(self) -> TextWriter:
        """
        Get: Output(self: HttpResponse) -> TextWriter
        Set: Output(self: HttpResponse) = value
        """
        ...

    @property
    def OutputStream(self) -> Stream:
        """ Get: OutputStream(self: HttpResponse) -> Stream """
        ...

    @property
    def RedirectLocation(self) -> str:
        """
        Get: RedirectLocation(self: HttpResponse) -> str
        Set: RedirectLocation(self: HttpResponse) = value
        """
        ...

    @property
    def Status(self) -> str:
        """
        Get: Status(self: HttpResponse) -> str
        Set: Status(self: HttpResponse) = value
        """
        ...

    @property
    def StatusCode(self) -> int:
        """
        Get: StatusCode(self: HttpResponse) -> int
        Set: StatusCode(self: HttpResponse) = value
        """
        ...

    @property
    def StatusDescription(self) -> str:
        """
        Get: StatusDescription(self: HttpResponse) -> str
        Set: StatusDescription(self: HttpResponse) = value
        """
        ...

    @property
    def SubStatusCode(self) -> int:
        """
        Get: SubStatusCode(self: HttpResponse) -> int
        Set: SubStatusCode(self: HttpResponse) = value
        """
        ...

    @property
    def SupportsAsyncFlush(self) -> bool:
        """ Get: SupportsAsyncFlush(self: HttpResponse) -> bool """
        ...

    @property
    def SuppressContent(self) -> bool:
        """
        Get: SuppressContent(self: HttpResponse) -> bool
        Set: SuppressContent(self: HttpResponse) = value
        """
        ...

    @property
    def SuppressDefaultCacheControlHeader(self) -> bool:
        """
        Get: SuppressDefaultCacheControlHeader(self: HttpResponse) -> bool
        Set: SuppressDefaultCacheControlHeader(self: HttpResponse) = value
        """
        ...

    @property
    def SuppressFormsAuthenticationRedirect(self) -> bool:
        """
        Get: SuppressFormsAuthenticationRedirect(self: HttpResponse) -> bool
        Set: SuppressFormsAuthenticationRedirect(self: HttpResponse) = value
        """
        ...

    @property
    def TrySkipIisCustomErrors(self) -> bool:
        """
        Get: TrySkipIisCustomErrors(self: HttpResponse) -> bool
        Set: TrySkipIisCustomErrors(self: HttpResponse) = value
        """
        ...


    def AddCacheDependency(self, dependencies:Array): # -> 
        """ AddCacheDependency(self: HttpResponse, *dependencies: Array[CacheDependency]) """
        ...

    def AddCacheItemDependencies(self, cacheKeys:ArrayList): # -> 
        """ AddCacheItemDependencies(self: HttpResponse, cacheKeys: ArrayList)AddCacheItemDependencies(self: HttpResponse, cacheKeys: Array[str]) """
        ...

    def AddCacheItemDependency(self, cacheKey:str): # -> 
        """ AddCacheItemDependency(self: HttpResponse, cacheKey: str) """
        ...

    def AddFileDependencies(self, filenames:ArrayList): # -> 
        """ AddFileDependencies(self: HttpResponse, filenames: ArrayList)AddFileDependencies(self: HttpResponse, filenames: Array[str]) """
        ...

    def AddFileDependency(self, filename:str): # -> 
        """ AddFileDependency(self: HttpResponse, filename: str) """
        ...

    def AddHeader(self, name:str, value:str): # -> 
        """ AddHeader(self: HttpResponse, name: str, value: str) """
        ...

    def AddOnSendingHeaders(self, callback:Action): # -> ISubscriptionToken
        """ AddOnSendingHeaders(self: HttpResponse, callback: Action[HttpContext]) -> ISubscriptionToken """
        ...

    def AppendCookie(self, cookie:HttpCookie): # -> 
        """ AppendCookie(self: HttpResponse, cookie: HttpCookie) """
        ...

    def AppendHeader(self, name:str, value:str): # -> 
        """ AppendHeader(self: HttpResponse, name: str, value: str) """
        ...

    def AppendToLog(self, param:str): # -> 
        """ AppendToLog(self: HttpResponse, param: str) """
        ...

    def ApplyAppPathModifier(self, virtualPath:str) -> str:
        """ ApplyAppPathModifier(self: HttpResponse, virtualPath: str) -> str """
        ...

    def BeginFlush(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginFlush(self: HttpResponse, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BinaryWrite(self, buffer:Array): # -> 
        """ BinaryWrite(self: HttpResponse, buffer: Array[Byte]) """
        ...

    def Clear(self): # -> 
        """ Clear(self: HttpResponse) """
        ...

    def ClearContent(self): # -> 
        """ ClearContent(self: HttpResponse) """
        ...

    def ClearHeaders(self): # -> 
        """ ClearHeaders(self: HttpResponse) """
        ...

    def Close(self): # -> 
        """ Close(self: HttpResponse) """
        ...

    def DisableKernelCache(self): # -> 
        """ DisableKernelCache(self: HttpResponse) """
        ...

    def DisableUserCache(self): # -> 
        """ DisableUserCache(self: HttpResponse) """
        ...

    def End(self): # -> 
        """ End(self: HttpResponse) """
        ...

    def EndFlush(self, asyncResult:IAsyncResult): # -> 
        """ EndFlush(self: HttpResponse, asyncResult: IAsyncResult) """
        ...

    def Flush(self): # -> 
        """ Flush(self: HttpResponse) """
        ...

    def FlushAsync(self) -> Task:
        """ FlushAsync(self: HttpResponse) -> Task """
        ...

    def Pics(self, value:str): # -> 
        """ Pics(self: HttpResponse, value: str) """
        ...

    def PushPromise(self, path:str, method:str = ..., headers:NameValueCollection = ...): # -> 
        """ PushPromise(self: HttpResponse, path: str)PushPromise(self: HttpResponse, path: str, method: str, headers: NameValueCollection) """
        ...

    def Redirect(self, url:str, endResponse:bool = ...): # -> 
        """ Redirect(self: HttpResponse, url: str)Redirect(self: HttpResponse, url: str, endResponse: bool) """
        ...

    def RedirectPermanent(self, url:str, endResponse:bool = ...): # -> 
        """ RedirectPermanent(self: HttpResponse, url: str)RedirectPermanent(self: HttpResponse, url: str, endResponse: bool) """
        ...

    def RedirectToRoute(self, *__args:str): # -> 
        """ RedirectToRoute(self: HttpResponse, routeName: str)RedirectToRoute(self: HttpResponse, routeValues: RouteValueDictionary)RedirectToRoute(self: HttpResponse, routeName: str, routeValues: RouteValueDictionary)RedirectToRoute(self: HttpResponse, routeValues: object)RedirectToRoute(self: HttpResponse, routeName: str, routeValues: object) """
        ...

    def RedirectToRoutePermanent(self, *__args:str): # -> 
        """ RedirectToRoutePermanent(self: HttpResponse, routeName: str)RedirectToRoutePermanent(self: HttpResponse, routeValues: RouteValueDictionary)RedirectToRoutePermanent(self: HttpResponse, routeName: str, routeValues: RouteValueDictionary)RedirectToRoutePermanent(self: HttpResponse, routeValues: object)RedirectToRoutePermanent(self: HttpResponse, routeName: str, routeValues: object) """
        ...

    @staticmethod
    def RemoveOutputCacheItem(path:str, providerName:str = ...): # -> 
        """ RemoveOutputCacheItem(path: str)RemoveOutputCacheItem(path: str, providerName: str) """
        ...

    def SetCookie(self, cookie:HttpCookie): # -> 
        """ SetCookie(self: HttpResponse, cookie: HttpCookie) """
        ...

    def TransmitFile(self, filename:str, offset:Int64 = ..., length:Int64 = ...): # -> 
        """ TransmitFile(self: HttpResponse, filename: str)TransmitFile(self: HttpResponse, filename: str, offset: Int64, length: Int64) """
        ...

    def Write(self, *__args:str): # -> 
        """ Write(self: HttpResponse, s: str)Write(self: HttpResponse, obj: object)Write(self: HttpResponse, ch: Char)Write(self: HttpResponse, buffer: Array[Char], index: int, count: int) """
        ...

    def WriteFile(self, *__args:str): # -> 
        """ WriteFile(self: HttpResponse, filename: str)WriteFile(self: HttpResponse, filename: str, offset: Int64, size: Int64)WriteFile(self: HttpResponse, filename: str, readIntoMemory: bool)WriteFile(self: HttpResponse, fileHandle: IntPtr, offset: Int64, size: Int64) """
        ...

    def WriteSubstitution(self, callback): # ->  # Not found arg types: {'callback': 'HttpResponseSubstitutionCallback'}
        """ WriteSubstitution(self: HttpResponse, callback: HttpResponseSubstitutionCallback) """
        ...


class HttpResponseBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Buffer(self) -> bool:
        """
        Get: Buffer(self: HttpResponseBase) -> bool
        Set: Buffer(self: HttpResponseBase) = value
        """
        ...

    @property
    def BufferOutput(self) -> bool:
        """
        Get: BufferOutput(self: HttpResponseBase) -> bool
        Set: BufferOutput(self: HttpResponseBase) = value
        """
        ...

    @property
    def Cache(self) -> HttpCachePolicyBase:
        """ Get: Cache(self: HttpResponseBase) -> HttpCachePolicyBase """
        ...

    @property
    def CacheControl(self) -> str:
        """
        Get: CacheControl(self: HttpResponseBase) -> str
        Set: CacheControl(self: HttpResponseBase) = value
        """
        ...

    @property
    def Charset(self) -> str:
        """
        Get: Charset(self: HttpResponseBase) -> str
        Set: Charset(self: HttpResponseBase) = value
        """
        ...

    @property
    def ClientDisconnectedToken(self) -> CancellationToken:
        """ Get: ClientDisconnectedToken(self: HttpResponseBase) -> CancellationToken """
        ...

    @property
    def ContentEncoding(self) -> Encoding:
        """
        Get: ContentEncoding(self: HttpResponseBase) -> Encoding
        Set: ContentEncoding(self: HttpResponseBase) = value
        """
        ...

    @property
    def ContentType(self) -> str:
        """
        Get: ContentType(self: HttpResponseBase) -> str
        Set: ContentType(self: HttpResponseBase) = value
        """
        ...

    @property
    def Cookies(self) -> HttpCookieCollection:
        """ Get: Cookies(self: HttpResponseBase) -> HttpCookieCollection """
        ...

    @property
    def Expires(self) -> int:
        """
        Get: Expires(self: HttpResponseBase) -> int
        Set: Expires(self: HttpResponseBase) = value
        """
        ...

    @property
    def ExpiresAbsolute(self) -> DateTime:
        """
        Get: ExpiresAbsolute(self: HttpResponseBase) -> DateTime
        Set: ExpiresAbsolute(self: HttpResponseBase) = value
        """
        ...

    @property
    def Filter(self) -> Stream:
        """
        Get: Filter(self: HttpResponseBase) -> Stream
        Set: Filter(self: HttpResponseBase) = value
        """
        ...

    @property
    def HeaderEncoding(self) -> Encoding:
        """
        Get: HeaderEncoding(self: HttpResponseBase) -> Encoding
        Set: HeaderEncoding(self: HttpResponseBase) = value
        """
        ...

    @property
    def Headers(self) -> NameValueCollection:
        """ Get: Headers(self: HttpResponseBase) -> NameValueCollection """
        ...

    @property
    def HeadersWritten(self) -> bool:
        """ Get: HeadersWritten(self: HttpResponseBase) -> bool """
        ...

    @property
    def IsClientConnected(self) -> bool:
        """ Get: IsClientConnected(self: HttpResponseBase) -> bool """
        ...

    @property
    def IsRequestBeingRedirected(self) -> bool:
        """ Get: IsRequestBeingRedirected(self: HttpResponseBase) -> bool """
        ...

    @property
    def Output(self) -> TextWriter:
        """
        Get: Output(self: HttpResponseBase) -> TextWriter
        Set: Output(self: HttpResponseBase) = value
        """
        ...

    @property
    def OutputStream(self) -> Stream:
        """ Get: OutputStream(self: HttpResponseBase) -> Stream """
        ...

    @property
    def RedirectLocation(self) -> str:
        """
        Get: RedirectLocation(self: HttpResponseBase) -> str
        Set: RedirectLocation(self: HttpResponseBase) = value
        """
        ...

    @property
    def Status(self) -> str:
        """
        Get: Status(self: HttpResponseBase) -> str
        Set: Status(self: HttpResponseBase) = value
        """
        ...

    @property
    def StatusCode(self) -> int:
        """
        Get: StatusCode(self: HttpResponseBase) -> int
        Set: StatusCode(self: HttpResponseBase) = value
        """
        ...

    @property
    def StatusDescription(self) -> str:
        """
        Get: StatusDescription(self: HttpResponseBase) -> str
        Set: StatusDescription(self: HttpResponseBase) = value
        """
        ...

    @property
    def SubStatusCode(self) -> int:
        """
        Get: SubStatusCode(self: HttpResponseBase) -> int
        Set: SubStatusCode(self: HttpResponseBase) = value
        """
        ...

    @property
    def SupportsAsyncFlush(self) -> bool:
        """ Get: SupportsAsyncFlush(self: HttpResponseBase) -> bool """
        ...

    @property
    def SuppressContent(self) -> bool:
        """
        Get: SuppressContent(self: HttpResponseBase) -> bool
        Set: SuppressContent(self: HttpResponseBase) = value
        """
        ...

    @property
    def SuppressDefaultCacheControlHeader(self) -> bool:
        """
        Get: SuppressDefaultCacheControlHeader(self: HttpResponseBase) -> bool
        Set: SuppressDefaultCacheControlHeader(self: HttpResponseBase) = value
        """
        ...

    @property
    def SuppressFormsAuthenticationRedirect(self) -> bool:
        """
        Get: SuppressFormsAuthenticationRedirect(self: HttpResponseBase) -> bool
        Set: SuppressFormsAuthenticationRedirect(self: HttpResponseBase) = value
        """
        ...

    @property
    def TrySkipIisCustomErrors(self) -> bool:
        """
        Get: TrySkipIisCustomErrors(self: HttpResponseBase) -> bool
        Set: TrySkipIisCustomErrors(self: HttpResponseBase) = value
        """
        ...


    def AddCacheDependency(self, dependencies:Array): # -> 
        """ AddCacheDependency(self: HttpResponseBase, *dependencies: Array[CacheDependency]) """
        ...

    def AddCacheItemDependencies(self, cacheKeys:ArrayList): # -> 
        """ AddCacheItemDependencies(self: HttpResponseBase, cacheKeys: ArrayList)AddCacheItemDependencies(self: HttpResponseBase, cacheKeys: Array[str]) """
        ...

    def AddCacheItemDependency(self, cacheKey:str): # -> 
        """ AddCacheItemDependency(self: HttpResponseBase, cacheKey: str) """
        ...

    def AddFileDependencies(self, filenames:ArrayList): # -> 
        """ AddFileDependencies(self: HttpResponseBase, filenames: ArrayList)AddFileDependencies(self: HttpResponseBase, filenames: Array[str]) """
        ...

    def AddFileDependency(self, filename:str): # -> 
        """ AddFileDependency(self: HttpResponseBase, filename: str) """
        ...

    def AddHeader(self, name:str, value:str): # -> 
        """ AddHeader(self: HttpResponseBase, name: str, value: str) """
        ...

    def AddOnSendingHeaders(self, callback:Action): # -> ISubscriptionToken
        """ AddOnSendingHeaders(self: HttpResponseBase, callback: Action[HttpContextBase]) -> ISubscriptionToken """
        ...

    def AppendCookie(self, cookie:HttpCookie): # -> 
        """ AppendCookie(self: HttpResponseBase, cookie: HttpCookie) """
        ...

    def AppendHeader(self, name:str, value:str): # -> 
        """ AppendHeader(self: HttpResponseBase, name: str, value: str) """
        ...

    def AppendToLog(self, param:str): # -> 
        """ AppendToLog(self: HttpResponseBase, param: str) """
        ...

    def ApplyAppPathModifier(self, virtualPath:str) -> str:
        """ ApplyAppPathModifier(self: HttpResponseBase, virtualPath: str) -> str """
        ...

    def BeginFlush(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginFlush(self: HttpResponseBase, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BinaryWrite(self, buffer:Array): # -> 
        """ BinaryWrite(self: HttpResponseBase, buffer: Array[Byte]) """
        ...

    def Clear(self): # -> 
        """ Clear(self: HttpResponseBase) """
        ...

    def ClearContent(self): # -> 
        """ ClearContent(self: HttpResponseBase) """
        ...

    def ClearHeaders(self): # -> 
        """ ClearHeaders(self: HttpResponseBase) """
        ...

    def Close(self): # -> 
        """ Close(self: HttpResponseBase) """
        ...

    def DisableKernelCache(self): # -> 
        """ DisableKernelCache(self: HttpResponseBase) """
        ...

    def DisableUserCache(self): # -> 
        """ DisableUserCache(self: HttpResponseBase) """
        ...

    def End(self): # -> 
        """ End(self: HttpResponseBase) """
        ...

    def EndFlush(self, asyncResult:IAsyncResult): # -> 
        """ EndFlush(self: HttpResponseBase, asyncResult: IAsyncResult) """
        ...

    def Flush(self): # -> 
        """ Flush(self: HttpResponseBase) """
        ...

    def FlushAsync(self) -> Task:
        """ FlushAsync(self: HttpResponseBase) -> Task """
        ...

    def Pics(self, value:str): # -> 
        """ Pics(self: HttpResponseBase, value: str) """
        ...

    def PushPromise(self, path:str, method:str = ..., headers:NameValueCollection = ...): # -> 
        """ PushPromise(self: HttpResponseBase, path: str)PushPromise(self: HttpResponseBase, path: str, method: str, headers: NameValueCollection) """
        ...

    def Redirect(self, url:str, endResponse:bool = ...): # -> 
        """ Redirect(self: HttpResponseBase, url: str)Redirect(self: HttpResponseBase, url: str, endResponse: bool) """
        ...

    def RedirectPermanent(self, url:str, endResponse:bool = ...): # -> 
        """ RedirectPermanent(self: HttpResponseBase, url: str)RedirectPermanent(self: HttpResponseBase, url: str, endResponse: bool) """
        ...

    def RedirectToRoute(self, *__args:object): # -> 
        """ RedirectToRoute(self: HttpResponseBase, routeValues: object)RedirectToRoute(self: HttpResponseBase, routeName: str)RedirectToRoute(self: HttpResponseBase, routeValues: RouteValueDictionary)RedirectToRoute(self: HttpResponseBase, routeName: str, routeValues: object)RedirectToRoute(self: HttpResponseBase, routeName: str, routeValues: RouteValueDictionary) """
        ...

    def RedirectToRoutePermanent(self, *__args:object): # -> 
        """ RedirectToRoutePermanent(self: HttpResponseBase, routeValues: object)RedirectToRoutePermanent(self: HttpResponseBase, routeName: str)RedirectToRoutePermanent(self: HttpResponseBase, routeValues: RouteValueDictionary)RedirectToRoutePermanent(self: HttpResponseBase, routeName: str, routeValues: object)RedirectToRoutePermanent(self: HttpResponseBase, routeName: str, routeValues: RouteValueDictionary) """
        ...

    def RemoveOutputCacheItem(self, path:str, providerName:str = ...): # -> 
        """ RemoveOutputCacheItem(self: HttpResponseBase, path: str)RemoveOutputCacheItem(self: HttpResponseBase, path: str, providerName: str) """
        ...

    def SetCookie(self, cookie:HttpCookie): # -> 
        """ SetCookie(self: HttpResponseBase, cookie: HttpCookie) """
        ...

    def TransmitFile(self, filename:str, offset:Int64 = ..., length:Int64 = ...): # -> 
        """ TransmitFile(self: HttpResponseBase, filename: str)TransmitFile(self: HttpResponseBase, filename: str, offset: Int64, length: Int64) """
        ...

    def Write(self, *__args:Char): # -> 
        """ Write(self: HttpResponseBase, ch: Char)Write(self: HttpResponseBase, buffer: Array[Char], index: int, count: int)Write(self: HttpResponseBase, obj: object)Write(self: HttpResponseBase, s: str) """
        ...

    def WriteFile(self, *__args:str): # -> 
        """ WriteFile(self: HttpResponseBase, filename: str)WriteFile(self: HttpResponseBase, filename: str, readIntoMemory: bool)WriteFile(self: HttpResponseBase, filename: str, offset: Int64, size: Int64)WriteFile(self: HttpResponseBase, fileHandle: IntPtr, offset: Int64, size: Int64) """
        ...

    def WriteSubstitution(self, callback): # ->  # Not found arg types: {'callback': 'HttpResponseSubstitutionCallback'}
        """ WriteSubstitution(self: HttpResponseBase, callback: HttpResponseSubstitutionCallback) """
        ...


class HttpResponseSubstitutionCallback(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ HttpResponseSubstitutionCallback(object: object, method: IntPtr) """
    def BeginInvoke(self, context:HttpContext, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: HttpResponseSubstitutionCallback, context: HttpContext, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> str:
        """ EndInvoke(self: HttpResponseSubstitutionCallback, result: IAsyncResult) -> str """
        ...

    def Invoke(self, context:HttpContext) -> str:
        """ Invoke(self: HttpResponseSubstitutionCallback, context: HttpContext) -> str """
        ...


class HttpResponseWrapper(HttpResponseBase): # skipped bases: <type 'object'>
    """ HttpResponseWrapper(httpResponse: HttpResponse) """
    def __new__(cls, httpResponse:HttpResponse) -> Self:
        """ __new__(cls: type, httpResponse: HttpResponse) """
        ...


class HttpRuntime: # skipped bases: <type 'object'>, <type 'object'>
    """ HttpRuntime() """
    @property
    def AppDomainAppId(self) -> str:
        """ Get: AppDomainAppId() -> str """
        ...

    @property
    def AppDomainAppPath(self) -> str:
        """ Get: AppDomainAppPath() -> str """
        ...

    @property
    def AppDomainAppVirtualPath(self) -> str:
        """ Get: AppDomainAppVirtualPath() -> str """
        ...

    @property
    def AppDomainId(self) -> str:
        """ Get: AppDomainId() -> str """
        ...

    @property
    def AspClientScriptPhysicalPath(self) -> str:
        """ Get: AspClientScriptPhysicalPath() -> str """
        ...

    @property
    def AspClientScriptVirtualPath(self) -> str:
        """ Get: AspClientScriptVirtualPath() -> str """
        ...

    @property
    def AspInstallDirectory(self) -> str:
        """ Get: AspInstallDirectory() -> str """
        ...

    @property
    def BinDirectory(self) -> str:
        """ Get: BinDirectory() -> str """
        ...

    @property
    def Cache(self) -> Cache:
        """ Get: Cache() -> Cache """
        ...

    @property
    def ClrInstallDirectory(self) -> str:
        """ Get: ClrInstallDirectory() -> str """
        ...

    @property
    def CodegenDir(self) -> str:
        """ Get: CodegenDir() -> str """
        ...

    @property
    def IISVersion(self) -> Version:
        """ Get: IISVersion() -> Version """
        ...

    @property
    def IsOnUNCShare(self) -> bool:
        """ Get: IsOnUNCShare() -> bool """
        ...

    @property
    def MachineConfigurationDirectory(self) -> str:
        """ Get: MachineConfigurationDirectory() -> str """
        ...

    @property
    def TargetFramework(self) -> Version:
        """ Get: TargetFramework() -> Version """
        ...

    @property
    def UsingIntegratedPipeline(self) -> bool:
        """ Get: UsingIntegratedPipeline() -> bool """
        ...

    @property
    def WebObjectActivator(self) -> IServiceProvider:
        """
        Get: WebObjectActivator() -> IServiceProvider
        Set: WebObjectActivator() = value
        """
        ...


    @staticmethod
    def Close(): # -> 
        """ Close() """
        ...

    @staticmethod
    def GetNamedPermissionSet() -> NamedPermissionSet:
        """ GetNamedPermissionSet() -> NamedPermissionSet """
        ...

    @staticmethod
    def ProcessRequest(wr): # ->  # Not found arg types: {'wr': 'HttpWorkerRequest'}
        """ ProcessRequest(wr: HttpWorkerRequest) """
        ...

    @staticmethod
    def UnloadAppDomain(): # -> 
        """ UnloadAppDomain() """
        ...



class HttpServerUtility: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def MachineName(self) -> str:
        """ Get: MachineName(self: HttpServerUtility) -> str """
        ...

    @property
    def ScriptTimeout(self) -> int:
        """
        Get: ScriptTimeout(self: HttpServerUtility) -> int
        Set: ScriptTimeout(self: HttpServerUtility) = value
        """
        ...


    def ClearError(self): # -> 
        """ ClearError(self: HttpServerUtility) """
        ...

    def CreateObject(self, *__args:Type) -> object:
        """
        CreateObject(self: HttpServerUtility, type: Type) -> object
        CreateObject(self: HttpServerUtility, progID: str) -> object
        """
        ...

    def CreateObjectFromClsid(self, clsid:str) -> object:
        """ CreateObjectFromClsid(self: HttpServerUtility, clsid: str) -> object """
        ...

    def Execute(self, *__args:str): # -> 
        """ Execute(self: HttpServerUtility, path: str)Execute(self: HttpServerUtility, path: str, writer: TextWriter)Execute(self: HttpServerUtility, path: str, preserveForm: bool)Execute(self: HttpServerUtility, handler: IHttpHandler, writer: TextWriter, preserveForm: bool)Execute(self: HttpServerUtility, path: str, writer: TextWriter, preserveForm: bool) """
        ...

    def GetLastError(self) -> Exception:
        """ GetLastError(self: HttpServerUtility) -> Exception """
        ...

    def HtmlDecode(self, s:str, output:TextWriter = ...): # -> 
        """
        HtmlDecode(self: HttpServerUtility, s: str) -> str
        HtmlDecode(self: HttpServerUtility, s: str, output: TextWriter)
        """
        ...

    def HtmlEncode(self, s:str, output:TextWriter = ...): # -> 
        """
        HtmlEncode(self: HttpServerUtility, s: str) -> str
        HtmlEncode(self: HttpServerUtility, s: str, output: TextWriter)
        """
        ...

    def MapPath(self, path:str) -> str:
        """ MapPath(self: HttpServerUtility, path: str) -> str """
        ...

    def Transfer(self, *__args:str): # -> 
        """ Transfer(self: HttpServerUtility, path: str, preserveForm: bool)Transfer(self: HttpServerUtility, path: str)Transfer(self: HttpServerUtility, handler: IHttpHandler, preserveForm: bool) """
        ...

    def TransferRequest(self, path:str, preserveForm:bool = ..., method:str = ..., headers:NameValueCollection = ..., preserveUser:bool = ...): # -> 
        """ TransferRequest(self: HttpServerUtility, path: str)TransferRequest(self: HttpServerUtility, path: str, preserveForm: bool)TransferRequest(self: HttpServerUtility, path: str, preserveForm: bool, method: str, headers: NameValueCollection)TransferRequest(self: HttpServerUtility, path: str, preserveForm: bool, method: str, headers: NameValueCollection, preserveUser: bool) """
        ...

    def UrlDecode(self, s:str, output:TextWriter = ...): # -> 
        """
        UrlDecode(self: HttpServerUtility, s: str) -> str
        UrlDecode(self: HttpServerUtility, s: str, output: TextWriter)
        """
        ...

    def UrlEncode(self, s:str, output:TextWriter = ...): # -> 
        """
        UrlEncode(self: HttpServerUtility, s: str) -> str
        UrlEncode(self: HttpServerUtility, s: str, output: TextWriter)
        """
        ...

    def UrlPathEncode(self, s:str) -> str:
        """ UrlPathEncode(self: HttpServerUtility, s: str) -> str """
        ...

    @staticmethod
    def UrlTokenDecode(input:str) -> Array:
        """ UrlTokenDecode(input: str) -> Array[Byte] """
        ...

    @staticmethod
    def UrlTokenEncode(input:Array) -> str:
        """ UrlTokenEncode(input: Array[Byte]) -> str """
        ...


class HttpServerUtilityBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def MachineName(self) -> str:
        """ Get: MachineName(self: HttpServerUtilityBase) -> str """
        ...

    @property
    def ScriptTimeout(self) -> int:
        """
        Get: ScriptTimeout(self: HttpServerUtilityBase) -> int
        Set: ScriptTimeout(self: HttpServerUtilityBase) = value
        """
        ...


    def ClearError(self): # -> 
        """ ClearError(self: HttpServerUtilityBase) """
        ...

    def CreateObject(self, *__args:str) -> object:
        """
        CreateObject(self: HttpServerUtilityBase, progID: str) -> object
        CreateObject(self: HttpServerUtilityBase, type: Type) -> object
        """
        ...

    def CreateObjectFromClsid(self, clsid:str) -> object:
        """ CreateObjectFromClsid(self: HttpServerUtilityBase, clsid: str) -> object """
        ...

    def Execute(self, *__args:str): # -> 
        """ Execute(self: HttpServerUtilityBase, path: str)Execute(self: HttpServerUtilityBase, path: str, writer: TextWriter)Execute(self: HttpServerUtilityBase, path: str, preserveForm: bool)Execute(self: HttpServerUtilityBase, path: str, writer: TextWriter, preserveForm: bool)Execute(self: HttpServerUtilityBase, handler: IHttpHandler, writer: TextWriter, preserveForm: bool) """
        ...

    def GetLastError(self) -> Exception:
        """ GetLastError(self: HttpServerUtilityBase) -> Exception """
        ...

    def HtmlDecode(self, s:str, output:TextWriter = ...): # -> 
        """
        HtmlDecode(self: HttpServerUtilityBase, s: str) -> str
        HtmlDecode(self: HttpServerUtilityBase, s: str, output: TextWriter)
        """
        ...

    def HtmlEncode(self, s:str, output:TextWriter = ...): # -> 
        """
        HtmlEncode(self: HttpServerUtilityBase, s: str) -> str
        HtmlEncode(self: HttpServerUtilityBase, s: str, output: TextWriter)
        """
        ...

    def MapPath(self, path:str) -> str:
        """ MapPath(self: HttpServerUtilityBase, path: str) -> str """
        ...

    def Transfer(self, *__args:str): # -> 
        """ Transfer(self: HttpServerUtilityBase, path: str, preserveForm: bool)Transfer(self: HttpServerUtilityBase, path: str)Transfer(self: HttpServerUtilityBase, handler: IHttpHandler, preserveForm: bool) """
        ...

    def TransferRequest(self, path:str, preserveForm:bool = ..., method:str = ..., headers:NameValueCollection = ..., preserveUser:bool = ...): # -> 
        """ TransferRequest(self: HttpServerUtilityBase, path: str)TransferRequest(self: HttpServerUtilityBase, path: str, preserveForm: bool)TransferRequest(self: HttpServerUtilityBase, path: str, preserveForm: bool, method: str, headers: NameValueCollection)TransferRequest(self: HttpServerUtilityBase, path: str, preserveForm: bool, method: str, headers: NameValueCollection, preserveUser: bool) """
        ...

    def UrlDecode(self, s:str, output:TextWriter = ...): # -> 
        """
        UrlDecode(self: HttpServerUtilityBase, s: str) -> str
        UrlDecode(self: HttpServerUtilityBase, s: str, output: TextWriter)
        """
        ...

    def UrlEncode(self, s:str, output:TextWriter = ...): # -> 
        """
        UrlEncode(self: HttpServerUtilityBase, s: str) -> str
        UrlEncode(self: HttpServerUtilityBase, s: str, output: TextWriter)
        """
        ...

    def UrlPathEncode(self, s:str) -> str:
        """ UrlPathEncode(self: HttpServerUtilityBase, s: str) -> str """
        ...

    def UrlTokenDecode(self, input:str) -> Array:
        """ UrlTokenDecode(self: HttpServerUtilityBase, input: str) -> Array[Byte] """
        ...

    def UrlTokenEncode(self, input:Array) -> str:
        """ UrlTokenEncode(self: HttpServerUtilityBase, input: Array[Byte]) -> str """
        ...


class HttpServerUtilityWrapper(HttpServerUtilityBase): # skipped bases: <type 'object'>
    """ HttpServerUtilityWrapper(httpServerUtility: HttpServerUtility) """
    def __new__(cls, httpServerUtility:HttpServerUtility) -> Self:
        """ __new__(cls: type, httpServerUtility: HttpServerUtility) """
        ...


class HttpSessionStateBase(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def CodePage(self) -> int:
        """
        Get: CodePage(self: HttpSessionStateBase) -> int
        Set: CodePage(self: HttpSessionStateBase) = value
        """
        ...

    @property
    def Contents(self) -> HttpSessionStateBase:
        """ Get: Contents(self: HttpSessionStateBase) -> HttpSessionStateBase """
        ...

    @property
    def CookieMode(self) -> HttpCookieMode:
        """ Get: CookieMode(self: HttpSessionStateBase) -> HttpCookieMode """
        ...

    @property
    def IsCookieless(self) -> bool:
        """ Get: IsCookieless(self: HttpSessionStateBase) -> bool """
        ...

    @property
    def IsNewSession(self) -> bool:
        """ Get: IsNewSession(self: HttpSessionStateBase) -> bool """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: HttpSessionStateBase) -> bool """
        ...

    @property
    def Keys(self): # -> KeysCollection
        """ Get: Keys(self: HttpSessionStateBase) -> KeysCollection """
        ...

    @property
    def LCID(self) -> int:
        """
        Get: LCID(self: HttpSessionStateBase) -> int
        Set: LCID(self: HttpSessionStateBase) = value
        """
        ...

    @property
    def Mode(self) -> SessionStateMode:
        """ Get: Mode(self: HttpSessionStateBase) -> SessionStateMode """
        ...

    @property
    def SessionID(self) -> str:
        """ Get: SessionID(self: HttpSessionStateBase) -> str """
        ...

    @property
    def StaticObjects(self): # -> HttpStaticObjectsCollectionBase
        """ Get: StaticObjects(self: HttpSessionStateBase) -> HttpStaticObjectsCollectionBase """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: HttpSessionStateBase) -> int
        Set: Timeout(self: HttpSessionStateBase) = value
        """
        ...


    def Abandon(self): # -> 
        """ Abandon(self: HttpSessionStateBase) """
        ...

    def Add(self, name:str, value:object): # -> 
        """ Add(self: HttpSessionStateBase, name: str, value: object) """
        ...

    def Clear(self): # -> 
        """ Clear(self: HttpSessionStateBase) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: HttpSessionStateBase) -> IEnumerator """
        ...

    def Remove(self, name:str): # -> 
        """ Remove(self: HttpSessionStateBase, name: str) """
        ...

    def RemoveAll(self): # -> 
        """ RemoveAll(self: HttpSessionStateBase) """
        ...

    def RemoveAt(self, index:int): # -> 
        """ RemoveAt(self: HttpSessionStateBase, index: int) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]=x.__setitem__(i, y) <==> x[i]= """
        ...


class HttpSessionStateWrapper(HttpSessionStateBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ HttpSessionStateWrapper(httpSessionState: HttpSessionState) """
    def __new__(cls, httpSessionState:HttpSessionState) -> Self:
        """ __new__(cls: type, httpSessionState: HttpSessionState) """
        ...


class HttpStaticObjectsCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ HttpStaticObjectsCollection() """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: HttpStaticObjectsCollection) -> bool """
        ...

    @property
    def NeverAccessed(self) -> bool:
        """ Get: NeverAccessed(self: HttpStaticObjectsCollection) -> bool """
        ...


    @staticmethod
    def Deserialize(reader:BinaryReader) -> HttpStaticObjectsCollection:
        """ Deserialize(reader: BinaryReader) -> HttpStaticObjectsCollection """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: HttpStaticObjectsCollection) -> IEnumerator """
        ...

    def GetObject(self, name:str) -> object:
        """ GetObject(self: HttpStaticObjectsCollection, name: str) -> object """
        ...

    def Serialize(self, writer:BinaryWriter): # -> 
        """ Serialize(self: HttpStaticObjectsCollection, writer: BinaryWriter) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class HttpStaticObjectsCollectionBase(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: HttpStaticObjectsCollectionBase) -> bool """
        ...

    @property
    def NeverAccessed(self) -> bool:
        """ Get: NeverAccessed(self: HttpStaticObjectsCollectionBase) -> bool """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: HttpStaticObjectsCollectionBase) -> IEnumerator """
        ...

    def GetObject(self, name:str) -> object:
        """ GetObject(self: HttpStaticObjectsCollectionBase, name: str) -> object """
        ...

    def Serialize(self, writer:BinaryWriter): # -> 
        """ Serialize(self: HttpStaticObjectsCollectionBase, writer: BinaryWriter) """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class HttpStaticObjectsCollectionWrapper(HttpStaticObjectsCollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ HttpStaticObjectsCollectionWrapper(httpStaticObjectsCollection: HttpStaticObjectsCollection) """
    def __new__(cls, httpStaticObjectsCollection:HttpStaticObjectsCollection) -> Self:
        """ __new__(cls: type, httpStaticObjectsCollection: HttpStaticObjectsCollection) """
        ...


class HttpTaskAsyncHandler(IHttpAsyncHandler): # skipped bases: <type 'IHttpHandler'>, <type 'object'>
    """ no doc """
    @property
    def IsReusable(self) -> bool:
        """ Get: IsReusable(self: HttpTaskAsyncHandler) -> bool """
        ...


    def ProcessRequest(self, context:HttpContext): # -> 
        """ ProcessRequest(self: HttpTaskAsyncHandler, context: HttpContext) """
        ...

    def ProcessRequestAsync(self, context:HttpContext) -> Task:
        """ ProcessRequestAsync(self: HttpTaskAsyncHandler, context: HttpContext) -> Task """
        ...


class HttpUnhandledException(HttpException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    HttpUnhandledException()
    HttpUnhandledException(message: str)
    HttpUnhandledException(message: str, innerException: Exception)
    """
    SerializeObjectState = ...


class HttpUtility: # skipped bases: <type 'object'>, <type 'object'>
    """ HttpUtility() """
    @staticmethod
    def HtmlAttributeEncode(s:str, output:TextWriter = ...): # -> 
        """
        HtmlAttributeEncode(s: str) -> str
        HtmlAttributeEncode(s: str, output: TextWriter)
        """
        ...

    @staticmethod
    def HtmlDecode(s:str, output:TextWriter = ...): # -> 
        """
        HtmlDecode(s: str) -> str
        HtmlDecode(s: str, output: TextWriter)
        """
        ...

    @staticmethod
    def HtmlEncode(*__args:str) -> str:
        """
        HtmlEncode(s: str) -> str
        HtmlEncode(value: object) -> str
        HtmlEncode(s: str, output: TextWriter)
        """
        ...

    @staticmethod
    def JavaScriptStringEncode(value:str, addDoubleQuotes:bool = ...) -> str:
        """
        JavaScriptStringEncode(value: str) -> str
        JavaScriptStringEncode(value: str, addDoubleQuotes: bool) -> str
        """
        ...

    @staticmethod
    def ParseQueryString(query:str, encoding:Encoding = ...) -> NameValueCollection:
        """
        ParseQueryString(query: str) -> NameValueCollection
        ParseQueryString(query: str, encoding: Encoding) -> NameValueCollection
        """
        ...

    @staticmethod
    def UrlDecode(*__args:str) -> str:
        """
        UrlDecode(str: str) -> str
        UrlDecode(str: str, e: Encoding) -> str
        UrlDecode(bytes: Array[Byte], e: Encoding) -> str
        UrlDecode(bytes: Array[Byte], offset: int, count: int, e: Encoding) -> str
        """
        ...

    @staticmethod
    def UrlDecodeToBytes(*__args:str) -> Array:
        """
        UrlDecodeToBytes(str: str) -> Array[Byte]
        UrlDecodeToBytes(str: str, e: Encoding) -> Array[Byte]
        UrlDecodeToBytes(bytes: Array[Byte]) -> Array[Byte]
        UrlDecodeToBytes(bytes: Array[Byte], offset: int, count: int) -> Array[Byte]
        """
        ...

    @staticmethod
    def UrlEncode(*__args:str) -> str:
        """
        UrlEncode(str: str) -> str
        UrlEncode(str: str, e: Encoding) -> str
        UrlEncode(bytes: Array[Byte]) -> str
        UrlEncode(bytes: Array[Byte], offset: int, count: int) -> str
        """
        ...

    @staticmethod
    def UrlEncodeToBytes(*__args:str) -> Array:
        """
        UrlEncodeToBytes(str: str) -> Array[Byte]
        UrlEncodeToBytes(str: str, e: Encoding) -> Array[Byte]
        UrlEncodeToBytes(bytes: Array[Byte]) -> Array[Byte]
        UrlEncodeToBytes(bytes: Array[Byte], offset: int, count: int) -> Array[Byte]
        """
        ...

    @staticmethod
    def UrlEncodeUnicode(str:str) -> str:
        """ UrlEncodeUnicode(str: str) -> str """
        ...

    @staticmethod
    def UrlEncodeUnicodeToBytes(str:str) -> Array:
        """ UrlEncodeUnicodeToBytes(str: str) -> Array[Byte] """
        ...

    @staticmethod
    def UrlPathEncode(str:str) -> str:
        """ UrlPathEncode(str: str) -> str """
        ...


class HttpValidationStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HttpValidationStatus, values: IgnoreThisRequest (2), Invalid (1), Valid (3) """
    IgnoreThisRequest: HttpValidationStatus = ...
    Invalid: HttpValidationStatus = ...
    Valid: HttpValidationStatus = ...
    value__ = ...


class HttpWorkerRequest: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def MachineConfigPath(self) -> str:
        """ Get: MachineConfigPath(self: HttpWorkerRequest) -> str """
        ...

    @property
    def MachineInstallDirectory(self) -> str:
        """ Get: MachineInstallDirectory(self: HttpWorkerRequest) -> str """
        ...

    @property
    def RequestTraceIdentifier(self) -> Guid:
        """ Get: RequestTraceIdentifier(self: HttpWorkerRequest) -> Guid """
        ...

    @property
    def RootWebConfigPath(self) -> str:
        """ Get: RootWebConfigPath(self: HttpWorkerRequest) -> str """
        ...

    @property
    def SupportsAsyncFlush(self) -> bool:
        """ Get: SupportsAsyncFlush(self: HttpWorkerRequest) -> bool """
        ...

    @property
    def SupportsAsyncRead(self) -> bool:
        """ Get: SupportsAsyncRead(self: HttpWorkerRequest) -> bool """
        ...


    def BeginFlush(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginFlush(self: HttpWorkerRequest, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginRead(self, buffer:Array, offset:int, count:int, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginRead(self: HttpWorkerRequest, buffer: Array[Byte], offset: int, count: int, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def CloseConnection(self): # -> 
        """ CloseConnection(self: HttpWorkerRequest) """
        ...

    def EndFlush(self, asyncResult:IAsyncResult): # -> 
        """ EndFlush(self: HttpWorkerRequest, asyncResult: IAsyncResult) """
        ...

    def EndOfRequest(self): # -> 
        """ EndOfRequest(self: HttpWorkerRequest) """
        ...

    def EndOfSendNotification(self, *args): #cannot find CLR method
        """ EndOfSendNotification(object: object, method: IntPtr) """
        ...

    def EndRead(self, asyncResult:IAsyncResult) -> int:
        """ EndRead(self: HttpWorkerRequest, asyncResult: IAsyncResult) -> int """
        ...

    def FlushResponse(self, finalFlush:bool): # -> 
        """ FlushResponse(self: HttpWorkerRequest, finalFlush: bool) """
        ...

    def GetAppPath(self) -> str:
        """ GetAppPath(self: HttpWorkerRequest) -> str """
        ...

    def GetAppPathTranslated(self) -> str:
        """ GetAppPathTranslated(self: HttpWorkerRequest) -> str """
        ...

    def GetAppPoolID(self) -> str:
        """ GetAppPoolID(self: HttpWorkerRequest) -> str """
        ...

    def GetBytesRead(self) -> Int64:
        """ GetBytesRead(self: HttpWorkerRequest) -> Int64 """
        ...

    def GetClientCertificate(self) -> Array:
        """ GetClientCertificate(self: HttpWorkerRequest) -> Array[Byte] """
        ...

    def GetClientCertificateBinaryIssuer(self) -> Array:
        """ GetClientCertificateBinaryIssuer(self: HttpWorkerRequest) -> Array[Byte] """
        ...

    def GetClientCertificateEncoding(self) -> int:
        """ GetClientCertificateEncoding(self: HttpWorkerRequest) -> int """
        ...

    def GetClientCertificatePublicKey(self) -> Array:
        """ GetClientCertificatePublicKey(self: HttpWorkerRequest) -> Array[Byte] """
        ...

    def GetClientCertificateValidFrom(self) -> DateTime:
        """ GetClientCertificateValidFrom(self: HttpWorkerRequest) -> DateTime """
        ...

    def GetClientCertificateValidUntil(self) -> DateTime:
        """ GetClientCertificateValidUntil(self: HttpWorkerRequest) -> DateTime """
        ...

    def GetConnectionID(self) -> Int64:
        """ GetConnectionID(self: HttpWorkerRequest) -> Int64 """
        ...

    def GetFilePath(self) -> str:
        """ GetFilePath(self: HttpWorkerRequest) -> str """
        ...

    def GetFilePathTranslated(self) -> str:
        """ GetFilePathTranslated(self: HttpWorkerRequest) -> str """
        ...

    def GetHttpVerbName(self) -> str:
        """ GetHttpVerbName(self: HttpWorkerRequest) -> str """
        ...

    def GetHttpVersion(self) -> str:
        """ GetHttpVersion(self: HttpWorkerRequest) -> str """
        ...

    def GetKnownRequestHeader(self, index:int) -> str:
        """ GetKnownRequestHeader(self: HttpWorkerRequest, index: int) -> str """
        ...

    @staticmethod
    def GetKnownRequestHeaderIndex(header:str) -> int:
        """ GetKnownRequestHeaderIndex(header: str) -> int """
        ...

    @staticmethod
    def GetKnownRequestHeaderName(index:int) -> str:
        """ GetKnownRequestHeaderName(index: int) -> str """
        ...

    @staticmethod
    def GetKnownResponseHeaderIndex(header:str) -> int:
        """ GetKnownResponseHeaderIndex(header: str) -> int """
        ...

    @staticmethod
    def GetKnownResponseHeaderName(index:int) -> str:
        """ GetKnownResponseHeaderName(index: int) -> str """
        ...

    def GetLocalAddress(self) -> str:
        """ GetLocalAddress(self: HttpWorkerRequest) -> str """
        ...

    def GetLocalPort(self) -> int:
        """ GetLocalPort(self: HttpWorkerRequest) -> int """
        ...

    def GetPathInfo(self) -> str:
        """ GetPathInfo(self: HttpWorkerRequest) -> str """
        ...

    def GetPreloadedEntityBody(self, buffer:Array = ..., offset:int = ...) -> int:
        """
        GetPreloadedEntityBody(self: HttpWorkerRequest, buffer: Array[Byte], offset: int) -> int
        GetPreloadedEntityBody(self: HttpWorkerRequest) -> Array[Byte]
        """
        ...

    def GetPreloadedEntityBodyLength(self) -> int:
        """ GetPreloadedEntityBodyLength(self: HttpWorkerRequest) -> int """
        ...

    def GetProtocol(self) -> str:
        """ GetProtocol(self: HttpWorkerRequest) -> str """
        ...

    def GetQueryString(self) -> str:
        """ GetQueryString(self: HttpWorkerRequest) -> str """
        ...

    def GetQueryStringRawBytes(self) -> Array:
        """ GetQueryStringRawBytes(self: HttpWorkerRequest) -> Array[Byte] """
        ...

    def GetRawUrl(self) -> str:
        """ GetRawUrl(self: HttpWorkerRequest) -> str """
        ...

    def GetRemoteAddress(self) -> str:
        """ GetRemoteAddress(self: HttpWorkerRequest) -> str """
        ...

    def GetRemoteName(self) -> str:
        """ GetRemoteName(self: HttpWorkerRequest) -> str """
        ...

    def GetRemotePort(self) -> int:
        """ GetRemotePort(self: HttpWorkerRequest) -> int """
        ...

    def GetRequestReason(self) -> int:
        """ GetRequestReason(self: HttpWorkerRequest) -> int """
        ...

    def GetServerName(self) -> str:
        """ GetServerName(self: HttpWorkerRequest) -> str """
        ...

    def GetServerVariable(self, name:str) -> str:
        """ GetServerVariable(self: HttpWorkerRequest, name: str) -> str """
        ...

    @staticmethod
    def GetStatusDescription(code:int) -> str:
        """ GetStatusDescription(code: int) -> str """
        ...

    def GetTotalEntityBodyLength(self) -> int:
        """ GetTotalEntityBodyLength(self: HttpWorkerRequest) -> int """
        ...

    def GetUnknownRequestHeader(self, name:str) -> str:
        """ GetUnknownRequestHeader(self: HttpWorkerRequest, name: str) -> str """
        ...

    def GetUnknownRequestHeaders(self) -> Array:
        """ GetUnknownRequestHeaders(self: HttpWorkerRequest) -> Array[Array[str]] """
        ...

    def GetUriPath(self) -> str:
        """ GetUriPath(self: HttpWorkerRequest) -> str """
        ...

    def GetUrlContextID(self) -> Int64:
        """ GetUrlContextID(self: HttpWorkerRequest) -> Int64 """
        ...

    def GetUserToken(self) -> IntPtr:
        """ GetUserToken(self: HttpWorkerRequest) -> IntPtr """
        ...

    def GetVirtualPathToken(self) -> IntPtr:
        """ GetVirtualPathToken(self: HttpWorkerRequest) -> IntPtr """
        ...

    def HasEntityBody(self) -> bool:
        """ HasEntityBody(self: HttpWorkerRequest) -> bool """
        ...

    def HeadersSent(self) -> bool:
        """ HeadersSent(self: HttpWorkerRequest) -> bool """
        ...

    def IsClientConnected(self) -> bool:
        """ IsClientConnected(self: HttpWorkerRequest) -> bool """
        ...

    def IsEntireEntityBodyIsPreloaded(self) -> bool:
        """ IsEntireEntityBodyIsPreloaded(self: HttpWorkerRequest) -> bool """
        ...

    def IsSecure(self) -> bool:
        """ IsSecure(self: HttpWorkerRequest) -> bool """
        ...

    def MapPath(self, virtualPath:str) -> str:
        """ MapPath(self: HttpWorkerRequest, virtualPath: str) -> str """
        ...

    def ReadEntityBody(self, buffer:Array, *__args:int) -> int:
        """
        ReadEntityBody(self: HttpWorkerRequest, buffer: Array[Byte], size: int) -> int
        ReadEntityBody(self: HttpWorkerRequest, buffer: Array[Byte], offset: int, size: int) -> int
        """
        ...

    def SendCalculatedContentLength(self, contentLength:int): # -> 
        """ SendCalculatedContentLength(self: HttpWorkerRequest, contentLength: int)SendCalculatedContentLength(self: HttpWorkerRequest, contentLength: Int64) """
        ...

    def SendKnownResponseHeader(self, index:int, value:str): # -> 
        """ SendKnownResponseHeader(self: HttpWorkerRequest, index: int, value: str) """
        ...

    def SendResponseFromFile(self, *__args): # -> 
        """ SendResponseFromFile(self: HttpWorkerRequest, filename: str, offset: Int64, length: Int64)SendResponseFromFile(self: HttpWorkerRequest, handle: IntPtr, offset: Int64, length: Int64) """
        ...

    def SendResponseFromMemory(self, data:Array, length:int): # -> 
        """ SendResponseFromMemory(self: HttpWorkerRequest, data: Array[Byte], length: int)SendResponseFromMemory(self: HttpWorkerRequest, data: IntPtr, length: int) """
        ...

    def SendStatus(self, statusCode:int, statusDescription:str): # -> 
        """ SendStatus(self: HttpWorkerRequest, statusCode: int, statusDescription: str) """
        ...

    def SendUnknownResponseHeader(self, name:str, value:str): # -> 
        """ SendUnknownResponseHeader(self: HttpWorkerRequest, name: str, value: str) """
        ...

    def SetEndOfSendNotification(self, callback, extraData:object): # ->  # Not found arg types: {'callback': 'EndOfSendNotification'}
        """ SetEndOfSendNotification(self: HttpWorkerRequest, callback: EndOfSendNotification, extraData: object) """
        ...

    HeaderAccept: int = ...
    HeaderAcceptCharset: int = ...
    HeaderAcceptEncoding: int = ...
    HeaderAcceptLanguage: int = ...
    HeaderAcceptRanges: int = ...
    HeaderAge: int = ...
    HeaderAllow: int = ...
    HeaderAuthorization: int = ...
    HeaderCacheControl: int = ...
    HeaderConnection: int = ...
    HeaderContentEncoding: int = ...
    HeaderContentLanguage: int = ...
    HeaderContentLength: int = ...
    HeaderContentLocation: int = ...
    HeaderContentMd5: int = ...
    HeaderContentRange: int = ...
    HeaderContentType: int = ...
    HeaderCookie: int = ...
    HeaderDate: int = ...
    HeaderEtag: int = ...
    HeaderExpect: int = ...
    HeaderExpires: int = ...
    HeaderFrom: int = ...
    HeaderHost: int = ...
    HeaderIfMatch: int = ...
    HeaderIfModifiedSince: int = ...
    HeaderIfNoneMatch: int = ...
    HeaderIfRange: int = ...
    HeaderIfUnmodifiedSince: int = ...
    HeaderKeepAlive: int = ...
    HeaderLastModified: int = ...
    HeaderLocation: int = ...
    HeaderMaxForwards: int = ...
    HeaderPragma: int = ...
    HeaderProxyAuthenticate: int = ...
    HeaderProxyAuthorization: int = ...
    HeaderRange: int = ...
    HeaderReferer: int = ...
    HeaderRetryAfter: int = ...
    HeaderServer: int = ...
    HeaderSetCookie: int = ...
    HeaderTe: int = ...
    HeaderTrailer: int = ...
    HeaderTransferEncoding: int = ...
    HeaderUpgrade: int = ...
    HeaderUserAgent: int = ...
    HeaderVary: int = ...
    HeaderVia: int = ...
    HeaderWarning: int = ...
    HeaderWwwAuthenticate: int = ...
    ReasonCachePolicy: int = ...
    ReasonCacheSecurity: int = ...
    ReasonClientDisconnect: int = ...
    ReasonDefault: int = ...
    ReasonFileHandleCacheMiss: int = ...
    ReasonResponseCacheMiss: int = ...
    RequestHeaderMaximum: int = ...
    ResponseHeaderMaximum: int = ...


class HttpWriter(TextWriter): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def OutputStream(self) -> Stream:
        """ Get: OutputStream(self: HttpWriter) -> Stream """
        ...


    def WriteBytes(self, buffer:Array, index:int, count:int): # -> 
        """ WriteBytes(self: HttpWriter, buffer: Array[Byte], index: int, count: int) """
        ...

    def WriteString(self, s:str, index:int, count:int): # -> 
        """ WriteString(self: HttpWriter, s: str, index: int, count: int) """
        ...

    CoreNewLine = ...


class IHtmlString: # skipped bases: <type 'object'>
    """ no doc """
    def ToHtmlString(self) -> str:
        """ ToHtmlString(self: IHtmlString) -> str """
        ...


class IHttpHandlerFactory: # skipped bases: <type 'object'>
    """ no doc """
    def GetHandler(self, context:HttpContext, requestType:str, url:str, pathTranslated:str) -> IHttpHandler:
        """ GetHandler(self: IHttpHandlerFactory, context: HttpContext, requestType: str, url: str, pathTranslated: str) -> IHttpHandler """
        ...

    def ReleaseHandler(self, handler:IHttpHandler): # -> 
        """ ReleaseHandler(self: IHttpHandlerFactory, handler: IHttpHandler) """
        ...


class IHttpModule: # skipped bases: <type 'object'>
    """ no doc """
    def Dispose(self): # -> 
        """ Dispose(self: IHttpModule) """
        ...

    def Init(self, context:HttpApplication): # -> 
        """ Init(self: IHttpModule, context: HttpApplication) """
        ...


class IisTraceListener(TraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ IisTraceListener() """
    pass

class IPartitionResolver: # skipped bases: <type 'object'>
    """ no doc """
    def Initialize(self): # -> 
        """ Initialize(self: IPartitionResolver) """
        ...

    def ResolvePartition(self, key:object) -> str:
        """ ResolvePartition(self: IPartitionResolver, key: object) -> str """
        ...


class ISubscriptionToken: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsActive(self) -> bool:
        """ Get: IsActive(self: ISubscriptionToken) -> bool """
        ...


    def Unsubscribe(self): # -> 
        """ Unsubscribe(self: ISubscriptionToken) """
        ...


class ITlsTokenBindingInfo: # skipped bases: <type 'object'>
    """ no doc """
    def GetProvidedTokenBindingId(self) -> Array:
        """ GetProvidedTokenBindingId(self: ITlsTokenBindingInfo) -> Array[Byte] """
        ...

    def GetReferredTokenBindingId(self) -> Array:
        """ GetReferredTokenBindingId(self: ITlsTokenBindingInfo) -> Array[Byte] """
        ...


class MimeMapping: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def GetMimeMapping(fileName:str) -> str:
        """ GetMimeMapping(fileName: str) -> str """
        ...

    __all__: list = ...


class ParserError: # skipped bases: <type 'object'>, <type 'object'>
    """
    ParserError()
    ParserError(errorText: str, virtualPath: str, line: int)
    """
    @property
    def ErrorText(self) -> str:
        """
        Get: ErrorText(self: ParserError) -> str
        Set: ErrorText(self: ParserError) = value
        """
        ...

    @property
    def Line(self) -> int:
        """
        Get: Line(self: ParserError) -> int
        Set: Line(self: ParserError) = value
        """
        ...

    @property
    def VirtualPath(self) -> str:
        """
        Get: VirtualPath(self: ParserError) -> str
        Set: VirtualPath(self: ParserError) = value
        """
        ...



class ParserErrorCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """
    ParserErrorCollection()
    ParserErrorCollection(value: Array[ParserError])
    """
    def Add(self, value:ParserError) -> int:
        """ Add(self: ParserErrorCollection, value: ParserError) -> int """
        ...

    def AddRange(self, value:Array): # -> 
        """ AddRange(self: ParserErrorCollection, value: Array[ParserError])AddRange(self: ParserErrorCollection, value: ParserErrorCollection) """
        ...

    def Contains(self, value:ParserError) -> bool:
        """ Contains(self: ParserErrorCollection, value: ParserError) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: ParserErrorCollection, array: Array[ParserError], index: int) """
        ...

    def IndexOf(self, value:ParserError) -> int:
        """ IndexOf(self: ParserErrorCollection, value: ParserError) -> int """
        ...

    def Insert(self, index:int, value:ParserError): # -> 
        """ Insert(self: ParserErrorCollection, index: int, value: ParserError) """
        ...

    def Remove(self, value:ParserError): # -> 
        """ Remove(self: ParserErrorCollection, value: ParserError) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class PreApplicationStartMethodAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ PreApplicationStartMethodAttribute(type: Type, methodName: str) """
    @property
    def MethodName(self) -> str:
        """ Get: MethodName(self: PreApplicationStartMethodAttribute) -> str """
        ...

    @property
    def Type(self) -> Type:
        """ Get: Type(self: PreApplicationStartMethodAttribute) -> Type """
        ...


    def __new__(cls, type:Type, methodName:str) -> Self:
        """ __new__(cls: type, type: Type, methodName: str) """
        ...


class ProcessInfo: # skipped bases: <type 'object'>, <type 'object'>
    """
    ProcessInfo(startTime: DateTime, age: TimeSpan, processID: int, requestCount: int, status: ProcessStatus, shutdownReason: ProcessShutdownReason, peakMemoryUsed: int)
    ProcessInfo()
    """
    @property
    def Age(self) -> TimeSpan:
        """ Get: Age(self: ProcessInfo) -> TimeSpan """
        ...

    @property
    def PeakMemoryUsed(self) -> int:
        """ Get: PeakMemoryUsed(self: ProcessInfo) -> int """
        ...

    @property
    def ProcessID(self) -> int:
        """ Get: ProcessID(self: ProcessInfo) -> int """
        ...

    @property
    def RequestCount(self) -> int:
        """ Get: RequestCount(self: ProcessInfo) -> int """
        ...

    @property
    def ShutdownReason(self): # -> ProcessShutdownReason
        """ Get: ShutdownReason(self: ProcessInfo) -> ProcessShutdownReason """
        ...

    @property
    def StartTime(self) -> DateTime:
        """ Get: StartTime(self: ProcessInfo) -> DateTime """
        ...

    @property
    def Status(self): # -> ProcessStatus
        """ Get: Status(self: ProcessInfo) -> ProcessStatus """
        ...


    def SetAll(self, startTime:DateTime, age:TimeSpan, processID:int, requestCount:int, status, shutdownReason, peakMemoryUsed:int): # ->  # Not found arg types: {'shutdownReason': 'ProcessShutdownReason', 'status': 'ProcessStatus'}
        """ SetAll(self: ProcessInfo, startTime: DateTime, age: TimeSpan, processID: int, requestCount: int, status: ProcessStatus, shutdownReason: ProcessShutdownReason, peakMemoryUsed: int) """
        ...


class ProcessModelInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ ProcessModelInfo() """
    @staticmethod
    def GetCurrentProcessInfo() -> ProcessInfo:
        """ GetCurrentProcessInfo() -> ProcessInfo """
        ...

    @staticmethod
    def GetHistory(numRecords:int) -> Array:
        """ GetHistory(numRecords: int) -> Array[ProcessInfo] """
        ...


class ProcessShutdownReason(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProcessShutdownReason, values: DeadlockSuspected (8), IdleTimeout (5), MemoryLimitExceeded (6), None (0), PingFailed (7), RequestQueueLimit (3), RequestsLimit (2), Timeout (4), Unexpected (1) """
    DeadlockSuspected: ProcessShutdownReason = ...
    IdleTimeout: ProcessShutdownReason = ...
    MemoryLimitExceeded: ProcessShutdownReason = ...
    PingFailed: ProcessShutdownReason = ...
    RequestQueueLimit: ProcessShutdownReason = ...
    RequestsLimit: ProcessShutdownReason = ...
    Timeout: ProcessShutdownReason = ...
    Unexpected: ProcessShutdownReason = ...
    value__ = ...


class ProcessStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ProcessStatus, values: Alive (1), ShutDown (3), ShuttingDown (2), Terminated (4) """
    Alive: ProcessStatus = ...
    ShutDown: ProcessStatus = ...
    ShuttingDown: ProcessStatus = ...
    Terminated: ProcessStatus = ...
    value__ = ...


class ReadEntityBodyMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ReadEntityBodyMode, values: Buffered (3), Bufferless (2), Classic (1), None (0) """
    Buffered: ReadEntityBodyMode = ...
    Bufferless: ReadEntityBodyMode = ...
    Classic: ReadEntityBodyMode = ...
    value__ = ...


class RequestNotification(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) RequestNotification, values: AcquireRequestState (32), AuthenticateRequest (2), AuthorizeRequest (4), BeginRequest (1), EndRequest (2048), ExecuteRequestHandler (128), LogRequest (1024), MapRequestHandler (16), PreExecuteRequestHandler (64), ReleaseRequestState (256), ResolveRequestCache (8), SendResponse (536870912), UpdateRequestCache (512) """
    AcquireRequestState: RequestNotification = ...
    AuthenticateRequest: RequestNotification = ...
    AuthorizeRequest: RequestNotification = ...
    BeginRequest: RequestNotification = ...
    EndRequest: RequestNotification = ...
    ExecuteRequestHandler: RequestNotification = ...
    LogRequest: RequestNotification = ...
    MapRequestHandler: RequestNotification = ...
    PreExecuteRequestHandler: RequestNotification = ...
    ReleaseRequestState: RequestNotification = ...
    ResolveRequestCache: RequestNotification = ...
    SendResponse: RequestNotification = ...
    UpdateRequestCache: RequestNotification = ...
    value__ = ...


class RequestNotificationStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RequestNotificationStatus, values: Continue (0), FinishRequest (2), Pending (1) """
    Continue: RequestNotificationStatus = ...
    FinishRequest: RequestNotificationStatus = ...
    Pending: RequestNotificationStatus = ...
    value__ = ...


class SameSiteMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SameSiteMode, values: Lax (1), None (0), Strict (2) """
    Lax: SameSiteMode = ...
    Strict: SameSiteMode = ...
    value__ = ...


class SiteMap: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CurrentNode(self): # -> SiteMapNode
        """ Get: CurrentNode() -> SiteMapNode """
        ...

    @property
    def Enabled(self) -> bool:
        """ Get: Enabled() -> bool """
        ...

    @property
    def Provider(self): # -> SiteMapProvider
        """ Get: Provider() -> SiteMapProvider """
        ...

    @property
    def Providers(self): # -> SiteMapProviderCollection
        """ Get: Providers() -> SiteMapProviderCollection """
        ...

    @property
    def RootNode(self): # -> SiteMapNode
        """ Get: RootNode() -> SiteMapNode """
        ...


    SiteMapResolve = ...
    __all__: list = ...


class SiteMapNode(INavigateUIData, ICloneable, IHierarchyData): # skipped bases: <type 'object'>
    """
    SiteMapNode(provider: SiteMapProvider, key: str)
    SiteMapNode(provider: SiteMapProvider, key: str, url: str)
    SiteMapNode(provider: SiteMapProvider, key: str, url: str, title: str)
    SiteMapNode(provider: SiteMapProvider, key: str, url: str, title: str, description: str)
    SiteMapNode(provider: SiteMapProvider, key: str, url: str, title: str, description: str, roles: IList, attributes: NameValueCollection, explicitResourceKeys: NameValueCollection, implicitResourceKey: str)
    """
    @property
    def Attributes(self):
        ...

    @property
    def ChildNodes(self): # -> SiteMapNodeCollection
        """
        Get: ChildNodes(self: SiteMapNode) -> SiteMapNodeCollection
        Set: ChildNodes(self: SiteMapNode) = value
        """
        ...

    @property
    def HasChildNodes(self) -> bool:
        """ Get: HasChildNodes(self: SiteMapNode) -> bool """
        ...

    @property
    def Key(self) -> str:
        """ Get: Key(self: SiteMapNode) -> str """
        ...

    @property
    def NextSibling(self) -> SiteMapNode:
        """ Get: NextSibling(self: SiteMapNode) -> SiteMapNode """
        ...

    @property
    def ParentNode(self) -> SiteMapNode:
        """
        Get: ParentNode(self: SiteMapNode) -> SiteMapNode
        Set: ParentNode(self: SiteMapNode) = value
        """
        ...

    @property
    def PreviousSibling(self) -> SiteMapNode:
        """ Get: PreviousSibling(self: SiteMapNode) -> SiteMapNode """
        ...

    @property
    def Provider(self): # -> SiteMapProvider
        """ Get: Provider(self: SiteMapNode) -> SiteMapProvider """
        ...

    @property
    def ReadOnly(self) -> bool:
        """
        Get: ReadOnly(self: SiteMapNode) -> bool
        Set: ReadOnly(self: SiteMapNode) = value
        """
        ...

    @property
    def ResourceKey(self) -> str:
        """
        Get: ResourceKey(self: SiteMapNode) -> str
        Set: ResourceKey(self: SiteMapNode) = value
        """
        ...

    @property
    def Roles(self) -> IList:
        """
        Get: Roles(self: SiteMapNode) -> IList
        Set: Roles(self: SiteMapNode) = value
        """
        ...

    @property
    def RootNode(self) -> SiteMapNode:
        """ Get: RootNode(self: SiteMapNode) -> SiteMapNode """
        ...

    @property
    def Title(self) -> str:
        """
        Get: Title(self: SiteMapNode) -> str
        Set: Title(self: SiteMapNode) = value
        """
        ...

    @property
    def Url(self) -> str:
        """
        Get: Url(self: SiteMapNode) -> str
        Set: Url(self: SiteMapNode) = value
        """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: SiteMapNode, obj: object) -> bool """
        ...

    def GetAllNodes(self): # -> SiteMapNodeCollection
        """ GetAllNodes(self: SiteMapNode) -> SiteMapNodeCollection """
        ...

    def GetDataSourceView(self, owner, viewName:str): # -> SiteMapDataSourceView # Not found arg types: {'owner': 'SiteMapDataSource'}
        """ GetDataSourceView(self: SiteMapNode, owner: SiteMapDataSource, viewName: str) -> SiteMapDataSourceView """
        ...

    def GetExplicitResourceString(self, *args): #cannot find CLR method
        """ GetExplicitResourceString(self: SiteMapNode, attributeName: str, defaultValue: str, throwIfNotFound: bool) -> str """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SiteMapNode) -> int """
        ...

    def GetHierarchicalDataSourceView(self): # -> SiteMapHierarchicalDataSourceView
        """ GetHierarchicalDataSourceView(self: SiteMapNode) -> SiteMapHierarchicalDataSourceView """
        ...

    def GetImplicitResourceString(self, *args): #cannot find CLR method
        """ GetImplicitResourceString(self: SiteMapNode, attributeName: str) -> str """
        ...

    def IsAccessibleToUser(self, context:HttpContext) -> bool:
        """ IsAccessibleToUser(self: SiteMapNode, context: HttpContext) -> bool """
        ...

    def IsDescendantOf(self, node:SiteMapNode) -> bool:
        """ IsDescendantOf(self: SiteMapNode, node: SiteMapNode) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: SiteMapNode) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class SiteMapNodeCollection(IList, IHierarchicalEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    SiteMapNodeCollection()
    SiteMapNodeCollection(capacity: int)
    SiteMapNodeCollection(value: SiteMapNode)
    SiteMapNodeCollection(value: Array[SiteMapNode])
    SiteMapNodeCollection(value: SiteMapNodeCollection)
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: SiteMapNodeCollection) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: SiteMapNodeCollection) -> bool """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: SiteMapNodeCollection) -> object """
        ...


    def AddRange(self, value:Array): # -> 
        """ AddRange(self: SiteMapNodeCollection, value: Array[SiteMapNode])AddRange(self: SiteMapNodeCollection, value: SiteMapNodeCollection) """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: SiteMapNodeCollection, array: Array[SiteMapNode], index: int) """
        ...

    def GetDataSourceView(self, owner, viewName:str): # -> SiteMapDataSourceView # Not found arg types: {'owner': 'SiteMapDataSource'}
        """ GetDataSourceView(self: SiteMapNodeCollection, owner: SiteMapDataSource, viewName: str) -> SiteMapDataSourceView """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: SiteMapNodeCollection) -> IEnumerator """
        ...

    def GetHierarchicalDataSourceView(self): # -> SiteMapHierarchicalDataSourceView
        """ GetHierarchicalDataSourceView(self: SiteMapNodeCollection) -> SiteMapHierarchicalDataSourceView """
        ...

    def OnValidate(self, *args): #cannot find CLR method
        """ OnValidate(self: SiteMapNodeCollection, value: object) """
        ...

    @staticmethod
    def ReadOnly(collection:SiteMapNodeCollection) -> SiteMapNodeCollection:
        """ ReadOnly(collection: SiteMapNodeCollection) -> SiteMapNodeCollection """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ Contains(self: IList, value: object) -> bool """
        ...


class SiteMapProvider(ProviderBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CurrentNode(self) -> SiteMapNode:
        """ Get: CurrentNode(self: SiteMapProvider) -> SiteMapNode """
        ...

    @property
    def EnableLocalization(self) -> bool:
        """
        Get: EnableLocalization(self: SiteMapProvider) -> bool
        Set: EnableLocalization(self: SiteMapProvider) = value
        """
        ...

    @property
    def ParentProvider(self) -> SiteMapProvider:
        """
        Get: ParentProvider(self: SiteMapProvider) -> SiteMapProvider
        Set: ParentProvider(self: SiteMapProvider) = value
        """
        ...

    @property
    def ResourceKey(self) -> str:
        """
        Get: ResourceKey(self: SiteMapProvider) -> str
        Set: ResourceKey(self: SiteMapProvider) = value
        """
        ...

    @property
    def RootNode(self) -> SiteMapNode:
        """ Get: RootNode(self: SiteMapProvider) -> SiteMapNode """
        ...

    @property
    def RootProvider(self) -> SiteMapProvider:
        """ Get: RootProvider(self: SiteMapProvider) -> SiteMapProvider """
        ...

    @property
    def SecurityTrimmingEnabled(self) -> bool:
        """ Get: SecurityTrimmingEnabled(self: SiteMapProvider) -> bool """
        ...


    def AddNode(self, *args): #cannot find CLR method
        """ AddNode(self: SiteMapProvider, node: SiteMapNode)AddNode(self: SiteMapProvider, node: SiteMapNode, parentNode: SiteMapNode) """
        ...

    def FindSiteMapNode(self, *__args:HttpContext) -> SiteMapNode:
        """
        FindSiteMapNode(self: SiteMapProvider, context: HttpContext) -> SiteMapNode
        FindSiteMapNode(self: SiteMapProvider, rawUrl: str) -> SiteMapNode
        """
        ...

    def FindSiteMapNodeFromKey(self, key:str) -> SiteMapNode:
        """ FindSiteMapNodeFromKey(self: SiteMapProvider, key: str) -> SiteMapNode """
        ...

    def GetChildNodes(self, node:SiteMapNode) -> SiteMapNodeCollection:
        """ GetChildNodes(self: SiteMapProvider, node: SiteMapNode) -> SiteMapNodeCollection """
        ...

    def GetCurrentNodeAndHintAncestorNodes(self, upLevel:int) -> SiteMapNode:
        """ GetCurrentNodeAndHintAncestorNodes(self: SiteMapProvider, upLevel: int) -> SiteMapNode """
        ...

    def GetCurrentNodeAndHintNeighborhoodNodes(self, upLevel:int, downLevel:int) -> SiteMapNode:
        """ GetCurrentNodeAndHintNeighborhoodNodes(self: SiteMapProvider, upLevel: int, downLevel: int) -> SiteMapNode """
        ...

    def GetParentNode(self, node:SiteMapNode) -> SiteMapNode:
        """ GetParentNode(self: SiteMapProvider, node: SiteMapNode) -> SiteMapNode """
        ...

    def GetParentNodeRelativeToCurrentNodeAndHintDownFromParent(self, walkupLevels:int, relativeDepthFromWalkup:int) -> SiteMapNode:
        """ GetParentNodeRelativeToCurrentNodeAndHintDownFromParent(self: SiteMapProvider, walkupLevels: int, relativeDepthFromWalkup: int) -> SiteMapNode """
        ...

    def GetParentNodeRelativeToNodeAndHintDownFromParent(self, node:SiteMapNode, walkupLevels:int, relativeDepthFromWalkup:int) -> SiteMapNode:
        """ GetParentNodeRelativeToNodeAndHintDownFromParent(self: SiteMapProvider, node: SiteMapNode, walkupLevels: int, relativeDepthFromWalkup: int) -> SiteMapNode """
        ...

    def GetRootNodeCore(self, *args): #cannot find CLR method
        """ GetRootNodeCore(self: SiteMapProvider) -> SiteMapNode """
        ...

    def GetRootNodeCoreFromProvider(self, *args): #cannot find CLR method
        """ GetRootNodeCoreFromProvider(provider: SiteMapProvider) -> SiteMapNode """
        ...

    def HintAncestorNodes(self, node:SiteMapNode, upLevel:int): # -> 
        """ HintAncestorNodes(self: SiteMapProvider, node: SiteMapNode, upLevel: int) """
        ...

    def HintNeighborhoodNodes(self, node:SiteMapNode, upLevel:int, downLevel:int): # -> 
        """ HintNeighborhoodNodes(self: SiteMapProvider, node: SiteMapNode, upLevel: int, downLevel: int) """
        ...

    def IsAccessibleToUser(self, context:HttpContext, node:SiteMapNode) -> bool:
        """ IsAccessibleToUser(self: SiteMapProvider, context: HttpContext, node: SiteMapNode) -> bool """
        ...

    def RemoveNode(self, *args): #cannot find CLR method
        """ RemoveNode(self: SiteMapProvider, node: SiteMapNode) """
        ...

    def ResolveSiteMapNode(self, *args): #cannot find CLR method
        """ ResolveSiteMapNode(self: SiteMapProvider, context: HttpContext) -> SiteMapNode """
        ...

    SiteMapResolve = ...


class SiteMapProviderCollection(ProviderCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ SiteMapProviderCollection() """
    def AddArray(self, providerArray:Array): # -> 
        """ AddArray(self: SiteMapProviderCollection, providerArray: Array[SiteMapProvider]) """
        ...


class SiteMapResolveEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ SiteMapResolveEventArgs(context: HttpContext, provider: SiteMapProvider) """
    @property
    def Context(self) -> HttpContext:
        """ Get: Context(self: SiteMapResolveEventArgs) -> HttpContext """
        ...

    @property
    def Provider(self) -> SiteMapProvider:
        """ Get: Provider(self: SiteMapResolveEventArgs) -> SiteMapProvider """
        ...


    def __new__(cls, context:HttpContext, provider:SiteMapProvider) -> Self:
        """ __new__(cls: type, context: HttpContext, provider: SiteMapProvider) """
        ...


class SiteMapResolveEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ SiteMapResolveEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:SiteMapResolveEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: SiteMapResolveEventHandler, sender: object, e: SiteMapResolveEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> SiteMapNode:
        """ EndInvoke(self: SiteMapResolveEventHandler, result: IAsyncResult) -> SiteMapNode """
        ...

    def Invoke(self, sender:object, e:SiteMapResolveEventArgs) -> SiteMapNode:
        """ Invoke(self: SiteMapResolveEventHandler, sender: object, e: SiteMapResolveEventArgs) -> SiteMapNode """
        ...


class StaticSiteMapProvider(SiteMapProvider): # skipped bases: <type 'object'>
    """ no doc """
    def BuildSiteMap(self) -> SiteMapNode:
        """ BuildSiteMap(self: StaticSiteMapProvider) -> SiteMapNode """
        ...

    def Clear(self, *args): #cannot find CLR method
        """ Clear(self: StaticSiteMapProvider) """
        ...


class TaskEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TaskEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:EventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: TaskEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> Task:
        """ EndInvoke(self: TaskEventHandler, result: IAsyncResult) -> Task """
        ...

    def Invoke(self, sender:object, e:EventArgs) -> Task:
        """ Invoke(self: TaskEventHandler, sender: object, e: EventArgs) -> Task """
        ...


class TraceContext: # skipped bases: <type 'object'>, <type 'object'>
    """ TraceContext(context: HttpContext) """
    @property
    def IsEnabled(self) -> bool:
        """
        Get: IsEnabled(self: TraceContext) -> bool
        Set: IsEnabled(self: TraceContext) = value
        """
        ...

    @property
    def TraceMode(self): # -> TraceMode
        """
        Get: TraceMode(self: TraceContext) -> TraceMode
        Set: TraceMode(self: TraceContext) = value
        """
        ...


    def Warn(self, *__args:str): # -> 
        """ Warn(self: TraceContext, message: str)Warn(self: TraceContext, category: str, message: str)Warn(self: TraceContext, category: str, message: str, errorInfo: Exception) """
        ...

    def Write(self, *__args:str): # -> 
        """ Write(self: TraceContext, message: str)Write(self: TraceContext, category: str, message: str)Write(self: TraceContext, category: str, message: str, errorInfo: Exception) """
        ...

    TraceFinished = ...


class TraceContextEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ TraceContextEventArgs(records: ICollection) """
    @property
    def TraceRecords(self) -> ICollection:
        """ Get: TraceRecords(self: TraceContextEventArgs) -> ICollection """
        ...


    def __new__(cls, records:ICollection) -> Self:
        """ __new__(cls: type, records: ICollection) """
        ...


class TraceContextEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ TraceContextEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:TraceContextEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: TraceContextEventHandler, sender: object, e: TraceContextEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: TraceContextEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:TraceContextEventArgs): # -> 
        """ Invoke(self: TraceContextEventHandler, sender: object, e: TraceContextEventArgs) """
        ...


class TraceContextRecord: # skipped bases: <type 'object'>, <type 'object'>
    """ TraceContextRecord(category: str, msg: str, isWarning: bool, errorInfo: Exception) """
    @property
    def Category(self) -> str:
        """ Get: Category(self: TraceContextRecord) -> str """
        ...

    @property
    def ErrorInfo(self) -> Exception:
        """ Get: ErrorInfo(self: TraceContextRecord) -> Exception """
        ...

    @property
    def IsWarning(self) -> bool:
        """ Get: IsWarning(self: TraceContextRecord) -> bool """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: TraceContextRecord) -> str """
        ...



class TraceMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TraceMode, values: Default (2), SortByCategory (1), SortByTime (0) """
    Default: TraceMode = ...
    SortByCategory: TraceMode = ...
    SortByTime: TraceMode = ...
    value__ = ...


class UnvalidatedRequestValues: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Cookies(self) -> HttpCookieCollection:
        """ Get: Cookies(self: UnvalidatedRequestValues) -> HttpCookieCollection """
        ...

    @property
    def Files(self) -> HttpFileCollection:
        """ Get: Files(self: UnvalidatedRequestValues) -> HttpFileCollection """
        ...

    @property
    def Form(self) -> NameValueCollection:
        """ Get: Form(self: UnvalidatedRequestValues) -> NameValueCollection """
        ...

    @property
    def Headers(self) -> NameValueCollection:
        """ Get: Headers(self: UnvalidatedRequestValues) -> NameValueCollection """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: UnvalidatedRequestValues) -> str """
        ...

    @property
    def PathInfo(self) -> str:
        """ Get: PathInfo(self: UnvalidatedRequestValues) -> str """
        ...

    @property
    def QueryString(self) -> NameValueCollection:
        """ Get: QueryString(self: UnvalidatedRequestValues) -> NameValueCollection """
        ...

    @property
    def RawUrl(self) -> str:
        """ Get: RawUrl(self: UnvalidatedRequestValues) -> str """
        ...

    @property
    def Url(self) -> Uri:
        """ Get: Url(self: UnvalidatedRequestValues) -> Uri """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class UnvalidatedRequestValuesBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Cookies(self) -> HttpCookieCollection:
        """ Get: Cookies(self: UnvalidatedRequestValuesBase) -> HttpCookieCollection """
        ...

    @property
    def Files(self) -> HttpFileCollectionBase:
        """ Get: Files(self: UnvalidatedRequestValuesBase) -> HttpFileCollectionBase """
        ...

    @property
    def Form(self) -> NameValueCollection:
        """ Get: Form(self: UnvalidatedRequestValuesBase) -> NameValueCollection """
        ...

    @property
    def Headers(self) -> NameValueCollection:
        """ Get: Headers(self: UnvalidatedRequestValuesBase) -> NameValueCollection """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: UnvalidatedRequestValuesBase) -> str """
        ...

    @property
    def PathInfo(self) -> str:
        """ Get: PathInfo(self: UnvalidatedRequestValuesBase) -> str """
        ...

    @property
    def QueryString(self) -> NameValueCollection:
        """ Get: QueryString(self: UnvalidatedRequestValuesBase) -> NameValueCollection """
        ...

    @property
    def RawUrl(self) -> str:
        """ Get: RawUrl(self: UnvalidatedRequestValuesBase) -> str """
        ...

    @property
    def Url(self) -> Uri:
        """ Get: Url(self: UnvalidatedRequestValuesBase) -> Uri """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...


class UnvalidatedRequestValuesWrapper(UnvalidatedRequestValuesBase): # skipped bases: <type 'object'>
    """ UnvalidatedRequestValuesWrapper(requestValues: UnvalidatedRequestValues) """
    def __new__(cls, requestValues:UnvalidatedRequestValues) -> Self:
        """ __new__(cls: type, requestValues: UnvalidatedRequestValues) """
        ...


class VirtualPathUtility: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def AppendTrailingSlash(virtualPath:str) -> str:
        """ AppendTrailingSlash(virtualPath: str) -> str """
        ...

    @staticmethod
    def Combine(basePath:str, relativePath:str) -> str:
        """ Combine(basePath: str, relativePath: str) -> str """
        ...

    @staticmethod
    def GetDirectory(virtualPath:str) -> str:
        """ GetDirectory(virtualPath: str) -> str """
        ...

    @staticmethod
    def GetExtension(virtualPath:str) -> str:
        """ GetExtension(virtualPath: str) -> str """
        ...

    @staticmethod
    def GetFileName(virtualPath:str) -> str:
        """ GetFileName(virtualPath: str) -> str """
        ...

    @staticmethod
    def IsAbsolute(virtualPath:str) -> bool:
        """ IsAbsolute(virtualPath: str) -> bool """
        ...

    @staticmethod
    def IsAppRelative(virtualPath:str) -> bool:
        """ IsAppRelative(virtualPath: str) -> bool """
        ...

    @staticmethod
    def MakeRelative(fromPath:str, toPath:str) -> str:
        """ MakeRelative(fromPath: str, toPath: str) -> str """
        ...

    @staticmethod
    def RemoveTrailingSlash(virtualPath:str) -> str:
        """ RemoveTrailingSlash(virtualPath: str) -> str """
        ...

    @staticmethod
    def ToAbsolute(virtualPath:str, applicationPath:str = ...) -> str:
        """
        ToAbsolute(virtualPath: str) -> str
        ToAbsolute(virtualPath: str, applicationPath: str) -> str
        """
        ...

    @staticmethod
    def ToAppRelative(virtualPath:str, applicationPath:str = ...) -> str:
        """
        ToAppRelative(virtualPath: str) -> str
        ToAppRelative(virtualPath: str, applicationPath: str) -> str
        """
        ...

    __all__: list = ...


class WebPageTraceListener(TraceListener): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ WebPageTraceListener() """
    pass

class XmlSiteMapProvider(IDisposable, StaticSiteMapProvider): # skipped bases: <type 'object'>
    """ XmlSiteMapProvider() """
    @property
    def CurrentNode(self) -> SiteMapNode:
        """ Get: CurrentNode(self: XmlSiteMapProvider) -> SiteMapNode """
        ...

    @property
    def RootNode(self) -> SiteMapNode:
        """ Get: RootNode(self: XmlSiteMapProvider) -> SiteMapNode """
        ...


    def AddProvider(self, *args): #cannot find CLR method
        """ AddProvider(self: XmlSiteMapProvider, providerName: str, parentNode: SiteMapNode) """
        ...

    def Initialize(self, name:str, attributes:NameValueCollection): # -> 
        """ Initialize(self: XmlSiteMapProvider, name: str, attributes: NameValueCollection) """
        ...

    def RemoveProvider(self, *args): #cannot find CLR method
        """ RemoveProvider(self: XmlSiteMapProvider, providerName: str) """
        ...


# variables with complex values

