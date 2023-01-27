# encoding: utf-8
# module System.Net calls itself Net
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Net.Http, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Net, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a, System.Net.Http.WebRequest, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.VisualBasic import Collection

from System import (Array, AsyncCallback, DateTime, Enum, EventArgs, 
    FormatException, Guid, IAsyncResult, IDisposable, Int64, 
    InvalidOperationException, MarshalByRefObject, MulticastDelegate, 
    TimeSpan, Type, Uri, Version)

from System.Collections import (ArrayList, ICollection, IEnumerable, 
    IEnumerator)

from System.Collections.Specialized import (NameValueCollection, 
    StringDictionary)

from System.ComponentModel import (AsyncCompletedEventArgs, Component, 
    ProgressChangedEventArgs, Win32Exception)

from System.IO import Stream, TextWriter

from System.Management import AuthenticationLevel

from System.Net.Cache import RequestCachePolicy

from System.Net.Security import (EncryptionPolicy, 
    RemoteCertificateValidationCallback)

from System.Net.Sockets import AddressFamily

from System.Runtime.Serialization import (ISerializable, SerializationInfo, 
    StreamingContext)

from System.Security import CodeAccessPermission, IPermission, SecureString

from System.Security.Authentication.ExtendedProtection import (ChannelBinding, 
    ChannelBindingKind, ExtendedProtectionPolicy, ServiceNameCollection)

from System.Security.Cryptography.X509Certificates import (X509Certificate, 
    X509Certificate2, X509CertificateCollection)

from System.Security.Permissions import (CodeAccessSecurityAttribute, 
    IUnrestrictedPermission, PermissionState)

from System.Security.Principal import (GenericIdentity, IPrincipal, 
    TokenImpersonationLevel)

from System.Text import Encoding

from System.Threading import SynchronizationContext

from System.Threading.Tasks import Task

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: (BoundEvent, 
    ExtendedProtectionSelector, IAutoWebProxy, ICloseEx, KeysCollection, 
    field#)
"""

# no functions
# classes

class AuthenticationManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CredentialPolicy(self) -> ICredentialPolicy:
        """
        Get: CredentialPolicy() -> ICredentialPolicy
        Set: CredentialPolicy() = value
        """
        ...

    @property
    def CustomTargetNameDictionary(self) -> StringDictionary:
        """ Get: CustomTargetNameDictionary() -> StringDictionary """
        ...

    @property
    def RegisteredModules(self) -> IEnumerator:
        """ Get: RegisteredModules() -> IEnumerator """
        ...


    @staticmethod
    def Authenticate(challenge:str, request:WebRequest, credentials:ICredentials) -> Authorization:
        """ Authenticate(challenge: str, request: WebRequest, credentials: ICredentials) -> Authorization """
        ...

    @staticmethod
    def PreAuthenticate(request:WebRequest, credentials:ICredentials) -> Authorization:
        """ PreAuthenticate(request: WebRequest, credentials: ICredentials) -> Authorization """
        ...

    @staticmethod
    def Register(authenticationModule:IAuthenticationModule): # -> 
        """ Register(authenticationModule: IAuthenticationModule) """
        ...

    @staticmethod
    def Unregister(*__args:IAuthenticationModule): # -> 
        """ Unregister(authenticationModule: IAuthenticationModule)Unregister(authenticationScheme: str) """
        ...



class AuthenticationSchemes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) AuthenticationSchemes, values: Anonymous (32768), Basic (8), Digest (1), IntegratedWindowsAuthentication (6), Negotiate (2), None (0), Ntlm (4) """
    Anonymous: AuthenticationSchemes = ...
    Basic: AuthenticationSchemes = ...
    Digest: AuthenticationSchemes = ...
    IntegratedWindowsAuthentication: AuthenticationSchemes = ...
    Negotiate: AuthenticationSchemes = ...
    Ntlm: AuthenticationSchemes = ...
    value__ = ...


class AuthenticationSchemeSelector(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ AuthenticationSchemeSelector(object: object, method: IntPtr) """
    def BeginInvoke(self, httpRequest:HttpListenerRequest, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: AuthenticationSchemeSelector, httpRequest: HttpListenerRequest, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> AuthenticationSchemes:
        """ EndInvoke(self: AuthenticationSchemeSelector, result: IAsyncResult) -> AuthenticationSchemes """
        ...

    def Invoke(self, httpRequest:HttpListenerRequest) -> AuthenticationSchemes:
        """ Invoke(self: AuthenticationSchemeSelector, httpRequest: HttpListenerRequest) -> AuthenticationSchemes """
        ...


class Authorization: # skipped bases: <type 'object'>, <type 'object'>
    """
    Authorization(token: str)
    Authorization(token: str, finished: bool)
    Authorization(token: str, finished: bool, connectionGroupId: str)
    """
    @property
    def Complete(self) -> bool:
        """ Get: Complete(self: Authorization) -> bool """
        ...

    @property
    def ConnectionGroupId(self) -> str:
        """ Get: ConnectionGroupId(self: Authorization) -> str """
        ...

    @property
    def Message(self) -> str:
        """ Get: Message(self: Authorization) -> str """
        ...

    @property
    def MutuallyAuthenticated(self) -> bool:
        """
        Get: MutuallyAuthenticated(self: Authorization) -> bool
        Set: MutuallyAuthenticated(self: Authorization) = value
        """
        ...

    @property
    def ProtectionRealm(self) -> Array:
        """
        Get: ProtectionRealm(self: Authorization) -> Array[str]
        Set: ProtectionRealm(self: Authorization) = value
        """
        ...



class BindIPEndPoint(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ BindIPEndPoint(object: object, method: IntPtr) """
    def BeginInvoke(self, servicePoint:ServicePoint, remoteEndPoint:IPEndPoint, retryCount:int, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: BindIPEndPoint, servicePoint: ServicePoint, remoteEndPoint: IPEndPoint, retryCount: int, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult) -> IPEndPoint:
        """ EndInvoke(self: BindIPEndPoint, result: IAsyncResult) -> IPEndPoint """
        ...

    def Invoke(self, servicePoint:ServicePoint, remoteEndPoint:IPEndPoint, retryCount:int) -> IPEndPoint:
        """ Invoke(self: BindIPEndPoint, servicePoint: ServicePoint, remoteEndPoint: IPEndPoint, retryCount: int) -> IPEndPoint """
        ...


class Cookie: # skipped bases: <type 'object'>, <type 'object'>
    """
    Cookie()
    Cookie(name: str, value: str)
    Cookie(name: str, value: str, path: str)
    Cookie(name: str, value: str, path: str, domain: str)
    """
    @property
    def Comment(self) -> str:
        """
        Get: Comment(self: Cookie) -> str
        Set: Comment(self: Cookie) = value
        """
        ...

    @property
    def CommentUri(self) -> Uri:
        """
        Get: CommentUri(self: Cookie) -> Uri
        Set: CommentUri(self: Cookie) = value
        """
        ...

    @property
    def Discard(self) -> bool:
        """
        Get: Discard(self: Cookie) -> bool
        Set: Discard(self: Cookie) = value
        """
        ...

    @property
    def Domain(self) -> str:
        """
        Get: Domain(self: Cookie) -> str
        Set: Domain(self: Cookie) = value
        """
        ...

    @property
    def Expired(self) -> bool:
        """
        Get: Expired(self: Cookie) -> bool
        Set: Expired(self: Cookie) = value
        """
        ...

    @property
    def Expires(self) -> DateTime:
        """
        Get: Expires(self: Cookie) -> DateTime
        Set: Expires(self: Cookie) = value
        """
        ...

    @property
    def HttpOnly(self) -> bool:
        """
        Get: HttpOnly(self: Cookie) -> bool
        Set: HttpOnly(self: Cookie) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: Cookie) -> str
        Set: Name(self: Cookie) = value
        """
        ...

    @property
    def Path(self) -> str:
        """
        Get: Path(self: Cookie) -> str
        Set: Path(self: Cookie) = value
        """
        ...

    @property
    def Port(self) -> str:
        """
        Get: Port(self: Cookie) -> str
        Set: Port(self: Cookie) = value
        """
        ...

    @property
    def Secure(self) -> bool:
        """
        Get: Secure(self: Cookie) -> bool
        Set: Secure(self: Cookie) = value
        """
        ...

    @property
    def TimeStamp(self) -> DateTime:
        """ Get: TimeStamp(self: Cookie) -> DateTime """
        ...

    @property
    def Value(self) -> str:
        """
        Get: Value(self: Cookie) -> str
        Set: Value(self: Cookie) = value
        """
        ...

    @property
    def Version(self) -> int:
        """
        Get: Version(self: Cookie) -> int
        Set: Version(self: Cookie) = value
        """
        ...


    def Equals(self, comparand:object) -> bool:
        """ Equals(self: Cookie, comparand: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: Cookie) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: Cookie) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CookieCollection(ICollection): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ CookieCollection() """
    @property
    def IsReadOnly(self) -> bool:
        """ Get: IsReadOnly(self: CookieCollection) -> bool """
        ...


    def Add(self, *__args:Cookie): # -> 
        """ Add(self: CookieCollection, cookie: Cookie)Add(self: CookieCollection, cookies: CookieCollection) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: CookieCollection) -> IEnumerator """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class CookieContainer: # skipped bases: <type 'object'>, <type 'object'>
    """
    CookieContainer()
    CookieContainer(capacity: int)
    CookieContainer(capacity: int, perDomainCapacity: int, maxCookieSize: int)
    """
    @property
    def Capacity(self) -> int:
        """
        Get: Capacity(self: CookieContainer) -> int
        Set: Capacity(self: CookieContainer) = value
        """
        ...

    @property
    def Count(self) -> int:
        """ Get: Count(self: CookieContainer) -> int """
        ...

    @property
    def MaxCookieSize(self) -> int:
        """
        Get: MaxCookieSize(self: CookieContainer) -> int
        Set: MaxCookieSize(self: CookieContainer) = value
        """
        ...

    @property
    def PerDomainCapacity(self) -> int:
        """
        Get: PerDomainCapacity(self: CookieContainer) -> int
        Set: PerDomainCapacity(self: CookieContainer) = value
        """
        ...


    def Add(self, *__args:CookieCollection): # -> 
        """ Add(self: CookieContainer, cookies: CookieCollection)Add(self: CookieContainer, uri: Uri, cookie: Cookie)Add(self: CookieContainer, uri: Uri, cookies: CookieCollection)Add(self: CookieContainer, cookie: Cookie) """
        ...

    def GetCookieHeader(self, uri:Uri) -> str:
        """ GetCookieHeader(self: CookieContainer, uri: Uri) -> str """
        ...

    def GetCookies(self, uri:Uri) -> CookieCollection:
        """ GetCookies(self: CookieContainer, uri: Uri) -> CookieCollection """
        ...

    def SetCookies(self, uri:Uri, cookieHeader:str): # -> 
        """ SetCookies(self: CookieContainer, uri: Uri, cookieHeader: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...

    DefaultCookieLengthLimit: int = ...
    DefaultCookieLimit: int = ...
    DefaultPerDomainCookieLimit: int = ...


class CookieException(FormatException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """ CookieException() """
    def GetObjectData(self, serializationInfo:SerializationInfo, streamingContext:StreamingContext): # -> 
        """ GetObjectData(self: CookieException, serializationInfo: SerializationInfo, streamingContext: StreamingContext) """
        ...

    SerializeObjectState = ...


class CredentialCache(ICredentials, ICredentialsByHost, IEnumerable): # skipped bases: <type 'object'>
    """ CredentialCache() """
    @property
    def DefaultCredentials(self) -> ICredentials:
        """ Get: DefaultCredentials() -> ICredentials """
        ...

    @property
    def DefaultNetworkCredentials(self) -> NetworkCredential:
        """ Get: DefaultNetworkCredentials() -> NetworkCredential """
        ...


    def Add(self, *__args): # -> 
        """ Add(self: CredentialCache, uriPrefix: Uri, authType: str, cred: NetworkCredential)Add(self: CredentialCache, host: str, port: int, authenticationType: str, credential: NetworkCredential) """
        ...

    def Remove(self, *__args): # -> 
        """ Remove(self: CredentialCache, uriPrefix: Uri, authType: str)Remove(self: CredentialCache, host: str, port: int, authenticationType: str) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        ...



class DecompressionMethods(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DecompressionMethods, values: Deflate (2), GZip (1), None (0) """
    Deflate: DecompressionMethods = ...
    GZip: DecompressionMethods = ...
    value__ = ...


class Dns: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def BeginGetHostAddresses(hostNameOrAddress:str, requestCallback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginGetHostAddresses(hostNameOrAddress: str, requestCallback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    @staticmethod
    def BeginGetHostByName(hostName:str, requestCallback:AsyncCallback, stateObject:object) -> IAsyncResult:
        """ BeginGetHostByName(hostName: str, requestCallback: AsyncCallback, stateObject: object) -> IAsyncResult """
        ...

    @staticmethod
    def BeginGetHostEntry(*__args) -> IAsyncResult:
        """
        BeginGetHostEntry(hostNameOrAddress: str, requestCallback: AsyncCallback, stateObject: object) -> IAsyncResult
        BeginGetHostEntry(address: IPAddress, requestCallback: AsyncCallback, stateObject: object) -> IAsyncResult
        """
        ...

    @staticmethod
    def BeginResolve(hostName:str, requestCallback:AsyncCallback, stateObject:object) -> IAsyncResult:
        """ BeginResolve(hostName: str, requestCallback: AsyncCallback, stateObject: object) -> IAsyncResult """
        ...

    @staticmethod
    def EndGetHostAddresses(asyncResult:IAsyncResult) -> Array:
        """ EndGetHostAddresses(asyncResult: IAsyncResult) -> Array[IPAddress] """
        ...

    @staticmethod
    def EndGetHostByName(asyncResult:IAsyncResult) -> IPHostEntry:
        """ EndGetHostByName(asyncResult: IAsyncResult) -> IPHostEntry """
        ...

    @staticmethod
    def EndGetHostEntry(asyncResult:IAsyncResult) -> IPHostEntry:
        """ EndGetHostEntry(asyncResult: IAsyncResult) -> IPHostEntry """
        ...

    @staticmethod
    def EndResolve(asyncResult:IAsyncResult) -> IPHostEntry:
        """ EndResolve(asyncResult: IAsyncResult) -> IPHostEntry """
        ...

    @staticmethod
    def GetHostAddresses(hostNameOrAddress:str) -> Array:
        """ GetHostAddresses(hostNameOrAddress: str) -> Array[IPAddress] """
        ...

    @staticmethod
    def GetHostAddressesAsync(hostNameOrAddress:str) -> Task:
        """ GetHostAddressesAsync(hostNameOrAddress: str) -> Task[Array[IPAddress]] """
        ...

    @staticmethod
    def GetHostByAddress(address:str) -> IPHostEntry:
        """
        GetHostByAddress(address: str) -> IPHostEntry
        GetHostByAddress(address: IPAddress) -> IPHostEntry
        """
        ...

    @staticmethod
    def GetHostByName(hostName:str) -> IPHostEntry:
        """ GetHostByName(hostName: str) -> IPHostEntry """
        ...

    @staticmethod
    def GetHostEntry(*__args:IPAddress) -> IPHostEntry:
        """
        GetHostEntry(address: IPAddress) -> IPHostEntry
        GetHostEntry(hostNameOrAddress: str) -> IPHostEntry
        """
        ...

    @staticmethod
    def GetHostEntryAsync(*__args:IPAddress) -> Task:
        """
        GetHostEntryAsync(address: IPAddress) -> Task[IPHostEntry]
        GetHostEntryAsync(hostNameOrAddress: str) -> Task[IPHostEntry]
        """
        ...

    @staticmethod
    def GetHostName() -> str:
        """ GetHostName() -> str """
        ...

    @staticmethod
    def Resolve(hostName:str) -> IPHostEntry:
        """ Resolve(hostName: str) -> IPHostEntry """
        ...

    __all__: list = ...


class EndPoint: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AddressFamily(self) -> AddressFamily:
        """ Get: AddressFamily(self: EndPoint) -> AddressFamily """
        ...


    def Create(self, socketAddress:SocketAddress) -> EndPoint:
        """ Create(self: EndPoint, socketAddress: SocketAddress) -> EndPoint """
        ...

    def Serialize(self) -> SocketAddress:
        """ Serialize(self: EndPoint) -> SocketAddress """
        ...


class DnsEndPoint(EndPoint): # skipped bases: <type 'object'>
    """
    DnsEndPoint(host: str, port: int)
    DnsEndPoint(host: str, port: int, addressFamily: AddressFamily)
    """
    @property
    def Host(self) -> str:
        """ Get: Host(self: DnsEndPoint) -> str """
        ...

    @property
    def Port(self) -> int:
        """ Get: Port(self: DnsEndPoint) -> int """
        ...


    def Equals(self, comparand:object) -> bool:
        """ Equals(self: DnsEndPoint, comparand: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: DnsEndPoint) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: DnsEndPoint) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, host:str, port:int, addressFamily:AddressFamily = ...) -> Self:
        """
        __new__(cls: type, host: str, port: int)
        __new__(cls: type, host: str, port: int, addressFamily: AddressFamily)
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DnsPermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """ DnsPermission(state: PermissionState) """
    def __new__(cls, state:PermissionState) -> Self:
        """ __new__(cls: type, state: PermissionState) """
        ...


class DnsPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ DnsPermissionAttribute(action: SecurityAction) """
    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: DnsPermissionAttribute) -> IPermission """
        ...


class DownloadDataCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Result(self) -> Array:
        """ Get: Result(self: DownloadDataCompletedEventArgs) -> Array[Byte] """
        ...



class DownloadDataCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DownloadDataCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DownloadDataCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DownloadDataCompletedEventHandler, sender: object, e: DownloadDataCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DownloadDataCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DownloadDataCompletedEventArgs): # -> 
        """ Invoke(self: DownloadDataCompletedEventHandler, sender: object, e: DownloadDataCompletedEventArgs) """
        ...


class DownloadProgressChangedEventArgs(ProgressChangedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BytesReceived(self) -> Int64:
        """ Get: BytesReceived(self: DownloadProgressChangedEventArgs) -> Int64 """
        ...

    @property
    def TotalBytesToReceive(self) -> Int64:
        """ Get: TotalBytesToReceive(self: DownloadProgressChangedEventArgs) -> Int64 """
        ...



class DownloadProgressChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DownloadProgressChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DownloadProgressChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DownloadProgressChangedEventHandler, sender: object, e: DownloadProgressChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DownloadProgressChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DownloadProgressChangedEventArgs): # -> 
        """ Invoke(self: DownloadProgressChangedEventHandler, sender: object, e: DownloadProgressChangedEventArgs) """
        ...


class DownloadStringCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Result(self) -> str:
        """ Get: Result(self: DownloadStringCompletedEventArgs) -> str """
        ...



class DownloadStringCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DownloadStringCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:DownloadStringCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DownloadStringCompletedEventHandler, sender: object, e: DownloadStringCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: DownloadStringCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:DownloadStringCompletedEventArgs): # -> 
        """ Invoke(self: DownloadStringCompletedEventHandler, sender: object, e: DownloadStringCompletedEventArgs) """
        ...


class EndpointPermission: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Hostname(self) -> str:
        """ Get: Hostname(self: EndpointPermission) -> str """
        ...

    @property
    def Port(self) -> int:
        """ Get: Port(self: EndpointPermission) -> int """
        ...

    @property
    def Transport(self) -> TransportType:
        """ Get: Transport(self: EndpointPermission) -> TransportType """
        ...


    def Equals(self, obj:object) -> bool:
        """ Equals(self: EndpointPermission, obj: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: EndpointPermission) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: EndpointPermission) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class WebRequest(MarshalByRefObject, ISerializable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AuthenticationLevel(self) -> AuthenticationLevel:
        """
        Get: AuthenticationLevel(self: WebRequest) -> AuthenticationLevel
        Set: AuthenticationLevel(self: WebRequest) = value
        """
        ...

    @property
    def CachePolicy(self) -> RequestCachePolicy:
        """
        Get: CachePolicy(self: WebRequest) -> RequestCachePolicy
        Set: CachePolicy(self: WebRequest) = value
        """
        ...

    @property
    def ConnectionGroupName(self) -> str:
        """
        Get: ConnectionGroupName(self: WebRequest) -> str
        Set: ConnectionGroupName(self: WebRequest) = value
        """
        ...

    @property
    def ContentLength(self) -> Int64:
        """
        Get: ContentLength(self: WebRequest) -> Int64
        Set: ContentLength(self: WebRequest) = value
        """
        ...

    @property
    def ContentType(self) -> str:
        """
        Get: ContentType(self: WebRequest) -> str
        Set: ContentType(self: WebRequest) = value
        """
        ...

    @property
    def CreatorInstance(self) -> IWebRequestCreate:
        """ Get: CreatorInstance(self: WebRequest) -> IWebRequestCreate """
        ...

    @property
    def Credentials(self) -> ICredentials:
        """
        Get: Credentials(self: WebRequest) -> ICredentials
        Set: Credentials(self: WebRequest) = value
        """
        ...

    @property
    def DefaultCachePolicy(self) -> RequestCachePolicy:
        """
        Get: DefaultCachePolicy() -> RequestCachePolicy
        Set: DefaultCachePolicy() = value
        """
        ...

    @property
    def DefaultWebProxy(self) -> IWebProxy:
        """
        Get: DefaultWebProxy() -> IWebProxy
        Set: DefaultWebProxy() = value
        """
        ...

    @property
    def Headers(self) -> WebHeaderCollection:
        """
        Get: Headers(self: WebRequest) -> WebHeaderCollection
        Set: Headers(self: WebRequest) = value
        """
        ...

    @property
    def ImpersonationLevel(self) -> TokenImpersonationLevel:
        """
        Get: ImpersonationLevel(self: WebRequest) -> TokenImpersonationLevel
        Set: ImpersonationLevel(self: WebRequest) = value
        """
        ...

    @property
    def Method(self) -> str:
        """
        Get: Method(self: WebRequest) -> str
        Set: Method(self: WebRequest) = value
        """
        ...

    @property
    def PreAuthenticate(self) -> bool:
        """
        Get: PreAuthenticate(self: WebRequest) -> bool
        Set: PreAuthenticate(self: WebRequest) = value
        """
        ...

    @property
    def Proxy(self) -> IWebProxy:
        """
        Get: Proxy(self: WebRequest) -> IWebProxy
        Set: Proxy(self: WebRequest) = value
        """
        ...

    @property
    def RequestUri(self) -> Uri:
        """ Get: RequestUri(self: WebRequest) -> Uri """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: WebRequest) -> int
        Set: Timeout(self: WebRequest) = value
        """
        ...

    @property
    def UseDefaultCredentials(self) -> bool:
        """
        Get: UseDefaultCredentials(self: WebRequest) -> bool
        Set: UseDefaultCredentials(self: WebRequest) = value
        """
        ...


    def Abort(self): # -> 
        """ Abort(self: WebRequest) """
        ...

    def BeginGetRequestStream(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginGetRequestStream(self: WebRequest, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def BeginGetResponse(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginGetResponse(self: WebRequest, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    @staticmethod
    def Create(*__args:str) -> WebRequest:
        """
        Create(requestUriString: str) -> WebRequest
        Create(requestUri: Uri) -> WebRequest
        """
        ...

    @staticmethod
    def CreateDefault(requestUri:Uri) -> WebRequest:
        """ CreateDefault(requestUri: Uri) -> WebRequest """
        ...

    @staticmethod
    def CreateHttp(*__args:str) -> HttpWebRequest:
        """
        CreateHttp(requestUriString: str) -> HttpWebRequest
        CreateHttp(requestUri: Uri) -> HttpWebRequest
        """
        ...

    def EndGetRequestStream(self, asyncResult:IAsyncResult) -> Stream:
        """ EndGetRequestStream(self: WebRequest, asyncResult: IAsyncResult) -> Stream """
        ...

    def EndGetResponse(self, asyncResult:IAsyncResult) -> WebResponse:
        """ EndGetResponse(self: WebRequest, asyncResult: IAsyncResult) -> WebResponse """
        ...

    def GetRequestStream(self) -> Stream:
        """ GetRequestStream(self: WebRequest) -> Stream """
        ...

    def GetRequestStreamAsync(self) -> Task:
        """ GetRequestStreamAsync(self: WebRequest) -> Task[Stream] """
        ...

    def GetResponse(self) -> WebResponse:
        """ GetResponse(self: WebRequest) -> WebResponse """
        ...

    def GetResponseAsync(self) -> Task:
        """ GetResponseAsync(self: WebRequest) -> Task[WebResponse] """
        ...

    @staticmethod
    def GetSystemWebProxy() -> IWebProxy:
        """ GetSystemWebProxy() -> IWebProxy """
        ...

    @staticmethod
    def RegisterPortableWebRequestCreator(creator:IWebRequestCreate): # -> 
        """ RegisterPortableWebRequestCreator(creator: IWebRequestCreate) """
        ...

    @staticmethod
    def RegisterPrefix(prefix:str, creator:IWebRequestCreate) -> bool:
        """ RegisterPrefix(prefix: str, creator: IWebRequestCreate) -> bool """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, serializationInfo: SerializationInfo, streamingContext: StreamingContext)
        """
        ...



class FileWebRequest(WebRequest): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ no doc """
    pass

class WebResponse(IDisposable, MarshalByRefObject, ISerializable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ContentLength(self) -> Int64:
        """
        Get: ContentLength(self: WebResponse) -> Int64
        Set: ContentLength(self: WebResponse) = value
        """
        ...

    @property
    def ContentType(self) -> str:
        """
        Get: ContentType(self: WebResponse) -> str
        Set: ContentType(self: WebResponse) = value
        """
        ...

    @property
    def Headers(self) -> WebHeaderCollection:
        """ Get: Headers(self: WebResponse) -> WebHeaderCollection """
        ...

    @property
    def IsFromCache(self) -> bool:
        """ Get: IsFromCache(self: WebResponse) -> bool """
        ...

    @property
    def IsMutuallyAuthenticated(self) -> bool:
        """ Get: IsMutuallyAuthenticated(self: WebResponse) -> bool """
        ...

    @property
    def ResponseUri(self) -> Uri:
        """ Get: ResponseUri(self: WebResponse) -> Uri """
        ...

    @property
    def SupportsHeaders(self) -> bool:
        """ Get: SupportsHeaders(self: WebResponse) -> bool """
        ...


    def Close(self): # -> 
        """ Close(self: WebResponse) """
        ...

    def GetResponseStream(self) -> Stream:
        """ GetResponseStream(self: WebResponse) -> Stream """
        ...

    def __new__(cls, *args): #cannot find CLR constructor
        """
        __new__(cls: type)
        __new__(cls: type, serializationInfo: SerializationInfo, streamingContext: StreamingContext)
        """
        ...


class FileWebResponse(ICloseEx, WebResponse): # skipped bases: <type 'IDisposable'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    pass

class FtpStatusCode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum FtpStatusCode, values: AccountNeeded (532), ActionAbortedLocalProcessingError (451), ActionAbortedUnknownPageType (551), ActionNotTakenFilenameNotAllowed (553), ActionNotTakenFileUnavailable (550), ActionNotTakenFileUnavailableOrBusy (450), ActionNotTakenInsufficientSpace (452), ArgumentSyntaxError (501), BadCommandSequence (503), CantOpenData (425), ClosingControl (221), ClosingData (226), CommandExtraneous (202), CommandNotImplemented (502), CommandOK (200), CommandSyntaxError (500), ConnectionClosed (426), DataAlreadyOpen (125), DirectoryStatus (212), EnteringPassive (227), FileActionAborted (552), FileActionOK (250), FileCommandPending (350), FileStatus (213), LoggedInProceed (230), NeedLoginAccount (332), NotLoggedIn (530), OpeningData (150), PathnameCreated (257), RestartMarker (110), SendPasswordCommand (331), SendUserCommand (220), ServerWantsSecureSession (234), ServiceNotAvailable (421), ServiceTemporarilyNotAvailable (120), SystemType (215), Undefined (0) """
    AccountNeeded: FtpStatusCode = ...
    ActionAbortedLocalProcessingError: FtpStatusCode = ...
    ActionAbortedUnknownPageType: FtpStatusCode = ...
    ActionNotTakenFilenameNotAllowed: FtpStatusCode = ...
    ActionNotTakenFileUnavailable: FtpStatusCode = ...
    ActionNotTakenFileUnavailableOrBusy: FtpStatusCode = ...
    ActionNotTakenInsufficientSpace: FtpStatusCode = ...
    ArgumentSyntaxError: FtpStatusCode = ...
    BadCommandSequence: FtpStatusCode = ...
    CantOpenData: FtpStatusCode = ...
    ClosingControl: FtpStatusCode = ...
    ClosingData: FtpStatusCode = ...
    CommandExtraneous: FtpStatusCode = ...
    CommandNotImplemented: FtpStatusCode = ...
    CommandOK: FtpStatusCode = ...
    CommandSyntaxError: FtpStatusCode = ...
    ConnectionClosed: FtpStatusCode = ...
    DataAlreadyOpen: FtpStatusCode = ...
    DirectoryStatus: FtpStatusCode = ...
    EnteringPassive: FtpStatusCode = ...
    FileActionAborted: FtpStatusCode = ...
    FileActionOK: FtpStatusCode = ...
    FileCommandPending: FtpStatusCode = ...
    FileStatus: FtpStatusCode = ...
    LoggedInProceed: FtpStatusCode = ...
    NeedLoginAccount: FtpStatusCode = ...
    NotLoggedIn: FtpStatusCode = ...
    OpeningData: FtpStatusCode = ...
    PathnameCreated: FtpStatusCode = ...
    RestartMarker: FtpStatusCode = ...
    SendPasswordCommand: FtpStatusCode = ...
    SendUserCommand: FtpStatusCode = ...
    ServerWantsSecureSession: FtpStatusCode = ...
    ServiceNotAvailable: FtpStatusCode = ...
    ServiceTemporarilyNotAvailable: FtpStatusCode = ...
    SystemType: FtpStatusCode = ...
    Undefined: FtpStatusCode = ...
    value__ = ...


class FtpWebRequest(WebRequest): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def ClientCertificates(self) -> X509CertificateCollection:
        """
        Get: ClientCertificates(self: FtpWebRequest) -> X509CertificateCollection
        Set: ClientCertificates(self: FtpWebRequest) = value
        """
        ...

    @property
    def ContentOffset(self) -> Int64:
        """
        Get: ContentOffset(self: FtpWebRequest) -> Int64
        Set: ContentOffset(self: FtpWebRequest) = value
        """
        ...

    @property
    def EnableSsl(self) -> bool:
        """
        Get: EnableSsl(self: FtpWebRequest) -> bool
        Set: EnableSsl(self: FtpWebRequest) = value
        """
        ...

    @property
    def KeepAlive(self) -> bool:
        """
        Get: KeepAlive(self: FtpWebRequest) -> bool
        Set: KeepAlive(self: FtpWebRequest) = value
        """
        ...

    @property
    def ReadWriteTimeout(self) -> int:
        """
        Get: ReadWriteTimeout(self: FtpWebRequest) -> int
        Set: ReadWriteTimeout(self: FtpWebRequest) = value
        """
        ...

    @property
    def RenameTo(self) -> str:
        """
        Get: RenameTo(self: FtpWebRequest) -> str
        Set: RenameTo(self: FtpWebRequest) = value
        """
        ...

    @property
    def ServicePoint(self) -> ServicePoint:
        """ Get: ServicePoint(self: FtpWebRequest) -> ServicePoint """
        ...

    @property
    def UseBinary(self) -> bool:
        """
        Get: UseBinary(self: FtpWebRequest) -> bool
        Set: UseBinary(self: FtpWebRequest) = value
        """
        ...

    @property
    def UsePassive(self) -> bool:
        """
        Get: UsePassive(self: FtpWebRequest) -> bool
        Set: UsePassive(self: FtpWebRequest) = value
        """
        ...


    DefaultCachePolicy: RequestCachePolicy = ...


class FtpWebResponse(WebResponse): # skipped bases: <type 'IDisposable'>, <type 'ISerializable'>, <type 'object'>
    """ no doc """
    @property
    def BannerMessage(self) -> str:
        """ Get: BannerMessage(self: FtpWebResponse) -> str """
        ...

    @property
    def ExitMessage(self) -> str:
        """ Get: ExitMessage(self: FtpWebResponse) -> str """
        ...

    @property
    def LastModified(self) -> DateTime:
        """ Get: LastModified(self: FtpWebResponse) -> DateTime """
        ...

    @property
    def StatusCode(self) -> FtpStatusCode:
        """ Get: StatusCode(self: FtpWebResponse) -> FtpStatusCode """
        ...

    @property
    def StatusDescription(self) -> str:
        """ Get: StatusDescription(self: FtpWebResponse) -> str """
        ...

    @property
    def WelcomeMessage(self) -> str:
        """ Get: WelcomeMessage(self: FtpWebResponse) -> str """
        ...



class GlobalProxySelection: # skipped bases: <type 'object'>, <type 'object'>
    """ GlobalProxySelection() """
    @property
    def Select(self) -> IWebProxy:
        """
        Get: Select() -> IWebProxy
        Set: Select() = value
        """
        ...


    @staticmethod
    def GetEmptyWebProxy() -> IWebProxy:
        """ GetEmptyWebProxy() -> IWebProxy """
        ...



class HttpContinueDelegate(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ HttpContinueDelegate(object: object, method: IntPtr) """
    def BeginInvoke(self, StatusCode:int, httpHeaders:WebHeaderCollection, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: HttpContinueDelegate, StatusCode: int, httpHeaders: WebHeaderCollection, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: HttpContinueDelegate, result: IAsyncResult) """
        ...

    def Invoke(self, StatusCode:int, httpHeaders:WebHeaderCollection): # -> 
        """ Invoke(self: HttpContinueDelegate, StatusCode: int, httpHeaders: WebHeaderCollection) """
        ...


class HttpListener(IDisposable): # skipped bases: <type 'object'>
    """ HttpListener() """
    @property
    def AuthenticationSchemes(self) -> AuthenticationSchemes:
        """
        Get: AuthenticationSchemes(self: HttpListener) -> AuthenticationSchemes
        Set: AuthenticationSchemes(self: HttpListener) = value
        """
        ...

    @property
    def AuthenticationSchemeSelectorDelegate(self) -> AuthenticationSchemeSelector:
        """
        Get: AuthenticationSchemeSelectorDelegate(self: HttpListener) -> AuthenticationSchemeSelector
        Set: AuthenticationSchemeSelectorDelegate(self: HttpListener) = value
        """
        ...

    @property
    def DefaultServiceNames(self) -> ServiceNameCollection:
        """ Get: DefaultServiceNames(self: HttpListener) -> ServiceNameCollection """
        ...

    @property
    def ExtendedProtectionPolicy(self) -> ExtendedProtectionPolicy:
        """
        Get: ExtendedProtectionPolicy(self: HttpListener) -> ExtendedProtectionPolicy
        Set: ExtendedProtectionPolicy(self: HttpListener) = value
        """
        ...

    @property
    def ExtendedProtectionSelectorDelegate(self): # -> ExtendedProtectionSelector
        """
        Get: ExtendedProtectionSelectorDelegate(self: HttpListener) -> ExtendedProtectionSelector
        Set: ExtendedProtectionSelectorDelegate(self: HttpListener) = value
        """
        ...

    @property
    def IgnoreWriteExceptions(self) -> bool:
        """
        Get: IgnoreWriteExceptions(self: HttpListener) -> bool
        Set: IgnoreWriteExceptions(self: HttpListener) = value
        """
        ...

    @property
    def IsListening(self) -> bool:
        """ Get: IsListening(self: HttpListener) -> bool """
        ...

    @property
    def IsSupported(self) -> bool:
        """ Get: IsSupported() -> bool """
        ...

    @property
    def Prefixes(self) -> HttpListenerPrefixCollection:
        """ Get: Prefixes(self: HttpListener) -> HttpListenerPrefixCollection """
        ...

    @property
    def Realm(self) -> str:
        """
        Get: Realm(self: HttpListener) -> str
        Set: Realm(self: HttpListener) = value
        """
        ...

    @property
    def TimeoutManager(self) -> HttpListenerTimeoutManager:
        """ Get: TimeoutManager(self: HttpListener) -> HttpListenerTimeoutManager """
        ...

    @property
    def UnsafeConnectionNtlmAuthentication(self) -> bool:
        """
        Get: UnsafeConnectionNtlmAuthentication(self: HttpListener) -> bool
        Set: UnsafeConnectionNtlmAuthentication(self: HttpListener) = value
        """
        ...


    def Abort(self): # -> 
        """ Abort(self: HttpListener) """
        ...

    def BeginGetContext(self, callback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginGetContext(self: HttpListener, callback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def Close(self): # -> 
        """ Close(self: HttpListener) """
        ...

    def EndGetContext(self, asyncResult:IAsyncResult) -> HttpListenerContext:
        """ EndGetContext(self: HttpListener, asyncResult: IAsyncResult) -> HttpListenerContext """
        ...

    def ExtendedProtectionSelector(self, *args): #cannot find CLR method
        """ ExtendedProtectionSelector(object: object, method: IntPtr) """
        ...

    def GetContext(self) -> HttpListenerContext:
        """ GetContext(self: HttpListener) -> HttpListenerContext """
        ...

    def GetContextAsync(self) -> Task:
        """ GetContextAsync(self: HttpListener) -> Task[HttpListenerContext] """
        ...

    def Start(self): # -> 
        """ Start(self: HttpListener) """
        ...

    def Stop(self): # -> 
        """ Stop(self: HttpListener) """
        ...



class HttpListenerBasicIdentity(GenericIdentity): # skipped bases: <type 'IIdentity'>, <type 'object'>
    """ HttpListenerBasicIdentity(username: str, password: str) """
    @property
    def Password(self) -> str:
        """ Get: Password(self: HttpListenerBasicIdentity) -> str """
        ...



class HttpListenerContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Request(self) -> HttpListenerRequest:
        """ Get: Request(self: HttpListenerContext) -> HttpListenerRequest """
        ...

    @property
    def Response(self) -> HttpListenerResponse:
        """ Get: Response(self: HttpListenerContext) -> HttpListenerResponse """
        ...

    @property
    def User(self) -> IPrincipal:
        """ Get: User(self: HttpListenerContext) -> IPrincipal """
        ...


    def AcceptWebSocketAsync(self, subProtocol:str, *__args:TimeSpan) -> Task:
        """
        AcceptWebSocketAsync(self: HttpListenerContext, subProtocol: str) -> Task[HttpListenerWebSocketContext]
        AcceptWebSocketAsync(self: HttpListenerContext, subProtocol: str, keepAliveInterval: TimeSpan) -> Task[HttpListenerWebSocketContext]
        AcceptWebSocketAsync(self: HttpListenerContext, subProtocol: str, receiveBufferSize: int, keepAliveInterval: TimeSpan) -> Task[HttpListenerWebSocketContext]
        AcceptWebSocketAsync(self: HttpListenerContext, subProtocol: str, receiveBufferSize: int, keepAliveInterval: TimeSpan, internalBuffer: ArraySegment[Byte]) -> Task[HttpListenerWebSocketContext]
        """
        ...


class HttpListenerException(Win32Exception): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    HttpListenerException()
    HttpListenerException(errorCode: int)
    HttpListenerException(errorCode: int, message: str)
    """
    @property
    def ErrorCode(self) -> int:
        """ Get: ErrorCode(self: HttpListenerException) -> int """
        ...


    SerializeObjectState = ...


class HttpListenerPrefixCollection(ICollection): # skipped bases: <type 'IEnumerable[str]'>, <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: HttpListenerPrefixCollection) -> bool """
        ...


    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: HttpListenerPrefixCollection) -> IEnumerator[str] """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...


class HttpListenerRequest: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def AcceptTypes(self) -> Array:
        """ Get: AcceptTypes(self: HttpListenerRequest) -> Array[str] """
        ...

    @property
    def ClientCertificateError(self) -> int:
        """ Get: ClientCertificateError(self: HttpListenerRequest) -> int """
        ...

    @property
    def ContentEncoding(self) -> Encoding:
        """ Get: ContentEncoding(self: HttpListenerRequest) -> Encoding """
        ...

    @property
    def ContentLength64(self) -> Int64:
        """ Get: ContentLength64(self: HttpListenerRequest) -> Int64 """
        ...

    @property
    def ContentType(self) -> str:
        """ Get: ContentType(self: HttpListenerRequest) -> str """
        ...

    @property
    def Cookies(self) -> CookieCollection:
        """ Get: Cookies(self: HttpListenerRequest) -> CookieCollection """
        ...

    @property
    def HasEntityBody(self) -> bool:
        """ Get: HasEntityBody(self: HttpListenerRequest) -> bool """
        ...

    @property
    def Headers(self) -> NameValueCollection:
        """ Get: Headers(self: HttpListenerRequest) -> NameValueCollection """
        ...

    @property
    def HttpMethod(self) -> str:
        """ Get: HttpMethod(self: HttpListenerRequest) -> str """
        ...

    @property
    def InputStream(self) -> Stream:
        """ Get: InputStream(self: HttpListenerRequest) -> Stream """
        ...

    @property
    def IsAuthenticated(self) -> bool:
        """ Get: IsAuthenticated(self: HttpListenerRequest) -> bool """
        ...

    @property
    def IsLocal(self) -> bool:
        """ Get: IsLocal(self: HttpListenerRequest) -> bool """
        ...

    @property
    def IsSecureConnection(self) -> bool:
        """ Get: IsSecureConnection(self: HttpListenerRequest) -> bool """
        ...

    @property
    def IsWebSocketRequest(self) -> bool:
        """ Get: IsWebSocketRequest(self: HttpListenerRequest) -> bool """
        ...

    @property
    def KeepAlive(self) -> bool:
        """ Get: KeepAlive(self: HttpListenerRequest) -> bool """
        ...

    @property
    def LocalEndPoint(self) -> IPEndPoint:
        """ Get: LocalEndPoint(self: HttpListenerRequest) -> IPEndPoint """
        ...

    @property
    def ProtocolVersion(self) -> Version:
        """ Get: ProtocolVersion(self: HttpListenerRequest) -> Version """
        ...

    @property
    def QueryString(self) -> NameValueCollection:
        """ Get: QueryString(self: HttpListenerRequest) -> NameValueCollection """
        ...

    @property
    def RawUrl(self) -> str:
        """ Get: RawUrl(self: HttpListenerRequest) -> str """
        ...

    @property
    def RemoteEndPoint(self) -> IPEndPoint:
        """ Get: RemoteEndPoint(self: HttpListenerRequest) -> IPEndPoint """
        ...

    @property
    def RequestTraceIdentifier(self) -> Guid:
        """ Get: RequestTraceIdentifier(self: HttpListenerRequest) -> Guid """
        ...

    @property
    def ServiceName(self) -> str:
        """ Get: ServiceName(self: HttpListenerRequest) -> str """
        ...

    @property
    def TransportContext(self) -> TransportContext:
        """ Get: TransportContext(self: HttpListenerRequest) -> TransportContext """
        ...

    @property
    def Url(self) -> Uri:
        """ Get: Url(self: HttpListenerRequest) -> Uri """
        ...

    @property
    def UrlReferrer(self) -> Uri:
        """ Get: UrlReferrer(self: HttpListenerRequest) -> Uri """
        ...

    @property
    def UserAgent(self) -> str:
        """ Get: UserAgent(self: HttpListenerRequest) -> str """
        ...

    @property
    def UserHostAddress(self) -> str:
        """ Get: UserHostAddress(self: HttpListenerRequest) -> str """
        ...

    @property
    def UserHostName(self) -> str:
        """ Get: UserHostName(self: HttpListenerRequest) -> str """
        ...

    @property
    def UserLanguages(self) -> Array:
        """ Get: UserLanguages(self: HttpListenerRequest) -> Array[str] """
        ...


    def BeginGetClientCertificate(self, requestCallback:AsyncCallback, state:object) -> IAsyncResult:
        """ BeginGetClientCertificate(self: HttpListenerRequest, requestCallback: AsyncCallback, state: object) -> IAsyncResult """
        ...

    def EndGetClientCertificate(self, asyncResult:IAsyncResult) -> X509Certificate2:
        """ EndGetClientCertificate(self: HttpListenerRequest, asyncResult: IAsyncResult) -> X509Certificate2 """
        ...

    def GetClientCertificate(self) -> X509Certificate2:
        """ GetClientCertificate(self: HttpListenerRequest) -> X509Certificate2 """
        ...

    def GetClientCertificateAsync(self) -> Task:
        """ GetClientCertificateAsync(self: HttpListenerRequest) -> Task[X509Certificate2] """
        ...


class HttpListenerResponse(IDisposable): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ContentEncoding(self) -> Encoding:
        """
        Get: ContentEncoding(self: HttpListenerResponse) -> Encoding
        Set: ContentEncoding(self: HttpListenerResponse) = value
        """
        ...

    @property
    def ContentLength64(self) -> Int64:
        """
        Get: ContentLength64(self: HttpListenerResponse) -> Int64
        Set: ContentLength64(self: HttpListenerResponse) = value
        """
        ...

    @property
    def ContentType(self) -> str:
        """
        Get: ContentType(self: HttpListenerResponse) -> str
        Set: ContentType(self: HttpListenerResponse) = value
        """
        ...

    @property
    def Cookies(self) -> CookieCollection:
        """
        Get: Cookies(self: HttpListenerResponse) -> CookieCollection
        Set: Cookies(self: HttpListenerResponse) = value
        """
        ...

    @property
    def Headers(self) -> WebHeaderCollection:
        """
        Get: Headers(self: HttpListenerResponse) -> WebHeaderCollection
        Set: Headers(self: HttpListenerResponse) = value
        """
        ...

    @property
    def KeepAlive(self) -> bool:
        """
        Get: KeepAlive(self: HttpListenerResponse) -> bool
        Set: KeepAlive(self: HttpListenerResponse) = value
        """
        ...

    @property
    def OutputStream(self) -> Stream:
        """ Get: OutputStream(self: HttpListenerResponse) -> Stream """
        ...

    @property
    def ProtocolVersion(self) -> Version:
        """
        Get: ProtocolVersion(self: HttpListenerResponse) -> Version
        Set: ProtocolVersion(self: HttpListenerResponse) = value
        """
        ...

    @property
    def RedirectLocation(self) -> str:
        """
        Get: RedirectLocation(self: HttpListenerResponse) -> str
        Set: RedirectLocation(self: HttpListenerResponse) = value
        """
        ...

    @property
    def SendChunked(self) -> bool:
        """
        Get: SendChunked(self: HttpListenerResponse) -> bool
        Set: SendChunked(self: HttpListenerResponse) = value
        """
        ...

    @property
    def StatusCode(self) -> int:
        """
        Get: StatusCode(self: HttpListenerResponse) -> int
        Set: StatusCode(self: HttpListenerResponse) = value
        """
        ...

    @property
    def StatusDescription(self) -> str:
        """
        Get: StatusDescription(self: HttpListenerResponse) -> str
        Set: StatusDescription(self: HttpListenerResponse) = value
        """
        ...


    def Abort(self): # -> 
        """ Abort(self: HttpListenerResponse) """
        ...

    def AddHeader(self, name:str, value:str): # -> 
        """ AddHeader(self: HttpListenerResponse, name: str, value: str) """
        ...

    def AppendCookie(self, cookie:Cookie): # -> 
        """ AppendCookie(self: HttpListenerResponse, cookie: Cookie) """
        ...

    def AppendHeader(self, name:str, value:str): # -> 
        """ AppendHeader(self: HttpListenerResponse, name: str, value: str) """
        ...

    def Close(self, responseEntity:Array = ..., willBlock:bool = ...): # -> 
        """ Close(self: HttpListenerResponse, responseEntity: Array[Byte], willBlock: bool)Close(self: HttpListenerResponse) """
        ...

    def CopyFrom(self, templateResponse:HttpListenerResponse): # -> 
        """ CopyFrom(self: HttpListenerResponse, templateResponse: HttpListenerResponse) """
        ...

    def Redirect(self, url:str): # -> 
        """ Redirect(self: HttpListenerResponse, url: str) """
        ...

    def SetCookie(self, cookie:Cookie): # -> 
        """ SetCookie(self: HttpListenerResponse, cookie: Cookie) """
        ...


class HttpListenerTimeoutManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def DrainEntityBody(self) -> TimeSpan:
        """
        Get: DrainEntityBody(self: HttpListenerTimeoutManager) -> TimeSpan
        Set: DrainEntityBody(self: HttpListenerTimeoutManager) = value
        """
        ...

    @property
    def EntityBody(self) -> TimeSpan:
        """
        Get: EntityBody(self: HttpListenerTimeoutManager) -> TimeSpan
        Set: EntityBody(self: HttpListenerTimeoutManager) = value
        """
        ...

    @property
    def HeaderWait(self) -> TimeSpan:
        """
        Get: HeaderWait(self: HttpListenerTimeoutManager) -> TimeSpan
        Set: HeaderWait(self: HttpListenerTimeoutManager) = value
        """
        ...

    @property
    def IdleConnection(self) -> TimeSpan:
        """
        Get: IdleConnection(self: HttpListenerTimeoutManager) -> TimeSpan
        Set: IdleConnection(self: HttpListenerTimeoutManager) = value
        """
        ...

    @property
    def MinSendBytesPerSecond(self) -> Int64:
        """
        Get: MinSendBytesPerSecond(self: HttpListenerTimeoutManager) -> Int64
        Set: MinSendBytesPerSecond(self: HttpListenerTimeoutManager) = value
        """
        ...

    @property
    def RequestQueue(self) -> TimeSpan:
        """
        Get: RequestQueue(self: HttpListenerTimeoutManager) -> TimeSpan
        Set: RequestQueue(self: HttpListenerTimeoutManager) = value
        """
        ...



class HttpRequestHeader(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HttpRequestHeader, values: Accept (20), AcceptCharset (21), AcceptEncoding (22), AcceptLanguage (23), Allow (10), Authorization (24), CacheControl (0), Connection (1), ContentEncoding (13), ContentLanguage (14), ContentLength (11), ContentLocation (15), ContentMd5 (16), ContentRange (17), ContentType (12), Cookie (25), Date (2), Expect (26), Expires (18), From (27), Host (28), IfMatch (29), IfModifiedSince (30), IfNoneMatch (31), IfRange (32), IfUnmodifiedSince (33), KeepAlive (3), LastModified (19), MaxForwards (34), Pragma (4), ProxyAuthorization (35), Range (37), Referer (36), Te (38), Trailer (5), TransferEncoding (6), Translate (39), Upgrade (7), UserAgent (40), Via (8), Warning (9) """
    Accept: HttpRequestHeader = ...
    AcceptCharset: HttpRequestHeader = ...
    AcceptEncoding: HttpRequestHeader = ...
    AcceptLanguage: HttpRequestHeader = ...
    Allow: HttpRequestHeader = ...
    Authorization: HttpRequestHeader = ...
    CacheControl: HttpRequestHeader = ...
    Connection: HttpRequestHeader = ...
    ContentEncoding: HttpRequestHeader = ...
    ContentLanguage: HttpRequestHeader = ...
    ContentLength: HttpRequestHeader = ...
    ContentLocation: HttpRequestHeader = ...
    ContentMd5: HttpRequestHeader = ...
    ContentRange: HttpRequestHeader = ...
    ContentType: HttpRequestHeader = ...
    Cookie: HttpRequestHeader = ...
    Date: HttpRequestHeader = ...
    Expect: HttpRequestHeader = ...
    Expires: HttpRequestHeader = ...
    From: HttpRequestHeader = ...
    Host: HttpRequestHeader = ...
    IfMatch: HttpRequestHeader = ...
    IfModifiedSince: HttpRequestHeader = ...
    IfNoneMatch: HttpRequestHeader = ...
    IfRange: HttpRequestHeader = ...
    IfUnmodifiedSince: HttpRequestHeader = ...
    KeepAlive: HttpRequestHeader = ...
    LastModified: HttpRequestHeader = ...
    MaxForwards: HttpRequestHeader = ...
    Pragma: HttpRequestHeader = ...
    ProxyAuthorization: HttpRequestHeader = ...
    Range: HttpRequestHeader = ...
    Referer: HttpRequestHeader = ...
    Te: HttpRequestHeader = ...
    Trailer: HttpRequestHeader = ...
    TransferEncoding: HttpRequestHeader = ...
    Translate: HttpRequestHeader = ...
    Upgrade: HttpRequestHeader = ...
    UserAgent: HttpRequestHeader = ...
    value__ = ...
    Via: HttpRequestHeader = ...
    Warning: HttpRequestHeader = ...


class HttpResponseHeader(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HttpResponseHeader, values: AcceptRanges (20), Age (21), Allow (10), CacheControl (0), Connection (1), ContentEncoding (13), ContentLanguage (14), ContentLength (11), ContentLocation (15), ContentMd5 (16), ContentRange (17), ContentType (12), Date (2), ETag (22), Expires (18), KeepAlive (3), LastModified (19), Location (23), Pragma (4), ProxyAuthenticate (24), RetryAfter (25), Server (26), SetCookie (27), Trailer (5), TransferEncoding (6), Upgrade (7), Vary (28), Via (8), Warning (9), WwwAuthenticate (29) """
    AcceptRanges: HttpResponseHeader = ...
    Age: HttpResponseHeader = ...
    Allow: HttpResponseHeader = ...
    CacheControl: HttpResponseHeader = ...
    Connection: HttpResponseHeader = ...
    ContentEncoding: HttpResponseHeader = ...
    ContentLanguage: HttpResponseHeader = ...
    ContentLength: HttpResponseHeader = ...
    ContentLocation: HttpResponseHeader = ...
    ContentMd5: HttpResponseHeader = ...
    ContentRange: HttpResponseHeader = ...
    ContentType: HttpResponseHeader = ...
    Date: HttpResponseHeader = ...
    ETag: HttpResponseHeader = ...
    Expires: HttpResponseHeader = ...
    KeepAlive: HttpResponseHeader = ...
    LastModified: HttpResponseHeader = ...
    Location: HttpResponseHeader = ...
    Pragma: HttpResponseHeader = ...
    ProxyAuthenticate: HttpResponseHeader = ...
    RetryAfter: HttpResponseHeader = ...
    Server: HttpResponseHeader = ...
    SetCookie: HttpResponseHeader = ...
    Trailer: HttpResponseHeader = ...
    TransferEncoding: HttpResponseHeader = ...
    Upgrade: HttpResponseHeader = ...
    value__ = ...
    Vary: HttpResponseHeader = ...
    Via: HttpResponseHeader = ...
    Warning: HttpResponseHeader = ...
    WwwAuthenticate: HttpResponseHeader = ...


class HttpStatusCode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum HttpStatusCode, values: Accepted (202), Ambiguous (300), BadGateway (502), BadRequest (400), Conflict (409), Continue (100), Created (201), ExpectationFailed (417), Forbidden (403), Found (302), GatewayTimeout (504), Gone (410), HttpVersionNotSupported (505), InternalServerError (500), LengthRequired (411), MethodNotAllowed (405), Moved (301), MovedPermanently (301), MultipleChoices (300), NoContent (204), NonAuthoritativeInformation (203), NotAcceptable (406), NotFound (404), NotImplemented (501), NotModified (304), OK (200), PartialContent (206), PaymentRequired (402), PreconditionFailed (412), ProxyAuthenticationRequired (407), Redirect (302), RedirectKeepVerb (307), RedirectMethod (303), RequestedRangeNotSatisfiable (416), RequestEntityTooLarge (413), RequestTimeout (408), RequestUriTooLong (414), ResetContent (205), SeeOther (303), ServiceUnavailable (503), SwitchingProtocols (101), TemporaryRedirect (307), Unauthorized (401), UnsupportedMediaType (415), Unused (306), UpgradeRequired (426), UseProxy (305) """
    Accepted: HttpStatusCode = ...
    Ambiguous: HttpStatusCode = ...
    BadGateway: HttpStatusCode = ...
    BadRequest: HttpStatusCode = ...
    Conflict: HttpStatusCode = ...
    Continue: HttpStatusCode = ...
    Created: HttpStatusCode = ...
    ExpectationFailed: HttpStatusCode = ...
    Forbidden: HttpStatusCode = ...
    Found: HttpStatusCode = ...
    GatewayTimeout: HttpStatusCode = ...
    Gone: HttpStatusCode = ...
    HttpVersionNotSupported: HttpStatusCode = ...
    InternalServerError: HttpStatusCode = ...
    LengthRequired: HttpStatusCode = ...
    MethodNotAllowed: HttpStatusCode = ...
    Moved: HttpStatusCode = ...
    MovedPermanently: HttpStatusCode = ...
    MultipleChoices: HttpStatusCode = ...
    NoContent: HttpStatusCode = ...
    NonAuthoritativeInformation: HttpStatusCode = ...
    NotAcceptable: HttpStatusCode = ...
    NotFound: HttpStatusCode = ...
    NotImplemented: HttpStatusCode = ...
    NotModified: HttpStatusCode = ...
    OK: HttpStatusCode = ...
    PartialContent: HttpStatusCode = ...
    PaymentRequired: HttpStatusCode = ...
    PreconditionFailed: HttpStatusCode = ...
    ProxyAuthenticationRequired: HttpStatusCode = ...
    Redirect: HttpStatusCode = ...
    RedirectKeepVerb: HttpStatusCode = ...
    RedirectMethod: HttpStatusCode = ...
    RequestedRangeNotSatisfiable: HttpStatusCode = ...
    RequestEntityTooLarge: HttpStatusCode = ...
    RequestTimeout: HttpStatusCode = ...
    RequestUriTooLong: HttpStatusCode = ...
    ResetContent: HttpStatusCode = ...
    SeeOther: HttpStatusCode = ...
    ServiceUnavailable: HttpStatusCode = ...
    SwitchingProtocols: HttpStatusCode = ...
    TemporaryRedirect: HttpStatusCode = ...
    Unauthorized: HttpStatusCode = ...
    UnsupportedMediaType: HttpStatusCode = ...
    Unused: HttpStatusCode = ...
    UpgradeRequired: HttpStatusCode = ...
    UseProxy: HttpStatusCode = ...
    value__ = ...


class HttpVersion: # skipped bases: <type 'object'>, <type 'object'>
    """ HttpVersion() """
    Version10: Version = ...
    Version11: Version = ...


class HttpWebRequest(WebRequest): # skipped bases: <type 'ISerializable'>, <type 'object'>
    """ HttpWebRequest() """
    @property
    def Accept(self) -> str:
        """
        Get: Accept(self: HttpWebRequest) -> str
        Set: Accept(self: HttpWebRequest) = value
        """
        ...

    @property
    def Address(self) -> Uri:
        """ Get: Address(self: HttpWebRequest) -> Uri """
        ...

    @property
    def AllowAutoRedirect(self) -> bool:
        """
        Get: AllowAutoRedirect(self: HttpWebRequest) -> bool
        Set: AllowAutoRedirect(self: HttpWebRequest) = value
        """
        ...

    @property
    def AllowReadStreamBuffering(self) -> bool:
        """
        Get: AllowReadStreamBuffering(self: HttpWebRequest) -> bool
        Set: AllowReadStreamBuffering(self: HttpWebRequest) = value
        """
        ...

    @property
    def AllowWriteStreamBuffering(self) -> bool:
        """
        Get: AllowWriteStreamBuffering(self: HttpWebRequest) -> bool
        Set: AllowWriteStreamBuffering(self: HttpWebRequest) = value
        """
        ...

    @property
    def AutomaticDecompression(self) -> DecompressionMethods:
        """
        Get: AutomaticDecompression(self: HttpWebRequest) -> DecompressionMethods
        Set: AutomaticDecompression(self: HttpWebRequest) = value
        """
        ...

    @property
    def ClientCertificates(self) -> X509CertificateCollection:
        """
        Get: ClientCertificates(self: HttpWebRequest) -> X509CertificateCollection
        Set: ClientCertificates(self: HttpWebRequest) = value
        """
        ...

    @property
    def Connection(self) -> str:
        """
        Get: Connection(self: HttpWebRequest) -> str
        Set: Connection(self: HttpWebRequest) = value
        """
        ...

    @property
    def ContinueDelegate(self) -> HttpContinueDelegate:
        """
        Get: ContinueDelegate(self: HttpWebRequest) -> HttpContinueDelegate
        Set: ContinueDelegate(self: HttpWebRequest) = value
        """
        ...

    @property
    def ContinueTimeout(self) -> int:
        """
        Get: ContinueTimeout(self: HttpWebRequest) -> int
        Set: ContinueTimeout(self: HttpWebRequest) = value
        """
        ...

    @property
    def CookieContainer(self) -> CookieContainer:
        """
        Get: CookieContainer(self: HttpWebRequest) -> CookieContainer
        Set: CookieContainer(self: HttpWebRequest) = value
        """
        ...

    @property
    def Date(self) -> DateTime:
        """
        Get: Date(self: HttpWebRequest) -> DateTime
        Set: Date(self: HttpWebRequest) = value
        """
        ...

    @property
    def DefaultMaximumErrorResponseLength(self) -> int:
        """
        Get: DefaultMaximumErrorResponseLength() -> int
        Set: DefaultMaximumErrorResponseLength() = value
        """
        ...

    @property
    def DefaultMaximumResponseHeadersLength(self) -> int:
        """
        Get: DefaultMaximumResponseHeadersLength() -> int
        Set: DefaultMaximumResponseHeadersLength() = value
        """
        ...

    @property
    def Expect(self) -> str:
        """
        Get: Expect(self: HttpWebRequest) -> str
        Set: Expect(self: HttpWebRequest) = value
        """
        ...

    @property
    def HaveResponse(self) -> bool:
        """ Get: HaveResponse(self: HttpWebRequest) -> bool """
        ...

    @property
    def Host(self) -> str:
        """
        Get: Host(self: HttpWebRequest) -> str
        Set: Host(self: HttpWebRequest) = value
        """
        ...

    @property
    def IfModifiedSince(self) -> DateTime:
        """
        Get: IfModifiedSince(self: HttpWebRequest) -> DateTime
        Set: IfModifiedSince(self: HttpWebRequest) = value
        """
        ...

    @property
    def KeepAlive(self) -> bool:
        """
        Get: KeepAlive(self: HttpWebRequest) -> bool
        Set: KeepAlive(self: HttpWebRequest) = value
        """
        ...

    @property
    def MaximumAutomaticRedirections(self) -> int:
        """
        Get: MaximumAutomaticRedirections(self: HttpWebRequest) -> int
        Set: MaximumAutomaticRedirections(self: HttpWebRequest) = value
        """
        ...

    @property
    def MaximumResponseHeadersLength(self) -> int:
        """
        Get: MaximumResponseHeadersLength(self: HttpWebRequest) -> int
        Set: MaximumResponseHeadersLength(self: HttpWebRequest) = value
        """
        ...

    @property
    def MediaType(self) -> str:
        """
        Get: MediaType(self: HttpWebRequest) -> str
        Set: MediaType(self: HttpWebRequest) = value
        """
        ...

    @property
    def Pipelined(self) -> bool:
        """
        Get: Pipelined(self: HttpWebRequest) -> bool
        Set: Pipelined(self: HttpWebRequest) = value
        """
        ...

    @property
    def ProtocolVersion(self) -> Version:
        """
        Get: ProtocolVersion(self: HttpWebRequest) -> Version
        Set: ProtocolVersion(self: HttpWebRequest) = value
        """
        ...

    @property
    def ReadWriteTimeout(self) -> int:
        """
        Get: ReadWriteTimeout(self: HttpWebRequest) -> int
        Set: ReadWriteTimeout(self: HttpWebRequest) = value
        """
        ...

    @property
    def Referer(self) -> str:
        """
        Get: Referer(self: HttpWebRequest) -> str
        Set: Referer(self: HttpWebRequest) = value
        """
        ...

    @property
    def SendChunked(self) -> bool:
        """
        Get: SendChunked(self: HttpWebRequest) -> bool
        Set: SendChunked(self: HttpWebRequest) = value
        """
        ...

    @property
    def ServerCertificateValidationCallback(self) -> RemoteCertificateValidationCallback:
        """
        Get: ServerCertificateValidationCallback(self: HttpWebRequest) -> RemoteCertificateValidationCallback
        Set: ServerCertificateValidationCallback(self: HttpWebRequest) = value
        """
        ...

    @property
    def ServicePoint(self) -> ServicePoint:
        """ Get: ServicePoint(self: HttpWebRequest) -> ServicePoint """
        ...

    @property
    def SupportsCookieContainer(self) -> bool:
        """ Get: SupportsCookieContainer(self: HttpWebRequest) -> bool """
        ...

    @property
    def TransferEncoding(self) -> str:
        """
        Get: TransferEncoding(self: HttpWebRequest) -> str
        Set: TransferEncoding(self: HttpWebRequest) = value
        """
        ...

    @property
    def UnsafeAuthenticatedConnectionSharing(self) -> bool:
        """
        Get: UnsafeAuthenticatedConnectionSharing(self: HttpWebRequest) -> bool
        Set: UnsafeAuthenticatedConnectionSharing(self: HttpWebRequest) = value
        """
        ...

    @property
    def UserAgent(self) -> str:
        """
        Get: UserAgent(self: HttpWebRequest) -> str
        Set: UserAgent(self: HttpWebRequest) = value
        """
        ...


    def AddRange(self, *__args:int): # -> 
        """ AddRange(self: HttpWebRequest, from: int, to: int)AddRange(self: HttpWebRequest, from: Int64, to: Int64)AddRange(self: HttpWebRequest, range: int)AddRange(self: HttpWebRequest, range: Int64)AddRange(self: HttpWebRequest, rangeSpecifier: str, from: int, to: int)AddRange(self: HttpWebRequest, rangeSpecifier: str, from: Int64, to: Int64)AddRange(self: HttpWebRequest, rangeSpecifier: str, range: int)AddRange(self: HttpWebRequest, rangeSpecifier: str, range: Int64) """
        ...

    DefaultCachePolicy: RequestCachePolicy = ...


class HttpWebResponse(WebResponse): # skipped bases: <type 'IDisposable'>, <type 'ISerializable'>, <type 'object'>
    """ HttpWebResponse() """
    @property
    def CharacterSet(self) -> str:
        """ Get: CharacterSet(self: HttpWebResponse) -> str """
        ...

    @property
    def ContentEncoding(self) -> str:
        """ Get: ContentEncoding(self: HttpWebResponse) -> str """
        ...

    @property
    def Cookies(self) -> CookieCollection:
        """
        Get: Cookies(self: HttpWebResponse) -> CookieCollection
        Set: Cookies(self: HttpWebResponse) = value
        """
        ...

    @property
    def LastModified(self) -> DateTime:
        """ Get: LastModified(self: HttpWebResponse) -> DateTime """
        ...

    @property
    def Method(self) -> str:
        """ Get: Method(self: HttpWebResponse) -> str """
        ...

    @property
    def ProtocolVersion(self) -> Version:
        """ Get: ProtocolVersion(self: HttpWebResponse) -> Version """
        ...

    @property
    def Server(self) -> str:
        """ Get: Server(self: HttpWebResponse) -> str """
        ...

    @property
    def StatusCode(self) -> HttpStatusCode:
        """ Get: StatusCode(self: HttpWebResponse) -> HttpStatusCode """
        ...

    @property
    def StatusDescription(self) -> str:
        """ Get: StatusDescription(self: HttpWebResponse) -> str """
        ...


    def GetResponseHeader(self, headerName:str) -> str:
        """ GetResponseHeader(self: HttpWebResponse, headerName: str) -> str """
        ...


class IAuthenticationModule: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def AuthenticationType(self) -> str:
        """ Get: AuthenticationType(self: IAuthenticationModule) -> str """
        ...

    @property
    def CanPreAuthenticate(self) -> bool:
        """ Get: CanPreAuthenticate(self: IAuthenticationModule) -> bool """
        ...


    def Authenticate(self, challenge:str, request:WebRequest, credentials:ICredentials) -> Authorization:
        """ Authenticate(self: IAuthenticationModule, challenge: str, request: WebRequest, credentials: ICredentials) -> Authorization """
        ...

    def PreAuthenticate(self, request:WebRequest, credentials:ICredentials) -> Authorization:
        """ PreAuthenticate(self: IAuthenticationModule, request: WebRequest, credentials: ICredentials) -> Authorization """
        ...


class ICertificatePolicy: # skipped bases: <type 'object'>
    """ no doc """
    def CheckValidationResult(self, srvPoint:ServicePoint, certificate:X509Certificate, request:WebRequest, certificateProblem:int) -> bool:
        """ CheckValidationResult(self: ICertificatePolicy, srvPoint: ServicePoint, certificate: X509Certificate, request: WebRequest, certificateProblem: int) -> bool """
        ...


class ICredentialPolicy: # skipped bases: <type 'object'>
    """ no doc """
    def ShouldSendCredential(self, challengeUri:Uri, request:WebRequest, credential:NetworkCredential, authenticationModule:IAuthenticationModule) -> bool:
        """ ShouldSendCredential(self: ICredentialPolicy, challengeUri: Uri, request: WebRequest, credential: NetworkCredential, authenticationModule: IAuthenticationModule) -> bool """
        ...


class ICredentials: # skipped bases: <type 'object'>
    """ no doc """
    def GetCredential(self, uri:Uri, authType:str) -> NetworkCredential:
        """ GetCredential(self: ICredentials, uri: Uri, authType: str) -> NetworkCredential """
        ...


class ICredentialsByHost: # skipped bases: <type 'object'>
    """ no doc """
    def GetCredential(self, host:str, port:int, authenticationType:str) -> NetworkCredential:
        """ GetCredential(self: ICredentialsByHost, host: str, port: int, authenticationType: str) -> NetworkCredential """
        ...


class INetworkProgress: # skipped bases: <type 'object'>
    """ no doc """
    ProgressChanged = ...
    ProgressCompleted = ...
    ProgressFailed = ...


class IPAddress: # skipped bases: <type 'object'>, <type 'object'>
    """
    IPAddress(newAddress: Int64)
    IPAddress(address: Array[Byte], scopeid: Int64)
    IPAddress(address: Array[Byte])
    """
    @property
    def Address(self) -> Int64:
        """
        Get: Address(self: IPAddress) -> Int64
        Set: Address(self: IPAddress) = value
        """
        ...

    @property
    def AddressFamily(self) -> AddressFamily:
        """ Get: AddressFamily(self: IPAddress) -> AddressFamily """
        ...

    @property
    def IsIPv4MappedToIPv6(self) -> bool:
        """ Get: IsIPv4MappedToIPv6(self: IPAddress) -> bool """
        ...

    @property
    def IsIPv6LinkLocal(self) -> bool:
        """ Get: IsIPv6LinkLocal(self: IPAddress) -> bool """
        ...

    @property
    def IsIPv6Multicast(self) -> bool:
        """ Get: IsIPv6Multicast(self: IPAddress) -> bool """
        ...

    @property
    def IsIPv6SiteLocal(self) -> bool:
        """ Get: IsIPv6SiteLocal(self: IPAddress) -> bool """
        ...

    @property
    def IsIPv6Teredo(self) -> bool:
        """ Get: IsIPv6Teredo(self: IPAddress) -> bool """
        ...

    @property
    def ScopeId(self) -> Int64:
        """
        Get: ScopeId(self: IPAddress) -> Int64
        Set: ScopeId(self: IPAddress) = value
        """
        ...


    def Equals(self, comparand:object) -> bool:
        """ Equals(self: IPAddress, comparand: object) -> bool """
        ...

    def GetAddressBytes(self) -> Array:
        """ GetAddressBytes(self: IPAddress) -> Array[Byte] """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: IPAddress) -> int """
        ...

    @staticmethod
    def HostToNetworkOrder(host:Int64) -> Int64:
        """
        HostToNetworkOrder(host: Int64) -> Int64
        HostToNetworkOrder(host: int) -> int
        HostToNetworkOrder(host: Int16) -> Int16
        """
        ...

    @staticmethod
    def IsLoopback(address:IPAddress) -> bool:
        """ IsLoopback(address: IPAddress) -> bool """
        ...

    def MapToIPv4(self) -> IPAddress:
        """ MapToIPv4(self: IPAddress) -> IPAddress """
        ...

    def MapToIPv6(self) -> IPAddress:
        """ MapToIPv6(self: IPAddress) -> IPAddress """
        ...

    @staticmethod
    def NetworkToHostOrder(network:Int64) -> Int64:
        """
        NetworkToHostOrder(network: Int64) -> Int64
        NetworkToHostOrder(network: int) -> int
        NetworkToHostOrder(network: Int16) -> Int16
        """
        ...

    @staticmethod
    def Parse(ipString:str) -> IPAddress:
        """ Parse(ipString: str) -> IPAddress """
        ...

    def ToString(self) -> str:
        """ ToString(self: IPAddress) -> str """
        ...

    @staticmethod
    def TryParse(ipString, address) -> Tuple_[bool, IPAddress]:
        """ TryParse(ipString: str) -> (bool, IPAddress) """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    Any: IPAddress = ...
    Broadcast: IPAddress = ...
    IPv6Any: IPAddress = ...
    IPv6Loopback: IPAddress = ...
    IPv6None: IPAddress = ...
    Loopback: IPAddress = ...


class IPEndPoint(EndPoint): # skipped bases: <type 'object'>
    """
    IPEndPoint(address: Int64, port: int)
    IPEndPoint(address: IPAddress, port: int)
    """
    @property
    def Address(self) -> IPAddress:
        """
        Get: Address(self: IPEndPoint) -> IPAddress
        Set: Address(self: IPEndPoint) = value
        """
        ...

    @property
    def Port(self) -> int:
        """
        Get: Port(self: IPEndPoint) -> int
        Set: Port(self: IPEndPoint) = value
        """
        ...


    def Equals(self, comparand:object) -> bool:
        """ Equals(self: IPEndPoint, comparand: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: IPEndPoint) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: IPEndPoint) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __new__(cls, address:Int64, port:int) -> Self:
        """
        __new__(cls: type, address: Int64, port: int)
        __new__(cls: type, address: IPAddress, port: int)
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    MaxPort: int = ...
    MinPort: int = ...


class IPEndPointCollection(Collection): # skipped bases: <type 'ICollection[IPEndPoint]'>, <type 'IEnumerable'>, <type 'IList'>, <type 'IReadOnlyCollection[IPEndPoint]'>, <type 'IEnumerable[IPEndPoint]'>, <type 'IReadOnlyList[IPEndPoint]'>, <type 'ICollection'>, <type 'IList[IPEndPoint]'>, <type 'object'>
    """ IPEndPointCollection() """
    pass

class IPHostEntry: # skipped bases: <type 'object'>, <type 'object'>
    """ IPHostEntry() """
    @property
    def AddressList(self) -> Array:
        """
        Get: AddressList(self: IPHostEntry) -> Array[IPAddress]
        Set: AddressList(self: IPHostEntry) = value
        """
        ...

    @property
    def Aliases(self) -> Array:
        """
        Get: Aliases(self: IPHostEntry) -> Array[str]
        Set: Aliases(self: IPHostEntry) = value
        """
        ...

    @property
    def HostName(self) -> str:
        """
        Get: HostName(self: IPHostEntry) -> str
        Set: HostName(self: IPHostEntry) = value
        """
        ...



class IUnsafeWebRequestCreate: # skipped bases: <type 'object'>
    """ no doc """
    def Create(self, uri:Uri) -> WebRequest:
        """ Create(self: IUnsafeWebRequestCreate, uri: Uri) -> WebRequest """
        ...


class IWebProxy: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Credentials(self) -> ICredentials:
        """
        Get: Credentials(self: IWebProxy) -> ICredentials
        Set: Credentials(self: IWebProxy) = value
        """
        ...


    def GetProxy(self, destination:Uri) -> Uri:
        """ GetProxy(self: IWebProxy, destination: Uri) -> Uri """
        ...

    def IsBypassed(self, host:Uri) -> bool:
        """ IsBypassed(self: IWebProxy, host: Uri) -> bool """
        ...


class IWebProxyScript: # skipped bases: <type 'object'>
    """ no doc """
    def Close(self): # -> 
        """ Close(self: IWebProxyScript) """
        ...

    def Load(self, scriptLocation:Uri, script:str, helperType:Type) -> bool:
        """ Load(self: IWebProxyScript, scriptLocation: Uri, script: str, helperType: Type) -> bool """
        ...

    def Run(self, url:str, host:str) -> str:
        """ Run(self: IWebProxyScript, url: str, host: str) -> str """
        ...


class IWebRequestCreate: # skipped bases: <type 'object'>
    """ no doc """
    def Create(self, uri:Uri) -> WebRequest:
        """ Create(self: IWebRequestCreate, uri: Uri) -> WebRequest """
        ...


class NetworkAccess(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) NetworkAccess, values: Accept (128), Connect (64) """
    Accept: NetworkAccess = ...
    Connect: NetworkAccess = ...
    value__ = ...


class NetworkCredential(ICredentials, ICredentialsByHost): # skipped bases: <type 'object'>
    """
    NetworkCredential()
    NetworkCredential(userName: str, password: str)
    NetworkCredential(userName: str, password: SecureString)
    NetworkCredential(userName: str, password: str, domain: str)
    NetworkCredential(userName: str, password: SecureString, domain: str)
    """
    @property
    def Domain(self) -> str:
        """
        Get: Domain(self: NetworkCredential) -> str
        Set: Domain(self: NetworkCredential) = value
        """
        ...

    @property
    def Password(self) -> str:
        """
        Get: Password(self: NetworkCredential) -> str
        Set: Password(self: NetworkCredential) = value
        """
        ...

    @property
    def SecurePassword(self) -> SecureString:
        """
        Get: SecurePassword(self: NetworkCredential) -> SecureString
        Set: SecurePassword(self: NetworkCredential) = value
        """
        ...

    @property
    def UserName(self) -> str:
        """
        Get: UserName(self: NetworkCredential) -> str
        Set: UserName(self: NetworkCredential) = value
        """
        ...



class NetworkProgressChangedEventArgs(ProgressChangedEventArgs): # skipped bases: <type 'object'>
    """ NetworkProgressChangedEventArgs(percentage: int, processedBytes: int, totalBytes: int, userState: object) """
    @property
    def ProcessedBytes(self) -> int:
        """ Get: ProcessedBytes(self: NetworkProgressChangedEventArgs) -> int """
        ...

    @property
    def TotalBytes(self) -> int:
        """ Get: TotalBytes(self: NetworkProgressChangedEventArgs) -> int """
        ...



class OpenReadCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Result(self) -> Stream:
        """ Get: Result(self: OpenReadCompletedEventArgs) -> Stream """
        ...



class OpenReadCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OpenReadCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:OpenReadCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: OpenReadCompletedEventHandler, sender: object, e: OpenReadCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: OpenReadCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:OpenReadCompletedEventArgs): # -> 
        """ Invoke(self: OpenReadCompletedEventHandler, sender: object, e: OpenReadCompletedEventArgs) """
        ...


class OpenWriteCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Result(self) -> Stream:
        """ Get: Result(self: OpenWriteCompletedEventArgs) -> Stream """
        ...



class OpenWriteCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ OpenWriteCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:OpenWriteCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: OpenWriteCompletedEventHandler, sender: object, e: OpenWriteCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: OpenWriteCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:OpenWriteCompletedEventArgs): # -> 
        """ Invoke(self: OpenWriteCompletedEventHandler, sender: object, e: OpenWriteCompletedEventArgs) """
        ...


class ProtocolViolationException(InvalidOperationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    ProtocolViolationException()
    ProtocolViolationException(message: str)
    """
    def GetObjectData(self, serializationInfo:SerializationInfo, streamingContext:StreamingContext): # -> 
        """ GetObjectData(self: ProtocolViolationException, serializationInfo: SerializationInfo, streamingContext: StreamingContext) """
        ...

    SerializeObjectState = ...


class SecurityProtocolType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SecurityProtocolType, values: Ssl3 (48), SystemDefault (0), Tls (192), Tls11 (768), Tls12 (3072), Tls13 (12288) """
    Ssl3: SecurityProtocolType = ...
    SystemDefault: SecurityProtocolType = ...
    Tls: SecurityProtocolType = ...
    Tls11: SecurityProtocolType = ...
    Tls12: SecurityProtocolType = ...
    Tls13: SecurityProtocolType = ...
    value__ = ...


class ServicePoint: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Address(self) -> Uri:
        """ Get: Address(self: ServicePoint) -> Uri """
        ...

    @property
    def BindIPEndPointDelegate(self) -> BindIPEndPoint:
        """
        Get: BindIPEndPointDelegate(self: ServicePoint) -> BindIPEndPoint
        Set: BindIPEndPointDelegate(self: ServicePoint) = value
        """
        ...

    @property
    def Certificate(self) -> X509Certificate:
        """ Get: Certificate(self: ServicePoint) -> X509Certificate """
        ...

    @property
    def ClientCertificate(self) -> X509Certificate:
        """ Get: ClientCertificate(self: ServicePoint) -> X509Certificate """
        ...

    @property
    def ConnectionLeaseTimeout(self) -> int:
        """
        Get: ConnectionLeaseTimeout(self: ServicePoint) -> int
        Set: ConnectionLeaseTimeout(self: ServicePoint) = value
        """
        ...

    @property
    def ConnectionLimit(self) -> int:
        """
        Get: ConnectionLimit(self: ServicePoint) -> int
        Set: ConnectionLimit(self: ServicePoint) = value
        """
        ...

    @property
    def ConnectionName(self) -> str:
        """ Get: ConnectionName(self: ServicePoint) -> str """
        ...

    @property
    def CurrentConnections(self) -> int:
        """ Get: CurrentConnections(self: ServicePoint) -> int """
        ...

    @property
    def Expect100Continue(self) -> bool:
        """
        Get: Expect100Continue(self: ServicePoint) -> bool
        Set: Expect100Continue(self: ServicePoint) = value
        """
        ...

    @property
    def IdleSince(self) -> DateTime:
        """ Get: IdleSince(self: ServicePoint) -> DateTime """
        ...

    @property
    def MaxIdleTime(self) -> int:
        """
        Get: MaxIdleTime(self: ServicePoint) -> int
        Set: MaxIdleTime(self: ServicePoint) = value
        """
        ...

    @property
    def ProtocolVersion(self) -> Version:
        """ Get: ProtocolVersion(self: ServicePoint) -> Version """
        ...

    @property
    def ReceiveBufferSize(self) -> int:
        """
        Get: ReceiveBufferSize(self: ServicePoint) -> int
        Set: ReceiveBufferSize(self: ServicePoint) = value
        """
        ...

    @property
    def SupportsPipelining(self) -> bool:
        """ Get: SupportsPipelining(self: ServicePoint) -> bool """
        ...

    @property
    def UseNagleAlgorithm(self) -> bool:
        """
        Get: UseNagleAlgorithm(self: ServicePoint) -> bool
        Set: UseNagleAlgorithm(self: ServicePoint) = value
        """
        ...


    def CloseConnectionGroup(self, connectionGroupName:str) -> bool:
        """ CloseConnectionGroup(self: ServicePoint, connectionGroupName: str) -> bool """
        ...

    def SetTcpKeepAlive(self, enabled:bool, keepAliveTime:int, keepAliveInterval:int): # -> 
        """ SetTcpKeepAlive(self: ServicePoint, enabled: bool, keepAliveTime: int, keepAliveInterval: int) """
        ...


class ServicePointManager: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def CertificatePolicy(self) -> ICertificatePolicy:
        """
        Get: CertificatePolicy() -> ICertificatePolicy
        Set: CertificatePolicy() = value
        """
        ...

    @property
    def CheckCertificateRevocationList(self) -> bool:
        """
        Get: CheckCertificateRevocationList() -> bool
        Set: CheckCertificateRevocationList() = value
        """
        ...

    @property
    def DefaultConnectionLimit(self) -> int:
        """
        Get: DefaultConnectionLimit() -> int
        Set: DefaultConnectionLimit() = value
        """
        ...

    @property
    def DnsRefreshTimeout(self) -> int:
        """
        Get: DnsRefreshTimeout() -> int
        Set: DnsRefreshTimeout() = value
        """
        ...

    @property
    def EnableDnsRoundRobin(self) -> bool:
        """
        Get: EnableDnsRoundRobin() -> bool
        Set: EnableDnsRoundRobin() = value
        """
        ...

    @property
    def EncryptionPolicy(self) -> EncryptionPolicy:
        """ Get: EncryptionPolicy() -> EncryptionPolicy """
        ...

    @property
    def Expect100Continue(self) -> bool:
        """
        Get: Expect100Continue() -> bool
        Set: Expect100Continue() = value
        """
        ...

    @property
    def MaxServicePointIdleTime(self) -> int:
        """
        Get: MaxServicePointIdleTime() -> int
        Set: MaxServicePointIdleTime() = value
        """
        ...

    @property
    def MaxServicePoints(self) -> int:
        """
        Get: MaxServicePoints() -> int
        Set: MaxServicePoints() = value
        """
        ...

    @property
    def ReusePort(self) -> bool:
        """
        Get: ReusePort() -> bool
        Set: ReusePort() = value
        """
        ...

    @property
    def SecurityProtocol(self) -> SecurityProtocolType:
        """
        Get: SecurityProtocol() -> SecurityProtocolType
        Set: SecurityProtocol() = value
        """
        ...

    @property
    def ServerCertificateValidationCallback(self) -> RemoteCertificateValidationCallback:
        """
        Get: ServerCertificateValidationCallback() -> RemoteCertificateValidationCallback
        Set: ServerCertificateValidationCallback() = value
        """
        ...

    @property
    def UseNagleAlgorithm(self) -> bool:
        """
        Get: UseNagleAlgorithm() -> bool
        Set: UseNagleAlgorithm() = value
        """
        ...


    @staticmethod
    def FindServicePoint(*__args:Uri) -> ServicePoint:
        """
        FindServicePoint(address: Uri) -> ServicePoint
        FindServicePoint(uriString: str, proxy: IWebProxy) -> ServicePoint
        FindServicePoint(address: Uri, proxy: IWebProxy) -> ServicePoint
        """
        ...

    @staticmethod
    def SetTcpKeepAlive(enabled:bool, keepAliveTime:int, keepAliveInterval:int): # -> 
        """ SetTcpKeepAlive(enabled: bool, keepAliveTime: int, keepAliveInterval: int) """
        ...

    DefaultNonPersistentConnectionLimit: int = ...
    DefaultPersistentConnectionLimit: int = ...


class SocketAddress: # skipped bases: <type 'object'>, <type 'object'>
    """
    SocketAddress(family: AddressFamily)
    SocketAddress(family: AddressFamily, size: int)
    """
    @property
    def Family(self) -> AddressFamily:
        """ Get: Family(self: SocketAddress) -> AddressFamily """
        ...

    @property
    def Size(self) -> int:
        """ Get: Size(self: SocketAddress) -> int """
        ...


    def Equals(self, comparand:object) -> bool:
        """ Equals(self: SocketAddress, comparand: object) -> bool """
        ...

    def GetHashCode(self) -> int:
        """ GetHashCode(self: SocketAddress) -> int """
        ...

    def ToString(self) -> str:
        """ ToString(self: SocketAddress) -> str """
        ...

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class SocketPermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    SocketPermission(state: PermissionState)
    SocketPermission(access: NetworkAccess, transport: TransportType, hostName: str, portNumber: int)
    """
    @property
    def AcceptList(self) -> IEnumerator:
        """ Get: AcceptList(self: SocketPermission) -> IEnumerator """
        ...

    @property
    def ConnectList(self) -> IEnumerator:
        """ Get: ConnectList(self: SocketPermission) -> IEnumerator """
        ...


    def AddPermission(self, access:NetworkAccess, transport:TransportType, hostName:str, portNumber:int): # -> 
        """ AddPermission(self: SocketPermission, access: NetworkAccess, transport: TransportType, hostName: str, portNumber: int) """
        ...

    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type, access: NetworkAccess, transport: TransportType, hostName: str, portNumber: int)
        """
        ...

    AllPorts: int = ...


class SocketPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SocketPermissionAttribute(action: SecurityAction) """
    @property
    def Access(self) -> str:
        """
        Get: Access(self: SocketPermissionAttribute) -> str
        Set: Access(self: SocketPermissionAttribute) = value
        """
        ...

    @property
    def Host(self) -> str:
        """
        Get: Host(self: SocketPermissionAttribute) -> str
        Set: Host(self: SocketPermissionAttribute) = value
        """
        ...

    @property
    def Port(self) -> str:
        """
        Get: Port(self: SocketPermissionAttribute) -> str
        Set: Port(self: SocketPermissionAttribute) = value
        """
        ...

    @property
    def Transport(self) -> str:
        """
        Get: Transport(self: SocketPermissionAttribute) -> str
        Set: Transport(self: SocketPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: SocketPermissionAttribute) -> IPermission """
        ...


class TransportContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def GetChannelBinding(self, kind:ChannelBindingKind) -> ChannelBinding:
        """ GetChannelBinding(self: TransportContext, kind: ChannelBindingKind) -> ChannelBinding """
        ...

    def GetTlsTokenBindings(self) -> IEnumerable:
        """ GetTlsTokenBindings(self: TransportContext) -> IEnumerable[TokenBinding] """
        ...


class TransportType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum TransportType, values: All (3), Connectionless (1), ConnectionOriented (2), Tcp (2), Udp (1) """
    All: TransportType = ...
    Connectionless: TransportType = ...
    ConnectionOriented: TransportType = ...
    Tcp: TransportType = ...
    Udp: TransportType = ...
    value__ = ...


class UiSynchronizationContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Current(self) -> SynchronizationContext:
        """
        Get: Current() -> SynchronizationContext
        Set: Current() = value
        """
        ...

    @property
    def ManagedUiThreadId(self) -> int:
        """
        Get: ManagedUiThreadId() -> int
        Set: ManagedUiThreadId() = value
        """
        ...


    __all__: list = ...


class UploadDataCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Result(self) -> Array:
        """ Get: Result(self: UploadDataCompletedEventArgs) -> Array[Byte] """
        ...



class UploadDataCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ UploadDataCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:UploadDataCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: UploadDataCompletedEventHandler, sender: object, e: UploadDataCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: UploadDataCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:UploadDataCompletedEventArgs): # -> 
        """ Invoke(self: UploadDataCompletedEventHandler, sender: object, e: UploadDataCompletedEventArgs) """
        ...


class UploadFileCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Result(self) -> Array:
        """ Get: Result(self: UploadFileCompletedEventArgs) -> Array[Byte] """
        ...



class UploadFileCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ UploadFileCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:UploadFileCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: UploadFileCompletedEventHandler, sender: object, e: UploadFileCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: UploadFileCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:UploadFileCompletedEventArgs): # -> 
        """ Invoke(self: UploadFileCompletedEventHandler, sender: object, e: UploadFileCompletedEventArgs) """
        ...


class UploadProgressChangedEventArgs(ProgressChangedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def BytesReceived(self) -> Int64:
        """ Get: BytesReceived(self: UploadProgressChangedEventArgs) -> Int64 """
        ...

    @property
    def BytesSent(self) -> Int64:
        """ Get: BytesSent(self: UploadProgressChangedEventArgs) -> Int64 """
        ...

    @property
    def TotalBytesToReceive(self) -> Int64:
        """ Get: TotalBytesToReceive(self: UploadProgressChangedEventArgs) -> Int64 """
        ...

    @property
    def TotalBytesToSend(self) -> Int64:
        """ Get: TotalBytesToSend(self: UploadProgressChangedEventArgs) -> Int64 """
        ...



class UploadProgressChangedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ UploadProgressChangedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:UploadProgressChangedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: UploadProgressChangedEventHandler, sender: object, e: UploadProgressChangedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: UploadProgressChangedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:UploadProgressChangedEventArgs): # -> 
        """ Invoke(self: UploadProgressChangedEventHandler, sender: object, e: UploadProgressChangedEventArgs) """
        ...


class UploadStringCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Result(self) -> str:
        """ Get: Result(self: UploadStringCompletedEventArgs) -> str """
        ...



class UploadStringCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ UploadStringCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:UploadStringCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: UploadStringCompletedEventHandler, sender: object, e: UploadStringCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: UploadStringCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:UploadStringCompletedEventArgs): # -> 
        """ Invoke(self: UploadStringCompletedEventHandler, sender: object, e: UploadStringCompletedEventArgs) """
        ...


class UploadValuesCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Result(self) -> Array:
        """ Get: Result(self: UploadValuesCompletedEventArgs) -> Array[Byte] """
        ...



class UploadValuesCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ UploadValuesCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:UploadValuesCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: UploadValuesCompletedEventHandler, sender: object, e: UploadValuesCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: UploadValuesCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:UploadValuesCompletedEventArgs): # -> 
        """ Invoke(self: UploadValuesCompletedEventHandler, sender: object, e: UploadValuesCompletedEventArgs) """
        ...


class WebClient(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ WebClient() """
    @property
    def AllowReadStreamBuffering(self) -> bool:
        """
        Get: AllowReadStreamBuffering(self: WebClient) -> bool
        Set: AllowReadStreamBuffering(self: WebClient) = value
        """
        ...

    @property
    def AllowWriteStreamBuffering(self) -> bool:
        """
        Get: AllowWriteStreamBuffering(self: WebClient) -> bool
        Set: AllowWriteStreamBuffering(self: WebClient) = value
        """
        ...

    @property
    def BaseAddress(self) -> str:
        """
        Get: BaseAddress(self: WebClient) -> str
        Set: BaseAddress(self: WebClient) = value
        """
        ...

    @property
    def CachePolicy(self) -> RequestCachePolicy:
        """
        Get: CachePolicy(self: WebClient) -> RequestCachePolicy
        Set: CachePolicy(self: WebClient) = value
        """
        ...

    @property
    def Credentials(self) -> ICredentials:
        """
        Get: Credentials(self: WebClient) -> ICredentials
        Set: Credentials(self: WebClient) = value
        """
        ...

    @property
    def Encoding(self) -> Encoding:
        """
        Get: Encoding(self: WebClient) -> Encoding
        Set: Encoding(self: WebClient) = value
        """
        ...

    @property
    def Headers(self) -> WebHeaderCollection:
        """
        Get: Headers(self: WebClient) -> WebHeaderCollection
        Set: Headers(self: WebClient) = value
        """
        ...

    @property
    def IsBusy(self) -> bool:
        """ Get: IsBusy(self: WebClient) -> bool """
        ...

    @property
    def Proxy(self) -> IWebProxy:
        """
        Get: Proxy(self: WebClient) -> IWebProxy
        Set: Proxy(self: WebClient) = value
        """
        ...

    @property
    def QueryString(self) -> NameValueCollection:
        """
        Get: QueryString(self: WebClient) -> NameValueCollection
        Set: QueryString(self: WebClient) = value
        """
        ...

    @property
    def ResponseHeaders(self) -> WebHeaderCollection:
        """ Get: ResponseHeaders(self: WebClient) -> WebHeaderCollection """
        ...

    @property
    def UseDefaultCredentials(self) -> bool:
        """
        Get: UseDefaultCredentials(self: WebClient) -> bool
        Set: UseDefaultCredentials(self: WebClient) = value
        """
        ...


    def CancelAsync(self): # -> 
        """ CancelAsync(self: WebClient) """
        ...

    def DownloadData(self, address:str) -> Array:
        """
        DownloadData(self: WebClient, address: str) -> Array[Byte]
        DownloadData(self: WebClient, address: Uri) -> Array[Byte]
        """
        ...

    def DownloadDataAsync(self, address:Uri, userToken:object = ...): # -> 
        """ DownloadDataAsync(self: WebClient, address: Uri)DownloadDataAsync(self: WebClient, address: Uri, userToken: object) """
        ...

    def DownloadDataTaskAsync(self, address:str) -> Task:
        """
        DownloadDataTaskAsync(self: WebClient, address: str) -> Task[Array[Byte]]
        DownloadDataTaskAsync(self: WebClient, address: Uri) -> Task[Array[Byte]]
        """
        ...

    def DownloadFile(self, address:str, fileName:str): # -> 
        """ DownloadFile(self: WebClient, address: str, fileName: str)DownloadFile(self: WebClient, address: Uri, fileName: str) """
        ...

    def DownloadFileAsync(self, address:Uri, fileName:str, userToken:object = ...): # -> 
        """ DownloadFileAsync(self: WebClient, address: Uri, fileName: str)DownloadFileAsync(self: WebClient, address: Uri, fileName: str, userToken: object) """
        ...

    def DownloadFileTaskAsync(self, address:str, fileName:str) -> Task:
        """
        DownloadFileTaskAsync(self: WebClient, address: str, fileName: str) -> Task
        DownloadFileTaskAsync(self: WebClient, address: Uri, fileName: str) -> Task
        """
        ...

    def DownloadString(self, address:str) -> str:
        """
        DownloadString(self: WebClient, address: str) -> str
        DownloadString(self: WebClient, address: Uri) -> str
        """
        ...

    def DownloadStringAsync(self, address:Uri, userToken:object = ...): # -> 
        """ DownloadStringAsync(self: WebClient, address: Uri)DownloadStringAsync(self: WebClient, address: Uri, userToken: object) """
        ...

    def DownloadStringTaskAsync(self, address:str) -> Task:
        """
        DownloadStringTaskAsync(self: WebClient, address: str) -> Task[str]
        DownloadStringTaskAsync(self: WebClient, address: Uri) -> Task[str]
        """
        ...

    def GetWebRequest(self, *args): #cannot find CLR method
        """ GetWebRequest(self: WebClient, address: Uri) -> WebRequest """
        ...

    def GetWebResponse(self, *args): #cannot find CLR method
        """
        GetWebResponse(self: WebClient, request: WebRequest) -> WebResponse
        GetWebResponse(self: WebClient, request: WebRequest, result: IAsyncResult) -> WebResponse
        """
        ...

    def OnDownloadDataCompleted(self, *args): #cannot find CLR method
        """ OnDownloadDataCompleted(self: WebClient, e: DownloadDataCompletedEventArgs) """
        ...

    def OnDownloadFileCompleted(self, *args): #cannot find CLR method
        """ OnDownloadFileCompleted(self: WebClient, e: AsyncCompletedEventArgs) """
        ...

    def OnDownloadProgressChanged(self, *args): #cannot find CLR method
        """ OnDownloadProgressChanged(self: WebClient, e: DownloadProgressChangedEventArgs) """
        ...

    def OnDownloadStringCompleted(self, *args): #cannot find CLR method
        """ OnDownloadStringCompleted(self: WebClient, e: DownloadStringCompletedEventArgs) """
        ...

    def OnOpenReadCompleted(self, *args): #cannot find CLR method
        """ OnOpenReadCompleted(self: WebClient, e: OpenReadCompletedEventArgs) """
        ...

    def OnOpenWriteCompleted(self, *args): #cannot find CLR method
        """ OnOpenWriteCompleted(self: WebClient, e: OpenWriteCompletedEventArgs) """
        ...

    def OnUploadDataCompleted(self, *args): #cannot find CLR method
        """ OnUploadDataCompleted(self: WebClient, e: UploadDataCompletedEventArgs) """
        ...

    def OnUploadFileCompleted(self, *args): #cannot find CLR method
        """ OnUploadFileCompleted(self: WebClient, e: UploadFileCompletedEventArgs) """
        ...

    def OnUploadProgressChanged(self, *args): #cannot find CLR method
        """ OnUploadProgressChanged(self: WebClient, e: UploadProgressChangedEventArgs) """
        ...

    def OnUploadStringCompleted(self, *args): #cannot find CLR method
        """ OnUploadStringCompleted(self: WebClient, e: UploadStringCompletedEventArgs) """
        ...

    def OnUploadValuesCompleted(self, *args): #cannot find CLR method
        """ OnUploadValuesCompleted(self: WebClient, e: UploadValuesCompletedEventArgs) """
        ...

    def OnWriteStreamClosed(self, *args): #cannot find CLR method
        """ OnWriteStreamClosed(self: WebClient, e: WriteStreamClosedEventArgs) """
        ...

    def OpenRead(self, address:str) -> Stream:
        """
        OpenRead(self: WebClient, address: str) -> Stream
        OpenRead(self: WebClient, address: Uri) -> Stream
        """
        ...

    def OpenReadAsync(self, address:Uri, userToken:object = ...): # -> 
        """ OpenReadAsync(self: WebClient, address: Uri)OpenReadAsync(self: WebClient, address: Uri, userToken: object) """
        ...

    def OpenReadTaskAsync(self, address:str) -> Task:
        """
        OpenReadTaskAsync(self: WebClient, address: str) -> Task[Stream]
        OpenReadTaskAsync(self: WebClient, address: Uri) -> Task[Stream]
        """
        ...

    def OpenWrite(self, address:str, method:str = ...) -> Stream:
        """
        OpenWrite(self: WebClient, address: str) -> Stream
        OpenWrite(self: WebClient, address: Uri) -> Stream
        OpenWrite(self: WebClient, address: str, method: str) -> Stream
        OpenWrite(self: WebClient, address: Uri, method: str) -> Stream
        """
        ...

    def OpenWriteAsync(self, address:Uri, method:str = ..., userToken:object = ...): # -> 
        """ OpenWriteAsync(self: WebClient, address: Uri)OpenWriteAsync(self: WebClient, address: Uri, method: str)OpenWriteAsync(self: WebClient, address: Uri, method: str, userToken: object) """
        ...

    def OpenWriteTaskAsync(self, address:str, method:str = ...) -> Task:
        """
        OpenWriteTaskAsync(self: WebClient, address: str) -> Task[Stream]
        OpenWriteTaskAsync(self: WebClient, address: Uri) -> Task[Stream]
        OpenWriteTaskAsync(self: WebClient, address: str, method: str) -> Task[Stream]
        OpenWriteTaskAsync(self: WebClient, address: Uri, method: str) -> Task[Stream]
        """
        ...

    def UploadData(self, address:str, *__args:Array) -> Array:
        """
        UploadData(self: WebClient, address: str, data: Array[Byte]) -> Array[Byte]
        UploadData(self: WebClient, address: Uri, data: Array[Byte]) -> Array[Byte]
        UploadData(self: WebClient, address: str, method: str, data: Array[Byte]) -> Array[Byte]
        UploadData(self: WebClient, address: Uri, method: str, data: Array[Byte]) -> Array[Byte]
        """
        ...

    def UploadDataAsync(self, address:Uri, *__args:Array): # -> 
        """ UploadDataAsync(self: WebClient, address: Uri, data: Array[Byte])UploadDataAsync(self: WebClient, address: Uri, method: str, data: Array[Byte])UploadDataAsync(self: WebClient, address: Uri, method: str, data: Array[Byte], userToken: object) """
        ...

    def UploadDataTaskAsync(self, address:str, *__args:Array) -> Task:
        """
        UploadDataTaskAsync(self: WebClient, address: str, data: Array[Byte]) -> Task[Array[Byte]]
        UploadDataTaskAsync(self: WebClient, address: Uri, data: Array[Byte]) -> Task[Array[Byte]]
        UploadDataTaskAsync(self: WebClient, address: str, method: str, data: Array[Byte]) -> Task[Array[Byte]]
        UploadDataTaskAsync(self: WebClient, address: Uri, method: str, data: Array[Byte]) -> Task[Array[Byte]]
        """
        ...

    def UploadFile(self, address:str, *__args:str) -> Array:
        """
        UploadFile(self: WebClient, address: str, fileName: str) -> Array[Byte]
        UploadFile(self: WebClient, address: Uri, fileName: str) -> Array[Byte]
        UploadFile(self: WebClient, address: str, method: str, fileName: str) -> Array[Byte]
        UploadFile(self: WebClient, address: Uri, method: str, fileName: str) -> Array[Byte]
        """
        ...

    def UploadFileAsync(self, address:Uri, *__args:str): # -> 
        """ UploadFileAsync(self: WebClient, address: Uri, fileName: str)UploadFileAsync(self: WebClient, address: Uri, method: str, fileName: str)UploadFileAsync(self: WebClient, address: Uri, method: str, fileName: str, userToken: object) """
        ...

    def UploadFileTaskAsync(self, address:str, *__args:str) -> Task:
        """
        UploadFileTaskAsync(self: WebClient, address: str, fileName: str) -> Task[Array[Byte]]
        UploadFileTaskAsync(self: WebClient, address: Uri, fileName: str) -> Task[Array[Byte]]
        UploadFileTaskAsync(self: WebClient, address: str, method: str, fileName: str) -> Task[Array[Byte]]
        UploadFileTaskAsync(self: WebClient, address: Uri, method: str, fileName: str) -> Task[Array[Byte]]
        """
        ...

    def UploadString(self, address:str, *__args:str) -> str:
        """
        UploadString(self: WebClient, address: str, data: str) -> str
        UploadString(self: WebClient, address: Uri, data: str) -> str
        UploadString(self: WebClient, address: str, method: str, data: str) -> str
        UploadString(self: WebClient, address: Uri, method: str, data: str) -> str
        """
        ...

    def UploadStringAsync(self, address:Uri, *__args:str): # -> 
        """ UploadStringAsync(self: WebClient, address: Uri, data: str)UploadStringAsync(self: WebClient, address: Uri, method: str, data: str)UploadStringAsync(self: WebClient, address: Uri, method: str, data: str, userToken: object) """
        ...

    def UploadStringTaskAsync(self, address:str, *__args:str) -> Task:
        """
        UploadStringTaskAsync(self: WebClient, address: str, data: str) -> Task[str]
        UploadStringTaskAsync(self: WebClient, address: Uri, data: str) -> Task[str]
        UploadStringTaskAsync(self: WebClient, address: str, method: str, data: str) -> Task[str]
        UploadStringTaskAsync(self: WebClient, address: Uri, method: str, data: str) -> Task[str]
        """
        ...

    def UploadValues(self, address:str, *__args:NameValueCollection) -> Array:
        """
        UploadValues(self: WebClient, address: str, data: NameValueCollection) -> Array[Byte]
        UploadValues(self: WebClient, address: Uri, data: NameValueCollection) -> Array[Byte]
        UploadValues(self: WebClient, address: str, method: str, data: NameValueCollection) -> Array[Byte]
        UploadValues(self: WebClient, address: Uri, method: str, data: NameValueCollection) -> Array[Byte]
        """
        ...

    def UploadValuesAsync(self, address:Uri, *__args:NameValueCollection): # -> 
        """ UploadValuesAsync(self: WebClient, address: Uri, data: NameValueCollection)UploadValuesAsync(self: WebClient, address: Uri, method: str, data: NameValueCollection)UploadValuesAsync(self: WebClient, address: Uri, method: str, data: NameValueCollection, userToken: object) """
        ...

    def UploadValuesTaskAsync(self, address:str, *__args:NameValueCollection) -> Task:
        """
        UploadValuesTaskAsync(self: WebClient, address: str, data: NameValueCollection) -> Task[Array[Byte]]
        UploadValuesTaskAsync(self: WebClient, address: str, method: str, data: NameValueCollection) -> Task[Array[Byte]]
        UploadValuesTaskAsync(self: WebClient, address: Uri, data: NameValueCollection) -> Task[Array[Byte]]
        UploadValuesTaskAsync(self: WebClient, address: Uri, method: str, data: NameValueCollection) -> Task[Array[Byte]]
        """
        ...

    DownloadDataCompleted = ...
    DownloadFileCompleted = ...
    DownloadProgressChanged = ...
    DownloadStringCompleted = ...
    OpenReadCompleted = ...
    OpenWriteCompleted = ...
    UploadDataCompleted = ...
    UploadFileCompleted = ...
    UploadProgressChanged = ...
    UploadStringCompleted = ...
    UploadValuesCompleted = ...
    WriteStreamClosed = ...


class WebException(InvalidOperationException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    WebException()
    WebException(message: str)
    WebException(message: str, innerException: Exception)
    WebException(message: str, status: WebExceptionStatus)
    WebException(message: str, innerException: Exception, status: WebExceptionStatus, response: WebResponse)
    """
    @property
    def Response(self) -> WebResponse:
        """ Get: Response(self: WebException) -> WebResponse """
        ...

    @property
    def Status(self) -> WebExceptionStatus:
        """ Get: Status(self: WebException) -> WebExceptionStatus """
        ...


    def GetObjectData(self, serializationInfo:SerializationInfo, streamingContext:StreamingContext): # -> 
        """ GetObjectData(self: WebException, serializationInfo: SerializationInfo, streamingContext: StreamingContext) """
        ...

    SerializeObjectState = ...


class WebExceptionStatus(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WebExceptionStatus, values: CacheEntryNotFound (18), ConnectFailure (2), ConnectionClosed (8), KeepAliveFailure (12), MessageLengthLimitExceeded (17), NameResolutionFailure (1), Pending (13), PipelineFailure (5), ProtocolError (7), ProxyNameResolutionFailure (15), ReceiveFailure (3), RequestCanceled (6), RequestProhibitedByCachePolicy (19), RequestProhibitedByProxy (20), SecureChannelFailure (10), SendFailure (4), ServerProtocolViolation (11), Success (0), Timeout (14), TrustFailure (9), UnknownError (16) """
    CacheEntryNotFound: WebExceptionStatus = ...
    ConnectFailure: WebExceptionStatus = ...
    ConnectionClosed: WebExceptionStatus = ...
    KeepAliveFailure: WebExceptionStatus = ...
    MessageLengthLimitExceeded: WebExceptionStatus = ...
    NameResolutionFailure: WebExceptionStatus = ...
    Pending: WebExceptionStatus = ...
    PipelineFailure: WebExceptionStatus = ...
    ProtocolError: WebExceptionStatus = ...
    ProxyNameResolutionFailure: WebExceptionStatus = ...
    ReceiveFailure: WebExceptionStatus = ...
    RequestCanceled: WebExceptionStatus = ...
    RequestProhibitedByCachePolicy: WebExceptionStatus = ...
    RequestProhibitedByProxy: WebExceptionStatus = ...
    SecureChannelFailure: WebExceptionStatus = ...
    SendFailure: WebExceptionStatus = ...
    ServerProtocolViolation: WebExceptionStatus = ...
    Success: WebExceptionStatus = ...
    Timeout: WebExceptionStatus = ...
    TrustFailure: WebExceptionStatus = ...
    UnknownError: WebExceptionStatus = ...
    value__ = ...


class WebHeaderCollection(NameValueCollection): # skipped bases: <type 'IDeserializationCallback'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'ISerializable'>, <type 'object'>
    """ WebHeaderCollection() """
    @property
    def Keys(self): # -> KeysCollection
        """ Get: Keys(self: WebHeaderCollection) -> KeysCollection """
        ...


    def AddWithoutValidate(self, *args): #cannot find CLR method
        """ AddWithoutValidate(self: WebHeaderCollection, headerName: str, headerValue: str) """
        ...

    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: WebHeaderCollection) -> IEnumerator """
        ...

    @staticmethod
    def IsRestricted(headerName:str, response:bool = ...) -> bool:
        """
        IsRestricted(headerName: str) -> bool
        IsRestricted(headerName: str, response: bool) -> bool
        """
        ...

    def ToByteArray(self) -> Array:
        """ ToByteArray(self: WebHeaderCollection) -> Array[Byte] """
        ...

    def ToString(self) -> str:
        """ ToString(self: WebHeaderCollection) -> str """
        ...

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        ...

    def __str__(self, *args): #cannot find CLR method
        ...


class WebPermission(IUnrestrictedPermission, CodeAccessPermission): # skipped bases: <type 'IPermission'>, <type 'ISecurityEncodable'>, <type 'IStackWalk'>, <type 'object'>
    """
    WebPermission(state: PermissionState)
    WebPermission()
    WebPermission(access: NetworkAccess, uriRegex: Regex)
    WebPermission(access: NetworkAccess, uriString: str)
    """
    @property
    def AcceptList(self) -> IEnumerator:
        """ Get: AcceptList(self: WebPermission) -> IEnumerator """
        ...

    @property
    def ConnectList(self) -> IEnumerator:
        """ Get: ConnectList(self: WebPermission) -> IEnumerator """
        ...


    def AddPermission(self, access:NetworkAccess, *__args:str): # -> 
        """ AddPermission(self: WebPermission, access: NetworkAccess, uriString: str)AddPermission(self: WebPermission, access: NetworkAccess, uriRegex: Regex) """
        ...

    def __new__(cls, *__args:PermissionState) -> Self:
        """
        __new__(cls: type, state: PermissionState)
        __new__(cls: type)
        __new__(cls: type, access: NetworkAccess, uriRegex: Regex)
        __new__(cls: type, access: NetworkAccess, uriString: str)
        """
        ...


class WebPermissionAttribute(CodeAccessSecurityAttribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ WebPermissionAttribute(action: SecurityAction) """
    @property
    def Accept(self) -> str:
        """
        Get: Accept(self: WebPermissionAttribute) -> str
        Set: Accept(self: WebPermissionAttribute) = value
        """
        ...

    @property
    def AcceptPattern(self) -> str:
        """
        Get: AcceptPattern(self: WebPermissionAttribute) -> str
        Set: AcceptPattern(self: WebPermissionAttribute) = value
        """
        ...

    @property
    def Connect(self) -> str:
        """
        Get: Connect(self: WebPermissionAttribute) -> str
        Set: Connect(self: WebPermissionAttribute) = value
        """
        ...

    @property
    def ConnectPattern(self) -> str:
        """
        Get: ConnectPattern(self: WebPermissionAttribute) -> str
        Set: ConnectPattern(self: WebPermissionAttribute) = value
        """
        ...


    def CreatePermission(self) -> IPermission:
        """ CreatePermission(self: WebPermissionAttribute) -> IPermission """
        ...


class WebProxy(IAutoWebProxy, ISerializable): # skipped bases: <type 'IWebProxy'>, <type 'object'>
    """
    WebProxy()
    WebProxy(Address: Uri)
    WebProxy(Address: Uri, BypassOnLocal: bool)
    WebProxy(Address: Uri, BypassOnLocal: bool, BypassList: Array[str])
    WebProxy(Address: Uri, BypassOnLocal: bool, BypassList: Array[str], Credentials: ICredentials)
    WebProxy(Host: str, Port: int)
    WebProxy(Address: str)
    WebProxy(Address: str, BypassOnLocal: bool)
    WebProxy(Address: str, BypassOnLocal: bool, BypassList: Array[str])
    WebProxy(Address: str, BypassOnLocal: bool, BypassList: Array[str], Credentials: ICredentials)
    """
    @property
    def Address(self) -> Uri:
        """
        Get: Address(self: WebProxy) -> Uri
        Set: Address(self: WebProxy) = value
        """
        ...

    @property
    def BypassArrayList(self) -> ArrayList:
        """ Get: BypassArrayList(self: WebProxy) -> ArrayList """
        ...

    @property
    def BypassList(self) -> Array:
        """
        Get: BypassList(self: WebProxy) -> Array[str]
        Set: BypassList(self: WebProxy) = value
        """
        ...

    @property
    def BypassProxyOnLocal(self) -> bool:
        """
        Get: BypassProxyOnLocal(self: WebProxy) -> bool
        Set: BypassProxyOnLocal(self: WebProxy) = value
        """
        ...

    @property
    def Credentials(self) -> ICredentials:
        """
        Get: Credentials(self: WebProxy) -> ICredentials
        Set: Credentials(self: WebProxy) = value
        """
        ...

    @property
    def UseDefaultCredentials(self) -> bool:
        """
        Get: UseDefaultCredentials(self: WebProxy) -> bool
        Set: UseDefaultCredentials(self: WebProxy) = value
        """
        ...


    @staticmethod
    def GetDefaultProxy() -> WebProxy:
        """ GetDefaultProxy() -> WebProxy """
        ...

    def GetProxy(self, destination:Uri) -> Uri:
        """ GetProxy(self: WebProxy, destination: Uri) -> Uri """
        ...

    def IsBypassed(self, host:Uri) -> bool:
        """ IsBypassed(self: WebProxy, host: Uri) -> bool """
        ...


class WebRequestMethods: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def File(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Ftp(self, *args): #cannot find CLR method
        """ no doc """
        ...

    def Http(self, *args): #cannot find CLR method
        """ no doc """
        ...

    __all__: list = ...


class WebUtility: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def HtmlDecode(value:str, output:TextWriter = ...): # -> 
        """
        HtmlDecode(value: str) -> str
        HtmlDecode(value: str, output: TextWriter)
        """
        ...

    @staticmethod
    def HtmlEncode(value:str, output:TextWriter = ...): # -> 
        """
        HtmlEncode(value: str) -> str
        HtmlEncode(value: str, output: TextWriter)
        """
        ...

    @staticmethod
    def UrlDecode(encodedValue:str) -> str:
        """ UrlDecode(encodedValue: str) -> str """
        ...

    @staticmethod
    def UrlDecodeToBytes(encodedValue:Array, offset:int, count:int) -> Array:
        """ UrlDecodeToBytes(encodedValue: Array[Byte], offset: int, count: int) -> Array[Byte] """
        ...

    @staticmethod
    def UrlEncode(value:str) -> str:
        """ UrlEncode(value: str) -> str """
        ...

    @staticmethod
    def UrlEncodeToBytes(value:Array, offset:int, count:int) -> Array:
        """ UrlEncodeToBytes(value: Array[Byte], offset: int, count: int) -> Array[Byte] """
        ...

    __all__: list = ...


class WriteStreamClosedEventArgs(EventArgs): # skipped bases: <type 'object'>
    """ WriteStreamClosedEventArgs() """
    @property
    def Error(self) -> Exception:
        """ Get: Error(self: WriteStreamClosedEventArgs) -> Exception """
        ...



class WriteStreamClosedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ WriteStreamClosedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:WriteStreamClosedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: WriteStreamClosedEventHandler, sender: object, e: WriteStreamClosedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: WriteStreamClosedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:WriteStreamClosedEventArgs): # -> 
        """ Invoke(self: WriteStreamClosedEventHandler, sender: object, e: WriteStreamClosedEventArgs) """
        ...


# variables with complex values

