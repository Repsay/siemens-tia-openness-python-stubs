# encoding: utf-8
# module Siemens.Engineering.Upload calls itself Upload
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringComposition, IEngineeringObject,
    IEngineeringService)

from Siemens.Engineering.Connection import (ConfigurationAddress,
    ConnectionConfiguration)

from Siemens.Engineering.HW import Device

from Siemens.Engineering.Upload.Configurations import UploadConfiguration

from System import (AsyncCallback, DateTime, Enum, IAsyncResult, IEquatable,
    MulticastDelegate)

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class StationUploadProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Service provides station upload """
    @property
    def Configuration(self) -> ConnectionConfiguration:
        """
        Connection Configuration.

        Get: Configuration(self: StationUploadProvider) -> ConnectionConfiguration
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: StationUploadProvider) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: StationUploadProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def StationUpload(self, configurationAddress:ConfigurationAddress, uploadConfigurationDelegate:UploadConfigurationDelegate) -> UploadResult:
        """
        StationUpload(self: StationUploadProvider, configurationAddress: ConfigurationAddress, uploadConfigurationDelegate: UploadConfigurationDelegate) -> UploadResult

            Service provides station upload functionality

            configurationAddress: Configuration address for station upload

            uploadConfigurationDelegate: Upload parameter

            Returns: Siemens.Engineering.Upload.UploadResult
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: StationUploadProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UploadConfigurationDelegate(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ UploadConfigurationDelegate(object: object, method: IntPtr) """
    def BeginInvoke(self, uploadConfiguration:UploadConfiguration, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: UploadConfigurationDelegate, uploadConfiguration: UploadConfiguration, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # ->
        """ EndInvoke(self: UploadConfigurationDelegate, result: IAsyncResult) """
        ...

    def Invoke(self, uploadConfiguration:UploadConfiguration): # ->
        """ Invoke(self: UploadConfigurationDelegate, uploadConfiguration: UploadConfiguration) """
        ...


class UploadResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ The results of a Upload """
    @property
    def ErrorCount(self) -> int:
        """
        Number of errors in a given Upload scenario

        Get: ErrorCount(self: UploadResult) -> int
        """
        ...

    @property
    def Messages(self) -> UploadResultMessageComposition:
        """
        Collection of output messages for the result of a given Upload scenario.

        Get: Messages(self: UploadResult) -> UploadResultMessageComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: UploadResult) -> IEngineeringObject
        """
        ...

    @property
    def State(self) -> UploadResultState:
        """
        Final state of a given compile scenario

        Get: State(self: UploadResult) -> UploadResultState
        """
        ...

    @property
    def UploadedStation(self) -> Device:
        """
        The uploaded station if upload was successful.

        Get: UploadedStation(self: UploadResult) -> Device
        """
        ...

    @property
    def WarningCount(self) -> int:
        """
        Number of warnings in a given Upload scenario

        Get: WarningCount(self: UploadResult) -> int
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UploadResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UploadResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UploadResultMessage(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Upload result message """
    @property
    def DateTime(self) -> DateTime:
        """
        Date and time in a Upload message

        Get: DateTime(self: UploadResultMessage) -> DateTime
        """
        ...

    @property
    def ErrorCount(self) -> int:
        """
        Number of errors in a Upload message

        Get: ErrorCount(self: UploadResultMessage) -> int
        """
        ...

    @property
    def Message(self) -> str:
        """
        Description or content of a Upload message

        Get: Message(self: UploadResultMessage) -> str
        """
        ...

    @property
    def Messages(self) -> UploadResultMessageComposition:
        """
        Access to the Upload messages for a given Upload scenario

        Get: Messages(self: UploadResultMessage) -> UploadResultMessageComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: UploadResultMessage) -> IEngineeringObject
        """
        ...

    @property
    def State(self) -> UploadResultState:
        """
        Final state in a Upload message

        Get: State(self: UploadResultMessage) -> UploadResultState
        """
        ...

    @property
    def WarningCount(self) -> int:
        """
        Number of warnings in a Upload message

        Get: WarningCount(self: UploadResultMessage) -> int
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UploadResultMessage) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UploadResultMessage) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UploadResultMessageComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of Upload result messages. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: UploadResultMessageComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: UploadResultMessageComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: UploadResultMessageComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[UploadResultMessage](enumerable: IEnumerable[UploadResultMessage], value: UploadResultMessage) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class UploadResultState(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    The list of possible compiler result options

    enum UploadResultState, values: Error (3), Information (1), Success (0), Warning (2)
    """
    Error: UploadResultState = ...
    Information: UploadResultState = ...
    Success: UploadResultState = ...
    value__ = ...
    Warning: UploadResultState = ...


# variables with complex values
