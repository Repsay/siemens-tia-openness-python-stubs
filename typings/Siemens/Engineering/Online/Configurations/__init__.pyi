# encoding: utf-8
# module Siemens.Engineering.Online.Configurations calls itself Configurations
# from Siemens.Engineering, Version=16.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import IEngineeringObject

from System import IEquatable

from System.Security import SecureString

"""The following names are not found in the module: IInternalObjectAccess
"""

from Siemens import IInternalObjectAccess

# no functions
# classes

class OnlineConfiguration(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'object'>
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


class OnlinePasswordConfiguration(OnlineConfiguration): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ Online configuration base class for password configurations """
    def SetPassword(self, password:SecureString): # ->
        """
        SetPassword(self: OnlinePasswordConfiguration, password: SecureString)

            Set password for protected module

            password: Set password for legitimate the connection
        """
        ...


class OnlineReadAccessPassword(OnlinePasswordConfiguration): # skipped bases: <type 'IEngineeringObject'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IInternalObjectAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'IEquatable[object]'>, <type 'object'>
    """ Passwordconfiguration for read access """
    pass
