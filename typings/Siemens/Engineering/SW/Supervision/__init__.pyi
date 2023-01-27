# encoding: utf-8
# module Siemens.Engineering.SW.Supervision calls itself Supervision
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringComposition, IEngineeringObject,
    IEngineeringService, ImportOptions)

from System import Enum, IEquatable

from System.IO import FileInfo

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class SupervisionProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ prodiag global supervision provider of proDiagFB """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SupervisionProvider) -> IEngineeringObject
        """
        ...


    def ExportSupervisionsToXlsx(self, path:FileInfo) -> SupervisionXlsxResult:
        """
        ExportSupervisionsToXlsx(self: SupervisionProvider, path: FileInfo) -> SupervisionXlsxResult

            Export of prodiag global supervisions to xlsx file

            path: path for exported prodiag global supervisions

            Returns: Siemens.Engineering.SW.Supervision.SupervisionXlsxResult
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SupervisionProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ImportSupervisionSettingsFromXlsx(self, path:FileInfo, importOptions:ImportOptions) -> SupervisionXlsxResult:
        """
        ImportSupervisionSettingsFromXlsx(self: SupervisionProvider, path: FileInfo, importOptions: ImportOptions) -> SupervisionXlsxResult

            Import of prodiag settings from xlsx file

            path: path of xlsx file

            importOptions: option to select type of import

            Returns: Siemens.Engineering.SW.Supervision.SupervisionXlsxResult
        """
        ...

    def ImportSupervisionsFromXlsx(self, path:FileInfo, importOptions:ImportOptions) -> SupervisionXlsxResult:
        """
        ImportSupervisionsFromXlsx(self: SupervisionProvider, path: FileInfo, importOptions: ImportOptions) -> SupervisionXlsxResult

            Import of prodiag global supervisions from xlsx file

            path: path from where prodiag global supervisions gets imported

            importOptions: option to select type of import

            Returns: Siemens.Engineering.SW.Supervision.SupervisionXlsxResult
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SupervisionProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SupervisionSettingsExportImportResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents supervision settings export/import final result. """
    @property
    def ErrorCount(self) -> int:
        """
        Error count after export/import of supervision settings

        Get: ErrorCount(self: SupervisionSettingsExportImportResult) -> int
        """
        ...

    @property
    def Messages(self) -> SupervisionSettingsExportImportResultMessageComposition:
        """
        List of supervision settings export/import messages

        Get: Messages(self: SupervisionSettingsExportImportResult) -> SupervisionSettingsExportImportResultMessageComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SupervisionSettingsExportImportResult) -> IEngineeringObject
        """
        ...

    @property
    def State(self) -> SupervisionSettingsExportImportResultState:
        """
        Final state of the supervision settings export/import result.

        Get: State(self: SupervisionSettingsExportImportResult) -> SupervisionSettingsExportImportResultState
        """
        ...

    @property
    def WarningCount(self) -> int:
        """
        Warning count after import of supervision settings

        Get: WarningCount(self: SupervisionSettingsExportImportResult) -> int
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SupervisionSettingsExportImportResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SupervisionSettingsExportImportResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SupervisionSettingsExportImportResultMessage(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents supervision settings export/import final result message """
    @property
    def Message(self) -> str:
        """
        Final message text of supervision settings export/import result.

        Get: Message(self: SupervisionSettingsExportImportResultMessage) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SupervisionSettingsExportImportResultMessage) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SupervisionSettingsExportImportResultMessage) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SupervisionSettingsExportImportResultMessage) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SupervisionSettingsExportImportResultMessageComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of SupervisionSettingsExportImportResultMessage """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: SupervisionSettingsExportImportResultMessageComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SupervisionSettingsExportImportResultMessageComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SupervisionSettingsExportImportResultMessageComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SupervisionSettingsExportImportResultMessage](enumerable: IEnumerable[SupervisionSettingsExportImportResultMessage], value: SupervisionSettingsExportImportResultMessage) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SupervisionSettingsExportImportResultState(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    The state of supervision settings export/import result

    enum SupervisionSettingsExportImportResultState, values: ErrorRollback (1), Success (0)
    """
    ErrorRollback: SupervisionSettingsExportImportResultState = ...
    Success: SupervisionSettingsExportImportResultState = ...
    value__ = ...


class SupervisionSettingsProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Provider for supervision settings """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SupervisionSettingsProvider) -> IEngineeringObject
        """
        ...


    def Export(self, filePath:FileInfo) -> SupervisionSettingsExportImportResult:
        """
        Export(self: SupervisionSettingsProvider, filePath: FileInfo) -> SupervisionSettingsExportImportResult

            Exports supervision settings in DAT file format

            filePath: File path where file having .dat extension is exported

            Returns: Siemens.Engineering.SW.Supervision.SupervisionSettingsExportImportResult
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SupervisionSettingsProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, filePath:FileInfo) -> SupervisionSettingsExportImportResult:
        """
        Import(self: SupervisionSettingsProvider, filePath: FileInfo) -> SupervisionSettingsExportImportResult

            Imports supervision settings from DAT file

            filePath: File path where file having .dat extension is imported

            Returns: Siemens.Engineering.SW.Supervision.SupervisionSettingsExportImportResult
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SupervisionSettingsProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SupervisionXlsxResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents a supervision export or import result. """
    @property
    def LogFilePath(self) -> FileInfo:
        """
        Path to the log file.

        Get: LogFilePath(self: SupervisionXlsxResult) -> FileInfo
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SupervisionXlsxResult) -> IEngineeringObject
        """
        ...

    @property
    def State(self) -> SupervisionXlsxResultState:
        """
        Final state of the supervision export or import result.

        Get: State(self: SupervisionXlsxResult) -> SupervisionXlsxResultState
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: SupervisionXlsxResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: SupervisionXlsxResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SupervisionXlsxResultState(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Supervision import/export result state

    enum SupervisionXlsxResultState, values: Failure (1), Success (0)
    """
    Failure: SupervisionXlsxResultState = ...
    Success: SupervisionXlsxResultState = ...
    value__ = ...
