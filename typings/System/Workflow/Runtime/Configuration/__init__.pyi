# encoding: utf-8
# module System.Workflow.Runtime.Configuration calls itself Configuration
# from System.Workflow.Runtime, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System.Collections.Specialized import NameValueCollection

from System.Configuration import (ConfigurationElement, 
    ConfigurationElementCollection, ConfigurationSection, 
    NameValueConfigurationCollection)


# no functions
# classes

class WorkflowRuntimeSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ WorkflowRuntimeSection() """
    @property
    def CommonParameters(self) -> NameValueConfigurationCollection:
        """ Get: CommonParameters(self: WorkflowRuntimeSection) -> NameValueConfigurationCollection """
        ...

    @property
    def EnablePerformanceCounters(self) -> bool:
        """
        Get: EnablePerformanceCounters(self: WorkflowRuntimeSection) -> bool
        Set: EnablePerformanceCounters(self: WorkflowRuntimeSection) = value
        """
        ...

    @property
    def Name(self) -> str:
        """
        Get: Name(self: WorkflowRuntimeSection) -> str
        Set: Name(self: WorkflowRuntimeSection) = value
        """
        ...

    @property
    def Services(self) -> WorkflowRuntimeServiceElementCollection:
        """ Get: Services(self: WorkflowRuntimeSection) -> WorkflowRuntimeServiceElementCollection """
        ...

    @property
    def ValidateOnCreate(self) -> bool:
        """
        Get: ValidateOnCreate(self: WorkflowRuntimeSection) -> bool
        Set: ValidateOnCreate(self: WorkflowRuntimeSection) = value
        """
        ...

    @property
    def WorkflowDefinitionCacheCapacity(self) -> int:
        """
        Get: WorkflowDefinitionCacheCapacity(self: WorkflowRuntimeSection) -> int
        Set: WorkflowDefinitionCacheCapacity(self: WorkflowRuntimeSection) = value
        """
        ...



class WorkflowRuntimeServiceElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ WorkflowRuntimeServiceElement() """
    @property
    def Parameters(self) -> NameValueCollection:
        """ Get: Parameters(self: WorkflowRuntimeServiceElement) -> NameValueCollection """
        ...

    @property
    def Type(self) -> str:
        """
        Get: Type(self: WorkflowRuntimeServiceElement) -> str
        Set: Type(self: WorkflowRuntimeServiceElement) = value
        """
        ...



class WorkflowRuntimeServiceElementCollection(ConfigurationElementCollection): # skipped bases: <type 'IEnumerable'>, <type 'ICollection'>, <type 'object'>
    """ WorkflowRuntimeServiceElementCollection() """
    def Add(self, serviceSettings:WorkflowRuntimeServiceElement): # -> 
        """ Add(self: WorkflowRuntimeServiceElementCollection, serviceSettings: WorkflowRuntimeServiceElement) """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...


