# encoding: utf-8
# module Siemens.Engineering.HW.Features calls itself Features
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringAssociation, IEngineeringObject,
    IEngineeringService)

from Siemens.Engineering.HW import (AddressAssociation, Device, DeviceItem,
    ForceTableAccessRuleComposition, HardwareResource,
    HwIdentifierAssociation, ISyncDomainParticipant, InterfaceOperatingModes,
    IoConnectorComposition, IoControllerComposition,
    MasterSecretConfiguration, MrpDomainComposition, NetType, NodeComposition,
    OpcUaUserComposition, PcInterfaceAssignmentMode, PlcProtectionAccessLevel,
    Software, Subnet, SubnetComposition, SyncDomainComposition,
    TransferAreaComposition, WatchTableAccessRuleComposition,
    WebserverUserComposition)

from System import Array, Enum, IEquatable

from System.Collections import IEnumerable, IList

from System.IO import FileInfo

from System.Security import SecureString

"""The following names are not found in the module: (
    IInternalAssociationAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalAssociationAccess, IInternalObjectAccess

# no functions
# classes

class HardwareFeature(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
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


class DeviceItemFeature(HardwareFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Base class for all DeviceItem related services """
    @property
    def OwnedBy(self) -> DeviceItem:
        """
        DeviceItem Object that owns this role

        Get: OwnedBy(self: DeviceItemFeature) -> DeviceItem
        """
        ...



class AddressController(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Address controller device """
    @property
    def RegisteredAddresses(self) -> AddressAssociation:
        """
        Associated registered address

        Get: RegisteredAddresses(self: AddressController) -> AddressAssociation
        """
        ...



class AddressControllerAssociation(IEquatable, IEngineeringAssociation, IInternalAssociationAccess): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
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


class DeviceFeature(HardwareFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Base class for all Device related services """
    @property
    def OwnedBy(self) -> Device:
        """
        Device Object that owns this role

        Get: OwnedBy(self: DeviceFeature) -> Device
        """
        ...



class DisplayProtection(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents the Display Protection Service """
    def SetPassword(self, password:SecureString): # ->
        """
        SetPassword(self: DisplayProtection, password: SecureString)

            Sets password for display

            password: password for display
        """
        ...


class FrontPanelDisplay(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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



class GsdDevice(IEngineeringService, IGsdObject, DeviceFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Gsd device """
    pass

class GsdDeviceItem(IEngineeringService, IGsdObject, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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


class HwIdentifierController(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a HW identifier controller """
    @property
    def RegisteredHwIdentifiers(self) -> HwIdentifierAssociation:
        """
        Associated registered HW identifiers

        Get: RegisteredHwIdentifiers(self: HwIdentifierController) -> HwIdentifierAssociation
        """
        ...



class HwIdentifierControllerAssociation(IEquatable, IEngineeringAssociation, IInternalAssociationAccess): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
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


class ImConnection(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents the IM connection """
    def Connect(self, partnerPort:DeviceItem): # ->
        """
        Connect(self: ImConnection, partnerPort: DeviceItem)

            Connects to the partner port

            partnerPort: Specifies which partner port to which the connection needs to be established
        """
        ...

    def Disconnect(self): # ->
        """
        Disconnect(self: ImConnection)

            Disconnects from the partner port
        """
        ...

    def GetPartnerPort(self) -> DeviceItem:
        """
        GetPartnerPort(self: ImConnection) -> DeviceItem

            Gets the partner port details

            Returns: Siemens.Engineering.HW.DeviceItem
        """
        ...


class ModuleDescriptionUpdater(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents the ModuleDescriptionUpdater """
    @property
    def CanUpdate(self) -> bool:
        """
        Exists a new version of deviceitem to update

        Get: CanUpdate(self: ModuleDescriptionUpdater) -> bool
        """
        ...


    def UpdateModuleDescription(self) -> bool:
        """
        UpdateModuleDescription(self: ModuleDescriptionUpdater) -> bool

            Update module description of the deviceItem or deviceItems

            Returns: System.Boolean
        """
        ...


class SubnetFeature(HardwareFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Base class for Subnet related services """
    @property
    def OwnedBy(self) -> Subnet:
        """
        Subnet Object that owns this role

        Get: OwnedBy(self: SubnetFeature) -> Subnet
        """
        ...



class MrpDomainOwner(IEngineeringService, SubnetFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Mrp Domain owner """
    @property
    def MrpDomains(self) -> MrpDomainComposition:
        """
        Composition of Mrp Domain

        Get: MrpDomains(self: MrpDomainOwner) -> MrpDomainComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: MrpDomainOwner) -> IEngineeringObject
        """
        ...



class NetworkInterface(ISyncDomainParticipant, IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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



class NetworkInterfaceAssociation(IEquatable, IEngineeringAssociation, IInternalAssociationAccess): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Association of Network Interfaces """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent..

        Get: Parent(self: NetworkInterfaceAssociation) -> IEngineeringObject
        """
        ...


    def Add(self, item:NetworkInterface): # ->
        """
        Add(self: NetworkInterfaceAssociation, item: NetworkInterface)

            Adds an item.

            item: The item to be added.
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: NetworkInterfaceAssociation) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: NetworkInterfaceAssociation) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[NetworkInterface](enumerable: IEnumerable[NetworkInterface], value: NetworkInterface) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class NetworkPort(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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


class NetworkPortAssociation(IEquatable, IEngineeringAssociation, IInternalAssociationAccess): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
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


class OpcUaUserManagement(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a OpcUa User Management """
    @property
    def OpcUaUsers(self) -> OpcUaUserComposition:
        """
        Composition of OpcUaUsers

        Get: OpcUaUsers(self: OpcUaUserManagement) -> OpcUaUserComposition
        """
        ...



class PcInterfaceAssignment(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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


class PlcAccessLevelProvider(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
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


class PlcMasterSecretConfigurator(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents the Master Secret configuration for the PLC """
    @property
    def MasterSecretConfiguration(self) -> MasterSecretConfiguration:
        """
        Indicates the PLC protection type

        Get: MasterSecretConfiguration(self: PlcMasterSecretConfigurator) -> MasterSecretConfiguration
        """
        ...


    def ChangePassword(self, oldPassword:SecureString, newPassword:SecureString): # ->
        """
        ChangePassword(self: PlcMasterSecretConfigurator, oldPassword: SecureString, newPassword: SecureString)

            Change the Master Secret key for the protected PLC

            oldPassword: Specifies the old master secret key

            newPassword: Specifies the new master secret key
        """
        ...

    def Protect(self, password:SecureString): # ->
        """
        Protect(self: PlcMasterSecretConfigurator, password: SecureString)

            Protect the PLC with the Master Secret key(password)

            password: Specifies the Master Secret key
        """
        ...

    def Reset(self): # ->
        """
        Reset(self: PlcMasterSecretConfigurator)

            Removes PLC configuration data from the TIA Portal project and the PLC
        """
        ...

    def Unprotect(self, password:SecureString = ...): # ->
        """
        Unprotect(self: PlcMasterSecretConfigurator)

            Unprotects the PLC configuration data from the TIA Portal project and the PLC

        Unprotect(self: PlcMasterSecretConfigurator, password: SecureString)

            Unprotects the PLC configuration data from the TIA Portal project and the PLC

            password: Specifies the Master Secret password
        """
        ...


class SoftwareContainer(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a class containing software components """
    @property
    def Software(self) -> Software:
        """
        Gets the software target containing the software elements of the device

        Get: Software(self: SoftwareContainer) -> Software
        """
        ...



class SubnetOwner(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Subnet owner """
    @property
    def Subnets(self) -> SubnetComposition:
        """
        Composition of Subnets

        Get: Subnets(self: SubnetOwner) -> SubnetComposition
        """
        ...



class SyncDomainOwner(IEngineeringService, SubnetFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Sync Domain owner """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: SyncDomainOwner) -> IEngineeringObject
        """
        ...

    @property
    def SyncDomains(self) -> SyncDomainComposition:
        """
        Composition of Sync Domain

        Get: SyncDomains(self: SyncDomainOwner) -> SyncDomainComposition
        """
        ...



class WatchAndForceTableAccessManager(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents a Webserver watch And forceTables """
    @property
    def ForcetableAccessRules(self) -> ForceTableAccessRuleComposition:
        """
        Composition of ForcetableAccess

        Get: ForcetableAccessRules(self: WatchAndForceTableAccessManager) -> ForceTableAccessRuleComposition
        """
        ...

    @property
    def WatchtableAccessRules(self) -> WatchTableAccessRuleComposition:
        """
        Composition of Watch Table Access Rules

        Get: WatchtableAccessRules(self: WatchAndForceTableAccessManager) -> WatchTableAccessRuleComposition
        """
        ...



class WebDBGenerateOptions(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    The list of possible generate options for actions

    enum (flags) WebDBGenerateOptions, values: None (0), Override (1)
    """
    Override: WebDBGenerateOptions = ...
    value__ = ...


class WebserverUserDefinedPages(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represents the Web Server user defined pages service """
    def GenerateBlocks(self, *__args:WebDBGenerateOptions) -> IList:
        """
        GenerateBlocks(self: WebserverUserDefinedPages, generateOptions: WebDBGenerateOptions) -> IList[PlcBlock]

            Generate blocks

            generateOptions: Options to use for Generate

            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Blocks.PlcBlock>

        GenerateBlocks(self: WebserverUserDefinedPages, htmlDirectory: DirectoryInfo, defaultHTMLPage: FileInfo, applicationName: str, generateOptions: WebDBGenerateOptions) -> IList[PlcBlock]

            Generate blocks

            htmlDirectory: HTML directory of the webpage

            defaultHTMLPage: Default HTML page file

            applicationName: The application name

            generateOptions: Options to use for Generate

            Returns: System.Collections.Generic.IList<Siemens.Engineering.SW.Blocks.PlcBlock>
        """
        ...


class WebserverUserManagement(IEngineeringService, DeviceItemFeature): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Represent the webserver usermanagement """
    @property
    def WebserverUsers(self) -> WebserverUserComposition:
        """
        Composition of webserver users

        Get: WebserverUsers(self: WebserverUserManagement) -> WebserverUserComposition
        """
        ...
