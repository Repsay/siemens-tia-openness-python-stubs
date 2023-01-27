# encoding: utf-8
# module System.Web.Services.Protocols calls itself Protocols
# from System.Web.Services, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Array, AsyncCallback, Attribute, Enum, IAsyncResult, 
    MulticastDelegate, SystemException, Type)

from System.Collections import ArrayList, CollectionBase

from System.ComponentModel import AsyncCompletedEventArgs, Component

from System.IO import Stream

from System.Net import (CookieContainer, ICredentials, IWebProxy, WebRequest, 
    WebResponse)

from System.Reflection import (ICustomAttributeProvider, MemberInfo, 
    MethodInfo, ParameterInfo)

from System.Security.Cryptography.X509Certificates import (
    X509CertificateCollection)

from System.Text import Encoding

from System.Web import HttpRequest, IHttpHandlerFactory

from System.Web.Services import WsiProfiles

from System.Web.Services.Description import SoapBindingUse

from System.Xml import (XmlElement, XmlNode, XmlQualifiedName, XmlReader, 
    XmlWriter)

from System.Xml.Serialization import XmlSerializer

from typing import Self

"""The following names are not found in the module: BoundEvent, field#
"""

# no functions
# classes

class MimeFormatter: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @staticmethod
    def CreateInstance(type:Type, initializer:object) -> MimeFormatter:
        """ CreateInstance(type: Type, initializer: object) -> MimeFormatter """
        ...

    @staticmethod
    def GetInitializer(*__args) -> object:
        """
        GetInitializer(type: Type, methodInfo: LogicalMethodInfo) -> object
        GetInitializer(self: MimeFormatter, methodInfo: LogicalMethodInfo) -> object
        """
        ...

    @staticmethod
    def GetInitializers(*__args) -> Array:
        """
        GetInitializers(type: Type, methodInfos: Array[LogicalMethodInfo]) -> Array[object]
        GetInitializers(self: MimeFormatter, methodInfos: Array[LogicalMethodInfo]) -> Array[object]
        """
        ...

    def Initialize(self, initializer:object): # -> 
        """ Initialize(self: MimeFormatter, initializer: object) """
        ...


class MimeReturnReader(MimeFormatter): # skipped bases: <type 'object'>
    """ no doc """
    def Read(self, response:WebResponse, responseStream:Stream) -> object:
        """ Read(self: MimeReturnReader, response: WebResponse, responseStream: Stream) -> object """
        ...


class AnyReturnReader(MimeReturnReader): # skipped bases: <type 'object'>
    """ AnyReturnReader() """
    def GetInitializer(self, methodInfo:LogicalMethodInfo) -> object:
        """ GetInitializer(self: AnyReturnReader, methodInfo: LogicalMethodInfo) -> object """
        ...

    def Initialize(self, o:object): # -> 
        """ Initialize(self: AnyReturnReader, o: object) """
        ...


class MimeParameterReader(MimeFormatter): # skipped bases: <type 'object'>
    """ no doc """
    def Read(self, request:HttpRequest) -> Array:
        """ Read(self: MimeParameterReader, request: HttpRequest) -> Array[object] """
        ...


class ValueCollectionParameterReader(MimeParameterReader): # skipped bases: <type 'object'>
    """ no doc """
    def GetInitializer(self, methodInfo:LogicalMethodInfo) -> object:
        """ GetInitializer(self: ValueCollectionParameterReader, methodInfo: LogicalMethodInfo) -> object """
        ...

    def Initialize(self, o:object): # -> 
        """ Initialize(self: ValueCollectionParameterReader, o: object) """
        ...

    @staticmethod
    def IsSupported(*__args:LogicalMethodInfo) -> bool:
        """
        IsSupported(methodInfo: LogicalMethodInfo) -> bool
        IsSupported(paramInfo: ParameterInfo) -> bool
        """
        ...


class HtmlFormParameterReader(ValueCollectionParameterReader): # skipped bases: <type 'object'>
    """ HtmlFormParameterReader() """
    pass

class MimeParameterWriter(MimeFormatter): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def RequestEncoding(self) -> Encoding:
        """
        Get: RequestEncoding(self: MimeParameterWriter) -> Encoding
        Set: RequestEncoding(self: MimeParameterWriter) = value
        """
        ...

    @property
    def UsesWriteRequest(self) -> bool:
        """ Get: UsesWriteRequest(self: MimeParameterWriter) -> bool """
        ...


    def GetRequestUrl(self, url:str, parameters:Array) -> str:
        """ GetRequestUrl(self: MimeParameterWriter, url: str, parameters: Array[object]) -> str """
        ...

    def InitializeRequest(self, request:WebRequest, values:Array): # -> 
        """ InitializeRequest(self: MimeParameterWriter, request: WebRequest, values: Array[object]) """
        ...

    def WriteRequest(self, requestStream:Stream, values:Array): # -> 
        """ WriteRequest(self: MimeParameterWriter, requestStream: Stream, values: Array[object]) """
        ...


class UrlEncodedParameterWriter(MimeParameterWriter): # skipped bases: <type 'object'>
    """ no doc """
    def Encode(self, *args): #cannot find CLR method
        """ Encode(self: UrlEncodedParameterWriter, writer: TextWriter, values: Array[object])Encode(self: UrlEncodedParameterWriter, writer: TextWriter, name: str, value: object) """
        ...

    def GetInitializer(self, methodInfo:LogicalMethodInfo) -> object:
        """ GetInitializer(self: UrlEncodedParameterWriter, methodInfo: LogicalMethodInfo) -> object """
        ...

    def Initialize(self, initializer:object): # -> 
        """ Initialize(self: UrlEncodedParameterWriter, initializer: object) """
        ...


class HtmlFormParameterWriter(UrlEncodedParameterWriter): # skipped bases: <type 'object'>
    """ HtmlFormParameterWriter() """
    @property
    def UsesWriteRequest(self) -> bool:
        """ Get: UsesWriteRequest(self: HtmlFormParameterWriter) -> bool """
        ...


    def InitializeRequest(self, request:WebRequest, values:Array): # -> 
        """ InitializeRequest(self: HtmlFormParameterWriter, request: WebRequest, values: Array[object]) """
        ...

    def WriteRequest(self, requestStream:Stream, values:Array): # -> 
        """ WriteRequest(self: HtmlFormParameterWriter, requestStream: Stream, values: Array[object]) """
        ...


class WebClientProtocol(Component): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def ConnectionGroupName(self) -> str:
        """
        Get: ConnectionGroupName(self: WebClientProtocol) -> str
        Set: ConnectionGroupName(self: WebClientProtocol) = value
        """
        ...

    @property
    def Credentials(self) -> ICredentials:
        """
        Get: Credentials(self: WebClientProtocol) -> ICredentials
        Set: Credentials(self: WebClientProtocol) = value
        """
        ...

    @property
    def PreAuthenticate(self) -> bool:
        """
        Get: PreAuthenticate(self: WebClientProtocol) -> bool
        Set: PreAuthenticate(self: WebClientProtocol) = value
        """
        ...

    @property
    def RequestEncoding(self) -> Encoding:
        """
        Get: RequestEncoding(self: WebClientProtocol) -> Encoding
        Set: RequestEncoding(self: WebClientProtocol) = value
        """
        ...

    @property
    def Timeout(self) -> int:
        """
        Get: Timeout(self: WebClientProtocol) -> int
        Set: Timeout(self: WebClientProtocol) = value
        """
        ...

    @property
    def Url(self) -> str:
        """
        Get: Url(self: WebClientProtocol) -> str
        Set: Url(self: WebClientProtocol) = value
        """
        ...

    @property
    def UseDefaultCredentials(self) -> bool:
        """
        Get: UseDefaultCredentials(self: WebClientProtocol) -> bool
        Set: UseDefaultCredentials(self: WebClientProtocol) = value
        """
        ...


    def Abort(self): # -> 
        """ Abort(self: WebClientProtocol) """
        ...

    def AddToCache(self, *args): #cannot find CLR method
        """ AddToCache(type: Type, value: object) """
        ...

    def GetFromCache(self, *args): #cannot find CLR method
        """ GetFromCache(type: Type) -> object """
        ...

    def GetWebRequest(self, *args): #cannot find CLR method
        """ GetWebRequest(self: WebClientProtocol, uri: Uri) -> WebRequest """
        ...

    def GetWebResponse(self, *args): #cannot find CLR method
        """
        GetWebResponse(self: WebClientProtocol, request: WebRequest, result: IAsyncResult) -> WebResponse
        GetWebResponse(self: WebClientProtocol, request: WebRequest) -> WebResponse
        """
        ...


class HttpWebClientProtocol(WebClientProtocol): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    @property
    def AllowAutoRedirect(self) -> bool:
        """
        Get: AllowAutoRedirect(self: HttpWebClientProtocol) -> bool
        Set: AllowAutoRedirect(self: HttpWebClientProtocol) = value
        """
        ...

    @property
    def ClientCertificates(self) -> X509CertificateCollection:
        """ Get: ClientCertificates(self: HttpWebClientProtocol) -> X509CertificateCollection """
        ...

    @property
    def CookieContainer(self) -> CookieContainer:
        """
        Get: CookieContainer(self: HttpWebClientProtocol) -> CookieContainer
        Set: CookieContainer(self: HttpWebClientProtocol) = value
        """
        ...

    @property
    def EnableDecompression(self) -> bool:
        """
        Get: EnableDecompression(self: HttpWebClientProtocol) -> bool
        Set: EnableDecompression(self: HttpWebClientProtocol) = value
        """
        ...

    @property
    def Proxy(self) -> IWebProxy:
        """
        Get: Proxy(self: HttpWebClientProtocol) -> IWebProxy
        Set: Proxy(self: HttpWebClientProtocol) = value
        """
        ...

    @property
    def UnsafeAuthenticatedConnectionSharing(self) -> bool:
        """
        Get: UnsafeAuthenticatedConnectionSharing(self: HttpWebClientProtocol) -> bool
        Set: UnsafeAuthenticatedConnectionSharing(self: HttpWebClientProtocol) = value
        """
        ...

    @property
    def UserAgent(self) -> str:
        """
        Get: UserAgent(self: HttpWebClientProtocol) -> str
        Set: UserAgent(self: HttpWebClientProtocol) = value
        """
        ...


    def CancelAsync(self, *args): #cannot find CLR method
        """ CancelAsync(self: HttpWebClientProtocol, userState: object) """
        ...

    @staticmethod
    def GenerateXmlMappings(*__args) -> bool:
        """
        GenerateXmlMappings(type: Type, mappings: ArrayList) -> bool
        GenerateXmlMappings(types: Array[Type], mappings: ArrayList) -> Hashtable
        """
        ...


class HttpSimpleClientProtocol(HttpWebClientProtocol): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ no doc """
    def BeginInvoke(self, *args): #cannot find CLR method
        """ BeginInvoke(self: HttpSimpleClientProtocol, methodName: str, requestUrl: str, parameters: Array[object], callback: AsyncCallback, asyncState: object) -> IAsyncResult """
        ...

    def EndInvoke(self, *args): #cannot find CLR method
        """ EndInvoke(self: HttpSimpleClientProtocol, asyncResult: IAsyncResult) -> object """
        ...

    def Invoke(self, *args): #cannot find CLR method
        """ Invoke(self: HttpSimpleClientProtocol, methodName: str, requestUrl: str, parameters: Array[object]) -> object """
        ...

    def InvokeAsync(self, *args): #cannot find CLR method
        """ InvokeAsync(self: HttpSimpleClientProtocol, methodName: str, requestUrl: str, parameters: Array[object], callback: SendOrPostCallback)InvokeAsync(self: HttpSimpleClientProtocol, methodName: str, requestUrl: str, parameters: Array[object], callback: SendOrPostCallback, userState: object) """
        ...


class HttpGetClientProtocol(HttpSimpleClientProtocol): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ HttpGetClientProtocol() """
    pass

class HttpMethodAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    HttpMethodAttribute()
    HttpMethodAttribute(returnFormatter: Type, parameterFormatter: Type)
    """
    @property
    def ParameterFormatter(self) -> Type:
        """
        Get: ParameterFormatter(self: HttpMethodAttribute) -> Type
        Set: ParameterFormatter(self: HttpMethodAttribute) = value
        """
        ...

    @property
    def ReturnFormatter(self) -> Type:
        """
        Get: ReturnFormatter(self: HttpMethodAttribute) -> Type
        Set: ReturnFormatter(self: HttpMethodAttribute) = value
        """
        ...


    def __new__(cls, returnFormatter:Type = ..., parameterFormatter:Type = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, returnFormatter: Type, parameterFormatter: Type)
        """
        ...


class HttpPostClientProtocol(HttpSimpleClientProtocol): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ HttpPostClientProtocol() """
    pass

class InvokeCompletedEventArgs(AsyncCompletedEventArgs): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Results(self) -> Array:
        """ Get: Results(self: InvokeCompletedEventArgs) -> Array[object] """
        ...



class InvokeCompletedEventHandler(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ InvokeCompletedEventHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender:object, e:InvokeCompletedEventArgs, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: InvokeCompletedEventHandler, sender: object, e: InvokeCompletedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # -> 
        """ EndInvoke(self: InvokeCompletedEventHandler, result: IAsyncResult) """
        ...

    def Invoke(self, sender:object, e:InvokeCompletedEventArgs): # -> 
        """ Invoke(self: InvokeCompletedEventHandler, sender: object, e: InvokeCompletedEventArgs) """
        ...


class LogicalMethodInfo: # skipped bases: <type 'object'>, <type 'object'>
    """ LogicalMethodInfo(methodInfo: MethodInfo) """
    @property
    def AsyncCallbackParameter(self) -> ParameterInfo:
        """ Get: AsyncCallbackParameter(self: LogicalMethodInfo) -> ParameterInfo """
        ...

    @property
    def AsyncResultParameter(self) -> ParameterInfo:
        """ Get: AsyncResultParameter(self: LogicalMethodInfo) -> ParameterInfo """
        ...

    @property
    def AsyncStateParameter(self) -> ParameterInfo:
        """ Get: AsyncStateParameter(self: LogicalMethodInfo) -> ParameterInfo """
        ...

    @property
    def BeginMethodInfo(self) -> MethodInfo:
        """ Get: BeginMethodInfo(self: LogicalMethodInfo) -> MethodInfo """
        ...

    @property
    def CustomAttributeProvider(self) -> ICustomAttributeProvider:
        """ Get: CustomAttributeProvider(self: LogicalMethodInfo) -> ICustomAttributeProvider """
        ...

    @property
    def DeclaringType(self) -> Type:
        """ Get: DeclaringType(self: LogicalMethodInfo) -> Type """
        ...

    @property
    def EndMethodInfo(self) -> MethodInfo:
        """ Get: EndMethodInfo(self: LogicalMethodInfo) -> MethodInfo """
        ...

    @property
    def InParameters(self) -> Array:
        """ Get: InParameters(self: LogicalMethodInfo) -> Array[ParameterInfo] """
        ...

    @property
    def IsAsync(self) -> bool:
        """ Get: IsAsync(self: LogicalMethodInfo) -> bool """
        ...

    @property
    def IsVoid(self) -> bool:
        """ Get: IsVoid(self: LogicalMethodInfo) -> bool """
        ...

    @property
    def MethodInfo(self) -> MethodInfo:
        """ Get: MethodInfo(self: LogicalMethodInfo) -> MethodInfo """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: LogicalMethodInfo) -> str """
        ...

    @property
    def OutParameters(self) -> Array:
        """ Get: OutParameters(self: LogicalMethodInfo) -> Array[ParameterInfo] """
        ...

    @property
    def Parameters(self) -> Array:
        """ Get: Parameters(self: LogicalMethodInfo) -> Array[ParameterInfo] """
        ...

    @property
    def ReturnType(self) -> Type:
        """ Get: ReturnType(self: LogicalMethodInfo) -> Type """
        ...

    @property
    def ReturnTypeCustomAttributeProvider(self) -> ICustomAttributeProvider:
        """ Get: ReturnTypeCustomAttributeProvider(self: LogicalMethodInfo) -> ICustomAttributeProvider """
        ...


    def BeginInvoke(self, target:object, values:Array, callback:AsyncCallback, asyncState:object) -> IAsyncResult:
        """ BeginInvoke(self: LogicalMethodInfo, target: object, values: Array[object], callback: AsyncCallback, asyncState: object) -> IAsyncResult """
        ...

    @staticmethod
    def Create(methodInfos:Array, types:LogicalMethodTypes = ...) -> Array:
        """
        Create(methodInfos: Array[MethodInfo]) -> Array[LogicalMethodInfo]
        Create(methodInfos: Array[MethodInfo], types: LogicalMethodTypes) -> Array[LogicalMethodInfo]
        """
        ...

    def EndInvoke(self, target:object, asyncResult:IAsyncResult) -> Array:
        """ EndInvoke(self: LogicalMethodInfo, target: object, asyncResult: IAsyncResult) -> Array[object] """
        ...

    def GetCustomAttribute(self, type:Type) -> object:
        """ GetCustomAttribute(self: LogicalMethodInfo, type: Type) -> object """
        ...

    def GetCustomAttributes(self, type:Type) -> Array:
        """ GetCustomAttributes(self: LogicalMethodInfo, type: Type) -> Array[object] """
        ...

    def Invoke(self, target:object, values:Array) -> Array:
        """ Invoke(self: LogicalMethodInfo, target: object, values: Array[object]) -> Array[object] """
        ...

    @staticmethod
    def IsBeginMethod(methodInfo:MethodInfo) -> bool:
        """ IsBeginMethod(methodInfo: MethodInfo) -> bool """
        ...

    @staticmethod
    def IsEndMethod(methodInfo:MethodInfo) -> bool:
        """ IsEndMethod(methodInfo: MethodInfo) -> bool """
        ...

    def ToString(self) -> str:
        """ ToString(self: LogicalMethodInfo) -> str """
        ...


class LogicalMethodTypes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum LogicalMethodTypes, values: Async (2), Sync (1) """
    Async: LogicalMethodTypes = ...
    Sync: LogicalMethodTypes = ...
    value__ = ...


class MatchAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ MatchAttribute(pattern: str) """
    @property
    def Capture(self) -> int:
        """
        Get: Capture(self: MatchAttribute) -> int
        Set: Capture(self: MatchAttribute) = value
        """
        ...

    @property
    def Group(self) -> int:
        """
        Get: Group(self: MatchAttribute) -> int
        Set: Group(self: MatchAttribute) = value
        """
        ...

    @property
    def IgnoreCase(self) -> bool:
        """
        Get: IgnoreCase(self: MatchAttribute) -> bool
        Set: IgnoreCase(self: MatchAttribute) = value
        """
        ...

    @property
    def MaxRepeats(self) -> int:
        """
        Get: MaxRepeats(self: MatchAttribute) -> int
        Set: MaxRepeats(self: MatchAttribute) = value
        """
        ...

    @property
    def Pattern(self) -> str:
        """
        Get: Pattern(self: MatchAttribute) -> str
        Set: Pattern(self: MatchAttribute) = value
        """
        ...


    def __new__(cls, pattern:str) -> Self:
        """ __new__(cls: type, pattern: str) """
        ...


class NopReturnReader(MimeReturnReader): # skipped bases: <type 'object'>
    """ NopReturnReader() """
    def GetInitializer(self, methodInfo:LogicalMethodInfo) -> object:
        """ GetInitializer(self: NopReturnReader, methodInfo: LogicalMethodInfo) -> object """
        ...

    def Initialize(self, initializer:object): # -> 
        """ Initialize(self: NopReturnReader, initializer: object) """
        ...


class PatternMatcher: # skipped bases: <type 'object'>, <type 'object'>
    """ PatternMatcher(type: Type) """
    def Match(self, text:str) -> object:
        """ Match(self: PatternMatcher, text: str) -> object """
        ...


class ServerProtocol: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Context(self):
        ...

    @property
    def Request(self):
        ...

    @property
    def Response(self):
        ...

    @property
    def Target(self):
        ...


    def AddToCache(self, *args): #cannot find CLR method
        """ AddToCache(self: ServerProtocol, protocolType: Type, serverType: Type, value: object) """
        ...

    def GetFromCache(self, *args): #cannot find CLR method
        """ GetFromCache(self: ServerProtocol, protocolType: Type, serverType: Type) -> object """
        ...


class ServerProtocolFactory: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def CreateIfRequestCompatible(self, *args): #cannot find CLR method
        """ CreateIfRequestCompatible(self: ServerProtocolFactory, request: HttpRequest) -> ServerProtocol """
        ...


class ServerType: # skipped bases: <type 'object'>, <type 'object'>
    """ ServerType(type: Type) """
    pass

class Soap12FaultCodes: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    DataEncodingUnknownFaultCode: XmlQualifiedName = ...
    EncodingMissingIdFaultCode: XmlQualifiedName = ...
    EncodingUntypedValueFaultCode: XmlQualifiedName = ...
    MustUnderstandFaultCode: XmlQualifiedName = ...
    ReceiverFaultCode: XmlQualifiedName = ...
    RpcBadArgumentsFaultCode: XmlQualifiedName = ...
    RpcProcedureNotPresentFaultCode: XmlQualifiedName = ...
    SenderFaultCode: XmlQualifiedName = ...
    VersionMismatchFaultCode: XmlQualifiedName = ...


class SoapMessage: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Action(self) -> str:
        """ Get: Action(self: SoapMessage) -> str """
        ...

    @property
    def ContentEncoding(self) -> str:
        """
        Get: ContentEncoding(self: SoapMessage) -> str
        Set: ContentEncoding(self: SoapMessage) = value
        """
        ...

    @property
    def ContentType(self) -> str:
        """
        Get: ContentType(self: SoapMessage) -> str
        Set: ContentType(self: SoapMessage) = value
        """
        ...

    @property
    def Exception(self) -> SoapException:
        """
        Get: Exception(self: SoapMessage) -> SoapException
        Set: Exception(self: SoapMessage) = value
        """
        ...

    @property
    def Headers(self) -> SoapHeaderCollection:
        """ Get: Headers(self: SoapMessage) -> SoapHeaderCollection """
        ...

    @property
    def MethodInfo(self) -> LogicalMethodInfo:
        """ Get: MethodInfo(self: SoapMessage) -> LogicalMethodInfo """
        ...

    @property
    def OneWay(self) -> bool:
        """ Get: OneWay(self: SoapMessage) -> bool """
        ...

    @property
    def SoapVersion(self) -> SoapProtocolVersion:
        """ Get: SoapVersion(self: SoapMessage) -> SoapProtocolVersion """
        ...

    @property
    def Stage(self) -> SoapMessageStage:
        """ Get: Stage(self: SoapMessage) -> SoapMessageStage """
        ...

    @property
    def Stream(self) -> Stream:
        """ Get: Stream(self: SoapMessage) -> Stream """
        ...

    @property
    def Url(self) -> str:
        """ Get: Url(self: SoapMessage) -> str """
        ...


    def EnsureInStage(self, *args): #cannot find CLR method
        """ EnsureInStage(self: SoapMessage) """
        ...

    def EnsureOutStage(self, *args): #cannot find CLR method
        """ EnsureOutStage(self: SoapMessage) """
        ...

    def EnsureStage(self, *args): #cannot find CLR method
        """ EnsureStage(self: SoapMessage, stage: SoapMessageStage) """
        ...

    def GetInParameterValue(self, index:int) -> object:
        """ GetInParameterValue(self: SoapMessage, index: int) -> object """
        ...

    def GetOutParameterValue(self, index:int) -> object:
        """ GetOutParameterValue(self: SoapMessage, index: int) -> object """
        ...

    def GetReturnValue(self) -> object:
        """ GetReturnValue(self: SoapMessage) -> object """
        ...


class SoapClientMessage(SoapMessage): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Client(self) -> SoapHttpClientProtocol:
        """ Get: Client(self: SoapClientMessage) -> SoapHttpClientProtocol """
        ...



class SoapDocumentMethodAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SoapDocumentMethodAttribute()
    SoapDocumentMethodAttribute(action: str)
    """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: SoapDocumentMethodAttribute) -> str
        Set: Action(self: SoapDocumentMethodAttribute) = value
        """
        ...

    @property
    def Binding(self) -> str:
        """
        Get: Binding(self: SoapDocumentMethodAttribute) -> str
        Set: Binding(self: SoapDocumentMethodAttribute) = value
        """
        ...

    @property
    def OneWay(self) -> bool:
        """
        Get: OneWay(self: SoapDocumentMethodAttribute) -> bool
        Set: OneWay(self: SoapDocumentMethodAttribute) = value
        """
        ...

    @property
    def ParameterStyle(self) -> SoapParameterStyle:
        """
        Get: ParameterStyle(self: SoapDocumentMethodAttribute) -> SoapParameterStyle
        Set: ParameterStyle(self: SoapDocumentMethodAttribute) = value
        """
        ...

    @property
    def RequestElementName(self) -> str:
        """
        Get: RequestElementName(self: SoapDocumentMethodAttribute) -> str
        Set: RequestElementName(self: SoapDocumentMethodAttribute) = value
        """
        ...

    @property
    def RequestNamespace(self) -> str:
        """
        Get: RequestNamespace(self: SoapDocumentMethodAttribute) -> str
        Set: RequestNamespace(self: SoapDocumentMethodAttribute) = value
        """
        ...

    @property
    def ResponseElementName(self) -> str:
        """
        Get: ResponseElementName(self: SoapDocumentMethodAttribute) -> str
        Set: ResponseElementName(self: SoapDocumentMethodAttribute) = value
        """
        ...

    @property
    def ResponseNamespace(self) -> str:
        """
        Get: ResponseNamespace(self: SoapDocumentMethodAttribute) -> str
        Set: ResponseNamespace(self: SoapDocumentMethodAttribute) = value
        """
        ...

    @property
    def Use(self) -> SoapBindingUse:
        """
        Get: Use(self: SoapDocumentMethodAttribute) -> SoapBindingUse
        Set: Use(self: SoapDocumentMethodAttribute) = value
        """
        ...


    def __new__(cls, action:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, action: str)
        """
        ...


class SoapDocumentServiceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SoapDocumentServiceAttribute()
    SoapDocumentServiceAttribute(use: SoapBindingUse)
    SoapDocumentServiceAttribute(use: SoapBindingUse, paramStyle: SoapParameterStyle)
    """
    @property
    def ParameterStyle(self) -> SoapParameterStyle:
        """
        Get: ParameterStyle(self: SoapDocumentServiceAttribute) -> SoapParameterStyle
        Set: ParameterStyle(self: SoapDocumentServiceAttribute) = value
        """
        ...

    @property
    def RoutingStyle(self) -> SoapServiceRoutingStyle:
        """
        Get: RoutingStyle(self: SoapDocumentServiceAttribute) -> SoapServiceRoutingStyle
        Set: RoutingStyle(self: SoapDocumentServiceAttribute) = value
        """
        ...

    @property
    def Use(self) -> SoapBindingUse:
        """
        Get: Use(self: SoapDocumentServiceAttribute) -> SoapBindingUse
        Set: Use(self: SoapDocumentServiceAttribute) = value
        """
        ...


    def __new__(cls, use:SoapBindingUse = ..., paramStyle:SoapParameterStyle = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, use: SoapBindingUse)
        __new__(cls: type, use: SoapBindingUse, paramStyle: SoapParameterStyle)
        """
        ...


class SoapException(SystemException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SoapException()
    SoapException(message: str, code: XmlQualifiedName, actor: str)
    SoapException(message: str, code: XmlQualifiedName, actor: str, innerException: Exception)
    SoapException(message: str, code: XmlQualifiedName)
    SoapException(message: str, code: XmlQualifiedName, innerException: Exception)
    SoapException(message: str, code: XmlQualifiedName, actor: str, detail: XmlNode)
    SoapException(message: str, code: XmlQualifiedName, actor: str, detail: XmlNode, innerException: Exception)
    SoapException(message: str, code: XmlQualifiedName, subCode: SoapFaultSubCode)
    SoapException(message: str, code: XmlQualifiedName, actor: str, role: str, detail: XmlNode, subCode: SoapFaultSubCode, innerException: Exception)
    SoapException(message: str, code: XmlQualifiedName, actor: str, role: str, lang: str, detail: XmlNode, subCode: SoapFaultSubCode, innerException: Exception)
    """
    @property
    def Actor(self) -> str:
        """ Get: Actor(self: SoapException) -> str """
        ...

    @property
    def Code(self) -> XmlQualifiedName:
        """ Get: Code(self: SoapException) -> XmlQualifiedName """
        ...

    @property
    def Detail(self) -> XmlNode:
        """ Get: Detail(self: SoapException) -> XmlNode """
        ...

    @property
    def Lang(self) -> str:
        """ Get: Lang(self: SoapException) -> str """
        ...

    @property
    def Node(self) -> str:
        """ Get: Node(self: SoapException) -> str """
        ...

    @property
    def Role(self) -> str:
        """ Get: Role(self: SoapException) -> str """
        ...

    @property
    def SubCode(self) -> SoapFaultSubCode:
        """ Get: SubCode(self: SoapException) -> SoapFaultSubCode """
        ...


    @staticmethod
    def IsClientFaultCode(code:XmlQualifiedName) -> bool:
        """ IsClientFaultCode(code: XmlQualifiedName) -> bool """
        ...

    @staticmethod
    def IsMustUnderstandFaultCode(code:XmlQualifiedName) -> bool:
        """ IsMustUnderstandFaultCode(code: XmlQualifiedName) -> bool """
        ...

    @staticmethod
    def IsServerFaultCode(code:XmlQualifiedName) -> bool:
        """ IsServerFaultCode(code: XmlQualifiedName) -> bool """
        ...

    @staticmethod
    def IsVersionMismatchFaultCode(code:XmlQualifiedName) -> bool:
        """ IsVersionMismatchFaultCode(code: XmlQualifiedName) -> bool """
        ...

    ClientFaultCode: XmlQualifiedName = ...
    DetailElementName: XmlQualifiedName = ...
    MustUnderstandFaultCode: XmlQualifiedName = ...
    SerializeObjectState = ...
    ServerFaultCode: XmlQualifiedName = ...
    VersionMismatchFaultCode: XmlQualifiedName = ...


class SoapExtension: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    def ChainStream(self, stream:Stream) -> Stream:
        """ ChainStream(self: SoapExtension, stream: Stream) -> Stream """
        ...

    def GetInitializer(self, *__args:Type) -> object:
        """
        GetInitializer(self: SoapExtension, methodInfo: LogicalMethodInfo, attribute: SoapExtensionAttribute) -> object
        GetInitializer(self: SoapExtension, serviceType: Type) -> object
        """
        ...

    def Initialize(self, initializer:object): # -> 
        """ Initialize(self: SoapExtension, initializer: object) """
        ...

    def ProcessMessage(self, message:SoapMessage): # -> 
        """ ProcessMessage(self: SoapExtension, message: SoapMessage) """
        ...


class SoapExtensionAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ no doc """
    @property
    def ExtensionType(self) -> Type:
        """ Get: ExtensionType(self: SoapExtensionAttribute) -> Type """
        ...

    @property
    def Priority(self) -> int:
        """
        Get: Priority(self: SoapExtensionAttribute) -> int
        Set: Priority(self: SoapExtensionAttribute) = value
        """
        ...



class SoapFaultSubCode: # skipped bases: <type 'object'>, <type 'object'>
    """
    SoapFaultSubCode(code: XmlQualifiedName)
    SoapFaultSubCode(code: XmlQualifiedName, subCode: SoapFaultSubCode)
    """
    @property
    def Code(self) -> XmlQualifiedName:
        """ Get: Code(self: SoapFaultSubCode) -> XmlQualifiedName """
        ...

    @property
    def SubCode(self) -> SoapFaultSubCode:
        """ Get: SubCode(self: SoapFaultSubCode) -> SoapFaultSubCode """
        ...



class SoapHeader: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Actor(self) -> str:
        """
        Get: Actor(self: SoapHeader) -> str
        Set: Actor(self: SoapHeader) = value
        """
        ...

    @property
    def DidUnderstand(self) -> bool:
        """
        Get: DidUnderstand(self: SoapHeader) -> bool
        Set: DidUnderstand(self: SoapHeader) = value
        """
        ...

    @property
    def EncodedMustUnderstand(self) -> str:
        """
        Get: EncodedMustUnderstand(self: SoapHeader) -> str
        Set: EncodedMustUnderstand(self: SoapHeader) = value
        """
        ...

    @property
    def EncodedMustUnderstand12(self) -> str:
        """
        Get: EncodedMustUnderstand12(self: SoapHeader) -> str
        Set: EncodedMustUnderstand12(self: SoapHeader) = value
        """
        ...

    @property
    def EncodedRelay(self) -> str:
        """
        Get: EncodedRelay(self: SoapHeader) -> str
        Set: EncodedRelay(self: SoapHeader) = value
        """
        ...

    @property
    def MustUnderstand(self) -> bool:
        """
        Get: MustUnderstand(self: SoapHeader) -> bool
        Set: MustUnderstand(self: SoapHeader) = value
        """
        ...

    @property
    def Relay(self) -> bool:
        """
        Get: Relay(self: SoapHeader) -> bool
        Set: Relay(self: SoapHeader) = value
        """
        ...

    @property
    def Role(self) -> str:
        """
        Get: Role(self: SoapHeader) -> str
        Set: Role(self: SoapHeader) = value
        """
        ...



class SoapHeaderAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SoapHeaderAttribute(memberName: str) """
    @property
    def Direction(self) -> SoapHeaderDirection:
        """
        Get: Direction(self: SoapHeaderAttribute) -> SoapHeaderDirection
        Set: Direction(self: SoapHeaderAttribute) = value
        """
        ...

    @property
    def MemberName(self) -> str:
        """
        Get: MemberName(self: SoapHeaderAttribute) -> str
        Set: MemberName(self: SoapHeaderAttribute) = value
        """
        ...

    @property
    def Required(self) -> bool:
        """
        Get: Required(self: SoapHeaderAttribute) -> bool
        Set: Required(self: SoapHeaderAttribute) = value
        """
        ...


    def __new__(cls, memberName:str) -> Self:
        """ __new__(cls: type, memberName: str) """
        ...


class SoapHeaderCollection(CollectionBase): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'IList'>, <type 'object'>
    """ SoapHeaderCollection() """
    def Add(self, header:SoapHeader) -> int:
        """ Add(self: SoapHeaderCollection, header: SoapHeader) -> int """
        ...

    def Contains(self, header:SoapHeader) -> bool:
        """ Contains(self: SoapHeaderCollection, header: SoapHeader) -> bool """
        ...

    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: SoapHeaderCollection, array: Array[SoapHeader], index: int) """
        ...

    def IndexOf(self, header:SoapHeader) -> int:
        """ IndexOf(self: SoapHeaderCollection, header: SoapHeader) -> int """
        ...

    def Insert(self, index:int, header:SoapHeader): # -> 
        """ Insert(self: SoapHeaderCollection, index: int, header: SoapHeader) """
        ...

    def Remove(self, header:SoapHeader): # -> 
        """ Remove(self: SoapHeaderCollection, header: SoapHeader) """
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


class SoapHeaderDirection(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) SoapHeaderDirection, values: Fault (4), In (1), InOut (3), Out (2) """
    Fault: SoapHeaderDirection = ...
    In: SoapHeaderDirection = ...
    InOut: SoapHeaderDirection = ...
    Out: SoapHeaderDirection = ...
    value__ = ...


class SoapHeaderException(SoapException): # skipped bases: <type '_Exception'>, <type 'ISerializable'>, <type 'object'>
    """
    SoapHeaderException()
    SoapHeaderException(message: str, code: XmlQualifiedName, actor: str)
    SoapHeaderException(message: str, code: XmlQualifiedName, actor: str, innerException: Exception)
    SoapHeaderException(message: str, code: XmlQualifiedName)
    SoapHeaderException(message: str, code: XmlQualifiedName, innerException: Exception)
    SoapHeaderException(message: str, code: XmlQualifiedName, actor: str, role: str, subCode: SoapFaultSubCode, innerException: Exception)
    SoapHeaderException(message: str, code: XmlQualifiedName, actor: str, role: str, lang: str, subCode: SoapFaultSubCode, innerException: Exception)
    """
    SerializeObjectState = ...


class SoapHeaderHandling: # skipped bases: <type 'object'>, <type 'object'>
    """ SoapHeaderHandling() """
    @staticmethod
    def EnsureHeadersUnderstood(headers:SoapHeaderCollection): # -> 
        """ EnsureHeadersUnderstood(headers: SoapHeaderCollection) """
        ...

    @staticmethod
    def GetHeaderMembers(headers:SoapHeaderCollection, target:object, mappings:Array, direction:SoapHeaderDirection, client:bool): # -> 
        """ GetHeaderMembers(headers: SoapHeaderCollection, target: object, mappings: Array[SoapHeaderMapping], direction: SoapHeaderDirection, client: bool) """
        ...

    def ReadHeaders(self, reader:XmlReader, serializer:XmlSerializer, headers:SoapHeaderCollection, mappings:Array, direction:SoapHeaderDirection, envelopeNS:str, encodingStyle:str, checkRequiredHeaders:bool) -> str:
        """ ReadHeaders(self: SoapHeaderHandling, reader: XmlReader, serializer: XmlSerializer, headers: SoapHeaderCollection, mappings: Array[SoapHeaderMapping], direction: SoapHeaderDirection, envelopeNS: str, encodingStyle: str, checkRequiredHeaders: bool) -> str """
        ...

    @staticmethod
    def SetHeaderMembers(headers:SoapHeaderCollection, target:object, mappings:Array, direction:SoapHeaderDirection, client:bool): # -> 
        """ SetHeaderMembers(headers: SoapHeaderCollection, target: object, mappings: Array[SoapHeaderMapping], direction: SoapHeaderDirection, client: bool) """
        ...

    @staticmethod
    def WriteHeaders(writer:XmlWriter, serializer:XmlSerializer, headers:SoapHeaderCollection, mappings:Array, direction:SoapHeaderDirection, isEncoded:bool, defaultNS:str, serviceDefaultIsEncoded:bool, envelopeNS:str): # -> 
        """ WriteHeaders(writer: XmlWriter, serializer: XmlSerializer, headers: SoapHeaderCollection, mappings: Array[SoapHeaderMapping], direction: SoapHeaderDirection, isEncoded: bool, defaultNS: str, serviceDefaultIsEncoded: bool, envelopeNS: str) """
        ...

    @staticmethod
    def WriteUnknownHeaders(writer:XmlWriter, headers:SoapHeaderCollection, envelopeNS:str): # -> 
        """ WriteUnknownHeaders(writer: XmlWriter, headers: SoapHeaderCollection, envelopeNS: str) """
        ...


class SoapHeaderMapping: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Custom(self) -> bool:
        """ Get: Custom(self: SoapHeaderMapping) -> bool """
        ...

    @property
    def Direction(self) -> SoapHeaderDirection:
        """ Get: Direction(self: SoapHeaderMapping) -> SoapHeaderDirection """
        ...

    @property
    def HeaderType(self) -> Type:
        """ Get: HeaderType(self: SoapHeaderMapping) -> Type """
        ...

    @property
    def MemberInfo(self) -> MemberInfo:
        """ Get: MemberInfo(self: SoapHeaderMapping) -> MemberInfo """
        ...

    @property
    def Repeats(self) -> bool:
        """ Get: Repeats(self: SoapHeaderMapping) -> bool """
        ...



class SoapHttpClientProtocol(HttpWebClientProtocol): # skipped bases: <type 'IDisposable'>, <type 'IComponent'>, <type 'object'>
    """ SoapHttpClientProtocol() """
    @property
    def SoapVersion(self) -> SoapProtocolVersion:
        """
        Get: SoapVersion(self: SoapHttpClientProtocol) -> SoapProtocolVersion
        Set: SoapVersion(self: SoapHttpClientProtocol) = value
        """
        ...


    def BeginInvoke(self, *args): #cannot find CLR method
        """ BeginInvoke(self: SoapHttpClientProtocol, methodName: str, parameters: Array[object], callback: AsyncCallback, asyncState: object) -> IAsyncResult """
        ...

    def Discover(self): # -> 
        """ Discover(self: SoapHttpClientProtocol) """
        ...

    def EndInvoke(self, *args): #cannot find CLR method
        """ EndInvoke(self: SoapHttpClientProtocol, asyncResult: IAsyncResult) -> Array[object] """
        ...

    def GetReaderForMessage(self, *args): #cannot find CLR method
        """ GetReaderForMessage(self: SoapHttpClientProtocol, message: SoapClientMessage, bufferSize: int) -> XmlReader """
        ...

    def GetWriterForMessage(self, *args): #cannot find CLR method
        """ GetWriterForMessage(self: SoapHttpClientProtocol, message: SoapClientMessage, bufferSize: int) -> XmlWriter """
        ...

    def Invoke(self, *args): #cannot find CLR method
        """ Invoke(self: SoapHttpClientProtocol, methodName: str, parameters: Array[object]) -> Array[object] """
        ...

    def InvokeAsync(self, *args): #cannot find CLR method
        """ InvokeAsync(self: SoapHttpClientProtocol, methodName: str, parameters: Array[object], callback: SendOrPostCallback)InvokeAsync(self: SoapHttpClientProtocol, methodName: str, parameters: Array[object], callback: SendOrPostCallback, userState: object) """
        ...


class SoapMessageStage(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SoapMessageStage, values: AfterDeserialize (8), AfterSerialize (2), BeforeDeserialize (4), BeforeSerialize (1) """
    AfterDeserialize: SoapMessageStage = ...
    AfterSerialize: SoapMessageStage = ...
    BeforeDeserialize: SoapMessageStage = ...
    BeforeSerialize: SoapMessageStage = ...
    value__ = ...


class SoapParameterStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SoapParameterStyle, values: Bare (1), Default (0), Wrapped (2) """
    Bare: SoapParameterStyle = ...
    Default: SoapParameterStyle = ...
    value__ = ...
    Wrapped: SoapParameterStyle = ...


class SoapProtocolVersion(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SoapProtocolVersion, values: Default (0), Soap11 (1), Soap12 (2) """
    Default: SoapProtocolVersion = ...
    Soap11: SoapProtocolVersion = ...
    Soap12: SoapProtocolVersion = ...
    value__ = ...


class SoapRpcMethodAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """
    SoapRpcMethodAttribute()
    SoapRpcMethodAttribute(action: str)
    """
    @property
    def Action(self) -> str:
        """
        Get: Action(self: SoapRpcMethodAttribute) -> str
        Set: Action(self: SoapRpcMethodAttribute) = value
        """
        ...

    @property
    def Binding(self) -> str:
        """
        Get: Binding(self: SoapRpcMethodAttribute) -> str
        Set: Binding(self: SoapRpcMethodAttribute) = value
        """
        ...

    @property
    def OneWay(self) -> bool:
        """
        Get: OneWay(self: SoapRpcMethodAttribute) -> bool
        Set: OneWay(self: SoapRpcMethodAttribute) = value
        """
        ...

    @property
    def RequestElementName(self) -> str:
        """
        Get: RequestElementName(self: SoapRpcMethodAttribute) -> str
        Set: RequestElementName(self: SoapRpcMethodAttribute) = value
        """
        ...

    @property
    def RequestNamespace(self) -> str:
        """
        Get: RequestNamespace(self: SoapRpcMethodAttribute) -> str
        Set: RequestNamespace(self: SoapRpcMethodAttribute) = value
        """
        ...

    @property
    def ResponseElementName(self) -> str:
        """
        Get: ResponseElementName(self: SoapRpcMethodAttribute) -> str
        Set: ResponseElementName(self: SoapRpcMethodAttribute) = value
        """
        ...

    @property
    def ResponseNamespace(self) -> str:
        """
        Get: ResponseNamespace(self: SoapRpcMethodAttribute) -> str
        Set: ResponseNamespace(self: SoapRpcMethodAttribute) = value
        """
        ...

    @property
    def Use(self) -> SoapBindingUse:
        """
        Get: Use(self: SoapRpcMethodAttribute) -> SoapBindingUse
        Set: Use(self: SoapRpcMethodAttribute) = value
        """
        ...


    def __new__(cls, action:str = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, action: str)
        """
        ...


class SoapRpcServiceAttribute(Attribute): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ SoapRpcServiceAttribute() """
    @property
    def RoutingStyle(self) -> SoapServiceRoutingStyle:
        """
        Get: RoutingStyle(self: SoapRpcServiceAttribute) -> SoapServiceRoutingStyle
        Set: RoutingStyle(self: SoapRpcServiceAttribute) = value
        """
        ...

    @property
    def Use(self) -> SoapBindingUse:
        """
        Get: Use(self: SoapRpcServiceAttribute) -> SoapBindingUse
        Set: Use(self: SoapRpcServiceAttribute) = value
        """
        ...



class SoapServerMessage(SoapMessage): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Server(self) -> object:
        """ Get: Server(self: SoapServerMessage) -> object """
        ...



class SoapServerMethod: # skipped bases: <type 'object'>, <type 'object'>
    """
    SoapServerMethod()
    SoapServerMethod(serverType: Type, methodInfo: LogicalMethodInfo)
    """
    @property
    def Action(self) -> str:
        """ Get: Action(self: SoapServerMethod) -> str """
        ...

    @property
    def BindingUse(self) -> SoapBindingUse:
        """ Get: BindingUse(self: SoapServerMethod) -> SoapBindingUse """
        ...

    @property
    def InHeaderMappings(self) -> Array:
        """ Get: InHeaderMappings(self: SoapServerMethod) -> Array[SoapHeaderMapping] """
        ...

    @property
    def InHeaderSerializer(self) -> XmlSerializer:
        """ Get: InHeaderSerializer(self: SoapServerMethod) -> XmlSerializer """
        ...

    @property
    def MethodInfo(self) -> LogicalMethodInfo:
        """ Get: MethodInfo(self: SoapServerMethod) -> LogicalMethodInfo """
        ...

    @property
    def OneWay(self) -> bool:
        """ Get: OneWay(self: SoapServerMethod) -> bool """
        ...

    @property
    def OutHeaderMappings(self) -> Array:
        """ Get: OutHeaderMappings(self: SoapServerMethod) -> Array[SoapHeaderMapping] """
        ...

    @property
    def OutHeaderSerializer(self) -> XmlSerializer:
        """ Get: OutHeaderSerializer(self: SoapServerMethod) -> XmlSerializer """
        ...

    @property
    def ParameterSerializer(self) -> XmlSerializer:
        """ Get: ParameterSerializer(self: SoapServerMethod) -> XmlSerializer """
        ...

    @property
    def ParameterStyle(self) -> SoapParameterStyle:
        """ Get: ParameterStyle(self: SoapServerMethod) -> SoapParameterStyle """
        ...

    @property
    def ReturnSerializer(self) -> XmlSerializer:
        """ Get: ReturnSerializer(self: SoapServerMethod) -> XmlSerializer """
        ...

    @property
    def Rpc(self) -> bool:
        """ Get: Rpc(self: SoapServerMethod) -> bool """
        ...

    @property
    def WsiClaims(self) -> WsiProfiles:
        """ Get: WsiClaims(self: SoapServerMethod) -> WsiProfiles """
        ...



class SoapServerProtocol(ServerProtocol): # skipped bases: <type 'object'>
    """ no doc """
    def GetReaderForMessage(self, *args): #cannot find CLR method
        """ GetReaderForMessage(self: SoapServerProtocol, message: SoapServerMessage, bufferSize: int) -> XmlReader """
        ...

    def GetWriterForMessage(self, *args): #cannot find CLR method
        """ GetWriterForMessage(self: SoapServerProtocol, message: SoapServerMessage, bufferSize: int) -> XmlWriter """
        ...

    def ModifyInitializedExtensions(self, *args): #cannot find CLR method
        """ ModifyInitializedExtensions(self: SoapServerProtocol, group: PriorityGroup, extensions: Array[SoapExtension]) -> Array[SoapExtension] """
        ...

    def RouteRequest(self, *args): #cannot find CLR method
        """ RouteRequest(self: SoapServerProtocol, message: SoapServerMessage) -> SoapServerMethod """
        ...


class SoapServerProtocolFactory(ServerProtocolFactory): # skipped bases: <type 'object'>
    """ SoapServerProtocolFactory() """
    pass

class SoapServerType(ServerType): # skipped bases: <type 'object'>
    """ SoapServerType(type: Type, protocolsSupported: WebServiceProtocols) """
    @property
    def ServiceDefaultIsEncoded(self) -> bool:
        """ Get: ServiceDefaultIsEncoded(self: SoapServerType) -> bool """
        ...

    @property
    def ServiceNamespace(self) -> str:
        """ Get: ServiceNamespace(self: SoapServerType) -> str """
        ...

    @property
    def ServiceRoutingOnSoapAction(self) -> bool:
        """ Get: ServiceRoutingOnSoapAction(self: SoapServerType) -> bool """
        ...


    def GetDuplicateMethod(self, key:object) -> SoapServerMethod:
        """ GetDuplicateMethod(self: SoapServerType, key: object) -> SoapServerMethod """
        ...

    def GetMethod(self, key:object) -> SoapServerMethod:
        """ GetMethod(self: SoapServerType, key: object) -> SoapServerMethod """
        ...


class SoapServiceRoutingStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SoapServiceRoutingStyle, values: RequestElement (1), SoapAction (0) """
    RequestElement: SoapServiceRoutingStyle = ...
    SoapAction: SoapServiceRoutingStyle = ...
    value__ = ...


class SoapUnknownHeader(SoapHeader): # skipped bases: <type 'object'>
    """ SoapUnknownHeader() """
    @property
    def Element(self) -> XmlElement:
        """
        Get: Element(self: SoapUnknownHeader) -> XmlElement
        Set: Element(self: SoapUnknownHeader) = value
        """
        ...



class TextReturnReader(MimeReturnReader): # skipped bases: <type 'object'>
    """ TextReturnReader() """
    def GetInitializer(self, methodInfo:LogicalMethodInfo) -> object:
        """ GetInitializer(self: TextReturnReader, methodInfo: LogicalMethodInfo) -> object """
        ...

    def Initialize(self, o:object): # -> 
        """ Initialize(self: TextReturnReader, o: object) """
        ...


class UrlParameterReader(ValueCollectionParameterReader): # skipped bases: <type 'object'>
    """ UrlParameterReader() """
    pass

class UrlParameterWriter(UrlEncodedParameterWriter): # skipped bases: <type 'object'>
    """ UrlParameterWriter() """
    def GetRequestUrl(self, url:str, parameters:Array) -> str:
        """ GetRequestUrl(self: UrlParameterWriter, url: str, parameters: Array[object]) -> str """
        ...


class WebClientAsyncResult(IAsyncResult): # skipped bases: <type 'object'>
    """ no doc """
    def Abort(self): # -> 
        """ Abort(self: WebClientAsyncResult) """
        ...


class WebServiceHandlerFactory(IHttpHandlerFactory): # skipped bases: <type 'object'>
    """ WebServiceHandlerFactory() """
    pass

class XmlReturnReader(MimeReturnReader): # skipped bases: <type 'object'>
    """ XmlReturnReader() """
    def GetInitializer(self, methodInfo:LogicalMethodInfo) -> object:
        """ GetInitializer(self: XmlReturnReader, methodInfo: LogicalMethodInfo) -> object """
        ...

    def GetInitializers(self, methodInfos:Array) -> Array:
        """ GetInitializers(self: XmlReturnReader, methodInfos: Array[LogicalMethodInfo]) -> Array[object] """
        ...

    def Initialize(self, o:object): # -> 
        """ Initialize(self: XmlReturnReader, o: object) """
        ...


