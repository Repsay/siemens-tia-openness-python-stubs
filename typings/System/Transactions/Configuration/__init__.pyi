# encoding: utf-8
# module System.Transactions.Configuration calls itself Configuration
# from System.Transactions, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import TimeSpan

from System.Configuration import (Configuration, ConfigurationSection, 
    ConfigurationSectionGroup)


# no functions
# classes

class DefaultSettingsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ DefaultSettingsSection() """
    @property
    def DistributedTransactionManagerName(self) -> str:
        """
        Get: DistributedTransactionManagerName(self: DefaultSettingsSection) -> str
        Set: DistributedTransactionManagerName(self: DefaultSettingsSection) = value
        """
        ...

    @property
    def Timeout(self) -> TimeSpan:
        """
        Get: Timeout(self: DefaultSettingsSection) -> TimeSpan
        Set: Timeout(self: DefaultSettingsSection) = value
        """
        ...



class MachineSettingsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ MachineSettingsSection() """
    @property
    def MaxTimeout(self) -> TimeSpan:
        """
        Get: MaxTimeout(self: MachineSettingsSection) -> TimeSpan
        Set: MaxTimeout(self: MachineSettingsSection) = value
        """
        ...



class TransactionsSectionGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ TransactionsSectionGroup() """
    @property
    def DefaultSettings(self) -> DefaultSettingsSection:
        """ Get: DefaultSettings(self: TransactionsSectionGroup) -> DefaultSettingsSection """
        ...

    @property
    def MachineSettings(self) -> MachineSettingsSection:
        """ Get: MachineSettings(self: TransactionsSectionGroup) -> MachineSettingsSection """
        ...


    @staticmethod
    def GetSectionGroup(config:Configuration) -> TransactionsSectionGroup:
        """ GetSectionGroup(config: Configuration) -> TransactionsSectionGroup """
        ...


