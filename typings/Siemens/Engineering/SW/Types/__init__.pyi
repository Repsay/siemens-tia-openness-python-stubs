# encoding: utf-8
# module Siemens.Engineering.SW.Types calls itself Types
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (ExportOptions, IEngineeringComposition, 
    IEngineeringObject, IEngineeringServiceProvider, ImportOptions)

from Siemens.Engineering.Library.MasterCopies import (IMasterCopySource, 
    IMasterCopyTarget, MasterCopy)

from Siemens.Engineering.Library.Types import (
    ILibraryTypeInstantiationTarget, LibraryType, LibraryTypeVersion)

from Siemens.Engineering.SW import SWImportOptions

from Siemens.Engineering.SW.ExternalSources import IGenerateSource

from System import DateTime, IEquatable

from System.Collections import IList

from System.IO import FileInfo

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess)
"""

# no functions
# classes

class PlcType(IInternalObjectAccess, IEngineeringServiceProvider, IEngineeringObject, IGenerateSource, IMasterCopySource, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IServiceProvider'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Plc type """
    @property
    def CreationDate(self) -> DateTime:
        """
        Creation date of this Plc type
        Get: CreationDate(self: PlcType) -> DateTime
        """
        ...

    @property
    def InterfaceModifiedDate(self) -> DateTime:
        """
        Get last breakable interface change of the PLC data type
        Get: InterfaceModifiedDate(self: PlcType) -> DateTime
        """
        ...

    @property
    def IsConsistent(self) -> bool:
        """
        True if block and used data is consistent
        Get: IsConsistent(self: PlcType) -> bool
        """
        ...

    @property
    def IsKnowHowProtected(self) -> bool:
        """
        Gets the know-how protection status of the block
        Get: IsKnowHowProtected(self: PlcType) -> bool
        """
        ...

    @property
    def ModifiedDate(self) -> DateTime:
        """
        Get the last non-breakable modification of the PLC data type
        Get: ModifiedDate(self: PlcType) -> DateTime
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the Plc type
        Get: Name(self: PlcType) -> str
        Set: Name(self: PlcType) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: PlcType) -> IEngineeringObject
        """
        ...


    def Delete(self): # -> 
        """
        Delete(self: PlcType)
            Deletes this instance.
        """
        ...

    def Export(self, path:FileInfo, exportOptions:ExportOptions): # -> 
        """
        Export(self: PlcType, path: FileInfo, exportOptions: ExportOptions)
            Simatic ML export of a Plc type
            path: Path to the Simatic ML file
            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcType) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ShowInEditor(self): # -> 
        """
        ShowInEditor(self: PlcType)
            Show the indicated item in the Plc type editor
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcType) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcStruct(PlcType): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringServiceProvider'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IMasterCopySource'>, <type 'IGenerateSource'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Plc struct """
    pass

class PlcSystemTypeGroup(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Group containing Plc system types """
    @property
    def Name(self) -> str:
        """
        The name of the Plc system type group
        Get: Name(self: PlcSystemTypeGroup) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: PlcSystemTypeGroup) -> IEngineeringObject
        """
        ...

    @property
    def Types(self) -> PlcTypeComposition:
        """
        Composition of Plc system types
        Get: Types(self: PlcSystemTypeGroup) -> PlcTypeComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcSystemTypeGroup) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcSystemTypeGroup) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcSystemTypeGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of PlcSystemTypeGroups """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: PlcSystemTypeGroupComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcSystemTypeGroupComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcSystemTypeGroupComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcSystemTypeGroup](enumerable: IEnumerable[PlcSystemTypeGroup], value: PlcSystemTypeGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcTypeComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of PlcTypes """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: PlcTypeComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, *__args:MasterCopy) -> PlcType:
        """
        CreateFrom(self: PlcTypeComposition, sourceMasterCopy: MasterCopy) -> PlcType
            Create PlcType from MasterCopy
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.Types.PlcType
        CreateFrom(self: PlcTypeComposition, libraryTypeVersion: PlcTypeLibraryTypeVersion) -> PlcType
            Create plc type from type version
            libraryTypeVersion: Library type version
            Returns: Siemens.Engineering.SW.Types.PlcType
        """
        ...

    def Find(self, name:str) -> PlcType:
        """
        Find(self: PlcTypeComposition, name: str) -> PlcType
            Finds a given Plc type
            name: Name to find
            Returns: Siemens.Engineering.SW.Types.PlcType
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcTypeComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path:FileInfo, importOptions:ImportOptions, swImportOptions:SWImportOptions = ...) -> IList:
        """
        Import(self: PlcTypeComposition, path: FileInfo, importOptions: ImportOptions) -> IList[PlcType]
            Simatic ML import of a Plc type
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Types.PlcType>
        Import(self: PlcTypeComposition, path: FileInfo, importOptions: ImportOptions, swImportOptions: SWImportOptions) -> IList[PlcType]
            Simatic ML import of a Plc type
            path: Path to the Simatic ML file
            importOptions: Options to use for Import
            swImportOptions: Sw import options to use for Import
            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Types.PlcType>
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcTypeComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcType](enumerable: IEnumerable[PlcType], value: PlcType) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcTypeGroup(IEquatable, IEngineeringObject, IEngineeringServiceProvider, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IServiceProvider'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Group containing Plc types & Plc type user groups """
    @property
    def Groups(self) -> PlcTypeUserGroupComposition:
        """
        Composition of Plc type user groups
        Get: Groups(self: PlcTypeGroup) -> PlcTypeUserGroupComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the Plc type group
        Get: Name(self: PlcTypeGroup) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: PlcTypeGroup) -> IEngineeringObject
        """
        ...

    @property
    def Types(self) -> PlcTypeComposition:
        """
        Composition of Plc types
        Get: Types(self: PlcTypeGroup) -> PlcTypeComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcTypeGroup) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcTypeGroup) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PlcTypeLibraryType(LibraryType): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a library type made from a Plc type """
    pass

class PlcTypeLibraryTypeVersion(LibraryTypeVersion): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a library type version made from a Plc type """
    pass

class PlcTypeSystemGroup(ILibraryTypeInstantiationTarget, IMasterCopyTarget, PlcTypeGroup): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringServiceProvider'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ System group containing Plc types & Plc type user groups """
    @property
    def SystemTypeGroups(self) -> PlcSystemTypeGroupComposition:
        """
        Composition of system data types
        Get: SystemTypeGroups(self: PlcTypeSystemGroup) -> PlcSystemTypeGroupComposition
        """
        ...



class PlcTypeUserGroup(ILibraryTypeInstantiationTarget, IMasterCopySource, PlcTypeGroup, IMasterCopyTarget): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringServiceProvider'>, <type 'IEngineeringInstance'>, <type 'IServiceProvider'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ User group containing Plc types & Plc type user groups """
    def Delete(self): # -> 
        """
        Delete(self: PlcTypeUserGroup)
            Deletes this instance.
        """
        ...


class PlcTypeUserGroupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of PlcTypeUserGroups """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: PlcTypeUserGroupComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy:MasterCopy) -> PlcTypeUserGroup:
        """
        CreateFrom(self: PlcTypeUserGroupComposition, sourceMasterCopy: MasterCopy) -> PlcTypeUserGroup
            Create PlcTypeUserGroup from MasterCopy
            sourceMasterCopy: The source master copy
            Returns: Siemens.Engineering.SW.Types.PlcTypeUserGroup
        """
        ...

    def Find(self, name:str) -> PlcTypeUserGroup:
        """
        Find(self: PlcTypeUserGroupComposition, name: str) -> PlcTypeUserGroup
            Finds a given Plc type user group
            name: Name to find
            Returns: Siemens.Engineering.SW.Types.PlcTypeUserGroup
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: PlcTypeUserGroupComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: PlcTypeUserGroupComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PlcTypeUserGroup](enumerable: IEnumerable[PlcTypeUserGroup], value: PlcTypeUserGroup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


