# encoding: utf-8
# module System.Web.Routing calls itself Routing
# from System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Sdk.Sfc import Enumerator

from Microsoft.VisualBasic import Collection

from System import Enum, IDisposable

from System.Collections import ICollection, IDictionary

from System.Web import HttpContextBase, IHttpHandler, IHttpModule

from typing import Self

"""The following names are not found in the module: field#
"""

# no functions
# classes

class IRouteConstraint: # skipped bases: <type 'object'>
    """ no doc """
    def Match(self, httpContext:HttpContextBase, route:Route, parameterName:str, values:RouteValueDictionary, routeDirection:RouteDirection) -> bool:
        """ Match(self: IRouteConstraint, httpContext: HttpContextBase, route: Route, parameterName: str, values: RouteValueDictionary, routeDirection: RouteDirection) -> bool """
        ...


class HttpMethodConstraint(IRouteConstraint): # skipped bases: <type 'object'>
    """ HttpMethodConstraint(*allowedMethods: Array[str]) """
    @property
    def AllowedMethods(self) -> ICollection:
        """ Get: AllowedMethods(self: HttpMethodConstraint) -> ICollection[str] """
        ...



class IRouteHandler: # skipped bases: <type 'object'>
    """ no doc """
    def GetHttpHandler(self, requestContext:RequestContext) -> IHttpHandler:
        """ GetHttpHandler(self: IRouteHandler, requestContext: RequestContext) -> IHttpHandler """
        ...


class PageRouteHandler(IRouteHandler): # skipped bases: <type 'object'>
    """
    PageRouteHandler(virtualPath: str)
    PageRouteHandler(virtualPath: str, checkPhysicalUrlAccess: bool)
    """
    @property
    def CheckPhysicalUrlAccess(self) -> bool:
        """ Get: CheckPhysicalUrlAccess(self: PageRouteHandler) -> bool """
        ...

    @property
    def VirtualPath(self) -> str:
        """ Get: VirtualPath(self: PageRouteHandler) -> str """
        ...


    def GetSubstitutedVirtualPath(self, requestContext:RequestContext) -> str:
        """ GetSubstitutedVirtualPath(self: PageRouteHandler, requestContext: RequestContext) -> str """
        ...


class RequestContext: # skipped bases: <type 'object'>, <type 'object'>
    """
    RequestContext()
    RequestContext(httpContext: HttpContextBase, routeData: RouteData)
    """
    @property
    def HttpContext(self) -> HttpContextBase:
        """
        Get: HttpContext(self: RequestContext) -> HttpContextBase
        Set: HttpContext(self: RequestContext) = value
        """
        ...

    @property
    def RouteData(self) -> RouteData:
        """
        Get: RouteData(self: RequestContext) -> RouteData
        Set: RouteData(self: RequestContext) = value
        """
        ...



class RouteBase: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def RouteExistingFiles(self) -> bool:
        """
        Get: RouteExistingFiles(self: RouteBase) -> bool
        Set: RouteExistingFiles(self: RouteBase) = value
        """
        ...


    def GetRouteData(self, httpContext:HttpContextBase) -> RouteData:
        """ GetRouteData(self: RouteBase, httpContext: HttpContextBase) -> RouteData """
        ...

    def GetVirtualPath(self, requestContext:RequestContext, values:RouteValueDictionary) -> VirtualPathData:
        """ GetVirtualPath(self: RouteBase, requestContext: RequestContext, values: RouteValueDictionary) -> VirtualPathData """
        ...


class Route(RouteBase): # skipped bases: <type 'object'>
    """
    Route(url: str, routeHandler: IRouteHandler)
    Route(url: str, defaults: RouteValueDictionary, routeHandler: IRouteHandler)
    Route(url: str, defaults: RouteValueDictionary, constraints: RouteValueDictionary, routeHandler: IRouteHandler)
    Route(url: str, defaults: RouteValueDictionary, constraints: RouteValueDictionary, dataTokens: RouteValueDictionary, routeHandler: IRouteHandler)
    """
    @property
    def Constraints(self) -> RouteValueDictionary:
        """
        Get: Constraints(self: Route) -> RouteValueDictionary
        Set: Constraints(self: Route) = value
        """
        ...

    @property
    def DataTokens(self) -> RouteValueDictionary:
        """
        Get: DataTokens(self: Route) -> RouteValueDictionary
        Set: DataTokens(self: Route) = value
        """
        ...

    @property
    def Defaults(self) -> RouteValueDictionary:
        """
        Get: Defaults(self: Route) -> RouteValueDictionary
        Set: Defaults(self: Route) = value
        """
        ...

    @property
    def RouteHandler(self) -> IRouteHandler:
        """
        Get: RouteHandler(self: Route) -> IRouteHandler
        Set: RouteHandler(self: Route) = value
        """
        ...

    @property
    def Url(self) -> str:
        """
        Get: Url(self: Route) -> str
        Set: Url(self: Route) = value
        """
        ...


    def ProcessConstraint(self, *args): #cannot find CLR method
        """ ProcessConstraint(self: Route, httpContext: HttpContextBase, constraint: object, parameterName: str, values: RouteValueDictionary, routeDirection: RouteDirection) -> bool """
        ...

    def __new__(cls, url:str, *__args:IRouteHandler) -> Self:
        """
        __new__(cls: type, url: str, routeHandler: IRouteHandler)
        __new__(cls: type, url: str, defaults: RouteValueDictionary, routeHandler: IRouteHandler)
        __new__(cls: type, url: str, defaults: RouteValueDictionary, constraints: RouteValueDictionary, routeHandler: IRouteHandler)
        __new__(cls: type, url: str, defaults: RouteValueDictionary, constraints: RouteValueDictionary, dataTokens: RouteValueDictionary, routeHandler: IRouteHandler)
        """
        ...


class RouteCollection(Collection): # skipped bases: <type 'IReadOnlyList[RouteBase]'>, <type 'IEnumerable[RouteBase]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IList[RouteBase]'>, <type 'IReadOnlyCollection[RouteBase]'>, <type 'ICollection'>, <type 'ICollection[RouteBase]'>, <type 'object'>
    """
    RouteCollection()
    RouteCollection(virtualPathProvider: VirtualPathProvider)
    """
    @property
    def AppendTrailingSlash(self) -> bool:
        """
        Get: AppendTrailingSlash(self: RouteCollection) -> bool
        Set: AppendTrailingSlash(self: RouteCollection) = value
        """
        ...

    @property
    def LowercaseUrls(self) -> bool:
        """
        Get: LowercaseUrls(self: RouteCollection) -> bool
        Set: LowercaseUrls(self: RouteCollection) = value
        """
        ...

    @property
    def RouteExistingFiles(self) -> bool:
        """
        Get: RouteExistingFiles(self: RouteCollection) -> bool
        Set: RouteExistingFiles(self: RouteCollection) = value
        """
        ...


    def GetReadLock(self) -> IDisposable:
        """ GetReadLock(self: RouteCollection) -> IDisposable """
        ...

    def GetRouteData(self, httpContext:HttpContextBase) -> RouteData:
        """ GetRouteData(self: RouteCollection, httpContext: HttpContextBase) -> RouteData """
        ...

    def GetVirtualPath(self, requestContext:RequestContext, *__args:RouteValueDictionary) -> VirtualPathData:
        """
        GetVirtualPath(self: RouteCollection, requestContext: RequestContext, values: RouteValueDictionary) -> VirtualPathData
        GetVirtualPath(self: RouteCollection, requestContext: RequestContext, name: str, values: RouteValueDictionary) -> VirtualPathData
        """
        ...

    def GetWriteLock(self) -> IDisposable:
        """ GetWriteLock(self: RouteCollection) -> IDisposable """
        ...

    def Ignore(self, url:str, constraints:object = ...): # -> 
        """ Ignore(self: RouteCollection, url: str)Ignore(self: RouteCollection, url: str, constraints: object) """
        ...

    def MapPageRoute(self, routeName:str, routeUrl:str, physicalFile:str, checkPhysicalUrlAccess:bool = ..., defaults:RouteValueDictionary = ..., constraints:RouteValueDictionary = ..., dataTokens:RouteValueDictionary = ...) -> Route:
        """
        MapPageRoute(self: RouteCollection, routeName: str, routeUrl: str, physicalFile: str) -> Route
        MapPageRoute(self: RouteCollection, routeName: str, routeUrl: str, physicalFile: str, checkPhysicalUrlAccess: bool) -> Route
        MapPageRoute(self: RouteCollection, routeName: str, routeUrl: str, physicalFile: str, checkPhysicalUrlAccess: bool, defaults: RouteValueDictionary) -> Route
        MapPageRoute(self: RouteCollection, routeName: str, routeUrl: str, physicalFile: str, checkPhysicalUrlAccess: bool, defaults: RouteValueDictionary, constraints: RouteValueDictionary) -> Route
        MapPageRoute(self: RouteCollection, routeName: str, routeUrl: str, physicalFile: str, checkPhysicalUrlAccess: bool, defaults: RouteValueDictionary, constraints: RouteValueDictionary, dataTokens: RouteValueDictionary) -> Route
        """
        ...


class RouteData: # skipped bases: <type 'object'>, <type 'object'>
    """
    RouteData()
    RouteData(route: RouteBase, routeHandler: IRouteHandler)
    """
    @property
    def DataTokens(self) -> RouteValueDictionary:
        """ Get: DataTokens(self: RouteData) -> RouteValueDictionary """
        ...

    @property
    def Route(self) -> RouteBase:
        """
        Get: Route(self: RouteData) -> RouteBase
        Set: Route(self: RouteData) = value
        """
        ...

    @property
    def RouteHandler(self) -> IRouteHandler:
        """
        Get: RouteHandler(self: RouteData) -> IRouteHandler
        Set: RouteHandler(self: RouteData) = value
        """
        ...

    @property
    def Values(self) -> RouteValueDictionary:
        """ Get: Values(self: RouteData) -> RouteValueDictionary """
        ...


    def GetRequiredString(self, valueName:str) -> str:
        """ GetRequiredString(self: RouteData, valueName: str) -> str """
        ...


class RouteDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum RouteDirection, values: IncomingRequest (0), UrlGeneration (1) """
    IncomingRequest: RouteDirection = ...
    UrlGeneration: RouteDirection = ...
    value__ = ...


class RouteTable: # skipped bases: <type 'object'>, <type 'object'>
    """ RouteTable() """
    @property
    def Routes(self) -> RouteCollection:
        """ Get: Routes() -> RouteCollection """
        ...




class RouteValueDictionary(IDictionary): # skipped bases: <type 'IEnumerable[KeyValuePair[str, object]]'>, <type 'ICollection[KeyValuePair[str, object]]'>, <type 'IEnumerable'>, <type 'object'>
    """
    RouteValueDictionary()
    RouteValueDictionary(values: object)
    RouteValueDictionary(dictionary: IDictionary[str, object])
    """
    @property
    def Count(self) -> int:
        """ Get: Count(self: RouteValueDictionary) -> int """
        ...


    def Clear(self): # -> 
        """ Clear(self: RouteValueDictionary) """
        ...

    def ContainsValue(self, value:object) -> bool:
        """ ContainsValue(self: RouteValueDictionary, value: object) -> bool """
        ...

    def GetEnumerator(self) -> Enumerator:
        """ GetEnumerator(self: RouteValueDictionary) -> Enumerator """
        ...


class StopRoutingHandler(IRouteHandler): # skipped bases: <type 'object'>
    """ StopRoutingHandler() """
    pass

class UrlRoutingHandler(IHttpHandler): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RouteCollection(self) -> RouteCollection:
        """
        Get: RouteCollection(self: UrlRoutingHandler) -> RouteCollection
        Set: RouteCollection(self: UrlRoutingHandler) = value
        """
        ...


    def VerifyAndProcessRequest(self, *args): #cannot find CLR method
        """ VerifyAndProcessRequest(self: UrlRoutingHandler, httpHandler: IHttpHandler, httpContext: HttpContextBase) """
        ...


class UrlRoutingModule(IHttpModule): # skipped bases: <type 'object'>
    """ UrlRoutingModule() """
    @property
    def RouteCollection(self) -> RouteCollection:
        """
        Get: RouteCollection(self: UrlRoutingModule) -> RouteCollection
        Set: RouteCollection(self: UrlRoutingModule) = value
        """
        ...


    def PostMapRequestHandler(self, context:HttpContextBase): # -> 
        """ PostMapRequestHandler(self: UrlRoutingModule, context: HttpContextBase) """
        ...

    def PostResolveRequestCache(self, context:HttpContextBase): # -> 
        """ PostResolveRequestCache(self: UrlRoutingModule, context: HttpContextBase) """
        ...


class VirtualPathData: # skipped bases: <type 'object'>, <type 'object'>
    """ VirtualPathData(route: RouteBase, virtualPath: str) """
    @property
    def DataTokens(self) -> RouteValueDictionary:
        """ Get: DataTokens(self: VirtualPathData) -> RouteValueDictionary """
        ...

    @property
    def Route(self) -> RouteBase:
        """
        Get: Route(self: VirtualPathData) -> RouteBase
        Set: Route(self: VirtualPathData) = value
        """
        ...

    @property
    def VirtualPath(self) -> str:
        """
        Get: VirtualPath(self: VirtualPathData) -> str
        Set: VirtualPath(self: VirtualPathData) = value
        """
        ...



