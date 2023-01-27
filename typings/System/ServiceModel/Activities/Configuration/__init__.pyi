# encoding: utf-8
# module System.ServiceModel.Activities.Configuration calls itself Configuration
# from System.ServiceModel.Activities, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" no doc """
from __future__ import annotations
from System import TimeSpan, Uri

from System.Configuration import (Configuration, ConfigurationElement, 
    ConfigurationSection, ConfigurationSectionGroup)

from System.ServiceModel.Activities.Description import (
    WorkflowUnhandledExceptionAction)

"""The following names are not found in the module: (BehaviorExtensionElement, 
    InstanceCompletionAction, InstanceEncodingOption, 
    InstanceLockedExceptionAction, StandardEndpointCollectionElement, 
    StandardEndpointElement)
"""

# no functions
# classes

class BufferedReceiveElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ BufferedReceiveElement() """
    @property
    def MaxPendingMessagesPerChannel(self) -> int:
        """
        Get: MaxPendingMessagesPerChannel(self: BufferedReceiveElement) -> int
        Set: MaxPendingMessagesPerChannel(self: BufferedReceiveElement) = value
        """
        ...



class ChannelSettingsElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ ChannelSettingsElement() """
    @property
    def IdleTimeout(self) -> TimeSpan:
        """
        Get: IdleTimeout(self: ChannelSettingsElement) -> TimeSpan
        Set: IdleTimeout(self: ChannelSettingsElement) = value
        """
        ...

    @property
    def LeaseTimeout(self) -> TimeSpan:
        """
        Get: LeaseTimeout(self: ChannelSettingsElement) -> TimeSpan
        Set: LeaseTimeout(self: ChannelSettingsElement) = value
        """
        ...

    @property
    def MaxItemsInCache(self) -> int:
        """
        Get: MaxItemsInCache(self: ChannelSettingsElement) -> int
        Set: MaxItemsInCache(self: ChannelSettingsElement) = value
        """
        ...



class EtwTrackingBehaviorElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ EtwTrackingBehaviorElement() """
    @property
    def ProfileName(self) -> str:
        """
        Get: ProfileName(self: EtwTrackingBehaviorElement) -> str
        Set: ProfileName(self: EtwTrackingBehaviorElement) = value
        """
        ...



class FactorySettingsElement(ConfigurationElement): # skipped bases: <type 'object'>
    """ FactorySettingsElement() """
    @property
    def IdleTimeout(self) -> TimeSpan:
        """
        Get: IdleTimeout(self: FactorySettingsElement) -> TimeSpan
        Set: IdleTimeout(self: FactorySettingsElement) = value
        """
        ...

    @property
    def LeaseTimeout(self) -> TimeSpan:
        """
        Get: LeaseTimeout(self: FactorySettingsElement) -> TimeSpan
        Set: LeaseTimeout(self: FactorySettingsElement) = value
        """
        ...

    @property
    def MaxItemsInCache(self) -> int:
        """
        Get: MaxItemsInCache(self: FactorySettingsElement) -> int
        Set: MaxItemsInCache(self: FactorySettingsElement) = value
        """
        ...



class SendMessageChannelCacheElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ SendMessageChannelCacheElement() """
    @property
    def AllowUnsafeCaching(self) -> bool:
        """
        Get: AllowUnsafeCaching(self: SendMessageChannelCacheElement) -> bool
        Set: AllowUnsafeCaching(self: SendMessageChannelCacheElement) = value
        """
        ...

    @property
    def ChannelSettings(self) -> ChannelSettingsElement:
        """ Get: ChannelSettings(self: SendMessageChannelCacheElement) -> ChannelSettingsElement """
        ...

    @property
    def FactorySettings(self) -> FactorySettingsElement:
        """ Get: FactorySettings(self: SendMessageChannelCacheElement) -> FactorySettingsElement """
        ...



class ServiceModelActivitiesSectionGroup(ConfigurationSectionGroup): # skipped bases: <type 'object'>
    """ ServiceModelActivitiesSectionGroup() """
    @property
    def WorkflowHostingOptionsSection(self) -> WorkflowHostingOptionsSection:
        """ Get: WorkflowHostingOptionsSection(self: ServiceModelActivitiesSectionGroup) -> WorkflowHostingOptionsSection """
        ...


    @staticmethod
    def GetSectionGroup(config:Configuration) -> ServiceModelActivitiesSectionGroup:
        """ GetSectionGroup(config: Configuration) -> ServiceModelActivitiesSectionGroup """
        ...


class SqlWorkflowInstanceStoreElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ SqlWorkflowInstanceStoreElement() """
    @property
    def ConnectionString(self) -> str:
        """
        Get: ConnectionString(self: SqlWorkflowInstanceStoreElement) -> str
        Set: ConnectionString(self: SqlWorkflowInstanceStoreElement) = value
        """
        ...

    @property
    def ConnectionStringName(self) -> str:
        """
        Get: ConnectionStringName(self: SqlWorkflowInstanceStoreElement) -> str
        Set: ConnectionStringName(self: SqlWorkflowInstanceStoreElement) = value
        """
        ...

    @property
    def HostLockRenewalPeriod(self) -> TimeSpan:
        """
        Get: HostLockRenewalPeriod(self: SqlWorkflowInstanceStoreElement) -> TimeSpan
        Set: HostLockRenewalPeriod(self: SqlWorkflowInstanceStoreElement) = value
        """
        ...

    @property
    def InstanceCompletionAction(self): # -> InstanceCompletionAction
        """
        Get: InstanceCompletionAction(self: SqlWorkflowInstanceStoreElement) -> InstanceCompletionAction
        Set: InstanceCompletionAction(self: SqlWorkflowInstanceStoreElement) = value
        """
        ...

    @property
    def InstanceEncodingOption(self): # -> InstanceEncodingOption
        """
        Get: InstanceEncodingOption(self: SqlWorkflowInstanceStoreElement) -> InstanceEncodingOption
        Set: InstanceEncodingOption(self: SqlWorkflowInstanceStoreElement) = value
        """
        ...

    @property
    def InstanceLockedExceptionAction(self): # -> InstanceLockedExceptionAction
        """
        Get: InstanceLockedExceptionAction(self: SqlWorkflowInstanceStoreElement) -> InstanceLockedExceptionAction
        Set: InstanceLockedExceptionAction(self: SqlWorkflowInstanceStoreElement) = value
        """
        ...

    @property
    def MaxConnectionRetries(self) -> int:
        """
        Get: MaxConnectionRetries(self: SqlWorkflowInstanceStoreElement) -> int
        Set: MaxConnectionRetries(self: SqlWorkflowInstanceStoreElement) = value
        """
        ...

    @property
    def RunnableInstancesDetectionPeriod(self) -> TimeSpan:
        """
        Get: RunnableInstancesDetectionPeriod(self: SqlWorkflowInstanceStoreElement) -> TimeSpan
        Set: RunnableInstancesDetectionPeriod(self: SqlWorkflowInstanceStoreElement) = value
        """
        ...



class WorkflowControlEndpointCollectionElement(StandardEndpointCollectionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WorkflowControlEndpointCollectionElement() """
    pass

class WorkflowControlEndpointElement(StandardEndpointElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WorkflowControlEndpointElement() """
    @property
    def Address(self) -> Uri:
        """
        Get: Address(self: WorkflowControlEndpointElement) -> Uri
        Set: Address(self: WorkflowControlEndpointElement) = value
        """
        ...

    @property
    def Binding(self) -> str:
        """
        Get: Binding(self: WorkflowControlEndpointElement) -> str
        Set: Binding(self: WorkflowControlEndpointElement) = value
        """
        ...

    @property
    def BindingConfiguration(self) -> str:
        """
        Get: BindingConfiguration(self: WorkflowControlEndpointElement) -> str
        Set: BindingConfiguration(self: WorkflowControlEndpointElement) = value
        """
        ...



class WorkflowHostingOptionsSection(ConfigurationSection): # skipped bases: <type 'object'>
    """ WorkflowHostingOptionsSection() """
    @property
    def OverrideSiteName(self) -> bool:
        """
        Get: OverrideSiteName(self: WorkflowHostingOptionsSection) -> bool
        Set: OverrideSiteName(self: WorkflowHostingOptionsSection) = value
        """
        ...



class WorkflowIdleElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WorkflowIdleElement() """
    @property
    def TimeToPersist(self) -> TimeSpan:
        """
        Get: TimeToPersist(self: WorkflowIdleElement) -> TimeSpan
        Set: TimeToPersist(self: WorkflowIdleElement) = value
        """
        ...

    @property
    def TimeToUnload(self) -> TimeSpan:
        """
        Get: TimeToUnload(self: WorkflowIdleElement) -> TimeSpan
        Set: TimeToUnload(self: WorkflowIdleElement) = value
        """
        ...



class WorkflowInstanceManagementElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WorkflowInstanceManagementElement() """
    @property
    def AuthorizedWindowsGroup(self) -> str:
        """
        Get: AuthorizedWindowsGroup(self: WorkflowInstanceManagementElement) -> str
        Set: AuthorizedWindowsGroup(self: WorkflowInstanceManagementElement) = value
        """
        ...



class WorkflowUnhandledExceptionElement(BehaviorExtensionElement): # skipped bases: <type 'IConfigurationContextProviderInternal'>, <type 'object'>
    """ WorkflowUnhandledExceptionElement() """
    @property
    def Action(self) -> WorkflowUnhandledExceptionAction:
        """
        Get: Action(self: WorkflowUnhandledExceptionElement) -> WorkflowUnhandledExceptionAction
        Set: Action(self: WorkflowUnhandledExceptionElement) = value
        """
        ...



