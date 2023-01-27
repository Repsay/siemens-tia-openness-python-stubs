# encoding: utf-8
# module Siemens.Engineering.Hmi.Globalization calls itself Globalization
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (ExportOptions, IEngineeringComposition,
    IEngineeringObject, ImportOptions)

from System import IEquatable

from System.Collections import IList

from System.IO import FileInfo

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class MultiLingualGraphic(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a multilingual graphic object of the project """
    @property
    def Name(self) -> str:
        """
        The name of the multilingual graphic

        Get: Name(self: MultiLingualGraphic) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: MultiLingualGraphic) -> IEngineeringObject
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: MultiLingualGraphic)

            Deletes this instance.
        """
        ...

    def Export(self, path:FileInfo, exportOptions:ExportOptions): # ->
        """
        Export(self: MultiLingualGraphic, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a multilingual graphic

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: MultiLingualGraphic) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: MultiLingualGraphic) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MultiLingualGraphicComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of MultiLingualGraphics """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: MultiLingualGraphicComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> MultiLingualGraphic:
        """
        Find(self: MultiLingualGraphicComposition, name: str) -> MultiLingualGraphic

            Finds a given multilingual graphic

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Globalization.MultiLingualGraphic
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: MultiLingualGraphicComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path:FileInfo, importOptions:ImportOptions) -> IList:
        """
        Import(self: MultiLingualGraphicComposition, path: FileInfo, importOptions: ImportOptions) -> IList[MultiLingualGraphic]

            Simatic ML import of a multilingual graphic

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Globalization.MultiLingualGraphic>
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: MultiLingualGraphicComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MultiLingualGraphic](enumerable: IEnumerable[MultiLingualGraphic], value: MultiLingualGraphic) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
