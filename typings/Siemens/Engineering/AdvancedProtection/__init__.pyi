# encoding: utf-8
# module Siemens.Engineering.AdvancedProtection calls itself AdvancedProtection
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import IEngineeringService

from System import IEquatable

from System.Collections import IEnumerable

from System.Security import SecureString

"""The following names are not found in the module: IInternalObjectAccess
"""

# no functions
# classes

class ProtectionProviderBase(IEquatable, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Defines the contract of a Protection Provider, should be used as the base class for client-specific ProtectionProviders """
    def GetHashCode(self) -> int:
        """
        GetHashCode(self: ProtectionProviderBase) -> int
            Returns a hash code for this instance.
            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def GetInvalidPasswordCharacters(self) -> IEnumerable:
        """
        GetInvalidPasswordCharacters(self: ProtectionProviderBase) -> IEnumerable[Char]
            Gets the invalid characters from the user password input
            Returns: System.Collections.Generic.IEnumerable<System.Char>
        """
        ...

    def Protect(self, newPassword:SecureString): # -> 
        """
        Protect(self: ProtectionProviderBase, newPassword: SecureString)
            Sets protection for the underlying object
            newPassword: the password to protect the object with
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: ProtectionProviderBase) -> str
            Returns a System.String that represents the current System.Object.
            Returns: A System.String that represents the current System.Object.
        """
        ...

    def Unprotect(self, currentPassword:SecureString): # -> 
        """
        Unprotect(self: ProtectionProviderBase, currentPassword: SecureString)
            Removes protection from the underlying object
            currentPassword: the password the underlying object is currently protected with
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


