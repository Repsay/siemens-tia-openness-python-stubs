# encoding: utf-8
# module Siemens.Engineering.VersionControl calls itself VersionControl
# from Siemens.Engineering, Version=16.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringComposition, IEngineeringObject,
    IEngineeringService, IEngineeringServiceProvider, MultilingualText)

from System import Enum, IEquatable

from System.IO import DirectoryInfo

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class CompareState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    Compare status

    enum CompareState, values: Equal (0), Unequal (1), Unknown (3), WorkspaceFileMissing (2)
    """
    Equal: CompareState = ...
    Unequal: CompareState = ...
    Unknown: CompareState = ...
    value__ = ...
    WorkspaceFileMissing: CompareState = ...


class IndividualObjectCompareDetails(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    Individual object compare details

    enum (flags) IndividualObjectCompareDetails, values: None (0), ProjectObjectChanged (1), WorkspaceFileChanged (2)
    """
    ProjectObjectChanged: IndividualObjectCompareDetails = ...
    value__ = ...
    WorkspaceFileChanged: IndividualObjectCompareDetails = ...


class IndividualObjectCompareResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Individual Object Compare Result """
    @property
    def CompareState(self) -> CompareState:
        """
        Compare state

        Get: CompareState(self: IndividualObjectCompareResult) -> CompareState
        """
        ...

    @property
    def IndividualObjectCompareDetails(self) -> IndividualObjectCompareDetails:
        """
        Individual object compare details

        Get: IndividualObjectCompareDetails(self: IndividualObjectCompareResult) -> IndividualObjectCompareDetails
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: IndividualObjectCompareResult) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: IndividualObjectCompareResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: IndividualObjectCompareResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class IndividualObjectSynchronizationStatus(IEquatable, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Individual object synchronization status """
    def GetHashCode(self) -> int:
        """
        GetHashCode(self: IndividualObjectSynchronizationStatus) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def GetStatus(self) -> IndividualObjectCompareResult:
        """
        GetStatus(self: IndividualObjectSynchronizationStatus) -> IndividualObjectCompareResult

            Get status of individual object

            Returns: Siemens.Engineering.VersionControl.IndividualObjectCompareResult
        """
        ...

    def Synchronize(self, synchronizationMode:SynchronizationMode): # ->
        """
        Synchronize(self: IndividualObjectSynchronizationStatus, synchronizationMode: SynchronizationMode)

            Sync differences

            synchronizationMode: Sync mode for sync action
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: IndividualObjectSynchronizationStatus) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def UpdateStatus(self): # ->
        """
        UpdateStatus(self: IndividualObjectSynchronizationStatus)

            Update mapping status
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SynchronizationMode(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    Describe the sync direction

    enum SynchronizationMode, values: ProjectToWorkspace (0), WorkspaceToProject (1)
    """
    ProjectToWorkspace: SynchronizationMode = ...
    value__ = ...
    WorkspaceToProject: SynchronizationMode = ...


class VersionControlInterface(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Service to access the WorkspaceSystemGroup """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: VersionControlInterface) -> IEngineeringObject
        """
        ...

    @property
    def WorkspaceGroup(self) -> WorkspaceSystemGroup:
        """
        Service to provide WorkspaceSystemGroup folder

        Get: WorkspaceGroup(self: VersionControlInterface) -> WorkspaceSystemGroup
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: VersionControlInterface) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: VersionControlInterface) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class Workspace(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents a VCI workspace """
    @property
    def Comment(self) -> MultilingualText:
        """
        The comment of the Workspace

        Get: Comment(self: Workspace) -> MultilingualText
        """
        ...

    @property
    def Mappings(self) -> WorkspaceMappingComposition:
        """
        Navigate to workspace entry

        Get: Mappings(self: Workspace) -> WorkspaceMappingComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the Workspace

        Get: Name(self: Workspace) -> str

        Set: Name(self: Workspace) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: Workspace) -> IEngineeringObject
        """
        ...

    @property
    def RootPath(self) -> DirectoryInfo:
        """
        The root path of the Workspace

        Get: RootPath(self: Workspace) -> DirectoryInfo

        Set: RootPath(self: Workspace) = value
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: Workspace)

            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: Workspace) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: Workspace) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class WorkspaceComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Collection of workspaces """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: WorkspaceComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> Workspace:
        """
        Find(self: WorkspaceComposition, name: str) -> Workspace

            Find a workspace

            name: The name of the workspace

            Returns: Siemens.Engineering.VersionControl.Workspace
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: WorkspaceComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: WorkspaceComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Workspace](enumerable: IEnumerable[Workspace], value: Workspace) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class WorkspaceGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Group containing Workspaces & Workspace user groups """
    @property
    def Groups(self) -> WorkspaceUserGroupComposition:
        """
        Navigate to user group

        Get: Groups(self: WorkspaceGroup) -> WorkspaceUserGroupComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: WorkspaceGroup) -> IEngineeringObject
        """
        ...

    @property
    def Workspaces(self) -> WorkspaceComposition:
        """
        Collection of workspaces

        Get: Workspaces(self: WorkspaceGroup) -> WorkspaceComposition
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: WorkspaceGroup)

            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: WorkspaceGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: WorkspaceGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class WorkspaceMapping(IEquatable, IEngineeringObject, IEngineeringServiceProvider, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IServiceProvider'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents a VCI workspace entry """
    @property
    def LinkedProjectObject(self) -> IEngineeringObject:
        """
        Linked object

        Get: LinkedProjectObject(self: WorkspaceMapping) -> IEngineeringObject
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: WorkspaceMapping) -> IEngineeringObject
        """
        ...

    @property
    def RelativeWorkspacePath(self) -> str:
        """
        The relative file path of the Workspace entry

        Get: RelativeWorkspacePath(self: WorkspaceMapping) -> str

        Set: RelativeWorkspacePath(self: WorkspaceMapping) = value
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: WorkspaceMapping)

            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: WorkspaceMapping) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: WorkspaceMapping) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class WorkspaceMappingComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Collection of Workspace entries """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: WorkspaceMappingComposition) -> IEngineeringObject
        """
        ...


    def Find(self, linkedProjectObject:IEngineeringObject) -> WorkspaceMapping:
        """
        Find(self: WorkspaceMappingComposition, linkedProjectObject: IEngineeringObject) -> WorkspaceMapping

            Find a workspace entry

            linkedProjectObject: Linked Object

            Returns: Siemens.Engineering.VersionControl.WorkspaceMapping
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: WorkspaceMappingComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: WorkspaceMappingComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[WorkspaceMapping](enumerable: IEnumerable[WorkspaceMapping], value: WorkspaceMapping) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class WorkspaceSystemGroup(WorkspaceGroup): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ The top folder for workspaces """
    @property
    def Name(self) -> str:
        """
        Name of the system group

        Get: Name(self: WorkspaceSystemGroup) -> str
        """
        ...



class WorkspaceUserGroup(WorkspaceGroup): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ User group for workspaces """
    @property
    def Name(self) -> str:
        """
        Name of the user group

        Get: Name(self: WorkspaceUserGroup) -> str

        Set: Name(self: WorkspaceUserGroup) = value
        """
        ...



class WorkspaceUserGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Collection of user groups """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: WorkspaceUserGroupComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> WorkspaceUserGroup:
        """
        Find(self: WorkspaceUserGroupComposition, name: str) -> WorkspaceUserGroup

            Find a user group

            name: The name of the user group

            Returns: Siemens.Engineering.VersionControl.WorkspaceUserGroup
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: WorkspaceUserGroupComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: WorkspaceUserGroupComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[WorkspaceUserGroup](enumerable: IEnumerable[WorkspaceUserGroup], value: WorkspaceUserGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
