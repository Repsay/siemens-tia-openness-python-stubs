# encoding: utf-8
# module Siemens.Engineering.HW.Features calls itself Features
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringAssociation, IEngineeringObject, 
    IEngineeringService)

from Siemens.Engineering.HW import (AddressAssociation, Device, DeviceItem, 
    HardwareResource, HwIdentifierAssociation, InterfaceOperatingModes, 
    IoConnectorComposition, IoControllerComposition, NetType, NodeComposition, 
    PcInterfaceAssignmentMode, PlcProtectionAccessLevel, Software, 
    SubnetComposition, TransferAreaComposition)

from System import Array, IEquatable

from System.Collections import IEnumerable

from System.IO import FileInfo

from System.Security import SecureString

"""The following names are not found in the module: (
    IInternalAssociationAccess, IInternalObjectAccess)
"""

# no functions
# classes

class HardwareFeature(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Base class for all HW related services """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object
        Get: Parent(self: HardwareFeature) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: HardwareFeature) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: HardwareFeature) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DeviceItemFeature(HardwareFeature): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Base class for all DeviceItem related services """
    @property
    def OwnedBy(self) -> DeviceItem:
        """
        DeviceItem Object that owns this role
        Get: OwnedBy(self: DeviceItemFeature) -> DeviceItem
        """
        ...



class AddressController(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Address controller device """
    @property
    def RegisteredAddresses(self) -> AddressAssociation:
        """
        Associated registered address
        Get: RegisteredAddresses(self: AddressController) -> AddressAssociation
        """
        ...



class AddressControllerAssociation(IEquatable, IEngineeringAssociation, IInternalAssociationAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Associated address controllers """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent..
        Get: Parent(self: AddressControllerAssociation) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: AddressControllerAssociation) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: AddressControllerAssociation) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[AddressController](enumerable: IEnumerable[AddressController], value: AddressController) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DeviceFeature(HardwareFeature): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Base class for all Device related services """
    @property
    def OwnedBy(self) -> Device:
        """
        Device Object that owns this role
        Get: OwnedBy(self: DeviceFeature) -> Device
        """
        ...



class FrontPanelDisplay(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents the Front Panel Display """
    @property
    def AdaptLogoActivated(self) -> bool:
        """
        Adapt the logo to the display
        Get: AdaptLogoActivated(self: FrontPanelDisplay) -> bool
        Set: AdaptLogoActivated(self: FrontPanelDisplay) = value
        """
        ...

    @property
    def UserDefinedLogoActivated(self) -> bool:
        """
        Activate or deactivate the User Defined Logo
        Get: UserDefinedLogoActivated(self: FrontPanelDisplay) -> bool
        Set: UserDefinedLogoActivated(self: FrontPanelDisplay) = value
        """
        ...


    def SetUserDefinedLogo(self, logoImagePath:FileInfo): # -> 
        """
        SetUserDefinedLogo(self: FrontPanelDisplay, logoImagePath: FileInfo)
            Sets the Logo on the Display
            logoImagePath: Specifies the file info of the logo
        """
        ...


class IGsdObject: # skipped bases: <type 'object'>
    """ Properties of a Gsd hardware object """
    @property
    def GsdId(self) -> str:
        """
        The Gsd ID of the Gsd object
        Get: GsdId(self: IGsdObject) -> str
        """
        ...

    @property
    def GsdName(self) -> str:
        """
        The Gsd Name of the Gsd object
        Get: GsdName(self: IGsdObject) -> str
        """
        ...

    @property
    def GsdType(self) -> str:
        """
        The Gsd Type of the Gsd object
        Get: GsdType(self: IGsdObject) -> str
        """
        ...

    @property
    def IsProfibus(self) -> bool:
        """
        Indicates if this Gsd device item supports Profibus
        Get: IsProfibus(self: IGsdObject) -> bool
        """
        ...

    @property
    def IsProfinet(self) -> bool:
        """
        Indicates if this Gsd object supports Profinet
        Get: IsProfinet(self: IGsdObject) -> bool
        """
        ...



class GsdDevice(IEngineeringService, IGsdObject, DeviceFeature): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Gsd device """
    pass

class GsdDeviceItem(IEngineeringService, IGsdObject, DeviceItemFeature): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Gsd device item """
    def GetPrmData(self, dsNumber:int, byteOffset:int, length:int) -> Array:
        """
        GetPrmData(self: GsdDeviceItem, dsNumber: int, byteOffset: int, length: int) -> Array[Byte]
            Returns the Prm Data for this Gsd device item
            dsNumber: Specifies which dsNumber to set the Prm Data to this Gsd device item
            byteOffset: The byte offset
            length: Specifies which length to get the Prm Data from this Gsd device item
            Returns: System.Byte[]
        """
        ...

    def SetPrmData(self, dsNumber:int, byteOffset:int, prmData:IEnumerable): # -> 
        """ SetPrmData(self: GsdDeviceItem, dsNumber: int, byteOffset: int, prmData: IEnumerable[Byte]) """
        ...


class HwIdentifierController(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a HW identifier controller """
    @property
    def RegisteredHwIdentifiers(self) -> HwIdentifierAssociation:
        """
        Associated registered HW identifiers
        Get: RegisteredHwIdentifiers(self: HwIdentifierController) -> HwIdentifierAssociation
        """
        ...



class HwIdentifierControllerAssociation(IEquatable, IEngineeringAssociation, IInternalAssociationAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Associated Hw identifier controllers """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent..
        Get: Parent(self: HwIdentifierControllerAssociation) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: HwIdentifierControllerAssociation) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: HwIdentifierControllerAssociation) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[HwIdentifierController](enumerable: IEnumerable[HwIdentifierController], value: HwIdentifierController) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class NetworkInterface(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a HW interface """
    @property
    def InterfaceOperatingMode(self) -> InterfaceOperatingModes:
        """
        The operating mode of this interface
        Get: InterfaceOperatingMode(self: NetworkInterface) -> InterfaceOperatingModes
        Set: InterfaceOperatingMode(self: NetworkInterface) = value
        """
        ...

    @property
    def InterfaceType(self) -> NetType:
        """
        The type of this interface
        Get: InterfaceType(self: NetworkInterface) -> NetType
        Set: InterfaceType(self: NetworkInterface) = value
        """
        ...

    @property
    def IoConnectors(self) -> IoConnectorComposition:
        """
        Composition of IO connectors
        Get: IoConnectors(self: NetworkInterface) -> IoConnectorComposition
        """
        ...

    @property
    def IoControllers(self) -> IoControllerComposition:
        """
        Composition of IO controllers
        Get: IoControllers(self: NetworkInterface) -> IoControllerComposition
        """
        ...

    @property
    def Nodes(self) -> NodeComposition:
        """
        Composition of nodes
        Get: Nodes(self: NetworkInterface) -> NodeComposition
        """
        ...

    @property
    def Ports(self) -> NetworkPortAssociation:
        """
        Associated ports
        Get: Ports(self: NetworkInterface) -> NetworkPortAssociation
        """
        ...

    @property
    def TransferAreas(self) -> TransferAreaComposition:
        """
        Composition of transfer areas
        Get: TransferAreas(self: NetworkInterface) -> TransferAreaComposition
        """
        ...



class NetworkPort(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a port on a device item """
    @property
    def ConnectedPorts(self) -> NetworkPortAssociation:
        """
        Internal use only
        Get: ConnectedPorts(self: NetworkPort) -> NetworkPortAssociation
        """
        ...

    @property
    def Interface(self) -> NetworkInterface:
        """
        The interface supported by this port
        Get: Interface(self: NetworkPort) -> NetworkInterface
        """
        ...


    def ConnectToPort(self, partnerPort:NetworkPort): # -> 
        """
        ConnectToPort(self: NetworkPort, partnerPort: NetworkPort)
            Connects to the Port
            partnerPort: The partner port to be disconnected
        """
        ...

    def DisconnectFromPort(self, partnerPort:NetworkPort): # -> 
        """
        DisconnectFromPort(self: NetworkPort, partnerPort: NetworkPort)
            Disconnects a device from the given port
            partnerPort: The partner port to be disconnected
        """
        ...


class NetworkPortAssociation(IEquatable, IEngineeringAssociation, IInternalAssociationAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'object'>
    """ Associated ports """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent..
        Get: Parent(self: NetworkPortAssociation) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: NetworkPortAssociation) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: NetworkPortAssociation) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[NetworkPort](enumerable: IEnumerable[NetworkPort], value: NetworkPort) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class PcInterfaceAssignment(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Interface Assignment Provider """
    @property
    def HardwareResource(self) -> HardwareResource:
        """
        Get or set hardware resource of interface
        Get: HardwareResource(self: PcInterfaceAssignment) -> HardwareResource
        Set: HardwareResource(self: PcInterfaceAssignment) = value
        """
        ...

    @property
    def IpcExpansion(self) -> str:
        """
        Get or set hardware IPC Expansion of interface
        Get: IpcExpansion(self: PcInterfaceAssignment) -> str
        Set: IpcExpansion(self: PcInterfaceAssignment) = value
        """
        ...

    @property
    def PcInterfaceAssignmentMode(self) -> PcInterfaceAssignmentMode:
        """
        Returns type of interface assignment
        Get: PcInterfaceAssignmentMode(self: PcInterfaceAssignment) -> PcInterfaceAssignmentMode
        """
        ...

    @property
    def SoftwarePlc(self) -> DeviceItem:
        """
        Returns cpu DeviceItem
        Get: SoftwarePlc(self: PcInterfaceAssignment) -> DeviceItem
        """
        ...


    def AssignInterface(self, interfaceAssignmentFor:PcInterfaceAssignmentMode, softwareTarget:DeviceItem = ...): # -> 
        """
        AssignInterface(self: PcInterfaceAssignment, interfaceAssignmentFor: PcInterfaceAssignmentMode)
            Assign interface to one of the following( None, PC Station)
            interfaceAssignmentFor: assignment type for interface
        AssignInterface(self: PcInterfaceAssignment, interfaceAssignmentFor: PcInterfaceAssignmentMode, softwareTarget: DeviceItem)
            Assign interface to Software PLC
            interfaceAssignmentFor: assignment type for interface
            softwareTarget: if interface assignment will be to CPU, provide cpu device item
        """
        ...

    def GetAvailableIPCExpansions(self) -> IEnumerable:
        """
        GetAvailableIPCExpansions(self: PcInterfaceAssignment) -> IEnumerable[str]
            Get available IPC expansion list that can be selected
            Returns: System.Collections.Generic.IEnumerable<System.String>
        """
        ...


class PlcAccessLevelProvider(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents the Access level of the PLC Plus """
    @property
    def PlcProtectionAccessLevel(self) -> PlcProtectionAccessLevel:
        """
        To set the protection access level type
        Get: PlcProtectionAccessLevel(self: PlcAccessLevelProvider) -> PlcProtectionAccessLevel
        Set: PlcProtectionAccessLevel(self: PlcAccessLevelProvider) = value
        """
        ...


    def ResetPassword(self, accessLevelType:PlcProtectionAccessLevel): # -> 
        """
        ResetPassword(self: PlcAccessLevelProvider, accessLevelType: PlcProtectionAccessLevel)
            Reset the password for the specific Access Level Type
            accessLevelType: Specifies the Access level type
        """
        ...

    def SetPassword(self, accessLevelType:PlcProtectionAccessLevel, password:SecureString): # -> 
        """
        SetPassword(self: PlcAccessLevelProvider, accessLevelType: PlcProtectionAccessLevel, password: SecureString)
            set the password for the specific Access Level Type
            accessLevelType: Specifies the protection Access level type
            password: Specifies the password for the access level type
        """
        ...


class SoftwareContainer(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a class containing software components """
    @property
    def Software(self) -> Software:
        """
        Gets the software target containing the software elements of the device
        Get: Software(self: SoftwareContainer) -> Software
        """
        ...



class SubnetOwner(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Subnet owner """
    @property
    def Subnets(self) -> SubnetComposition:
        """
        Composition of Subnets
        Get: Subnets(self: SubnetOwner) -> SubnetComposition
        """
        ...



