# encoding: utf-8
# module Microsoft.SqlServer.Management.Sdk.Differencing calls itself Differencing
# from Microsoft.SqlServer.Management.Sdk.Sfc, Version=14.0.0.0, Culture=neutral, PublicKeyToken=89845dcd8080cc91
# by generator 1.145
""" no doc """
from __future__ import annotations
from Microsoft.SqlServer.Management.Sdk.Differencing.SPI import (
    ProviderRegistry)

from Microsoft.SqlServer.Management.Sdk.Sfc import Urn

from System import Enum

from System.Collections import IDictionary, IEnumerable

"""The following names are not found in the module: T, field#
"""

# no functions
# classes

class DifferencingService: # skipped bases: <type 'object'>, <type 'object'>
    """ no doc """
    @property
    def Service(self) -> DifferencingService:
        """ Get: Service() -> DifferencingService """
        ...


    def CreateDefaultRegistry(self) -> ProviderRegistry:
        """ CreateDefaultRegistry(self: DifferencingService) -> ProviderRegistry """
        ...

    def CreateDifferencer(self, registry:ProviderRegistry = ...) -> IDifferencer:
        """
        CreateDifferencer(self: DifferencingService) -> IDifferencer
        CreateDifferencer(self: DifferencingService, registry: ProviderRegistry) -> IDifferencer
        """
        ...



class DiffType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """ enum (flags) DiffType, values: Created (2), Deleted (4), Equivalent (1), None (0), Updated (8) """
    Created: DiffType = ...
    Deleted: DiffType = ...
    Equivalent: DiffType = ...
    Updated: DiffType = ...
    value__ = ...


class IDiffEntry: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def ChangeType(self) -> DiffType:
        """ Get: ChangeType(self: IDiffEntry) -> DiffType """
        ...

    @property
    def Properties(self) -> IDictionary:
        """ Get: Properties(self: IDiffEntry) -> IDictionary[str, IPair[object]] """
        ...

    @property
    def Source(self) -> Urn:
        """ Get: Source(self: IDiffEntry) -> Urn """
        ...

    @property
    def Target(self) -> Urn:
        """ Get: Target(self: IDiffEntry) -> Urn """
        ...



class IDifferencer: # skipped bases: <type 'object'>
    """ no doc """
    def CompareGraphs(self, source:object, target:object) -> IDiffgram:
        """ CompareGraphs(self: IDifferencer, source: object, target: object) -> IDiffgram """
        ...

    def IsTypeEmitted(self, type:DiffType) -> bool:
        """ IsTypeEmitted(self: IDifferencer, type: DiffType) -> bool """
        ...

    def SetTypeEmitted(self, type:DiffType): # -> 
        """ SetTypeEmitted(self: IDifferencer, type: DiffType) """
        ...

    def UnsetTypeEmitted(self, type:DiffType): # -> 
        """ UnsetTypeEmitted(self: IDifferencer, type: DiffType) """
        ...


class IDiffgram(IEnumerable): # skipped bases: <type 'IEnumerable'>, <type 'object'>
    """ no doc """
    @property
    def SourceRoot(self) -> object:
        """ Get: SourceRoot(self: IDiffgram) -> object """
        ...

    @property
    def TargetRoot(self) -> object:
        """ Get: TargetRoot(self: IDiffgram) -> object """
        ...


    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[IDiffEntry](enumerable: IEnumerable[IDiffEntry], value: IDiffEntry) -> bool """
        ...


class IPair: # skipped bases: <type 'object'>
    """ no doc """
    @property
    def Source(self): # -> T
        """ Get: Source(self: IPair[T]) -> T """
        ...

    @property
    def Target(self): # -> T
        """ Get: Target(self: IPair[T]) -> T """
        ...



# variables with complex values

