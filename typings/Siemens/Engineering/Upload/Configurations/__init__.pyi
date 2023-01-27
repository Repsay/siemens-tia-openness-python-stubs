# encoding: utf-8
# module Siemens.Engineering.Upload.Configurations calls itself Configurations
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
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

class UploadConfiguration(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Upload configuration base class. """
    @property
    def Message(self) -> str:
        """
        Descriptions of this onfiguration

        Get: Message(self: UploadConfiguration) -> str
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: UploadConfiguration) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UploadConfiguration) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UploadConfiguration) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UploadPasswordConfiguration(UploadConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Upload password configuration. """
    def SetPassword(self, password:SecureString): # ->
        """
        SetPassword(self: UploadPasswordConfiguration, password: SecureString)

            Sets password

            password: Required password.
        """
        ...


class ModuleReadAccessPassword(UploadPasswordConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Enter a password to gain read access to the module """
    pass

class ModuleWriteAccessPassword(UploadPasswordConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Enter a password to gain write access to the module """
    pass

class PasswordReadAccess(UploadPasswordConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ The PLC need a password for Readaccess. """
    pass

class UploadSelectionConfiguration(UploadConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEngineeringObject'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Upload configuration that provides choices. """
    pass

class UploadMissingProducts(UploadSelectionConfiguration): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalObjectAccess'>, <type 'IEquatable[object]'>, <type 'IEngineeringObject'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ The PLC contains additional data of missing products. """
    @property
    def CurrentSelection(self) -> UploadMissingProductsSelections:
        """
        Current selection for this configuration.

        Get: CurrentSelection(self: UploadMissingProducts) -> UploadMissingProductsSelections

        Set: CurrentSelection(self: UploadMissingProducts) = value
        """
        ...



class UploadMissingProductsSelections(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    Available selections for UploadMissingProductsCategory configuration

    enum UploadMissingProductsSelections, values: NoAction (0), TryUpload (1)
    """
    NoAction: UploadMissingProductsSelections = ...
    TryUpload: UploadMissingProductsSelections = ...
    value__ = ...
