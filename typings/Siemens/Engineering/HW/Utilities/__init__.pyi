# encoding: utf-8
# module Siemens.Engineering.HW.Utilities calls itself Utilities
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import IEngineeringComposition, IEngineeringObject

from Siemens.Engineering.HW import Device, DeviceItem

from System import Array, IEquatable

from System.IO import FileInfo

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class HardwareUtility(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Abstract base class for all extensions to the HW model """
    @property
    def Identifier(self) -> str:
        """
        Identifier for this HW extension

        Get: Identifier(self: HardwareUtility) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: HardwareUtility) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: HardwareUtility) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: HardwareUtility) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class CardReaderPscProvider(HardwareUtility): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Card reader provider utility for .psc file """
    def Export(self, device:Device, fileName:FileInfo): # ->
        """
        Export(self: CardReaderPscProvider, device: Device, fileName: FileInfo)

            Exports device configuration to file

            device: device to be exported

            fileName: file name that will be saved(*.psc)
        """
        ...


class HardwareUtilityComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of HardwareUtilities """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: HardwareUtilityComposition) -> IEngineeringObject
        """
        ...


    def Find(self, identifier:str) -> HardwareUtility:
        """
        Find(self: HardwareUtilityComposition, identifier: str) -> HardwareUtility

            Finds a given extension

            identifier: Identifier to find

            Returns: Siemens.Engineering.HW.Utilities.HardwareUtility
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: HardwareUtilityComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: HardwareUtilityComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[HardwareUtility](enumerable: IEnumerable[HardwareUtility], value: HardwareUtility) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ModuleInformationProvider(HardwareUtility): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Service provider for module information """
    def FindContainerTypes(self, typeIdentifier:str) -> Array:
        """
        FindContainerTypes(self: ModuleInformationProvider, typeIdentifier: str) -> Array[str]

            Finds the possible container types

            typeIdentifier: The type identifier to use to find a given container type

            Returns: System.String[]
        """
        ...

    def FindModuleTypes(self, partialTypeIdentifier:str) -> Array:
        """
        FindModuleTypes(self: ModuleInformationProvider, partialTypeIdentifier: str) -> Array[str]

            Finds the possible module types

            partialTypeIdentifier: The partial type identifier to be used to find a given module type

            Returns: System.String[]
        """
        ...

    def GetTypeIdentifierNormalized(self, typeIdentifier:str) -> str:
        """
        GetTypeIdentifierNormalized(self: ModuleInformationProvider, typeIdentifier: str) -> str

            Gets the TypeIdentifierNormalized

            typeIdentifier: The type identifier to be used to get TypeIdentifierNormalized

            Returns: System.String
        """
        ...


class OpcUaExportProvider(HardwareUtility): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Service provider for export of OPC UA """
    def Export(self, deviceItem:DeviceItem, path:FileInfo): # ->
        """
        Export(self: OpcUaExportProvider, deviceItem: DeviceItem, path: FileInfo)

            Simatic ML export of a OPC UA

            deviceItem: The device item to be exported

            path: Path to the export file
        """
        ...
