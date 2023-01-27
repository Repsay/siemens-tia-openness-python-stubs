# encoding: utf-8
# module Siemens.Engineering.Library calls itself Library
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringComposition, IEngineeringObject, 
    ITransactionSupport, LanguageSettings, MultilingualText, OpenMode, 
    Project)

from Siemens.Engineering.Library.MasterCopies import MasterCopySystemFolder

from Siemens.Engineering.Library.Types import (LibraryType, 
    LibraryTypeSystemFolder, LibraryTypeVersion, UpdateCheckMode, 
    UpdateCheckResult)

from Siemens.Engineering.SW import ISoftwareCompareTarget

from System import Enum, Guid, IEquatable

from System.Collections import IEnumerable, IList

from System.IO import DirectoryInfo, FileInfo

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

# no functions
# classes

class ILibrary: # skipped bases: <type 'object'>
    """ Base interface implemented by all libraries """
    @property
    def MasterCopyFolder(self) -> MasterCopySystemFolder:
        """
        System folder containing master copies and master copy folders
        Get: MasterCopyFolder(self: ILibrary) -> MasterCopySystemFolder
        """
        ...

    @property
    def TypeFolder(self) -> LibraryTypeSystemFolder:
        """
        System folder containing library types and library type folders
        Get: TypeFolder(self: ILibrary) -> LibraryTypeSystemFolder
        """
        ...


    def FindType(self, typeGuid:Guid) -> LibraryType:
        """
        FindType(self: ILibrary, typeGuid: Guid) -> LibraryType
            Searches the global library for a type object using a type GUID as the search criteria
            typeGuid: Globally unique identifier of the type object to be searched for
            Returns: Siemens.Engineering.Library.Types.LibraryType
        """
        ...

    def FindVersion(self, versionGuid:Guid) -> LibraryTypeVersion:
        """
        FindVersion(self: ILibrary, versionGuid: Guid) -> LibraryTypeVersion
            Searches the global library for a version object using a version GUID as the search criteria
            versionGuid: Globally unique identifier of the version object to be searched for
            Returns: Siemens.Engineering.Library.Types.LibraryTypeVersion
        """
        ...

    def UpdateCheck(self, project:Project, updateCheckMode:UpdateCheckMode) -> UpdateCheckResult:
        """
        UpdateCheck(self: ILibrary, project: Project, updateCheckMode: UpdateCheckMode) -> UpdateCheckResult
            Identify all instances in a project that require updating based on the content of this library
            project: The project to be compared with this library
            updateCheckMode: Used to control whether or not to log out of date instances
            Returns: Siemens.Engineering.Library.Types.UpdateCheckResult
        """
        ...

    def UpdateLibrary(self, sourceTypesAndFolders:IEnumerable, targetLibrary:ILibrary): # -> 
        """ UpdateLibrary(self: ILibrary, sourceTypesAndFolders: IEnumerable[ILibraryTypeOrFolderSelection], targetLibrary: ILibrary) """
        ...

    def UpdateProject(self, sourceTypesAndFolders:IEnumerable, updateProjectScopes:IEnumerable): # -> 
        """ UpdateProject(self: ILibrary, sourceTypesAndFolders: IEnumerable[ILibraryTypeOrFolderSelection], updateProjectScopes: IEnumerable[IUpdateProjectScope]) """
        ...


class GlobalLibrary(IInternalObjectAccess, ITransactionSupport, ILibrary, IEngineeringObject, ISoftwareCompareTarget, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a global library """
    @property
    def Author(self) -> str:
        """
        Author of the Global Library
        Get: Author(self: GlobalLibrary) -> str
        """
        ...

    @property
    def Comment(self) -> MultilingualText:
        """
        The global libraries comment
        Get: Comment(self: GlobalLibrary) -> MultilingualText
        """
        ...

    @property
    def IsModified(self) -> bool:
        """
        True if the global library has been modified
        Get: IsModified(self: GlobalLibrary) -> bool
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """
        Is the global library open only for read
        Get: IsReadOnly(self: GlobalLibrary) -> bool
        """
        ...

    @property
    def LanguageSettings(self) -> LanguageSettings:
        """
        Global Library language settings
        Get: LanguageSettings(self: GlobalLibrary) -> LanguageSettings
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the global library.
        Get: Name(self: GlobalLibrary) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: GlobalLibrary) -> IEngineeringObject
        """
        ...

    @property
    def Path(self) -> FileInfo:
        """
        The path to this global library
        Get: Path(self: GlobalLibrary) -> FileInfo
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: GlobalLibrary) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: GlobalLibrary) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CorporateGlobalLibrary(GlobalLibrary): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'ILibrary'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'ITransactionSupport'>, <type 'ISoftwareCompareTarget'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ A corporate global library. """
    pass

class GlobalLibraryComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of GlobalLibraries """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: GlobalLibraryComposition) -> IEngineeringObject
        """
        ...


    def GetGlobalLibraryInfos(self) -> IList:
        """
        GetGlobalLibraryInfos(self: GlobalLibraryComposition) -> IList[GlobalLibraryInfo]
            Returns a list of LibraryInfo's representing preview state Global Libraries
            Returns: System.Collections.Generic.IList<Siemens.Engineering.Library.GlobalLibraryInfo>
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: GlobalLibraryComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Open(self, *__args:GlobalLibraryInfo) -> GlobalLibrary:
        """
        Open(self: GlobalLibraryComposition, libraryInfo: GlobalLibraryInfo) -> GlobalLibrary
            Opens the specified global library
            libraryInfo: The global library info associated with a global library to be opened
            Returns: Siemens.Engineering.Library.GlobalLibrary
        Open(self: GlobalLibraryComposition, path: FileInfo, openMode: OpenMode) -> UserGlobalLibrary
            Opens the specified global library
            path: Path to the global library
            openMode: The open mode to open the global library with.
            Returns: Siemens.Engineering.Library.UserGlobalLibrary
        """
        ...

    def OpenWithUpgrade(self, path:FileInfo) -> UserGlobalLibrary:
        """
        OpenWithUpgrade(self: GlobalLibraryComposition, path: FileInfo) -> UserGlobalLibrary
            Opens the specified global library and allows for upgrade of older versions if possible.
            path: Path to the global library
            Returns: Siemens.Engineering.Library.UserGlobalLibrary
        """
        ...

    def Retrieve(self, sourcePath:FileInfo, targetDirectory:DirectoryInfo, openMode:OpenMode) -> UserGlobalLibrary:
        """
        Retrieve(self: GlobalLibraryComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo, openMode: OpenMode) -> UserGlobalLibrary
            Retrieves an archived library
            sourcePath: The path of the archived library file
            targetDirectory: The path to the folder where library would be retrieved.
            openMode: The open mode to open the global library with.
            Returns: Siemens.Engineering.Library.UserGlobalLibrary
        """
        ...

    def RetrieveWithUpgrade(self, sourcePath:FileInfo, targetDirectory:DirectoryInfo, openMode:OpenMode) -> UserGlobalLibrary:
        """
        RetrieveWithUpgrade(self: GlobalLibraryComposition, sourcePath: FileInfo, targetDirectory: DirectoryInfo, openMode: OpenMode) -> UserGlobalLibrary
            Retrieves a library from an archive and upgrades it to the current version
            sourcePath: The path of the archived library file
            targetDirectory: The path to the folder where library would be retrieved.
            openMode: The open mode to open the global library with.
            Returns: Siemens.Engineering.Library.UserGlobalLibrary
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: GlobalLibraryComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[GlobalLibrary](enumerable: IEnumerable[GlobalLibrary], value: GlobalLibrary) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class GlobalLibraryInfo(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents information for a Global Library """
    @property
    def IsOpen(self) -> bool:
        """
        Returns a Boolean representing if the global library associated with this GlobalLibraryInfo is already open or not.
        Get: IsOpen(self: GlobalLibraryInfo) -> bool
        """
        ...

    @property
    def IsReadOnly(self) -> bool:
        """
        True if the globa library is currently read only.
        Get: IsReadOnly(self: GlobalLibraryInfo) -> bool
        """
        ...

    @property
    def LibraryType(self) -> GlobalLibraryType:
        """
        The Global Library Type
        Get: LibraryType(self: GlobalLibraryInfo) -> GlobalLibraryType
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the global library.
        Get: Name(self: GlobalLibraryInfo) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: GlobalLibraryInfo) -> IEngineeringObject
        """
        ...

    @property
    def Path(self) -> FileInfo:
        """
        The full library path.
        Get: Path(self: GlobalLibraryInfo) -> FileInfo
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: GlobalLibraryInfo) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: GlobalLibraryInfo) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class GlobalLibraryType(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Represents the GlobalLibrary Types such as System, User, or Corporate
    enum GlobalLibraryType, values: Corporate (1), System (0), User (2)
    """
    Corporate: GlobalLibraryType = ...
    System: GlobalLibraryType = ...
    User: GlobalLibraryType = ...
    value__ = ...


class LibraryArchivationMode(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Library archivation modes
    enum LibraryArchivationMode, values: Compressed (1), DiscardRestorableData (2), DiscardRestorableDataAndCompressed (3), None (0)
    """
    Compressed: LibraryArchivationMode = ...
    DiscardRestorableData: LibraryArchivationMode = ...
    DiscardRestorableDataAndCompressed: LibraryArchivationMode = ...
    value__ = ...


class ProjectLibrary(IEquatable, IEngineeringObject, ILibrary, ISoftwareCompareTarget, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents the project library """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: ProjectLibrary) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ProjectLibrary) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ProjectLibrary) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SystemGlobalLibrary(GlobalLibrary): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'ILibrary'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'ITransactionSupport'>, <type 'ISoftwareCompareTarget'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a System Library """
    pass

class UserGlobalLibrary(GlobalLibrary): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'ILibrary'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'ITransactionSupport'>, <type 'ISoftwareCompareTarget'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a User Global Library """
    def Archive(self, targetDirectory:DirectoryInfo, targetName:str, archivationMode:LibraryArchivationMode): # -> 
        """
        Archive(self: UserGlobalLibrary, targetDirectory: DirectoryInfo, targetName: str, archivationMode: LibraryArchivationMode)
            Archives the User Global library.
            targetDirectory: Directory where the library to be archived
            targetName: File name for the archived file
            archivationMode: Archivation mode
        """
        ...

    def Close(self): # -> 
        """
        Close(self: UserGlobalLibrary)
            Closes the User Library
        """
        ...

    def Save(self): # -> 
        """
        Save(self: UserGlobalLibrary)
            Saves the User Library
        """
        ...

    def SaveAs(self, targetDirectory:DirectoryInfo): # -> 
        """
        SaveAs(self: UserGlobalLibrary, targetDirectory: DirectoryInfo)
            Save a User Library to another location
            targetDirectory: The target directory path to save the User Library
        """
        ...


# variables with complex values

