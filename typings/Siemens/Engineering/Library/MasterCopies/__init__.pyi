# encoding: utf-8
# module Siemens.Engineering.Library.MasterCopies calls itself MasterCopies
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringAssociation,
    IEngineeringComposition, IEngineeringObject)

from Siemens.Engineering.SiVArc import (ISivarcLibraryItem,
    ISivarcLibraryMasterCopy, ISivarcProgramBlockSource)

from Siemens.Engineering.SW import ISoftwareCompareTarget

from System import DateTime, Enum, IEquatable, Type

"""The following names are not found in the module: (
    IInternalAssociationAccess, IInternalCompositionAccess,
    IInternalObjectAccess, field#)
"""

from Siemens import IInternalAssociationAccess, IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class IMasterCopySource: # skipped bases: <type 'object'>
    """ A source item used to create a master copy """
    pass

class IMasterCopyTarget: # skipped bases: <type 'object'>
    """ Target for pasting a library master copy """
    pass

class MasterCopy(ISivarcLibraryMasterCopy, IEquatable, ISivarcLibraryItem, ISivarcProgramBlockSource, IEngineeringObject, ISoftwareCompareTarget, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Represents a library master copy """
    @property
    def Author(self) -> str:
        """
        Author of the master copy

        Get: Author(self: MasterCopy) -> str
        """
        ...

    @property
    def ContentDescriptions(self) -> MasterCopyContentDescriptionComposition:
        """
        Content descriptions

        Get: ContentDescriptions(self: MasterCopy) -> MasterCopyContentDescriptionComposition
        """
        ...

    @property
    def CreationDate(self) -> DateTime:
        """
        Creation date of this master copy

        Get: CreationDate(self: MasterCopy) -> DateTime
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the MasterCopy

        Get: Name(self: MasterCopy) -> str

        Set: Name(self: MasterCopy) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: MasterCopy) -> IEngineeringObject
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: MasterCopy)

            Deletes this instance.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: MasterCopy) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: MasterCopy) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MasterCopyAssociation(IEquatable, IEngineeringAssociation, IInternalAssociationAccess): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Associated MasterCopies """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent..

        Get: Parent(self: MasterCopyAssociation) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: MasterCopyAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: MasterCopyAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MasterCopy](enumerable: IEnumerable[MasterCopy], value: MasterCopy) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MasterCopyComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of MasterCopies """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: MasterCopyComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy:MasterCopy) -> MasterCopy:
        """
        CreateFrom(self: MasterCopyComposition, sourceMasterCopy: MasterCopy) -> MasterCopy

            Create from given Master Copy

            sourceMasterCopy: Source MasterCopy

            Returns: Siemens.Engineering.Library.MasterCopies.MasterCopy
        """
        ...

    def Find(self, name:str) -> MasterCopy:
        """
        Find(self: MasterCopyComposition, name: str) -> MasterCopy

            Finds a given MasterCopy

            name: Name to find

            Returns: Siemens.Engineering.Library.MasterCopies.MasterCopy
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: MasterCopyComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: MasterCopyComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MasterCopy](enumerable: IEnumerable[MasterCopy], value: MasterCopy) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MasterCopyContentDescription(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Master copy content description """
    @property
    def ContentName(self) -> str:
        """
        name of master coy content

        Get: ContentName(self: MasterCopyContentDescription) -> str
        """
        ...

    @property
    def ContentType(self) -> Type:
        """
        Type of master copy content

        Get: ContentType(self: MasterCopyContentDescription) -> Type
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: MasterCopyContentDescription) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: MasterCopyContentDescription) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: MasterCopyContentDescription) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MasterCopyContentDescriptionComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of master copy contents """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: MasterCopyContentDescriptionComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: MasterCopyContentDescriptionComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: MasterCopyContentDescriptionComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MasterCopyContentDescription](enumerable: IEnumerable[MasterCopyContentDescription], value: MasterCopyContentDescription) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MasterCopyFolder(IEquatable, IEngineeringObject, ISivarcLibraryItem, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Folder containing Master Copies & Master Copy folders """
    @property
    def Folders(self) -> MasterCopyUserFolderComposition:
        """
        Composition of MasterCopy user folders

        Get: Folders(self: MasterCopyFolder) -> MasterCopyUserFolderComposition
        """
        ...

    @property
    def MasterCopies(self) -> MasterCopyComposition:
        """
        Composition of MasterCopies

        Get: MasterCopies(self: MasterCopyFolder) -> MasterCopyComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the MasterCopy folder

        Get: Name(self: MasterCopyFolder) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: MasterCopyFolder) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: MasterCopyFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: MasterCopyFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class MasterCopyMode(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    The list of possible scenarios supported by master copy 'copy' action parameterization

    enum MasterCopyMode, values: Rename (1), Replace (2), ThrowIfExists (0)
    """
    Rename: MasterCopyMode = ...
    Replace: MasterCopyMode = ...
    ThrowIfExists: MasterCopyMode = ...
    value__ = ...


class MasterCopySystemFolder(MasterCopyFolder): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'ISivarcLibraryItem'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ System folder containing Master Copies & Master Copy folders """
    pass

class MasterCopyUserFolder(MasterCopyFolder): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'ISivarcLibraryItem'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ User folder containing Master Copies & Master Copy folders """
    def Delete(self): # ->
        """
        Delete(self: MasterCopyUserFolder)

            Deletes this instance.
        """
        ...


class MasterCopyUserFolderComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of MasterCopyUserFolders """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: MasterCopyUserFolderComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> MasterCopyUserFolder:
        """
        Find(self: MasterCopyUserFolderComposition, name: str) -> MasterCopyUserFolder

            Finds a given MasterCopy user folder

            name: Name to find

            Returns: Siemens.Engineering.Library.MasterCopies.MasterCopyUserFolder
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: MasterCopyUserFolderComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: MasterCopyUserFolderComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MasterCopyUserFolder](enumerable: IEnumerable[MasterCopyUserFolder], value: MasterCopyUserFolder) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
