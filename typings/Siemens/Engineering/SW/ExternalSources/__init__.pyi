# encoding: utf-8
# module Siemens.Engineering.SW.ExternalSources calls itself ExternalSources
# from Siemens.Engineering, Version=16.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import IEngineeringComposition, IEngineeringObject

from Siemens.Engineering.Library.MasterCopies import (IMasterCopySource,
    MasterCopy)

from System import Enum, IEquatable

from System.Collections import IEnumerable, IList

from System.IO import FileInfo

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class GenerateBlockOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    Lists the possible options for block generation from source

    enum GenerateBlockOption, values: KeepOnError (1), None (0)
    """
    KeepOnError: GenerateBlockOption = ...
    value__ = ...


class GenerateOptions(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    Options for source generation

    enum GenerateOptions, values: None (0), WithDependencies (1)
    """
    value__ = ...
    WithDependencies: GenerateOptions = ...


class IGenerateSource: # skipped bases: <type 'object'>
    """ Can generate source. """
    pass

class PlcExternalSource(IEquatable, IEngineeringObject, IMasterCopySource, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents a Plc external source """
    @property
    def Name(self) -> str:
        """
        The name of the Plc external source

        Get: Name(self: PlcExternalSource) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: PlcExternalSource) -> IEngineeringObject
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: PlcExternalSource)

            Deletes this instance.
        """
        ...

    def GenerateBlocksFromSource(self, generateBlockOption:GenerateBlockOption = ...) -> IList:
        """
        GenerateBlocksFromSource(self: PlcExternalSource)

            Creates a block or blocks from the current source file object

        GenerateBlocksFromSource(self: PlcExternalSource, generateBlockOption: GenerateBlockOption) -> IList[IEngineeringObject]

            Creates a block or blocks from the current source file object

            generateBlockOption: Option to use for block generation from source

            Returns: System.Collections.Generic.IList<Siemens.Engineering.IEngineeringObject>
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcExternalSource) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcExternalSource) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcExternalSourceComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of PlcExternalSources """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: PlcExternalSourceComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy:MasterCopy) -> PlcExternalSource:
        """
        CreateFrom(self: PlcExternalSourceComposition, sourceMasterCopy: MasterCopy) -> PlcExternalSource

            Create External Source from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSource
        """
        ...

    def CreateFromFile(self, name:str, path:str) -> PlcExternalSource:
        """
        CreateFromFile(self: PlcExternalSourceComposition, name: str, path: str) -> PlcExternalSource

            Create an external source from a specified file

            name: Name of Plc external source to be created

            path: Path to the external source file

            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSource
        """
        ...

    def Find(self, name:str) -> PlcExternalSource:
        """
        Find(self: PlcExternalSourceComposition, name: str) -> PlcExternalSource

            Finds a given Plc external source

            name: Name to find

            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSource
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcExternalSourceComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcExternalSourceComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcExternalSource](enumerable: IEnumerable[PlcExternalSource], value: PlcExternalSource) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcExternalSourceGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Group containing Plc external sources & Plc external source user groups """
    @property
    def ExternalSources(self) -> PlcExternalSourceComposition:
        """
        Composition of Plc external sources

        Get: ExternalSources(self: PlcExternalSourceGroup) -> PlcExternalSourceComposition
        """
        ...

    @property
    def Groups(self) -> PlcExternalSourceUserGroupComposition:
        """
        Composition of Plc external source user groups

        Get: Groups(self: PlcExternalSourceGroup) -> PlcExternalSourceUserGroupComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the Plc external source group

        Get: Name(self: PlcExternalSourceGroup) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: PlcExternalSourceGroup) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcExternalSourceGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcExternalSourceGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcExternalSourceSystemGroup(PlcExternalSourceGroup): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ System group containing Plc external sources & Plc external source user groups """
    def GenerateSource(self, blocks:IEnumerable, sourceFile:FileInfo, generateOption:GenerateOptions = ...): # ->
        """ GenerateSource(self: PlcExternalSourceSystemGroup, blocks: IEnumerable[IGenerateSource], sourceFile: FileInfo)GenerateSource(self: PlcExternalSourceSystemGroup, blocks: IEnumerable[IGenerateSource], sourceFile: FileInfo, generateOption: GenerateOptions) """
        ...


class PlcExternalSourceUserGroup(PlcExternalSourceGroup): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ User group containing Plc external sources & Plc external source user groups """
    def Delete(self): # ->
        """
        Delete(self: PlcExternalSourceUserGroup)

            Deletes this instance.
        """
        ...


class PlcExternalSourceUserGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of PlcExternalSourceUserGroups """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: PlcExternalSourceUserGroupComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy:MasterCopy) -> PlcExternalSourceUserGroup:
        """
        CreateFrom(self: PlcExternalSourceUserGroupComposition, sourceMasterCopy: MasterCopy) -> PlcExternalSourceUserGroup

            Create ExternalSourceUserGroup from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSourceUserGroup
        """
        ...

    def Find(self, name:str) -> PlcExternalSourceUserGroup:
        """
        Find(self: PlcExternalSourceUserGroupComposition, name: str) -> PlcExternalSourceUserGroup

            Finds a given Plc external source user group

            name: Name to find

            Returns: Siemens.Engineering.SW.ExternalSources.PlcExternalSourceUserGroup
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcExternalSourceUserGroupComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcExternalSourceUserGroupComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcExternalSourceUserGroup](enumerable: IEnumerable[PlcExternalSourceUserGroup], value: PlcExternalSourceUserGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
