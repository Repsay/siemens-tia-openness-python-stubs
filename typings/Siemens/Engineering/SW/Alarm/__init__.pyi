# encoding: utf-8
# module Siemens.Engineering.SW.Alarm calls itself Alarm
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringComposition, IEngineeringObject,
    IEngineeringService, ImportOptions)

from System import Enum, IEquatable

from System.Collections import IEnumerable

from System.IO import FileInfo

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class AlarmClassDataProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Common alarm classes """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: AlarmClassDataProvider) -> IEngineeringObject
        """
        ...


    def Export(self, path:FileInfo) -> AlarmClassExportImportResult:
        """
        Export(self: AlarmClassDataProvider, path: FileInfo) -> AlarmClassExportImportResult

            Exports common alarm classes to a file

            path: Path for alarm class export

            Returns: Siemens.Engineering.SW.Alarm.AlarmClassExportImportResult
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: AlarmClassDataProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path:FileInfo) -> AlarmClassExportImportResult:
        """
        Import(self: AlarmClassDataProvider, path: FileInfo) -> AlarmClassExportImportResult

            Imports common alarm classes from file

            path: Path to import common alarm classes from

            Returns: Siemens.Engineering.SW.Alarm.AlarmClassExportImportResult
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: AlarmClassDataProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AlarmClassExportImportResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Result of an alarm class export or import """
    @property
    def ErrorCount(self) -> int:
        """
        Number of errors occured during the process

        Get: ErrorCount(self: AlarmClassExportImportResult) -> int
        """
        ...

    @property
    def Messages(self) -> AlarmClassExportImportResultMessageComposition:
        """
        Messages of the alarm class export/import

        Get: Messages(self: AlarmClassExportImportResult) -> AlarmClassExportImportResultMessageComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: AlarmClassExportImportResult) -> IEngineeringObject
        """
        ...

    @property
    def State(self) -> AlarmClassExportImportResultState:
        """
        Result state of the process

        Get: State(self: AlarmClassExportImportResult) -> AlarmClassExportImportResultState
        """
        ...

    @property
    def WarningCount(self) -> int:
        """
        Number of warnings created during the process

        Get: WarningCount(self: AlarmClassExportImportResult) -> int
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: AlarmClassExportImportResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: AlarmClassExportImportResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AlarmClassExportImportResultMessage(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Messages generated during alarm class export/import """
    @property
    def Message(self) -> str:
        """
        Description of an error or warning

        Get: Message(self: AlarmClassExportImportResultMessage) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: AlarmClassExportImportResultMessage) -> IEngineeringObject
        """
        ...

    @property
    def State(self) -> AlarmClassExportImportResultState:
        """
        State of the message

        Get: State(self: AlarmClassExportImportResultMessage) -> AlarmClassExportImportResultState
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: AlarmClassExportImportResultMessage) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: AlarmClassExportImportResultMessage) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AlarmClassExportImportResultMessageComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Collection of alarm class export/import messages """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: AlarmClassExportImportResultMessageComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: AlarmClassExportImportResultMessageComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: AlarmClassExportImportResultMessageComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[AlarmClassExportImportResultMessage](enumerable: IEnumerable[AlarmClassExportImportResultMessage], value: AlarmClassExportImportResultMessage) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class AlarmClassExportImportResultState(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Result state of common alarm class export or import

    enum AlarmClassExportImportResultState, values: Error (2), Success (0), Warning (1)
    """
    Error: AlarmClassExportImportResultState = ...
    Success: AlarmClassExportImportResultState = ...
    value__ = ...
    Warning: AlarmClassExportImportResultState = ...


class PlcAlarmTextListProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Plc alarm text lists of the PLC or Unit. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Parent of this object, can be Plc or Unit.

        Get: Parent(self: PlcAlarmTextListProvider) -> IEngineeringObject
        """
        ...


    def ExportToXlsx(self, path:FileInfo, textLists:IEnumerable = ..., languages:IEnumerable = ...) -> TextListXlsxResult:
        """
        ExportToXlsx(self: PlcAlarmTextListProvider, path: FileInfo) -> TextListXlsxResult

            Exports text lists to xlsx file.

            path: Path of the xlsx file to be exported.

            Returns: Siemens.Engineering.SW.Alarm.TextListXlsxResult

        ExportToXlsx(self: PlcAlarmTextListProvider, path: FileInfo, textLists: IEnumerable[str], languages: IEnumerable[Language]) -> TextListXlsxResult
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcAlarmTextListProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ImportFromXlsx(self, path:FileInfo, importOptions:ImportOptions) -> TextListXlsxResult:
        """
        ImportFromXlsx(self: PlcAlarmTextListProvider, path: FileInfo, importOptions: ImportOptions) -> TextListXlsxResult

            Imports text lists from excel file.

            path: Path of the xlsx file to be imported.

            importOptions: Options for Import

            Returns: Siemens.Engineering.SW.Alarm.TextListXlsxResult
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcAlarmTextListProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcAlarmTextProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Access to alarm text of the PLC or Unit. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Parent of this object, can be Plc or Unit.

        Get: Parent(self: PlcAlarmTextProvider) -> IEngineeringObject
        """
        ...


    def ExportInstanceTextsToXlsx(self, path:FileInfo, languages:IEnumerable, options:PlcAlarmTextXlsxExportOption) -> PlcAlarmTextXlsxResult:
        """ ExportInstanceTextsToXlsx(self: PlcAlarmTextProvider, path: FileInfo, languages: IEnumerable[Language], options: PlcAlarmTextXlsxExportOption) -> PlcAlarmTextXlsxResult """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcAlarmTextProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ImportInstanceTextsFromXlsx(self, path:FileInfo, languages:IEnumerable) -> PlcAlarmTextXlsxResult:
        """ ImportInstanceTextsFromXlsx(self: PlcAlarmTextProvider, path: FileInfo, languages: IEnumerable[Language]) -> PlcAlarmTextXlsxResult """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcAlarmTextProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcAlarmTextXlsxExportOption(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Export content options.

    enum (flags) PlcAlarmTextXlsxExportOption, values: All (8), IncludeAdditionalTexts (2), IncludeAlarmClass (4), IncludeInfoText (1), None (0)
    """
    All: PlcAlarmTextXlsxExportOption = ...
    IncludeAdditionalTexts: PlcAlarmTextXlsxExportOption = ...
    IncludeAlarmClass: PlcAlarmTextXlsxExportOption = ...
    IncludeInfoText: PlcAlarmTextXlsxExportOption = ...
    value__ = ...


class PlcAlarmTextXlsxResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents an alarm text export or import result. """
    @property
    def LogFilePath(self) -> FileInfo:
        """
        Path to the log file.

        Get: LogFilePath(self: PlcAlarmTextXlsxResult) -> FileInfo
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: PlcAlarmTextXlsxResult) -> IEngineeringObject
        """
        ...

    @property
    def State(self) -> PlcAlarmTextXlsxResultState:
        """
        Final state of the alarm texts export or import result.

        Get: State(self: PlcAlarmTextXlsxResult) -> PlcAlarmTextXlsxResultState
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcAlarmTextXlsxResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcAlarmTextXlsxResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcAlarmTextXlsxResultState(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    The state of text lists export or import result.

    enum PlcAlarmTextXlsxResultState, values: Error (2), OK (0), Warning (1)
    """
    Error: PlcAlarmTextXlsxResultState = ...
    OK: PlcAlarmTextXlsxResultState = ...
    value__ = ...
    Warning: PlcAlarmTextXlsxResultState = ...


class TextListXlsxResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents a text lists export or import result. """
    @property
    def LogFilePath(self) -> FileInfo:
        """
        Path to the log file.

        Get: LogFilePath(self: TextListXlsxResult) -> FileInfo
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: TextListXlsxResult) -> IEngineeringObject
        """
        ...

    @property
    def State(self) -> TextListXlsxResultState:
        """
        Final state of the text lists export or import result.

        Get: State(self: TextListXlsxResult) -> TextListXlsxResultState
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TextListXlsxResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TextListXlsxResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TextListXlsxResultState(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    The state of text lists export or import result.

    enum TextListXlsxResultState, values: Error (2), OK (0), Warning (1)
    """
    Error: TextListXlsxResultState = ...
    OK: TextListXlsxResultState = ...
    value__ = ...
    Warning: TextListXlsxResultState = ...


# variables with complex values
