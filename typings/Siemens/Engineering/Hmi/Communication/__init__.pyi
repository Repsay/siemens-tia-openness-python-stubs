# encoding: utf-8
# module Siemens.Engineering.Hmi.Communication calls itself Communication
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
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

class Connection(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents a logical connection between an HMI device and a PLC device """
    @property
    def Name(self) -> str:
        """
        The name of the connection

        Get: Name(self: Connection) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: Connection) -> IEngineeringObject
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: Connection)

            Deletes this instance.
        """
        ...

    def Export(self, path:FileInfo, exportOptions:ExportOptions): # ->
        """
        Export(self: Connection, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a connection

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: Connection) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: Connection) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConnectionComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of Connections """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ConnectionComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> Connection:
        """
        Find(self: ConnectionComposition, name: str) -> Connection

            Finds a given connection

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Communication.Connection
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ConnectionComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path:FileInfo, importOptions:ImportOptions) -> IList:
        """
        Import(self: ConnectionComposition, path: FileInfo, importOptions: ImportOptions) -> IList[Connection]

            Simatic ML import of a connection

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Communication.Connection>
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ConnectionComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Connection](enumerable: IEnumerable[Connection], value: Connection) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
