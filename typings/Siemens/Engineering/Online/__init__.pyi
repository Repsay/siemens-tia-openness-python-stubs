# encoding: utf-8
# module Siemens.Engineering.Online calls itself Online
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import IEngineeringObject, IEngineeringService

from Siemens.Engineering.Connection import ConnectionConfiguration

from System import Enum, IEquatable

"""The following names are not found in the module: (IInternalObjectAccess,
    field#)
"""

from Siemens import IInternalObjectAccess

# no functions
# classes

class OnlineProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Service provider for online behaviors """
    @property
    def Configuration(self) -> ConnectionConfiguration:
        """
        Gets the connection configuration

        Get: Configuration(self: OnlineProvider) -> ConnectionConfiguration
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: OnlineProvider) -> IEngineeringObject
        """
        ...

    @property
    def State(self) -> OnlineState:
        """
        Check the Online state.

        Get: State(self: OnlineProvider) -> OnlineState
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: OnlineProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def GoOffline(self): # ->
        """
        GoOffline(self: OnlineProvider)

            Command to go offline
        """
        ...

    def GoOnline(self) -> OnlineState:
        """
        GoOnline(self: OnlineProvider) -> OnlineState

            Command to go online

            Returns: Siemens.Engineering.Online.OnlineState
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: OnlineProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class OnlineState(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    The list of possible online states

    enum OnlineState, values: Connecting (1), Disconnecting (6), Incompatible (3), NotReachable (4), Offline (0), Online (2), Protected (5)
    """
    Connecting: OnlineState = ...
    Disconnecting: OnlineState = ...
    Incompatible: OnlineState = ...
    NotReachable: OnlineState = ...
    Offline: OnlineState = ...
    Online: OnlineState = ...
    Protected: OnlineState = ...
    value__ = ...


class RHOnlineProvider(IEquatable, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Service provides online functionality for R/H systems """
    @property
    def BackupState(self) -> OnlineState:
        """
        Check the Online state of the Backup PLC.

        Get: BackupState(self: RHOnlineProvider) -> OnlineState
        """
        ...

    @property
    def Configuration(self) -> ConnectionConfiguration:
        """
        Gets the connection configuration

        Get: Configuration(self: RHOnlineProvider) -> ConnectionConfiguration
        """
        ...

    @property
    def PrimaryState(self) -> OnlineState:
        """
        Check the Online state of the Primary PLC.

        Get: PrimaryState(self: RHOnlineProvider) -> OnlineState
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: RHOnlineProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def GoOffline(self): # ->
        """
        GoOffline(self: RHOnlineProvider)

            Command to go offline
        """
        ...

    def GoOnlineToBackup(self) -> OnlineState:
        """
        GoOnlineToBackup(self: RHOnlineProvider) -> OnlineState

            Command to go online to the backup PLC

            Returns: Siemens.Engineering.Online.OnlineState
        """
        ...

    def GoOnlineToPrimary(self) -> OnlineState:
        """
        GoOnlineToPrimary(self: RHOnlineProvider) -> OnlineState

            Command to go online to the primary Primary

            Returns: Siemens.Engineering.Online.OnlineState
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: RHOnlineProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...
