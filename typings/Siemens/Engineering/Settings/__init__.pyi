# encoding: utf-8
# module Siemens.Engineering.Settings calls itself Settings
# from Siemens.Engineering, Version=16.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import IEngineeringComposition, IEngineeringObject

from System import IEquatable

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class TiaPortalSetting(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents a TiaPortal setting. """
    @property
    def Name(self) -> str:
        """
        Represents the name of a TiaPortalSetting.

        Get: Name(self: TiaPortalSetting) -> str

        Set: Name(self: TiaPortalSetting) = value
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: TiaPortalSetting) -> IEngineeringObject
        """
        ...

    @property
    def Value(self) -> object:
        """
        Represents the value of a TiaPortalSetting.

        Get: Value(self: TiaPortalSetting) -> object

        Set: Value(self: TiaPortalSetting) = value
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TiaPortalSetting) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TiaPortalSetting) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TiaPortalSettingComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Represents a composition of TiaPortalSettings. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: TiaPortalSettingComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> TiaPortalSetting:
        """
        Find(self: TiaPortalSettingComposition, name: str) -> TiaPortalSetting

            Returns the TiaPortalSetting with the matching name.

            name: The name of the TiaPortalSetting to find.

            Returns: Siemens.Engineering.Settings.TiaPortalSetting
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TiaPortalSettingComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TiaPortalSettingComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TiaPortalSetting](enumerable: IEnumerable[TiaPortalSetting], value: TiaPortalSetting) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TiaPortalSettingsFolder(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Represents a TiaPortal settings folder """
    @property
    def Folders(self) -> TiaPortalSettingsFolderComposition:
        """
        Composition of TiaPortalSettingsFolders

        Get: Folders(self: TiaPortalSettingsFolder) -> TiaPortalSettingsFolderComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        Represents the name of a TiaPortalSettingsFolder.

        Get: Name(self: TiaPortalSettingsFolder) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: TiaPortalSettingsFolder) -> IEngineeringObject
        """
        ...

    @property
    def Settings(self) -> TiaPortalSettingComposition:
        """
        Composition of TiaPortalSettings

        Get: Settings(self: TiaPortalSettingsFolder) -> TiaPortalSettingComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TiaPortalSettingsFolder) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TiaPortalSettingsFolder) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class TiaPortalSettingsFolderComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of TiaPortalSettingsFolders """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: TiaPortalSettingsFolderComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> TiaPortalSettingsFolder:
        """
        Find(self: TiaPortalSettingsFolderComposition, name: str) -> TiaPortalSettingsFolder

            Returns the TiaPortalSettingsFolder with the matching name.

            name: The name of the TiaPortalSettingsFolder to find.

            Returns: Siemens.Engineering.Settings.TiaPortalSettingsFolder
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: TiaPortalSettingsFolderComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: TiaPortalSettingsFolderComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TiaPortalSettingsFolder](enumerable: IEnumerable[TiaPortalSettingsFolder], value: TiaPortalSettingsFolder) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
