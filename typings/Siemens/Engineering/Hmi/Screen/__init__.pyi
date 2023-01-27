# encoding: utf-8
# module Siemens.Engineering.Hmi.Screen calls itself Screen
# from Siemens.Engineering, Version=16.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (ExportOptions, IEngineeringComposition,
    IEngineeringObject, IEngineeringServiceProvider, ImportOptions)

from Siemens.Engineering.Library.MasterCopies import (IMasterCopySource,
    IMasterCopyTarget, MasterCopy)

from Siemens.Engineering.Library.Types import (
    ILibraryTypeInstantiationTarget, LibraryType, LibraryTypeVersion)

from System import Enum, IEquatable

from System.Collections import IList

from System.IO import FileInfo

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class Screen(IEquatable, IEngineeringObject, IEngineeringServiceProvider, IMasterCopySource, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IServiceProvider'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents a screen """
    @property
    def Name(self) -> str:
        """
        The name of the screen

        Get: Name(self: Screen) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: Screen) -> IEngineeringObject
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: Screen)

            Deletes this instance.
        """
        ...

    def Export(self, path:FileInfo, exportOptions:ExportOptions): # ->
        """
        Export(self: Screen, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a screen

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: Screen) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: Screen) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of Screens """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ScreenComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, *__args:ScreenLibraryTypeVersion) -> Screen:
        """
        CreateFrom(self: ScreenComposition, libraryTypeVersion: ScreenLibraryTypeVersion) -> Screen

            Create screen from type version

            libraryTypeVersion: screen version

            Returns: Siemens.Engineering.Hmi.Screen.Screen

        CreateFrom(self: ScreenComposition, sourceMasterCopy: MasterCopy) -> Screen

            Create Screen from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.Hmi.Screen.Screen
        """
        ...

    def Find(self, name:str) -> Screen:
        """
        Find(self: ScreenComposition, name: str) -> Screen

            Finds a given screen

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Screen.Screen
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path:FileInfo, importOptions:ImportOptions) -> IList:
        """
        Import(self: ScreenComposition, path: FileInfo, importOptions: ImportOptions) -> IList[Screen]

            Simatic ML import of a screen

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Screen.Screen>
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Screen](enumerable: IEnumerable[Screen], value: Screen) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenFolder(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents a screen folder """
    @property
    def Folders(self) -> ScreenUserFolderComposition:
        """
        Composition of screen user folders

        Get: Folders(self: ScreenFolder) -> ScreenUserFolderComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the screen folder

        Get: Name(self: ScreenFolder) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ScreenFolder) -> IEngineeringObject
        """
        ...

    @property
    def Screens(self) -> ScreenComposition:
        """
        Composition of screens

        Get: Screens(self: ScreenFolder) -> ScreenComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenGlobalElements(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents the screen global elements """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ScreenGlobalElements) -> IEngineeringObject
        """
        ...


    def Export(self, path:FileInfo, exportOptions:ExportOptions): # ->
        """
        Export(self: ScreenGlobalElements, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of screen global elements

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenGlobalElements) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenGlobalElements) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenLibraryType(LibraryType): # skipped bases: <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'ISivarcLibraryItem'>, <type 'ISivarcProgramBlockSource'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'object'>
    """ Represents a library type made from a screen """
    pass

class ScreenLibraryTypeVersion(LibraryTypeVersion): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ Represents a library type version made from a screen """
    pass

class ScreenOverview(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Editor for elements in the overview """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ScreenOverview) -> IEngineeringObject
        """
        ...


    def Export(self, path:FileInfo, exportOptions:ExportOptions): # ->
        """
        Export(self: ScreenOverview, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a screen overview

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenOverview) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenOverview) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenPopup(IEquatable, IEngineeringObject, IMasterCopySource, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Pop-up screen """
    @property
    def Name(self) -> str:
        """
        Gets or sets the screen name.

        Get: Name(self: ScreenPopup) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ScreenPopup) -> IEngineeringObject
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: ScreenPopup)

            Deletes this instance.
        """
        ...

    def Export(self, path:FileInfo, exportOptions:ExportOptions): # ->
        """
        Export(self: ScreenPopup, path: FileInfo, exportOptions: ExportOptions)

            Common export

            path: Path to the Simatic ML file

            exportOptions: Determines whether the default values are exported or not
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenPopup) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenPopup) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenPopupComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of popup screens. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ScreenPopupComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy:MasterCopy) -> ScreenPopup:
        """
        CreateFrom(self: ScreenPopupComposition, sourceMasterCopy: MasterCopy) -> ScreenPopup

            Create ScreenPopup from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.Hmi.Screen.ScreenPopup
        """
        ...

    def Find(self, name:str) -> ScreenPopup:
        """
        Find(self: ScreenPopupComposition, name: str) -> ScreenPopup

            Finds a given screen popup

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Screen.ScreenPopup
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenPopupComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path:FileInfo, importOptions:ImportOptions) -> IList:
        """
        Import(self: ScreenPopupComposition, path: FileInfo, importOptions: ImportOptions) -> IList[ScreenPopup]

            Import Action

            path: Path to the Simatic ML file

            importOptions: Options to use for the Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Screen.ScreenPopup>
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenPopupComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ScreenPopup](enumerable: IEnumerable[ScreenPopup], value: ScreenPopup) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenPopupFolder(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Folder containing screen popups """
    @property
    def Folders(self) -> ScreenPopupUserFolderComposition:
        """
        Composition of screen popup user folders

        Get: Folders(self: ScreenPopupFolder) -> ScreenPopupUserFolderComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the screen popup folder

        Get: Name(self: ScreenPopupFolder) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ScreenPopupFolder) -> IEngineeringObject
        """
        ...

    @property
    def ScreenPopups(self) -> ScreenPopupComposition:
        """
        Composition of screen popups

        Get: ScreenPopups(self: ScreenPopupFolder) -> ScreenPopupComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenPopupFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenPopupFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenPopupSystemFolder(ScreenPopupFolder, IMasterCopyTarget): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ System folder containing screen popups """
    pass

class ScreenPopupUserFolder(ScreenPopupFolder, IMasterCopySource, IMasterCopyTarget): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ User folder containing screen popups """
    def Delete(self): # ->
        """
        Delete(self: ScreenPopupUserFolder)

            Deletes this instance.
        """
        ...


class ScreenPopupUserFolderComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of ScreenPopupUserFolders """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ScreenPopupUserFolderComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> ScreenPopupUserFolder:
        """
        Find(self: ScreenPopupUserFolderComposition, name: str) -> ScreenPopupUserFolder

            Finds a given screen popup user folder

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Screen.ScreenPopupUserFolder
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenPopupUserFolderComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenPopupUserFolderComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ScreenPopupUserFolder](enumerable: IEnumerable[ScreenPopupUserFolder], value: ScreenPopupUserFolder) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenSlidein(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Slide-In screen """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ScreenSlidein) -> IEngineeringObject
        """
        ...

    @property
    def SlideinType(self) -> SlideinType:
        """
        Type of a Slide-In screen.

        Get: SlideinType(self: ScreenSlidein) -> SlideinType
        """
        ...


    def Export(self, path:FileInfo, exportOptions:ExportOptions): # ->
        """
        Export(self: ScreenSlidein, path: FileInfo, exportOptions: ExportOptions)

            Common export

            path: Path to the Simatic ML file

            exportOptions: Determines whether the default values are exported or not
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenSlidein) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenSlidein) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenSlideinComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of slidein screens. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ScreenSlideinComposition) -> IEngineeringObject
        """
        ...


    def Find(self, slideinType:SlideinType) -> ScreenSlidein:
        """
        Find(self: ScreenSlideinComposition, slideinType: SlideinType) -> ScreenSlidein

            Find a slidein screen.

            slideinType: Slidein to find

            Returns: Siemens.Engineering.Hmi.Screen.ScreenSlidein
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenSlideinComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path:FileInfo, importOptions:ImportOptions) -> IList:
        """
        Import(self: ScreenSlideinComposition, path: FileInfo, importOptions: ImportOptions) -> IList[ScreenSlidein]

            Import Action

            path: Path to the Simatic ML file

            importOptions: Options to use for the Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Screen.ScreenSlidein>
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenSlideinComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ScreenSlidein](enumerable: IEnumerable[ScreenSlidein], value: ScreenSlidein) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenSlideinSystemFolder(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Folder for slide-in screens """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ScreenSlideinSystemFolder) -> IEngineeringObject
        """
        ...

    @property
    def ScreenSlideins(self) -> ScreenSlideinComposition:
        """
        Returns a collection of slide-in screens in that folder.

        Get: ScreenSlideins(self: ScreenSlideinSystemFolder) -> ScreenSlideinComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenSlideinSystemFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenSlideinSystemFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenSystemFolder(ScreenFolder, ILibraryTypeInstantiationTarget, IMasterCopyTarget): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ System folder containing screens """
    pass

class ScreenTemplate(IEquatable, IEngineeringObject, IMasterCopySource, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents a screen template """
    @property
    def Name(self) -> str:
        """
        The name of the screen template

        Get: Name(self: ScreenTemplate) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ScreenTemplate) -> IEngineeringObject
        """
        ...


    def Delete(self): # ->
        """
        Delete(self: ScreenTemplate)

            Deletes this instance.
        """
        ...

    def Export(self, path:FileInfo, exportOptions:ExportOptions): # ->
        """
        Export(self: ScreenTemplate, path: FileInfo, exportOptions: ExportOptions)

            Simatic ML export of a screen template

            path: Path to the Simatic ML file

            exportOptions: Option to use for export (default, readonly, etc.)
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenTemplate) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenTemplate) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenTemplateComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of ScreenTemplates """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ScreenTemplateComposition) -> IEngineeringObject
        """
        ...


    def CreateFrom(self, sourceMasterCopy:MasterCopy) -> ScreenTemplate:
        """
        CreateFrom(self: ScreenTemplateComposition, sourceMasterCopy: MasterCopy) -> ScreenTemplate

            Create ScreenTemplate from MasterCopy

            sourceMasterCopy: The source master copy

            Returns: Siemens.Engineering.Hmi.Screen.ScreenTemplate
        """
        ...

    def Find(self, name:str) -> ScreenTemplate:
        """
        Find(self: ScreenTemplateComposition, name: str) -> ScreenTemplate

            Finds a given screen template

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Screen.ScreenTemplate
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenTemplateComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Import(self, path:FileInfo, importOptions:ImportOptions) -> IList:
        """
        Import(self: ScreenTemplateComposition, path: FileInfo, importOptions: ImportOptions) -> IList[ScreenTemplate]

            Simatic ML import of a screen template

            path: Path to the Simatic ML file

            importOptions: Options to use for Import

            Returns: System.Collections.Generic.IList<Siemens.Engineering.Hmi.Screen.ScreenTemplate>
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenTemplateComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ScreenTemplate](enumerable: IEnumerable[ScreenTemplate], value: ScreenTemplate) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenTemplateFolder(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Folder containing screen templates """
    @property
    def Folders(self) -> ScreenTemplateUserFolderComposition:
        """
        Composition of screen template user folders

        Get: Folders(self: ScreenTemplateFolder) -> ScreenTemplateUserFolderComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the screen template folder

        Get: Name(self: ScreenTemplateFolder) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ScreenTemplateFolder) -> IEngineeringObject
        """
        ...

    @property
    def ScreenTemplates(self) -> ScreenTemplateComposition:
        """
        Composition of screen templates

        Get: ScreenTemplates(self: ScreenTemplateFolder) -> ScreenTemplateComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenTemplateFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenTemplateFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenTemplateSystemFolder(ScreenTemplateFolder, IMasterCopyTarget): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ System folder containing screen templates """
    pass

class ScreenTemplateUserFolder(ScreenTemplateFolder, IMasterCopySource, IMasterCopyTarget): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ User folder containing screen templates """
    def Delete(self): # ->
        """
        Delete(self: ScreenTemplateUserFolder)

            Deletes this instance.
        """
        ...


class ScreenTemplateUserFolderComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of ScreenTemplateUserFolders """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ScreenTemplateUserFolderComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> ScreenTemplateUserFolder:
        """
        Find(self: ScreenTemplateUserFolderComposition, name: str) -> ScreenTemplateUserFolder

            Finds a given screen template user folder

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Screen.ScreenTemplateUserFolder
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenTemplateUserFolderComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenTemplateUserFolderComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ScreenTemplateUserFolder](enumerable: IEnumerable[ScreenTemplateUserFolder], value: ScreenTemplateUserFolder) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ScreenUserFolder(ScreenFolder, ILibraryTypeInstantiationTarget, IMasterCopySource, IMasterCopyTarget): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ User folder containing screens """
    def Delete(self): # ->
        """
        Delete(self: ScreenUserFolder)

            Deletes this instance.
        """
        ...


class ScreenUserFolderComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of ScreenUserFolders """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ScreenUserFolderComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> ScreenUserFolder:
        """
        Find(self: ScreenUserFolderComposition, name: str) -> ScreenUserFolder

            Finds a given screen user folder

            name: Name to find

            Returns: Siemens.Engineering.Hmi.Screen.ScreenUserFolder
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ScreenUserFolderComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ScreenUserFolderComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ScreenUserFolder](enumerable: IEnumerable[ScreenUserFolder], value: ScreenUserFolder) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class SlideinType(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    Defines the available Slide-In screen types.

    enum SlideinType, values: Bottom (1), Left (2), Right (3), Top (0)
    """
    Bottom: SlideinType = ...
    Left: SlideinType = ...
    Right: SlideinType = ...
    Top: SlideinType = ...
    value__ = ...


class StyleLibraryType(LibraryType): # skipped bases: <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'ISivarcLibraryItem'>, <type 'ISivarcProgramBlockSource'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'object'>
    """ Represents a library type made from a style """
    pass

class StyleLibraryTypeVersion(LibraryTypeVersion): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ Represents a library type version made from a style """
    pass

class StyleSheetLibraryType(LibraryType): # skipped bases: <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'ISivarcLibraryItem'>, <type 'ISivarcProgramBlockSource'>, <type 'ILibraryTypeOrFolderSelection'>, <type 'object'>
    """ Represents a library type made from a style sheet """
    pass

class StyleSheetLibraryTypeVersion(LibraryTypeVersion): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ Represents a library type version made from a style sheet """
    pass

class VisibilityModes(Enum): # skipped bases: <type 'IFormattable'>, <type 'IConvertible'>, <type 'IComparable'>, <type 'object'>
    """
    Defindes the VisibilityModes

    enum VisibilityModes, values: FadeOut (0), ShowAlways (1), ShowNever (2)
    """
    FadeOut: VisibilityModes = ...
    ShowAlways: VisibilityModes = ...
    ShowNever: VisibilityModes = ...
    value__ = ...
