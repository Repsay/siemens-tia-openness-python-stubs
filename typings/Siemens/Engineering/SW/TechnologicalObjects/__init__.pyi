# encoding: utf-8
# module Siemens.Engineering.SW.TechnologicalObjects calls itself TechnologicalObjects
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (ExportOptions, IEngineeringAssociation,
    IEngineeringComposition, IEngineeringObject, IEngineeringServiceProvider)

from Siemens.Engineering.Library.MasterCopies import MasterCopy

from Siemens.Engineering.SW.Blocks import InstanceDB

from System import IEquatable, Version

from System.IO import FileInfo

"""The following names are not found in the module: (
    IInternalAssociationAccess, IInternalCompositionAccess,
    IInternalObjectAccess)
"""

from Siemens import IInternalAssociationAccess, IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class TechnologicalInstanceDB(InstanceDB): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringServiceProvider'>, <type 'IServiceProvider'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IMasterCopySource'>, <type 'IGenerateSource'>, <type 'IInternalBaseAccess'>, <type 'IShowable'>, <type 'object'>
    """ Instance of a technological DB """
    @property
    def Name(self) -> str:
        """
        Name of the Block

        Get: Name(self: TechnologicalInstanceDB) -> str

        Set: Name(self: TechnologicalInstanceDB) = value
        """
        ...

    @property
    def OfSystemLibElement(self) -> str:
        """
        Gets the name of the system library element associated with the DB

        Get: OfSystemLibElement(self: TechnologicalInstanceDB) -> str
        """
        ...

    @property
    def OfSystemLibVersion(self) -> Version:
        """
        Gets the version of the system library element associated with the DB

        Get: OfSystemLibVersion(self: TechnologicalInstanceDB) -> Version

        Set: OfSystemLibVersion(self: TechnologicalInstanceDB) = value
        """
        ...

    @property
    def Parameters(self) -> TechnologicalParameterComposition:
        """
        Get all technological parameters

        Get: Parameters(self: TechnologicalInstanceDB) -> TechnologicalParameterComposition
        """
        ...


    def Export(self, path:FileInfo, exportOptions:ExportOptions): # ->
        """
        Export(self: TechnologicalInstanceDB, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a TechnlogicalInstanceDB

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...


class TechnologicalInstanceDBAssociation(IEquatable, IEngineeringAssociation, IInternalAssociationAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ TO Association """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent..

        Get: Parent(self: TechnologicalInstanceDBAssociation) -> IEngineeringObject
        """
        ...


    def Add(self, item:TechnologicalInstanceDB): # ->
        """
        Add(self: TechnologicalInstanceDBAssociation, item: TechnologicalInstanceDB)

            Adds an item.

            item: The item to be added.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TechnologicalInstanceDBAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Remove(self, item:TechnologicalInstanceDB) -> bool:
        """
        Remove(self: TechnologicalInstanceDBAssociation, item: TechnologicalInstanceDB) -> bool

            Removes an item.

            item: The item to be removed.

            Returns: true if the item was removed; otherwise false.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TechnologicalInstanceDBAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TechnologicalInstanceDB](enumerable: IEnumerable[TechnologicalInstanceDB], value: TechnologicalInstanceDB) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TechnologicalInstanceDBComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ TO composition """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: TechnologicalInstanceDBComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy:MasterCopy) -> TechnologicalInstanceDB:
        """
        CreateFrom(self: TechnologicalInstanceDBComposition, sourceMasterCopy: MasterCopy) -> TechnologicalInstanceDB

            Create TechnologicalInstanceDB from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.SW.TechnologicalObjects.TechnologicalInstanceDB
        """
        ...

    def Find(self, name:str) -> TechnologicalInstanceDB:
        """
        Find(self: TechnologicalInstanceDBComposition, name: str) -> TechnologicalInstanceDB

            Find by its name

            name: Name of the TechnologicalInstanceDB

            Returns: Siemens.Engineering.SW.TechnologicalObjects.TechnologicalInstanceDB
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TechnologicalInstanceDBComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TechnologicalInstanceDBComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TechnologicalInstanceDB](enumerable: IEnumerable[TechnologicalInstanceDB], value: TechnologicalInstanceDB) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TechnologicalInstanceDBGroup(IEquatable, IEngineeringObject, IEngineeringServiceProvider, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IServiceProvider'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Contains Technological Objects """
    @property
    def Name(self) -> str:
        """
        Name of external source group

        Get: Name(self: TechnologicalInstanceDBGroup) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        Parent of this object

        Get: Parent(self: TechnologicalInstanceDBGroup) -> IEngineeringObject
        """
        ...

    @property
    def TechnologicalObjects(self) -> TechnologicalInstanceDBComposition:
        """
        Get all technological objects

        Get: TechnologicalObjects(self: TechnologicalInstanceDBGroup) -> TechnologicalInstanceDBComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TechnologicalInstanceDBGroup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TechnologicalInstanceDBGroup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TechnologicalInstanceDBSystemGroup(TechnologicalInstanceDBGroup): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringServiceProvider'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Contains Technological Objects """
    pass

class TechnologicalParameter(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represenst a technological parameter """
    @property
    def Name(self) -> str:
        """
        Represents the name of a technological parameter

        Get: Name(self: TechnologicalParameter) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: TechnologicalParameter) -> IEngineeringObject
        """
        ...

    @property
    def Value(self) -> object:
        """
        Represents the value of a technological parameter

        Get: Value(self: TechnologicalParameter) -> object

        Set: Value(self: TechnologicalParameter) = value
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TechnologicalParameter) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TechnologicalParameter) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TechnologicalParameterComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Parameter composition """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: TechnologicalParameterComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> TechnologicalParameter:
        """
        Find(self: TechnologicalParameterComposition, name: str) -> TechnologicalParameter

            Finds a TechnologicalParameter by name

            name: The name of the TechnologicalParameter

            Returns: Siemens.Engineering.SW.TechnologicalObjects.TechnologicalParameter
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TechnologicalParameterComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TechnologicalParameterComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TechnologicalParameter](enumerable: IEnumerable[TechnologicalParameter], value: TechnologicalParameter) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


# variables with complex values
