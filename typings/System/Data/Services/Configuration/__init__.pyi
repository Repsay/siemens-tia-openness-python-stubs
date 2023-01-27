# encoding: utf-8
# module System.Data.Services.Configuration calls itself Configuration
# from System.Data.Services, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Configuration import (ConfigurationElement, ConfigurationSection, 
    ConfigurationSectionGroup)


# no functions
# classes

class DataServicesFeaturesSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ DataServicesFeaturesSection() """
    @property
    def ReplaceFunction(self) -> DataServicesReplaceFunctionFeature:
        """
        Get: ReplaceFunction(self: DataServicesFeaturesSection) -> DataServicesReplaceFunctionFeature
        Set: ReplaceFunction(self: DataServicesFeaturesSection) = value
        """
        ...



class DataServicesReplaceFunctionFeature(ConfigurationElement): # skipped bases: <type 'object'>
    """ DataServicesReplaceFunctionFeature() """
    @property
    def Enable(self) -> bool:
        """
        Get: Enable(self: DataServicesReplaceFunctionFeature) -> bool
        Set: Enable(self: DataServicesReplaceFunctionFeature) = value
        """
        ...



class DataServicesSectionGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ DataServicesSectionGroup() """
    @property
    def Features(self) -> DataServicesFeaturesSection:
        """ Get: Features(self: DataServicesSectionGroup) -> DataServicesFeaturesSection """
        ...



