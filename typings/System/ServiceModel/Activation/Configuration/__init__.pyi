# encoding: utf-8
# module System.ServiceModel.Activation.Configuration calls itself Configuration
# from System.ServiceModel, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import TimeSpan

from System.Configuration import (Configuration, ConfigurationElement, 
    ConfigurationSection, ConfigurationSectionGroup)

from System.Security.Principal import SecurityIdentifier

from System.ServiceModel.Configuration import (
    ServiceModelConfigurationElementCollection)

from typing import Self


# no functions
# classes

class DiagnosticSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ DiagnosticSection() """
    @property
    def PerformanceCountersEnabled(self) -> bool:
        """
        Get: PerformanceCountersEnabled(self: DiagnosticSection) -> bool
        Set: PerformanceCountersEnabled(self: DiagnosticSection) = value
        """
        ...



class NetPipeSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ NetPipeSection() """
    @property
    def AllowAccounts(self) -> SecurityIdentifierElementCollection:
        """ Get: AllowAccounts(self: NetPipeSection) -> SecurityIdentifierElementCollection """
        ...

    @property
    def MaxPendingAccepts(self) -> int:
        """
        Get: MaxPendingAccepts(self: NetPipeSection) -> int
        Set: MaxPendingAccepts(self: NetPipeSection) = value
        """
        ...

    @property
    def MaxPendingConnections(self) -> int:
        """
        Get: MaxPendingConnections(self: NetPipeSection) -> int
        Set: MaxPendingConnections(self: NetPipeSection) = value
        """
        ...

    @property
    def ReceiveTimeout(self) -> TimeSpan:
        """
        Get: ReceiveTimeout(self: NetPipeSection) -> TimeSpan
        Set: ReceiveTimeout(self: NetPipeSection) = value
        """
        ...



class NetTcpSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ NetTcpSection() """
    @property
    def AllowAccounts(self) -> SecurityIdentifierElementCollection:
        """ Get: AllowAccounts(self: NetTcpSection) -> SecurityIdentifierElementCollection """
        ...

    @property
    def ListenBacklog(self) -> int:
        """
        Get: ListenBacklog(self: NetTcpSection) -> int
        Set: ListenBacklog(self: NetTcpSection) = value
        """
        ...

    @property
    def MaxPendingAccepts(self) -> int:
        """
        Get: MaxPendingAccepts(self: NetTcpSection) -> int
        Set: MaxPendingAccepts(self: NetTcpSection) = value
        """
        ...

    @property
    def MaxPendingConnections(self) -> int:
        """
        Get: MaxPendingConnections(self: NetTcpSection) -> int
        Set: MaxPendingConnections(self: NetTcpSection) = value
        """
        ...

    @property
    def ReceiveTimeout(self) -> TimeSpan:
        """
        Get: ReceiveTimeout(self: NetTcpSection) -> TimeSpan
        Set: ReceiveTimeout(self: NetTcpSection) = value
        """
        ...

    @property
    def TeredoEnabled(self) -> bool:
        """
        Get: TeredoEnabled(self: NetTcpSection) -> bool
        Set: TeredoEnabled(self: NetTcpSection) = value
        """
        ...



class SecurityIdentifierElement(ConfigurationElement): # skipped bases: <type 'object'>
    """
    SecurityIdentifierElement()
    SecurityIdentifierElement(sid: SecurityIdentifier)
    """
    @property
    def SecurityIdentifier(self) -> SecurityIdentifier:
        """
        Get: SecurityIdentifier(self: SecurityIdentifierElement) -> SecurityIdentifier
        Set: SecurityIdentifier(self: SecurityIdentifierElement) = value
        """
        ...


    def __new__(cls, sid:SecurityIdentifier = ...) -> Self:
        """
        __new__(cls: type)
        __new__(cls: type, sid: SecurityIdentifier)
        """
        ...


class SecurityIdentifierElementCollection(ServiceModelConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ SecurityIdentifierElementCollection() """
    pass

class ServiceModelActivationSectionGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ ServiceModelActivationSectionGroup() """
    @property
    def Diagnostics(self) -> DiagnosticSection:
        """ Get: Diagnostics(self: ServiceModelActivationSectionGroup) -> DiagnosticSection """
        ...

    @property
    def NetPipe(self) -> NetPipeSection:
        """ Get: NetPipe(self: ServiceModelActivationSectionGroup) -> NetPipeSection """
        ...

    @property
    def NetTcp(self) -> NetTcpSection:
        """ Get: NetTcp(self: ServiceModelActivationSectionGroup) -> NetTcpSection """
        ...


    @staticmethod
    def GetSectionGroup(config:Configuration) -> ServiceModelActivationSectionGroup:
        """ GetSectionGroup(config: Configuration) -> ServiceModelActivationSectionGroup """
        ...


