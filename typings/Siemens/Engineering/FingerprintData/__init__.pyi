# encoding: utf-8
# module Siemens.Engineering.FingerprintData calls itself FingerprintData
# from Siemens.Engineering, Version=16.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringComposition, IEngineeringObject,
    IEngineeringService)

from Siemens.Engineering.Connection import (ConfigurationAddress,
    ConnectionConfiguration)

from Siemens.Engineering.Online import OnlineConfigurationDelegate

from System import IEquatable

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class FingerprintDataItem(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Baseclass for all FingerprintDataItems """
    @property
    def FingerprintDataIdentifier(self) -> str:
        """
        Type of item delivers the fingerprintdataitem

        Get: FingerprintDataIdentifier(self: FingerprintDataItem) -> str
        """
        ...

    @property
    def FingerprintDataValue(self) -> str:
        """
        The value of the fingerprintdataitem

        Get: FingerprintDataValue(self: FingerprintDataItem) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: FingerprintDataItem) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: FingerprintDataItem) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: FingerprintDataItem) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class FingerprintDataItemComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEnumerable'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Composition of FingerprintDateItems """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: FingerprintDataItemComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: FingerprintDataItemComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: FingerprintDataItemComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[FingerprintDataItem](enumerable: IEnumerable[FingerprintDataItem], value: FingerprintDataItem) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class FingerprintDataProvider(IEquatable, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Service provides fingerprintdata functionality """
    @property
    def Configuration(self) -> ConnectionConfiguration:
        """
        Connection Configuration.

        Get: Configuration(self: FingerprintDataProvider) -> ConnectionConfiguration
        """
        ...


    def GetFingerprintData(self, configurationAddress:ConfigurationAddress, onlineConfigurationDelegate:OnlineConfigurationDelegate) -> FingerprintDataResult:
        """
        GetFingerprintData(self: FingerprintDataProvider, configurationAddress: ConfigurationAddress, onlineConfigurationDelegate: OnlineConfigurationDelegate) -> FingerprintDataResult

            Contains a composition of fingerprintdataitems

            configurationAddress: Configuration address for fingerprintdata

            onlineConfigurationDelegate: Online configuration delegate

            Returns: Siemens.Engineering.FingerprintData.FingerprintDataResult
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: FingerprintDataProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: FingerprintDataProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class FingerprintDataResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Result of action GetFingerprintData """
    @property
    def FingerprintDataItems(self) -> FingerprintDataItemComposition:
        """
        Composition of fingerprintdataitems

        Get: FingerprintDataItems(self: FingerprintDataResult) -> FingerprintDataItemComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: FingerprintDataResult) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: FingerprintDataResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: FingerprintDataResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
