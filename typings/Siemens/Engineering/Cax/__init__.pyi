# encoding: utf-8
# module Siemens.Engineering.Cax calls itself Cax
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import IEngineeringObject, IEngineeringService

from Siemens.Engineering.HW import Device

from System import Enum, IEquatable

from System.IO import FileInfo

"""The following names are not found in the module: (IInternalObjectAccess,
    field#)
"""

from Siemens import IInternalObjectAccess

# no functions
# classes

class CaxImportOptions(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Cax Import Merge options

    enum CaxImportOptions, values: MoveToParkingLot (0), OverwriteTiaDevice (1), RetainTiaDevice (2)
    """
    MoveToParkingLot: CaxImportOptions = ...
    OverwriteTiaDevice: CaxImportOptions = ...
    RetainTiaDevice: CaxImportOptions = ...
    value__ = ...


class CaxProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Service Provider for CAx Export/Import operations """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: CaxProvider) -> IEngineeringObject
        """
        ...


    def Export(self, *__args) -> bool:
        """
        Export(self: CaxProvider, deviceToExport: Device, exportFilePath: FileInfo, logFilePath: FileInfo) -> bool

            Command to CAx Export at Device level

            deviceToExport: Device to Export

            exportFilePath: Export file path

            logFilePath: Log file path

            Returns: System.Boolean

        Export(self: CaxProvider, projectToExport: Project, exportFilePath: FileInfo, logFilePath: FileInfo) -> bool

            Command to CAx Export at Project level

            projectToExport: Project to Export

            exportFilePath: Export file Path

            logFilePath: Log file Path

            Returns: System.Boolean

        Export(self: CaxProvider, projectToExport: ProjectBase, exportFilePath: FileInfo, logFilePath: FileInfo) -> bool

            Command to CAx Export at Single/Multi user Project level

            projectToExport: Project to Export. Project can be single user or Multi-user.

            exportFilePath: Export file Path

            logFilePath: Log file Path

            Returns: System.Boolean
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CaxProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, importFilePath:FileInfo, logFilePath:FileInfo, importOption:CaxImportOptions) -> bool:
        """
        Import(self: CaxProvider, importFilePath: FileInfo, logFilePath: FileInfo, importOption: CaxImportOptions) -> bool

            Command to CAx Import

            importFilePath: Import file path

            logFilePath: Log file path

            importOption: Cax Import Merge options

            Returns: System.Boolean
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CaxProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
