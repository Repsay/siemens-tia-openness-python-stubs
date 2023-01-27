# encoding: utf-8
# module System.Workflow.Activities.Configuration calls itself Configuration
# from System.Workflow.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Configuration import ConfigurationSection


# no functions
# classes

class ActiveDirectoryRoleFactoryConfiguration(ConfigurationSection): # skipped bases: <type 'object'>
    """ ActiveDirectoryRoleFactoryConfiguration() """
    @property
    def DirectReports(self) -> str:
        """
        Get: DirectReports(self: ActiveDirectoryRoleFactoryConfiguration) -> str
        Set: DirectReports(self: ActiveDirectoryRoleFactoryConfiguration) = value
        """
        ...

    @property
    def DistinguishedName(self) -> str:
        """
        Get: DistinguishedName(self: ActiveDirectoryRoleFactoryConfiguration) -> str
        Set: DistinguishedName(self: ActiveDirectoryRoleFactoryConfiguration) = value
        """
        ...

    @property
    def Group(self) -> str:
        """
        Get: Group(self: ActiveDirectoryRoleFactoryConfiguration) -> str
        Set: Group(self: ActiveDirectoryRoleFactoryConfiguration) = value
        """
        ...

    @property
    def Manager(self) -> str:
        """
        Get: Manager(self: ActiveDirectoryRoleFactoryConfiguration) -> str
        Set: Manager(self: ActiveDirectoryRoleFactoryConfiguration) = value
        """
        ...

    @property
    def Member(self) -> str:
        """
        Get: Member(self: ActiveDirectoryRoleFactoryConfiguration) -> str
        Set: Member(self: ActiveDirectoryRoleFactoryConfiguration) = value
        """
        ...

    @property
    def RootPath(self) -> str:
        """
        Get: RootPath(self: ActiveDirectoryRoleFactoryConfiguration) -> str
        Set: RootPath(self: ActiveDirectoryRoleFactoryConfiguration) = value
        """
        ...



