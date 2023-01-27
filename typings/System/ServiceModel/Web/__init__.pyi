# encoding: utf-8
# module System.ServiceModel.Web calls itself Web
# from System.ServiceModel.Web, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import (Attribute, DateTime, Enum, Int64, Nullable, Uri, 
    UriTemplate, UriTemplateMatch)

from System.Collections import IEnumerable

from System.Collections.ObjectModel import Collection

from System.IO import Stream

from System.Messaging import Message

from System.Net import HttpStatusCode, WebHeaderCollection

from System.Runtime.Serialization import SerializationInfo, StreamingContext

from System.Runtime.Serialization.Json import DataContractJsonSerializer

from System.ServiceModel import ChannelFactory, IExtension, ServiceHost

from System.ServiceModel.Description import (IContractBehavior, 
    IOperationBehavior)

from System.ServiceModel.Syndication import SyndicationItem

from System.Text import Encoding

from typing import Self

"""The following names are not found in the module: (BoundEvent, 
    IOperationContractAttributeProvider, IWmiInstanceProvider, T, field#)
"""

# no functions
# classes

class AspNetCacheProfileAttribute(Attribute, IOperationBehavior): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ AspNetCacheProfileAttribute(cacheProfileName: str) """
    @property
    def CacheProfileName(self) -> str:
        """ Get: CacheProfileName(self: AspNetCacheProfileAttribute) -> str """
        ...


    def __new__(cls, cacheProfileName:str) -> Self:
        """ __new__(cls: type, cacheProfileName: str) """
        ...


class IncomingWebRequestContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Accept(self) -> str:
        """ Get: Accept(self: IncomingWebRequestContext) -> str """
        ...

    @property
    def ContentLength(self) -> Int64:
        """ Get: ContentLength(self: IncomingWebRequestContext) -> Int64 """
        ...

    @property
    def ContentType(self) -> str:
        """ Get: ContentType(self: IncomingWebRequestContext) -> str """
        ...

    @property
    def Headers(self) -> WebHeaderCollection:
        """ Get: Headers(self: IncomingWebRequestContext) -> WebHeaderCollection """
        ...

    @property
    def IfMatch(self) -> IEnumerable:
        """ Get: IfMatch(self: IncomingWebRequestContext) -> IEnumerable[str] """
        ...

    @property
    def IfModifiedSince(self) -> Nullable:
        """ Get: IfModifiedSince(self: IncomingWebRequestContext) -> Nullable[DateTime] """
        ...

    @property
    def IfNoneMatch(self) -> IEnumerable:
        """ Get: IfNoneMatch(self: IncomingWebRequestContext) -> IEnumerable[str] """
        ...

    @property
    def IfUnmodifiedSince(self) -> Nullable:
        """ Get: IfUnmodifiedSince(self: IncomingWebRequestContext) -> Nullable[DateTime] """
        ...

    @property
    def Method(self) -> str:
        """ Get: Method(self: IncomingWebRequestContext) -> str """
        ...

    @property
    def UriTemplateMatch(self) -> UriTemplateMatch:
        """
        Get: UriTemplateMatch(self: IncomingWebRequestContext) -> UriTemplateMatch
        Set: UriTemplateMatch(self: IncomingWebRequestContext) = value
        """
        ...

    @property
    def UserAgent(self) -> str:
        """ Get: UserAgent(self: IncomingWebRequestContext) -> str """
        ...


    def CheckConditionalRetrieve(self, *__args:str): # -> 
        """ CheckConditionalRetrieve(self: IncomingWebRequestContext, entityTag: str)CheckConditionalRetrieve(self: IncomingWebRequestContext, entityTag: int)CheckConditionalRetrieve(self: IncomingWebRequestContext, entityTag: Int64)CheckConditionalRetrieve(self: IncomingWebRequestContext, entityTag: Guid)CheckConditionalRetrieve(self: IncomingWebRequestContext, lastModified: DateTime) """
        ...

    def CheckConditionalUpdate(self, entityTag:str): # -> 
        """ CheckConditionalUpdate(self: IncomingWebRequestContext, entityTag: str)CheckConditionalUpdate(self: IncomingWebRequestContext, entityTag: int)CheckConditionalUpdate(self: IncomingWebRequestContext, entityTag: Int64)CheckConditionalUpdate(self: IncomingWebRequestContext, entityTag: Guid) """
        ...

    def GetAcceptHeaderElements(self) -> Collection:
        """ GetAcceptHeaderElements(self: IncomingWebRequestContext) -> Collection[ContentType] """
        ...


class IncomingWebResponseContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def ContentLength(self) -> Int64:
        """ Get: ContentLength(self: IncomingWebResponseContext) -> Int64 """
        ...

    @property
    def ContentType(self) -> str:
        """ Get: ContentType(self: IncomingWebResponseContext) -> str """
        ...

    @property
    def ETag(self) -> str:
        """ Get: ETag(self: IncomingWebResponseContext) -> str """
        ...

    @property
    def Headers(self) -> WebHeaderCollection:
        """ Get: Headers(self: IncomingWebResponseContext) -> WebHeaderCollection """
        ...

    @property
    def Location(self) -> str:
        """ Get: Location(self: IncomingWebResponseContext) -> str """
        ...

    @property
    def StatusCode(self) -> HttpStatusCode:
        """ Get: StatusCode(self: IncomingWebResponseContext) -> HttpStatusCode """
        ...

    @property
    def StatusDescription(self) -> str:
        """ Get: StatusDescription(self: IncomingWebResponseContext) -> str """
        ...



class JavascriptCallbackBehaviorAttribute(Attribute, IContractBehavior): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ JavascriptCallbackBehaviorAttribute() """
    @property
    def UrlParameterName(self) -> str:
        """
        Get: UrlParameterName(self: JavascriptCallbackBehaviorAttribute) -> str
        Set: UrlParameterName(self: JavascriptCallbackBehaviorAttribute) = value
        """
        ...



class OutgoingWebRequestContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Accept(self) -> str:
        """
        Get: Accept(self: OutgoingWebRequestContext) -> str
        Set: Accept(self: OutgoingWebRequestContext) = value
        """
        ...

    @property
    def ContentLength(self) -> Int64:
        """
        Get: ContentLength(self: OutgoingWebRequestContext) -> Int64
        Set: ContentLength(self: OutgoingWebRequestContext) = value
        """
        ...

    @property
    def ContentType(self) -> str:
        """
        Get: ContentType(self: OutgoingWebRequestContext) -> str
        Set: ContentType(self: OutgoingWebRequestContext) = value
        """
        ...

    @property
    def Headers(self) -> WebHeaderCollection:
        """ Get: Headers(self: OutgoingWebRequestContext) -> WebHeaderCollection """
        ...

    @property
    def IfMatch(self) -> str:
        """
        Get: IfMatch(self: OutgoingWebRequestContext) -> str
        Set: IfMatch(self: OutgoingWebRequestContext) = value
        """
        ...

    @property
    def IfModifiedSince(self) -> str:
        """
        Get: IfModifiedSince(self: OutgoingWebRequestContext) -> str
        Set: IfModifiedSince(self: OutgoingWebRequestContext) = value
        """
        ...

    @property
    def IfNoneMatch(self) -> str:
        """
        Get: IfNoneMatch(self: OutgoingWebRequestContext) -> str
        Set: IfNoneMatch(self: OutgoingWebRequestContext) = value
        """
        ...

    @property
    def IfUnmodifiedSince(self) -> str:
        """
        Get: IfUnmodifiedSince(self: OutgoingWebRequestContext) -> str
        Set: IfUnmodifiedSince(self: OutgoingWebRequestContext) = value
        """
        ...

    @property
    def Method(self) -> str:
        """
        Get: Method(self: OutgoingWebRequestContext) -> str
        Set: Method(self: OutgoingWebRequestContext) = value
        """
        ...

    @property
    def SuppressEntityBody(self) -> bool:
        """
        Get: SuppressEntityBody(self: OutgoingWebRequestContext) -> bool
        Set: SuppressEntityBody(self: OutgoingWebRequestContext) = value
        """
        ...

    @property
    def UserAgent(self) -> str:
        """
        Get: UserAgent(self: OutgoingWebRequestContext) -> str
        Set: UserAgent(self: OutgoingWebRequestContext) = value
        """
        ...



class OutgoingWebResponseContext: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def BindingWriteEncoding(self) -> Encoding:
        """ Get: BindingWriteEncoding(self: OutgoingWebResponseContext) -> Encoding """
        ...

    @property
    def ContentLength(self) -> Int64:
        """
        Get: ContentLength(self: OutgoingWebResponseContext) -> Int64
        Set: ContentLength(self: OutgoingWebResponseContext) = value
        """
        ...

    @property
    def ContentType(self) -> str:
        """
        Get: ContentType(self: OutgoingWebResponseContext) -> str
        Set: ContentType(self: OutgoingWebResponseContext) = value
        """
        ...

    @property
    def ETag(self) -> str:
        """
        Get: ETag(self: OutgoingWebResponseContext) -> str
        Set: ETag(self: OutgoingWebResponseContext) = value
        """
        ...

    @property
    def Format(self) -> Nullable:
        """
        Get: Format(self: OutgoingWebResponseContext) -> Nullable[WebMessageFormat]
        Set: Format(self: OutgoingWebResponseContext) = value
        """
        ...

    @property
    def Headers(self) -> WebHeaderCollection:
        """ Get: Headers(self: OutgoingWebResponseContext) -> WebHeaderCollection """
        ...

    @property
    def LastModified(self) -> DateTime:
        """
        Get: LastModified(self: OutgoingWebResponseContext) -> DateTime
        Set: LastModified(self: OutgoingWebResponseContext) = value
        """
        ...

    @property
    def Location(self) -> str:
        """
        Get: Location(self: OutgoingWebResponseContext) -> str
        Set: Location(self: OutgoingWebResponseContext) = value
        """
        ...

    @property
    def StatusCode(self) -> HttpStatusCode:
        """
        Get: StatusCode(self: OutgoingWebResponseContext) -> HttpStatusCode
        Set: StatusCode(self: OutgoingWebResponseContext) = value
        """
        ...

    @property
    def StatusDescription(self) -> str:
        """
        Get: StatusDescription(self: OutgoingWebResponseContext) -> str
        Set: StatusDescription(self: OutgoingWebResponseContext) = value
        """
        ...

    @property
    def SuppressEntityBody(self) -> bool:
        """
        Get: SuppressEntityBody(self: OutgoingWebResponseContext) -> bool
        Set: SuppressEntityBody(self: OutgoingWebResponseContext) = value
        """
        ...


    def SetETag(self, entityTag:str): # -> 
        """ SetETag(self: OutgoingWebResponseContext, entityTag: str)SetETag(self: OutgoingWebResponseContext, entityTag: int)SetETag(self: OutgoingWebResponseContext, entityTag: Int64)SetETag(self: OutgoingWebResponseContext, entityTag: Guid) """
        ...

    def SetStatusAsCreated(self, locationUri:Uri): # -> 
        """ SetStatusAsCreated(self: OutgoingWebResponseContext, locationUri: Uri) """
        ...

    def SetStatusAsNotFound(self, description:str = ...): # -> 
        """ SetStatusAsNotFound(self: OutgoingWebResponseContext)SetStatusAsNotFound(self: OutgoingWebResponseContext, description: str) """
        ...


class WebChannelFactory(ChannelFactory): # skipped bases: <type 'IDisposable'>, <type 'IChannelFactory'>, <type 'ICommunicationObject'>, <type 'IChannelFactory[TChannel]'>, <type 'object'>
    """
    WebChannelFactory[TChannel]()
    WebChannelFactory[TChannel](binding: Binding)
    WebChannelFactory[TChannel](endpoint: ServiceEndpoint)
    WebChannelFactory[TChannel](endpointConfigurationName: str)
    WebChannelFactory[TChannel](channelType: Type)
    WebChannelFactory[TChannel](remoteAddress: Uri)
    WebChannelFactory[TChannel](binding: Binding, remoteAddress: Uri)
    WebChannelFactory[TChannel](endpointConfigurationName: str, remoteAddress: Uri)
    """
    pass

class WebFaultException: # skipped bases: <type 'object'>
    """ WebFaultException(statusCode: HttpStatusCode) """
    @property
    def StatusCode(self) -> HttpStatusCode:
        """ Get: StatusCode(self: WebFaultException) -> HttpStatusCode """
        ...


    def GetObjectData(self, info:SerializationInfo, context:StreamingContext): # -> 
        """ GetObjectData(self: WebFaultException, info: SerializationInfo, context: StreamingContext) """
        ...

    def __new__(cls, statusCode:HttpStatusCode) -> Self:
        """
        __new__(cls: type, statusCode: HttpStatusCode)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        ...

    def __reduce_ex__(self, *args): #cannot find CLR method
        ...

    def __str__(self, *args): #cannot find CLR method
        ...

    SerializeObjectState = ...


class WebGetAttribute(Attribute, IOperationContractAttributeProvider, IOperationBehavior, IWmiInstanceProvider): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ WebGetAttribute() """
    @property
    def BodyStyle(self) -> WebMessageBodyStyle:
        """
        Get: BodyStyle(self: WebGetAttribute) -> WebMessageBodyStyle
        Set: BodyStyle(self: WebGetAttribute) = value
        """
        ...

    @property
    def IsBodyStyleSetExplicitly(self) -> bool:
        """ Get: IsBodyStyleSetExplicitly(self: WebGetAttribute) -> bool """
        ...

    @property
    def IsRequestFormatSetExplicitly(self) -> bool:
        """ Get: IsRequestFormatSetExplicitly(self: WebGetAttribute) -> bool """
        ...

    @property
    def IsResponseFormatSetExplicitly(self) -> bool:
        """ Get: IsResponseFormatSetExplicitly(self: WebGetAttribute) -> bool """
        ...

    @property
    def RequestFormat(self) -> WebMessageFormat:
        """
        Get: RequestFormat(self: WebGetAttribute) -> WebMessageFormat
        Set: RequestFormat(self: WebGetAttribute) = value
        """
        ...

    @property
    def ResponseFormat(self) -> WebMessageFormat:
        """
        Get: ResponseFormat(self: WebGetAttribute) -> WebMessageFormat
        Set: ResponseFormat(self: WebGetAttribute) = value
        """
        ...

    @property
    def UriTemplate(self) -> str:
        """
        Get: UriTemplate(self: WebGetAttribute) -> str
        Set: UriTemplate(self: WebGetAttribute) = value
        """
        ...



class WebInvokeAttribute(Attribute, IOperationContractAttributeProvider, IOperationBehavior, IWmiInstanceProvider): # skipped bases: <type '_Attribute'>, <type 'object'>
    """ WebInvokeAttribute() """
    @property
    def BodyStyle(self) -> WebMessageBodyStyle:
        """
        Get: BodyStyle(self: WebInvokeAttribute) -> WebMessageBodyStyle
        Set: BodyStyle(self: WebInvokeAttribute) = value
        """
        ...

    @property
    def IsBodyStyleSetExplicitly(self) -> bool:
        """ Get: IsBodyStyleSetExplicitly(self: WebInvokeAttribute) -> bool """
        ...

    @property
    def IsRequestFormatSetExplicitly(self) -> bool:
        """ Get: IsRequestFormatSetExplicitly(self: WebInvokeAttribute) -> bool """
        ...

    @property
    def IsResponseFormatSetExplicitly(self) -> bool:
        """ Get: IsResponseFormatSetExplicitly(self: WebInvokeAttribute) -> bool """
        ...

    @property
    def Method(self) -> str:
        """
        Get: Method(self: WebInvokeAttribute) -> str
        Set: Method(self: WebInvokeAttribute) = value
        """
        ...

    @property
    def RequestFormat(self) -> WebMessageFormat:
        """
        Get: RequestFormat(self: WebInvokeAttribute) -> WebMessageFormat
        Set: RequestFormat(self: WebInvokeAttribute) = value
        """
        ...

    @property
    def ResponseFormat(self) -> WebMessageFormat:
        """
        Get: ResponseFormat(self: WebInvokeAttribute) -> WebMessageFormat
        Set: ResponseFormat(self: WebInvokeAttribute) = value
        """
        ...

    @property
    def UriTemplate(self) -> str:
        """
        Get: UriTemplate(self: WebInvokeAttribute) -> str
        Set: UriTemplate(self: WebInvokeAttribute) = value
        """
        ...



class WebMessageBodyStyle(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WebMessageBodyStyle, values: Bare (0), Wrapped (1), WrappedRequest (2), WrappedResponse (3) """
    Bare: WebMessageBodyStyle = ...
    value__ = ...
    Wrapped: WebMessageBodyStyle = ...
    WrappedRequest: WebMessageBodyStyle = ...
    WrappedResponse: WebMessageBodyStyle = ...


class WebMessageFormat(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum WebMessageFormat, values: Json (1), Xml (0) """
    Json: WebMessageFormat = ...
    value__ = ...
    Xml: WebMessageFormat = ...


class WebOperationContext(IExtension): # skipped bases: <type 'object'>
    """ WebOperationContext(operationContext: OperationContext) """
    @property
    def Current(self) -> WebOperationContext:
        """ Get: Current() -> WebOperationContext """
        ...

    @property
    def IncomingRequest(self) -> IncomingWebRequestContext:
        """ Get: IncomingRequest(self: WebOperationContext) -> IncomingWebRequestContext """
        ...

    @property
    def IncomingResponse(self) -> IncomingWebResponseContext:
        """ Get: IncomingResponse(self: WebOperationContext) -> IncomingWebResponseContext """
        ...

    @property
    def OutgoingRequest(self) -> OutgoingWebRequestContext:
        """ Get: OutgoingRequest(self: WebOperationContext) -> OutgoingWebRequestContext """
        ...

    @property
    def OutgoingResponse(self) -> OutgoingWebResponseContext:
        """ Get: OutgoingResponse(self: WebOperationContext) -> OutgoingWebResponseContext """
        ...


    def CreateAtom10Response(self, *__args:SyndicationItem) -> Message:
        """
        CreateAtom10Response(self: WebOperationContext, item: SyndicationItem) -> Message
        CreateAtom10Response(self: WebOperationContext, feed: SyndicationFeed) -> Message
        CreateAtom10Response(self: WebOperationContext, document: ServiceDocument) -> Message
        """
        ...

    def CreateJsonResponse(self, instance, serializer:DataContractJsonSerializer = ...) -> Message: # Not found arg types: {'instance': 'T'}
        """
        CreateJsonResponse[T](self: WebOperationContext, instance: T) -> Message
        CreateJsonResponse[T](self: WebOperationContext, instance: T, serializer: DataContractJsonSerializer) -> Message
        """
        ...

    def CreateStreamResponse(self, *__args) -> Message:
        """
        CreateStreamResponse(self: WebOperationContext, stream: Stream, contentType: str) -> Message
        CreateStreamResponse(self: WebOperationContext, bodyWriter: StreamBodyWriter, contentType: str) -> Message
        CreateStreamResponse(self: WebOperationContext, streamWriter: Action[Stream], contentType: str) -> Message
        """
        ...

    def CreateTextResponse(self, *__args:str) -> Message:
        """
        CreateTextResponse(self: WebOperationContext, text: str) -> Message
        CreateTextResponse(self: WebOperationContext, text: str, contentType: str) -> Message
        CreateTextResponse(self: WebOperationContext, text: str, contentType: str, encoding: Encoding) -> Message
        CreateTextResponse(self: WebOperationContext, textWriter: Action[TextWriter], contentType: str) -> Message
        CreateTextResponse(self: WebOperationContext, textWriter: Action[TextWriter], contentType: str, encoding: Encoding) -> Message
        """
        ...

    def CreateXmlResponse(self, *__args) -> Message: # Not found arg types: {'*__args': 'T'}
        """
        CreateXmlResponse[T](self: WebOperationContext, instance: T) -> Message
        CreateXmlResponse[T](self: WebOperationContext, instance: T, serializer: XmlObjectSerializer) -> Message
        CreateXmlResponse[T](self: WebOperationContext, instance: T, serializer: XmlSerializer) -> Message
        CreateXmlResponse(self: WebOperationContext, document: XDocument) -> Message
        CreateXmlResponse(self: WebOperationContext, element: XElement) -> Message
        """
        ...

    def GetUriTemplate(self, operationName:str) -> UriTemplate:
        """ GetUriTemplate(self: WebOperationContext, operationName: str) -> UriTemplate """
        ...


class WebServiceHost(ServiceHost): # skipped bases: <type 'IDisposable'>, <type 'ICommunicationObject'>, <type 'IExtensibleObject[ServiceHostBase]'>, <type 'object'>
    """
    WebServiceHost()
    WebServiceHost(singletonInstance: object, *baseAddresses: Array[Uri])
    WebServiceHost(serviceType: Type, *baseAddresses: Array[Uri])
    """
    pass

