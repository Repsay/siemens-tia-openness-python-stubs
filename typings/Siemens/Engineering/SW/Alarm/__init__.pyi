# encoding: utf-8
# module Siemens.Engineering.SW.Alarm calls itself Alarm
# from Siemens.Engineering, Version=16.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringObject, IEngineeringService,
    ImportOptions)

from System import Enum, IEquatable

from System.Collections import IEnumerable

from System.IO import FileInfo

"""The following names are not found in the module: (IInternalObjectAccess,
    field#)
"""

from Siemens import IInternalObjectAccess

# no functions
# classes

class PlcAlarmTextListProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
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


class PlcAlarmTextProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
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


class PlcAlarmTextXlsxExportOption(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    Export content options.

    enum (flags) PlcAlarmTextXlsxExportOption, values: All (8), IncludeAdditionalTexts (2), IncludeAlarmClass (4), IncludeInfoText (1), None (0)
    """
    All: PlcAlarmTextXlsxExportOption = ...
    IncludeAdditionalTexts: PlcAlarmTextXlsxExportOption = ...
    IncludeAlarmClass: PlcAlarmTextXlsxExportOption = ...
    IncludeInfoText: PlcAlarmTextXlsxExportOption = ...
    value__ = ...


class PlcAlarmTextXlsxResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
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


class PlcAlarmTextXlsxResultState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    The state of text lists export or import result.

    enum PlcAlarmTextXlsxResultState, values: Error (2), OK (0), Warning (1)
    """
    Error: PlcAlarmTextXlsxResultState = ...
    OK: PlcAlarmTextXlsxResultState = ...
    value__ = ...
    Warning: PlcAlarmTextXlsxResultState = ...


class TextListXlsxResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
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


class TextListXlsxResultState(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    The state of text lists export or import result.

    enum TextListXlsxResultState, values: Error (2), OK (0), Warning (1)
    """
    Error: TextListXlsxResultState = ...
    OK: TextListXlsxResultState = ...
    value__ = ...
    Warning: TextListXlsxResultState = ...
