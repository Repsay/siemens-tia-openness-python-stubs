# encoding: utf-8
# module System.Runtime.Remoting.Channels calls itself Channels
# from mscorlib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, System.Runtime.Remoting, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import Array, Enum, IAsyncResult, MarshalByRefObject

from System.Collections import IDictionary, IEnumerator, IList

from System.IO import Stream

from System.Net import EndPoint

from System.Runtime.Remoting.Messaging import (IMessage, IMessageCtrl, 
    IMessageSink)

from System.Runtime.Serialization.Formatters import TypeFilterLevel

from System.Security.Principal import IIdentity

from typing import Tuple as Tuple_

"""The following names are not found in the module: field#
"""

# no functions
# classes

class BaseChannelObjectWithProperties(IDictionary): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    @property
    def Count(self) -> int:
        """ Get: Count(self: BaseChannelObjectWithProperties) -> int """
        ...

    @property
    def IsSynchronized(self) -> bool:
        """ Get: IsSynchronized(self: BaseChannelObjectWithProperties) -> bool """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: BaseChannelObjectWithProperties) -> IDictionary """
        ...

    @property
    def SyncRoot(self) -> object:
        """ Get: SyncRoot(self: BaseChannelObjectWithProperties) -> object """
        ...


    def CopyTo(self, array:Array, index:int): # -> 
        """ CopyTo(self: BaseChannelObjectWithProperties, array: Array, index: int) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary, key: object) -> bool """
        ...


class BaseChannelSinkWithProperties(BaseChannelObjectWithProperties): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    pass

class BaseChannelWithProperties(BaseChannelObjectWithProperties): # skipped bases: <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ no doc """
    SinksWithProperties = ...


class BinaryClientFormatterSink(IClientFormatterSink): # skipped bases: <type 'IClientChannelSink'>, <type 'IChannelSinkBase'>, <type 'IMessageSink'>, <type 'object'>
    """ BinaryClientFormatterSink(nextSink: IClientChannelSink) """
    @property
    def NextChannelSink(self) -> IClientChannelSink:
        """ Get: NextChannelSink(self: BinaryClientFormatterSink) -> IClientChannelSink """
        ...

    @property
    def NextSink(self) -> IMessageSink:
        """ Get: NextSink(self: BinaryClientFormatterSink) -> IMessageSink """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: BinaryClientFormatterSink) -> IDictionary """
        ...


    def AsyncProcessMessage(self, msg:IMessage, replySink:IMessageSink) -> IMessageCtrl:
        """ AsyncProcessMessage(self: BinaryClientFormatterSink, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl """
        ...

    def AsyncProcessRequest(self, sinkStack:IClientChannelSinkStack, msg:IMessage, headers:ITransportHeaders, stream:Stream): # -> 
        """ AsyncProcessRequest(self: BinaryClientFormatterSink, sinkStack: IClientChannelSinkStack, msg: IMessage, headers: ITransportHeaders, stream: Stream) """
        ...

    def AsyncProcessResponse(self, sinkStack:IClientResponseChannelSinkStack, state:object, headers:ITransportHeaders, stream:Stream): # -> 
        """ AsyncProcessResponse(self: BinaryClientFormatterSink, sinkStack: IClientResponseChannelSinkStack, state: object, headers: ITransportHeaders, stream: Stream) """
        ...

    def GetRequestStream(self, msg:IMessage, headers:ITransportHeaders) -> Stream:
        """ GetRequestStream(self: BinaryClientFormatterSink, msg: IMessage, headers: ITransportHeaders) -> Stream """
        ...

    def ProcessMessage(self, msg, requestHeaders, requestStream, responseHeaders, responseStream) -> Tuple_[ITransportHeaders, Stream]:
        """ ProcessMessage(self: BinaryClientFormatterSink, msg: IMessage, requestHeaders: ITransportHeaders, requestStream: Stream) -> (ITransportHeaders, Stream) """
        ...

    def SyncProcessMessage(self, msg:IMessage) -> IMessage:
        """ SyncProcessMessage(self: BinaryClientFormatterSink, msg: IMessage) -> IMessage """
        ...


class BinaryClientFormatterSinkProvider(IClientFormatterSinkProvider): # skipped bases: <type 'IClientChannelSinkProvider'>, <type 'object'>
    """
    BinaryClientFormatterSinkProvider()
    BinaryClientFormatterSinkProvider(properties: IDictionary, providerData: ICollection)
    """
    @property
    def Next(self) -> IClientChannelSinkProvider:
        """
        Get: Next(self: BinaryClientFormatterSinkProvider) -> IClientChannelSinkProvider
        Set: Next(self: BinaryClientFormatterSinkProvider) = value
        """
        ...


    def CreateSink(self, channel:IChannelSender, url:str, remoteChannelData:object) -> IClientChannelSink:
        """ CreateSink(self: BinaryClientFormatterSinkProvider, channel: IChannelSender, url: str, remoteChannelData: object) -> IClientChannelSink """
        ...


class BinaryServerFormatterSink(IServerChannelSink): # skipped bases: <type 'IChannelSinkBase'>, <type 'object'>
    """ BinaryServerFormatterSink(protocol: Protocol, nextSink: IServerChannelSink, receiver: IChannelReceiver) """
    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: BinaryServerFormatterSink) -> IDictionary """
        ...

    @property
    def TypeFilterLevel(self) -> TypeFilterLevel:
        """
        Get: TypeFilterLevel(self: BinaryServerFormatterSink) -> TypeFilterLevel
        Set: TypeFilterLevel(self: BinaryServerFormatterSink) = value
        """
        ...


    def Protocol(self, *args): #cannot find CLR method
        """ enum Protocol, values: Http (0), Other (1) """
        ...



class BinaryServerFormatterSinkProvider(IServerFormatterSinkProvider): # skipped bases: <type 'IServerChannelSinkProvider'>, <type 'object'>
    """
    BinaryServerFormatterSinkProvider()
    BinaryServerFormatterSinkProvider(properties: IDictionary, providerData: ICollection)
    """
    @property
    def Next(self) -> IServerChannelSinkProvider:
        """
        Get: Next(self: BinaryServerFormatterSinkProvider) -> IServerChannelSinkProvider
        Set: Next(self: BinaryServerFormatterSinkProvider) = value
        """
        ...

    @property
    def TypeFilterLevel(self) -> TypeFilterLevel:
        """
        Get: TypeFilterLevel(self: BinaryServerFormatterSinkProvider) -> TypeFilterLevel
        Set: TypeFilterLevel(self: BinaryServerFormatterSinkProvider) = value
        """
        ...


    def CreateSink(self, channel:IChannelReceiver) -> IServerChannelSink:
        """ CreateSink(self: BinaryServerFormatterSinkProvider, channel: IChannelReceiver) -> IServerChannelSink """
        ...

    def GetChannelData(self, channelData:IChannelDataStore): # -> 
        """ GetChannelData(self: BinaryServerFormatterSinkProvider, channelData: IChannelDataStore) """
        ...


class ChannelDataStore(IChannelDataStore): # skipped bases: <type 'object'>
    """ ChannelDataStore(channelURIs: Array[str]) """
    pass

class ChannelServices: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def RegisteredChannels(self) -> Array:
        """ Get: RegisteredChannels() -> Array[IChannel] """
        ...


    @staticmethod
    def AsyncDispatchMessage(msg:IMessage, replySink:IMessageSink) -> IMessageCtrl:
        """ AsyncDispatchMessage(msg: IMessage, replySink: IMessageSink) -> IMessageCtrl """
        ...

    @staticmethod
    def CreateServerChannelSinkChain(provider:IServerChannelSinkProvider, channel:IChannelReceiver) -> IServerChannelSink:
        """ CreateServerChannelSinkChain(provider: IServerChannelSinkProvider, channel: IChannelReceiver) -> IServerChannelSink """
        ...

    @staticmethod
    def DispatchMessage(sinkStack, msg, replyMsg) -> Tuple_[ServerProcessing, IMessage]:
        """ DispatchMessage(sinkStack: IServerChannelSinkStack, msg: IMessage) -> (ServerProcessing, IMessage) """
        ...

    @staticmethod
    def GetChannel(name:str) -> IChannel:
        """ GetChannel(name: str) -> IChannel """
        ...

    @staticmethod
    def GetChannelSinkProperties(obj:object) -> IDictionary:
        """ GetChannelSinkProperties(obj: object) -> IDictionary """
        ...

    @staticmethod
    def GetUrlsForObject(obj:MarshalByRefObject) -> Array:
        """ GetUrlsForObject(obj: MarshalByRefObject) -> Array[str] """
        ...

    @staticmethod
    def RegisterChannel(chnl:IChannel, ensureSecurity:bool = ...): # -> 
        """ RegisterChannel(chnl: IChannel, ensureSecurity: bool)RegisterChannel(chnl: IChannel) """
        ...

    @staticmethod
    def SyncDispatchMessage(msg:IMessage) -> IMessage:
        """ SyncDispatchMessage(msg: IMessage) -> IMessage """
        ...

    @staticmethod
    def UnregisterChannel(chnl:IChannel): # -> 
        """ UnregisterChannel(chnl: IChannel) """
        ...



class ClientChannelSinkStack(IClientChannelSinkStack): # skipped bases: <type 'IClientResponseChannelSinkStack'>, <type 'object'>
    """
    ClientChannelSinkStack()
    ClientChannelSinkStack(replySink: IMessageSink)
    """
    def AsyncProcessResponse(self, headers:ITransportHeaders, stream:Stream): # -> 
        """ AsyncProcessResponse(self: ClientChannelSinkStack, headers: ITransportHeaders, stream: Stream) """
        ...

    def DispatchException(self, e:Exception): # -> 
        """ DispatchException(self: ClientChannelSinkStack, e: Exception) """
        ...

    def DispatchReplyMessage(self, msg:IMessage): # -> 
        """ DispatchReplyMessage(self: ClientChannelSinkStack, msg: IMessage) """
        ...


class CommonTransportKeys: # skipped bases: <type 'object'>, <type 'object'>
    """ CommonTransportKeys() """
    ConnectionId: str = ...
    IPAddress: str = ...
    RequestUri: str = ...


class IAuthorizeRemotingConnection: # skipped bases: <type 'object'>
    """ no doc """
    def IsConnectingEndPointAuthorized(self, endPoint:EndPoint) -> bool:
        """ IsConnectingEndPointAuthorized(self: IAuthorizeRemotingConnection, endPoint: EndPoint) -> bool """
        ...

    def IsConnectingIdentityAuthorized(self, identity:IIdentity) -> bool:
        """ IsConnectingIdentityAuthorized(self: IAuthorizeRemotingConnection, identity: IIdentity) -> bool """
        ...


class IChannel: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ChannelName(self) -> str:
        """ Get: ChannelName(self: IChannel) -> str """
        ...

    @property
    def ChannelPriority(self) -> int:
        """ Get: ChannelPriority(self: IChannel) -> int """
        ...


    def Parse(self, url, objectURI) -> Tuple_[str, str]:
        """ Parse(self: IChannel, url: str) -> (str, str) """
        ...


class IChannelDataStore: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ChannelUris(self) -> Array:
        """ Get: ChannelUris(self: IChannelDataStore) -> Array[str] """
        ...


    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class IChannelReceiver(IChannel): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ChannelData(self) -> object:
        """ Get: ChannelData(self: IChannelReceiver) -> object """
        ...


    def GetUrlsForUri(self, objectURI:str) -> Array:
        """ GetUrlsForUri(self: IChannelReceiver, objectURI: str) -> Array[str] """
        ...

    def StartListening(self, data:object): # -> 
        """ StartListening(self: IChannelReceiver, data: object) """
        ...

    def StopListening(self, data:object): # -> 
        """ StopListening(self: IChannelReceiver, data: object) """
        ...


class IChannelReceiverHook: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ChannelScheme(self) -> str:
        """ Get: ChannelScheme(self: IChannelReceiverHook) -> str """
        ...

    @property
    def ChannelSinkChain(self) -> IServerChannelSink:
        """ Get: ChannelSinkChain(self: IChannelReceiverHook) -> IServerChannelSink """
        ...

    @property
    def WantsToListen(self) -> bool:
        """ Get: WantsToListen(self: IChannelReceiverHook) -> bool """
        ...


    def AddHookChannelUri(self, channelUri:str): # -> 
        """ AddHookChannelUri(self: IChannelReceiverHook, channelUri: str) """
        ...


class IChannelSender(IChannel): # skipped bases: <type 'object'>
    """ no doc """
    def CreateMessageSink(self, url, remoteChannelData, objectURI) -> Tuple_[IMessageSink, str]:
        """ CreateMessageSink(self: IChannelSender, url: str, remoteChannelData: object) -> (IMessageSink, str) """
        ...


class IChannelSinkBase: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: IChannelSinkBase) -> IDictionary """
        ...



class IClientChannelSink(IChannelSinkBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def NextChannelSink(self) -> IClientChannelSink:
        """ Get: NextChannelSink(self: IClientChannelSink) -> IClientChannelSink """
        ...


    def AsyncProcessRequest(self, sinkStack:IClientChannelSinkStack, msg:IMessage, headers:ITransportHeaders, stream:Stream): # -> 
        """ AsyncProcessRequest(self: IClientChannelSink, sinkStack: IClientChannelSinkStack, msg: IMessage, headers: ITransportHeaders, stream: Stream) """
        ...

    def AsyncProcessResponse(self, sinkStack:IClientResponseChannelSinkStack, state:object, headers:ITransportHeaders, stream:Stream): # -> 
        """ AsyncProcessResponse(self: IClientChannelSink, sinkStack: IClientResponseChannelSinkStack, state: object, headers: ITransportHeaders, stream: Stream) """
        ...

    def GetRequestStream(self, msg:IMessage, headers:ITransportHeaders) -> Stream:
        """ GetRequestStream(self: IClientChannelSink, msg: IMessage, headers: ITransportHeaders) -> Stream """
        ...

    def ProcessMessage(self, msg, requestHeaders, requestStream, responseHeaders, responseStream) -> Tuple_[ITransportHeaders, Stream]:
        """ ProcessMessage(self: IClientChannelSink, msg: IMessage, requestHeaders: ITransportHeaders, requestStream: Stream) -> (ITransportHeaders, Stream) """
        ...


class IClientChannelSinkProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Next(self) -> IClientChannelSinkProvider:
        """
        Get: Next(self: IClientChannelSinkProvider) -> IClientChannelSinkProvider
        Set: Next(self: IClientChannelSinkProvider) = value
        """
        ...


    def CreateSink(self, channel:IChannelSender, url:str, remoteChannelData:object) -> IClientChannelSink:
        """ CreateSink(self: IClientChannelSinkProvider, channel: IChannelSender, url: str, remoteChannelData: object) -> IClientChannelSink """
        ...


class IClientResponseChannelSinkStack: # skipped bases: <type 'object'>
    """ no doc """
    def AsyncProcessResponse(self, headers:ITransportHeaders, stream:Stream): # -> 
        """ AsyncProcessResponse(self: IClientResponseChannelSinkStack, headers: ITransportHeaders, stream: Stream) """
        ...

    def DispatchException(self, e:Exception): # -> 
        """ DispatchException(self: IClientResponseChannelSinkStack, e: Exception) """
        ...

    def DispatchReplyMessage(self, msg:IMessage): # -> 
        """ DispatchReplyMessage(self: IClientResponseChannelSinkStack, msg: IMessage) """
        ...


class IClientChannelSinkStack(IClientResponseChannelSinkStack): # skipped bases: <type 'object'>
    """ no doc """
    def Pop(self, sink:IClientChannelSink) -> object:
        """ Pop(self: IClientChannelSinkStack, sink: IClientChannelSink) -> object """
        ...

    def Push(self, sink:IClientChannelSink, state:object): # -> 
        """ Push(self: IClientChannelSinkStack, sink: IClientChannelSink, state: object) """
        ...


class IClientFormatterSink(IMessageSink, IClientChannelSink): # skipped bases: <type 'IChannelSinkBase'>, <type 'object'>
    """ no doc """
    pass

class IClientFormatterSinkProvider(IClientChannelSinkProvider): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ISecurableChannel: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def IsSecured(self) -> bool:
        """
        Get: IsSecured(self: ISecurableChannel) -> bool
        Set: IsSecured(self: ISecurableChannel) = value
        """
        ...



class IServerChannelSink(IChannelSinkBase): # skipped bases: <type 'object'>
    """ no doc """
    @property
    def NextChannelSink(self) -> IServerChannelSink:
        """ Get: NextChannelSink(self: IServerChannelSink) -> IServerChannelSink """
        ...


    def AsyncProcessResponse(self, sinkStack:IServerResponseChannelSinkStack, state:object, msg:IMessage, headers:ITransportHeaders, stream:Stream): # -> 
        """ AsyncProcessResponse(self: IServerChannelSink, sinkStack: IServerResponseChannelSinkStack, state: object, msg: IMessage, headers: ITransportHeaders, stream: Stream) """
        ...

    def GetResponseStream(self, sinkStack:IServerResponseChannelSinkStack, state:object, msg:IMessage, headers:ITransportHeaders) -> Stream:
        """ GetResponseStream(self: IServerChannelSink, sinkStack: IServerResponseChannelSinkStack, state: object, msg: IMessage, headers: ITransportHeaders) -> Stream """
        ...

    def ProcessMessage(self, sinkStack, requestMsg, requestHeaders, requestStream, responseMsg, responseHeaders, responseStream) -> Tuple_[ServerProcessing, IMessage, ITransportHeaders, Stream]:
        """ ProcessMessage(self: IServerChannelSink, sinkStack: IServerChannelSinkStack, requestMsg: IMessage, requestHeaders: ITransportHeaders, requestStream: Stream) -> (ServerProcessing, IMessage, ITransportHeaders, Stream) """
        ...


class IServerChannelSinkProvider: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Next(self) -> IServerChannelSinkProvider:
        """
        Get: Next(self: IServerChannelSinkProvider) -> IServerChannelSinkProvider
        Set: Next(self: IServerChannelSinkProvider) = value
        """
        ...


    def CreateSink(self, channel:IChannelReceiver) -> IServerChannelSink:
        """ CreateSink(self: IServerChannelSinkProvider, channel: IChannelReceiver) -> IServerChannelSink """
        ...

    def GetChannelData(self, channelData:IChannelDataStore): # -> 
        """ GetChannelData(self: IServerChannelSinkProvider, channelData: IChannelDataStore) """
        ...


class IServerResponseChannelSinkStack: # skipped bases: <type 'object'>
    """ no doc """
    def AsyncProcessResponse(self, msg:IMessage, headers:ITransportHeaders, stream:Stream): # -> 
        """ AsyncProcessResponse(self: IServerResponseChannelSinkStack, msg: IMessage, headers: ITransportHeaders, stream: Stream) """
        ...

    def GetResponseStream(self, msg:IMessage, headers:ITransportHeaders) -> Stream:
        """ GetResponseStream(self: IServerResponseChannelSinkStack, msg: IMessage, headers: ITransportHeaders) -> Stream """
        ...


class IServerChannelSinkStack(IServerResponseChannelSinkStack): # skipped bases: <type 'object'>
    """ no doc """
    def Pop(self, sink:IServerChannelSink) -> object:
        """ Pop(self: IServerChannelSinkStack, sink: IServerChannelSink) -> object """
        ...

    def Push(self, sink:IServerChannelSink, state:object): # -> 
        """ Push(self: IServerChannelSinkStack, sink: IServerChannelSink, state: object) """
        ...

    def ServerCallback(self, ar:IAsyncResult): # -> 
        """ ServerCallback(self: IServerChannelSinkStack, ar: IAsyncResult) """
        ...

    def Store(self, sink:IServerChannelSink, state:object): # -> 
        """ Store(self: IServerChannelSinkStack, sink: IServerChannelSink, state: object) """
        ...

    def StoreAndDispatch(self, sink:IServerChannelSink, state:object): # -> 
        """ StoreAndDispatch(self: IServerChannelSinkStack, sink: IServerChannelSink, state: object) """
        ...


class IServerFormatterSinkProvider(IServerChannelSinkProvider): # skipped bases: <type 'object'>
    """ no doc """
    pass

class ITransportHeaders: # skipped bases: <type 'object'>
    """ no doc """
    def GetEnumerator(self) -> IEnumerator:
        """ GetEnumerator(self: ITransportHeaders) -> IEnumerator """
        ...

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        ...

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        ...


class ServerChannelSinkStack(IServerChannelSinkStack): # skipped bases: <type 'IServerResponseChannelSinkStack'>, <type 'object'>
    """ ServerChannelSinkStack() """
    def AsyncProcessResponse(self, msg:IMessage, headers:ITransportHeaders, stream:Stream): # -> 
        """ AsyncProcessResponse(self: ServerChannelSinkStack, msg: IMessage, headers: ITransportHeaders, stream: Stream) """
        ...

    def GetResponseStream(self, msg:IMessage, headers:ITransportHeaders) -> Stream:
        """ GetResponseStream(self: ServerChannelSinkStack, msg: IMessage, headers: ITransportHeaders) -> Stream """
        ...


class ServerProcessing(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum ServerProcessing, values: Async (2), Complete (0), OneWay (1) """
    Async: ServerProcessing = ...
    Complete: ServerProcessing = ...
    OneWay: ServerProcessing = ...
    value__ = ...


class SinkProviderData: # skipped bases: <type 'object'>, <type 'object'>
    """ SinkProviderData(name: str) """
    @property
    def Children(self) -> IList:
        """ Get: Children(self: SinkProviderData) -> IList """
        ...

    @property
    def Name(self) -> str:
        """ Get: Name(self: SinkProviderData) -> str """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: SinkProviderData) -> IDictionary """
        ...



class SoapClientFormatterSink(IClientFormatterSink): # skipped bases: <type 'IClientChannelSink'>, <type 'IChannelSinkBase'>, <type 'IMessageSink'>, <type 'object'>
    """ SoapClientFormatterSink(nextSink: IClientChannelSink) """
    @property
    def NextChannelSink(self) -> IClientChannelSink:
        """ Get: NextChannelSink(self: SoapClientFormatterSink) -> IClientChannelSink """
        ...

    @property
    def NextSink(self) -> IMessageSink:
        """ Get: NextSink(self: SoapClientFormatterSink) -> IMessageSink """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: SoapClientFormatterSink) -> IDictionary """
        ...


    def AsyncProcessMessage(self, msg:IMessage, replySink:IMessageSink) -> IMessageCtrl:
        """ AsyncProcessMessage(self: SoapClientFormatterSink, msg: IMessage, replySink: IMessageSink) -> IMessageCtrl """
        ...

    def AsyncProcessRequest(self, sinkStack:IClientChannelSinkStack, msg:IMessage, headers:ITransportHeaders, stream:Stream): # -> 
        """ AsyncProcessRequest(self: SoapClientFormatterSink, sinkStack: IClientChannelSinkStack, msg: IMessage, headers: ITransportHeaders, stream: Stream) """
        ...

    def AsyncProcessResponse(self, sinkStack:IClientResponseChannelSinkStack, state:object, headers:ITransportHeaders, stream:Stream): # -> 
        """ AsyncProcessResponse(self: SoapClientFormatterSink, sinkStack: IClientResponseChannelSinkStack, state: object, headers: ITransportHeaders, stream: Stream) """
        ...

    def GetRequestStream(self, msg:IMessage, headers:ITransportHeaders) -> Stream:
        """ GetRequestStream(self: SoapClientFormatterSink, msg: IMessage, headers: ITransportHeaders) -> Stream """
        ...

    def ProcessMessage(self, msg, requestHeaders, requestStream, responseHeaders, responseStream) -> Tuple_[ITransportHeaders, Stream]:
        """ ProcessMessage(self: SoapClientFormatterSink, msg: IMessage, requestHeaders: ITransportHeaders, requestStream: Stream) -> (ITransportHeaders, Stream) """
        ...

    def SyncProcessMessage(self, msg:IMessage) -> IMessage:
        """ SyncProcessMessage(self: SoapClientFormatterSink, msg: IMessage) -> IMessage """
        ...


class SoapClientFormatterSinkProvider(IClientFormatterSinkProvider): # skipped bases: <type 'IClientChannelSinkProvider'>, <type 'object'>
    """
    SoapClientFormatterSinkProvider()
    SoapClientFormatterSinkProvider(properties: IDictionary, providerData: ICollection)
    """
    @property
    def Next(self) -> IClientChannelSinkProvider:
        """
        Get: Next(self: SoapClientFormatterSinkProvider) -> IClientChannelSinkProvider
        Set: Next(self: SoapClientFormatterSinkProvider) = value
        """
        ...


    def CreateSink(self, channel:IChannelSender, url:str, remoteChannelData:object) -> IClientChannelSink:
        """ CreateSink(self: SoapClientFormatterSinkProvider, channel: IChannelSender, url: str, remoteChannelData: object) -> IClientChannelSink """
        ...


class SoapServerFormatterSink(IServerChannelSink): # skipped bases: <type 'IChannelSinkBase'>, <type 'object'>
    """ SoapServerFormatterSink(protocol: Protocol, nextSink: IServerChannelSink, receiver: IChannelReceiver) """
    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: SoapServerFormatterSink) -> IDictionary """
        ...

    @property
    def TypeFilterLevel(self) -> TypeFilterLevel:
        """
        Get: TypeFilterLevel(self: SoapServerFormatterSink) -> TypeFilterLevel
        Set: TypeFilterLevel(self: SoapServerFormatterSink) = value
        """
        ...


    def Protocol(self, *args): #cannot find CLR method
        """ enum Protocol, values: Http (0), Other (1) """
        ...



class SoapServerFormatterSinkProvider(IServerFormatterSinkProvider): # skipped bases: <type 'IServerChannelSinkProvider'>, <type 'object'>
    """
    SoapServerFormatterSinkProvider()
    SoapServerFormatterSinkProvider(properties: IDictionary, providerData: ICollection)
    """
    @property
    def Next(self) -> IServerChannelSinkProvider:
        """
        Get: Next(self: SoapServerFormatterSinkProvider) -> IServerChannelSinkProvider
        Set: Next(self: SoapServerFormatterSinkProvider) = value
        """
        ...

    @property
    def TypeFilterLevel(self) -> TypeFilterLevel:
        """
        Get: TypeFilterLevel(self: SoapServerFormatterSinkProvider) -> TypeFilterLevel
        Set: TypeFilterLevel(self: SoapServerFormatterSinkProvider) = value
        """
        ...


    def CreateSink(self, channel:IChannelReceiver) -> IServerChannelSink:
        """ CreateSink(self: SoapServerFormatterSinkProvider, channel: IChannelReceiver) -> IServerChannelSink """
        ...

    def GetChannelData(self, channelData:IChannelDataStore): # -> 
        """ GetChannelData(self: SoapServerFormatterSinkProvider, channelData: IChannelDataStore) """
        ...


class SocketCachePolicy(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum SocketCachePolicy, values: AbsoluteTimeout (1), Default (0) """
    AbsoluteTimeout: SocketCachePolicy = ...
    Default: SocketCachePolicy = ...
    value__ = ...


class TransportHeaders(ITransportHeaders): # skipped bases: <type 'object'>
    """ TransportHeaders() """
    pass

# variables with complex values

