# encoding: utf-8
# module Siemens.Engineering.Hmi.RuntimeScripting calls itself RuntimeScripting
# from Siemens.Engineering, Version=16.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (ExportOptions, IEngineeringComposition,
    IEngineeringObject, IEngineeringServiceProvider, ImportOptions)

from Siemens.Engineering.Library.MasterCopies import (IMasterCopySource,
    IMasterCopyTarget)

from Siemens.Engineering.Library.Types import (
    ILibraryTypeInstantiationTarget, LibraryType, LibraryTypeVersion)

from System import IEquatable

from System.Collections import IList

from System.IO import FileInfo

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class CScriptLibraryType(LibraryType): # skipped bases: <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'ISivarcLibraryItem'>, <type 'ISivarcProgramBlockSource'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'object'>
    """ Class representing a Cscript library type """
    pass

class CScriptLibraryTypeVersion(LibraryTypeVersion): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ Class representing a Cscript library type version """
    pass

class VBScript(IEquatable, IEngineeringObject, IEngineeringServiceProvider, IMasterCopySource, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IServiceProvider'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents a VBscript """
    @property
    def Name(self) -> str:
        """
        The name of the VBScript

        Get: Name(self: VBScript) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: VBScript) -> IEngineeringObject
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: VBScript)

            Deletes this instance.
        """
        ...

    def Export(self, path:FileInfo, exportOptions:ExportOptions): # ->
        """
        Export(self: VBScript, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a VBScript

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: VBScript) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: VBScript) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class VBScriptComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of VBScripts """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: VBScriptComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, *__args:VBScriptLibraryTypeVersion) -> VBScript:
        """
        CreateFrom(self: VBScriptComposition, libraryTypeVersion: VBScriptLibraryTypeVersion) -> VBScript

            Create script from library type version

            libraryTypeVersion: library type version

            Returns: Siemens.Engineering.Hmi.RuntimeScripting.VBScript

        CreateFrom(self: VBScriptComposition, sourceMasterCopy: MasterCopy) -> VBScript

            Create VBScript from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.Hmi.RuntimeScripting.VBScript
        """
        ...

    def Find(self, name:str) -> VBScript:
        """
        Find(self: VBScriptComposition, name: str) -> VBScript

            Finds a given VBScript

            name: Name to find

            Returns: Siemens.Engineering.Hmi.RuntimeScripting.VBScript
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: VBScriptComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path:FileInfo, importOptions:ImportOptions) -> IList:
        """
        Import(self: VBScriptComposition, path: FileInfo, importOptions: ImportOptions) -> IList[VBScript]

            Simatic ML import of a VBScript

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.RuntimeScripting.VBScript>
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: VBScriptComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[VBScript](enumerable: IEnumerable[VBScript], value: VBScript) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class VBScriptFolder(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Folder containing VBScripts & VBScript user folders """
    @property
    def Folders(self) -> VBScriptUserFolderComposition:
        """
        Composition of VBScript user folders

        Get: Folders(self: VBScriptFolder) -> VBScriptUserFolderComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the VBScript folder

        Get: Name(self: VBScriptFolder) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: VBScriptFolder) -> IEngineeringObject
        """
        ...

    @property
    def VBScripts(self) -> VBScriptComposition:
        """
        Composition of VBScripts

        Get: VBScripts(self: VBScriptFolder) -> VBScriptComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: VBScriptFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: VBScriptFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class VBScriptLibraryType(LibraryType): # skipped bases: <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'ISivarcLibraryItem'>, <type 'ISivarcProgramBlockSource'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'object'>
    """ Represents a library type made from a VBScript """
    pass

class VBScriptLibraryTypeVersion(LibraryTypeVersion): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ Represents a library type version made from a VBScript """
    pass

class VBScriptSystemFolder(ILibraryTypeInstantiationTarget, VBScriptFolder, IMasterCopyTarget): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ System folder containing VBScripts & VBScript user folders """
    pass

class VBScriptUserFolder(ILibraryTypeInstantiationTarget, VBScriptFolder, IMasterCopySource, IMasterCopyTarget): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ User folder containing VBScripts & VBScript user folders """
    def Delete(self): # ->
        """
        Delete(self: VBScriptUserFolder)

            Deletes this instance.
        """
        ...


class VBScriptUserFolderComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of VBScriptUserFolders """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: VBScriptUserFolderComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> VBScriptUserFolder:
        """
        Find(self: VBScriptUserFolderComposition, name: str) -> VBScriptUserFolder

            Finds a given VBScript user folder

            name: Name to find

            Returns: Siemens.Engineering.Hmi.RuntimeScripting.VBScriptUserFolder
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: VBScriptUserFolderComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: VBScriptUserFolderComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[VBScriptUserFolder](enumerable: IEnumerable[VBScriptUserFolder], value: VBScriptUserFolder) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
