# encoding: utf-8
# module Siemens.Engineering.Library.Types calls itself Types
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (ExportOptions, IEngineeringAssociation, 
    IEngineeringComposition, IEngineeringObject, IEngineeringService, 
    MultilingualText)

from Siemens.Engineering.Library import ILibrary

from Siemens.Engineering.Library.MasterCopies import MasterCopyAssociation

from System import DateTime, Enum, Guid, IEquatable, Version

from System.Collections import IDictionary, IList

from System.IO import FileInfo

"""The following names are not found in the module: (
    IInternalAssociationAccess, IInternalCompositionAccess, 
    IInternalObjectAccess, field#)
"""

# no functions
# classes

class IInstanceSearchScope: # skipped bases: <type 'object'>
    """ Scope of the project to search when performing a 'Find instances in project' operation """
    pass

class ILibraryTypeInstantiationTarget: # skipped bases: <type 'object'>
    """ Target for instantiation of a library type-version """
    pass

class ILibraryTypeOrFolderSelection: # skipped bases: <type 'object'>
    """ A library type or folder. """
    pass

class IUpdateProjectScope: # skipped bases: <type 'object'>
    """ Represents the scope of the project that may be updated """
    pass

class LibraryType(IEquatable, IEngineeringObject, ILibraryTypeOrFolderSelection, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a library type """
    @property
    def Author(self) -> str:
        """
        Author of the library type
        Get: Author(self: LibraryType) -> str
        """
        ...

    @property
    def Comment(self) -> MultilingualText:
        """
        The library type's comment
        Get: Comment(self: LibraryType) -> MultilingualText
        """
        ...

    @property
    def Guid(self) -> Guid:
        """
        Gets the GUID of this library type
        Get: Guid(self: LibraryType) -> Guid
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the library type
        Get: Name(self: LibraryType) -> str
        Set: Name(self: LibraryType) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: LibraryType) -> IEngineeringObject
        """
        ...

    @property
    def Versions(self) -> LibraryTypeVersionComposition:
        """
        Composition of library type versions
        Get: Versions(self: LibraryType) -> LibraryTypeVersionComposition
        """
        ...


    def Delete(self): # -> 
        """
        Delete(self: LibraryType)
            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: LibraryType) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: LibraryType) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def UpdateLibrary(self, targetLibrary:ILibrary): # -> 
        """
        UpdateLibrary(self: LibraryType, targetLibrary: ILibrary)
            Updates the target library with the latest content from this type
            targetLibrary: Target library to update
        """
        ...

    def UpdateProject(self, updateProjectScope:IUpdateProjectScope): # -> 
        """
        UpdateProject(self: LibraryType, updateProjectScope: IUpdateProjectScope)
            Updates the project with the latest content from this type
            updateProjectScope: The scope of the project that will be updated.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LibraryTypeComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of LibraryTypes """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: LibraryTypeComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> LibraryType:
        """
        Find(self: LibraryTypeComposition, name: str) -> LibraryType
            Finds a given library type
            name: Name to find
            Returns: Siemens.Engineering.Library.Types.LibraryType
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: LibraryTypeComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: LibraryTypeComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[LibraryType](enumerable: IEnumerable[LibraryType], value: LibraryType) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LibraryTypeFolder(IEquatable, IEngineeringObject, ILibraryTypeOrFolderSelection, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Folder containing library types & library type folders """
    @property
    def Folders(self) -> LibraryTypeUserFolderComposition:
        """
        Composition of library type user folders
        Get: Folders(self: LibraryTypeFolder) -> LibraryTypeUserFolderComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the library type folder
        Get: Name(self: LibraryTypeFolder) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: LibraryTypeFolder) -> IEngineeringObject
        """
        ...

    @property
    def Types(self) -> LibraryTypeComposition:
        """
        Composition of library types
        Get: Types(self: LibraryTypeFolder) -> LibraryTypeComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: LibraryTypeFolder) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: LibraryTypeFolder) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LibraryTypeInstanceInfo(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Library instance service """
    @property
    def LibraryTypeInstance(self) -> IEngineeringObject:
        """
        Library type instance
        Get: LibraryTypeInstance(self: LibraryTypeInstanceInfo) -> IEngineeringObject
        """
        ...

    @property
    def LibraryTypeVersion(self) -> LibraryTypeVersion:
        """
        Connected version
        Get: LibraryTypeVersion(self: LibraryTypeInstanceInfo) -> LibraryTypeVersion
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: LibraryTypeInstanceInfo) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: LibraryTypeInstanceInfo) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: LibraryTypeInstanceInfo) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LibraryTypeSystemFolder(LibraryTypeFolder): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ System folder containing library types & library type folders """
    pass

class LibraryTypeUserFolder(LibraryTypeFolder): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ User folder containing library types & library type folders """
    def Delete(self): # -> 
        """
        Delete(self: LibraryTypeUserFolder)
            Deletes this instance.
        """
        ...


class LibraryTypeUserFolderComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of LibraryTypeUserFolders """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: LibraryTypeUserFolderComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> LibraryTypeUserFolder:
        """
        Find(self: LibraryTypeUserFolderComposition, name: str) -> LibraryTypeUserFolder
            Finds a given library type user folder
            name: Name to find
            Returns: Siemens.Engineering.Library.Types.LibraryTypeUserFolder
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: LibraryTypeUserFolderComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: LibraryTypeUserFolderComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[LibraryTypeUserFolder](enumerable: IEnumerable[LibraryTypeUserFolder], value: LibraryTypeUserFolder) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LibraryTypeVersion(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a library type version """
    @property
    def Author(self) -> str:
        """
        Author of the library type version
        Get: Author(self: LibraryTypeVersion) -> str
        """
        ...

    @property
    def Comment(self) -> MultilingualText:
        """
        The library type version's comment
        Get: Comment(self: LibraryTypeVersion) -> MultilingualText
        """
        ...

    @property
    def Dependencies(self) -> LibraryTypeVersionAssociation:
        """
        Returns all versions that this version depends on
        Get: Dependencies(self: LibraryTypeVersion) -> LibraryTypeVersionAssociation
        """
        ...

    @property
    def Dependents(self) -> LibraryTypeVersionAssociation:
        """
        Returns all versions that depend on this version
        Get: Dependents(self: LibraryTypeVersion) -> LibraryTypeVersionAssociation
        """
        ...

    @property
    def Guid(self) -> Guid:
        """
        Gets the GUID of this library version
        Get: Guid(self: LibraryTypeVersion) -> Guid
        """
        ...

    @property
    def MasterCopiesContainingInstances(self) -> MasterCopyAssociation:
        """
        Gets the master copies that contain instances of this version
        Get: MasterCopiesContainingInstances(self: LibraryTypeVersion) -> MasterCopyAssociation
        """
        ...

    @property
    def ModifiedDate(self) -> DateTime:
        """
        Gets the last modified date and time
        Get: ModifiedDate(self: LibraryTypeVersion) -> DateTime
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: LibraryTypeVersion) -> IEngineeringObject
        """
        ...

    @property
    def State(self) -> LibraryTypeVersionState:
        """
        Gets the state of the version
        Get: State(self: LibraryTypeVersion) -> LibraryTypeVersionState
        """
        ...

    @property
    def TypeObject(self) -> LibraryType:
        """
        Gets the connected type object
        Get: TypeObject(self: LibraryTypeVersion) -> LibraryType
        """
        ...

    @property
    def VersionNumber(self) -> Version:
        """
        Gets the library version number. The format is Major.Minor.Build
        Get: VersionNumber(self: LibraryTypeVersion) -> Version
        """
        ...


    def Delete(self): # -> 
        """
        Delete(self: LibraryTypeVersion)
            Deletes this instance.
        """
        ...

    def Export(self, exportFileInfo:FileInfo, exportOptions:ExportOptions): # -> 
        """
        Export(self: LibraryTypeVersion, exportFileInfo: FileInfo, exportOptions: ExportOptions)
            Export Version
            exportFileInfo: exportFileInfo
            exportOptions: exportOptions
        """
        ...

    def FindInstances(self, searchScope:IInstanceSearchScope) -> IList:
        """
        FindInstances(self: LibraryTypeVersion, searchScope: IInstanceSearchScope) -> IList[LibraryTypeInstanceInfo]
            Find all instances in the given scope that are connected to this version.
            searchScope: Scope within the project to search when performing a 'Find instance in project' operation. This may be a ControllerTarget, HmiTarget, etc.
            Returns: System.Collections.Generic.IList<Siemens.Engineering.Library.Types.LibraryTypeInstanceInfo>
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: LibraryTypeVersion) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: LibraryTypeVersion) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LibraryTypeVersionAssociation(IEquatable, IEngineeringAssociation, IInternalAssociationAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Associated library type versions """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent..
        Get: Parent(self: LibraryTypeVersionAssociation) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: LibraryTypeVersionAssociation) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: LibraryTypeVersionAssociation) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[LibraryTypeVersion](enumerable: IEnumerable[LibraryTypeVersion], value: LibraryTypeVersion) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LibraryTypeVersionComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of LibraryTypeVersions """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: LibraryTypeVersionComposition) -> IEngineeringObject
        """
        ...


    def Find(self, versionNumber:Version) -> LibraryTypeVersion:
        """
        Find(self: LibraryTypeVersionComposition, versionNumber: Version) -> LibraryTypeVersion
            Finds a given library type version
            versionNumber: VersionNumber to find
            Returns: Siemens.Engineering.Library.Types.LibraryTypeVersion
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: LibraryTypeVersionComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: LibraryTypeVersionComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[LibraryTypeVersion](enumerable: IEnumerable[LibraryTypeVersion], value: LibraryTypeVersion) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class LibraryTypeVersionState(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Defines the library version object state
    enum LibraryTypeVersionState, values: Committed (1), InWork (0)
    """
    Committed: LibraryTypeVersionState = ...
    InWork: LibraryTypeVersionState = ...
    value__ = ...


class UpdateCheckMode(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Used to control verbosity of logging output from the update check
    enum UpdateCheckMode, values: ReportOutOfDateAndUpToDate (1), ReportOutOfDateOnly (0)
    """
    ReportOutOfDateAndUpToDate: UpdateCheckMode = ...
    ReportOutOfDateOnly: UpdateCheckMode = ...
    value__ = ...


class UpdateCheckResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Result returned from the update check operation """
    @property
    def Messages(self) -> UpdateCheckResultMessageComposition:
        """
        Log messages explaining the details of the update check
        Get: Messages(self: UpdateCheckResult) -> UpdateCheckResultMessageComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: UpdateCheckResult) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UpdateCheckResult) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UpdateCheckResult) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UpdateCheckResultMessage(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Log message explaining the details of the update check """
    @property
    def Description(self) -> str:
        """
        Gets the header for this result of the update check
        Get: Description(self: UpdateCheckResultMessage) -> str
        """
        ...

    @property
    def MessageParts(self) -> IDictionary:
        """
        Gets the log messages specific to each description explaining the details of the update check.
        Get: MessageParts(self: UpdateCheckResultMessage) -> IDictionary[str, str]
        """
        ...

    @property
    def Messages(self) -> UpdateCheckResultMessageComposition:
        """
        Log messages explaining the details of the update check
        Get: Messages(self: UpdateCheckResultMessage) -> UpdateCheckResultMessageComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: UpdateCheckResultMessage) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UpdateCheckResultMessage) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UpdateCheckResultMessage) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UpdateCheckResultMessageComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of UpdateCheckResultMessages """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.
        Get: Parent(self: UpdateCheckResultMessageComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UpdateCheckResultMessageComposition) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UpdateCheckResultMessageComposition) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[UpdateCheckResultMessage](enumerable: IEnumerable[UpdateCheckResultMessage], value: UpdateCheckResultMessage) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


