# encoding: utf-8
# module Siemens.Engineering.HW.Systemdiagnostics.Settings calls itself Settings
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import IEngineeringObject, IEngineeringService

from System import Enum, IEquatable

from System.IO import FileInfo

"""The following names are not found in the module: (IInternalObjectAccess,
    field#)
"""

from Siemens import IInternalObjectAccess

# no functions
# classes

class SystemdiagnosticsSettingsDataProvider(IEquatable, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'object'>
    """ This class is used to export and import system diagnostics project relevant settings """
    def Export(self, filePath:FileInfo) -> SystemdiagnosticsSettingsExportImportResult:
        """
        Export(self: SystemdiagnosticsSettingsDataProvider, filePath: FileInfo) -> SystemdiagnosticsSettingsExportImportResult

            This method is used to export system diagnostics project relevant settings

            filePath: Path for system diagnostics settings export file

            Returns: Siemens.Engineering.HW.Systemdiagnostics.Settings.SystemdiagnosticsSettingsExportImportResult
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SystemdiagnosticsSettingsDataProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, filePath:FileInfo) -> SystemdiagnosticsSettingsExportImportResult:
        """
        Import(self: SystemdiagnosticsSettingsDataProvider, filePath: FileInfo) -> SystemdiagnosticsSettingsExportImportResult

            This method is used to import system diagnostics project relevant settings

            filePath: Path for system diagnostics settings import file

            Returns: Siemens.Engineering.HW.Systemdiagnostics.Settings.SystemdiagnosticsSettingsExportImportResult
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SystemdiagnosticsSettingsDataProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SystemdiagnosticsSettingsExportImportResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Result of an diagnostic class export or import """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SystemdiagnosticsSettingsExportImportResult) -> IEngineeringObject
        """
        ...

    @property
    def State(self) -> SystemdiagnosticsSettingsExportImportResultState:
        """
        Result state of the process

        Get: State(self: SystemdiagnosticsSettingsExportImportResult) -> SystemdiagnosticsSettingsExportImportResultState
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SystemdiagnosticsSettingsExportImportResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SystemdiagnosticsSettingsExportImportResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SystemdiagnosticsSettingsExportImportResultState(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Result state of system diagnostics settings export or import

    enum SystemdiagnosticsSettingsExportImportResultState, values: Error (2), Success (0), Warning (1)
    """
    Error: SystemdiagnosticsSettingsExportImportResultState = ...
    Success: SystemdiagnosticsSettingsExportImportResultState = ...
    value__ = ...
    Warning: SystemdiagnosticsSettingsExportImportResultState = ...
