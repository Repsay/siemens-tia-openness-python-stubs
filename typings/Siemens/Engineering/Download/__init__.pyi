# encoding: utf-8
# module Siemens.Engineering.Download calls itself Download
# from Siemens.Engineering, Version=15.1.0.0, Culture=neutral, PublicKeyToken=d29ec89bac048f84
# by generator 1.145
""" no doc """
from __future__ import annotations
from Siemens.Engineering import (IEngineeringComposition, IEngineeringObject,
    IEngineeringService)

from Siemens.Engineering.Connection import (ConnectionConfiguration,
    IConfiguration)

from Siemens.Engineering.Download.Configurations import (
    DownloadConfiguration)

from System import (AsyncCallback, DateTime, Enum, IAsyncResult, IEquatable,
    MulticastDelegate)

"""The following names are not found in the module: (
    IInternalCompositionAccess, IInternalObjectAccess, field#)
"""

from Siemens import IInternalCompositionAccess, IInternalObjectAccess

# no functions
# classes

class DownloadConfigurationDelegate(MulticastDelegate): # skipped bases: <type 'ISerializable'>, <type 'ICloneable'>, <type 'object'>
    """ DownloadConfigurationDelegate(object: object, method: IntPtr) """
    def BeginInvoke(self, downloadConfiguration:DownloadConfiguration, callback:AsyncCallback, object:object) -> IAsyncResult:
        """ BeginInvoke(self: DownloadConfigurationDelegate, downloadConfiguration: DownloadConfiguration, callback: AsyncCallback, object: object) -> IAsyncResult """
        ...

    def EndInvoke(self, result:IAsyncResult): # ->
        """ EndInvoke(self: DownloadConfigurationDelegate, result: IAsyncResult) """
        ...

    def Invoke(self, downloadConfiguration:DownloadConfiguration): # ->
        """ Invoke(self: DownloadConfigurationDelegate, downloadConfiguration: DownloadConfiguration) """
        ...


class DownloadOptions(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    The list of possible download options

    enum (flags) DownloadOptions, values: Hardware (1), None (0), Software (2)
    """
    Hardware: DownloadOptions = ...
    Software: DownloadOptions = ...
    value__ = ...


class DownloadProvider(IEquatable, IEngineeringObject, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Service provides download functionality """
    @property
    def Configuration(self) -> ConnectionConfiguration:
        """
        Connection Configuration.

        Get: Configuration(self: DownloadProvider) -> ConnectionConfiguration
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: DownloadProvider) -> IEngineeringObject
        """
        ...


    def Download(self, configuration:IConfiguration, preDownloadConfigurationDelegate:DownloadConfigurationDelegate, postDownloadConfigurationDelegate:DownloadConfigurationDelegate, downloadOptions:DownloadOptions) -> DownloadResult:
        """
        Download(self: DownloadProvider, configuration: IConfiguration, preDownloadConfigurationDelegate: DownloadConfigurationDelegate, postDownloadConfigurationDelegate: DownloadConfigurationDelegate, downloadOptions: DownloadOptions) -> DownloadResult

            Downloads hardware and software to the device

            configuration: Connection cofiguration path to a device.

            preDownloadConfigurationDelegate: This delegate will be called for each configuration before the download.

            postDownloadConfigurationDelegate: This delegate will be called for each configuration after the download.

            downloadOptions: Download options

            Returns: Siemens.Engineering.Download.DownloadResult
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: DownloadProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: DownloadProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DownloadResult(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ The results of a download """
    @property
    def ErrorCount(self) -> int:
        """
        Number of errors in a given download scenario

        Get: ErrorCount(self: DownloadResult) -> int
        """
        ...

    @property
    def Messages(self) -> DownloadResultMessageComposition:
        """
        Collection of output messages for the result of a given download scenario.

        Get: Messages(self: DownloadResult) -> DownloadResultMessageComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: DownloadResult) -> IEngineeringObject
        """
        ...

    @property
    def State(self) -> DownloadResultState:
        """
        Final state of a given compile scenario

        Get: State(self: DownloadResult) -> DownloadResultState
        """
        ...

    @property
    def WarningCount(self) -> int:
        """
        Number of warnings in a given download scenario

        Get: WarningCount(self: DownloadResult) -> int
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: DownloadResult) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: DownloadResult) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DownloadResultMessage(IEquatable, IEngineeringObject, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Download result message """
    @property
    def DateTime(self) -> DateTime:
        """
        Date and time in a download message

        Get: DateTime(self: DownloadResultMessage) -> DateTime
        """
        ...

    @property
    def ErrorCount(self) -> int:
        """
        Number of errors in a download message

        Get: ErrorCount(self: DownloadResultMessage) -> int
        """
        ...

    @property
    def Message(self) -> str:
        """
        Description or content of a download message

        Get: Message(self: DownloadResultMessage) -> str
        """
        ...

    @property
    def Messages(self) -> DownloadResultMessageComposition:
        """
        Access to the download messages for a given download scenario

        Get: Messages(self: DownloadResultMessage) -> DownloadResultMessageComposition
        """
        ...

    @property
    def Parent(self) -> IEngineeringObject:
        """
        EOM parent of this object

        Get: Parent(self: DownloadResultMessage) -> IEngineeringObject
        """
        ...

    @property
    def State(self) -> DownloadResultState:
        """
        Final state in a download message

        Get: State(self: DownloadResultMessage) -> DownloadResultState
        """
        ...

    @property
    def WarningCount(self) -> int:
        """
        Number of warnings in a download message

        Get: WarningCount(self: DownloadResultMessage) -> int
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: DownloadResultMessage) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: DownloadResultMessage) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DownloadResultMessageComposition(IInternalCompositionAccess, IEngineeringComposition, IEquatable): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IEngineeringInstance'>, <type 'IEnumerable'>, <type 'IInternalCollectionAccess'>, <type 'IInternalBaseAccess'>, <type 'IEngineeringCompositionOrObject'>, <type 'object'>
    """ Composition of download result messages. """
    @property
    def Parent(self) -> IEngineeringObject:
        """
        Gets the parent.

        Get: Parent(self: DownloadResultMessageComposition) -> IEngineeringObject
        """
        ...


    def GetHashCode(self) -> int:
        """
        GetHashCode(self: DownloadResultMessageComposition) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: DownloadResultMessageComposition) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[DownloadResultMessage](enumerable: IEnumerable[DownloadResultMessage], value: DownloadResultMessage) -> bool """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


class DownloadResultState(Enum): # skipped bases: <type 'IConvertible'>, <type 'IComparable'>, <type 'IFormattable'>, <type 'object'>
    """
    The list of possible compiler result options

    enum DownloadResultState, values: Error (3), Information (1), Success (0), Warning (2)
    """
    Error: DownloadResultState = ...
    Information: DownloadResultState = ...
    Success: DownloadResultState = ...
    value__ = ...
    Warning: DownloadResultState = ...


class RHDownloadProvider(IEquatable, IEngineeringService, IInternalObjectAccess): # skipped bases: <type 'IInternalInstanceAccess'>, <type 'IInternalBaseAccess'>, <type 'object'>
    """ Service provides download functionality for R/H systems """
    @property
    def Configuration(self) -> ConnectionConfiguration:
        """
        Connection Configuration.

        Get: Configuration(self: RHDownloadProvider) -> ConnectionConfiguration
        """
        ...


    def DownloadToBackup(self, configuration:IConfiguration, preDownloadConfigurationDelegate:DownloadConfigurationDelegate, postDownloadConfigurationDelegate:DownloadConfigurationDelegate, downloadOptions:DownloadOptions) -> DownloadResult:
        """
        DownloadToBackup(self: RHDownloadProvider, configuration: IConfiguration, preDownloadConfigurationDelegate: DownloadConfigurationDelegate, postDownloadConfigurationDelegate: DownloadConfigurationDelegate, downloadOptions: DownloadOptions) -> DownloadResult

            Downloads hardware and software to the backup device

            configuration: Connection cofiguration path to a device.

            preDownloadConfigurationDelegate: This delegate will be called for each configuration before the download.

            postDownloadConfigurationDelegate: This delegate will be called for each configuration after the download.

            downloadOptions: Download options

            Returns: Siemens.Engineering.Download.DownloadResult
        """
        ...

    def DownloadToPrimary(self, configuration:IConfiguration, preDownloadConfigurationDelegate:DownloadConfigurationDelegate, postDownloadConfigurationDelegate:DownloadConfigurationDelegate, downloadOptions:DownloadOptions) -> DownloadResult:
        """
        DownloadToPrimary(self: RHDownloadProvider, configuration: IConfiguration, preDownloadConfigurationDelegate: DownloadConfigurationDelegate, postDownloadConfigurationDelegate: DownloadConfigurationDelegate, downloadOptions: DownloadOptions) -> DownloadResult

            Downloads hardware and software to the primary device

            configuration: Connection cofiguration path to a device.

            preDownloadConfigurationDelegate: This delegate will be called for each configuration before the download.

            postDownloadConfigurationDelegate: This delegate will be called for each configuration after the download.

            downloadOptions: Download options

            Returns: Siemens.Engineering.Download.DownloadResult
        """
        ...

    def GetHashCode(self) -> int:
        """
        GetHashCode(self: RHDownloadProvider) -> int

            Returns a hash code for this instance.

            Returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    def ToString(self) -> str:
        """
        ToString(self: RHDownloadProvider) -> str

            Returns a System.String that represents the current System.Object.

            Returns: A System.String that represents the current System.Object.
        """
        ...

    def __ne__(self, *args): #cannot find CLR method
        ...


# variables with complex values
