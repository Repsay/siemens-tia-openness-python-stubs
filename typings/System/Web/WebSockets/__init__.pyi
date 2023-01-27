# encoding: utf-8
# module System.Web.WebSockets calls itself WebSockets
# from System.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, DateTime, Uri

from System.Collections import IDictionary

from System.Collections.Specialized import NameValueCollection

from System.Net.WebSockets import WebSocket, WebSocketContext

from System.Security.Principal import WindowsIdentity

from System.Web import (HttpApplicationStateBase, HttpClientCertificate, 
    HttpCookieCollection, HttpServerUtilityBase, UnvalidatedRequestValuesBase)

from System.Web.Caching import Cache

from System.Web.Profile import ProfileBase

"""The following names are not found in the module: IAsyncAbortableWebSocket
"""

# no functions
# classes

class AspNetWebSocket(WebSocket, IAsyncAbortableWebSocket): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    pass

class AspNetWebSocketContext(WebSocketContext): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AnonymousID(self) -> str:
        """ Get: AnonymousID(self: AspNetWebSocketContext) -> str """
        ...

    @property
    def Application(self) -> HttpApplicationStateBase:
        """ Get: Application(self: AspNetWebSocketContext) -> HttpApplicationStateBase """
        ...

    @property
    def ApplicationPath(self) -> str:
        """ Get: ApplicationPath(self: AspNetWebSocketContext) -> str """
        ...

    @property
    def Cache(self) -> Cache:
        """ Get: Cache(self: AspNetWebSocketContext) -> Cache """
        ...

    @property
    def ClientCertificate(self) -> HttpClientCertificate:
        """ Get: ClientCertificate(self: AspNetWebSocketContext) -> HttpClientCertificate """
        ...

    @property
    def ConnectionCount(self) -> int:
        """ Get: ConnectionCount() -> int """
        ...

    @property
    def Cookies(self) -> HttpCookieCollection:
        """ Get: Cookies(self: AspNetWebSocketContext) -> HttpCookieCollection """
        ...

    @property
    def FilePath(self) -> str:
        """ Get: FilePath(self: AspNetWebSocketContext) -> str """
        ...

    @property
    def IsClientConnected(self) -> bool:
        """ Get: IsClientConnected(self: AspNetWebSocketContext) -> bool """
        ...

    @property
    def IsDebuggingEnabled(self) -> bool:
        """ Get: IsDebuggingEnabled(self: AspNetWebSocketContext) -> bool """
        ...

    @property
    def Items(self) -> IDictionary:
        """ Get: Items(self: AspNetWebSocketContext) -> IDictionary """
        ...

    @property
    def LogonUserIdentity(self) -> WindowsIdentity:
        """ Get: LogonUserIdentity(self: AspNetWebSocketContext) -> WindowsIdentity """
        ...

    @property
    def Path(self) -> str:
        """ Get: Path(self: AspNetWebSocketContext) -> str """
        ...

    @property
    def PathInfo(self) -> str:
        """ Get: PathInfo(self: AspNetWebSocketContext) -> str """
        ...

    @property
    def Profile(self) -> ProfileBase:
        """ Get: Profile(self: AspNetWebSocketContext) -> ProfileBase """
        ...

    @property
    def QueryString(self) -> NameValueCollection:
        """ Get: QueryString(self: AspNetWebSocketContext) -> NameValueCollection """
        ...

    @property
    def RawUrl(self) -> str:
        """ Get: RawUrl(self: AspNetWebSocketContext) -> str """
        ...

    @property
    def Server(self) -> HttpServerUtilityBase:
        """ Get: Server(self: AspNetWebSocketContext) -> HttpServerUtilityBase """
        ...

    @property
    def ServerVariables(self) -> NameValueCollection:
        """ Get: ServerVariables(self: AspNetWebSocketContext) -> NameValueCollection """
        ...

    @property
    def Timestamp(self) -> DateTime:
        """ Get: Timestamp(self: AspNetWebSocketContext) -> DateTime """
        ...

    @property
    def Unvalidated(self) -> UnvalidatedRequestValuesBase:
        """ Get: Unvalidated(self: AspNetWebSocketContext) -> UnvalidatedRequestValuesBase """
        ...

    @property
    def UrlReferrer(self) -> Uri:
        """ Get: UrlReferrer(self: AspNetWebSocketContext) -> Uri """
        ...

    @property
    def UserAgent(self) -> str:
        """ Get: UserAgent(self: AspNetWebSocketContext) -> str """
        ...

    @property
    def UserHostAddress(self) -> str:
        """ Get: UserHostAddress(self: AspNetWebSocketContext) -> str """
        ...

    @property
    def UserHostName(self) -> str:
        """ Get: UserHostName(self: AspNetWebSocketContext) -> str """
        ...

    @property
    def UserLanguages(self) -> Array:
        """ Get: UserLanguages(self: AspNetWebSocketContext) -> Array[str] """
        ...




class AspNetWebSocketOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ AspNetWebSocketOptions() """
    @property
    def RequireSameOrigin(self) -> bool:
        """
        Get: RequireSameOrigin(self: AspNetWebSocketOptions) -> bool
        Set: RequireSameOrigin(self: AspNetWebSocketOptions) = value
        """
        ...

    @property
    def SubProtocol(self) -> str:
        """
        Get: SubProtocol(self: AspNetWebSocketOptions) -> str
        Set: SubProtocol(self: AspNetWebSocketOptions) = value
        """
        ...



