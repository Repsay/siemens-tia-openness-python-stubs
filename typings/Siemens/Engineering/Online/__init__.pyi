# encoding: utf-8
# module Siemens.Engineering.Online calls itself Online
# from Siemens.Engineering, Version=17.0.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84, Siemens.Engineering.AddIn, Version=17.0.0.0, Culture=neutral, PublicKeyToken=65b871d8372d6a8f
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import IEngineeringObject, IEngineeringService

from Siemens.Engineering.Connection import ConnectionConfiguration

from Siemens.Engineering.Online.Configurations import OnlineConfiguration

from System import (AsyncCallback, Enum, IAsyncResult, IEquatable,
    MulticastDelegate)

from System.Security import SecureString

"""The following names are not found in the module: (IInternalObjectAccess,
    field#)
"""

from Siemens import IInternalObjectAccess

# no functions
# classes

class OnlineConfigurationDelegate(MulticastDelegate): # skipped bases: <type 'ICloneable'>, <type 'ISerializable'>, <type 'object'>
    """
    Delegate for OnlineConfiguration callbacks

    OnlineConfigurationDelegate(object: object, method: IntPtr)
    """
    def BeginInvoke(self, onlineConfiguration:OnlineConfiguration, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: OnlineConfigurationDelegate, onlineConfiguration: OnlineConfiguration, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # ->
        """ EndInvoke(self: OnlineConfigurationDelegate, result: IAsyncResult) """
        ...

    def Invoke(self, onlineConfiguration:OnlineConfiguration): # ->
        """ Invoke(self: OnlineConfigurationDelegate, onlineConfiguration: OnlineConfiguration) """
        ...


class OnlineProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IEngineeringCompositionOrObject'>, <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'object'>
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

    def ResetPlcMasterSecret(self): # ->
        """
        ResetPlcMasterSecret(self: OnlineProvider)

            Delete the Plc Master Secret
        """
        ...

    def SetPlcMasterSecret(self, securePassword:SecureString): # ->
        """
        SetPlcMasterSecret(self: OnlineProvider, securePassword: SecureString)

            Performs the reset of the plc master secure password

            securePassword: The new master secret. If the password is NULL the master secret will be deleted.
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


class OnlineState(Enum): # skipped bases: <type 'IComparable'>, <type 'IFormattable'>, <type 'IConvertible'>, <type 'object'>
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


class RHOnlineProvider(IEquatable, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalBaseAccess'>, <type 'IInternalInstanceAccess'>, <type 'object'>
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


# variables with complex values
