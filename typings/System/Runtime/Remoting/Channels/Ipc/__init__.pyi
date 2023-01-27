# encoding: utf-8
# module System.Runtime.Remoting.Channels.Ipc calls itself Ipc
# from System.Runtime.Remoting, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Runtime.Remoting.Channels import (IChannelReceiver, 
    IChannelSender, ISecurableChannel)

from typing import Tuple as Tuple_


# no functions
# classes

class IpcChannel(ISecurableChannel, IChannelSender, IChannelReceiver): # skipped bases: <type 'IChannel'>, <type 'object'>
    """
    IpcChannel()
    IpcChannel(portName: str)
    IpcChannel(properties: IDictionary, clientSinkProvider: IClientChannelSinkProvider, serverSinkProvider: IServerChannelSinkProvider)
    IpcChannel(properties: IDictionary, clientSinkProvider: IClientChannelSinkProvider, serverSinkProvider: IServerChannelSinkProvider, securityDescriptor: CommonSecurityDescriptor)
    """
    @property
    def ChannelName(self) -> str:
        """ Get: ChannelName(self: IpcChannel) -> str """
        ...

    @property
    def ChannelPriority(self) -> int:
        """ Get: ChannelPriority(self: IpcChannel) -> int """
        ...


    def Parse(self, url, objectURI) -> Tuple_[str, str]:
        """ Parse(self: IpcChannel, url: str) -> (str, str) """
        ...


class IpcClientChannel(ISecurableChannel, IChannelSender): # skipped bases: <type 'IChannel'>, <type 'object'>
    """
    IpcClientChannel()
    IpcClientChannel(name: str, sinkProvider: IClientChannelSinkProvider)
    IpcClientChannel(properties: IDictionary, sinkProvider: IClientChannelSinkProvider)
    """
    @property
    def ChannelName(self) -> str:
        """ Get: ChannelName(self: IpcClientChannel) -> str """
        ...

    @property
    def ChannelPriority(self) -> int:
        """ Get: ChannelPriority(self: IpcClientChannel) -> int """
        ...


    def Parse(self, url, objectURI) -> Tuple_[str, str]:
        """ Parse(self: IpcClientChannel, url: str) -> (str, str) """
        ...


class IpcServerChannel(ISecurableChannel, IChannelReceiver): # skipped bases: <type 'IChannel'>, <type 'object'>
    """
    IpcServerChannel(portName: str)
    IpcServerChannel(name: str, portName: str)
    IpcServerChannel(name: str, portName: str, sinkProvider: IServerChannelSinkProvider)
    IpcServerChannel(properties: IDictionary, sinkProvider: IServerChannelSinkProvider)
    IpcServerChannel(properties: IDictionary, sinkProvider: IServerChannelSinkProvider, securityDescriptor: CommonSecurityDescriptor)
    """
    @property
    def ChannelName(self) -> str:
        """ Get: ChannelName(self: IpcServerChannel) -> str """
        ...

    @property
    def ChannelPriority(self) -> int:
        """ Get: ChannelPriority(self: IpcServerChannel) -> int """
        ...


    def GetChannelUri(self) -> str:
        """ GetChannelUri(self: IpcServerChannel) -> str """
        ...

    def Parse(self, url, objectURI) -> Tuple_[str, str]:
        """ Parse(self: IpcServerChannel, url: str) -> (str, str) """
        ...


