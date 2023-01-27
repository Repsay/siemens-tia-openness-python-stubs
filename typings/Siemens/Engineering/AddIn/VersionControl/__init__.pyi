# encoding: utf-8
# module Siemens.Engineering.AddIn.VersionControl calls itself VersionControl
# from Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import IEngineeringObject

from Siemens.Engineering.VersionControl import WorkspaceMapping, Workspace

from System import Enum, IDisposable, IEquatable

from System.Collections import IEnumerable

from System.IO import DirectoryInfo, FileInfo

from Siemens import IInternalObjectAccess

"""The following names are not found in the module: (IInternalObjectAccess,
    field#)
"""

# no functions
# classes

class ExportResult(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Result of export indicating whether the export was successful

    enum ExportResult, values: Aborted (2), Failed (1), Succeeded (0)
    """
    Aborted: ExportResult = ...
    Failed: ExportResult = ...
    Succeeded: ExportResult = ...
    value__ = ...


class ExportStatus(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Export status

    enum ExportStatus, values: Failed (1), Skipped (2), Succeeded (0)
    """
    Failed: ExportStatus = ...
    Skipped: ExportStatus = ...
    Succeeded: ExportStatus = ...
    value__ = ...


class InitialPostExportInfo(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Info object passed to VCI repository add-ins during synchronization post-export """
    @property
    def ExportStatus(self) -> ExportStatus:
        """
        Status of an export on an individual item. Indicates whether the export on the item succeeded, failed, or was skipped.

        Get: ExportStatus(self: InitialPostExportInfo) -> ExportStatus
        """
        ...

    @property
    def FileToExportTo(self) -> FileInfo:
        """
        File on disk which is the result of the export to workspace

        Get: FileToExportTo(self: InitialPostExportInfo) -> FileInfo
        """
        ...

    @property
    def ObjectToExport(self) -> IEngineeringObject:
        """
        Object to export from TIA Portal

        Get: ObjectToExport(self: InitialPostExportInfo) -> IEngineeringObject
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: InitialPostExportInfo) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: InitialPostExportInfo) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: InitialPostExportInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class InitialPreExportInfo(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Info object passed to VCI repository add-ins during drag/drop pre-export """
    @property
    def FileToExportTo(self) -> FileInfo:
        """
        File on disk which is the result of the export to workspace

        Get: FileToExportTo(self: InitialPreExportInfo) -> FileInfo
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: InitialPreExportInfo) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: InitialPreExportInfo) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: InitialPreExportInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SyncPostExportInfo(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Info object passed to VCI repository add-ins during synchronization post-export """
    @property
    def ExportStatus(self) -> ExportStatus:
        """
        Status of an export on an individual item. Indicates whether the export on the item succeeded, failed, or was skipped

        Get: ExportStatus(self: SyncPostExportInfo) -> ExportStatus
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SyncPostExportInfo) -> IEngineeringObject
        """
        ...

    @property
    def WorkspaceEntry(self) -> WorkspaceMapping:
        """
        Workspace entry for an individual item

        Get: WorkspaceEntry(self: SyncPostExportInfo) -> WorkspaceMapping
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SyncPostExportInfo) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SyncPostExportInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SyncPreExportInfo(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Info object passed to VCI repository add-ins during synchronization pre-export """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SyncPreExportInfo) -> IEngineeringObject
        """
        ...

    @property
    def WorkspaceEntry(self) -> WorkspaceMapping:
        """
        Workspace entry for an individual item

        Get: WorkspaceEntry(self: SyncPreExportInfo) -> WorkspaceMapping
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SyncPreExportInfo) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SyncPreExportInfo) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class VciEditorAddInProvider(IDisposable): # skipped bases: <type 'object'>
    """ Provides custom addins for Vci workspace view """
    def GetVciWorkspaceViewAddInProvider(self) -> VciWorkspaceViewAddInProvider:
        """
        GetVciWorkspaceViewAddInProvider(self: VciEditorAddInProvider) -> VciWorkspaceViewAddInProvider

            Provides custom addins for Vci workspace view

            Returns: VciWorkspaceViewAddInProvider
        """
        ...


class VciInitialExportAddInContext(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Context object used by VCI to provide the user's currently configured workspace to the VCI repository add-in """
    @property
    def CurrentWorkspace(self) -> Workspace:
        """
        The user's currently configured VCI workspace

        Get: CurrentWorkspace(self: VciInitialExportAddInContext) -> Workspace
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: VciInitialExportAddInContext) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: VciInitialExportAddInContext) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: VciInitialExportAddInContext) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class VciInitialExportSupport(IDisposable): # skipped bases: <type 'object'>
    """ Support for AddIn actions during initial export. """
    def PostExportExecute(self, itemsToExport:IEnumerable, vciInitialExportAddInContext:VciInitialExportAddInContext) -> ExportResult:
        """ PostExportExecute(self: VciInitialExportSupport, itemsToExport: IEnumerable[InitialPostExportInfo], vciInitialExportAddInContext: VciInitialExportAddInContext) -> ExportResult """
        ...

    def PreExportExecute(self, itemsToExport:IEnumerable, vciInitialExportAddInContext:VciInitialExportAddInContext) -> ExportResult:
        """ PreExportExecute(self: VciInitialExportSupport, itemsToExport: IEnumerable[InitialPreExportInfo], vciInitialExportAddInContext: VciInitialExportAddInContext) -> ExportResult """
        ...


class VciRepositoryAddIn: # skipped bases: <type 'object'>, <type 'object'>
    """  """
    @property
    def DisplayName(self) -> str:
        """ Get: DisplayName(self: VciRepositoryAddIn) -> str """
        ...


    def GetVciWorkflowAddInSupport(self) -> VciWorkflowAddInSupport:
        """ GetVciWorkflowAddInSupport(self: VciRepositoryAddIn) -> VciWorkflowAddInSupport """
        ...

    def GetVciWorkspaceViewAddInProvider(self) -> VciWorkspaceViewAddInProvider:
        """ GetVciWorkspaceViewAddInProvider(self: VciRepositoryAddIn) -> VciWorkspaceViewAddInProvider """
        ...


class VciRepositoryAddInProvider(IDisposable): # skipped bases: <type 'object'>
    """ Provides custom repository addins """
    def GetVciRepositoryAddIns(self) -> IEnumerable:
        """
        GetVciRepositoryAddIns(self: VciRepositoryAddInProvider) -> IEnumerable[VciRepositoryAddIn]

            Provides custom repository addins

            Returns: VciRepositoryAddins
        """
        ...


class VciSyncExportAddInContext(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Context object used by VCI to provide the user's currently configured workspace to the VCI repository add-in """
    @property
    def CurrentWorkspace(self) -> Workspace:
        """
        The user's currently configured VCI workspace

        Get: CurrentWorkspace(self: VciSyncExportAddInContext) -> Workspace
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: VciSyncExportAddInContext) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: VciSyncExportAddInContext) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: VciSyncExportAddInContext) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class VciSyncExportSupport(IDisposable): # skipped bases: <type 'object'>
    """
    Support for AddIn actions during sync export.

    VciSyncExportSupport()
    """
    def PostExportExecute(self, itemsToExport:IEnumerable, vciSyncExportAddInContext:VciSyncExportAddInContext) -> ExportResult:
        """ PostExportExecute(self: VciSyncExportSupport, itemsToExport: IEnumerable[SyncPostExportInfo], vciSyncExportAddInContext: VciSyncExportAddInContext) -> ExportResult """
        ...

    def PreExportExecute(self, itemsToExport:IEnumerable, vciSyncExportAddInContext:VciSyncExportAddInContext) -> ExportResult:
        """ PreExportExecute(self: VciSyncExportSupport, itemsToExport: IEnumerable[SyncPreExportInfo], vciSyncExportAddInContext: VciSyncExportAddInContext) -> ExportResult """
        ...


class VciWorkflowAddInSupport: # skipped bases: <type 'object'>, <type 'object'>
    """  """
    def CreateInitialExportSupport(self) -> VciInitialExportSupport:
        """ CreateInitialExportSupport(self: VciWorkflowAddInSupport) -> VciInitialExportSupport """
        ...

    def CreateSyncExportSupport(self) -> VciSyncExportSupport:
        """ CreateSyncExportSupport(self: VciWorkflowAddInSupport) -> VciSyncExportSupport """
        ...


class VciWorkspaceViewAddInProvider(IDisposable): # skipped bases: <type 'object'>
    """ Provides custom contextMenus on Vci workspace view """
    def GetContextMenuAddIns(self) -> IEnumerable:
        """
        GetContextMenuAddIns(self: VciWorkspaceViewAddInProvider) -> IEnumerable[ContextMenuAddIn]

            Provides custom contextMenus on Vci workspace view

            Returns: ContextMenuAddIn
        """
        ...


class WorkspaceFile(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents """
    @property
    def FileInfo(self) -> FileInfo:
        """
        The full file path of a file in the VCI workspace

        Get: FileInfo(self: WorkspaceFile) -> FileInfo
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: WorkspaceFile) -> IEngineeringObject
        """
        ...

    @property
    def Workspace(self) -> Workspace:
        """
        Represents a VCI workspace

        Get: Workspace(self: WorkspaceFile) -> Workspace
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: WorkspaceFile) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: WorkspaceFile) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class WorkspaceFolder(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents a subfolder browsable in the workspace view """
    @property
    def DirectoryInfo(self) -> DirectoryInfo:
        """
        Represents a directory in the VCI workspace

        Get: DirectoryInfo(self: WorkspaceFolder) -> DirectoryInfo
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: WorkspaceFolder) -> IEngineeringObject
        """
        ...

    @property
    def Workspace(self) -> Workspace:
        """
        Represents a VCI workspace

        Get: Workspace(self: WorkspaceFolder) -> Workspace
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: WorkspaceFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: WorkspaceFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
