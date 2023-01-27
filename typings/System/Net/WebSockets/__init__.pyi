# encoding: utf-8
# module System.Net.WebSockets calls itself WebSockets
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import ArraySegment, Enum, IDisposable, Nullable, TimeSpan, Uri

from System.Collections import IEnumerable

from System.Collections.Specialized import NameValueCollection

from System.ComponentModel import Win32Exception

from System.IO import Stream

from System.Net import (CookieCollection, CookieContainer, ICredentials, 
    IWebProxy)

from System.Security.Cryptography.X509Certificates import (
    X509CertificateCollection)

from System.Security.Principal import IPrincipal

from System.Threading import CancellationToken

from System.Threading.Tasks import Task

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class WebSocket(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def CloseStatus(self) -> Nullable:
        """ Get: CloseStatus(self: WebSocket) -> Nullable[WebSocketCloseStatus] """
        ...

    @property
    def CloseStatusDescription(self) -> str:
        """ Get: CloseStatusDescription(self: WebSocket) -> str """
        ...

    @property
    def DefaultKeepAliveInterval(self) -> TimeSpan:
        """ Get: DefaultKeepAliveInterval() -> TimeSpan """
        ...

    @property
    def State(self) -> WebSocketState:
        """ Get: State(self: WebSocket) -> WebSocketState """
        ...

    @property
    def SubProtocol(self) -> str:
        """ Get: SubProtocol(self: WebSocket) -> str """
        ...


    def Abort(self): # -> 
        """ Abort(self: WebSocket) """
        ...

    def CloseAsync(self, closeStatus:WebSocketCloseStatus, statusDescription:str, cancellationToken:CancellationToken) -> Task:
        """ CloseAsync(self: WebSocket, closeStatus: WebSocketCloseStatus, statusDescription: str, cancellationToken: CancellationToken) -> Task """
        ...

    def CloseOutputAsync(self, closeStatus:WebSocketCloseStatus, statusDescription:str, cancellationToken:CancellationToken) -> Task:
        """ CloseOutputAsync(self: WebSocket, closeStatus: WebSocketCloseStatus, statusDescription: str, cancellationToken: CancellationToken) -> Task """
        ...

    @staticmethod
    def CreateClientBuffer(receiveBufferSize:int, sendBufferSize:int) -> ArraySegment:
        """ CreateClientBuffer(receiveBufferSize: int, sendBufferSize: int) -> ArraySegment[Byte] """
        ...

    @staticmethod
    def CreateClientWebSocket(innerStream:Stream, subProtocol:str, receiveBufferSize:int, sendBufferSize:int, keepAliveInterval:TimeSpan, useZeroMaskingKey:bool, internalBuffer:ArraySegment) -> WebSocket:
        """ CreateClientWebSocket(innerStream: Stream, subProtocol: str, receiveBufferSize: int, sendBufferSize: int, keepAliveInterval: TimeSpan, useZeroMaskingKey: bool, internalBuffer: ArraySegment[Byte]) -> WebSocket """
        ...

    @staticmethod
    def CreateServerBuffer(receiveBufferSize:int) -> ArraySegment:
        """ CreateServerBuffer(receiveBufferSize: int) -> ArraySegment[Byte] """
        ...

    @staticmethod
    def IsApplicationTargeting45() -> bool:
        """ IsApplicationTargeting45() -> bool """
        ...

    def IsStateTerminal(self, *args): #cannot find CLR method
        """ IsStateTerminal(state: WebSocketState) -> bool """
        ...

    def ReceiveAsync(self, buffer:ArraySegment, cancellationToken:CancellationToken) -> Task:
        """ ReceiveAsync(self: WebSocket, buffer: ArraySegment[Byte], cancellationToken: CancellationToken) -> Task[WebSocketReceiveResult] """
        ...

    @staticmethod
    def RegisterPrefixes(): # -> 
        """ RegisterPrefixes() """
        ...

    def SendAsync(self, buffer:ArraySegment, messageType:WebSocketMessageType, endOfMessage:bool, cancellationToken:CancellationToken) -> Task:
        """ SendAsync(self: WebSocket, buffer: ArraySegment[Byte], messageType: WebSocketMessageType, endOfMessage: bool, cancellationToken: CancellationToken) -> Task """
        ...

    def ThrowOnInvalidState(self, *args): #cannot find CLR method
        """ ThrowOnInvalidState(state: WebSocketState, *validStates: Array[WebSocketState]) """
        ...



class ClientWebSocket(WebSocket): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ ClientWebSocket() """
    @property
    def Options(self) -> ClientWebSocketOptions:
        """ Get: Options(self: ClientWebSocket) -> ClientWebSocketOptions """
        ...


    def ConnectAsync(self, uri:Uri, cancellationToken:CancellationToken) -> Task:
        """ ConnectAsync(self: ClientWebSocket, uri: Uri, cancellationToken: CancellationToken) -> Task """
        ...


class ClientWebSocketOptions: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ClientCertificates(self) -> X509CertificateCollection:
        """
        Get: ClientCertificates(self: ClientWebSocketOptions) -> X509CertificateCollection
        Set: ClientCertificates(self: ClientWebSocketOptions) = value
        """
        ...

    @property
    def Cookies(self) -> CookieContainer:
        """
        Get: Cookies(self: ClientWebSocketOptions) -> CookieContainer
        Set: Cookies(self: ClientWebSocketOptions) = value
        """
        ...

    @property
    def Credentials(self) -> ICredentials:
        """
        Get: Credentials(self: ClientWebSocketOptions) -> ICredentials
        Set: Credentials(self: ClientWebSocketOptions) = value
        """
        ...

    @property
    def KeepAliveInterval(self) -> TimeSpan:
        """
        Get: KeepAliveInterval(self: ClientWebSocketOptions) -> TimeSpan
        Set: KeepAliveInterval(self: ClientWebSocketOptions) = value
        """
        ...

    @property
    def Proxy(self) -> IWebProxy:
        """
        Get: Proxy(self: ClientWebSocketOptions) -> IWebProxy
        Set: Proxy(self: ClientWebSocketOptions) = value
        """
        ...

    @property
    def UseDefaultCredentials(self) -> bool:
        """
        Get: UseDefaultCredentials(self: ClientWebSocketOptions) -> bool
        Set: UseDefaultCredentials(self: ClientWebSocketOptions) = value
        """
        ...


    def AddSubProtocol(self, subProtocol:str): # -> 
        """ AddSubProtocol(self: ClientWebSocketOptions, subProtocol: str) """
        ...

    def SetBuffer(self, receiveBufferSize:int, sendBufferSize:int, buffer:ArraySegment = ...): # -> 
        """ SetBuffer(self: ClientWebSocketOptions, receiveBufferSize: int, sendBufferSize: int)SetBuffer(self: ClientWebSocketOptions, receiveBufferSize: int, sendBufferSize: int, buffer: ArraySegment[Byte]) """
        ...

    def SetRequestHeader(self, headerName:str, headerValue:str): # -> 
        """ SetRequestHeader(self: ClientWebSocketOptions, headerName: str, headerValue: str) """
        ...


class WebSocketContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CookieCollection(self) -> CookieCollection:
        """ Get: CookieCollection(self: WebSocketContext) -> CookieCollection """
        ...

    @property
    def Headers(self) -> NameValueCollection:
        """ Get: Headers(self: WebSocketContext) -> NameValueCollection """
        ...

    @property
    def IsAuthenticated(self) -> bool:
        """ Get: IsAuthenticated(self: WebSocketContext) -> bool """
        ...

    @property
    def IsLocal(self) -> bool:
        """ Get: IsLocal(self: WebSocketContext) -> bool """
        ...

    @property
    def IsSecureConnection(self) -> bool:
        """ Get: IsSecureConnection(self: WebSocketContext) -> bool """
        ...

    @property
    def Origin(self) -> str:
        """ Get: Origin(self: WebSocketContext) -> str """
        ...

    @property
    def RequestUri(self) -> Uri:
        """ Get: RequestUri(self: WebSocketContext) -> Uri """
        ...

    @property
    def SecWebSocketKey(self) -> str:
        """ Get: SecWebSocketKey(self: WebSocketContext) -> str """
        ...

    @property
    def SecWebSocketProtocols(self) -> IEnumerable:
        """ Get: SecWebSocketProtocols(self: WebSocketContext) -> IEnumerable[str] """
        ...

    @property
    def SecWebSocketVersion(self) -> str:
        """ Get: SecWebSocketVersion(self: WebSocketContext) -> str """
        ...

    @property
    def User(self) -> IPrincipal:
        """ Get: User(self: WebSocketContext) -> IPrincipal """
        ...

    @property
    def WebSocket(self) -> WebSocket:
        """ Get: WebSocket(self: WebSocketContext) -> WebSocket """
        ...



class HttpListenerWebSocketContext(WebSocketContext): # skipped bases: <type 'object'>
    """ no doc """
    pass

class WebSocketCloseStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WebSocketCloseStatus, values: Empty (1005), EndpointUnavailable (1001), InternalServerError (1011), InvalidMessageType (1003), InvalidPayloadData (1007), MandatoryExtension (1010), MessageTooBig (1009), NormalClosure (1000), PolicyViolation (1008), ProtocolError (1002) """
    Empty: WebSocketCloseStatus = ...
    EndpointUnavailable: WebSocketCloseStatus = ...
    InternalServerError: WebSocketCloseStatus = ...
    InvalidMessageType: WebSocketCloseStatus = ...
    InvalidPayloadData: WebSocketCloseStatus = ...
    MandatoryExtension: WebSocketCloseStatus = ...
    MessageTooBig: WebSocketCloseStatus = ...
    NormalClosure: WebSocketCloseStatus = ...
    PolicyViolation: WebSocketCloseStatus = ...
    ProtocolError: WebSocketCloseStatus = ...
    value__ = ...


class WebSocketError(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WebSocketError, values: ConnectionClosedPrematurely (8), Faulted (2), HeaderError (7), InvalidMessageType (1), InvalidState (9), NativeError (3), NotAWebSocket (4), Success (0), UnsupportedProtocol (6), UnsupportedVersion (5) """
    ConnectionClosedPrematurely: WebSocketError = ...
    Faulted: WebSocketError = ...
    HeaderError: WebSocketError = ...
    InvalidMessageType: WebSocketError = ...
    InvalidState: WebSocketError = ...
    NativeError: WebSocketError = ...
    NotAWebSocket: WebSocketError = ...
    Success: WebSocketError = ...
    UnsupportedProtocol: WebSocketError = ...
    UnsupportedVersion: WebSocketError = ...
    value__ = ...


class WebSocketException(Win32Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WebSocketException()
    WebSocketException(error: WebSocketError)
    WebSocketException(error: WebSocketError, message: str)
    WebSocketException(error: WebSocketError, innerException: Exception)
    WebSocketException(error: WebSocketError, message: str, innerException: Exception)
    WebSocketException(nativeError: int)
    WebSocketException(nativeError: int, message: str)
    WebSocketException(nativeError: int, innerException: Exception)
    WebSocketException(error: WebSocketError, nativeError: int)
    WebSocketException(error: WebSocketError, nativeError: int, message: str)
    WebSocketException(error: WebSocketError, nativeError: int, innerException: Exception)
    WebSocketException(error: WebSocketError, nativeError: int, message: str, innerException: Exception)
    WebSocketException(message: str)
    WebSocketException(message: str, innerException: Exception)
    """
    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: WebSocketException) -> int """
        ...

    @property
    def WebSocketErrorCode(self) -> WebSocketError:
        """ Get: WebSocketErrorCode(self: WebSocketException) -> WebSocketError """
        ...


    SerializeObjectState = ...


class WebSocketMessageType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WebSocketMessageType, values: Binary (1), Close (2), Text (0) """
    Binary: WebSocketMessageType = ...
    Close: WebSocketMessageType = ...
    Text: WebSocketMessageType = ...
    value__ = ...


class WebSocketReceiveResult: # skipped bases: <type 'object'>, <type 'object'>
    """
    WebSocketReceiveResult(count: int, messageType: WebSocketMessageType, endOfMessage: bool)
    WebSocketReceiveResult(count: int, messageType: WebSocketMessageType, endOfMessage: bool, closeStatus: Nullable[WebSocketCloseStatus], closeStatusDescription: str)
    """
    @property
    def CloseStatus(self) -> Nullable:
        """ Get: CloseStatus(self: WebSocketReceiveResult) -> Nullable[WebSocketCloseStatus] """
        ...

    @property
    def CloseStatusDescription(self) -> str:
        """ Get: CloseStatusDescription(self: WebSocketReceiveResult) -> str """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: WebSocketReceiveResult) -> int """
        ...

    @property
    def EndOfMessage(self) -> bool:
        """ Get: EndOfMessage(self: WebSocketReceiveResult) -> bool """
        ...

    @property
    def MessageType(self) -> WebSocketMessageType:
        """ Get: MessageType(self: WebSocketReceiveResult) -> WebSocketMessageType """
        ...



class WebSocketState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WebSocketState, values: Aborted (6), Closed (5), CloseReceived (4), CloseSent (3), Connecting (1), None (0), Open (2) """
    Aborted: WebSocketState = ...
    Closed: WebSocketState = ...
    CloseReceived: WebSocketState = ...
    CloseSent: WebSocketState = ...
    Connecting: WebSocketState = ...
    Open: WebSocketState = ...
    value__ = ...


