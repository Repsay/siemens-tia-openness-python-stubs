# encoding: utf-8
# module Siemens.Engineering.Hmi.Tag calls itself Tag
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (ExportOptions, IEngineeringComposition,
    IEngineeringObject, IEngineeringServiceProvider, ImportOptions)

from Siemens.Engineering.Hmi import ILimit

from Siemens.Engineering.Library.MasterCopies import (IMasterCopySource,
    IMasterCopyTarget, MasterCopy)

from Siemens.Engineering.Library.Types import (LibraryType,
    LibraryTypeVersion)

from System import IEquatable

from System.Collections import IList

from System.IO import FileInfo

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess)
"""
from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class HmiUdtLibraryType(LibraryType): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a library type made from a Udt """
    pass

class HmiUdtLibraryTypeVersion(LibraryTypeVersion): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a library type version made from a Udt """
    pass

class Tag(IInternalObjectAccess, IEngineeringServiceProvider, IEngineeringObject, ILimit, IMasterCopySource, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IServiceProvider'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents an Hmi tag """
    @property
    def Name(self) -> str:
        """
        The name of the tag

        Get: Name(self: Tag) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: Tag) -> IEngineeringObject
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: Tag)

            Deletes this instance.
        """
        ...

    def Export(self, path:FileInfo, exportOptions:ExportOptions): # ->
        """
        Export(self: Tag, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a tag

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: Tag) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: Tag) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TagComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of (Hmi)Tags """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: TagComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy:MasterCopy) -> Tag:
        """
        CreateFrom(self: TagComposition, sourceMasterCopy: MasterCopy) -> Tag

            Create Tag from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.Hmi.Tag.Tag
        """
        ...

    def Find(self, name:str) -> Tag:
        """
        Find(self: TagComposition, name: str) -> Tag

            Finds a given tag

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Tag.Tag
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TagComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path:FileInfo, importOptions:ImportOptions) -> IList:
        """
        Import(self: TagComposition, path: FileInfo, importOptions: ImportOptions) -> IList[Tag]

            Simatic ML import of a tag

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Tag.Tag>
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TagComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Tag](enumerable: IEnumerable[Tag], value: Tag) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TagFolder(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Folder containing Hmi tag tables & Hmi tag user folders """
    @property
    def Folders(self) -> TagUserFolderComposition:
        """
        Composition of tag user folders

        Get: Folders(self: TagFolder) -> TagUserFolderComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the tag folder

        Get: Name(self: TagFolder) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: TagFolder) -> IEngineeringObject
        """
        ...

    @property
    def TagTables(self) -> TagTableComposition:
        """
        Composition of Hmi tag tables

        Get: TagTables(self: TagFolder) -> TagTableComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TagFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TagFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TagSystemFolder(IMasterCopyTarget, TagFolder): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ System folder containing Hmi tag tables & Hmi tag user folders """
    @property
    def DefaultTagTable(self) -> TagTable:
        """
        Get the default Hmi tag table

        Get: DefaultTagTable(self: TagSystemFolder) -> TagTable
        """
        ...



class TagTable(IEquatable, IEngineeringObject, IMasterCopySource, IMasterCopyTarget, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents an Hmi tag table """
    @property
    def IsSystemObject(self) -> bool:
        """
        Gets a value that identifies this is the default tag table

        Get: IsSystemObject(self: TagTable) -> bool
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the tag table

        Get: Name(self: TagTable) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: TagTable) -> IEngineeringObject
        """
        ...

    @property
    def Tags(self) -> TagComposition:
        """
        Composition of Hmi tags

        Get: Tags(self: TagTable) -> TagComposition
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: TagTable)

            Deletes this instance.
        """
        ...

    def Export(self, path:FileInfo, exportOptions:ExportOptions): # ->
        """
        Export(self: TagTable, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a tag table

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TagTable) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TagTable) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TagTableComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of (Hmi)TagTables """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: TagTableComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy:MasterCopy) -> TagTable:
        """
        CreateFrom(self: TagTableComposition, sourceMasterCopy: MasterCopy) -> TagTable

            Create TagTable from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.Hmi.Tag.TagTable
        """
        ...

    def Find(self, name:str) -> TagTable:
        """
        Find(self: TagTableComposition, name: str) -> TagTable

            Finds a given tag table

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Tag.TagTable
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TagTableComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path:FileInfo, importOptions:ImportOptions) -> IList:
        """
        Import(self: TagTableComposition, path: FileInfo, importOptions: ImportOptions) -> IList[TagTable]

            Simatic ML import of a tag table

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Tag.TagTable>
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TagTableComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TagTable](enumerable: IEnumerable[TagTable], value: TagTable) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TagUserFolder(IMasterCopySource, TagFolder, IMasterCopyTarget): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ User folder containing Hmi tag tables & Hmi tag user folders """
    def Delete(self): # ->
        """
        Delete(self: TagUserFolder)

            Deletes this instance.
        """
        ...


class TagUserFolderComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of (Hmi)TagUserFolders """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: TagUserFolderComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> TagUserFolder:
        """
        Find(self: TagUserFolderComposition, name: str) -> TagUserFolder

            Finds a given tag user folder

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Tag.TagUserFolder
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TagUserFolderComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TagUserFolderComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TagUserFolder](enumerable: IEnumerable[TagUserFolder], value: TagUserFolder) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
