# encoding: utf-8
# module System.Runtime.Remoting.Channels.Http calls itself Http
# from System.Runtime.Remoting, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Runtime.Remoting.Channels import (BaseChannelWithProperties, 
    IChannelReceiver, IChannelReceiverHook, IChannelSender, ISecurableChannel)

from System.Web import IHttpHandler, IHttpHandlerFactory

from typing import Self, Tuple as Tuple_

"""The following names are not found in the module: field#
"""

# no functions
# classes

class HttpChannel(ISecurableChannel, BaseChannelWithProperties, IChannelSender, IChannelReceiverHook, IChannelReceiver): # skipped bases: <type 'IChannel'>, <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    HttpChannel()
    HttpChannel(port: int)
    HttpChannel(properties: IDictionary, clientSinkProvider: IClientChannelSinkProvider, serverSinkProvider: IServerChannelSinkProvider)
    """
    @property
    def ChannelName(self) -> str:
        """ Get: ChannelName(self: HttpChannel) -> str """
        ...

    @property
    def ChannelPriority(self) -> int:
        """ Get: ChannelPriority(self: HttpChannel) -> int """
        ...


    def Parse(self, url, objectURI) -> Tuple_[str, str]:
        """ Parse(self: HttpChannel, url: str) -> (str, str) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary, key: object) -> bool """
        ...

    def __new__(cls, *__args:int) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, port: int)
        __new__(cls: type, properties: IDictionary, clientSinkProvider: IClientChannelSinkProvider, serverSinkProvider: IServerChannelSinkProvider)
        """
        ...

    SinksWithProperties = ...


class HttpClientChannel(ISecurableChannel, BaseChannelWithProperties, IChannelSender): # skipped bases: <type 'IChannel'>, <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    HttpClientChannel()
    HttpClientChannel(name: str, sinkProvider: IClientChannelSinkProvider)
    HttpClientChannel(properties: IDictionary, sinkProvider: IClientChannelSinkProvider)
    """
    @property
    def ChannelName(self) -> str:
        """ Get: ChannelName(self: HttpClientChannel) -> str """
        ...

    @property
    def ChannelPriority(self) -> int:
        """ Get: ChannelPriority(self: HttpClientChannel) -> int """
        ...


    def Parse(self, url, objectURI) -> Tuple_[str, str]:
        """ Parse(self: HttpClientChannel, url: str) -> (str, str) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary, key: object) -> bool """
        ...

    def __new__(cls, *__args) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, name: str, sinkProvider: IClientChannelSinkProvider)
        __new__(cls: type, properties: IDictionary, sinkProvider: IClientChannelSinkProvider)
        """
        ...

    SinksWithProperties = ...


class HttpRemotingHandler(IHttpHandler): # skipped bases: <type 'object'>
    """
    HttpRemotingHandler()
    HttpRemotingHandler(type: Type, srvID: object)
    """
    pass

class HttpRemotingHandlerFactory(IHttpHandlerFactory): # skipped bases: <type 'object'>
    """ HttpRemotingHandlerFactory() """
    pass

class HttpServerChannel(BaseChannelWithProperties, IChannelReceiverHook, IChannelReceiver): # skipped bases: <type 'IChannel'>, <type 'IDictionary'>, <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """
    HttpServerChannel()
    HttpServerChannel(port: int)
    HttpServerChannel(name: str, port: int)
    HttpServerChannel(name: str, port: int, sinkProvider: IServerChannelSinkProvider)
    HttpServerChannel(properties: IDictionary, sinkProvider: IServerChannelSinkProvider)
    """
    @property
    def ChannelName(self) -> str:
        """ Get: ChannelName(self: HttpServerChannel) -> str """
        ...

    @property
    def ChannelPriority(self) -> int:
        """ Get: ChannelPriority(self: HttpServerChannel) -> int """
        ...


    def GetChannelUri(self) -> str:
        """ GetChannelUri(self: HttpServerChannel) -> str """
        ...

    def Parse(self, url, objectURI) -> Tuple_[str, str]:
        """ Parse(self: HttpServerChannel, url: str) -> (str, str) """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary, key: object) -> bool """
        ...

    def __new__(cls, *__args:int) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, port: int)
        __new__(cls: type, name: str, port: int)
        __new__(cls: type, name: str, port: int, sinkProvider: IServerChannelSinkProvider)
        __new__(cls: type, properties: IDictionary, sinkProvider: IServerChannelSinkProvider)
        """
        ...

    SinksWithProperties = ...


