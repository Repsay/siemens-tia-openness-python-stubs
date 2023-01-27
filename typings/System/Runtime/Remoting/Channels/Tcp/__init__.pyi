# encoding: utf-8
# module System.Runtime.Remoting.Channels.Tcp calls itself Tcp
# from System.Runtime.Remoting, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Runtime.Remoting.Channels import (IChannelReceiver, 
    IChannelSender, ISecurableChannel)

from typing import Tuple as Tuple_


# no functions
# classes

class TcpChannel(ISecurableChannel, IChannelSender, IChannelReceiver): # skipped bases: <type 'IChannel'>, <type 'object'>
    """
    TcpChannel()
    TcpChannel(port: int)
    TcpChannel(properties: IDictionary, clientSinkProvider: IClientChannelSinkProvider, serverSinkProvider: IServerChannelSinkProvider)
    """
    @property
    def ChannelName(self) -> str:
        """ Get: ChannelName(self: TcpChannel) -> str """
        ...

    @property
    def ChannelPriority(self) -> int:
        """ Get: ChannelPriority(self: TcpChannel) -> int """
        ...


    def Parse(self, url, objectURI) -> Tuple_[str, str]:
        """ Parse(self: TcpChannel, url: str) -> (str, str) """
        ...


class TcpClientChannel(ISecurableChannel, IChannelSender): # skipped bases: <type 'IChannel'>, <type 'object'>
    """
    TcpClientChannel()
    TcpClientChannel(name: str, sinkProvider: IClientChannelSinkProvider)
    TcpClientChannel(properties: IDictionary, sinkProvider: IClientChannelSinkProvider)
    """
    @property
    def ChannelName(self) -> str:
        """ Get: ChannelName(self: TcpClientChannel) -> str """
        ...

    @property
    def ChannelPriority(self) -> int:
        """ Get: ChannelPriority(self: TcpClientChannel) -> int """
        ...


    def Parse(self, url, objectURI) -> Tuple_[str, str]:
        """ Parse(self: TcpClientChannel, url: str) -> (str, str) """
        ...


class TcpServerChannel(ISecurableChannel, IChannelReceiver): # skipped bases: <type 'IChannel'>, <type 'object'>
    """
    TcpServerChannel(port: int)
    TcpServerChannel(name: str, port: int)
    TcpServerChannel(name: str, port: int, sinkProvider: IServerChannelSinkProvider)
    TcpServerChannel(properties: IDictionary, sinkProvider: IServerChannelSinkProvider)
    TcpServerChannel(properties: IDictionary, sinkProvider: IServerChannelSinkProvider, authorizeCallback: IAuthorizeRemotingConnection)
    """
    @property
    def ChannelName(self) -> str:
        """ Get: ChannelName(self: TcpServerChannel) -> str """
        ...

    @property
    def ChannelPriority(self) -> int:
        """ Get: ChannelPriority(self: TcpServerChannel) -> int """
        ...


    def GetChannelUri(self) -> str:
        """ GetChannelUri(self: TcpServerChannel) -> str """
        ...

    def Parse(self, url, objectURI) -> Tuple_[str, str]:
        """ Parse(self: TcpServerChannel, url: str) -> (str, str) """
        ...


