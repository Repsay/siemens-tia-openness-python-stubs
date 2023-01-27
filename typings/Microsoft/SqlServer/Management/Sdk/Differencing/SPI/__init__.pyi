# encoding: utf-8
# module Microsoft.SqlServer.Management.Sdk.Differencing.SPI calls itself SPI
# from Microsoft.SqlServer.Management.Sdk.Sfc, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Sdk.Sfc import (ISfcSimpleList, 
    ISfcSimpleNode)

from System.Collections import ICollection, IComparer, IEnumerable

from typing import Tuple as Tuple_


# no functions
# classes

class AvailablePropertyValueProvider(Provider): # skipped bases: <type 'object'>
    """ no doc """
    def IsGraphSupported(self, node:ISfcSimpleNode) -> bool:
        """ IsGraphSupported(self: AvailablePropertyValueProvider, node: ISfcSimpleNode) -> bool """
        ...

    def IsValueAvailable(self, node:ISfcSimpleNode, propName:str) -> bool:
        """ IsValueAvailable(self: AvailablePropertyValueProvider, node: ISfcSimpleNode, propName: str) -> bool """
        ...


class ContainerSortingProvider(Provider): # skipped bases: <type 'object'>
    """ no doc """
    def AreGraphsSupported(self, source:ISfcSimpleNode, target:ISfcSimpleNode) -> bool:
        """ AreGraphsSupported(self: ContainerSortingProvider, source: ISfcSimpleNode, target: ISfcSimpleNode) -> bool """
        ...

    def GetComparer(self, list:ISfcSimpleList, list2:ISfcSimpleList) -> IComparer:
        """ GetComparer(self: ContainerSortingProvider, list: ISfcSimpleList, list2: ISfcSimpleList) -> IComparer[ISfcSimpleNode] """
        ...

    def SortLists(self, source, target, sortedSource, sortedTarget) -> Tuple_[IEnumerable, IEnumerable]:
        """ SortLists(self: ContainerSortingProvider, source: ISfcSimpleList, target: ISfcSimpleList) -> (IEnumerable[ISfcSimpleNode], IEnumerable[ISfcSimpleNode]) """
        ...


class NodeItemNamesAdapterProvider(Provider): # skipped bases: <type 'object'>
    """ no doc """
    def GetPropertyNames(self, node:ISfcSimpleNode) -> IEnumerable:
        """ GetPropertyNames(self: NodeItemNamesAdapterProvider, node: ISfcSimpleNode) -> IEnumerable[str] """
        ...

    def GetRelatedContainerNames(self, node:ISfcSimpleNode) -> IEnumerable:
        """ GetRelatedContainerNames(self: NodeItemNamesAdapterProvider, node: ISfcSimpleNode) -> IEnumerable[str] """
        ...

    def GetRelatedObjectNames(self, node:ISfcSimpleNode) -> IEnumerable:
        """ GetRelatedObjectNames(self: NodeItemNamesAdapterProvider, node: ISfcSimpleNode) -> IEnumerable[str] """
        ...

    def IsContainerInNatrualOrder(self, node:ISfcSimpleNode, name:str) -> bool:
        """ IsContainerInNatrualOrder(self: NodeItemNamesAdapterProvider, node: ISfcSimpleNode, name: str) -> bool """
        ...

    def IsGraphSupported(self, node:ISfcSimpleNode) -> bool:
        """ IsGraphSupported(self: NodeItemNamesAdapterProvider, node: ISfcSimpleNode) -> bool """
        ...


class MetadataNodeItemNamesProvider(NodeItemNamesAdapterProvider): # skipped bases: <type 'Provider'>, <type 'object'>
    """ MetadataNodeItemNamesProvider() """
    pass

class PropertyComparerProvider(Provider): # skipped bases: <type 'object'>
    """ no doc """
    def AreGraphsSupported(self, source:ISfcSimpleNode, target:ISfcSimpleNode) -> bool:
        """ AreGraphsSupported(self: PropertyComparerProvider, source: ISfcSimpleNode, target: ISfcSimpleNode) -> bool """
        ...

    def Compare(self, source:ISfcSimpleNode, target:ISfcSimpleNode, propName:str) -> bool:
        """ Compare(self: PropertyComparerProvider, source: ISfcSimpleNode, target: ISfcSimpleNode, propName: str) -> bool """
        ...


class Provider: # skipped bases: <type 'object'>
    """ no doc """
    pass

class ProviderRegistry: # skipped bases: <type 'object'>, <type 'object'>
    """ ProviderRegistry() """
    @property
    def AvailablePropertyValueProviders(self) -> ICollection:
        """ Get: AvailablePropertyValueProviders(self: ProviderRegistry) -> ICollection[AvailablePropertyValueProvider] """
        ...

    @property
    def ContainerSortingProviders(self) -> ICollection:
        """ Get: ContainerSortingProviders(self: ProviderRegistry) -> ICollection[ContainerSortingProvider] """
        ...

    @property
    def NodeItemNameAdapterProviders(self) -> ICollection:
        """ Get: NodeItemNameAdapterProviders(self: ProviderRegistry) -> ICollection[NodeItemNamesAdapterProvider] """
        ...

    @property
    def PropertyComparerProviders(self) -> ICollection:
        """ Get: PropertyComparerProviders(self: ProviderRegistry) -> ICollection[PropertyComparerProvider] """
        ...

    @property
    def SfcNodeAdapterProviders(self) -> ICollection:
        """ Get: SfcNodeAdapterProviders(self: ProviderRegistry) -> ICollection[SfcNodeAdapterProvider] """
        ...


    def RegisterProvider(self, provider:SfcNodeAdapterProvider) -> bool:
        """
        RegisterProvider(self: ProviderRegistry, provider: SfcNodeAdapterProvider) -> bool
        RegisterProvider(self: ProviderRegistry, provider: AvailablePropertyValueProvider) -> bool
        RegisterProvider(self: ProviderRegistry, provider: PropertyComparerProvider) -> bool
        RegisterProvider(self: ProviderRegistry, provider: NodeItemNamesAdapterProvider) -> bool
        RegisterProvider(self: ProviderRegistry, provider: ContainerSortingProvider) -> bool
        """
        ...

    def UnregisterProvider(self, provider:SfcNodeAdapterProvider) -> bool:
        """
        UnregisterProvider(self: ProviderRegistry, provider: SfcNodeAdapterProvider) -> bool
        UnregisterProvider(self: ProviderRegistry, provider: AvailablePropertyValueProvider) -> bool
        UnregisterProvider(self: ProviderRegistry, provider: PropertyComparerProvider) -> bool
        UnregisterProvider(self: ProviderRegistry, provider: NodeItemNamesAdapterProvider) -> bool
        UnregisterProvider(self: ProviderRegistry, provider: ContainerSortingProvider) -> bool
        """
        ...


class SfcNodeAdapterProvider(Provider): # skipped bases: <type 'object'>
    """ no doc """
    def GetGraphAdapter(self, obj:object) -> ISfcSimpleNode:
        """ GetGraphAdapter(self: SfcNodeAdapterProvider, obj: object) -> ISfcSimpleNode """
        ...

    def IsGraphSupported(self, obj:object) -> bool:
        """ IsGraphSupported(self: SfcNodeAdapterProvider, obj: object) -> bool """
        ...


