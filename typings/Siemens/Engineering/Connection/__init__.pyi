# encoding: utf-8
# module Siemens.Engineering.Connection calls itself Connection
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import IEngineeringComposition, IEngineeringObject

from System import IEquatable

"""The following names are not found in the module: (BoundEvent,
    IInternalCompositionAccess, IInternalObjectAccess)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class IConfiguration: # skipped bases: <type 'object'>
    """ Connection cofiguration path to a device. """
    pass

class ConfigurationAddress(IEquatable, IEngineeringObject, IConfiguration, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ The connection configuration address """
    @property
    def Address(self) -> str:
        """
        The nodeaddress as string

        Get: Address(self: ConfigurationAddress) -> str
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the configuration address

        Get: Name(self: ConfigurationAddress) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ConfigurationAddress) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ConfigurationAddress) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ConfigurationAddress) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConfigurationAddressComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of ConfigurationAddresses """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ConfigurationAddressComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> ConfigurationAddress:
        """
        Find(self: ConfigurationAddressComposition, name: str) -> ConfigurationAddress

            Finds a given configuration address

            name: Name to find

            Returns: Siemens.Engineering.Connection.ConfigurationAddress
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ConfigurationAddressComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ConfigurationAddressComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ConfigurationAddress](enumerable: IEnumerable[ConfigurationAddress], value: ConfigurationAddress) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConfigurationGateway(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ The connection configuration gateway """
    @property
    def Addresses(self) -> ConfigurationAddressComposition:
        """
        Composition of configuration addresses

        Get: Addresses(self: ConfigurationGateway) -> ConfigurationAddressComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the configuration gateway

        Get: Name(self: ConfigurationGateway) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ConfigurationGateway) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ConfigurationGateway) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ConfigurationGateway) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConfigurationGatewayComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of ConfigurationGateways """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ConfigurationGatewayComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> ConfigurationGateway:
        """
        Find(self: ConfigurationGatewayComposition, name: str) -> ConfigurationGateway

            Finds a given configuration gateway

            name: Name to find

            Returns: Siemens.Engineering.Connection.ConfigurationGateway
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ConfigurationGatewayComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ConfigurationGatewayComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ConfigurationGateway](enumerable: IEnumerable[ConfigurationGateway], value: ConfigurationGateway) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConfigurationMode(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ The connection configuration mode """
    @property
    def Name(self) -> str:
        """
        The name of the configuration mode

        Get: Name(self: ConfigurationMode) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ConfigurationMode) -> IEngineeringObject
        """
        ...

    @property
    def PcInterfaces(self) -> ConfigurationPcInterfaceComposition:
        """
        Composition of Pc interfaces

        Get: PcInterfaces(self: ConfigurationMode) -> ConfigurationPcInterfaceComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ConfigurationMode) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ConfigurationMode) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConfigurationModeComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of ConfigurationModes """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ConfigurationModeComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> ConfigurationMode:
        """
        Find(self: ConfigurationModeComposition, name: str) -> ConfigurationMode

            Finds a given configuration mode

            name: Name to find

            Returns: Siemens.Engineering.Connection.ConfigurationMode
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ConfigurationModeComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ConfigurationModeComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ConfigurationMode](enumerable: IEnumerable[ConfigurationMode], value: ConfigurationMode) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConfigurationPcInterface(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ The connection configuration pc interface """
    @property
    def Addresses(self) -> ConfigurationAddressComposition:
        """
        Composition of configurationAddress

        Get: Addresses(self: ConfigurationPcInterface) -> ConfigurationAddressComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the configuration Pc interface

        Get: Name(self: ConfigurationPcInterface) -> str
        """
        ...

    @property
    def Number(self) -> int:
        """
        Number identifying PcInterface

        Get: Number(self: ConfigurationPcInterface) -> int
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ConfigurationPcInterface) -> IEngineeringObject
        """
        ...

    @property
    def Subnets(self) -> ConfigurationSubnetComposition:
        """
        Composition of configuration Subnets

        Get: Subnets(self: ConfigurationPcInterface) -> ConfigurationSubnetComposition
        """
        ...

    @property
    def TargetInterfaces(self) -> ConfigurationTargetInterfaceComposition:
        """
        Composition of configuration target interfaces

        Get: TargetInterfaces(self: ConfigurationPcInterface) -> ConfigurationTargetInterfaceComposition
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ConfigurationPcInterface) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ConfigurationPcInterface) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConfigurationPcInterfaceComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of ConfigurationPcInterfaces """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ConfigurationPcInterfaceComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str, number:int) -> ConfigurationPcInterface:
        """
        Find(self: ConfigurationPcInterfaceComposition, name: str, number: int) -> ConfigurationPcInterface

            Finds a given configuration pc interface

            name: Name to find

            number: Number to find

            Returns: Siemens.Engineering.Connection.ConfigurationPcInterface
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ConfigurationPcInterfaceComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ConfigurationPcInterfaceComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ConfigurationPcInterface](enumerable: IEnumerable[ConfigurationPcInterface], value: ConfigurationPcInterface) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConfigurationSubnet(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ The connection configuration subnet """
    @property
    def Addresses(self) -> ConfigurationAddressComposition:
        """
        Composition of configuration addresses

        Get: Addresses(self: ConfigurationSubnet) -> ConfigurationAddressComposition
        """
        ...

    @property
    def Gateways(self) -> ConfigurationGatewayComposition:
        """
        Get all gateways associated with this subnet

        Get: Gateways(self: ConfigurationSubnet) -> ConfigurationGatewayComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the configuration Subnet

        Get: Name(self: ConfigurationSubnet) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ConfigurationSubnet) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ConfigurationSubnet) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ConfigurationSubnet) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConfigurationSubnetComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of ConfigurationSubnets """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ConfigurationSubnetComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> ConfigurationSubnet:
        """
        Find(self: ConfigurationSubnetComposition, name: str) -> ConfigurationSubnet

            Finds a given configuration Subnet

            name: Name to find

            Returns: Siemens.Engineering.Connection.ConfigurationSubnet
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ConfigurationSubnetComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ConfigurationSubnetComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ConfigurationSubnet](enumerable: IEnumerable[ConfigurationSubnet], value: ConfigurationSubnet) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConfigurationTargetInterface(IEquatable, IEngineeringObject, IConfiguration, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ The connection configuration target interface """
    @property
    def Addresses(self) -> ConfigurationAddressComposition:
        """
        Composition of configurationAddress

        Get: Addresses(self: ConfigurationTargetInterface) -> ConfigurationAddressComposition
        """
        ...

    @property
    def Name(self) -> str:
        """
        The name of the configuration target interface

        Get: Name(self: ConfigurationTargetInterface) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ConfigurationTargetInterface) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ConfigurationTargetInterface) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ConfigurationTargetInterface) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConfigurationTargetInterfaceComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalBaseAccess'>, <type 'IInternalCollectionAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of ConfigurationTargetInterfaces """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: ConfigurationTargetInterfaceComposition) -> IEngineeringObject
        """
        ...


    def Find(self, name:str) -> ConfigurationTargetInterface:
        """
        Find(self: ConfigurationTargetInterfaceComposition, name: str) -> ConfigurationTargetInterface

            Finds a given configuration target interface

            name: Name to find

            Returns: Siemens.Engineering.Connection.ConfigurationTargetInterface
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ConfigurationTargetInterfaceComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ConfigurationTargetInterfaceComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ConfigurationTargetInterface](enumerable: IEnumerable[ConfigurationTargetInterface], value: ConfigurationTargetInterface) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class ConnectionConfiguration(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Provides the online connection """
    @property
    def EnableLegacyCommunication(self): # ->
        """
        Disable Tls (Transport Layer Security) protocol.

        Get: EnableLegacyCommunication(self: ConnectionConfiguration) -> bool

        Set: EnableLegacyCommunication(self: ConnectionConfiguration) = value
        """
        ...

    @property
    def IsConfigured(self) -> bool:
        """
        Indicates if the connection is configured

        Get: IsConfigured(self: ConnectionConfiguration) -> bool
        """
        ...

    @property
    def Modes(self) -> ConfigurationModeComposition:
        """
        Composition of configuration modes

        Get: Modes(self: ConnectionConfiguration) -> ConfigurationModeComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: ConnectionConfiguration) -> IEngineeringObject
        """
        ...


    def ApplyConfiguration(self, *__args:ConfigurationAddress) -> bool:
        """
        ApplyConfiguration(self: ConnectionConfiguration, address: ConfigurationAddress) -> bool

            If online is configured, then apply the configuration

            address: The address to apply the configuration

            Returns: System.Boolean

        ApplyConfiguration(self: ConnectionConfiguration, targetInterface: ConfigurationTargetInterface) -> bool

            If online is configured, then apply the configuration

            targetInterface: The target interface for which to apply the configuration

            Returns: System.Boolean
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ConnectionConfiguration) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ConnectionConfiguration) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...

    OnlineLegitimation = ...
