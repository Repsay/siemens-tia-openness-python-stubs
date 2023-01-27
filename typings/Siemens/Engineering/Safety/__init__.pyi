# encoding: utf-8
# module Siemens.Engineering.Safety calls itself Safety
# from Siemens.Engineering, Version=16.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=16.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import IEngineeringService

from System import IEquatable

"""The following names are not found in the module: IInternalObjectAccess
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class GlobalSettings(IEquatable, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ GlobalSettings """
    def GetHashCode(self) -> int:
        """
        GetHashCode(self: GlobalSettings) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def SafetyModificationsPossible(self, safetyModificationsPossible:bool): # ->
        """
        SafetyModificationsPossible(self: GlobalSettings, safetyModificationsPossible: bool)

            Specify wether changes to an F-Program are possible

            safetyModificationsPossible: If true the Safety access protection is active otherwise changes to an F-program are not allowed
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: GlobalSettings) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def UsernameForFChangeHistory(self, usernameForFChangeHistory:str): # ->
        """
        UsernameForFChangeHistory(self: GlobalSettings, usernameForFChangeHistory: str)

            Sets the username to be used for F-change history entries

            usernameForFChangeHistory: Username to be used for F-change history entries
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
