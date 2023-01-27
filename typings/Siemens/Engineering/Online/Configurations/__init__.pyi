# encoding: utf-8
# module Siemens.Engineering.Online.Configurations calls itself Configurations
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import IEngineeringObject

from System import Enum, IEquatable

from System.Security import SecureString

"""The following names are not found in the module: (IInternalObjectAccess,
    field#)
"""

from Siemens import IInternalObjectAccess

# no functions
# classes

class OnlineConfiguration(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Online configuration base class """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: OnlineConfiguration) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: OnlineConfiguration) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: OnlineConfiguration) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class OnlineConfigurationSelection(OnlineConfiguration): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Online configuration that provide choices. """
    pass

class OnlinePasswordConfiguration(OnlineConfiguration): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
    """ Online configuration base class for password configurations """
    def SetPassword(self, password:SecureString): # ->
        """
        SetPassword(self: OnlinePasswordConfiguration, password: SecureString)

            Set password for protected module

            password: Set password for legitimate the connection
        """
        ...


class OnlineReadAccessPassword(OnlinePasswordConfiguration): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Passwordconfiguration for read access """
    pass

class TlsVerificationConfiguration(OnlineConfigurationSelection): # skipped bases: <type 'IInternalObjectAccess'>, <type 'IEngineeringInstance'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Online configuration for TlsCommunication. """
    @property
    def CurrentSelection(self) -> TlsVerificationConfigurationSelection:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: TlsVerificationConfiguration) -> TlsVerificationConfigurationSelection

        Set: CurrentSelection(self: TlsVerificationConfiguration) = value
        """
        ...

    @property
    def PlcName(self) -> str:
        """
        Name of the Plc for this configuration

        Get: PlcName(self: TlsVerificationConfiguration) -> str
        """
        ...

    @property
    def VerificationInfo(self) -> str:
        """
        Message to verify if the connection can be trusted.

        Get: VerificationInfo(self: TlsVerificationConfiguration) -> str
        """
        ...



class TlsVerificationConfigurationSelection(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
    """
    Selection if the connection can be trustable or not.

    enum TlsVerificationConfigurationSelection, values: NonTrusted (2), NonVerified (0), Trusted (1)
    """
    NonTrusted: TlsVerificationConfigurationSelection = ...
    NonVerified: TlsVerificationConfigurationSelection = ...
    Trusted: TlsVerificationConfigurationSelection = ...
    value__ = ...
