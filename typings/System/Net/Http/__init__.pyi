# encoding: utf-8
# module System.Net.Http calls itself Http
# from System.Net.Http, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Net.Http.WebRequest, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, Enum, IDisposable, IEquatable, Int64, TimeSpan, 
    Uri, Version)

from System.Collections import IDictionary, IEnumerable

from System.IO import Stream

from System.Management import AuthenticationLevel

from System.Net import (CookieContainer, DecompressionMethods, HttpStatusCode, 
    ICredentials, IWebProxy, TransportContext)

from System.Net.Cache import RequestCachePolicy

from System.Net.Http.Headers import (HttpContentHeaders, HttpRequestHeaders, 
    HttpResponseHeaders)

from System.Net.Security import RemoteCertificateValidationCallback

from System.Security.Authentication import SslProtocols

from System.Security.Cryptography.X509Certificates import (
    X509CertificateCollection)

from System.Security.Principal import TokenImpersonationLevel

from System.Threading import CancellationToken

from System.Threading.Tasks import Task

from typing import Self

"""The following names are not found in the module: BoundEvent, Func, field#
"""

# no functions
# classes

class HttpContent(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Headers(self) -> HttpContentHeaders:
        """ Get: Headers(self: HttpContent) -> HttpContentHeaders """
        ...


    def CopyToAsync(self, stream:Stream, context:TransportContext = ...) -> Task:
        """
        CopyToAsync(self: HttpContent, stream: Stream) -> Task
        CopyToAsync(self: HttpContent, stream: Stream, context: TransportContext) -> Task
        """
        ...

    def CreateContentReadStreamAsync(self, *args): #cannot find CLR method
        """ CreateContentReadStreamAsync(self: HttpContent) -> Task[Stream] """
        ...

    def LoadIntoBufferAsync(self, maxBufferSize:Int64 = ...) -> Task:
        """
        LoadIntoBufferAsync(self: HttpContent, maxBufferSize: Int64) -> Task
        LoadIntoBufferAsync(self: HttpContent) -> Task
        """
        ...

    def ReadAsByteArrayAsync(self) -> Task:
        """ ReadAsByteArrayAsync(self: HttpContent) -> Task[Array[Byte]] """
        ...

    def ReadAsStreamAsync(self) -> Task:
        """ ReadAsStreamAsync(self: HttpContent) -> Task[Stream] """
        ...

    def ReadAsStringAsync(self) -> Task:
        """ ReadAsStringAsync(self: HttpContent) -> Task[str] """
        ...

    def SerializeToStreamAsync(self, *args): #cannot find CLR method
        """ SerializeToStreamAsync(self: HttpContent, stream: Stream, context: TransportContext) -> Task """
        ...

    def TryComputeLength(self, *args): #cannot find CLR method
        """ TryComputeLength(self: HttpContent) -> (bool, Int64) """
        ...


class ByteArrayContent(HttpContent): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    ByteArrayContent(content: Array[Byte])
    ByteArrayContent(content: Array[Byte], offset: int, count: int)
    """
    def __new__(cls, content:Array, offset:int = ..., count:int = ...) -> Self:
        """
        __new__(cls: type, content: Array[Byte])
        __new__(cls: type, content: Array[Byte], offset: int, count: int)
        """
        ...


class ClientCertificateOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ClientCertificateOption, values: Automatic (1), Manual (0) """
    Automatic: ClientCertificateOption = ...
    Manual: ClientCertificateOption = ...
    value__ = ...


class HttpMessageHandler(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    def SendAsync(self, *args): #cannot find CLR method
        """ SendAsync(self: HttpMessageHandler, request: HttpRequestMessage, cancellationToken: CancellationToken) -> Task[HttpResponseMessage] """
        ...


class DelegatingHandler(HttpMessageHandler): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    @property
    def InnerHandler(self) -> HttpMessageHandler:
        """
        Get: InnerHandler(self: DelegatingHandler) -> HttpMessageHandler
        Set: InnerHandler(self: DelegatingHandler) = value
        """
        ...


    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, innerHandler: HttpMessageHandler)
        """
        ...


class FormUrlEncodedContent(ByteArrayContent): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ FormUrlEncodedContent(nameValueCollection: IEnumerable[KeyValuePair[str, str]]) """
    pass

class HttpMessageInvoker(IDisposable): # skipped bases: <type 'object'>
    """
    HttpMessageInvoker(handler: HttpMessageHandler)
    HttpMessageInvoker(handler: HttpMessageHandler, disposeHandler: bool)
    """
    def SendAsync(self, request:HttpRequestMessage, cancellationToken:CancellationToken) -> Task:
        """ SendAsync(self: HttpMessageInvoker, request: HttpRequestMessage, cancellationToken: CancellationToken) -> Task[HttpResponseMessage] """
        ...


class HttpClient(HttpMessageInvoker): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    HttpClient()
    HttpClient(handler: HttpMessageHandler)
    HttpClient(handler: HttpMessageHandler, disposeHandler: bool)
    """
    @property
    def BaseAddress(self) -> Uri:
        """
        Get: BaseAddress(self: HttpClient) -> Uri
        Set: BaseAddress(self: HttpClient) = value
        """
        ...

    @property
    def DefaultRequestHeaders(self) -> HttpRequestHeaders:
        """ Get: DefaultRequestHeaders(self: HttpClient) -> HttpRequestHeaders """
        ...

    @property
    def MaxResponseContentBufferSize(self) -> Int64:
        """
        Get: MaxResponseContentBufferSize(self: HttpClient) -> Int64
        Set: MaxResponseContentBufferSize(self: HttpClient) = value
        """
        ...

    @property
    def Timeout(self) -> TimeSpan:
        """
        Get: Timeout(self: HttpClient) -> TimeSpan
        Set: Timeout(self: HttpClient) = value
        """
        ...


    def CancelPendingRequests(self): # -> 
        """ CancelPendingRequests(self: HttpClient) """
        ...

    def DeleteAsync(self, requestUri:str, cancellationToken:CancellationToken = ...) -> Task:
        """
        DeleteAsync(self: HttpClient, requestUri: str) -> Task[HttpResponseMessage]
        DeleteAsync(self: HttpClient, requestUri: Uri) -> Task[HttpResponseMessage]
        DeleteAsync(self: HttpClient, requestUri: str, cancellationToken: CancellationToken) -> Task[HttpResponseMessage]
        DeleteAsync(self: HttpClient, requestUri: Uri, cancellationToken: CancellationToken) -> Task[HttpResponseMessage]
        """
        ...

    def GetAsync(self, requestUri:Uri, *__args:CancellationToken) -> Task:
        """
        GetAsync(self: HttpClient, requestUri: Uri, cancellationToken: CancellationToken) -> Task[HttpResponseMessage]
        GetAsync(self: HttpClient, requestUri: str) -> Task[HttpResponseMessage]
        GetAsync(self: HttpClient, requestUri: Uri) -> Task[HttpResponseMessage]
        GetAsync(self: HttpClient, requestUri: str, completionOption: HttpCompletionOption) -> Task[HttpResponseMessage]
        GetAsync(self: HttpClient, requestUri: Uri, completionOption: HttpCompletionOption) -> Task[HttpResponseMessage]
        GetAsync(self: HttpClient, requestUri: str, cancellationToken: CancellationToken) -> Task[HttpResponseMessage]
        GetAsync(self: HttpClient, requestUri: str, completionOption: HttpCompletionOption, cancellationToken: CancellationToken) -> Task[HttpResponseMessage]
        GetAsync(self: HttpClient, requestUri: Uri, completionOption: HttpCompletionOption, cancellationToken: CancellationToken) -> Task[HttpResponseMessage]
        """
        ...

    def GetByteArrayAsync(self, requestUri:str) -> Task:
        """
        GetByteArrayAsync(self: HttpClient, requestUri: str) -> Task[Array[Byte]]
        GetByteArrayAsync(self: HttpClient, requestUri: Uri) -> Task[Array[Byte]]
        """
        ...

    def GetStreamAsync(self, requestUri:str) -> Task:
        """
        GetStreamAsync(self: HttpClient, requestUri: str) -> Task[Stream]
        GetStreamAsync(self: HttpClient, requestUri: Uri) -> Task[Stream]
        """
        ...

    def GetStringAsync(self, requestUri:str) -> Task:
        """
        GetStringAsync(self: HttpClient, requestUri: str) -> Task[str]
        GetStringAsync(self: HttpClient, requestUri: Uri) -> Task[str]
        """
        ...

    def PostAsync(self, requestUri:str, content:HttpContent, cancellationToken:CancellationToken = ...) -> Task:
        """
        PostAsync(self: HttpClient, requestUri: str, content: HttpContent) -> Task[HttpResponseMessage]
        PostAsync(self: HttpClient, requestUri: Uri, content: HttpContent) -> Task[HttpResponseMessage]
        PostAsync(self: HttpClient, requestUri: str, content: HttpContent, cancellationToken: CancellationToken) -> Task[HttpResponseMessage]
        PostAsync(self: HttpClient, requestUri: Uri, content: HttpContent, cancellationToken: CancellationToken) -> Task[HttpResponseMessage]
        """
        ...

    def PutAsync(self, requestUri:str, content:HttpContent, cancellationToken:CancellationToken = ...) -> Task:
        """
        PutAsync(self: HttpClient, requestUri: str, content: HttpContent) -> Task[HttpResponseMessage]
        PutAsync(self: HttpClient, requestUri: Uri, content: HttpContent) -> Task[HttpResponseMessage]
        PutAsync(self: HttpClient, requestUri: str, content: HttpContent, cancellationToken: CancellationToken) -> Task[HttpResponseMessage]
        PutAsync(self: HttpClient, requestUri: Uri, content: HttpContent, cancellationToken: CancellationToken) -> Task[HttpResponseMessage]
        """
        ...


class HttpClientHandler(HttpMessageHandler): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ HttpClientHandler() """
    @property
    def AllowAutoRedirect(self) -> bool:
        """
        Get: AllowAutoRedirect(self: HttpClientHandler) -> bool
        Set: AllowAutoRedirect(self: HttpClientHandler) = value
        """
        ...

    @property
    def AutomaticDecompression(self) -> DecompressionMethods:
        """
        Get: AutomaticDecompression(self: HttpClientHandler) -> DecompressionMethods
        Set: AutomaticDecompression(self: HttpClientHandler) = value
        """
        ...

    @property
    def CheckCertificateRevocationList(self) -> bool:
        """
        Get: CheckCertificateRevocationList(self: HttpClientHandler) -> bool
        Set: CheckCertificateRevocationList(self: HttpClientHandler) = value
        """
        ...

    @property
    def ClientCertificateOptions(self) -> ClientCertificateOption:
        """
        Get: ClientCertificateOptions(self: HttpClientHandler) -> ClientCertificateOption
        Set: ClientCertificateOptions(self: HttpClientHandler) = value
        """
        ...

    @property
    def ClientCertificates(self) -> X509CertificateCollection:
        """ Get: ClientCertificates(self: HttpClientHandler) -> X509CertificateCollection """
        ...

    @property
    def CookieContainer(self) -> CookieContainer:
        """
        Get: CookieContainer(self: HttpClientHandler) -> CookieContainer
        Set: CookieContainer(self: HttpClientHandler) = value
        """
        ...

    @property
    def Credentials(self) -> ICredentials:
        """
        Get: Credentials(self: HttpClientHandler) -> ICredentials
        Set: Credentials(self: HttpClientHandler) = value
        """
        ...

    @property
    def DangerousAcceptAnyServerCertificateValidator(self): # -> Func
        """ Get: DangerousAcceptAnyServerCertificateValidator() -> Func[HttpRequestMessage, X509Certificate2, X509Chain, SslPolicyErrors, bool] """
        ...

    @property
    def DefaultProxyCredentials(self) -> ICredentials:
        """
        Get: DefaultProxyCredentials(self: HttpClientHandler) -> ICredentials
        Set: DefaultProxyCredentials(self: HttpClientHandler) = value
        """
        ...

    @property
    def MaxAutomaticRedirections(self) -> int:
        """
        Get: MaxAutomaticRedirections(self: HttpClientHandler) -> int
        Set: MaxAutomaticRedirections(self: HttpClientHandler) = value
        """
        ...

    @property
    def MaxConnectionsPerServer(self) -> int:
        """
        Get: MaxConnectionsPerServer(self: HttpClientHandler) -> int
        Set: MaxConnectionsPerServer(self: HttpClientHandler) = value
        """
        ...

    @property
    def MaxRequestContentBufferSize(self) -> Int64:
        """
        Get: MaxRequestContentBufferSize(self: HttpClientHandler) -> Int64
        Set: MaxRequestContentBufferSize(self: HttpClientHandler) = value
        """
        ...

    @property
    def MaxResponseHeadersLength(self) -> int:
        """
        Get: MaxResponseHeadersLength(self: HttpClientHandler) -> int
        Set: MaxResponseHeadersLength(self: HttpClientHandler) = value
        """
        ...

    @property
    def PreAuthenticate(self) -> bool:
        """
        Get: PreAuthenticate(self: HttpClientHandler) -> bool
        Set: PreAuthenticate(self: HttpClientHandler) = value
        """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: HttpClientHandler) -> IDictionary[str, object] """
        ...

    @property
    def Proxy(self) -> IWebProxy:
        """
        Get: Proxy(self: HttpClientHandler) -> IWebProxy
        Set: Proxy(self: HttpClientHandler) = value
        """
        ...

    @property
    def ServerCertificateCustomValidationCallback(self): # -> Func
        """
        Get: ServerCertificateCustomValidationCallback(self: HttpClientHandler) -> Func[HttpRequestMessage, X509Certificate2, X509Chain, SslPolicyErrors, bool]
        Set: ServerCertificateCustomValidationCallback(self: HttpClientHandler) = value
        """
        ...

    @property
    def SslProtocols(self) -> SslProtocols:
        """
        Get: SslProtocols(self: HttpClientHandler) -> SslProtocols
        Set: SslProtocols(self: HttpClientHandler) = value
        """
        ...

    @property
    def SupportsAutomaticDecompression(self) -> bool:
        """ Get: SupportsAutomaticDecompression(self: HttpClientHandler) -> bool """
        ...

    @property
    def SupportsProxy(self) -> bool:
        """ Get: SupportsProxy(self: HttpClientHandler) -> bool """
        ...

    @property
    def SupportsRedirectConfiguration(self) -> bool:
        """ Get: SupportsRedirectConfiguration(self: HttpClientHandler) -> bool """
        ...

    @property
    def UseCookies(self) -> bool:
        """
        Get: UseCookies(self: HttpClientHandler) -> bool
        Set: UseCookies(self: HttpClientHandler) = value
        """
        ...

    @property
    def UseDefaultCredentials(self) -> bool:
        """
        Get: UseDefaultCredentials(self: HttpClientHandler) -> bool
        Set: UseDefaultCredentials(self: HttpClientHandler) = value
        """
        ...

    @property
    def UseProxy(self) -> bool:
        """
        Get: UseProxy(self: HttpClientHandler) -> bool
        Set: UseProxy(self: HttpClientHandler) = value
        """
        ...



class HttpCompletionOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HttpCompletionOption, values: ResponseContentRead (0), ResponseHeadersRead (1) """
    ResponseContentRead: HttpCompletionOption = ...
    ResponseHeadersRead: HttpCompletionOption = ...
    value__ = ...


class HttpMethod(IEquatable): # skipped bases: <type 'object'>
    """ HttpMethod(method: str) """
    @property
    def Delete(self) -> HttpMethod:
        """ Get: Delete() -> HttpMethod """
        ...

    @property
    def Get(self) -> HttpMethod:
        """ Get: Get() -> HttpMethod """
        ...

    @property
    def Head(self) -> HttpMethod:
        """ Get: Head() -> HttpMethod """
        ...

    @property
    def Method(self) -> str:
        """ Get: Method(self: HttpMethod) -> str """
        ...

    @property
    def Options(self) -> HttpMethod:
        """ Get: Options() -> HttpMethod """
        ...

    @property
    def Post(self) -> HttpMethod:
        """ Get: Post() -> HttpMethod """
        ...

    @property
    def Put(self) -> HttpMethod:
        """ Get: Put() -> HttpMethod """
        ...

    @property
    def Trace(self) -> HttpMethod:
        """ Get: Trace() -> HttpMethod """
        ...


    def GetHashCode(self) -> int:
        """ GetHashCode(self: HttpMethod) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: HttpMethod) -> str """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...



class HttpRequestException(Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    HttpRequestException()
    HttpRequestException(message: str)
    HttpRequestException(message: str, inner: Exception)
    """
    SerializeObjectState = ...


class HttpRequestMessage(IDisposable): # skipped bases: <type 'object'>
    """
    HttpRequestMessage()
    HttpRequestMessage(method: HttpMethod, requestUri: Uri)
    HttpRequestMessage(method: HttpMethod, requestUri: str)
    """
    @property
    def Content(self) -> HttpContent:
        """
        Get: Content(self: HttpRequestMessage) -> HttpContent
        Set: Content(self: HttpRequestMessage) = value
        """
        ...

    @property
    def Headers(self) -> HttpRequestHeaders:
        """ Get: Headers(self: HttpRequestMessage) -> HttpRequestHeaders """
        ...

    @property
    def Method(self) -> HttpMethod:
        """
        Get: Method(self: HttpRequestMessage) -> HttpMethod
        Set: Method(self: HttpRequestMessage) = value
        """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: HttpRequestMessage) -> IDictionary[str, object] """
        ...

    @property
    def RequestUri(self) -> Uri:
        """
        Get: RequestUri(self: HttpRequestMessage) -> Uri
        Set: RequestUri(self: HttpRequestMessage) = value
        """
        ...

    @property
    def Version(self) -> Version:
        """
        Get: Version(self: HttpRequestMessage) -> Version
        Set: Version(self: HttpRequestMessage) = value
        """
        ...


    def ToString(self) -> str:
        """ ToString(self: HttpRequestMessage) -> str """
        ...


class HttpResponseMessage(IDisposable): # skipped bases: <type 'object'>
    """
    HttpResponseMessage()
    HttpResponseMessage(statusCode: HttpStatusCode)
    """
    @property
    def Content(self) -> HttpContent:
        """
        Get: Content(self: HttpResponseMessage) -> HttpContent
        Set: Content(self: HttpResponseMessage) = value
        """
        ...

    @property
    def Headers(self) -> HttpResponseHeaders:
        """ Get: Headers(self: HttpResponseMessage) -> HttpResponseHeaders """
        ...

    @property
    def IsSuccessStatusCode(self) -> bool:
        """ Get: IsSuccessStatusCode(self: HttpResponseMessage) -> bool """
        ...

    @property
    def ReasonPhrase(self) -> str:
        """
        Get: ReasonPhrase(self: HttpResponseMessage) -> str
        Set: ReasonPhrase(self: HttpResponseMessage) = value
        """
        ...

    @property
    def RequestMessage(self) -> HttpRequestMessage:
        """
        Get: RequestMessage(self: HttpResponseMessage) -> HttpRequestMessage
        Set: RequestMessage(self: HttpResponseMessage) = value
        """
        ...

    @property
    def StatusCode(self) -> HttpStatusCode:
        """
        Get: StatusCode(self: HttpResponseMessage) -> HttpStatusCode
        Set: StatusCode(self: HttpResponseMessage) = value
        """
        ...

    @property
    def Version(self) -> Version:
        """
        Get: Version(self: HttpResponseMessage) -> Version
        Set: Version(self: HttpResponseMessage) = value
        """
        ...


    def EnsureSuccessStatusCode(self) -> HttpResponseMessage:
        """ EnsureSuccessStatusCode(self: HttpResponseMessage) -> HttpResponseMessage """
        ...

    def ToString(self) -> str:
        """ ToString(self: HttpResponseMessage) -> str """
        ...


class MessageProcessingHandler(DelegatingHandler): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ no doc """
    def ProcessRequest(self, *args): #cannot find CLR method
        """ ProcessRequest(self: MessageProcessingHandler, request: HttpRequestMessage, cancellationToken: CancellationToken) -> HttpRequestMessage """
        ...

    def ProcessResponse(self, *args): #cannot find CLR method
        """ ProcessResponse(self: MessageProcessingHandler, response: HttpResponseMessage, cancellationToken: CancellationToken) -> HttpResponseMessage """
        ...


class MultipartContent(HttpContent, IEnumerable): # skipped bases: <type 'IDisposable'>, <type 'IEnumerable'>, <type 'object'>
    """
    MultipartContent()
    MultipartContent(subtype: str)
    MultipartContent(subtype: str, boundary: str)
    """
    def Add(self, content:HttpContent): # -> 
        """ Add(self: MultipartContent, content: HttpContent) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[HttpContent](enumerable: IEnumerable[HttpContent], value: HttpContent) -> bool """
        ...

    def __new__(cls, subtype:str = ..., boundary:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, subtype: str)
        __new__(cls: type, subtype: str, boundary: str)
        """
        ...


class MultipartFormDataContent(MultipartContent): # skipped bases: <type 'IDisposable'>, <type 'IEnumerable[HttpContent]'>, <type 'IEnumerable'>, <type 'object'>
    """
    MultipartFormDataContent()
    MultipartFormDataContent(boundary: str)
    """
    pass

class RtcRequestFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def Create(method:HttpMethod, uri:Uri) -> HttpRequestMessage:
        """ Create(method: HttpMethod, uri: Uri) -> HttpRequestMessage """
        ...

    __all__: list = ...


class StreamContent(HttpContent): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    StreamContent(content: Stream)
    StreamContent(content: Stream, bufferSize: int)
    """
    def __new__(cls, content:Stream, bufferSize:int = ...) -> Self:
        """
        __new__(cls: type, content: Stream)
        __new__(cls: type, content: Stream, bufferSize: int)
        """
        ...


class StringContent(ByteArrayContent): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """
    StringContent(content: str)
    StringContent(content: str, encoding: Encoding)
    StringContent(content: str, encoding: Encoding, mediaType: str)
    """
    pass

class WebRequestHandler(HttpClientHandler): # skipped bases: <type 'IDisposable'>, <type 'object'>
    """ WebRequestHandler() """
    @property
    def AllowPipelining(self) -> bool:
        """
        Get: AllowPipelining(self: WebRequestHandler) -> bool
        Set: AllowPipelining(self: WebRequestHandler) = value
        """
        ...

    @property
    def AuthenticationLevel(self) -> AuthenticationLevel:
        """
        Get: AuthenticationLevel(self: WebRequestHandler) -> AuthenticationLevel
        Set: AuthenticationLevel(self: WebRequestHandler) = value
        """
        ...

    @property
    def CachePolicy(self) -> RequestCachePolicy:
        """
        Get: CachePolicy(self: WebRequestHandler) -> RequestCachePolicy
        Set: CachePolicy(self: WebRequestHandler) = value
        """
        ...

    @property
    def ContinueTimeout(self) -> TimeSpan:
        """
        Get: ContinueTimeout(self: WebRequestHandler) -> TimeSpan
        Set: ContinueTimeout(self: WebRequestHandler) = value
        """
        ...

    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """
        Get: ImpersonationLevel(self: WebRequestHandler) -> TokenImpersonationLevel
        Set: ImpersonationLevel(self: WebRequestHandler) = value
        """
        ...

    @property
    def ReadWriteTimeout(self) -> int:
        """
        Get: ReadWriteTimeout(self: WebRequestHandler) -> int
        Set: ReadWriteTimeout(self: WebRequestHandler) = value
        """
        ...

    @property
    def ServerCertificateValidationCallback(self) -> RemoteCertificateValidationCallback:
        """
        Get: ServerCertificateValidationCallback(self: WebRequestHandler) -> RemoteCertificateValidationCallback
        Set: ServerCertificateValidationCallback(self: WebRequestHandler) = value
        """
        ...

    @property
    def UnsafeAuthenticatedConnectionSharing(self) -> bool:
        """
        Get: UnsafeAuthenticatedConnectionSharing(self: WebRequestHandler) -> bool
        Set: UnsafeAuthenticatedConnectionSharing(self: WebRequestHandler) = value
        """
        ...



# variables with complex values

