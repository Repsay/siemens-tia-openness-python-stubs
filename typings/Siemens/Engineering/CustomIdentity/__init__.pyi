# encoding: utf-8
# module Siemens.Engineering.CustomIdentity calls itself CustomIdentity
# from Siemens.Engineering, Version=16.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (EngineeringTargetInvocationException,
    IEngineeringService)

from System import IEquatable

"""The following names are not found in the module: (BoundEvent,
    IInternalObjectAccess)
"""

from Siemens import IInternalObjectAccess

# no functions
# classes

class CustomIdentityNotFoundException(EngineeringTargetInvocationException): # skipped bases: <type 'ISerializable'>, <type '_Exception'>, <type 'object'>
    """
    Throws if CustomIdentity is not found for a given key.

    CustomIdentityNotFoundException()

    CustomIdentityNotFoundException(text: str)

    CustomIdentityNotFoundException(text: str, exception: Exception)

    CustomIdentityNotFoundException(text: str, *detailTexts: Array[str])
    """
    SerializeObjectState = ...


class CustomIdentityProvider(IEquatable, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ The class for setting and getting the user defined key-value """
    def Get(self, key:str) -> str:
        """
        Get(self: CustomIdentityProvider, key: str) -> str

            Get the value for the given key

            key: The user defined key

            Returns: System.String
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: CustomIdentityProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def Remove(self, key:str): # ->
        """
        Remove(self: CustomIdentityProvider, key: str)

            Remove CustomIdentity entry for the given key

            key: The key to which the custom identity entry to be deleted.
        """
        ...

    def Set(self, key:str, value:str): # ->
        """
        Set(self: CustomIdentityProvider, key: str, value: str)

            The user defined key and value to set

            key: User defined key

            value: User defined value
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: CustomIdentityProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
